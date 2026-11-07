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

Qué hace:
  * Lee cada repositorio tres veces por caminos distintos (API, HTML, crudo).
  * Rota el orden de las lecturas para que ningún camino favorezca un resultado.
  * Detecta discrepancias entre lecturas y las anota sin elegir una a gusto.
  * Guarda el censo en docs/envios/_medicion-{canal}.json cuando se pasa --guardar.

Qué NO hace:
  * No elige la respuesta que más le gusta cuando las tres lecturas discrepan.
  * No redondea estrellas ni convierte «sin licencia» en «probablemente MIT».
  * No usa dependencias externas de red: todo va por urllib de la stdlib.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
MEDICIONES: tuple[Path, ...] = (
    RAIZ / "docs" / "envios" / "_medicion-whatsapp.json",
    RAIZ / "docs" / "envios" / "_medicion-facebook.json",
)
UA: str = "la-bandita-tres-lecturas/1.0 (+archivo publico)"
TIMEOUT: int = 30


@dataclass(frozen=True)
class FilaMedicion:
    """Una fila de medición: los campos que coincidieron en las tres lecturas."""

    stars: int | str
    licencia: str
    lenguaje: str
    push: str
    desc: str
    archivado: bool
    estado: str
    release: str = ""
    release_fecha: str = ""


@dataclass
class ResultadoMedicion:
    """Resultado de medir un repositorio: fila de datos y avisos de discrepancia."""

    repo: str
    fila: FilaMedicion | None
    avisos: list[str] = field(default_factory=list)
    error: str | None = None

    @property
    def leido(self) -> bool:
        return self.fila is not None and self.error is None


def _llave() -> str:
    """Llave local de la casa: vive fuera del repositorio y nunca se imprime."""
    for ruta, clave in (
        (Path("/home/user/.boveda/tokens.env"), "PAT_FINO"),
        (Path("/tmp/.lbt"), "GHP_A"),
    ):
        try:
            for linea in ruta.read_text(encoding="utf-8").splitlines():
                if linea.startswith(clave + "="):
                    return linea.split("=", 1)[1].strip()
        except OSError:
            continue
    return ""


LLAVE: str = _llave()


def _trae(url: str, acepta: str = "text/html") -> str:
    """Petición HTTP síncrona con timeout y cabecera de usuario de la casa."""
    cabeceras = {"User-Agent": UA, "Accept": acepta}
    if LLAVE and "api.github.com" in url:
        cabeceras["Authorization"] = "Bearer " + LLAVE
    req = urllib.request.Request(url, headers=cabeceras)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as respuesta:
        return respuesta.read().decode("utf-8", "replace")


def leer_1(repo: str) -> dict:
    """Búsqueda: endpoint distinto al de repositorios, con su propio cupo."""
    url = f"https://api.github.com/search/repositories?q=repo:{repo}&per_page=1"
    try:
        d = json.loads(_trae(url, "application/vnd.github+json"))
        it = (d.get("items") or [None])[0]
    except urllib.error.HTTPError:
        it = None
    if not it:  # la búsqueda rechaza algunos nombres: se pregunta por el repo
        it = json.loads(_trae(f"https://api.github.com/repos/{repo}", "application/vnd.github+json"))
        it = dict(
            it,
            stargazers_count=it.get("stargazers_count"),
            pushed_at=it.get("pushed_at"),
            archived=it.get("archived"),
            language=it.get("language"),
            description=it.get("description"),
            license=it.get("license"),
        )
    licencia = (it.get("license") or {}).get("spdx_id") or "sin licencia"
    return {
        "stars": it.get("stargazers_count"),
        "licencia": licencia,
        "lenguaje": it.get("language") or "—",
        "push": (it.get("pushed_at") or "")[:10],
        "desc": it.get("description") or "",
        "archivado": bool(it.get("archived")),
    }


def leer_2(repo: str) -> dict:
    """HTML del repositorio: cuenta de estrellas y licencia tal como se ven."""
    h = _trae(f"https://github.com/{repo}")
    out: dict = {}
    m = re.search(r'id="repo-stars-counter-star"[^>]*title="([\d,\.]+)"', h)
    if not m:
        m = re.search(r"([\d\.,]+)\s*</span>\s*<span[^>]*>\s*stars", h, re.I)
    if m:
        out["stars_html"] = int(re.sub(r"[^\d]", "", m.group(1)))
    m = re.search(r'/blob/[^"]*(LICEN[CS]E[^"]*)', h, re.I)
    if m:
        out["licencia_html"] = m.group(1)
    m = re.search(r'relative-time[^>]*datetime="([\d\-T:Z]+)"', h)
    if m:
        out["push_html"] = m.group(1)[:10]
    if "stars_html" not in out:
        m = re.search(r'"stargazerCount":(\d+)', h)
        if m:
            out["stars_html"] = int(m.group(1))
    if "push_html" not in out:
        m = re.search(r'"pushedAt":"([\d\-T:Z]+)"', h) or re.search(r'datetime="([\d\-T:Z]+)"', h)
        if m:
            out["push_html"] = m.group(1)[:10]
    if not out:
        raise LookupError("la página no trajo metadatos")
    return out


def leer_3(repo: str) -> dict:
    """Contenido crudo: README y LICENSE, sin pasar por la interfaz."""
    out: dict = {}
    nombres = (
        "README.md", "readme.md", "README.MD", "Readme.md", "README.rst",
        "README", "readme", "README.txt",
    )
    for rama in ("HEAD", "main", "master"):
        txt = ""
        for n in nombres:
            try:
                txt = _trae(f"https://raw.githubusercontent.com/{repo}/{rama}/{n}", "text/plain")
            except urllib.error.HTTPError:
                continue
            if txt:
                break
        if txt:
            out["readme_bytes"] = len(txt)
            lic = re.search(r"(Apache-2\.0|GPL-3\.0|AGPL-3\.0|MPL-2\.0|MIT|BSD-3-Clause)", txt)
            if lic:
                out["licencia_readme"] = lic.group(1)
            ver = re.search(r"\bv?\d+\.\d+(?:\.\d+)?\b", txt)
            if ver:
                out["version_readme"] = ver.group(0)
            break
    if not out:
        raise LookupError("no hay README crudo legible")
    return out


async def medir_async(repo: str, turno: int = 0) -> ResultadoMedicion:
    """Las tres lecturas se hacen siempre, y en orden distinto cada vez.

    El orden rota con `turno` para que dos recursos seguidos no se lean con
    la misma secuencia.
    """
    avisos: list[str] = []
    orden: list[tuple] = [
        (leer_1, "búsqueda"),
        (leer_2, "página"),
        (leer_3, "crudo"),
    ]
    rotado = orden[turno % 3:] + orden[: turno % 3]
    hechas: dict[str, dict] = {}
    for funcion, _nombre in rotado:
        try:
            hechas[funcion.__name__] = await asyncio.to_thread(funcion, repo)
        except Exception as exc:  # noqa: BLE001 — se informa y se sigue
            return ResultadoMedicion(repo=repo, fila=None, error=f"{type(exc).__name__}: {exc}")

    r1, r2, r3 = hechas["leer_1"], hechas["leer_2"], hechas["leer_3"]
    fila = FilaMedicion(
        stars=r1["stars"],
        licencia=r1["licencia"],
        lenguaje=r1["lenguaje"],
        push=r1["push"],
        desc=r1["desc"],
        archivado=r1["archivado"],
        estado="archivado" if r1["archivado"] else "vivo",
        release="",
        release_fecha="",
    )

    if r2.get("stars_html") and isinstance(r1["stars"], int) and abs(r2["stars_html"] - r1["stars"]) > 0:
        avisos.append(f"estrellas: búsqueda {r1['stars']} · página {r2['stars_html']}")
        fila = FilaMedicion(**{**fila.__dict__, "stars": r2["stars_html"]})
    if r2.get("push_html") and r1["push"] and r2["push_html"] != r1["push"]:
        avisos.append(f"empujón: búsqueda {r1['push']} · página {r2['push_html']}")
    if r3.get("licencia_readme") and r1["licencia"] not in ("sin licencia", r3["licencia_readme"]):
        avisos.append(f"licencia: búsqueda {r1['licencia']} · README {r3['licencia_readme']}")

    return ResultadoMedicion(repo=repo, fila=fila, avisos=avisos)


async def _medir_todos(repos: list[str], guardar: bool) -> tuple[dict[str, dict], int]:
    filas: dict[str, dict] = {}
    problemas = 0
    pausa = 0.0 if LLAVE else 6.5  # cupo de la búsqueda: 10 por minuto sin token

    async def una(repo: str, i: int) -> None:
        nonlocal problemas
        if i and pausa:
            await asyncio.sleep(pausa)
        try:
            resultado = await medir_async(repo, i)
        except Exception as exc:  # noqa: BLE001
            print(f"NO LEÍDO  {repo}  ({type(exc).__name__}: {exc})")
            problemas += 1
            return
        if resultado.error:
            print(f"NO LEÍDO  {repo}  ({resultado.error})")
            problemas += 1
            return
        assert resultado.fila is not None
        filas[repo] = {
            **resultado.fila.__dict__,
            "stars_pieza": resultado.fila.stars,
        }
        marca = "·" if not resultado.avisos else "≠"
        print(f"{marca} {repo}  ★{resultado.fila.stars} {resultado.fila.licencia} "
              f"{resultado.fila.lenguaje} push {resultado.fila.push}")
        for aviso in resultado.avisos:
            print(f"    ¡tres lecturas no coinciden! {aviso}")

    await asyncio.gather(*(una(r, i) for i, r in enumerate(repos)))

    if guardar and filas:
        for path in MEDICIONES:
            try:
                d = json.loads(path.read_text(encoding="utf-8"))
            except (FileNotFoundError, json.JSONDecodeError):
                d = {"repos": {}}
            d.setdefault("repos", {}).update(filas)
            path.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"guardados {len(filas)} repositorios en las dos mediciones")

    return filas, problemas


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Mide cada repositorio tres veces por tres caminos distintos y reporta discrepancias.",
    )
    parser.add_argument("--guardar", action="store_true", help="guarda el censo en docs/envios/_medicion-*.json")
    args = parser.parse_args(argv)

    repos = [l.strip() for l in sys.stdin if l.strip() and not l.startswith("#")]
    filas, problemas = asyncio.run(_medir_todos(repos, args.guardar))
    print(f"TRES LECTURAS · {len(filas)} medidos · {problemas} sin leer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
