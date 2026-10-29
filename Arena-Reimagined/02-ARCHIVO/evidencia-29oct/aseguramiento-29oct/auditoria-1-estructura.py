#!/usr/bin/env python3
import json, re, csv
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
WA=R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'; FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
fallos=[]
# --- WA estructura
wa_files=sorted(f for f in WA.glob('*.md') if not f.name.startswith('LEEME'))
ids_wa={}
for f in wa_files:
    m=re.match(r'(\d+)-',f.name)
    if m: ids_wa.setdefault(int(m.group(1)),[]).append(f.name)
faltan_wa=[i for i in range(0,109) if i not in ids_wa]
nota_doble=[]; sin_nota=[]
for f in wa_files:
    t=f.read_text(encoding='utf-8')
    c=t.count('💓 *PULSO 29-OCT-2026')
    if c==0: sin_nota.append(f.name)
    if c>1: nota_doble.append((f.name,c))
print(f'WA: {len(wa_files)} archivos · ids 00-108 faltantes: {faltan_wa} · sin nota: {len(sin_nota)} · nota doble: {len(nota_doble)}')
if faltan_wa or sin_nota or nota_doble: fallos.append(f'WA estructura: faltan={faltan_wa} sin={sin_nota} dobles={nota_doble}')
# largos WA
fuera=[]
for f in wa_files:
    n=len(f.read_text(encoding='utf-8'))
    m=re.match(r'(\d+)-',f.name)
    if m and int(m.group(1))>=1 and not (60000<=n<=66000): fuera.append((f.name[:3],n))
print('WA fuera de banda 60-66k (canónicas de serie):',len(fuera), fuera[:10])
# --- FB estructura
fb_files=sorted(f for f in FB.glob('*.md') if not f.name.startswith('LEEME'))
ids_fb={}
for f in fb_files:
    m=re.match(r'(\d+)-',f.name)
    if m: ids_fb.setdefault(int(m.group(1)),[]).append(f.name)
faltan_fb=[i for i in range(0,132) if i not in ids_fb]
pulso_doble=[]; sin_pulso=[]; sin_titulo=[]; muy_corta=[]
for f in fb_files:
    t=f.read_text(encoding='utf-8')
    c=t.count('PULSO 29-OCT-2026')+t.count('Pulso de nacimiento 29-oct-2026')
    base=t.count('💓')
    if base==0: sin_pulso.append(f.name)
    if 'Pulso de nacimiento' in t and t.count('Pulso de nacimiento 29-oct-2026')>1: pulso_doble.append(f.name)
    if not t.startswith('# '): sin_titulo.append(f.name)
    if len(t)<1200 and int(re.match(r'(\d+)-',f.name).group(1))>=83: muy_corta.append((f.name[:3],len(t)))
print(f'FB: {len(fb_files)} archivos · ids únicos {len(ids_fb)} · faltantes 00-131: {faltan_fb} · sin 💓: {len(sin_pulso)} · sin título #: {len(sin_titulo)} · nacimiento doble: {len(pulso_doble)} · nuevas <1200c: {muy_corta}')
if faltan_fb or sin_pulso or sin_titulo or pulso_doble: fallos.append(f'FB estructura: faltan={faltan_fb} sinPulso={sin_pulso[:3]} sinTitulo={sin_titulo[:3]} dobles={pulso_doble}')
# --- cruce de placas de piezas nuevas FB contra datasets verificados
datasets=[]
for p in [R/'02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct/repos-al-dia-29oct.tsv',
          R/'02-ARCHIVO/_rearm-29oct/investigacion-29oct/apps-traidas-por-el-dueno.json',
          R/'02-ARCHIVO/_rearm-29oct/investigacion-29oct/candidatos-nuevos-29oct.json',
          R/'02-ARCHIVO/_rearm-29oct/investigacion-29oct/radar-nuevo-29oct.json',
          R/'02-ARCHIVO/_rearm-29oct/investigacion-29oct/sucesores-verificados.json',
          R/'02-ARCHIVO/_rearm-29oct/descubrimiento-29oct/ejemplos-del-dueno.json',
          R/'02-ARCHIVO/_rearm-29oct/descubrimiento-29oct/descubrimientos-confirmados.json',
          R/'02-ARCHIVO/_rearm-29oct/creacion-fb-83-108/verificacion-fuentes-83-108.json']:
    if not p.exists(): print('dataset ausente en proyecto (vive en GitHub):',p.name); continue
    if p.suffix=='.tsv':
        for row in csv.DictReader(open(p,encoding='utf-8'),delimiter='\t'): datasets.append(row['slug'].lower())
    else:
        for r in json.load(open(p,encoding='utf-8')):
            if isinstance(r,dict) and r.get('slug'): datasets.append(r['slug'].lower())
DS=set(datasets)
print('slugs con dato verificado en datasets locales:',len(DS))
no_verificadas={}
for f in fb_files:
    m=re.match(r'(\d+)-',f.name)
    if not m: continue
    n=int(m.group(1))
    if n<2 or (2<n<83): continue
    t=f.read_text(encoding='utf-8')
    for s in re.findall(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`', t):
        if s.lower() not in DS: no_verificadas.setdefault(f.name[:3],[]).append(s.lower())
print('placas en piezas nuevas NO cruzadas con dataset local:',no_verificadas)
if no_verificadas: fallos.append(f'placas sin cruce local: {no_verificadas}')
print('\nFALLOS:',fallos if fallos else 'NINGUNO en auditoría 1')
json.dump({'faltan_wa':faltan_wa,'sin_nota_wa':sin_nota,'nota_doble_wa':nota_doble,'faltan_fb':faltan_fb,'sin_pulso_fb':sin_pulso,'no_verificadas':no_verificadas,'wa_fuera_banda':fuera},open(R/'02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/auditoria-1.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
