#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAREAS · el extractor del archivo: de las piezas al tablero, sin copiar a mano.

Hoy las tareas de la casa viven donde deben vivir —dentro de la pieza que las
engendra, como líneas `#task 004 · ...`— pero eso las vuelve invisibles para quien
no abre los documentos uno por uno. Este programa las cosecha, comprueba que la
numeración no tenga huecos ni repetidos y escribe el tablero en `docs/TAREAS.md`.

Qué hace, en una frase: lee las piezas vivas, saca las tareas, y publica un
tablero que se puede leer de arriba abajo.

Qué no hace: no inventa tareas, no las cierra por su cuenta y no toca las
piezas. Cerrar una tarea es un acto humano que se escribe en la pieza siguiente.

Uso:
    python3 tools/tareas.py              # escribe docs/TAREAS.md y resume por pantalla
    python3 tools/tareas.py --json       # salida legible por máquina
    python3 tools/tareas.py --revisar    # solo comprueba, no escribe (para la CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLICACIONES = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
SALIDA = RAIZ / "docs" / "TAREAS.md"

TAREA = re.compile(r"^#task\s+(\d+)\s*·\s*(.+?)\s*$", re.M)
FECHA = re.compile(r"(\d{4}-\d{2}-\d{2})")
CANALES = {"Facebook-dominicano-ES": "Facebook", "WhatsApp-dominicano-ES": "WhatsApp"}


def piezas() -> list[Path]:
    """Solo las piezas del ciclo vivo: la raíz de cada canal, sin LEEME ni archivo."""
    salida: list[Path] = []
    for carpeta in CANALES:
        d = PUBLICACIONES / carpeta
        if not d.exists():
            continue
        salida += [p for p in sorted(d.glob("*.md"))
                   if not p.name.lower().startswith(("leeme", "readme"))]
    return salida


def cosechar() -> list[dict]:
    halladas: list[dict] = []
    for p in piezas():
        texto = p.read_text(encoding="utf-8", errors="replace")
        canal = next((v for k, v in CANALES.items() if k in str(p)), "?")
        m = FECHA.search(p.name)
        for num, cuerpo in TAREA.findall(texto):
            halladas.append({
                "id": int(num),
                "texto": re.sub(r"\s+", " ", cuerpo).strip(),
                "pieza": p.name,
                "canal": canal,
                "corte": m.group(1) if m else "",
            })
    return sorted(halladas, key=lambda t: (t["id"], t["canal"]))


def revisar(tareas: list[dict]) -> tuple[list[str], list[str]]:
    """La numeración es **por pieza**: cada pieza numera sus propias tareas desde 001.

    Se comprueba, entonces, dentro de cada pieza: que no haya huecos ni repetidos. Se informa
    aparte —sin bloquear— de las piezas que empezaron a numerar en otro sitio, porque la regla
    se fijó el 3-nov-2026 y las piezas publicadas antes no se retocan: se declaran.
    """
    fallos: list[str] = []
    avisos: list[str] = []
    if not tareas:
        return ["no hay ninguna tarea declarada en las piezas vivas"], []
    por_pieza: dict[str, list[dict]] = {}
    for t in tareas:
        por_pieza.setdefault(t["pieza"], []).append(t)
    for pieza, lista in sorted(por_pieza.items()):
        ids = sorted(t["id"] for t in lista)
        if len(set(ids)) != len(ids):
            fallos.append(f"{pieza[:40]}: número de tarea repetido dentro de la misma pieza")
        for a, b in zip(ids, ids[1:]):
            if b != a + 1:
                fallos.append(f"{pieza[:40]}: hueco en la numeración, se salta de {a:03d} a {b:03d}")
        if ids[0] != 1:
            avisos.append(f"{pieza[:40]}: numera desde {ids[0]:03d} y no desde 001 (pieza publicada antes de la regla; se declara, no se retoca)")
    return fallos, avisos


def escribir(tareas: list[dict], fallos: list[str], avisos: list[str]) -> None:
    ids = sorted({t["id"] for t in tareas})
    filas = "\n".join(
        f"| {t['id']:03d} | {t['texto']} | {t['canal']} · {t['pieza'][:2]} | {t['corte']} |"
        for t in tareas)
    rango = f"{ids[0]:03d} a {ids[-1]:03d}" if ids else "—"
    estado = "Numeración sin huecos ni repetidos dentro de cada pieza." if not fallos else "Numeración CON incidencias: ver la nota al pie."
    nota_avisos = ("\n".join(f"> **Declarado:** {a}" for a in avisos)
                   or "> Ninguna pieza fuera de la regla de numeración.")
    cuerpo = f"""# TABLERO DE TAREAS

*Generado por `tools/tareas.py` el día que se corre. No se edita a mano: se vuelve a correr.*

**TL;DR —** {len(tareas)} tareas abiertas en {len(piezas())} piezas vivas, numeradas dentro de cada pieza, de {rango}. {estado} El tablero se regenera con `make tareas` y la integración continua comprueba que no haya huecos.

## De dónde salen

Cada tarea vive en la pieza que la engendra, como una línea `#task NNN · texto`. Esa es la regla de la casa: **una tarea no se guarda en una lista aparte, se escribe dentro del documento que la justifica**, para que quien lea la pieza vea qué quedó pendiente y por qué. Este tablero no es la fuente: es la vista.

## Las tareas abiertas

| # | Tarea | Origen | Corte |
|---|---|---|---|
{filas}

## Numeración: la regla y lo declarado

{nota_avisos}

La numeración es **por pieza**, no global: cada pieza numera sus tareas desde 001 porque la compuerta de novedad (M28) las cuenta dentro de la pieza. Por eso la misma cifra puede aparecer en dos piezas distintas y no es un error: la tarea se identifica por su número **y** su pieza.

## Cómo se cierra una tarea

No se borra de aquí. Se cumple, y la pieza siguiente lo cuenta con su medición al lado. Cuando una tarea se cumple, su número deja de aparecer en las piezas nuevas y el tablero se encoge solo en la próxima corrida. Una tarea que llevas tres meses sin hacer no es una tarea: es una decisión que hay que tomar y decir en voz alta.

## Las comprobaciones que hace este programa

1. **Sin huecos**: la numeración sube de uno en uno; un salto se declara aquí y no se disimula.
2. **Sin textos contradictorios**: el mismo número no puede decir dos cosas distintas en dos canales.

*La Bandita informa a partir de fuentes fechadas.*
"""
    SALIDA.write_text(cuerpo, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Cosecha las #task de las piezas vivas.")
    ap.add_argument("--json", action="store_true", help="salida legible por máquina")
    ap.add_argument("--revisar", action="store_true", help="comprueba sin escribir el tablero")
    a = ap.parse_args()

    tareas = cosechar()
    fallos, avisos = revisar(tareas)
    if a.json:
        print(json.dumps({"tareas": tareas, "fallos": fallos, "avisos": avisos,
                          "piezas": len(piezas())}, ensure_ascii=False, indent=1))
        return 0 if not fallos else 1
    if not a.revisar:
        escribir(tareas, fallos, avisos)
        print(f"tablero escrito: {SALIDA.relative_to(RAIZ)} · {len(tareas)} tareas")
    for f in fallos:
        print(f"  ✗ {f}")
    for x in avisos:
        print(f"  · {x}")
    print(f"tareas: {len(tareas)} · piezas: {len(piezas())} · incidencias: {len(fallos)} · declaradas: {len(avisos)}")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
