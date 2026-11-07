# -*- coding: utf-8 -*-
"""Motor pulso 19-oct: ★18oct→★19oct solo repos pulsados hoy (58). Tokens >=100,
colisiones de token viejo excluidas. Fechas de pulso/censo en líneas tocadas -> 19-oct.
Uso: motor-pulso-19oct.py dry|aplicar"""
import re, glob, sys, os
MODO=sys.argv[1] if len(sys.argv)>1 else "dry"
BASE="/home/user/Arena-Reimagined"
def fmt(n): return f"{n:,}".replace(",",".")
old={}; 
for ln in open(f"{BASE}/02-ARCHIVO/_rearm-18oct/censo-fresco-18oct-tarde.tsv",encoding="utf-8"):
    c=ln.rstrip("\n").split("\t")
    if len(c)>=5: old[c[0]]=int(c[1])
fresh={}
for ln in open(f"{BASE}/02-ARCHIVO/_rearm-19oct/censo-fresco-19oct-parcial.tsv",encoding="utf-8"):
    c=ln.rstrip("\n").split("\t")
    if len(c)>=5: fresh[c[0]]={'s':int(c[1]),'push':c[3]}
# colisiones: token viejo compartido por >1 repo con destinos distintos
tokmap={}
for r,v in fresh.items():
    if r in old and old[r]!=v['s'] and old[r]>=100:
        tokmap.setdefault("★"+fmt(old[r]),set()).add((r,"★"+fmt(v['s'])))
tok2repo={}; colisiones=[]
for tok,dest in tokmap.items():
    if len({d[1] for d in dest})==1: tok2repo[tok]=next(iter(dest))
    else: colisiones.append((tok,dest))
print("tokens a actualizar:",len(tok2repo),"colisiones excluidas:",colisiones)
files=[]
for pat in [f"{BASE}/01-PUBLICACIONES/WhatsApp-dominicano-ES/*.md", f"{BASE}/02-ARCHIVO/_fuentes-serie/pack-*.txt", f"{BASE}/packs/pack-*.txt"]:
    files+=glob.glob(pat)
files=[f for f in files if not f.endswith("LEEME-de-la-carpeta.md")]
# excluir 96-100 (agregados del censo: se actualizan con censo completo, no parcial)
def excluida(f):
    b=os.path.basename(f)
    m=re.match(r"(9[6-9]|100)-",b) or re.match(r"pack-(9[6-9]|100)\.txt",b)
    return bool(m)
resumen=[]
for f in sorted(files):
    if excluida(f): continue
    t0=open(f,encoding="utf-8").read(); lineas=t0.split("\n"); cambios=[]
    for i,ln in enumerate(lineas):
        ln0=ln
        for tok,(r,new) in sorted(tok2repo.items(), key=lambda x:-len(x[0])):
            if tok in ln: ln=ln.replace(tok,new)
        if ln!=ln0:
            ln=ln.replace("(pulso 18-oct-2026)","(pulso 19-oct-2026)").replace("(censo 18-oct-2026)","(censo 19-oct-2026)")
            ln=ln.replace("pulso 18-oct-2026","pulso 19-oct-2026").replace("censo 18-oct-2026","censo 19-oct-2026")
            # push HOY: si algún repo citado en la línea no empujó 19-oct, fecharlo
            if re.search(r"push de HOY|push HOY|empuje de HOY|push de hoy", ln):
                for r,v in fresh.items():
                    if fmt(v['s']) in ln and v['push']!="2026-10-19" and v['push'][5:7]=="10":
                        dia=v['push'][8:10].lstrip("0")+"-oct"
                        ln=re.sub(r"push de HOY|push HOY|empuje de HOY","push "+dia,ln,count=1)
                        ln=re.sub(r"push de hoy","push "+dia,ln,count=1)
                        break
            cambios.append(i+1); lineas[i]=ln
    if cambios:
        resumen.append((os.path.basename(f)[:56],len(cambios)))
        if MODO=="aplicar": open(f,'w',encoding="utf-8").write("\n".join(lineas))
for r,c in resumen: print(f"  {r}: {c} líneas")
print("ARCHIVOS CON DELTA:",len(resumen))
if MODO=="aplicar": print("APLICADO")
