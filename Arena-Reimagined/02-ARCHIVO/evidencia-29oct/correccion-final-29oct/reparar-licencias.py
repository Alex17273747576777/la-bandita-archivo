#!/usr/bin/env python3
import re, csv, textwrap
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
lic={}
with open(R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv',encoding='utf-8',newline='') as fh:
    for r in csv.DictReader(fh,delimiter='\t'): lic[r['slug'].lower()]=r['licencia']
MANUAL={'seedvault-app/seedvault':'Apache-2.0 (texto de su LICENSE leído el 29-oct-2026)',
        'naman14/timber':'sin archivo LICENSE en su repo (verificado el 29-oct-2026)'}
def estado_lic(slug):
    s=slug.lower()
    if s in MANUAL: return MANUAL[s]
    v=lic.get(s)
    if v is None: return None
    if v.startswith('presente-no-clasificado'): return 'licencia presente en su repo, no clasificada como SPDX (texto leído el 29-oct-2026)'
    if v.startswith('sin archivo LICENSE'): return 'sin archivo LICENSE en su repo (verificado por API 29-oct-2026)'
    return v
pat=re.compile(r'Licencias\s+sin\s+resolver\s+hoy\s+\(\d+\):\s+(.*?)\.\s+Sin\s+licencia\s+clara\s+no\s+hay\s+recomendación\s+completa:\s+queda\s+la\s+alerta\s+firmada\.|Licencias\s+sin\s+resolver\s+hoy\s+\(\d+\):\s+(.*?)\.\s+Sin\s+licencia\s+clara,\s+la\s+recomendación\s+queda\s+incompleta\s+y\s+así\s+se\s+firma\.',re.S)
def reemplazo(m):
    cuerpo=m.group(1) or m.group(2)
    slugs=re.findall(r'`([^`]+)`',cuerpo)
    partes=[]; faltan=[]
    for s in slugs:
        e=estado_lic(s)
        if e is None: faltan.append(s)
        else: partes.append(f'`{s}` — {e}')
    if faltan: print('REVISAR sin dato:',faltan); return m.group(0)
    txt='Licencias al 29-oct-2026 (resueltas hoy, sin inventar SPDX): '+ '; '.join(partes)+'.'
    return '\n'.join(textwrap.wrap(txt,width=96,break_long_words=False,break_on_hyphens=False))
tot=0; files=set()
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in sorted((R/'01-PUBLICACIONES'/serie).glob('*.md')):
        if f.name.startswith('LEEME'): continue
        t=f.read_text(encoding='utf-8'); nueva,n=pat.subn(reemplazo,t)
        if n: f.write_text(nueva,encoding='utf-8'); tot+=n; files.add(f.name)
print('frases de licencia corregidas:',tot,'en',len(files),'archivos')
