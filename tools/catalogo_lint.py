#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""catalogo_lint.py · revisa las fichas del catálogo y dice cuáles se sostienen.

Doce comprobaciones que se pueden leer. No dicen si el programa es bueno: dicen si
la ficha es honesta, está fechada y no es la misma plantilla copiada 269 veces.

  C01 carpeta y archivo con el slug del repositorio
  C02 cabecera con racimo, repositorio y fecha de medición
  C03 bloque de medición con al menos cinco campos
  C04 licencia declarada (o «sin licencia declarada», que también es un dato)
  C05 fecha de medición válida y no futura
  C06 enlaces con el formato `- nombre: URL` y el del repositorio presente
  C07 sección «Qué no está verificado»
  C08 marcadores de guía y estado de la guía (escrita o pendiente)
  C09 sin tablas de Markdown
  C10 sin promesas imposibles ni superlativos de folleto
  C11 sin frases largas repetidas en más del 15 % de las fichas
  C12 una guía escrita tiene al menos tres apartados propios

Uso:
    python3 tools/catalogo_lint.py
    python3 tools/catalogo_lint.py --racimo shizuku-y-herederos
    python3 tools/catalogo_lint.py --json
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
PENDIENTE = "No hay guía escrita todavía"

SUPERLATIVOS = re.compile(
    r"\bimprescindible\b|\bla mejor\b|\bel mejor\b|100 ?%|infalible|garantizad|sin precedentes|revolucionari",
    re.I)


def fichas():
    for p in sorted(CATALOGO.glob("*/FICHA.md")):
        yield p.parent.name, p.read_text(encoding="utf-8")


def guia_de(t: str) -> str:
    m = re.search(re.escape(INICIO) + r"(.*?)" + re.escape(FIN), t, re.S)
    return m.group(1).strip() if m else ""


def frases_largas(fichas_txt: list[str]) -> Counter:
    c = Counter()
    for t in fichas_txt:
        vistas = set()
        for linea in t.splitlines():
            l = linea.strip()
            if len(l) < 120 or l.startswith("-") or l.startswith(">") or l.startswith("*"):
                continue
            vistas.add(l)
        c.update(vistas)
    return c


def revisar(solo: str | None):
    fallos, avisos, stats = [], [], {"total": 0, "guias": 0, "pendientes": 0}
    todas = list(fichas())
    contador = frases_largas([t for _, t in todas])
    tope_repeticion = max(3, int(len(todas) * 0.15))

    for carpeta, t in todas:
        med = re.search(r"\*\*Racimo:\*\* ([^·]+) · \*\*Repositorio:\*\* `([^`]+)`", t)
        if solo and (not med or med.group(1).strip() != solo):
            continue
        stats["total"] += 1
        nombre = med.group(2) if med else carpeta

        def f(codigo, detalle):
            fallos.append({"ficha": carpeta, "c": codigo, "detalle": detalle})

        # C01
        if med and carpeta != med.group(2).replace("/", "--").lower():
            f("C01", f"la carpeta no coincide con el repositorio ({nombre})")
        # C02
        if not med or "**Medido:**" not in t.split("\n## ")[0]:
            f("C02", "la cabecera no declara racimo, repositorio y fecha")
        # C03
        bloque = t.split("## Lo que se midió")
        campos = re.findall(r"^- \*\*", bloque[1].split("##")[0], re.M) if len(bloque) > 1 else []
        if len(campos) < 5:
            f("C03", f"bloque de medición con {len(campos)} campos (se piden 5)")
        # C04
        if "**Licencia:**" not in t:
            f("C04", "sin línea de licencia")
        # C05
        m = re.search(r"\*\*Medido:\*\* (\d{4}-\d{2}-\d{2})", t)
        if not m:
            f("C05", "sin fecha de medición")
        else:
            try:
                if date.fromisoformat(m.group(1)) > date(2026, 11, 5):
                    f("C05", "fecha de medición futura")
            except ValueError:
                f("C05", "fecha de medición ilegible")
        # C06
        enlaces = re.findall(r"^- ([^:]+): (https?://\S+)$", t, re.M)
        if not enlaces:
            f("C06", "sin enlaces con formato `- nombre: URL`")
        elif not any("github.com/" + nombre in u for _, u in enlaces):
            f("C06", "falta el enlace al repositorio")
        # C07
        if "## Qué no está verificado" not in t:
            f("C07", "sin sección de lo no verificado")
        # C08 / C12
        g = guia_de(t)
        if not g:
            f("C08", "sin bloque de guía")
        elif g.startswith(PENDIENTE) or PENDIENTE in g:
            stats["pendientes"] += 1
        else:
            stats["guias"] += 1
            if len(re.findall(r"^### ", g, re.M)) < 3:
                f("C12", "guía escrita con menos de tres apartados propios")
        # C09
        if re.search(r"^\|.*\|.*\|$", t, re.M):
            f("C09", "tiene una tabla de Markdown (en un teléfono no se lee)")
        # C10
        # las comillas del autor —descripción, cita del README— no son prosa propia
        propio = "\n".join(l for l in t.splitlines()
                           if not l.strip().startswith((">", "*"))
                           and "Lo que dice su propio texto" not in l)
        m = SUPERLATIVOS.search(propio)
        if m:
            f("C10", f"superlativo de folleto: «{m.group(0)}»")
        # C11
        for linea in t.splitlines():
            l = linea.strip()
            if len(l) >= 120 and contador[l] > tope_repeticion:
                f("C11", f"frase repetida en {contador[l]} fichas: «{l[:60]}…»")
                break

    return fallos, stats


def main() -> int:
    solo = sys.argv[sys.argv.index("--racimo") + 1] if "--racimo" in sys.argv else None
    fallos, stats = revisar(solo)

    if "--json" in sys.argv:
        print(json.dumps({"fallos": fallos, "stats": stats}, ensure_ascii=False, indent=1))
        return 1 if fallos else 0

    print(f"CATÁLOGO · {stats['total']} fichas · {stats['guias']} con guía escrita · "
          f"{stats['pendientes']} esperando guía")
    por_codigo = Counter(f["c"] for f in fallos)
    for f in fallos[:40]:
        print(f"  ✗ {f['c']} {f['ficha']}: {f['detalle']}")
    if len(fallos) > 40:
        print(f"  … y {len(fallos) - 40} más")
    if por_codigo:
        print("resumen:", ", ".join(f"{k}×{v}" for k, v in sorted(por_codigo.items())))
    print(f"fallos: {len(fallos)}")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
