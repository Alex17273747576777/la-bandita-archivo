#!/usr/bin/env python3
"""HABILIDAD · PULSO DE REPOS (la verdad se mide, no se recuerda)
Mide repos de GitHub por la vía gobernante: API si hay LB_TOKEN en el entorno; si no, web oficial.
Semántica de la casa: 404=muerto · 451=bloqueo legal (existe) · 403/429=cuota o bot (NO es muerte).
Uso: LB_TOKEN=... python3 pulso.py owner/repo [owner/repo ...]  |  pulso.py --archivo slugs.txt"""
import concurrent.futures, json, os, sys, urllib.request, urllib.error
H={'User-Agent':'LaBanditaPulso/skill','Accept':'application/vnd.github+json'}
if os.environ.get('LB_TOKEN'): H['Authorization']='Bearer '+os.environ['LB_TOKEN']
def mide(slug):
    try:
        with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}',headers=H),timeout=25) as r:
            d=json.loads(r.read().decode('utf-8','ignore'))
        return {'slug':slug,'estado':'vivo','stars':d['stargazers_count'],'ultimo_push':d['pushed_at'][:10],'archivado':d['archived'],'licencia':(d.get('license') or {}).get('spdx_id') or 'sin SPDX (leer LICENSE o firmar ausencia)'}
    except urllib.error.HTTPError as e:
        return {'slug':slug,'estado':{404:'muerto (404)',451:'bloqueado legal (451): existe',403:'cuota/bot (403): NO declarar muerto',429:'cuota (429): reintentar, NO declarar muerto'}.get(e.code,f'http {e.code}')}
    except Exception as e: return {'slug':slug,'estado':f'error de red: {type(e).__name__} (reintentar)'}
slugs=[]
if '--archivo' in sys.argv:
    slugs=[l.strip() for l in open(sys.argv[sys.argv.index('--archivo')+1],encoding='utf-8') if l.strip()]
else: slugs=[a for a in sys.argv[1:] if not a.startswith('--')]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for r in ex.map(mide,slugs): print(json.dumps(r,ensure_ascii=False))
