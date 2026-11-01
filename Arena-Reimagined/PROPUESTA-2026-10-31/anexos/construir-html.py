#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye la presentación web autocontenida de la propuesta.

Sin CDN, sin fuentes externas, sin imágenes externas: solo CSS, SVG inline y JS propio.
Lee PROPUESTA-LA-BANDITA-EMPRESA.md y escribe propuesta-la-bandita.html.
"""
import html, re, unicodedata
from pathlib import Path
import mistune

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "PROPUESTA-LA-BANDITA-EMPRESA.md"
DESTINO = RAIZ / "propuesta-la-bandita.html"

ETIQUETAS = {
    "0": "Resumen", "1": "Diagnóstico", "2": "Mercado", "3": "Ofertas",
    "4": "Economía", "5": "Arquitectura", "6": "MCP", "7": "Gobernanza",
    "8": "Plan", "9": "Riesgos", "10": "Métricas", "11": "Decisiones", "12": "Anexos",
}

def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "seccion"

md = mistune.create_markdown(plugins=["table", "strikethrough"], escape=False)

def convertir(texto: str) -> str:
    salida = md(texto)
    # tablas desplazables sin romper el flujo
    salida = salida.replace("<table>", '<div class="tabla-wrap"><table>').replace("</table>", "</table></div>")
    return salida

fuente = ORIGEN.read_text(encoding="utf-8")
partes = re.split(r"^## ", fuente, flags=re.M)
preambulo = partes[0]
secciones = []
for p in partes[1:]:
    lineas = p.split("\n", 1)
    titulo = lineas[0].strip()
    cuerpo = lineas[1] if len(lineas) > 1 else ""
    secciones.append((titulo, cuerpo))

# id estable y etiqueta corta de navegación
nav, cuerpos = [], []
for i, (titulo, cuerpo) in enumerate(secciones):
    if not re.match(r"\d+\.", titulo):   # solo secciones numeradas: la portada vive en el HTML
        continue
    numero = re.match(r"(\d+)", titulo)
    clave = numero.group(1) if numero else ""
    sid = f"s-{clave}" if clave else slug(titulo)
    etiqueta = ETIQUETAS.get(clave) or titulo.split(":")[0][:24]
    limpio = re.sub(r"^\d+\.\s*", "", titulo)
    nav.append((sid, etiqueta, limpio))
    cuerpos.append(f'<section class="tarjeta" id="{sid}">'
                   f'<h2><span class="num">{clave.zfill(2) if clave else "··"}</span>{html.escape(limpio)}</h2>'
                   f'{convertir(cuerpo)}</section>')

# bloque de portada propio (no depende del markdown de cabecera)
portada = """
<header class="hero" id="inicio">
  <div class="hero-glow" aria-hidden="true"></div>
  <p class="eyebrow">Propuesta ejecutiva · corte medido el 31 de octubre de 2026</p>
  <h1>La Bandita<br><span class="grad">de archivo verificado<br>a empresa de verificación</span></h1>
  <p class="lead">El repositorio ya tiene lo que casi nadie tiene: 261 publicaciones con fecha,
  un registro de 6.826 repositorios medidos y un método que detecta sus propios errores.
  Lo que no tiene es empresa. Esta es la propuesta para construirla sin traicionar el método.</p>
  <div class="kpis">
    <div class="kpi"><b>259</b><span>publicaciones vivas</span></div>
    <div class="kpi"><b>6.826</b><span>repos medidos</span></div>
    <div class="kpi"><b>701</b><span>recursos mapeados</span></div>
    <div class="kpi"><b>53.886</b><span>servidores MCP</span></div>
    <div class="kpi"><b>9</b><span>compuertas</span></div>
    <div class="kpi"><b>78,8 %</b><span>sin licencia declarada</span></div>
  </div>
  <div class="aviso">
    <svg class="ico" viewBox="0 0 24 24"><path d="M12 3 3 20h18L12 3zm0 5v6m0 3v.5"/></svg>
    <p><b>Lo que se pide:</b> cinco decisiones del dueño (licencia, marca, canal, patrocinio y servidor MCP)
    y autorización del primer trimestre. <b>Inversión de infraestructura:</b> menos de US$10 al mes en fase 1.
    <b>Riesgo principal:</b> seguir igual.</p>
  </div>
  <nav class="chips" aria-label="Índice">
    CHIPS
  </nav>
</header>
"""
chips = "".join(f'<a class="chip" href="#{sid}">{html.escape(et)}</a>' for sid, et, _ in nav)
portada = portada.replace("CHIPS", chips)

navlateral = "".join(
    f'<a class="nav-item" href="#{sid}" data-target="{sid}"><i aria-hidden="true"></i>{html.escape(et)}</a>'
    for sid, et, _ in nav)
CORTOS = {"Resumen": "Inicio", "Diagnóstico": "Datos", "Arquitectura": "Diseño",
          "MCP": "MCP", "Plan": "Plan", "Decisiones": "Decidir"}
navmovil = "".join(
    f'<a class="mnav-item" href="#{sid}" data-target="{sid}">{html.escape(CORTOS.get(et, et[:9]))}</a>'
    for sid, et, _ in nav if et in CORTOS)

CSS = Path(Path(__file__).parent / "estilo.css").read_text(encoding="utf-8")
JS = Path(Path(__file__).parent / "app.js").read_text(encoding="utf-8")

documento = f"""<!DOCTYPE html>
<html lang="es-DO" data-paleta="cana">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="dark light">
<meta name="description" content="Propuesta ejecutiva de La Bandita: de archivo verificado a empresa de verificación. Corte medido el 31 de octubre de 2026.">
<title>La Bandita · Propuesta empresarial 2026</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="progreso" id="progreso" aria-hidden="true"></div>

<header class="barra">
  <a class="marca" href="#inicio">
    <svg class="logo" viewBox="0 0 32 32" aria-hidden="true">
      <path class="l1" d="M16 2 29 9v14L16 30 3 23V9z"/>
      <path class="l2" d="M16 9.5 23 13v8l-7 3.5L9 21v-8z"/>
      <circle class="l3" cx="16" cy="17" r="3"/>
    </svg>
    <span class="marca-txt"><b>LA BANDITA</b><small>propuesta 2026</small></span>
  </a>
  <div class="barra-acciones">
    <button class="boton" id="buscarBtn" aria-label="Buscar en la propuesta">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m16.5 16.5 4 4"/></svg>
    </button>
    <button class="boton" id="sonidoBtn" aria-label="Sonido de interfaz" aria-pressed="false">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9h3l4-3v12l-4-3H4z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg>
    </button>
    <div class="paletas">
      <button class="boton" id="paletaBtn" aria-label="Cambiar paleta" aria-expanded="false">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="8" r="1.6"/><circle cx="8.4" cy="13" r="1.6"/><circle cx="15.6" cy="13" r="1.6"/></svg>
      </button>
      <div class="paleta-menu" id="paletaMenu" role="menu">
        <button data-paleta="cana"><i style="--c:#17c98a"></i>Caña esmeralda</button>
        <button data-paleta="malecon"><i style="--c:#3fa9ff"></i>Malecón</button>
        <button data-paleta="azucar"><i style="--c:#f2b23c"></i>Azúcar</button>
        <button data-paleta="fogata"><i style="--c:#ff5f3c"></i>Fogata</button>
        <button data-paleta="tinta"><i style="--c:#b8c4d4"></i>Tinta</button>
        <button data-paleta="amoled"><i style="--c:#e8eef7"></i>Amoled</button>
      </div>
    </div>
    <span class="sello">31 · 10 · 2026</span>
  </div>
</header>

<div class="buscador" id="buscador" hidden>
  <input id="buscarInput" type="search" placeholder="Buscar en la propuesta…" autocomplete="off">
  <span class="cuenta" id="buscarCuenta">0</span>
  <button id="buscarCerrar" aria-label="Cerrar búsqueda">✕</button>
</div>

<div class="marco">
  <aside class="lateral">
    <p class="lateral-titulo">Secciones</p>
    {navlateral}
    <div class="lateral-pie">
      <p>Documento autocontenido: sin CDN, sin fuentes externas, sin imágenes remotas.</p>
    </div>
  </aside>
  <main class="contenido" id="contenido">
    {portada}
    {''.join(cuerpos)}
    <footer class="pie">
      <div class="firma">
        <svg class="logo" viewBox="0 0 32 32" aria-hidden="true">
          <path class="l1" d="M16 2 29 9v14L16 30 3 23V9z"/>
          <path class="l2" d="M16 9.5 23 13v8l-7 3.5L9 21v-8z"/>
          <circle class="l3" cx="16" cy="17" r="3"/>
        </svg>
        <p><b>La Bandita</b> · verifica antes de recomendar — y ahora también antes de vender.<br>
        Corte 31 de octubre de 2026 · repositorio <span class="mono">Alex17273747576777/la-bandita-archivo</span></p>
      </div>
      <div class="metadatos">
        <span class="pill">HTML autocontenido</span>
        <span class="pill">Cero CDN</span>
        <span class="pill">Cifras medidas, no estimadas</span>
      </div>
    </footer>
  </main>
</div>

<nav class="mnav" aria-label="Secciones principales">
  {navmovil}
</nav>

<script>
{JS}
</script>
</body>
</html>
"""

DESTINO.write_text(documento, encoding="utf-8")
kb = DESTINO.stat().st_size / 1024
print(f"OK · {DESTINO.name} · {kb:.1f} KB · {len(secciones)} secciones · "
      f"CDN externos: {documento.count('http') - documento.count('https://github.com') } enlaces (solo contenido)")
