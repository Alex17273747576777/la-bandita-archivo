#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""labandita-registro · servidor MCP de solo lectura sobre el registro verificado de La Bandita.

Regla de honestidad del servidor: NINGUNA herramienta devuelve una afirmación sin fecha.
Si el dato supera el umbral de frescura, se responde `estado: "rancio"` con la edad exacta
en vez de devolverlo como si fuera de hoy. Un servidor que miente con seguridad es peor
que uno que no existe.

Transporte: stdio (servidor local). Sin escritura, sin red, sin credenciales.
Ejecutar: python3 mcp-labandita-registro/servidor.py
Requiere: pip install "mcp>=2,<3"   (o mcp<2, que usa FastMCP)
"""
from __future__ import annotations
import json
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
LOTES = RAIZ / "attestations"
UMBRAL_FRESCURA = 180

try:                                    # SDK 2.x
    from mcp.server.mcpserver import MCPServer as Servidor
except ImportError:                     # SDK 1.x
    from mcp.server.fastmcp import FastMCP as Servidor  # type: ignore


def _fichas() -> list[dict]:
    cache = getattr(_fichas, "_cache", None)
    if cache is None:
        cache = []
        for p in sorted(REGISTRO.glob("*.json")):
            if p.name.startswith("_"):
                continue
            try:
                cache.append(json.loads(p.read_text(encoding="utf-8")))
            except json.JSONDecodeError:
                continue
        _fichas._cache = cache  # type: ignore[attr-defined]
    return cache


def _edad(ficha: dict) -> int:
    try:
        return (date.today() - date.fromisoformat(ficha["medido_en"])).days
    except Exception:
        return -1


def _con_fecha(ficha: dict) -> dict:
    edad = _edad(ficha)
    return {
        **ficha,
        "estado_frescura": "rancio" if edad > UMBRAL_FRESCURA or edad < 0 else "vigente",
        "edad_dias": edad,
        "umbral_dias": UMBRAL_FRESCURA,
    }


def _resumen(f: dict) -> dict:
    """Lo mínimo para decidir, siempre con fecha y fuente."""
    return {
        "repo": f["repo"],
        "estado_frescura": _con_fecha(f)["estado_frescura"],
        "edad_dias": _con_fecha(f)["edad_dias"],
        "medido_en": f["medido_en"],
        "licencia": f["licencia"]["spdx"],
        "metodo_licencia": f["licencia"]["metodo"],
        "actividad": f["actividad"]["estado"],
        "ultimo_push": f["actividad"]["ultimo_push"],
        "stars": (f.get("merito") or {}).get("stars"),
        "fuente": f["fuente"]["primaria"],
    }


servidor = Servidor(
    name="labandita-registro",
    title="Registro verificado de La Bandita",
    version="1.0.0",
    instructions=("Registro de repositorios del ecosistema Android libre, medido y fechado por La Bandita. "
                  "Toda respuesta trae medido_en, fuente y estado_frescura. Si un dato está rancio, dilo: "
                  "no lo presentes como actual."),
)


@servidor.tool(description="Busca recursos del registro por texto libre (nombre, descripción, repo).")
def buscar_recurso(texto: str, limite: int = 10) -> dict:
    if not texto or len(texto.strip()) < 2:
        return {"error": "texto demasiado corto", "criterio": "mínimo 2 caracteres"}
    aguja = texto.strip().lower()
    encontrados = []
    for f in _fichas():
        campo = f"{f['repo']} {f.get('descripcion', '')} {' '.join(f.get('piezas', []))}".lower()
        if aguja in campo:
            encontrados.append(f)
    encontrados.sort(key=lambda f: -((f.get("merito") or {}).get("stars") or 0))
    return {
        "consulta": texto,
        "coincidencias": len(encontrados),
        "resultados": [_resumen(f) for f in encontrados[: max(1, min(limite, 50))]],
    }


@servidor.tool(description="Devuelve la ficha completa de un repositorio (owner/name), con su evidencia.")
def ficha_recurso(repo: str) -> dict:
    objetivo = (repo or "").strip().lower()
    for f in _fichas():
        if f["repo"].lower() == objetivo:
            return _con_fecha(f)
    return {"error": "no está en el registro", "repo": repo,
            "nota": "ausencia declarada: no se inventa una ficha que no existe"}


@servidor.tool(description="Agregados de una familia o de todo el registro: vivos, dormidos, licencias.")
def censo_familia(familia: str = "") -> dict:
    aguja = (familia or "").strip().lower()
    seleccion = [f for f in _fichas() if not aguja or aguja in f["repo"].lower()
                 or any(aguja in p.lower() for p in f.get("piezas", []))]
    estados, licencias = {}, {}
    for f in seleccion:
        estados[f["actividad"]["estado"]] = estados.get(f["actividad"]["estado"], 0) + 1
        clave = f["licencia"]["spdx"] or "sin licencia declarada"
        licencias[clave] = licencias.get(clave, 0) + 1
    return {
        "familia": familia or "(todo el registro)",
        "fichas": len(seleccion),
        "actividad": estados,
        "licencias": dict(sorted(licencias.items(), key=lambda x: -x[1])[:10]),
        "medido_en": sorted({f["medido_en"] for f in seleccion})[-1] if seleccion else None,
        "nota": "agregado calculado sobre el registro tal como fue medido; no extrapola",
    }


@servidor.tool(description="Dice si el dato de un recurso está vigente o rancio, con la edad exacta.")
def estado_frescura(repo: str) -> dict:
    objetivo = (repo or "").strip().lower()
    for f in _fichas():
        if f["repo"].lower() == objetivo:
            edad = _edad(f)
            return {"repo": f["repo"], "medido_en": f["medido_en"], "edad_dias": edad,
                    "umbral_dias": UMBRAL_FRESCURA,
                    "veredicto": "rancio" if edad > UMBRAL_FRESCURA or edad < 0 else "vigente",
                    "recomendacion": "volver a medir antes de citarlo" if edad > UMBRAL_FRESCURA else "se puede citar con su fecha"}
    return {"error": "no está en el registro", "repo": repo}


@servidor.tool(description="Verifica la licencia siguiendo el orden de la casa: SPDX → endpoint → texto → ausencia firmada.")
def verificar_licencia(repo: str) -> dict:
    objetivo = (repo or "").strip().lower()
    for f in _fichas():
        if f["repo"].lower() == objetivo:
            lic = f["licencia"]
            return {"repo": f["repo"], "spdx": lic["spdx"], "metodo": lic["metodo"],
                    "verificado_en": lic["verificado_en"], "archivo": lic.get("archivo"),
                    "lectura": ("sin licencia declarada: se firma la ausencia, no se inventa una licencia"
                                if lic["metodo"] == "ausencia-firmada" else
                                "identificador tal como lo devolvió la fuente, sin interpretación"),
                    "medido_en": f["medido_en"]}
    return {"error": "no está en el registro", "repo": repo}


@servidor.tool(description="Devuelve la atestación del último lote y la cadena de huellas.")
def atestacion_lote(lote: str = "") -> dict:
    if not LOTES.exists():
        return {"error": "no hay atestaciones", "nota": "correr tools/atestar.py"}
    # Sólo `lote-AAAA-MM-DD.json`: los paquetes `.sigstore.json` casan con el comodín y no son lotes.
    lotes = sorted(p for p in LOTES.glob("lote-*.json") if re.fullmatch(r"lote-\d{4}-\d{2}-\d{2}\.json", p.name))
    if not lotes:
        return {"error": "no hay atestaciones"}
    buscado = (lote or "").strip()
    elegido = next((p for p in lotes if buscado and buscado in p.name), lotes[-1])
    datos = json.loads(elegido.read_text(encoding="utf-8"))
    # La tabla (una huella por archivo, más de un megabyte) no cabe en una respuesta: se da su
    # tamaño y dónde está. Quien quiera comprobar un archivo tiene el `.tsv` al lado.
    if isinstance(datos.get("tabla"), dict):
        datos["tabla"] = {"entradas": len(datos["tabla"]),
                          "archivo": f"attestations/{elegido.stem}.tsv"}
    # Hay lotes con dos formas: hasta el 7 de noviembre (`lote`, `huella_lote_anterior`) y desde
    # el 9 (`fecha`, `anterior`). Esta herramienta sólo leía la vieja y reventaba con KeyError en
    # cuanto existió un lote nuevo; la integración continua no lo veía (`| tee` sin pipefail).
    cadena = []
    for p in lotes:
        d = json.loads(p.read_text(encoding="utf-8"))
        cadena.append({"lote": d.get("lote") or d.get("fecha") or p.stem.removeprefix("lote-"),
                       "huella": d.get("huella"),
                       "anterior": d.get("huella_lote_anterior", d.get("anterior"))})
    return {"atestacion": datos, "cadena": cadena,
            "advertencia": "el sello prueba que los archivos no cambiaron después de firmarse; "
                           "no prueba que la medición sea correcta — eso lo prueba la vara"}


def main() -> int:
    transporte = "stdio"
    if len(sys.argv) > 2 and sys.argv[1] == "--transporte":
        transporte = sys.argv[2]
    servidor.run(transporte=transporte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
