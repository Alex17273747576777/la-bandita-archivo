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

Qué guarda como prueba, y por qué: cada ficha medida deja su payload crudo en
`registry/_evidencia/<id>.json` con la fecha de la medición **dentro** del propio archivo
(`_medido_en`) y el SHA-256 de esos bytes en la ficha. Sin eso, una ficha puede declarar una
fecha que nada respalda —que es exactamente lo que pasó con 4.186 fichas del censo del 15-oct,
fechadas el 3-nov sin haber vuelto a mirar la API—.

Uso:
  LBT=<token> python3 tools/censo_medir.py --lote 50            # todas las fichas
  LBT=<token> python3 tools/censo_medir.py --lote 50 --limite 500   # prueba
  LBT=<token> python3 tools/censo_medir.py --vencidas          # solo las que hay que remedir
  LBT=<token> python3 tools/censo_medir.py --solo ids.txt      # una lista explícita
  python3 tools/censo_medir.py --estado                         # qué hay hecho
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
EVIDENCIA = REGISTRO / "_evidencia"
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


def guardar_evidencia(ficha: dict, v: dict, hoy: str) -> None:
    """Guarda la respuesta cruda con su fecha dentro y sella sus bytes en la ficha.

    La fecha del payload es la que manda: si el archivo dice `_medido_en: 2026-11-03`, la
    ficha puede declarar ese día sin pedir permiso a la memoria de nadie.
    """
    EVIDENCIA.mkdir(exist_ok=True)
    ruta = EVIDENCIA / f"{ficha['id']}.json"
    cuerpo = dict(v)
    cuerpo["_medido_en"] = hoy
    cuerpo["_fuente"] = "github-graphql"
    texto = json.dumps(cuerpo, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    ruta.write_text(texto, encoding="utf-8")
    ficha["evidencia"] = {
        "nota": "respuesta cruda de la API GraphQL; la fecha va dentro del propio archivo",
        "payload_ref": f"registry/_evidencia/{ficha['id']}.json",
        "sha256": hashlib.sha256(texto.encode("utf-8")).hexdigest(),
    }


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
    ficha["frescura"] = {"estado": "vencida", "dias": 0, "evidencia_en": hoy,
                         "proxima_remedicion": None, "ventana_dias": None,
                         "motivo": "el repositorio no existe: la API devolvió 404"}
    despues = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito")},
                         sort_keys=True, ensure_ascii=False)
    return antes != despues


def aplicar(ficha: dict, v: dict, hoy: str) -> bool:
    corte = date.fromisoformat(hoy)
    antes = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito", "procedencia",
                                                  "evidencia", "frescura")},
                       sort_keys=True, ensure_ascii=False)
    guardar_evidencia(ficha, v, hoy)
    ficha["medido_en"] = hoy
    ficha["frescura_dias"] = 0
    # Una ficha remedida deja de estar vencida: el bloque lo vuelve a escribir
    # `tools/vencimiento.py --aplicar`, que es el único que decide el estado.
    ficha.pop("frescura", None)
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
    despues = json.dumps({k: ficha.get(k) for k in ("medido_en", "actividad", "merito", "procedencia",
                                                   "evidencia", "frescura")},
                         sort_keys=True, ensure_ascii=False)
    return antes != despues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", type=int, default=50)
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--estado", action="store_true")
    ap.add_argument("--seco", action="store_true")
    ap.add_argument("--vencidas", action="store_true",
                    help="solo las fichas sin respaldo o vencidas, según tools/vencimiento.py")
    ap.add_argument("--solo", metavar="ARCHIVO", help="un archivo con ids, uno por línea")
    a = ap.parse_args()
    fs = fichas()
    if a.estado:
        hechas = sum(1 for p in fs if json.loads(p.read_text(encoding="utf-8")).get("medido_en") == fecha_casa_hoy())
        print(f"fichas: {len(fs)} · medidas hoy ({fecha_casa_hoy()}): {hechas}")
        return 0
    tok = os.environ.get("LBT") or ""
    if not tok:
        print("falta LBT")
        return 1
    # La fecha es la de la casa (Santo Domingo), no la del servidor: el entorno corre en UTC
    # y a las 20:30 del 3 de noviembre ya dice 4. Fechar con UTC puso un día de más una vez.
    hoy = fecha_casa_hoy()
    solo: set[str] | None = None
    if a.solo:
        solo = {l.strip() for l in Path(a.solo).read_text(encoding="utf-8").splitlines() if l.strip()}
        print(f"lista explícita: {len(solo)} ids")
    if a.vencidas:
        solo = set()
        for estado in ("sin_respaldo", "vencida"):
            salida = subprocess.run([sys.executable, str(Path(__file__).with_name("vencimiento.py")),
                                     "--lista", estado], capture_output=True, text=True)
            solo.update(l.strip() for l in salida.stdout.splitlines() if l.strip())
        print(f"a remedir por vencimiento: {len(solo)} fichas")
    pendientes = []
    for p in fs:
        d = json.loads(p.read_text(encoding="utf-8"))
        # ya medida hoy: no se vuelve a pedir (el 404 también es una medida del día)
        if solo is not None and d.get("id") not in solo:
            continue
        if solo is None and d.get("medido_en") == hoy:
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
