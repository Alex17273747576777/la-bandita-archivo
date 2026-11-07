#!/usr/bin/env python3
"""HABILIDAD · ARRANQUE DE SUELO FIRME  (vara de arranque)
Detecta la mordida del snapshot y deja el taller listo ANTES de afirmar cualquier estado.
Orden de verdad: GitHub > espejo local > proyecto. Nunca se trabaja sobre un suelo sin medir.
Uso: python3 arranque.py [--restaurar]"""
import hashlib, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
MAN=R/'02-ARCHIVO/evidencia-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv'
MIR=Path('/home/user/la-bandita-archivo')
restaurar='--restaurar' in sys.argv
mani={}
if not MAN.exists() or MAN.stat().st_size<1000:
    print('SUELO DESCONOCIDO: falta el manifiesto o está vacío. NO se afirma nada: rescatar evidencia de GitHub primero.')
    raise SystemExit(2)
if MAN.exists():
    for ln in MAN.read_text(encoding='utf-8').splitlines()[1:]:
        s,n,b,h=ln.split('\t'); mani[(s,n)]=h
def estado(carp):
    faltan=distintos=ok=0
    for (s,n),h in mani.items():
        f=carp/s/n
        if not f.exists(): faltan+=1
        elif hashlib.sha256(f.read_bytes()).hexdigest()!=h: distintos+=1
        else: ok+=1
    return ok,faltan,distintos
proy=estado(R/'01-PUBLICACIONES'); espejo=estado(MIR)
print(f'arranque · manifiesto: {len(mani)} piezas')
print(f'  proyecto: ok={proy[0]} faltan={proy[1]} distintos={proy[2]}')
print(f'  espejo:   ok={espejo[0]} faltan={espejo[1]} distintos={espejo[2]}')
if proy[1]+proy[2]==0:
    print('SUELO FIRME: el proyecto está íntegro. Se puede trabajar.')
elif restaurar:
    n=0
    for (s,nombre),h in mani.items():
        dest=R/'01-PUBLICACIONES'/s/nombre; src=MIR/s/nombre
        if src.exists() and (not dest.exists() or hashlib.sha256(dest.read_bytes()).hexdigest()!=h):
            dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(src.read_bytes()); n+=1
    ok,f,d=estado(R/'01-PUBLICACIONES')
    print(f'restauradas {n} desde el espejo · ahora: faltan={f} distintos={d}')
    print('SUELO FIRME tras restaurar.' if f+d==0 else 'OJO: el espejo también está dañado → rescatar de GitHub (ver SKILL-guardado-github).')
else:
    print('SUELO ROTO: corre con --restaurar (o rescata de GitHub) antes de tocar nada.')
