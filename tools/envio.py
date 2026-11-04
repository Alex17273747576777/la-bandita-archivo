#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ENVÍO · convierte una pieza del archivo en mensajes que WhatsApp no corta.

Qué hace y qué no:
  · Corta la pieza en mensajes de menos de `TOPE` caracteres **sin partir nunca un bloque de
    código** ni una tabla, y sin perder una sola línea del cuerpo (se verifica con `--verificar`).
  · Aparta el cierre viejo («Hoy, jueves 29 de octubre…») en un apéndice marcado NO ENVIAR: mandarlo
    como si fuera de hoy sería firmar una fecha falsa.
  · Mide hoy, con la API de GitHub, los repositorios que la pieza cita, y escribe un cierre nuevo
    con las estrellas de hoy, el delta contra lo que la pieza decía y la licencia vigente.
  · No reescribe la pieza: el original queda intacto y su sha256 va en la cabecera del envío.

Uso:
  LBT=<token> python3 tools/envio.py --medir          # una vez: mide todos los repos y enlaces
  python3 tools/envio.py --generar                    # escribe un archivo de envío por pieza
  python3 tools/envio.py --verificar                  # comprueba los envíos generados
  python3 tools/envio.py --generar --pieza 02         # solo una
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402

# Fecha "de trabajo". En generación es la del día; al verificar un envío ya archivado es la que el
# propio envío declara, para que la comprobación sea determinista y no se caiga sola a medianoche.
_FECHA_AS_OF: str | None = None


def hoy_efectivo() -> str:
    return _FECHA_AS_OF or fecha_casa_hoy()

RAIZ = Path(__file__).resolve().parents[1]  # se puede cambiar con --raiz (lo usa la autoprueba)
PUBLICACIONES = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
SALIDA = RAIZ / "docs" / "envios"
CANALES = {"whatsapp": "WhatsApp-dominicano-ES", "facebook": "Facebook-dominicano-ES"}


def carpeta(canal: str) -> Path:
    return PUBLICACIONES / CANALES[canal]


def dir_salida(canal: str) -> Path:
    return SALIDA / canal


def medicion(canal: str) -> Path:
    return SALIDA / f"_medicion-{canal}.json"
MARCA = "═══"  # separador de mensajes: ninguna pieza usa estos caracteres
CANAL = "whatsapp"  # lo fija la línea de órdenes
TOPE = 3960  # WhatsApp corta en 65.536, pero el tope de la casa es 4.000; 3.960 deja aire al marcador
MARGEN = 45  # espacio que se reserva para el «sigue abajo»
MES = {"01": "ene", "02": "feb", "03": "mar", "04": "abr", "05": "may", "06": "jun",
       "07": "jul", "08": "ago", "09": "sep", "10": "oct", "11": "nov", "12": "dic"}
DIAS = {"lunes": 0, "martes": 1, "miércoles": 2, "miercoles": 2, "jueves": 3,
        "viernes": 4, "sábado": 5, "sabado": 5, "domingo": 6}
MESES = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7,
         "agosto": 8, "septiembre": 9, "setiembre": 9, "octubre": 10, "noviembre": 11,
         "diciembre": 12}


# ─────────────────────────── piezas ───────────────────────────

def piezas(canal: str = "whatsapp") -> list[Path]:
    return sorted(p for p in carpeta(canal).glob("*.md")
                  if not p.name.lower().startswith(("leeme", "readme")))


def numero(p: Path) -> str:
    m = re.match(r"^(\d+)", p.name)
    return m.group(1) if m else "00"


def fecha_pieza(p: Path) -> str:
    m = re.search(r"-(\d{4}-\d{2}-\d{2})-dominicano", p.name)
    return m.group(1) if m else ""


def bon(f: str) -> str:
    """2026-10-15 → 15-oct-2026 (para leerlo, no para ordenarlo)."""
    if not f:
        return "sin fecha en el nombre"
    y, mm, dd = f.split("-")
    return f"{int(dd)}-{MES[mm]}-{y}"


def fecha_real(texto: str, p: Path) -> tuple[str, str]:
    """La fecha que la pieza declara por dentro manda; el nombre del archivo puede ser el del lote.
    Devuelve (fecha_real, fuente) con fuente en {'dateline','nombre'}."""
    cabecera = "\n".join(texto.split("\n")[:40])
    m = re.search(r"(\d{1,2}) de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|"
                  r"setiembre|octubre|noviembre|diciembre) de (\d{4})", cabecera, re.I)
    if m:
        return f"{m.group(3)}-{MESES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}", "dateline"
    return fecha_pieza(p), "nombre"


def edad(f: str) -> int:
    if not f:
        return -1
    return (date(*map(int, hoy_efectivo().split("-"))) - date(*map(int, f.split("-")))).days


# ─────────────────────── extracción de datos ───────────────────────

REPO_URL = re.compile(r"https?://github\.com/([\w.\-]+)/([\w.\-]+)")
FICHA = re.compile(r"\*\*([\w.\-]+/[\w.\-]+)\*\*(.{0,400}?)★([\d.]+)", re.S)
BASURA = ".,;:)]}»«\"'…"


def limpiar_repo(owner: str, name: str) -> str:
    """`KotatsuApp/Kotatsu.` no es un repositorio: el punto es de la prosa. Se limpia y se prueba."""
    return f"{owner.rstrip(BASURA)}/{name.rstrip(BASURA)}"


def repos_citados(texto: str) -> dict[str, dict]:
    """Repos con estrella declarada en la pieza (si la hay) y todos los citados por enlace."""
    salida: dict[str, dict] = {}
    for m in FICHA.finditer(texto):
        repo = m.group(1).rstrip(BASURA)
        if repo.split("/")[1].endswith((".git",)):
            continue
        if "stars_pieza" not in salida.setdefault(repo, {}):
            salida[repo]["stars_pieza"] = int(m.group(3).replace(".", ""))
    # repos citados en `backticks` o en **negrita** sin estrella al lado
    for m in re.finditer(r"[`*]{1,2}([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)[`*]{1,2}", texto):
        repo = limpiar_repo(m.group(1), m.group(2))
        nombre = repo.split("/")[1]
        if "." in nombre or not nombre:
            continue
        if m.group(1) in ("orgs", "sponsors", "topics", "search", "features", "apps"):
            continue
        salida.setdefault(repo, {})
    for m in REPO_URL.finditer(texto):
        owner, name = m.group(1), m.group(2)
        repo = limpiar_repo(owner, name)
        if repo.split("/")[1].endswith((".git", ".md", ".png", ".jpg")) or "." in repo.split("/")[1]:
            continue
        if owner in ("orgs", "sponsors", "topics", "search", "features", "apps", "marketplace"):
            continue
        salida.setdefault(repo, {})
    return salida


def enlaces(texto: str) -> list[str]:
    """Los enlaces, sin la puntuación que la prosa les pega al final (» « . , ))."""
    return sorted({u.rstrip(BASURA) for u in re.findall(r"https?://[^\s\)\]\|<>\"']+", texto)
                   if len(u.rstrip(BASURA)) > 12})


# ─────────────────────────── medición ───────────────────────────

def api(url: str, tok: str) -> dict:
    r = subprocess.run(
        ["curl", "-sS", "-m", "25", "-H", f"Authorization: Bearer {tok}",
         "-H", "Accept: application/vnd.github+json", url],
        capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"_error": "respuesta ilegible"}


def medir_repo(repo: str, tok: str) -> dict:
    d = api(f"https://api.github.com/repos/{repo}", tok)
    if not d or "_error" in d or d.get("message") == "Not Found":
        return {"estado": "muerto", "motivo": (d or {}).get("message", "sin respuesta")}
    if "full_name" not in d:
        return {"estado": "error", "motivo": (d or {}).get("message", "sin datos")}
    rel = api(f"https://api.github.com/repos/{repo}/releases/latest", tok)
    return {
        "estado": "vivo",
        "stars": d.get("stargazers_count"),
        "push": (d.get("pushed_at") or "")[:10],
        "archivado": bool(d.get("archived")),
        "licencia": (d.get("license") or {}).get("spdx_id"),
        "lenguaje": d.get("language"),
        "desc": (d.get("description") or "").strip(),
        "release": (rel or {}).get("tag_name"),
        "release_fecha": ((rel or {}).get("published_at") or "")[:10],
    }


def medir_enlace(u: str) -> dict:
    r = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-m", "25", "-L", "-A",
         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127 Safari/537.36",
         "-w", "%{http_code}", u], capture_output=True, text=True)
    c = r.stdout.strip() or "000"
    if c == "200":
        veredicto = "responde"
    elif c in ("401", "403", "429"):
        veredicto = "no deja entrar a un robot"  # NO es un enlace muerto
    elif c == "000":
        veredicto = "no respondio en 25 s"
    elif c in ("404", "410"):
        veredicto = "no existe hoy"
    else:
        veredicto = "responde con codigo " + c
    return {"codigo": c, "veredicto": veredicto}


def medir(tok: str, canal: str = "whatsapp") -> int:
    todas = piezas(canal)
    repos: dict[str, dict] = {}
    urls: set[str] = set()
    for p in todas:
        t = p.read_text(encoding="utf-8", errors="replace")
        repos.update(repos_citados(t))
        urls |= set(enlaces(t))
    print(f"piezas {len(todas)} · repos {len(repos)} · enlaces {len(urls)}", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        medidos = dict(zip(repos, ex.map(lambda r: medir_repo(r, tok), repos)))
    print("repos medidos", flush=True)
    with ThreadPoolExecutor(max_workers=12) as ex:
        links = dict(zip(sorted(urls), ex.map(medir_enlace, sorted(urls))))
    print("enlaces medidos", flush=True)
    datos = {
        "medido_en": hoy_efectivo(),
        "medido_en_utc": datetime.now().astimezone().isoformat(timespec="seconds"),
        "repos": {k: {**v, "stars_pieza": repos[k].get("stars_pieza")} for k, v in medidos.items()},
        "enlaces": links,
        "nota": ("estado medido con la API de GitHub y con peticiones HTTP el día indicado; "
                 "un 404 se registra como muerto, un 403/429 nunca"),
    }
    SALIDA.mkdir(parents=True, exist_ok=True)
    medicion(canal).write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    vivos = sum(1 for v in medidos.values() if v["estado"] == "vivo")
    muertos = sum(1 for v in medidos.values() if v["estado"] == "muerto")
    ok = sum(1 for v in links.values() if v["codigo"] == "200")
    print(f"medición {canal}: {len(medidos)} repos ({vivos} vivos, {muertos} muertos) · "
          f"{ok}/{len(links)} enlaces en 200")
    return 0


# ─────────────────────────── partir ───────────────────────────

SEPARADOR = re.compile(r"─{10,}")


def bloques(texto: str) -> list[str]:
    """Corta por los separadores de la casa, pero nunca dentro de una valla ```."""
    salida, buf, dentro = [], [], False
    for ln in texto.split("\n"):
        cierra = ln.count("```")
        if not dentro and SEPARADOR.fullmatch(ln.strip()) and not cierra:
            if buf:
                salida.append("\n".join(buf).strip("\n"))
                buf = []
            continue
        buf.append(ln)
        if cierra % 2:
            dentro = not dentro
    if buf:
        salida.append("\n".join(buf).strip("\n"))
    return [b for b in salida if b.strip()]


def subdividir(t: str, tope: int = TOPE) -> list[str]:
    """Corta por líneas sin dejar una valla de código abierta: si el corte cae dentro de un bloque,
    se cierra con ``` y se reabre en el mensaje siguiente. Un mensaje a medias con una valla suelta
    se lee como un error del archivo, no como un corte del mensajero."""
    trozos, cur, largo, dentro = [], [], 0, False

    def cerrar():
        nonlocal cur, largo
        texto = "\n".join(cur)
        if dentro:
            texto += "\n```"
        trozos.append(texto)
        cur = ["```"] if dentro else []
        largo = 3 if cur else 0

    for ln in t.split("\n"):
        if len(ln) > tope:  # línea más larga que un mensaje: se parte por espacios
            if cur:
                cerrar()
            resto = ln
            while len(resto) > tope:
                c = resto.rfind(" ", 0, tope)
                c = c if c > 200 else tope
                trozos.append(resto[:c].rstrip())
                resto = resto[c:].lstrip()
            cur, largo = [resto], len(resto)
            continue
        if largo + len(ln) + 1 > tope and cur:
            cerrar()
        cur.append(ln)
        largo += len(ln) + 1
        if ln.count("```") % 2:
            dentro = not dentro
    if cur:
        trozos.append("\n".join(cur))
    return [x for x in trozos if x.strip()]


def partir(texto: str, tope: int = TOPE) -> list[str]:
    partes, cur = [], ""
    for b in bloques(texto):
        cand = (cur + "\n\n" + b).strip("\n") if cur else b
        if len(cand) <= tope:
            cur = cand
            continue
        if cur:
            partes.append(cur)
        if len(b) <= tope:
            cur = b
        else:
            sub = subdividir(b, tope)
            partes += sub[:-1]
            cur = sub[-1]
    if cur:
        partes.append(cur)
    return partes


# ─────────────────── cierre viejo y cierre de hoy ───────────────────

def cierre_viejo(texto: str) -> tuple[str, str]:
    """Separa (cuerpo, apéndice) cuando el cierre está fechado en un día que no es hoy."""
    lineas = texto.rstrip("\n").split("\n")
    hoy = hoy_efectivo()
    corte = None
    for i, ln in enumerate(lineas):
        if i < len(lineas) * 0.5:
            continue
        s = ln.strip()
        pulso = re.match(r"^[💓*]*\s*PULSO\s+\d{1,2}-[A-Z]{3}-\d{4}", s, re.I)
        hoy_falso = re.match(r"^💓.*\bHoy,?\s+(lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo)", s, re.I)
        if pulso or hoy_falso:
            corte = i
            break
    if corte is None:
        return texto.rstrip("\n"), ""
    cuerpo = "\n".join(lineas[:corte]).rstrip("\n")
    apendice = "\n".join(lineas[corte:]).strip("\n")
    # si el apéndice no trae fecha, se queda con el cuerpo: no hay nada viejo que apartar
    if not re.search(r"\b(20\d\d)\b", apendice) or not re.search(
            r"(lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo|\d{1,2} de \w+)", apendice, re.I):
        return texto.rstrip("\n"), ""
    if hoy and hoy in apendice:
        return texto.rstrip("\n"), ""
    return cuerpo, apendice


def fnum(n) -> str:
    return f"{n:,}".replace(",", ".") if isinstance(n, int) else str(n)


def cierre_hoy(repos: dict, med: dict, nombre: str, links: dict | None = None) -> list[str]:
    """Mensajes de cierre con la medición de hoy. No afirma nada que no haya devuelto la API."""
    lineas, sin_dato = [], []
    for repo, info in repos.items():
        m = med.get(repo) or {}
        if not m:
            sin_dato.append(repo)
            continue
        if m.get("estado") == "muerto":
            lineas.append(f"• {repo} — *muerto*: el repositorio responde 404 hoy. Se nombra para "
                          f"esquivarlo, no se recomienda.")
            continue
        if m.get("estado") != "vivo":
            lineas.append(f"• {repo} — sin dato hoy (la API no respondió). No afirmo nada.")
            continue
        estrella = fnum(m.get("stars"))
        d = ""
        if isinstance(m.get("stars_pieza"), int) and isinstance(m.get("stars"), int):
            delta = m["stars"] - m["stars_pieza"]
            d = " (sin cambio)" if delta == 0 else f" ({delta:+d})".replace(",", ".")
        p_ = m.get("push") or ""
        dias = edad(p_) if p_ else -1
        if dias < 0:
            empuje = "sin fecha de empuje"
        elif dias <= 1:
            empuje = "empujó en las últimas horas"
        elif dias <= 45:
            empuje = f"empujó el {bon(p_)} (hace {dias} días)"
        else:
            empuje = f"*dormido*: sin empujar desde el {bon(p_)} ({dias} días)"
        lic = m.get("licencia") or "sin licencia detectada por la API"
        arch = " · *ARCHIVADO*" if m.get("archivado") else ""
        rel = ""
        if m.get("release"):
            rel = f" · última release {m['release']}" + (f" ({bon(m['release_fecha'])})" if m.get("release_fecha") else "")
        lineas.append(f"• {repo} — ★{estrella}{d} · {empuje} · {lic}{rel}{arch}")
    if not lineas:
        return []
    hoy = med["_hoy"].split("-")
    mes = [k for k, v in MESES.items() if v == int(hoy[1])][0]
    cabecera = (f"💓 *EL ESTADO DE HOY · {nombre}*\n\n"
                f"Medí otra vez, hoy {date(*map(int, med['_hoy'].split('-'))).day} de {mes} de {hoy[0]}, "
                f"los {len(repos)} repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es "
                f"lo que devolvió, no lo que decía la pieza:\n")
    if sin_dato:
        cabecera += (f"\n(De {len(sin_dato)} no tengo dato de hoy y lo digo: {', '.join(sin_dato[:6])}"
                     f"{'…' if len(sin_dato) > 6 else ''}.)\n")
    # el primer mensaje lleva la cabecera; el presupuesto se calcula con ella dentro
    presupuesto = TOPE - MARGEN - len(cabecera) - 2
    trozos = partir("\n".join(lineas), max(800, presupuesto))
    salida = [cabecera + "\n" + trozos[0]] + trozos[1:]
    # el resto de trozos no lleva cabecera: se pueden reagrupar de dos en dos si caben
    salida = [salida[0]] + trozos[1:]
    if links:
        salida += partir(resumen_enlaces(links), TOPE - MARGEN)
    salida.append("💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo "
                  "cambió, la fecha del dato está escrita al lado para que no te engañe.")
    return salida


def resumen_enlaces(links: dict) -> str:
    """Los enlaces de la pieza, contados por veredicto. Un 403 no es un enlace muerto y se dice."""
    from collections import Counter
    c = Counter(v.get("veredicto", "?") for v in links.values())
    total = len(links)
    ok = c.get("responde", 0)
    partes = ["💓 *LOS ENLACES · medidos hoy uno por uno*", "",
              f"De los {total} enlaces de esta pieza, *{ok} responden*."]
    raros = {k: v for k, v in links.items() if v.get("veredicto") != "responde"}
    if not raros:
        partes.append("Ninguno roto.")
    else:
        partes.append("")
        for u, v in sorted(raros.items()):
            codigo, ver = v.get("codigo"), v.get("veredicto")
            if ver == "no deja entrar a un robot":
                partes.append(f"• {u} — contesta {codigo} a un robot. *No está muerto*: ábrelo en tu "
                              f"navegador y lo verás.")
            elif ver == "no existe hoy":
                partes.append(f"• {u} — {codigo}. No existe hoy: no lo abras, no lo recomiendo.")
            elif ver == "no respondio en 25 s":
                partes.append(f"• {u} — no respondió en 25 segundos. No digo que esté caído: digo que no "
                              f"me contestó.")
            else:
                partes.append(f"• {u} — {codigo}. Error del servidor; no es culpa del enlace.")
    return "\n".join(partes)


# ─────────────────────────── portada ───────────────────────────

def titulo_pieza(texto: str, p: Path | None = None) -> str:
    """El título es la línea en negrita que va justo encima de la dateline de la casa."""
    lineas = [l.strip() for l in texto.split("\n")]
    for l in lineas[:12]:
        m = re.match(r"^\*(\d+)\s*[—–-]\s*(.+?)\*$", l)
        if m:
            return m.group(2).strip()
        h = re.match(r"^#+\s*(.+)$", l)
        if h and re.search(r"repos de esta pieza|medidos hoy|lectura de la medici|preguntas frecuentes|"
                           r"mini-?quiz|glosario|c[oó]mo verificar|mapa de esta gu", h.group(1), re.I):
            continue
        if h:
            t = h.group(1).strip().strip("*").strip()
            t = re.sub(r"^(Publicaci[oó]n|Pieza)\s*\d+\s*[—–-]\s*", "", t, flags=re.I)
            if len(t) >= 8:
                return t if len(t) <= 100 else t[:97].rstrip() + "…"
    for i, l in enumerate(lineas):
        if "La Bandita ·" in l or "La Bandita ·" in l.replace("*", ""):
            for j in range(i - 1, max(-1, i - 6), -1):
                cand = lineas[j].strip("* ").strip()
                if lineas[j].startswith("*") and 12 <= len(cand) <= 170 and "La Bandita" not in cand:
                    return cand
    if p is not None:
        # del nombre del archivo, sin la cola técnica
        base = re.sub(r"-WhatsApp-La-Bandita-.*$", "", p.stem)
        base = re.sub(r"^\d+-", "", base).replace("-", " ").strip()
        if base:
            return base
    for ln in texto.split("\n"):
        t = ln.strip()
        if t.startswith("*") and t.endswith("*") and 12 <= len(t) <= 170 and "La Bandita ·" not in t:
            return t.strip("*").strip()
    return p.stem if p else "La Bandita"


def portada(p: Path, texto: str, repos: dict, med: dict, n_mensajes: int) -> str:
    f, fuente = fecha_real(texto, p)
    hoy = hoy_efectivo()
    vivos = sum(1 for r in repos if (med.get(r) or {}).get("estado") == "vivo")
    muertos = [r for r in repos if (med.get(r) or {}).get("estado") == "muerto"]
    lic = {}
    for r in repos:
        m = med.get(r) or {}
        if m.get("estado") == "vivo":
            lic[m.get("licencia") or "sin licencia"] = lic.get(m.get("licencia") or "sin licencia", 0) + 1
    lic_txt = " · ".join(f"{k} {v}" for k, v in sorted(lic.items(), key=lambda kv: -kv[1])[:4])
    url = ("https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/"
           + p.relative_to(RAIZ).as_posix())
    t = titulo_pieza(texto, p)
    lineas = [
        f"*{t}*",
        "",
        f"La Bandita · pieza {numero(p)} · guía del {bon(f)} · te la mando hoy en {n_mensajes} mensajes.",
        "",
        (f"Antes de mandártela volví a medir lo que afirma: *{len(repos)} repositorios, {vivos} vivos"
         + (f" y {len(muertos)} muerto{'s' if len(muertos) != 1 else ''}" if muertos else "")
         + f"*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, "
           f"con la fecha al lado."),
    ]
    if lic_txt:
        lineas += ["", f"Licencias de lo que recomienda: {lic_txt}."]
    if f and f != hoy_efectivo():
        lineas += ["", (f"⚠️ *Aviso de fecha:* este texto se escribió el {bon(f)}. Todo lo que dice "
                        f"«hoy» dentro se refiere a ese día, no a este. La medición de hoy va al final, "
                        f"firmada y con su fecha.")]
    lineas += [
        "",
        f"La guía entera, ya guardada en el archivo: {url}",
        "",
        f"💓 {date(*map(int, hoy.split('-'))).day} de "
        f"{[k for k, v in MESES.items() if v == int(hoy.split('-')[1])][0]} de {hoy.split('-')[0]}. "
        f"Lo que no medí, lo digo: no lo medí.",
    ]
    return "\n".join(lineas)


# ─────────────────────────── generar ───────────────────────────

def con_marcadores(mensajes: list[str]) -> list[str]:
    """«sigue abajo» en todos menos el último, para que nadie crea que la guía terminó ahí."""
    M = len(mensajes) - 1  # la portada no cuenta como parte
    salida = [mensajes[0]]
    for i, t in enumerate(mensajes[1:], 1):
        salida.append(t if i == M else f"{t}\n\n⏬ sigue abajo · parte {i} de {M}")
    return salida


def una(p: Path, med: dict, escribir: bool = True) -> dict:
    texto_original = p.read_text(encoding="utf-8", errors="replace")
    cuerpo, apendice = cierre_viejo(texto_original)
    repos = repos_citados(cuerpo)
    urls = set(enlaces(texto_original))
    viv = {k: v for k, v in med.items() if isinstance(v, dict)}
    valla_abierta = cuerpo.count("```") % 2 == 1
    if valla_abierta:
        # la pieza deja un bloque de código sin cerrar: el envío lo cierra para que se pueda leer,
        # y lo dice. La pieza original NO se toca.
        cuerpo = cuerpo + "\n```"
    partes = partir(cuerpo, TOPE - MARGEN - 260)  # margen extra: aviso de fecha y cierre de valla
    # enlaces de verdad (http), con su veredicto de hoy
    links = {u: viv[u] for u in urls
             if u in viv and isinstance(viv[u], dict) and "veredicto" in viv[u]}
    cierre = cierre_hoy(repos, {"_hoy": hoy_efectivo(), **viv}, f"pieza {numero(p)}", links)
    # el cierre se agrupa: mensajes cortos seguidos se pegan si caben
    while len(cierre) > 2 and len(cierre[0]) + len(cierre[1]) + 2 <= TOPE - MARGEN:
        cierre = [cierre[0] + "\n\n" + cierre[1]] + cierre[2:]
    # las etiquetas estratégicas viajan en el ÚLTIMO mensaje: enterradas en medio no las ve nadie
    etiquetas = []
    for i, parte in enumerate(partes):
        if "🏷️" in parte and "Etiquetas estratégicas" in parte:
            cabeza, _, cola = parte.partition("🏷️")
            m = re.search(r"#\w[\w\s#]*$", cola.strip())
            if m:
                etiquetas.append("*🏷️ Etiquetas estratégicas*\n\n" + " ".join(m.group(0).split()))
            resto = cabeza.strip().strip("─").strip()   # el cuerpo NO se pierde: solo se va el bloque
            partes[i] = resto
            if not resto:
                partes.pop(i)
            break
    if etiquetas and cierre:
        cierre[-1] = cierre[-1] + "\n\n" + etiquetas[0]
    f_real, _ = fecha_real(cuerpo, p)
    if f_real and f_real != hoy_efectivo() and partes:
        partes[0] = (f"[Texto del {bon(f_real)}: cuando dice «hoy», es ese día. La medición de hoy está "
                     f"al final.]\n\n") + partes[0]
    # la portada se escribe al final, cuando ya se sabe cuántos mensajes van de verdad
    total = 1 + len(partes) + len(cierre)
    cabeza = portada(p, cuerpo, repos, viv, total)
    mensajes = con_marcadores([cabeza] + partes + cierre)
    assert len(mensajes) == total, (len(mensajes), total)
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    canal_nombre = "WhatsApp" if CANAL == "whatsapp" else "Facebook"
    salida = [f"# PIEZA {numero(p)} · envío para {canal_nombre}", "",
              f"- **Pieza original:** `{p.relative_to(RAIZ).as_posix()}`",
              f"- **Fecha de la pieza:** {bon(fecha_real(cuerpo, p)[0])} "
              f"(según {fecha_real(cuerpo, p)[1]}; edad hoy: {edad(fecha_real(cuerpo, p)[0])} días)",
              f"- **sha256 de la pieza:** `{sha}`",
              f"- **Envío generado:** {hoy_efectivo()} · {len(mensajes)} mensajes · "
              f"el mayor de {max(len(t) for t in mensajes)} caracteres",
              "- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.",]
    if valla_abierta:
        salida.append("- **Aviso:** la pieza original deja una valla de código sin cerrar; este envío la "
                      "cierra al final del cuerpo para que se pueda leer. La pieza no se modificó.")
    salida.append("")
    for i, t in enumerate(mensajes, 1):
        salida += [f"{MARCA} MENSAJE {i} de {len(mensajes)} · {len(t)} caracteres {MARCA}", "", t, ""]
    if apendice:
        salida += ["## APÉNDICE · verificación original de la pieza — **NO ENVIAR**", "",
                   ("Va aquí porque está fechada en el día en que se escribió. Mandarla hoy sería afirmar "
                    "que ese día es hoy: falso. Se conserva para que se pueda comprobar."), "",
                   apendice, ""]
    contenido = "\n".join(salida)
    datos = {"pieza": p.relative_to(RAIZ).as_posix(), "numero": numero(p), "mensajes": len(mensajes),
             "mayor": max(len(t) for t in mensajes), "caracteres": len(contenido),
             "sha256": sha, "repos": len(repos), "enlaces": len(links), "apendice": bool(apendice),
             "valla_cerrada": valla_abierta, "titulo": titulo_pieza(cuerpo, p),
             "repos_muertos": sorted(r for r in repos if (viv.get(r) or {}).get("estado") == "muerto")}
    datos["_contenido"] = contenido
    if escribir:
        d = dir_salida(CANAL)
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{p.stem}.md").write_text(contenido, encoding="utf-8")
    return datos


def generar(solo: str | None = None, canal: str = "whatsapp", permitir_huecos: bool = False) -> int:
    if not medicion(canal).exists():
        print("falta la medición: correr --medir primero")
        return 1
    datos = json.loads(medicion(canal).read_text(encoding="utf-8"))
    med = {**datos.get("enlaces", {}), **datos["repos"]}  # repos por «owner/nombre», enlaces por URL
    filas, huecos = [], []
    for p in piezas(canal):
        if solo and numero(p) != solo:
            continue
        cuerpo, _ = cierre_viejo(p.read_text(encoding="utf-8", errors="replace"))
        faltan = [r for r in repos_citados(cuerpo) if r not in med]
        if faltan:
            huecos.append((p.name, faltan))
        filas.append(una(p, med))
    indice = [f"# ENVÍOS DE {'WHATSAPP' if canal == 'whatsapp' else 'FACEBOOK'} · índice", "",
              f"Generado el {hoy_efectivo()} a partir de la medición del mismo día "
              f"(`docs/envios/_medicion-{canal}.json`). Reglas y plan: `docs/envios/COMO-SE-MANDA.md`.", "",
              f"Cada archivo de `docs/envios/{canal}/` es un envío listo para copiar: portada, cuerpo "
              "partido en mensajes de menos de 4.000 caracteres y cierre con el estado de hoy. La pieza "
              "original no se toca; su sha256 va en la cabecera del envío, así que si la pieza cambia, el "
              "envío queda marcado como desactualizado.", "",
              "| Pieza | Título | Mensajes | Mayor | Repos | Muertos | Apéndice | Archivo |",
              "|---|---|---|---|---|---|---|---|"]
    for f in sorted(filas, key=lambda x: (x["numero"], x["pieza"])):
        titulo = (f.get("titulo") or "")[:70].replace("|", "/")
        nombre = Path(f["pieza"]).stem
        indice.append(f"| {f['numero']} | {titulo} | {f['mensajes']} | {f['mayor']} | {f['repos']} | "
                      f"{len(f['repos_muertos'])} | {'sí' if f['apendice'] else 'no'} | `{nombre}` |")
    tot = sum(f["mensajes"] for f in filas)
    indice += ["", f"**{len(filas)} piezas · {tot} mensajes** · el mayor de todos: "
                   f"{max((f['mayor'] for f in filas), default=0)} caracteres.", "",
               ""]
    d = dir_salida(canal)
    d.mkdir(parents=True, exist_ok=True)
    (d / "_INDICE.md").write_text("\n".join(indice) + "\n", encoding="utf-8")
    json.dump(filas, (SALIDA / f"_envios-{canal}.json").open("w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"generados {len(filas)} envíos · {tot} mensajes · mayor {max((f['mayor'] for f in filas), default=0)}")
    if huecos:
        # un cierre que dice «medí N repos» cuando la mitad no tienen dato es una mentira con fecha.
        print(f"AVISO: {len(huecos)} piezas citan repositorios sin medición de hoy:")
        for nombre, faltan in huecos[:6]:
            print(f"  · {nombre[:60]}: {', '.join(faltan[:4])}{'…' if len(faltan) > 4 else ''}")
        print("  vuelve a medir con --medir antes de publicar estos envíos")
        if not permitir_huecos:
            return 1
    return 0


# ─────────────────────────── verificar ───────────────────────────

def fecha_declarada(envio: str) -> str | None:
    """La fecha que el propio envío declara, para verificar un archivo archivado contra el
    generador *de su día*.

    Sin esto, todo envío nacía imposible de verificar a la mañana siguiente y la línea de CI se
    ponía roja sola cada medianoche aunque nadie hubiera tocado un byte. Se lee de la cabecera
    (`- **Envío generado:** AAAA-MM-DD`), que es la que el generador escribe siempre; si falta,
    se intenta la firma final.
    """
    m = re.search(r"En[ **]*vío generado:\*\*\s*(\d{4})-(\d{2})-(\d{2})", envio)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"💓[^\n]*?(\d{1,2}) de ([a-záéíóú]+) de (\d{4})", envio)
    if not m:
        return None
    meses = {v: k for k, v in MESES.items()}
    mes = m.group(2).lower()[:3]
    if mes not in meses:
        return None
    return f"{m.group(3)}-{meses[mes]:02d}-{int(m.group(1)):02d}"


def verificar(canal: str = "whatsapp") -> int:
    """Tres cosas: que quepa, que el cuerpo esté entero y que el archivo sea exactamente lo que el
    generador produce hoy. Si alguien edita un envío a mano, se nota."""
    fallos = []
    datos_med = (json.loads(medicion(canal).read_text(encoding="utf-8"))
                 if medicion(canal).exists() else {})
    med = {**datos_med.get("enlaces", {}), **datos_med.get("repos", {})}
    archivos = sorted(p for p in dir_salida(canal).glob("*.md") if not p.name.startswith("_"))
    for env in archivos:
        t = env.read_text(encoding="utf-8")
        bloques_msg = re.findall(r"^═══ MENSAJE \d+ de (\d+) · (\d+) caracteres ═══\n\n(.*?)(?=\n═══ |\n## APÉNDICE|\Z)",
                                 t, re.S | re.M)
        if not bloques_msg:
            fallos.append(f"{env.name}: sin mensajes")
            continue
        total = int(bloques_msg[0][0])
        if len(bloques_msg) != total:
            fallos.append(f"{env.name}: dice {total} mensajes y hay {len(bloques_msg)}")
        for etiqueta, largo, cuerpo in bloques_msg:
            if int(largo) > TOPE:
                fallos.append(f"{env.name}: un mensaje de {largo} caracteres (> {TOPE})")
            if int(largo) != len(cuerpo.rstrip("\n")):
                fallos.append(f"{env.name}: la cabecera dice {largo} y el mensaje tiene "
                              f"{len(cuerpo.rstrip())}")
            if "\u200d" in cuerpo:
                fallos.append(f"{env.name}: carácter de ancho cero en un mensaje")
            if cuerpo.count("```") % 2:
                fallos.append(f"{env.name}: valla de código sin cerrar en un mensaje")
        pieza = re.search(r"\*\*Pieza original:\*\* `([^`]+)`", t)
        sha = re.search(r"\*\*sha256 de la pieza:\*\* `([0-9a-f]{64})`", t)
        if not pieza or not sha:
            fallos.append(f"{env.name}: sin pieza o sin sha256")
            continue
        src = RAIZ / pieza.group(1)
        if not src.exists():
            fallos.append(f"{env.name}: la pieza citada no existe")
            continue
        if hashlib.sha256(src.read_bytes()).hexdigest() != sha.group(1):
            fallos.append(f"{env.name}: la pieza cambió desde que se generó el envío (regenerar)")
        original = src.read_text(encoding="utf-8", errors="replace")
        cuerpo_ok, apendice = cierre_viejo(original)
        enviado = "\n".join(c for _, _, c in bloques_msg)
        perdidas = [ln.strip() for ln in cuerpo_ok.split("\n")
                    if ln.strip() and not SEPARADOR.fullmatch(ln.strip())
                    and len(ln.strip()) > 3 and ln.strip() not in enviado]
        if perdidas:
            fallos.append(f"{env.name}: {len(perdidas)} líneas del cuerpo no llegaron al envío "
                          f"(ej.: {perdidas[0][:60]})")
        if apendice and "NO ENVIAR" not in t:
            fallos.append(f"{env.name}: apéndice sin la marca NO ENVIAR")
        if "💓" not in bloques_msg[-1][2]:
            fallos.append(f"{env.name}: el último mensaje no lleva firma")
        if med:
            global _FECHA_AS_OF
            previa, _FECHA_AS_OF = _FECHA_AS_OF, fecha_declarada(t)
            esperado = una(src, med, escribir=False)["_contenido"]
            _FECHA_AS_OF = previa
            if esperado != t:
                fallos.append(f"{env.name}: el archivo no coincide con lo que genera el programa "
                              f"(editado a mano o medición vieja: regenerar)")
    print(f"envíos revisados: {len(archivos)} · fallos: {len(fallos)}")
    for f in fallos[:25]:
        print("  ·", f)
    return 0 if not fallos else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--medir", action="store_true")
    ap.add_argument("--generar", action="store_true")
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--pieza", default=None)
    ap.add_argument("--canal", default="ambos", choices=("whatsapp", "facebook", "ambos"))
    ap.add_argument("--raiz", default=None, help="árbol alternativo (solo para la autoprueba)")
    ap.add_argument("--permitir-huecos", action="store_true",
                    help="genera aunque haya repos citados sin medición (no publicar así)")
    a = ap.parse_args()
    global RAIZ
    if a.raiz:
        RAIZ = Path(a.raiz).resolve()
        globals()["PUBLICACIONES"] = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
        globals()["SALIDA"] = RAIZ / "docs" / "envios"
    canales = ["whatsapp", "facebook"] if a.canal == "ambos" else [a.canal]
    global CANAL
    if a.medir:
        tok = os.environ.get("LBT") or ""
        if not tok:
            print("falta LBT en el entorno")
            return 1
        for c in canales:
            CANAL = c
            r = medir(tok, c)
            if r:
                return r
        return 0
    if a.generar:
        for c in canales:
            CANAL = c
            r = generar(a.pieza, c, a.permitir_huecos)
            if r:
                return r
        return 0
    if a.verificar:
        mal = 0
        for c in canales:
            CANAL = c
            mal += verificar(c)
        return 0 if mal == 0 else 1
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
