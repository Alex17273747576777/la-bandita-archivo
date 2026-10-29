#!/usr/bin/env python3
import concurrent.futures, json, re, urllib.request, html as ihtml
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct')
slugs=json.load(open(BASE/'universo-total.json',encoding='utf-8'))['universo']
salida=BASE/'verificacion-total-29oct.jsonl'
hechos={}
if salida.exists():
    for l in salida.read_text(encoding='utf-8').splitlines():
        if l.strip():
            r=json.loads(l); hechos[r['slug']]=r
todo=[s for s in slugs if s not in hechos]
print('total',len(slugs),'hechos',len(hechos),'por hacer',len(todo),flush=True)
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
    rec['is_fork']=('"isFork":true' in body)
    rec['created']=(m(r'"createdAt":"([^"]+)"') or '')[:10] or None
    rec['license']=m(r'"spdxId":"([A-Z0-9.+-]+)"')
    mm=re.search(r'<meta property="og:url" content="https://github.com/([^"]+)"',body)
    rec['full']=mm.group(1) if mm else slug
    ds=re.search(r'<meta name="description" content="([^"]+)"',body)
    rec['descripcion']=ihtml.unescape(ds.group(1))[:220] if ds else None
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
with open(salida,'a',encoding='utf-8') as out:
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        futs={ex.submit(check,s):s for s in todo}
        n=0
        for f in concurrent.futures.as_completed(futs):
            rec=f.result(); out.write(json.dumps(rec,ensure_ascii=False)+'\n'); out.flush(); n+=1
            if n%50==0: print(f'{n}/{len(todo)}',flush=True)
print('FIN',len(todo))
