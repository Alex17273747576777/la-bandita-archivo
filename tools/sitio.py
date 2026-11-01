#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SITIO · genera el sitio estático de La Bandita desde las piezas y el registro.

Principios (los mismos del módulo de referencia, corregidos):
  · autocontenido: cero CDN, cero fuentes remotas, iconos SVG a mano;
  · una URL por pieza y por ficha: el archivo deja de ser un solo HTML de 1 MB;
  · cada dato con su fecha; nada se presenta como fresco si no lo es;
  · RSS y JSON-LD para que una máquina entienda qué se afirma y cuándo.

Uso: python3 tools/sitio.py [--salida site] [--limite N]
Salida: index.html, piezas/, registro/, ficha/, feed.xml, datos/registro.json
"""
from __future__ import annotations
import argparse, html, json, re, shutil, unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PUBLICACIONES = RAIZ / "Arena-Reimagined/01-PUBLICACIONES"
REGISTRO = RAIZ / "registry"
SITIO = RAIZ / "site"
UMBRAL_FRESCURA = 180

CSS = """
:root{--r2:12px;--r3:18px;--r4:24px;--acc:#17c98a;--acc2:#8df2c6;--acc-rgb:23,201,138;
--bg:#050b09;--bg2:#08130f;--texto:#e8eef6;--texto2:#c3d0dd;--apagado:#8ea0b2;
--sup:rgba(255,255,255,.04);--borde:rgba(255,255,255,.085)}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(900px 500px at 80% -8%,rgba(0,255,178,.09),transparent 60%),
linear-gradient(175deg,var(--bg2),var(--bg) 60%);color:var(--texto);
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.72;font-size:16.5px}
a{color:var(--acc2);text-decoration:none}a:hover{text-decoration:underline}
.barra{position:sticky;top:0;z-index:20;display:flex;align-items:center;justify-content:space-between;
gap:14px;padding:12px clamp(14px,3vw,28px);background:rgba(6,10,12,.82);
-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);border-bottom:1px solid var(--borde)}
.marca{display:flex;gap:10px;align-items:center;color:inherit;font-weight:700;letter-spacing:.14em;font-size:14px}
.marca small{display:block;font-weight:400;letter-spacing:.12em;font-size:10px;color:var(--apagado);text-transform:uppercase}
main{max-width:980px;margin:0 auto;padding:clamp(18px,3vw,34px) clamp(14px,3vw,28px) 90px}
h1{font-size:clamp(26px,4.4vw,42px);line-height:1.1;letter-spacing:-.02em;margin:.2em 0 .5em}
h2{font-size:clamp(19px,2.4vw,25px);letter-spacing:-.015em;margin:1.6em 0 .5em}
h3{font-size:15.5px;color:var(--acc2);margin:1.4em 0 .4em}
p,li{color:var(--texto2)}strong{color:#fff}
.hero{padding:26px 0 8px}
.eyebrow{font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin:0 0 12px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:18px 0}
.kpi{background:var(--sup);border:1px solid var(--borde);border-radius:var(--r3);padding:13px 15px}
.kpi b{display:block;font-family:ui-monospace,monospace;font-size:23px;color:var(--acc2);line-height:1.1}
.kpi span{font-size:11.5px;color:var(--apagado)}
.buscador{display:flex;gap:8px;margin:14px 0}
input[type=search]{flex:1;padding:11px 14px;border-radius:var(--r2);border:1px solid var(--borde);
background:rgba(255,255,255,.04);color:var(--texto);font:inherit;font-size:15px;outline:none}
input[type=search]:focus{border-color:rgba(var(--acc-rgb),.6);box-shadow:0 0 0 3px rgba(var(--acc-rgb),.14)}
.cuenta{font-family:ui-monospace,monospace;font-size:12px;color:var(--acc2);align-self:center;min-width:74px;text-align:right}
.lista{display:grid;gap:9px;margin:16px 0;padding:0;list-style:none}
.item{display:block;padding:13px 15px;border:1px solid var(--borde);border-radius:var(--r2);background:var(--sup)}
.item:hover{border-color:rgba(var(--acc-rgb),.5);text-decoration:none}
.item b{display:block;color:var(--texto);font-size:14.6px;font-weight:600;line-height:1.35}
.item small{display:block;color:var(--apagado);font-size:11.6px;margin-top:3px}
.ficha{background:var(--sup);border:1px solid var(--borde);border-radius:var(--r3);padding:14px 16px;margin:12px 0}
.ficha dl{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;margin:8px 0 0;font-size:14px}
.ficha dt{color:var(--apagado);font-size:12px;text-transform:uppercase;letter-spacing:.08em}
.ficha dd{margin:0;color:var(--texto)}
.pill{display:inline-block;font-size:11px;padding:3px 9px;border-radius:99px;border:1px solid var(--borde);
color:var(--apagado);margin:2px 4px 2px 0}
.pill.vivo{color:var(--acc2);border-color:rgba(var(--acc-rgb),.45)}
.pill.rancio{color:#ffb46b;border-color:rgba(255,180,107,.45)}
.pieza p{color:var(--texto2);margin:0 0 13px}
.pieza h2{color:var(--texto);border-top:1px solid var(--borde);padding-top:18px}
.pieza .meta{font-size:12.5px;color:var(--apagado);margin-bottom:18px}
pre{background:#04070a;border:1px solid var(--borde);border-radius:var(--r2);padding:14px;overflow-x:auto;font-size:12.6px}
code{font-family:ui-monospace,monospace;font-size:.88em;background:rgba(var(--acc-rgb),.12);
color:var(--acc2);padding:.1em .35em;border-radius:5px}
table{width:100%;border-collapse:collapse;font-size:13.6px;margin:12px 0}
th{text-align:left;font-size:10.6px;letter-spacing:.12em;text-transform:uppercase;color:var(--acc2);
border-bottom:1px solid rgba(var(--acc-rgb),.3);padding:8px 10px}
td{padding:8px 10px;border-bottom:1px solid rgba(255,255,255,.055);color:var(--texto2)}
footer{margin-top:40px;padding-top:18px;border-top:1px solid var(--borde);font-size:12.5px;color:var(--apagado)}
.volver{font-size:12.6px;color:var(--apagado)}
mark{background:rgba(var(--acc-rgb),.38);color:#fff;border-radius:3px}
"""


def titulo_de(texto: str, respaldo: str) -> str:
    """Título presentable: primera línea con letras, sin la numeración de la casa
    (el número vive en el archivo, no en el titular — regla D-003). No altera el cuerpo."""
    for linea in texto.split("\n"):
        limpio = linea.strip().strip("*#").strip()
        letras = re.sub(r"[^A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", "", limpio)
        if len(letras) < 12:
            continue
        limpio = re.sub(r"^Publicaci[oó]n\s+\d+\s*[—–:-]\s*", "", limpio, flags=re.I)
        limpio = re.sub(r"\s+", " ", limpio).strip("*# ").strip()
        if len(limpio) >= 12:
            return limpio[:160]
    return respaldo[:160]


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()[:120] or "pieza"


def esc(t: str) -> str:
    return html.escape(t, quote=False)


def md_a_html(texto: str) -> str:
    """Convertidor mínimo: encabezados, listas, tablas, código, énfasis y párrafos."""
    salida, en_lista, en_tabla, en_codigo = [], False, False, False
    for linea in texto.split("\n"):
        if linea.startswith("```"):
            en_codigo = not en_codigo
            salida.append("</pre>" if not en_codigo else "<pre>")
            continue
        if en_codigo:
            salida.append(esc(linea))
            continue
        if re.match(r"^\s*\|.*\|\s*$", linea):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in celdas):
                continue
            if not en_tabla:
                salida.append("<table>")
                en_tabla = True
                salida.append("<tr>" + "".join(f"<th>{esc(c)}</th>" for c in celdas) + "</tr>")
            else:
                salida.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in celdas) + "</tr>")
            continue
        if en_tabla:
            salida.append("</table>")
            en_tabla = False
        m = re.match(r"^(#{1,6})\s+(.*)$", linea)
        if m:
            if en_lista:
                salida.append("</ul>")
                en_lista = False
            n = max(2, len(m.group(1)))
            salida.append(f"<h{n}>{formato(m.group(2))}</h{n}>")
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", linea)
        if m:
            if not en_lista:
                salida.append("<ul>")
                en_lista = True
            salida.append(f"<li>{formato(m.group(1))}</li>")
            continue
        if en_lista:
            salida.append("</ul>")
            en_lista = False
        if not linea.strip():
            continue
        if linea.startswith(">"):
            salida.append(f"<blockquote>{formato(linea.lstrip('> '))}</blockquote>")
            continue
        salida.append(f"<p>{formato(linea)}</p>")
    if en_lista:
        salida.append("</ul>")
    if en_tabla:
        salida.append("</table>")
    if en_codigo:
        salida.append("</pre>")
    return "\n".join(salida)


def formato(t: str) -> str:
    t = esc(t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"(?<![\"'>])(https?://[^\s<)]+)", r'<a href="\1">\1</a>', t)
    return t


LOGO = ('<svg width="28" height="28" viewBox="0 0 32 32" aria-hidden="true">'
        '<path d="M16 2 29 9v14L16 30 3 23V9z" fill="none" stroke="#17c98a" stroke-width="1.4"/>'
        '<path d="M16 9.5 23 13v8l-7 3.5L9 21v-8z" fill="rgba(23,201,138,.16)" stroke="#8df2c6" stroke-width="1.1"/>'
        '<circle cx="16" cy="17" r="3" fill="#17c98a"/></svg>')


def plantilla(titulo: str, cuerpo: str, descripcion: str = "", jsonld: dict | None = None) -> str:
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="es-DO"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{esc(descripcion)}">
<title>{esc(titulo)}</title>{ld}
<style>{CSS}</style></head>
<body>
<header class="barra"><a class="marca" href="/index.html">{LOGO}<span>LA BANDITA<small>archivo verificado</small></span></a>
<span class="pill">{date.today().isoformat()}</span></header>
<main>{cuerpo}</main>
<footer>La Bandita verifica antes de recomendar · cada dato con su fecha · generado el {date.today().isoformat()}
sin recursos externos (cero CDN, cero fuentes remotas).</footer>
</body></html>"""


def cargar_fichas() -> list[dict]:
    salida = []
    for p in sorted(REGISTRO.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            salida.append(json.loads(p.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    return salida


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(SITIO))
    ap.add_argument("--limite", type=int, default=0, help="limita piezas (pruebas)")
    args = ap.parse_args()
    destino = Path(args.salida)
    if destino.exists():
        shutil.rmtree(destino)
    (destino / "piezas").mkdir(parents=True)
    (destino / "registro").mkdir()
    (destino / "ficha").mkdir()
    (destino / "datos").mkdir()

    hoy = date.today()
    fichas = cargar_fichas()
    piezas = sorted(p for p in PUBLICACIONES.rglob("*.md")
                    if not p.name.lower().startswith(("leeme", "readme")))
    if args.limite:
        piezas = piezas[: args.limite]

    # índice de piezas
    entradas = []
    for p in piezas:
        texto = p.read_text(encoding="utf-8", errors="replace")
        primera = titulo_de(texto, p.stem)
        fecha = re.search(r"\d{1,2} de \w+ de 20\d\d", texto)
        plataforma = "WhatsApp" if "whatsapp" in p.parent.name.lower() else "Facebook"
        entradas.append({"archivo": p, "texto": texto, "titulo": primera[:160],
                         "fecha": fecha.group(0) if fecha else "", "plataforma": plataforma,
                         "slug": slug(p.stem)})

    lista = "".join(
        f'<li><a class="item" href="piezas/{e["slug"]}.html" data-busca="{esc((e["titulo"] + " " + e["plataforma"]).lower())}">'
        f'<b>{esc(e["titulo"])}</b><small>{e["plataforma"]} · {esc(e["fecha"] or "sin fecha en el cuerpo")}</small></a></li>'
        for e in entradas)

    # conteos del registro
    vivos = sum(1 for f in fichas if f["actividad"]["estado"] == "vivo")
    sin_lic = sum(1 for f in fichas if f["licencia"]["metodo"] == "ausencia-firmada")
    edades = []
    for f in fichas:
        try:
            edades.append((hoy - date.fromisoformat(f["medido_en"])).days)
        except Exception:
            pass
    edad = max(edades) if edades else 0
    estado_reg = "rancio" if edad > UMBRAL_FRESCURA else "vigente"

    cuerpo_index = f"""
<section class="hero">
<p class="eyebrow">Archivo verificado · ecosistema Android libre · dominicano-ES</p>
<h1>Todo lo que la casa ha medido, con su fecha y a un clic</h1>
<p>Este sitio se genera desde las piezas y el registro. Cada dato declara cuándo se midió y con qué
método; lo que no se pudo verificar se firma como ausencia en vez de inventarse.</p>
<div class="kpis">
  <div class="kpi"><b>{len(entradas)}</b><span>piezas publicadas</span></div>
  <div class="kpi"><b>{len(fichas):,}</b><span>fichas de repositorio</span></div>
  <div class="kpi"><b>{vivos:,}</b><span>repositorios vivos</span></div>
  <div class="kpi"><b>{sin_lic:,}</b><span>sin licencia declarada</span></div>
  <div class="kpi"><b>{edad}</b><span>días de antigüedad del dato</span></div>
</div>
<p><span class="pill {'rancio' if estado_reg == 'rancio' else 'vivo'}">registro {estado_reg}</span>
<span class="pill">umbral de frescura {UMBRAL_FRESCURA} días</span>
<a class="pill" href="registro/index.html">ver el registro completo</a>
<a class="pill" href="feed.xml">RSS</a></p>
</section>
<div class="buscador">
  <input type="search" id="q" placeholder="Buscar en las {len(entradas)} piezas…" autocomplete="off">
  <span class="cuenta" id="c">{len(entradas)}</span>
</div>
<ul class="lista" id="lista">{lista}</ul>"""
    (destino / "index.html").write_text(plantilla(
        "La Bandita · archivo verificado", cuerpo_index,
        "Archivo verificado del ecosistema Android libre en español dominicano, con fecha y evidencia en cada dato.",
        {"@context": "https://schema.org", "@type": "WebSite", "name": "La Bandita",
         "description": "Archivo verificado del ecosistema Android libre", "inLanguage": "es-DO"}), encoding="utf-8")

    # páginas por pieza
    for e in entradas:
        cuerpo = f"""<a class="volver" href="../index.html">← volver al archivo</a>
<div class="pieza"><h1>{esc(e['titulo'])}</h1>
<p class="meta">{e['plataforma']} · {esc(e['fecha'] or 'fecha no declarada')} · {len(e['texto']):,} caracteres</p>
{md_a_html(e['texto'])}</div>"""
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": e["titulo"],
              "inLanguage": "es-DO", "author": {"@type": "Organization", "name": "La Bandita"},
              "datePublished": e["fecha"] or None, "publisher": {"@type": "Organization", "name": "La Bandita"}}
        (destino / "piezas" / f"{e['slug']}.html").write_text(
            plantilla(e["titulo"], cuerpo, e["titulo"], ld), encoding="utf-8")

    # registro: datos + navegador
    compacto = [{"repo": f["repo"], "id": f["id"], "lic": f["licencia"]["spdx"],
                 "met": f["licencia"]["metodo"], "est": f["actividad"]["estado"],
                 "push": f["actividad"]["ultimo_push"], "stars": (f.get("merito") or {}).get("stars"),
                 "medido": f["medido_en"], "piezas": f.get("piezas", [])} for f in fichas]
    (destino / "datos" / "registro.json").write_text(json.dumps(
        {"generado": hoy.isoformat(), "umbral_frescura": UMBRAL_FRESCURA, "fichas": compacto},
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    cuerpo_reg = f"""<a class="volver" href="../index.html">← volver al archivo</a>
<h1>Registro de repositorios</h1>
<p>{len(fichas):,} fichas medidas el 15 de octubre de 2026 contra la API oficial de GitHub.
El registro pesa y se nota: {sin_lic:,} repositorios no declaran licencia (firmado como ausencia,
no inventado como licencia).</p>
<p><span class="pill {'rancio' if estado_reg == 'rancio' else 'vivo'}">estado: {estado_reg}</span>
<span class="pill">edad máxima {edad} días</span>
<a class="pill" href="../datos/registro.json">descargar JSON</a></p>
<div class="buscador"><input type="search" id="q" placeholder="Buscar por repo, licencia o estado…" autocomplete="off">
<span class="cuenta" id="c">—</span></div>
<ul class="lista" id="lista"></ul>
<script>
let datos = null;
fetch('../datos/registro.json').then(r=>r.json()).then(d=>{{datos=d.fichas; pintar('');}}).catch(()=>{{}});
const q=document.getElementById('q'), lista=document.getElementById('lista'), c=document.getElementById('c');
function pintar(txt){{
  if(!datos) return; const a=txt.trim().toLowerCase();
  const res = a ? datos.filter(f=>(f.repo+' '+(f.lic||'')+' '+f.est).toLowerCase().includes(a)) : datos;
  c.textContent = res.length.toLocaleString('es-DO') + ' de ' + datos.length.toLocaleString('es-DO');
  lista.innerHTML = res.slice(0,300).map(f=>`<li><a class="item" href="../ficha/${{f.id}}.html">
    <b>${{f.repo}}</b><small>${{f.est}} · ${{f.lic||'sin licencia declarada'}} · ★${{(f.stars||0).toLocaleString('es-DO')}} ·
    último push ${{f.push||'—'}} · medido ${{f.medido}}</small></a></li>`).join('')
    + (res.length>300 ? `<li class="item"><small>Mostrando 300 de ${{res.length.toLocaleString('es-DO')}}. Afine la búsqueda.</small></li>` : '');
}}
q.addEventListener('input',e=>pintar(e.target.value));
</script>"""
    (destino / "registro" / "index.html").write_text(plantilla(
        "Registro de repositorios · La Bandita", cuerpo_reg,
        "Registro verificado de repositorios del ecosistema Android libre, medido y fechado."), encoding="utf-8")

    # fichas con piezas asociadas: página propia
    con_piezas = [f for f in fichas if f.get("piezas")]
    for f in con_piezas:
        edad_f = (hoy - date.fromisoformat(f["medido_en"])).days if f.get("medido_en") else -1
        cuerpo = f"""<a class="volver" href="../registro/index.html">← volver al registro</a>
<h1>{esc(f['repo'])}</h1>
<div class="ficha"><dl>
<dt>medido</dt><dd>{esc(f['medido_en'])} ({edad_f} días) ·
  <span class="pill {'rancio' if edad_f > UMBRAL_FRESCURA else 'vivo'}">{'rancio' if edad_f > UMBRAL_FRESCURA else 'vigente'}</span></dd>
<dt>licencia</dt><dd>{esc(str(f['licencia']['spdx'] or 'sin licencia declarada'))} · método {esc(f['licencia']['metodo'])}</dd>
<dt>actividad</dt><dd>{esc(f['actividad']['estado'])} · último push {esc(str(f['actividad']['ultimo_push']))}</dd>
<dt>estrellas</dt><dd>{esc(str((f.get('merito') or {}).get('stars')))}</dd>
<dt>fuente</dt><dd>{esc(f['fuente']['primaria'])} · {esc(f['fuente']['metodo'])}</dd>
<dt>evidencia</dt><dd><code>{esc(f['evidencia']['sha256'][:32])}…</code> · {esc(f['evidencia'].get('payload_ref',''))}</dd>
</dl></div>
<h2>Piezas donde aparece</h2><ul class="lista">{''.join(f'<li class="item"><b>{esc(p)}</b></li>' for p in f['piezas'][:12])}</ul>"""
        (destino / "ficha" / f"{f['id']}.html").write_text(
            plantilla(f"{f['repo']} · La Bandita", cuerpo, f"Ficha medida de {f['repo']}"), encoding="utf-8")

    # RSS
    items = "".join(f"""<item><title>{esc(e['titulo'])}</title>
<link>piezas/{e['slug']}.html</link><guid>piezas/{e['slug']}.html</guid>
<category>{e['plataforma']}</category><description>{esc(e['texto'][:280])}</description></item>"""
                    for e in entradas[:40])
    (destino / "feed.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>La Bandita</title>
<description>Archivo verificado del ecosistema Android libre en español dominicano</description>
<link>index.html</link><language>es-DO</language>{items}</channel></rss>""", encoding="utf-8")

    peso = sum(p.stat().st_size for p in destino.rglob("*") if p.is_file())
    print(f"sitio generado: {len(entradas)} piezas · {len(con_piezas)} fichas con página · "
          f"{len(fichas)} fichas en el navegador · {peso/1048576:.1f} MB · cero CDN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
