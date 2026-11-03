#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RE-MEDICIÓN DEL REGISTRO · deja de mirar el censo del 15-oct y lo vuelve a medir hoy.

Por qué existe: el registro tenía 6.832 fichas medidas el 15-oct-2026. La compuerta G2 avisa a los
180 días, pero una casa que presume de fechas no espera al aviso: vuelve a medir.

Cómo lo hace sin agotar el límite de la API: la API REST cobra una petición por repositorio y el
límite es de 5.000 por hora —no alcanza para 6.832—. La API **GraphQL** cobra por nodos, así que
se piden 50 repositorios por consulta: 6.832 fichas caen en ~137 consultas.

Qué escribe, por ficha: `medido_en` (hoy), `merito.stars`, `actividad.ultimo_push`,
`actividad.estado` (vivo/dormido con el umbral de la casa), `actividad.ultima_release` y
`actividad.release_en`, `licencia.spdx` cuando la API lo certifica, y `procedencia.commit` +
`procedencia.swhid` (el SWHID de una revisión git es `swh:1:rev:<sha1 del commit>`, que es
intrínseco: no hay que preguntárselo a nadie para calcularlo).

Uso:
  LBT=<token> python3 tools/censo_medir.py --lote 50            # todas las fichas
  LBT=<token> python3 tools/censo_medir.py --lote 50 --limite 500   # prueba
  python3 tools/censo_medir.py --estado                         # qué hay hecho
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
API = "https://api.github.com/graphql"
ESTADO = RAIZ / "docs" / "_remedicion.json"
UMBRAL_DORMIDO = 180

CONSULTA = """
query {
  rateLimit { remaining }
  %s
}
"""

FRAGMENTO = """
  a%s: repository(owner: "%s", name: "%s") {
    nameWithOwner
    stargazerCount
    forkCount
    isArchived
    pushedAt
    licenseInfo { spdxId name }
    diskUsage
    defaultBranchRef { target { ... on Commit { oid committedDate } } }
    releases(last: 1, orderBy: {field: CREATED_AT, direction: DESC}) { nodes { tagName publishedAt isPrerelease } }
    issues(states: OPEN) { totalCount }
  }
"""


def fichas() -> list[Path]:
    return sorted(p for p in REGISTRO.glob("*.json") if not p.name.startswith("_"))


def pedir(tok: str, repos: list[str]) -> dict:
    """Una consulta GraphQL con N alias. Devuelve {repo: datos}."""
    trozos = []
    for i, repo in enumerate(repos):
        if "/" not in repo:
            continue
        ow, nom = repo.split("/", 1)
        trozos.append(FRAGMENTO % (i, ow.replace('"', ""), nom.replace('"', "")))
    if not trozos:
        return {}
    cuerpo = json.dumps({"query": CONSULTA % "".join(trozos)}).encode()
    req = urllib.request.Request(API, data=cuerpo, headers={
        "Authorization": f"Bearer {tok}", "Content-Type": "application/json",
        "User-Agent": "la-bandita-censo"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            raise SystemExit(f"token rechazado o límite agotado: HTTP {e.code}")
        return {}
    except Exception:
        return {}
    datos = (d.get("data") or {})
    salida = {}
    for i, repo in enumerate(repos):
        v = datos.get(f"a{i}")
        if v:
            salida[repo] = v
    return salida


def estado_de(push: str, corte: date) -> str:
    if not push or not re.match(r"^\d{4}-\d{2}-\d{2}", push):
        return "indeterminado"
    dias = (corte - date.fromisoformat(push[:10])).days
    return "vivo" if dias <= UMBRAL_DORMIDO else "dormido"


def marcar_inexistente(ficha: dict, hoy: str) -> bool:
    """La API no conoce el repositorio: 404. Eso no es «sin dato», es un veredicto y se escribe:
    una ficha de un repositorio que no existe no puede seguir contando como viva."""
    antes = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito")},
                       sort_keys=True, ensure_ascii=False)
    ficha["medido_en"] = hoy
    ficha["frescura_dias"] = 0
    act = ficha.setdefault("actividad", {})
    act["estado"] = "muerto"
    act["semantica_http"] = 404
    mer = ficha.setdefault("merito", {})
    mer["stars"] = None
    despues = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito")},
                         sort_keys=True, ensure_ascii=False)
    return antes != despues


def aplicar(ficha: dict, v: dict, hoy: str) -> bool:
    corte = date.fromisoformat(hoy)
    antes = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito", "procedencia")},
                       sort_keys=True, ensure_ascii=False)
    ficha["medido_en"] = hoy
    ficha["frescura_dias"] = 0
    mer = ficha.setdefault("merito", {})
    mer["stars"] = v.get("stargazerCount")
    act = ficha.setdefault("actividad", {})
    push = v.get("pushedAt") or ""
    act["ultimo_push"] = push[:10] or None
    act["estado"] = estado_de(push, corte)
    act["semantica_http"] = 200
    rels = ((v.get("releases") or {}).get("nodes") or [])
    if rels:
        act["ultima_release"] = rels[0].get("tagName")
        act["release_en"] = (rels[0].get("publishedAt") or "")[:10] or None
    lic = ficha.setdefault("licencia", {})
    spdx = ((v.get("licenseInfo") or {}) or {}).get("spdxId")
    if spdx:
        lic.update(spdx=spdx, metodo="spdx-api", verificado_en=hoy)
    commit = ((v.get("defaultBranchRef") or {}).get("target") or {}).get("oid")
    proc = ficha.setdefault("procedencia", {})
    if commit:
        proc["commit"] = commit
        proc["swhid"] = f"swh:1:rev:{commit}"
        proc.setdefault("swh_estado", None)
    despues = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito", "procedencia")},
                         sort_keys=True, ensure_ascii=False)
    return antes != despues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", type=int, default=50)
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--estado", action="store_true")
    ap.add_argument("--seco", action="store_true")
    a = ap.parse_args()
    fs = fichas()
    if a.estado:
        hechas = sum(1 for p in fs if json.loads(p.read_text(encoding="utf-8")).get("medido_en") == date.today().isoformat())
        print(f"fichas: {len(fs)} · medidas hoy ({date.today().isoformat()}): {hechas}")
        return 0
    tok = os.environ.get("LBT") or ""
    if not tok:
        print("falta LBT")
        return 1
    hoy = date.today().isoformat()
    pendientes = []
    for p in fs:
        d = json.loads(p.read_text(encoding="utf-8"))
        # ya medida hoy: no se vuelve a pedir (el 404 también es una medida del día)
        if d.get("medido_en") == hoy:
            continue
        repo = d.get("repo") or d.get("id", "").replace("--", "/", 1)
        if repo:
            pendientes.append((p, repo))
    if a.limite:
        pendientes = pendientes[: a.limite]
    print(f"a re-medir: {len(pendientes)} fichas · lote {a.lote}")
    hechas, cambiadas, inexistentes, t0 = 0, 0, 0, time.time()
    for inicio in range(0, len(pendientes), a.lote):
        grupo = pendientes[inicio:inicio + a.lote]
        datos = pedir(tok, [r for _, r in grupo])
        for p, repo in grupo:
            v = datos.get(repo)
            d = json.loads(p.read_text(encoding="utf-8"))
            if v:
                cambio = aplicar(d, v, hoy)
            else:
                cambio = marcar_inexistente(d, hoy)
                inexistentes += 1
            if cambio and not a.seco:
                p.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                             encoding="utf-8")
                cambiadas += 1
            hechas += 1
        if hechas and hechas % 500 < a.lote:
            vel = hechas / max(1, time.time() - t0)
            print(f"  … {hechas}/{len(pendientes)} · {cambiadas} fichas actualizadas · "
                  f"{vel:.0f} fichas/s", flush=True)
        ESTADO.parent.mkdir(exist_ok=True)
        ESTADO.write_text(json.dumps({"fecha": hoy, "hechas": hechas, "total": len(pendientes),
                                      "cambiadas": cambiadas, "inexistentes": inexistentes},
                                     ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nre-medición: {hechas} fichas leídas · {cambiadas} actualizadas · "
          f"{inexistentes} con 404 (repositorio que no existe) · {len(pendientes) - hechas} sin respuesta")
    return 0


if __name__ == "__main__":
    sys.exit(main())
