#!/usr/bin/env python3
"""HABILIDAD · VERIFICACIÓN MULTINIVEL (vara de verificación)
L0 suelo (hash) · L1 lupa aire · L2 catálogo==disco · L3 placas contra datasets · L4 integridad de paquete.
Sin red: niveles 0-2 y 4. Uso: python3 chequeo-niveles.py [--con-lupa]"""
import hashlib, json, subprocess, sys, zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[2]
res={}
# L0
mani={}
for ln in (R/'02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    s,n,b,h=ln.split('\t'); mani[(s,n)]=h
mal=sum(1 for (s,n),h in mani.items() if not (R/'01-PUBLICACIONES'/s/n).exists() or hashlib.sha256((R/'01-PUBLICACIONES'/s/n).read_bytes()).hexdigest()!=h)
res['L0 suelo']=('OK' if mal==0 else f'{mal} problemas')
# L1
if '--con-lupa' in sys.argv:
    import tempfile, shutil
    ok=True
    for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
        with tempfile.TemporaryDirectory() as td:
            for f in (R/'01-PUBLICACIONES'/serie).glob('*.md'):
                if not f.name.startswith('LEEME'): shutil.copy2(f,td)
            r=subprocess.run(['python3',str(R/'_herramientas/lupa-v6-aire.py'),td],capture_output=True)
            ok = ok and r.returncode==0
    res['L1 lupa']=('OK' if ok else 'REVISAR')
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
print('VEREDICTO:', 'TODO EN ORDEN' if all(v.startswith('OK') for v in res.values()) else 'HAY QUE REPARAR ANTES DE SEGUIR')
