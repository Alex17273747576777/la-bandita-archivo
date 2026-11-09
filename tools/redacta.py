#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REDACTOR · arma una pieza de Facebook con los números puestos por código.

Cómo funciona:
  * La VOZ de la pieza se escribe a mano en docs/almas/NN.md, con marcas {{TABLA}}, {{AGREGADOS}},
    {{FIRMAS}}, {{NUEVOS}}, {{MAS_ESTRELLAS}}, {{SIN_ENTREGA}}, {{DOMINIOS}}.
  * Los NÚMEROS salen de docs/MEDICION-PNN-<fecha>.json, que a su vez sale del censo medido.
  * Este programa une las dos cosas y escribe el archivo de la pieza con su nombre largo.

Qué NO hace:
  * No inventa un dato: si el JSON no lo trae, escribe «aquí no hay».
  * No decide el tema ni el orden: eso está en el alma.
  * No toca la pieza anterior: la reemplaza solo si se le pide --reemplazar, y entonces la mueve
    a _reemplazadas-<fecha>/ para que quede el rastro.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import statistics
import sys
import unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLIC = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES" / "Facebook-dominicano-ES"
ALMAS = RAIZ / "docs" / "almas"
HOY = date.today().isoformat()


# ── números en palabras y en cifras ─────────────────────────────────────────
def miles(n) -> str:
    if n is None:
        return "aquí no hay"
    return f"{n:,}".replace(",", ".")


def letras(n: int) -> str:
    u = ["cero", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
         "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho",
         "diecinueve", "veinte"]
    if n <= 20:
        return u[n]
    if n < 30:
        return ["veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis",
                "veintisiete", "veintiocho", "veintinueve"][n - 21]
    if n < 100:
        d, r = divmod(n, 10)
        dec = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta",
               8: "ochenta", 9: "noventa"}
        return dec[d] + (f" y {u[r]}" if r else "")
    if n < 1000:
        if n == 100:
            return "cien"
        c, r = divmod(n, 100)
        cent = {1: "ciento", 2: "doscientas", 3: "trescientas", 4: "cuatrocientas",
                5: "quinientas", 6: "seiscientas", 7: "setecientas", 8: "ochocientas",
                9: "novecientas"}
        return cent[c] + (f" {letras(r)}" if r else "")
    if n < 1_000_000:
        m, r = divmod(n, 1000)
        return ("mil" if m == 1 else f"{letras(m)} mil") + (f" {letras(r)}" if r else "")
    m, r = divmod(n, 1_000_000)
    return ("un millón" if m == 1 else f"{letras(m)} millones") + (f" {letras(r)}" if r else "")


def fecha_larga(iso: str | None) -> str:
    if not iso:
        return "aquí no hay"
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
             "septiembre", "octubre", "noviembre", "diciembre"]
    a, m, d = iso.split("-")
    return f"{int(d)} de {meses[int(m) - 1]} de {a}"


# ── piezas de texto ────────────────────────────────────────────────────────
def _es_hecho(x: dict) -> bool:
    """Una ficha puede ser de repositorio o de un hecho medido (piezas personales 35–40).

    Las personales no tienen estrellas ni licencia: tienen un hecho y su valor. Se distinguen
    por la forma de la ficha, no por el número de pieza, para que esto siga sirviendo mañana.
    """
    return "repo" not in x and "hecho" in x


def _ficha_linea(i: int, x: dict) -> str:
    if _es_hecho(x):
        v = x.get("valor")
        if v is None or v == "":
            v = "aquí no hay"
        elif isinstance(v, int):
            v = miles(v)
        return f"{i}. **{x['hecho']}** — {v}."
    lic = x.get("licencia") or "sin licencia declarada"
    partes = [
        f"**{x['repo']}**",
        f"★{miles(x.get('stars'))}",
        lic,
        f"nació el {fecha_larga(x.get('nace'))} ({miles(x.get('dias_nace'))} días)",
    ]
    if x.get("ultima_entrega"):
        partes.append(f"última entrega del {fecha_larga(x['ultima_entrega'])}")
    else:
        partes.append("sin ninguna entrega publicada")
    partes.append(f"{miles(x.get('adjuntos_ultima'))} adjuntos y **{miles(x.get('huellas_ultima'))} con suma**")
    if x.get("descargas_ultima"):
        partes.append(f"{miles(x['descargas_ultima'])} descargas en esa entrega")
    if x.get("dias_push") is not None:
        partes.append(f"último empujón hace {miles(x['dias_push'])} días")
    if x.get("abiertas") is not None:
        partes.append(f"{miles(x['abiertas'])} incidencias abiertas")
    return f"{i}. " + " · ".join(partes) + "."


def tabla(fichas: list[dict]) -> str:
    return "\n\n".join(_ficha_linea(i + 1, x) for i, x in enumerate(fichas))


def agregados(d: dict) -> str:
    f = d["fichas"]
    n = len(f)
    if all(_es_hecho(x) for x in f):
        medidos = [x for x in f if x.get("valor") not in (None, "")]
        return (
            f"{letras(n).capitalize()} hechos en la medición de esta pieza, del 9 de noviembre de 2026. "
            f"**{miles(len(medidos))}** traen un valor medido contra su fuente y "
            f"**{miles(n - len(medidos))}** quedan declarados como «aquí no hay», porque no se midieron "
            f"o no se deben medir. Lo que no se midió, aquí no se escribe."
        )
    estrellas = [x["stars"] for x in f if x.get("stars") is not None]
    total = sum(estrellas)
    mediana = int(statistics.median(estrellas)) if estrellas else None
    adj = sum(x.get("adjuntos_ultima") or 0 for x in f)
    hue = sum(x.get("huellas_ultima") or 0 for x in f)
    con_h = [x for x in f if (x.get("huellas_ultima") or 0) > 0]
    dl = sum(x.get("descargas_ultima") or 0 for x in f)
    sin_lic = [x for x in f if not x.get("licencia")]
    activos = [x for x in f if x.get("dias_push") is not None and x["dias_push"] <= 7]
    sin_ent = [x for x in f if not x.get("ultima_entrega")]
    return (
        f"{letras(n).capitalize()} repositorios vivos, medidos el 9 de noviembre de 2026 contra la API "
        f"pública de GitHub. Suman **{miles(total)} estrellas** y **{miles(dl)} descargas** declaradas en "
        f"su última entrega. La mediana de estrellas es **{miles(mediana)}**. "
        f"**{letras(len(con_h)).capitalize()} de {letras(n)}** publican la huella de lo que entregan: "
        f"**{miles(hue)} sumas** repartidas entre **{miles(adj)} adjuntos**. "
        f"**{letras(len(sin_lic)).capitalize()}** no declaran licencia, "
        f"**{letras(len(activos))}** empujaron código en los últimos siete días y "
        f"**{letras(len(sin_ent))}** no han publicado nunca una entrega."
    )


def firmas(d: dict) -> str:
    if all(_es_hecho(x) for x in d["fichas"]):
        return "Esta pieza no mide repositorios: mide hechos. Aquí no hay sumas de comprobación que contar."
    f = [x for x in d["fichas"] if (x.get("huellas_ultima") or 0) > 0]
    if not f:
        return "Ninguno de los medidos publica una sola suma de comprobación. Aquí no hay."
    f.sort(key=lambda x: -(x.get("huellas_ultima") or 0))
    lineas = []
    for x in f:
        lineas.append(
            f"• **{x['repo']}** — {miles(x.get('huellas_ultima'))} sumas de "
            f"{miles(x.get('adjuntos_ultima'))} adjuntos, en una entrega del "
            f"{fecha_larga(x.get('ultima_entrega'))}."
        )
    return "\n".join(lineas)


def nuevos(d: dict, dias: int = 400) -> str:
    f = [x for x in d["fichas"] if x.get("dias_nace") is not None and x["dias_nace"] <= dias]
    if not f:
        return "De los medidos en esta pieza, ninguno nació en el último año. Aquí no hay."
    f.sort(key=lambda x: x["dias_nace"])
    lineas = []
    for x in f:
        lineas.append(
            f"• **{x['repo']}** — {miles(x['dias_nace'])} días de vida, ★{miles(x.get('stars'))}, "
            f"entrega del {fecha_larga(x.get('ultima_entrega'))}, "
            f"{miles(x.get('huellas_ultima'))} sumas de {miles(x.get('adjuntos_ultima'))} adjuntos."
        )
    return "\n".join(lineas)


def extremos(d: dict) -> str:
    if all(_es_hecho(x) for x in d.get("fichas", [])):
        return "Aquí no hay: esta pieza mide hechos, no repositorios."
    f = d["fichas"]
    top = max(f, key=lambda x: x.get("stars") or 0)
    bajo = min(f, key=lambda x: x.get("stars") or 0)
    # «El más viejo» es el que nació hace MÁS días, y se nombra con SUS cifras, no con las de
    # otro: aquí estaba el error que dejaba una cifra ajena pegada a su nombre.
    mas_viejo = max((x for x in f if x.get("dias_nace") is not None), key=lambda x: x["dias_nace"])
    return (
        f"El que más estrellas tiene es **{top['repo']}**, con ★{miles(top.get('stars'))} y "
        f"**{miles(top.get('huellas_ultima'))} sumas** de {miles(top.get('adjuntos_ultima'))} adjuntos. "
        f"El que menos es **{bajo['repo']}**, ★{miles(bajo.get('stars'))}, "
        f"**{miles(bajo.get('huellas_ultima'))} sumas** de {miles(bajo.get('adjuntos_ultima'))}. "
        f"El más viejo de la lista es **{mas_viejo['repo']}**: "
        f"★{miles(mas_viejo.get('stars'))}, {miles(mas_viejo['dias_nace'])} días, "
        f"desde {fecha_larga(mas_viejo.get('nace'))}, "
        f"{miles(mas_viejo.get('huellas_ultima'))} sumas de {miles(mas_viejo.get('adjuntos_ultima'))} adjuntos."
    )


def sin_entrega(d: dict) -> str:
    if all(_es_hecho(x) for x in d.get("fichas", [])):
        return "Aquí no hay: esta pieza mide hechos, no repositorios."
    f = [x for x in d["fichas"] if not x.get("ultima_entrega")]
    if not f:
        return "Todos los medidos en esta pieza han publicado al menos una entrega."
    lineas = [f"• **{x['repo']}** — ★{miles(x.get('stars'))}, nacido el {fecha_larga(x.get('nace'))}." for x in f]
    return "\n".join(lineas)


# ── montaje ────────────────────────────────────────────────────────────────
def cargar_medicion(pieza: str) -> dict:
    for p in sorted(RAIZ.glob(f"docs/MEDICION-P{pieza}-*.json")):
        return json.loads(p.read_text(encoding="utf-8"))
    raise SystemExit(f"falta docs/MEDICION-P{pieza}-*.json — pasa tools/elige.py primero")


def nombre_archivo(alma: str, pieza: str) -> str:
    """El nombre largo de la casa: título en slug, canal, fecha y edición."""
    titulo = ""
    for linea in alma.splitlines():
        if linea.startswith("TITULO:"):
            titulo = linea.split(":", 1)[1].strip()
            break
    slug = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^A-Za-z0-9]+", "-", slug).strip("-")
    return f"{pieza}-{slug}-Facebook-La-Bandita-{HOY}-dominicano-ES.md"


def cifras_por_repo(d: dict) -> str:
    if all(_es_hecho(x) for x in d.get("fichas", [])):
        return "Aquí no hay: esta pieza mide hechos, no repositorios."
    """Una tabla de verdad: cada repositorio con sus propias cifras, sin prosa alrededor.
    Así ninguna cifra puede quedar pegada al nombre de otro: la columna es la fila."""
    claves = [("repo", "Repositorio"), ("stars", "Estrellas"), ("dias_nace", "Días de vida"),
              ("dias_push", "Días sin empujar"), ("adjuntos_ultima", "Adjuntos"),
              ("huellas_ultima", "Sumas"), ("descargas_ultima", "Descargas"),
              ("licencia", "Licencia"), ("ultima_entrega", "Última entrega")]
    cabecera = "| " + " | ".join(t for _, t in claves) + " |"
    raya = "|" + "|".join("---" for _ in claves) + "|"
    filas = []
    for x in d["fichas"]:
        celdas = []
        for k, _ in claves:
            v = x.get(k)
            if k == "repo":
                celdas.append(f"`{v}`")
            elif k == "licencia":
                celdas.append(str(v) if v else "sin declarar")
            elif k == "ultima_entrega":
                celdas.append(str(v) if v else "nunca")
            elif isinstance(v, int):
                celdas.append(miles(v))
            else:
                celdas.append("aquí no hay")
        filas.append("| " + " | ".join(celdas) + " |")
    return "\n".join([cabecera, raya] + filas)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Arma las piezas desde el alma y la medición.")
    ap.add_argument("piezas", nargs="+", help="NN de cada pieza")
    ap.add_argument("--reemplazar", action="store_true", help="mueve la pieza vieja a _reemplazadas")
    ap.add_argument("--ver", action="store_true", help="solo imprimir, no escribir")
    args = ap.parse_args()

    for pieza in args.piezas:
        pieza = pieza.zfill(2)
        alma_path = ALMAS / f"{pieza}.md"
        if not alma_path.exists():
            print(f"  {pieza}: sin alma todavía — se salta")
            continue
        alma = alma_path.read_text(encoding="utf-8")
        d = cargar_medicion(pieza)

        cuerpo = alma
        reemplazos = {
            "{{TABLA}}": tabla(d["fichas"]),
            "{{AGREGADOS}}": agregados(d),
            "{{FIRMAS}}": firmas(d),
            "{{NUEVOS}}": nuevos(d),
            "{{EXTREMOS}}": extremos(d),
            "{{SIN_ENTREGA}}": sin_entrega(d),
            "{{TABLA_CIFRAS}}": cifras_por_repo(d),
            "{{N}}": letras(len(d["fichas"])),
            "{{TOTAL_ESTRELLAS}}": miles(sum(x.get("stars") or 0 for x in d["fichas"])),
        }
        for marca, valor in reemplazos.items():
            cuerpo = cuerpo.replace(marca, valor)

        # El encabezado TITULO:/RESUMEN: es para el nombre del archivo y el LEEME, no para el cuerpo.
        cuerpo = re.sub(r"^TITULO:.*\n", "", cuerpo, flags=re.MULTILINE)
        cuerpo = re.sub(r"^RESUMEN:.*\n", "", cuerpo, flags=re.MULTILINE)

        dest = PUBLIC / nombre_archivo(alma, pieza)
        print(f"  {pieza}: {len(cuerpo)} caracteres → {dest.name[:70]}…")
        if args.ver:
            continue

        if args.reemplazar:
            viejos = [p for p in PUBLIC.glob(f"{pieza}-*.md")
                      if p.suffix == ".md" and not p.name.startswith("_")
                      and "Comentario-fijado" not in p.name and p.name != dest.name]
            if viejos:
                saco = PUBLIC / f"_reemplazadas-{HOY}"
                saco.mkdir(exist_ok=True)
                for v in viejos:
                    shutil.move(str(v), saco / v.name)
                    print(f"       vieja movida: {v.name[:60]}…")
        dest.write_text(cuerpo, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
