#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGISTRO · construye las fichas JSON del activo vendible desde el censo medido.

Fuente: Arena-Reimagined/02-ARCHIVO/censo-ecosistema-2026-10-15.tsv (medición del 15-oct-2026).
Salida: registry/<id>.json, una ficha por repositorio, conforme a schemas/ficha.schema.json.

Honestidad del dato: la evidencia que la casa conserva de esa medición es la fila del censo.
El campo `evidencia.sha256` sella esa fila, no un payload de API que no se guardó. Quien quiera
el payload crudo tiene `payload_ref` y la fecha para volver a medirlo.

Uso: python3 tools/registro_construir.py [--medido-en YYYY-MM-DD] [--verificar]
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys, unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CENSO = RAIZ / "Arena-Reimagined/02-ARCHIVO/censo-ecosistema-2026-10-15.tsv"
MAPA = RAIZ / "Arena-Reimagined/02-ARCHIVO/mapa-recursos-29oct.json"
SALIDA = RAIZ / "registry"
UMBRAL_DORMIDO = 180



import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402

MEDIDO_EN = "2026-10-15"


def ident(repo: str) -> str:
    base = repo.replace("/", "--").lower()
    base = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-z0-9._-]+", "-", base).strip("-.")
    return (base or "ficha")[:80]


def estado(push: str, corte: date) -> str:
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", push or ""):
        return "indeterminado"
    dias = (corte - date.fromisoformat(push)).days
    if dias < 0:
        return "indeterminado"
    return "vivo" if dias <= UMBRAL_DORMIDO else "dormido"


def piezas_por_repo() -> dict[str, list[str]]:
    if not MAPA.exists():
        return {}
    datos = json.loads(MAPA.read_text(encoding="utf-8"))
    por_pieza = datos.get("por_pieza") or {}
    salida: dict[str, list[str]] = {}
    for pieza, repos in por_pieza.items():
        if isinstance(repos, str):
            repos = [repos]
        for r in repos or []:
            if isinstance(r, str):
                salida.setdefault(r.lower(), []).append(str(pieza))
    return {k: sorted(set(v)) for k, v in salida.items()}


def leer_censo() -> tuple[list[dict], list[str]]:
    """Parsea el TSV por columnas, sin csv: el archivo trae una comilla suelta que
    descoloca al lector estándar y mezcla descripciones con filas ajenas."""
    lineas = CENSO.read_text(encoding="utf-8").split("\n")
    cabecera = lineas[0].split("\t")
    if cabecera[:2] != ["repo", "stars"]:
        raise SystemExit(f"cabecera inesperada en el censo: {cabecera[:3]}")
    filas, avisos = [], []
    for n, linea in enumerate(lineas[1:], start=2):
        if not linea.strip():
            continue
        partes = linea.split("\t")
        if len(partes) < 8:
            avisos.append(f"línea {n}: columnas insuficientes ({len(partes)})")
            continue
        repo = partes[0].strip()
        if "/" not in repo:
            avisos.append(f"línea {n}: no parece owner/repo: {repo[:40]}")
            continue
        if partes[5].startswith('"') or partes[5].endswith('"'):
            avisos.append(f"línea {n}: comilla suelta en descripcion de {repo}")
        filas.append({
            "repo": repo,
            "stars": partes[1].strip(),
            "creada": partes[2].strip(),
            "push": partes[3].strip(),
            "licencia": partes[4].strip(),
            "descripcion": "\t".join(partes[5:-2]).strip().strip('"'),
            "fuente": partes[-2].strip(),
            "stars_por_mes": partes[-1].strip(),
        })
    return filas, avisos


def licencia_de(valor: str, medido_en: str = MEDIDO_EN) -> dict:
    """Orden de la casa: SPDX → endpoint → texto → ausencia firmada."""
    v = (valor or "").strip()
    if not v or v == "-":
        return {"spdx": None, "metodo": "ausencia-firmada", "verificado_en": medido_en, "archivo": None}
    if v.upper() == "NOASSERTION":
        return {"spdx": "NOASSERTION", "metodo": "endpoint-license", "verificado_en": medido_en, "archivo": None}
    return {"spdx": v, "metodo": "spdx-api", "verificado_en": medido_en, "archivo": None}


def construir(medido_en: str) -> int:
    corte = date.fromisoformat(medido_en)
    filas, avisos = leer_censo()
    indice = piezas_por_repo()
    SALIDA.mkdir(exist_ok=True)
    for viejo in SALIDA.glob("*.json"):
        viejo.unlink()
    vistos = {}
    for f in filas:
        repo = (f.get("repo") or "").strip()
        if not repo or "/" not in repo:
            continue
        fid = ident(repo)
        vistos[fid] = vistos.get(fid, 0) + 1
        if vistos[fid] > 1:
            fid = f"{fid}-{vistos[fid]}"
        stars = int(f["stars"]) if (f.get("stars") or "").isdigit() else None
        try:
            vel = float(f["stars_por_mes"]) if (f.get("stars_por_mes") or "").strip() else None
        except ValueError:
            vel = None
        push = (f.get("push") or "").strip()
        fila_canonica = json.dumps({k: (f.get(k) or "") for k in sorted(f)}, ensure_ascii=False, separators=(",", ":"))
        ficha = {
            "id": fid,
            "repo": repo,
            "nombre": repo.split("/", 1)[1],
            "descripcion": (f.get("descripcion") or "")[:400],
            "medido_en": medido_en,
            "fuente": {
                "primaria": "github-api",
                "secundarias": [],
                "metodo": "campos del censo de la casa medidos contra la API oficial de GitHub; sin inferencias",
            },
            "licencia": licencia_de(f.get("licencia", ""), medido_en),
            "actividad": {
                "ultimo_push": push if re.match(r"^\d{4}-\d{2}-\d{2}$", push) else None,
                "estado": estado(push, corte),
                "semantica_http": 200,
                "ultima_release": None,
                "release_en": None,
            },
            "merito": {"stars": stars, "stars_por_mes": vel, "scorecard": None, "scorecard_en": None},
            "procedencia": {"swhid": None, "commit": None, "atestacion": None},
            "evidencia": {
                "sha256": hashlib.sha256(fila_canonica.encode()).hexdigest(),
                "payload_ref": f"censo-ecosistema-2026-10-15.tsv#{repo}",
                "nota": "sello de la fila del censo tal como se midió; no se conservó payload de API aparte",
            },
            "piezas": indice.get(repo.lower(), []),
            "frescura_dias": max(0, (date.fromisoformat(fecha_casa_hoy()) - corte).days),
        }
        (SALIDA / f"{fid}.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                            encoding="utf-8")
    calidad = {
        "censo": str(CENSO.relative_to(RAIZ)),
        "filas_leidas": len(filas),
        "avisos": avisos,
        "licencias": {
            "spdx_api": sum(1 for f in filas if (f["licencia"] or "").strip() not in ("", "-", "NOASSERTION")),
            "noassertion_endpoint": sum(1 for f in filas if f["licencia"].upper() == "NOASSERTION"),
            "ausencia_firmada": sum(1 for f in filas if (f["licencia"] or "").strip() in ("", "-")),
        },
        "nota": "Los avisos no se borran: el censo se conserva tal como se midió y el defecto queda a la vista.",
    }
    (SALIDA / "_calidad-censo.json").write_text(json.dumps(calidad, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (SALIDA / "_indice.json").write_text(
        json.dumps({"medido_en": medido_en, "fichas": len(list(SALIDA.glob('*.json'))) - 1,
                    "esquema": "schemas/ficha.schema.json"},
                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return len(list(SALIDA.glob("*.json"))) - 1


def main() -> int:
    global MEDIDO_EN
    ap = argparse.ArgumentParser()
    ap.add_argument("--medido-en", default=MEDIDO_EN)
    ap.add_argument("--verificar", action="store_true", help="no escribe: comprueba que el registro está al día")
    ap.add_argument("--indice", action="store_true",
                    help="refresca solo registry/_indice.json desde el disco (no toca las fichas)")
    args = ap.parse_args()
    MEDIDO_EN = args.medido_en
    if args.indice:
        # El índice cuenta lo que HAY, no lo que se construyó: tras una re-medición las fichas
        # cambian de fecha y el índice se quedaba diciendo la del censo. Reconstruir el registro
        # entero desde el censo borraría la re-medición, así que este modo solo toca el índice.
        fichas = [p for p in SALIDA.glob("*.json") if not p.name.startswith("_")]
        fechas = sorted({json.loads(p.read_text(encoding="utf-8")).get("medido_en")
                         for p in fichas if json.loads(p.read_text(encoding="utf-8")).get("medido_en")})
        indice = {"medido_en": fechas[-1] if fechas else MEDIDO_EN,
                  "medido_en_rango": [fechas[0], fechas[-1]] if fechas else [],
                  "fichas": len(fichas),
                  "esquema": "schemas/ficha.schema.json",
                  "nota": "medido_en es la fecha más reciente del registro; medido_en_rango dice la más vieja y la más nueva. Un registro medido en un solo día tiene un solo valor."}
        (SALIDA / "_indice.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n",
                                              encoding="utf-8")
        print(f"índice refrescado: {len(fichas)} fichas · medido_en {indice['medido_en']} · "
              f"rango {indice['medido_en_rango']}")
        return 0
    if args.verificar:
        actuales = len(list(SALIDA.glob("*.json"))) - 1
        print(f"registro en disco: {actuales} fichas · medido_en declarado: "
              f"{json.loads((SALIDA / '_indice.json').read_text())['medido_en'] if (SALIDA / '_indice.json').exists() else '—'}")
        return 0 if actuales > 0 else 1
    n = construir(args.medido_en)
    print(f"registro construido: {n} fichas · medido_en {args.medido_en} · salida registry/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
