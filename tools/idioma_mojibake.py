#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOJIBAKE · mide la salud de codificación del corpus. No corrige: señala.

Detecta tres cosas, cada una con su evidencia:
  1. archivos que no decodifican como UTF-8 estricto;
  2. firmas de mojibake (UTF-8 leído como Latin-1: «Ã¡», «Ã©», «â€œ»);
  3. piernas de texto con densidad anómala de esas firmas (más de 3 por 1.000 caracteres).

Uso: python3 tools/idioma_mojibake.py [--json]
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PATRONES = {
    "acento_roto": re.compile(r"Ã[¡©ª­³±º­©­­­­]"),
    "comilla_rota": re.compile(r"â€[œ“”]"),
    "a_tilde": re.compile(r"Ã¡|Ã©|Ã­|Ã³|Ãº|Ã±"),
    "c2_c3": re.compile(r"Â[«»º°]"),
}
CUBIERTAS = ("Arena-Reimagined/01-PUBLICACIONES", "corpus-la-bandita", "03-PUBLICACIONES-2026-09-15",
             "04-VERSIONES-MULTIIDIOMA", "Arena-Reimagined/PROPUESTA-2026-10-31", "docs")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    no_utf8, sospechosos = [], []
    revisados = 0
    for p in sorted(RAIZ.rglob("*")):
        if not p.is_file() or ".git" in p.parts:
            continue
        rel = p.relative_to(RAIZ).as_posix()
        if not any(rel.startswith(c) for c in CUBIERTAS) or p.suffix.lower() not in {".md", ".txt", ".html"}:
            continue
        revisados += 1
        crudo = p.read_bytes()
        try:
            texto = crudo.decode("utf-8")
        except UnicodeDecodeError as e:
            no_utf8.append({"archivo": rel, "error": f"byte {e.start}: {e.reason}"})
            continue
        marcas = {k: len(v.findall(texto)) for k, v in PATRONES.items()}
        total = sum(marcas.values())
        if total >= 3:
            denso = total / max(len(texto), 1) * 1000
            if denso >= 0.5:
                sospechosos.append({"archivo": rel, "marcas": marcas, "por_mil": round(denso, 2),
                                    "caracteres": len(texto)})
    informe = {"revisados": revisados, "no_utf8": no_utf8, "mojibake": sospechosos,
               "nota": "medición, no corrección: la casa no edita piezas publicadas sin orden del dueño"}
    if args.json:
        print(json.dumps(informe, ensure_ascii=False, indent=1))
    else:
        print("SALUD DE CODIFICACIÓN · solo mide")
        print(f"archivos revisados: {revisados}")
        print(f"no decodifican como UTF-8: {len(no_utf8)}")
        for x in no_utf8[:10]:
            print(f"  · {x['archivo']} — {x['error']}")
        print(f"con mojibake denso: {len(sospechosos)}")
        for x in sospechosos[:10]:
            print(f"  · {x['archivo']} — {x['por_mil']} marcas por mil · {x['marcas']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
