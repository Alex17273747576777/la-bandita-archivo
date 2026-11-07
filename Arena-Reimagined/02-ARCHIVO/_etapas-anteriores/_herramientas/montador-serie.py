#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MONTADOR DE LA SERIE 21-178 — ensambla secciones /tmp/pNN/s*.txt + glos.txt,
# invierte quiz (>>>REV>>> x -> REV| reverse), parte bloques >380 por frases,
# valida banda/★/FE0F/litanía/quiz y escribe la pieza final con su nombre canónico.
# USO: python3 montador-serie.py <NN> <slug-sin-NN>
import re, sys, os, hashlib
from collections import Counter
NN=sys.argv[1]; SLUG=sys.argv[2]
D=f"/tmp/p{NN}"
orden=[f"{D}/s{i:02d}.txt" for i in range(1,11)]+[f"{D}/s12.txt",f"{D}/glos.txt",f"{D}/s13.txt",f"{D}/s11.txt"]
texto="\n\n".join(open(p,encoding='utf-8').read().rstrip("\n") for p in orden)+"\n"
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
        for p in x.split(" · "):
            cand=(buf+" · "+p) if buf else p
            if len(cand)<=380: buf=cand
            else:
                if buf: out.append(buf)
                buf=p
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
over=[b for b in real if len(b)>380]
sindate=[l for l in L if (not l.startswith("REV|")) and "★" in l and re.search(r"★\s*\d", l) and not any(y in l for y in ("2023","2024","2025","2026"))]
heads=[l for l in L if re.match(r"^\*[^*\n]+\*$", l)]
fe0f=[h for h in heads if "\ufe0f" in h]
c=Counter()
for b in real:
    w=b.split()
    if len(w)>=2: c[(w[0].strip("*"),w[1].strip("*"))]+=1
lits=[(k,v) for k,v in c.items() if v>=5]
qs=[l for l in L if l.startswith("REV|")]
dec=[l[4:][::-1] for l in qs]
ok = 62000<=len(tf)<=64000 and len(over)==0 and len(sindate)==0 and len(fe0f)==0 and len(lits)==1 and lits[0][0]==("No","dice") and len(qs)==5
print(f"pieza {NN}: {len(tf)}c · >380:{len(over)} · ★sinFecha:{len(sindate)} · FE0F:{len(fe0f)} · litanías:{lits} · REV|:{len(qs)}")
for b in over[:4]: print("  OVER:",len(b),repr(b[:90]))
for l in sindate: print("  STARFANTASMA:",repr(l[:120]))
if not ok:
    print("REVISAR ✗"); sys.exit(1)
dest=f"/home/user/Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES/{NN}-{SLUG}-WhatsApp-La-Bandita-2026-10-15-dominicano-ES.md"
open(dest,'w',encoding='utf-8').write(tf)
print("ESCRITA:",dest)
print("SHA-256 16h:",hashlib.sha256(tf.encode()).hexdigest()[:16])
