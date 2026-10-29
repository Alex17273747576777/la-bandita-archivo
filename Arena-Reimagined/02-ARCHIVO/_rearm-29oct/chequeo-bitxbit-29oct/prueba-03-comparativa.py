#!/usr/bin/env python3
"""NIVEL 3 · re-medición completa y comparativa contra la pasada anterior."""
import concurrent.futures, json, os, urllib.request, urllib.error
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); D=R/'02-ARCHIVO/_rearm-29oct/chequeo-bitxbit-29oct'; U=R/'02-ARCHIVO/_rearm-29oct/chequeo-universal-29oct'
prev=json.load(open(U/'medicion-universal.json',encoding='utf-8'))
TOKEN=os.environ.get('LB_TOKEN','')
H={'User-Agent':'LaBanditaBitXBit/29-oct-2026','Accept':'application/vnd.github+json'}
if TOKEN: H['Authorization']=f'Bearer {TOKEN}'
def repo(slug):
    if slug=='usuario/repositorio': return {'slug':slug,'http':'marcador'}
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}',headers=H),timeout=25) as r:
            d=json.loads(r.read().decode('utf-8','ignore'))
        return {'slug':slug,'http':200,'stars':d['stargazers_count'],'pushed':d['pushed_at'][:10],'archived':d['archived'],'license':(d.get('license') or {}).get('spdx_id')}
    except urllib.error.HTTPError as e: return {'slug':slug,'http':e.code}
    except Exception as e: return {'slug':slug,'http':type(e).__name__}
slugs=list(prev['repos'])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    new={r['slug']:r for r in ex.map(repo,slugs)}
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaBitXBit/29-oct-2026)'}
def url(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA,method='GET'),timeout=20) as r: return (u,r.status)
    except urllib.error.HTTPError as e: return (u,e.code)
    except Exception as e: return (u,type(e).__name__)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    nurls=dict(ex.map(url,list(prev['urls'])))
# comparativa
cambios_estado=[]; drift=[]; arch_new=[]
for s,n in new.items():
    p=prev['repos'][s]
    if n.get('http')!=p.get('http'): cambios_estado.append((s,p.get('http'),n.get('http')))
    if n.get('http')==200 and p.get('http')==200:
        if n['stars']!=p['stars']: drift.append((s,p['stars'],n['stars']))
        if n['archived'] and not p['archived']: arch_new.append(s)
ucambios=[(u,prev['urls'][u],nurls[u]) for u in nurls if str(prev['urls'][u])!=str(nurls[u])]
print(f'comparativa repos: {len(new)} re-medidos · cambios de estado: {cambios_estado} · archivados nuevos: {arch_new} · deriva de estrellas en {len(drift)} repos (máx {max((abs(b-a) for _,a,b in drift),default=0)})')
print('comparativa URL: cambios:',ucambios)
json.dump({'repos':new,'urls':nurls,'cambios_estado':cambios_estado,'arch_nuevos':arch_new,'drift':drift,'url_cambios':ucambios},open(D/'prueba-03-comparativa.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
