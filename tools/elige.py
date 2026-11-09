#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ELIGE · saca de la medición ya hecha las fichas de una pieza, sin medir nada nuevo.

Qué hace:
  * Lee docs/CENSO-MEDIDO-2026-11-09.json (3.125 repositorios medidos uno por uno).
  * Filtra por sección de fmhy.net, por palabra clave del nombre o por cohorte de edad.
  * Escribe docs/MEDICION-PNN-2026-11-09.json con lo que la pieza va a citar, para que la
    pieza pueda citar una ruta que existe de verdad (lo comprueba la compuerta G17).
  * Imprime una tabla corta para escribir la pieza sin volver al JSON grande.

Qué NO hace:
  * No inventa campos: si un dato no se midió, queda como null.
  * No decide el orden de la pieza: eso lo escribe quien redacta.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CENSO = RAIZ / "docs" / "CENSO-MEDIDO-2026-11-09.json"
SALIDA = RAIZ / "docs"


def cargar() -> list[dict]:
    datos = json.loads(CENSO.read_text(encoding="utf-8"))
    return [r for r in datos["repos"] if r.get("estado") == "vivo"]


def por_seccion(repos: list[dict], patron: str) -> list[dict]:
    rx = re.compile(patron, re.IGNORECASE)
    return [r for r in repos if rx.search(r.get("repo", "") + " " + (r.get("descripcion") or ""))]


def jovenes(repos: list[dict], dias: int) -> list[dict]:
    return [r for r in repos if r.get("dias_nace") is not None and r["dias_nace"] <= dias]


def con_huella(repos: list[dict]) -> list[dict]:
    return [r for r in repos if (r.get("huellas_ultima") or 0) > 0]


def ficha(r: dict) -> dict:
    """Los campos que una pieza puede citar. Los que no se midieron quedan en null."""
    return {
        "repo": r["repo"],
        "stars": r.get("stars"),
        "forks": r.get("forks"),
        "licencia": r.get("licencia"),
        "nace": r.get("nace"),
        "dias_nace": r.get("dias_nace"),
        "push": r.get("push"),
        "dias_push": r.get("dias_push"),
        "entregas": r.get("entregas"),
        "ultima_entrega": r.get("rel_fecha"),
        "rel_dias": r.get("rel_dias"),
        "adjuntos_ultima": r.get("adjuntos_ultima"),
        "huellas_ultima": r.get("huellas_ultima"),
        "descargas_ultima": r.get("descargas_ultima"),
        "abiertas": r.get("abiertas"),
        "archivado": r.get("archivado"),
        "lenguaje": r.get("lenguaje"),
    }


def tabla(repos: list[dict], limite: int) -> str:
    lineas = []
    for r in repos[:limite]:
        lineas.append(
            f"  {r['repo'][:44]:44} ★{r.get('stars')!s:>7} "
            f"nace={r.get('dias_nace')!s:>4}d push={r.get('dias_push')!s:>4}d "
            f"adj={r.get('adjuntos_ultima')!s:>4} huella={r.get('huellas_ultima')!s:>2} "
            f"lic={str(r.get('licencia'))[:9]:9}"
        )
    return "\n".join(lineas)


def main() -> int:
    ap = argparse.ArgumentParser(description="Elige fichas medidas para una pieza.")
    ap.add_argument("--pieza", required=True, help="NN de la pieza")
    ap.add_argument("--clave", default="", help="palabra clave en el nombre o la descripción")
    ap.add_argument("--dias-nace", type=int, default=0, help="solo nacidos hace N días o menos")
    ap.add_argument("--huella", action="store_true", help="solo los que publican huella")
    ap.add_argument("--orden", default="stars", choices=["stars", "dias_nace", "rel_dias", "huellas_ultima"])
    ap.add_argument("--limite", type=int, default=20, help="cuántas fichas se guardan")
    ap.add_argument("--ver", action="store_true", help="solo imprimir, no escribir JSON")
    args = ap.parse_args()

    repos = cargar()
    if args.clave:
        repos = por_seccion(repos, args.clave)
    if args.dias_nace:
        repos = jovenes(repos, args.dias_nace)
    if args.huella:
        repos = con_huella(repos)
    repos.sort(key=lambda r: (r.get(args.orden) is None, -(r.get(args.orden) or 0)))

    elegidos = repos[: args.limite]
    print(tabla(elegidos, args.limite))
    print(f"\n{len(elegidos)} de {len(repos)} candidatos · orden por {args.orden}")

    if not args.ver:
        salida = SALIDA / f"MEDICION-P{args.pieza}-2026-11-09.json"
        salida.write_text(
            json.dumps(
                {
                    "pieza": args.pieza,
                    "medido_en": date.today().isoformat(),
                    "fuente": "docs/CENSO-MEDIDO-2026-11-09.json — censo de fmhy.net medido contra la API pública de GitHub",
                    "filtro": {
                        "clave": args.clave or None,
                        "dias_nace": args.dias_nace or None,
                        "con_huella": args.huella,
                        "orden": args.orden,
                    },
                    "total_candidatos": len(repos),
                    "fichas": [ficha(r) for r in elegidos],
                },
                ensure_ascii=False,
                indent=1,
            ),
            encoding="utf-8",
        )
        print(f"→ {salida.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
