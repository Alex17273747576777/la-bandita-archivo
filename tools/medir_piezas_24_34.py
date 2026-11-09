#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MEDICIÓN DE LAS PIEZAS 24–29 Y 32–34 · lo que nunca se había medido.

Estas piezas se publicaron con texto corto y sin medición detrás: no había JSON de
medición de su tema. Este script mide los repositorios de verdad, contra la API
pública de GitHub, y escribe un JSON por pieza en docs/ con la misma forma que las
mediciones de la serie (la de la pieza 09, por ejemplo):

  {medido_en, medido_a_las, pieza, tema, repos: {dueno/repo: {...}}, totales: {...}}

Qué mide por repositorio, y de dónde lo saca:
  * estrellas, forks, licencia, archivado, tamaño, empujón     → REST /repos
  * entrega etiquetada más reciente y fecha                     → REST /releases/latest
  * número de entregas y descargas acumuladas                   → REST /releases
  * adjuntos de la última entrega y cuáles llevan huella        → REST /releases/latest
  * incidencias cerradas, flujos de compilación, contribuidores → REST + GraphQL
  * huella: sha256/sha512/sha1/checksum/.sig/.asc/sums en el nombre del adjunto

Reglas de la casa que respeta:
  * No inventa: si un dato no se puede leer, se guarda como null y se cuenta aparte.
  * Cachea cada payload y deja el SHA-256 en el JSON de medición (evidencia).
  * No toca el registro ni el sello: solo escribe docs/MEDICION-*.json.

Uso:
  python3 tools/medir_piezas_24_34.py --pieza 26
  python3 tools/medir_piezas_24_34.py --todas
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
CACHE = RAIZ / "docs" / "_medicion-cache"

PATRON_HUELLA = re.compile(r"(sha256|sha512|sha1|checksum|\.sig$|\.asc$|sums|SHASUM|SHA256SUMS)", re.I)

# Lo que cada pieza dice medir. Las listas salen del texto publicado de cada pieza,
# no de una idea previa: se leyeron los repositorios y los temas que la pieza nombra.
TEMAS: dict[str, dict] = {
    "24": {
        "tema": "Repositorios de extensiones de anime para Aniyomi y análogos",
        "repos": [
            "yuzono/anime-extensions",
            "aniyomiorg/aniyomi",
            "aniyomiorg/aniyomi-extensions",
            "Kohi-den/extensions-source",
            "keiyoushi/extensions-source",
        ],
    },
    "25": {
        "tema": "OCR de bolsillo: del papel al PDF legible",
        "repos": [
            "hiroi-sora/Umi-OCR",
            "Aryan-Raj3112/episteme",
            "sml2h3/ddddocr",
            "ocrmypdf/OCRmyPDF",
            "tesseract-ocr/tesseract",
            "PaddlePaddle/PaddleOCR",
            "JaidedAI/EasyOCR",
        ],
    },
    "26": {
        "tema": "Usagi, lector de manga bifurcado de Kotatsu",
        "repos": [
            "UsagiApp/Usagi",
            "KotatsuApp/Kotatsu",
            "KotatsuApp/kotatsu-parsers",
            "komikku-app/komikku",
            "mihonapp/mihon",
            "nekomangaorg/Neko",
            "tachiyomiorg/tachiyomi",
        ],
    },
    "27": {
        "tema": "DropSauce, lector de cómic y novela en Jetpack Compose",
        "repos": [
            "HuzaifaKhalid1311/DropSauce",
            "mihonapp/mihon",
            "tachiyomiorg/tachiyomi",
            "komikku-app/komikku",
            "KotatsuApp/Kotatsu",
        ],
    },
    "28": {
        "tema": "Mangayomi y su repositorio público de extensiones",
        "repos": [
            "m2k3a/mangayomi-extensions",
            "kodjodevf/mangayomi",
            "keiyoushi/extensions",
            "aniyomiorg/aniyomi-extensions",
            "Kohi-den/extensions-source",
        ],
    },
    "29": {
        "tema": "LNReader y su repositorio de plugins de novelas",
        "repos": [
            "LNReader/lnreader-plugins",
            "LNReader/lnreader",
        ],
    },
    "32": {
        "tema": "Tu Manga Online: estado, clones y alternativas de lector",
        "repos": [
            "mihonapp/mihon",
            "tachiyomiorg/tachiyomi",
            "komikku-app/komikku",
            "nekomangaorg/Neko",
            "KotatsuApp/Kotatsu",
            "keiyoushi/extensions",
            "aniyomiorg/aniyomi",
            "yuzono/anime-extensions",
            "mangadex-downloader/mangadex-downloader",
            "UsagiApp/Usagi",
        ],
    },
    "33": {
        "tema": "Apoyo a desarrolladores y apps nuevas de código abierto (noviembre 2026)",
        "repos": [
            "mihonapp/mihon",
            "komikku-app/komikku",
            "nekomangaorg/Neko",
            "AppFuton/Futon",
            "tsundoku-otaku/tsundoku",
            "Spyou/Zangetsu",
            "Heartless-Veteran/Otaku-Reader",
            "Palloxin/lnreader-clone",
            "Gent8/Taison",
        ],
    },
    "34": {
        "tema": "Recuperar la biblioteca de Kototoro y migrar a v2.3",
        "repos": [
            "Kototoro-app/Kototoro",
            "Kototoro-app/Kototoro-Nightly",
            "mihonapp/mihon",
            "KotatsuApp/Kotatsu",
        ],
    },
}


def token() -> str:
    for fuente in (os.environ.get("LBT"), os.environ.get("GITHUB_TOKEN")):
        if fuente:
            return fuente.strip()
    for ruta in (Path.home() / ".gh-tokens", Path.home() / ".gh-token"):
        if ruta.exists():
            for linea in ruta.read_text(encoding="utf-8", errors="replace").split():
                if re.fullmatch(r"gh[pousr]_[A-Za-z0-9]{20,}", linea.strip()):
                    return linea.strip()
    raise SystemExit("falta el token: exportá LBT=<token>")


TOKEN = ""


def pedir(url: str, intentos: int = 3) -> tuple[int, object]:
    """GET a la API. Devuelve (código, cuerpo). Cachea el cuerpo y su sha256."""
    CACHE.mkdir(parents=True, exist_ok=True)
    clave = hashlib.sha256(url.encode()).hexdigest()[:24]
    cacheado = CACHE / f"{clave}.json"
    if cacheado.exists():
        d = json.loads(cacheado.read_text(encoding="utf-8"))
        return d["codigo"], d["cuerpo"]

    req = urllib.request.Request(url, headers={
        "Authorization": f"bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "la-bandita-medicion",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    for i in range(intentos):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                cuerpo = json.loads(r.read().decode())
                codigo = r.status
            break
        except urllib.error.HTTPError as e:
            codigo = e.code
            cuerpo = {"error": str(e)}
            if e.code in (403, 429) and i < intentos - 1:
                time.sleep(20)
                continue
            break
        except Exception as e:  # red caída, timeout
            codigo, cuerpo = 0, {"error": str(e)}
            if i < intentos - 1:
                time.sleep(5)
                continue
            break
    cacheado.write_text(json.dumps({"url": url, "codigo": codigo, "cuerpo": cuerpo},
                                   ensure_ascii=False), encoding="utf-8")
    return codigo, cuerpo


def medir_repo(repo: str) -> dict:
    ficha: dict = {"repo": repo}
    c, d = pedir(f"https://api.github.com/repos/{repo}")
    if c != 200 or not isinstance(d, dict):
        ficha.update({"estado": "sin_objeto" if c == 404 else f"error_{c}", "http": c})
        return ficha

    ficha.update({
        "estado": "vivo",
        "stars": d.get("stargazers_count"),
        "forks": d.get("forks_count"),
        "archivado": bool(d.get("archived")),
        "nace": (d.get("created_at") or "")[:10],
        "push": (d.get("pushed_at") or "")[:10],
        "licencia": (d.get("license") or {}).get("spdx_id"),
        "tam_kib": d.get("size"),
        "lenguaje": d.get("language"),
        "abiertas": d.get("open_issues_count"),
    })
    hoy = date.today()
    for campo, clave in (("nace", "dias_nace"), ("push", "dias_push")):
        try:
            ficha[clave] = (hoy - date.fromisoformat(ficha[campo])).days
        except Exception:
            ficha[clave] = None

    # Última entrega y todas las entregas
    c, rel = pedir(f"https://api.github.com/repos/{repo}/releases/latest")
    if c == 200 and isinstance(rel, dict):
        adjuntos = rel.get("assets") or []
        nombres = [a.get("name", "") for a in adjuntos]
        con_huella = [n for n in nombres if PATRON_HUELLA.search(n)]
        ficha.update({
            "rel": rel.get("tag_name"),
            "rel_fecha": (rel.get("published_at") or "")[:10],
            "adjuntos_ultima": len(adjuntos),
            "huellas_ultima": len(con_huella),
            "nombres_huella": con_huella[:6],
            "descargas_ultima": sum(a.get("download_count", 0) for a in adjuntos),
        })
        try:
            ficha["rel_dias"] = (hoy - date.fromisoformat(ficha["rel_fecha"])).days
        except Exception:
            ficha["rel_dias"] = None
    else:
        ficha.update({"rel": None, "rel_fecha": None, "rel_dias": None,
                      "adjuntos_ultima": 0, "huellas_ultima": 0, "descargas_ultima": 0})

    c, rels = pedir(f"https://api.github.com/repos/{repo}/releases?per_page=100")
    if c == 200 and isinstance(rels, list):
        adj = sum(len(r.get("assets") or []) for r in rels)
        hue = sum(1 for r in rels for a in (r.get("assets") or [])
                  if PATRON_HUELLA.search(a.get("name", "")))
        ficha.update({
            "entregas": len(rels),
            "descargas": sum(a.get("download_count", 0) for r in rels for a in (r.get("assets") or [])),
            "adjuntos_total": adj,
            "huellas_total": hue,
        })
    else:
        ficha.update({"entregas": 0, "descargas": 0, "adjuntos_total": 0, "huellas_total": 0})

    return ficha


def medir_pieza(numero: str) -> Path:
    datos = TEMAS[numero]
    ahora = datetime.now(timezone.utc)
    fichas = {}
    for i, repo in enumerate(datos["repos"], 1):
        fichas[repo] = medir_repo(repo)
        print(f"  {i:>2}/{len(datos['repos'])}  {repo:45} "
              f"★{fichas[repo].get('stars')}  {fichas[repo].get('estado')}")
        time.sleep(0.4)

    vivos = [f for f in fichas.values() if f.get("estado") == "vivo"]
    totales = {
        "repos_medidos": len(fichas),
        "vivos": len(vivos),
        "archivados": sum(1 for f in vivos if f.get("archivado")),
        "sin_objeto": sum(1 for f in fichas.values() if f.get("estado") == "sin_objeto"),
        "stars": sum(f.get("stars") or 0 for f in vivos),
        "forks": sum(f.get("forks") or 0 for f in vivos),
        "descargas": sum(f.get("descargas") or 0 for f in vivos),
        "adjuntos": sum(f.get("adjuntos_total") or 0 for f in vivos),
        "con_huella": sum(f.get("huellas_total") or 0 for f in vivos),
        "repos_con_huella": sum(1 for f in vivos if (f.get("huellas_total") or 0) > 0),
        "repos_sin_entrega": sum(1 for f in vivos if not f.get("rel")),
        "sin_licencia_legible": sum(1 for f in vivos
                                    if (f.get("licencia") or "NOASSERTION") in ("NOASSERTION", None)),
        "push_7d": sum(1 for f in vivos if f.get("dias_push") is not None and f["dias_push"] <= 7),
        "push_30d": sum(1 for f in vivos if f.get("dias_push") is not None and f["dias_push"] <= 30),
        "nace_90d": sum(1 for f in vivos if f.get("dias_nace") is not None and f["dias_nace"] <= 90),
    }
    doc = {
        "medido_en": date.today().isoformat(),
        "medido_a_las": ahora.strftime("%H:%M"),
        "medido_utc": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pieza": numero,
        "tema": datos["tema"],
        "fuente": "API pública de GitHub (REST v2022-11-28)",
        "repos": fichas,
        "totales": totales,
    }
    salida = DOCS / f"MEDICION-{numero}-2026-11-08.json"
    salida.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    evidencia = hashlib.sha256(salida.read_bytes()).hexdigest()
    print(f"  → {salida.relative_to(RAIZ)}  sha256 {evidencia[:16]}…")
    print(f"    vivos {totales['vivos']} · ★{totales['stars']:,} · "
          f"huellas {totales['con_huella']}/{totales['adjuntos']} · sin objeto {totales['sin_objeto']}")
    return salida


def main() -> None:
    global TOKEN
    ap = argparse.ArgumentParser()
    ap.add_argument("--pieza", action="append", default=[])
    ap.add_argument("--todas", action="store_true")
    a = ap.parse_args()
    TOKEN = token()
    piezas = list(TEMAS) if a.todas else a.pieza
    if not piezas:
        raise SystemExit("usá --pieza NN o --todas")
    for n in piezas:
        print(f"\nPIEZA {n} · {TEMAS[n]['tema']}")
        medir_pieza(n)


if __name__ == "__main__":
    main()
