#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync_fuentes.py · pone al día los créditos y las versiones de lo que la biblioteca cita.

Lee `corpus-la-bandita/teclado/FUENTES.json`, pregunta a GitHub por cada repositorio y
cada entrega, y reescribe:

  · corpus-la-bandita/teclado/VERSIONES.json  · última entrega, fecha del empujón y licencia
  · corpus-la-bandita/teclado/CREDITOS.md     · quién hizo cada cosa y bajo qué licencia

No inventa: si un repositorio no contesta, lo deja dicho en el fichero.

Uso:
    python3 tools/sync_fuentes.py
    python3 tools/sync_fuentes.py --comprobar   # falla si algún crédito está desfasado
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CARPETA = RAIZ / "corpus-la-bandita" / "teclado"
FUENTES = CARPETA / "FUENTES.json"
VERSIONES = CARPETA / "VERSIONES.json"
CREDITOS = CARPETA / "CREDITOS.md"
TOKEN = os.environ.get("GHP_A") or os.environ.get("GITHUB_TOKEN")


def pide(url):
    cab = {"Accept": "application/vnd.github+json", "User-Agent": "la-bandita/sync"}
    if TOKEN:
        cab["Authorization"] = "token " + TOKEN
    r = urllib.request.Request(url, headers=cab)
    try:
        with urllib.request.urlopen(r, timeout=40) as f:
            return json.load(f)
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}"}
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)[:80]}


def ficha(repo):
    d = pide(f"https://api.github.com/repos/{repo}")
    if d.get("_error") or d.get("message"):
        return {"repo": repo, "error": d.get("_error") or d.get("message")}
    rel = pide(f"https://api.github.com/repos/{repo}/releases/latest")
    return {
        "repo": repo,
        "estrellas": d.get("stargazers_count"),
        "archivado": d.get("archived"),
        "licencia": (d.get("license") or {}).get("spdx_id"),
        "empujon": (d.get("pushed_at") or "")[:10],
        "ultima_entrega": (rel.get("tag_name"), (rel.get("published_at") or "")[:10]) if rel.get("tag_name") else None,
        "consulta": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def main() -> int:
    fuentes = json.loads(FUENTES.read_text(encoding="utf-8"))
    salida, desfase = [], False
    for t in fuentes["teclados"]:
        f = ficha(t["repo"])
        f["rol"] = t["rol"]
        f["deriva_de"] = t.get("deriva_de")
        f["licencia_declarada_aqui"] = t["licencia"]
        # solo se avisa cuando GitHub da una licencia SPDX estándar y no coincide;
        # las licencias propias (FUTO Source First) salen como NOASSERTION y no son un desfase
        if f.get("licencia") and f["licencia"] != "NOASSERTION":
            if t["licencia"].split()[0].lower() not in str(f["licencia"]).lower():
                desfase = True
        salida.append(f)

    VERSIONES.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")

    lineas = ["# Créditos del teclado y de la biblioteca de instrucciones", "",
              "Todo lo que esta carpeta usa es de otros. Aquí está quién lo hizo, con qué licencia y",
              "hasta qué fecha se ha comprobado. Generado por `tools/sync_fuentes.py`; no se edita a mano.", ""]
    for f in salida:
        if f.get("error"):
            lineas.append(f"- **{f['repo']}** · no contesta: {f['error']}")
            continue
        entrega = f"{f['ultima_entrega'][0]} ({f['ultima_entrega'][1]})" if f["ultima_entrega"] else "sin entregas etiquetadas"
        lineas.append(f"- **{f['repo']}** · {f['rol']} · {f['licencia']} · última entrega {entrega} · "
                      f"último empujón {f['empujon']}")
        if f.get("deriva_de"):
            lineas.append(f"  - deriva de `{f['deriva_de']}`: el mérito del motor es de quien lo escribió primero")
    lineas += ["", "La biblioteca de `prompts.json` es texto propio, publicado bajo la misma licencia que este",
               "repositorio. Las instrucciones no incluyen código de terceros ni citas de nadie."]
    CREDITOS.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print(f"créditos escritos: {len(salida)} fuentes · desfase de licencia: {'sí' if desfase else 'no'}")
    return 1 if (desfase and "--comprobar" in sys.argv) else 0


if __name__ == "__main__":
    raise SystemExit(main())
