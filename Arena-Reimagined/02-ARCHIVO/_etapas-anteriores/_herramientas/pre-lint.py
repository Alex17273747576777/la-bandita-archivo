#!/usr/bin/env python3
"""Pre-lint v3: replica el pipeline del montador (split incluido) y reporta lo que él vería."""
import sys, re
from collections import Counter
p=sys.argv[1]
texto=open(p,encoding='utf-8').read()
texto="\n".join(("REV|"+l[10:][::-1] if l.startswith(">>>REV>>> ") else l) for l in texto.split("\n"))
def bloques(t):
    L=t.split("\n"); bs=[];cur=[];inf=False
    for l in L:
        if l.strip().startswith("```"):
            if cur: bs.append("\n".join(cur)); cur=[]
            inf=not inf; continue
        if inf: continue
        if l.strip()=="":
            if cur: bs.append("\n".join(cur)); cur=[]
            continue
        cur.append(l)
    if cur: bs.append("\n".join(cur))
    return bs
def split_blk(b):
    fr=[];buf=""
    for sent in re.split(r"(?<=[.!?…]) +", b):
        if len(buf)+len(sent)+1<=380: buf=(buf+" "+sent).strip()
        else:
            if buf: fr.append(buf)
            buf=sent
    if buf: fr.append(buf)
    out=[]
    for x in fr:
        if len(x)<=380: out.append(x); continue
        buf=""
        for part in x.split(" · "):
            cand=(buf+" · "+part) if buf else part
            if len(cand)<=380: buf=cand
            else:
                if buf: out.append(buf)
                buf=part
        if buf: out.append(buf)
    return out
nuevos=[]
for b in bloques(texto):
    if len(b)>380 and not (len(b.split("\n"))==1 and (b.startswith("REV|") or b.startswith("(Las respuestas"))):
        nuevos.extend(split_blk(b))
    else: nuevos.append(b)
tf="\n\n".join(nuevos)
L=tf.split("\n")
blocks=[];cur=[];inf=False
for l in L:
    if l.strip().startswith("```"):
        if cur: blocks.append("\n".join(cur)); cur=[]
        inf=not inf; continue
    if inf: continue
    if l.strip()=="":
        if cur: blocks.append("\n".join(cur)); cur=[]
        continue
    cur.append(l)
if cur: blocks.append("\n".join(cur))
real=[b for b in blocks if not (len(b.split("\n"))==1 and (b.startswith("REV|") or b.startswith("(Las respuestas")))]
errs=[]
if "=====GLOS=====" not in open(p,encoding='utf-8').read(): errs.append("FALTA =====GLOS=====")
c=Counter()
for b in real:
    w=b.split()
    if len(w)>=2: c[(w[0].strip("*"),w[1].strip("*"))]+=1
for k,v in c.items():
    if v>=5 and k!=("No","dice"): errs.append(f"arranque x{v}: {k}")
nodice=[b for b in real if b.strip().startswith("No dice")]
if len(nodice)<5: errs.append(f"'No dice' x{len(nodice)} <5")
sindate=[l for l in L if (not l.startswith("REV|")) and "★" in l and re.search(r"★\s*\d", l) and not any(y in l for y in ("2023","2024","2025","2026"))]
for l in sindate: errs.append("★sinFecha: "+l[:80])
in_f=False
for b in bloques(open(p,encoding='utf-8').read()):
    if b.strip().startswith("```"): in_f=not in_f; continue
    if in_f or b.startswith("REV|"): continue
    for sent in re.split(r"(?<=[.!?…]) +", b):
        if len(sent)>380: errs.append(f"FRASE {len(sent)}c >380: {sent[:70]}")
print("\n".join(errs) if errs else "PACK LIMPIO ✓")
