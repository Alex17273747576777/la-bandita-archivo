#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ALINEAR · poner en el texto la cifra que la fuente acaba de dar (error E26).

Cuando una pieza cita veinte repositorios y la fuente mueve siete estrellas, el
trabajo no es recordar cuáles: es que un programa las cambie y lo diga en voz
alta. Esta herramienta hace solo eso, y solo donde no hay duda:

  · la línea tiene que nombrar **un** repositorio medido (si nombra dos, no toca);
  · solo cambia el número pegado a ★ (ni fechas, ni descargas, ni licencias);
  · imprime cada cambio, para que se pueda leer antes de creer.

Uso:
    python3 tools/alinear.py --pieza <pieza.md> --medicion docs/MEDICION-XX-2026-11-04.json
    python3 tools/alinear.py --pieza <pieza.md> --medicion ... --aplicar
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def main() -> int:
    a = sys.argv[1:]
    if "--pieza" not in a or "--medicion" not in a:
        print(__doc__)
        return 2
    pieza = Path(a[a.index("--pieza") + 1])
    med = json.loads(Path(a[a.index("--medicion") + 1]).read_text(encoding="utf-8"))
    repos = {r.split("/")[-1].lower(): (r, d) for r, d in (med.get("repos") or {}).items()
             if d.get("estado") == "vivo"}
    lineas = pieza.read_text(encoding="utf-8").splitlines()
    cambios = []
    for i, ln in enumerate(lineas):
        if "★" not in ln:
            continue
        halla = [(n, r, d) for n, (r, d) in repos.items() if n in ln.lower()]
        # «shizuku» está dentro de «shizuku-next»: si un nombre contiene a otro, gana el largo
        halla = [(n, r, d) for n, r, d in halla
                 if not any(n != otro and n in otro for otro, _, _ in halla)]
        if len(halla) != 1:
            continue
        _, repo, d = halla[0]
        nuevo = re.sub(r"★\s?[\d.]+", "★" + miles(d["stars"]), ln)
        if nuevo != ln:
            cambios.append((i + 1, repo, ln, nuevo))
            lineas[i] = nuevo
    for n, repo, viejo, nuevo in cambios:
        v = re.search(r"★[\d.]+", viejo)
        x = re.search(r"★[\d.]+", nuevo)
        print(f"  línea {n:>3} · {repo:<38} {v.group(0) if v else '—'} → {x.group(0) if x else '—'}")
    print(f"alineadas: {len(cambios)} · sin tocar: el resto")
    if "--aplicar" in a:
        pieza.write_text("\n".join(lineas) + "\n", encoding="utf-8")
        print(f"escrito: {pieza.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
