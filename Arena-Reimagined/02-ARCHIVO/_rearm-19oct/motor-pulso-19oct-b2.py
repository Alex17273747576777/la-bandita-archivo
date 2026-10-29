# -*- coding: utf-8 -*-
"""Motor pulso 19-oct batch2: ★18oct->★19oct solo repos del batch2. Uso: dry|aplicar"""
import re, glob, sys, os
MODO=sys.argv[1] if len(sys.argv)>1 else "dry"
BASE="/home/user/Arena-Reimagined"
def fmt(n): return f"{n:,}".replace(",",".")
old={}
for ln in open(f"{BASE}/02-ARCHIVO/_rearm-18oct/censo-fresco-18oct-tarde.tsv",encoding="utf-8"):
    c=ln.rstrip("\n").split("\t")
    if len(c)>=5: old[c[0]]=int(c[1])
fresh={}
for ln in open(f"{BASE}/02-ARCHIVO/_rearm-19oct/censo-19oct-b2.tsv",encoding="utf-8"):
    c=ln.rstrip("\n").split("\t")
    if len(c)>=5: fresh[c[0]]={'s':int(c[1]),'push':c[3]}
tokmap={}
for r,v in fresh.items():
    if r in old and old[r]!=v['s'] and old[r]>=100: tokmap.setdefault("★"+fmt(old[r]),set()).add((r,"★"+fmt(v['s'])))
tok2repo={}; col=[]
for tok,dest in tokmap.items():
    if len({d[1] for d in dest})==1: tok2repo[tok]=next(iter(dest))
    else: col.append(tok)
print("tokens:",len(tok2repo),"colisiones excluidas:",col)
files=[f for pat in [f"{BASE}/01-PUBLICACIONES/WhatsApp-dominicano-ES/*.md",f"{BASE}/02-ARCHIVO/_fuentes-serie/pack-*.txt",f"{BASE}/packs/pack-*.txt"] for f in glob.glob(pat) if not f.endswith("LEEME-de-la-carpeta.md")]
def exc(f):
    b=os.path.basename(f); return bool(re.match(r"(9[6-9]|100)-",b) or re.match(r"pack-(9[6-9]|100)\.txt",b))
res=[]
for f in sorted(files):
    if exc(f): continue
    lineas=open(f,encoding="utf-8").read().split("\n"); camb=[]
    for i,ln in enumerate(lineas):
        ln0=ln
        for tok,(r,new) in sorted(tok2repo.items(),key=lambda x:-len(x[0])):
            if tok in ln: ln=ln.replace(tok,new)
        if ln!=ln0:
            ln=ln.replace("(pulso 18-oct-2026)","(pulso 19-oct-2026)").replace("(censo 18-oct-2026)","(censo 19-oct-2026)").replace("pulso 18-oct-2026","pulso 19-oct-2026").replace("censo 18-oct-2026","censo 19-oct-2026")
            camb.append(i+1); lineas[i]=ln
    if camb:
        res.append((os.path.basename(f)[:50],len(camb)))
        if MODO=="aplicar": open(f,'w',encoding="utf-8").write("\n".join(lineas))
for r,c in res: print(f"  {r}: {c}")
print("ARCHIVOS CON DELTA:",len(res), "APLICADO" if MODO=="aplicar" else "(dry)")
