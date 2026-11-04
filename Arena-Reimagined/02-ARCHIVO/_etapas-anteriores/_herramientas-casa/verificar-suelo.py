#!/usr/bin/env python3
"""LA BANDITA · Verificador de suelo firme (anti-mordida).
Compara el corpus en disco contra el manifiesto SHA-256 y avisa ANTES de afirmar estado.
Uso: python3 verificar-suelo.py [--restaurar]
  --restaurar copia desde el espejo SOLO los archivos que falten o difieran del manifiesto."""
import hashlib, sys
from pathlib import Path
R=Path(__file__).resolve().parent.parent
MAN=R/'02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv'
MIR=Path('/home/user/la-bandita-archivo')
restaurar='--restaurar' in sys.argv
mani={}
for ln in MAN.read_text(encoding='utf-8').splitlines()[1:]:
    s,n,b,h=ln.split('\t'); mani[(s,n)]=(int(b),h)
mal=[]
for (serie,nombre),(b,h) in mani.items():
    f=R/'01-PUBLICACIONES'/serie/nombre
    if not f.exists(): mal.append((serie,nombre,'AUSENTE')); continue
    if hashlib.sha256(f.read_bytes()).hexdigest()!=h: mal.append((serie,nombre,'HASH DISTINTO'))
print(f'verificar-suelo: {len(mani)} piezas en manifiesto · problemas: {len(mal)}')
for m in mal[:20]: print('  ',m)
if mal and restaurar:
    n=0
    for serie,nombre,_ in mal:
        src=MIR/serie/nombre
        if src.exists():
            (R/'01-PUBLICACIONES'/serie/nombre).write_bytes(src.read_bytes()); n+=1
    print(f'restaurados desde espejo: {n} (volver a correr sin --restaurar para confirmar 0)')
sys.exit(1 if mal and not restaurar else 0)
