#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el HTML único con las 262 publicaciones (114 WhatsApp + 148 Facebook)."""
import json, pathlib, re, html

RAIZ = pathlib.Path(__file__).resolve().parents[1] / 'Arena-Reimagined' / '01-PUBLICACIONES'
SALIDA = RAIZ / 'LAS-262-PUBLICACIONES-2026-11-01.html'
CANALES = [("whatsapp", "WhatsApp", "WhatsApp-dominicano-ES"), ("facebook", "Facebook", "Facebook-dominicano-ES")]
HOY = {"whatsapp": {"01-Tiendas-APK-legales-mods-reloj-2027-WhatsApp-La-Bandita-2026-10-31-dominicano-ES.md",
                   "02-El-mueble-de-los-tres-cajones-familia-Tachiyomi-servidores-y-archivo-WhatsApp-La-Bandita-2026-10-31-dominicano-ES.md"},
       "facebook": {"01-Tiendas-APK-legales-mods-reloj-2027-Facebook-La-Bandita-2026-10-31-dominicano-ES.md",
                   "02-El-barrio-cambio-de-gente-mueble-de-comics-Facebook-La-Bandita-2026-10-31-dominicano-ES.md"}}

def num(nombre):
    m = re.match(r"^(\d+)", nombre)
    return m.group(1) if m else "00"

def titulo(nombre):
    t = re.sub(r"-(WhatsApp|Facebook)-La-Bandita-.*$", "", nombre)
    t = re.sub(r"^\d+-", "", t).replace("-", " ").strip()
    return t[:120]

def fecha(nombre):
    m = re.search(r"-(\d{4}-\d{2}-\d{2})", nombre)
    return m.group(1) if m else ""

def bonito(f):
    if not f: return ""
    y,m,d = f.split("-")
    meses=["","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{int(d)} de {meses[int(m)]} de {y}"

piezas = []
for canal, etiqueta, carpeta in CANALES:
    for f in sorted((RAIZ/carpeta).glob("*.md")):
        if f.name.lower().startswith(("leeme","readme")): continue
        texto = f.read_text(encoding="utf-8")
        n = num(f.name)
        piezas.append({
            "canal": canal, "canalEtiqueta": etiqueta, "numero": n,
            "titulo": titulo(f.name), "archivo": f.name,
            "fecha": fecha(f.name), "fechaBonita": bonito(fecha(f.name)),
            "caracteres": len(texto), "texto": texto, "clave": canal + "/" + f.name,
            "nuevo": f.name in HOY[canal],
        })
piezas.sort(key=lambda p: (p["canal"], int(p["numero"]), p["titulo"]))
n_wa = sum(1 for p in piezas if p["canal"]=="whatsapp")
n_fb = sum(1 for p in piezas if p["canal"]=="facebook")
total_car = sum(p["caracteres"] for p in piezas)

def esc(t):
    return html.escape(t)

def a_html(t):
    t = esc(t)
    t = re.sub(r"\*\*([^*\n]{1,80})\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]{1,80})\*(?!\*)", r"<b>\1</b>", t)
    return t

datos = json.dumps([{k:v for k,v in p.items() if k not in ("texto",)} for p in piezas], ensure_ascii=False)
textos = json.dumps({p["clave"]: p["texto"] for p in piezas}, ensure_ascii=False).replace("</", "<\\/")

filas = []
for p in piezas:
    filas.append(
      f'<button class="fila{" nuevo" if p["nuevo"] else ""}" data-canal="{p["canal"]}" data-archivo="{esc(p["clave"])}" '
      f'data-busca="{esc((p["numero"]+" "+p["titulo"]+" "+p["canalEtiqueta"]).lower())}">'
      f'<span class="num">{esc(p["numero"])}</span>'
      f'<span class="tit">{esc(p["titulo"])}</span>'
      f'<span class="meta"><span class="chip {p["canal"]}">{p["canalEtiqueta"]}</span>'
      f'<span class="car">{p["caracteres"]:,}</span>'.replace(",", ".") +
      f'{"<span class=\'badge\'>reescrita hoy</span>" if p["nuevo"] else ""}</span></button>')

HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>La Bandita · las 262 publicaciones · 1 de noviembre de 2026</title>
<style>
  :root {{
    --tinta:#12100e; --papel:#faf6ee; --papel2:#f2ebdd; --linea:#d8ccb4;
    --acento:#8a1c1c; --acento2:#1f4e3d; --gris:#6b6153;
  }}
  * {{ box-sizing:border-box; }}
  html,body {{ margin:0; padding:0; background:var(--papel); color:var(--tinta); }}
  body {{ font-family: ui-serif, Georgia, "Times New Roman", serif; line-height:1.55; }}
  header.tope {{ background:var(--tinta); color:var(--papel); padding:22px 20px 18px; }}
  header.tope h1 {{ margin:0 0 6px; font-size:clamp(20px,3.4vw,32px); letter-spacing:.4px; }}
  header.tope .sub {{ color:#d8ccb4; font-size:14px; }}
  header.tope .cifras {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:14px; }}
  header.tope .cifra {{ background:#241f1a; border:1px solid #3a332b; border-radius:10px; padding:8px 12px; font-size:13px; }}
  header.tope .cifra b {{ font-size:18px; display:block; color:#fff; }}
  .aviso {{ background:var(--acento2); color:#f4efe2; padding:10px 20px; font-size:13.5px; }}
  .aviso b {{ color:#fff; }}
  .barra {{ position:sticky; top:0; z-index:20; background:var(--papel2); border-bottom:1px solid var(--linea);
            padding:10px 16px; display:flex; gap:10px; flex-wrap:wrap; align-items:center; }}
  .barra input[type=search] {{ flex:1 1 260px; padding:9px 12px; border:1px solid var(--linea); border-radius:9px;
            background:#fff; font:inherit; font-size:14px; min-width:180px; }}
  .barra .filtro {{ padding:8px 12px; border:1px solid var(--linea); background:#fff; border-radius:9px; cursor:pointer; font:inherit; font-size:13.5px; }}
  .barra .filtro.activo {{ background:var(--tinta); color:var(--papel); border-color:var(--tinta); }}
  .barra .cuenta {{ margin-left:auto; font-size:13px; color:var(--gris); }}
  main {{ display:grid; grid-template-columns:minmax(280px,380px) 1fr; gap:0; min-height:calc(100vh - 190px); }}
  nav.indice {{ border-right:1px solid var(--linea); max-height:calc(100vh - 120px); overflow:auto; padding:8px 8px 40px; background:#fffdf8; }}
  .fila {{ display:grid; grid-template-columns:auto 1fr; grid-template-areas:"num tit" "num meta"; gap:0 10px; width:100%;
           text-align:left; background:none; border:0; border-bottom:1px solid #eee5d3; padding:10px 8px; cursor:pointer; font:inherit; }}
  .fila:hover {{ background:#f7f1e3; }}
  .fila.sel {{ background:#efe6d2; box-shadow:inset 3px 0 0 var(--acento); }}
  .fila .num {{ grid-area:num; align-self:start; font-size:12px; color:var(--gris); font-variant-numeric:tabular-nums; padding-top:3px; min-width:26px; }}
  .fila .tit {{ grid-area:tit; font-size:14px; line-height:1.3; }}
  .fila .meta {{ grid-area:meta; display:flex; gap:8px; align-items:center; flex-wrap:wrap; margin-top:4px; font-size:11.5px; color:var(--gris); }}
  .chip {{ border-radius:999px; padding:1px 8px; font-size:11px; border:1px solid; }}
  .chip.whatsapp {{ color:#0d5c3a; border-color:#0d5c3a; }}
  .chip.facebook {{ color:#123a6b; border-color:#123a6b; }}
  .badge {{ background:var(--acento); color:#fff; border-radius:999px; padding:1px 8px; font-size:10.5px; }}
  section.lector {{ padding:22px 26px 80px; max-width:860px; }}
  section.lector h2 {{ font-size:clamp(18px,2.4vw,26px); margin:0 0 4px; }}
  section.lector .datos {{ font-size:12.5px; color:var(--gris); margin-bottom:18px; }}
  section.lector .datos code {{ background:#f0e8d6; padding:1px 6px; border-radius:5px; }}
  pre.pieza {{ white-space:pre-wrap; word-wrap:break-word; font-family:inherit; font-size:15.5px; line-height:1.62;
               background:none; border:0; padding:0; margin:0; }}
  .portada {{ padding:26px 26px 10px; max-width:860px; }}
  .portada h2 {{ margin:0 0 8px; font-size:22px; }}
  .portada p {{ font-size:15px; color:#2b2620; }}
  .tabla {{ width:100%; border-collapse:collapse; font-size:13.5px; margin:14px 0 8px; }}
  .tabla th, .tabla td {{ border-bottom:1px solid var(--linea); padding:6px 8px; text-align:left; vertical-align:top; }}
  .tabla th {{ background:#f0e8d6; }}
  .nota {{ font-size:13px; color:var(--gris); }}
  @media (max-width:820px) {{
    main {{ grid-template-columns:1fr; }}
    nav.indice {{ max-height:42vh; border-right:0; border-bottom:1px solid var(--linea); }}
    section.lector {{ padding:18px 16px 60px; }}
  }}
</style>
</head>
<body>
<header class="tope">
  <h1>La Bandita · las {len(piezas)} publicaciones</h1>
  <div class="sub">Archivo completo en un solo archivo · domingo 1 de noviembre de 2026 · Santo Domingo (UTC-4)</div>
  <div class="cifras">
    <div class="cifra"><b>{n_wa}</b>de WhatsApp</div>
    <div class="cifra"><b>{n_fb}</b>de Facebook</div>
    <div class="cifra"><b>{len(piezas)}</b>publicaciones</div>
    <div class="cifra"><b>{total_car//1000}.{total_car%1000:03d}</b>caracteres en total</div>
    <div class="cifra"><b>4</b>reescritas hoy desde cero</div>
    <div class="cifra"><b>10.019</b>archivos sellados</div>
  </div>
</header>
<div class="aviso">Hecho hoy, con medición del día: <b>4 piezas reescritas enteras</b> (01 y 02 de los dos canales) con <b>repositorios nuevos de los últimos nueve meses</b> — RepoStore, ShizuStore, AppManagerNG, universal-installer, InstallerX-Revived, Yokai, Usagi, Chimahon, Ciallo Reader, Yomihon, manga-tui, LocalViewer y más — y con los <b>cebos de junio de 2026</b> señalados con nombre y fecha. Lo que no se midió está dicho como no medido.</div>
<div class="barra">
  <input type="search" id="q" placeholder="Buscar por número, título o canal…" autocomplete="off">
  <button class="filtro activo" data-f="todas">Todas</button>
  <button class="filtro" data-f="whatsapp">WhatsApp</button>
  <button class="filtro" data-f="facebook">Facebook</button>
  <button class="filtro" id="soloNuevas">Reescritas hoy</button>
  <span class="cuenta" id="cuenta"></span>
</div>
<main>
  <nav class="indice" id="indice">
    {''.join(filas)}
  </nav>
  <div id="panel">
    <div class="portada" id="portada">
      <h2>Cómo se lee este archivo</h2>
      <p>Están las <b>{len(piezas)} publicaciones</b> de los dos canales, íntegras, tal como se escribieron, cada una con su número, su canal y su longitud real en caracteres. El buscador filtra por número o por título; los botones filtran por canal; «Reescritas hoy» deja solo las cuatro que se hicieron de nuevo el 1 de noviembre de 2026.</p>
      <p class="nota">Las 258 restantes se conservan tal cual, con la fecha que llevan dentro. No se han retocado para que parezcan frescas: si una pieza es del 15 de septiembre, lo dice. Mezclar datos de días anteriores con los de hoy sería exactamente el problema que este archivo denuncia.</p>
      <h2 style="margin-top:22px">Las cuatro reescritas hoy</h2>
      <table class="tabla">
        <tr><th>Pieza</th><th>Caracteres</th><th>Repos medidos</th><th>Qué trae de nuevo</th></tr>
        <tr><td><b>01 WhatsApp</b></td><td>63.093</td><td>31</td><td>Trece puertas nacidas en 2025-2026, el cementerio de los cebos del 28-jun-2026 y «cómo se lee una lista de hace cuatro meses»</td></tr>
        <tr><td><b>01 Facebook</b></td><td>42.740</td><td>22</td><td>Escena del que copió una lista vieja, doce casas (seis nuevas) y dieciséis apps donde la fecha de la release no es la del proyecto</td></tr>
        <tr><td><b>02 WhatsApp</b></td><td>63.094</td><td>56</td><td>Censo de dieciocho proyectos que no existían hace nueve meses, servidores que no son Suwayomi y los cebos con su fecha</td></tr>
        <tr><td><b>02 Facebook</b></td><td>42.249</td><td>56</td><td>Pieza nueva entera: seis escenas de mudanza, tutorial de doce pasos, archivo, sincronización y ficha de 49 repos con fecha de nacimiento</td></tr>
      </table>
      <p class="nota">Fuentes nuevas usadas hoy para descubrir: búsquedas de la API de GitHub con filtro de empuje posterior al 1 de agosto de 2026, más <code>fmhy.net</code>, <code>appteka.store</code> y los repositorios de los mismos autores. Todo lo citado se midió uno por uno con la API: estrellas, licencia declarada, fecha de creación, último empuje y última release.</p>
    </div>
  </div>
</main>
<script>
const PIEZAS = {datos};
const TEXTOS = {textos};
const panel = document.getElementById('panel');
const indice = document.getElementById('indice');
const cuenta = document.getElementById('cuenta');
let filtroCanal = 'todas', soloNuevas = false, q = '';

function esc(s) {{ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }}
function aHtml(t) {{
  return esc(t)
    .replace(/\\*\\*([^*\\n]{{1,80}})\\*\\*/g, '<b>$1</b>')
    .replace(/(^|[^*])\\*([^*\\n]{{1,80}})\\*(?!\\*)/g, '$1<b>$2</b>');
}}
function abrir(archivo) {{
  const meta = PIEZAS.find(p => p.clave === archivo);
  if (!meta) return;
  const texto = TEXTOS[archivo] || '';
  panel.innerHTML = '<section class="lector"><h2>Pieza ' + esc(meta.numero) + ' · ' + esc(meta.titulo) + '</h2>'
    + '<div class="datos">' + esc(meta.canalEtiqueta) + ' · ' + meta.caracteres.toLocaleString('es-DO') + ' caracteres · '
    + 'fecha del archivo: ' + esc(meta.fechaBonita || 'sin fecha en el nombre') + ' · <code>' + esc(meta.archivo) + '</code></div>'
    + '<pre class="pieza">' + aHtml(texto) + '</pre></section>';
  document.querySelectorAll('.fila').forEach(b => b.classList.toggle('sel', b.dataset.archivo === archivo));
  indice.querySelector('.fila.sel')?.scrollIntoView({{block:'nearest'}});
  panel.scrollIntoView({{block:'start'}});
}}
function aplicar() {{
  let n = 0;
  document.querySelectorAll('.fila').forEach(b => {{
    const okCanal = filtroCanal === 'todas' || b.dataset.canal === filtroCanal;
    const okNueva = !soloNuevas || b.classList.contains('nuevo');
    const okQ = !q || b.dataset.busca.includes(q);
    const ver = okCanal && okNueva && okQ;
    b.style.display = ver ? '' : 'none';
    if (ver) n++;
  }});
  cuenta.textContent = n + ' de ' + PIEZAS.length + ' publicaciones';
}}
document.getElementById('q').addEventListener('input', e => {{ q = e.target.value.trim().toLowerCase(); aplicar(); }});
document.querySelectorAll('.filtro[data-f]').forEach(b => b.addEventListener('click', () => {{
  document.querySelectorAll('.filtro[data-f]').forEach(x => x.classList.remove('activo'));
  b.classList.add('activo'); filtroCanal = b.dataset.f; aplicar();
}}));
document.getElementById('soloNuevas').addEventListener('click', e => {{
  soloNuevas = !soloNuevas; e.target.classList.toggle('activo', soloNuevas); aplicar();
}});
indice.addEventListener('click', e => {{
  const b = e.target.closest('.fila'); if (b) abrir(b.dataset.archivo);
}});
aplicar();
</script>
</body>
</html>
"""
SALIDA.parent.mkdir(parents=True, exist_ok=True)
SALIDA.write_text(HTML, encoding="utf-8")
print(f"escrito {SALIDA} · {len(HTML):,} caracteres · {len(piezas)} publicaciones ({n_wa} WA + {n_fb} FB)")
