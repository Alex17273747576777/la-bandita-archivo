#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CENSO DE ÍNDICES · qué repositorios enlazan los catálogos que la casa no había mirado.

Toma las páginas de fmhy.net (y las que se le pasen con --url), saca **todos los
enlaces a GitHub** con su sección, y los cruza contra `registry/` para separar dos
cosas que hasta ahora se mezclaban:

  * **recursos nuevos**: repositorios que FMHY lista y la casa nunca ha medido;
  * **ya medidos**: los que están en el registro, con la fecha de su ficha.

No mide nada contra la API: eso es el paso siguiente (`tools/medir_censo.py`). Este
solo construye el censo y lo deja en `docs/CENSO-FMHY-<fecha>.json`.

Qué NO hace: no descarga contenido, no sigue enlaces de espejos ni de descarga, y
no valida que el recurso sea bueno — solo que existe como repositorio enlazado.
"""
from __future__ import annotations

import argparse
import glob
import html
import json
import re
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
REGISTRO = RAIZ / "registry"

PAGINAS = [
    "https://fmhy.net/mobile",
    "https://fmhy.net/reading",
    "https://fmhy.net/downloading",
    "https://fmhy.net/torrenting",
    "https://fmhy.net/audio",
    "https://fmhy.net/video",
    "https://fmhy.net/privacy",
    "https://fmhy.net/file-tools",
    "https://fmhy.net/system-tools",
    "https://fmhy.net/internet-tools",
    "https://fmhy.net/text-tools",
    "https://fmhy.net/image-tools",
    "https://fmhy.net/developer-tools",
    "https://fmhy.net/linux-macos",
    "https://fmhy.net/other/selfhosting",
    "https://fmhy.net/other/backups",
]

GH = re.compile(r"https?://github\.com/([\w.-]+)/([\w.-]+)")


def traer(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "la-bandita-censo"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def texto(x: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", x))).strip()


def enlaces_de(pagina: str, cuerpo: str) -> list[dict]:
    """Saca los enlaces a GitHub con la sección (h2/h3) en la que aparecen."""
    partes = re.split(r"(<h[23][^>]*>.*?</h[23]>)", cuerpo, flags=re.S)
    seccion, filas = "(inicio)", []
    for p in partes:
        if re.match(r"<h[23]", p):
            seccion = texto(p)
            continue
        for u, etiqueta in re.findall(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', p, re.S):
            m = GH.match(u)
            if not m:
                continue
            dueno, repo = m.group(1), m.group(2).rstrip(".")
            if repo.endswith(".git"):
                repo = repo[:-4]
            filas.append({"pagina": pagina, "seccion": seccion, "dueno": dueno, "repo": repo,
                          "full": f"{dueno}/{repo}", "url": u, "texto": texto(etiqueta)[:90]})
    return filas


def del_registro() -> set[str]:
    conocidos: set[str] = set()
    for f in glob.glob(str(REGISTRO / "*.json")):
        if Path(f).name.startswith("_"):
            continue
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8"))
        except Exception:
            continue
        repo = d.get("repo") or (d.get("id") or "").replace("--", "/", 1)
        if repo:
            conocidos.add(repo.lower())
    return conocidos


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", action="append", default=[])
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()

    conocidos = del_registro()
    paginas = PAGINAS + a.url
    todas: dict[str, dict] = {}
    resumen = []
    for url in paginas:
        try:
            cuerpo = traer(url)
        except Exception as e:
            print(f"  ✗ {url}: {type(e).__name__}")
            resumen.append({"pagina": url, "estado": f"error {type(e).__name__}", "github": 0})
            continue
        filas = enlaces_de(url, cuerpo)
        for f in filas:
            clave = f["full"].lower()
            if clave in todas:
                todas[clave]["tambien_en"].append(url)
                continue
            f["tambien_en"] = []
            f["en_registro"] = clave in conocidos
            todas[clave] = f
        resumen.append({"pagina": url, "estado": "ok", "github": len(filas),
                        "nuevos": sum(1 for f in filas if f["full"].lower() not in conocidos)})
        print(f"  ✓ {url:45} github={len(filas):4} nuevos={resumen[-1]['nuevos']}")

    nuevos = [v for v in todas.values() if not v["en_registro"]]
    ya = [v for v in todas.values() if v["en_registro"]]
    salida = DOCS / (a.salida or f"CENSO-FMHY-{date.today().isoformat()}.json")
    salida.write_text(json.dumps({
        "medido_en": date.today().isoformat(),
        "fuente": "índices enlazados por fmhy.net",
        "paginas": resumen,
        "totales": {"repos_distintos": len(todas), "nuevos": len(nuevos), "ya_en_registro": len(ya)},
        "nuevos": sorted(nuevos, key=lambda v: v["full"].lower()),
        "ya_en_registro": sorted(ya, key=lambda v: v["full"].lower()),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nrepos distintos: {len(todas)} · nuevos para la casa: {len(nuevos)} · ya en registro: {len(ya)}")
    print(f"→ {salida.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
