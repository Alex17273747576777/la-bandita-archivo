#!/usr/bin/env python3
import concurrent.futures, csv, json, os, urllib.request, urllib.error
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); BASE=R/'02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct'
rows=list(csv.DictReader(open(BASE/'repos-al-dia-29oct.tsv',encoding='utf-8'),delimiter='\t'))
TOKEN=os.environ.get('LB_TOKEN','')
H={'User-Agent':'LaBanditaAseguramiento/29-oct-2026','Accept':'application/vnd.github+json'}
if TOKEN: H['Authorization']=f'Bearer {TOKEN}'
def check(row):
    slug=row['slug']
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}',headers=H),timeout=30) as r:
            d=json.loads(r.read().decode('utf-8','ignore')); rem=r.headers.get('X-RateLimit-Remaining')
        return {'slug':slug,'http':200,'stars':d['stargazers_count'],'pushed':d['pushed_at'][:10],'archived':d['archived'],
                'license':(d.get('license') or {}).get('spdx_id'),'full':d['full_name'].lower(),'remaining':rem}
    except urllib.error.HTTPError as e:
        return {'slug':slug,'http':e.code}
    except Exception as e:
        return {'slug':slug,'http':f'err:{type(e).__name__}'}
out={}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    futs={ex.submit(check,r):r for r in rows}
    n=0
    for f in concurrent.futures.as_completed(futs):
        rec=f.result(); out[rec['slug']]=rec; n+=1
        if n%150==0: print(n,'/',len(rows),'cuota restante:',rec.get('remaining'),flush=True)
prev={r['slug']:r for r in rows}
drift=[]; muertos_nuevos=[]; cambios_lic=[]
for slug,now in out.items():
    p=prev[slug]
    if now.get('http')!=200:
        if p['estado']=='ok': muertos_nuevos.append((slug,now.get('http'),p['ultima_actividad']))
        continue
    try: ps=int(p['stars']) if p['stars'] else 0
    except Exception: ps=0
    ds=now['stars']-ps
    dpush = (now['pushed'] or '') > (p['ultima_actividad'] or '')
    darch = now['archived'] and p['banda']!='archivado'
    if dpush or darch or abs(ds)>=50: drift.append({'slug':slug,'stars_antes':p['stars'],'stars_hoy':now['stars'],'delta':ds,'push_antes':p['ultima_actividad'],'push_hoy':now['pushed'],'archivado_antes':p['banda'],'archivado_hoy':now['archived'],'lic_nueva':now['license'],'lic_antes':p['licencia']})
    if now['license'] and now['license'] not in ('NOASSERTION',) and p['licencia'] in ('sin resolver','NOASSERTION'): cambios_lic.append((slug,p['licencia'],now['license']))
json.dump({'drift':drift,'muertos_nuevos':muertos_nuevos,'licencias_resueltas_ahora':cambios_lic},open(R/'02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/repulso-drift.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('REPULSO: universo',len(out),'· con deriva material:',len(drift),'· que pasaron a no responder:',muertos_nuevos,'· licencias que GitHub ya resuelve:',cambios_lic)
for d in drift[:25]: print(' ',d)
