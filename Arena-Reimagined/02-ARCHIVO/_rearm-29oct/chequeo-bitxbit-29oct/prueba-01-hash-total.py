#!/usr/bin/env python3
"""NIVEL 1 · hash total bit por bit de cada archivo del proyecto y sus copias."""
import hashlib, zipfile
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); MIR=Path('/home/user/la-bandita-archivo'); OUT=R/'02-ARCHIVO/_rearm-29oct/chequeo-bitxbit-29oct'
H=lambda b: hashlib.sha256(b).hexdigest()
# censo completo del proyecto (excluye cachés)
EXCL={'.git','__pycache__'}
todo={}
for p in sorted(R.rglob('*')):
    if p.is_file() and not any(x in EXCL for x in p.parts):
        todo[str(p.relative_to(R))]=H(p.read_bytes())
print(f'archivos totales en proyecto: {len(todo)}')
man=OUT/'MANIFIESTO-BITXBIT-TOTAL.tsv'
man.write_text('ruta\tsha256\n'+''.join(f'{k}\t{v}\n' for k,v in todo.items()),encoding='utf-8')
# espejo: corpus + catálogo + entrega
espejo_ok=espejo_mal=0; faltas=[]
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in (R/'01-PUBLICACIONES'/serie).glob('*.md'):
        if H((MIR/serie/f.name).read_bytes())==todo[f'01-PUBLICACIONES/{serie}/{f.name}']: espejo_ok+=1
        else: espejo_mal+=1; faltas.append(f.name)
print(f'espejo corpus: idénticos {espejo_ok} · distintos {espejo_mal}')
# zip: cada entrada contra su archivo
z=zipfile.ZipFile(R/'ENTREGA-La-Bandita-29oct2026.zip')
zd=0
for n in z.namelist():
    if n.endswith('/'): continue
    if H(z.read(n))!=todo.get(n): zd+=1; print('zip distinto:',n)
print('zip: entradas comprobadas','· distintas:',zd,'· testzip:',z.testzip() is None)
