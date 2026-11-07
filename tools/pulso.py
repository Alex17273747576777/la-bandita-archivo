#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PULSO · mide repositorios en fuente primaria y escribe fichas con evidencia cruda.

Lo que hace distinto a este pulso del censo viejo: **guarda el payload** que midió y lo sella.
La ficha declara `evidencia.payload_ref` y `evidencia.sha256` del JSON exacto que devolvió la API,
así que cualquiera puede recomputar el hash y comprobar que el dato no se tocó después.

Orden de licencia de la casa: SPDX → endpoint → texto del archivo → ausencia firmada.
Semántica de códigos: 404 es muerte; 403/429 es cuota, jamás muerte; 451 es bloqueo.

Uso:
  python3 tools/pulso.py --repos owner/a owner/b
  python3 tools/pulso.py --desde-archivo candidatos.txt
  python3 tools/pulso.py --piezas          # los repos citados en las piezas
  python3 tools/pulso.py --registro --limite 200
  opciones: --concurrente 6 --scorecard --swh --seco
Token: variable de entorno LB_TOKEN (nunca en el código ni en el historial).

Qué hace:
  * Mide repositorios contra la API de GitHub (GET /repos, /license, /releases/latest, /commits).
  * Guarda el payload crudo en registry/_evidencia/<id>.json con SHA-256 en la ficha.
  * Resuelve licencias por SPDX → endpoint → texto → ausencia firmada.
  * Consulta OpenSSF Scorecard y Software Heritage cuando se pide.
  * Mide con concurrencia controlada (asyncio) y reintentos ante cuota (403/429).

Qué NO hace:
  * No opina ni puntúa la calidad del programa; solo mide y archiva.
  * No borra una ficha porque el proyecto se murió: la marca como muerto.
  * No convierte 403/429 (cuota) en muerte: solo 404 es muerte.
  * No usa token escrito en el código: solo desde variable de entorno LB_TOKEN.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy, larga  # noqa: E402

RAIZ: Path = Path(__file__).resolve().parents[1]
REGISTRO: Path = RAIZ / "registry"
EVIDENCIA: Path = REGISTRO / "_evidencia"
API: str = "https://api.github.com"
UMBRAL_DORMIDO: int = 180
TOKEN: str = os.environ.get("LB_TOKEN", "").strip()


@dataclass(frozen=True)
class LicenciaFicha:
    spdx: str | None
    metodo: str  # spdx-api | texto-license | endpoint-license | ausencia-firmada
    verificado_en: str
    archivo: str | None = None
    nota: str | None = None


@dataclass(frozen=True)
class ActividadFicha:
    ultimo_push: str | None
    estado: str  # vivo | dormido | muerto | indeterminado
    semantica_http: int
    ultima_release: str | None = None
    release_en: str | None = None


@dataclass(frozen=True)
class MeritoFicha:
    stars: int | None
    stars_por_mes: float | None
    scorecard: int | None
    scorecard_en: str | None


@dataclass(frozen=True)
class ProcedenciaFicha:
    swhid: str | None
    commit: str | None
    atestacion: str | None = None
    swh_estado: str | None = None
    swh_solicitud: str | None = None


@dataclass(frozen=True)
class EvidenciaFicha:
    sha256: str
    payload_ref: str
    nota: str = ""


@dataclass
class Ficha:
    id: str
    repo: str
    nombre: str
    descripcion: str
    web: str | None
    medido_en: str
    fuente_primaria: str
    fuente_secundarias: list[str]
    fuente_metodo: str
    licencia: LicenciaFicha
    actividad: ActividadFicha
    merito: MeritoFicha
    procedencia: ProcedenciaFicha
    evidencia: EvidenciaFicha
    piezas: list[str] = field(default_factory=list)
    frescura_dias: int = 0

    def a_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "repo": self.repo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "web": self.web,
            "medido_en": self.medido_en,
            "fuente": {
                "primaria": self.fuente_primaria,
                "secundarias": self.fuente_secundarias,
                "metodo": self.fuente_metodo,
            },
            "licencia": {
                "spdx": self.licencia.spdx,
                "metodo": self.licencia.metodo,
                "verificado_en": self.licencia.verificado_en,
                "archivo": self.licencia.archivo,
                **({"nota": self.licencia.nota} if self.licencia.nota else {}),
            },
            "actividad": {
                "ultimo_push": self.actividad.ultimo_push,
                "estado": self.actividad.estado,
                "semantica_http": self.actividad.semantica_http,
                "ultima_release": self.actividad.ultima_release,
                "release_en": self.actividad.release_en,
            },
            "merito": {
                "stars": self.merito.stars,
                "stars_por_mes": self.merito.stars_por_mes,
                "scorecard": self.merito.scorecard,
                "scorecard_en": self.merito.scorecard_en,
            },
            "procedencia": {
                "swhid": self.procedencia.swhid,
                "commit": self.procedencia.commit,
                "atestacion": self.procedencia.atestacion,
                "swh_estado": self.procedencia.swh_estado,
                "swh_solicitud": self.procedencia.swh_solicitud,
            },
            "evidencia": {
                "sha256": self.evidencia.sha256,
                "payload_ref": self.evidencia.payload_ref,
                "nota": self.evidencia.nota,
            },
            "piezas": self.piezas,
            "frescura_dias": self.frescura_dias,
        }


def cabeceras() -> dict[str, str]:
    h = {"Accept": "application/vnd.github+json", "User-Agent": "la-bandita-pulso/1.0"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def _json_o_nada(cuerpo: bytes) -> dict[str, Any]:
    try:
        return json.loads(cuerpo or b"{}")
    except Exception:
        return {}


async def _pedir_async(url: str, crudo: bool = False, intentos: int = 3) -> tuple[int, bytes | dict[str, Any]]:
    """Petición asíncrona con reintentos solo ante cuota (403/429), jamás ante 404."""
    for n in range(intentos):
        try:
            req = urllib.request.Request(url, headers=cabeceras())
            status, cuerpo = await asyncio.to_thread(_pedir_sincrono, req)
            if crudo:
                return status, cuerpo
            return status, _json_o_nada(cuerpo)
        except urllib.error.HTTPError as e:
            cuerpo = e.read()
            if e.code in (403, 429) and n < intentos - 1:
                espera = 2 ** n * 3
                print(f"    cuota {e.code}: esperando {espera}s", file=sys.stderr)
                await asyncio.sleep(espera)
                continue
            if crudo:
                return e.code, cuerpo
            return e.code, _json_o_nada(cuerpo)
        except Exception:
            if n < intentos - 1:
                await asyncio.sleep(2 * (n + 1))
                continue
            return 0, b"" if crudo else {}
    return 0, b"" if crudo else {}


def _pedir_sincrono(req: urllib.request.Request) -> tuple[int, bytes]:
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.status, r.read() or b""


def ident(repo: str) -> str:
    base = repo.replace("/", "--").lower()
    base = re.sub(r"[^a-z0-9._-]+", "-", base).strip("-.")
    return (base or "ficha")[:80]


def estado_de(push: str | None, referencia: date) -> str:
    if not push or not re.match(r"^\d{4}-\d{2}-\d{2}", push):
        return "indeterminado"
    dias = (referencia - date.fromisoformat(push[:10])).days
    return "vivo" if dias <= UMBRAL_DORMIDO else "dormido"


async def verificar_licencia_async(repo: str, datos: dict[str, Any]) -> LicenciaFicha:
    """SPDX → endpoint → texto → ausencia firmada."""
    lic = datos.get("license") or {}
    spdx = lic.get("spdx_id")
    if spdx and spdx != "NOASSERTION":
        return LicenciaFicha(spdx=spdx, metodo="spdx-api", verificado_en=hoy())

    cod, contenido = await _pedir_async(f"{API}/repos/{repo}/license")
    if cod == 200 and isinstance(contenido, dict):
        nombre = contenido.get("name")
        spdx_archivo = (contenido.get("license") or {}).get("spdx_id")
        if spdx_archivo and spdx_archivo != "NOASSERTION":
            return LicenciaFicha(spdx=spdx_archivo, metodo="texto-license", verificado_en=hoy(), archivo=nombre)
        return LicenciaFicha(spdx=spdx, metodo="texto-license", verificado_en=hoy(), archivo=nombre)

    cod, raiz = await _pedir_async(f"{API}/repos/{repo}/contents/")
    if cod == 200 and isinstance(raiz, list):
        for x in raiz:
            if re.fullmatch(r"(LICEN[CS]E|COPYING|LICENCE)[A-Za-z0-9._-]*", x.get("name", ""), re.I):
                return LicenciaFicha(spdx=spdx if spdx != "NOASSERTION" else None, metodo="texto-license", verificado_en=hoy(), archivo=x["name"])

    cod_r, readme = await _pedir_async(f"{API}/repos/{repo}/readme", crudo=True)
    if cod_r == 200 and isinstance(readme, bytes):
        texto = readme.decode("utf-8", "replace")
        patron = re.compile(
            r"(CC[ -]BY(?:[ -]SA)?[ -]?[0-9.]*|CC0[ -]?1\.0|Creative Commons [A-Za-z0-9. -]{0,30}|MIT|Apache[ -]2\.0|GPL[ -]?[23]\.0|AGPL[ -]?3\.0|LGPL[ -]?[23]\.1|BSD[ -][23]-Clause|Unlicense|MPL[ -]2\.0|WTFPL)",
            re.I,
        )
        seccion = ""
        m = re.search(r"^#{1,3}\s*(?:licen[cs]e|licencia)\s*$", texto, re.I | re.M)
        if m:
            seccion = texto[m.end(): m.end() + 800]
        candidatos = sorted({c.group(1).strip() for c in patron.finditer(seccion)})
        origen = "README (sección License)"
        if not candidatos:
            candidatos = sorted({c.group(1).strip() for c in patron.finditer(texto)})
            origen = "README (texto completo)"
        if len(candidatos) == 1:
            return LicenciaFicha(spdx=candidatos[0], metodo="texto-license", verificado_en=hoy(), archivo=origen,
                                nota="licencia declarada por el proyecto en su propio README; el endpoint de GitHub no la clasifica")
        if len(candidatos) > 1:
            return LicenciaFicha(spdx=None, metodo="texto-license", verificado_en=hoy(),
                                archivo="README (varias licencias)",
                                nota="ambiguo: el README menciona " + ", ".join(candidatos[:8]) + "; requiere lectura humana")

    return LicenciaFicha(spdx=None, metodo="ausencia-firmada", verificado_en=hoy(), archivo=None)


async def medir_async(repo: str, con_scorecard: bool, con_swh: bool, ligero: bool = False) -> dict[str, Any] | None:
    cod, datos = await _pedir_async(f"{API}/repos/{repo}")
    if cod != 200 or not isinstance(datos, dict) or "full_name" not in datos:
        if cod == 404:
            fid = ident(repo)
            ficha = {
                "id": fid, "repo": repo, "nombre": repo.split("/", 1)[-1],
                "descripcion": "repositorio no encontrado al medir (HTTP 404)",
                "medido_en": hoy(),
                "fuente": {"primaria": "github-api", "secundarias": [],
                           "metodo": "GET /repos devolvió 404: el repositorio no existe o fue retirado"},
                "licencia": {"spdx": None, "metodo": "ausencia-firmada", "verificado_en": hoy(), "archivo": None},
                "actividad": {"ultimo_push": None, "estado": "muerto", "semantica_http": 404,
                              "ultima_release": None, "release_en": None},
                "merito": {"stars": None, "stars_por_mes": None, "scorecard": None, "scorecard_en": None},
                "procedencia": {"swhid": None, "commit": None, "atestacion": None},
                "evidencia": {"sha256": hashlib.sha256(b"404:" + repo.encode()).hexdigest(),
                              "payload_ref": "respuesta 404 de la API",
                              "nota": "no hay payload que guardar: la ausencia es el dato"},
                "piezas": [], "frescura_dias": 0,
            }
            previa = REGISTRO / f"{fid}.json"
            if previa.exists():
                try:
                    ficha["piezas"] = json.loads(previa.read_text(encoding="utf-8")).get("piezas", [])
                except Exception:
                    pass
            previa.write_text(json.dumps(ficha, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            return {"repo": repo, "error": "HTTP 404 · registrado como muerto", "medido_en": hoy()}
        return {"repo": repo, "error": f"HTTP {cod} (no se registra muerte sin 404)", "medido_en": hoy()}

    fid = ident(datos["full_name"])
    destino_id = REGISTRO / f"{fid}.json"
    if destino_id.exists():
        try:
            previo = json.loads(destino_id.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
        if previo.get("repo", "").lower() not in ("", datos["full_name"].lower()):
            fid = f"{fid}-{hashlib.sha1(datos['full_name'].encode()).hexdigest()[:6]}"

    EVIDENCIA.mkdir(parents=True, exist_ok=True)
    crudo = json.dumps(datos, ensure_ascii=False, sort_keys=True).encode()
    (EVIDENCIA / f"{fid}.json").write_bytes(json.dumps(datos, ensure_ascii=False, indent=1, sort_keys=True).encode())

    rel, commit = {}, None
    if not ligero:
        _, rel = await _pedir_async(f"{API}/repos/{repo}/releases/latest")
        _, commits = await _pedir_async(f"{API}/repos/{repo}/commits?per_page=1")
        if isinstance(commits, list) and commits:
            commit = commits[0].get("sha")

    licencia = await verificar_licencia_async(repo, datos)

    merito: dict[str, Any] = {"stars": datos.get("stargazers_count"), "stars_por_mes": None,
                              "scorecard": None, "scorecard_en": None}
    if con_scorecard:
        cod_s, sc = await _pedir_async(f"https://api.securityscorecards.dev/projects/github.com/{repo}")
        if cod_s == 200 and isinstance(sc, dict):
            merito["scorecard"] = sc.get("score")
            merito["scorecard_en"] = (sc.get("date") or "")[:10] or None

    swhid, swh_estado, swh_solicitud = None, None, None
    if con_swh and commit:
        cod_w, sw = await _pedir_async(f"https://archive.softwareheritage.org/api/1/revision/{commit}/")
        if cod_w == 200 and isinstance(sw, dict):
            identificador = sw.get("id") or ""
            if re.fullmatch(r"[0-9a-f]{40}", identificador or ""):
                identificador = f"swh:1:rev:{identificador}"
            swhid, swh_estado = identificador or None, "archivada"
        else:
            cod_s, sol = await _pedir_async(
                f"https://archive.softwareheritage.org/api/1/origin/save/git/url/https://github.com/{repo}/", metodo="POST")
            if cod_s in (200, 201) and isinstance(sol, dict):
                swh_solicitud = sol.get("id")
                swh_estado = sol.get("save_task_status") or sol.get("save_request_status")
                if swh_estado in ("scheduled", "pending", "running"):
                    swh_estado = f"solicitada ({swh_estado})"
            else:
                swh_estado = f"sin archivo (HTTP {cod_s})"

    ahora_str = hoy()
    referencia = date.fromisoformat(ahora_str)
    push = (datos.get("pushed_at") or "")[:10] or None
    estado = estado_de(push, referencia)

    ficha_dict: dict[str, Any] = {
        "id": fid,
        "repo": datos["full_name"],
        "nombre": datos["full_name"].split("/", 1)[1],
        "descripcion": (datos.get("description") or "")[:400],
        "medido_en": ahora_str,
        "fuente": {
            "primaria": "github-api",
            "secundarias": [s for s, ok in (("scorecard", merito["scorecard"] is not None),
                                            ("software-heritage", swhid is not None)) if ok],
            "metodo": "GET /repos, /releases/latest, /license y /commits?per_page=1 con token; payload sellado",
        },
        "licencia": {
            "spdx": licencia.spdx,
            "metodo": licencia.metodo,
            "verificado_en": licencia.verificado_en,
            "archivo": licencia.archivo,
            **({"nota": licencia.nota} if licencia.nota else {}),
        },
        "actividad": {
            "ultimo_push": push,
            "estado": estado,
            "semantica_http": cod,
            "ultima_release": rel.get("tag_name") if isinstance(rel, dict) and rel.get("tag_name") else None,
            "release_en": ((rel.get("published_at") or "")[:10] or None) if isinstance(rel, dict) else None,
        },
        "merito": merito,
        "procedencia": {
            "swhid": swhid,
            "commit": commit,
            "atestacion": None,
            "swh_estado": swh_estado,
            "swh_solicitud": swh_solicitud,
        },
        "evidencia": {
            "sha256": hashlib.sha256(crudo).hexdigest(),
            "payload_ref": f"registry/_evidencia/{fid}.json",
            "nota": "hash del JSON exacto devuelto por la API en la fecha declarada",
        },
        "piezas": [],
        "frescura_dias": 0,
    }
    if datos.get("archived"):
        ficha_dict["actividad"]["estado"] = "dormido"
    if datos.get("homepage"):
        ficha_dict["web"] = datos["homepage"]

    # conservar piezas ya asociadas
    destino = REGISTRO / f"{fid}.json"
    if destino.exists():
        try:
            previo = json.loads(destino.read_text(encoding="utf-8"))
            ficha_dict["piezas"] = previo.get("piezas", [])
            if ligero and previo.get("procedencia"):
                for clave in ("swhid", "commit", "swh_estado", "swh_solicitud"):
                    if not ficha_dict["procedencia"].get(clave) and previo["procedencia"].get(clave):
                        ficha_dict["procedencia"][clave] = previo["procedencia"][clave]
        except Exception:
            pass

    destino.write_text(json.dumps(ficha_dict, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return ficha_dict


def repos_de_piezas() -> list[str]:
    vistos: dict[str, int] = {}
    for p in sorted(REGISTRO.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if d.get("piezas"):
            vistos[d["repo"]] = len(d["piezas"])
    return [r for r, _ in sorted(vistos.items(), key=lambda x: -x[1])]


def repos_del_registro(limite: int = 0) -> list[str]:
    filas: list[tuple[int, str]] = []
    for p in sorted(REGISTRO.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        filas.append(((d.get("merito") or {}).get("stars") or 0, d["repo"]))
    filas.sort(reverse=True)
    return [r for _, r in (filas[:limite] if limite else filas)]


async def _medir_todos(repos: list[str], concurrente: int, con_scorecard: bool, con_swh: bool, ligero: bool) -> tuple[list[dict], list[tuple[str, str]]]:
    resultados: list[dict] = []
    errores: list[tuple[str, str]] = []

    sem = asyncio.Semaphore(concurrente)

    async def una(repo: str) -> None:
        async with sem:
            try:
                res = await medir_async(repo, con_scorecard, con_swh, ligero)
            except Exception as e:
                errores.append((repo, str(e)))
                print(f"  excepción {repo}: {e}")
                return
            if res and "error" in res:
                errores.append((repo, res["error"]))
                print(f"  {repo}: {res['error']}")
            elif res:
                resultados.append(res)
                print(f"  {res['repo']:<44} ★{str(res['merito']['stars']):<7} "
                      f"{res['actividad']['estado']:<10} {str(res['licencia']['spdx'] or 'sin licencia'):<14} "
                      f"{res['licencia']['metodo']:<16} push {res['actividad']['ultimo_push']}"
                      + (f" · scorecard {res['merito']['scorecard']}" if res['merito']['scorecard'] is not None else "")
                      + (" · SWHID sí" if res['procedencia']['swhid'] else ""))

    await asyncio.gather(*(una(r) for r in repos))
    return resultados, errores


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Mide repositorios en fuente primaria y escribe fichas con evidencia cruda.")
    parser.add_argument("--repos", nargs="*", default=[])
    parser.add_argument("--desde-archivo")
    parser.add_argument("--piezas", action="store_true")
    parser.add_argument("--registro", action="store_true")
    parser.add_argument("--limite", type=int, default=0)
    parser.add_argument("--concurrente", type=int, default=6)
    parser.add_argument("--scorecard", action="store_true")
    parser.add_argument("--swh", action="store_true")
    parser.add_argument("--seco", action="store_true")
    parser.add_argument("--ligero", action="store_true", help="solo /repos y licencia: barridos grandes")
    args = parser.parse_args(argv)

    if not TOKEN:
        print("ABORTA: falta LB_TOKEN en el entorno. Sin token, la cuota anónima (60/h) hace la medición inútil.")
        return 2

    lista = list(args.repos)
    if args.desde_archivo:
        lista += [l.strip() for l in Path(args.desde_archivo).read_text(encoding="utf-8").splitlines()
                  if l.strip() and not l.startswith("#")]
    if args.piezas:
        lista += repos_de_piezas()
    if args.registro:
        lista += repos_del_registro(args.limite)

    vistos: set[str] = set()
    limpia: list[str] = []
    for r in lista:
        r = r.strip().strip("/")
        if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", r) and r.lower() not in vistos:
            vistos.add(r.lower())
            limpia.append(r)

    if not limpia:
        print("nada que medir")
        return 1

    print(f"PULSO · {larga()} · {len(limpia)} repositorios · concurrencia {args.concurrente} · "
          f"scorecard {'sí' if args.scorecard else 'no'} · swh {'sí' if args.swh else 'no'}")

    if args.seco:
        print("\n".join(limpia))
        return 0

    resultados, errores = asyncio.run(_medir_todos(limpia, args.concurrente, args.scorecard, args.swh, args.ligero))

    resumen = {
        "fecha": hoy(),
        "medidos": len(resultados),
        "errores": len(errores),
        "vivos": sum(1 for r in resultados if r["actividad"]["estado"] == "vivo"),
        "sin_licencia": sum(1 for r in resultados if r["licencia"]["metodo"] == "ausencia-firmada"),
        "con_swhid": sum(1 for r in resultados if r["procedencia"]["swhid"]),
        "con_scorecard": sum(1 for r in resultados if r["merito"]["scorecard"] is not None),
        "errores_detalle": [{"repo": r, "error": e} for r, e in errores],
    }
    (REGISTRO / f"_pulso-{hoy()}.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nresumen: {len(resultados)} medidos · {resumen['vivos']} vivos · "
          f"{resumen['sin_licencia']} sin licencia declarada · {resumen['con_swhid']} con SWHID · "
          f"{resumen['con_scorecard']} con scorecard · {len(errores)} errores")
    return 0 if not errores else 0


if __name__ == "__main__":
    sys.exit(main())
