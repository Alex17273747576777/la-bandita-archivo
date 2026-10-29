#!/usr/bin/env python3
import json, re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
slugs={}; urls={}
for carp in [R/'01-PUBLICACIONES/WhatsApp-dominicano-ES', R/'01-PUBLICACIONES/Facebook-dominicano-ES']:
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8',errors='replace')
        for s in re.findall(r'github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)',t):
            s=s.lower().rstrip('.,)').removesuffix('.git')
            slugs.setdefault(s,set()).add(f.name[:3])
        for s in re.findall(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`',t):
            slugs.setdefault(s.lower(),set()).add(f.name[:3])
        for u in re.findall(r'https?://[^\s\)\]"\'<>]+',t):
            u=u.rstrip('.,;:')
            urls.setdefault(u,set()).add(f.name[:3])
print('slugs github distintos citados en TODO el corpus:',len(slugs))
print('URL completas distintas:',len(urls))
otros={u:v for u,v in urls.items() if 'github.com' not in u}
print('URL no-github:',len(otros))
json.dump({'slugs':{k:sorted(v) for k,v in slugs.items()},'urls_no_github':{k:sorted(v) for k,v in otros.items()}},open(R/'02-ARCHIVO/_rearm-29oct/chequeo-universal-29oct/universo-citas.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
