#!/usr/bin/env python3
"""DESMETA · fuera el meta-comentario genérico que opaca la información central.
Se retira SOLO sección ritual repetida (reglas de la casa, vara, pieza madre en FB;
última aguja y cartas al lector en WA). Lo que queda no se toca ni en una coma."""
import re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
def desmeta_fb_md(t):
    lineas=t.split('\n'); out=[]; i=0; quitadas=0
    while i<len(lineas):
        ln=lineas[i]
        if re.match(r'^## (📦|⚖|🧭 La pieza madre)',ln):
            quitadas+=1; i+=1
            while i<len(lineas) and not lineas[i].startswith('## '): i+=1
            continue
        out.append(ln); i+=1
    return '\n'.join(out),quitadas
def desmeta_fb_vieja(t):
    segs=re.split(r'(━{5,}\n?)',t)
    out=[]; quitadas=0; j=0
    while j<len(segs):
        seg=segs[j]
        cab=seg.strip().split('\n')[0] if seg.strip() else ''
        if any(k in cab for k in ['REGLAS DE LA CASA','LA VARA','PIEZA MADRE']) and j>0:
            quitadas+=1
            if out and re.fullmatch(r'━{5,}\n?',out[-1]): out.pop()
            j+=1; continue
        out.append(seg); j+=1
    return ''.join(out),quitadas
def desmeta_wa(t):
    lineas=t.split('\n'); out=[]; i=0; quitadas=0
    while i<len(lineas):
        ln=lineas[i]
        if re.match(r'^\*[^*]*(ÚLTIMA AGUJA|CARTAS AL LECTOR)[^*]*\*$',ln.strip()):
            quitadas+=1; i+=1
            while i<len(lineas) and not re.match(r'^\*[^*]{3,}\*$',lineas[i].strip()): i+=1
            continue
        out.append(ln); i+=1
    return '\n'.join(out),quitadas
for serie,esfb in [('Facebook-dominicano-ES',True),('WhatsApp-dominicano-ES',False)]:
    carp=R/'01-PUBLICACIONES'/serie; piezas=secciones=chars=0
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8')
        if esfb:
            nueva,q=desmeta_fb_md(t)
            if q==0: nueva,q=desmeta_fb_vieja(t)
        else:
            nueva,q=desmeta_wa(t)
        nueva=re.sub(r'\n{3,}','\n\n',nueva)
        if q:
            f.write_text(nueva,encoding='utf-8'); piezas+=1; secciones+=q; chars+=len(t)-len(nueva)
    print(f'{serie}: {piezas} piezas limpiadas · {secciones} secciones rituales fuera · {chars:,} caracteres de meta retirados')
