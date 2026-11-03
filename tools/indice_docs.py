#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÍNDICE · el mapa de la carpeta docs y del juego de herramientas, sin escribirlo a mano.

`docs/` llegó a doscientos ochenta y cuatro archivos y la carpeta `tools/` a treinta y
cinco programas. Un índice escrito a mano envejece la primera semana; uno generado no
puede mentir porque se vuelve a correr. Este programa lee, clasifica y escribe
`docs/INDICE.md`: primero los documentos agrupados por familia, y después cada
herramienta con la frase con la que se presenta.

Qué recibe: el árbol del repositorio.
Qué produce: `docs/INDICE.md`, un archivo. Nada más.
Qué no hace: no borra, no mueve y no decide qué documento es importante. Ordena lo
que hay y deja que el lector juzgue.

Uso:
    python3 tools/indice_docs.py            # escribe docs/INDICE.md
    python3 tools/indice_docs.py --json     # solo el inventario, sin escribir
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
TOOLS = RAIZ / "tools"
SALIDA = DOCS / "INDICE.md"

# Familias por prefijo del nombre. Lo que no cae en ninguna va a «Otros», que es donde
# hay que mirar cuando una familia nueva aparece sin nombre.
FAMILIAS = (
    ("ACTA", "Actas · lo que se hizo y se firmó"),
    ("INFORME", "Informes · el estado contado"),
    ("REVISION", "Revisiones · lecturas de un día concreto"),
    ("POLITICA", "Políticas · reglas de operación"),
    ("PROTOCOLO", "Protocolos · cómo se corrige y cómo se responde"),
    ("CONFORMIDAD", "Conformidad · contra el manual de la casa"),
    ("PLAN", "Planes · trabajo por delante"),
    ("PROMPTS", "Prompts · encargos largos"),
    ("NUEVOS", "Descubrimientos · lo que apareció medido"),
    ("INVENTARIO", "Inventarios · qué hay"),
    ("BARRIDO", "Barridos · barridos de error"),
    ("DECISIONES", "Decisiones · el porqué de una bifurcación"),
    ("DESCUBRIMIENTOS", "Descubrimientos · lo que apareció medido"),
    ("ERRATA", "Erratas · lo que se corrigió"),
    ("PENDIENTES", "Pendientes · listas de espera"),
    ("CANAL", "Canales · cómo se publica en cada red"),
    ("TMO", "TMO · el caso de las tiendas"),
    ("INTELIGENCIA", "Inteligencia · señales del ecosistema"),
    ("NLNET", "NLnet · el expediente del fondo"),
    ("MCP", "MCP · el servidor y su registro"),
)


def titulo(texto: str) -> str:
    for linea in texto.splitlines():
        if linea.startswith("# "):
            return linea[2:].strip()[:96]
    return ""


def resumen(texto: str) -> str:
    """La primera oración completa del primer párrafo con cuerpo.

    Un párrafo del Markdown está partido en varias líneas, así que hay que unirlas
    antes de leerlo: si no, el índice se queda con un fragmento que empieza a media
    frase («tras la limpieza del 2-nov, con su huella…»), que no dice nada.
    """
    parrafos: list[str] = []
    buf: list[str] = []
    for linea in texto.splitlines():
        l = linea.strip()
        es_bloque = (not l) or l.startswith(("#", "|", ">", "```", "---", "<")) \
            or re.match(r"^([-*+]\s|\d+[.)]\s)", l)
        if es_bloque:
            if buf:
                parrafos.append(" ".join(buf))
                buf = []
            continue
        buf.append(l)
    if buf:
        parrafos.append(" ".join(buf))

    for p in parrafos:
        if len(p) < 60:
            continue
        # Una oración empieza en mayúscula o en signo de apertura; si empieza en
        # minúscula, es la cola de la línea anterior y no sirve como presentación.
        if not (p[0].isupper() or p[0] in '«"¡¿'):
            continue
        frase = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ«¡¿])", p)[0].strip()
        if len(frase) < 45:
            continue
        if len(frase) > 150:
            frase = frase[:150].rsplit(" ", 1)[0] + "…"
        return frase
    return ""


def familia(nombre: str) -> str:
    arriba = nombre.upper()
    for prefijo, etiqueta in FAMILIAS:
        if arriba.startswith(prefijo):
            return etiqueta
    return "Otros · sin familia declarada"


def documentos() -> dict[str, list[dict]]:
    grupos: dict[str, list[dict]] = defaultdict(list)
    for p in sorted(DOCS.rglob("*.md")):
        if p.name == "INDICE.md" or "_historico" in p.parts:
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        grupos[familia(p.name)].append({
            "archivo": p.relative_to(RAIZ).as_posix(),
            "titulo": titulo(t) or p.stem.replace("-", " "),
            "resumen": resumen(t) or "— sin primera oración con cuerpo —",
            "lineas": t.count("\n") + 1,
        })
    return grupos


def herramientas() -> list[dict]:
    salida = []
    for p in sorted(TOOLS.glob("*.py")):
        if p.name.startswith("_"):
            continue
        try:
            doc = ast.get_docstring(ast.parse(p.read_text(encoding="utf-8", errors="replace"))) or ""
        except SyntaxError:
            doc = ""
        primera = next((l.strip() for l in doc.splitlines() if l.strip()), "")
        salida.append({"archivo": f"tools/{p.name}",
                       "que_es": primera[:140] or "(sin docstring)",
                       "lineas": p.read_text(encoding="utf-8", errors="replace").count("\n") + 1})
    return salida


def escribir(grupos: dict[str, list[dict]], tools: list[dict]) -> None:
    total_docs = sum(len(v) for v in grupos.values())
    secciones = []
    for etiqueta in sorted(grupos):
        filas = "\n".join(
            f"| [`{d['archivo'].split('/')[-1]}`]({d['archivo'].split('docs/')[-1]}) | {d['titulo']} | {d['resumen']} | {d['lineas']} |"
            for d in sorted(grupos[etiqueta], key=lambda x: x["archivo"]))
        secciones.append(f"### {etiqueta}\n\n| Documento | Título | De qué va | Líneas |\n|---|---|---|---|\n{filas}")
    filas_tools = "\n".join(
        f"| [`{t['archivo'].split('/')[-1]}`](../{t['archivo']}) | {t['que_es']} | {t['lineas']} |"
        for t in tools)
    cuerpo = f"""# ÍNDICE DEL ARCHIVO

*Generado por `tools/indice_docs.py`. No se edita a mano: se vuelve a correr.*

**TL;DR —** {total_docs} documentos en `docs/`, agrupados en {len(grupos)} familias, y {len(tools)} herramientas en `tools/`. Cada herramienta se presenta con la primera frase de su propio código, así que el índice no puede desactualizarse sin que el código cambie primero.

## Para qué sirve este índice

`docs/` es la memoria escrita de la casa: actas, informes, políticas y protocolos. Con los meses se vuelve un cajón donde no se encuentra nada, y una casa sin índice obliga a recordar. Esto es lo contrario: se corre un comando y el cajón se ordena solo.

## Los documentos, por familia

{chr(10).join(secciones)}

## Las herramientas

Cada programa de `tools/` hace una cosa y la dice en la primera línea de su código. Esa frase es la que aparece aquí, sin traducción ni adorno.

| Herramienta | Qué hace | Líneas |
|---|---|---|
{filas_tools}

## Cómo se mantiene

```
make indice      # reescribe este archivo
make tareas      # reescribe el tablero de tareas
make verificar   # compuertas completas
```

*La Bandita informa a partir de fuentes fechadas.*
"""
    SALIDA.write_text(cuerpo, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Índice de docs y de herramientas.")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    grupos, tools = documentos(), herramientas()
    if a.json:
        print(json.dumps({"documentos": grupos, "herramientas": tools}, ensure_ascii=False, indent=1))
        return 0
    escribir(grupos, tools)
    print(f"índice escrito: {SALIDA.relative_to(RAIZ)} · "
          f"{sum(len(v) for v in grupos.values())} documentos · {len(tools)} herramientas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
