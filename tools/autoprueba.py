#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUTOPRUEBA DE LA VARA · una compuerta que no falla ante un fallo sintético no es una compuerta.

Por cada compuerta se construye un árbol de prueba con UNA violación conocida y se exige que
tools/vara.py salga con código 1. Si alguna no lo detecta, esta prueba falla y la línea se detiene.

Uso: python3 tools/autoprueba.py
"""
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
VARA = RAIZ / "tools" / "vara.py"


def arbol_base(destino: Path) -> None:
    """Copia lo mínimo: esquema, una ficha sana, una pieza sana, sello y baseline."""
    (destino / "schemas").mkdir(parents=True)
    (destino / "tools").mkdir()
    (destino / "registry").mkdir()
    piezas = destino / "Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES"
    piezas.mkdir(parents=True)
    shutil.copy(RAIZ / "schemas/ficha.schema.json", destino / "schemas/ficha.schema.json")
    fuente = sorted((RAIZ / "registry").glob("*.json"))
    fuente = [f for f in fuente if not f.name.startswith("_")][0]
    shutil.copy(fuente, destino / "registry/ficha.json")
    pieza = sorted((RAIZ / "Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES").glob("*.md"))[0]
    shutil.copy(pieza, piezas / pieza.name)
    (destino / "tools/baseline.json").write_text('{"congelados": {}}\n', encoding="utf-8")
    # sello coherente con el árbol de prueba
    import hashlib
    lineas = []
    for p in sorted(destino.rglob("*")):
        if p.is_file() and p.name != "_manifiesto-sha256.tsv" and "tools" not in p.parts:
            lineas.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(destino).as_posix()}")
    (destino / "registry/_manifiesto-sha256.tsv").write_text("\n".join(lineas) + "\n", encoding="utf-8")


def correr(destino: Path) -> int:
    r = subprocess.run([sys.executable, str(VARA), "--raiz", str(destino), "--json"],
                       capture_output=True, text=True)
    return r.returncode


def editar_json(p: Path, f) -> None:
    d = json.loads(p.read_text(encoding="utf-8"))
    f(d)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


CASOS = {}


def caso(nombre):
    def envolver(fn):
        CASOS[nombre] = fn
        return fn
    return envolver


@caso("G1 esquema: ficha sin medido_en")
def _(raiz): editar_json(raiz / "registry/ficha.json", lambda d: d.pop("medido_en"))


@caso("G1 esquema: SWHID sin forma canónica")
def _(raiz):
    editar_json(raiz / "registry/ficha.json",
                lambda d: d["procedencia"].update(swhid="8d0cf730bc0a875f23477dc9015294bb6e024eb9"))


@caso("G2 frescura: medición de hace 400 días")
def _(raiz): editar_json(raiz / "registry/ficha.json", lambda d: d.update(medido_en="2025-01-01"))


@caso("G3 licencia: sin SPDX y sin ausencia firmada")
def _(raiz): editar_json(raiz / "registry/ficha.json", lambda d: d["licencia"].update(spdx=None, metodo="spdx-api"))


@caso("G4 actividad: muerto por HTTP 429")
def _(raiz): editar_json(raiz / "registry/ficha.json", lambda d: d["actividad"].update(estado="muerto", semantica_http=429))


@caso("G5 integridad: ficha alterada tras el sello")
def _(raiz): editar_json(raiz / "registry/ficha.json", lambda d: d.update(descripcion="alterada a mano"))


@caso("G5 integridad: archivo nuevo después del sello")
def _(raiz):
    d = raiz / "docs"
    d.mkdir(exist_ok=True)
    (d / "colado.md").write_text("Esto entró al archivo después de firmarse y nadie lo selló.\n", encoding="utf-8")


@caso("G10 bandas: pieza fuera de su banda declarada")
def _(raiz):
    d = raiz / "docs"
    d.mkdir(exist_ok=True)
    pieza = sorted((raiz / "Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES").glob("*.md"))[0]
    (d / "bandas.json").write_text(
        '{"whatsapp": {"min": 63000, "max": 63099, "piezas": {"01": '
        '{"archivo": "' + pieza.name + '", "caracteres": 0}}}}', encoding="utf-8")


@caso("G9 envíos: mensaje que no coincide con su cabecera")
def _(raiz):
    d = raiz / "docs/envios/whatsapp"
    d.mkdir(parents=True, exist_ok=True)
    (d / "envio-falso.md").write_text(
        "# PIEZA 99 · envío falso\n\n═══ MENSAJE 1 de 3 · 900 caracteres ═══\n\n"
        "Esto dice 900 y tiene treinta.\n", encoding="utf-8")


@caso("G7 enlaces: binario recetado")
def _(raiz):
    p = sorted((raiz / "Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES").glob("*.md"))[0]
    p.write_text(p.read_text(encoding="utf-8") + "\n\nDescarga: https://ejemplo.invalid/app-mod.apk\n", encoding="utf-8")


@caso("G0 piezas: pieza sin 💓 y sin fecha")
def _(raiz):
    p = sorted((raiz / "Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES").glob("*.md"))[0]
    p.write_text("Pieza sin firma ni fecha.\n", encoding="utf-8")


def main() -> int:
    fallos = []
    for nombre, fn in CASOS.items():
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp) / "arbol"
            arbol_base(raiz)
            sano = correr(raiz)
            if sano != 0:
                fallos.append(f"{nombre}: el árbol de prueba no estaba sano antes de romperlo")
                continue
            fn(raiz)
            roto = correr(raiz)
            estado = "detectado" if roto != 0 else "NO DETECTADO"
            print(f"  {estado:<13} {nombre}")
            if roto == 0:
                fallos.append(nombre)
    print()
    print(f"autoprueba: {len(CASOS) - len(fallos)}/{len(CASOS)} violaciones detectadas · "
          f"fallos: {'NINGUNO' if not fallos else len(fallos)}")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
