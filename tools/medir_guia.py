#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MEDIR LA GUÍA MAESTRA · la pieza 05 no se escribe a mano, se mide.

La guía maestra guarda cada ficha en `guia-maestra/datos/apps/<id>.json` y su
cifra viva en `senal`. Ese bloque se puede quedar viejo sin que nadie lo note,
porque el texto se lee bien igual. Este programa lo vuelve a medir y dice, app
por app, qué cambió.

  señales que se re-miden: estrellas · nota (escrutinio, con sus pesos) · edad ·
  última entrega · descargas de las 10 últimas · contribuyentes · tamaño ·
  flujos de CI · incidencias abiertas.

Uso:
    LBT=... python3 tools/medir_guia.py                      # mide y muestra el diff
    LBT=... python3 tools/medir_guia.py --aplicar            # escribe senal + medido_en
    python3 tools/medir_guia.py --ver guia-maestra/datos/medicion-2026-11-04.json

`--aplicar` nunca borra: la señal anterior queda en
`guia-maestra/datos/_senal-anterior/<fecha>/<id>.json`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.request
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
APPS = RAIZ / "guia-maestra" / "datos" / "apps"
HIST = RAIZ / "guia-maestra" / "datos" / "_senal-anterior"
API = "https://api.github.com"


def token() -> str:
    t = os.environ.get("LBT") or os.environ.get("PAT_FINO")
    if not t:
        print("falta LBT: exportá el token de lectura")
        raise SystemExit(2)
    return t


def rest(ruta: str, tok: str):
    req = urllib.request.Request(API + ruta, headers={
        "Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json",
        "User-Agent": "la-bandita-medir-guia"})
    for intento in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception:
            time.sleep(2 * (intento + 1))
    return None


def escrutinio(repos: list[str], tok: str) -> dict[str, dict]:
    """La nota no se inventa: la calcula `tools/escrutinio.py` con sus pesos publicados."""
    if not repos:
        return {}
    antes = RAIZ / "docs" / f"ESCRUTINIO-{date.today().isoformat()}.json"
    previos = set()
    if antes.exists():
        previos = {x["repo"] for x in json.loads(antes.read_text(encoding="utf-8"))["fichas"]}
    env = dict(os.environ, LBT=tok)
    for i in range(0, len(repos), 20):
        lote = repos[i:i + 20]
        subprocess.run([sys.executable, str(RAIZ / "tools" / "escrutinio.py"),
                        "--repos", ",".join(lote)], cwd=RAIZ, env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not antes.exists():
        return {}
    todo = {x["repo"]: x for x in json.loads(antes.read_text(encoding="utf-8"))["fichas"]}
    return {r: todo[r] for r in repos if r in todo}


def medir(tok: str) -> dict[str, dict]:
    apps = []
    for f in sorted(APPS.glob("*.json")):
        apps.append(json.loads(f.read_text(encoding="utf-8")))
    repos = [a["repo"] for a in apps]
    notas = escrutinio(repos, tok)
    salida = {}
    for a in apps:
        r = a["repo"]
        d = rest(f"/repos/{r}", tok)
        if not d or d.get("message"):
            salida[a["id"]] = {"repo": r, "estado": "sin objeto"}
            continue
        rels = rest(f"/repos/{r}/releases?per_page=10", tok) or []
        descargas = sum(x.get("download_count", 0) for rel in rels if isinstance(rel, dict)
                        for x in (rel.get("assets") or []))
        e = notas.get(r, {})
        salida[a["id"]] = {
            "repo": r, "estado": "vivo",
            "senal": {
                "estrellas": d.get("stargazers_count"),
                "nota": e.get("puntos", (a.get("senal") or {}).get("nota")),
                "edad_dias": (date.today() - date.fromisoformat(d["created_at"][:10])).days,
                "ultima_entrega": e.get("ultima_entrega") or (a.get("senal") or {}).get("ultima_entrega"),
                "descargas_10": descargas,
                "contribuyentes": e.get("contribuyentes"),
                "repo_mb": round((d.get("size") or 0) / 1024, 1),
                "ci": len(e.get("flujos_ci") or []),
                "incidencias": (f"{(e.get('incidencias') or {}).get('abiertas')} abiertas"
                                if e.get("incidencias") else (a.get("senal") or {}).get("incidencias")),
            },
            "licencia": (d.get("license") or {}).get("spdx_id"),
            "push": (d.get("pushed_at") or "")[:10],
        }
    return salida


def diff(viejo: dict, nuevo: dict) -> list[str]:
    out = []
    for k in ("estrellas", "nota", "edad_dias", "ultima_entrega", "descargas_10",
              "contribuyentes", "repo_mb", "ci", "incidencias"):
        a, b = viejo.get(k), nuevo.get(k)
        if a != b:
            out.append(f"{k}: {a} → {b}")
    return out


def aplicar(datos: dict, fecha: str) -> int:
    cambios = 0
    for f in sorted(APPS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        nuevo = datos.get(d["id"], {})
        if nuevo.get("estado") != "vivo":
            continue
        viejo = d.get("senal") or {}
        cambios_ = diff(viejo, nuevo["senal"])
        if not cambios_:
            continue
        dest = HIST / fecha
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f.name).write_text(json.dumps(
            {"id": d["id"], "senal": viejo, "medido_en": d.get("medido_en")},
            ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        d["senal"] = nuevo["senal"]
        d["medido_en"] = fecha
        if nuevo.get("licencia") and nuevo["licencia"] != "NOASSERTION":
            d.setdefault("licencia", {})["spdx"] = nuevo["licencia"]
        f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        cambios += 1
    return cambios


def main() -> int:
    a = sys.argv[1:]
    if "--ver" in a:
        d = json.loads(Path(a[a.index("--ver") + 1]).read_text(encoding="utf-8"))
        print(f"GUÍA MAESTRA · medición del {d['medido_en']} a las {d['medido_a_las']} · {len(d['apps'])} apps")
        for k, v in d["apps"].items():
            if v.get("senal"):
                s = v["senal"]
                print(f"  {k:<18} ★{s['estrellas']:>7} · nota {s['nota']:>3} · {s['edad_dias']:>5} d · "
                      f"{s['descargas_10']:>9} desc · {s['repo_mb']:>8} MB")
        return 0
    tok = token()
    datos = medir(tok)
    fecha = date.today().isoformat()
    destino = RAIZ / "guia-maestra" / "datos" / f"medicion-{fecha}.json"
    destino.write_text(json.dumps(
        {"medido_en": fecha, "medido_a_las": datetime.now().strftime("%H:%M"),
         "fuente": "API de GitHub con LBT + tools/escrutinio.py", "apps": datos},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    movidos = 0
    for f in sorted(APPS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        nuevo = datos.get(d["id"], {})
        if nuevo.get("estado") != "vivo":
            continue
        c = diff(d.get("senal") or {}, nuevo["senal"])
        if c:
            movidos += 1
            print(f"  {d['id']:<18} {c[0]}" + (f"  (+{len(c)-1} más)" if len(c) > 1 else ""))
    print(f"medición escrita: {destino} · {movidos} fichas con alguna cifra movida")
    if "--aplicar" in a:
        n = aplicar(datos, fecha)
        print(f"aplicado: {n} fichas reescritas · la señal anterior queda en {HIST.relative_to(RAIZ)}/{fecha}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
