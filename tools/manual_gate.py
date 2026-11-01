#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compuerta del MANUAL DE ESTILO Y OPERACIONES V3.0 (1-nov-2026).

Ejecuta los criterios obligatorios C-01 a C-24 de
`corpus-la-bandita/CIMIENTOS — criterios obligatorios y precedencia (1-nov-2026).md`
sobre las piezas de la serie viva y devuelve, por pieza, VERDE / VENTANA / ROJO.

Uso:
    python3 tools/manual_gate.py                 # informe legible de todas las piezas
    python3 tools/manual_gate.py --verificar     # solo las piezas con banda declarada
    python3 tools/manual_gate.py --json          # salida para vara.py / actas
    python3 tools/manual_gate.py --pieza RUTA    # una sola pieza

Códigos de la compuerta:
    M01 firma textual        M02 meme del corte      M03 remate propio (único)
    M04 mapa 5-12            M05 en una página       M06 FAQ 6-12
    M07 enlaces completos    M08 fichas con campos   M09 frases prohibidas
    M10 notas al pie         M11 banda de longitud   M12 meta-comentarios
    M13 cabecera             M14 signos dobles       M15 secretos / mods
    M16 promesas             M23 párrafos compartidos
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBL = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
BANDAS = RAIZ / "docs" / "bandas.json"

FIRMA = "La Bandita informa a partir de fuentes fechadas."

PROHIBIDAS = [
    "la mejor para todos", "imprescindible", "100% segura", "totalmente segura",
    "todo el mundo sabe", "según expertos", "últimas 24 horas", "no te lo pierdas",
    "descárgalo ya", "descárgala ya", "el único que necesitas", "revolucionario",
    "único en su clase", "sin precedentes", "el futuro es ahora", "game changer",
    "la mejor de todas", "la más segura",
]

META = [
    "en esta pieza voy", "esta sección explica", "aquí va un dato",
    "lo que esta pieza no dice", "cómo se lee esta pieza",
    "voy a contar", "voy a explicar", "en esta sección",
]
# excepciones declaradas en CIMIENTOS §3.7: explicar CÓMO se midió es evidencia, no meta-relato
META_EXENTO = ["cómo se midió", "cómo se mide", "cómo comprobar", "el método"]

PROMESAS = ["te avisaré", "te aviso cuando", "te avisamos cuando", "volveré a avisarte",
            "te mantendré informado", "te informaré cuando"]

SECRETOS = [r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
            r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"]


def piezas() -> list[Path]:
    out = []
    for d in ("WhatsApp-dominicano-ES", "Facebook-dominicano-ES"):
        out += sorted((PUBL / d).glob("*.md"))
    return out


def canal(p: Path) -> str:
    return "whatsapp" if "WhatsApp" in p.parent.name else "facebook"


def bandas() -> dict:
    try:
        return json.loads(BANDAS.read_text(encoding="utf-8"))
    except Exception:
        return {}


def parrafos(t: str, minimo: int = 100) -> set[str]:
    return {x.strip() for x in re.split(r"\n\s*\n", t) if len(x.strip()) >= minimo}


def trozos(t: str) -> list[str]:
    """Divide la pieza en bloques por el separador de la casa."""
    return [b for b in re.split(r"\n?─{10,}\n?", t) if b.strip()]


def seccion(t: str, claves: tuple[str, ...]) -> str:
    """Devuelve el bloque de la sección pedida.

    Primero busca una línea que SEA el encabezado (quitando #, * y espacios) y devuelve desde
    esa línea hasta el siguiente separador: así no se confunde el mapa del principio —que solo
    nombra la sección— con la sección de verdad. Si no hay encabezado suelto, cae al criterio
    de bloques: gana el que tenga el encabezado en su primer renglón, luego el que más enlaces
    tenga y, si sigue el empate, el más temprano.
    """
    lineas = t.splitlines()
    for k in claves:
        for n, l in enumerate(lineas):
            limpio = l.strip().lstrip("#").strip().strip("*# ").strip().lower()
            if limpio.startswith(k.lower()):
                resto = "\n".join(lineas[n:])
                corte = re.search(r"\n?─{10,}", resto)
                return resto[: corte.start()] if corte else resto
    candidatos = []
    for b in trozos(t):
        for l in b.splitlines():
            ls = l.strip().lstrip("#").strip().strip("*# ").strip()
            if any(k.lower() in ls.lower() for k in claves):
                candidatos.append(b)
                break
    if not candidatos:
        return ""

    def peso(b: str) -> tuple[int, int, int]:
        primero = next((l for l in b.splitlines() if l.strip()), "")
        lp = primero.strip().lstrip("#").strip().strip("*# ").strip().lower()
        cabecera = 1 if any(k.lower() in lp for k in claves) else 0
        return (cabecera, b.count("http"), -candidatos.index(b))

    return max(candidatos, key=peso)


def check(p: Path, bk: dict, firmas_vistas: dict, todos: dict[str, set[str]]) -> dict:
    t = p.read_text(encoding="utf-8", errors="replace")
    f: list[tuple[str, str, str]] = []   # (código, severidad, detalle)
    ok: list[str] = []

    # M11 · banda
    pieza_no = re.match(r"^(\d+)", p.name)
    pieza_no = pieza_no.group(1) if pieza_no else None
    entrada = (bk.get(canal(p), {}).get("piezas", {}) or {}).get(pieza_no or "", {})
    banda = bk.get(canal(p), {})
    if entrada:
        lo, hi = banda.get("min"), banda.get("max")
        if lo and hi and not (lo <= len(t) <= hi):
            f.append(("M11", "critica", f"{len(t)} caracteres fuera de la banda {lo}-{hi}"))
        else:
            ok.append(f"M11 banda {len(t)} en {lo}-{hi}")
    else:
        f.append(("M11", "forma", "pieza sin banda declarada en docs/bandas.json"))

    # M01 · firma textual
    if FIRMA in t:
        ok.append("M01 firma textual")
    else:
        f.append(("M01", "critica", "falta la firma textual obligatoria"))

    # M13 · cabecera con fecha larga
    meses = ("enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre")
    if re.search(r"\d{1,2} de (" + meses + r") de \d{4}", t[:1200]):
        ok.append("M13 fecha de corte en formato largo")
    else:
        f.append(("M13", "forma", "la cabecera no declara la fecha de corte en formato largo"))

    # M02 · meme del corte (dos líneas con guion largo justo antes de la firma)
    lineas = t.splitlines()
    pos = next((i for i, l in enumerate(lineas) if FIRMA in l), None)
    if pos is not None:
        prev = [l.strip() for l in lineas[max(0, pos - 6):pos] if l.strip()]
        meme = [l for l in prev if l.startswith("—") or l.startswith("> —")]
        if len(meme) >= 2:
            ok.append("M02 meme del corte")
        else:
            f.append(("M02", "critica", "no hay meme de dos líneas antes de la firma"))
    else:
        f.append(("M02", "critica", "sin firma: no se puede comprobar el meme"))

    # M03 · remate propio tras la firma, único entre piezas
    remate = ""
    for l in lineas:
        if FIRMA in l:
            remate = l.split(FIRMA, 1)[1].strip()
    if len(remate) < 10:
        f.append(("M03", "critica", "la firma no lleva remate propio"))
    elif remate in firmas_vistas:
        f.append(("M03", "critica", f"remate calcado de {firmas_vistas[remate]}"))
    else:
        firmas_vistas[remate] = p.name[:60]
        ok.append("M03 remate propio")

    # M04 · mapa 5-12 entradas
    mapa = seccion(t, ("🗺️", "mapa de esta guía"))
    if not mapa:
        f.append(("M04", "critica", "sin mapa `🗺️ Mapa de esta guía`"))
    else:
        n = len(re.findall(r"^\s*[├└]──", mapa, re.M))
        if 5 <= n <= 12:
            ok.append(f"M04 mapa con {n} entradas")
        else:
            f.append(("M04", "forma", f"mapa con {n} entradas (se exigen 5-12)"))

    # M05 · en una página, 3-5 párrafos
    una = seccion(t, ("en una página",))
    if not una:
        f.append(("M05", "forma", "sin sección «En una página»"))
    else:
        n = 0
        for x in re.split(r"\n\s*\n", una):
            x = x.strip()
            if len(x) <= 80:
                continue
            if all(l.lstrip().startswith(("•", "-", "├", "└")) for l in x.splitlines() if l.strip()):
                continue
            if x.startswith("*") and x.endswith("*") and "\n" not in x and len(x) < 200:
                continue  # subtítulo suelto
            n += 1
        if 3 <= n <= 5:
            ok.append(f"M05 en una página con {n} párrafos")
        else:
            f.append(("M05", "forma", f"«En una página» con {n} párrafos (se exigen 3-5)"))

    # M06 · FAQ 6-12
    if not seccion(t, ("preguntas frecuentes", "preguntas que me hacen", "preguntas que me llegan", "preguntas", "❓")):
        f.append(("M06", "forma", "sin sección de preguntas frecuentes"))
    else:
        n = len(re.findall(r"^(?:\*\*[^*\n]{6,}\?\*\*|\*«[^\n]{6,}\?»\*)", t, re.M))
        if 6 <= n <= 12:
            ok.append(f"M06 FAQ con {n} preguntas")
        else:
            f.append(("M06", "forma", f"FAQ con {n} preguntas (se exigen 6-12)"))

    # M07 · enlaces con formato y cobertura
    enl = seccion(t, ("🔗", "enlaces"))
    if not enl:
        f.append(("M07", "critica", "sin sección de enlaces"))
    else:
        def urls(x: str) -> set[str]:
            # una URL citada dentro de una frase puede venir con » o un punto pegado:
            # se limpia antes de comparar, o el cotejo acusa un enlace que sí está.
            return {re.sub(r"[»\.,;:!\?\)\]]+$", "", u)
                    for u in re.findall(r"https?://[^\s\)]+", x)}
        en_lista = urls(enl)
        en_cuerpo = urls(t) - en_lista
        formato = len(re.findall(r"^-\s+[^:\n]+:\s+https?://", enl, re.M))
        faltan = en_cuerpo - en_lista
        if faltan:
            f.append(("M07", "critica", f"{len(faltan)} URL del cuerpo fuera de la lista de enlaces"))
        elif formato == 0:
            f.append(("M07", "forma", "los enlaces no usan el formato `- Nombre: URL`"))
        else:
            ok.append(f"M07 {len(en_lista)} enlaces, {formato} con formato de la casa")

    # M08 · fichas con campos
    fichas = re.findall(r"★[\d\.]+", t)
    if fichas:
        if re.search(r"licencia|GPL|MIT|Apache|AGPL|CC0|Unlicense|NOASSERTION|sin licencia", t, re.I):
            ok.append(f"M08 {len(fichas)} marcas de estrella con campo de licencia")
        else:
            f.append(("M08", "forma", "fichas sin campo de licencia"))
    else:
        f.append(("M08", "forma", "sin fichas con estrellas"))

    # M09 · frases prohibidas
    golpe = [x for x in PROHIBIDAS if x in t.lower()]
    if golpe:
        f.append(("M09", "critica", "frases prohibidas: " + ", ".join(golpe[:4])))
    else:
        ok.append("M09 cero frases prohibidas")

    # M10 · notas al pie fechadas
    notas = seccion(t, ("🗒️", "notas al pie"))
    if notas and re.search(r"\((?:1|2|3|4|5|6|7|8|9|1\d|2\d|3\d)-(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)", notas):
        ok.append("M10 notas al pie fechadas")
    else:
        f.append(("M10", "forma", "sin notas al pie fechadas"))

    # M12 · meta-comentarios del proceso
    bajo = t.lower()
    hallados = []
    for m in META:
        if m in bajo:
            ctx = bajo[max(0, bajo.find(m) - 60): bajo.find(m) + 80]
            if any(e in ctx for e in META_EXENTO):
                continue
            hallados.append(m)
    if hallados:
        f.append(("M12", "forma", "meta-comentarios: " + ", ".join(hallados[:4])))
    else:
        ok.append("M12 sin meta-comentarios del proceso")

    # M14 · signos dobles
    if re.search(r"[¡!?]{2,}|\?!|!\?", t):
        f.append(("M14", "forma", "signos dobles o de venta"))
    else:
        ok.append("M14 sin signos dobles")

    # M15 · secretos y mods
    sec = [pat for pat in SECRETOS if re.search(pat, t)]
    if sec:
        f.append(("M15", "critica", "posible secreto en el texto"))
    elif re.search(r"https?://[^\s]*(?:mod|revanced|apkmod)[^\s]*\.apk", t, re.I):
        f.append(("M15", "critica", "enlace directo a APK de mod"))
    else:
        ok.append("M15 sin secretos ni APK de mods")

    # M16 · promesas de vigilancia
    pr = [x for x in PROMESAS if x in bajo]
    if pr:
        f.append(("M16", "critica", "promesa de vigilancia: " + ", ".join(pr)))
    else:
        ok.append("M16 sin promesas")

    # M23 · párrafos compartidos con otras piezas
    pp = parrafos(t)
    compartidos = 0
    for otro, sp in todos.items():
        if otro == p.name:
            continue
        compartidos += len(pp & sp)
    if compartidos:
        f.append(("M23", "critica", f"{compartidos} párrafos compartidos con otras piezas"))
    else:
        ok.append("M23 cero párrafos compartidos")

    critica = any(s == "critica" for _, s, _ in f)
    forma = any(s == "forma" for _, s, _ in f)
    veredicto = "ROJO" if critica else ("VENTANA" if forma else "VERDE")
    return {"pieza": str(p.relative_to(RAIZ)), "canal": canal(p), "caracteres": len(t),
            "veredicto": veredicto, "fallos": f, "cumple": ok}


def main() -> int:
    args = sys.argv[1:]
    bk = bandas()
    ps = piezas()
    if "--pieza" in args:
        i = args.index("--pieza")
        ps = [RAIZ / args[i + 1]]
    solo_banda = "--verificar" in args
    if solo_banda:
        con_banda = set()
        for c in ("whatsapp", "facebook"):
            for ent in (bk.get(c, {}).get("piezas", {}) or {}).values():
                if isinstance(ent, dict) and ent.get("archivo"):
                    con_banda.add(ent["archivo"])
        ps = [p for p in ps if p.name in con_banda]
    todos = {p.name: parrafos(p.read_text(encoding="utf-8", errors="replace")) for p in piece_all()}
    firmas: dict[str, str] = {}
    res = [check(p, bk, firmas, todos) for p in ps]

    if "--json" in args:
        print(json.dumps({"piezas": res}, ensure_ascii=False, indent=1))
    else:
        orden = {"ROJO": 0, "VENTANA": 1, "VERDE": 2}
        res.sort(key=lambda r: (orden[r["veredicto"]], r["pieza"]))
        cuenta = {v: sum(1 for r in res if r["veredicto"] == v) for v in orden}
        print(f"MANUAL GATE · {len(res)} piezas · VERDE {cuenta['VERDE']} · "
              f"VENTANA {cuenta['VENTANA']} · ROJO {cuenta['ROJO']}")
        for r in res:
            print(f"\n{r['veredicto']:8s} {r['pieza'].split('/')[-1][:70]} · {r['caracteres']} car.")
            for cod, sev, det in r["fallos"]:
                print(f"   ✗ {cod} [{sev}] {det}")
    return 1 if any(r["veredicto"] == "ROJO" for r in res) else 0


def piece_all() -> list[Path]:
    return piezas()


if __name__ == "__main__":
    sys.exit(main())
