#!/usr/bin/env python3
import hashlib, json, re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); MIR=Path('/home/user/la-bandita-archivo')
html=(R/'02-ARCHIVO/catalogo-la-bandita.html').read_text(encoding='utf-8')
i=html.find('{"wa":')
dec=json.JSONDecoder(); data,_=dec.raw_decode(html,i)
print('catálogo embebido: WA',len(data['wa']),'· FB',len(data['fb']))
wa_files=sorted(f for f in (R/'01-PUBLICACIONES/WhatsApp-dominicano-ES').glob('*.md'))
fb_files=sorted(f for f in (R/'01-PUBLICACIONES/Facebook-dominicano-ES').glob('*.md') if not f.name.startswith('LEEME'))
emb_wa={p['file'] for p in data['wa']}; emb_fb={p['file'] for p in data['fb']}
fb_con_corazon=[f.name for f in fb_files if '💓' in f.read_text(encoding='utf-8')]
print('FB con 💓 (elegibles muro):',len(fb_con_corazon),'· en catálogo:',len(emb_fb),'· ¿todas?',set(fb_con_corazon)==emb_fb)
# textos embebidos idénticos a disco
dif=0
emb_map={p['file']:p['text'] for p in data['fb']}
for name in list(emb_fb)[:1000]:
    if emb_map[name] != (R/'01-PUBLICACIONES/Facebook-dominicano-ES'/name).read_text(encoding='utf-8'): dif+=1
print('FB textos embebidos != disco:',dif)
difw=0
emb_mapw={p['file']:p['text'] for p in data['wa']}
for name in emb_wa:
    p=R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'/name
    if p.exists() and emb_mapw[name] != p.read_text(encoding='utf-8'): difw+=1
print('WA textos embebidos != disco:',difw)
# colas WA: nota completa al final
mal_cola=[]
for p in data['wa']:
    t=p['text']
    if 'Vara de cierre' not in t[-600:]: mal_cola.append(p['file'][:3])
print('WA canon sin vara de cierre al final:',mal_cola)
# manifiesto SHA y espejo
man=[]; distintos=[]
for serie,carp in [('WhatsApp-dominicano-ES',R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'),('Facebook-dominicano-ES',R/'01-PUBLICACIONES/Facebook-dominicano-ES')]:
    for f in sorted(carp.glob('*.md')):
        b=f.read_bytes(); man.append((serie,f.name,len(b),hashlib.sha256(b).hexdigest()))
        mf=MIR/serie/f.name
        if not mf.exists() or mf.read_bytes()!=b: distintos.append(f'{serie}/{f.name}')
out=R/'02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv'
out.write_text('serie\tarchivo\tbytes\tsha256\n'+''.join(f'{a}\t{b}\t{c}\t{d}\n' for a,b,c,d in man),encoding='utf-8')
print(f'manifiesto: {len(man)} piezas · espejo distinto en: {distintos if distintos else "NINGÚN archivo"}')
for extra in ['02-ARCHIVO/catalogo-la-bandita.html','02-ARCHIVO/registro-2026-10-15.md']:
    a=(R/extra).read_bytes(); b=(MIR/extra).read_bytes() if (MIR/extra).exists() else b''
    print(extra,'espejo idéntico:',a==b)
