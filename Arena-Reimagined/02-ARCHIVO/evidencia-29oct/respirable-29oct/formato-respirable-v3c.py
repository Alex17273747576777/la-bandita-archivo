#!/usr/bin/env python3
"""v3c · troceo real (normaliza el envolvido antes de buscar frases) y placas compactas:
los atributos · cuelgan de su viñeta sin blancos entre ellos; el aire va ENTRE placas."""
import re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
PALABRAS=re.compile(r'[^\W_]+',re.UNICODE)
palabras=lambda t: PALABRAS.findall(t.lower())
LIMPIO=re.compile(r'(?<![\dA-ZÁÉÍÓÚÑ]\.)(?<=[.!?…])\s+(?=[A-ZÁÉÍÓÚÑa-záéíóúñ¿¡«*\d])')
def es_prosa(s):
    return not any(l.lstrip().startswith(('•','▸','━','#','>','-','💓','📥','🧩','·')) for l in s.split('\n'))
def trocea(bloque):
    s=bloque.strip('\n')
    if len(s)<=240 or not es_prosa(s): return bloque
    plano=re.sub(r'\s+',' ',s)
    frases=LIMPIO.split(plano)
    if len(frases)<2:
        if len(plano)>340 and '; ' in plano:
            partes=plano.split('; '); grupos=[]; actual=[]
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
def compacta_placas(t):
    lineas=t.split('\n'); out=[]
    for i,ln in enumerate(lineas):
        if ln=='' and out:
            prev=out[-1]
            nxt=lineas[i+1] if i+1<len(lineas) else ''
            if (prev.startswith('•') or prev.startswith('·')) and nxt.startswith('·'):
                continue
        out.append(ln)
    return '\n'.join(out)
def stats(carp):
    return sum(1 for f in carp.glob('*.md') for b in f.read_text(encoding='utf-8').split('\n\n') if len(b)>240)
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    carp=R/'01-PUBLICACIONES'/serie; antes=stats(carp); ap=rej=0
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8')
        nueva='\n\n'.join(trocea(b) for b in t.split('\n\n'))
        if serie.startswith('Facebook'): nueva=compacta_placas(nueva)
        nueva=re.sub(r'\n{3,}','\n\n',nueva)
        if palabras(t)!=palabras(nueva): rej+=1; continue
        if nueva!=t: f.write_text(nueva,encoding='utf-8'); ap+=1
    print(f'{serie}: párrafos>240 {antes} → {stats(carp)} · tocadas {ap} · rechazadas {rej}')
