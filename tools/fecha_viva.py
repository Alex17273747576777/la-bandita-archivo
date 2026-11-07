#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FECHA VIVA · la fecha se lee en vivo al empezar y al terminar, no se recuerda.

El dueño lo pidió el 4-nov-2026 después de un apagón de dos horas: «siempre, a partir de
ahora, revisá la fecha entera en vivo antes de empezar cualquier censo y al terminarlo».

La razón es simple y no tiene nada de ceremonia: un censo hecho a las 9 de la mañana y
publicado a las 3 de la tarde es un censo de la mañana. Y una máquina que estuvo apagada
dos horas puede amanecer con la fecha de ayer en el reloj local, con lo que toda la
medición queda firmada con el día equivocado.

Qué hace, en este orden:
  1. lee la hora de la casa (America/Santo_Domingo) y la de UTC;
  2. lee la hora de **fuera**, del encabezado `Date` de la API de GitHub —una fuente que
     no es esta máquina y que no puede estar mal por un apagón local—;
  3. compara las dos y dice si hay desfase de minutos o de día;
  4. imprime la fecha entera en palabras, el día de la semana, la semana ISO y la hora;
  5. deja constancia en `docs/FECHA-VIVA.json` la primera y la última vez del día.

Uso:
    python3 tools/fecha_viva.py --inicio     # antes de cualquier censo (lo llama `make ritual`)
    python3 tools/fecha_viva.py --fin        # después del censo, y compara con el inicio
    python3 tools/fecha_viva.py --decir      # solo decir la fecha, sin escribir nada
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ACTA = RAIZ / "docs" / "FECHA-VIVA.json"
CASA = "America/Santo_Domingo"
MESES = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio",
         8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
DIAS = {0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves", 4: "viernes", 5: "sábado", 6: "domingo"}


def hora(zona: str) -> datetime:
    """La hora en una zona, dicha por el sistema operativo. Sin adivinar el desfase a mano."""
    r = subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S"], capture_output=True, text=True,
                       env={"TZ": zona, "PATH": "/usr/bin:/bin"})
    return datetime.fromisoformat(r.stdout.strip())


def hora_de_casa() -> datetime:
    return hora(CASA)


def hora_de_fuera() -> datetime | None:
    """La hora de GitHub, que no depende de ningún reloj de esta máquina."""
    r = subprocess.run(["curl", "-sI", "--max-time", "20", "https://api.github.com"], capture_output=True, text=True)
    m = re.search(r"^date:\s*(.+)$", r.stdout, re.I | re.M)
    if not m:
        return None
    return parsedate_to_datetime(m.group(1).strip()).astimezone(timezone.utc).replace(tzinfo=None)


def decir(casa: datetime, fuera: datetime | None) -> str:
    larga = f"{DIAS[casa.weekday()]} {casa.day} de {MESES[casa.month]} de {casa.year}"
    iso = casa.isocalendar()
    linea = (f"FECHA VIVA · {larga} · {casa.strftime('%H:%M:%S')} en Santo Domingo "
             f"({hora('UTC').strftime('%H:%M:%S')} UTC) · semana ISO {iso[1]} de {iso[0]}")
    if fuera is None:
        return linea + "\n  · sin hora de fuera: no se pudo leer el encabezado de GitHub (se sigue, pero se anota)"
    propio_utc = hora("UTC")
    minutos = round((propio_utc - fuera).total_seconds() / 60, 1)
    aviso = ""
    if abs(minutos) >= 2:
        aviso = f"\n  ✗ desfase con la hora de fuera: {minutos:+.1f} min — el reloj de esta máquina no es de fiar"
    elif abs(minutos) >= 0.5:
        aviso = f"\n  · desfase aceptable con la hora de fuera: {minutos:+.1f} min"
    else:
        aviso = f"\n  · reloj en hora con la fuente de fuera ({minutos:+.1f} min)"
    return linea + aviso


def registrar(momento: str) -> int:
    casa = hora_de_casa()
    fuera = hora_de_fuera()
    texto = decir(casa, fuera)
    print(texto)
    datos = {"fecha": casa.date().isoformat()}
    if ACTA.exists():
        datos = json.loads(ACTA.read_text(encoding="utf-8"))
    hoy = casa.date().isoformat()
    if datos.get("fecha") != hoy:
        datos = {"fecha": hoy, "veces": []}
    datos.setdefault("veces", []).append({
        "momento": momento, "casa": casa.isoformat(timespec="seconds"),
        "utc": hora("UTC").isoformat(timespec="seconds"),
        "fuera": fuera.isoformat(timespec="seconds") if fuera else None,
        "dia_de_la_semana": DIAS[casa.weekday()]})
    ACTA.parent.mkdir(parents=True, exist_ok=True)
    ACTA.write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  · anotado en {ACTA.relative_to(RAIZ)} como «{momento}» "
          f"({len([v for v in datos['veces'] if v['momento'] == momento])} vez/veces hoy)")
    return 0


def main() -> int:
    a = sys.argv[1:]
    if "--decir" in a:
        print(decir(hora_de_casa(), hora_de_fuera()))
        return 0
    if "--inicio" in a:
        return registrar("inicio")
    if "--fin" in a:
        registrar("fin")
        # la comprobación que importa: ¿el censo empezó y terminó el mismo día?
        datos = json.loads(ACTA.read_text(encoding="utf-8")) if ACTA.exists() else {}
        veces = datos.get("veces") or []
        if veces:
            primero = veces[0]["casa"][:10]
            ultimo = veces[-1]["casa"][:10]
            if primero != ultimo:
                print(f"  ✗ el censo empezó el {primero} y termina el {ultimo}: hay que volver a medir, "
                      "no se puede firmar con dos fechas")
                return 1
            print(f"  ✓ empezó y terminó el mismo día: {primero}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
