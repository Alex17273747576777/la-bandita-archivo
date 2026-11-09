#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WEB · arma la página pública del archivo, en un solo archivo, sin nada externo.

Qué hace:
  * Lee docs/CENSO-MEDIDO-2026-11-09.json (3.125 repositorios medidos) y registry/*.json.
  * Escribe web/index.html con los datos metidos dentro: sin CDN, sin fuentes externas, sin
    JavaScript de terceros. Se abre desde un archivo y funciona sin red.
  * Deja web/datos.json por separado para quien quiera reusar los datos.

Qué NO hace:
  * No inventa campos: los que no se midieron salen como null y la página los muestra así.
  * No aloja binarios ni enlaza a descargas directas.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CENSO = RAIZ / "docs" / "CENSO-MEDIDO-2026-11-09.json"
REGISTRO = RAIZ / "registry"
WEB = RAIZ / "web"


def datos() -> dict:
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    fichas = []
    for r in censo["repos"]:
        if r.get("estado") != "vivo":
            continue
        fichas.append({
            "repo": r["repo"],
            "estrellas": r.get("stars"),
            "licencia": r.get("licencia"),
            "dias_nace": r.get("dias_nace"),
            "dias_push": r.get("dias_push"),
            "entregas": r.get("entregas"),
            "ultima": r.get("rel_fecha"),
            "adjuntos": r.get("adjuntos_ultima"),
            "sumas": r.get("huellas_ultima"),
            "descargas": r.get("descargas_ultima"),
            "lenguaje": r.get("lenguaje"),
        })
    fichas.sort(key=lambda x: -(x["estrellas"] or 0))
    return {
        "titulo": "El archivo abierto de La Bandita",
        "medido_en": "2026-11-09",
        "fuente": "censo de fmhy.net medido contra la API pública de GitHub",
        "totales": censo["totales"],
        "fichas_propias": len(list(REGISTRO.glob("*.json"))),
        "repos": fichas,
    }


HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<style>
:root {{
  --fondo:#0d1117; --panel:#161b22; --borde:#30363d; --texto:#e6edf3;
  --tenue:#8b949e; --acento:#58a6ff; --verde:#3fb950; --rojo:#f85149; --ambar:#d29922;
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0; background:var(--fondo); color:var(--texto);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  line-height:1.55;
}}
header {{ padding:2.2rem 1.2rem 1.4rem; border-bottom:1px solid var(--borde); }}
h1 {{ margin:0 0 .4rem; font-size:1.7rem; letter-spacing:-.02em; }}
.sub {{ color:var(--tenue); font-size:.92rem; max-width:62rem; }}
.cifras {{ display:flex; flex-wrap:wrap; gap:1.6rem; margin:1.4rem 0 0; }}
.cifra {{ min-width:7rem; }}
.cifra b {{ display:block; font-size:1.5rem; color:var(--acento); font-variant-numeric:tabular-nums; }}
.cifra span {{ font-size:.76rem; color:var(--tenue); text-transform:uppercase; letter-spacing:.06em; }}
main {{ padding:1.2rem; max-width:80rem; margin:0 auto; }}
.controles {{ display:flex; flex-wrap:wrap; gap:.6rem; margin-bottom:1rem; align-items:center; }}
input[type=search], select {{
  background:var(--panel); color:var(--texto); border:1px solid var(--borde);
  border-radius:6px; padding:.5rem .7rem; font-size:.9rem;
}}
input[type=search] {{ flex:1 1 18rem; }}
label.check {{ font-size:.85rem; color:var(--tenue); display:flex; gap:.35rem; align-items:center; }}
table {{ width:100%; border-collapse:collapse; font-size:.85rem; }}
th, td {{ text-align:left; padding:.45rem .55rem; border-bottom:1px solid var(--borde); }}
th {{ position:sticky; top:0; background:var(--fondo); cursor:pointer; user-select:none; color:var(--tenue);
      font-size:.74rem; text-transform:uppercase; letter-spacing:.05em; }}
th:hover {{ color:var(--acento); }}
td.num {{ text-align:right; font-variant-numeric:tabular-nums; }}
a {{ color:var(--acento); text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
.si {{ color:var(--verde); }} .no {{ color:var(--rojo); }} .nada {{ color:var(--tenue); }}
footer {{ padding:2rem 1.2rem 3rem; color:var(--tenue); font-size:.8rem; border-top:1px solid var(--borde); margin-top:2rem; }}
.pagina {{ margin:1rem 0; display:flex; gap:.5rem; align-items:center; font-size:.85rem; }}
button {{ background:var(--panel); color:var(--texto); border:1px solid var(--borde);
          border-radius:6px; padding:.35rem .8rem; cursor:pointer; }}
button:disabled {{ opacity:.4; cursor:default; }}
code {{ background:var(--panel); padding:.1rem .3rem; border-radius:4px; font-size:.85em; }}
.aviso {{ background:var(--panel); border:1px solid var(--borde); border-left:3px solid var(--ambar);
          padding:.7rem .9rem; border-radius:4px; font-size:.83rem; color:var(--tenue); margin:1rem 0; }}
</style>
</head>
<body>
<header>
  <h1>{titulo}</h1>
  <p class="sub">Todo lo que hay aquí se midió contra la API pública de GitHub el 9 de noviembre de 2026.
  Ningún dato está estimado, copiado de un artículo ni puesto a mano: si un campo no se pudo medir,
  dice «aquí no hay». Los programas no se alojan en esta página; cada fila enlaza al repositorio de quien lo hizo.</p>
  <div class="cifras">
    <div class="cifra"><b>{n_repos}</b><span>repositorios vivos</span></div>
    <div class="cifra"><b>{n_estrellas}</b><span>estrellas sumadas</span></div>
    <div class="cifra"><b>{n_sumas}</b><span>publican huella</span></div>
    <div class="cifra"><b>{n_adjuntos}</b><span>adjuntos medidos</span></div>
    <div class="cifra"><b>{n_propias}</b><span>fichas propias</span></div>
  </div>
</header>
<main>
  <div class="aviso">
    <b>Cómo leer la columna «sumas»:</b> cuenta los archivos de comprobación
    (<code>sha256</code>, <code>asc</code>, <code>sig</code>…) que trae la última entrega del repositorio.
    Un <span class="si">número</span> significa que puedes comprobar lo que bajas;
    <span class="no">0</span> significa que el autor no publicó con qué compararlo.
  </div>
  <div class="controles">
    <input type="search" id="busca" placeholder="Buscar por nombre de repositorio… (por ejemplo: audio, mihon, vpn)">
    <select id="orden">
      <option value="estrellas">Ordenar por estrellas</option>
      <option value="sumas">Ordenar por sumas publicadas</option>
      <option value="dias_nace">Ordenar por más nuevo</option>
      <option value="dias_push">Ordenar por actividad reciente</option>
      <option value="adjuntos">Ordenar por adjuntos</option>
    </select>
    <label class="check"><input type="checkbox" id="soloSumas"> solo los que publican sumas</label>
  </div>
  <div class="pagina">
    <button id="antes" disabled>← antes</button>
    <span id="cuenta"></span>
    <button id="despues">después →</button>
  </div>
  <table>
    <thead><tr>
      <th>Repositorio</th><th class="num">Estrellas</th><th class="num">Sumas</th>
      <th class="num">Adjuntos</th><th class="num">Días de vida</th><th class="num">Días sin empujar</th>
      <th>Licencia</th><th>Última entrega</th>
    </tr></thead>
    <tbody id="filas"></tbody>
  </table>
  <div class="pagina">
    <button id="antes2" disabled>← antes</button>
    <span id="cuenta2"></span>
    <button id="despues2">después →</button>
  </div>
</main>
<footer>
  <p><b>Fuente de los datos:</b> {fuente}. Censo de 16 páginas de fmhy.net cruzado con el registro de
  este archivo; {medidos} repositorios medidos, {n_repos} vivos, {archivados} archivados, {sin_objeto} sin objeto,
  {errores} errores de medición.</p>
  <p><b>Licencia de los datos:</b> los datos medidos se publican como dominio público (CC0).
  El código de la página también. Los programas enlazados tienen la licencia que declara cada autor y se
  consulta en su propio repositorio: aquí no se afirma la licencia de nadie más allá de lo que la API devolvió.</p>
  <p>Sin rastreadores, sin cuentas, sin cookies y sin llamadas a ningún servidor: los datos van dentro del archivo.</p>
</footer>
<script>
const DATOS = {datos_json};
let filtrados = DATOS.repos.slice();
let pagina = 0;
const POR_PAGINA = 100;

const busca = document.getElementById('busca');
const orden = document.getElementById('orden');
const soloSumas = document.getElementById('soloSumas');

function miles(n) {{
  if (n === null || n === undefined) return '<span class="nada">aquí no hay</span>';
  return n.toLocaleString('es-DO');
}}

function aplicar() {{
  const q = busca.value.trim().toLowerCase();
  filtrados = DATOS.repos.filter(r => {{
    if (q && !r.repo.toLowerCase().includes(q)) return false;
    if (soloSumas.checked && !(r.sumas > 0)) return false;
    return true;
  }});
  const clave = orden.value;
  filtrados.sort((a, b) => {{
    const va = a[clave], vb = b[clave];
    if (va === null || va === undefined) return 1;
    if (vb === null || vb === undefined) return -1;
    return clave === 'dias_nace' || clave === 'dias_push' ? va - vb : vb - va;
  }});
  pagina = 0;
  pintar();
}}

function pintar() {{
  const desde = pagina * POR_PAGINA;
  const trozo = filtrados.slice(desde, desde + POR_PAGINA);
  document.getElementById('filas').innerHTML = trozo.map(r => {{
    const suma = r.sumas === null || r.sumas === undefined
      ? '<span class="nada">aquí no hay</span>'
      : (r.sumas > 0 ? `<span class="si">${{r.sumas}}</span>` : '<span class="no">0</span>');
    return `<tr>
      <td><a href="https://github.com/${{r.repo}}" rel="noopener noreferrer nofollow" target="_blank">${{r.repo}}</a></td>
      <td class="num">${{miles(r.estrellas)}}</td>
      <td class="num">${{suma}}</td>
      <td class="num">${{miles(r.adjuntos)}}</td>
      <td class="num">${{miles(r.dias_nace)}}</td>
      <td class="num">${{miles(r.dias_push)}}</td>
      <td>${{r.licencia ? r.licencia : '<span class="nada">sin declarar</span>'}}</td>
      <td>${{r.ultima ? r.ultima : '<span class="nada">nunca</span>'}}</td>
    </tr>`;
  }}).join('');
  const total = filtrados.length;
  const texto = `${{desde + 1}}–${{Math.min(desde + POR_PAGINA, total)}} de ${{total}}`;
  document.getElementById('cuenta').textContent = texto;
  document.getElementById('cuenta2').textContent = texto;
  for (const id of ['antes', 'antes2']) document.getElementById(id).disabled = pagina === 0;
  for (const id of ['despues', 'despues2'])
    document.getElementById(id).disabled = desde + POR_PAGINA >= total;
}}

function mover(d) {{ pagina = Math.max(0, pagina + d); pintar(); window.scrollTo({{top: 0, behavior: 'smooth'}}); }}

busca.addEventListener('input', aplicar);
orden.addEventListener('change', aplicar);
soloSumas.addEventListener('change', aplicar);
document.getElementById('antes').addEventListener('click', () => mover(-1));
document.getElementById('antes2').addEventListener('click', () => mover(-1));
document.getElementById('despues').addEventListener('click', () => mover(1));
document.getElementById('despues2').addEventListener('click', () => mover(1));
aplicar();
</script>
</body>
</html>
"""


def main() -> int:
    d = datos()
    WEB.mkdir(exist_ok=True)
    (WEB / "datos.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    t = d["totales"]
    html = HTML.format(
        titulo=d["titulo"],
        fuente=d["fuente"],
        medido_en=d["medido_en"],
        n_repos=f"{t['vivos']:,}".replace(",", "."),
        n_estrellas=f"{t['stars']:,}".replace(",", "."),
        n_sumas=f"{t['con_huella_ultima']:,}".replace(",", "."),
        n_adjuntos=f"{t['adjuntos_ultima']:,}".replace(",", "."),
        n_propias=f"{d['fichas_propias']:,}".replace(",", "."),
        medidos=f"{t['medidos']:,}".replace(",", "."),
        archivados=t["archivados"],
        sin_objeto=t["sin_objeto"],
        errores=t["errores"],
        datos_json=json.dumps({"repos": d["repos"]}, ensure_ascii=False, separators=(",", ":")),
    )
    (WEB / "index.html").write_text(html, encoding="utf-8")
    kb = (WEB / "index.html").stat().st_size / 1024
    print(f"web/index.html · {kb:.0f} KB · {len(d['repos'])} repositorios · sin recursos externos")
    print(f"web/datos.json · {(WEB / 'datos.json').stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
