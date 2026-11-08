#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ATESTACIÓN · sella el registro con SHA-256 y encadena el lote anterior.

Recorre el árbol, calcula la huella SHA-256 de cada archivo que `sello_reglas` dice que debe
sellarse, y escribe un manifiesto encadenado con el lote anterior: cada sello lleva dentro la
huella del sello de ayer.

Uso:
  python3 tools/atestar.py                    # sella el árbol completo
  python3 tools/atestar.py --verificar        # verifica que el sello actual coincida con el árbol

Qué hace:
  * Calcula SHA-256 de cada archivo que debe sellarse (según tools/sello_reglas.py).
  * Escribe attestations/lote-YYYY-MM-DD.json con la huella y la del lote anterior.
  * Escribe attestations/lote-YYYY-MM-DD.tsv con la tabla de huellas por archivo.
  * Con --verificar, compara el manifiesto actual contra el árbol tal como está.

Qué NO hace:
  * No decide qué archivos importan: usa sello_reglas.py para saberlo.
  * Si falta un archivo, lo dice en vez de callarlo.
  * No firma con llave propia: la firma Sigstore se hace en la integración continua.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sello_reglas import archivos as archivos_para_sellar  # noqa: E402

RAIZ: Path = Path(__file__).resolve().parents[1]
ATTESTATIONS: Path = RAIZ / "attestations"


def _fecha_hoy() -> date:
    """Fecha de hoy, permitiendo sobrescritura vía variable de entorno LOTE_FECHA (YYYY-MM-DD)."""
    fecha_env = os.environ.get("LOTE_FECHA")
    if fecha_env:
        try:
            return date.fromisoformat(fecha_env)
        except ValueError:
            pass
    return date.today()


def _huella_archivo(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def _cargar_lote_anterior() -> dict | None:
    """Busca el lote de atestación más reciente previo a hoy."""
    hoy = _fecha_hoy().isoformat()
    lotes: list[Path] = sorted(ATTESTATIONS.glob("lote-*.json"))
    previos = [l for l in lotes if l.stem != f"lote-{hoy}"]
    if not previos:
        return None
    try:
        return json.loads(previos[-1].read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def sellar() -> dict:
    """Sella el árbol completo y devuelve el manifiesto del lote."""
    sello_path_hoy = ATTESTATIONS / f"lote-{_fecha_hoy().isoformat()}.json"
    lista = archivos_para_sellar(RAIZ, manifiesto=sello_path_hoy)
    huellas: dict[str, str] = {}
    for p in lista:
        rel = str(p.relative_to(RAIZ))
        huellas[rel] = _huella_archivo(p)

    anterior = _cargar_lote_anterior()
    huella_anterior = anterior.get("huella") if anterior else None

    lote = {
        "fecha": _fecha_hoy().isoformat(),
        "archivos": len(lista),
        "huella": hashlib.sha256(json.dumps(huellas, sort_keys=True).encode()).hexdigest(),
        "anterior": huella_anterior,
        "tabla": huellas,
    }

    ATTESTATIONS.mkdir(parents=True, exist_ok=True)
    hoy_iso = _fecha_hoy().isoformat()
    (ATTESTATIONS / f"lote-{hoy_iso}.json").write_text(
        json.dumps(lote, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )

    lineas = ["archivo\tsha256"]
    for rel in sorted(huellas):
        lineas.append(f"{rel}\t{huellas[rel]}")
    (ATTESTATIONS / f"lote-{hoy_iso}.tsv").write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print(f"atestación lote-{hoy_iso}: {len(lista)} archivos · huella {lote['huella'][:16]}…")
    if huella_anterior:
        print(f"  anterior: {huella_anterior[:16]}…")
    return lote


def verificar() -> int:
    """Verifica que el sello del lote actual coincida con el árbol. Devuelve 0 si OK."""
    sello_path = ATTESTATIONS / f"lote-{_fecha_hoy().isoformat()}.json"
    if not sello_path.exists():
        print(f"no existe el lote de hoy: {sello_path}")
        return 1

    try:
        lote = json.loads(sello_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"lote corrupto: {e}")
        return 1

    lista = archivos_para_sellar(RAIZ, manifiesto=sello_path)
    huellas_actuales: dict[str, str] = {}
    for p in lista:
        rel = str(p.relative_to(RAIZ))
        huellas_actuales[rel] = _huella_archivo(p)

    tabla_lote = lote.get("tabla", {})
    alterados = [r for r, h in tabla_lote.items() if huellas_actuales.get(r) != h]
    ausentes = [r for r in tabla_lote if r not in huellas_actuales]
    nuevos = [r for r in huellas_actuales if r not in tabla_lote]

    ok = not alterados and not ausentes and not nuevos
    if ok:
        print(f"integridad: {len(lista)} archivos OK · 0 alterados o ausentes · 0 sin sellar · 0 desaparecidos")
        return 0

    print(f"sello roto: {len(alterados)} alterados · {len(ausentes)} desaparecidos · {len(nuevos)} sin sellar")
    for r in alterados[:10]:
        print(f"  alterado: {r}")
    for r in ausentes[:10]:
        print(f"  ausente: {r}")
    for r in nuevos[:10]:
        print(f"  sin sellar: {r}")
    return 1


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Sella el árbol con SHA-256 encadenado.")
    parser.add_argument("--verificar", action="store_true", help="verifica que el sello coincida con el árbol")
    args = parser.parse_args(argv)

    if args.verificar:
        return verificar()
    sellar()
    return 0


if __name__ == "__main__":
    sys.exit(main())
