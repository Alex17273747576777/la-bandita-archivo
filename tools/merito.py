#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MÉRITO MEDIDO · el Scorecard de OpenSSF sustituye a ★ como señal de mérito.

La casa dictó el 3-nov-2026 que lo popular no es mérito. ★ mide cuánta gente miró; el Scorecard
mide si el proyecto se mantiene, si revisa sus cambios, si firma sus publicaciones y si tiene
artefactos binarios opacos. Se pide a la API pública de deps.dev (espejo oficial del Scorecard de
OpenSSF, sin llave), se guarda la fecha de la medición y se escribe en la ficha:
`merito.scorecard` (0–10) y `merito.scorecard_en` (fecha).

Uso:
  python3 tools/merito.py --calendario            # los repositorios del registro de novedades
  python3 tools/merito.py --repos a/b,c/d
  python3 tools/merito.py --piezas                # los citados por las piezas con banda declarada
  python3 tools/merito.py … --seco
"""
from __future__ import annotations

import glob
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
API = "https://api.deps.dev/v3alpha/projects/"


def scorecard(repo: str) -> dict | None:
    url = API + urllib.parse.quote("github.com/" + repo, safe="")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={
                "Accept": "application/json", "User-Agent": "la-bandita-merito"}), timeout=30) as r:
            d = json.loads(r.read().decode())
    except Exception:
        return None
    sc = d.get("scorecard") or {}
    fecha = (sc.get("date") or "")[:10]
    if not fecha:
        return None
    peores = sorted([c for c in sc.get("checks", []) if isinstance(c.get("score"), int) and c["score"] < 0],
                    key=lambda c: c["name"])
    return {"repo": repo, "score": sc.get("overallScore"), "fecha": fecha,
            "estrellas": d.get("starsCount"), "no_evaluables": [c["name"] for c in peores]}


def fichas_por_repo() -> dict[str, Path]:
    indice = {}
    for f in glob.glob(str(RAIZ / "registry" / "*.json")):
        if Path(f).name.startswith("_"):
            continue
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:
            continue
        repo = d.get("repo") or d.get("id", "").replace("--", "/", 1)
        if repo:
            indice[repo.lower()] = Path(f)
    return indice


def repos_de_piezas() -> list[str]:
    bk = json.loads((RAIZ / "docs" / "bandas.json").read_text(encoding="utf-8"))
    nombres = set()
    for cfg in bk.values():
        if isinstance(cfg, dict):
            for ent in (cfg.get("piezas") or {}).values():
                if isinstance(ent, dict) and ent.get("archivo"):
                    nombres.add(ent["archivo"])
    fuera = []
    for p in (RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES").rglob("*.md"):
        if p.name in nombres:
            texto = p.read_text(encoding="utf-8", errors="replace")
            fuera += re.findall(r"\b([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)\b(?=[^\n]{0,40}?)", texto[:40000])
    # solo lo que parece owner/repo de GitHub y no rutas del árbol
    limpio = {x for x in fuera if not x.startswith(("Arena-Reimagined", "docs/", "registry/", "tools/"))
              and "/" in x and not x.endswith((".md", ".json", ".py", ".yml"))}
    return sorted(limpio)


def repos_calendario() -> list[str]:
    d = json.loads((RAIZ / "docs" / "CALENDARIO-DE-NOVEDADES.json").read_text(encoding="utf-8"))
    out = []
    for n in d.get("novedades", []):
        for r in n.get("repos", []):
            if r.get("repo"):
                out.append(r["repo"])
    return sorted(set(out))


def main() -> int:
    args = sys.argv[1:]
    seco = "--seco" in args
    if "--calendario" in args:
        repos = repos_calendario()
    elif "--piezas" in args:
        repos = repos_de_piezas()
    elif "--repos" in args:
        repos = [x.strip() for x in args[args.index("--repos") + 1].split(",") if x.strip()]
    else:
        print(__doc__)
        return 2
    indice = fichas_por_repo()
    hoy = date.today().isoformat()
    medidos, acta = 0, []
    for repo in repos:
        m = scorecard(repo)
        if not m:
            acta.append({"repo": repo, "scorecard": None, "motivo": "sin dato en deps.dev"})
            continue
        acta.append(m)
        f = indice.get(repo.lower())
        if f and not seco:
            d = json.loads(f.read_text(encoding="utf-8"))
            mer = d.setdefault("merito", {})
            mer["scorecard"] = m["score"]
            mer["scorecard_en"] = m["fecha"]
            f.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                         encoding="utf-8")
        medidos += 1
        print(f"  {repo:<42} ★{str(m['estrellas']):>7} · scorecard {m['score']}/10 (medido {m['fecha']})")
        time.sleep(0.2)
    print(f"\nscorecard medido: {medidos} de {len(repos)} repositorios · acta en docs/")
    if not seco:
        salida = RAIZ / "docs" / f"SCORECARD-{hoy}.json"
        previo = []
        if salida.exists():   # el acta del día se acumula: cada corrida añade, no pisa
            try:
                previo = json.loads(salida.read_text(encoding="utf-8")).get("detalle", [])
            except Exception:
                previo = []
        por_repo = {x["repo"]: x for x in previo}
        por_repo.update({x["repo"]: x for x in acta})
        detalle = sorted(por_repo.values(), key=lambda x: (x.get("score") is None,
                                                           -(x.get("score") or 0)))
        salida.write_text(json.dumps({"fecha": hoy, "medidos": sum(1 for x in detalle if x.get("score") is not None),
                                      "sin_dato": sum(1 for x in detalle if x.get("score") is None),
                                      "detalle": detalle}, ensure_ascii=False, indent=1) + "\n",
                          encoding="utf-8")
        print("acta:", salida.relative_to(RAIZ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
