#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EXTRACCIÓN FRESCA · lo que existe hoy, medido hoy, con el reloj puesto.

El problema que resuelve: una guía que se apoya en un censo de hace siete meses no informa, arquea.
Este programa hace dos cosas separadas, porque juntas tumban la API:

  1. BUSCAR (barato): la búsqueda devuelve solo nombre, estrellas, fechas y lenguaje.
  2. MEDIR (caro): cada repositorio elegido se pide por su nodo, en lotes de veinte alias, con
     licencia, copias, incidencias, tamaño, temas, lista de publicaciones y el commit de la cabeza.

Un 502 en la búsqueda no es un dato: se reintenta con espera y, si vuelve a fallar, se declara.

Uso:
  LBT=... python3 tools/extraer_fresco.py --nuevos 120 --dias 90
  LBT=... python3 tools/extraer_fresco.py --movers 120 --dias 7
  python3 tools/extraer_fresco.py --ver docs/FRESCO-2026-11-03-nuevos.json
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
TEMAS = ("android", "f-droid", "self-hosted", "privacy", "kotlin", "rust",
         "termux", "on-device-ai", "material-you", "adb")


def token() -> str:
    t = os.environ.get("LBT") or os.environ.get("PAT_FINO") or os.environ.get("GHP_A") or ""
    if not t:
        env = Path.home() / ".boveda" / "tokens.env"
        if env.exists():
            for linea in env.read_text().splitlines():
                if linea.startswith(("PAT_FINO=", "GHP_A=")):
                    t = linea.split("=", 1)[1].strip().strip('"')
                    break
    return t


TOK = token()
CAB = {"Authorization": f"Bearer {TOK}", "Content-Type": "application/json",
       "User-Agent": "la-bandita-fresco/1.0"}


def gql(query: str, intentos: int = 4) -> dict:
    for i in range(intentos):
        req = urllib.request.Request("https://api.github.com/graphql",
                                     data=json.dumps({"query": query}).encode(), headers=CAB)
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.loads(r.read().decode())
            if d.get("errors"):
                raise RuntimeError(str(d["errors"])[:200])
            return d["data"]
        except (urllib.error.HTTPError, RuntimeError, TimeoutError) as e:
            if i == intentos - 1:
                raise
            time.sleep(3 * (i + 1))
    raise RuntimeError("sin respuesta")


BUSCAR = """
query{ search(query:"%s", type:REPOSITORY, first:100%s) {
  repositoryCount pageInfo{hasNextPage endCursor}
  nodes{ ... on Repository { nameWithOwner stargazerCount pushedAt createdAt primaryLanguage{name} isArchived isFork } }
} }
"""

MEDIR = """
query{ %s }
"""

CAMPOS = """a%d: repository(owner:"%s", name:"%s") {
  nameWithOwner description stargazerCount forkCount isArchived isFork createdAt pushedAt diskUsage
  primaryLanguage{name} licenseInfo{spdxId}
  issues(states: OPEN){totalCount}
  releases(last:1, orderBy:{field: CREATED_AT, direction: DESC}){totalCount nodes{tagName publishedAt isPrerelease}}
  defaultBranchRef{target{... on Commit{oid committedDate}}}
  repositoryTopics(first:8){nodes{topic{name}}}
  watchers{totalCount}
}"""


def buscar(q: str, n: int = 120) -> list[dict]:
    out, cursor, paginas = [], None, 0
    while paginas < 6 and len(out) < n:
        after = f', after:"{cursor}"' if cursor else ""
        d = gql(BUSCAR % (q.replace('"', ""), after))["search"]
        out += [x for x in d["nodes"] if x]
        if not d["pageInfo"]["hasNextPage"]:
            break
        cursor = d["pageInfo"]["endCursor"]
        paginas += 1
        time.sleep(0.6)
    return out[:n]


def medir(repos: list[str], lote: int = 20) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for i in range(0, len(repos), lote):
        grupo = repos[i:i + lote]
        partes = []
        for j, r in enumerate(grupo):
            ow, nom = r.split("/", 1)
            partes.append(CAMPOS % (j, ow, nom))
        try:
            d = gql(MEDIR % "\n".join(partes))
        except Exception as e:
            print(f"  aviso: lote {i} falló ({str(e)[:60]}), se pide de uno en uno")
            d = {}
            for j, r in enumerate(grupo):
                ow, nom = r.split("/", 1)
                try:
                    d.update(gql(MEDIR % (CAMPOS % (j, ow, nom))))
                except Exception:
                    pass
                time.sleep(0.5)
        for j, r in enumerate(grupo):
            if d.get(f"a{j}"):
                out[r] = d[f"a{j}"]
        time.sleep(0.4)
    return out


def ficha(r: dict, hoy: date) -> dict:
    rel = (r.get("releases") or {}).get("nodes") or [{}]
    ult = rel[0] if rel else {}
    push = (r.get("pushedAt") or "")[:10]
    creado = (r.get("createdAt") or "")[:10]
    return {
        "repo": r["nameWithOwner"],
        "desc": (r.get("description") or "")[:220],
        "stars": r.get("stargazerCount"),
        "forks": r.get("forkCount"),
        "vigilantes": (r.get("watchers") or {}).get("totalCount"),
        "creado": creado,
        "edad_dias": (hoy - date.fromisoformat(creado)).days if creado else None,
        "push": push,
        "dias_sin_push": (hoy - date.fromisoformat(push)).days if push else None,
        "archivado": r.get("isArchived"),
        "es_copia": r.get("isFork"),
        "licencia": (r.get("licenseInfo") or {}).get("spdxId"),
        "lenguaje": (r.get("primaryLanguage") or {}).get("name"),
        "tamanyo_kb": r.get("diskUsage"),
        "incidencias": (r.get("issues") or {}).get("totalCount"),
        "publicaciones": (r.get("releases") or {}).get("totalCount"),
        "ultima": {"tag": ult.get("tagName"), "fecha": (ult.get("publishedAt") or "")[:10],
                   "pre": ult.get("isPrerelease")},
        "temas": [x["topic"]["name"] for x in ((r.get("repositoryTopics") or {}).get("nodes") or [])],
        "commit": ((r.get("defaultBranchRef") or {}).get("target") or {}).get("oid"),
    }


def main() -> int:
    args = sys.argv[1:]
    hoy = date.today()
    if "--ver" in args:
        d = json.loads(Path(args[args.index("--ver") + 1]).read_text(encoding="utf-8"))
        print(json.dumps({k: v for k, v in d.items() if k != "fichas"}, ensure_ascii=False, indent=1))
        for f in sorted(d["fichas"], key=lambda x: -(x.get("stars") or 0)):
            print(f"  ★{f['stars']:<6} {f['repo'][:40]:<40} edad {f['edad_dias']:>4} d · "
                  f"push {f['push']} · {str(f['licencia'])[:12]:<12} · pub {f['publicaciones']:>4} · "
                  f"{str(f['ultima']['tag'])[:18]}")
        return 0
    modo = "nuevos" if "--nuevos" in args else ("movers" if "--movers" in args else None)
    if not modo:
        print(__doc__)
        return 2
    n = int(args[args.index("--" + modo) + 1]) if len(args) > args.index("--" + modo) + 1 and \
        not args[args.index("--" + modo) + 1].startswith("--") else 120
    dias = int(args[args.index("--dias") + 1]) if "--dias" in args else (90 if modo == "nuevos" else 7)
    desde = (hoy - timedelta(days=dias)).isoformat()
    consultas = ([f"topic:{t} created:>={desde} stars:>=2" for t in TEMAS] if modo == "nuevos"
                 else [f"topic:{t} pushed:>={desde} stars:>=20" for t in TEMAS])
    vistos: dict[str, dict] = {}
    fallidas = []
    for q in consultas:
        try:
            for r in buscar(q, n):
                vistos.setdefault(r["nameWithOwner"], r)
        except Exception as e:
            fallidas.append({"consulta": q, "error": str(e)[:120]})
            print(f"  aviso: «{q}» falló: {str(e)[:70]}")
        time.sleep(0.5)
    print(f"búsqueda: {len(vistos)} repositorios · {len(fallidas)} consultas fallidas")
    orden = sorted(vistos, key=lambda k: -(vistos[k].get("stargazerCount") or 0))[:n]
    detalle = medir(orden)
    fichas = [ficha(v, hoy) for k, v in detalle.items()]
    fichas.sort(key=lambda x: (-(x["stars"] or 0), x["repo"]))
    salida = DOCS / f"FRESCO-{hoy.isoformat()}-{modo}.json"
    salida.write_text(json.dumps({
        "fecha": hoy.isoformat(),
        "medido_en": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "modo": modo, "ventana_dias": dias, "consultas": consultas, "consultas_fallidas": fallidas,
        "encontrados": len(vistos), "medidos": len(fichas),
        "vivos_30d": sum(1 for f in fichas if (f["dias_sin_push"] or 999) <= 30),
        "con_publicaciones": sum(1 for f in fichas if f["publicaciones"]),
        "fichas": fichas}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"FRESCO · {modo} · ventana {dias} d · {len(fichas)} medidos · "
          f"{sum(1 for f in fichas if (f['dias_sin_push'] or 999) <= 30)} con empujón en 30 d · "
          f"acta en {salida.name}")
    for f in fichas[:15]:
        print(f"  ★{f['stars']:<6} {f['repo'][:38]:<38} edad {f['edad_dias']:>3} d · {f['licencia']} · "
              f"pub {f['publicaciones']} · {f['lenguaje']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
