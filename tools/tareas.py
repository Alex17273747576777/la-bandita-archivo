#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TAREAS · el extractor del archivo: de las piezas al tablero, sin copiar a mano.

Hoy las tareas de la casa viven donde deben vivir —dentro de la pieza que las
engendra, como líneas `#task 004 · ...`— pero eso las vuelve invisibles para quien
no abre los documentos uno por uno. Este programa las cosecha, comprueba que la
numeración no tenga huecos ni repetidos y escribe el tablero en `docs/TAREAS.md`.

Qué hace, en una frase: lee las piezas vivas, saca las tareas, y publica un
tablero que se puede leer de arriba abajo.

Qué no hace: no inventa tareas, no las cierra por su cuenta y no toca las
piezas. Cerrar una tarea es un acto humano que se escribe en la pieza siguiente.

Uso:
    python3 tools/tareas.py              # escribe docs/TAREAS.md y resume por pantalla
    python3 tools/tareas.py --json       # salida legible por máquina
    python3 tools/tareas.py --revisar    # solo comprueba, no escribe (para la CI)

── Lo que `--revisar` comprueba, y lo que no puede ─────────────────────────────
Las piezas del ciclo vivo (`Arena-Reimagined/01-PUBLICACIONES/<canal>/*.md`) NO
están versionadas en este repositorio: medido el 2026-11-17 sobre el árbol de
`main` (19.005 blobs), esa carpeta no existe. El tablero `docs/TAREAS.md` sí está
versionado, o sea que el repo publica un derivado sin publicar su materia prima.

Consecuencia honesta: en un clon limpio (y por tanto en la CI) la correspondencia
tablero↔piezas **no se puede comprobar**. Antes este programa salía 1 con el
mensaje «no hay ninguna tarea declarada en las piezas vivas», que sonaba a
defecto de contenido y era otra cosa: faltaba la carpeta entera, no las tareas.
La vara estuvo roja por eso en cada push desde el 2026-11-15.

Ahora `--revisar` hace dos cosas separadas y las dice por su nombre:
  1. comprueba el tablero contra sí mismo (lo que SÍ se puede hacer sin piezas);
  2. si las piezas están, comprueba además que el tablero les corresponde.
Cuando faltan las piezas, el punto 2 se declara en el informe y la última línea
dice lo que se comprobó de verdad. No se simula un verde: se acota.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLICACIONES = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
SALIDA = RAIZ / "docs" / "TAREAS.md"

TAREA = re.compile(r"^#task\s+(\d+)\s*·\s*(.+?)\s*$", re.M)
FECHA = re.compile(r"(\d{4}-\d{2}-\d{2})")
FILA = re.compile(r"^\|\s*(\d{3})\s*\|(.*)$")
TLDR = re.compile(r"\*\*TL;DR —\*\*\s+(\d+)\s+tareas abiertas en\s+(\d+)\s+piezas vivas")
CANALES = {"Facebook-dominicano-ES": "Facebook", "WhatsApp-dominicano-ES": "WhatsApp"}


def piezas() -> list[Path]:
    """Solo las piezas del ciclo vivo: la raíz de cada canal, sin LEEME ni archivo."""
    salida: list[Path] = []
    for carpeta in CANALES:
        d = PUBLICACIONES / carpeta
        if not d.exists():
            continue
        salida += [p for p in sorted(d.glob("*.md"))
                   if not p.name.lower().startswith(("leeme", "readme"))]
    return salida


def cosechar() -> list[dict]:
    halladas: list[dict] = []
    for p in piezas():
        texto = p.read_text(encoding="utf-8", errors="replace")
        canal = next((v for k, v in CANALES.items() if k in str(p)), "?")
        m = FECHA.search(p.name)
        for num, cuerpo in TAREA.findall(texto):
            halladas.append({
                "id": int(num),
                "texto": re.sub(r"\s+", " ", cuerpo).strip(),
                "pieza": p.name,
                "canal": canal,
                "corte": m.group(1) if m else "",
            })
    return sorted(halladas, key=lambda t: (t["id"], t["canal"]))


def piezas_declaradas_por_el_tablero() -> int:
    """Con cuántas piezas vivas dice el TL;DR que se generó el tablero. Cero si no lo dice."""
    if not SALIDA.exists():
        return 0
    m = TLDR.search(SALIDA.read_text(encoding="utf-8"))
    return int(m.group(2)) if m else 0


def revisar(tareas: list[dict], hay_piezas: bool) -> tuple[list[str], list[str]]:
    """La numeración es **por pieza**: cada pieza numera sus propias tareas desde 001.

    Se comprueba, entonces, dentro de cada pieza: que no haya huecos ni repetidos, y
    —regla 2 del tablero, que hasta el 2026-11-17 estaba escrita en el documento y no
    en el código— que un mismo número dentro de una misma pieza no diga dos cosas
    distintas. Entre piezas distintas el mismo número SÍ puede repetirse con otro
    texto: eso lo dice la regla de numeración por pieza y no es fallo.

    Se informa aparte —sin bloquear— de las piezas que empezaron a numerar en otro
    sitio, porque la regla se fijó el 3-nov-2026 y las piezas publicadas antes no se
    retocan: se declaran.
    """
    fallos: list[str] = []
    avisos: list[str] = []
    if not tareas:
        # Dos cosas distintas que hasta el 2026-11-17 se decían con el mismo mensaje:
        #   · hay piezas y ninguna declara #task  → fallo (se borraron las tareas o cambió el formato)
        #   · no hay ninguna pieza en este clon   → no es un fallo de contenido, es falta de materia
        #     prima: la carpeta del ciclo vivo no está versionada. Se declara con la cifra que el
        #     propio tablero trae, para que la ausencia se vea cuantificada y no pase por verde mudo.
        if hay_piezas:
            return ["hay piezas vivas pero ninguna declara tareas #task: o se borraron o cambió el formato"], []
        declaradas = piezas_declaradas_por_el_tablero()
        avisos.append(
            f"sin piezas vivas en este clon: la numeración y la correspondencia no se comprueban aquí. "
            f"El tablero publicado dice que se generó con {declaradas} piezas vivas en "
            f"{PUBLICACIONES.relative_to(RAIZ)}, carpeta que no está versionada en el repositorio."
        )
        return [], avisos
    por_pieza: dict[str, list[dict]] = {}
    for t in tareas:
        por_pieza.setdefault(t["pieza"], []).append(t)
    for pieza, lista in sorted(por_pieza.items()):
        ids = sorted(t["id"] for t in lista)
        if len(set(ids)) != len(ids):
            fallos.append(f"{pieza[:40]}: número de tarea repetido dentro de la misma pieza")
        textos = {}
        for t in lista:
            textos.setdefault(t["id"], set()).add(t["texto"])
        for num, dichos in sorted(textos.items()):
            if len(dichos) > 1:
                fallos.append(f"{pieza[:40]}: la tarea {num:03d} dice {len(dichos)} cosas distintas en la misma pieza")
        for a, b in zip(sorted(set(ids)), sorted(set(ids))[1:]):
            if b != a + 1:
                fallos.append(f"{pieza[:40]}: hueco en la numeración, se salta de {a:03d} a {b:03d}")
        if ids[0] != 1:
            avisos.append(f"{pieza[:40]}: numera desde {ids[0]:03d} y no desde 001 (pieza publicada antes de la regla; se declara, no se retoca)")
    return fallos, avisos


def tareas_publicadas() -> int:
    """Cuántas tareas hay en el tablero que ya está escrito. Cero si no existe."""
    if not SALIDA.exists():
        return 0
    return sum(1 for l in SALIDA.read_text(encoding="utf-8").splitlines()
               if l.startswith("| ") and l[2:5].isdigit())


def leer_tablero() -> tuple[list[tuple[int, str]], list[str]]:
    """El tablero versionado, leído contra sí mismo: lo que se puede comprobar sin piezas.

    Devuelve las filas `(número, texto)` y los fallos de forma. No compara con las
    piezas: eso es `corresponder()`.
    """
    fallos: list[str] = []
    if not SALIDA.exists():
        return [], [f"no existe {SALIDA.relative_to(RAIZ)}: el tablero no está versionado"]
    lineas = SALIDA.read_text(encoding="utf-8").splitlines()
    if "| # | Tarea | Origen | Corte |" not in lineas:
        fallos.append("el tablero no tiene la cabecera que genera este programa: o se editó a mano o cambió el formato")
    tldr = TLDR.search("\n".join(lineas))
    filas: list[tuple[int, str]] = []
    for l in lineas:
        if not l.startswith("| ") or l[2:5] == "---":
            continue
        celdas = [x.strip() for x in l.strip("|").split("|")]
        if len(celdas) != 4:
            fallos.append(f"fila con {len(celdas)} columnas en vez de 4: {l[:60]}")
            continue
        if not re.fullmatch(r"\d{3}", celdas[0]):
            continue                      # no es una fila de tarea (cabecera, separador)
        if not celdas[1]:
            fallos.append(f"la tarea {celdas[0]} tiene el texto vacío")
        filas.append((int(celdas[0]), celdas[1]))
    if not filas:
        fallos.append("el tablero no tiene ninguna fila de tarea: está vacío o no es el que genera este programa")
    if not tldr:
        fallos.append("el tablero no declara su TL;DR con el número de tareas")
    elif int(tldr.group(1)) != len(filas):
        fallos.append(f"el TL;DR dice {tldr.group(1)} tareas y la tabla tiene {len(filas)} filas: el resumen miente")
    return filas, fallos


def corresponder(filas: list[tuple[int, str]], tareas: list[dict]) -> list[str]:
    """Con las piezas delante: ¿el tablero les corresponde? Es la comprobación que faltaba.

    Hasta el 2026-11-17 `--revisar` miraba la numeración de las piezas y nunca
    comparaba el resultado con el tablero publicado: un tablero viejo pasaba en verde.
    """
    fallos: list[str] = []
    del_tablero = sorted(filas)
    de_las_piezas = sorted((t["id"], t["texto"]) for t in tareas)
    if del_tablero == de_las_piezas:
        return fallos
    if len(del_tablero) != len(de_las_piezas):
        fallos.append(f"tablero desactualizado: {len(del_tablero)} filas publicadas y {len(de_las_piezas)} tareas en las piezas vivas; corré `make tareas`")
    solo_tablero = sorted(set(del_tablero) - set(de_las_piezas))
    solo_piezas = sorted(set(de_las_piezas) - set(del_tablero))
    for num, texto in solo_tablero[:5]:
        fallos.append(f"el tablero publica {num:03d} · {texto[:50]} y ninguna pieza viva lo declara")
    for num, texto in solo_piezas[:5]:
        fallos.append(f"las piezas declaran {num:03d} · {texto[:50]} y el tablero no lo publica")
    return fallos


def escribir(tareas: list[dict], fallos: list[str], avisos: list[str]) -> None:
    # Guarda contra el vaciado. Pasó de verdad el 2026-11-17: en un clon que no tiene las piezas
    # vivas, esta función escribió un tablero de 0 tareas —borrando las 90 que había— y el aviso
    # «no hay ninguna tarea declarada» llegó DESPUÉS de escribir, con el fichero ya destruido.
    # Un generador que no encuentra su materia prima no publica un resultado vacío: se niega.
    if not tareas:
        anteriores = tareas_publicadas()
        if anteriores:
            raise SystemExit(
                f"NO se escribe el tablero: {SALIDA.relative_to(RAIZ)} tiene {anteriores} tareas y no "
                f"apareció ninguna pieza viva en {PUBLICACIONES.relative_to(RAIZ)}. O el clon está "
                "incompleto o los canales se movieron. Vaciarlo no es cosechar: es perderlo. "
                "Para regenerarlo de verdad hacen falta las piezas; para dejarlo como está, no "
                "tocar nada."
            )
    ids = sorted({t["id"] for t in tareas})
    filas = "\n".join(
        f"| {t['id']:03d} | {t['texto']} | {t['canal']} · {t['pieza'][:2]} | {t['corte']} |"
        for t in tareas)
    rango = f"{ids[0]:03d} a {ids[-1]:03d}" if ids else "—"
    estado = "Numeración sin huecos ni repetidos dentro de cada pieza." if not fallos else "Numeración CON incidencias: ver la nota al pie."
    nota_avisos = ("\n".join(f"> **Declarado:** {a}" for a in avisos)
                   or "> Ninguna pieza fuera de la regla de numeración.")
    cuerpo = f"""# TABLERO DE TAREAS

*Generado por `tools/tareas.py` el día que se corre. No se edita a mano: se vuelve a correr.*

**TL;DR —** {len(tareas)} tareas abiertas en {len(piezas())} piezas vivas, numeradas dentro de cada pieza, de {rango}. {estado} El tablero se regenera con `make tareas` y la integración continua comprueba que no haya huecos.

## De dónde salen

Cada tarea vive en la pieza que la engendra, como una línea `#task NNN · texto`. Esa es la regla de la casa: **una tarea no se guarda en una lista aparte, se escribe dentro del documento que la justifica**, para que quien lea la pieza vea qué quedó pendiente y por qué. Este tablero no es la fuente: es la vista.

## Las tareas abiertas

| # | Tarea | Origen | Corte |
|---|---|---|---|
{filas}

## Numeración: la regla y lo declarado

{nota_avisos}

La numeración es **por pieza**, no global: cada pieza numera sus tareas desde 001 porque la compuerta de novedad (M28) las cuenta dentro de la pieza. Por eso la misma cifra puede aparecer en dos piezas distintas y no es un error: la tarea se identifica por su número **y** su pieza.

## Cómo se cierra una tarea

No se borra de aquí. Se cumple, y la pieza siguiente lo cuenta con su medición al lado. Cuando una tarea se cumple, su número deja de aparecer en las piezas nuevas y el tablero se encoge solo en la próxima corrida. Una tarea que llevas tres meses sin hacer no es una tarea: es una decisión que hay que tomar y decir en voz alta.

## Las comprobaciones que hace este programa

Las cuatro están en el código; ninguna se anuncia aquí sin estar escrita abajo.

1. **Sin huecos**: dentro de cada pieza la numeración sube de uno en uno; un salto se declara aquí y no se disimula.
2. **Sin textos contradictorios**: dentro de una misma pieza, un número no puede decir dos cosas distintas. Entre piezas distintas el mismo número sí puede repetirse con otro texto —la numeración es por pieza— y por eso la columna *Origen* de esta tabla, que sólo trae las dos primeras letras del fichero, no basta para distinguirlas: hace falta abrir la pieza.
3. **Tablero íntegro**: la tabla tiene cuatro columnas, ids de tres dígitos, ningún texto vacío y el TL;DR dice el mismo número de tareas que filas hay.
4. **Tablero al día**: con las piezas delante, las filas publicadas y las tareas cosechadas son las mismas, una por una.

*Y la que no se puede hacer aquí, dicha en voz alta: las piezas del ciclo vivo no están
versionadas en este repositorio, así que en un clon limpio —y en la integración continua—
las comprobaciones 1, 2 y 4 no tienen materia prima. Ahí corre la 3, y el informe de
`--revisar` declara lo que faltó en vez de dar un verde que no es.*

*La Bandita informa a partir de fuentes fechadas.*
"""
    SALIDA.write_text(cuerpo, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Cosecha las #task de las piezas vivas.")
    ap.add_argument("--json", action="store_true", help="salida legible por máquina")
    ap.add_argument("--revisar", action="store_true", help="comprueba sin escribir el tablero")
    a = ap.parse_args()

    tareas = cosechar()
    hay_piezas = bool(piezas())
    fallos, avisos = revisar(tareas, hay_piezas)
    filas, fallos_tablero = leer_tablero()
    if a.revisar or a.json:
        fallos = fallos + fallos_tablero
        if tareas:
            fallos = fallos + corresponder(filas, tareas)

    if a.json:
        print(json.dumps({"tareas": tareas, "fallos": fallos, "avisos": avisos,
                          "piezas": len(piezas()), "filas_tablero": len(filas)},
                         ensure_ascii=False, indent=1))
        return 0 if not fallos else 1
    if not a.revisar:
        escribir(tareas, fallos, avisos)
        print(f"tablero escrito: {SALIDA.relative_to(RAIZ)} · {len(tareas)} tareas")
    for f in fallos:
        print(f"  ✗ {f}")
    for x in avisos:
        print(f"  · {x}")
    if a.revisar:
        # El informe dice qué se comprobó de verdad. Sin piezas no se puede afirmar que el
        # tablero esté al día: se afirma que está íntegro y se declara lo que faltó.
        if hay_piezas:
            print(f"piezas vivas: {len(piezas())} en {PUBLICACIONES.relative_to(RAIZ)}"
                  + ("" if tareas else " · ninguna declara #task"))
            print(f"correspondencia tablero↔piezas: comprobada ({len(filas)} filas vs {len(tareas)} tareas)")
        else:
            print(f"piezas vivas: 0 — {PUBLICACIONES.relative_to(RAIZ)} no existe en este clon "
                  "(la carpeta no está versionada en el repositorio)")
            print("correspondencia tablero↔piezas: NO comprobable aquí; declarado, no simulado")
        print(f"tablero íntegro: {len(filas)} filas leídas de {SALIDA.relative_to(RAIZ)} · "
              f"{len(fallos_tablero)} fallos de forma")
        print("fallos: NINGUNO" if not fallos else f"fallos: {len(fallos)}")
    print(f"tareas: {len(tareas)} · piezas: {len(piezas())} · incidencias: {len(fallos)} · declaradas: {len(avisos)}")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
