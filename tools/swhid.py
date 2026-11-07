#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SWHID POR REVISIÓN MEDIDA · el código que se midió, citado de forma que no se pueda perder.

Un SWHID de revisión git (`swh:1:rev:<sha1>`) es intrínseco: se calcula, no se pregunta. Lo que sí
hay que preguntar es si Software Heritage tiene archivada esa revisión, porque un identificador que
nadie guardó no sirve para citar nada.

Esta herramienta: (1) toma el commit de la cabeza de cada repositorio —el que ya guardó la
re-medición del registro—, (2) calcula el SWHID, (3) le pregunta al archivo si lo tiene y (4), si no
lo tiene, **pide el archivado del origen** y deja el número de solicitud. Todo queda escrito en la
ficha y en un acta fechada.

Uso:
  python3 tools/swhid.py --piezas          # los repositorios citados por las piezas con banda
  python3 tools/swhid.py --repos a/b,c/d
  python3 tools/swhid.py --limite 20 --seco
"""
from __future__ import annotations

import glob
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SWH = "https://archive.softwareheritage.org/api/1"
UA = {"User-Agent": "la-bandita-swhid/1.0 (archivo de la casa)"}


def _get(url: str) -> tuple[int, dict]:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={**UA, "Accept": "application/json"}),
                                    timeout=45) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, {}
    except Exception:
        return 0, {}


def _post(url: str) -> tuple[int, dict]:
    try:
        req = urllib.request.Request(url, data=b"", headers=UA, method="POST")
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, {}
    except Exception:
        return 0, {}


def fichas() -> dict[str, Path]:
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
    texto = []
    for p in (RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES").rglob("*.md"):
        if p.name in nombres:
            texto.append(p.read_text(encoding="utf-8", errors="replace"))
    out = set()
    for t in texto:
        for m in re.finditer(r"https://github\.com/([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", t):
            out.add(m.group(1))
    return sorted(out)


def main() -> int:
    args = sys.argv[1:]
    if "--piezas" in args:
        repos = repos_de_piezas()
    elif "--repos" in args:
        repos = [x.strip() for x in args[args.index("--repos") + 1].split(",") if x.strip()]
    else:
        print(__doc__)
        return 2
    seco = "--seco" in args
    limite = int(args[args.index("--limite") + 1]) if "--limite" in args else 0
    if limite:
        repos = repos[:limite]
    indice = fichas()
    hoy = date.today().isoformat()
    acta, archivadas, pedidas, sin_commit = [], 0, 0, 0
    for repo in repos:
        f = indice.get(repo.lower())
        commit = None
        if f:
            commit = (json.loads(f.read_text(encoding="utf-8")).get("procedencia") or {}).get("commit")
        if not commit:
            sin_commit += 1
            acta.append({"repo": repo, "swhid": None, "estado": "sin commit medido"})
            continue
        swhid = f"swh:1:rev:{commit}"
        cod, j = _get(f"{SWH}/revision/{commit}/")
        if cod == 200:
            estado, archivadas = "archivada", archivadas + 1
            solicitud = j.get("id") or None
        else:
            cod2, j2 = _post(f"{SWH}/origin/save/git/url/" +
                             urllib.parse.quote(f"https://github.com/{repo}/", safe="") + "/")
            estado = f"solicitud {cod2}"
            solicitud = j2.get("save_request_status") or j2.get("id") or None
            pedidas += 1
            time.sleep(1.2)
        acta.append({"repo": repo, "swhid": swhid, "estado": estado, "solicitud": solicitud})
        if f and not seco:
            d = json.loads(f.read_text(encoding="utf-8"))
            proc = d.setdefault("procedencia", {})
            proc["swhid"] = swhid
            proc["swh_estado"] = estado
            proc["swh_solicitud"] = solicitud
            f.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        time.sleep(0.35)
    print(f"SWHID · {len(repos)} repositorios · archivadas {archivadas} · solicitadas {pedidas} · "
          f"sin commit {sin_commit}")
    for x in acta[:12]:
        print(f"  {x['repo'][:40]:<40} {x['estado']:<26} {str(x['swhid'])[:26]}")
    if not seco:
        salida = RAIZ / "docs" / f"SWHID-{hoy}.json"
        salida.write_text(json.dumps({"fecha": hoy, "repositorios": len(repos),
                                      "archivadas": archivadas, "solicitadas": pedidas,
                                      "detalle": acta}, ensure_ascii=False, indent=1) + "\n",
                          encoding="utf-8")
        print("acta:", salida.relative_to(RAIZ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
