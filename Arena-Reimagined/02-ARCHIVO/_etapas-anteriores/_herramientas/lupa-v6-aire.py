#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# LUPA v6 "AIRE" — mide lo que v4/v5 NO medían: respiro, frescura, dialecto.
# Nace del señalamiento del dueño (15-oct noche): "siguen sin ser respirables,
# la info no está 100% al día, la infraestructura actúa bizarra". Defecto->cicatriz.
import sys, os, re, hashlib, json

REVLINE = re.compile(r"^REV\|")
LISTISH = re.compile(r"^[·•—]|^—«|^Peldaño |^Taller \d|^Mito \d|^Caso \d|^Fila \d|^Cláusula \d|^Estación \d|^Hilo \d|^Día \d")
RELATIVE = re.compile(r"\b(hoy|mañana|ayer|este jueves|mismo jueves|MISMO jueves|esta tarde|la tarde del censo|matinal|al cierre)\b")

def medir(path):
    d = open(path, encoding="utf-8").read()
    L = d.split("\n")
    total = len(d)
    # --- respiro ---
    blocks = []  # (start_line, len_chars, text)
    cur = []; start = 1; infence = False; run = 0; maxrun = 0
    air = 0
    for i, l in enumerate(L, 1):
        if l.strip().startswith("```"):
            infence = not infence
            if cur: blocks.append((start, sum(len(x)+1 for x in cur)-1, "\n".join(cur))); cur=[]; start=i+1
            continue
        if infence: continue
        if l.strip()=="":
            air += 1
            if cur: blocks.append((start, sum(len(x)+1 for x in cur)-1, "\n".join(cur))); cur=[]; start=i+1
            maxrun = max(maxrun, run); run = 0
        else:
            if not cur: start = i
            cur.append(l); run += 1
    if cur: blocks.append((start, sum(len(x)+1 for x in cur)-1, "\n".join(cur)))
    maxrun = max(maxrun, run)
    over380 = [(s,n) for s,n,t in blocks if n > 380 and not (len(t.split(chr(10)))==1 and (t.startswith("REV|") or t.startswith("(Las respuestas")))]
    over700 = [(s,n) for s,n,t in blocks if n > 700]
    p380 = 100.0*len(over380)/max(1,len(blocks))
    # --- frescura (fuera de fences) ---
    rel = []
    infence=False
    for i,l in enumerate(L,1):
        if l.strip().startswith("```"): infence = not infence; continue
        if infence: continue
        if "2026" in l or "15-oct" in l: continue
        m = RELATIVE.search(l)
        if m: rel.append((i, m.group(1), l.strip()[:70]))
    hoy = [ (i,l.strip()[:60]) for i,l in enumerate(L,1) if re.search(r"\bhoy\b", l) and "censo abierto" not in l ]
    # --- dialecto ---
    rev = sum(1 for l in L if l.startswith("REV|"))
    fences = sum(1 for l in L if l.strip().startswith("```"))
    return dict(path=path, total=total, blocks=len(blocks), maxblock=max((n for _,n,_ in blocks), default=0),
                over380=len(over380), over700=len(over700), pct380=round(p380,1),
                maxrun=maxrun, blanks=air, rel=len(rel), rel_top=rel[:6], hoy=len(hoy), rev=rev, fences=fences//2)

if __name__ == "__main__":
    d = sys.argv[1]
    files = sorted(f for f in os.listdir(d) if f.endswith(".md") and not f.startswith("LEEME"))
    print("%-6s %7s %5s %6s %5s %5s %5s %4s %4s %4s %4s" % ("pieza","bytes","maxP",">380",">700","%>380","sinAire","rel","hoy","REV","fence"))
    for f in files:
        m = medir(os.path.join(d,f))
        tag = f[:2]
        print("%-6s %7d %5d %5d %5d %5s %5d %4d %4d %4d %5d" % (tag, m["total"], m["maxblock"], m["over380"], m["over700"], str(m["pct380"])+"%", m["maxrun"], m["rel"], m["hoy"], m["rev"], m["fences"]))
        for i,pat,txt in m["rel_top"][:3]:
            print("         L%d [%s] %s" % (i,pat,txt))
