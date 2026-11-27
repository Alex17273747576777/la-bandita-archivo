#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RETIRADA DE ISSUES · cierra los propios que nadie va a leer, sin escribir en el hilo.

Lee `docs/RETIRADA-ISSUES-2026-11-27.json`, que es la decisión (no la inventa aquí: el
archivo manda). Por cada entrada de la lista blanca:

  * comprueba el estado real del issue antes de tocarlo;
  * si ya está cerrado, lo dice y no hace nada (idempotente);
  * si sigue abierto, lo cierra con `state_reason=not_planned` y **sin comentario**.

Por qué sin comentario: `kana-shii` pidió el 2026-11-12, en `komikku#892`, «Stop spamming shit
in old ass not planned issues». Un cierre quita el issue de la lista del mantenedor; un comentario,
además de no quitarlo, le manda una notificación. El registro de la decisión vive en
`docs/RETIRADA-ISSUES-2026-11-27.md`, que es nuestro, no suyo.

Token: hace falta uno con escritura en repositorios de terceros. El fine-grained de la cuenta
devuelve HTTP 403 en esos repos (medido el 2026-11-27 sobre komikku#1311). Se lee de la variable
`GH_TOKEN` o de la primera línea de `~/.gh-tokens`; nunca se imprime.

Uso:
    python3 tools/retirar_issues.py --simular   # dice qué haría, no escribe nada
    python3 tools/retirar_issues.py             # cierra los que toca
"""
from __future__ import annotations

import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parents[1]
PLAN = RAIZ / "docs" / "RETIRADA-ISSUES-2026-11-27.json"
API = "https://api.github.com"


def token() -> str:
    t = os.environ.get("GH_TOKEN", "").strip()
    if t:
        return t
    ruta = pathlib.Path.home() / ".gh-tokens"
    if ruta.is_file():
        return ruta.read_text(encoding="utf-8").splitlines()[0].strip()
    return ""


def pide(url: str, tok: str, metodo: str = "GET", datos: dict | None = None) -> tuple[int, dict]:
    cuerpo = json.dumps(datos).encode() if datos is not None else None
    cab = {
        "Authorization": "Bearer " + tok,
        "Accept": "application/vnd.github+json",
        "User-Agent": "retirada-issues",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if cuerpo:
        cab["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=cuerpo, headers=cab, method=metodo)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "{}")
        except Exception:
            return e.code, {}
    except urllib.error.URLError as e:
        return 0, {"message": str(e)}


def main() -> int:
    simular = "--simular" in sys.argv
    if not PLAN.is_file():
        print(f"falta {PLAN.relative_to(RAIZ)}: sin la decisión escrita no se toca nada")
        return 2
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    lista = plan.get("cerrar", [])
    if not lista:
        print("la lista de cierre está vacía")
        return 2

    tok = token()
    if not tok and not simular:
        print("no hay token: exporta GH_TOKEN o deja la primera línea de ~/.gh-tokens")
        return 2

    cerrados = ya = fallos = 0
    for it in lista:
        repo, n = it["repo"], it["numero"]
        url = f"{API}/repos/{repo}/issues/{n}"
        codigo, d = pide(url, tok or "sin-token")
        if codigo != 200:
            print(f"[FALLO] {repo}#{n}: no se pudo leer ({codigo} {d.get('message', '')})")
            fallos += 1
            continue
        if d.get("state") == "closed":
            print(f"[ya]    {repo}#{n}: ya estaba cerrado")
            ya += 1
            continue
        if simular:
            print(f"[haría] {repo}#{n}: cerrar sin comentario · {it['titulo'][:60]}")
            cerrados += 1
            continue
        codigo, d = pide(url, tok, "PATCH", {"state": "closed", "state_reason": "not_planned"})
        if codigo == 200 and d.get("state") == "closed":
            print(f"[ok]    {repo}#{n}: cerrado")
            cerrados += 1
        else:
            print(f"[FALLO] {repo}#{n}: {codigo} {d.get('message', '')}")
            fallos += 1
        time.sleep(0.4)  # no hace falta prisa; la API castiga las ráfagas

    verbo = "se cerrarían" if simular else "cerrados"
    print(f"\n{verbo}: {cerrados} · ya cerrados: {ya} · fallos: {fallos}")
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
