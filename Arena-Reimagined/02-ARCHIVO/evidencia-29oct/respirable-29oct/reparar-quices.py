#!/usr/bin/env python3
"""Repara los quices que el motor nunca pudo descifrar: sus respuestas venían en
líneas REV sueltas sin numerar. Se numeran al derecho (1=, 2=...) y se vuelve a
cifrar al revés en una sola línea: mismas respuestas, ahora sí descifrables."""
import re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
def descifra_ok(bloque_rev):
    segs=[s[4:] if s.startswith('REV|') else s for s in bloque_rev.replace('\n','|REV|').split('|REV|') if s]
    return any(re.match(r'^1\s*[=:]',s[::-1]) for s in segs)
def reparar(t):
    lineas=t.split('\n'); out=[]; i=0; n=0
    while i<len(lineas):
        if re.sub(r'^[*\s]+','',lineas[i]).startswith('Respuestas al rev'):
            out.append(lineas[i]); i+=1
            # recoger la zona REV hasta (Las respuestas
            zona=[]; j=i
            while j<len(lineas) and not lineas[j].startswith('(Las respuestas'):
                zona.append(lineas[j]); j+=1
            revs=[l for l in zona if l.startswith('REV|')]
            if revs and not descifra_ok('\n'.join(revs)):
                segs=[]
                for l in revs:
                    partes=[s for s in l.split('|REV|')]
                    for k,p in enumerate(partes):
                        p=p[4:] if k==0 and p.startswith('REV|') else p
                        if p.strip(): segs.append(p)
                planos=[s[::-1].strip() for s in segs]
                nueva='REV|' + '|REV|'.join(f'{k+1}={p}'[::-1] for k,p in enumerate(planos))
                out.append(''); out.append(nueva); n+=1; i=j; continue
            out.extend(zona); i=j; continue
        out.append(lineas[i]); i+=1
    return '\n'.join(out),n
tot=0
for carp in [R/'01-PUBLICACIONES/WhatsApp-dominicano-ES', R/'01-PUBLICACIONES/Facebook-dominicano-ES']:
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8'); nueva,n=reparar(t)
        if n: f.write_text(nueva,encoding='utf-8'); tot+=n
print('quices reparados (numerados y re-cifrados):',tot)
