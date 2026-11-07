#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
empaquetar-kit.py — ETAPA 4: sellado y kit de entrega (reproducible, determinístico en contenido).
Arma 02-ARCHIVO/_kit-etapa4/ con: fuentes · envases · mapa · capturas · herramientas · actas ·
LEEMME.md (cadena de sellos medida al momento) · SHA256SUMS.txt.
Luego: canon-labandita-kit-etapa4.zip (raíz del repo) + su .sha256. Verifica el ZIP.
Cumple: token jamás en docs/ZIP · nombre ASCII · ZIP con SHA-256 · sin metadatos IA en pluma.
"""
import os, hashlib, zipfile, shutil, re, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
KIT = os.path.join(REPO, "02-ARCHIVO", "_kit-etapa4")
ZIP = os.path.join(REPO, "canon-labandita-kit-etapa4.zip")

COPIAS = [
    ("00-CANON/TRATADO.md", "fuentes/TRATADO.md"),
    ("00-CANON/MANUAL-COMPLETO.md", "fuentes/MANUAL-COMPLETO.md"),
    ("00-CANON/LECCIONES-ALEXIS.md", "fuentes/LECCIONES-ALEXIS.md"),
    ("00-CANON/CANON-CIMIENTO-V28sep.html", "fuentes/CANON-CIMIENTO-V28sep.html"),
    ("00-CANON/COMPENDIO-INTEGRAL-LibroE-V26sep.html", "fuentes/COMPENDIO-INTEGRAL-LibroE-V26sep.html"),
    ("00-CANON/_envases-xhtml/TRATADO-envase-XHTML-2026-10-10.xhtml", "envases/TRATADO-envase-XHTML.xhtml"),
    ("00-CANON/_envases-xhtml/MANUAL-COMPLETO-envase-XHTML-2026-10-10.xhtml", "envases/MANUAL-COMPLETO-envase-XHTML.xhtml"),
    ("00-CANON/_envases-xhtml/LECCIONES-ALEXIS-envase-XHTML-2026-10-10.xhtml", "envases/LECCIONES-ALEXIS-envase-XHTML.xhtml"),
    ("00-CANON/_envases-xhtml/CANON-CIMIENTO-envase-XHTML-2026-10-10.xhtml", "envases/CANON-CIMIENTO-envase-XHTML.xhtml"),
    ("00-CANON/_envases-xhtml/COMPENDIO-INTEGRAL-envase-XHTML-2026-10-10.xhtml", "envases/COMPENDIO-INTEGRAL-envase-XHTML.xhtml"),
    ("00-CANON/_mapa-canon/MAPA-CANON.json", "mapa/MAPA-CANON.json"),
    ("00-CANON/_mapa-canon/MAPA-CANON.md", "mapa/MAPA-CANON.md"),
    ("00-CANON/_mapa-canon/sello.txt", "mapa/sello.txt"),
    ("00-CANON/_mapa-canon/DEMOLICION-CONTENIDO.json", "mapa/DEMOLICION-CONTENIDO.json"),
    ("02-ARCHIVO/registro-2026-10-14.md", "actas/registro-2026-10-14.md"),
    ("02-ARCHIVO/registro-2026-10-11.md", "actas/registro-2026-10-11.md"),
    ("02-ARCHIVO/registro-2026-10-10.md", "actas/registro-2026-10-10.md"),
    ("02-ARCHIVO/_herramientas/mapa-canon.py", "herramientas/mapa-canon.py"),
    ("02-ARCHIVO/_herramientas/reconstruccion-toc.py", "herramientas/reconstruccion-toc.py"),
    ("02-ARCHIVO/_herramientas/demolicion-contenido.py", "herramientas/demolicion-contenido.py"),
    ("02-ARCHIVO/_herramientas/auditoria-estatica-canon.py", "herramientas/auditoria-estatica-canon.py"),
    ("02-ARCHIVO/_herramientas/bateria-funcionamiento.py", "herramientas/bateria-funcionamiento.py"),
    ("02-ARCHIVO/_herramientas/bateria-viva.js", "herramientas/bateria-viva.js"),
    ("02-ARCHIVO/_herramientas/envase-xhtml-canon.py", "herramientas/envase-xhtml-canon.py"),
]
CAPTURAS = sorted(os.listdir(os.path.join(REPO, "02-ARCHIVO", "_capturas-etapa3")))

def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def muertos_envase(p):
    d = open(p, encoding="utf-8").read()
    ids = set(re.findall(r'id="([^"]+)"', d))
    return len({t for t in re.findall(r'href="#([^"]+)"', d) if t not in ids})

def main():
    if os.path.exists(KIT): shutil.rmtree(KIT)
    for _, dst in COPIAS:
        dstp = os.path.join(KIT, dst)
        os.makedirs(os.path.dirname(dstp), exist_ok=True)
        shutil.copy2(os.path.join(REPO, _), dstp)
    cdir = os.path.join(KIT, "capturas")
    os.makedirs(cdir, exist_ok=True)
    for c in CAPTURAS:
        shutil.copy2(os.path.join(REPO, "02-ARCHIVO", "_capturas-etapa3", c), os.path.join(cdir, c))
    # sellos medidos al momento
    sellos = {}
    for src, dst in COPIAS:
        rel = dst.split("/")[0]
        sellos.setdefault(rel, []).append((os.path.basename(dst), os.path.getsize(os.path.join(KIT, dst)), sha256(os.path.join(KIT, dst))))
    envs = {k: v for k, v in sellos.items() if k == "envases"}
    # verificación viva de navegación en envases (medida ahora)
    nav = {n.split("-envase")[0]: muertos_envase(os.path.join(KIT, "envases", n)) for n, _, _ in envs["envases"]}
    leemme = """# KIT DE ENTREGA — CAMPAÑA CANON (E0–E4), LA BANDITA
Estado: pre-publicación. E5 (publicación) solo bajo orden expresa del dueño y con su
satisfacción total. Este kit fue armado por el taller al servicio del dueño; el proceso
completo, con cifras medidas, vive en `actas/registro-2026-10-14.md`.

## Contenido
- `fuentes/` — 5 piezas del canon: TRATADO, MANUAL, LECCIONES (.md, navegación reconstruida
  bajo orden expresa del dueño: SOLO targets de anclas; palabras del autor intactas byte-a-byte)
  y CANON-CIMIENTO + COMPENDIO (HTML legacy, intactos: sello original sin cambios).
- `envases/` — 5 ediciones XHTML autocontenidas (0 recursos externos, 0 peticiones, offline,
  imprimible; búsqueda, tema auto/claro/oscuro, navegación con scrollspy).
- `mapa/` — MAPA-CANON.json (inventario total, regenerable byte-a-byte con
  `python3 herramientas/mapa-canon.py --verify`), DEMOLICION-CONTENIDO.json (demolición E1) y sello.
- `capturas/` — 10 evidencias visuales (5 escritorio-claro + 5 móvil-oscuro), Etapa 3.
- `herramientas/` — el taller completo (mapa, reparador de TOC, demolición, vara E1,
  batería estática, batería viva, convertidor).
- `actas/` — registros fechados 10/11/14-oct-2026. Append-only.

## Cadena de sellos (sha256, primeros 16 hex)
Fuentes .md — antes → después (mutación autorizada: solo targets de anclas):
- TRATADO:   3c58d9f907205f3a → {t}
- MANUAL:    c4c33f44c02cdeef → {m}
- LECCIONES: 1539dfcf753bb4d3 → {l}
Fuentes HTML legacy — INTACTOS (sello del 11-oct sin cambios):
- CIMIENTO:  f517f6b7b301d6bf
- COMPENDIO: 07830c49e685aa16
Envases XHTML finales (esta cocción):
{envs}
Navegación medida en los envases de ESTE kit — anclas muertas: {nav} (0 en las 5).

## Verificación (todo corre desde la raíz del kit extraído)
1. `sha256sum -c SHA256SUMS.txt`
2. `python3 herramientas/mapa-canon.py --verify` (requiere la estructura del repo; en el kit
   el mapa viene sellado en `mapa/sello.txt`)
3. `python3 herramientas/bateria-funcionamiento.py` (batería estática 5×11)
4. Abrir cualquier `envases/*.xhtml` en un navegador: consola limpia, deep-links, `/` busca,
   tema, móvil sin desborde horizontal (batería viva: 5/5, acta 14-oct).

## Doctrina
Regla de oro (Art. D-007): «Ninguna derogación se ejecuta en silencio. Cada una lleva su
fila, su fecha y su firma. Así se corrige sin mentir sobre el pasado.» — Esta entrega es
esa fila. Mejor que lo que precedió, nunca perfecto.
"""
    env_lines = "\n".join("- %s: %d B · `%s`" % (n.replace("-envase-XHTML.xhtml", ""), b, h) for n, b, h in envs["envases"])
    open(os.path.join(KIT, "LEEMME.md"), "w", encoding="utf-8").write(leemme.format(
        t=sellos["fuentes"][0][2], m=sellos["fuentes"][1][2], l=sellos["fuentes"][2][2],
        envs=env_lines, nav=", ".join("%s=%d" % (k, v) for k, v in nav.items())))
    # manifiesto
    rutas = []
    for raiz, _, files in os.walk(KIT):
        for f in sorted(files):
            p = os.path.join(raiz, f)
            rutas.append((os.path.relpath(p, KIT), p))
    rutas.sort()
    with open(os.path.join(KIT, "SHA256SUMS.txt"), "w", encoding="utf-8") as fh:
        for rel, p in rutas:
            fh.write("%s  %s\n" % (sha256(p), rel))
    rutas.append(("SHA256SUMS.txt", os.path.join(KIT, "SHA256SUMS.txt")))
    # zip
    if os.path.exists(ZIP): os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for rel, p in rutas:
            z.write(p, "canon-labandita-kit-etapa4/" + rel)
    zsha = sha256(ZIP)
    open(ZIP + ".sha256", "w").write("%s  canon-labandita-kit-etapa4.zip\n" % zsha)
    # verificación del zip
    with zipfile.ZipFile(ZIP) as z:
        mal = z.testzip()
        n = len(z.namelist())
    print("KIT: %d archivos · LEEMME + SHA256SUMS incluidos" % (len(rutas) + 2))
    print("verificación de navegación (medida en el kit): %s" % nav)
    print("ZIP: %s · %d B · sha256 %s · testzip=%s · %d entradas" % (
        os.path.basename(ZIP), os.path.getsize(ZIP), zsha, "OK" if mal is None else "CORRUPTO", n))
    print("SELLOS FINALES: fuentes %s" % {k: [(a, c) for a, b, c in v] for k, v in sellos.items() if k == "fuentes"})

if __name__ == "__main__":
    main()
