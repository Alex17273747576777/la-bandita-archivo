#!/usr/bin/env python3
"""Refuerzo v3b: trocea también frases con minúscula tras el punto y oraciones únicas
largas por su punto y coma. Mismo guardián de palabras idénticas."""
import re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
PALABRAS=re.compile(r'[^\W_]+',re.UNICODE)
palabras=lambda t: PALABRAS.findall(t.lower())
LIMPIO=re.compile(r'(?<![\dA-ZÁÉÍÓÚÑ]\.)(?<=[.!?…])\s+(?=[A-ZÁÉÍÓÚÑa-záéíóúñ¿¡«*\d])')
def trocea(bloque):
    s=bloque.strip('\n')
    if len(s)<=240 or '\n' in s: return bloque
    if s.lstrip().startswith(('•','▸','━','#','>','-','💓','❝','«','📥','🧩','*')): return bloque
    frases=LIMPIO.split(s)
    if len(frases)<2:
        # oración única muy larga: respiro por punto y coma
        if len(s)>340 and '; ' in s:
            partes=s.split('; ')
            grupos=[]; actual=[]
            for p in partes:
                actual.append(p)
                if sum(len(x) for x in actual)>200: grupos.append('; '.join(actual)); actual=[]
            if actual: grupos.append('; '.join(actual))
            return '\n\n'.join(grupos)
        return bloque
    grupos=[]; actual=[]
    for fr in frases:
        actual.append(fr)
        if len(actual)>=2: grupos.append(' '.join(actual)); actual=[]
    if actual: grupos.append(' '.join(actual))
    return '\n\n'.join(grupos)
def stats(carp):
    par=0
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8'); par+=sum(1 for b in t.split('\n\n') if len(b)>240)
    return par
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    carp=R/'01-PUBLICACIONES'/serie; antes=stats(carp); ap=rej=0
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8')
        nueva='\n\n'.join(trocea(b) for b in t.split('\n\n'))
        if palabras(t)!=palabras(nueva): rej+=1; continue
        if nueva!=t: f.write_text(nueva,encoding='utf-8'); ap+=1
    print(f'{serie}: párrafos>240 {antes} → {stats(carp)} · tocadas {ap} · rechazadas {rej}')
