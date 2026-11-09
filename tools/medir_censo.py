#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MEDIR EL CENSO · la API REST cobra una petición por repositorio; GraphQL cobra por nodos.

El censo de fmhy.net deja 3.125 repositorios que la casa nunca ha medido. Con REST
(una petición por repo) no alcanza el cupo de 5.000/hora para medirlos todos con
entregas. GraphQL permite pedir 60 repositorios por consulta con los campos que
hacen falta, así que este medidor usa GraphQL **y** REST solo para lo que GraphQL
no da: los adjuntos de la última entrega y cuáles llevan huella.

Uso:
  LBT=<token> python3 tools/medir_censo.py --lote 60 --limite 120   # prueba
  LBT=<token> python3 tools/medir_censo.py --todo                   # los 3.125
  python3 tools/medir_censo.py --estado

Qué escribe: `docs/CENSO-MEDIDO-<fecha>.json` con una ficha por repositorio, y
`docs/_censo/parcial-<n>.json` por lote, para no perder lo medido si se corta.

Qué NO hace: no inventa cifras. Si un repositorio no existe o la consulta falla,
queda como `sin_objeto` o `error` y se cuenta aparte.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
PARCIAL = DOCS / "_censo"
CENSO = DOCS / f"CENSO-FMHY-{date.today().isoformat()}.json"
SALIDA = DOCS / f"CENSO-MEDIDO-{date.today().isoformat()}.json"

CONSULTA = """
query($lote: [String!]!) {
  repos: search(query: %s, type: REPOSITORY, first: 1) { repositoryCount }
}
"""

Q = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner
    stargazerCount
    forkCount
    isArchived
    createdAt
    pushedAt
    diskUsage
    licenseInfo { spdxId }
    primaryLanguage { name }
    openIssues: issues(states: OPEN) { totalCount }
    releases(first: 1, orderBy: {field: CREATED_AT, direction: DESC}) {
      totalCount
      nodes {
        tagName
        publishedAt
        releaseAssets(first: 100) { totalCount }
      }
    }
  }
}
"""


def token() -> str:
    for v in (os.environ.get("LBT"), os.environ.get("GITHUB_TOKEN")):
        if v:
            return v.strip()
    for ruta in (Path.home() / ".gh-tokens", Path.home() / ".gh-token"):
        if ruta.exists():
            for linea in ruta.read_text(encoding="utf-8", errors="replace").split():
                if re.fullmatch(r"gh[pousr]_[A-Za-z0-9]{20,}", linea.strip()):
                    return linea.strip()
    raise SystemExit("falta el token: exportá LBT=<token>")


def gql(tok: str, consulta: str, variables: dict) -> tuple[int, dict]:
    cuerpo = json.dumps({"query": consulta, "variables": variables}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=cuerpo,
                                 headers={"Authorization": f"bearer {tok}",
                                          "Content-Type": "application/json",
                                          "User-Agent": "la-bandita-censo"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:200]}
    except Exception as e:
        return 0, {"error": str(e)[:200]}


def rest(tok: str, url: str) -> tuple[int, object]:
    req = urllib.request.Request(url, headers={"Authorization": f"bearer {tok}",
                                               "Accept": "application/vnd.github+json",
                                               "User-Agent": "la-bandita-censo"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return 0, None


PATRON_HUELLA = re.compile(r"(sha256|sha512|sha1|checksum|\.sig$|\.asc$|sums|SHA256SUMS)", re.I)


def medir(tok: str, full: str, con_adjuntos: bool = True) -> dict:
    dueno, _, nombre = full.partition("/")
    c, d = gql(tok, Q, {"owner": dueno, "name": nombre})
    ficha: dict = {"repo": full}
    if c != 200 or not isinstance(d, dict) or "data" not in d:
        ficha["estado"] = "error" if c != 200 else "sin_objeto"
        ficha["http"] = c
        return ficha
    r = (d.get("data") or {}).get("repository")
    if not r:
        ficha["estado"] = "sin_objeto"
        return ficha
    rels = r.get("releases") or {}
    nodos = rels.get("nodes") or []
    ult = nodos[0] if nodos else {}
    hoy = date.today()
    ficha.update({
        "estado": "vivo",
        "stars": r.get("stargazerCount"),
        "forks": r.get("forkCount"),
        "archivado": r.get("isArchived"),
        "nace": (r.get("createdAt") or "")[:10],
        "push": (r.get("pushedAt") or "")[:10],
        "licencia": (r.get("licenseInfo") or {}).get("spdxId"),
        "lenguaje": (r.get("primaryLanguage") or {}).get("name"),
        "tam_kib": r.get("diskUsage"),
        "abiertas": ((r.get("openIssues") or {}).get("totalCount")),
        "entregas": rels.get("totalCount"),
        "rel": ult.get("tagName"),
        "rel_fecha": (ult.get("publishedAt") or "")[:10],
        "adjuntos_ultima": ((ult.get("releaseAssets") or {}).get("totalCount")),
    })
    for campo, clave in (("nace", "dias_nace"), ("push", "dias_push"), ("rel_fecha", "rel_dias")):
        try:
            ficha[clave] = (hoy - date.fromisoformat(ficha[campo])).days
        except Exception:
            ficha[clave] = None
    if con_adjuntos and ficha.get("rel"):
        c2, d2 = rest(tok, f"https://api.github.com/repos/{full}/releases/latest")
        if c2 == 200 and isinstance(d2, dict):
            nombres = [a.get("name", "") for a in (d2.get("assets") or [])]
            huellas = [n for n in nombres if PATRON_HUELLA.search(n)]
            ficha["adjuntos_ultima"] = len(nombres)
            ficha["huellas_ultima"] = len(huellas)
            ficha["descargas_ultima"] = sum(a.get("download_count", 0) for a in (d2.get("assets") or []))
    ficha.setdefault("huellas_ultima", 0)
    ficha.setdefault("descargas_ultima", 0)
    return ficha


def pendientes() -> list[str]:
    nuevos = [x["full"] for x in json.loads(CENSO.read_text(encoding="utf-8"))["nuevos"]]
    hechos: set[str] = set()
    if PARCIAL.exists():
        for f in sorted(PARCIAL.glob("parcial-*.json")):
            for ficha in json.loads(f.read_text(encoding="utf-8")):
                hechos.add(ficha["repo"].lower())
    return [n for n in nuevos if n.lower() not in hechos]


def estado() -> None:
    total = len(json.loads(CENSO.read_text(encoding="utf-8"))["nuevos"])
    falta = pendientes()
    print(f"censo: {total} · medidos: {total - len(falta)} · pendientes: {len(falta)}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", type=int, default=60)
    ap.add_argument("--limite", type=int, default=0, help="cuántos medir en esta corrida")
    ap.add_argument("--todo", action="store_true")
    ap.add_argument("--estado", action="store_true")
    a = ap.parse_args()
    if a.estado:
        estado()
        return
    tok = token()
    falta = pendientes()
    objetivo = falta if a.todo else falta[: (a.limite or a.lote)]
    PARCIAL.mkdir(parents=True, exist_ok=True)
    n = len(list(PARCIAL.glob("parcial-*.json"))) + 1
    lote: list[dict] = []
    t0 = time.time()
    for i, full in enumerate(objetivo, 1):
        lote.append(medir(tok, full))
        if i % 10 == 0:
            print(f"  {i}/{len(objetivo)} · {time.time()-t0:.0f}s · último {full}")
        time.sleep(0.05)
    (PARCIAL / f"parcial-{n:04d}.json").write_text(json.dumps(lote, ensure_ascii=False), encoding="utf-8")
    print(f"lote {n} guardado · {len(lote)} fichas · quedan {len(falta)-len(lote)}")
    consolidar()


def consolidar() -> None:
    fichas: dict[str, dict] = {}
    if PARCIAL.exists():
        for f in sorted(PARCIAL.glob("parcial-*.json")):
            for x in json.loads(f.read_text(encoding="utf-8")):
                fichas[x["repo"].lower()] = x
    vivos = [x for x in fichas.values() if x.get("estado") == "vivo"]
    doc = {
        "medido_en": date.today().isoformat(),
        "medido_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fuente": "API GraphQL de GitHub (60 campos por consulta) + REST solo para adjuntos",
        "totales": {
            "medidos": len(fichas), "vivos": len(vivos),
            "archivados": sum(1 for x in vivos if x.get("archivado")),
            "sin_objeto": sum(1 for x in fichas.values() if x.get("estado") == "sin_objeto"),
            "errores": sum(1 for x in fichas.values() if x.get("estado") == "error"),
            "stars": sum(x.get("stars") or 0 for x in vivos),
            "con_huella_ultima": sum(1 for x in vivos if (x.get("huellas_ultima") or 0) > 0),
            "adjuntos_ultima": sum(x.get("adjuntos_ultima") or 0 for x in vivos),
            "push_7d": sum(1 for x in vivos if x.get("dias_push") is not None and x["dias_push"] <= 7),
            "push_30d": sum(1 for x in vivos if x.get("dias_push") is not None and x["dias_push"] <= 30),
            "nace_90d": sum(1 for x in vivos if x.get("dias_nace") is not None and x["dias_nace"] <= 90),
            "sin_licencia": sum(1 for x in vivos if (x.get("licencia") or "NOASSERTION") == "NOASSERTION"),
            "sin_entrega": sum(1 for x in vivos if not x.get("rel")),
        },
        "repos": sorted(fichas.values(), key=lambda x: -(x.get("stars") or 0)),
    }
    SALIDA.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    t = doc["totales"]
    print(f"→ {SALIDA.relative_to(RAIZ)} · medidos {t['medidos']} · vivos {t['vivos']} · "
          f"★{t['stars']:,} · con huella {t['con_huella_ultima']} · sin objeto {t['sin_objeto']}")


if __name__ == "__main__":
    main()
