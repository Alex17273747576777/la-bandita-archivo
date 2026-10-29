#!/usr/bin/env python3
"""NIVEL 4 · placas impresas vs medición fresca. NIVEL 5 · estrés de hash repetido/paralelo."""
import concurrent.futures, hashlib, json, re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); D=R/'02-ARCHIVO/_rearm-29oct/chequeo-bitxbit-29oct'; FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
fresh=json.load(open(D/'prueba-03-comparativa.json',encoding='utf-8'))['repos']
def num(s):
    s=s.strip()
    if re.match(r'^\d{1,3}(\.\d{3})+$',s): return int(s.replace('.',''))
    if re.match(r'^\d+,\d+$',s): return int(float(s.replace(',','.'))*1000)
    return int(s) if s.isdigit() else None
desv=[]
for f in sorted(FB.glob('*.md')):
    m=re.match(r'(\d+)-',f.name)
    if not m or not (int(m.group(1))>=83 or int(m.group(1))==2): continue
    t=f.read_text(encoding='utf-8')
    for seg in re.findall(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`[^•\n]{0,80}?★\s*([\d\.,]+)( mil)?',t):
        slug,val,mil=seg[0].lower(),num(seg[1]),seg[2]
        if val is None or slug not in fresh or fresh[slug].get('http')!=200: continue
        if mil: val=int(val*1000) if val<1000 else val
        real=fresh[slug]['stars']
        if abs(val-real)>max(3,real*0.03): desv.append((f.name[:3],slug,val,real))
print('NIVEL 4 · placas FB nuevas fuera de tolerancia vs fresco:',desv if desv else 'NINGUNA')
mani={}
for ln in (R/'02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    s,n,b,hh=ln.split('\t'); mani[(s,n)]=hh
archivos=[(s,R/'01-PUBLICACIONES'/s/n) for (s,n) in mani]
def pasada(_):
    return all(hashlib.sha256(p.read_bytes()).hexdigest()==mani[(s,p.name)] for s,p in archivos)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    resultados=list(ex.map(pasada,range(5)))
print('NIVEL 5 · 5 pasadas paralelas de hash sobre 261 piezas, todas idénticas al manifiesto:',resultados)
json.dump({'desviaciones_placa':desv,'hash_pasadas':resultados},open(D/'prueba-04-05.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
