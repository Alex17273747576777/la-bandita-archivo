#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lint_teclado.py · comprueba la biblioteca de instrucciones y la exporta.

No mide si una IA obedece: eso no se puede medir desde aquí y quien diga que lo
mide está inventando. Lo que sí comprueba, con reglas que se pueden leer:

  T01 destino declarado y válido (tecla / atajo / macro)
  T02 tope físico: LeanType admite 10 teclas de IA (CUSTOM_AI_1..10 en su código)
  T03 longitud que cabe en una tecla (≤400) y en un atajo (≤700)
  T04 arranca con un verbo en imperativo: la tarea, no el personaje
  T05 contrato de salida explícito (qué devuelve y qué no)
  T06 sin cortesía ni condicionales que invitan a conversar
  T07 sin marcadores sin resolver (TODO, XXX, <algo>)
  T08 sin promesas imposibles (100 %, infalible, perfecto)
  T09 sin duplicados por parecido (Jaccard > 0,75 sobre palabras)
  T10 el idioma no se fija salvo en las teclas de traducción
  T11 atajos con forma `;palabra` y sin repetirse

Uso:
    python3 tools/lint_teclado.py                 # informe
    python3 tools/lint_teclado.py --exportar      # además escribe exportado/
    python3 tools/lint_teclado.py --json          # para el acta
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / "corpus-la-bandita" / "teclado" / "prompts.json"
SALIDA = RAIZ / "corpus-la-bandita" / "teclado" / "exportado"

TOPE_TECLAS = 10          # medido en LeanType: KeyCode.CUSTOM_AI_1 … CUSTOM_AI_10
MAX_TECLA = 400
MAX_ATAJO = 700

IMPERATIVOS = {
    "corrige", "reescribe", "resume", "expande", "pasa", "traduce", "extrae",
    "escribe", "da", "revisa", "convierte", "explica", "redacta", "compara",
    "ordena", "separa", "calcula", "propone", "mide", "comprueba", "limpia",
}
CONTRATOS = (
    "devuelve solo", "devuelve únicamente", "devuelve tres bloques", "sin viñetas",
    "sin adjetivos", "máximo", "una línea por", "escribe ninguna", "no escribas nada más",
    "devuelve el texto", "sin adorno", "separa", "máximo 90 palabras",
)
CORTESIA = re.compile(r"por favor|si puedes|podr[ií]as|ser[ií]a posible|gracias de antemano", re.I)
MARCADORES = re.compile(r"\bTODO\b|\bXXX\b|<[a-záéíóúñ]{2,}>|\bFIXME\b")
MAGIA = re.compile(r"100 ?%|infalible|perfect[oa]|garantiz|siempre funciona|nunca falla", re.I)
IDIOMA = re.compile(r"en espa[ñn]ol|en castellano|responde en espa[ñn]ol", re.I)


def palabras(t: str) -> set[str]:
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return {p for p in re.findall(r"[a-z]{4,}", t)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def revisar(datos: dict) -> tuple[list[dict], list[dict]]:
    fallos: list[dict] = []
    ok: list[dict] = []

    teclas = datos["teclas"]
    atajos = datos["atajos"]
    macros = datos["macros"]

    # T02 · tope físico
    if len(teclas) > TOPE_TECLAS:
        fallos.append({"c": "T02", "id": "biblioteca",
                       "detalle": f"{len(teclas)} teclas de IA; el teclado admite {TOPE_TECLAS}"})
    else:
        ok.append({"c": "T02", "id": "biblioteca", "detalle": f"{len(teclas)} teclas de IA, caben en {TOPE_TECLAS}"})

    vistos: list[tuple[str, set[str]]] = []
    for p in teclas + atajos:
        grupo = "tecla" if p in teclas else "atajo"
        texto = p["prompt"]
        lim = MAX_TECLA if grupo == "tecla" else MAX_ATAJO

        if grupo == "tecla" and not p.get("palabra_clave"):
            fallos.append({"c": "T01", "id": p["id"], "detalle": "tecla sin palabra clave"})
        if grupo == "atajo" and not re.fullmatch(r";[a-z]{2,8}", p.get("atajo", "")):
            fallos.append({"c": "T11", "id": p["id"], "detalle": f"atajo con forma rara: {p.get('atajo')}"})

        if len(texto) > lim:
            fallos.append({"c": "T03", "id": p["id"], "detalle": f"{len(texto)} caracteres (tope {lim})"})

        primera = re.findall(r"[a-záéíóúñ]+", texto.lower())[:1]
        if not primera or primera[0] not in IMPERATIVOS:
            fallos.append({"c": "T04", "id": p["id"],
                           "detalle": f"no arranca con imperativo (empieza por «{primera[0] if primera else ''}»)"})

        bajo = texto.lower()
        if not any(c in bajo for c in CONTRATOS):
            fallos.append({"c": "T05", "id": p["id"], "detalle": "sin contrato de salida"})
        if CORTESIA.search(texto):
            fallos.append({"c": "T06", "id": p["id"], "detalle": "pide las cosas por favor"})
        if MARCADORES.search(texto):
            fallos.append({"c": "T07", "id": p["id"], "detalle": "marcador sin resolver"})
        if MAGIA.search(texto):
            fallos.append({"c": "T08", "id": p["id"], "detalle": "promesa imposible"})
        if IDIOMA.search(texto) and not p["id"].startswith("traducir"):
            fallos.append({"c": "T10", "id": p["id"], "detalle": "fija el idioma de salida"})

        conj = palabras(texto)
        for otro, suyo in vistos:
            j = jaccard(conj, suyo)
            if j > 0.75:
                fallos.append({"c": "T09", "id": p["id"], "detalle": f"se parece a {otro} ({j:.0%})"})
        vistos.append((p["id"], conj))

    atajos_vistos: set[str] = set()
    for m in macros:
        if m["atajo"] in atajos_vistos:
            fallos.append({"c": "T11", "id": m["id"], "detalle": "atajo repetido"})
        atajos_vistos.add(m["atajo"])

    if not fallos:
        ok.append({"c": "TODAS", "id": "biblioteca", "detalle": "11 comprobaciones sin un solo fallo"})
    return fallos, ok


def exportar(datos: dict) -> dict:
    SALIDA.mkdir(parents=True, exist_ok=True)
    hechos = {}

    # 1 · LeanType: diez teclas, en el orden en que se configuran
    lineas = ["# LeanType · las 10 teclas de IA, para copiar una por una",
              "# Ajustes → Teclado → Teclas de IA personalizadas", ""]
    for i, p in enumerate(datos["teclas"], 1):
        lineas += [f"Tecla {i} · {p['nombre']}",
                   f"Palabra clave: {p['palabra_clave']}",
                   f"Prompt: {p['prompt']}", ""]
    (SALIDA / "leantype-teclas.txt").write_text("\n".join(lineas), encoding="utf-8")
    hechos["leantype-teclas.txt"] = len(datos["teclas"])

    # 2 · LeanType: atajos del expansor
    lineas = ["# LeanType → Text Expander · atajo ; texto", ""]
    for a in datos["atajos"]:
        lineas += [f"Atajo: {a['atajo']}", f"Texto: {a['prompt']}", ""]
    for m in datos["macros"]:
        lineas += [f"Atajo: {m['atajo']}", f"Texto: {m['texto']}", ""]
    (SALIDA / "expansor-atajos.txt").write_text("\n".join(lineas), encoding="utf-8")
    hechos["expansor-atajos.txt"] = len(datos["atajos"]) + len(datos["macros"])

    # 3 · AnySoftKeyboard: fragmento de add-on con el esquema real de QuickText
    trozos = ['<?xml version="1.0" encoding="UTF-8"?>',
              "<!-- Fragmento para un add-on de QuickText de AnySoftKeyboard.",
              "     El esquema es el de ime/addons/quick_text/res/xml/quick_text_keys.xml.",
              "     Para instalarlo hay que compilar el add-on: no se puede soltar suelto. -->",
              "<QuickTextKeys>"]
    for i, a in enumerate(datos["atajos"], 1):
        etiqueta = a["atajo"].replace(";", "").replace("&", "&amp;")
        texto = a["prompt"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        trozos += ["    <QuickTextKey",
                   f'        id="{a["id"]}_quick_text_key"',
                   f'        keyLabel="{etiqueta}"',
                   f'        keyOutputText="{texto}"',
                   f'        description="{a["nombre"]}"',
                   f'        index="{i}"/>']
    trozos.append("</QuickTextKeys>")
    (SALIDA / "ask-quicktext.xml").write_text("\n".join(trozos) + "\n", encoding="utf-8")
    hechos["ask-quicktext.xml"] = len(datos["atajos"])

    return hechos


def main() -> int:
    datos = json.loads(DATOS.read_text(encoding="utf-8"))
    fallos, ok = revisar(datos)

    if "--json" in sys.argv:
        print(json.dumps({"fallos": fallos, "ok": ok}, ensure_ascii=False, indent=1))
    else:
        print(f"BIBLIOTECA {datos['version']} · {len(datos['teclas'])} teclas · "
              f"{len(datos['atajos'])} atajos · {len(datos['macros'])} macros")
        for f in fallos:
            print(f"  ✗ {f['c']} {f['id']}: {f['detalle']}")
        for o in ok:
            print(f"  ✓ {o['c']} {o['detalle']}")
        print(f"fallos: {len(fallos)}")

    if "--exportar" in sys.argv:
        hechos = exportar(datos)
        for nombre, n in hechos.items():
            print(f"  → {nombre}: {n} entradas")

    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
