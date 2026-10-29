#!/usr/bin/env python3
"""Corrección del corpus (29-oct-2026, pase final):
1) Restaura las notas 💓 PULSO que la reparación de quices truncó en 41 piezas WA
   (solo la nota firmada, desde el rescate del commit 43aa6e5; el bloque duplicado
   sin firmar que la precedía NO vuelve: era duplicado de la propia nota).
2) Retira bloques previos a la nota que duplican bloques de la nota (WA).
3) Sustituye «Licencias sin resolver hoy» por el estado resuelto según el dataset
   del día (+2 resueltos a mano hoy: Seedvault y Timber). Sin inventar SPDX."""
import re, csv, textwrap
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); OLD=Path('/home/user/rescate-43/Arena-Reimagined/01-PUBLICACIONES')
WA=R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'; FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
def norm(s): return re.sub(r'\s+',' ',s).strip()
# --- dataset de licencias ---
lic={}
with open(R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv',encoding='utf-8',newline='') as fh:
    for r in csv.DictReader(fh,delimiter='\t'): lic[r['slug'].lower()]=r['licencia']
MANUAL={'seedvault-app/seedvault':'Apache-2.0 (texto de su LICENSE leído el 29-oct-2026)',
        'naman14/timber':'sin archivo LICENSE en su repo (verificado el 29-oct-2026)'}
def estado_lic(slug):
    s=slug.lower()
    if s in MANUAL: return MANUAL[s]
    v=lic.get(s)
    if v is None: return None
    if v.startswith('presente-no-clasificado'): return 'licencia presente en su repo, no clasificada como SPDX (texto leído el 29-oct-2026)'
    if v.startswith('sin archivo LICENSE'): return 'sin archivo LICENSE en su repo (verificado por API 29-oct-2026)'
    return v
# --- 1) restaurar notas ---
restauradas=0
for f in sorted(WA.glob('*.md')):
    if f.name.startswith('LEEME'): continue
    t=f.read_text(encoding='utf-8')
    if '💓' in t: continue
    g=OLD/'WhatsApp-dominicano-ES'/f.name
    if not g.exists(): print('SIN RESCATE:',f.name); continue
    vieja=g.read_text(encoding='utf-8'); i=vieja.find('💓 *PULSO')
    if i<0: print('RESCATE SIN NOTA:',f.name); continue
    nota=vieja[i:].rstrip()+'\n'
    f.write_text(t.rstrip()+'\n\n'+nota,encoding='utf-8'); restauradas+=1
print('notas 💓 restauradas en WA:',restauradas)
# --- 2) dedupe previo a la nota ---
quitados=0; archivos=0
for f in sorted(WA.glob('*.md')):
    if f.name.startswith('LEEME'): continue
    t=f.read_text(encoding='utf-8'); i=t.find('💓 *PULSO')
    if i<0: continue
    pre,post=t[:i],t[i:]
    post_norms={norm(b) for b in re.split(r'\n\s*\n',post) if len(norm(b))>=50}
    bloques=re.split(r'(\n\s*\n)',pre)
    # trabajar por bloques de texto (índices pares)
    textos=[b for b in bloques if b.strip()]
    dup=[norm(b) in post_norms and len(norm(b))>=50 for b in textos]
    if not any(dup): continue
    nuevos=[]; n=0
    for b,d in zip(textos,dup):
        nb=norm(b)
        es_cabecera = nb.startswith('*') and nb.endswith('*') and len(nb)<90 and nb in {norm(x) for x in re.split(r'\n\s*\n',post)}
        if d or (es_cabecera and any(dup)):
            n+=1; continue
        nuevos.append(b.strip())
    if n:
        f.write_text('\n\n'.join(nuevos).rstrip()+'\n\n'+post,encoding='utf-8'); quitados+=n; archivos+=1
print(f'dedupe previo a la nota: {quitados} bloques retirados en {archivos} archivos WA')
# --- 3) licencias resueltas ---
pat=re.compile(r'Licencias sin resolver hoy \(\d+\): (.*?)\.\s+Sin licencia clara no hay recomendación completa: queda la alerta firmada\.|Licencias sin resolver hoy \(\d+\): (.*?)\.\s+Sin licencia clara, la recomendación queda incompleta y así se firma\.',re.S)
def reemplazo(m):
    cuerpo=m.group(1) or m.group(2)
    slugs=re.findall(r'`([^`]+)`',cuerpo)
    partes=[]; faltan=[]
    for s in slugs:
        e=estado_lic(s)
        if e is None: faltan.append(s)
        else: partes.append(f'`{s}` — {e}')
    if faltan: return m.group(0)+' [REVISAR: '+','.join(faltan)+']'
    txt='Licencias al 29-oct-2026 (resueltas hoy, sin inventar SPDX): '+ '; '.join(partes)+'.'
    return '\n'.join(textwrap.wrap(txt,width=96,break_long_words=False,break_on_hyphens=False))
tot=0; files=set()
for carp in [WA,FB]:
    for f in sorted(carp.glob('*.md')):
        if f.name.startswith('LEEME'): continue
        t=f.read_text(encoding='utf-8'); nueva,n=pat.subn(reemplazo,t)
        if n: f.write_text(nueva,encoding='utf-8'); tot+=n; files.add(f.name)
print('frases de licencia corregidas:',tot,'en',len(files),'archivos')
