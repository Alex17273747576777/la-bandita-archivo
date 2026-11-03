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
             # la guía maestra es contenido publicado: sus fichas y su texto se sellan igual
             "guia-maestra",
             # el gobierno del repositorio también se sella. Antes quedaba fuera y por eso
             # el README podía cambiar sin que el sello lo notara: exactamente el agujero
             # que este archivo existe para cerrar.
             ".github", "LICENSES", ".reuse",
             "README.md", "ARQUITECTURA.md", "MAPA-DEL-ARCHIVO.md",
             "MANIFIESTO-ARQUITECTURA.md", "CORAZON-LA-BANDITA.md",
             "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md",
             "CHANGELOG.md", "NOTICE", "LICENSE", "Makefile")

# Archivos sin sufijo que también se sellan: el `Makefile` es la puerta de entrada —si cambia un
# destino, cambia lo que cualquiera ejecuta con confianza— y `.reuse/dep5` es la licencia de todo
# lo que no lleva cabecera propia.
EXACTOS = {"Makefile", ".reuse/dep5"}

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
        if p.suffix not in SUFIJOS and rel not in EXACTOS:
            continue
        if manifiesto is not None and p == manifiesto:
            continue
        salida.append(p)
    return salida
