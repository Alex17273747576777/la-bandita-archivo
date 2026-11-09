#!/usr/bin/env python3
"""Cuadra docs/bandas.json contra los archivos que existen de verdad.

La banda no es una meta de escritura: es el registro de lo que la pieza mide hoy,
con el margen de ±50 caracteres que usa la serie. Si un archivo cambia —una
corrección anotada, un párrafo quitado—, la banda queda vieja y G10 lo grita.
Este programa rehace el registro leyendo los archivos, no al revés.

Uso:
    python3 tools/bandas.py            # informe, no toca nada
    python3 tools/bandas.py --cuadrar  # reescribe docs/bandas.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
BANDAS = RAIZ / "docs" / "bandas.json"
PUBLICACIONES = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
MARGEN = 50


def archivo_en(canal: Path, nombre: str) -> Path | None:
    for p in canal.glob("*.md"):
        if p.name == nombre:
            return p
    return None


def main() -> int:
    cuadrar = "--cuadrar" in sys.argv
    datos = json.loads(BANDAS.read_text(encoding="utf-8"))
    cambios: list[str] = []
    faltan: list[str] = []
    iguales = 0

    for canal in sorted(p for p in PUBLICACIONES.iterdir() if p.is_dir()):
        clave = canal.name.replace("-dominicano-ES", "")
        seccion = None
        for k, v in datos.items():
            if k.lower() == clave.lower() and isinstance(v, dict):
                seccion = v
                break
        if not seccion:
            continue
        for num, info in sorted(seccion.get("piezas", {}).items()):
            nombre = info.get("archivo", "")
            ruta = archivo_en(canal, nombre)
            if ruta is None:
                # La pieza se reescribió: el nombre viejo ya no existe, pero la pieza sí.
                # Se busca por número y por tipo (cuerpo o fijado) y se corrige el registro,
                # que para eso está. No se borra la entrada sin decir qué pasó.
                base = num.split("-")[0]
                es_fijado = num.endswith("-fijado")
                cand = [q for q in canal.glob(f"{base}-*.md")
                        if ("Comentario-fijado" in q.name) == es_fijado]
                if len(cand) == 1:
                    cambios.append(f"{clave}/{num}: nombre viejo → {cand[0].name[:44]}…")
                    if cuadrar:
                        info["archivo"] = cand[0].name
                    ruta = cand[0]
                else:
                    faltan.append(f"{clave}/{num}: {nombre}")
                    continue
            real = len(ruta.read_text(encoding="utf-8"))
            if (info.get("caracteres") == real and info.get("min") == real - MARGEN
                    and info.get("max") == real + MARGEN):
                iguales += 1
                continue
            cambios.append(f"{clave}/{num}: {info.get('caracteres')} → {real}")
            if cuadrar:
                info["caracteres"] = real
                info["min"] = real - MARGEN
                info["max"] = real + MARGEN

    if cuadrar and cambios:
        BANDAS.write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"bandas al día: {iguales} · desviadas: {len(cambios)} · archivos que no están: {len(faltan)}")
    for c in cambios[:20]:
        print("  ·", c)
    if faltan:
        print("  sin archivo:")
        for f in faltan[:10]:
            print("    -", f)
    if cambios and not cuadrar:
        print("\n(usa --cuadrar para rehacer el registro)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
