#!/usr/bin/env python3
"""FORMATO RESPIRABLE v2 · solo aire, cero palabras tocadas.
Reglas (layout únicamente): mapa mental en dos líneas por familia; placas una por bloque
con sus datos en líneas propias; aire entre bloques. Prueba: la secuencia de PALABRAS
de cada archivo debe ser idéntica antes y después; si una sola difiere, ese archivo no se toca."""
import re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
PALABRAS=re.compile(r'[^\W_]+',re.UNICODE)
def palabras(t): return PALABRAS.findall(t.lower())
def transforma(t):
    out=[]
    for ln in t.split('\n'):
        m=re.match(r'^• (.+?) → (.+?) → (.+)$',ln)
        if m and 'Mapa' not in ln:
            out.append(f'• {m.group(1)} → {m.group(2)}')
            out.append(m.group(3))
            continue
        if ln.startswith('• `') and '★' in ln:
            ln=re.sub(r' · (última actividad|licencia|sin archivo|creado el|creado|release|relevo|actividad) ',r'\n· \1 ',ln)
            out.append(ln)
            continue
        out.append(ln)
    t='\n'.join(out)
    # aire entre bloques de placa consecutivos
    t=re.sub(r'(\n· [^\n]+)\n(• `)',r'\1\n\n\2',t)
    t=re.sub(r'(• `[^`]+`[^\n]*)\n(• `)',r'\1\n\n\2',t)
    # aire garantizado alrededor de separadores y tras títulos de sección nacidas
    t=re.sub(r'\n{3,}','\n\n',t)
    return t
aplicadas=0; intactas=0; detalle=[]
for f in sorted(FB.glob('*.md')):
    orig=f.read_text(encoding='utf-8')
    nueva=transforma(orig)
    if palabras(orig)!=palabras(nueva):
        detalle.append((f.name,'RECHAZADA: cambiaría palabras')); continue
    if nueva!=orig:
        f.write_text(nueva,encoding='utf-8'); aplicadas+=1; detalle.append((f.name,f'{len(orig.splitlines())}→{len(nueva.splitlines())} líneas'))
    else: intactas+=1
print(f'formato respirable: transformadas {aplicadas} · ya respirables {intactas} · rechazadas {sum(1 for d in detalle if "RECHAZADA" in d[1])}')
for d in detalle[:12]: print('  ',d)
# estadística de respiro
def parrafos_max(carp):
    mx=[]
    for f in sorted(carp.glob('*.md')):
        mx.append(max((len(p) for p in f.read_text(encoding='utf-8').split('\n\n')),default=0))
    return sum(mx)/len(mx)
print('largo medio del párrafo más grande por pieza (tras):',round(parrafos_max(FB)))
