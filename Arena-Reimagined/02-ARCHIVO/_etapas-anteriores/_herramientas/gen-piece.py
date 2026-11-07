#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GENERADOR DE PIEZAS DE LA SERIE — pack.txt con marcadores =====S01===== … =====S13===== / =====GLOS=====
# (glos = entradas únicas de la pieza; se suman al glosario base de la familia cosecha)
# Luego invoca montador-serie.py (ensambla, invierte quiz, parte >380, valida, escribe con sello).
import sys, os, re, subprocess
NN=sys.argv[1]; SLUG=sys.argv[2]; PACK=sys.argv[3]
D=f"/tmp/p{NN}"; os.makedirs(D,exist_ok=True)
for f in os.listdir(D):
    if re.match(r"s\d+\.txt|glos\.txt",f): os.remove(os.path.join(D,f))
raw=open(PACK,encoding='utf-8').read()
parts=re.split(r"=====(S\d+|GLOS)=====\n",raw)
# parts: ['', 'S01', contenido, 'S02', contenido, ...]
it=iter(parts[1:])
glos_extra=""
for k,v in zip(it,it):
    v=v.strip("\n")
    if k=="GLOS": glos_extra=v
    else: open(f"{D}/{k.lower()}.txt",'w',encoding='utf-8').write(v+"\n")
base=open("_herramientas/familia-cosecha/glos-base.txt",encoding='utf-8').read().rstrip("\n")
glos_paras="\n\n".join(l for l in glos_extra.split("\n") if l.strip())
open(f"{D}/glos.txt",'w',encoding='utf-8').write(base+("\n\n"+glos_paras if glos_paras else "")+"\n")
print(f"piezas escritas en {D} · glos extra {len(glos_extra)}c")
r=subprocess.run([sys.executable,"_herramientas/montador-serie.py",NN,SLUG],capture_output=True,text=True)
print(r.stdout, r.stderr)
sys.exit(r.returncode)
