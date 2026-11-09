#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MIDE LA PIEZA 42 · los 41 índices de Miyomi que nadie había medido.

Miyomi lista 47 índices y solo uno estaba en el archivo. Aquí se miden los otros cuarenta
y uno contra la API pública de GitHub: estrellas, licencia, edad, actividad, última entrega
y —lo que de verdad importa en esta serie— cuántos adjuntos publica y cuántos llevan suma.

Se separan dos cosas que se suelen mezclar:
  * los que están en GitHub, medibles con la API;
  * los que viven en otra forja (git.luna-app.eu, codeberg), que se dicen y no se finge medirlos.

Escribe docs/MEDICION-P42-2026-11-09.json con la forma de ficha de repositorio que ya
entienden redacta.py, fijados.py y coteja.py.

Uso: python3 tools/medir_indices_42.py
"""
from __future__ import annotations

import json
import subprocess
import time
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DOCS = RAIZ / "docs"
HOY = "2026-11-09"
HOY_D = date(2026, 11, 9)


def token() -> str:
    out = subprocess.run(["bash", "-c", "grep -m1 -o 'ghp_[A-Za-z0-9]*' ~/.gh-tokens"],
                         capture_output=True, text=True).stdout.strip()
    return out


def gh(path: str, t: str) -> dict:
    r = subprocess.run(["curl", "-s", "-m", "30", "-H", f"Authorization: bearer {t}",
                        f"https://api.github.com/{path}"], capture_output=True, text=True).stdout
    try:
        return json.loads(r)
    except Exception:  # noqa: BLE001
        return {}


def dias(iso: str | None) -> int | None:
    if not iso:
        return None
    try:
        return (HOY_D - date.fromisoformat(iso[:10])).days
    except Exception:  # noqa: BLE001
        return None


def medir_repo(full: str, t: str) -> dict | None:
    j = gh(f"repos/{full}", t)
    if (not isinstance(j, dict) or not j or j.get("message")):
        # Puede estar mudado: la API responde 301 con el número del repositorio, y por ese
        # número se llega al nombre de hoy sin adivinar nada.
        red = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{redirect_url}",
                              "-H", f"Authorization: bearer {t}",
                              f"https://api.github.com/repos/{full}"],
                             capture_output=True, text=True).stdout.strip()
        if "/repositories/" in red:
            j = gh(red.split("api.github.com/")[-1], t)
        if not isinstance(j, dict) or not j or j.get("message"):
            return None
    rel = gh(f"repos/{full}/releases/latest", t)
    if not isinstance(rel, dict):
        rel = {}
    adj = rel.get("assets") or []
    n_adj = len(adj)
    n_hue = sum(1 for a in adj if any(k in a["name"].lower()
                                      for k in (".sha256", ".sha512", ".asc", ".sig", "sums", "checksum")))
    return {
        "repo": j["full_name"],
        "stars": j.get("stargazers_count"),
        "forks": j.get("forks_count"),
        "licencia": (j.get("license") or {}).get("spdx_id"),
        "nace": (j.get("created_at") or "")[:10],
        "dias_nace": dias(j.get("created_at")),
        "dias_push": dias(j.get("pushed_at")),
        "abiertas": j.get("open_issues_count"),
        "entregas": None,
        "ultima_entrega": (rel.get("published_at") or "")[:10] or None,
        "adjuntos_ultima": n_adj if rel and not rel.get("message") else None,
        "huellas_ultima": n_hue if rel and not rel.get("message") else None,
        "descargas_ultima": sum(a.get("download_count", 0) for a in adj) if adj else 0,
        "archivado": j.get("archived"),
        "lenguaje": j.get("language"),
    }


def main() -> int:
    t = token()
    cand = json.loads((DOCS / "CANDIDATOS-MIYOMI-2026-11-09.json").read_text(encoding="utf-8"))
    fichas, fuera_de_github = [], []
    for c in cand:
        # Miyomi guarda el repositorio de tres maneras: «dueno/repo» a secas, la URL
        # completa de GitHub, o una URL de otra forja. La primera versión de este medidor
        # solo aceptaba la URL completa y mandó 41 repos de GitHub a «otra forja». Se
        # corrige el lector: «dueno/repo» ES GitHub mientras no diga lo contrario.
        full = c["repo"].strip()
        if full.startswith("https://github.com/"):
            full = full[len("https://github.com/"):]
        if full.startswith(("http://", "https://")) or "/" not in full:
            fuera_de_github.append({"nombre": c["nombre"], "url": full, "likes": c.get("likes")})
            continue
        full = full.strip("/")
        # Miyomi guarda a veces la ruta del lanzamiento («dueno/repo/releases»), a veces la
        # del commit. Lo que se mide es el repositorio: dueño y nombre, y nada más.
        partes = [x for x in full.split("/") if x]
        if len(partes) > 2:
            full = "/".join(partes[:2])
        f = medir_repo(full, t)
        if f:
            f["indice_de_miyomi"] = c["nombre"]
            f["me_gusta_miyomi"] = c.get("likes")
            f["idioma_indice"] = c.get("idioma")
            fichas.append(f)
        else:
            fuera_de_github.append({"nombre": c["nombre"], "url": full, "likes": c.get("likes"),
                                    "nota": "la API no lo devuelve"})
        time.sleep(0.3)

    fichas.sort(key=lambda x: -(x.get("stars") or 0))
    d = {
        "medido_en": HOY,
        "medido_a_las": time.strftime("%H:%M"),
        "pieza": "42",
        "tema": (f"Los índices de extensión que nadie había medido: {len(fichas)} medidos y "
                 f"{len(fuera_de_github)} en otra forja"),
        "fuente": ("miyomi.app/api/extensions (los 41 índices que no estaban en el archivo) + "
                   "API pública de GitHub por repositorio"),
        "fichas": fichas,
        "fuera_de_github": fuera_de_github,
        "nota": ("Cada ficha es un repositorio medido hoy. Los que viven en otra forja se listan "
                 "aparte: no se finge haberlos medido."),
    }
    p = DOCS / f"MEDICION-P42-{HOY}.json"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  ✓ 42: {len(fichas)} medidos · {len(fuera_de_github)} fuera de GitHub · {p.name}")
    for f in fichas:
        print(f"     ★{f['stars']:6} {f['repo'][:42]:42} {str(f['licencia'])[:10]:10} "
              f"firmas={f['huellas_ultima']}/{f['adjuntos_ultima']} push={f['dias_push']}d")
    for f in fuera_de_github:
        print(f"     [otra forja] {f['nombre'][:30]:30} {f['url'][:48]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
