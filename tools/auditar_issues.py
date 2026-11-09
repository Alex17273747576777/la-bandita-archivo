#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITORÍA DE ISSUES · escanea los issues y comentarios propios antes de tocar nada.

Saca, por cada issue: repositorio, número, estado, título, tamaño del cuerpo, cuántos
comentarios tiene, si algún mantenedor respondió, y cuáles de esos comentarios son míos.
Con eso se puede decidir qué conviene reescribir y qué no — en vez de editar 118 a ciegas.

Escribe docs/AUDITORIA-ISSUES-<fecha>.json y un resumen por pantalla.
"""
from __future__ import annotations

import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
HOY = "2026-11-09"


def token() -> str:
    return subprocess.run(["bash", "-c", "grep -m1 -o 'ghp_[A-Za-z0-9]*' ~/.gh-tokens"],
                          capture_output=True, text=True).stdout.strip()


T = token()


def api(path: str) -> dict | list:
    r = subprocess.run(["curl", "-s", "-m", "40", "-H", f"Authorization: bearer {T}",
                        "-H", "Accept: application/vnd.github+json",
                        f"https://api.github.com/{path}"], capture_output=True, text=True).stdout
    try:
        return json.loads(r)
    except Exception:  # noqa: BLE001
        return {}


def yo() -> str:
    return api("user").get("login", "")


def mis_issues(login: str) -> list[dict]:
    salida, pagina = [], 1
    while True:
        d = api(f"search/issues?q=author:{login}+type:issue&per_page=100&page={pagina}")
        items = d.get("items", []) if isinstance(d, dict) else []
        if not items:
            break
        salida += items
        if len(items) < 100:
            break
        pagina += 1
        time.sleep(1)
    return salida


def detalle(item: dict, login: str) -> dict:
    repo = "/".join(item["repository_url"].split("/repos/")[-1].split("/")[-2:])
    n = item["number"]
    comentarios = api(f"repos/{repo}/issues/{n}/comments?per_page=100")
    if not isinstance(comentarios, list):
        comentarios = []
    mios = [c for c in comentarios if c.get("user", {}).get("login") == login]
    ajenos = [c for c in comentarios if c.get("user", {}).get("login") != login]
    cuerpo = item.get("body") or ""
    return {
        "repo": repo,
        "numero": n,
        "estado": item["state"],
        "titulo": item["title"],
        "creado": (item.get("created_at") or "")[:10],
        "actualizado": (item.get("updated_at") or "")[:10],
        "car_cuerpo": len(cuerpo),
        "lineas_cuerpo": cuerpo.count("\n") + 1,
        "comentarios_total": len(comentarios),
        "comentarios_mios": [{"id": c["id"], "car": len(c.get("body") or ""),
                              "creado": (c.get("created_at") or "")[:10],
                              "url": c["html_url"]} for c in mios],
        "respondido_por_otros": len(ajenos),
        "quien_respondio": sorted({c["user"]["login"] for c in ajenos})[:5],
        "es_mi_repo": repo.split("/")[0].lower() == login.lower(),
        "url": item["html_url"],
        "emoji_en_titulo": any(ord(ch) > 0x2190 for ch in item["title"][:4]),
        "empieza_con_almohadilla": cuerpo.lstrip().startswith("#"),
    }


def main() -> int:
    login = yo()
    items = mis_issues(login)
    print(f"login: {login} · issues encontrados: {len(items)}")
    with ThreadPoolExecutor(max_workers=8) as ex:
        fichas = list(ex.map(lambda it: detalle(it, login), items))
    abiertos = [f for f in fichas if f["estado"] == "open"]
    cerrados = [f for f in fichas if f["estado"] == "closed"]
    mios = [f for f in fichas if f["es_mi_repo"]]
    con_respuesta = [f for f in abiertos if f["respondido_por_otros"] > 0]
    sin_respuesta = [f for f in abiertos if f["respondido_por_otros"] == 0]
    print(f"  abiertos {len(abiertos)} · cerrados {len(cerrados)}")
    print(f"  en mis repos {len(mios)} · en repos ajenos {len(fichas) - len(mios)}")
    print(f"  abiertos con respuesta de mantenedor {len(con_respuesta)} · sin respuesta {len(sin_respuesta)}")
    print(f"  comentarios míos en total: {sum(len(f['comentarios_mios']) for f in fichas)}")
    print(f"  cuerpo medio: {sum(f['car_cuerpo'] for f in fichas) // max(1, len(fichas))} car")
    grandes = [f for f in fichas if f["car_cuerpo"] > 15000]
    print(f"  con cuerpo de más de 15.000 car: {len(grandes)}")
    d = {"medido_en": HOY, "login": login, "total": len(fichas),
         "abiertos": len(abiertos), "cerrados": len(cerrados),
         "issues": fichas}
    (DOCS / f"AUDITORIA-ISSUES-{HOY}.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\n  → docs/AUDITORIA-ISSUES-{HOY}.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
