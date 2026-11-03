#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ESCRUTINIO · la nota que decide qué merece una ficha, dicha en voz alta.

El problema del olfato es que no se puede auditar. Este programa convierte el criterio en números con
peso declarado, para que una recomendación se pueda discutir y volver a correr el mes que viene.

Señales duras, cada una con su porqué:

  licencia    15  una licencia que se pueda leer y nombrar. Sin licencia no hay permiso para nada.
  CI          10  flujos de integración en el árbol: hay quien compila antes de publicar.
  adjuntos    10  al menos un adjunto con huella (.sha256/.asc/.sig) en las últimas entregas.
  entrega     10  una entrega en los últimos 30 días: el paquete se puede bajar hoy.
  commits     10  actividad en los últimos 30 días, escalada.
  equipo      10  personas distintas: el indicador más honesto de relevo.
  cola        10  proporción de incidencias cerradas sobre el total: alguien atiende.
  seguridad    5  SECURITY.md: hay un canal para reportar un fallo.
  mérito      20  Scorecard de OpenSSF vía deps.dev, cuando existe.

Penalizaciones, también declaradas:

  −30 archivado · −10 ninguna entrega con adjuntos · −15 atención anómala (menos de 14 días y más de
  5.000 estrellas sin equipo detrás) · −5 una sola persona con más de 50 entregas.

Uso:
  LBT=... python3 tools/escrutinio.py --top 0                 # todo lo medido hoy en FRESCO
  LBT=... python3 tools/escrutinio.py --repos a/b,c/d
  python3 tools/escrutinio.py --ver docs/ESCRUTINIO-2026-11-03.json
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
       "User-Agent": "la-bandita-escrutinio/1.0"}


def gql(q: str, intentos: int = 3) -> dict:
    for i in range(intentos):
        req = urllib.request.Request("https://api.github.com/graphql",
                                     data=json.dumps({"query": q}).encode(),
                                     headers={**CAB, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode()).get("data") or {}
        except Exception:
            if i == intentos - 1:
                return {}
            time.sleep(2 * (i + 1))
    return {}


def rest(ruta: str):
    try:
        with urllib.request.urlopen(urllib.request.Request("https://api.github.com" + ruta,
                                   headers=CAB), timeout=45) as r:
            return json.loads(r.read().decode()), r.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception:
        return None, 0


def scorecard(repo: str) -> tuple[float | None, str | None]:
    import urllib.parse
    url = "https://api.deps.dev/v3alpha/projects/" + urllib.parse.quote(f"github.com/{repo}", safe="")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": CAB["User-Agent"]}),
                                    timeout=30) as r:
            d = json.loads(r.read().decode())
        for s in d.get("scorecard") or []:
            if s.get("overallScore") is not None:
                return float(s["overallScore"]) * 10, (s.get("date") or "")[:10]
    except Exception:
        pass
    return None, None


CAMPOS = """a%d: repository(owner:"%s", name:"%s") {
  nameWithOwner stargazerCount forkCount isArchived createdAt pushedAt diskUsage
  licenseInfo{spdxId} hasIssuesEnabled
  issuesOpen: issues(states: OPEN){totalCount}
  issuesClosed: issues(states: CLOSED){totalCount}
  defaultBranchRef{target{... on Commit{oid history(since:"%s"){totalCount}}}}
  workflows: object(expression:"HEAD:.github/workflows"){ ... on Tree { entries { name } } }
  seguridad: object(expression:"HEAD:SECURITY.md"){ oid }
  contribuyendo: object(expression:"HEAD:CONTRIBUTING.md"){ oid }
}"""


def medir_bloque(repos: list[str], desde: str) -> dict[str, dict]:
    out = {}
    for i in range(0, len(repos), 20):
        grupo = repos[i:i + 20]
        partes = []
        for j, r in enumerate(grupo):
            ow, nom = r.split("/", 1)
            partes.append(CAMPOS % (j, ow, nom, desde))
        d = gql("query{ %s }" % "\n".join(partes))
        for j, r in enumerate(grupo):
            if d.get(f"a{j}"):
                out[r] = d[f"a{j}"]
        time.sleep(0.4)
    return out


def evaluar(repo: str, b: dict, contribuyentes: int | None, sc: float | None, hoy: date,
             entregas: list[dict] | None = None) -> dict:
    r, notas = 0, []
    lic = (b.get("licenseInfo") or {}).get("spdxId")
    if lic and lic != "NOASSERTION":
        r += 15; notas.append(f"licencia legible ({lic}) +15")
    else:
        notas.append("sin licencia reconocida +0")
    flujos = [e["name"] for e in ((b.get("workflows") or {}).get("entries") or [])]
    if flujos:
        r += 10; notas.append(f"integración continua con {len(flujos)} flujo(s) +10")
    else:
        notas.append("sin flujos de integración +0")
    adj = [a for rel in (entregas or []) for a in (rel.get("adjuntos") or [])]
    huella = [a for a in adj if any(x in (a.get("name") or "").lower()
                                    for x in (".sha256", ".sig", ".asc", "sha256sum", ".sha512"))]
    if huella:
        r += 10; notas.append(f"adjunto con huella ({huella[0]['name']}) +10")
    elif adj:
        notas.append("adjuntos sin huella +0")
    else:
        r -= 10; notas.append("ninguna entrega con adjuntos −10")
    # la entrega más reciente PUBLICADA: los borradores traen fecha nula y no cuentan
    fecha_ult = max((e.get("fecha") or "" for e in (entregas or [])), default="")
    if fecha_ult and (hoy - date.fromisoformat(fecha_ult)).days <= 30:
        r += 10; notas.append("entrega en los últimos 30 días +10")
    else:
        notas.append("sin entrega reciente +0")
    commits = (((b.get("defaultBranchRef") or {}).get("target") or {}).get("history") or {}).get("totalCount") or 0
    pc = 10 if commits >= 30 else (7 if commits >= 10 else (4 if commits >= 1 else 0))
    r += pc; notas.append(f"{commits} cambios en 30 días +{pc}")
    if contribuyentes is None:
        notas.append("equipo sin medir +0")
    else:
        pe = 10 if contribuyentes >= 10 else (7 if contribuyentes >= 5 else (4 if contribuyentes >= 2 else 0))
        r += pe; notas.append(f"{contribuyentes} personas empujando +{pe}")
    ab = (b.get("issuesOpen") or {}).get("totalCount") or 0
    ce = (b.get("issuesClosed") or {}).get("totalCount") or 0
    if ab + ce:
        ratio = ce / (ab + ce)
        pcol = round(10 * ratio)
        r += pcol; notas.append(f"incidencias cerradas {ce}/{ab + ce} +{pcol}")
    if b.get("seguridad"):
        r += 5; notas.append("SECURITY.md presente +5")
    if sc is not None:
        pm = round(20 * (sc / 100))
        r += pm; notas.append(f"Scorecard {sc / 10:.1f}/10 +{pm}")
    else:
        notas.append("sin Scorecard en deps.dev +0")
    edad = (hoy - date.fromisoformat((b.get("createdAt") or "")[:10])).days
    if b.get("isArchived"):
        r -= 30; notas.append("archivado −30")
    if edad < 14 and (b.get("stargazerCount") or 0) > 5000 and (contribuyentes or 0) < 10:
        r -= 15; notas.append("atención anómala: menos de 14 días, más de 5.000 estrellas y sin equipo −15")
    if (contribuyentes or 0) <= 1 and (((b.get("releases") or {}).get("totalCount")) or 0) > 50:
        r -= 5; notas.append("una sola persona con más de 50 entregas −5")
    return {"repo": repo, "puntos": max(0, min(100, r)), "licencia": lic,
            "flujos_ci": flujos[:5], "adjuntos": len(adj), "con_huella": len(huella),
            "ultima_entrega": fecha_ult, "commits_30d": commits, "contribuyentes": contribuyentes,
            "incidencias": {"abiertas": ab, "cerradas": ce},
            "security_md": bool(b.get("seguridad")), "scorecard": sc, "edad_dias": edad,
            "archivado": b.get("isArchived"), "notas": notas}


def main() -> int:
    a = sys.argv[1:]
    hoy = date.today()
    if "--ver" in a:
        d = json.loads(Path(a[a.index("--ver") + 1]).read_text(encoding="utf-8"))
        print(f"ESCRUTINIO · {d['fecha']} · {len(d['fichas'])} repositorios")
        for f in d["fichas"]:
            print(f"  {f['puntos']:>3} pts · {f['repo'][:44]:<44} {str(f['licencia'])[:12]:<12} "
                  f"CI {len(f['flujos_ci'])} · huella {f['con_huella']} · {f['commits_30d']:>3} commits · "
                  f"{str(f['contribuyentes']):>3} pers · scorecard {f['scorecard']}")
        return 0
    if "--repos" in a:
        repos = [x.strip() for x in a[a.index("--repos") + 1].split(",") if x.strip()]
    else:
        fuente = sorted(DOCS.glob(f"FRESCO-{hoy.isoformat()}-*.json"))
        if not fuente:
            print("no hay volcado de hoy: corre extraer_fresco primero")
            return 2
        pool: dict[str, dict] = {}
        for f in fuente:
            for x in json.loads(f.read_text(encoding="utf-8"))["fichas"]:
                pool[x["repo"]] = x
        repos = [x for x in pool if not pool[x].get("archivado")]
        top = int(a[a.index("--top") + 1]) if "--top" in a else 0
        if top:
            repos = sorted(repos, key=lambda k: -(pool[k].get("stars") or 0))[:top]
    print(f"escrutinio: {len(repos)} repositorios")
    bloques = medir_bloque(repos, (hoy - timedelta(days=30)).isoformat() + "T00:00:00Z")
    fichas = []
    for i, repo in enumerate(repos):
        b = bloques.get(repo)
        if not b:
            continue
        c, _ = rest(f"/repos/{repo}/contributors?per_page=100&anon=false")
        contrib = len(c) if isinstance(c, list) else None
        sc, _ = scorecard(repo)
        rel, _ = rest(f"/repos/{repo}/releases?per_page=10")
        entregas = []
        if isinstance(rel, list):
            for x in rel:
                if not isinstance(x, dict) or x.get("draft"):
                    continue
                entregas.append({"tag": x.get("tag_name"), "fecha": (x.get("published_at") or "")[:10],
                                 "adjuntos": [{"name": (ay or {}).get("name") or ""} for ay in (x.get("assets") or [])]})
        fichas.append(evaluar(repo, b, contrib, sc, hoy, entregas))
        if (i + 1) % 10 == 0:
            print(f"  … {i + 1}/{len(repos)}", flush=True)
        time.sleep(0.2)
    salida = DOCS / f"ESCRUTINIO-{hoy.isoformat()}.json"
    # el acta se acumula: correr el escrutinio sobre dos repositorios no puede borrar los otros 298
    if salida.exists():
        previo = json.loads(salida.read_text(encoding="utf-8")).get("fichas") or []
        por_repo = {x["repo"]: x for x in previo}
        por_repo.update({x["repo"]: x for x in fichas})
        fichas = list(por_repo.values())
    fichas.sort(key=lambda x: (-x["puntos"], -(x["commits_30d"] or 0), x["repo"]))
    salida.write_text(json.dumps({"fecha": hoy.isoformat(),
                                  "medido_en": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                                  "pesos": {"licencia": 15, "ci": 10, "huella": 10, "entrega": 10, "commits": 10,
                                            "equipo": 10, "cola": 10, "seguridad": 5, "merito": 20},
                                  "penalizaciones": {"archivado": -30, "sin_adjuntos": -10,
                                                     "atencion_anomala": -15, "una_sola_persona": -5},
                                  "medidos": len(fichas), "fichas": fichas},
                                 ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nESCRUTINIO · {len(fichas)} medidos · acta en {salida.name}")
    for f in fichas[:20]:
        print(f"  {f['puntos']:>3} pts · {f['repo'][:40]:<40} CI {len(f['flujos_ci'])} · "
              f"huella {f['con_huella']} · {f['commits_30d']:>3} commits · {str(f['contribuyentes']):>3} pers · "
              f"scorecard {f['scorecard']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
