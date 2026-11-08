#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FECHA DE LA CASA · una sola fuente de verdad para el día.

La casa vive en Santo Domingo (UTC-4, sin horario de verano). El entorno donde corren las
herramientas suele estar en UTC, y ahí «hoy» cambia cuatro horas antes que en el barrio: a las
20:35 del 31 de octubre en Santo Domingo, UTC ya dice 1 de noviembre. Fechar con la hora del
servidor puso un día de más en la errata de esta misma jornada. Se corrigió aquí, una vez.

Uso:
  python3 tools/fecha_casa.py            → 2026-10-31
  python3 tools/fecha_casa.py --larga    → sábado 31 de octubre de 2026
  python3 tools/fecha_casa.py --json     → {"fecha": "2026-10-31", "zona": "America/Santo_Domingo"}

Qué hace:
  * Devuelve la fecha ISO de hoy en la zona horaria de la casa (America/Santo_Domingo).
  * Devuelve la fecha en formato largo para cabecer las piezas.

Qué NO hace:
  * No adivina la zona horaria: la declara y la usa siempre.
  * No consulta servidores externos: la fecha la da el sistema operativo con TZ fijo.
  * No depende del reloj del servidor si está en UTC: convierte a Santo Domingo.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import date, datetime
from zoneinfo import ZoneInfo

ZONA: ZoneInfo = ZoneInfo("America/Santo_Domingo")
DIAS: tuple[str, ...] = (
    "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo",
)
MESES: tuple[str, ...] = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
)


@dataclass(frozen=True)
class FechaCasa:
    """Fecha de la casa: valor único, inmutable, validado contra la zona horaria."""

    iso: str
    larga: str
    zona: str = "America/Santo_Domingo"

    @classmethod
    def ahora(cls) -> "FechaCasa":
        """Construye la fecha de la casa desde el reloj del sistema en Santo Domingo."""
        momento: datetime = datetime.now(ZONA)
        d: date = momento.date()
        return cls(
            iso=d.isoformat(),
            larga=f"{DIAS[d.weekday()]} {d.day} de {MESES[d.month - 1]} de {d.year}",
            zona="America/Santo_Domingo",
        )

    def json(self) -> str:
        return json.dumps(
            {"fecha": self.iso, "zona": self.zona, "larga": self.larga},
            ensure_ascii=False,
        )


def hoy() -> str:
    """Fecha ISO de la casa (Santo Domingo)."""
    return FechaCasa.ahora().iso


def larga(momento: datetime | None = None) -> str:
    if momento is None:
        return FechaCasa.ahora().larga
    d = momento.date()
    return f"{DIAS[d.weekday()]} {d.day} de {MESES[d.month - 1]} de {d.year}"


def hoy_iso() -> str:
    return hoy()


def _construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Una sola fuente de verdad para el día de La Bandita (Santo Domingo).",
    )
    parser.add_argument(
        "--larga",
        action="store_true",
        help="muestra la fecha en formato largo para cabecer piezas",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emite JSON con fecha, zona y larga",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _construir_parser()
    args = parser.parse_args(argv)
    fecha = FechaCasa.ahora()
    if args.json:
        print(fecha.json())
    elif args.larga:
        print(fecha.larga)
    else:
        print(fecha.iso)
    return 0


if __name__ == "__main__":
    sys.exit(main())
