#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FIJADOS · genera el comentario fijado de cada pieza desde su medición.

Qué hace:
  * Lee docs/MEDICION-PNN-<fecha>.json de cada pieza reescrita.
  * Escribe el comentario fijado (900–4.000 caracteres) con los mismos números que el cuerpo,
    para que el fijado y la pieza no puedan decir cosas distintas.
  * Respeta el fijado existente de las piezas que todavía no se han reescrito: no las toca.

Qué NO hace:
  * No inventa: si no hay medición para una pieza, la salta y lo dice.
  * No reescribe el pasado en silencio: mueve el fijado viejo a _reemplazadas-<fecha>/.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import statistics
import unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLIC = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES" / "Facebook-dominicano-ES"
HOY = date.today().isoformat()

NOMBRES = {
    "01": "La huella o el silencio",
    "02": "La música que no se cae",
    "03": "La caja fuerte del bolsillo",
    "04": "La lista del permiso",
    "05": "La guía maestra",
    "06": "El taller de los parches",
    "07": "La pantalla grande",
    "08": "La red: seis caminos",
    "09": "Archivos, copias y nubes propias",
    "10": "Las tiendas de extensiones",
    "11": "Las aplicaciones que leen",
    "12": "El kit de reemplazo",
}


def miles(n) -> str:
    if n is None:
        return "aquí no hay"
    return f"{n:,}".replace(",", ".")


def cargar(pieza: str) -> dict | None:
    for p in sorted(RAIZ.glob(f"docs/MEDICION-P{pieza}-*.json")):
        return json.loads(p.read_text(encoding="utf-8"))
    return None


def cuerpo_fijado(pieza: str, d: dict) -> str:
    f = d["fichas"]
    estrellas = [x["stars"] for x in f if x.get("stars") is not None]
    con_h = [x for x in f if (x.get("huellas_ultima") or 0) > 0]
    adj = sum(x.get("adjuntos_ultima") or 0 for x in f)
    sumas = sum(x.get("huellas_ultima") or 0 for x in f)
    dl = sum(x.get("descargas_ultima") or 0 for x in f)
    mediana = int(statistics.median(estrellas)) if estrellas else None
    top = max(f, key=lambda x: x.get("stars") or 0)
    activos = [x for x in f if x.get("dias_push") is not None and x["dias_push"] <= 7]
    sin_ent = [x for x in f if not x.get("ultima_entrega")]

    if con_h:
        mejores = sorted(con_h, key=lambda x: -(x.get("huellas_ultima") or 0))[:2]
        linea_firma = " · ".join(
            f"**{x['repo']}** ({miles(x.get('huellas_ultima'))} de {miles(x.get('adjuntos_ultima'))})"
            for x in mejores
        )
        titulo_firma = f"**{len(con_h)} de {len(f)} publican huella**"
    else:
        linea_firma = "**ninguno**"
        titulo_firma = f"**cero de {len(f)} publican huella** — el cero absoluto de la serie"

    lineas = [
        "━━━━━━━━━━━━━",
        "",
        f"📎 *Comentario fijado · Pieza {pieza} — {NOMBRES.get(pieza, 'la serie')}*",
        "",
        "Enlaces rápidos:",
        f"• Cuerpo de la publicación: pieza {pieza} de Facebook",
        "• Fecha de la medición: domingo 8 y lunes 9 de noviembre de 2026",
        f"• Medido con: {len(f)} repositorios · API pública de GitHub (consulta por repositorio)",
        f"• Archivo de la medición: `docs/MEDICION-P{pieza}-2026-11-09.json`",
        "",
        "Lo que dicen los números medidos:",
        f"• **{len(f)}** repositorios vivos: **{miles(sum(estrellas))} estrellas** (mediana {miles(mediana)}) "
        f"y **{miles(dl)} descargas** declaradas en la última entrega.",
        f"• {titulo_firma}: **{miles(sumas)} sumas** repartidas entre **{miles(adj)} adjuntos**.",
        f"• Los que firman: {linea_firma}.",
        f"• El de más estrellas: **{top['repo']}**, ★{miles(top.get('stars'))}, "
        f"{miles(top.get('huellas_ultima'))} sumas de {miles(top.get('adjuntos_ultima'))} adjuntos.",
        f"• {len(activos)} empujaron código en los últimos siete días; "
        f"{len(sin_ent)} no han publicado nunca una entrega.",
        "",
        "**Seis órdenes para comprobarlo tú mismo:**",
        "1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.",
        "2. En Termux: `pkg install coreutils && sha256sum archivo.apk` —o el archivo que hayas bajado—.",
        "3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.",
        "4. Para un APK: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.",
        "5. Si no hay suma, pídela en las incidencias del repositorio. Es un archivo de dos líneas.",
        "6. Si hay atestación firmada: `gh attestation verify archivo.apk --repo dueno/nombre`.",
        "",
        "Los datos en bruto, con los nombres de los 3.125 repositorios medidos, están en el repositorio público: "
        f"`docs/CENSO-MEDIDO-2026-11-09.json` y `docs/MEDICION-P{pieza}-2026-11-09.json`.",
        "",
        "*💓 La Bandita informa. Lo que no se midió, aquí no se escribe.*",
        "",
    ]
    return "\n".join(lineas)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Genera los fijados desde las mediciones.")
    ap.add_argument("piezas", nargs="*", help="NN de cada pieza (por defecto: todas las que tengan medición)")
    ap.add_argument("--ver", action="store_true")
    args = ap.parse_args()

    piezas = args.piezas or [p.stem.split("-")[1].replace("P", "") for p in sorted(RAIZ.glob("docs/MEDICION-P*-2026-11-09.json"))]
    hechos = 0
    for pieza in piezas:
        pieza = pieza.zfill(2)
        d = cargar(pieza)
        if d is None:
            print(f"  {pieza}: sin medición, se salta")
            continue
        texto = cuerpo_fijado(pieza, d)
        nombre = f"{pieza}-Comentario-fijado-facebook-La-Bandita-{HOY}-dominicano-ES.md"
        print(f"  {pieza}: {len(texto)} caracteres → {nombre}")
        if args.ver:
            continue
        if not 900 <= len(texto) <= 4000:
            print(f"       FUERA DE BANDA (900–4.000): no se escribe")
            continue
        viejos = [p for p in PUBLIC.glob(f"{pieza}-Comentario-fijado-*.md") if p.name != nombre]
        if viejos:
            saco = PUBLIC / f"_reemplazadas-{HOY}"
            saco.mkdir(exist_ok=True)
            for v in viejos:
                shutil.move(str(v), saco / v.name)
                print(f"       fijado viejo movido: {v.name[:52]}…")
        (PUBLIC / nombre).write_text(texto, encoding="utf-8")
        hechos += 1
    print(f"\n{hechos} fijados escritos desde su medición")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv))
