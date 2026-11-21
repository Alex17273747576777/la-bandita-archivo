#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FEYNMAN · comprueba que las reglas, textos guía y los 12 capítulos cumplen los 4 pasos.

Verifica de forma determinista que la norma obligatoria del método de Richard Feynman
(selección/estudio, enseñanza simple sin jerga, detección de lagunas con vuelta a fuente,
y simplificación con analogía) está presente e íntegra en la ley raíz, los cimientos,
los procesos, las habilidades, la documentación de listas/análisis/recursos y los doce
capítulos de la guía maestra.
"""
from __future__ import annotations

import sys
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]

PASOS_CAPITULO: tuple[str, ...] = (
    "1. **Seleccionar y estudiar el concepto:**",
    "2. **Enseñarlo con palabras simples:**",
    "3. **Identificar lagunas y volver a la fuente original:**",
    "4. **Simplificar y revisar con analogías:**",
)


def verificar(raiz: Path | None = None) -> list[str]:
    base = raiz or RAIZ
    fallos: list[str] = []

    obligatorios = [
        ("CORAZON-LA-BANDITA.md", "MÉTODO RICHARD FEYNMAN"),
        ("REGLAS/INDICE-DE-REGLAS.md", "Método de Richard Feynman"),
        ("CIMIENTOS/04-VOZ-Y-CIERRE.md", "Método Richard Feynman"),
        ("PROCESOS/01-PIEZA.md", "Método Feynman (4 pasos)"),
        ("SKILLS/escribir-pieza/SKILL.md", "Método Richard Feynman completo"),
        ("docs/METODO-FEYNMAN-OBLIGATORIO.md", "Aplicación completa a las **listas de textos**"),
    ]
    for rel, marca in obligatorios:
        p = base / rel
        if not p.is_file():
            fallos.append(f"falta archivo obligatorio: {rel}")
            continue
        txt = p.read_text(encoding="utf-8")
        if marca not in txt:
            fallos.append(f"{rel}: falta la marca '{marca}'")

    cap_dir = base / "guia-maestra" / "texto" / "capitulos"
    capitulos = sorted(cap_dir.glob("*.md"))
    if len(capitulos) != 12:
        fallos.append(f"guia-maestra: se esperaban 12 capítulos, hay {len(capitulos)}")

    for cap in capitulos:
        txt = cap.read_text(encoding="utf-8")
        if "## Método Richard Feynman (4 pasos obligatorios)" not in txt:
            fallos.append(f"{cap.name}: falta sección Feynman")
            continue
        for paso in PASOS_CAPITULO:
            if paso not in txt:
                fallos.append(f"{cap.name}: falta '{paso}'")
        if "*analogía" not in txt.lower():
            fallos.append(f"{cap.name}: falta analogía explícita en paso 4")

    return fallos


def main() -> int:
    fallos = verificar()
    if fallos:
        for f in fallos:
            print("FALLO:", f)
        print(f"feynman: {len(fallos)} fallos")
        return 1
    print("feynman: 12 capítulos + 6 documentos normativos completos (4/4 pasos) · fallos: NINGUNO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
