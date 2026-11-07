#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FICHA PROFUNDA · lo que hay que abrir antes de recomendar algo.

Para cada repositorio elegido: presentación leída en crudo, licencia leída en el archivo, últimas
diez publicaciones con fecha y tamaño de adjuntos, descargas acumuladas, contribuyentes, empujones
en los últimos treinta días, incidencias y peticiones abiertas, y el identificador de revisión con su
estado en el archivo público.

Uso:
  LBT=... python3 tools/ficha_profunda.py owner/repo [owner/repo ...]
  LBT=... python3 tools/ficha_profunda.py --lista archivo.txt
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
CAB = {"Authorization": f"Bearer {TOK}", "Accept": "application/vnd.github+json",
       "User-Agent": "la-bandita-ficha/1.0"}


def rest(ruta: str):
    req = urllib.request.Request("https://api.github.com" + ruta, headers=CAB)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode()), r.status
    except urllib.error.HTTPError as e:
        return None, e.code


def gql(query: str) -> dict:
    req = urllib.request.Request("https://api.github.com/graphql",
                                 data=json.dumps({"query": query}).encode(),
                                 headers={**CAB, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode()).get("data") or {}
    except Exception:
        return {}


def texto_readme(repo: str) -> str:
    d, cod = rest(f"/repos/{repo}")
    if not d:
        return ""
    for cab in ("Accept: application/vnd.github.raw"):
        pass
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/readme",
                                 headers={**CAB, "Accept": "application/vnd.github.raw"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return ""


def licencia_texto(repo: str) -> str:
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/license",
                                 headers={**CAB, "Accept": "application/vnd.github.raw"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8", "replace")[:400]
    except Exception:
        return ""


def shas_desde(repo: str, desde: date) -> int:
    d, _ = rest(f"/repos/{repo}/commits?since={desde.isoformat()}T00:00:00Z&per_page=100")
    return len(d) if isinstance(d, list) else 0


def medir(repo: str) -> dict:
    hoy = date.today()
    base, _ = rest(f"/repos/{repo}")
    rel, _ = rest(f"/repos/{repo}/releases?per_page=10")
    contrib, _ = rest(f"/repos/{repo}/contributors?per_page=100&anon=false")
    prs, _ = rest(f"/repos/{repo}/pulls?state=open&per_page=100")
    if not base:
        return {"repo": repo, "error": "sin respuesta"}
    creado = (base.get("created_at") or "")[:10]
    push = (base.get("pushed_at") or "")[:10]
    publicaciones = rel if isinstance(rel, list) else []
    descargas = sum((a.get("download_count") or 0) for r in publicaciones for a in (r.get("assets") or []))
    adjuntos = sum(len(r.get("assets") or []) for r in publicaciones)
    g = gql('{repository(owner:"%s", name:"%s"){releases{totalCount} '
            'defaultBranchRef{target{... on Commit{oid committedDate}}} '
            'issues(states:OPEN){totalCount} forkCount stargazerCount '
            'vulnerabilityAlerts(first:1){totalCount}}}' % tuple(repo.split("/", 1)))
    r0 = (g.get("repository") or {})
    commit = ((r0.get("defaultBranchRef") or {}).get("target") or {}).get("oid")
    readme = texto_readme(repo)
    return {
        "repo": repo,
        "nombre": base.get("name"),
        "desc": base.get("description"),
        "autoria": (base.get("owner") or {}).get("login"),
        "tipo_autor": (base.get("owner") or {}).get("type"),
        "web": base.get("homepage"),
        "creado": creado,
        "edad_dias": (hoy - date.fromisoformat(creado)).days if creado else None,
        "push": push,
        "dias_sin_push": (hoy - date.fromisoformat(push)).days if push else None,
        "stars": base.get("stargazers_count"),
        "forks": base.get("forks_count"),
        "vigilantes": base.get("subscribers_count"),
        "incidencias": base.get("open_issues_count"),
        "peticiones_abiertas": len(prs) if isinstance(prs, list) else None,
        "contribuyentes": len(contrib) if isinstance(contrib, list) else None,
        "licencia": (base.get("license") or {}).get("spdx_id"),
        "licencia_texto": licencia_texto(repo)[:300],
        "lenguaje": base.get("language"),
        "tamanyo_kb": base.get("size"),
        "temas": base.get("topics") or [],
        "archivado": base.get("archived"),
        "es_copia": base.get("fork"),
        "publicaciones_totales": (r0.get("releases") or {}).get("totalCount") or base.get("releases_count"),
        "ultimas": [{"tag": r.get("tag_name"), "fecha": (r.get("published_at") or "")[:10],
                     "pre": r.get("prerelease"),
                     "adjuntos": [{"nombre": a.get("name"), "kb": round((a.get("size") or 0) / 1024, 1),
                                   "descargas": a.get("download_count")} for a in (r.get("assets") or [])]}
                    for r in publicaciones[:10]],
        "adjuntos_10": adjuntos,
        "descargas_10": descargas,
        "commits_30d": shas_desde(repo, hoy - timedelta(days=30)),
        "commits_90d": shas_desde(repo, hoy - timedelta(days=90)),
        "commit": commit,
        "readme_chars": len(readme),
        "readme_inicio": readme[:1800],
        "readme_idiomas": [i for i in ("español", "English", "中文", "日本語") if i.lower() in readme.lower()],
    }


def main() -> int:
    a = sys.argv[1:]
    if "--lista" in a:
        repos = [x.strip() for x in Path(a[a.index("--lista") + 1]).read_text().split() if x.strip()]
    else:
        repos = [x for x in a if "/" in x and not x.startswith("--")]
    if not repos:
        print(__doc__)
        return 2
    hoy = date.today()
    fichas = []
    for r in repos:
        f = medir(r)
        fichas.append(f)
        if "error" not in f:
            print(f"{r[:40]:<40} ★{f['stars']:<6} {str(f['licencia'])[:12]:<12} pub {f['publicaciones_totales']} · "
                  f"desc {f['descargas_10']:>6} · commits 30d {f['commits_30d']:>3} · "
                  f"contrib {f['contribuyentes']} · readme {f['readme_chars']}")
        else:
            print(f"{r[:40]:<40} ERROR")
        time.sleep(0.5)
    salida = DOCS / f"FICHA-PROFUNDA-{hoy.isoformat()}.json"
    previo = {}
    if salida.exists():
        previo = json.loads(salida.read_text(encoding="utf-8"))
    acumulado = {x["repo"]: x for x in (previo.get("fichas") or []) if "repo" in x}
    acumulado.update({x["repo"]: x for x in fichas if "error" not in x})
    salida.write_text(json.dumps({
        "fecha": hoy.isoformat(),
        "medido_en": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "fichas": sorted(acumulado.values(), key=lambda x: -(x.get("stars") or 0))},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nacta: {salida.name} · {len(acumulado)} fichas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
