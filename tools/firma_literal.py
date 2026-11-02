#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TESTIGO DE FIRMA · comprueba lo que M01 no puede comprobar con una regex.

`manual_gate` (M01) exige que cada pieza contenga la frase de la casa
«La Bandita informa a partir de fuentes fechadas.». No puede exigir más, porque
la frase aparece dentro de un párrafo con remate propio y cada pieza la lleva
distinta.

Este testigo añade tres exigencias textuales que sí se pueden comprobar letra
por letra, sin interpretación:

  1. la frase de la casa aparece EXACTAMENTE igual (sin cambios de puntuación);
  2. va en el último bloque de la pieza, junto al remate, no perdida en el medio;
  3. el bloque de medición del corte lleva fecha del día de la casa y la hora
     («entre las HH:MM y las HH:MM»), que es lo que separa un dato fresco de uno
     heredado.

Uso:
    python3 tools/firma_literal.py            # informe de todas las piezas vivas
    python3 tools/firma_literal.py --verificar  # código de salida 1 si algo falla
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBL = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
FIRMA = "La Bandita informa a partir de fuentes fechadas."
MESES = ("ene", "feb", "mar", "abr", "may", "jun",
         "jul", "ago", "sep", "oct", "nov", "dic")


def piezas() -> tuple[list[Path], int]:
    """Solo las piezas con banda declarada: son las que se están reescribiendo.

    Las demás siguen en el archivo viejo y no se les exige la firma literal; se
    cuentan y se dicen, para que nadie crea que se revisaron y pasaron."""
    bandas = json.loads((RAIZ / "docs" / "bandas.json").read_text(encoding="utf-8"))
    vivas = []
    for canal, clave in (("WhatsApp-dominicano-ES", "whatsapp"),
                         ("Facebook-dominicano-ES", "facebook")):
        for _, v in (bandas.get(clave, {}).get("piezas", {}) or {}).items():
            f = PUBL / canal / v["archivo"]
            if f.exists():
                vivas.append(f)
    todas = [p for c in ("WhatsApp-dominicano-ES", "Facebook-dominicano-ES")
             for p in (PUBL / c).glob("*.md") if not p.name.startswith("_")]
    return sorted(vivas), len(todas) - len(vivas)


def revisar(p: Path) -> list[str]:
    t = p.read_text(encoding="utf-8", errors="replace")
    fallos = []

    # 1 · la frase, letra por letra
    if FIRMA not in t:
        fallos.append("no lleva la frase de la casa, tal cual")
        return fallos

    # 2 · la frase vive al final del cuerpo, antes de las notas al pie
    pos = t.index(FIRMA)
    notas = re.search(r"^##\s*🗒️", t, re.M)
    if notas and pos > notas.start():
        fallos.append("la frase de la casa quedó después de las notas al pie")
    elif pos < len(t) * 0.80:
        fallos.append("la frase de la casa no está en el cierre")

    # 3 · la medición del corte lleva día y hora
    linea = re.search(r"Medición del corte:?\*?\s*([^\n]+)", t)
    if not linea:
        fallos.append("no hay bloque de medición del corte")
    elif not re.search(r"\d{1,2}:\d{2}", linea.group(1)):
        fallos.append("la medición del corte no dice la hora")
    # 4 · el día de la casa: la fecha larga de la cabecera y al menos una nota fechada
    #     con ESE día. Antes estaba clavado el 1 de noviembre; clavarlo obliga a editar
    #     el testigo cada día, que es la clase de trampa que este archivo no se permite.
    cabecera = re.search(r"(\d{1,2}) de (" + "|".join(MESES) + r")[a-z]* de (\d{4})",
                         t[:1500])
    if not cabecera:
        fallos.append("la cabecera no trae fecha larga del día de la casa")
        return fallos
    dia_num, mes, anio = cabecera.group(1), cabecera.group(2), cabecera.group(3)
    sello = f"({dia_num}-{mes})"
    if sello not in t:
        fallos.append(f"ninguna nota del corte lleva fecha del día de la casa {sello}")
    if anio not in t:
        fallos.append("la pieza no repite el año del corte")
    return fallos


def main() -> int:
    verificar = "--verificar" in sys.argv
    vivas, viejas = piezas()
    total = fallos = 0
    for p in vivas:
        total += 1
        f = revisar(p)
        if f:
            fallos += 1
            print(f"ROJO   {p.name[:70]}")
            for x in f:
                print(f"   ✗ {x}")
    print(f"FIRMA LITERAL · {total} piezas vivas · {total - fallos} en regla · "
          f"{fallos} con fallo · {viejas} del archivo viejo sin exigencia")
    return 1 if (verificar and fallos) else 0


if __name__ == "__main__":
    sys.exit(main())
