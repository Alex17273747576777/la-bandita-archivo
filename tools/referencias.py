#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REFERENCIAS · comprueba que ninguna carpeta movida siga citada por su ruta vieja.

Guarda la tabla de carpetas movidas y audita el árbol contra ella, distinguiendo
dos cosas que no son lo mismo:

* una ruta vieja citada por un archivo que hoy se lee o se ejecuta → FALLO (detiene la línea);
* una ruta vieja citada por un acta o un registro histórico → CITA (se conserva y el mapa la traduce).

Qué hace:
  * Lee la tabla de mudanzas (carpetas antes → después).
  * Recorre todos los archivos de texto del árbol buscando citas a rutas viejas.
  * Distingue citas en archivos vivos vs. actas/histórico.
  * Reporta 0 rutas vivas rotas si todo está bien.

Qué NO hace:
  * No corrige rutas por su cuenta: corregir una ruta exige saber qué quería decir la frase.
  * No modifica actas ni registros históricos: esas citas se conservan a propósito.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
MAPA: Path = RAIZ / "MAPA-DEL-ARCHIVO.md"

# Tabla de mudanzas conocidas (antes → después). Se actualiza con cada reestructura del árbol.
MUDANZAS: dict[str, str] = {
    "uploads/": "ARCHIVO-HISTORICO/subidas-2026-09/",
    "Arena-Reimagined/_versiones/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_versiones/",
    "Arena-Reimagined/packs/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/packs/",
    "Arena-Reimagined/_herramientas/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas/",
    "Arena-Reimagined/_herramientas-casa/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas-casa/",
    "Arena-Reimagined/_referencia/": "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_referencia/",
    "_archivo-historico/": "ARCHIVO-HISTORICO/",
}

EXTENSIONES_TEXTO: tuple[str, ...] = (
    ".md", ".py", ".json", ".tsv", ".csv", ".yaml", ".yml", ".txt", ".html", ".css", ".js",
)


@dataclass
class Cita:
    archivo: Path
    linea: int
    texto: str
    ruta_vieja: str


def _es_acta_o_historico(ruta: Path) -> bool:
    partes = ruta.parts
    return any(p in ("ARCHIVO-HISTORICO", "02-ARCHIVO", "_ARCHIVO-HISTORICO") for p in partes) or "docs/" in str(ruta.parent)


def _buscar_citas(contenido: str) -> list[str]:
    """Busca menciones a rutas viejas en el contenido de un archivo."""
    encontradas: list[str] = []
    for ruta_vieja in MUDANZAS:
        patron = re.escape(ruta_vieja.rstrip("/"))
        if re.search(patron, contenido):
            encontradas.append(ruta_vieja)
    return encontradas


def _auditar_archivo(ruta: Path) -> list[Cita]:
    if not ruta.suffix in EXTENSIONES_TEXTO:
        return []
    try:
        contenido = ruta.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    citas: list[Cita] = []
    for i, linea in enumerate(contenido.splitlines(), 1):
        for rv in _buscar_citas(linea):
            citas.append(Cita(archivo=ruta, linea=i, texto=linea.strip(), ruta_vieja=rv))
    return citas


def main() -> int:
    citas_vivas: list[Cita] = []
    citas_historicas: list[Cita] = []

    for p in RAIZ.rglob("*"):
        if not p.is_file():
            continue
        if ".git" in p.parts:
            continue
        if p.name == ".gitignore":
            continue
        for c in _auditar_archivo(p):
            if _es_acta_o_historico(p):
                citas_historicas.append(c)
            else:
                citas_vivas.append(c)

    print(f"referencias: {len(citas_vivas)} rutas vivas rotas · {len(citas_historicas)} citas históricas")
    if citas_vivas:
        print("  ⚠ rutas vivas rotas (deben corregirse):")
        for c in citas_vivas[:20]:
            print(f"    {c.archivo.relative_to(RAIZ)}:{c.linea} · cita a {c.ruta_vieja}")
        print("  G17 impide que la próxima mudanza se olvide de esto.")
        return 1
    print("  0 rutas vivas rotas · G17 en verde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
