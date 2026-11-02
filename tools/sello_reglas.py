#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGLAS DEL SELLO · en un solo sitio, para que la vara y la atestación no se contradigan.

Si `tools/atestar.py` sellara con unas reglas y `tools/vara.py` comprobara con otras, la compuerta
podría dar por bueno un árbol que la atestación nunca firmó. Aquí vive la única lista.

Lo que se sella: el contenido y los datos que se publican —incluidos los `.txt` de envío, que son lo
que sale a la calle—. Lo que queda fuera: el código que los revisa (si se sellara, cada mejora de la
vara rompería su propio sello) y las atestaciones anteriores.
"""
from __future__ import annotations
from pathlib import Path

CUBIERTAS = ("registry", "schemas", "Arena-Reimagined/01-PUBLICACIONES",
             "Arena-Reimagined/PROPUESTA-2026-10-31", "docs", "LEGAL",
             # la ley y el conocimiento operativo también se sellan: si alguien cambia una regla de
             # madrugada, el sello lo delata igual que un cambio de dato.
             "CIMIENTOS", "SKILLS", "PROCESOS", "corpus-la-bandita",
             "MANIFIESTO-ARQUITECTURA.md", "README.md")

SUFIJOS = {".json", ".md", ".tsv", ".yml", ".html", ".schema", ".txt"}


def archivos(raiz: Path, manifiesto: Path | None = None) -> list[Path]:
    """Archivos que deben estar en el sello de este árbol, en orden estable."""
    salida = []
    for p in sorted(raiz.rglob("*")):
        if not p.is_file() or ".git" in p.parts or "attestations" in p.parts:
            continue
        rel = p.relative_to(raiz).as_posix()
        if not any(rel.startswith(c) for c in CUBIERTAS):
            continue
        if p.suffix not in SUFIJOS:
            continue
        if manifiesto is not None and p == manifiesto:
            continue
        salida.append(p)
    return salida
