#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGLAS DEL SELLO · en un solo sitio, para que la vara y la atestación no se contradigan.

Si `tools/atestar.py` sellara con unas reglas y `tools/vara.py` comprobara con otras, la compuerta
podría dar por bueno un árbol que la atestación nunca firmó. Aquí vive la única lista.

Lo que se sella: el contenido y los datos que se publican —incluidos los `.txt` de envío, que son lo
que sale a la calle—. Lo que queda fuera: el código que los revisa (si se sellara, cada mejora de la
vara rompería su propio sello) y las atestaciones anteriores.

Qué hace:
  * Define la lista única de directorios, sufijos y archivos exactos que entran en el sello.
  * Proporciona `archivos(raiz, manifiesto)` para listar los archivos que deben sellarse.

Qué NO hace:
  * No sella por sí mismo: solo dice qué archivos entran.
  * No decide cuándo re-sellar: eso lo hace `atestar.py`.
  * No modifica el árbol: solo lee rutas.
"""
from __future__ import annotations

from pathlib import Path

CUBIERTAS: tuple[str, ...] = (
    "registry", "schemas", "Arena-Reimagined/01-PUBLICACIONES",
    "Arena-Reimagined/PROPUESTA-2026-10-31", "docs", "LEGAL",
    "CIMIENTOS", "SKILLS", "PROCESOS", "corpus-la-bandita",
    "guia-maestra",
    ".github", "LICENSES", ".reuse",
    "README.md", "ARQUITECTURA.md", "MAPA-DEL-ARCHIVO.md",
    "MANIFIESTO-ARQUITECTURA.md", "CORAZON-LA-BANDITA.md",
    "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md",
    "CHANGELOG.md", "NOTICE", "LICENSE", "Makefile",
)

EXACTOS: frozenset[str] = frozenset({"Makefile", ".reuse/dep5"})

SUFIJOS: frozenset[str] = frozenset({".json", ".md", ".tsv", ".yml", ".html", ".schema", ".txt"})

EXCLUIDOS: frozenset[str] = frozenset({".git", "attestations", "site"})


def _esta_cubierto(rel: str) -> bool:
    """Un archivo está cubierto si su ruta comienza por alguno de los directorios de CUBIERTAS."""
    return any(rel.startswith(c) for c in CUBIERTAS)


def archivos(raiz: Path, manifiesto: Path | None = None) -> list[Path]:
    """Archivos que deben estar en el sello de este árbol, en orden estable."""
    salida: list[Path] = []
    for p in sorted(raiz.rglob("*")):
        if not p.is_file():
            continue
        partes = p.parts
        if ".git" in partes or "attestations" in partes or "site" in partes:
            continue
        rel = p.relative_to(raiz).as_posix()
        if not _esta_cubierto(rel):
            continue
        if p.suffix not in SUFIJOS and rel not in EXACTOS:
            continue
        if manifiesto is not None and p == manifiesto:
            continue
        salida.append(p)
    return salida


if __name__ == "__main__":
    import sys
    raiz = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    lista = archivos(raiz)
    print(f"{len(lista)} archivos para sellar")
    for p in lista[:20]:
        print(f"  {p.relative_to(raiz)}")
    if len(lista) > 20:
        print(f"  … y {len(lista) - 20} más")
