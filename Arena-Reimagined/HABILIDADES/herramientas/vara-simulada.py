#!/usr/bin/env python3
"""VARA SIMULADA · replica fiel de laVara() del catálogo, sin navegador.
Si esto no dice OK, el catálogo NO se entrega: nada de descubrir los fallos en el teléfono del dueño."""
import hashlib, json, re
from pathlib import Path
R=Path(__file__).resolve().parents[2]
html=(R/'02-ARCHIVO/catalogo-la-bandita.html').read_text(encoding='utf-8')
i=html.find('{"wa":'); D,_=json.JSONDecoder().raw_decode(html,i)
m=re.search(r'D\.fb\.length!==(\d+)',html); ESPERA=int(m.group(1)) if m else None
def blocks(text):
    L=text.split('\n'); out=[]; buf=[]; inf=False
    def flush():
        if buf: out.append({'raw':'\n'.join(buf),'fence':False}); buf.clear()
    for l in L:
        if l.strip().startswith('```'):
            flush(); out.append({'raw':l,'fence':True}); inf=not inf; continue
        if inf: out.append({'raw':l,'fence':True}); continue
        if l.strip()=='': flush(); continue
        buf.append(l)
    flush(); return out
def health(text):
    bs=[b for b in blocks(text) if not b['fence'] and not re.match(r'^(REV\||\(Las respuestas)',b['raw'])]
    return {'over':sum(1 for b in bs if len(b['raw'])>380),'max':max((len(b['raw']) for b in bs),default=0)}
def extractQuiz(text):
    L=text.split('\n'); found=[]
    for i,l in enumerate(L):
        if re.sub(r'^[*\s]+','',l).startswith('Respuestas al rev'): found.append(i)
    res=[]
    for i0 in found:
        j=i0+1
        while j<len(L) and L[j].strip()=='': j+=1
        rev=''
        while j<len(L) and L[j].startswith('REV|'): rev+=(('\n' if rev else '')+L[j]); j+=1
        ans=''
        if not rev and j<len(L) and re.match(r'^\d+\s*:',L[j]): ans=L[j]
        res.append({'rev':rev,'ans':ans})
    return res
def descifra(qz):
    if qz['rev']:
        segs=[s for s in qz['rev'].replace('\n','|REV|').split('|REV|')]
        segs=[s[4:] if s.startswith('REV|') else s for s in segs if s]
        return [s[::-1] for s in segs]
    items=[]
    for it in re.split(r'\s+—\s+',qz['ans']):
        m=re.match(r'^(\d+)\s*:\s*([\s\S]*)$',it)
        items.append((m.group(1)+': '+m.group(2)[::-1]) if m else it)
    return items
fallos=[]; nquiz=0
for p in D['wa']:
    if len(p['text'])!=p['len']: fallos.append(f"cps≠len en #{p['id']}")
    h=health(p['text'])
    if h!=p['health']: fallos.append(f"salud≠sello en #{p['id']} (catálogo {p['health']} vs real {h})")
    if not re.fullmatch(r'[0-9a-f]{16}',p['sha']): fallos.append(f"sello inválido en #{p['id']}")
    for qz in extractQuiz(p['text']):
        nquiz+=1
        if not any(re.match(r'^1\s*[=:]',d) for d in descifra(qz)): fallos.append(f"quiz no descifra en #{p['id']}")
    if '💓' not in p['text']: fallos.append(f"WA sin 💓: #{p['id']}")
if ESPERA is not None and len(D['fb'])!=ESPERA: fallos.append(f'FB≠{ESPERA}')
for p in D['fb']:
    if '💓' not in p['text']: fallos.append('FB sin 💓: '+p['file'])
    if len(p['text'])!=p['len']: fallos.append('FB cps≠len: '+p['file'])
    for qz in extractQuiz(p['text']):
        nquiz+=1
        if not any(re.match(r'^1\s*[=:]',d) for d in descifra(qz)): fallos.append('quiz FB no descifra: '+p['file'])
print(f'vara simulada: WA {len(D["wa"])} · FB {len(D["fb"])} (esperados {ESPERA}) · quices {nquiz} · fallos: {fallos if fallos else "NINGUNO — VARA APROBADA ✓"}')
