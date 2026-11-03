#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOCTOR · el primer comando que se corre en una máquina nueva, y el último antes de publicar.

Un repositorio de este tamaño se vuelve hostil cuando nadie sabe por dónde empezar:
treinta herramientas, diez mil archivos sellados y quince compuertas. El doctor no
arregla nada —arreglar sin diagnóstico es lo que rompe los archivos—, solo mira y
dice, en cinco bloques, si esta máquina puede trabajar y en qué estado está el árbol.

Qué mira:
  1. Entorno   · versión de Python, dependencias, git y su configuración mínima.
  2. Árbol     · existencia de las carpetas y archivos que todo lo demás da por hechos.
  3. Estado    · piezas vivas, bandas declaradas, tareas y envíos.
  4. Integridad· si el sello SHA-256 está al día o si alguien tocó algo sin re-sellar.
  5. Veredicto · LISTO, LISTO CON AVISOS o DETENIDO, con la salida para cada caso.

Uso:
    python3 tools/doctor.py           # informe humano
    python3 tools/doctor.py --json    # informe legible por máquina
    python3 tools/doctor.py --breve   # solo el veredicto y los fallos
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLICACIONES = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
CANALES = ("Facebook-dominicano-ES", "WhatsApp-dominicano-ES")

ESENCIALES = (
    "README.md", "MAPA-DEL-ARCHIVO.md", "ARQUITECTURA.md", "Makefile",
    "tools/vara.py", "tools/atestar.py", "tools/manual_gate.py", "tools/novedad_gate.py",
    "tools/envio.py", "tools/tareas.py", "tools/indice_docs.py",
    "docs/bandas.json", "guia-maestra/datos/capitulos.json", "registry", "schemas",
)


def bloque_entorno() -> dict:
    r = {"python": sys.version.split()[0], "python_ok": sys.version_info >= (3, 10)}
    for modulo in ("jsonschema", "mcp"):
        try:
            __import__(modulo)
            r[modulo] = True
        except Exception:
            r[modulo] = False
    try:
        git = subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
        r["git"] = git.stdout.strip()
    except Exception:
        r["git"] = ""
    try:
        dentro = subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "--is-inside-work-tree"],
                                capture_output=True, text=True, check=True).stdout.strip()
        rama = subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "--abbrev-ref", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
        r["git_arbol"] = dentro == "true"
        r["rama"] = rama
        r["head"] = subprocess.run(["git", "-C", str(RAIZ), "rev-parse", "--short", "HEAD"],
                                   capture_output=True, text=True, check=True).stdout.strip()
        r["sucio"] = bool(subprocess.run(["git", "-C", str(RAIZ), "status", "--porcelain"],
                                         capture_output=True, text=True).stdout.strip())
    except Exception:
        r["git_arbol"] = False
    return r


def bloque_arbol() -> dict:
    faltan = [x for x in ESENCIALES if not (RAIZ / x).exists()]
    canales = {c: len([p for p in (PUBLICACIONES / c).glob("*.md")
                       if not p.name.lower().startswith(("leeme", "readme"))])
               for c in CANALES if (PUBLICACIONES / c).exists()}
    return {"faltan": faltan, "piezas_vivas": canales,
            "archivo_historico": (RAIZ / "ARCHIVO-HISTORICO").exists()}


def bloque_estado() -> dict:
    bandas = RAIZ / "docs" / "bandas.json"
    declaradas = 0
    if bandas.exists():
        d = json.loads(bandas.read_text(encoding="utf-8"))
        declaradas = sum(len((c.get("piezas") or {})) for c in d.values() if isinstance(c, dict))
    envios = {c: len(list((RAIZ / "docs" / "envios" / c.replace("-dominicano-ES", "")).glob("*.md")))
              for c in CANALES if (RAIZ / "docs" / "envios" / c.replace("-dominicano-ES", "")).exists()}
    tareas = RAIZ / "docs" / "TAREAS.md"
    indice = RAIZ / "docs" / "INDICE.md"
    caps = RAIZ / "guia-maestra" / "datos" / "apps"
    return {"bandas_declaradas": declaradas, "envios": envios,
            "tablero_tareas": tareas.exists(), "indice_docs": indice.exists(),
            "fichas_guia": len(list(caps.glob("*.json"))) if caps.exists() else 0}


def bloque_integridad() -> dict:
    """Se pregunta al sello, no se recalcula: el doctor informa, no re-sella."""
    try:
        p = subprocess.run([sys.executable, str(RAIZ / "tools" / "atestar.py"), "--verificar"],
                           capture_output=True, text=True, cwd=RAIZ, timeout=900)
        salida = (p.stdout + p.stderr).strip().splitlines()
        return {"ok": p.returncode == 0, "detalle": salida[-2:] if salida else []}
    except Exception as e:  # pragma: no cover - solo si git o python fallan
        return {"ok": False, "detalle": [f"no se pudo comprobar: {e}"]}


def main() -> int:
    ap = argparse.ArgumentParser(description="Diagnóstico de entorno y estado del archivo.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--breve", action="store_true")
    a = ap.parse_args()

    entorno, arbol, estado = bloque_entorno(), bloque_arbol(), bloque_estado()
    integridad = bloque_integridad()

    fallos, avisos = [], []
    if not entorno["python_ok"]:
        fallos.append(f"Python {entorno['python']}: hace falta 3.10 o posterior")
    if not entorno.get("git_arbol"):
        fallos.append("no es un árbol de git: las compuertas de integridad no pueden correr")
    if arbol["faltan"]:
        fallos.append("faltan piezas esenciales: " + ", ".join(arbol["faltan"]))
    if not integridad["ok"]:
        avisos.append("el sello SHA-256 no cuadra: alguien tocó el árbol sin re-sellar (make sellar)")
    for modulo in ("jsonschema", "mcp"):
        if not entorno.get(modulo):
            avisos.append(f"falta la dependencia «{modulo}» (pip install {modulo}) — la CI la tiene")
    if entorno.get("sucio"):
        avisos.append("hay cambios sin confirmar en el árbol de trabajo")
    if not estado["tablero_tareas"] or not estado["indice_docs"]:
        avisos.append("faltan documentos derivados: corré «make libro»")

    veredicto = "DETENIDO" if fallos else ("LISTO CON AVISOS" if avisos else "LISTO")

    if a.json:
        print(json.dumps({"veredicto": veredicto, "fallos": fallos, "avisos": avisos,
                          "entorno": entorno, "arbol": arbol, "estado": estado,
                          "integridad": integridad}, ensure_ascii=False, indent=1))
        return 0 if not fallos else 1

    if not a.breve:
        print("\nDOCTOR DE LA CASA · diagnóstico en cinco bloques\n")
        print(f"1 · ENTORNO    Python {entorno['python']} · {entorno.get('git', 'sin git')} · "
              f"rama {entorno.get('rama', '?')} · cabeza {entorno.get('head', '?')}")
        dep = " · ".join(f"{m} {'sí' if entorno.get(m) else 'no'}" for m in ("jsonschema", "mcp"))
        print(f"                dependencias: {dep}")
        print(f"2 · ÁRBOL      piezas vivas {arbol['piezas_vivas']} · archivo histórico "
              f"{'presente' if arbol['archivo_historico'] else 'AUSENTE'}")
        print(f"3 · ESTADO     fichas de la guía {estado['fichas_guia']} · bandas declaradas "
              f"{estado['bandas_declaradas']} · envíos {estado['envios']}")
        print(f"4 · INTEGRIDAD {'sello al día' if integridad['ok'] else 'sello roto'}"
              + (f" · {integridad['detalle'][-1][:70]}" if integridad["detalle"] else ""))
        print(f"5 · VEREDICTO  {veredicto}\n")
    else:
        print(f"VEREDICTO  {veredicto}")

    for f in fallos:
        print(f"  ✗ {f}")
    for x in avisos:
        print(f"  · {x}")
    if not fallos and not avisos:
        print("  nada que corregir: make verificar")
    return 0 if not fallos else 1


if __name__ == "__main__":
    raise SystemExit(main())
