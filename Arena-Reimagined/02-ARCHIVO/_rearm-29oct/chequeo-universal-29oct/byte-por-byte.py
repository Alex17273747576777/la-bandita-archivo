#!/usr/bin/env python3
import hashlib, json, zipfile
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); MIR=Path('/home/user/la-bandita-archivo')
def H(b): return hashlib.sha256(b).hexdigest()
# 1) proyecto vs espejo (corpus + catálogo + herramientas-casa)
dif=[]
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in (R/'01-PUBLICACIONES'/serie).glob('*.md'):
        if (MIR/serie/f.name).read_bytes()!=f.read_bytes(): dif.append(f'{serie}/{f.name}')
print('1) corpus proyecto≠espejo:',dif if dif else '0 diferencias')
print('   catálogo espejo idéntico:',(MIR/'02-ARCHIVO/catalogo-la-bandita.html').read_bytes()==(R/'02-ARCHIVO/catalogo-la-bandita.html').read_bytes())
# 2) ENTREGA vs proyecto
difE=[]
for sub,serie in [('01-WhatsApp-00-108','WhatsApp-dominicano-ES'),('02-Facebook-00-131','Facebook-dominicano-ES')]:
    for f in (R/'ENTREGA-29OCT-2026'/sub).glob('*'):
        ref=R/'01-PUBLICACIONES'/serie/f.name
        if not ref.exists() or ref.read_bytes()!=f.read_bytes(): difE.append(f'{sub}/{f.name}')
print('2) ENTREGA≠proyecto:',difE if difE else '0 diferencias')
# 3) ZIP vs carpeta ENTREGA
z=zipfile.ZipFile(R/'ENTREGA-La-Bandita-29oct2026.zip')
bad=z.testzip(); zdif=[]
names={n for n in z.namelist() if not n.endswith('/')}
disk={str(p.relative_to(R)) for p in (R/'ENTREGA-29OCT-2026').rglob('*') if p.is_file()}
for n in names:
    if z.read(n)!=(R/n).read_bytes(): zdif.append(n)
print('3) zip íntegro:',bad is None,'· entradas:',len(names),'· archivos en carpeta:',len(disk),'· nombres distintos:',names.symmetric_difference(disk),'· bytes distintos:',zdif if zdif else 0)
# 4) catálogo: estructura y textos
h=(R/'02-ARCHIVO/catalogo-la-bandita.html').read_text(encoding='utf-8')
i=h.find('{"wa":'); data,_=json.JSONDecoder().raw_decode(h,i)
emb_wa={p['file']:p['text'] for p in data['wa']}; emb_fb={p['file']:p['text'] for p in data['fb']}
d4=[]
for name,t in emb_wa.items():
    if (R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'/name).read_text(encoding='utf-8')!=t: d4.append(name)
for name,t in emb_fb.items():
    if (R/'01-PUBLICACIONES/Facebook-dominicano-ES'/name).read_text(encoding='utf-8')!=t: d4.append(name)
ids=[p.get('id') for p in data['fb']]; titulos_fb=[p.get('title') for p in data['fb']]
print(f"4) catálogo: WA {len(emb_wa)} · FB {len(emb_fb)} · textos!=disco: {len(d4)} · ids fb duplicados: {len(ids)-len(set(ids))} · piezas FB sin título: {sum(1 for t in titulos_fb if not t)}")
import re
print('   build:',re.search(r'build=2026-10-29 [\d:]+',h).group(0),'· funciones clave:',all(s in h for s in ['function render','function filtra','shuffle','descargables','muro']))
# 5) residual textual: 'sin resolver' fuera de contextos históricos
resid=[]
for carp in [R/'01-PUBLICACIONES/WhatsApp-dominicano-ES',R/'01-PUBLICACIONES/Facebook-dominicano-ES']:
    for f in sorted(carp.glob('*.md')):
        for ln,t in enumerate(f.read_text(encoding='utf-8').splitlines(),1):
            if 'licencia sin resolver' in t and not any(k in t for k in ['FE DE ERRATAS','salió','Cerrada la jornada','recomendación incompleta','no queda ni una']): resid.append((f.name[:3],ln,t[:90]))
print('5) residuos "licencia sin resolver" por pulir:',resid)
# 6) encoding global
mal_enc=[]
for carp in [R/'01-PUBLICACIONES/WhatsApp-dominicano-ES',R/'01-PUBLICACIONES/Facebook-dominicano-ES']:
    for f in sorted(carp.glob('*.md')):
        try: f.read_text(encoding='utf-8')
        except UnicodeDecodeError: mal_enc.append(f.name)
        if '�' in f.read_text(encoding='utf-8',errors='replace'): mal_enc.append(f.name+' �')
print('6) archivos con problema de encoding:',mal_enc if mal_enc else 'ninguno')
