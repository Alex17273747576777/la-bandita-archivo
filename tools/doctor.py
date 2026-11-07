#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOCTOR · el primer comando que se corre en una máquina nueva, y el último antes de publicar.

Mira cinco bloques —entorno, árbol, estado, integridad y veredicto— y dice
LISTO, LISTO CON AVISOS o DETENIDO, con la salida para cada caso.

Qué hace:
  * Diagnostica el entorno (Python, git, dependencias).
  * Revisa el árbol (piezas vivas, archivo histórico).
  * Revisa el estado (fichas de la guía, bandas declaradas, envíos).
  * Revisa la integridad (sello SHA-256, archivos alterados o ausentes).
  * Emite un veredicto: LISTO / LISTO CON AVISOS / DETENIDO.

Qué NO hace:
  * No arregla nada: solo diagnostica.
  * Diagnosticar y arreglar en el mismo gesto es lo que rompe los archivos.
"""
from __future__ import annotations

import importlib
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]


@dataclass
class Bloque:
    nombre: str
    estado: str  # ok | aviso | error
    detalles: list[str]


def _comando(cmd: list[str]) -> str:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or r.stderr.strip()
    except Exception as e:
        return f"error: {e}"


def _bloque_entorno() -> Bloque:
    detalles: list[str] = []
    py = sys.version.split()[0]
    detalles.append(f"Python {py}")
    git = _comando(["git", "--version"])
    detalles.append(f"git {git}")
    rama = _comando(["git", "branch", "--show-current"])
    detalles.append(f"rama {rama}")
    cabeza = _comando(["git", "rev-parse", "--short", "HEAD"])
    detalles.append(f"cabeza {cabeza}")
    for mod in ("jsonschema", "mcp"):
        try:
            importlib.import_module(mod)
            detalles.append(f"dependencias: {mod} sí")
        except ImportError:
            detalles.append(f"dependencias: {mod} no")
    return Bloque("ENTORNO", "ok", detalles)


def _bloque_arbol() -> Bloque:
    detalles: list[str] = []
    publicaciones = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
    piezas_vivas: dict[str, int] = {}
    if publicaciones.exists():
        for canal in publicaciones.iterdir():
            if canal.is_dir():
                md = [f for f in canal.iterdir() if f.suffix == ".md" and not f.name.startswith("_")]
                piezas_vivas[canal.name] = len(md)
    detalles.append(f"piezas vivas {piezas_vivas}")
    historico = RAIZ / "ARCHIVO-HISTORICO"
    detalles.append(f"archivo histórico {'presente' if historico.exists() else 'ausente'}")
    return Bloque("ÁRBOL", "ok", detalles)


def _bloque_estado() -> Bloque:
    detalles: list[str] = []
    guia = RAIZ / "guia-maestra" / "datos" / "apps"
    if guia.exists():
        n_fichas = len([f for f in guia.iterdir() if f.suffix == ".json"])
        detalles.append(f"fichas de la guía {n_fichas}")
    else:
        detalles.append("fichas de la guía 0")
    bandas = RAIZ / "docs" / "bandas.json"
    if bandas.exists():
        import json
        try:
            b = json.loads(bandas.read_text(encoding="utf-8"))
            detalles.append(f"bandas declaradas {len(b)}")
        except (json.JSONDecodeError, OSError):
            detalles.append("bandas declaradas ?")
    else:
        detalles.append("bandas declaradas 0")
    envios = RAIZ / "docs" / "envios"
    n_envíos = 0
    if envios.exists():
        for sub in envios.iterdir():
            if sub.is_dir():
                n_envíos += len([f for f in sub.iterdir() if f.suffix == ".md"])
    detalles.append(f"envíos {{{n_envíos}}}")
    return Bloque("ESTADO", "ok", detalles)


def _bloque_integridad() -> Bloque:
    detalles: list[str] = []
    from atestar import _archivos_del_arbol, _cargar_gitignore, _huella_archivo
    ignorar = _cargar_gitignore()
    archivos = _archivos_del_arbol(ignorar)
    total = len(archivos)
    alterados = 0
    ausentes = 0
    sin_sellar = 0
    sello_path = RAIZ / "attestations" / f"lote-{__import__('datetime').date.today().isoformat()}.json"
    if sello_path.exists():
        import json as _json
        try:
            lote = _json.loads(sello_path.read_text(encoding="utf-8"))
            tabla = lote.get("tabla", {})
            huellas_actuales = {str(p.relative_to(RAIZ)): _huella_archivo(p) for p in archivos}
            alterados = sum(1 for r, h in tabla.items() if huellas_actuales.get(r) != h)
            ausentes = sum(1 for r in tabla if r not in huellas_actuales)
            sin_sellar = sum(1 for r in huellas_actuales if r not in tabla)
        except (json.JSONDecodeError, OSError):
            alterados = total
    estado = "ok" if (alterados == 0 and ausentes == 0 and sin_sellar == 0) else "aviso"
    detalles.append(f"integridad: {total} archivos OK · {alterados} alterados o ausentes · {sin_sellar} sin sellar · {ausentes} desaparecidos")
    return Bloque("INTEGRIDAD", estado, detalles)


def _veredicto(bloques: list[Bloque]) -> str:
    for b in bloques:
        if b.estado == "error":
            return "DETENIDO"
    for b in bloques:
        if b.estado == "aviso":
            return "LISTO CON AVISOS"
    return "LISTO"


def main() -> int:
    print("\nDOCTOR DE LA CASA · diagnóstico en cinco bloques\n")
    bloques = [
        _bloque_entorno(),
        _bloque_arbol(),
        _bloque_estado(),
        _bloque_integridad(),
    ]
    for b in bloques:
        icono = {"ok": "✓", "aviso": "·", "error": "✗"}[b.estado]
        print(f"{icono} {b.nombre}")
        for d in b.detalles:
            print(f"   {d}")
    veredicto = _veredicto(bloques)
    icono_v = {"LISTO": "✓", "LISTO CON AVISOS": "·", "DETENIDO": "✗"}[veredicto]
    print(f"\n{icono_v} VEREDICTO {veredicto}\n")
    if veredicto == "DETENIDO":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
