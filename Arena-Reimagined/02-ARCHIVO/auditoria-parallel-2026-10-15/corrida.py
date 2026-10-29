#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CORRIDA PARALELA de la lupa v5 — adaptación hiper extrema de contexto.
Nada de parámetros únicos: cada pieza recibe SU corte (del nombre de archivo),
SU banda (D-002 / FB-en-construcción / cimientos sin banda de publicación),
SUS claves de quiz (donde constan), SU doctrina (donde existe acta), y los
cimientos legacy se informan con lupa completa pero SIN gates de publicación
(no son piezas WhatsApp: son interior del taller).
Paralelo real: 2 trabajadores (nproc=2).
"""
import os, re, sys, json, hashlib, subprocess
from concurrent.futures import ThreadPoolExecutor

RAIZ = "/home/user/Arena-Reimagined"
SALIDA = os.path.join(RAIZ, "02-ARCHIVO", "auditoria-parallel-2026-10-15")
LUPA = os.path.join(RAIZ, "_herramientas", "lupa-v5-evolutiva.py")
os.makedirs(SALIDA, exist_ok=True)

KEYS = {
    "01-Tiendas-APK": "dueño conocido|GitLab|hito (4 países)",
    "02-Kototoro": "cédula|peldaño|11:29",
}
DOCTRINA = os.path.join(RAIZ, "02-ARCHIVO", "doctrina-lupa.json")

def piezas():
    out = []
    wd = os.path.join(RAIZ, "01-PUBLICACIONES", "WhatsApp-dominicano-ES")
    for f in sorted(os.listdir(wd)):
        if f.endswith(".md") and not f.startswith("LEEME"):
            out.append((os.path.join(wd, f), "whatsapp"))
    cd = os.path.join(RAIZ, "00-CANON")
    for f in ["manual-estilo-visual-la-bandita-v1-2026-10-15.md",
              "metodo-ensenanza-la-bandita-v1-2026-10-15.md",
              "MANUAL-COMPLETO.md", "MANUAL-FICHAS-FALLOS.md", "TRATADO.md"]:
        p = os.path.join(cd, f)
        if os.path.exists(p): out.append((p, "cimiento"))
    return out

def banda(slug, familia):
    if familia == "cimiento":
        return ("cimiento-interior", None, None)
    if "Facebook" in slug or slug.startswith("10-Gltools"):
        return ("FB-40k (en construcción)", 40000, 44000)
    return ("D-002", 62000, 64000)

def corte(slug):
    m = re.search(r"(2026-\d\d-\d\d)", slug)
    return m.group(1) if m else "2026-10-15"

def trabajo(arg):
    path, familia = arg
    slug = os.path.basename(path)
    args = [sys.executable, LUPA, path, "--cutover", corte(slug)]
    if "--keys" and any(slug.startswith(k) for k in KEYS):
        for k in KEYS:
            if slug.startswith(k):
                args += ["--keys", KEYS[k]]; break
    if slug.startswith("01-Tiendas"):
        args += ["--doctrina", DOCTRINA]
    rp = os.path.join(SALIDA, re.sub(r"[^A-Za-z0-9.-]+", "_", slug)[:60] + ".reporte.txt")
    with open(rp, "w", encoding="utf-8") as fh:
        subprocess.run(args, stdout=fh, stderr=subprocess.STDOUT, timeout=600)
    # resumen del reporte
    fams = {}; total = sello = estado = "?"
    for ln in open(rp, encoding="utf-8"):
        m = re.match(r"\s+\[([^\]]+)\]", ln)
        if m:
            f = m.group(1).split()[0]
            fams[f] = fams.get(f, 0) + 1
        m = re.match(r"TOTAL: (\d+) c · banda: (.+?) · sello: (\w+)", ln)
        if m: total, estado, sello = int(m.group(1)), m.group(2).strip(), m.group(3)
    bname, blo, bhi = banda(slug, familia)
    if familia == "cimiento":
        juez = "interior del taller (sin gate de publicación)"
    elif "FB" in bname:
        juez = "EN CONSTRUCCIÓN (%d c de 40.000)" % total
    else:
        juez = "DENTRO ✓" if (blo and blo <= total <= bhi) else "FUERA ✗"
    return dict(slug=slug, familia=familia, corte=corte(slug), banda=bname,
                chars=total, sello=sello, juez=juez, fams=fams, reporte=os.path.basename(rp))

if __name__ == "__main__":
    P = piezas()
    print("PIEZAS EN PARALELO: %d (2 trabajadores)" % len(P))
    with ThreadPoolExecutor(max_workers=2) as ex:
        res = list(ex.map(trabajo, P))
    json.dump(res, open(os.path.join(SALIDA, "consolidado.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print()
    print("%-58s %-9s %-10s %-8s %-9s %s" % ("PIEZA", "CORTE", "BANDA", "CARACT", "SELLO", "JUEZ"))
    for r in res:
        print("%-58s %-9s %-10s %-8d %-9.8s %s" % (r["slug"][:58], r["corte"][5:], r["banda"][:10], r["chars"], r["sello"], r["juez"]))
    print()
    print("%-58s %s" % ("PIEZA", "FAMILIAS DE ALERTAS (todas cuentan; doctrina anota)"))
    for r in res:
        fs = " ".join("%s:%d" % (k, v) for k, v in sorted(r["fams"].items()))
        print("%-58s %s" % (r["slug"][:58], fs if fs else "(0 alertas)"))
