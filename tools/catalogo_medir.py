#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""catalogo_medir.py · mide los recursos del catálogo y guarda la evidencia.

Para cada recurso, en este orden:

  1 · lo que dice GitHub: estrellas, licencia, archivado, empujón, creación.
  2 · la última entrega etiquetada, si la hay.
  3 · el README real (raw), y de él: el primer párrafo con contenido, las líneas
      que hablan de instalar y las plataformas que menciona.
  4 · las banderas de texto que la IA no ve si no se le piden: soporte negado,
      abandono declarado, espejo, requisito de root o de Shizuku.

No interpreta. Guarda lo medido con su fecha y su URL, y deja el juicio para la
ficha, que es donde se puede leer.

Uso:
    python3 tools/catalogo_medir.py                 # todos los racimos
    python3 tools/catalogo_medir.py --racimo audio  # uno solo
    python3 tools/catalogo_medir.py --limpio        # tira lo medido y empieza de cero
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
RECURSOS = CATALOGO / "recursos.json"
MEDIDO = CATALOGO / "medido.json"
TOKEN = os.environ.get("GHP_A") or os.environ.get("GITHUB_TOKEN")

CAB = {"Accept": "application/vnd.github+json", "User-Agent": "la-bandita/catalogo"}

BANDERAS = [
    ("pide root", r"\broot\b|superusuario|\bsu\b binary"),
    ("pide shizuku", r"shizuku"),
    ("pide magisk", r"magisk|\bxposed\b|lsposed"),
    ("soporte negado", r"no support|sin soporte|unsupported|no longer supported|not maintained"),
    ("abandono declarado", r"unmaintained|abandoned|deprecated|archiv|won'?t be updated"),
    ("espejo declarado", r"\bmirror\b|espejo|fork of|derivado de"),
    ("aviso de retirada", r"dmca|takedown|cease and desist"),
]

PLATAFORMAS = [
    ("Android", r"android|\bapk\b|f-droid|play store"),
    ("iOS", r"\bios\b|iphone|ipad|app store"),
    ("Windows", r"windows|\bexe\b|\.msi\b"),
    ("macOS", r"macos|\bbrew\b|\.dmg\b"),
    ("Linux", r"\blinux\b|\.deb\b|flatpak|appimage|\.rpm\b|snap"),
    ("Web", r"self-host|docker|servidor|server|web ui|navegador"),
]


def pide(url: str, crudo: bool = False, intentos: int = 2):
    cab = dict(CAB)
    if TOKEN and "api.github.com" in url:
        cab["Authorization"] = "token " + TOKEN
    for n in range(intentos):
        try:
            r = urllib.request.Request(url, headers=cab)
            with urllib.request.urlopen(r, timeout=40) as f:
                datos = f.read(2_000_000)
                return datos if crudo else json.loads(datos)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and n + 1 < intentos:
                time.sleep(20)
                continue
            return {"_error": f"HTTP {e.code}"} if not crudo else b""
        except Exception:  # noqa: BLE001
            if n + 1 < intentos:
                time.sleep(3)
                continue
            return {"_error": "sin respuesta"} if not crudo else b""
    return {"_error": "sin respuesta"} if not crudo else b""


def primer_parrafo(texto: str) -> str:
    """El primer párrafo con contenido que no sea un título, un escudo ni una tabla."""
    for bloque in re.split(r"\n\s*\n", texto):
        b = bloque.strip()
        if not b or b.startswith("#") or b.startswith("![") or b.startswith("[!["):
            continue
        if b.startswith("|") or b.startswith("<") or b.startswith("[!"):
            continue
        limpio = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", b)
        limpio = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", limpio)
        limpio = re.sub(r"[*_`>#]", "", limpio).strip()
        if len(limpio) > 60:
            return re.sub(r"\s+", " ", limpio)[:400]
    return ""


def lineas_de_instalacion(texto: str) -> list[str]:
    salida = []
    for l in texto.splitlines():
        t = l.strip()
        if len(t) < 8 or len(t) > 200:
            continue
        if re.search(r"install|instal|descarg|download|requisit|requiere|prerrequisit|setup", t, re.I):
            limpio = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
            limpio = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", lambda m: m.group(1) or m.group(2), limpio)
            limpio = re.sub(r"^[#>*\-\s]+", "", limpio).strip()
            limpio = re.sub(r"\s+", " ", limpio)
            if not re.search(r"[a-zA-Záéíóúñ]{4,}", limpio):
                continue
            if limpio.startswith("http"):
                limpio = "la web que da el proyecto: " + limpio
            if 10 < len(limpio) < 160 and limpio not in salida:
                salida.append(limpio)
        if len(salida) >= 4:
            break
    return salida


def medir(repo: str) -> dict:
    meta = pide(f"https://api.github.com/repos/{repo}")
    if meta.get("_error") or meta.get("message"):
        return {"repo": repo, "existe": False, "error": meta.get("_error") or meta.get("message")}

    rel = pide(f"https://api.github.com/repos/{repo}/releases/latest")
    entrega = None
    if isinstance(rel, dict) and rel.get("tag_name"):
        entrega = {"tag": rel["tag_name"], "fecha": (rel.get("published_at") or "")[:10],
                   "adjuntos": len(rel.get("assets") or [])}

    leeme = pide(f"https://raw.githubusercontent.com/{repo}/HEAD/README.md", crudo=True)
    texto = leeme.decode("utf-8", "replace") if isinstance(leeme, bytes) else ""

    banderas = []
    for etiqueta, patron in BANDERAS:
        m = re.search(patron, texto, re.I)
        if m:
            banderas.append(etiqueta)
    plataformas = [n for n, patron in PLATAFORMAS if re.search(patron, texto, re.I)]

    return {
        "repo": repo,
        "existe": True,
        "nombre": meta.get("name"),
        "descripcion": (meta.get("description") or "").strip(),
        "estrellas": meta.get("stargazers_count"),
        "forks": meta.get("forks_count"),
        "archivado": meta.get("archived"),
        "deshabilitado": meta.get("disabled"),
        "licencia": (meta.get("license") or {}).get("spdx_id"),
        "empujon": (meta.get("pushed_at") or "")[:10],
        "creado": (meta.get("created_at") or "")[:10],
        "incidencias_abiertas": meta.get("open_issues_count"),
        "lenguaje": meta.get("language"),
        "temas": (meta.get("topics") or [])[:6],
        "entrega": entrega,
        "web": meta.get("homepage") or None,
        "leeme_bytes": len(texto),
        "claim": primer_parrafo(texto),
        "instalacion": lineas_de_instalacion(texto),
        "plataformas": plataformas,
        "banderas": banderas,
        "medido": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def main() -> int:
    if not RECURSOS.exists():
        sys.exit("falta catalogo/recursos.json: primero hay que declarar los recursos por racimo")
    recursos = json.loads(RECURSOS.read_text(encoding="utf-8"))
    # siempre se parte de lo que ya había: medir un racimo no puede borrar los demás
    previo = json.loads(MEDIDO.read_text(encoding="utf-8")) if MEDIDO.exists() else {}
    if "--limpio" in sys.argv:
        previo = {}

    solo = None
    if "--racimo" in sys.argv:
        solo = sys.argv[sys.argv.index("--racimo") + 1]

    todos = []
    for racimo, lista in recursos["racimos"].items():
        if solo and racimo != solo:
            continue
        for r in lista:
            todos.append((racimo, r["repo"] if isinstance(r, dict) else r))

    hecho, fallado = 0, 0
    for i, (racimo, repo) in enumerate(todos, 1):
        if repo in previo and isinstance(previo[repo], dict) and previo[repo].get("existe"):
            continue
        f = medir(repo)
        f["racimo"] = racimo
        previo[repo] = f
        hecho += 1
        if not f.get("existe"):
            fallado += 1
        if i % 20 == 0:
            print(f"  {i}/{len(todos)} medidos · último: {repo}", flush=True)
            MEDIDO.write_text(json.dumps(previo, ensure_ascii=False, indent=1), encoding="utf-8")

    MEDIDO.write_text(json.dumps(previo, ensure_ascii=False, indent=1), encoding="utf-8")
    vivos = sum(1 for v in previo.values() if v.get("existe"))
    print(f"medidos: {len(previo)} · vivos: {vivos} · sin respuesta: {fallado} · escritos en {MEDIDO.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
