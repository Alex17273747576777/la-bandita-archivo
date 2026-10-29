#!/usr/bin/env python3
import concurrent.futures, json, re, urllib.request, html as ihtml
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/descubrimiento-29oct')
CAND=['sleepless-index/ribbt','mailo037/hamstr','rajnishone/linklift','eurt-labs/stash','amisles/v4aw','ramik4/ytindir']
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaVerificacion/29-oct-2026)'}
def fetch(url,timeout=30):
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout)
def check(slug):
    rec={'slug':slug,'checked':'2026-10-29'}
    try:
        with fetch(f'https://github.com/{slug}') as r: body=r.read(4_000_000).decode('utf-8','ignore')
    except Exception as e: rec['estado']=f'error:{type(e).__name__} {e}'; return rec
    def m(p):
        mm=re.search(p,body); return mm.group(1) if mm else None
    rec['stars']=int(m(r'"stargazerCount":(\d+)') or 0) or None
    rec['forks']=int(m(r'"forkCount":(\d+)') or 0) or None
    rec['archived']=('"isArchived":true' in body)
    rec['created']=(m(r'"createdAt":"([^"]+)"') or '')[:10] or None
    rec['license']=m(r'"spdxId":"([A-Z0-9.+-]+)"')
    mm=re.search(r'<meta property="og:url" content="https://github.com/([^"]+)"',body); rec['full']=mm.group(1) if mm else slug
    ds=re.search(r'<meta name="description" content="([^"]+)"',body); rec['descripcion']=ihtml.unescape(ds.group(1))[:240] if ds else None
    try:
        with fetch(f'https://github.com/{slug}/commits.atom') as r: atom=r.read(300_000).decode('utf-8','ignore')
        d=re.findall(r'<updated>([^<]+)</updated>',atom); rec['commit']=(d[1] if len(d)>1 else d[0])[:10] if d else None
    except Exception: rec['commit']=None
    try:
        with fetch(f'https://github.com/{slug}/releases.atom') as r: atom=r.read(300_000).decode('utf-8','ignore')
        d=re.findall(r'<updated>([^<]+)</updated>',atom); t=re.findall(r'<title>([^<]+)</title>',atom)
        rec['release_at']=(d[0][:10] if d else None); rec['release']=(t[1] if len(t)>1 else None)
    except Exception: rec['release_at']=None; rec['release']=None
    return rec
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    futs={ex.submit(check,s):s for s in CAND}
    for f in concurrent.futures.as_completed(futs): out.append(f.result())
out.sort(key=lambda x:(x.get('commit') or ''),reverse=True)
json.dump(out,open(BASE/'ejemplos-del-dueno.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for r in out: print(r.get('commit'),'|',r['slug'],'|',r.get('estado') or '','★',r.get('stars'),'|',r.get('license'),'| creado',r.get('created'),'|', (r.get('release') or '')[:35],r.get('release_at') or '','|', (r.get('descripcion') or '')[:110])
