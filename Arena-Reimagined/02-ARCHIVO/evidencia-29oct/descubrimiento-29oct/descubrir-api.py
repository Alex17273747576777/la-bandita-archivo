#!/usr/bin/env python3
import json, os, time, urllib.request, urllib.parse
from pathlib import Path
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/descubrimiento-29oct')
TOKEN=os.environ.get('LB_TOKEN','')
H={'User-Agent':'LaBanditaDescubrimiento/29-oct-2026','Accept':'application/vnd.github+json'}
if TOKEN: H['Authorization']=f'Bearer {TOKEN}'
conoc=set()
tsv=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct/repos-al-dia-29oct.tsv')
if tsv.exists():
    for ln in tsv.read_text(encoding='utf-8').splitlines()[1:]:
        if ln.strip(): conoc.add(ln.split('\t')[0].lower())
print('ya en la obra:',len(conoc))
CATS={
 'descarga':'android downloader yt-dlp in:name,description,readme pushed:>2026-08-01',
 'manga':'android manga reader in:name,description pushed:>2026-08-01',
 'anime':'android anime streaming app in:name,description pushed:>2026-08-01',
 'musica':'android music client player in:name,description pushed:>2026-08-01',
 'video':'android video player client in:name,description pushed:>2026-08-01',
 'lanzador':'android launcher in:name,description stars:>100 pushed:>2026-08-01',
 'archivos':'android file manager in:name,description stars:>100 pushed:>2026-08-01',
 'red':'android vpn proxy client in:name,description pushed:>2026-08-01',
 'respaldo':'android backup app in:name,description pushed:>2026-08-01',
 'tiendas':'android app store fdroid client in:name,description pushed:>2026-08-01',
}
salida={}
for cat,q in CATS.items():
    u='https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':q,'sort':'updated','order':'desc','per_page':12})
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40) as r:
            d=json.loads(r.read().decode('utf-8','ignore')); rem=r.headers.get('X-RateLimit-Remaining')
    except Exception as e:
        print(cat,'ERROR',e); continue
    items=[]
    for it in d.get('items',[]):
        fn=it['full_name'].lower()
        items.append({'slug':fn,'stars':it['stargazers_count'],'created':it['created_at'][:10],'pushed':it['pushed_at'][:10],
                      'license':(it.get('license') or {}).get('spdx_id'),'desc':(it.get('description') or '')[:130],
                      'nuevo_en_obra':fn not in conoc,'archived':it.get('archived'),'fork':it.get('fork')})
    salida[cat]=items
    print(f"== {cat} (quedan {rem}) ==")
    for i in items[:8]: print(' ', i['pushed'], i['slug'], '★',i['stars'], i['license'], 'nac',i['created'], 'NUEVO' if i['nuevo_en_obra'] else 'ya-estaba', '|', i['desc'][:70])
    time.sleep(2.5)
json.dump(salida,open(BASE/'busqueda-categorias-api.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('guardado')
