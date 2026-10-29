#!/usr/bin/env python3
import concurrent.futures, json, re, time, urllib.request, html as ihtml, sys
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct')
salida=BASE/'verificacion-total-29oct.jsonl'
recs=[json.loads(l) for l in salida.read_text(encoding='utf-8').splitlines() if l.strip()]
buenos={r['slug']:r for r in recs if '429' not in (r.get('estado') or '')}
todo=sorted({r['slug'] for r in recs if '429' in (r.get('estado') or '')} - set(buenos))
# eliminar líneas 429 (se reescriben al verificar)
salida.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in buenos.values()),encoding='utf-8')
print('a reintentar:',len(todo),flush=True)
UA={'User-Agent':'Mozilla/5.0 (compatible; LaBanditaVerificacion/29-oct-2026)'}
def fetch(url,timeout=30):
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout)
def check(slug):
    rec={'slug':slug,'checked':'2026-10-29'}
    for intento in range(4):
        try:
            with fetch(f'https://github.com/{slug}') as r: body=r.read(4_000_000).decode('utf-8','ignore')
            break
        except Exception as e:
            msg=str(e)
            if '429' in msg and intento<3:
                time.sleep(15*(intento+1)); continue
            rec['estado']=f'error:{type(e).__name__} {e}'; return rec
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
    try:
        with fetch(f'https://github.com/{slug}/commits.atom') as r: atom=r.read(300_000).decode('utf-8','ignore')
        d=re.findall(r'<updated>([^<]+)</updated>',atom); rec['commit']=(d[1] if len(d)>1 else d[0])[:10] if d else None
    except Exception: rec['commit']=None
    try:
        with fetch(f'https://github.com/{slug}/releases.atom') as r: atom=r.read(300_000).decode('utf-8','ignore')
        d=re.findall(r'<updated>([^<]+)</updated>',atom); t=re.findall(r'<title>([^<]+)</title>',atom)
        rec['release_at']=(d[0][:10] if d else None); rec['release']=(t[1] if len(t)>1 else None)
    except Exception: rec['release_at']=None; rec['release']=None
    time.sleep(0.6)
    return rec
ini=int(sys.argv[1]) if len(sys.argv)>1 else 0
fin=int(sys.argv[2]) if len(sys.argv)>2 else len(todo)
lote=todo[ini:fin]
print(f'lote {ini}:{fin} de {len(todo)}',flush=True)
n=0
with open(salida,'a',encoding='utf-8') as out:
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        futs={ex.submit(check,s):s for s in lote}
        for f in concurrent.futures.as_completed(futs):
            rec=f.result(); out.write(json.dumps(rec,ensure_ascii=False)+'\n'); out.flush(); n+=1
            if n%50==0: print(f'{n}/{len(lote)}',flush=True)
print('LOTE FIN',ini,fin)
