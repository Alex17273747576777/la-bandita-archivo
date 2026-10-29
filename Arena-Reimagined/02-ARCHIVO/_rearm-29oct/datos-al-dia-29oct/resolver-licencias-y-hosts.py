#!/usr/bin/env python3
import concurrent.futures, json, urllib.request, urllib.parse
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct')
VER=[json.loads(l) for l in (BASE/'verificacion-total-29oct.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
sin=[r['slug'] for r in VER if not r.get('estado') and r.get('license') in (None,'NOASSERTION')]
print('sin SPDX claro:',len(sin),flush=True)
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaVerificacion/29-oct-2026)'}
def get(u,timeout=20):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=timeout) as r: return r.status,r.read(4000)
    except Exception: return None,b''
def clasificar(t):
    h=t.lower()
    if 'gnu affero general public license' in h: return 'AGPL-3.0'
    if 'gnu lesser general public license' in h: return 'LGPL'
    if 'gnu general public license' in h and 'version 3' in h: return 'GPL-3.0'
    if 'gnu general public license' in h and 'version 2' in h: return 'GPL-2.0'
    if 'gnu general public license' in h: return 'GPL'
    if 'apache license' in h: return 'Apache-2.0'
    if 'mit license' in h or 'permission is hereby granted, free of charge' in h: return 'MIT'
    if 'mozilla public license' in h: return 'MPL-2.0'
    if 'redistribution and use in source and binary forms' in h: return 'BSD'
    if 'isc license' in h: return 'ISC'
    if 'the unlicense' in h: return 'Unlicense'
    if 'creative commons' in h: return 'CC'
    if 'gplv3 only' in h: return 'GPL-3.0'
    return 'presente-no-clasificado:'+t.strip().splitlines()[0][:60] if t.strip() else '?'
def resolve(slug):
    for b in ('main','master'):
        for n in ('LICENSE','LICENSE.md','COPYING','LICENSE.txt'):
            st,data=get(f'https://raw.githubusercontent.com/{slug}/{b}/{n}')
            if st==200:
                return {'slug':slug,'archivo':f'{b}/{n}','licencia_por_texto':clasificar(data.decode('utf-8','ignore'))}
    return {'slug':slug,'archivo':None,'licencia_por_texto':'sin-license-rutas-comunes'}
lic={}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(resolve,sin): lic[r['slug']]=r
json.dump(lic,open(BASE/'licencias-por-texto-total.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
from collections import Counter
print(Counter(v['licencia_por_texto'].split(':')[0] for v in lic.values()))
# otros hosts
U=json.load(open(BASE/'universo-total.json',encoding='utf-8'))
hosts={}
def codeberg(slug):
    st,data=get(f'https://codeberg.org/api/v1/repos/{slug}')
    if st==200:
        d=json.loads(data.decode('utf-8','ignore') if len(data)>=10 else '{}')
        return None
    return None
def host_check(key):
    host,slug=key.split(':',1)
    rec={'key':key,'checked':'2026-10-29'}
    if host=='codeberg':
        st,data=get(f'https://codeberg.org/api/v1/repos/{slug}',25)
        if st==200:
            d=json.loads(urllib.request.urlopen(urllib.request.Request(f'https://codeberg.org/api/v1/repos/{slug}',headers=UA),timeout=25).read().decode('utf-8','ignore'))
            rec.update({'existe':True,'stars':d.get('stars_count'),'forks':d.get('forks_count'),'archived':d.get('archived'),'updated':(d.get('updated_at') or '')[:10],'descripcion':(d.get('description') or '')[:180],'releases_url':f'https://codeberg.org/{slug}/releases'})
        else: rec.update({'existe':False,'http':st})
    else:
        pid=urllib.parse.quote(f'{slug}',safe='')
        try:
            with urllib.request.urlopen(urllib.request.Request(f'https://gitlab.com/api/v4/projects/{pid}',headers=UA),timeout=25) as r:
                d=json.loads(r.read().decode('utf-8','ignore'))
            rec.update({'existe':True,'stars':d.get('star_count'),'forks':d.get('forks_count'),'archived':d.get('archived'),'updated':(d.get('last_activity_at') or '')[:10],'descripcion':(d.get('description') or '')[:180]})
        except Exception as e: rec.update({'existe':False,'error':str(e)[:80]})
    return rec
keys=list(U['otros_hosts'].keys())
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    for r in ex.map(host_check,keys): hosts[r['key']]=r; print(r)
json.dump(hosts,open(BASE/'otros-hosts-verificados.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('licencias y hosts FIN')
