#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auditoria-estatica-canon.py — vara estática E1 para la familia del canon (11/14-oct).
Uso:  python3 auditoria-estatica-canon.py <pieza>   (p.ej. LECCIONES-ALEXIS)
Comprueba fuente (md o html) y envase XHTML. SOLO LECTURA — jamás muta.
Salida: OK/FALLO por check + veredicto. Exit 1 si hay fallos.
"""
import sys, re, os, hashlib
import xml.etree.ElementTree as ET

CANON = os.path.join(os.path.dirname(__file__), "..", "..", "00-CANON")
ENV = os.path.join(CANON, "_envases-xhtml")

PIEZAS = {
    "TRATADO":     ("TRATADO.md", "TRATADO-envase-XHTML-2026-10-10.xhtml"),
    "MANUAL":      ("MANUAL-COMPLETO.md", "MANUAL-COMPLETO-envase-XHTML-2026-10-10.xhtml"),
    "LECCIONES":   ("LECCIONES-ALEXIS.md", "LECCIONES-ALEXIS-envase-XHTML-2026-10-10.xhtml"),
    "CIMIENTO":    ("CANON-CIMIENTO-V28sep.html", "CANON-CIMIENTO-envase-XHTML-2026-10-10.xhtml"),
    "COMPENDIO":   ("COMPENDIO-INTEGRAL-LibroE-V26sep.html", "COMPENDIO-INTEGRAL-envase-XHTML-2026-10-10.xhtml"),
}

def sha16(b): return hashlib.sha256(b).hexdigest()[:16]

def chk(res, cond, msg):
    res.append((bool(cond), msg))

def audit_md(path, res):
    b = open(path, "rb").read()
    d = b.decode("utf-8")
    chk(res, not b.startswith(b"\xef\xbb\xbf"), "sin BOM")
    chk(res, "\r" not in d, "sin CRLF")
    chk(res, not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", d), "0 caracteres de control")
    fences = re.findall(r"^```", d, flags=re.M)
    chk(res, len(fences) % 2 == 0, "vallas de código balanceadas (%d)" % len(fences))
    # contorno de encabezados sin saltos
    levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) ", d, flags=re.M)]
    skips = [(levels[i], levels[i+1]) for i in range(len(levels)-1) if levels[i+1] > levels[i]+1]
    # (2.5) los saltos de contorno se MIDEN siempre y se clasifican LEGADO-ORDENADO:
    # el dueño ordenó conservarlos como legado (14-oct) — no son defecto ni se silencian.
    if skips:
        res.append((True, "contorno: %d salto(s) LEGADO-ordenado %s (conservados por orden del dueño)" % (len(skips), skips[:3])))
    else:
        res.append((True, "contorno sin saltos"))
    # tablas: filas con nº de pipes consistente dentro de cada bloque
    bad_tables = 0; tables = 0
    for block in re.finditer(r"(?:^\|.*\n)+", d, flags=re.M):
        tables += 1
        rows = block.group(0).strip("\n").split("\n")
        counts = {r.count("|") for r in rows}
        if len(counts) > 1: bad_tables += 1
    chk(res, bad_tables == 0, "tablas bien formadas (%d bloques, %d malos)" % (tables, bad_tables))
    # enlaces md bien formados
    badlinks = [m.group(0) for m in re.finditer(r"\]\([^ \)]*\s[^)]*\)", d)]
    chk(res, not badlinks, "enlaces md sin espacios: %s" % badlinks[:2])
    # anclas internas [x](#y) → encabezados presentes.
    # FIX #29 (2.5): el modelo anterior era GitHub (conserva acentos, no trunca, no
    # reescribe puntuación) — la hipótesis exacta que H#4/H#5 falsaron. El envase asigna
    # ids con el SLUGGER DEL CONVERTIDOR; la vara mide contra ese modelo (la realidad).
    import unicodedata
    def _cslug(t, used):
        s = unicodedata.normalize("NFKD", t)
        s = "".join(c for c in s if not unicodedata.combining(c)).lower()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48] or "sec"
        base, i = s, 2
        while s in used:
            s = "%s-%d" % (base, i); i += 1
        used.add(s)
        return s
    _used = set()
    heads = {_cslug(h.strip(), _used) for h in re.findall(r"^#{1,6} (.+)$", d, flags=re.M)}
    missing = [a for a in set(re.findall(r"\]\(#([^)]+)\)", d)) if a not in heads]
    chk(res, not missing, "anclas internas rotas (slugger convertidor): %s" % missing[:3])
    print("   fuente: %d B · sha16 %s" % (len(b), sha16(b)))
    return b

def audit_html(path, res):
    # fuente HTML legacy (no XHTML): se valida como HTML con lxml, NO como XML
    from lxml import etree as LET
    b = open(path, "rb").read()
    d = b.decode("utf-8")
    try:
        LET.HTML(b); ok = True; err = ""
    except Exception as e:
        ok = False; err = str(e)
    chk(res, ok, "HTML bien formado %s" % err)
    sids = set(re.findall(r'id="([^"]+)"', d))
    srotas = [h for h in set(re.findall(r'href="#([^"]+)"', d)) if h not in sids]
    chk(res, not srotas, "anclas del fuente rotas: %s" % srotas[:3])
    chk(res, not re.search(r"\ssrc=\"https?:", d), "0 recursos externos src")
    chk(res, not re.search(r"@import|url\(\s*['\"]?https?:", d), "0 recursos externos css")
    ids = re.findall(r'id="([^"]+)"', d)
    chk(res, len(ids) == len(set(ids)), "ids únicos (%d)" % len(ids))
    hrefs = set(re.findall(r'href="#([^"]+)"', d))
    rotas = [h for h in hrefs if h not in set(ids)]
    chk(res, not rotas, "anclas internas rotas: %s" % rotas[:3])
    chk(res, "<title>" in d, "title presente")
    chk(res, not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", d), "0 control chars")
    print("   fuente: %d B · sha16 %s" % (len(b), sha16(b)))
    return b

def audit_envase(path, res):
    b = open(path, "rb").read()
    d = b.decode("utf-8")
    try:
        ET.fromstring(b); ok = True; err = ""
    except ET.ParseError as e:
        ok = False; err = str(e)
    chk(res, ok, "XHTML bien formado %s" % err)
    chk(res, not re.search(r"\ssrc=\"https?:", d), "0 recursos externos src")
    chk(res, not re.search(r"@import|url\(\s*['\"]?https?:", d), "0 recursos externos css")
    ids = re.findall(r'id="([^"]+)"', d)
    chk(res, len(ids) == len(set(ids)), "ids únicos (%d)" % len(ids))
    hrefs = set(re.findall(r'href="#([^"]+)"', d))
    rotas = [h for h in hrefs if h not in set(ids)]
    chk(res, not rotas, "anclas rotas: %s" % rotas[:3])
    secs = len(re.findall(r"<section\b", d))
    print("   envase: %d B · sha16 %s · secciones %d" % (len(b), sha16(b), secs))
    return b, secs

def main():
    pieza = sys.argv[1].upper()
    if pieza not in PIEZAS:
        print("pieza desconocida:", pieza); sys.exit(2)
    src_rel, env_rel = PIEZAS[pieza]
    res = []
    print("═══ E1 %s ═══" % pieza)
    sp = os.path.join(CANON, src_rel)
    ep = os.path.join(ENV, env_rel)
    for p in (sp, ep):
        if not os.path.exists(p):
            print("AUSENTE:", p); sys.exit(2)
    if src_rel.endswith(".md"):
        audit_md(sp, res)
    else:
        audit_html(sp, res)
    _, secs = audit_envase(ep, res)
    fails = [m for ok, m in res if not ok]
    print("   VEREDICTO E1 %s: %d checks OK · %d FALLOS" % (pieza, len(res)-len(fails), len(fails)))
    for f in fails: print("     ✗", f)
    for ok, m in res:
        if ok and "LEGADO" in m: print("     ◆ LEGADO:", m)
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
