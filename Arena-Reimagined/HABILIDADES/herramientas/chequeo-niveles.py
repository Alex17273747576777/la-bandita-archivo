#!/usr/bin/env python3
"""HABILIDAD · VERIFICACIÓN MULTINIVEL (vara de verificación)
L0 suelo (hash) · L1 lupa aire (MEDICIÓN, no puerta: reporta cifras, no un OK vacío) ·
L2 catálogo==disco · L4 integridad de paquete. Las placas contra dataset se miden con
pulso.py y se firman en acta; ningún nivel declara OK por el solo hecho de correr.
Sin red: niveles 0-2 y 4. Uso: python3 chequeo-niveles.py [--con-lupa]"""
import hashlib, json, subprocess, sys, zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[2]
res={}
# L0
mani={}
for ln in (R/'02-ARCHIVO/evidencia-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    s,n,b,h=ln.split('\t'); mani[(s,n)]=h
mal=sum(1 for (s,n),h in mani.items() if not (R/'01-PUBLICACIONES'/s/n).exists() or hashlib.sha256((R/'01-PUBLICACIONES'/s/n).read_bytes()).hexdigest()!=h)
res['L0 suelo']=('OK' if mal==0 else f'{mal} problemas')
# L1 — la lupa v6 solo imprime medidas y siempre sale 0: aquí se miden, no se aplaude.
if '--con-lupa' in sys.argv:
    import importlib.util
    spec=importlib.util.spec_from_file_location('lupa',R/'_herramientas/lupa-v6-aire.py'); lupa=importlib.util.module_from_spec(spec); spec.loader.exec_module(lupa)
    resumen=[]
    for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
        ms=[lupa.medir(str(f)) for f in sorted((R/'01-PUBLICACIONES'/serie).glob('*.md')) if not f.name.startswith('LEEME')]
        resumen.append(f"{serie[:2]}: {len(ms)} piezas · bloques>380={sum(m['over380'] for m in ms)} · >700={sum(m['over700'] for m in ms)} · máx={max(m['maxblock'] for m in ms)}c")
    res['L1 lupa (medición)']='MEDIDA · '+' | '.join(resumen)
# L2
h=(R/'02-ARCHIVO/catalogo-la-bandita.html').read_text(encoding='utf-8'); i=h.find('{"wa":')
data,_=json.JSONDecoder().raw_decode(h,i)
dif=0
for p in data['wa']:
    if (R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'/p['file']).read_text(encoding='utf-8')!=p['text']: dif+=1
for p in data['fb']:
    if (R/'01-PUBLICACIONES/Facebook-dominicano-ES'/p['file']).read_text(encoding='utf-8')!=p['text']: dif+=1
res['L2 catálogo']=f'OK (WA {len(data["wa"])} · FB {len(data["fb"])} · 0 distintos)' if dif==0 else f'{dif} textos distintos'
# L4
z=zipfile.ZipFile(R/'ENTREGA-La-Bandita-29oct2026.zip')
res['L4 paquete']=f'OK ({len(z.namelist())} entradas, CRC íntegro)' if z.testzip() is None else 'ZIP DAÑADO'
for k,v in res.items(): print(f'{k}: {v}')
puertas=[v for k,v in res.items() if not k.startswith('L1')]
print('VEREDICTO:', 'TODO EN ORDEN' if all(v.startswith('OK') for v in puertas) else 'HAY QUE REPARAR ANTES DE SEGUIR')
