#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REFERENCIAS · comprueba que ninguna carpeta movida siga citada por su ruta vieja.

Cuando se mueve una carpeta con `git mv`, git mueve los archivos y **no** toca una sola
línea de los documentos que la citan. El árbol queda con rutas que ya no existen y nadie
se entera hasta que alguien las sigue. Ese es exactamente el error que produjo el desorden
anterior, así que aquí está la comprobación que lo impide.

Cómo distingue lo que hay que arreglar de lo que hay que dejar quieto:

- **Vivo**: lo que se lee o se ejecuta hoy — la raíz, `docs/`, `tools/`, `.github/`,
  la guía, el registro y lo publicado en los canales.
- **Histórico**: lo que se conserva como evidencia de lo que se hizo — `ARCHIVO-HISTORICO/`,
  `02-ARCHIVO/`, las entregas y las actas. Un documento histórico que se reescribe deja de
  servir como prueba: se conserva con su ruta de su día y este mapa la traduce.

Una ruta vieja citada por un archivo **vivo** es un fallo (código 1).
Una ruta vieja citada por un archivo **histórico** es una cita: se cuenta y se informa.

Qué recibe: el árbol del repositorio y la tabla `MOVED` de abajo.
Qué produce: un informe en la salida estándar, y con `--json` el mismo informe legible por
máquina. No escribe ni mueve nada.
Qué no hace: no corrige. Corregir una ruta exige saber qué quería decir la frase que la
cita, y eso no lo sabe un programa.

Uso:
    python3 tools/referencias.py           # informe legible
    python3 tools/referencias.py --json    # el mismo informe, para la CI
    python3 tools/referencias.py --peor    # solo lo que falla (código 1 si hay algo)
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

# ─────────────────────────────────────────────────────────────────────────────
#  La tabla de mudanzas. Se añade una fila por cada carpeta que se mueva, y el
#  programa se encarga del resto: es el registro que hace reproducible la pasada.
#
#  Cada fila se escribe **como se cita en los documentos**: con el prefijo
#  `Arena-Reimagined/` cuando se cita desde la raíz y sin él cuando se cita desde
#  dentro. Las dos formas apuntan al mismo sitio y las dos hay que corregirlas.
# ─────────────────────────────────────────────────────────────────────────────
MOVED = (
    #  pasada del 2026-11-03 · Arena-Reimagined, la memoria a su sitio
    ("_versiones/", "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_versiones/"),
    ("packs/", "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/packs/"),
    ("_herramientas/", "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas/"),
    ("_herramientas-casa/",
     "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_herramientas-casa/"),
    ("_referencia/", "Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_referencia/"),
)

# Archivos exentos, con su razón. Un archivo entra aquí cuando **su oficio es citar la
# ruta vieja**: el mapa que la traduce, el acta que la cuenta y este mismo programa.
# Eximir sin razón es la forma más rápida de que una compuerta deje de servir.
EXENTOS = {
    "tools/referencias.py": "la tabla de mudanzas vive aquí",
    "tools/autoprueba.py": "fabrica la violación a propósito, para comprobar que G17 la detecta",
    "MAPA-DEL-ARCHIVO.md": "es el traductor de rutas: cita la vieja a propósito",
    "ARQUITECTURA.md": "cita la pasada como parte de su relato de decisiones",
    "README.md": "declara la deuda con su nombre",
    "CHANGELOG.md": "registra la mudanza por su nombre",
    "Arena-Reimagined/LEEME-ESTRUCTURA.md": "es el mapa de esa carpeta: nombra la mudanza para explicarla",
}

# Prefijos que hoy se leen o se ejecutan. Si un archivo de aquí cita una ruta vieja,
# la compuerta se detiene: alguien va a seguir ese enlace y no va a encontrar nada.
VIVOS = (
    "docs/", "tools/", ".github/", "guia-maestra/", "registry/", "schemas/",
    "CIMIENTOS/", "PROCESOS/", "SKILLS/", "LEGAL/", "corpus-la-bandita/",
    "Arena-Reimagined/01-PUBLICACIONES/", "Arena-Reimagined/PROPUESTA-2026-10-31/",
    "mcp-labandita-registro/",
)
VIVOS_RAIZ = {"README.md", "MAPA-DEL-ARCHIVO.md", "ARQUITECTURA.md", "CHANGELOG.md",
              "CONTRIBUTING.md", "SECURITY.md", "SUPPORT.md", "CODE_OF_CONDUCT.md",
              "Makefile", "LEEME-ESTRUCTURA.md"}

# Lo que se conserva como prueba: se cita, no se reescribe.
HISTORICOS = ("ARCHIVO-HISTORICO/", "Arena-Reimagined/02-ARCHIVO/",
              "Arena-Reimagined/00-CANON/", "Arena-Reimagined/ENTREGA-29OCT-2026/",
              "Arena-Reimagined/ENTREGA", "Arena-Reimagined/HABILIDADES/")

# Un documento fechado en el nombre es una firma: el acta del día tal como se firmó.
# No se retoca para que diga otra cosa; si cambió el estado, lo dice el documento de hoy.
FIRMADO = re.compile(r"-20\d\d-\d\d-\d\d")

SUFIJOS = {".md", ".py", ".json", ".tsv", ".yml", ".yaml", ".txt", ".html", ".sh",
           ".js", ".xhtml", ".gitignore"}


def es_vivo(rel: str) -> bool:
    return rel in VIVOS_RAIZ or rel.endswith(".gitignore") or rel.startswith(VIVOS)


def es_historico(rel: str) -> bool:
    return rel.startswith(HISTORICOS) or bool(FIRMADO.search(rel.rsplit("/", 1)[-1]))


def archivos() -> list[Path]:
    salida = []
    for p in sorted(RAIZ.rglob("*")):
        if not p.is_file() or ".git" in p.parts:
            continue
        rel = p.relative_to(RAIZ).as_posix()
        # El destino de la mudanza cita sus propias rutas: no se audita a sí mismo.
        if rel.startswith("Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/"):
            continue
        if p.suffix not in SUFIJOS and p.name != ".gitignore":
            continue
        salida.append(p)
    return salida


def auditar() -> dict:
    # Se busca el nombre de la carpeta en cualquier posición, con o sin el prefijo
    # `Arena-Reimagined/`, pero **no** dentro de la ruta nueva (que contiene el viejo
    # como sufijo): para eso se mira que no venga precedido de `_etapas-anteriores/`.
    patrones = [(re.compile(r"(?<!_etapas-anteriores/)" + re.escape(vieja)), vieja, nueva)
                for vieja, nueva in MOVED]
    fallos: list[dict] = []       # rutas viejas citadas por archivos vivos
    citas: dict[str, int] = {}    # rutas viejas citadas por archivos históricos
    detalle_historicos: list[dict] = []
    vivos_revisados = 0

    for p in archivos():
        rel = p.relative_to(RAIZ).as_posix()
        try:
            texto = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if rel in EXENTOS:
            continue
        if es_vivo(rel):
            vivos_revisados += 1
        for patron, vieja, nueva in patrones:
            if not patron.search(texto):
                continue
            if es_historico(rel):
                # Se consulta primero lo histórico: un acta firmada dentro de `docs/`
                # sigue siendo un acta, aunque `docs/` sea carpeta viva.
                citas[vieja] = citas.get(vieja, 0) + texto.count(vieja)
                detalle_historicos.append({"archivo": rel, "cita": vieja})
            elif es_vivo(rel):
                for n, linea in enumerate(texto.splitlines(), 1):
                    if patron.search(linea):
                        fallos.append({"archivo": rel, "linea": n,
                                       "cita": vieja, "destino": nueva,
                                       "texto": linea.strip()[:160]})
            else:
                # Ni vivo ni histórico declarado: se trata como vivo. Ante la duda,
                # que se detenga la línea y alguien decida, en vez de pasar de largo.
                fallos.append({"archivo": rel, "linea": 0, "cita": vieja,
                               "destino": nueva,
                               "texto": "(archivo sin clasificar: se trata como vivo)"})

    return {
        "mudanzas": len(MOVED),
        "vivos_revisados": vivos_revisados,
        "fallos": fallos,
        "citas_historicas": citas,
        "archivos_historicos": len({d["archivo"] for d in detalle_historicos}),
        "veredicto": "SIN REFERENCIAS ROTAS" if not fallos else "REFERENCIAS ROTAS",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Busca rutas viejas citadas por archivos vivos.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--peor", action="store_true", help="solo los fallos")
    args = ap.parse_args()

    r = auditar()
    if args.json:
        # Con --json la salida es solo el informe: lo consume la compuerta G17 y un texto
        # humano pegado detrás rompería el lector.
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0 if not r["fallos"] else 1
    if args.peor:
        for f in r["fallos"]:
            print(f"✗ {f['archivo']}:{f['linea']} cita «{f['cita']}» → va a «{f['destino']}»")
        print(f"fallos: {len(r['fallos'])}")
        return 1 if r["fallos"] else 0

    print("REFERENCIAS · ¿alguna carpeta movida sigue citada por su ruta vieja?")
    print(f"mudanzas en la tabla: {r['mudanzas']} · archivos vivos revisados: {r['vivos_revisados']}")
    if r["fallos"]:
        print(f"\n✗ {len(r['fallos'])} referencias rotas en archivos vivos:")
        for f in r["fallos"]:
            print(f"  · {f['archivo']}:{f['linea']}  «{f['cita']}» → «{f['destino']}»")
            print(f"      {f['texto']}")
    else:
        print("\n✓ ninguna ruta vieja citada por un archivo vivo")
    if r["citas_historicas"]:
        print(f"\n· citas en documentos históricos (se conservan, se traducen): "
              f"{r['archivos_historicos']} archivos")
        for vieja, n in sorted(r["citas_historicas"].items()):
            print(f"    {vieja}  {n} citas")
    print(f"\nveredicto: {r['veredicto']}")
    return 1 if r["fallos"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
