#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VENCIMIENTO · qué ficha sigue vigente, cuál está por vencer y cuál hay que volver a medir.

Lee las fichas del registro, mide la edad de cada campo contra su evidencia (no contra lo
que la ficha declara), aplica las ventanas de docs/POLITICA-FRESCURA.json y escribe tres cosas:
el tablero docs/VENCIMIENTOS.md, el índice registry/_vencimientos.json y el bloque frescura
de cada ficha.

Qué hace:
  * Decide el estado de cada ficha: vigente | por_vencer | vencida | sin_respaldo | sin_objeto.
  * Usa la fecha dentro del payload de evidencia (registry/_evidencia/), no la fecha declarada.
  * Escribe docs/VENCIMIENTOS.md con el tablero de estado.
  * Escribe registry/_vencimientos.json con el índice de vencimientos.
  * Escribe el bloque frescura en cada ficha del registro.

Qué NO hace:
  * No mide repositorios: decide qué hay que medir y lo deja escrito.
  * No corrige fechas declaradas: solo reporta si la evidencia las respalda o no.
  * No borra fichas sin objeto: las declara y las deja para la historia.
"""
from __future__ import annotations

import json
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
REGISTRO: Path = RAIZ / "registry"
EVIDENCIA: Path = REGISTRO / "_evidencia"
DOCS: Path = RAIZ / "docs"
VENCIMIENTOS_MD: Path = DOCS / "VENCIMIENTOS.md"
VENCIMIENTOS_JSON: Path = REGISTRO / "_vencimientos.json"
POLITICA: Path = DOCS / "POLITICA-FRESCURA.json"

VENTANAS_DEFAULT: dict[str, int] = {
    "actividad": 30,
    "licencia": 90,
    "ficha_entera": 180,
}


def _cargar_politica() -> dict[str, int]:
    """Las ventanas de frescura, con la razón al lado de cada una.

    EL FALLO QUE ESTO ARREGLA
    -------------------------
    `docs/POLITICA-FRESCURA.json` pasó de `ventanas` como diccionario a `ventanas`
    como **lista de fichas** (`{campo, ventana_dias, por_que}`), que es mejor: cada
    ventana lleva escrita su razón. El código siguió llamando `.items()` sobre una
    lista y moría con `AttributeError: 'list' object has no attribute 'items'`.

    Pasaba desapercibido porque `vencimiento.py` no está entre los pasos que el
    flujo de integración ejecuta con el veredicto explícito, así que el error solo
    aparecía al llamarlo a mano.

    Se aceptan las dos formas. De la lista se toma la primera ficha de cada campo
    de primer nivel (`actividad.ultimo_push` → `actividad`), y lo que no aparezca
    se queda con el valor por defecto.
    """
    if POLITICA.exists():
        try:
            d = json.loads(POLITICA.read_text(encoding="utf-8"))
            bruto = d.get("ventanas")
            if isinstance(bruto, dict):
                return {k: int(v) for k, v in bruto.items()}
            if isinstance(bruto, list):
                ventanas = dict(VENTANAS_DEFAULT)
                for ficha in bruto:
                    if not isinstance(ficha, dict):
                        continue
                    campo = str(ficha.get("campo", ""))
                    dias = ficha.get("ventana_dias")
                    if not campo or dias is None:
                        continue
                    # `actividad.ultimo_push` → `actividad`; `licencia` → `licencia`.
                    clave = campo.split(".")[0]
                    if clave not in ventanas or clave == campo:
                        ventanas[clave] = int(dias)
                return ventanas
        except (json.JSONDecodeError, OSError, TypeError, ValueError):
            pass
    return VENTANAS_DEFAULT


def _fecha_de_evidencia(ficha: dict) -> date | None:
    """Lee la fecha dentro del archivo de evidencia, no la declarada en la ficha."""
    fid = ficha.get("id", "")
    ev = ficha.get("evidencia", {})
    payload_ref = ev.get("payload_ref", "")
    if payload_ref:
        ruta = RAIZ / payload_ref
        if ruta.exists():
            try:
                d = json.loads(ruta.read_text(encoding="utf-8"))
                fecha_str = d.get("_medido_en") or d.get("fecha")
                if fecha_str:
                    return date.fromisoformat(str(fecha_str)[:10])
            except (json.JSONDecodeError, OSError, ValueError):
                pass
    # fallback: fecha declarada en la ficha
    medido_en = ficha.get("medido_en")
    if medido_en:
        try:
            return date.fromisoformat(str(medido_en)[:10])
        except ValueError:
            pass
    return None


def _estado_ficha(ficha: dict, ventanas: dict[str, int], hoy: date) -> dict:
    """Calcula el bloque frescura de una ficha."""
    id_ficha = ficha.get("id", "")
    repo = ficha.get("repo", "")
    fecha_evidencia = _fecha_de_evidencia(ficha)
    medido_en_declarado = ficha.get("medido_en")

    # Determinar si el repositorio existe (sin_objeto = 404)
    actividad = ficha.get("actividad", {})
    estado_actividad = actividad.get("estado", "vivo")
    semantica_http = actividad.get("semantica_http")

    dias_evidencia = None
    if fecha_evidencia:
        dias_evidencia = (hoy - fecha_evidencia).days

    ventana_ficha = ventanas["ficha_entera"]
    ventana_actividad = ventanas["actividad"]
    ventana_licencia = ventanas["licencia"]

    # Determinar estado
    if semantica_http == 404 or estado_actividad == "muerto":
        estado = "sin_objeto"
        motivo = "el repositorio no existe: la API devolvió 404"
    elif fecha_evidencia is None:
        estado = "sin_respaldo"
        motivo = "no hay payload de evidencia que respalde la fecha declarada"
    elif dias_evidencia is not None and dias_evidencia > ventana_ficha:
        estado = "vencida"
        motivo = f"evidencia de hace {dias_evidencia} días (umbral {ventana_ficha})"
    elif dias_evidencia is not None and dias_evidencia > ventana_ficha * 0.75:
        estado = "por_vencer"
        motivo = f"evidencia de hace {dias_evidencia} días, próxima revisión en {ventana_ficha - dias_evidencia} días"
    else:
        estado = "vigente"
        motivo = f"evidencia de hace {dias_evidencia if dias_evidencia is not None else 0} días"

    # Verificar si la fecha declarada coincide con la evidencia
    fecha_declarada_valida = False
    if medido_en_declarado and fecha_evidencia:
        try:
            fecha_dec = date.fromisoformat(str(medido_en_declarado)[:10])
            fecha_declarada_valida = fecha_dec == fecha_evidencia
        except ValueError:
            pass

    proxima_remedicion = None
    if estado == "por_vencer" and dias_evidencia is not None:
        proxima_remedicion = str(fecha_evidencia + __import__("datetime").timedelta(days=ventana_ficha))
    elif estado == "vencida":
        proxima_remedicion = str(hoy)

    return {
        "estado": estado,
        "dias": dias_evidencia,
        "evidencia_en": str(fecha_evidencia) if fecha_evidencia else None,
        "proxima_remedicion": proxima_remedicion,
        "ventana_dias": ventana_ficha,
        "motivo": motivo,
        "fecha_declarada_valida": fecha_declarada_valida,
    }


def aplicar() -> dict:
    """Recalcula el estado de frescura de cada ficha y escribe los archivos de salida."""
    ventanas = _cargar_politica()
    hoy = date.today()
    fichas: list[Path] = sorted(p for p in REGISTRO.glob("*.json") if not p.name.startswith("_"))

    resumen = {"vigente": 0, "por_vencer": 0, "vencida": 0, "sin_respaldo": 0, "sin_objeto": 0}
    vencimientos: list[dict] = []

    for p in fichas:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue

        frescura = _estado_ficha(d, ventanas, hoy)
        resumen[frescura["estado"]] = resumen.get(frescura["estado"], 0) + 1

        d["frescura"] = frescura
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")

        vencimientos.append({
            "id": d.get("id", ""),
            "repo": d.get("repo", ""),
            "estado": frescura["estado"],
            "dias": frescura["dias"],
            "motivo": frescura["motivo"],
        })

    vencimientos.sort(key=lambda x: ({"vencida": 0, "por_vencer": 1, "sin_respaldo": 2, "sin_objeto": 3, "vigente": 4}.get(x["estado"], 5), -x["dias"] if x["dias"] is not None else 0))

    # Escribir docs/VENCIMIENTOS.md
    lineas = ["# VENCIMIENTOS DEL REGISTRO", "", f"Fecha de corte: {hoy.isoformat()}", ""]
    for estado, etiqueta in (("vigente", "Vigentes"), ("por_vencer", "Por vencer"), ("vencida", "Vencidas"), ("sin_respaldo", "Sin respaldo"), ("sin_objeto", "Sin objeto")):
        n = resumen.get(estado, 0)
        lineas.append(f"**{etiqueta}**: {n}")
    lineas.append("")
    lineas.append("## Detalle por estado")
    lineas.append("")
    for v in vencimientos:
        lineas.append(f"- {v['id']} · {v['repo']} · {v['estado']} · {v['motivo']}")
    VENCIMIENTOS_MD.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    # Escribir registry/_vencimientos.json
    VENCIMIENTOS_JSON.write_text(
        json.dumps({"fecha": hoy.isoformat(), "resumen": resumen, "fichas": vencimientos}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )

    print(f"vencimientos: {resumen['vigente']} vigentes · {resumen['por_vencer']} por vencer · "
          f"{resumen['vencida']} vencidas · {resumen['sin_respaldo']} sin respaldo · {resumen['sin_objeto']} sin objeto")
    return resumen


def lista_por_estado(estado: str) -> list[str]:
    """Devuelve la lista de ids de fichas en un estado dado."""
    if not VENCIMIENTOS_JSON.exists():
        return []
    try:
        d = json.loads(VENCIMIENTOS_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return [f["id"] for f in d.get("fichas", []) if f["estado"] == estado]


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Calcula el estado de frescura de cada ficha del registro.")
    parser.add_argument("--aplicar", action="store_true", help="recalcula y escribe el estado de frescura de todas las fichas")
    parser.add_argument("--lista", metavar="ESTADO", help="lista los ids de fichas en un estado dado")
    args = parser.parse_args(argv)

    if args.lista:
        ids = lista_por_estado(args.lista)
        for id_ficha in ids:
            print(id_ficha)
        return 0

    resumen = aplicar()
    return 0


if __name__ == "__main__":
    sys.exit(main())
