#!/usr/bin/env python3
"""FORMATO RESPIRABLE v3 · Facebook y WhatsApp, según la especificación investigada.
Solo aire: trocea párrafos largos por frases (1-3 por bloque), aire entre elementos de
lista en Facebook, envuelve líneas >100. Guardián: secuencia de palabras idéntica."""
import re, textwrap
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
PALABRAS=re.compile(r'[^\W_]+',re.UNICODE)
palabras=lambda t: PALABRAS.findall(t.lower())
FRASE=re.compile(r'(?<=[.!?…])\s+(?=[A-ZÁÉÍÓÚÑ¿¡«*\d])')
def trocea(bloque):
    if len(bloque)<=240 or '\n' in bloque: return bloque
    if bloque.lstrip().startswith(('•','▸','━','#','>','-','*','💓','❝','«','📥','🧩')): return bloque
    frases=FRASE.split(bloque)
    if len(frases)<2: return bloque
    grupos=[]; actual=[]
    for fr in frases:
        actual.append(fr)
        if len(actual)>=2: grupos.append(' '.join(actual)); actual=[]
    if actual: grupos.append(' '.join(actual))
    return '\n\n'.join(grupos)
def envuelve(ln):
    if len(ln)<=100 or ln.startswith(('http','`','|','━')): return ln
    return '\n'.join(textwrap.wrap(ln,width=96,break_long_words=False,break_on_hyphens=False)) if not ln.lstrip().startswith(('•','·','▸')) else ln
def transforma(t,es_fb):
    bloques=t.split('\n\n')
    bloques=[trocea(b.strip('\n')) for b in bloques]
    t='\n\n'.join(bloques)
    lineas=[]
    for ln in t.split('\n'):
        ln=envuelve(ln)
        lineas.append(ln)
        if es_fb and re.match(r'^(•|·|\d+\.)\s',ln) and ln.strip():
            lineas.append('')
    t='\n'.join(lineas)
    t=re.sub(r'\n{3,}','\n\n',t)
    return t
def stats(carp):
    par=lin=arch=0
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8'); arch+=1
        par+=sum(1 for b in t.split('\n\n') if len(b)>240)
        lin+=sum(1 for l in t.split('\n') if len(l)>100)
    return arch,par,lin
res={}
for serie,carp,es_fb in [('WhatsApp-dominicano-ES',R/'01-PUBLICACIONES/WhatsApp-dominicano-ES',False),('Facebook-dominicano-ES',R/'01-PUBLICACIONES/Facebook-dominicano-ES',True)]:
    a0=stats(carp); ap=rej=0
    for f in sorted(carp.glob('*.md')):
        orig=f.read_text(encoding='utf-8'); nueva=transforma(orig,es_fb)
        if palabras(orig)!=palabras(nueva): rej+=1; continue
        if nueva!=orig: f.write_text(nueva,encoding='utf-8'); ap+=1
    a1=stats(carp); res[serie]=(a0,a1,ap,rej)
    print(f'{serie}: antes(párrafos>240={a0[1]}, líneas>100={a0[2]}) → después({a1[1]}, {a1[2]}) · transformadas {ap} · rechazadas {rej}')
