#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""catalogo_ficha.py · escribe o actualiza la ficha de cada recurso medido.

La ficha tiene dos mitades y solo una se genera:

  · lo que se mide —estrellas, licencia, empujón, entrega, qué dice el README— se
    reescribe cada vez que se vuelve a medir;
  · lo que se piensa —la guía, el para qué sirve y el cuándo no— vive entre los
    marcadores GUIA:INICIO y GUIA:FIN y **no se toca** al regenerar.

Así el catálogo se puede volver a medir entero sin perder una línea escrita a mano,
que es lo que pasa cuando se regenera un catálogo sin separar las dos cosas.

Uso:
    python3 tools/catalogo_ficha.py                # crea las que faltan y actualiza las demás
    python3 tools/catalogo_ficha.py --solo audio   # un racimo
    python3 tools/catalogo_ficha.py --indice       # además reescribe catalogo/INDICE.md
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"

INICIO = "<!-- GUIA:INICIO -->"
FIN = "<!-- GUIA:FIN -->"
GUIA_PENDIENTE = """No hay guía escrita todavía. Lo de arriba está medido; lo de abajo, no.

Esta ficha se genera sola y la guía se escribe a mano, recurso por recurso: para qué sirve de
verdad, qué pasos hay que dar en un teléfono y en qué caso no vale la pena. Mientras eso no esté,
la ficha sirve para saber qué es y en qué estado está, no para instalarlo."""

DIAS = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7,
        "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}


def dias_desde(fecha: str) -> int | None:
    try:
        d = date.fromisoformat(fecha)
    except Exception:  # noqa: BLE001
        return None
    return (date(2026, 11, 5) - d).days


def fecha_larga(iso: str) -> str:
    try:
        d = date.fromisoformat(iso)
    except Exception:  # noqa: BLE001
        return iso or "sin fecha"
    meses = list(DIAS)
    return f"{d.day} de {meses[d.month - 1]} de {d.year}"


def slug(repo: str) -> str:
    return repo.replace("/", "--").lower()


def limpio(t: str) -> str:
    return re.sub(r"\s+", " ", (t or "").strip())


def estado(f: dict) -> str:
    if not f.get("existe"):
        return "no contesta"
    if f.get("archivado"):
        return "archivado"
    d = dias_desde(f.get("empujon", ""))
    if d is None:
        return "sin fecha"
    if d <= 30:
        return "vivo"
    if d <= 365:
        return "lento"
    return "parado"


def bloque_medido(f: dict) -> str:
    d = dias_desde(f.get("empujon", ""))
    e = estado(f)
    lineas = [
        f"- **Estado:** {e} · último empujón el {fecha_larga(f.get('empujon',''))}"
        + (f" (hace {d} días)" if d is not None else ""),
        f"- **Estrellas:** {f.get('estrellas', 0):,}".replace(",", ".") + f" · {f.get('forks', 0)} bifurcaciones · {f.get('incidencias_abiertas', 0)} incidencias abiertas",
        f"- **Licencia:** {f.get('licencia') or 'sin licencia declarada'}",
        f"- **Lenguaje:** {f.get('lenguaje') or 'no declarado'} · creado el {fecha_larga(f.get('creado',''))}",
    ]
    ent = f.get("entrega")
    if ent:
        lineas.append(f"- **Última entrega:** `{ent['tag']}` del {fecha_larga(ent['fecha'])} · {ent['adjuntos']} adjuntos")
    else:
        lineas.append("- **Última entrega:** sin entregas etiquetadas")
    if f.get("plataformas"):
        lineas.append("- **Plataformas que menciona su README:** " + ", ".join(f["plataformas"]))
    if f.get("banderas"):
        lineas.append("- **Lo que dice su propio texto:** " + ", ".join(f["banderas"]))
    lineas.append(f"- **Medido:** {f.get('medido', 'sin fecha')}")
    return "\n".join(lineas)


def bloque_instalacion(f: dict) -> str:
    lineas = f.get("instalacion") or []
    if not lineas:
        extra = f" Su web: {f['web']}." if f.get("web") else ""
        return "Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega." + extra
    return "\n".join(f"- {limpio(l)}" for l in lineas)


def ficha(f: dict, guia: str | None = None) -> str:
    repo = f["repo"]
    nombre = f.get("nombre") or repo.split("/")[-1]
    if nombre.lower() == repo.split("/")[-1].lower():
        nombre = f"{nombre} · {repo.split('/')[0]}"
    claim = limpio(f.get("claim") or "")
    desc = limpio(f.get("descripcion") or "")
    ent = f.get("entrega")

    cabecera = [
        f"# {nombre}",
        "",
        f"*{desc or 'sin descripción en su repositorio'}*",
        "",
        f"**Racimo:** {f.get('racimo', 'sin racimo')} · **Repositorio:** `{repo}` · "
        f"**Estado:** {estado(f)} · **Medido:** {f.get('medido','')}",
        "",
        "## Qué es, según quien lo hace",
        "",
    ]
    if claim:
        cabecera += [f"> {claim}", "",
                     "*Es lo que declara su README. No es una verificación: está aquí porque es lo que "
                     "el autor dice de su propio programa, y eso también se mide con la fecha delante.*", ""]
    else:
        cabecera += ["Su README no tiene un párrafo en prosa que se pueda citar: o es una lista de "
                     "escudos, o son capturas, o no hay README. Se deja dicho en vez de rellenarlo.", ""]

    cuerpo = [
        "## Lo que se midió",
        "",
        bloque_medido(f),
        "",
        "## Cómo se consigue",
        "",
        bloque_instalacion(f),
        "",
        "## Qué no está verificado",
        "",
        "Que funcione. Se mide el repositorio; no se ha instalado ni usado.",
        "",
        "## Enlaces",
        "",
        f"- repositorio: https://github.com/{repo}",
    ]
    if f.get("web"):
        cuerpo.append(f"- su web: {f['web']}")
    if ent:
        cuerpo.append(f"- la última entrega: https://github.com/{repo}/releases/latest")
    cuerpo += ["", "---", "", "## Guía", "", INICIO, "", (guia if guia is not None else GUIA_PENDIENTE).strip(), "", FIN, ""]
    return "\n".join(cabecera + cuerpo)


def leer_guia(previo: str) -> str | None:
    m = re.search(re.escape(INICIO) + r"(.*?)" + re.escape(FIN), previo, re.S)
    return m.group(1).strip() if m else None


def escribir_indice(medido: dict) -> Path:
    por_racimo: dict[str, list[dict]] = {}
    for repo, f in medido.items():
        por_racimo.setdefault(f.get("racimo", "sin racimo"), []).append(f)

    lineas = ["# Catálogo de recursos", "",
              "Una ficha por recurso, con lo medido y, cuando la hay, la guía escrita a mano.",
              "Este índice lo genera `tools/catalogo_ficha.py`; no se edita.", ""]
    total = sum(len(v) for v in por_racimo.values())
    escritas = sum(1 for f in medido.values()
                   if (CATALOGO / slug(f["repo"]) / "FICHA.md").exists()
                   and INICIO in (CATALOGO / slug(f["repo"]) / "FICHA.md").read_text(encoding="utf-8")
                   and GUIA_PENDIENTE.split("\n")[0] not in (CATALOGO / slug(f["repo"]) / "FICHA.md").read_text(encoding="utf-8"))
    lineas += [f"**{total} recursos** en {len(por_racimo)} racimos · **{escritas} con guía escrita** · "
               f"el resto, medidos y esperando su guía.", ""]

    for racimo in sorted(por_racimo):
        fichas = sorted(por_racimo[racimo], key=lambda x: -(x.get("estrellas") or 0))
        vivas = sum(1 for x in fichas if estado(x) in ("vivo", "lento"))
        lineas += [f"## {racimo}", "",
                   f"{len(fichas)} recursos · {vivas} con movimiento en el último año · "
                   f"{sum(1 for x in fichas if x.get('archivado'))} archivados", "",
                   "```"]
        for f in fichas:
            marca = {"vivo": "●", "lento": "◐", "parado": "○", "archivado": "✕", "no contesta": "✕"}.get(estado(f), "?")
            lineas.append(f"{marca} {f['repo']:<44} ★{(f.get('estrellas') or 0):<7} {f.get('empujon','')}")
        lineas += ["```", "",
                   "● vivo (≤30 días) · ◐ lento (≤1 año) · ○ parado (>1 año) · ✕ archivado o sin respuesta", ""]

    destino = CATALOGO / "INDICE.md"
    destino.write_text("\n".join(lineas), encoding="utf-8")
    return destino


def main() -> int:
    if not MEDIDO.exists():
        sys.exit("falta catalogo/medido.json: ejecuta antes tools/catalogo_medir.py")
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    solo = sys.argv[sys.argv.index("--solo") + 1] if "--solo" in sys.argv else None

    creadas = actualizadas = conservadas = 0
    for repo, f in medido.items():
        if solo and f.get("racimo") != solo:
            continue
        carpeta = CATALOGO / slug(repo)
        carpeta.mkdir(parents=True, exist_ok=True)
        destino = carpeta / "FICHA.md"
        guia = None
        if destino.exists():
            guia = leer_guia(destino.read_text(encoding="utf-8"))
            texto = ficha(f, guia)
            if texto != destino.read_text(encoding="utf-8"):
                destino.write_text(texto, encoding="utf-8")
                actualizadas += 1
            else:
                conservadas += 1
        else:
            destino.write_text(ficha(f), encoding="utf-8")
            creadas += 1

    print(f"fichas: {creadas} creadas · {actualizadas} actualizadas · {conservadas} sin cambios")
    if "--indice" in sys.argv:
        p = escribir_indice(medido)
        print("índice escrito:", p.relative_to(RAIZ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
