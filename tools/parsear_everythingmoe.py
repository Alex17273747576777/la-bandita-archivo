#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parser de EverythingMoe · lee las secciones guardadas y cuenta lo que hay de verdad.

Dos formas de bloque conviven en el HTML, y esto es lo que hacía que un primer
intento contara 84 entradas donde hay 91:

    <div data-rank="1" data-filter="Android, Manga" class="section-item">   ← con filtros
    <div data-rank="1" class="section-item">                                ← sin filtros

Dos trampas que costaron dos intentos fallidos:

  * El `data-filter` es **opcional**: si el patrón lo exige, se pierden en silencio las
    entradas de las secciones que no filtran (novela, herramientas).
  * La clase puede ser `class="section-item section-licensed"`: si el patrón exige
    `class="section-item"` cerrado, se pierden las 7 licenciadas de apps, 8 de anime y 11
    de manga. Aquí la clase acepta sufijo.

Números medidos con este parser: apps 91 · anime 110 · manga 96 · novela 64 ·
herramientas 33 · utils 3.
"""
import html
import json
import pathlib
import re

AQUI = pathlib.Path(__file__).resolve().parent
RE_BLOQUE = re.compile(r'<div data-rank="(\d+)"(?:\s+data-filter="([^"]*)")?\s+class="section-item[^"]*">')
RE_ENLACE = re.compile(r'<a href="([^"]+)"(?:\s+data-link="([^"]+)")?[^>]*>(.*?)</a>', re.S)


def parsear(path: pathlib.Path, seccion: str) -> list[dict]:
    h = path.read_text(encoding="utf-8", errors="ignore")
    trozos = [(m.start(), m.group(1), m.group(2)) for m in RE_BLOQUE.finditer(h)]
    salida = []
    for i, (pos, rank, filtros) in enumerate(trozos):
        fin = trozos[i + 1][0] if i + 1 < len(trozos) else len(h)
        bloque = h[pos:fin]
        a = RE_ENLACE.search(bloque)
        if not a:
            continue
        salida.append({
            "rank": int(rank),
            "nombre": html.unescape(re.sub(r"<[^>]+>", "", a.group(3)).strip()),
            "emo": a.group(1),
            "web": a.group(2),
            "filtros": [f.strip() for f in (filtros or "").split(",") if f.strip()],
            "seccion": seccion,
        })
    return salida


def main() -> None:
    todo = {}
    for f in sorted(AQUI.glob("*.html")):
        if f.stem in ("index",):
            continue
        todo[f.stem] = parsear(f, f.stem)
        print(f"{f.stem:8} {len(todo[f.stem]):3} entradas")
    total = sum(len(v) for v in todo.values())
    (AQUI / "emo-parseado.json").write_text(
        json.dumps(todo, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\ntotal: {total} entradas en {len(todo)} secciones")


if __name__ == "__main__":
    main()
