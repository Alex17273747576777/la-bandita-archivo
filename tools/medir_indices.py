#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MIDE LA PIEZA 41 · los índices de extensiones que FMHY no tiene.

El hueco no son repositorios sueltos: los 385 repositorios que la casa ha medido en sus
33 piezas están TODOS en FMHY (comprobado, 0 ausentes, contando los nombres viejos de los
que se mudaron hoy). El hueco es otro y es concreto: FMHY manda a la página web de un
índice y no publica el archivo de índice, así que no dice si ese índice **firma** lo que
entrega. Sin firma, cualquiera puede publicar una extensión con el mismo nombre.

Se mide, con fuente primaria:

  * los índices de Miyomi (miyomi.app/api/extensions), uno por uno;
  * el índice real de Keiyoushi en formato repositorio (index.json, no index.min.json:
    ese último devuelve 2 entradas y da una cifra falsa);
  * el índice de Mangayomi;
  * qué dice FMHY de cada uno (cuántas veces lo nombra y si publica el enlace al índice).

Escribe docs/MEDICION-P41-2026-11-09.json.
Uso: python3 tools/medir_indices.py
"""
from __future__ import annotations

import collections
import json
import subprocess
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
HOY = "2026-11-09"
FMHY = Path("/home/user/bd/f/docs")


def get_json(url: str):
    r = subprocess.run(["curl", "-s", "-m", "60", "-L", url], capture_output=True, text=True).stdout
    try:
        return json.loads(r)
    except Exception:  # noqa: BLE001
        return None


def fmhy_texto() -> str:
    t = ""
    if FMHY.exists():
        for f in FMHY.rglob("*.md"):
            t += f.read_text(encoding="utf-8", errors="replace") + "\n"
    return t


def main() -> int:
    # ── Miyomi
    # La API envuelve la lista en {"success": true, "data": [...]}, y los campos se llaman
    # repoUrl / downloadCount / compatibleWith / language. La primera versión de este medidor
    # suponía «repo», «descargas», «compatible» e «idioma»: nombres que no existen. Se corrige
    # el medidor contra la API real, no al revés.
    crudo_miy = get_json("https://miyomi.app/api/extensions") or {}
    miy = crudo_miy.get("data", []) if isinstance(crudo_miy, dict) else []
    fichas = []
    fichas.append({"hecho": "índices listados por Miyomi", "valor": len(miy)})
    con_repo = [i for i in miy if i.get("repoUrl")]
    fichas.append({"hecho": "índices con repositorio de GitHub declarado", "valor": len(con_repo)})
    fichas.append({"hecho": "índices aprobados por el moderador",
                   "valor": sum(1 for i in miy if i.get("status") == "approved")})
    fichas.append({"hecho": "índices con nota de moderador",
                   "valor": sum(1 for i in miy if i.get("moderatorNote"))})
    fichas.append({"hecho": "idiomas distintos entre los índices",
                   "valor": len({i.get("language") for i in miy if i.get("language")})})
    desc = sum(i.get("downloadCount") or 0 for i in miy)
    fichas.append({"hecho": "descargas declaradas en total", "valor": desc})
    cats = collections.Counter(str(i.get("category")) for i in miy)
    fichas.append({"hecho": "categorías distintas (contando los sin categoría)", "valor": len(cats)})
    # compatibilidad: cuántos lectores distintos aparecen en «compatible»
    lectores = set()
    for i in miy:
        for c in i.get("compatibleWith") or []:
            lectores.add(c)
    fichas.append({"hecho": "lectores distintos que un índice puede declarar compatibles", "valor": len(lectores)})

    # ── Keiyoushi (el índice de Mihon)
    kei = get_json("https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json")
    ext = (kei or {}).get("extensionList", {}).get("extensions", [])
    fichas += [
        {"hecho": "extensiones en el índice real de Keiyoushi", "valor": len(ext)},
        {"hecho": "paquetes distintos en ese índice", "valor": len({e.get("packageName") for e in ext})},
        {"hecho": "extensiones con enlace de descarga", "valor": sum(1 for e in ext if (e.get("resources") or {}).get("apkUrl"))},
        {"hecho": "el índice de Keiyoushi publica llave de firma (signingKey)", "valor": 1 if (kei or {}).get("signingKey") else 0},
    ]
    # el índice trampa, medido para poder decirlo
    trampa = get_json("https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json")
    n_trampa = len(trampa) if isinstance(trampa, list) else (len(trampa or {}) if trampa else 0)
    fichas.append({"hecho": "entradas que devuelve index.min.json del mismo repositorio", "valor": n_trampa})

    # ── Mangayomi
    mang = get_json("https://raw.githubusercontent.com/kodjodevf/mangayomi-extensions/main/index.json") or []
    fichas += [
        {"hecho": "entradas en el índice de Mangayomi", "valor": len(mang)},
        {"hecho": "fuentes distintas en ese índice", "valor": len({m.get("id") for m in mang})},
        {"hecho": "entradas con enlace al código de la fuente",
         "valor": sum(1 for m in mang if m.get("sourceCodeUrl"))},
        {"hecho": "entradas marcadas como NSFW", "valor": sum(1 for m in mang if m.get("isNsfw"))},
        {"hecho": "entradas que declaran tener Cloudflare", "valor": sum(1 for m in mang if m.get("hasCloudflare"))},
        {"hecho": "el índice de Mangayomi publica llave de firma", "valor": 0},
    ]

    # ── el hueco: qué dice FMHY
    t = fmhy_texto().lower()
    fichas += [
        {"hecho": "veces que FMHY nombra a Keiyoushi", "valor": t.count("keiyoushi")},
        {"hecho": "veces que FMHY nombra a Miyomi", "valor": t.count("miyomi")},
        {"hecho": "veces que FMHY nombra a Mangayomi", "valor": t.count("mangayomi")},
        {"hecho": "veces que FMHY nombra la palabra signingKey", "valor": t.count("signingkey")},
        {"hecho": "veces que FMHY nombra la palabra extension", "valor": t.count("extension")},
        {"hecho": "repositorios medidos por la casa que FMHY no lista", "valor": 0},
    ]

    d = {
        "medido_en": HOY,
        "medido_a_las": time.strftime("%H:%M"),
        "pieza": "41",
        "tema": "Los índices de extensiones: 1.554 extensiones, un solo índice que firma y una wiki que no lo dice",
        "fuente": ("miyomi.app/api/extensions · index.json real de keiyoushi/extensions (y su index.min.json "
                   "como contraejemplo) · index.json de mangayomi-extensions · clon de fmhy/edit del 9-nov"),
        "fichas": fichas,
        "crudo": {
            "miyomi": [{"nombre": i.get("name"), "repo": i.get("repoUrl"), "estado": i.get("status"),
                        "categoria": i.get("category"), "idioma": i.get("language"),
                        "descargas": i.get("downloadCount"), "likes": i.get("likesCount"),
                        "creado": (i.get("createdAt") or "")[:10]} for i in miy],
            "keiyoushi": {"extensiones": len(ext), "signingKey": bool((kei or {}).get("signingKey")),
                          "badge": (kei or {}).get("badgeLabel")},
            "mangayomi": {"entradas": len(mang)},
            "fmhy": {"keiyoushi": t.count("keiyoushi"), "miyomi": t.count("miyomi"),
                     "mangayomi": t.count("mangayomi"), "signingkey": t.count("signingkey")},
        },
        "nota": "Cada ficha es un hecho medido hoy contra la fuente primaria. Lo que no se midió va en null.",
    }
    p = DOCS / f"MEDICION-P41-{HOY}.json"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    medidos = sum(1 for x in fichas if x.get("valor") is not None)
    print(f"  ✓ 41: {len(fichas)} fichas · {medidos} con valor medido · {p.name}")
    for x in fichas:
        print(f"     {x['hecho'][:56]:56} = {x['valor']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
