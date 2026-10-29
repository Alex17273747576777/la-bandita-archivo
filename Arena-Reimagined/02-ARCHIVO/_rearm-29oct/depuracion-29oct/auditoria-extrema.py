#!/usr/bin/env python3
import collections, csv, hashlib, json, re, zipfile
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); D=R/'02-ARCHIVO/_rearm-29oct'
WA=R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'; FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
INFORME=[]
def log(*a): INFORME.append(' '.join(str(x) for x in a)); print(*a)
hallazgos=[]
# ---------- A) manifiesto re-hasheado
mani={}
for ln in (D/'aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    s,n,b,h=ln.split('\t'); mani[(s,n)]=h
mal=0
for serie,carp in [('WhatsApp-dominicano-ES',WA),('Facebook-dominicano-ES',FB)]:
    for f in sorted(carp.glob('*.md')):
        h=hashlib.sha256(f.read_bytes()).hexdigest()
        if mani.get((serie,f.name))!=h: mal+=1; hallazgos.append(('MANIFIESTO',serie,f.name))
log(f'A) manifiesto: {len(mani)} entradas · discrepancias: {mal}')
# ---------- B) zip
z=zipfile.ZipFile(R/'ENTREGA-La-Bandita-29oct2026.zip')
log('B) zip íntegro:', z.testzip() is None, '· entradas:', len(z.namelist()))
# ---------- C) datasets unificados (placa -> verdad)
verdad={}
def put(slug,**kw):
    v=verdad.setdefault(slug.lower(),{})
    for k,x in kw.items():
        if x not in (None,'','sin resolver','NOASSERTION'): v[k]=x
for row in csv.DictReader(open(D/'datos-al-dia-29oct/repos-al-dia-29oct.tsv',encoding='utf-8'),delimiter='\t'):
    put(row['slug'],stars=row['stars'],lic=row['licencia'],creado=None)
def loadj(p):
    try: return json.load(open(p,encoding='utf-8'))
    except Exception: return []
for r in loadj(D/'creacion-fb-83-108/verificacion-fuentes-83-108.json'):
    if isinstance(r,dict) and 'slug' in r: put(r['slug'],stars=r.get('stars'),lic=r.get('lic_spdx'),creado=r.get('created'))
for p in ['investigacion-29oct/candidatos-nuevos-29oct.json','investigacion-29oct/radar-nuevo-29oct.json','investigacion-29oct/sucesores-verificados.json','investigacion-29oct/apps-traidas-por-el-dueno.json']:
    for r in loadj(D/p):
        if isinstance(r,dict) and r.get('slug'): put(r['slug'],stars=r.get('stars'),lic=r.get('license'),creado=r.get('created'))
lic_txt={}
try: lic_txt=json.load(open(D/'creacion-fb-83-108/licencias-por-texto-final.json',encoding='utf-8'))
except Exception: pass
for s,v in lic_txt.items():
    if v and v[0]=='ok': put(s,lic=v[1])
for r in loadj(D/'investigacion-29oct/licencias-nuevas-final.json'):
    if isinstance(r,dict) and r.get('match'): put(r['slug'],lic=r['match'])
for r in loadj(D/'descubrimiento-29oct/ejemplos-del-dueno.json'):
    if isinstance(r,dict) and r.get('slug'): put(r['slug'],stars=r.get('stars'),lic=r.get('license'),creado=r.get('created'))
for r in loadj(D/'descubrimiento-29oct/descubrimientos-confirmados.json'):
    if isinstance(r,dict) and r.get('slug'): put(r['slug'],stars=r.get('stars'),lic=r.get('license'),creado=r.get('created'))
for r in loadj(D/'descubrimiento-29oct/licencias-descubrimientos.json'):
    if isinstance(r,dict) and r.get('match'): put(r['slug'],lic=r['match'])
try:
    for row in csv.DictReader(open(D/'descubrimiento-29oct/busqueda-categorias-api.json',encoding='utf-8'),delimiter='\t'): pass
except Exception: pass
log('C) slugs con verdad consolidada:',len(verdad))
def num_es(s):
    s=s.replace(' ','')
    m=re.match(r'^(\d{1,3}(?:\.\d{3})+)$',s)
    if m: return int(s.replace('.',''))
    m=re.match(r'^(\d+),(\d+)$',s)
    if m: return int(m.group(1))*1000+int(round(float('0.'+m.group(2))*1000))
    return int(s) if s.isdigit() else None
# ---------- C2) placas de piezas nuevas vs verdad
conflictos=[]
def check_pieces():
    for f in sorted(FB.glob('*.md')):
        m=re.match(r'(\d+)-',f.name)
        if not m: continue
        n=int(m.group(1))
        if not (n>=83 or n==2 or n>=109): continue
        t=f.read_text(encoding='utf-8')
        if '**Placa-Licencia' not in t: continue
        for seg in re.split(r'(?=`[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+`)', t.split('**Placa-Licencia')[1]):
            mm=re.match(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`',seg)
            if not mm: continue
            slug=mm.group(1).lower(); v=verdad.get(slug)
            if not v: conflictos.append((f.name[:3],slug,'SLUG SIN VERDAD CONSOLIDADA')); continue
            head=seg[:90]
            ms=re.search(r'★([\d\.,]+)( mil)?',head)
            if ms and v.get('stars') not in (None,''):
                val=num_es(ms.group(1))*(1000 if ms.group(2) else 1) if ',' in ms.group(1) and not ms.group(2) else (int(float(ms.group(1).replace(',','.'))*1000) if ms.group(2) else num_es(ms.group(1)))
                try:
                    if val is not None and abs(val-int(v['stars']))>max(2,int(v['stars'])*0.02): conflictos.append((f.name[:3],slug,f"★ pieza={val} datos={v['stars']}"))
                except Exception: pass
            ml=re.search(r'licencia ([A-Za-z0-9\-\.]+)',head)
            if ml and v.get('lic'):
                if ml.group(1)!=v['lic']: conflictos.append((f.name[:3],slug,f"LIC pieza={ml.group(1)} datos={v['lic']}"))
            mc=re.search(r'creado el (\d{4})-(\d{2})-(\d{2})',seg[:140])
            if mc and v.get('creado'):
                if '-'.join(mc.groups())!=str(v['creado'])[:10]: conflictos.append((f.name[:3],slug,f"CREADO pieza={'-'.join(mc.groups())} datos={v['creado']}"))
check_pieces()
log('C2) conflictos placa↔datos en piezas nuevas:',len(conflictos))
for c in conflictos: log('   ',c)
# ---------- D) anomalías de texto en todo el corpus
sospechosos=[]
for carp in (WA,FB):
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8',errors='replace')
        if '�' in t: sospechosos.append((f.name,'MOJIBAKE �'))
        for pat in ['undefined','NaN','{{','}}','None,','json','TODO ','FIXME']:
            if pat in t: sospechosos.append((f.name,f'patrón {pat}'))
        if t.count('`')%2==1: sospechosos.append((f.name,'backticks impares'))
        paras=[p.strip() for p in t.split('\n\n') if len(p.strip())>120]
        dup=[p for p,c in collections.Counter(paras).items() if c>1]
        for p in dup: sospechosos.append((f.name,'párrafo duplicado: '+p[:60]))
        if t.count('💓 *PULSO 29-OCT-2026')>1 or t.count('Pulso de nacimiento 29-oct-2026')>1: sospechosos.append((f.name,'nota duplicada'))
log('D) anomalías de texto:',len(sospechosos))
for s in sospechosos: log('   ',s)
# ---------- E) TSV integridad
rows=list(csv.DictReader(open(D/'datos-al-dia-29oct/repos-al-dia-29oct.tsv',encoding='utf-8'),delimiter='\t'))
slugs=[r['slug'] for r in rows]
log('E) TSV filas:',len(rows),'· slugs duplicados:',[s for s,c in collections.Counter(slugs).items() if c>1])
# ---------- F) enlaces github en notas WA vs universo
uni=set(s.lower() for s in slugs)
faltan=set()
for f in sorted(WA.glob('*.md')):
    t=f.read_text(encoding='utf-8')
    for s in re.findall(r'github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',t):
        s=s.lower().rstrip('.,)')
        if s not in uni: faltan.add(s)
log('F) repos citados en WhatsApp fuera del universo de 753:',len(faltan),sorted(faltan)[:20])
json.dump({'manifiesto_discrepancias':mal,'conflictos':conflictos,'sospechosos':sospechosos,'wa_fuera_universo':sorted(faltan)},open(D/'depuracion-29oct/auditoria-extrema.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
log('\nRESUMEN: manifiesto',mal,'· conflictos',len(conflictos),'· anomalías',len(sospechosos))
