#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mide los repositorios del cruce con EverythingMoe y clasifica el checksum de verdad.

Por qué existe: en el corte del 2026-11-27 se contó «checksum» cuando la API devolvía un
`digest`, y eso infló la cifra a 5 de 5 en los referentes. Aquí se separan **tres** cosas,
que no son lo mismo:

  * `checksum_publicado_archivo`: el proyecto adjunta un archivo (.sha256, Checksums, .sig).
  * `checksum_publicado_notas`:   la tabla SHA-256 vive en el cuerpo de la release.
  * `digest_api`:                 lo calcula GitHub al servir el asset. Sirve para comparar
                                 una descarga, pero no lo publica el proyecto y no sobrevive
                                 a que la release se edite.

Uso:
  LB_TOKEN=<token> python3 medir_cruce.py --entrada cruce.json --salida medidos.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://api.github.com"


def pide(url: str, tok: str) -> tuple[int, dict | list | None]:
    cab = {"Accept": "application/vnd.github+json", "User-Agent": "medir-cruce"}
    if tok:
        cab["Authorization"] = "Bearer " + tok
    req = urllib.request.Request(url, headers=cab)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:  # noqa: BLE001
        return 0, None


RE_TABLA = re.compile(r"\|\s*([A-Za-z0-9_.\- ]{2,40})\s*\|\s*([0-9a-fA-F]{64})\s*\|")


def mide(repo: str, tok: str) -> dict:
    f = {"repo": repo, "medido_en": time.strftime("%Y-%m-%d", time.gmtime())}
    code, d = pide(f"{API}/repos/{repo}", tok)
    f["http_repo"] = code
    if code != 200 or not isinstance(d, dict):
        f["estado"] = "indeterminado" if code in (403, 429, 0) else "no existe"
        return f
    f["nombre"] = d.get("full_name")
    f["web"] = d.get("html_url")
    f["estrellas"] = d.get("stargazers_count")
    f["forks"] = d.get("forks_count")
    f["abiertos"] = d.get("open_issues_count")
    f["lenguaje"] = d.get("language")
    f["licencia_api"] = (d.get("license") or {}).get("spdx_id")
    f["push"] = (d.get("pushed_at") or "")[:10]
    f["rama"] = d.get("default_branch")
    f["archivado"] = d.get("archived")
    f["creado"] = (d.get("created_at") or "")[:10]

    # licencia verificada leyendo el archivo, no solo la etiqueta de la API
    c, lic = pide(f"{API}/repos/{repo}/license", tok)
    f["licencia_archivo"] = (lic.get("license") or {}).get("spdx_id") if (c == 200 and isinstance(lic, dict)) else None
    f["licencia_archivo_ruta"] = lic.get("path") if (c == 200 and isinstance(lic, dict)) else None

    # última release
    c, rel = pide(f"{API}/repos/{repo}/releases/latest", tok)
    if c == 200 and isinstance(rel, dict):
        f["release"] = rel.get("tag_name")
        f["release_en"] = (rel.get("published_at") or "")[:10]
        assets = rel.get("assets") or []
        f["assets"] = len(assets)
        f["checksum_publicado_archivo"] = [
            a["name"] for a in assets
            if re.search(r"(sha256|checksums?|\.sig$|\.asc$|\.minisig$)", a["name"], re.I)]
        f["checksum_publicado_notas"] = bool(RE_TABLA.search(rel.get("body") or ""))
        f["digest_api"] = bool(assets and assets[0].get("digest"))
        f["digest_ejemplo"] = (assets[0].get("digest") or "")[:20] if assets else None
    else:
        f["release"] = None
        f["release_en"] = None
        f["assets"] = 0
        f["checksum_publicado_archivo"] = []
        f["checksum_publicado_notas"] = False
        f["digest_api"] = False

    f["checksum_publicado"] = bool(f["checksum_publicado_archivo"] or f["checksum_publicado_notas"])
    return f


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--salida", required=True)
    args = ap.parse_args()
    tok = os.environ.get("LB_TOKEN", "")

    datos = json.load(open(args.entrada, encoding="utf-8"))
    repos = sorted(datos.get("por_medir", {}))
    if not repos:
        print("no hay repositorios en por_medir", file=sys.stderr)
        return 1

    salida = []
    for i, r in enumerate(repos, 1):
        m = mide(r, tok)
        salida.append(m)
        marca = "OK " if m.get("http_repo") == 200 else "MAL"
        pub = "publica" if m.get("checksum_publicado") else ("solo-digest" if m.get("digest_api") else "nada")
        print(f"[{i:2}/{len(repos)}] {marca} {r:42} ★{m.get('estrellas')!s:>7} "
              f"lic={m.get('licencia_archivo') or m.get('licencia_api')} "
              f"rel={m.get('release')} checksum={pub}", flush=True)

    json.dump(salida, open(args.salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ok = sum(1 for x in salida if x.get("http_repo") == 200)
    pub = sum(1 for x in salida if x.get("checksum_publicado"))
    dig = sum(1 for x in salida if x.get("digest_api") and not x.get("checksum_publicado"))
    print(f"\nmedidos {ok}/{len(repos)} · checksum publicado {pub} · solo digest {dig} · "
          f"sin nada {ok - pub - dig}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
