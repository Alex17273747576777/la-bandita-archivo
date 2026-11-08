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
  2. lee la hora de fuera, del encabezado Date de la API de GitHub —una fuente que
     no es esta máquina y que no puede estar mal por un apagón local—;
  3. compara las dos y dice si hay desfase de minutos o de día;
  4. imprime la fecha entera en palabras, el día de la semana, la semana ISO y la hora;
  5. deja constancia en docs/FECHA-VIVA.json la primera y la última vez del día.

Qué NO hace:
  * No confía en el reloj local sin compararlo con una fuente externa.
  * No corrige el reloj del sistema: solo reporta el desfase.
  * No modifica ninguna pieza ni ficha: solo anota la fecha en docs/FECHA-VIVA.json.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
ACTA: Path = RAIZ / "docs" / "FECHA-VIVA.json"
CASA: str = "America/Santo_Domingo"
MESES: dict[int, str] = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
    7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}
DIAS: dict[int, str] = {
    0: "lunes", 1: "martes", 2: "miércoles", 3: "jueves",
    4: "viernes", 5: "sábado", 6: "domingo",
}


@dataclass(frozen=True)
class LecturaFecha:
    """Una lectura de fecha: hora local de la casa, hora UTC, y hora de fuera (GitHub)."""

    casa: datetime
    utc: datetime
    fuera: datetime | None
    desfase_min: float | None

    def en_palabras(self) -> str:
        larga = f"{DIAS[self.casa.weekday()]} {self.casa.day} de {MESES[self.casa.month]} de {self.casa.year}"
        iso = self.casa.isocalendar()
        partes = [
            f"FECHA VIVA · {larga} · {self.casa.strftime('%H:%M:%S')} en Santo Domingo",
            f"({self.utc.strftime('%H:%M:%S')} UTC)",
            f"semana ISO {iso[1]} de {iso[0]}",
        ]
        linea = " ".join(partes)
        if self.fuera is None:
            linea += "\n  · sin hora de fuera: no se pudo leer el encabezado de GitHub (se sigue, pero se anota)"
        elif self.desfase_min is not None:
            if abs(self.desfase_min) >= 2:
                linea += f"\n  ✗ desfase con la hora de fuera: {self.desfase_min:+.1f} min — el reloj de esta máquina no es de fiar"
            elif abs(self.desfase_min) >= 0.5:
                linea += f"\n  · desfase aceptable con la hora de fuera: {self.desfase_min:+.1f} min"
            else:
                linea += f"\n  · reloj en hora con la fuente de fuera ({self.desfase_min:+.1f} min)"
        return linea

    def misma_fecha_que(self, otra: "LecturaFecha") -> bool:
        return self.casa.date() == otra.casa.date()


def hora(zona: str) -> datetime:
    """La hora en una zona, dicha por el sistema operativo. Sin adivinar el desfase a mano."""
    r = subprocess.run(
        ["date", "+%Y-%m-%dT%H:%M:%S"],
        capture_output=True,
        text=True,
        env={"TZ": zona, "PATH": "/usr/bin:/bin"},
    )
    return datetime.fromisoformat(r.stdout.strip())


def hora_de_casa() -> datetime:
    return hora(CASA)


def hora_utc() -> datetime:
    return hora("UTC")


def hora_de_fuera() -> datetime | None:
    """La hora de GitHub, que no depende de ningún reloj de esta máquina."""
    r = subprocess.run(
        ["curl", "-sI", "--max-time", "20", "https://api.github.com"],
        capture_output=True,
        text=True,
    )
    m = re.search(r"^date:\s*(.+)$", r.stdout, re.I | re.M)
    if not m:
        return None
    return parsedate_to_datetime(m.group(1).strip()).astimezone(timezone.utc).replace(tzinfo=None)


def leer_fecha_viva() -> LecturaFecha:
    casa = hora_de_casa()
    utc = hora_utc()
    fuera = hora_de_fuera()
    desfase: float | None = None
    if fuera is not None:
        desfase = round((utc - fuera).total_seconds() / 60, 1)
    return LecturaFecha(casa=casa, utc=utc, fuera=fuera, desfase_min=desfase)


def registrar(momento: str) -> int:
    lectura = leer_fecha_viva()
    print(lectura.en_palabras())
    datos: dict = {"fecha": lectura.casa.date().isoformat()}
    if ACTA.exists():
        try:
            datos = json.loads(ACTA.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            datos = {"fecha": lectura.casa.date().isoformat()}
    hoy_iso = lectura.casa.date().isoformat()
    if datos.get("fecha") != hoy_iso:
        datos = {"fecha": hoy_iso, "veces": []}
    datos.setdefault("veces", []).append({
        "momento": momento,
        "casa": lectura.casa.isoformat(timespec="seconds"),
        "utc": lectura.utc.isoformat(timespec="seconds"),
        "fuera": lectura.fuera.isoformat(timespec="seconds") if lectura.fuera else None,
        "dia_de_la_semana": DIAS[lectura.casa.weekday()],
    })
    ACTA.parent.mkdir(parents=True, exist_ok=True)
    ACTA.write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_veces = sum(1 for v in datos["veces"] if v["momento"] == momento)
    print(
        f"  · anotado en {ACTA.relative_to(RAIZ)} como «{momento}» "
        f"({n_veces} vez/veces hoy)"
    )
    return 0


def mismo_dia_inicio_y_fin() -> bool:
    """Comprueba que el censo empezó y terminó el mismo día de la casa."""
    if not ACTA.exists():
        return True
    try:
        datos = json.loads(ACTA.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return True
    veces = datos.get("veces") or []
    if not veces:
        return True
    primero = veces[0]["casa"][:10]
    ultimo = veces[-1]["casa"][:10]
    if primero != ultimo:
        print(
            f"  ✗ el censo empezó el {primero} y termina el {ultimo}: hay que volver a medir, "
            "no se puede firmar con dos fechas"
        )
        return False
    print(f"  ✓ empezó y terminó el mismo día: {primero}")
    return True


def _construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lee la fecha en vivo al empezar y al terminar un censo, comparando con la fuente de fuera (GitHub).",
    )
    parser.add_argument("--decir", action="store_true", help="solo decir la fecha, sin escribir nada")
    parser.add_argument("--inicio", action="store_true", help="antes de cualquier censo (lo llama make ritual)")
    parser.add_argument("--fin", action="store_true", help="después del censo, y compara con el inicio")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _construir_parser()
    args = parser.parse_args(argv)

    if args.decir:
        print(leer_fecha_viva().en_palabras())
        return 0

    if args.inicio:
        return registrar("inicio")

    if args.fin:
        registrar("fin")
        return 0 if mismo_dia_inicio_y_fin() else 1

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
