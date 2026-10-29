#!/usr/bin/env python3
import concurrent.futures, html, re, urllib.error, urllib.request
from pathlib import Path
from collections import Counter
ROOT=Path('/home/user/Arena-Reimagined'); BASE=ROOT/'02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct'
URLRE=re.compile(r'https?://[^\s\)\]>"\'`”»]+')
urls={}
for carp in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in sorted((ROOT/'01-PUBLICACIONES'/carp).glob('*.md')):
        if f.name.startswith('LEEME'): continue
        for u in URLRE.findall(f.read_text(encoding='utf-8')):
            u=u.rstrip('.,;:)"\'»')
            if u and len(u)>8: urls.setdefault(u,set()).add(f.name)
print('URL únicas totales:',len(urls),flush=True)
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaVerificacion/29-oct-2026)','Accept':'text/html,application/xhtml+xml,*/*;q=0.8'}
cache={}
def check(u):
    rec={'url':u,'piezas':len(urls[u])}
    for method in ('HEAD','GET'):
        try:
            req=urllib.request.Request(u,headers=UA,method=method)
            with urllib.request.urlopen(req,timeout=20) as r:
                rec['status']=r.status; rec['final']=r.geturl(); return rec
        except urllib.error.HTTPError as e:
            rec['status']=e.code
            if method=='HEAD' and e.code in (403,405,501): continue
            return rec
        except Exception as e:
            rec['error']=f'{type(e).__name__}'
            if method=='HEAD': continue
            return rec
    return rec
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    futs={ex.submit(check,u):u for u in urls}
    for f in concurrent.futures.as_completed(futs): out.append(f.result())
out.sort(key=lambda x:x['url'])
with open(BASE/'urls-total-29oct.tsv','w',encoding='utf-8') as fo:
    fo.write('url\tpiezas\tstatus\tfinal\terror\n')
    for r in out: fo.write(f"{r['url']}\t{r['piezas']}\t{r.get('status','')}\t{r.get('final','')}\t{r.get('error','')}\n")
print(Counter(str(r.get('status')) for r in out))
for r in out:
    if str(r.get('status')) not in ('200',): print(r.get('status'),r['url'][:150],r.get('error',''))
