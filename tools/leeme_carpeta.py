#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LEEME DE LA CARPETA · cuadra lo que el LEEME dice con lo que hay en el disco.

Comprueba tres cosas sobre Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES:

  1. que cada número 01–40 tenga exactamente **un cuerpo y un comentario fijado**;
  2. que la columna «Cuerpo» y la columna «Fijado» del LEEME coincidan con los
     caracteres reales de cada archivo;
  3. que en la raíz de la carpeta no haya piezas sin número.

Qué NO hace: no valida el contenido editorial ni las cifras de cada pieza. Eso
son las compuertas de tools/vara.py.

Uso:
  python3 tools/leeme_carpeta.py              # comprueba; sale 0 solo si cuadra
  python3 tools/leeme_carpeta.py --arreglar   # reescribe las dos columnas
  python3 tools/leeme_carpeta.py --json       # informe legible por máquina
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CARPETA = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES" / "Facebook-dominicano-ES"
LEEME = CARPETA / "LEEME-de-la-carpeta.md"
PIEZAS = [f"{n:02d}" for n in range(1, 41)]

FILA = re.compile(r"^\|\s*(\d{2})\s*\|(?P<resto>.*)\|\s*$")


def medir() -> dict[str, dict[str, int]]:
    """Devuelve {número: {'cuerpo': caracteres, 'fijado': caracteres}}."""
    datos: dict[str, dict[str, int]] = {}
    for f in CARPETA.glob("*.md"):
        n = f.name[:2]
        if n not in PIEZAS:
            continue
        datos.setdefault(n, {})
        clave = "fijado" if "Comentario-fijado" in f.name else "cuerpo"
        datos[n][clave] = len(f.read_text(encoding="utf-8"))
    return datos


def huerfanos() -> list[str]:
    """Archivos .md en la raíz que no empiezan por número de pieza ni son el LEEME."""
    fuera = []
    for f in sorted(CARPETA.glob("*.md")):
        if f.name == LEEME.name:
            continue
        if f.name[:2] not in PIEZAS:
            fuera.append(f.name)
    return fuera


def columnas_del_leeme() -> dict[str, tuple[str, str]]:
    """Lee las columnas 3 y 4 (Cuerpo, Fijado) de la tabla del LEEME."""
    tabla: dict[str, tuple[str, str]] = {}
    for linea in LEEME.read_text(encoding="utf-8").splitlines():
        m = FILA.match(linea)
        if not m:
            continue
        celdas = [c.strip() for c in m.group("resto").split("|")]
        if len(celdas) >= 3:
            tabla[m.group(1)] = (celdas[1], celdas[2])
    return tabla


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def comprobar() -> int:
    datos, tabla = medir(), columnas_del_leeme()
    fallos: list[str] = []

    for n in PIEZAS:
        d = datos.get(n, {})
        if "cuerpo" not in d:
            fallos.append(f"pieza {n}: falta el cuerpo")
        if "fijado" not in d:
            fallos.append(f"pieza {n}: falta el comentario fijado")
        if n not in tabla:
            fallos.append(f"pieza {n}: no está en la tabla del LEEME")
        elif "cuerpo" in d and "fijado" in d:
            c_leeme, f_leeme = tabla[n]
            if c_leeme != miles(d["cuerpo"]):
                fallos.append(f"pieza {n}: el LEEME dice cuerpo {c_leeme} y el archivo tiene {miles(d['cuerpo'])}")
            if f_leeme != miles(d["fijado"]):
                fallos.append(f"pieza {n}: el LEEME dice fijado {f_leeme} y el archivo tiene {miles(d['fijado'])}")

    for nombre in huerfanos():
        fallos.append(f"archivo sin número de pieza en la raíz: {nombre}")

    for f in fallos:
        print("  FALLO ·", f)
    print(f"\npiezas comprobadas: {len(PIEZAS)} · fallos: {len(fallos)}")
    return 0 if not fallos else 1


def arreglar() -> int:
    datos = medir()
    lineas = LEEME.read_text(encoding="utf-8").splitlines()
    salida, tocadas = [], 0
    for linea in lineas:
        m = FILA.match(linea)
        if m and m.group(1) in datos and "cuerpo" in datos[m.group(1)] and "fijado" in datos[m.group(1)]:
            n = m.group(1)
            celdas = [c.strip() for c in m.group("resto").split("|")]
            if len(celdas) >= 3:
                celdas[1] = miles(datos[n]["cuerpo"])
                celdas[2] = miles(datos[n]["fijado"])
                linea = "| " + n + " | " + " | ".join(celdas) + " |"
                tocadas += 1
        salida.append(linea)
    LEEME.write_text("\n".join(salida) + "\n", encoding="utf-8")
    print(f"filas reescritas con el conteo real: {tocadas}")
    return 0


def main(argv: list[str]) -> int:
    if "--arreglar" in argv:
        return arreglar()
    if "--json" in argv:
        print(json.dumps({"medido": medir(), "huerfanos": huerfanos()}, ensure_ascii=False, indent=1))
        return 0
    return comprobar()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
