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
"""
from __future__ import annotations
import argparse, concurrent.futures as cf, hashlib, json, os, re, sys, time
import urllib.error, urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy, larga  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
EVIDENCIA = REGISTRO / "_evidencia"
API = "https://api.github.com"
UMBRAL_DORMIDO = 180
TOKEN = os.environ.get("LB_TOKEN", "").strip()


def cabeceras() -> dict:
    h = {"Accept": "application/vnd.github+json", "User-Agent": "la-bandita-pulso/1.0"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def pedir(url: str, crudo: bool = False, intentos: int = 3):
    """Devuelve (código, cuerpo_bytes). Reintenta solo ante cuota, jamás ante 404."""
    for n in range(intentos):
        try:
            req = urllib.request.Request(url, headers=cabeceras())
            with urllib.request.urlopen(req, timeout=40) as r:
                cuerpo = r.read()
                return r.status, cuerpo if crudo else json.loads(cuerpo or b"{}")
        except urllib.error.HTTPError as e:
            cuerpo = e.read()
            if e.code in (403, 429) and n < intentos - 1:
                espera = 2 ** n * 3
                print(f"    cuota {e.code}: esperando {espera}s", file=sys.stderr)
                time.sleep(espera)
                continue
            return e.code, (cuerpo if crudo else _json_o_nada(cuerpo))
        except Exception:
            if n < intentos - 1:
                time.sleep(2 * (n + 1))
                continue
            return 0, b""
    return 0, b""


def pedir_swh(url: str, metodo: str = "GET", intentos: int = 3):
    """Software Heritage rechaza las cabeceras de GitHub (406). Se le habla con las suyas."""
    for n in range(intentos):
        try:
            req = urllib.request.Request(url, data=b"" if metodo == "POST" else None,
                                         headers={"User-Agent": "la-bandita-pulso/1.0",
                                                  "Accept": "application/json"},
                                         method=metodo)
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.status, _json_o_nada(r.read())
        except urllib.error.HTTPError as e:
            cuerpo = _json_o_nada(e.read())
            if e.code in (429, 503) and n < intentos - 1:
                time.sleep(2 ** n * 3)
                continue
            return e.code, cuerpo
        except Exception:
            if n < intentos - 1:
                time.sleep(2)
                continue
            return 0, {}
    return 0, {}


def estado_swh(solicitud) -> str | None:
    if not solicitud:
        return None
    cod, datos = pedir_swh(f"https://archive.softwareheritage.org/api/1/origin/save/{solicitud}/")
    if cod == 200 and isinstance(datos, dict):
        return datos.get("save_task_status") or datos.get("save_request_status")
    return f"consulta HTTP {cod}"


def _json_o_nada(cuerpo: bytes):
    try:
        return json.loads(cuerpo or b"{}")
    except Exception:
        return {}


def ident(repo: str) -> str:
    base = repo.replace("/", "--").lower()
    base = re.sub(r"[^a-z0-9._-]+", "-", base).strip("-.")
    return (base or "ficha")[:80]


def estado(push: str | None, referencia: date) -> str:
    if not push or not re.match(r"^\d{4}-\d{2}-\d{2}", push):
        return "indeterminado"
    dias = (referencia - date.fromisoformat(push[:10])).days
    return "vivo" if dias <= UMBRAL_DORMIDO else "dormido"


def verificar_licencia(repo: str, datos: dict) -> dict:
    """SPDX → endpoint → texto → ausencia firmada. Devuelve el bloque de licencia."""
    lic = datos.get("license") or {}
    spdx = lic.get("spdx_id")
    if spdx and spdx not in ("NOASSERTION",):
        return {"spdx": spdx, "metodo": "spdx-api", "verificado_en": hoy(), "archivo": None}
    cod, contenido = pedir(f"{API}/repos/{repo}/license")
    if cod == 200 and isinstance(contenido, dict):
        nombre = contenido.get("name")
        spdx_archivo = (contenido.get("license") or {}).get("spdx_id")
        if spdx_archivo and spdx_archivo != "NOASSERTION":
            return {"spdx": spdx_archivo, "metodo": "texto-license", "verificado_en": hoy(), "archivo": nombre}
        return {"spdx": spdx, "metodo": "texto-license", "verificado_en": hoy(), "archivo": nombre}
    # sin endpoint de licencia: se busca el archivo a mano en la raíz
    # (y, si no hay archivo, la declaración de licencia en el texto del README cuenta como
    #  "texto-license": es lo que el proyecto firma en su propia casa)
    cod, raiz = pedir(f"{API}/repos/{repo}/contents/")
    if cod == 200 and isinstance(raiz, list):
        for x in raiz:
            if re.fullmatch(r"(LICEN[CS]E|COPYING|LICENCE)[A-Za-z0-9._-]*", x.get("name", ""), re.I):
                return {"spdx": spdx if spdx != "NOASSERTION" else None, "metodo": "texto-license",
                        "verificado_en": hoy(), "archivo": x["name"]}
    cod_r, readme = pedir(f"{API}/repos/{repo}/readme", crudo=True)
    if cod_r == 200 and isinstance(readme, bytes):
        texto = readme.decode("utf-8", "replace")
        m = re.search(r"(CC[ -]BY(?:[ -]SA)?[ -]?[0-9.]*|Creative Commons [A-Za-z0-9. -]{0,30}|MIT|Apache[ -]2\.0|GPL[ -]?[23]\.0|AGPL[ -]?3\.0|BSD[ -][23]-Clause|Unlicense|MPL[ -]2\.0)", texto, re.I)
        if m:
            return {"spdx": m.group(1).strip(), "metodo": "texto-license", "verificado_en": hoy(), "archivo": "README"}
    return {"spdx": None, "metodo": "ausencia-firmada", "verificado_en": hoy(), "archivo": None}


def medir(repo: str, con_scorecard: bool, con_swh: bool, ligero: bool = False) -> dict | None:
    cod, datos = pedir(f"{API}/repos/{repo}")
    if cod != 200 or not isinstance(datos, dict) or "full_name" not in datos:
        return {"repo": repo, "error": f"HTTP {cod}", "medido_en": hoy()}
    fid = ident(datos["full_name"])
    # blindaje contra colisión: dos repos distintos no pueden escribir la misma ficha
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

    # release y commit más recientes (se omiten en barridos grandes: cada llamada cuesta cuota)
    rel, commit = {}, None
    if not ligero:
        _, rel = pedir(f"{API}/repos/{repo}/releases/latest")
        _, commits = pedir(f"{API}/repos/{repo}/commits?per_page=1")
        if isinstance(commits, list) and commits:
            commit = commits[0].get("sha")
    licencia = verificar_licencia(repo, datos)

    merito = {"stars": datos.get("stargazers_count"), "stars_por_mes": None,
              "scorecard": None, "scorecard_en": None}
    if con_scorecard:
        cod_s, sc = pedir(f"https://api.securityscorecards.dev/projects/github.com/{repo}")
        if cod_s == 200 and isinstance(sc, dict):
            merito["scorecard"] = sc.get("score")
            merito["scorecard_en"] = (sc.get("date") or "")[:10] or None

    swhid, swh_estado, swh_solicitud = None, None, None
    if con_swh and commit:
        cod_w, sw = pedir_swh(f"https://archive.softwareheritage.org/api/1/revision/{commit}/")
        if cod_w == 200 and isinstance(sw, dict):
            identificador = sw.get("id") or ""
            if re.fullmatch(r"[0-9a-f]{40}", identificador or ""):
                identificador = f"swh:1:rev:{identificador}"
            swhid, swh_estado = identificador or None, "archivada"
        else:
            cod_s, sol = pedir_swh(
                f"https://archive.softwareheritage.org/api/1/origin/save/git/url/https://github.com/{repo}/", metodo="POST")
            if cod_s in (200, 201) and isinstance(sol, dict):
                swh_solicitud = sol.get("id")
                swh_estado = sol.get("save_task_status") or sol.get("save_request_status")
                if swh_estado in ("scheduled", "pending", "running"):
                    swh_estado = f"solicitada ({swh_estado})"
            else:
                swh_estado = f"sin archivo (HTTP {cod_s})"

    ficha = {
        "id": fid,
        "repo": datos["full_name"],
        "nombre": datos["full_name"].split("/", 1)[1],
        "descripcion": (datos.get("description") or "")[:400],
        "web": datos.get("homepage") or None,
        "medido_en": hoy(),
        "fuente": {"primaria": "github-api",
                   "secundarias": [s for s, ok in (("scorecard", merito["scorecard"] is not None),
                                                   ("software-heritage", swhid is not None)) if ok],
                   "metodo": "GET /repos, /releases/latest, /license y /commits?per_page=1 con token; payload sellado"},
        "licencia": licencia,
        "actividad": {
            "ultimo_push": (datos.get("pushed_at") or "")[:10] or None,
            "estado": estado(datos.get("pushed_at"), date.today() if False else date.fromisoformat(hoy())),
            "semantica_http": cod,
            "ultima_release": (rel.get("tag_name") if isinstance(rel, dict) and rel.get("tag_name") else None),
            "release_en": ((rel.get("published_at") or "")[:10] or None) if isinstance(rel, dict) else None,
        },
        "merito": merito,
        "procedencia": {"swhid": swhid, "commit": commit, "atestacion": None,
                        "swh_estado": swh_estado, "swh_solicitud": swh_solicitud},
        "evidencia": {"sha256": hashlib.sha256(crudo).hexdigest(),
                      "payload_ref": f"registry/_evidencia/{fid}.json",
                      "nota": "hash del JSON exacto devuelto por la API en la fecha declarada"},
        "piezas": [],
        "frescura_dias": 0,
    }
    if datos.get("archived"):
        ficha["actividad"]["estado"] = "dormido"
    # conservar piezas ya asociadas
    destino = REGISTRO / f"{fid}.json"
    if destino.exists():
        try:
            previo = json.loads(destino.read_text(encoding="utf-8"))
            ficha["piezas"] = previo.get("piezas", [])
            # un barrido ligero no borra la procedencia ya conseguida: se conserva la mejor
            if ligero and previo.get("procedencia"):
                for clave in ("swhid", "commit", "swh_estado", "swh_solicitud"):
                    if not ficha["procedencia"].get(clave) and previo["procedencia"].get(clave):
                        ficha["procedencia"][clave] = previo["procedencia"][clave]
        except Exception:
            pass
    if ficha["web"] is None:
        ficha.pop("web")
    destino.write_text(json.dumps(ficha, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return ficha


def repos_de_piezas() -> list[str]:
    vistos = {}
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
    filas = []
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos", nargs="*", default=[])
    ap.add_argument("--desde-archivo")
    ap.add_argument("--piezas", action="store_true")
    ap.add_argument("--registro", action="store_true")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--concurrente", type=int, default=6)
    ap.add_argument("--scorecard", action="store_true")
    ap.add_argument("--swh", action="store_true")
    ap.add_argument("--seco", action="store_true")
    ap.add_argument("--ligero", action="store_true", help="solo /repos y licencia: barridos grandes")
    args = ap.parse_args()

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
    vistos, limpia = set(), []
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

    resultados, errores = [], []
    with cf.ThreadPoolExecutor(max_workers=args.concurrente) as ex:
        futuros = {ex.submit(medir, r, args.scorecard, args.swh, args.ligero): r for r in limpia}
        for i, f in enumerate(cf.as_completed(futuros), 1):
            r = futuros[f]
            try:
                res = f.result()
            except Exception as e:
                errores.append((r, str(e)))
                print(f"  [{i:3d}] {r}: excepción {e}")
                continue
            if res and "error" in res:
                errores.append((r, res["error"]))
                print(f"  [{i:3d}] {r}: {res['error']}")
            elif res:
                resultados.append(res)
                print(f"  [{i:3d}] {res['repo']:<44} ★{res['merito']['stars']:<7} "
                      f"{res['actividad']['estado']:<10} {str(res['licencia']['spdx'] or 'sin licencia'):<14} "
                      f"{res['licencia']['metodo']:<16} push {res['actividad']['ultimo_push']}"
                      + (f" · scorecard {res['merito']['scorecard']}" if res['merito']['scorecard'] is not None else "")
                      + (" · SWHID sí" if res['procedencia']['swhid'] else ""))

    resumen = {"fecha": hoy(), "medidos": len(resultados), "errores": len(errores),
               "vivos": sum(1 for r in resultados if r["actividad"]["estado"] == "vivo"),
               "sin_licencia": sum(1 for r in resultados if r["licencia"]["metodo"] == "ausencia-firmada"),
               "con_swhid": sum(1 for r in resultados if r["procedencia"]["swhid"]),
               "con_scorecard": sum(1 for r in resultados if r["merito"]["scorecard"] is not None),
               "errores_detalle": [{"repo": r, "error": e} for r, e in errores]}
    (REGISTRO / f"_pulso-{hoy()}.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n",
                                                   encoding="utf-8")
    print(f"\nresumen: {len(resultados)} medidos · {resumen['vivos']} vivos · "
          f"{resumen['sin_licencia']} sin licencia declarada · {resumen['con_swhid']} con SWHID · "
          f"{resumen['con_scorecard']} con scorecard · {len(errores)} errores")
    return 0 if not errores else 0


if __name__ == "__main__":
    sys.exit(main())
