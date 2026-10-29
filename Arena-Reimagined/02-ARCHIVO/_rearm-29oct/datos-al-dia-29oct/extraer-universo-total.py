#!/usr/bin/env python3
import json, re
from pathlib import Path
ROOT=Path('/home/user/Arena-Reimagined')
URLRE=re.compile(r'https?://[^\s\)\]>"\'`”»]+')
BAD={'github','about','search','topics','collections','orgs','sponsors','features','marketplace','apps','login','join','settings','notifications','explore','pricing','team','enterprise','site','readme','users','gist','events','security','solutions','resources','open-source','customer-stories','sitemap','contact','legal','terms','privacy','pulls','issues','wiki','releases','blob','tree','raw','gist.github'}
EXTRE=re.compile(r'\.(png|jpg|jpeg|svg|json|md|zip|yml|yaml|xml|html|apk|css|js|webp|gif|txt)$')
def slugs_de(texto):
    cuerpo=texto.split('*📖 GLOSARIO')[0]
    s={}
    def add(slug,metodo):
        s.setdefault(slug,set()).add(metodo)
    for u in URLRE.findall(cuerpo):
        u2=u.rstrip('.,;:)\"\'»')
        if 'github.com/' in u2:
            rest=u2.split('github.com/',1)[1].split('/')
            if len(rest)>=2:
                a,b=rest[0],rest[1].rstrip('.,;:)')
                if a.lower() not in BAD and re.fullmatch(r'[A-Za-z0-9_.-]+',a) and re.fullmatch(r'[A-Za-z0-9_.-]+',b) and not EXTRE.search(b.lower()):
                    add(f'{a}/{b}'.lower(),'url')
    for tok in re.findall(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)\s*★', cuerpo):
        add(tok.lower(),'placa')
    for tok in re.findall(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`', cuerpo):
        if tok.count('/')==1 and tok.split('/')[0].lower() not in BAD: add(tok.lower(),'codigo')
    return {k:sorted(v) for k,v in s.items()}
out={}; otros={}
for serie,carp in [('WA','WhatsApp-dominicano-ES'),('FB','Facebook-dominicano-ES')]:
    per={}
    for f in sorted((ROOT/'01-PUBLICACIONES'/carp).glob('*.md')):
        if f.name.startswith('LEEME'): continue
        t=f.read_text(encoding='utf-8')
        per[f.name]=slugs_de(t)
        for u in URLRE.findall(t):
            u2=u.rstrip('.,;:)\"\'»')
            if 'codeberg.org/' in u2 or 'gitlab.com/' in u2:
                host='codeberg' if 'codeberg.org/' in u2 else 'gitlab'
                rest=u2.split('.org/',1)[-1].split('.com/',1)[-1].split('/')
                if len(rest)>=2: otros.setdefault(f'{host}:{rest[0]}/{rest[1]}'.lower(),set()).add(f.name)
    out[serie]=per
gh={x for serie in out.values() for v in serie.values() for x in v}
print('piezas WA/FB:',len(out['WA']),len(out['FB']))
print('slugs GitHub únicos extraídos:',len(gh))
print('otros hosts:',sorted(otros))
# enriquecer con mapa 701 y censo 188
mapa=json.load(open(ROOT/'02-ARCHIVO/_rearm-29oct/mapa-recursos-29oct.json',encoding='utf-8'))
mslugs=set()
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if isinstance(v,str) and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',v) and ('github' in k.lower() or k.lower() in ('repo','slug','full_name')): mslugs.add(v.lower())
            else: walk(v)
    elif isinstance(o,list):
        for i in o: walk(i)
walk(mapa)
print('slugs desde mapa (heurística):',len(mslugs))
censo=set()
for ln in (ROOT/'02-ARCHIVO/_rearm-18oct/censo-fresco-18oct-tarde.tsv').read_text(encoding='utf-8').splitlines():
    p=ln.split('\t')
    if len(p)>=6 and p[1].isdigit(): censo.add(p[0].lower())
print('censo:',len(censo))
json.dump({'piezas':out,'otros_hosts':{k:sorted(v) for k,v in otros.items()},'mapa_slugs':sorted(mslugs),'censo_slugs':sorted(censo),'universo':sorted(gh|mslugs|censo)},open(ROOT/'02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct/universo-total.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('UNIVERSO TOTAL:',len(gh|mslugs|censo))
