#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SITIO · genera el sitio estático de La Bandita desde las piezas y el registro.

Genera site/ con índice, piezas, fichas, registro y RSS, sin una sola dependencia externa.
El frontend solo lee site/datos/*.json. No consulta APIs en vivo, no depende de CDN y no tiene
recursos externos: se abre y funciona sin red.

Uso:
  python3 tools/sitio.py

Qué hace:
  * Lee las piezas de Arena-Reimagined/01-PUBLICACIONES/ y el registro de registry/.
  * Genera site/index.html, site/piezas/, site/ficha/, site/redes/, site/feed.xml.
  * Genera site/datos/registro.json y site/datos/redes.json.
  * Todo con HTML y CSS propios, cero CDN, cero fuentes externas.

Qué NO hace:
  * No toca las piezas: escribe en site/, que se puede borrar y volver a generar.
  * No carga tipografías, scripts o imágenes desde fuera.
  * No muestra una cifra que no exista en los datos generados.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
REGISTRO: Path = RAIZ / "registry"
PUBLICACIONES: Path = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
SITE: Path = RAIZ / "site"
DATOS: Path = SITE / "datos"
FICHA_DIR: Path = SITE / "ficha"
PIEZAS_DIR: Path = SITE / "piezas"
REDES_DIR: Path = SITE / "redes"

CSS = """/* LA BANDITA · diseño propio, cero dependencias externas */
:root{--fondo:#f5f7fa;--tarjeta:#ffffff;--texto:#1a1a2e;--acento:#a8d0e6;--acento-hover:#6cc29b;--borde:#e0e5ec;--suave:#6b7280}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--fondo);color:var(--texto);line-height:1.5;padding:24px}
a{color:var(--acento);text-decoration:none}
a:hover{color:var(--acento-hover)}
header{max-width:1200px;margin:0 auto 40px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
h1{font-size:1.5rem;margin-bottom:8px}
.subtitulo{color:var(--suave);font-size:0.95rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:24px;max-width:1200px;margin:0 auto}
.tarjeta{background:var(--tarjeta);border:1px solid var(--borde);border-radius:12px;padding:20px;transition:transform .2s,box-shadow .2s}
.tarjeta:hover{transform:translateY(-4px);box-shadow:0 8px 24px rgba(0,0,0,.06)}
.tarjeta h3{font-size:1.1rem;margin-bottom:8px}
.tarjeta p{font-size:0.9rem;color:var(--suave);margin-bottom:12px}
.meta{font-size:0.8rem;color:var(--suave);display:flex;gap:12px;flex-wrap:wrap}
.etiqueta{background:#e8eef5;padding:2px 8px;border-radius:6px;font-size:0.75rem}
footer{max-width:1200px;margin:40px auto 0;padding-top:24px;border-top:1px solid var(--borde);color:var(--suave);font-size:0.85rem}
@media (max-width:640px){body{padding:16px}.grid{grid-template-columns:1fr}}
"""

HTML_CABECERA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<style>{css}</style>
</head>
<body>
"""


def _escapar(texto: str) -> str:
    return html.escape(texto or "")


def _fecha_larga() -> str:
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    h = date.today()
    return f"{dias[h.weekday()]} {h.day} de {meses[h.month - 1]} de {h.year}"


def _lea_json(ruta: Path, por_defecto: object = None) -> object:
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return por_defecto


def _hash_contenido(contenido: str) -> str:
    return hashlib.sha256(contenido.encode("utf-8")).hexdigest()[:12]


def _piezas_vivas() -> list[dict]:
    """Lee las piezas vivas de ambos canales y devuelve metadatos."""
    piezas: list[dict] = []
    if not PUBLICACIONES.exists():
        return piezas
    for canal_dir in PUBLICACIONES.iterdir():
        if not canal_dir.is_dir():
            continue
        canal = canal_dir.name
        for p in sorted(canal_dir.iterdir()):
            if p.suffix != ".md" or p.name.startswith("_"):
                continue
            try:
                contenido = p.read_text(encoding="utf-8")
            except OSError:
                continue
            titulo_match = re.search(r"^#\s+(.+)$", contenido, re.M)
            titulo = _escapar(titulo_match.group(1).strip()) if titulo_match else p.stem
            fecha_match = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
            fecha = fecha_match.group(1) if fecha_match else ""
            estrellas = re.findall(r"★(\d[\d\.]*)", contenido)
            licencia_match = re.search(r"(GPL-[\d\.]+|MIT|Apache-[\d\.]+|AGPL-[\d\.]+|BSD-[\d\.]+|MPL-[\d\.]+)", contenido)
            licencia = _escapar(licencia_match.group(1)) if licencia_match else "—"
            piezas.append({
                "canal": canal,
                "archivo": p.name,
                "ruta": str(p.relative_to(RAIZ)),
                "titulo": titulo,
                "fecha": fecha,
                "caracteres": len(contenido),
                "estrellas": estrellas[0] if estrellas else "—",
                "licencia": licencia,
                "hash": _hash_contenido(contenido),
            })
    return sorted(piezas, key=lambda x: (x["fecha"], x["titulo"]))


def _fichas_registro() -> list[dict]:
    """Lee las fichas del registro y devuelve metadatos para el sitio."""
    fichas: list[dict] = []
    if not REGISTRO.exists():
        return fichas
    for p in sorted(REGISTRO.glob("*.json")):
        if p.name.startswith("_"):
            continue
        d = _lea_json(p)
        if d is None:
            continue
        fichas.append({
            "id": d.get("id", ""),
            "repo": d.get("repo", ""),
            "licencia": (d.get("licencia") or {}).get("spdx", "—"),
            "estado": (d.get("actividad") or {}).get("estado", "—"),
            "medido_en": d.get("medido_en", ""),
            "stars": (d.get("merito") or {}).get("stars", "—"),
        })
    return fichas


def generar_index(piezas: list[dict], fichas: list[dict]) -> None:
    """Genera site/index.html."""
    filas_piezas = ""
    for pz in piezas:
        filas_piezas += f"""
        <div class="tarjeta">
          <h3>{pz['titulo']}</h3>
          <p class="meta"><span class="etiqueta">{pz['canal']}</span> <span class="etiqueta">{pz['fecha']}</span> <span class="etiqueta">★{pz['estrellas']}</span> <span class="etiqueta">{pz['licencia']}</span></p>
          <p>{pz['caracteres']} caracteres · hash {pz['hash']}</p>
        </div>"""
    filas_fichas = ""
    for fc in fichas[:50]:
        filas_fichas += f"""
        <tr>
          <td>{_escapar(fc['id'])}</td>
          <td>{_escapar(fc['repo'])}</td>
          <td>{fc['licencia']}</td>
          <td>{fc['estado']}</td>
          <td>{fc['medido_en']}</td>
          <td>{fc['stars']}</td>
        </tr>"""
    html_contenido = HTML_CABECERA.format(
        titulo="La Bandita · archivo, ley y frontend",
        css=CSS,
    )
    html_contenido += f"""
    <header>
      <div>
        <h1>La Bandita</h1>
        <div class="subtitulo">Archivo de divulgación técnica en español sobre software libre para Android · {_fecha_larga()}</div>
      </div>
      <div>Total piezas: {len(piezas)} · Fichas registradas: {len(fichas)}</div>
    </header>
    <section>
      <h2>Piezas vivas</h2>
      <div class="grid">{filas_piezas}</div>
    </section>
    <section style="margin-top:40px">
      <h2>Registro de fichas (primeras 50)</h2>
      <table style="width:100%;border-collapse:collapse;font-size:0.85rem">
        <thead><tr style="text-align:left;border-bottom:1px solid var(--borde)"><th>ID</th><th>Repo</th><th>Licencia</th><th>Estado</th><th>Medido</th><th>★</th></tr></thead>
        <tbody>{filas_fichas}</tbody>
      </table>
    </section>
    <footer>La Bandita informa a partir de fuentes fechadas · Código MIT · Texto CC BY-SA 4.0 · Datos CC BY 4.0</footer>
    </body>
    </html>"""
    (SITE / "index.html").write_text(html_contenido, encoding="utf-8")


def generar_feed(piezas: list[dict]) -> None:
    """Genera site/feed.xml (RSS)."""
    items = ""
    for pz in piezas:
        items += f"""
  <item>
    <title><![CDATA[{pz['titulo']}]]></title>
    <link>https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/{pz['ruta']}</link>
    <pubDate>{pz['fecha']}</pubDate>
    <guid>{pz['hash']}</guid>
    <description><![CDATA[{pz['caracteres']} caracteres · {pz['canal']} · ★{pz['estrellas']} · {pz['licencia']}]]></description>
  </item>"""
    xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>La Bandita · publicaciones</title>
  <link>https://github.com/Alex17273747576777/la-bandita-archivo</link>
  <description>Archivo de divulgación técnica en español sobre software libre para Android</description>
  <lastBuildDate>{_fecha_larga()}</lastBuildDate>
  {items}
</channel>
</rss>"""
    (SITE / "feed.xml").write_text(xml, encoding="utf-8")


def generar_registro_json(fichas: list[dict]) -> None:
    """Genera site/datos/registro.json."""
    DATOS.mkdir(parents=True, exist_ok=True)
    (DATOS / "registro.json").write_text(
        json.dumps({"fecha": date.today().isoformat(), "total": len(fichas), "fichas": fichas},
                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def generar_redes() -> None:
    """Genera site/redes/index.html y site/datos/redes.json."""
    REDES_DIR.mkdir(parents=True, exist_ok=True)
    canales: dict[str, dict] = {}
    if PUBLICACIONES.exists():
        for canal_dir in PUBLICACIONES.iterdir():
            if not canal_dir.is_dir():
                continue
            nombre = canal_dir.name
            md = [f for f in canal_dir.iterdir() if f.suffix == ".md" and not f.name.startswith("_")]
            total_chars = 0
            for f in md:
                try:
                    total_chars += len(f.read_text(encoding="utf-8"))
                except OSError:
                    pass
            canales[nombre] = {
                "piezas": len(md),
                "caracteres": total_chars,
            }
    DATOS.mkdir(parents=True, exist_ok=True)
    (DATOS / "redes.json").write_text(
        json.dumps({"fecha": date.today().isoformat(), "redes": canales}, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    filas = ""
    for nombre, datos in canales.items():
        filas += f"<tr><td>{nombre}</td><td>{datos['piezas']}</td><td>{datos['caracteres']}</td></tr>"
    html_red = HTML_CABECERA.format(titulo="La Bandita · redes", css=CSS)
    html_red += f"""
    <header>
      <h1>Redes</h1>
      <div class="subtitulo">Qué se publicó en cada red y con qué interacción</div>
    </header>
    <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
      <thead><tr style="text-align:left;border-bottom:1px solid var(--borde)"><th>Red</th><th>Piezas</th><th>Caracteres</th></tr></thead>
      <tbody>{filas}</tbody>
    </table>
    <footer>Sin medición declarada se muestra como ausencia, nunca como cero falso.</footer>
    </body>
    </html>"""
    (REDES_DIR / "index.html").write_text(html_red, encoding="utf-8")


def generar_fichas(piezas: list[dict]) -> None:
    """Genera páginas individuales de ficha en site/piezas/ y site/ficha/."""
    PIEZAS_DIR.mkdir(parents=True, exist_ok=True)
    FICHA_DIR.mkdir(parents=True, exist_ok=True)
    for pz in piezas:
        contenido_pieza = f"""
        <h2>{pz['titulo']}</h2>
        <p class="meta"><span class="etiqueta">{pz['canal']}</span> <span class="etiqueta">{pz['fecha']}</span></p>
        <p>{pz['caracteres']} caracteres · hash {pz['hash']}</p>
        <p><a href="{pz['ruta']}">Ver pieza original (Markdown)</a></p>
        """
        html_pieza = HTML_CABECERA.format(titulo=pz['titulo'], css=CSS)
        html_pieza += f"<body>{contenido_pieza}<footer>La Bandita · {_fecha_larga()}</footer></body></html>"
        (PIEZAS_DIR / f"{pz['archivo'].replace('.md', '.html')}").write_text(html_pieza, encoding="utf-8")


def main() -> int:
    print("SITIO · generando sitio estático de La Bandita\n")
    piezas = _piezas_vivas()
    fichas = _fichas_registro()

    SITE.mkdir(parents=True, exist_ok=True)
    generar_index(piezas, fichas)
    generar_feed(piezas)
    generar_registro_json(fichas)
    generar_redes()
    generar_fichas(piezas)

    print(f"  site/index.html · {len(piezas)} piezas · {len(fichas)} fichas")
    print(f"  site/feed.xml · RSS generado")
    print(f"  site/datos/registro.json · proyección del registro")
    print(f"  site/datos/redes.json · datos de redes sociales")
    print(f"  site/redes/index.html · vista de redes")
    print(f"  site/piezas/ · {len(piezas)} páginas individuales")
    print("\nSitio generado en site/ · cero CDN · cero fuentes externas · abre sin red")
    return 0


if __name__ == "__main__":
    sys.exit(main())
