#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CUADRE · convierte un JSON de medición en prosa con los números escritos por código.

Qué hace:
  * Lee docs/MEDICION-PNN-<fecha>.json (lo que saca tools/elige.py del censo medido).
  * Calcula los agregados que una pieza cita: estrellas, mediana, cuántos publican huella,
    adjuntos, suma de descargas, quién es el más nuevo, el más viejo sin entrega, etc.
  * Imprime esas frases ya redactadas, para pegarlas en la pieza sin transcribir un número.

Qué NO hace:
  * No inventa: si un campo es null, escribe «aquí no hay» y sigue.
  * No redacta la pieza: solo los números. La voz de la pieza es aparte.
"""
from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def miles(n: int | None) -> str:
    if n is None:
        return "aquí no hay"
    return f"{n:,}".replace(",", ".")


def letras(n: int) -> str:
    """Número en palabras, en español dominicano, hasta millones."""
    unidades = ["cero", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
                "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
                "dieciocho", "diecinueve", "veinte"]
    if n <= 20:
        return unidades[n]
    if n < 30:  # veintiuno … veintinueve
        d, u = divmod(n, 10)
        return ["veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco",
                "veintiséis", "veintisiete", "veintiocho", "veintinueve"][u - 1]
    if n < 100:
        d, u = divmod(n, 10)
        decenas = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta",
                   8: "ochenta", 9: "noventa"}
        return decenas[d] + (f" y {unidades[u]}" if u else "")
    if n < 1000:
        c, r = divmod(n, 100)
        centenas = {1: "ciento", 2: "doscientas", 3: "trescientas", 4: "cuatrocientas",
                    5: "quinientas", 6: "seiscientas", 7: "setecientas", 8: "ochocientas",
                    9: "novecientas"}
        if n == 100:
            return "cien"
        return centenas[c] + (f" {letras(r)}" if r else "")
    if n < 1_000_000:
        m, r = divmod(n, 1000)
        pref = "mil" if m == 1 else f"{letras(m)} mil"
        return pref + (f" {letras(r)}" if r else "")
    m, r = divmod(n, 1_000_000)
    pref = "un millón" if m == 1 else f"{letras(m)} millones"
    return pref + (f" {letras(r)}" if r else "")


def cargar(pieza: str) -> dict:
    for p in sorted(RAIZ.glob(f"docs/MEDICION-P{pieza}-*.json")):
        return json.loads(p.read_text(encoding="utf-8"))
    raise SystemExit(f"no hay docs/MEDICION-P{pieza}-*.json: pasa primero tools/elige.py")


def agregados(d: dict) -> str:
    f = d["fichas"]
    n = len(f)
    estrellas = [x["stars"] for x in f if x["stars"] is not None]
    mediana = int(statistics.median(estrellas)) if estrellas else None
    huella = [x for x in f if (x["huellas_ultima"] or 0) > 0]
    adjuntos = sum(x["adjuntos_ultima"] or 0 for x in f)
    descargas = sum(x["descargas_ultima"] or 0 for x in f)
    sin_lic = [x for x in f if not x["licencia"]]
    nuevos = sorted([x for x in f if x["dias_nace"] is not None], key=lambda x: x["dias_nace"])
    activos = [x for x in f if x["dias_push"] is not None and x["dias_push"] <= 7]
    sin_entrega = [x for x in f if not x["ultima_entrega"]]
    top = max(f, key=lambda x: x["stars"] or 0)
    menos = min(f, key=lambda x: x["stars"] or 0)
    l = []
    l.append(f"pieza {d['pieza']} · {letras(n)} repositorios medidos el 9 de noviembre de 2026 contra la API pública de GitHub")
    l.append(f"estrellas: {miles(sum(estrellas))} ({letras(sum(estrellas))}) · mediana {miles(mediana)}")
    l.append(f"publican huella: {letras(len(huella))} de {letras(n)} · adjuntos en la última entrega {miles(adjuntos)} · descargas sumadas de última entrega {miles(descargas)}")
    l.append(f"sin licencia declarada: {letras(len(sin_lic))} · con push en los últimos 7 días: {letras(len(activos))} · sin ninguna entrega publicada: {letras(len(sin_entrega))}")
    if nuevos:
        j = nuevos[0]
        l.append(f"el más nuevo: {j['repo']} · {letras(j['dias_nace'])} días · ★{miles(j['stars'])} · entrega {j['ultima_entrega'] or 'aquí no hay'}")
    l.append(f"el que más estrellas tiene: {top['repo']} · ★{miles(top['stars'])} · nació hace {miles(top['dias_nace'])} días")
    l.append(f"el que menos: {menos['repo']} · ★{miles(menos['stars'])} · nació hace {miles(menos['dias_nace'])} días")
    if huella:
        l.append("los que firman, uno por uno:")
        for x in sorted(huella, key=lambda y: -(y["huellas_ultima"] or 0)):
            l.append(f"   · {x['repo']} — {miles(x['huellas_ultima'])} sumas de {miles(x['adjuntos_ultima'])} adjuntos · entrega {x['ultima_entrega']}")
    else:
        l.append("los que firman: aquí no hay")
    return "\n".join(l)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    pieza = argv[1].zfill(2)
    print(agregados(cargar(pieza)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
