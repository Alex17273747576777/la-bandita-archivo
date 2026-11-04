#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# QUIRÚJANO RESPIRO+FRESCURA — cura: (1) aire entre líneas-lista, (2) bloques >380c partidos,
# (3) anclajes relativos anclados a fecha. Respeta fences. No toca ★ ni headers.
import sys, re
LISTISH = re.compile(r"^[·•—]|^—«|^Peldaño |^Taller \d|^Mito \d|^Caso \d|^Fila \d|^Cláusula \d|^Estación \d|^Hilo \d|^Día \d|^\d\. ")
SENT = re.compile(r"(?<=[\.\?\!…;])\s+|\s·\s")

def split_block(text, maxc=380, minc=130):
    if len(text) <= maxc or text.startswith("REV|") or text.startswith("(Las respuestas"): return [text]
    parts = SENT.split(text)
    chunks = []; cur = ""
    for p in parts:
        if not cur: cur = p
        elif len(cur) + 1 + len(p) <= maxc: cur += " " + p
        else: chunks.append(cur); cur = p
    if cur: chunks.append(cur)
    out = []
    for c in chunks:
        if out and len(c) < minc and len(out[-1]) + 1 + len(c) <= maxc: out[-1] += " " + c
        else: out.append(c)
    return out

def fix(path):
    L = open(path, encoding="utf-8").read().split("\n")
    # 1) frescura: anclar relativos sin fecha
    for i,l in enumerate(L):
        if re.search(r"[jJ]ueves", l) and re.search(r"mismo|MISMO|este", l) and "15-oct" not in l and "2026" not in l:
            L[i] = l.replace("jueves", "jueves 15-oct-2026")
        elif "esta tarde" in l and "15-oct" not in l and "2026" not in l:
            L[i] = l.replace("esta tarde", "esta tarde del 15-oct-2026")
        elif re.search(r"esta mañana", l) and "15-oct" not in l and "2026" not in l and not l.startswith("*"):
            L[i] = l.replace("esta mañana", "esta mañana del 15-oct-2026")
    # 2) aire entre líneas-lista consecutivas (fuera de fence)
    out = []; infence = False
    for l in L:
        if l.strip().startswith("```"):
            infence = not infence; out.append(l); continue
        if not infence and LISTISH.match(l) and out and out[-1] and LISTISH.match(out[-1]):
            out.append("")
        out.append(l)
    # 3) partir bloques >380 (fuera de fence)
    L = out; out = []; buf = []
    def flush():
        if not buf: return
        text = "\n".join(buf)
        chunks = split_block(text)
        for j,c in enumerate(chunks):
            if j: out.append("")
            out.append(c)
        buf.clear()
    for l in L:
        if l.strip().startswith("```"):
            flush(); infence = not infence; out.append(l); continue
        if infence: out.append(l); continue
        if l.strip()=="": flush(); out.append(l)
        elif l.startswith("REV|") or l.startswith("(Las respuestas"): out.append(l)
        else: buf.append(l)
    flush()
    d = "\n".join(out)
    while "\n\n\n" in d: d = d.replace("\n\n\n","\n\n")
    open(path, "w", encoding="utf-8").write(d)
    return len(d)

for p in sys.argv[1:]:
    n = fix(p)
    print("%s -> %dc %s" % (p.split('/')[-1][:2], n, "DENTRO" if 62000<=n<=64000 else "FUERA"))
