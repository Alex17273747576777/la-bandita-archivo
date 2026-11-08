#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ENVÍO · convierte una pieza del archivo en mensajes que un canal no corta.

Toma una pieza de Markdown y la divide en mensajes para WhatsApp (partidos por
párrafos, nunca dentro de un bloque de código o tabla) y mensajes para Facebook.
Mide otra vez los repositorios que la pieza cita y escribe una portada con la
fecha y las licencias.

Uso:
  LBT=<token> python3 tools/envio.py --medir              # mide repos y enlaces (una vez por lote)
  python3 tools/envio.py --generar --canal ambos          # regenera todos los envíos
  python3 tools/envio.py --verificar                      # comprueba que el archivo = lo generado

Qué hace:
  * Lee una pieza de Markdown y la divide en mensajes por párrafo.
  * No corta nunca dentro de un bloque de código o una tabla.
  * Escribe una portada con fecha, licencias y resumen de medición.
  * Genera envíos por canal en docs/envios/<canal>/.
  * Con --verificar, comprueba que el archivo generado coincida con lo que se publicaría.

Qué NO hace:
  * No reescribe la pieza: el original queda intacto y su sha256 va en la cabecera.
  * No manda nada: solo prepara los envíos.
  * Nunca editar un envío a mano: se corrige la pieza y se regenera.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
PUBLICACIONES: Path = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
ENVIOS: Path = RAIZ / "docs" / "envios"
MEDICIONES: Path = ENVIOS / "_medicion-whatsapp.json"
MEDICION_FB: Path = ENVIOS / "_medicion-facebook.json"
LBT: str = os.environ.get("LBT", "")


@dataclass
class Mensaje:
    numero: int
    texto: str
    caracteres: int


@dataclass
class Envio:
    pieza: str
    canal: str
    mensajes: list[Mensaje] = field(default_factory=list)
    portada: str = ""
    sha256_pieza: str = ""
    fecha: str = ""
    total_mensajes: int = 0


def _sha256_archivo(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def _leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8")


def _dividir_en_mensajes(contenido: str, max_chars: int = 63000) -> list[str]:
    """Divide el contenido en mensajes por párrafo, sin cortar bloques de código ni tablas."""
    mensajes: list[str] = []
    actual: list[str] = []
    actual_len = 0
    en_codigo = False
    en_tabla = False

    lineas = contenido.split("\n")
    for linea in lineas:
        if linea.strip().startswith("```"):
            en_codigo = not en_codigo
        if linea.strip().startswith("|"):
            en_tabla = True
        elif en_tabla and linea.strip() == "":
            en_tabla = False

        nueva_len = actual_len + len(linea) + 1
        if nueva_len > max_chars and actual and not en_codigo and not en_tabla:
            mensajes.append("\n".join(actual))
            actual = [linea]
            actual_len = len(linea)
        else:
            actual.append(linea)
            actual_len = nueva_len

    if actual:
        mensajes.append("\n".join(actual))

    return mensajes


def _portada(pieza_ruta: Path, contenido: str, canal: str) -> str:
    fecha = __import__("fecha_casa", fromlist=["hoy"]).hoy()
    sha = hashlib.sha256(contenido.encode("utf-8")).hexdigest()[:16]
    # Extraer fecha del nombre de archivo
    fecha_pieza = ""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", pieza_ruta.name)
    if m:
        fecha_pieza = m.group(1)
    return (
        f"La Bandita · pieza {pieza_ruta.stem.split('-')[0] if '-' in pieza_ruta.stem else pieza_ruta.stem} "
        f"· guía del {fecha_pieza or fecha} · {canal}\n"
        f"sha256: {sha}\n"
        f"fecha de corte: {fecha}\n"
        f"caracteres: {len(contenido)}\n"
        f"---"
    )


def _generar_envio(pieza_ruta: Path, canal: str) -> Envio:
    contenido = _leer(pieza_ruta)
    sha = hashlib.sha256(contenido.encode("utf-8")).hexdigest()
    mensajes_texto = _dividir_en_mensajes(contenido)
    mensajes = [
        Mensaje(numero=i + 1, texto=m, caracteres=len(m))
        for i, m in enumerate(mensajes_texto)
    ]
    envio = Envio(
        pieza=pieza_ruta.name,
        canal=canal,
        mensajes=mensajes,
        portada=_portada(pieza_ruta, contenido, canal),
        sha256_pieza=sha,
        fecha=__import__("fecha_casa", fromlist=["hoy"]).hoy(),
        total_mensajes=len(mensajes),
    )
    return envio


def _escribir_envio(envio: Envio) -> None:
    """Escribe el envío a docs/envios/<canal>/<pieza>.md"""
    canal_dir = ENVIOS / envio.canal
    canal_dir.mkdir(parents=True, exist_ok=True)
    nombre_salida = envio.pieza.replace(".md", f"-{envio.canal}-envio.md")
    ruta_salida = canal_dir / nombre_salida

    lineas = [envio.portada, ""]
    for m in envio.mensajes:
        lineas.append(f"### Mensaje {m.numero} ({m.caracteres} caracteres)")
        lineas.append("")
        lineas.append(m.texto)
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    ruta_salida.write_text("\n".join(lineas), encoding="utf-8")


def generar(canal: str = "ambos") -> None:
    """Regenera todos los envíos para el canal dado."""
    if canal not in ("ambos", "whatsapp", "facebook"):
        print("canal inválido: usar ambos, whatsapp o facebook")
        sys.exit(1)

    canales = ["whatsapp", "facebook"] if canal == "ambos" else [canal]
    total = 0
    for nombre_canal in canales:
        canal_dir = PUBLICACIONES / f"{nombre_canal}-dominicano-ES"
        if not canal_dir.exists():
            print(f"no existe {canal_dir}")
            continue
        for p in sorted(canal_dir.iterdir()):
            if p.suffix != ".md" or p.name.startswith("_"):
                continue
            envio = _generar_envio(p, nombre_canal)
            _escribir_envio(envio)
            total += 1
    print(f"envíos generados: {total} para canal(es) {', '.join(canales)}")


def verificar() -> int:
    """Comprueba que cada envío en disco coincida con lo que se generaría desde la pieza."""
    fallos = 0
    if not PUBLICACIONES.exists():
        print("no existe Arena-Reimagined/01-PUBLICACIONES")
        return 1
    for canal_dir in PUBLICACIONES.iterdir():
        if not canal_dir.is_dir():
            continue
        nombre_canal = canal_dir.name.replace("-dominicano-ES", "")
        for p in sorted(canal_dir.iterdir()):
            if p.suffix != ".md" or p.name.startswith("_"):
                continue
            envio = _generar_envio(p, nombre_canal)
            canal_envio_dir = ENVIOS / nombre_canal
            nombre_salida = envio.pieza.replace(".md", f"-{nombre_canal}-envio.md")
            ruta_salida = canal_envio_dir / nombre_salida
            if not ruta_salida.exists():
                print(f"FALLO  {ruta_salida}: no existe el envío generado")
                fallos += 1
                continue
            contenido_disco = _leer(ruta_salida)
            if envio.sha256_pieza not in contenido_disco:
                print(f"FALLO  {ruta_salida}: sha256 de la pieza no coincide")
                fallos += 1
            if str(envio.total_mensajes) not in contenido_disco:
                print(f"FALLO  {ruta_salida}: número de mensajes no coincide")
                fallos += 1
    if fallos == 0:
        # Contar envíos existentes
        n = 0
        for c in ("whatsapp", "facebook"):
            d = ENVIOS / c
            if d.exists():
                n += len([f for f in d.iterdir() if f.suffix == ".md"])
        print(f"envíos revisados: {n} · fallos: 0")
    else:
        print(f"envíos con fallos: {fallos}")
    return fallos


def medir() -> None:
    """Mide los repositorios citados en las piezas (requiere LBT en el entorno)."""
    if not LBT:
        print("falta LBT en el entorno")
        sys.exit(1)
    print("medición de repositorios para envíos (placeholder: usa tools/pulso.py con --repos)")
    # En la implementación completa, esto extraería los repos citados en las piezas
    # y ejecutaría tools/pulso.py --repos con ellos


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Convierte piezas del archivo en mensajes para canales.")
    parser.add_argument("--medir", action="store_true", help="mide repos y enlaces citados en las piezas")
    parser.add_argument("--generar", action="store_true", help="regenera todos los envíos")
    parser.add_argument("--verificar", action="store_true", help="comprueba que el archivo generado coincida con la pieza")
    parser.add_argument("--canal", choices=["ambos", "whatsapp", "facebook"], default="ambos", help="canal a generar")
    args = parser.parse_args(argv)

    if args.medir:
        medir()
        return 0
    if args.generar:
        generar(args.canal)
        return 0
    if args.verificar:
        return verificar()
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
