#!/usr/bin/env python3
import json, re
from pathlib import Path
ROOT=Path('/home/user/Arena-Reimagined')
URLRE=re.compile(r'https?://[^\s\)\]>"\'`”»]+')
BAD={'github','about','search','topics','collections','orgs','sponsors','features','marketplace','apps','login','join','settings','notifications','explore','pricing','team','enterprise','site','readme','users','gist','events','customer-stories','security','solutions','resources','open-source'}
def slugs_de(texto):
    cuerpo=texto.split('*📖 GLOSARIO')[0].split('💓 *PULSO')[0].split('💓 *Pulso de nacimiento')[0]
    s=set()
    for u in URLRE.findall(cuerpo):
        u=u.rstrip('.,;:)\"\'»')
        if 'github.com/' in u:
            rest=u.split('github.com/',1)[1].split('/')
            if len(rest)>=2:
                a,b=rest[0],rest[1].rstrip('.,;:)')
                if a.lower() not in BAD and re.match(r'^[A-Za-z0-9_.-]+$',a) and re.match(r'^[A-Za-z0-9_.-]+$',b) and not b.endswith(('.png','.jpg','.svg','.json','.md','.zip')):
                    s.add(f'{a}/{b}'.lower())
    for tok in re.findall(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)\s*★', cuerpo): s.add(tok.lower())
    for tok in re.findall(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`', cuerpo):
        a=tok.split('/')[0]
        if a.lower() not in BAD and tok.count('/')==1: s.add(tok.lower())
    return s
out={}
for serie,carp in [('WA','WhatsApp-dominicano-ES'),('FB','Facebook-dominicano-ES')]:
    per={}
    for f in sorted((ROOT/'01-PUBLICACIONES'/carp).glob('*.md')):
        if f.name.startswith('LEEME'): continue
        per[f.name]=sorted(slugs_de(f.read_text(encoding='utf-8')))
    out[serie]=per
    print(serie,'piezas',len(per),'slugs únicos',len({x for v in per.values() for x in v}))
json.dump(out,open(ROOT/'02-ARCHIVO/_rearm-29oct/recuperacion-29oct/universo-por-pieza.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('guardado')
