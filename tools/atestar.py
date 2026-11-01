#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ATESTACIÓN · sella el registro con SHA-256 y encadena el lote anterior.

Lo que el sello prueba: los archivos no cambiaron después de firmarse.
Lo que NO prueba: que la medición sea correcta. Eso lo prueba la vara y la fecha declarada.
Cadena: cada lote guarda el sha256 del lote anterior; romper el historial se nota.

Uso:
  python3 tools/atestar.py            # crea sello si falta y escribe el lote
  python3 tools/atestar.py --verificar # solo verifica el sello existente
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import date, datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
SELLO = REGISTRO / "_manifiesto-sha256.tsv"
LOTES = RAIZ / "attestations"


CUBIERTAS = ("registry", "schemas", "Arena-Reimagined/01-PUBLICACIONES",
             "Arena-Reimagined/PROPUESTA-2026-10-31", "docs", "LEGAL")


def archivos() -> list[Path]:
    """Se sella el contenido y los datos: lo que se publica. El código que los revisa
    queda fuera a propósito — si se sellara, cada mejora de la vara rompería su propio sello."""
    salida = []
    for p in sorted(RAIZ.rglob("*")):
        if not p.is_file() or ".git" in p.parts or "attestations" in p.parts:
            continue
        rel = p.relative_to(RAIZ).as_posix()
        if not any(rel.startswith(c) for c in CUBIERTAS):
            continue
        if p.suffix not in {".json", ".md", ".tsv", ".yml", ".html", ".schema"}:
            continue
        if p == SELLO:
            continue
        salida.append(p)
    return salida


def sellar() -> str:
    lineas = []
    for p in archivos():
        lineas.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(RAIZ)}")
    SELLO.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return hashlib.sha256(SELLO.read_bytes()).hexdigest()


def verificar() -> tuple[int, int]:
    ok = mal = 0
    for linea in SELLO.read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        sha, _, ruta = linea.partition("  ")
        p = RAIZ / ruta
        if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == sha:
            ok += 1
        else:
            mal += 1
    return ok, mal


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    args = ap.parse_args()
    if args.verificar:
        ok, mal = verificar()
        print(f"integridad: {ok} archivos OK · {mal} alterados o ausentes")
        return 0 if mal == 0 else 1
    if SELLO.exists():
        ok, mal = verificar()
        if mal == 0:
            print(f"sello vigente: {ok} archivos sin cambios (no se re-sella)")
            return 0
        print(f"sello viejo: {mal} archivos cambiaron; se re-sella")
    huella_sello = sellar()
    LOTES.mkdir(exist_ok=True)
    anteriores = sorted(LOTES.glob("lote-*.json"))
    anterior = json.loads(anteriores[-1].read_text(encoding="utf-8"))["huella"] if anteriores else None
    ficha = {
        "lote": f"lote-{date.today().isoformat()}",
        "sellado_en": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "huella": huella_sello,
        "huella_lote_anterior": anterior,
        "archivos": len(SELLO.read_text(encoding="utf-8").splitlines()),
        "manifiesto": str(SELLO.relative_to(RAIZ)),
        "nota": "prueba que los archivos no cambiaron después de sellarse; no prueba que la medición sea correcta",
    }
    (LOTES / f"{ficha['lote']}.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"atestación {ficha['lote']}: {ficha['archivos']} archivos · huella {huella_sello[:16]}… · "
          f"anterior {anterior[:16] + '…' if anterior else 'ninguna'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
