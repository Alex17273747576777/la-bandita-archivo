#!/usr/bin/env python3
import concurrent.futures, json, re, urllib.request
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/creacion-fb-83-108')
D=json.load(open(BASE/'candidatos-fb-83-108.json',encoding='utf-8'))
d=json.load(open(BASE/'candidatos-fb-83-108.json',encoding='utf-8'))
d['piezas']['92']['slugs']=sorted(set(d['piezas']['92']['slugs'])|{'kitsumed/shizucallrecorder'})
d['piezas']['93']['slugs']=sorted(set(d['piezas']['93']['slugs'])|{'neoapplications/neo-backup'})
d['piezas']['94']['slugs']=sorted(set(d['piezas']['94']['slugs'])|{'vr-25/acc'})
allslugs=sorted({s for v in d['piezas'].values() for s in v['slugs']})
json.dump(d,open(BASE/'candidatos-fb-83-108.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaVerificacion/29-oct-2026)'}
def fetch(url,timeout=30):
    req=urllib.request.Request(url,headers=UA)
    return urllib.request.urlopen(req,timeout=timeout)
def check(slug):
    rec={'slug':slug,'checked':'2026-10-29'}
    try:
        with fetch(f'https://github.com/{slug}') as r:
            body=r.read(4_000_000).decode('utf-8','ignore'); rec['final']=r.geturl()
        def m(pat):
            mm=re.search(pat,body); return mm.group(1) if mm else None
        rec['stars']=int(m(r'"stargazerCount":(\d+)') or 0) or None
        rec['archived']=('"isArchived":true' in body)
        rec['created']=(m(r'"createdAt":"([^"]+)"') or '')[:10] or None
        lic=m(r'"spdxId":"([A-Z0-9.+-]+)"')
        rec['license']=lic
        fm=re.search(r'"name":"([^"]+)","ownerLogin"',body)
        rec['full']=None
        mm=re.search(r'<meta property="og:url" content="https://github.com/([^"]+)"',body)
        if mm: rec['full']=mm.group(1)
    except Exception as e:
        rec['estado']=f'error:{type(e).__name__} {e}'; return rec
    try:
        with fetch(f'https://github.com/{slug}/commits.atom') as r:
            atom=r.read(300_000).decode('utf-8','ignore')
        dates=re.findall(r'<updated>([^<]+)</updated>',atom)
        rec['commit']=(dates[1] if len(dates)>1 else dates[0])[:10] if dates else None
    except Exception as e: rec['commit']=None; rec['atom_error']=str(e)[:60]
    try:
        with fetch(f'https://github.com/{slug}/releases.atom') as r:
            atom=r.read(300_000).decode('utf-8','ignore')
        dates=re.findall(r'<updated>([^<]+)</updated>',atom)
        titles=re.findall(r'<title>([^<]+)</title>',atom)
        rec['release_at']=(dates[0] if dates else None)
        rec['release']=(titles[1] if len(titles)>1 else None)
        if rec['release_at']: rec['release_at']=rec['release_at'][:10]
    except Exception: rec['release_at']=None; rec['release']=None
    return rec
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    futs={ex.submit(check,s):s for s in allslugs}
    for f in concurrent.futures.as_completed(futs): out.append(f.result())
out.sort(key=lambda x:x['slug'])
json.dump(out,open(BASE/'verificacion-fuentes-83-108.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for r in out: print(r['slug'], r.get('estado') or '', r.get('stars'), r.get('commit'), r.get('license'), 'ARCH' if r.get('archived') else '')
print('total',len(out))
