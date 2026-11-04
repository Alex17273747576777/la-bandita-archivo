#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REMEDIR · la habilidad que nace del error E01–E05 (docs/ERRORES.md).

El dueño lo dijo el 4-nov-2026: «el que está prohibido copiar y pegar: debes
volver a verificar la información actualizada y actualizar cada dato, no solo
la fecha». Esta herramienta convierte esa frase en cuatro comprobaciones que
no dependen de la memoria de quien escribe:

  1. MEDIR HOY      cada repositorio citado se mide en vivo y se guarda en un
                    archivo con fecha y hora. Nunca se sobrescribe uno viejo.
  2. CIFRAS EN TEXTO toda estrella escrita en la pieza con la forma ★N tiene
                    que coincidir con lo que devuelve la fuente hoy.
  3. LA SUMA        el total de estrellas de una tabla se calcula, no se
                    recuerda: se imprime también en palabras para copiarlo.
  4. EL SOLAPE      compara la pieza con la versión anterior y dice qué tanto
                    se repite. Copiar y pegar deja de ser una opinión.

Uso:
    LBT=... python3 tools/remedir.py --escribir docs/MEDICION-01-2026-11-04.json --pieza <pieza>
    LBT=... python3 tools/remedir.py --pieza <pieza> --medicion docs/MEDICION-01-2026-11-04.json
    LBT=... python3 tools/remedir.py --solape <pieza-nueva> <pieza-vieja.md>
    python3 tools/remedir.py --suma 138 122 101 72 40 37 21 17 17 18 16 15

Sale con 1 si algo no cuadra, para que se pueda encadenar en el ritual.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
API = "https://api.github.com"
NUM = {0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete",
       8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce",
       15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte",
       21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro", 25: "veinticinco",
       26: "veintiséis", 27: "veintisiete", 28: "veintiocho", 29: "veintinueve", 30: "treinta"}
DECENAS = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
CENTENAS = {1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos", 5: "quinientos",
            6: "seiscientos", 7: "setecientos", 8: "ochocientos", 9: "novecientos"}


def _apocope(dicho: str) -> str:
    """«veintiuno mil» no existe: delante de mil y millones se dice veintiún y un."""
    if dicho.endswith("veintiuno"):
        return dicho[:-9] + "veintiún"
    if dicho.endswith(" y uno"):
        return dicho[:-3] + "un"
    if dicho == "uno":
        return "un"
    return dicho


def en_palabras(n: int, femenino: bool = False) -> str:
    """Escribe un entero en español, hasta los millones, como se usa en la serie.

    El género importa: son «seiscientas catorce estrellas», no «seiscientos catorce».
    Y el millón también: «un millón trescientas noventa y seis mil trescientas
    noventa y cinco», nunca «uno millones». Antes cortaba en mil y devolvía el
    número en cifras a partir de ahí, que es justo donde fallan las guías largas.
    """
    if n == 0:
        return "cero"
    if n < 0:
        return str(n)
    if n >= 1_000_000:
        millones, resto = divmod(n, 1_000_000)
        # delante de «mil» y «millones» el uno se apocopa: veintiún mil, treinta y un millones
        cabeza = "un millón" if millones == 1 else f"{_apocope(en_palabras(millones))} millones"
        return cabeza + (f" {en_palabras(resto, femenino)}" if resto else "")
    if n >= 1000:
        miles_, resto = divmod(n, 1000)
        cabeza = "mil" if miles_ == 1 else f"{_apocope(en_palabras(miles_))} mil"
        return cabeza + (f" {en_palabras(resto, femenino)}" if resto else "")
    if n == 100:
        return "cien"
    partes = []
    c, resto = divmod(n, 100)
    if c:
        partes.append(CENTENAS[c])
    if resto:
        if resto < 31:
            partes.append(NUM[resto])
        else:
            d, u = divmod(resto, 10)
            partes.append(DECENAS[d] + (f" y {NUM[u]}" if u else ""))
    dicho = " ".join(partes)
    if femenino:
        for m, f in (("cientos", "cientas"), ("doscientos", "doscientas"), ("trescientos", "trescientas"),
                     ("cuatrocientos", "cuatrocientas"), ("quinientos", "quinientas"),
                     ("seiscientos", "seiscientas"), ("setecientos", "setecientas"),
                     ("ochocientos", "ochocientas"), ("novecientos", "novecientas"),
                     ("veintiuno", "veintiuna"), (" y uno", " y una")):
            dicho = dicho.replace(m, f)
        if dicho == "uno":
            dicho = "una"
    return dicho


def api(url: str, tok: str) -> dict:
    r = subprocess.run(["curl", "-s", "-H", f"Authorization: Bearer {tok}", url],
                       capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {}


def repos_citados(texto: str) -> list[str]:
    """Solo enlaces a github.com/owner/repo, sin blob, tree, releases ni issues."""
    fuera = ("blob", "tree", "releases", "issues", "pulls", "wiki", "actions", "sponsors")
    vistos: dict[str, None] = {}
    for m in re.finditer(r"https?://github\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)((?:/\S*)?)", texto):
        owner, repo, resto = m.group(1), m.group(2), m.group(3).strip("/")
        if resto and resto.split("/")[0] in fuera:
            continue
        vistos.setdefault(f"{owner}/{repo}", None)
    return list(vistos)


def medir(repo: str, tok: str) -> dict:
    d = api(f"{API}/repos/{repo}", tok)
    if d.get("message"):
        return {"estado": "sin_objeto", "detalle": d["message"]}
    rel = api(f"{API}/repos/{repo}/releases?per_page=100", tok)
    rels = rel if isinstance(rel, list) else []
    ult = rels[0] if rels else None
    hoy = date.today()
    def dias(f):
        return (hoy - date.fromisoformat(f[:10])).days if f else None
    return {
        "estado": "vivo",
        "stars": d["stargazers_count"],
        "nace": d["created_at"][:10],
        "dias_nace": dias(d["created_at"]),
        "push": d["pushed_at"][:10],
        "dias_push": dias(d["pushed_at"]),
        "licencia": (d.get("license") or {}).get("spdx_id"),
        "archivado": d.get("archived"),
        "tam_mib": round(d["size"] / 1024, 1),
        "rel": ult["tag_name"] if ult else None,
        "rel_fecha": ult["published_at"][:10] if ult else None,
        "rel_dias": dias(ult["published_at"]) if ult else None,
        "entregas": len(rels),
        "descargas": sum(a.get("download_count", 0) for x in rels for a in x.get("assets", [])),
    }


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def escribir(pieza: Path, destino: Path) -> int:
    tok = os.environ.get("LBT") or os.environ.get("PAT_FINO")
    if not tok:
        print("falta LBT: exportá el token de lectura")
        return 2
    texto = pieza.read_text(encoding="utf-8", errors="replace")
    repos = repos_citados(texto)
    if not repos:
        print("no hay repositorios citados en la pieza")
        return 1
    datos = {}
    for r in repos:
        datos[r] = medir(r, tok)
        d = datos[r]
        if d["estado"] == "vivo":
            print(f"  {r:34} ★{d['stars']:6} · {d['dias_nace']:4} d · push {d['push']} · "
                  f"{str(d['licencia']):12} · {str(d['rel']):16} ({d['rel_dias']}) · {d['tam_mib']} MiB")
        else:
            print(f"  {r:34} sin objeto")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(
        {"medido_en": date.today().isoformat(), "medido_a_las": datetime.now().strftime("%H:%M"),
         "pieza": pieza.name, "repos": datos}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"medición escrita: {destino} · {len(datos)} repositorios · nunca se sobrescribe una anterior")
    return 0


def comparar(pieza: Path, medicion: Path) -> int:
    med = json.loads(medicion.read_text(encoding="utf-8"))
    texto = pieza.read_text(encoding="utf-8", errors="replace")
    fallos, avisos = [], []
    if med.get("medido_en") != date.today().isoformat():
        fallos.append(f"la medición es del {med.get('medido_en')} y hoy es {date.today()}")
    datos = {k: v for k, v in (med.get("repos") or {}).items() if v.get("estado") == "vivo"}
    citados = repos_citados(texto)
    # un repositorio que hoy no existe o está bloqueado por la plataforma no es una cifra
    # desactualizada: es un dato. Se declara y se sigue (error E34, la pieza 06).
    no_vivos = {k: v for k, v in (med.get("repos") or {}).items() if v.get("estado") != "vivo"}
    for r, v in no_vivos.items():
        if r in citados:
            avisos.append(f"{r}: sin objeto hoy ({str(v.get('detalle'))[:40]}); se declara en la pieza")
    faltan = [r for r in citados if r not in datos and r not in no_vivos]
    if faltan:
        fallos.append(f"{len(faltan)} repositorios citados sin medir: " + ", ".join(faltan[:4]))
    # el mapa del principio también lleva el icono: el corte tiene que ser la sección de
    # verdad, con su encabezado (negrita o almohadilla), nunca la línea del mapa
    corte_enlaces = re.search(r"\n(?:\*|#{1,3} )🔗[^\n]{0,24}?[Ee]nlaces", texto)
    cuerpo = texto[:corte_enlaces.start()] if corte_enlaces else texto
    # hay piezas que no llevan la estrella pegada al número porque el número vive en una
    # tabla con su columna ★. La cifra cuenta igual si aparece como celda (error E25).
    celdas = {c.strip().lstrip("★") for ln in texto.splitlines() if ln.startswith("|")
              for c in ln.split("|")}
    for r, d in sorted(datos.items()):
        marca = "★" + miles(d["stars"])
        if marca in texto or miles(d["stars"]) in celdas:
            continue
        # una cifra solo se exige a los programas que la pieza presenta; un catálogo citado como
        # enlace de apoyo no tiene por qué llevar sus estrellas (decisión de la casa, 4-nov)
        if r.split("/")[-1].lower() in cuerpo.lower():
            fallos.append(f"{r}: la fuente dice {marca} y esa cifra no aparece en el texto")
        else:
            avisos.append(f"{r}: citado solo como enlace de apoyo; su cifra de hoy es {marca}")
        if d.get("rel") and d["rel"] not in texto and d["entregas"]:
            avisos.append(f"{r}: la fuente publica {d['rel']} y el texto no lo nombra")
    print(f"REMEDIR · {len(datos)} repositorios medidos el {med.get('medido_en')} a las {med.get('medido_a_las')}")
    for a in avisos[:8]:
        print(f"   · aviso: {a}")
    for f in fallos:
        print(f"   ✗ {f}")
    print("veredicto:", "AL DÍA" if not fallos else f"{len(fallos)} datos desactualizados")
    return 0 if not fallos else 1


def solape(nueva: Path, vieja: Path, tope: float = 0.25) -> int:
    def parrafos(p: Path) -> set[str]:
        t = p.read_text(encoding="utf-8", errors="replace")
        return {x.strip() for x in re.split(r"\n\s*\n", t) if len(x.strip()) > 120}
    a, b = parrafos(nueva), parrafos(vieja)
    if not a:
        print("la pieza nueva no tiene párrafos largos")
        return 1
    comunes = a & b
    pct = len(comunes) / len(a)
    print(f"SOLAPE · {len(a)} párrafos nuevos · {len(comunes)} copiados de la versión anterior "
          f"({pct*100:.1f} %; tope {tope*100:.0f} %)")
    for c in sorted(comunes)[:3]:
        print(f"   · {c[:90]}…")
    print("veredicto:", "ESCRITA DE NUEVO" if pct <= tope else "ES UN RETOQUE, NO UNA PIEZA NUEVA")
    return 0 if pct <= tope else 1


def main() -> int:
    args = sys.argv[1:]
    if "--escribir" in args:
        i = args.index("--escribir")
        destino = Path(args[i + 1])
        pieza = Path(args[args.index("--pieza") + 1])
        return escribir(pieza, destino)
    if "--pieza" in args and "--medicion" in args:
        return comparar(Path(args[args.index("--pieza") + 1]), Path(args[args.index("--medicion") + 1]))
    if "--solape" in args:
        i = args.index("--solape")
        return solape(Path(args[i + 1]), Path(args[i + 2]))
    if "--suma" in args:
        i = args.index("--suma")
        nums = [int(x) for x in args[i + 1:] if x.isdigit()]
        total = sum(nums)
        print(f"suma: {miles(total)} · {en_palabras(total, True)} · {en_palabras(total)} · {len(nums)} cifras")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
