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
"""
from __future__ import annotations
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

ZONA = ZoneInfo("America/Santo_Domingo")
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
         "septiembre", "octubre", "noviembre", "diciembre"]


def ahora() -> datetime:
    return datetime.now(ZONA)


def hoy() -> str:
    """Fecha ISO de la casa (Santo Domingo)."""
    return ahora().date().isoformat()


def larga(momento: datetime | None = None) -> str:
    d = (momento or ahora()).date()
    return f"{DIAS[d.weekday()]} {d.day} de {MESES[d.month - 1]} de {d.year}"


def hoy_iso() -> str:
    return hoy()


if __name__ == "__main__":
    print(larga() if "--larga" in sys.argv else hoy())
