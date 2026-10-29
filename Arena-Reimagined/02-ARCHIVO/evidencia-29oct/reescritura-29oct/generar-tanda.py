#!/usr/bin/env python3
"""REESCRITURA TOTAL 29-oct-2026 · generador por tandas.
Uso: LB_TOKEN=... python3 generar-tanda.py <WhatsApp|Facebook> <desde> <hasta>
Reescribe EN EL MISMO ARCHIVO las piezas de la tanda: pulso en tiempo real de cada
repo (API GitHub) y de cada URL antes de escribir su placa. Nada se afirma sin medir:
404 firmado, 451 existe bloqueado, 403/429 = bot/cuota (se reintenta), licencia sin
SPDX no se inventa. Formato respirable v3, quiz REV de una línea (solo WhatsApp)."""
import concurrent.futures, csv, json, os, re, sys, textwrap, time, urllib.request, urllib.error
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
HOY='2026-10-29'
SERIE={'WhatsApp':'WhatsApp-dominicano-ES','Facebook':'Facebook-dominicano-ES'}[sys.argv[1]]
DESDE, HASTA = int(sys.argv[2]), int(sys.argv[3])
INV=json.loads((R/'02-ARCHIVO/evidencia-29oct/reescritura-29oct/inventario-enlaces.json').read_text(encoding='utf-8'))
DESC={}; LICDS={}
with open(R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv',encoding='utf-8',newline='') as fh:
    for r in csv.DictReader(fh,delimiter='\t'):
        DESC[r['slug'].lower()]=r['descripcion']; LICDS[r['slug'].lower()]=r['licencia']
H={'User-Agent':'LaBanditaPulso/reescritura','Accept':'application/vnd.github+json'}
if os.environ.get('LB_TOKEN'): H['Authorization']='Bearer '+os.environ['LB_TOKEN']
def mide_repo(slug):
    for intento in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(f'https://api.github.com/repos/{slug}',headers=H),timeout=25) as r:
                d=json.loads(r.read().decode('utf-8','ignore'))
            return {'slug':d['full_name'],'estado':'vivo','stars':d['stargazers_count'],'push':d['pushed_at'][:10],
                    'archivado':bool(d['archived']),'licencia':(d.get('license') or {}).get('spdx_id') or ''}
        except urllib.error.HTTPError as e:
            if e.code in (403,429) and intento==0: time.sleep(20); continue
            return {'slug':slug,'estado':{404:'caído (404)',451:'bloqueado legal (451): existe'}.get(e.code,f'http {e.code}')}
        except Exception as e:
            return {'slug':slug,'estado':f'error de red: {type(e).__name__}'}
def mide_url(u):
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36','Accept':'text/html,*/*'},method='GET')
        with urllib.request.urlopen(req,timeout=18) as r: return u,r.status
    except urllib.error.HTTPError as e: return u,e.code
    except Exception: return u,0
def clave(f):
    m=re.match(r'(\d+)',f); return (int(m.group(1)) if m else 9999,f)
def limpia(s): return re.sub(r'\s+',' ',s.replace('*','')).strip(' ·—')
def titulo_de(t,nombre):
    bloques=[b.strip() for b in re.split(r'\n\s*\n',t) if b.strip()]
    if bloques and set(bloques[0])<=set('─━═- ') and len(bloques)>1: bloques=bloques[1:]
    if bloques:
        b0=bloques[0]
        m=re.match(r'^#\s*(?:Publicación\s+\d+\s+—\s*)?(.+)$',b0,re.S)
        if m: return limpia(m.group(1))[:110]
        neg=re.findall(r'\*([^*]+)\*',b0,re.S)
        if neg: return limpia(neg[0])[:110]
        return limpia(b0)[:110]
    return re.sub(r'^\d+-','',nombre).replace('-',' ')[:110]
def wrap(s,w=94): return '\n'.join(textwrap.wrap(s,width=w,break_long_words=False,break_on_hyphens=False))
def banda(push):
    if push>=HOY: return 'hoy'
    if push>='2026-10-22': return '7d'
    if push>='2026-09-29': return '30d'
    if push>='2026-05-02': return '180d'
    return 'dormido'
def lic_de(m):
    if m.get('licencia'): return m['licencia']
    v=LICDS.get(m['slug'].lower())
    if v:
        if v.startswith('sin archivo LICENSE'): return 'sin archivo LICENSE en su repo (verificado por API 29-oct-2026)'
        if v.startswith('presente-no-clasificado'): return 'licencia presente en su repo, no clasificada como SPDX (texto leído el 29-oct-2026)'
        return v
    return 'sin clasificar por GitHub hoy (sin SPDX): no se inventa'
MAL_OWNER={'reference','example','user','username','owner','tu-usuario','usuario','org','repo'}
def es_repo(s):
    o=s.split('/')[0].lower()
    return o not in MAL_OWNER and not o.endswith('.github.io') and '.' not in o
for v in INV.values(): v['slugs']=[s for s in v['slugs'] if es_repo(s)]
archivos=sorted([f for f in (R/'01-PUBLICACIONES'/SERIE).glob('*.md') if not f.name.startswith('LEEME')],key=lambda f:clave(f.name))
tanda=archivos[DESDE:HASTA]
print(f'tanda: {len(tanda)} archivos ({tanda[0].name[:3]}…{tanda[-1].name[:3]})')
slugs={s for f in tanda for s in INV[f'{SERIE}/{f.name}']['slugs']}
urls={u for f in tanda for u in INV[f'{SERIE}/{f.name}']['urls']}
print(f'midiendo en tiempo real: {len(slugs)} repos · {len(urls)} URL')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: _med=list(ex.map(mide_repo,sorted(slugs)))
repos={s.lower():m for s,m in zip(sorted(slugs),_med)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: urlst=dict(ex.map(mide_url,sorted(urls)))
(R/'02-ARCHIVO/evidencia-29oct/reescritura-29oct'/f'pulso-{SERIE[:2]}-{DESDE}-{HASTA}.json').write_text(json.dumps({'repos':repos,'urls':urlst},ensure_ascii=False,indent=1),encoding='utf-8')
def placa(m):
    if m['estado']!='vivo':
        return f"• `{m['slug']}` — {m['estado']} al medir hoy ({HOY}): queda firmado, no recomendado."
    b=banda(m['push'])
    act={'hoy':'actividad HOY','7d':'actividad últimos 7 días','30d':'actividad últimos 30 días','180d':'actividad últimos 180 días','dormido':'dormido'}[b]
    L=[f"• `{m['slug']}` — ★{m['stars']:,}".replace(',','.')+f" (verificado {HOY})",
       f"· {act} · última actividad {m['push']}",
       f"· {lic_de(m)}"]
    if m['archivado']: L.append('· ARCHIVADO en GitHub: historia, no opción viva')
    return '\n'.join(L)
def fuentes(f):
    v=INV[f'{SERIE}/{f.name}']; out=[]
    for s in v['slugs']:
        m=repos[s.lower()]
        est={'vivo':'vivo','caído (404)':'no respondió hoy (404)','bloqueado legal (451): existe':'bloqueado legal (451): existe'}.get(m['estado'],m['estado'])
        out.append(f"• https://github.com/{s} — {est} al verificar hoy ({HOY})")
    for u in v['urls']:
        st=urlst.get(u,0)
        txt='respondió viva hoy' if 200<=st<400 else ('tras muro de bot/cuota ('+str(st)+'): no se declara muerta' if st in (401,403,429) else (f'no respondió hoy ({st})' if st else 'sin respuesta de red hoy'))
        out.append(f"• {u} — {txt} ({HOY})")
    return out
escritas=0
for f in tanda:
    key=f'{SERIE}/{f.name}'; v=INV[key]
    viejo=f.read_text(encoding='utf-8'); titulo=titulo_de(viejo,f.name)
    ms=[repos[s.lower()] for s in v['slugs']]
    vivos=[m for m in ms if m['estado']=='vivo']; caidos=[m for m in ms if m['estado']!='vivo']
    nhoy=sum(1 for m in vivos if banda(m['push'])=='hoy'); n7=sum(1 for m in vivos if banda(m['push'])=='7d')
    ndor=sum(1 for m in vivos if banda(m['push'])=='dormido'); narc=sum(1 for m in vivos if m['archivado'])
    top=sorted(vivos,key=lambda m:-m['stars'])[:1]
    cab_top=f" El mayor medido hoy: `{top[0]['slug']}` — ★{top[0]['stars']:,}".replace(',','.')+f", {lic_de(top[0])}, último empuje {top[0]['push']}." if top else ''
    respiro=(f"Esta pieza se borró y se reescribió hoy, jueves 29 de octubre de 2026, con cada "
             f"enlace comprobado en tiempo real antes de escribir su placa. Cita {len(ms)} repos: "
             f"{nhoy} empujaron hoy, {n7} en los últimos 7 días, {ndor} llevan más de 180 días "
             f"quietos y {narc} están archivados; los que ya no responden quedan firmados como "
             f"caídos, no escondidos.{cab_top}")
    placas=[placa(m) for m in sorted(ms,key=lambda m:-(m.get('stars') or 0))]
    if len(placas)>30:
        placas=placas[:30]+[f"• …y {len(ms)-30} repos más, todos medidos hoy ({HOY}): su placa completa vive en el dataset de la entrega."]
    fts=fuentes(f)
    nota=(f"💓 *PULSO {HOY} — pieza reescrita hoy con verificación en tiempo real (La Bandita).* "
          f"Se comprobaron hoy, uno a uno: {len(ms)} repos GitHub ({len(vivos)} vivos, {len(caidos)} firmados como caídos/bloqueados) "
          f"y {len(v['urls'])} enlace{'s' if len(v['urls'])!=1 else ''} externo{'s' if len(v['urls'])!=1 else ''} de esta pieza. Las placas de arriba salen de esa medición de hoy, no de memoria.")
    if SERIE.startswith('WhatsApp'):
        qs=[]
        sv=sorted(vivos,key=lambda m:-m['stars'])
        if len(sv)>=1: qs.append(('¿Qué repo de esta pieza tiene más estrellas medidas hoy?',f"`{sv[0]['slug']}` — ★{sv[0]['stars']:,}".replace(',','.')))
        if len(sv)>=2: qs.append((f"¿Qué licencia firma `{sv[1]['slug']}`?",lic_de(sv[1])))
        if len(sv)>=1:
            reciente=max(vivos,key=lambda m:m['push']); qs.append(('¿Qué repo empujó más recientemente?',f"`{reciente['slug']}` — {reciente['push']}"))
        quiz=''
        if qs:
            rev='REV|'+'|REV|'.join(f'{i+1}={a}'[::-1] for i,(_q,a) in enumerate(qs))
            preguntas='\n\n'.join(f'*{i+1}.* {q}' for i,(q,_a) in enumerate(qs))
            quiz=f"\n\n*🎯 MINI-QUIZ DE HOY*\n\n*LAS PREGUNTAS:*\n\n{preguntas}\n\n*Respuestas al revés (léelas de atrás para adelante):*\n\n{rev}\n\n(Las respuestas correctas son las líneas descifradas de arriba.)"
        texto=(f"*{titulo}*\n\n*La Bandita · 29 de octubre de 2026 · edición dominicano-español*\n\n"
               f"*⚡ EN UN RESPIRO*\n\n{wrap(respiro)}\n\n"
               f"*🗼 PLACAS AL PULSO ({HOY})*\n\n"+'\n\n'.join(placas)+
               (f"\n\n*🔗 FUENTES COMPROBADAS HOY*\n\n"+'\n'.join(fts) if fts else '')+
               quiz+f"\n\n{wrap(nota)}\n")
    else:
        num=int(re.match(r'(\d+)',f.name).group(1))
        texto=(f"# Publicación {num} — {titulo}\n\n**La Bandita · 29 de octubre de 2026**\n\n"
               f"## ⚡ En una página\n\n{wrap(respiro)}\n\n"
               f"## 🗼 Las placas al pulso ({HOY})\n\n"+'\n\n'.join(placas)+
               (f"\n\n## 🔗 Fuentes comprobadas hoy\n\n"+'\n'.join(fts) if fts else '')+
               f"\n\n{wrap(nota)}\n")
    f.write_text(texto,encoding='utf-8'); escritas+=1
print('piezas reescritas:',escritas)
