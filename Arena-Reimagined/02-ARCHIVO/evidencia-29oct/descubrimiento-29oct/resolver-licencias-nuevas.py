#!/usr/bin/env python3
import concurrent.futures, json, urllib.request
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/descubrimiento-29oct')
UA={'User-Agent':'Mozilla/5.0'}
def get(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=18) as r: return r.status,r.read(3000).decode('utf-8','ignore')
    except Exception: return None,''
def clasificar(t):
    h=t.lower()
    if 'gnu affero' in h: return 'AGPL-3.0'
    if 'gnu lesser' in h: return 'LGPL'
    if 'gnu general public license' in h and 'version 3' in h: return 'GPL-3.0'
    if 'gnu general public license' in h and 'version 2' in h: return 'GPL-2.0'
    if 'apache license' in h: return 'Apache-2.0'
    if 'mit license' in h or 'permission is hereby granted, free of charge' in h: return 'MIT'
    if 'mozilla public license' in h: return 'MPL-2.0'
    if 'redistribution and use in source and binary forms' in h: return 'BSD'
    return 'presente-no-clasificado'
def resolve(slug):
    for b in ('main','master'):
        for n in ('LICENSE','LICENSE.md','COPYING','LICENSE.txt'):
            st,t=get(f'https://raw.githubusercontent.com/{slug}/{b}/{n}')
            if st==200: return {'slug':slug,'licencia_por_texto':clasificar(t)}
    return {'slug':slug,'licencia_por_texto':'sin-license-rutas-comunes'}
targets=['mahmud0808/teledrive','bropines/tailsocks','johnnylord1/epigraph','advaithavinash/aniultimatium','devcaspian-hash/bokumi-app','raulshma/jellyplay']
out={}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for r in ex.map(resolve,targets): out[r['slug']]=r['licencia_por_texto']; print(r)
json.dump(out,open(BASE/'licencias-descubrimientos.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
