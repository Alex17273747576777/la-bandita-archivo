#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""COLA · el trabajo largo se hace en tramos cortos y se reanuda solo.

Problema que resuelve: cuando una tarea larga se corta a mitad —por tiempo, por
memoria, porque el entorno se reinicia—, quien la retoma no sabe qué estaba hecho
y suele repetirlo. La casa ya tenía el tablero de tareas (`tools/tareas.py`), pero
el tablero dice *qué falta*, no *hasta dónde llegué*.

Esta cola dice las dos cosas, y guarda la prueba de cada tramo:

  * cada paso tiene un id, una descripción y un puntero a su evidencia;
  * un paso solo se cierra con `--hecho` y **exige evidencia** (ruta, commit o
    cifra medida): no se puede marcar «hecho» a mano sin dejar rastro;
  * el estado vive en `docs/_cola/estado.json`, que se commitea, así que
    sobrevive a cualquier corte;
  * `--siguiente` devuelve **un** paso, nunca la lista entera: el trabajo se hace
    de uno en uno y cada uno se commitea.

Uso:
  python3 tools/cola.py --sembrar             # crea la cola del encargo vigente
  python3 tools/cola.py --siguiente           # imprime el próximo paso
  python3 tools/cola.py --hecho P03 --evidencia "commit abc1234 · 4 piezas"
  python3 tools/cola.py --estado              # cuántos van y cuántos faltan
  python3 tools/cola.py --json                # legible por máquina
  python3 tools/cola.py --autoprueba          # comprueba que la cola hace lo que dice

Qué NO hace:
  * no ejecuta el trabajo: solo lleva la cuenta y lo deja reanudable;
  * no cierra un paso sin evidencia;
  * no borra pasos: los pasos se cierran, no se eliminan.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ESTADO = RAIZ / "docs" / "_cola" / "estado.json"


def ahora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def leer() -> dict:
    if not ESTADO.exists():
        return {"encargo": "", "creada": ahora(), "pasos": []}
    return json.loads(ESTADO.read_text(encoding="utf-8"))


def guardar(d: dict) -> None:
    ESTADO.parent.mkdir(parents=True, exist_ok=True)
    ESTADO.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# Los pasos del encargo vigente: rehacer las cuarenta piezas de Facebook con
# recursos nuevos, revisando los catálogos de fmhy.net, miyomi.app y los índices
# que aparezcan. Cada paso dura minutos, no horas: es la regla contra el corte.
SEMILLA = {
    "encargo": "rehacer las 40 piezas de Facebook con recursos nuevos, catálogos revisados "
               "(fmhy.net, miyomi.app e índices encontrados) y issues al repositorio de fmhy",
    "pasos": [
        ("P01", "leer fmhy.net y anotar su estructura real: qué páginas hay, cómo se navega, si tiene API o índice."),
        ("P02", "leer fmhy.net/other/ y las páginas de índices: qué catálogos de índices lista y cuáles son medibles."),
        ("P03", "medir miyomi.app: qué ofrece, si su API sirve, qué repositorios de extensiones/publicaciones acepta."),
        ("P04", "buscar y anotar índices de extensiones y catálogos adicionales (mihon, keiyoushi, aniyomi, cloudstream, novelas)."),
        ("P05", "construir el censo de recursos nuevos: repositorios no medidos todavía, con dueño/repo, para las 40 piezas."),
        ("P06", "medir el censo contra la API de GitHub y guardar docs/MEDICION-CENSO-2026-11-08.json."),
        ("P07", "decidir el reparto: qué recursos van a cada una de las 40 piezas y con qué tema."),
        ("P08", "abrir issue en el repositorio de fmhy proponiendo los índices buenos que no estén ya listados."),
        ("P09", "escribir las piezas 01-10 con sus fichas medidas."),
        ("P10", "escribir las piezas 11-20 con sus fichas medidas."),
        ("P11", "escribir las piezas 21-30 con sus fichas medidas."),
        ("P12", "escribir las piezas 31-40 con sus fichas medidas."),
        ("P13", "generar los 40 comentarios fijados desde los JSON de medición."),
        ("P14", "cuadrar registro: bandas.json, LEEME, README, CHANGELOG y leeme_carpeta.py."),
        ("P15", "sellar y pasar la vara hasta fallos: NINGUNO; commit y push."),
    ],
}


def sembrar(forzar: bool = False) -> int:
    if ESTADO.exists() and not forzar:
        print(f"la cola ya existe en {ESTADO.relative_to(RAIZ)}; usá --sembrar --forzar para rehacerla")
        return 0
    d = {"encargo": SEMILLA["encargo"], "creada": ahora(),
         "pasos": [{"id": i, "descripcion": t, "hecho": False,
                    "evidencia": None, "cerrado_en": None} for i, t in SEMILLA["pasos"]]}
    guardar(d)
    print(f"cola sembrada: {len(d['pasos'])} pasos")
    return 0


def siguiente() -> int:
    d = leer()
    for p in d["pasos"]:
        if not p["hecho"]:
            total = len(d["pasos"])
            hechos = sum(1 for x in d["pasos"] if x["hecho"])
            print(f"{p['id']} · {p['descripcion']}")
            print(f"({hechos}/{total} hechos ·  cuando termines: --hecho {p['id']} --evidencia \"…\")")
            return 0
    print("no queda ningún paso abierto")
    return 0


def cerrar(paso: str, evidencia: str) -> int:
    d = leer()
    for p in d["pasos"]:
        if p["id"] == paso:
            if p["hecho"]:
                print(f"{paso} ya estaba cerrado; no se toca")
                return 0
            if not evidencia or len(evidencia.strip()) < 8:
                print("un paso no se cierra sin evidencia: ruta, commit o cifra medida")
                return 1
            p["hecho"] = True
            p["evidencia"] = evidencia.strip()
            p["cerrado_en"] = ahora()
            guardar(d)
            hechos = sum(1 for x in d["pasos"] if x["hecho"])
            print(f"{paso} cerrado · {hechos}/{len(d['pasos'])}")
            return 0
    print(f"no existe el paso {paso}")
    return 1


def estado() -> int:
    d = leer()
    hechos = [p for p in d["pasos"] if p["hecho"]]
    print(f"encargo: {d['encargo']}")
    print(f"pasos: {len(d['pasos'])} · hechos: {len(hechos)} · abiertos: {len(d['pasos']) - len(hechos)}")
    for p in hechos:
        print(f"  ✓ {p['id']}  {p['evidencia']}")
    for p in d["pasos"]:
        if not p["hecho"]:
            print(f"  · {p['id']}  {p['descripcion'][:88]}")
    return 0


def autoprueba() -> int:
    """La cola tiene que demostrar lo que dice: cierre con evidencia y reanudación."""
    global ESTADO
    import tempfile
    original = ESTADO
    with tempfile.TemporaryDirectory() as tmp:
        ESTADO = Path(tmp) / "estado.json"
        fallos = []
        sembrar()
        d = leer()
        if len(d["pasos"]) != len(SEMILLA["pasos"]):
            fallos.append("la siembra no creó todos los pasos")
        if cerrar("P01", "") != 1:
            fallos.append("cerró un paso sin evidencia (no debía)")
        if cerrar("P01", "docs/PRUEBA.json · 3 repos") != 0:
            fallos.append("no cerró un paso con evidencia")
        if cerrar("P01", "otra cosa") != 0 or leer()["pasos"][0]["evidencia"] != "docs/PRUEBA.json · 3 repos":
            fallos.append("un paso cerrado se dejó sobrescribir")
        sig = [p for p in leer()["pasos"] if not p["hecho"]][0]["id"]
        if sig != "P02":
            fallos.append(f"tras cerrar P01 el siguiente debería ser P02 y fue {sig}")
        if cerrar("P99", "x" * 10) != 1:
            fallos.append("aceptó un paso inexistente")
    ESTADO = original
    for f in fallos:
        print("  FALLO ·", f)
    print(f"autoprueba de la cola · {'VERDE' if not fallos else 'ROJA'} · comprobaciones: 6 · fallos: {len(fallos)}")
    return 0 if not fallos else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sembrar", action="store_true")
    ap.add_argument("--forzar", action="store_true")
    ap.add_argument("--siguiente", action="store_true")
    ap.add_argument("--hecho")
    ap.add_argument("--evidencia", default="")
    ap.add_argument("--estado", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--autoprueba", action="store_true")
    a = ap.parse_args(argv)
    if a.autoprueba:
        return autoprueba()
    if a.sembrar:
        return sembrar(a.forzar)
    if a.hecho:
        return cerrar(a.hecho, a.evidencia)
    if a.json:
        print(json.dumps(leer(), ensure_ascii=False, indent=1))
        return 0
    if a.estado:
        return estado()
    return siguiente()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
