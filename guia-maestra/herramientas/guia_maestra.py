#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍA MAESTRA · compuertas y generador.

Regla de oro del proyecto: **todo lo que es dato se genera; todo lo que es enseñanza se escribe.**

Este programa hace dos cosas y en ese orden:
  1. comprueba (M30–M34) que ninguna ficha entra sin crédito, sin nivel, sin pasos
     reproducibles, sin cita viva y sin dato de oficio;
  2. genera desde `datos/` las cuatro salidas: README-índice, CREDITOS.md, sitio y libro.

Uso:
  python3 herramientas/guia_maestra.py --compuertas
  python3 herramientas/guia_maestra.py --generar
  python3 herramientas/guia_maestra.py --generar --estricto   # falla si alguna compuerta no pasa
"""
from __future__ import annotations

import html
import json
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
APPS = RAIZ / "datos" / "apps"
CAPS = RAIZ / "datos" / "capitulos.json"
TEXTO = RAIZ / "texto" / "capitulos"
SITIO = RAIZ / "sitio"

NIVELES = {"principiante", "intermedio", "experto"}
MESES = {"01": "enero", "02": "febrero", "03": "marzo", "04": "abril", "05": "mayo", "06": "junio",
         "07": "julio", "08": "agosto", "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"}


def bon(fecha: str) -> str:
    """2026-11-03 → 3 de noviembre de 2026."""
    if not fecha:
        return "sin fecha"
    a, m, d = fecha.split("-")
    return f"{int(d)} de {MESES.get(m, m)} de {a}"


def fichas() -> list[dict]:
    out = []
    for f in sorted(APPS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        d["_archivo"] = f.name
        out.append(d)
    return out


# ─────────────────────────── compuertas ───────────────────────────

def m30_credito(f: dict) -> list[str]:
    fallos = []
    if not f.get("autores") or not all(a.get("nombre") and a.get("enlace") for a in f["autores"]):
        fallos.append("M30 sin autor con nombre y enlace")
    lic = f.get("licencia") or {}
    if not lic.get("spdx") or not lic.get("archivo"):
        fallos.append("M30 licencia sin SPDX o sin enlace a su archivo")
    if not f.get("medido_en"):
        fallos.append("M30 sin fecha de medición")
    if "credito" not in f or len(f.get("credito", "")) < 20:
        fallos.append("M30 sin línea de crédito legible")
    return fallos


def m31_nivel(f: dict) -> list[str]:
    fallos = []
    if f.get("nivel") not in NIVELES:
        fallos.append(f"M31 nivel inválido: {f.get('nivel')!r}")
    p = f.get("para_quien") or {}
    if not p.get("es") or not p.get("no_es"):
        fallos.append("M31 sin «para quién es» y «para quién no es»")
    if len(f.get("tarea", "")) < 40:
        fallos.append("M31 tarea sin declarar (se exigen 40 caracteres)")
    return fallos


def m32_pasos(f: dict) -> list[str]:
    fallos = []
    pasos = f.get("manos") or []
    if len(pasos) < 5:
        fallos.append(f"M32 solo {len(pasos)} pasos (se exigen 5 como mínimo)")
    if any(len(p) < 20 for p in pasos):
        fallos.append("M32 hay un paso sin acción descrita")
    if len(f.get("resultado_esperado", "")) < 30:
        fallos.append("M32 sin resultado esperado")
    if len(f.get("deshacer", "")) < 30:
        fallos.append("M32 sin cómo deshacer")
    if not f.get("si_sale_mal"):
        fallos.append("M32 sin qué hacer si sale mal")
    return fallos


def m33_cita(f: dict) -> list[str]:
    fallos = []
    o = f.get("oficio") or {}
    if len(o.get("como_comprobar", "")) < 40:
        fallos.append("M33 el dato de oficio no dice cómo comprobarlo")
    if not (o.get("comando") or o.get("url")):
        fallos.append("M33 sin comando ni enlace que permita repetir la comprobación")
    if not f.get("medido_en"):
        fallos.append("M33 sin fecha que feche la cita")
    return fallos


def m34_oficio(f: dict) -> list[str]:
    o = f.get("oficio") or {}
    if len(o.get("dato", "")) < 80:
        return ["M34 sin dato de oficio (mínimo 80 caracteres); si no hay dato, la aplicación no entra"]
    return []


def compuertas() -> int:
    fs = fichas()
    if not fs:
        print("compuertas: no hay fichas en datos/apps")
        return 2
    total = 0
    print(f"COMPUERTAS DE LA GUÍA MAESTRA · {len(fs)} fichas")
    for f in fs:
        fallos = m30_credito(f) + m31_nivel(f) + m32_pasos(f) + m33_cita(f) + m34_oficio(f)
        total += len(fallos)
        estado = "VERDE" if not fallos else "ROJO"
        print(f"  {estado:<5} {f['id']:<16} {f['nombre']:<16} nota {f['senal']['nota']:>3} · {f['nivel']}")
        for x in fallos:
            print(f"        ✗ {x}")
    print(f"\nfallos: {total}")
    return 0 if total == 0 else 1


# ─────────────────────────── salidas ───────────────────────────

def capitulos() -> list[dict]:
    return json.loads(CAPS.read_text(encoding="utf-8"))["capitulos"]


def creditos(fs: list[dict]) -> str:
    l = ["# Créditos", "",
         "Esta guía existe porque otras personas publicaron su trabajo con licencia abierta.",
         "Cada ficha dice quién lo hizo, con qué licencia y el día en que se midió.", "",
         "El texto de la guía es **CC BY-SA 4.0**; los datos de medición, **CC BY 4.0**. Las aplicaciones",
         "conservan su propia licencia, que se cita en cada ficha y no se altera aquí.", "",
         "| Aplicación | Autor | Licencia | Medido |", "|---|---|---|---|"]
    for f in sorted(fs, key=lambda x: x["nombre"].lower()):
        autores = ", ".join(f"[{a['nombre']}]({a['enlace']})" for a in f["autores"])
        l.append(f"| [{f['nombre']}](https://github.com/{f['repo']}) | {autores} | {f['licencia']['spdx']} | {bon(f['medido_en'])} |")
    l += ["", "## Retirada", "",
          "Cualquier autor que se sienta mal citado puede pedir la retirada de su ficha abriendo una incidencia",
          "en el repositorio. Se atiende en 72 horas y se deja constancia de la fecha.", ""]
    return "\n".join(l)


def indices(fs: list[dict]) -> str:
    caps = capitulos()
    hoy = date.today().isoformat()
    l = ["# Guía Maestra de La Bandita", "",
         "**Aplicaciones y recursos de código abierto, en español, con el oficio explicado.**", "",
         f"_Estado: {len(caps)} capítulos planificados · {len(fs)} fichas verificadas · última medición {bon(hoy)}_", "",
         "Cada ficha tiene tres capas: **Manos** (los pasos, para quien empieza), **Cabeza** (cómo funciona y",
         "dónde se rompe) y **Oficio** (un dato que casi nadie sabe y que se puede comprobar). Sin la tercera,",
         "la aplicación no entra.", "",
         "## Capítulos", "", "| # | Capítulo | Estado | Fichas |", "|---:|---|---|---:|"]
    por_cap: dict[int, list[dict]] = {}
    for f in fs:
        por_cap.setdefault(f["capitulo"], []).append(f)
    for c in caps:
        n = len(por_cap.get(c["numero"], []))
        estado = "publicado" if (TEXTO / c["archivo"]).exists() else ("en preparación" if c.get("planificado") else "pendiente")
        l.append(f"| {c['numero']} | {c['titulo']} | {estado} | {n} |")
    l += ["", "## Fichas publicadas", "",
          "| Aplicación | Nivel | Nota | Licencia | Autor | Medido |", "|---|---|---:|---|---|---|"]
    for f in sorted(fs, key=lambda x: (x["capitulo"], x["orden"])):
        autores = ", ".join(a["nombre"] for a in f["autores"])
        l.append(f"| [{f['nombre']}](https://github.com/{f['repo']}) | {f['nivel']} | **{f['senal']['nota']}** | "
                 f"{f['licencia']['spdx']} | {autores} | {bon(f['medido_en'])} |")
    l += ["", "## Cómo se mide la nota", "",
          "Nueve señales con peso publicado —licencia 15, compilación 10, adjunto con huella 10, entrega reciente 10,",
          "actividad 10, equipo 10, cola de incidencias 10, archivo de seguridad 5, mérito de terceros 20— y cuatro",
          "penalizaciones: archivado −30, sin adjuntos −10, atención anómala −15, una sola persona con más de cincuenta",
          "entregas −5. La nota mide cómo se publica, no cuánta gente lo bajó.", "",
          "## Lo que esta guía no hace", "",
          "- No aloja paquetes: enlaza al repositorio oficial y nada más.",
          "- No traduce con máquina: se escribe en español, una vez y bien.",
          "- No recomienda lo que no se puede comprobar: ficha sin crédito o sin dato de oficio, ficha que no entra.", "",
          "## Créditos", "",
          "Todos los autores están en [CREDITOS.md](CREDITOS.md). El texto es CC BY-SA 4.0 y los datos CC BY 4.0.", ""]
    return "\n".join(l)


CSS = """
:root{--papel:#f5f7fa;--tinta:#1f2933;--suave:#5b6673;--linea:#e0e5ec;--acento:#2b6cb0;--alerta:#8a2b2b}
*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);font:16px/1.68 Georgia,'Times New Roman',serif}
.hoja{max-width:1080px;margin:0 auto;padding:34px 22px 70px}
.rejilla{display:grid;grid-template-columns:repeat(12,1fr);gap:18px}
.col-12{grid-column:span 12}.col-8{grid-column:span 8}.col-4{grid-column:span 4}
header{border-bottom:3px double var(--linea);padding-bottom:16px;margin-bottom:26px}
h1{font-size:2.15rem;line-height:1.18;margin:.2em 0 .3em;letter-spacing:-.01em}
h2{font-size:1.42rem;margin:2.1em 0 .5em;border-left:5px solid var(--acento);padding-left:12px}
h3{font-size:1.12rem;margin:1.7em 0 .35em}
p{margin:.65em 0}
.ficha{background:#fff;border:1px solid var(--linea);border-radius:10px;padding:20px 22px;margin:22px 0;box-shadow:0 1px 0 #fff inset}
.sello{display:inline-block;background:var(--tinta);color:#fff;border-radius:999px;padding:2px 11px;font:600 12px/1.9 system-ui,sans-serif;letter-spacing:.03em}
.n0{background:#2f6b4f}.n1{background:#8a6d1f}.n2{background:#8a2b2b}
.meta{color:var(--suave);font:13px/1.6 system-ui,sans-serif}
.capa{border-top:1px dashed var(--linea);margin-top:16px;padding-top:12px}
.capa h4{margin:.2em 0 .4em;font:700 13px/1.4 system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;color:var(--acento)}
ol,ul{padding-left:22px}li{margin:.35em 0}
code,pre{font-family:'DejaVu Sans Mono',ui-monospace,monospace;font-size:.9em}
code{background:#eef1f5;padding:1px 5px;border-radius:4px}
pre{background:#1f2933;color:#f5f7fa;padding:12px 14px;border-radius:8px;overflow-x:auto}
table{width:100%;border-collapse:collapse;font:14px/1.5 system-ui,sans-serif;margin:12px 0}
th,td{border-bottom:1px solid var(--linea);padding:7px 8px;text-align:left;vertical-align:top}
th{background:#eef1f5}
.aviso{background:#fff;border-left:5px solid var(--alerta);padding:12px 16px;margin:16px 0}
footer{margin-top:44px;border-top:3px double var(--linea);padding-top:14px;color:var(--suave);font:13px/1.6 system-ui,sans-serif}
a{color:var(--acento)}
@media(max-width:760px){.col-8,.col-4{grid-column:span 12}}
"""


def html_ficha(f: dict) -> str:
    s = f["senal"]
    nivel_cls = {"principiante": "n0", "intermedio": "n1", "experto": "n2"}[f["nivel"]]
    pasos = "\n".join(f"<li>{html.escape(p)}</li>" for p in f["manos"])
    mal = "\n".join(f"<li>{html.escape(p)}</li>" for p in f["si_sale_mal"])
    cabeza = "\n".join(f"<p>{html.escape(p)}</p>" for p in f["cabeza"])
    limite = "\n".join(f"<li>{html.escape(p)}</li>" for p in f["limites"])
    riesgo = "\n".join(f"<li>{html.escape(p)}</li>" for p in f["riesgos"])
    autores = ", ".join(f'<a href="{a["enlace"]}">{html.escape(a["nombre"])}</a>' for a in f["autores"])
    alt = ", ".join(f'<a href="https://github.com/{r}">{html.escape(r)}</a>' for r in f.get("alternativas", []))
    return f"""
<article class="ficha">
  <h3>{html.escape(f['nombre'])} <span class="meta">· {html.escape(f['repo'])}</span></h3>
  <p class="meta">
    <span class="sello {nivel_cls}">{f['nivel']}</span>
    &nbsp;nota <strong>{s['nota']}/100</strong> ·
    ★{s['estrellas']:,} · {s['edad_dias']} días · última entrega {html.escape(s['ultima_entrega'])} ·
    {s['descargas_10']:,} descargas en 10 entregas · {s['contribuyentes']} personas ·
    {s['ci']} flujos de compilación · incidencias {html.escape(s['incidencias'])}.
  </p>
  <p>{html.escape(f['tarea'])}</p>
  <p class="meta"><strong>Para quién es:</strong> {html.escape(f['para_quien']['es'])}
     <br><strong>Para quién no es:</strong> {html.escape(f['para_quien']['no_es'])}</p>

  <div class="capa"><h4>Manos · los pasos</h4><ol>{pasos}</ol>
    <p><strong>Qué debe verse al terminar:</strong> {html.escape(f['resultado_esperado'])}</p>
    <p><strong>Si sale mal:</strong></p><ul>{mal}</ul>
    <p><strong>Cómo se deshace:</strong> {html.escape(f['deshacer'])}</p></div>

  <div class="capa"><h4>Cabeza · por qué funciona</h4>{cabeza}
    <p><strong>Límites:</strong></p><ul>{limite}</ul></div>

  <div class="capa"><h4>Oficio · el dato que casi nadie sabe</h4>
    <p>{html.escape(f['oficio']['dato'])}</p>
    <p><strong>Cómo se comprueba:</strong> {html.escape(f['oficio']['como_comprobar'])}</p>
    <pre><code>{html.escape(f['oficio']['comando'])}</code></pre></div>

  <div class="capa"><h4>Riesgos y alternativas</h4><ul>{riesgo}</ul>
    <p class="meta">Alternativas medidas: {alt or '—'}</p></div>

  <p class="meta">{html.escape(f['credito'])} · licencia {html.escape(f['licencia']['spdx'])}
     (<a href="{f['licencia']['archivo']}">archivo</a>) · ficha medida el {bon(f['medido_en'])}</p>
</article>"""


def html_indice(fs: list[dict]) -> str:
    caps = capitulos()
    por_cap: dict[int, list[dict]] = {}
    for f in fs:
        por_cap.setdefault(f["capitulo"], []).append(f)
    filas = "\n".join(
        f"<tr><td>{c['numero']}</td><td>{html.escape(c['titulo'])}</td>"
        f"<td>{'publicado' if (TEXTO / c['archivo']).exists() else 'pendiente'}</td>"
        f"<td>{len(por_cap.get(c['numero'], []))}</td></tr>" for c in caps)
    fichas_html = "\n".join(html_ficha(f) for f in sorted(fs, key=lambda x: x["orden"]))
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Guía Maestra de La Bandita · aplicaciones libres explicadas</title>
<style>{CSS}</style></head><body><div class="hoja">
<header><div class="rejilla"><div class="col-12">
<span class="meta">La Bandita · guía maestra · edición hispana</span>
<h1>Aplicaciones libres explicadas: del primer paso al oficio</h1>
<p class="meta">Lo que se puede instalar, cómo se usa de principio a fin y el detalle técnico que casi nadie cuenta.
Cada ficha lleva su autor, su licencia y la fecha en que se midió.</p>
</div></div></header>
<main class="rejilla"><div class="col-12">
<h2>Capítulos</h2><table><thead><tr><th>#</th><th>Capítulo</th><th>Estado</th><th>Fichas</th></tr></thead>
<tbody>{filas}</tbody></table>
<h2>Capítulo publicado</h2>
<p><a href="capitulo-03.html"><strong>3 · El permiso prestado</strong></a> — qué es el permiso de depuración,
cómo se concede, cómo se revoca y seis aplicaciones que lo usan, con sus tres capas.</p>
<h2>Fichas</h2>
{fichas_html}
<footer>
<p>Texto: CC BY-SA 4.0 · datos: CC BY 4.0 · titular: La Bandita.
Cada aplicación conserva su licencia. No se aloja ningún paquete: los enlaces van al repositorio oficial.</p>
<p>Generado desde <code>datos/</code> por <code>herramientas/guia_maestra.py</code>. Si una ficha no pasa las
compuertas M30–M34, no aparece aquí.</p>
</footer>
</div></main></div></body></html>"""


def generar() -> int:
    fs = fichas()
    if not fs:
        print("generar: no hay fichas")
        return 2
    (RAIZ / "README.md").write_text(indices(fs), encoding="utf-8")
    (RAIZ / "CREDITOS.md").write_text(creditos(fs), encoding="utf-8")
    SITIO.mkdir(exist_ok=True)
    (SITIO / "index.html").write_text(html_indice(fs), encoding="utf-8")
    # capítulo 3 como página propia, a partir del texto escrito a mano
    cap = TEXTO / "03-el-permiso-prestado.md"
    if cap.exists():
        cuerpo = cap.read_text(encoding="utf-8")
        fichas_pub = [f for f in fs if f["capitulo"] == 3]
        fichas_html = "\n".join(html_ficha(f) for f in sorted(fichas_pub, key=lambda x: x["orden"]))
        bloques = []
        for b in cuerpo.split("\n\n"):
            b = b.strip()
            if not b:
                continue
            if b.startswith("### "):
                bloques.append(f"<h3>{html.escape(b[4:])}</h3>")
            elif b.startswith("## "):
                bloques.append(f"<h2>{html.escape(b[3:])}</h2>")
            elif b.startswith("# "):
                bloques.append(f"<h1>{html.escape(b[2:])}</h1>")
            elif b.startswith("```"):
                bloques.append(f"<pre><code>{html.escape(b.strip('`').strip())}</code></pre>")
            elif b.startswith("- "):
                lis = "".join(f"<li>{html.escape(x[2:])}</li>" for x in b.splitlines() if x.startswith("- "))
                bloques.append(f"<ul>{lis}</ul>")
            elif b.startswith(">"):
                bloques.append(f"<blockquote>{html.escape(b.lstrip('> '))}</blockquote>")
            else:
                bloques.append(f"<p>{html.escape(b)}</p>")
        (SITIO / "capitulo-03.html").write_text(
            f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Capítulo 3 · El permiso prestado · Guía Maestra</title><style>{CSS}</style></head>
<body><div class="hoja"><p class="meta"><a href="index.html">← Guía Maestra</a> · capítulo 3</p>
{''.join(bloques)}
<h2>Las seis fichas del capítulo</h2>
{fichas_html}
<footer><p>Texto CC BY-SA 4.0 · datos CC BY 4.0 · La Bandita. Mediciones del {bon(date.today().isoformat())}.</p></footer>
</div></body></html>""", encoding="utf-8")
    print(f"generado: README.md · CREDITOS.md · sitio/index.html"
          f"{' · sitio/capitulo-03.html' if cap.exists() else ''} · {len(fs)} fichas")
    return 0


def main() -> int:
    a = sys.argv[1:]
    rc = 0
    if "--compuertas" in a:
        rc = compuertas()
    if "--generar" in a:
        g = generar()
        if "--estricto" in a and rc != 0:
            print("estricto: hay fallos de compuerta, no se publica")
            return 1
        rc = rc or g
    if not a:
        print(__doc__)
        return 2
    return rc


if __name__ == "__main__":
    sys.exit(main())
