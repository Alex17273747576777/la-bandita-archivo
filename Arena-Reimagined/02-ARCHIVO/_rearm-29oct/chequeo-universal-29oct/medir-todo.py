#!/usr/bin/env python3
import concurrent.futures, json, os, urllib.request, urllib.error
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); D=R/'02-ARCHIVO/_rearm-29oct/chequeo-universal-29oct'
U=json.load(open(D/'universo-citas.json',encoding='utf-8'))
TOKEN=os.environ.get('LB_TOKEN','')
H={'User-Agent':'LaBanditaChequeoUniversal/29-oct-2026','Accept':'application/vnd.github+json'}
if TOKEN: H['Authorization']=f'Bearer {TOKEN}'
def repo(slug):
    if slug=='usuario/repositorio': return {'slug':slug,'http':'marcador'}
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}',headers=H),timeout=25) as r:
            d=json.loads(r.read().decode('utf-8','ignore'))
        return {'slug':slug,'http':200,'stars':d['stargazers_count'],'pushed':d['pushed_at'][:10],'archived':d['archived'],'license':(d.get('license') or {}).get('spdx_id')}
    except urllib.error.HTTPError as e: return {'slug':slug,'http':e.code}
    except Exception as e: return {'slug':slug,'http':type(e).__name__}
slugs=list(U['slugs'])
res={}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for rec in ex.map(repo,slugs): res[rec['slug']]=rec
from collections import Counter
print('repos citados medidos:',len(res),Counter(str(v.get('http')) for v in res.values()))
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaChequeoUniversal/29-oct-2026)'}
def url(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA,method='GET'),timeout=20) as r: return (u,r.status)
    except urllib.error.HTTPError as e: return (u,e.code)
    except Exception as e: return (u,type(e).__name__)
urls=list(U['urls_no_github'])
ures={}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for u,s in ex.map(url,urls): ures[u]=s
print('URL no-github medidas:',len(ures),Counter(str(v) for v in ures.values()))
json.dump({'repos':res,'urls':ures},open(D/'medicion-universal.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
muertos={s:v for s,v in res.items() if v.get('http') not in (200,'marcador')}
print('repos citados NO vivos:',muertos)
caidas={u:s for u,s in ures.items() if s not in (200,301,302,403)}
print('URL externas no vivas:',caidas)
