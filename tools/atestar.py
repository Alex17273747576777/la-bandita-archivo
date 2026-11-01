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
import sys as _sys
_sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402
from sello_reglas import archivos as archivos_sellables  # noqa: E402
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
SELLO = REGISTRO / "_manifiesto-sha256.tsv"
LOTES = RAIZ / "attestations"


def archivos() -> list[Path]:
    """Qué se sella se decide en `sello_reglas.py`, para que la vara compruebe lo mismo."""
    return archivos_sellables(RAIZ, SELLO)


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


def altas_y_bajas() -> tuple[list[str], list[str]]:
    """El sello viejo solo miraba lo que ya estaba firmado: un archivo NUEVO entraba sin sello y
    nadie se enteraba. Aquí se comparan los dos conjuntos, el de disco y el del manifiesto."""
    en_disco = {p.relative_to(RAIZ).as_posix() for p in archivos()}
    en_sello = set()
    for linea in SELLO.read_text(encoding="utf-8").splitlines():
        if linea.strip():
            _, _, ruta = linea.partition("  ")
            en_sello.add(ruta)
    return sorted(en_disco - en_sello), sorted(en_sello - en_disco)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    args = ap.parse_args()
    if args.verificar:
        ok, mal = verificar()
        altas, bajas = altas_y_bajas()
        print(f"integridad: {ok} archivos OK · {mal} alterados o ausentes · "
              f"{len(altas)} sin sellar · {len(bajas)} desaparecidos")
        return 0 if (mal == 0 and not altas and not bajas) else 1
    if SELLO.exists():
        ok, mal = verificar()
        altas, bajas = altas_y_bajas()
        if mal == 0 and not altas and not bajas:
            print(f"sello vigente: {ok} archivos sin cambios (no se re-sella)")
            return 0
        motivo = []
        if mal:
            motivo.append(f"{mal} alterados")
        if altas:
            motivo.append(f"{len(altas)} sin sellar ({', '.join(altas[:3])}{'…' if len(altas) > 3 else ''})")
        if bajas:
            motivo.append(f"{len(bajas)} desaparecidos")
        print(f"sello viejo: {'; '.join(motivo)}; se re-sella")
    huella_sello = sellar()
    LOTES.mkdir(exist_ok=True)
    anteriores = sorted(LOTES.glob("lote-*.json"))
    anterior = json.loads(anteriores[-1].read_text(encoding="utf-8"))["huella"] if anteriores else None
    ficha = {
        "lote": f"lote-{fecha_casa_hoy()}",
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
