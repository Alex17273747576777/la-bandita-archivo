#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PREFLIGHT · la revisión obligatoria antes de sondear cualquier pieza.

Nace de la regla del dueño del 4-nov-2026, noche: «siempre antes de proceder con las
publicaciones pendientes, debemos estar revisando primero el historial antiguo y la fecha,
además de obviamente todo el ecosistema de recursos de código abierto, cada vez, antes de
empezar a sondear». Y de la comprobación de que el disco local no es de fiar: esta
herramienta escribe su acta y el resultado se empuja a GitHub (H22).

Hace tres cosas, en este orden y no en otro:

  1. LA FECHA     la lee en vivo de una fuente de fuera y la deja anotada (tools/fecha_viva).
  2. EL HISTORIAL qué piezas están publicadas ya, cuáles siguen pendientes según el mapa de
                  125, y con qué título y gancho, para no repetir tema ni cifras.
  3. EL ECOSISTEMA sondea GitHub por fecha de creación y por tema, antes de elegir nada:
                  devuelve los candidatos con su fecha de nacimiento, su empujón y sus
                  estrellas, medidos hoy.

Uso:
    LBT=<token> python3 tools/preflight.py --tema descarga
    LBT=<token> python3 tools/preflight.py --tema descarga --min-estrellas 50 --por-consulta 8
    python3 tools/preflight.py --historial      # solo 1 y 2, sin red de sondeo

Sale con 1 si el historial y el mapa no cuadran, para que no se escriba a ciegas.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
PUBL = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES" / "Facebook-dominicano-ES"
API = "https://api.github.com"

# Temas del mapa de 125 con sus consultas de sondeo. Cada consulta se lanza tal cual contra
# la API de búsqueda; el resultado se deduplica y se ordena por estrellas.
TOPICOS = {
    "descarga": [
        ("gestor de descargas", "download manager created:>2026-01-01"),
        ("descargador de medios", "media downloader created:>2026-04-01"),
        ("cara para yt-dlp", "yt-dlp android created:>2026-01-01"),
        ("vídeo por trozos", "m3u8 downloader created:>2026-01-01"),
        ("galerías y lotes", "gallery downloader created:>2026-01-01"),
        ("motor clásico", "aria2 gui"),
    ],
    "torrent": [
        ("clientes", "torrent client created:>2026-01-01"),
        ("herramientas", "torrent tools created:>2025-06-01"),
    ],
    "radio": [
        ("radio por internet", "internet radio android created:>2026-01-01"),
        ("directo y listas", "iptv player created:>2026-01-01"),
    ],
    "imagen": [
        ("galería", "gallery android created:>2026-01-01"),
        ("edición", "image editor created:>2026-01-01"),
        ("ocr", "ocr created:>2026-01-01"),
    ],
    "teclado": [
        ("teclado con IA", "ai keyboard created:>2026-01-01"),
        ("teclado para Android", "keyboard android ime created:>2026-01-01"),
        ("dictado por voz", "voice dictation created:>2025-06-01"),
        ("habla a texto sin nube", "speech to text offline whisper created:>2025-01-01"),
        ("atajos y plantillas", "text expander snippet created:>2025-01-01"),
        ("reescritura en línea", "grammar rewrite writing assistant created:>2026-01-01"),
    ],
    "red": [
        ("dns", "dns android created:>2026-01-01"),
        ("vpn", "vpn client created:>2026-01-01"),
    ],
}


def token() -> str | None:
    return os.environ.get("LBT") or os.environ.get("GHP_A") or os.environ.get("GITHUB_TOKEN")


def gh(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "la-bandita-preflight"})
    t = token()
    if t:
        req.add_header("Authorization", f"Bearer {t}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


# ── 1 · la fecha ────────────────────────────────────────────────────────────────────────
def paso_fecha() -> dict:
    out = subprocess.run([sys.executable, str(RAIZ / "tools" / "fecha_viva.py"), "--inicio"],
                         capture_output=True, text=True, cwd=RAIZ)
    linea = (out.stdout or "").strip().splitlines()
    print("1 · LA FECHA")
    for l in linea[:3]:
        print("   " + l.strip())
    return {"salida": linea[:3], "codigo": out.returncode}


# ── 2 · el historial ────────────────────────────────────────────────────────────────────
def piezas_publicadas() -> list[dict]:
    vistos = []
    if not PUBL.exists():
        return vistos
    for f in sorted(PUBL.glob("*.md")):
        m = re.match(r"^(\d{2})-(.+)\.md$", f.name)
        if m:
            vistos.append({"n": int(m.group(1)), "titulo": m.group(2).replace("-", " "), "archivo": f.name})
    return vistos


def mapa() -> dict[int, dict]:
    """Lee el mapa de 125 y devuelve número → {pieza, gancho}."""
    p = DOCS / "MAPA-125-FACEBOOK.md"
    if not p.exists():
        return {}
    filas = {}
    for linea in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*\*\*(\d{2,3})\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|", linea)
        if m:
            filas[int(m.group(1))] = {"pieza": m.group(2).strip(), "gancho": m.group(3).strip()}
    return filas


def paso_historial() -> dict:
    publicadas = piezas_publicadas()
    m = mapa()
    hechas = {p["n"] for p in publicadas}
    pendientes = [(n, m[n]) for n in sorted(m) if n not in hechas]
    print("\n2 · EL HISTORIAL")
    print(f"   publicadas: {len(publicadas)} · en el mapa: {len(m)} · pendientes: {len(pendientes)}")
    for p in publicadas[-4:]:
        print(f"   ✓ {p['n']:02d} {p['titulo'][:72]}")
    for n, d in pendientes[:3]:
        print(f"   → {n:02d} {d['pieza'][:40]:42s} · {d['gancho'][:60]}")
    return {"publicadas": [p["n"] for p in publicadas],
            "siguiente": pendientes[0][0] if pendientes else None,
            "pendientes": [n for n, _ in pendientes[:10]]}


# ── 3 · el ecosistema ───────────────────────────────────────────────────────────────────
def paso_ecosistema(tema: str, por_consulta: int, min_estrellas: int) -> dict:
    consultas = TOPICOS.get(tema)
    if not consultas:
        print(f"\n3 · EL ECOSISTEMA · tema «{tema}» sin consultas declaradas")
        return {"tema": tema, "candidatos": []}
    print(f"\n3 · EL ECOSISTEMA · tema «{tema}» · {len(consultas)} consultas antes de sondear nada")
    vistos: dict[str, dict] = {}
    hoy = date.today()
    for etiqueta, q in consultas:
        url = f"{API}/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page={por_consulta}"
        try:
            d = gh(url)
        except Exception as e:  # rate limit o red: se dice y se sigue
            print(f"   ! {etiqueta}: {e}")
            time.sleep(6)
            continue
        items = d.get("items") or []
        print(f"   · {etiqueta:24s} {len(items)} resultados")
        for r in items:
            if r["stargazers_count"] < min_estrellas:
                continue
            nace = date.fromisoformat(r["created_at"][:10])
            vistos[r["full_name"]] = {
                "repo": r["full_name"], "stars": r["stargazers_count"],
                "creado": r["created_at"][:10], "dias_nace": (hoy - nace).days,
                "push": r["pushed_at"][:10], "licencia": (r.get("license") or {}).get("spdx_id"),
                "archivado": r["archived"], "consulta": etiqueta}
        time.sleep(2)  # la búsqueda sin token va a 10/min; con token, 30/min
    cand = sorted(vistos.values(), key=lambda x: -x["stars"])
    for c in cand[:15]:
        print(f"   {c['repo']:44s} ★{c['stars']:>6} nace {c['creado']} ({c['dias_nace']:>4} d) push {c['push']}")
    return {"tema": tema, "consultas": [q for _, q in consultas], "candidatos": cand}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tema", default=None, help="tema del mapa a sondear: " + ", ".join(TOPICOS))
    ap.add_argument("--por-consulta", type=int, default=8)
    ap.add_argument("--min-estrellas", type=int, default=30)
    ap.add_argument("--historial", action="store_true", help="solo fecha e historial")
    a = ap.parse_args()

    print("PREFLIGHT · la revisión obligatoria antes de sondear (H21/H22)\n")
    f = paso_fecha()
    h = paso_historial()
    e = paso_ecosistema(a.tema, a.por_consulta, a.min_estrellas) if (a.tema and not a.historial) else {}

    hoy = date.today().isoformat()
    salida = DOCS / f"PREFLIGHT-{a.tema or 'historial'}-{hoy}.json"
    salida.write_text(json.dumps({
        "fecha": hoy, "medido_en": datetime.now().astimezone().isoformat(timespec="seconds"),
        "fecha_viva": f, "historial": h, "ecosistema": e,
        "regla": "siempre GitHub; nunca almacenamiento local con pérdida (H22)"},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nacta: {salida.relative_to(RAIZ)} · {len(e.get('candidatos', []))} candidatos")
    return 0 if h["siguiente"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
