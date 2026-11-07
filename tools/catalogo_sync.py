#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""catalogo_sync.py · pone al día el catálogo con los repositorios que cita.

Hace tres cosas y ninguna inventa:

  1 · pregunta a GitHub por cada recurso y compara con lo que hay medido: ¿hay
     entrega nueva?, ¿se movió el repositorio?, ¿está archivado ahora?, ¿cambió
     la licencia?
  2 · escribe `catalogo/SINCRONIA.json` con el resultado y la fecha de la consulta.
  3 · escribe `catalogo/CREDITOS.md` con quién hizo cada cosa y bajo qué licencia,
     que es lo que hay que tener a mano cuando alguien reutiliza el trabajo.

Con `--actualizar`, además, refresca `catalogo/medido.json` y reescribe las fichas
sin tocar las guías escritas a mano.

Uso:
    python3 tools/catalogo_sync.py                 # solo informa
    python3 tools/catalogo_sync.py --actualizar    # informa y pone al día
    python3 tools/catalogo_sync.py --racimo audio
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
SINCRONIA = CATALOGO / "SINCRONIA.json"
CREDITOS = CATALOGO / "CREDITOS.md"
TOKEN = os.environ.get("GHP_A") or os.environ.get("GITHUB_TOKEN")


def pide(url):
    cab = {"Accept": "application/vnd.github+json", "User-Agent": "la-bandita/sync"}
    if TOKEN:
        cab["Authorization"] = "token " + TOKEN
    try:
        r = urllib.request.Request(url, headers=cab)
        with urllib.request.urlopen(r, timeout=40) as f:
            return json.load(f)
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}"}
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)[:60]}


def estado_actual(repo):
    d = pide(f"https://api.github.com/repos/{repo}")
    if d.get("_error") or d.get("message"):
        return {"error": d.get("_error") or d.get("message")}
    rel = pide(f"https://api.github.com/repos/{repo}/releases/latest")
    return {
        "archivado": d.get("archived"),
        "licencia": (d.get("license") or {}).get("spdx_id"),
        "empujon": (d.get("pushed_at") or "")[:10],
        "estrellas": d.get("stargazers_count"),
        "entrega": rel.get("tag_name") if isinstance(rel, dict) else None,
        "entrega_fecha": (rel.get("published_at") or "")[:10] if isinstance(rel, dict) else None,
    }


def main() -> int:
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    solo = sys.argv[sys.argv.index("--racimo") + 1] if "--racimo" in sys.argv else None
    ahora = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    cambios, iguales, errores = [], 0, 0
    for repo, f in sorted(medido.items()):
        if solo and f.get("racimo") != solo:
            continue
        if not f.get("existe"):
            continue
        act = estado_actual(repo)
        if act.get("error"):
            errores += 1
            continue
        prev = f.get("entrega") or {}
        notas = []
        if act["entrega"] and act["entrega"] != prev.get("tag"):
            notas.append(f"entrega nueva: {prev.get('tag')} → {act['entrega']} ({act['entrega_fecha']})")
        if act["archivado"] and not f.get("archivado"):
            notas.append("archivado ahora")
        if act["licencia"] and f.get("licencia") and act["licencia"] != f.get("licencia"):
            notas.append(f"licencia: {f['licencia']} → {act['licencia']}")
        if act["empujon"] and act["empujon"] > (f.get("empujon") or ""):
            notas.append(f"empujón: {f.get('empujon')} → {act['empujon']}")
        if notas:
            cambios.append({"repo": repo, "racimo": f.get("racimo"), "notas": notas,
                            "consultado": ahora, "actual": act})
            if "--actualizar" in sys.argv:
                f["archivado"] = act["archivado"]
                f["licencia"] = act["licencia"] or f.get("licencia")
                f["empujon"] = act["empujon"] or f.get("empujon")
                f["estrellas"] = act["estrellas"] or f.get("estrellas")
                if act["entrega"]:
                    f["entrega"] = {"tag": act["entrega"], "fecha": act["entrega_fecha"],
                                    "adjuntos": (prev.get("adjuntos") if act["entrega"] == prev.get("tag") else 0)}
                f["medido"] = ahora
        else:
            iguales += 1

    SINCRONIA.write_text(json.dumps({"consultado": ahora, "cambios": cambios,
                                     "iguales": iguales, "sin_respuesta": errores},
                                    ensure_ascii=False, indent=1), encoding="utf-8")

    lineas = ["# Créditos del catálogo", "",
              f"Quién hizo cada recurso y bajo qué licencia. Generado por `tools/catalogo_sync.py` "
              f"el {ahora}; no se edita a mano.", ""]
    por_racimo: dict[str, list] = {}
    for f in medido.values():
        por_racimo.setdefault(f.get("racimo", "sin racimo"), []).append(f)
    for racimo in sorted(por_racimo):
        lineas += [f"## {racimo}", ""]
        for f in sorted(por_racimo[racimo], key=lambda x: -(x.get("estrellas") or 0)):
            if not f.get("existe"):
                lineas.append(f"- `{f['repo']}` · no contesta al medir")
                continue
            lineas.append(f"- `{f['repo']}` · {f.get('licencia') or 'sin licencia declarada'} · "
                          f"última entrega {((f.get('entrega') or {}).get('tag')) or 'ninguna'} · "
                          f"empujón {f.get('empujon')}")
        lineas.append("")
    lineas += ["---", "",
               "Las fichas, los textos de las guías y los programas de `tools/` son trabajo propio y van",
               "bajo la licencia del repositorio. Lo que está citado entre comillas es de su autor y se dice",
               "de quién es, con la fecha en la que se copió."]
    CREDITOS.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    if "--actualizar" in sys.argv and cambios:
        MEDIDO.write_text(json.dumps(medido, ensure_ascii=False, indent=1), encoding="utf-8")
        subprocess.run([sys.executable, str(RAIZ / "tools" / "catalogo_ficha.py"), "--indice"], check=False)

    print(f"consulta: {ahora} · sin cambios: {iguales} · con cambios: {len(cambios)} · sin respuesta: {errores}")
    for c in cambios[:15]:
        print(f"  · {c['repo']}: " + "; ".join(c["notas"]))
    if len(cambios) > 15:
        print(f"  … y {len(cambios) - 15} más en {SINCRONIA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
