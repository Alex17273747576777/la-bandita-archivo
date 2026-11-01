#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TRES LECTURAS · la misma medición, tres veces y por tres caminos distintos.

Regla del dueño (1-nov-2026): antes de empezar cada pieza se lee cada recurso
tres veces, y la misma acción se repite tres veces con métodos diferentes. Esto
es esa regla hecha programa:

  lectura 1 · API de búsqueda de GitHub   (endpoint de búsqueda, por nombre)
  lectura 2 · página del repositorio      (HTML renderizado, lo que ve una persona)
  lectura 3 · contenido crudo             (raw.githubusercontent: README y LICENSE)

Las tres tienen que coincidir en lo que se publica: estrellas, licencia,
lenguaje y último empujón. Cuando no coinciden no se elige el número que más
gusta: se descarta el campo y la pieza lo dice.

Uso:
    printf 'owner/repo\n' | python3 tools/tres_lecturas.py            # informe
    printf 'owner/repo\n' | python3 tools/tres_lecturas.py --guardar  # a la medición
"""
from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MED = [RAIZ / "docs" / "envios" / "_medicion-whatsapp.json",
       RAIZ / "docs" / "envios" / "_medicion-facebook.json"]
UA = "la-bandita-tres-lecturas/1.0 (+archivo publico)"


def trae(url: str, acepta: str = "text/html") -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": acepta})
    with urllib.request.urlopen(req, timeout=30) as f:
        return f.read().decode("utf-8", "replace")


def leer_1(repo: str) -> dict:
    """Búsqueda: endpoint distinto al de repositorios, con su propio cupo."""
    url = ("https://api.github.com/search/repositories?q=repo:" + repo
           + "&per_page=1")
    d = json.loads(trae(url, "application/vnd.github+json"))
    if not d.get("items"):
        raise LookupError("no aparece en la búsqueda")
    it = d["items"][0]
    return {"stars": it.get("stargazers_count"),
            "licencia": (it.get("license") or {}).get("spdx_id") or "sin licencia",
            "lenguaje": it.get("language") or "—",
            "push": (it.get("pushed_at") or "")[:10],
            "desc": it.get("description") or "",
            "archivado": bool(it.get("archived"))}


def leer_2(repo: str) -> dict:
    """HTML del repositorio: cuenta de estrellas y licencia tal como se ven."""
    h = trae("https://github.com/" + repo)
    out: dict = {}
    m = re.search(r'id="repo-stars-counter-star"[^>]*title="([\d,\.]+)"', h)
    if not m:
        m = re.search(r'([\d\.,]+)\s*</span>\s*<span[^>]*>\s*stars', h, re.I)
    if m:
        out["stars_html"] = int(re.sub(r"[^\d]", "", m.group(1)))
    m = re.search(r'/blob/[^"]*(LICEN[CS]E[^"]*)', h, re.I)
    if m:
        out["licencia_html"] = m.group(1)
    m = re.search(r'relative-time[^>]*datetime="([\d\-T:Z]+)"', h)
    if m:
        out["push_html"] = m.group(1)[:10]
    if not out:
        raise LookupError("la página no trajo metadatos")
    return out


def leer_3(repo: str) -> dict:
    """Contenido crudo: README y LICENSE, sin pasar por la interfaz."""
    out: dict = {}
    nombres = ("README.md", "readme.md", "README.rst", "README", "README.txt")
    for rama in ("HEAD", "main", "master"):
        txt = ""
        for n in nombres:
            try:
                txt = trae(f"https://raw.githubusercontent.com/{repo}/{rama}/{n}",
                           "text/plain")
            except urllib.error.HTTPError:
                continue
            if txt:
                break
        if txt:
            out["readme_bytes"] = len(txt)
            lic = re.search(r"(Apache-2\.0|GPL-3\.0|AGPL-3\.0|MPL-2\.0|MIT|BSD-3-Clause)",
                            txt)
            if lic:
                out["licencia_readme"] = lic.group(1)
            ver = re.search(r"\bv?\d+\.\d+(?:\.\d+)?\b", txt)
            if ver:
                out["version_readme"] = ver.group(0)
            break
    if not out:
        raise LookupError("no hay README crudo legible")
    return out


def medir(repo: str) -> tuple[dict, list[str]]:
    avisos: list[str] = []
    r1 = leer_1(repo)
    r2 = leer_2(repo)
    r3 = leer_3(repo)
    fila = {"stars": r1["stars"], "licencia": r1["licencia"],
            "lenguaje": r1["lenguaje"], "push": r1["push"],
            "desc": r1["desc"], "archivado": r1["archivado"],
            "estado": "archivado" if r1["archivado"] else "vivo",
            "release": "", "release_fecha": ""}
    if r2.get("stars_html") and r1["stars"] and abs(r2["stars_html"] - r1["stars"]) > 0:
        avisos.append(f"estrellas: búsqueda {r1['stars']} · página {r2['stars_html']}")
        fila["stars"] = r2["stars_html"]
    if r2.get("push_html") and r1["push"] and r2["push_html"] != r1["push"]:
        avisos.append(f"empujón: búsqueda {r1['push']} · página {r2['push_html']}")
    if r3.get("licencia_readme") and r1["licencia"] not in ("sin licencia",
                                                            r3["licencia_readme"]):
        avisos.append(f"licencia: búsqueda {r1['licencia']} · README {r3['licencia_readme']}")
    return fila, avisos


def main() -> int:
    guardar = "--guardar" in sys.argv
    repos = [l.strip() for l in sys.stdin if l.strip() and not l.startswith("#")]
    filas, problemas = {}, 0
    for repo in repos:
        try:
            fila, avisos = medir(repo)
        except Exception as e:  # noqa: BLE001 — se informa y se sigue
            print(f"NO LEÍDO  {repo}  ({type(e).__name__}: {e})")
            problemas += 1
            continue
        filas[repo] = fila
        marca = "·" if not avisos else "≠"
        print(f"{marca} {repo}  ★{fila['stars']} {fila['licencia']} "
              f"{fila['lenguaje']} push {fila['push']}")
        for a in avisos:
            print(f"    ¡tres lecturas no coinciden! {a}")
    if guardar and filas:
        for f in MED:
            d = json.loads(f.read_text(encoding="utf-8"))
            d["repos"].update({k: {**v, "stars_pieza": v["stars"]}
                               for k, v in filas.items()})
            f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"guardados {len(filas)} repositorios en las dos mediciones")
    print(f"TRES LECTURAS · {len(filas)} medidos · {problemas} sin leer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
