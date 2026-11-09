#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""COTEJO · comprueba que cada cifra de una pieza exista de verdad en su medición.

Qué hace:
  * Lee la pieza publicada y su docs/MEDICION-PNN-<fecha>.json.
  * Saca de la pieza todo número escrito con separador de miles (205.629), todo número de
    cuatro cifras o más (20028) y las cifras escritas en palabras que la pieza usa
    («setecientos treinta y ocho días»).
  * Comprueba que cada una aparezca en el JSON de esa pieza: como valor de un campo, como
    suma de varios, como diferencia, o como mediana.
  * Lista las que no aparecen. Esas son las que hay que mirar a mano.

Qué NO hace:
  * No corrige nada: reporta.
  * No da por bueno un número solo porque exista: un número puede existir y estar mal
    atribuido. Eso lo dice el informe aparte (tools/coteja.py --atribucion).
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLIC = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES" / "Facebook-dominicano-ES"

UNIDADES = {
    "cero": 0, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
    "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12, "trece": 13,
    "catorce": 14, "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18,
    "diecinueve": 19, "veinte": 20, "veintiuno": 21, "veintiún": 21, "veintidós": 22,
    "veintitrés": 23, "veinticuatro": 24, "veinticinco": 25, "veintiséis": 26,
    "veintisiete": 27, "veintiocho": 28, "veintinueve": 29,
}
DECENAS = {"treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
           "ochenta": 80, "noventa": 90}
CENTENAS = {"cien": 100, "ciento": 100, "doscientas": 200, "doscientos": 200,
            "trescientas": 300, "trescientos": 300, "cuatrocientas": 400, "cuatrocientos": 400,
            "quinientas": 500, "quinientos": 500, "seiscientas": 600, "seiscientos": 600,
            "setecientas": 700, "setecientos": 700, "ochocientas": 800, "ochocientos": 800,
            "novecientas": 900, "novecientos": 900}


def palabras_a_numero(texto: str) -> int | None:
    """«doscientas cinco mil seiscientas veintinueve» → 205629. Devuelve None si no se entiende."""
    total, actual, vistos = 0, 0, False
    for palabra in re.split(r"[\s-]+", texto.lower()):
        if palabra in UNIDADES:
            actual += UNIDADES[palabra]; vistos = True
        elif palabra in DECENAS:
            actual += DECENAS[palabra]; vistos = True
        elif palabra in CENTENAS:
            actual += CENTENAS[palabra]; vistos = True
        elif palabra in {"mil"}:
            actual = (actual or 1) * 1000; total += actual; actual = 0; vistos = True
        elif palabra in {"millón", "millon"}:
            actual = (actual or 1) * 1_000_000; total += actual; actual = 0; vistos = True
        elif palabra in {"millones"}:
            actual = (actual or 1) * 1_000_000; total += actual; actual = 0; vistos = True
        elif palabra in {"y", "de", "días", "dias", "sumas", "adjuntos", "estrellas"}:
            continue
        else:
            return None
    return total + actual if vistos else None


def universo(d: dict) -> set[int]:
    """Todos los números que la medición puede respaldar."""
    f = d["fichas"]
    nums: set[int] = {len(f)}
    claves = ["stars", "forks", "dias_nace", "dias_push", "entregas", "adjuntos_ultima",
              "huellas_ultima", "descargas_ultima", "abiertas", "rel_dias"]
    for x in f:
        for k in claves:
            v = x.get(k)
            if isinstance(v, int):
                nums.add(v)
    for k in claves:
        vals = [x.get(k) for x in f if isinstance(x.get(k), int)]
        if not vals:
            continue
        nums.add(sum(vals))
        nums.add(int(statistics.median(vals)))
        nums.add(min(vals))
        nums.add(max(vals))
        # diferencias entre los dos extremos: «trescientas treinta y cinco mil contra mil setecientas»
        nums.add(max(vals) - min(vals))
    # sumas de dos fichas, que es como la pieza cita «los dos más grandes»
    orden = sorted([x.get("stars") or 0 for x in f], reverse=True)
    if len(orden) >= 2:
        nums.add(orden[0] + orden[1])
    # conteos de subconjuntos
    nums.add(sum(1 for x in f if (x.get("huellas_ultima") or 0) > 0))
    nums.add(sum(1 for x in f if not x.get("ultima_entrega")))
    nums.add(sum(1 for x in f if not x.get("licencia")))
    nums.add(sum(1 for x in f if x.get("dias_push") is not None and x["dias_push"] <= 7))
    nums.add(sum(1 for x in f if x.get("dias_nace") is not None and x["dias_nace"] <= 365))
    nums.add(sum(1 for x in f if x.get("dias_nace") is not None and x["dias_nace"] <= 120))
    return nums


# Números que no salen de la medición de la pieza pero son legítimos: el tamaño del censo,
# los umbrales de los filtros y los años. Un año no es una cifra medida.
CONSTANTES = {3125, 3284, 120, 60, 365, 180, 900, 4000, 45000, 6000, 0}


def es_anio(v: int) -> bool:
    return 1900 <= v <= 2100


def _volcar(grupo: list[str], salida: list[tuple[str, int]], parser) -> None:
    """Añade el grupo si es un número de verdad. Si no, prueba a quitarle palabras por delante
    (un «y» suelto, un «mil» colgando) hasta que parsee."""
    for desde in range(0, min(3, len(grupo))):
        trozo = grupo[desde:]
        valor = parser(" ".join(trozo))
        if valor and valor >= 10:
            salida.append((" ".join(trozo), valor))
            return


def cifras_de(texto: str) -> list[tuple[str, int]]:
    salida: list[tuple[str, int]] = []
    # 205.629 o 1.554
    for m in re.finditer(r"\b\d{1,3}(?:\.\d{3})+\b", texto):
        salida.append((m.group(0), int(m.group(0).replace(".", ""))))
    # 20028, 7776 (cuatro cifras o más, sin separador)
    for m in re.finditer(r"\b\d{4,}\b", texto):
        crudo = m.group(0)
        if "." in crudo:
            continue
        salida.append((crudo, int(crudo)))
    # palabras: solo cuando van seguidas de una unidad medida («… estrellas», «… adjuntos»).
    # Así no se confunde «los dieciocho, uno por uno» con un número, ni «veinte» suelto.
    nombres = "|".join(sorted(list(CENTENAS) + list(DECENAS) + list(UNIDADES) +
                              ["mil", "millón", "millon", "millones", "y"], key=len, reverse=True))
    unidades = r"(estrellas|adjuntos|sumas|descargas|d[ií]as|repositorios|incidencias|entregas)"
    patron = re.compile(rf"((?:(?:{nombres})[\s-]+){{1,9}}){unidades}")
    for m in patron.finditer(texto.lower()):
        valor = palabras_a_numero(m.group(1))
        if valor and valor >= 10:
            salida.append((f"{m.group(1).strip()} {m.group(2)}", valor))
    return salida


def atribucion(pieza: str, d: dict) -> list[str]:
    """Comprueba que las cifras que van pegadas a un repositorio sean las de ESE repositorio.

    Se busca cada «**dueno/nombre**» y se miran los 220 caracteres siguientes: cada número que
    aparezca ahí tiene que estar entre los campos de ese repositorio. Si el número existe en la
    pieza pero es de otro, esto lo saca.
    """
    por_repo = {x["repo"]: x for x in d["fichas"]}
    fallos: list[str] = []
    cue = [p for p in PUBLIC.glob(f"{pieza}-*Facebook*.md")
           if not p.name.startswith("_") and "Comentario-fijado" not in p.name]
    for a in cue:
        texto = a.read_text(encoding="utf-8")
        for m in re.finditer(r"\*\*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\*\*", texto):
            repo = m.group(1)
            ficha = por_repo.get(repo)
            if ficha is None:
                continue
            validos = {v for k, v in ficha.items()
                       if isinstance(v, int) and k in
                       ("stars", "forks", "dias_nace", "dias_push", "entregas",
                        "adjuntos_ultima", "huellas_ultima", "descargas_ultima", "abiertas")}
            ventana = texto[m.end(): m.end() + 220]
            for crudo, valor in cifras_de(ventana):
                if valor in CONSTANTES or es_anio(valor) or valor in validos:
                    continue
                # Una cifra dentro de la ventana puede ser de la frase siguiente («entre los dos
                # hay trescientas veces más»). Solo se marca si el repo va seguido de «,» o «—»
                # y la cifra aparece ANTES del punto que cierra la frase.
                # La ventana no puede pasar del final de la frase NI del siguiente repositorio
                # en negrita: si no, las cifras del vecino se le atribuyen a este.
                cortes = [c for c in (ventana.find(". "), ventana.find("**")) if c >= 0]
                corte = min(cortes) if cortes else -1
                trozo = ventana if corte < 0 else ventana[:corte]
                if crudo not in trozo:
                    continue
                fallos.append(f"{repo}: «{crudo}» = {valor:,} no es un campo suyo".replace(",", "."))
    return fallos


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Coteja las cifras de una pieza contra su medición.")
    ap.add_argument("piezas", nargs="*")
    ap.add_argument("--todo", action="store_true", help="todas las piezas que tengan medición")
    args = ap.parse_args()

    piezas = args.piezas
    if args.todo or not piezas:
        piezas = sorted({p.stem.split("-")[1].replace("P", "")
                         for p in RAIZ.glob("docs/MEDICION-P*-2026-11-09.json")})

    total_revisadas = 0
    total_fuera = 0
    for pieza in piezas:
        pieza = pieza.zfill(2)
        med = next(iter(sorted(RAIZ.glob(f"docs/MEDICION-P{pieza}-*.json"))), None)
        if not med:
            print(f"  {pieza}: sin medición, se salta")
            continue
        d = json.loads(med.read_text(encoding="utf-8"))
        validos = universo(d)
        cue = [p for p in PUBLIC.glob(f"{pieza}-*Facebook*.md")
               if not p.name.startswith("_") and "Comentario-fijado" not in p.name]
        fij = [p for p in PUBLIC.glob(f"{pieza}-Comentario-fijado-*.md") if not p.name.startswith("_")]
        fuera: list[tuple[str, str, int]] = []
        revisadas = 0
        for etiqueta, archivos in (("cuerpo", cue), ("fijado", fij)):
            for a in archivos:
                texto = a.read_text(encoding="utf-8")
                for crudo, valor in cifras_de(texto):
                    revisadas += 1
                    if valor in CONSTANTES or es_anio(valor):
                        continue
                    if valor not in validos:
                        fuera.append((etiqueta, crudo, valor))
        total_revisadas += revisadas
        total_fuera += len(fuera)
        atri = atribucion(pieza, d)
        marca = "✓" if not fuera and not atri else "✗"
        print(f"{marca} {pieza}: {revisadas} cifras revisadas · {len(fuera)} sin respaldo · "
              f"{len(atri)} mal atribuidas")
        for etiqueta, crudo, valor in fuera[:8]:
            print(f"     · {etiqueta}: «{crudo}» = {valor:,}".replace(",", "."))
        if len(fuera) > 8:
            print(f"     · … y {len(fuera) - 8} más")
        for f in atri[:8]:
            print(f"     · atribución: {f}")
        if len(atri) > 8:
            print(f"     · … y {len(atri) - 8} más de atribución")
        total_fuera += len(atri)

    print(f"\nTOTAL: {total_revisadas} cifras revisadas · {total_fuera} sin respaldo")
    return 0 if total_fuera == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv))
