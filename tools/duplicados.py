#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DUPLICADOS · censo de copias por contenido, para gobernar sin borrar a ciegas.

No borra nada. Mide: agrupa archivos idénticos por SHA-256, detecta piezas duplicadas por
número y plataforma con distinta fecha, y publica cuánto pesa la duplicación. La decisión de
conservar o retirar es del dueño; esta herramienta solo le quita la venda.

Uso: python3 tools/duplicados.py [--json]
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CUBIERTAS = ("Arena-Reimagined/01-PUBLICACIONES", "Arena-Reimagined/00-CANON", "corpus-la-bandita",
             "ARCHIVO-HISTORICO/03-PUBLICACIONES-2026-09-15",
             "ARCHIVO-HISTORICO/04-VERSIONES-MULTIIDIOMA")


def archivos() -> list[Path]:
    salida = []
    for p in sorted(RAIZ.rglob("*")):
        if not p.is_file() or ".git" in p.parts or "attestations" in p.parts:
            continue
        rel = p.relative_to(RAIZ).as_posix()
        if any(rel.startswith(c) for c in CUBIERTAS) and p.suffix.lower() in {".md", ".html", ".json", ".tsv"}:
            salida.append(p)
    return salida


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    lista = archivos()
    por_hash: dict[str, list[Path]] = defaultdict(list)
    for p in lista:
        por_hash[hashlib.sha256(p.read_bytes()).hexdigest()].append(p)

    identicos = {h: v for h, v in por_hash.items() if len(v) > 1}
    bytes_repetidos = sum(p.stat().st_size for grupo in identicos.values() for p in grupo[1:])

    # piezas del mismo número y plataforma con distinta fecha en el nombre
    patron = re.compile(r"^(\d{2})-.*?(WhatsApp|Facebook)-La-Bandita-(\d{4}-\d{2}-\d{2})", re.I)
    por_pieza: dict[tuple[str, str], list[tuple[str, Path]]] = defaultdict(list)
    for p in lista:
        m = patron.match(p.name)
        if m:
            por_pieza[(m.group(1), m.group(2).lower())].append((m.group(3), p))
    versiones = {k: v for k, v in por_pieza.items() if len(v) > 1}

    informe = {
        "archivos_censados": len(lista),
        "grupos_identicos": len(identicos),
        "archivos_repetidos": sum(len(v) - 1 for v in identicos.values()),
        "bytes_repetidos": bytes_repetidos,
        "piezas_con_varias_fechas": {
            f"{k[0]}-{k[1]}": [{"fecha": f, "archivo": str(p.relative_to(RAIZ))} for f, p in sorted(v)]
            for k, v in sorted(versiones.items())
        },
        "nota": "no se borra nada: el censo se publica para que la decisión sea del dueño",
    }
    if args.json:
        print(json.dumps(informe, ensure_ascii=False, indent=1))
    else:
        print("CENSO DE DUPLICADOS · solo mide, no borra")
        print(f"archivos censados: {informe['archivos_censados']}")
        print(f"grupos idénticos: {informe['grupos_identicos']} · copias sobrantes: {informe['archivos_repetidos']} "
              f"· peso repetido: {informe['bytes_repetidos'] / 1048576:.1f} MB")
        print(f"piezas con varias fechas: {len(versiones)}")
        for k, v in sorted(versiones.items())[:12]:
            print(f"  · pieza {k[0]} {k[1]}: {', '.join(f for f, _ in sorted(v))}")
        if len(versiones) > 12:
            print(f"  · … y {len(versiones) - 12} más (ver --json)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
