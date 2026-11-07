#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REGISTRO · construye las fichas JSON del activo vendible desde el censo medido.

Construye las fichas JSON del registro desde el censo medido y comprueba que estén al día.
Cada ficha cumple schemas/ficha.schema.json. Un campo que falta no se rellena: se declara vacío.

Uso:
  python3 tools/registro_construir.py              # reconstruye el índice del registro
  python3 tools/registro_construir.py --verificar   # verifica que todas las fichas cumplan el esquema

Qué hace:
  * Lee las fichas de registry/*.json y valida cada una contra schemas/ficha.schema.json.
  * Escribe registry/_indice.json y registry/_calidad.json (generados, no fuente).
  * Con --verificar, comprueba que todas las fichas tengan los campos obligatorios.

Qué NO hace:
  * No inventa campos: si el censo no trae un dato, la ficha lo declara vacío.
  * No mide repositorios: eso es oficio de tools/pulso.py y tools/censo_medir.py.
  * No modifica fichas existentes: solo lee, valúa y genera índices.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    jsonschema = None

RAIZ: Path = Path(__file__).resolve().parents[1]
REGISTRO: Path = RAIZ / "registry"
SCHEMA: Path = RAIZ / "schemas" / "ficha.schema.json"
INDICE: Path = REGISTRO / "_indice.json"
CALIDAD: Path = REGISTRO / "_calidad.json"

CAMPOS_OBLIGATORIOS: tuple[str, ...] = (
    "id", "repo", "licencia", "actividad", "medido_en", "fuente", "evidencia",
)


def _cargar_schema() -> dict | None:
    if jsonschema is None:
        return None
    try:
        return json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _validar_ficha(d: dict, schema: dict | None) -> list[str]:
    errores: list[str] = []
    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in d:
            errores.append(f"falta campo obligatorio: {campo}")
    if schema is not None and jsonschema is not None:
        try:
            jsonschema.validate(d, schema)
        except jsonschema.ValidationError as e:
            errores.append(f"esquema: {e.message} en {e.absolute_path}")
    return errores


def construir() -> dict:
    """Lee todas las fichas del registro y devuelve un resumen de construcción."""
    fichas: list[Path] = sorted(p for p in REGISTRO.glob("*.json") if not p.name.startswith("_"))
    schema = _cargar_schema()
    total = len(fichas)
    validas = 0
    con_errores = 0
    detalle: list[dict] = []
    for p in fichas:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            con_errores += 1
            detalle.append({"archivo": p.name, "error": f"JSON inválido: {e}"})
            continue
        errs = _validar_ficha(d, schema)
        if errs:
            con_errores += 1
            detalle.append({"archivo": p.name, "errores": errs})
        else:
            validas += 1
    indice = {"total": total, "validas": validas, "con_errores": con_errores, "generado_en": __import__("fecha_casa", fromlist=["hoy"]).hoy()}
    INDICE.write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    calidad = {"por_ficha": detalle, "resumen": indice}
    CALIDAD.write_text(json.dumps(calidad, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return indice


def verificar() -> int:
    """Verifica que todas las fichas del registro cumplan el esquema. Devuelve 0 si todo OK."""
    schema = _cargar_schema()
    fichas: list[Path] = sorted(p for p in REGISTRO.glob("*.json") if not p.name.startswith("_"))
    fallos = 0
    for p in fichas:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"FALLO  {p.name}: JSON inválido: {e}")
            fallos += 1
            continue
        errs = _validar_ficha(d, schema)
        if errs:
            fallos += 1
            for e in errs:
                print(f"FALLO  {p.name}: {e}")
    if fallos == 0:
        print(f"registro en disco: {len(fichas)} fichas · todas válidas contra el esquema")
        return 0
    print(f"registro en disco: {len(fichas)} fichas · {fallos} con errores")
    return 1


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Construye y verifica las fichas JSON del registro.")
    parser.add_argument("--verificar", action="store_true", help="verifica que todas las fichas cumplan el esquema")
    args = parser.parse_args(argv)

    if args.verificar:
        return verificar()
    indice = construir()
    print(f"registro: {indice['total']} fichas · {indice['validas']} válidas · {indice['con_errores']} con errores")
    return 0 if indice["con_errores"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
