#!/usr/bin/env python3
"""Refino respirable: la licencia baja a su propia línea; el encabezado-tabla se vuelve frase.
La licencia se parte SOLO con saltos (palabras intactas, misma prueba); el encabezado es
la única edición de palabras y va contada y declarada."""
import re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
PALABRAS=re.compile(r'[^\W_]+',re.UNICODE)
palabras=lambda t: PALABRAS.findall(t.lower())
cambios=0; encabezados=0
LIC=r'(Apache-2\.0|MIT|GPL-3\.0|GPL-2\.0|AGPL-3\.0|LGPL-3\.0|BSD|MPL-2\.0|Unlicense|licencia|sin licencia|sin archivo)'
for f in sorted(FB.glob('*.md')):
    t=f.read_text(encoding='utf-8'); orig=t
    # encabezado de tabla disfrazada → frase (edición declarada)
    if '▸ Familia / Nombre / Lo que hace por ti' in t:
        t=t.replace('▸ Familia / Nombre / Lo que hace por ti','▸ La familia, quién la sirve y qué hace por ti'); encabezados+=1
    lineas=[]
    for ln in t.split('\n'):
        if ln.startswith('· '):
            ln=re.sub(r' · '+LIC, r'\n· \1', ln, count=1)
        lineas.append(ln)
    t='\n'.join(lineas)
    if t!=orig:
        antes=palabras(orig.replace('▸ La familia, quién la sirve y qué hace por ti','▸ Familia / Nombre / Lo que hace por ti'))
        if palabras(t)==antes or palabras(t)==palabras(orig):
            f.write_text(t,encoding='utf-8'); cambios+=1
print(f'refino: {cambios} piezas con la licencia en su línea · encabezados humanizados (edición declarada): {encabezados}')
