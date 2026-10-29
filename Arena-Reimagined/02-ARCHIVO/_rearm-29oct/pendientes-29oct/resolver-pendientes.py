#!/usr/bin/env python3
import base64, concurrent.futures, csv, json, os, re, urllib.request, urllib.error
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); E=R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv'
rows=list(csv.DictReader(open(E,encoding='utf-8'),delimiter='\t'))
TOKEN=os.environ.get('LB_TOKEN','')
H={'User-Agent':'LaBanditaPendientes/29-oct-2026','Accept':'application/vnd.github+json'}
if TOKEN: H['Authorization']=f'Bearer {TOKEN}'
sin=[r for r in rows if r['licencia'] in ('sin resolver','NOASSERTION','')]
print('celdas sin resolver a atacar:',len(sin),flush=True)
REGLAS=[(r'GPLv3|GNU GENERAL PUBLIC LICENSE\s*\n\s*Version 3|version 3 of the GNU General Public','GPL-3.0'),
(r'GNU AFFERO GENERAL PUBLIC LICENSE\s*\n\s*Version 3','AGPL-3.0'),
(r'GNU LESSER GENERAL PUBLIC LICENSE\s*\n\s*Version 3','LGPL-3.0'),
(r'GNU GENERAL PUBLIC LICENSE\s*\n\s*Version 2','GPL-2.0'),
(r'Apache License\s*\n\s*Version 2\.0','Apache-2.0'),
(r'MIT License|Permission is hereby granted, free of charge','MIT'),
(r'BSD 3-Clause|Redistribution and use in source and binary forms.+\n.+neither the name','BSD-3-Clause'),
(r'BSD 2-Clause','BSD-2-Clause'),
(r'Mozilla Public License Version 2\.0','MPL-2.0'),
(r'The Unlicense|free and unencumbered software released into the public domain','Unlicense'),
(r'ISC License','ISC'),(r'Boost Software License','BSL-1.0'),(r'Eclipse Public License','EPL-2.0'),
(r'DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE','WTFPL'),(r'Creative Commons Legal Code|CC0 1\.0','CC0-1.0')]
def classify(txt):
    for pat,name in REGLAS:
        if re.search(pat,txt,re.S): return name
    return None
def resolver(row):
    slug=row['slug']
    if row['estado']!='ok': return {'slug':slug,'resolucion':'no aplica: '+row['estado']}
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}/license',headers=H),timeout=30) as r:
            d=json.loads(r.read().decode('utf-8','ignore'))
        sp=(d.get('license') or {}).get('spdx_id'); content=d.get('content','')
        txt=''
        if content:
            try: txt=base64.b64decode(content).decode('utf-8','ignore')
            except Exception: pass
        lic=sp if sp and sp!='NOASSERTION' else classify(txt)
        return {'slug':slug,'resolucion':lic or 'LICENSE ilegible para clasificar','spdx_api':sp,'bytes':len(txt)}
    except urllib.error.HTTPError as e:
        if e.code==404: return {'slug':slug,'resolucion':'sin archivo LICENSE en el repo (verificado por API)'}
        return {'slug':slug,'resolucion':f'http {e.code}'}
    except Exception as e: return {'slug':slug,'resolucion':f'error {type(e).__name__}'}
res={}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    for rec in ex.map(resolver,sin): res[rec['slug']]=rec
json.dump(res,open(R/'02-ARCHIVO/_rearm-29oct/pendientes-29oct/licencias-resueltas-final.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
from collections import Counter
print(Counter(v['resolucion'] for v in res.values()))
# aplicar al TSV
n=0
for r in rows:
    if r['slug'] in res:
        nueva=res[r['slug']]['resolucion']
        if nueva not in ('no aplica: 404','no aplica: 451') and not nueva.startswith('http') and not nueva.startswith('error'):
            r['licencia']=nueva; r['licencia_fuente']='API GitHub /repos/license 29-oct (pendientes)'; n+=1
with open(E,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),delimiter='\t'); w.writeheader(); w.writerows(rows)
print('celdas actualizadas:',n,'· quedan sin resolver:',sum(1 for r in rows if r['licencia'] in ('sin resolver','NOASSERTION','')))
# pulso fino fuera del censo
fuera=['facebook/react-native','pinterest/gestalt','solana-labs/wallet-adapter','solana/wallet-adapter','spotify/backstage','browser-use/jev-ultrafast','ebony-vinyl/dsh-our-free-model','ish-app/ish','janhq/jan','pimpinpumpkin/vela','xai-org/grok-build','yetone/magpie']
def pulse(slug):
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}',headers=H),timeout=30) as r:
            d=json.loads(r.read().decode('utf-8','ignore'))
        return {'slug':slug,'http':200,'stars':d['stargazers_count'],'pushed':d['pushed_at'][:10],'archived':d['archived'],'license':(d.get('license') or {}).get('spdx_id'),'full':d['full_name']}
    except urllib.error.HTTPError as e: return {'slug':slug,'http':e.code}
    except Exception as e: return {'slug':slug,'http':type(e).__name__}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
    pulso=list(ex.map(pulse,fuera))
json.dump(pulso,open(R/'02-ARCHIVO/_rearm-29oct/pendientes-29oct/pulso-fuera-del-censo.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for p in pulso: print(p)
