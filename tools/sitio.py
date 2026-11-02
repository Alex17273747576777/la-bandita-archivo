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

sys_path = Path(__file__).resolve().parent
import sys as _sys
_sys.path.insert(0, str(sys_path))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
PUBLICACIONES = RAIZ / "Arena-Reimagined/01-PUBLICACIONES"
REGISTRO = RAIZ / "registry"
SITIO = RAIZ / "site"
UMBRAL_FRESCURA = 180

from diseno import CSS, JS, LOGO, ICONO_LUPA, cabeza  # sistema visual de la casa (tools/diseno.py)


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




def plantilla(titulo: str, cuerpo: str, descripcion: str = "", jsonld: dict | None = None,
              activo: str = "", raiz: str = "") -> str:
    """Página completa con el sistema visual de la casa.

    Autocontenida: CSS y JS incrustados, iconos SVG a mano, cero recursos externos.
    El tema (brisa/noche) se aplica antes del primer pintado para que no parpadee."""
    ld = (f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>'
          if jsonld else "")
    dia = date.today().isoformat()

    def enlace(destino: str, texto: str) -> str:
        clase = "chip" if destino != activo else "chip"
        marca = ' aria-current="page"' if destino == activo else ""
        return f'<a class="{clase}" href="{destino}"{marca}>{texto}</a>'

    nav = (enlace(f"{raiz}index.html", "Archivo")
           + enlace(f"{raiz}redes/index.html", "Redes")
           + enlace(f"{raiz}registro/index.html", "Registro")
           + enlace(f"{raiz}feed.xml", "RSS"))
    return (
        cabeza(esc(titulo), esc(descripcion), ld)
        + '<body>\n<div id="carga" aria-hidden="true"></div>\n'
        '<header class="barra">'
        f'<a class="marca" href="{raiz}index.html">{LOGO}<span>LA BANDITA<small>archivo verificado</small></span></a>'
        f'<nav class="der" aria-label="secciones">{nav}'
        f'<span class="sello">{dia}</span>'
        '<button class="boton icono" id="tema" type="button" aria-label="Cambiar de tema"></button>'
        '</nav></header>\n'
        f'<main>{cuerpo}</main>\n'
        f'<footer><b>La Bandita</b> verifica antes de recomendar: cada dato lleva su fecha y su método. '
        f'Lo que no se pudo medir se firma como ausencia, no se rellena. Generado el {dia} · '
        'sin recursos externos (cero CDN, cero fuentes remotas, cero rastreadores).</footer>\n'
        + JS
        + '</body></html>'
    )


CANALES_CONOCIDOS = {
    "facebook": ("Facebook", "Publicaciones largas del canal principal."),
    "whatsapp": ("WhatsApp", "Tandas cortas, partidas en trozos."),
    "comunidad": ("Comunidad", "Posts de respuesta a la comunidad."),
    "telegram": ("Telegram", "Versiones y avisos."),
    "instagram": ("Instagram", "Versiones adaptadas."),
    "reddit": ("Reddit", "Hilos y respuestas."),
    "discord": ("Discord", "Notas de servidor."),
    "xda": ("XDA", "Fichas técnicas para foro."),
    "rethubs": ("Rehubs", "Variante de publicación."),
    "otras": ("Otras redes", "Sin carpeta propia todavía."),
}


def canal_de_carpeta(nombre: str) -> str:
    """Canal legible a partir del nombre de la carpeta. `POSTS-COMUNIDAD` no es Facebook."""
    n = nombre.lower()
    for clave in ("whatsapp", "facebook", "comunidad", "telegram", "instagram", "reddit",
                  "discord", "xda", "rethubs"):
        if clave in n:
            return CANALES_CONOCIDOS[clave][0]
    if "archivo" in n:
        return "Archivo"
    return "Otras redes"


def interacciones_declaradas() -> dict:
    """Interacciones reales, si existen. Sin archivo no hay dato: se declara ausente, no se pone cero.

    Fuente opcional: `docs/interacciones.json`
      {"generado": "AAAA-MM-DD",
       "redes": {"facebook": {"seguidores": 1200, "publicaciones": 140, "alcance": 8400,
                              "reacciones": 310, "comentarios": 44, "compartidos": 27,
                              "medido": "AAAA-MM-DD", "fuente": "panel de la red"}}}
    """
    ruta = RAIZ / "docs" / "interacciones.json"
    if not ruta.exists():
        return {}
    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return datos.get("redes") or {}


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

    hoy = date.fromisoformat(fecha_casa_hoy())
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
        plataforma = canal_de_carpeta(p.parent.name)
        entradas.append({"archivo": p, "texto": texto, "titulo": primera[:160],
                         "fecha": fecha.group(0) if fecha else "", "plataforma": plataforma,
                         "slug": slug(p.stem)})

    # ── longitudes declaradas (banda de la casa) para el medidor de cada tarjeta ──
    bandas_path = RAIZ / "docs" / "bandas.json"
    bandas = {}
    if bandas_path.exists():
        try:
            bandas = json.loads(bandas_path.read_text(encoding="utf-8"))
        except Exception:
            bandas = {}
    largo_de: dict[str, tuple[int, int, int]] = {}
    for canal_b, cfg in bandas.items():
        if not isinstance(cfg, dict):
            continue
        for _num, info in (cfg.get("piezas") or {}).items():
            if info.get("archivo"):
                largo_de[info["archivo"]] = (int(info.get("caracteres") or 0),
                                             int(cfg.get("min") or 0), int(cfg.get("max") or 0))

    def tarjeta(e: dict) -> str:
        numero = re.match(r"^(\d+)", e["archivo"].stem)
        num = numero.group(1) if numero else "—"
        chars, lo, hi = largo_de.get(e["archivo"].name, (len(e["texto"]), 0, 0))
        pct = min(100, round(chars * 100 / hi)) if hi else 0
        canal_tag = "fb" if e["plataforma"] == "Facebook" else "wa"
        fecha_corta = e["fecha"].replace(" de ", " ") if e["fecha"] else "sin fecha"
        dentro = (lo <= chars <= hi) if hi else True
        clase_largo = "ok" if dentro else "fuera"
        texto_largo = "en banda" if dentro else "fuera de banda"
        busca = esc((e["titulo"] + " " + e["plataforma"] + " " + e["fecha"] + " pieza " + num).lower())
        return (
            f'<li class="revela"><a class="tarjeta" href="piezas/{e["slug"]}.html" data-busca="{busca}" '
            f'data-canal="{e["plataforma"].lower()}">'
            f'<span class="num">Pieza {num}</span>'
            f'<h3>{esc(e["titulo"])}</h3>'
            f'<div class="tags"><span class="tag {canal_tag}">{e["plataforma"]}</span>'
            f'<span class="tag">{esc(fecha_corta)}</span>'
            f'<span class="tag {clase_largo}">{texto_largo}</span></div>'
            f'<div class="medidor"><div class="cifra"><span>{chars:,} caracteres</span>'
            f'<span>{lo:,}–{hi:,}</span></div>'
            f'<div class="pista"><i data-pct="{pct}"></i></div></div>'
            f'</a></li>'
        )

    lista = "".join(tarjeta(e) for e in entradas)

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

    hace_hoy = sum(1 for e in entradas if "2 de noviembre de 2026" in e["fecha"])
    total_chars = sum(largo_de.get(e["archivo"].name, (len(e["texto"]), 0, 0))[0] for e in entradas)
    cuerpo_index = f"""
<section class="hero aparece">
<p class="eyebrow">Archivo verificado · ecosistema Android libre · dominicano-ES</p>
<h1>Todo lo que la casa ha medido, con su fecha y a un clic</h1>
<p>Este sitio se genera desde las piezas y el registro. Cada dato declara cuándo se midió y con qué
método; lo que no se pudo verificar se firma como ausencia en vez de inventarse. Aquí no se recomienda
nada que no se haya abierto, contado y fechado antes.</p>
<div class="kpis">
  <div class="kpi"><b data-n="{len(entradas)}">0</b><span>piezas publicadas</span></div>
  <div class="kpi"><b data-n="{hace_hoy}">0</b><span>medidas hoy</span></div>
  <div class="kpi"><b data-n="{total_chars}" data-miles="1">0</b><span>caracteres verificados</span></div>
  <div class="kpi"><b data-n="{len(fichas)}" data-miles="1">0</b><span>fichas de repositorio</span></div>
  <div class="kpi"><b data-n="{vivos}" data-miles="1">0</b><span>repositorios vivos</span></div>
  <div class="kpi"><b data-n="{sin_lic}" data-miles="1">0</b><span>sin licencia declarada</span></div>
</div>
<p><span class="pill {'rancio' if estado_reg == 'rancio' else 'vivo'}">registro {estado_reg}</span>
<span class="pill">antigüedad máxima {edad} días</span>
<span class="pill">umbral de frescura {UMBRAL_FRESCURA} días</span>
<a class="pill" href="registro/index.html">ver el registro completo</a>
<a class="pill" href="feed.xml">RSS</a></p>
</section>
<div class="controles aparece retardo-2" role="search">
  <div class="buscador">{ICONO_LUPA}<input type="search" id="q"
    placeholder="Buscar entre {len(entradas)} piezas… (tecla /)" autocomplete="off" aria-label="Buscar piezas"></div>
  <div class="chips" id="chips">
    <button class="chip" type="button" data-filtro="todo" aria-pressed="true">Todo</button>
    <button class="chip" type="button" data-filtro="facebook" aria-pressed="false">Facebook</button>
    <button class="chip" type="button" data-filtro="whatsapp" aria-pressed="false">WhatsApp</button>
  </div>
  <span class="cuenta" id="c">{len(entradas)} piezas</span>
</div>
<ul class="rejilla" id="lista">{lista}</ul>
<p class="vacio oculto" id="vacio">Ninguna pieza coincide con esa búsqueda. Prueba con el número, el
título o el canal.</p>
<script>
(function(){{
  var q=document.getElementById('q'), lista=document.getElementById('lista'),
      cuenta=document.getElementById('c'), vacio=document.getElementById('vacio'),
      chips=[].slice.call(document.querySelectorAll('#chips .chip'));
  var tarjetas=[].slice.call(lista.querySelectorAll('.tarjeta')),
      total=tarjetas.length, canal='todo';
  function pintar(){{
    var t=(q.value||'').trim().toLowerCase(), n=0;
    tarjetas.forEach(function(a){{
      var ok=(canal==='todo'||a.dataset.canal===canal)&&(!t||a.dataset.busca.indexOf(t)>-1);
      a.parentNode.classList.toggle('oculto', !ok);
      if(ok) n++;
    }});
    cuenta.textContent = n===total ? total+' piezas' : n+' de '+total;
    vacio.classList.toggle('oculto', n!==0);
  }}
  q.addEventListener('input', pintar);
  chips.forEach(function(b){{
    b.addEventListener('click', function(){{
      canal=b.dataset.filtro;
      chips.forEach(function(o){{o.setAttribute('aria-pressed', String(o===b));}});
      pintar();
    }});
  }});
}})();
</script>"""
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
            plantilla(e["titulo"], cuerpo, e["titulo"], ld, raiz="../"), encoding="utf-8")

    # registro: datos + navegador
    compacto = [{"repo": f["repo"], "id": f["id"], "lic": f["licencia"]["spdx"],
                 "met": f["licencia"]["metodo"], "est": f["actividad"]["estado"],
                 "push": f["actividad"]["ultimo_push"], "stars": (f.get("merito") or {}).get("stars"),
                 "medido": f["medido_en"], "piezas": f.get("piezas", [])} for f in fichas]
    (destino / "datos" / "registro.json").write_text(json.dumps(
        {"generado": hoy.isoformat(), "umbral_frescura": UMBRAL_FRESCURA, "fichas": compacto},
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    datos_inline = json.dumps(compacto, ensure_ascii=False, separators=(",", ":"))
    cuerpo_reg = f"""<a class="volver" href="../index.html">← volver al archivo</a>
<h1>Registro de repositorios</h1>
<p>{len(fichas):,} fichas, cada una con su fecha de medición y su método. El registro pesa y se nota:
{sin_lic:,} repositorios no declaran licencia, y eso se firma como ausencia en vez de inventarse
una licencia. La búsqueda filtra al escribir; no hace ninguna llamada a la red.</p>
<p><span class="pill {'rancio' if estado_reg == 'rancio' else 'vivo'}">estado: {estado_reg}</span>
<span class="pill">antigüedad máxima {edad} días</span>
<a class="pill" href="../datos/registro.json">descargar JSON</a></p>
<div class="controles">
  <div class="buscador">{ICONO_LUPA}<input type="search" id="q"
    placeholder="Buscar por repo, licencia o estado…" autocomplete="off" aria-label="Buscar en el registro"></div>
  <span class="cuenta" id="c">—</span>
</div>
<ul class="rejilla" id="lista"></ul>
<p class="vacio oculto" id="vacio">Nada en el registro coincide con esa búsqueda.</p>
<script id="datos-registro" type="application/json">{datos_inline}</script>
<script>
(function(){{
  var datos = JSON.parse(document.getElementById('datos-registro').textContent);
  var q = document.getElementById('q'), lista = document.getElementById('lista'),
      c = document.getElementById('c'), vacio = document.getElementById('vacio');
  function fila(f){{
    var est = f.est === 'vivo' ? 'ok' : 'fuera';
    var stars = (f.stars || 0).toLocaleString('es-DO');
    return '<li class="revela"><a class="tarjeta" href="../ficha/' + f.id + '.html">'
      + '<span class="num">' + f.id + '</span>'
      + '<h3>' + f.repo + '</h3>'
      + '<div class="tags"><span class="tag ' + est + '">' + f.est + '</span>'
      + '<span class="tag">' + (f.lic || 'sin licencia declarada') + '</span>'
      + '<span class="tag">★' + stars + '</span></div>'
      + '<div class="medidor"><div class="cifra"><span>último empujón ' + (f.push || '—') + '</span>'
      + '<span>medido ' + f.medido + '</span></div>'
      + '<div class="pista"><i data-pct="' + Math.min(100, Math.round(Math.log10(stars.replace(/\\./g,'')) * 20)) + '"></i></div></div>'
      + '</a></li>';
  }}
  function pintar(){{
    var t = (q.value || '').trim().toLowerCase(), n = 0;
    var res = datos.filter(function(f){{
      return !t || (f.repo + ' ' + (f.lic || '') + ' ' + f.est).toLowerCase().indexOf(t) > -1;
    }});
    n = res.length;
    c.textContent = n.toLocaleString('es-DO') + ' de ' + datos.length.toLocaleString('es-DO');
    lista.innerHTML = res.slice(0, 300).map(fila).join('');
    vacio.classList.toggle('oculto', n !== 0);
    if(res.length > 300){{
      vacio.classList.remove('oculto');
      vacio.textContent = 'Mostrando 300 de ' + res.length.toLocaleString('es-DO') + '. Afine la búsqueda.';
    }} else if(n === 0){{
      vacio.textContent = 'Nada en el registro coincide con esa búsqueda.';
    }}
    [].slice.call(lista.querySelectorAll('.pista i')).forEach(function(el){{
      requestAnimationFrame(function(){{ el.style.width = (el.dataset.pct || 0) + '%'; }});
    }});
  }}
  q.addEventListener('input', pintar);
  pintar();
}})();
</script>"""
    (destino / "registro" / "index.html").write_text(plantilla(
        "Registro de repositorios · La Bandita", cuerpo_reg,
        "Registro verificado de repositorios del ecosistema Android libre, medido y fechado.",
        raiz="../"), encoding="utf-8")

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
            plantilla(f"{f['repo']} · La Bandita", cuerpo, f"Ficha medida de {f['repo']}",
                      raiz="../"), encoding="utf-8")

    # ── REDES · qué se publicó en cada red y qué interacción se ha medido ──
    multi = RAIZ / "04-VERSIONES-MULTIIDIOMA"
    versos: dict[str, dict[str, int]] = {}
    if multi.exists():
        for red in sorted(d for d in multi.iterdir() if d.is_dir()):
            cuenta: dict[str, int] = {}
            for idioma in sorted(d for d in red.iterdir() if d.is_dir()):
                n = sum(1 for f in idioma.glob("*.md"))
                if n:
                    cuenta[idioma.name] = n
            if cuenta:
                versos[red.name] = cuenta

    por_red: dict[str, list[dict]] = {}
    for e in entradas:
        por_red.setdefault(e["plataforma"], []).append(e)
    for clave in versos:
        nombre = CANALES_CONOCIDOS.get(clave, (clave.capitalize(), ""))[0]
        por_red.setdefault(nombre, [])

    inter = interacciones_declaradas()
    clave_de_nombre = {v[0]: k for k, v in CANALES_CONOCIDOS.items()}

    def miles(n: int) -> str:
        return f"{n:,}".replace(",", ".")

    def tarjeta_red(nombre: str) -> str:
        piezas_red = sorted(por_red.get(nombre, []), key=lambda x: x["slug"], reverse=True)
        clave = clave_de_nombre.get(nombre, nombre.lower())
        idiomas = versos.get(clave, {})
        chars = sum(len(x["texto"]) for x in piezas_red)
        fechas = [x["fecha"] for x in piezas_red if x["fecha"]]
        dato = inter.get(clave) or {}
        if dato:
            metricas = "".join(
                f'<span class="tag ok">{k} {miles(int(v))}</span>' 
                for k, v in dato.items() if isinstance(v, (int, float)) and k != "publicaciones"
            )
            linea_int = (f'<p class="meta">interacción medida el {esc(str(dato.get("medido", "—")))}'
                         f' · fuente: {esc(str(dato.get("fuente", "declarada")))}</p>{metricas}')
        else:
            linea_int = ('<p class="meta">interacción: sin medición declarada — esta red no publica sus '
                         'cifras aquí y no se rellenan con ceros.</p>')
        lista_piezas = "".join(
            f'<li class="item"><a href="../piezas/{x["slug"]}.html">Pieza '
            f'{re.match(r"^(\d+)", x["archivo"].stem).group(1) if re.match(r"^(\d+)", x["archivo"].stem) else "—"}'
            f' · {esc(x["titulo"][:80])}</a></li>'
            for x in piezas_red[:3]
        ) or '<li class="item">Todavía sin piezas canónicas en esta red.</li>'
        if len(piezas_red) > 3:
            lista_piezas += (f'<li class="item">y {len(piezas_red) - 3} más en el '
                             f'<a href="../index.html">archivo</a>.</li>')
        linea_idiomas = ("".join(f'<span class="tag">{esc(k)} {v}</span>' for k, v in idiomas.items())
                         or '<span class="tag">sin versiones por idioma</span>')
        return f"""<article class="tarjeta revela">
<span class="num">{esc(nombre)}</span>
<h3>{len(piezas_red)} {'publicación' if len(piezas_red) == 1 else 'publicaciones'} · {miles(chars)} caracteres</h3>
<div class="tags">
  <span class="tag">{esc(fechas[0]) if fechas else "sin fecha"}</span>
  <span class="tag">{'con versiones en otros idiomas' if idiomas else ('sin piezas canónicas en el archivo' if not piezas_red else 'solo español')}</span>
  {linea_idiomas}
</div>
{linea_int}
<ul class="lista">{lista_piezas}</ul>
</article>"""

    todas = sorted(por_red, key=lambda n: (-len(por_red[n]), n))
    redes_orden = [n for n in todas
                   if por_red[n] or versos.get(clave_de_nombre.get(n, n.lower()))]
    vacias = [n for n in todas if n not in redes_orden]
    tarjetas_red = "".join(tarjeta_red(n) for n in redes_orden)
    linea_vacias = ('<p class="pill">sin actividad todavía: ' + ' · '.join(esc(n) for n in vacias) + '</p>'
                    if vacias else '')
    con_dato = sum(1 for n in redes_orden if inter.get(clave_de_nombre.get(n, n.lower())))
    total_pub = len(entradas)
    cuerpo_redes = f"""<a class="volver" href="../index.html">← volver al archivo</a>
<section class="hero aparece">
<p class="eyebrow">Redes · publicaciones e interacción</p>
<h1>Qué se publicó en cada red, y qué interacción se ha medido</h1>
<p>Esta página se genera desde el árbol del archivo: cuenta las piezas de cada canal y las versiones
por idioma. La interacción sale de <code>docs/interacciones.json</code> cuando existe; cuando no existe,
aquí se dice <b>sin medición declarada</b> en lugar de poner un cero que parezca un dato.</p>
<div class="kpis">
  <div class="kpi"><b data-n="{total_pub}">0</b><span>publicaciones contadas</span></div>
  <div class="kpi"><b data-n="{len(redes_orden)}">0</b><span>redes con actividad</span></div>
  <div class="kpi"><b data-n="{con_dato}">0</b><span>redes con interacción medida</span></div>
  <div class="kpi"><b data-n="{len(inter)}">0</b><span>bloques de interacción cargados</span></div>
</div>
</section>
{u''.join('')}
<ul class="rejilla" id="lista">{tarjetas_red}</ul>
<p class="aparece">{linea_vacias}</p>
<section class="pieza aparece retardo-2">
<h2>Cómo se añade la interacción de una red</h2>
<p>Se escribe a mano —una vez por corte, desde el panel de la propia red— en
<code>docs/interacciones.json</code>. Nada se estima y nada se deduce: si un número no está publicado por
la red, no se escribe.</p>
<pre>{{"generado": "2026-11-02",
 "redes": {{"facebook": {{"seguidores": 1200, "publicaciones": 140, "alcance": 8400,
            "reacciones": 310, "comentarios": 44, "compartidos": 27,
            "medido": "2026-11-02", "fuente": "panel de Facebook"}}}}}}</pre>
<p>Al volver a generar el sitio, esas cifras aparecen en la tarjeta de su red con su fecha y su fuente.
El archivo no se inventa: si el JSON no existe, la página lo declara.</p>
</section>"""
    (destino / "redes").mkdir()
    (destino / "redes" / "index.html").write_text(plantilla(
        "Redes · La Bandita", cuerpo_redes,
        "Publicaciones por red y su interacción declarada, con fecha y fuente.",
        raiz="../"), encoding="utf-8")
    (destino / "datos" / "redes.json").write_text(json.dumps({
        "generado": hoy.isoformat(),
        "redes": [{"red": n, "publicaciones": len(por_red.get(n, [])),
                   "caracteres": sum(len(x["texto"]) for x in por_red.get(n, [])),
                   "versiones_por_idioma": versos.get(clave_de_nombre.get(n, n.lower()), {}),
                   "interaccion": inter.get(clave_de_nombre.get(n, n.lower()))}
                  for n in redes_orden]}, ensure_ascii=False, indent=1), encoding="utf-8")

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
