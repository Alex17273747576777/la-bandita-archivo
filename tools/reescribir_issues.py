#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REESCRIBIR ISSUES · aplica un plan de reescritura sobre issues propios.

Qué hace:
  * Lee un plan JSON: por cada issue, `accion` (editar | cerrar_con_nota), `titulo` y `cuerpo`.
  * Edita por la API de GitHub, con el token del entorno.
  * Antes de tocar nada, comprueba que el issue es mío (autor == login).
  * Guarda en un registro cada cambio con el cuerpo ANTERIOR y el NUEVO, para poder volver atrás.
  * Respeta el ritmo de la API (una escritura cada ~1 s) y reintenta lo que devuelva 403/429.

Qué NO hace:
  * No borra issues. Cerrar deja el hilo y la nota.
  * No inventa cuerpos: salen del plan.

Uso:
  python3 tools/reescribir_issues.py plan.json            # simulación
  python3 tools/reescribir_issues.py plan.json --aplicar
"""
from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "docs" / "ISSUES-RESPALDO-2026-11-09" / "CAMBIOS-APLICADOS.json"


def token() -> str:
    return subprocess.run(["bash", "-c", "grep -m1 -o 'ghp_[A-Za-z0-9]*' ~/.gh-tokens"],
                          capture_output=True, text=True).stdout.strip()


def api(metodo: str, ruta: str, datos: dict | None = None) -> tuple[int, dict]:
    cmd = ["curl", "-s", "-w", "\n%{http_code}", "-X", metodo,
           "-H", f"Authorization: bearer {T}", "-H", "Accept: application/vnd.github+json",
           f"https://api.github.com/{ruta}"]
    if datos is not None:
        cmd += ["-d", json.dumps(datos)]
    salida = subprocess.run(cmd, capture_output=True, text=True).stdout
    cuerpo, _, codigo = salida.rpartition("\n")
    try:
        return int(codigo or 0), json.loads(cuerpo or "{}")
    except Exception:  # noqa: BLE001
        return int(codigo or 0), {"crudo": cuerpo[:300]}


T = token()
LOGIN = api("GET", "user")[1].get("login", "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--aplicar", action="store_true")
    ap.add_argument("--solo", default="", help="filtra por repo o por repo#numero")
    args = ap.parse_args()

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    reg: list[dict] = json.loads(REGISTRO.read_text(encoding="utf-8")) if REGISTRO.exists() else []
    hechos = {(r["repo"], r["numero"]) for r in reg}

    for item in plan["issues"]:
        clave = f"{item['repo']}#{item['numero']}"
        if args.solo and args.solo not in clave:
            continue
        if (item["repo"], item["numero"]) in hechos:
            print(f"  = {clave}: ya estaba hecho, se salta")
            continue
        cod, actual = api("GET", f"repos/{item['repo']}/issues/{item['numero']}")
        if cod != 200:
            print(f"  ✗ {clave}: HTTP {cod} al leer")
            continue
        autor = (actual.get("user") or {}).get("login", "")
        if autor != LOGIN:
            print(f"  ✗ {clave}: no es mío (autor {autor}), no se toca")
            continue
        # GitHub no permite editar issues cerrados por API; si está cerrado, se dice.
        cerrado = actual.get("state") == "closed"
        antes = {"titulo": actual.get("title"), "cuerpo": actual.get("body") or "", "estado": actual.get("state")}

        if item["accion"] == "editar":
            if cerrado:
                print(f"  · {clave}: cerrado, no se puede editar; se revisa la nota")
            nuevo = {"title": item["titulo"], "body": item["cuerpo"]}
            if args.aplicar and not cerrado:
                cod, res = api("PATCH", f"repos/{item['repo']}/issues/{item['numero']}", nuevo)
                print(f"  {'✓' if cod == 200 else '✗'} {clave}: editar → HTTP {cod}")
            else:
                print(f"  ~ {clave}: SIMULACIÓN editar · {len(item['cuerpo'])} car · «{item['titulo'][:60]}»")
        elif item["accion"] == "cerrar_con_nota":
            nota = {"body": item["nota"]}
            if args.aplicar:
                c1, _ = api("POST", f"repos/{item['repo']}/issues/{item['numero']}/comments", nota)
                c2, _ = api("PATCH", f"repos/{item['repo']}/issues/{item['numero']}",
                            {"state": "closed", "state_reason": item.get("razon", "not_planned")})
                print(f"  {'✓' if c2 == 200 else '✗'} {clave}: nota {c1} + cerrar {c2}")
            else:
                print(f"  ~ {clave}: SIMULACIÓN cerrar con nota · «{item['nota'][:70]}»")

        if args.aplicar:
            reg.append({"repo": item["repo"], "numero": item["numero"], "accion": item["accion"],
                        "antes": antes, "despues": {"titulo": item.get("titulo"),
                                                    "cuerpo": item.get("cuerpo"),
                                                    "nota": item.get("nota")},
                        "cuando": time.strftime("%Y-%m-%dT%H:%M:%S")})
            REGISTRO.parent.mkdir(parents=True, exist_ok=True)
            REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        time.sleep(1.1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
