#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VENCIMIENTO · qué ficha sigue vigente, cuál está por vencer y cuál hay que volver a medir.

Por qué existe: la vara ya avisaba a los 180 días (G2), pero ese aviso mira una sola cosa —
`medido_en`— y una fecha se puede escribir sin haber medido nada. Pasó aquí: 4.186 fichas
declaraban el 3 de noviembre teniendo como única evidencia una fila del censo del 15 de octubre.
La compuerta las contaba como recién medidas y ninguna estaba vencida, que es exactamente el
error que este programa existe para encontrar.

Cómo lo encuentra, en tres pasos:

1. **La ventana de cada campo**, con su razón, vive en `docs/POLITICA-FRESCURA.json`.
   No hay ventanas escritas dentro de este programa: si se cambia una, se cambia en un sitio.
2. **La edad se mide contra la evidencia**, no contra la confianza. Si la ficha dice que se
   midió el 3 de noviembre y su payload es del 15 de octubre, la edad que cuenta es la del
   payload y la ficha se marca `sin_respaldo`.
3. **El veredicto se escribe**: `docs/VENCIMIENTOS.md` para leer y `registry/_vencimientos.json`
   para que lo consuma la compuerta G16 de la vara.

Qué recibe: `registry/*.json`, `docs/POLITICA-FRESCURA.json` y la fecha de la casa.
Qué produce: `docs/VENCIMIENTOS.md`, `registry/_vencimientos.json` y, con `--aplicar`, el bloque
`frescura` dentro de cada ficha (estado, días, ventana y próxima remedición).
Qué no hace: **no mide repositorios**. Decide qué hay que medir y lo deja escrito; medir es el
oficio de `tools/censo_medir.py`. Un programa que decide y mide en el mismo gesto no se puede
auditar: cuando dice «vigente» nadie sabe si lo comprobó o si se lo creyó.

Uso:
    python3 tools/vencimiento.py                  # informe legible
    python3 tools/vencimiento.py --json           # legible por máquina
    python3 tools/vencimiento.py --aplicar        # escribe el bloque frescura en las fichas
    python3 tools/vencimiento.py --lista sin_respaldo   # ids, uno por línea (para medir)
    python3 tools/vencimiento.py --peor           # solo lo que falla (código 1 si hay algo)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
POLITICA = RAIZ / "docs" / "POLITICA-FRESCURA.json"
SALIDA_MD = RAIZ / "docs" / "VENCIMIENTOS.md"
SALIDA_JSON = REGISTRO / "_vencimientos.json"
AVISO_DIAS = 15          # los últimos 15 días de una ventana son «por vencer», no «vencida»


# ─────────────────────────────────────────────────────────────────────────────
#  La fecha de la evidencia: de dónde salió de verdad el dato que la ficha declara
# ─────────────────────────────────────────────────────────────────────────────
FECHA_EN_REF = re.compile(r"(20\d\d-\d\d-\d\d)")


def fecha_de_evidencia(ficha: dict) -> tuple[str | None, str]:
    """Devuelve (fecha, de dónde se leyó). None si no hay forma de saberlo.

    Se busca en este orden, y se para en el primero que responde:
    el payload propio (que trae su fecha dentro), la fila del censo (que la trae en el nombre
    del archivo) y el campo `medido_en` como último recurso declarado por la propia ficha.
    """
    ev = ficha.get("evidencia") or {}
    ref = ev.get("payload_ref") or ""
    if ref.startswith("registry/_evidencia/"):
        p = RAIZ / ref
        if not p.exists():
            return None, "payload citado que no existe"
        try:
            payload = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None, "payload ilegible"
        # El payload nuevo lleva su propia fecha dentro (`_medido_en`). El viejo, no: lo
        # que prueba es que la medición existió, no cuándo. En ese caso la fecha la pone la
        # ficha, y el origen lo dice para que nadie confunda una cosa con la otra.
        f = payload.get("_medido_en") or payload.get("medido_en") or payload.get("fecha")
        if f:
            return str(f)[:10], "payload propio fechado"
        return (ficha.get("medido_en") or None), "payload propio sin fecha dentro"
    m = FECHA_EN_REF.search(ref)
    if m:
        return m.group(1), "fila del censo"
    nota = (ev.get("nota") or "").lower()
    if "404" in ref or "404" in nota:
        return ficha.get("medido_en"), "respuesta 404 registrada"
    if "ficha profunda" in ref:
        return ficha.get("medido_en"), "ficha profunda del día"
    return None, "sin evidencia fechada"


def campo(ficha: dict, ruta: str):
    """Lee `actividad.ultimo_push`, `licencia` o `ficha` sin ternarios anidados."""
    if ruta == "ficha":
        return None
    actual = ficha
    for parte in ruta.split("."):
        if not isinstance(actual, dict):
            return None
        actual = actual.get(parte)
    return actual if isinstance(actual, str) and re.match(r"^\d{4}-\d{2}-\d{2}", actual) else None


def edad(fecha_iso: str, corte: date) -> int:
    return (corte - date.fromisoformat(fecha_iso[:10])).days


def fecha_de_medicion_de(ficha: dict, campo_nombre: str, f_ev: str | None,
                         declarada: str | None) -> tuple[str | None, str]:
    """Cuándo se midió ESE campo, no cuán viejo es el dato que contiene.

    La diferencia es la que hace útil la compuerta: un repositorio cuyo último empujón fue
    hace dos años está correctamente medido como dormido; lo que caduca es la *medición*,
    no el empujón. Se busca la fecha de comprobación propia del campo y, si no la tiene,
    se usa la de la ficha entera con su evidencia.
    """
    if campo_nombre == "licencia":
        v = (ficha.get("licencia") or {}).get("verificado_en")
        if v:
            return v[:10], "licencia.verificado_en"
    if campo_nombre == "merito.scorecard":
        s = (ficha.get("merito") or {}).get("scorecard_en")
        if s:
            return s[:10], "merito.scorecard_en"
        return None, "sin scorecard medido"
    return (f_ev or declarada), "medición de la ficha"


def evaluar(ficha: dict, ventanas: list[dict], corte: date) -> dict:
    """El veredicto de una ficha, con el campo que lo provoca a la vista."""
    f_ev, origen = fecha_de_evidencia(ficha)
    declarada = ficha.get("medido_en") or ""
    edades: dict[str, int] = {}
    vencidos: list[dict] = []

    for v in ventanas:
        nombre, dias = v["campo"], v["ventana_dias"]
        base, _de = fecha_de_medicion_de(ficha, nombre, f_ev, declarada)
        if not base:
            continue
        e = edad(base, corte)
        edades[nombre] = e
        if e > dias:
            vencidos.append({"campo": nombre, "dias": e, "ventana": dias})

    respaldo_ok = bool(f_ev) and bool(declarada) and f_ev[:10] == declarada[:10]

    # Un repositorio que la API no conoce (404) no se puede volver a medir nunca: la ficha
    # se queda, pero marcada. «Vigente» sería contarla como medida al día, que es justo lo
    # que este programa existe para no hacer.
    motivo = None
    if (ficha.get("actividad") or {}).get("semantica_http") == 404:
        estado = "sin_objeto"
        motivo = "el repositorio ya no existe: la API devuelve 404, no hay nada que volver a medir"
    elif not respaldo_ok:
        estado = "sin_respaldo"
    elif vencidos:
        estado = "vencida"
        motivo = "; ".join("%s de hace %s días (ventana %s)" % (c["campo"], c["dias"], c["ventana"])
                           for c in vencidos)
    elif any(dias - edades[nombre] <= AVISO_DIAS
             for v in ventanas if (nombre := v["campo"]) in edades
             for dias in [v["ventana_dias"]]):
        estado = "por_vencer"
    else:
        estado = "vigente"

    proxima = None
    if edades:
        margenes = [v["ventana_dias"] - edades[v["campo"]]
                    for v in ventanas if v["campo"] in edades]
        proxima = (corte + timedelta(days=max(0, min(margenes)))).isoformat()

    return {
        "id": ficha.get("id"),
        "repo": ficha.get("repo"),
        "estado": estado,
        "declarada": declarada or None,
        "evidencia": f_ev,
        "origen_evidencia": origen,
        "edad_dias": max(edades.values()) if edades else None,
        "edades": edades,
        "vencida_por": vencidos,
        "motivo": motivo,
        "proxima_remedicion": proxima,
    }


def fichas() -> list[Path]:
    return sorted(p for p in REGISTRO.glob("*.json") if not p.name.startswith("_"))


def evaluar_todo() -> tuple[dict, list[dict], Counter]:
    corte = date.fromisoformat(fecha_casa_hoy())
    politica = json.loads(POLITICA.read_text(encoding="utf-8"))
    ventanas = politica["ventanas"]
    resultados, ilegibles, cuenta = [], [], Counter()
    for p in fichas():
        try:
            ficha = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            ilegibles.append(p.name)
            continue
        r = evaluar(ficha, ventanas, corte)
        r["archivo"] = p.name
        resultados.append(r)
        cuenta[r["estado"]] += 1
    resumen = {
        "corte": corte.isoformat(),
        "fichas": len(resultados),
        "estados": dict(cuenta),
        "ventanas": {v["campo"]: v["ventana_dias"] for v in ventanas},
        "sin_respaldo": sum(1 for r in resultados if r["estado"] == "sin_respaldo"),
        "vencidas": sum(1 for r in resultados if r["estado"] == "vencida"),
        "sin_objeto": sum(1 for r in resultados if r["estado"] == "sin_objeto"),
        "ilegibles": ilegibles,
        "fichas_sin_respaldo": [r["id"] for r in resultados if r["estado"] == "sin_respaldo"][:50],
        "fichas_vencidas_sin_motivo": [r["id"] for r in resultados
                                       if r["estado"] == "vencida" and not r["motivo"]][:50],
        "veredicto": ("TODO VIGENTE" if not cuenta["sin_respaldo"] and not cuenta["vencida"]
                      else "HAY FICHAS QUE VOLVER A MEDIR"),
    }
    return resumen, resultados, cuenta


def mil(n) -> str:
    """Los números de la casa se leen con punto de millar: 6.838, no 6838."""
    return f"{n:,}".replace(",", ".")


def escribir_md(resumen: dict, resultados: list[dict]) -> None:
    corte = resumen["corte"]
    orden = {"sin_respaldo": 0, "vencida": 1, "por_vencer": 2, "sin_objeto": 3, "vigente": 4}
    peores = sorted(resultados, key=lambda r: (orden[r["estado"]], -(r["edad_dias"] or 0)))[:25]
    lineas = [
        "# VENCIMIENTOS DEL REGISTRO",
        "",
        "*Generado por `tools/vencimiento.py` con las ventanas de "
        "[`POLITICA-FRESCURA.json`](POLITICA-FRESCURA.json). No se edita a mano: se vuelve a correr.*",
        "",
        f"**TL;DR —** al corte del **{corte}**, de **{mil(resumen['fichas'])} fichas**: "
        f"**{mil(resumen['estados'].get('vigente', 0))} vigentes**, "
        f"**{resumen['estados'].get('por_vencer', 0)} por vencer**, "
        f"**{resumen['vencidas']} vencidas** y "
        f"**{resumen['sin_respaldo']} sin respaldo de fecha**. "
        f"Además, **{resumen.get('sin_objeto', 0)} sin objeto**: el repositorio ya no existe, "
        f"así que no hay nada que volver a medir. Veredicto: **{resumen['veredicto']}**.",
        "",
        "## Qué significa cada estado",
        "",
        "| Estado | Qué dice | Qué se hace |",
        "|---|---|---|",
        "| **vigente** | todos sus campos dentro de ventana y la fecha respaldada por su evidencia | nada |",
        "| **por vencer** | algún campo entra en sus últimos 15 días | se avisa: entra en la próxima tanda |",
        "| **vencida** | algún campo supera su ventana | se vuelve a medir, y si no se puede, se declara |",
        "| **sin respaldo** | la fecha declarada no es la de su evidencia | se vuelve a medir para que la fecha sea verdad |",
        "| **sin objeto** | el repositorio ya no existe (404) | no se puede remedir: se conserva la ficha con su motivo |",
        "",
        "## Las ventanas, y por qué cada una",
        "",
        "| Campo | Ventana | Por qué |",
        "|---|---|---|",
    ]
    for v in json.loads(POLITICA.read_text(encoding="utf-8"))["ventanas"]:
        lineas.append(f"| `{v['campo']}` | {v['ventana_dias']} días | {v['por_que']} |")
    lineas += [
        "",
        "## Las primeras veinticinco, por gravedad",
        "",
        "| Ficha | Estado | Declarada | Evidencia | Edad | Vencida por |",
        "|---|---|---|---|---|---|",
    ]
    for r in peores:
        trozos = ["%s (%s d)" % (c["campo"], c["dias"]) for c in r["vencida_por"]]
        por = ", ".join(trozos) or "—"
        lineas.append(f"| `{r['id']}` | **{r['estado']}** | {r['declarada'] or '—'} | "
                      f"{r['evidencia'] or '—'} | {r['edad_dias'] if r['edad_dias'] is not None else '—'} d | {por} |")
    lineas += [
        "",
        "## La deuda, dicha sin adorno",
        "",
        f"Las **{resumen['sin_respaldo']}** fichas sin respaldo no están desactualizadas: están mal "
        "fechadas. Declaran el día de la última corrida como si fuera el día de la medición, y su "
        "única evidencia es una fila del censo del 15 de octubre. Eso no es un dato viejo: es un "
        "dato con la fecha cambiada, y la compuerta G2 las contaba como recién medidas. Se "
        "remedian, y la que no se pueda remedir se queda marcada como vencida con su motivo escrito.",
        "",
        "*La Bandita informa a partir de fuentes fechadas.*",
        "",
    ]
    SALIDA_MD.write_text("\n".join(lineas), encoding="utf-8")


def aplicar(resultados: list[dict]) -> int:
    """Escribe el bloque `frescura` en cada ficha. Idempotente: correrlo dos veces no cambia nada."""
    tocadas = 0
    por_id = {r["id"]: r for r in resultados}
    for p in fichas():
        try:
            ficha = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        r = por_id.get(ficha.get("id"))
        if not r:
            continue
        bloque = {
            "estado": r["estado"],
            "dias": r["edad_dias"],
            "evidencia_en": r["evidencia"],
            "proxima_remedicion": r["proxima_remedicion"],
            "ventana_dias": max(v["ventana_dias"] for v in
                               json.loads(POLITICA.read_text(encoding="utf-8"))["ventanas"]
                               if v["campo"] in r["edades"]) if r["edades"] else None,
        }
        if r["motivo"]:
            bloque["motivo"] = r["motivo"]
        if ficha.get("frescura") != bloque:
            ficha["frescura"] = bloque
            p.write_text(json.dumps(ficha, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                         encoding="utf-8")
            tocadas += 1
    return tocadas


def main() -> int:
    ap = argparse.ArgumentParser(description="Decide qué ficha está vigente y cuál hay que remedir.")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--aplicar", action="store_true", help="escribe el bloque frescura en las fichas")
    ap.add_argument("--lista", metavar="ESTADO", help="ids de un estado, uno por línea")
    ap.add_argument("--peor", action="store_true", help="solo lo que falla")
    args = ap.parse_args()

    resumen, resultados, cuenta = evaluar_todo()

    if args.lista:
        for r in resultados:
            if r["estado"] == args.lista:
                print(r["id"])
        return 0

    SALIDA_JSON.parent.mkdir(parents=True, exist_ok=True)
    SALIDA_JSON.write_text(json.dumps({"resumen": resumen, "fichas": resultados},
                                      ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if args.json:
        # Solo el resumen, para que la compuerta G16 lo lea sin ruido alrededor.
        print(json.dumps(resumen, ensure_ascii=False, indent=1))
        return 0
    if args.peor:
        for r in resultados:
            if r["estado"] in {"sin_respaldo", "vencida"}:
                print(f"✗ {r['id']}: {r['estado']} · declarada {r['declarada']} · "
                      f"evidencia {r['evidencia']} ({r['origen_evidencia']})")
        print(f"sin respaldo: {resumen['sin_respaldo']} · vencidas: {resumen['vencidas']}")
        return 1 if resumen["sin_respaldo"] or resumen["vencidas"] else 0

    escribir_md(resumen, resultados)
    if args.aplicar:
        tocadas = aplicar(resultados)
        print(f"frescura escrita en {tocadas} fichas")
    print(f"VENCIMIENTOS · corte {resumen['corte']} · {mil(resumen['fichas'])} fichas")
    for estado in ("vigente", "por_vencer", "vencida", "sin_respaldo", "sin_objeto"):
        print(f"  {estado:14s} {mil(cuenta[estado])}".rstrip())
    print(f"\nveredicto: {resumen['veredicto']}")
    print(f"tablero escrito: docs/VENCIMIENTOS.md · índice: registry/_vencimientos.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
