#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TESTIGO DE NOVEDAD Y DE SERIE CORTA — N01–N08, M24–M28, M00.

`manual_gate.py` (M01–M23) comprueba la forma de la pieza. No puede comprobar lo
que el dueño exigió el 3-nov-2026: que la pieza traiga algo **nuevo**, que declare
la madurez de lo nuevo, que no recomiende por fama ni por estrellas, que no meta
meta-comentarios de IA o de plataforma, y que la serie corta lleve sus #task.

Este testigo comprueba, letra por letra y sin interpretar prosa:

  M24 banda de descubrimiento   al menos una ficha con <500★ o paquete de <30 d
  M25 madurez declarada         ficha con <100★ o tag -dev/beta/rc → «madurez»
  M26 abuelo sin fecha          ficha con empujón >365 d sin «sin movimiento»
  M27 meta-comentario IA/red    lista negra de fórmulas de proceso y de plataforma
  M28 #task de la serie corta   ≥2 tareas, numeración continua y sin huecos
  M00 triple lectura            bloque TRIPLE LECTURA del día (solo con --entrega)

Uso:
    python3 herramientas/novedad_gate.py <carpeta-o-archivo> [...] [--corte 2026-11-03]
    python3 herramientas/novedad_gate.py --entrega INFORME.md [--corte 2026-11-03]
    python3 herramientas/novedad_gate.py --json ...
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

MESES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
         "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}

# M27 · fórmulas que el dueño prohibió: proceso de escritura, la máquina, la plataforma
META_IA = ["como ia", "como modelo", "aquí va un dato", "en esta sección", "en esta pieza voy",
           "voy a explicar", "voy a contar", "he procesado", "este texto fue generado",
           "generado por ia", "con inteligencia artificial", "he encontrado en mis fuentes"]
META_RED = ["nuestra comunidad de facebook", "lo que facebook necesita", "comunidad de facebook",
            "los que me siguen en facebook", "si estás leyendo esto en facebook",
            "comparte para que llegue", "este post va dedicado", "en este post de facebook",
            "el algoritmo de facebook", "nuestra audiencia de whatsapp"]

ESTRELLA = re.compile(r"★\s*([\d\.]{1,9})")
FICHA_FECHA = re.compile(r"empuj[oó]n\s+(?:de\s+)?(\d{4}-\d{2}-\d{2}|\d{1,2}-([a-z]{3})-\d{4})", re.I)
TAG_DEV = re.compile(r"\b(v?\d+[\w\.\-]*(?:-dev|-beta|-rc|-alpha|beta|rc)\b)", re.I)


def a_fecha(s: str) -> date | None:
    s = s.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return date(int(m[1]), int(m[2]), int(m[3]))
    m = re.fullmatch(r"(\d{1,2})-([a-z]{3})-(\d{4})", s)
    if m and m[2] in MESES:
        return date(int(m[3]), MESES[m[2]], int(m[1]))
    return None


def parrafos(t: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", t) if len(p.strip()) > 60]


def estrellas(t: str) -> list[int]:
    out = []
    for m in ESTRELLA.finditer(t):
        v = m[1].replace(".", "")
        if v.isdigit():
            out.append(int(v))
    return out


def fichas(t: str) -> list[str]:
    """Párrafos que parecen ficha: llevan estrellas y una ruta owner/repo o una licencia."""
    return [p for p in parrafos(t)
            if ESTRELLA.search(p) and re.search(r"\b[\w\.\-]+/[\w\.\-]+\b|GPL|MIT|Apache|AGPL", p)]


def m24(t: str, corte: date) -> list[str]:
    f = fichas(t)
    if not f:
        return ["M24 sin fichas: no se puede comprobar la banda de descubrimiento"]
    for p in f:
        for e in estrellas(p):
            if e < 500:
                return []
    for p in f:
        m = re.search(r"paquete[^\n]{0,40}?(\d{1,2})-([a-z]{3})-(\d{4})", p)
        if m and m[2] in MESES:
            d = date(int(m[3]), MESES[m[2]], int(m[1]))
            if (corte - d).days <= 30:
                return []
    return [f"M24 ninguna ficha en la banda de descubrimiento (<500★ · <12 meses · paquete <30 d): {len(f)} fichas, "
            f"la menor con ★{min(estrellas(t))}"]


def m25(t: str) -> list[str]:
    fallos = []
    for p in fichas(t):
        if "madurez" in p.lower():
            continue
        e = estrellas(p)
        joven = any(x < 100 for x in e)
        dev = bool(TAG_DEV.search(p))
        if joven or dev:
            nombre = p[:48].replace("\n", " ")
            fallos.append(f"M25 ficha con ★{min(e) if e else '?'}{' y tag -dev/beta' if dev else ''} sin «madurez» declarada: {nombre}…")
    return fallos


def m26(t: str, corte: date) -> list[str]:
    fallos = []
    for p in fichas(t):
        m = FICHA_FECHA.search(p)
        if not m:
            continue
        d = a_fecha(m[1])
        if not d:
            continue
        dias = (corte - d).days
        if dias > 365 and "sin movimiento" not in p.lower():
            fallos.append(f"M26 ficha con empujón de {dias} días sin «sin movimiento desde»: {p[:48].replace(chr(10),' ')}…")
    return fallos


def m27(t: str) -> list[str]:
    bajo = t.lower()
    fallos = []
    for x in META_IA:
        if x in bajo:
            fallos.append(f"M27 meta-comentario de IA: «{x}»")
    for x in META_RED:
        if x in bajo:
            fallos.append(f"M27 meta-comentario de plataforma: «{x}»")
    return fallos


def m28(t: str, es_hdp: bool) -> list[str]:
    tareas = re.findall(r"#task\s+(\d+)", t)
    if not es_hdp and not tareas:
        return []
    if len(tareas) < 2:
        return [f"M28 serie corta con {len(tareas)} #task (se exigen 2 a 5)"]
    nums = [int(x) for x in tareas]
    if len(set(nums)) != len(nums):
        return ["M28 #task repetidos"]
    huecos = [b for a, b in zip(nums, nums[1:]) if b != a + 1]
    if huecos:
        return [f"M28 numeración con hueco: salta a {huecos[0]} (se exige continuidad o declararlo)"]
    return []


def m00(t: str, corte: date) -> list[str]:
    m = re.search(r"TRIPLE LECTURA\s*·\s*([^\n]+)", t)
    if not m:
        return ["M00 sin constancia de triple lectura del día"]
    if str(corte.year) not in m[1]:
        return [f"M00 constancia sin el año del corte: «{m[1][:40]}»"]
    return []


def revisar(p: Path, corte: date, entrega: bool) -> dict:
    t = p.read_text(encoding="utf-8", errors="replace")
    es_hdp = "hdp" in p.name.lower()
    fallos = m24(t, corte) + m25(t) + m26(t, corte) + m27(t) + m28(t, es_hdp)
    if entrega:
        fallos += m00(t, corte)
    criticos = [f for f in fallos if not f.startswith("M00")]
    return {"pieza": p.name, "caracteres": len(t), "hdp": es_hdp,
            "veredicto": "ROJO" if criticos else ("VENTANA" if fallos else "VERDE"), "fallos": fallos}


def main() -> int:
    args = sys.argv[1:]
    corte = date.today()
    if "--corte" in args:
        corte = a_fecha(args[args.index("--corte") + 1]) or corte
    entrega = "--entrega" in args
    js = "--json" in args
    rutas = [a for a in args if not a.startswith("--") and a not in (str(corte), "2026-11-03")]
    targets: list[Path] = []
    for r in rutas:
        q = Path(r)
        if q.is_dir():
            targets += sorted(q.glob("*.md"))
        elif q.exists():
            targets.append(q)
    if not targets:
        print("nada que revisar"); return 2
    res = [revisar(p, corte, entrega) for p in targets]
    if js:
        print(json.dumps({"corte": str(corte), "resultados": res}, ensure_ascii=False, indent=1))
    else:
        v = sum(1 for r in res if r["veredicto"] == "VERDE")
        ro = sum(1 for r in res if r["veredicto"] == "ROJO")
        print(f"NOVEDAD GATE · {len(res)} piezas · corte {corte} · VERDE {v} · ROJO {ro}")
        for r in res:
            print(f"\n{r['veredicto']:<9} {r['pieza'][:62]:<62} {r['caracteres']} car.")
            for f in r["fallos"]:
                print(f"   ✗ {f}")
    return 0 if all(r["veredicto"] != "ROJO" for r in res) else 1


if __name__ == "__main__":
    sys.exit(main())
