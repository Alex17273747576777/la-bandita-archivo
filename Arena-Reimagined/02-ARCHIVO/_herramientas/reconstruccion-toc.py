#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reconstruccion-toc.py v2 — Etapa 2: regeneración de targets de anclas en fuentes .md.
ÚNICA mutación de fuente autorizada (orden expresa del dueño, campaña canon E2).
v2 corrige el defecto #27 (el `#` se perdía en el reemplazo) y añade:
  · Fase 1 (TOC): targets regenerados con el slugger EXACTO del convertidor; matcher
    monótono con relación textual exigida; `#` SIEMPRE preservado (asertado por línea).
  · Fase 2 (cuerpo): enlaces-ancora muertos fuera del TOC (crucezas tipo «Hilos») se
    re-apuntan por estructura del label: fecha dd-mm + ordinal romano opcional →
    candidato ÚNICO exigido (sesión base = sin romano en 4ª posición).
  · Verificación NO ciega (todo el documento): conteo de anclas preservado · todo target
    final ∈ slugs reales (0 muertos) · texto fuera de targets byte-idéntico · aborta
    sin escribir ante cualquier aserción rota.
Uso:  python3 reconstruccion-toc.py RUTA.md           → preview
      python3 reconstruccion-toc.py RUTA.md --aplicar → escribe y verifica
"""
import sys, re, hashlib, unicodedata

def fold(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", fold(s)).strip()

def slug(t, used):
    s = re.sub(r"[^a-z0-9]+", "-", fold(t)).strip("-")[:48] or "sec"
    base, i = s, 2
    while s in used:
        s = "%s-%d" % (base, i); i += 1
    used.add(s)
    return s

TOC_LINE = re.compile(r"^(\s*-\s+\[[^\]]*\]\()#([^)]*)(\)\s*)$")
TOC_OK = re.compile(r"^\s*-\s+\[[^\]]*\]\(#[a-z0-9-]+\)\s*$")
HEAD = re.compile(r"^(#{1,6}) (.+)$")
LINK = re.compile(r"\]\(#([^)]*)\)")
MDLINK = re.compile(r"\[([^\]]+)\]\(#([^)]+)\)")
ROMAN = {"i","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii","xiii","xiv","xv","xvi","xvii","xviii","xix","xx"}

def relacion(label_n, head_n):
    if label_n == head_n: return True
    if head_n.startswith(label_n) or label_n.startswith(head_n): return True
    a, b = label_n.split(), head_n.split()
    n = 0
    for x, y in zip(a, b):
        if x != y: break
        n += len(x) + 1
    return n >= 12

def resuelve_cruceza(label, heads, slugs, slugset):
    """label tipo «09-15 (II)» → head cuyo norm = [2026, dd, mm, (romano)?, …]. ÚNICO."""
    t = norm(label).split()
    if len(t) < 2: return None
    dd, mm = t[0], t[1]
    rom = t[2] if len(t) > 2 and t[2] in ROMAN else None
    cands = []
    for h, s in zip(heads, slugs):
        ht = norm(h).split()
        if len(ht) < 4 or ht[0] != "2026" or ht[1] != dd or ht[2] != mm: continue
        if rom:
            if ht[3] == rom: cands.append(s)
        else:
            if ht[3] not in ROMAN: cands.append(s)
    if len(cands) == 1 and cands[0] in slugset:
        return cands[0]
    return None

def main():
    path = sys.argv[1]; aplicar = "--aplicar" in sys.argv
    raw = open(path, "rb").read()
    viejo_sello = hashlib.sha256(raw).hexdigest()[:16]
    d = raw.decode("utf-8"); lines = d.split("\n")
    heads, slugs = [], []
    used = set()
    for l in lines:
        m = HEAD.match(l)
        if m: heads.append(m.group(2).strip())
    slugs = [slug(h, used) for h in heads]
    slugset = set(slugs)
    es_toc = [bool(TOC_LINE.match(l)) for l in lines]
    bloques = []
    i = 0
    while i < len(lines):
        if es_toc[i]:
            j = i
            while j < len(lines) and es_toc[j]: j += 1
            bloques.append((i, j)); i = j
        else: i += 1
    en_toc = set()
    for bi, bj in bloques: en_toc.update(range(bi, bj))
    if not bloques:
        print("ABORTA: sin bloque TOC"); sys.exit(1)
    consumido = 0; nuevos = list(lines); ch_toc = []; ch_cuerpo = []
    # ── Fase 1: TOC monótono
    for bi, bj in bloques:
        for k in range(bi, bj):
            m = TOC_LINE.match(lines[k])
            pre, viejo_t, post = m.groups()
            label = re.match(r"^\s*-\s+\[([^\]]*)\]", lines[k]).group(1)
            ln = norm(label); elegido = None
            for h in range(consumido, len(heads)):
                if relacion(ln, norm(heads[h])):
                    elegido = h; break
            if elegido is None:
                print("ABORTA F1: entrada TOC sin encabezado compatible → L%d: %s" % (k + 1, label[:70])); sys.exit(1)
            consumido = elegido + 1
            nuevo_t = slugs[elegido]
            if nuevo_t != viejo_t:
                ch_toc.append((k + 1, viejo_t, nuevo_t))
                nuevos[k] = pre + "#" + nuevo_t + post   # FIX #27: el # se preserva SIEMPRE
            assert TOC_OK.match(nuevos[k]), "ABORTA F1: línea TOC malformada L%d" % (k + 1)
    # ── Fase 2: crucezas del cuerpo (solo targets MUERTOS)
    for k in range(len(lines)):
        if k in en_toc or not MDLINK.search(lines[k]): continue
        def rep(m):
            label, tgt = m.group(1), m.group(2)
            if tgt in slugset: return m.group(0)
            nuevo_t = resuelve_cruceza(label, heads, slugs, slugset)
            if nuevo_t is None:
                print("ABORTA F2: cruceza sin candidato único → L%d [%s](#%s)" % (k + 1, label, tgt)); sys.exit(1)
            ch_cuerpo.append((k + 1, tgt, nuevo_t))
            return "[%s](#%s)" % (label, nuevo_t)
        nuevos[k] = MDLINK.sub(rep, lines[k])
    # ── Verificación NO ciega (documento completo)
    pb = LINK.split(d); pa = LINK.split("\n".join(nuevos))
    assert len(pb) == len(pa), "ABORTA: cambió el número de anclas"
    assert pb[0::2] == pa[0::2], "ABORTA: texto fuera de targets alterado"
    muertos = [t for t in pa[1::2] if t not in slugset]
    if muertos:
        print("ABORTA: %d targets seguirían muertos: %s" % (len(muertos), muertos[:5])); sys.exit(1)
    print("heads %d · TOC %d entradas (%d targets corregidos) · cuerpo: %d crucezas corregidas · muertos post: 0/%d anclas" % (
        len(heads), sum(b - a for a, b in bloques), len(ch_toc), len(ch_cuerpo), len(pa[1::2])))
    for ln_, v, n in ch_toc[:6]: print("  TOC L%03d #%s → #%s" % (ln_, v, n))
    if len(ch_toc) > 6: print("  … y %d más en TOC" % (len(ch_toc) - 6))
    for ln_, v, n in ch_cuerpo[:8]: print("  cuerpo L%03d #%s → #%s" % (ln_, v, n))
    if len(ch_cuerpo) > 8: print("  … y %d más en cuerpo" % (len(ch_cuerpo) - 8))
    if aplicar:
        nd = "\n".join(nuevos).encode("utf-8")
        open(path, "wb").write(nd)
        print("APLICADO · sello %s → %s" % (viejo_sello, hashlib.sha256(nd).hexdigest()[:16]))
    else:
        print("PREVIEW (no escrito) · sello %s (sin cambio)" % viejo_sello)

if __name__ == "__main__":
    main()
