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


def piezas_extra() -> list[str]:
    """Piezas de la segunda vuelta: las que existen en la carpeta y no son del ciclo 01–40.

    El ciclo 01–40 está cerrado y no se reescribe. Lo que venga después se cuenta aparte,
    con su propio número, para que el LEEME no diga «cuarenta» cuando hay más.
    """
    vistas = []
    for f in CARPETA.glob("*.md"):
        m = re.match(r"(\d\d)-", f.name)
        if m and m.group(1) not in PIEZAS and m.group(1) not in vistas:
            vistas.append(m.group(1))
    return sorted(vistas)

FILA = re.compile(r"^\|\s*(\d{2})\s*\|(?P<resto>.*)\|\s*$")


def medir() -> dict[str, dict[str, int]]:
    """Devuelve {número: {'cuerpo': caracteres, 'fijado': caracteres}}."""
    datos: dict[str, dict[str, int]] = {}
    for f in CARPETA.glob("*.md"):
        n = f.name[:2]
        if not n.isdigit():
            continue  # el LEEME y cualquier archivo suelto no son piezas
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
        if f.name[:2] not in PIEZAS and f.name[:2] not in piezas_extra():
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


def _anadir_filas_que_faltan(datos: dict) -> None:
    """Si hay piezas en el disco que no están en la tabla, se añaden al final.

    El LEEME no es una lista cerrada: es el estado de la carpeta. Si la carpeta creció,
    el LEEME crece con ella; lo que no hace es reescribir las filas que ya estaban.
    """
    tabla = columnas_del_leeme()
    faltan = [n for n in PIEZAS + piezas_extra()
              if n in datos and "cuerpo" in datos[n] and "fijado" in datos[n] and n not in tabla]
    if not faltan:
        return
    lineas = LEEME.read_text(encoding="utf-8").splitlines()
    ultima = max((i for i, l in enumerate(lineas) if FILA.match(l)), default=len(lineas) - 1)
    nuevas = []
    for n in sorted(faltan):
        d = datos[n]
        nuevas.append(f"| {n} | Pieza {n} · segunda vuelta | {miles(d['cuerpo'])} | {miles(d['fijado'])} | **Añadida el 9-nov** · segunda vuelta, fuera del ciclo 01–40 |")
    lineas[ultima + 1:ultima + 1] = nuevas
    LEEME.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print(f"filas añadidas al LEEME: {len(nuevas)} → {' '.join(faltan)}")


def comprobar() -> int:
    datos, tabla = medir(), columnas_del_leeme()
    fallos: list[str] = []

    for n in PIEZAS + piezas_extra():
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
    total = len(PIEZAS) + len(piezas_extra())
    print(f"\npiezas comprobadas: {total} · fallos: {len(fallos)}")
    return 0 if not fallos else 1


def arreglar() -> int:
    datos = medir()
    _anadir_filas_que_faltan(datos)
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
