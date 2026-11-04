#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SELECTOR DE NOVEDAD — encuentra lo nuevo, lo recién publicado y lo desconocido.

El dueño fijó el 3-nov-2026 una regla editorial que manda sobre las demás: **primero lo
recién nacido, lo recién publicado y lo que casi nadie conoce**. Esa regla no se puede
cumplir de memoria —la memoria repite los mismos veinte proyectos famosos—, así que este
programa la convierte en una consulta sobre la evidencia que ya está sellada.

No mide: lee. Cada ficha del registro guarda el JSON crudo que devolvió la API el día de
su medición (`registry/_evidencia/<id>.json`), y de ahí salen la fecha de nacimiento del
repositorio, el último empujón, la última entrega y el tamaño. Con eso clasifica:

    nacido      creado hace 90 días o menos          · lo que acaba de aparecer
    joven       creado hace 365 días o menos         · todavía no tiene historia
    desconocido 300 estrellas o menos, y vivo        · lo que nadie ha recomendado aún
    recien      última entrega hace 30 días o menos  · lo que se movió esta semana
    joya        joven + vivo + desconocido + recién  · la combinación que pide la regla
    dormido     más de 365 días sin empujón
    muerto      el repositorio ya no existe (404)

Uso:
    python3 tools/novedad.py --joyas 30            # las treinta mejores joyas, hoy
    python3 tools/novedad.py --nacidos 90 --json   # lo nacido en el último trimestre
    python3 tools/novedad.py --desconocidos 50
    python3 tools/novedad.py --recien 30 --vivo
    python3 tools/novedad.py --ficha owner/repo     # por qué una ficha entra o no

El orden de las joyas no es por estrellas: es por **juventud × actividad**, porque ordenar
por estrellas devuelve siempre lo mismo y es justo lo contrario de lo que se pide.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "registry"
EVIDENCIA = REGISTRO / "_evidencia"

sys.path.insert(0, str(RAIZ / "tools"))
try:
    from fecha_casa import hoy as _hoy  # type: ignore
except Exception:  # pragma: no cover — el árbol puede no tener la herramienta
    def _hoy():
        return date.today()


def hoy() -> date:
    """La fecha de la casa puede venir como texto; aquí siempre es un `date`."""
    v = _hoy()
    return datetime.fromisoformat(str(v)).date() if isinstance(v, str) else v


def _fecha(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def fichas() -> list[dict]:
    """Devuelve una entrada por repositorio con lo que hace falta para decidir, ya calculado."""
    corte = hoy()
    salida: list[dict] = []
    for p in sorted(REGISTRO.glob("*.json")):
        try:
            f = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(f, dict) or "repo" not in f:
            continue
        ev_p = EVIDENCIA / (f.get("id") or p.stem)
        ev_p = ev_p.with_suffix(".json")
        ev: dict = {}
        if ev_p.exists():
            try:
                ev = json.loads(ev_p.read_text(encoding="utf-8"))
            except Exception:
                ev = {}
        nace = _fecha(ev.get("created_at"))
        push = _fecha((f.get("actividad") or {}).get("ultimo_push") or ev.get("pushed_at"))
        rel = _fecha((f.get("actividad") or {}).get("release_en"))
        estrellas = (f.get("merito") or {}).get("stars")
        if estrellas is None:
            estrellas = ev.get("stargazers_count")
        frescura = (f.get("frescura") or {}).get("estado", "vigente")
        salida.append({
            "id": f.get("id") or p.stem,
            "repo": f["repo"],
            "nombre": f.get("nombre") or f["repo"],
            "descripcion": (f.get("descripcion") or "").strip(),
            "estrellas": int(estrellas) if isinstance(estrellas, (int, float)) else None,
            "licencia": ((f.get("licencia") or {}).get("spdx") or "sin declarar"),
            "nace": nace.isoformat() if nace else None,
            "dias_vida": (corte - nace).days if nace else None,
            "push": push.isoformat() if push else None,
            "dias_push": (corte - push).days if push else None,
            "release": rel.isoformat() if rel else None,
            "dias_release": (corte - rel).days if rel else None,
            "ultima_release": (f.get("actividad") or {}).get("ultima_release"),
            "tamano_kb": ev.get("size"),
            "archivado": bool(ev.get("archived")),
            "sin_objeto": frescura == "sin_objeto",
            "medido_en": f.get("medido_en"),
        })
    return salida


def clasificar(f: dict) -> list[str]:
    marcas: list[str] = []
    if f["sin_objeto"]:
        return ["muerto"]
    if f["archivado"]:
        marcas.append("archivado")
    if f["dias_vida"] is not None and f["dias_vida"] <= 90:
        marcas.append("nacido")
    elif f["dias_vida"] is not None and f["dias_vida"] <= 365:
        marcas.append("joven")
    if f["estrellas"] is not None and f["estrellas"] <= 300 and (f["dias_push"] is None or f["dias_push"] <= 180):
        marcas.append("desconocido")
    if f["dias_release"] is not None and f["dias_release"] <= 30:
        marcas.append("recien")
    if f["dias_push"] is not None and f["dias_push"] > 365:
        marcas.append("dormido")
    return marcas


ANDROID = ("android", "apk", "shizuku", "magisk", "f-droid", "termux", "adb", "root",
           "material you", "kotlin", "compose", "wear os", "android tv")


def senales(f: dict) -> list[str]:
    """Lo que separa un proyecto de un montón de archivos. No es opinión: es lo que se puede ver."""
    s = []
    if not f["descripcion"]:
        s.append("sin-descripcion")
    if f["ultima_release"]:
        s.append("tiene-entrega")
    if f["licencia"] not in ("sin declarar", "NOASSERTION", None):
        s.append("licencia-clara")
    if (f["tamano_kb"] or 0) >= 1024:
        s.append("mas-de-1mb")
    if any(k in (f["descripcion"] or "").lower() for k in ANDROID):
        s.append("android")
    return s


def calidad(f: dict) -> float:
    """Cuánta señal trae. Sirve para no poner en portada un repositorio vacío de tres días."""
    s = senales(f)
    puntos = 0.0
    puntos += 0.35 if "tiene-entrega" in s else 0.0
    puntos += 0.20 if "mas-de-1mb" in s else 0.0
    puntos += 0.20 if "descripcion" not in [x for x in s] else 0.0
    puntos += 0.15 if "licencia-clara" in s else 0.0
    puntos += 0.10 if "android" in s else 0.0
    return round(puntos, 2)


def puntaje(f: dict) -> float:
    """Juventud × actividad, no fama. Lo nacido ayer vale más que lo de hace un año."""
    v = f["dias_vida"]
    p = f["dias_push"]
    if v is None or p is None:
        return 0.0
    joven = max(0.0, 1.0 - v / 730.0)          # dos años: por debajo de 1 se apaga despacio
    vivo = max(0.0, 1.0 - p / 180.0)           # seis meses sin empujón: cero
    raro = 1.0 if (f["estrellas"] or 0) <= 300 else 0.35
    senal = calidad(f)
    return round(100 * (0.34 * joven + 0.26 * vivo + 0.12 * raro + 0.28 * senal), 1)


def seleccionar(todas: list[dict], args) -> list[dict]:
    out = []
    for f in todas:
        m = clasificar(f)
        f["marcas"] = m
        f["senales"] = senales(f)
        f["calidad"] = calidad(f)
        f["puntaje"] = puntaje(f)
        if "muerto" in m:
            continue
        if getattr(args, "vivo", False) and (f["dias_push"] is None or f["dias_push"] > 180):
            continue
        if args.nacidos is not None and (f["dias_vida"] is None or f["dias_vida"] > args.nacidos):
            continue
        if args.desconocidos is not None and "desconocido" not in m:
            continue
        if args.recien is not None and (f["dias_release"] is None or f["dias_release"] > args.recien):
            continue
        if args.min_calidad is not None and calidad(f) < args.min_calidad:
            continue
        if args.joyas is not None:
            if not ({"joven", "nacido"} & set(m)) or "desconocido" not in m:
                continue
            if f["dias_push"] is None or f["dias_push"] > 30:
                continue
        out.append(f)
    out.sort(key=lambda x: -x["puntaje"])
    tope = args.joyas or args.nacidos or args.desconocidos or args.recien or 20
    return out[: max(tope, 1)]


def linea(f: dict) -> str:
    est = f"{f['estrellas']:,}".replace(",", ".") if f["estrellas"] is not None else "?"
    vida = f"{f['dias_vida']} d" if f["dias_vida"] is not None else "?"
    push = f"{f['dias_push']} d" if f["dias_push"] is not None else "?"
    rel = f"{f['dias_release']} d" if f["dias_release"] is not None else "—"
    return (f"{f['puntaje']:>5} │ ★{est:>8} │ vida {vida:>7} │ empujón {push:>6} │ entrega {rel:>6} │ "
            f"{f['licencia']:<12} │ {f['repo'][:44]:<44} │ {','.join(f['marcas'])}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Encuentra lo nuevo, lo recién publicado y lo desconocido.")
    ap.add_argument("--joyas", type=int, help="joven + vivo + desconocido, ordenado por juventud")
    ap.add_argument("--nacidos", type=int, help="creados hace N días o menos")
    ap.add_argument("--desconocidos", type=int, help="≤300★ y vivos")
    ap.add_argument("--recien", type=int, help="última entrega hace N días o menos")
    ap.add_argument("--vivo", action="store_true", help="solo empujón de 180 días o menos")
    ap.add_argument("--min-calidad", type=float, default=None,
                    help="exige señal mínima (0–1): entrega, tamaño, descripción, licencia, tema Android")
    ap.add_argument("--ficha", help="explica una ficha concreta (owner/repo)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    todas = fichas()
    if args.ficha:
        f = next((x for x in todas if x["repo"].lower() == args.ficha.lower()), None)
        if not f:
            print(f"no está en el registro: {args.ficha}")
            return 1
        f["marcas"] = clasificar(f)
        f["senales"] = senales(f)
        f["calidad"] = calidad(f)
        f["puntaje"] = puntaje(f)
        print(json.dumps(f, ensure_ascii=False, indent=1) if args.json else
              "\n".join(f"{k}: {v}" for k, v in f.items()))
        return 0

    sel = seleccionar(todas, args)
    if args.json:
        print(json.dumps(sel, ensure_ascii=False, indent=1))
        return 0

    vivas = sum(1 for f in todas if not f["sin_objeto"])
    print(f"corte {hoy()} · {len(todas)} fichas · {vivas} con objeto · selección: {len(sel)}\n")
    print("puntos │ estrellas │     vida │  empujón │ entrega │ licencia     │ repositorio                                  │ marcas")
    print("─" * 148)
    for f in sel:
        print(linea(f))
    print("\nOrden: juventud × actividad, no fama. Una joya es joven, está viva, casi nadie la conoce y publicó hace menos de un mes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
