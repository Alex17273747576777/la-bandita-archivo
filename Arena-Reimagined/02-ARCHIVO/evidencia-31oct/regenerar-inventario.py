#!/usr/bin/env python3
"""Regenera inventario-enlaces.json desde las piezas actuales (31-oct-2026).
El inventario original (29-oct) se perdió con la mordida en las tres fuentes
(proyecto, espejo y remoto). Las piezas rehechas conservan los mismos enlaces
—solo cambió la redacción—, así que el inventario se reconstruye extrayendo de
cada pieza sus URLs de GitHub (fichas) y sus enlaces externos (sección propia).
Las líneas «Web:» de las fichas son metadato del repo, no enlace de la pieza:
se excluyen. Se valida contra los totales históricos (259 archivos, ~780 slugs).
"""
import json, re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
GH=re.compile(r'https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
inv={}
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in sorted((R/'01-PUBLICACIONES'/serie).glob('*.md')):
        if f.name.startswith('LEEME'): continue
        t=f.read_text(encoding='utf-8')
        slugs=sorted(set(GH.findall(t)))
        urls=[]
        en_sec=False
        for ln in t.split('\n'):
            if ln.startswith('## Enlaces externos'): en_sec=True; continue
            if en_sec and ln.startswith('## '): en_sec=False
            if en_sec:
                m=re.match(r'- (https?://\S+) —',ln)
                if m: urls.append(m.group(1))
        inv[f'{serie}/{f.name}']={'slugs':slugs,'urls':urls}
out=R/'02-ARCHIVO/evidencia-29oct/reescritura-29oct'
out.mkdir(parents=True,exist_ok=True)
(out/'inventario-enlaces.json').write_text(json.dumps(inv,ensure_ascii=False,indent=1),encoding='utf-8')
tot_slugs={s for v in inv.values() for s in v['slugs']}
tot_urls={u for v in inv.values() for u in v['urls']}
print(f'inventario regenerado: {len(inv)} archivos · {len(tot_slugs)} slugs únicos · {len(tot_urls)} URL no-GitHub únicas')
print('(histórico 29-oct: 259 archivos · 780 slugs · 103 URL)')
