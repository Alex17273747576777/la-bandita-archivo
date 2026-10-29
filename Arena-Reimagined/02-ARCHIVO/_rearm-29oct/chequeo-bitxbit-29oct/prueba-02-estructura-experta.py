#!/usr/bin/env python3
"""NIVEL 2 · estrés estructural y de caracteres, pieza por pieza (v2 corregida)."""
import collections, json, re, unicodedata
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); OUT=R/'02-ARCHIVO/_rearm-29oct/chequeo-bitxbit-29oct'
hallazgos=[]
def rev(f):
    b=f.read_bytes(); t=b.decode('utf-8')
    if b'\r\n' in b: hallazgos.append((f.name,'CRLF'))
    if b.startswith(b'\xef\xbb\xbf'): hallazgos.append((f.name,'BOM'))
    if not t.endswith('\n'): hallazgos.append((f.name,'sin newline final'))
    ctrl=sorted({c for c in t if unicodedata.category(c)=='Cc' and c not in '\n\t'})
    if ctrl: hallazgos.append((f.name,f'chars de control: {[hex(ord(c)) for c in ctrl]}'))
    if t.count('```')%2==1: hallazgos.append((f.name,'vallas ``` impares'))
    if t.count('**')%2==1: hallazgos.append((f.name,'negritas ** impares'))
    nb=t.count('\u00a0')
    if nb: hallazgos.append((f.name,f'NBSP x{nb}'))
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in sorted((R/'01-PUBLICACIONES'/serie).glob('*.md')): rev(f)
resumen=collections.Counter(h[1].split(' x')[0] for h in hallazgos)
print('NIVEL 2 · hallazgos por tipo:',dict(resumen))
for h in hallazgos[:15]: print('  ',h)
h=(R/'02-ARCHIVO/catalogo-la-bandita.html').read_text(encoding='utf-8')
data=None
for i in range(25):
    j=h.find('{"wa":'); data,_=json.JSONDecoder().raw_decode(h,j)
def pid(name):
    m=re.match(r'(\d+)-',name); return int(m.group(1)) if m else -1
gwa=collections.defaultdict(list); gfb=collections.defaultdict(list)
for p in data['wa']: gwa[pid(p['file'])].append(p)
for p in data['fb']: gfb[pid(p['file'])].append(p)
print(f'catálogo estrés: 25 parses OK · grupos WA {len(gwa)} (esperados 109) · grupos FB {len(gfb)} (esperados 132)')
print('  huecos WA:',[i for i in range(109) if i not in gwa],'· huecos FB:',[i for i in range(132) if i not in gfb])
faltan=[p['file'] for p in data['wa']+data['fb'] if not all(p.get(k) for k in ('file','title','text'))]
print('  piezas con campos vacíos:',faltan)
colas=[p['file'][:3] for p in data['wa'] if '💓' not in p['text'][-4500:]]
print('  WA embebidas sin 💓 en la cola:',colas)
json.dump({'hallazgos':hallazgos,'resumen':dict(resumen),'grupos_wa':len(gwa),'grupos_fb':len(gfb),'faltan_campos':faltan},open(OUT/'prueba-02-resultado.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
