#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DESCUBRIR · extrae repositorios de una fuente y los cruza contra el registro.

Una lista curada ajena sirve para descubrir, no para creer: aquí solo se extraen nombres de
repositorio y se marcan los que el registro de la casa todavía no tiene. El juicio —estrellas,
licencia, actividad, si sirve— lo pone el pulso, midiendo en fuente primaria.

Uso:
  python3 tools/descubrir.py --fuente README.md [--fuente otra.md] [--etiqueta nombre]
Salida: docs/candidatos-<fecha>.tsv y un resumen por pantalla.
"""
from __future__ import annotations
import argparse, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
DOCS = RAIZ / "docs"
URL_REPO = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
RUIDO = {"topics", "login", "apps", "features", "about", "pricing", "sponsors", "marketplace",
         "security", "enterprise", "collections", "trending", "explore", "settings", "orgs"}
EXT = (".git", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".apk", ".zip", ".md")


def limpia_repo(owner: str, name: str) -> str | None:
    name = re.split(r"[#?]", name)[0].rstrip("/")
    if name.lower().endswith(EXT):
        name = re.sub(r"\.(git|png|jpe?g|svg|gif|apk|zip|md)$", "", name, flags=re.I)
    if owner.lower() in RUIDO or not name or name.lower() in RUIDO:
        return None
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", owner) or not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
        return None
    return f"{owner}/{name}"


def en_registro() -> set[str]:
    conocidos = set()
    for p in REGISTRO.glob("*.json"):
        if p.name.startswith("_"):
            continue
        try:
            conocidos.add(json.loads(p.read_text(encoding="utf-8"))["repo"].lower())
        except Exception:
            continue
    return conocidos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuente", action="append", required=True)
    ap.add_argument("--etiqueta", default="fuente")
    args = ap.parse_args()
    conocidos = en_registro()
    hallado: dict[str, dict] = {}
    for ruta in args.fuente:
        texto = Path(ruta).read_text(encoding="utf-8", errors="replace")
        categoria = "(sin categoría)"
        for linea in texto.split("\n"):
            m_cat = re.match(r"^#{2,3}\s+(.*)$", linea)
            if m_cat:
                categoria = m_cat.group(1).strip("# ").strip()[:60]
            for m in URL_REPO.finditer(linea):
                repo = limpia_repo(m.group(1), m.group(2))
                if not repo:
                    continue
                d = hallado.setdefault(repo.lower(), {"repo": repo, "categorias": Counter(), "menciones": 0})
                d["menciones"] += 1
                if categoria:
                    d["categorias"][categoria] += 1
    filas = []
    for clave, d in hallado.items():
        filas.append({
            "repo": d["repo"],
            "categoria": d["categorias"].most_common(1)[0][0] if d["categorias"] else "(sin categoría)",
            "menciones": d["menciones"],
            "en_registro": "sí" if clave in conocidos else "no",
        })
    filas.sort(key=lambda f: (f["en_registro"] == "sí", -f["menciones"], f["repo"].lower()))
    nuevos = [f for f in filas if f["en_registro"] == "no"]
    DOCS.mkdir(exist_ok=True)
    destino = DOCS / f"candidatos-{hoy()}.tsv"
    with destino.open("w", encoding="utf-8") as fh:
        fh.write("repo\tcategoria\tmenciones\ten_registro\n")
        for f in filas:
            fh.write(f"{f['repo']}\t{f['categoria']}\t{f['menciones']}\t{f['en_registro']}\n")
    por_cat = Counter(f["categoria"] for f in nuevos)
    print(f"DESCUBRIR · {args.etiqueta} · {hoy()}")
    print(f"repositorios distintos citados: {len(filas)} · ya en el registro: {len(filas) - len(nuevos)} · nuevos: {len(nuevos)}")
    print("nuevos por categoría (los 12 primeros):")
    for cat, n in por_cat.most_common(12):
        print(f"  · {cat}: {n}")
    print(f"listado: {destino.relative_to(RAIZ)}")
    (DOCS / f"candidatos-{hoy()}-nuevos.txt").write_text("\n".join(f["repo"] for f in nuevos) + "\n", encoding="utf-8")
    print(f"lista para el pulso: docs/candidatos-{hoy()}-nuevos.txt ({len(nuevos)} repositorios)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
