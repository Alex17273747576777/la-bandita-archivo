#!/usr/bin/env python3
"""FUSIÓN EDITORIAL v3 · 29-oct-2026 (noche).
Uso: LB_TOKEN=... python3 generar-v3.py <WhatsApp|Facebook> <desde> <hasta>
Depurar y rehacer, por fin en ese orden:
- BASE: la pieza ORIGINAL del corpus 3fa5a5f (rescate-editorial), con su voz
  editorial íntegra: gancho, semilla, guía, casos, mitos, meme, cierre.
- FUERA: las secciones-caparazón cuyo contenido es una ficha fechada
  (placas al pulso viejo, enlaces, segundo respiro con cifras) y todo
  párrafo de ritual sobre el propio proceso.
- DENTRO: la ficha medida HOY (descripción oficial de cada autor, ★,
  actividad, release, licencia verificada o ausencia firmada, caídos
  firmados) donde vivía la placa vieja, y la fecha del día en la cabecera.
- El mini-quiz WA se regenera desde los datos de hoy: las respuestas del
  original son de su fecha y ya no son verdad medible."""
import concurrent.futures, csv, hashlib, json, os, re, sys, time, urllib.request, urllib.error
from datetime import date
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); ORIG=Path('/home/user/rescate-editorial/Arena-Reimagined/01-PUBLICACIONES')
HOY='2026-10-29'; HOY_D=date(2026,10,29); FECHA_LARGA='jueves 29 de octubre de 2026'
SERIE={'WhatsApp':'WhatsApp-dominicano-ES','Facebook':'Facebook-dominicano-ES'}[sys.argv[1]]
DESDE, HASTA = int(sys.argv[2]), int(sys.argv[3])
INV=json.loads((R/'02-ARCHIVO/evidencia-29oct-rehechura/inventario-enlaces.json').read_text(encoding='utf-8'))
LICDS={}
with open(R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv',encoding='utf-8',newline='') as fh:
    for r in csv.DictReader(fh,delimiter='\t'): LICDS[r['slug'].lower()]=r['licencia']
H={'User-Agent':'LaBanditaPulso/fusion-editorial','Accept':'application/vnd.github+json'}
if os.environ.get('LB_TOKEN'): H['Authorization']='Bearer '+os.environ['LB_TOKEN']
def get(url):
    req=urllib.request.Request(url,headers=H)
    with urllib.request.urlopen(req,timeout=25) as r: return json.loads(r.read().decode('utf-8','ignore'))
def mide_repo(slug):
    for intento in range(2):
        try:
            d=get(f'https://api.github.com/repos/{slug}')
            rel=''
            try:
                rd=get(f"https://api.github.com/repos/{d['full_name']}/releases/latest")
                rel=f"{rd.get('tag_name','')} ({(rd.get('published_at') or '')[:10]})"
            except Exception: rel=''
            return {'slug':d['full_name'],'estado':'vivo','stars':d['stargazers_count'],'push':d['pushed_at'][:10],
                    'archivado':bool(d['archived']),'licencia':(d.get('license') or {}).get('spdx_id') or '',
                    'desc':(d.get('description') or '').strip(),'temas':d.get('topics') or [],
                    'lenguaje':d.get('language') or '','web':(d.get('homepage') or '').strip(),'release':rel}
        except urllib.error.HTTPError as e:
            if e.code in (403,429) and intento==0: time.sleep(15); continue
            return {'slug':slug,'estado':{404:'caído (404)',451:'bloqueado legal (451): existe'}.get(e.code,f'http {e.code}')}
        except Exception as e: return {'slug':slug,'estado':f'error de red: {type(e).__name__}'}
def mide_url(u):
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36','Accept':'text/html,*/*'},method='GET')
        with urllib.request.urlopen(req,timeout=15) as r: return u,r.status
    except urllib.error.HTTPError as e: return u,e.code
    except Exception: return u,0
def clave(f):
    m=re.match(r'(\d+)',f); return (int(m.group(1)) if m else 9999,f)
def dias(push):
    y,m,d=int(push[:4]),int(push[5:7]),int(push[8:10]); return (HOY_D-date(y,m,d)).days
def fmt(n): return f'{n:,}'.replace(',','.')
def lic_de(m):
    if m.get('licencia') and m['licencia'].upper()!='NOASSERTION': return m['licencia']
    v=LICDS.get(m['slug'].lower())
    if v:
        if v.startswith('sin archivo LICENSE'): return 'sin archivo LICENSE en su repo (verificado)'
        if v.startswith('presente-no-clasificado'): return 'licencia presente en su repo, no clasificada como SPDX (texto leído el 29-oct-2026)'
        return v
    return 'sin SPDX de GitHub: no se inventa'
MAL_OWNER={'reference','example','user','username','owner','tu-usuario','usuario','org','repo'}
def es_repo(s):
    o=s.split('/')[0].lower(); return o not in MAL_OWNER and not o.endswith('.github.io') and '.' not in o
for v in INV.values(): v['slugs']=[s for s in v['slugs'] if es_repo(s)]
archivos=sorted([f for f in (R/'01-PUBLICACIONES'/SERIE).glob('*.md') if not f.name.startswith('LEEME')],key=lambda f:clave(f.name))
tanda=archivos[DESDE:HASTA]
slugs={s for f in tanda for s in INV[f'{SERIE}/{f.name}']['slugs']}
urls={u for f in tanda for u in INV[f'{SERIE}/{f.name}']['urls']}
print(f'tanda v3: {len(tanda)} archivos · midiendo en vivo: {len(slugs)} repos · {len(urls)} URL')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: _med=list(ex.map(mide_repo,sorted(slugs)))
repos={s.lower():m for s,m in zip(sorted(slugs),_med)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: urlst=dict(ex.map(mide_url,sorted(urls)))

def desc_corta(m):
    d=re.sub(r'\s+',' ',m.get('desc') or '').strip()
    if not d: return ''
    return (d[:177].rsplit(' ',1)[0]+'…') if len(d)>180 else d
def ficha(m):
    if m['estado']!='vivo':
        return f"- **{m['slug']}** — {m['estado']} al medir hoy: queda firmado, no recomendado. https://github.com/{m['slug']}"
    dd=dias(m['push'])
    act='empujó hoy' if dd==0 else ('empujó ayer' if dd==1 else f"su último empuje fue el {m['push']} (hace {dd} días)")
    datos=[f"★{fmt(m['stars'])}",act,f"licencia {lic_de(m)}"]
    if m.get('lenguaje'): datos.append(m['lenguaje'])
    if m.get('release'): datos.append(f"última release {m['release']}")
    if m['archivado']: datos.append('ARCHIVADO: historia, no opción viva')
    d=desc_corta(m)
    cab=f"- **{m['slug']}** — «{d}»" if d else f"- **{m['slug']}** — su repo no trae descripción oficial"
    temas=f"\n  Temas: {' · '.join(m['temas'][:6])}" if m.get('temas') else ''
    web=f" · Web: {m['web']}" if m.get('web') else ''
    return f"{cab}\n  {' · '.join(datos)} · https://github.com/{m['slug']}{web}{temas}"

CAP=re.compile(r'placas|enlace|fuente|repositorio|segunda fila|primera fila|pulso al corte|señales de futuro|actividad medida',re.I)
RITUAL=['se borró y se reescribió','no de memoria','comprobaron hoy, uno a uno','pieza reescrita hoy','empujaron hoy,','repos GitHub (','Las placas de arriba','Actividad medida hoy:','Alertas de continuidad (verificadas','Alcance de esta nota:','historia original no se reescribe','esta nota solo añade el estado medido','Continuidad: sin archivados ni dormidos']
def cabecera(ln):
    s=ln.strip()
    m=re.match(r'#{1,3}\s+(.*)',s) or re.match(r'\*([^\*]{2,140})\*\s*:?$',s)
    return m.group(1) if m else None
def limpiar_viejo(original):
    out=[]; skip=False
    for ln in original.split('\n'):
        tit=cabecera(ln)
        if tit is not None:
            if 'MINI-QUIZ' in tit.upper(): skip=True; continue
            if CAP.search(tit): skip=True; continue
            skip=False
        if skip: continue
        s0=ln.strip()
        if s0.startswith('REV|'): continue
        if 'MÉTODO DE LA CASA' in ln.upper() or 'METODO DE LA CASA' in ln.upper(): skip=True; continue  # meta-proceso: cómo se horneó
        if 'Cerró dentro de su banda' in ln or 'cerró dentro de la banda de la casa' in ln: continue  # cierre ritual de era anterior
        if '(verificado ' in ln: continue  # sello de fecha de la placa vieja
        if 'EN UN RESPIRO' in s0.upper(): skip=True; continue  # respiro ritual: resumen viejo idéntico
        if re.match(r'^•\s*`[^`]+`\s*—',s0): continue  # viñeta de la placa vieja
        if s0.startswith(('• Escaparate:','• Código:','• Licencia:')): continue  # campos de la placa vieja
        if re.match(r'^`[^`]+`$',s0): continue  # slug suelto, resto de formato viejo
        if s0.startswith('Vara de cierre: futuro y actividad'): continue  # frase de cierre repetida, sin dato de la pieza
        if any(fr in ln for fr in RITUAL): continue
        out.append(ln)
    texto='\n'.join(out)
    partes=texto.split('\n\n')
    limpias=[]
    for p in partes:
        if re.search(r'\d+\s+repos',p) and 'empujaron' in p and 'medid' in p.lower()[:80]: continue
        limpias.append(p)
    texto='\n\n'.join(limpias)
    return re.sub(r'\n{3,}','\n\n',texto).strip()+'\n'

escritas=0; sin_original=[]
for f in tanda:
    key=f'{SERIE}/{f.name}'; v=INV[key]
    orig_p=ORIG/SERIE/f.name
    if not orig_p.exists(): sin_original.append(f.name); continue
    base=limpiar_viejo(orig_p.read_text(encoding='utf-8'))
    ms=[repos[s.lower()] for s in v['slugs']]
    vivos=[m for m in ms if m['estado']=='vivo']; caidos=[m for m in ms if m['estado']!='vivo']
    fichas=[ficha(m) for m in sorted(ms,key=lambda m:-(m.get('stars') or 0))]
    bloque=("*📋 LA FICHA DE HOY*"+"\n\n"+"\n\n".join(fichas)) if fichas else ''
    enlaces=[]
    for u in v['urls']:
        st=urlst.get(u,0)
        txt=('respondió viva hoy' if 200<=st<400 else ('tras muro de bot/cuota ('+str(st)+'): no se declara muerta' if st in (401,403,429)
             else ('no respondió hoy ('+str(st)+')' if st else 'sin respuesta de red hoy')))
        enlaces.append(f'- {u} — {txt}')
    seccion_enl=("\n\n🔗 Enlaces de hoy:\n\n"+'\n'.join(enlaces)) if enlaces else ''
    quiz=''
    if not SERIE.startswith('Facebook'):
        qs=[]; sv=sorted(vivos,key=lambda m:-m['stars']); sem=int(hashlib.md5(f.name.encode()).hexdigest(),16)
        def RQ(op): return op[sem % len(op)]
        pool=[]
        if sv: pool.append((RQ(['¿Qué repo de esta pieza tiene más estrellas medidas hoy?','¿Cuál es el repo con más ★ de la pieza, según la medición de hoy?','De esta pieza, ¿qué repo mide más estrellas hoy?','¿Quién manda en estrellas dentro de esta pieza?','Con los números de hoy, ¿qué repo de la pieza va primero en ★?']),f"{sv[0]['slug']} — ★{fmt(sv[0]['stars'])}"))
        if len(sv)>=2: pool.append((RQ([f"¿Qué licencia firma {sv[1]['slug']}?",f"¿Bajo qué licencia se publica {sv[1]['slug']}?",f"La licencia de {sv[1]['slug']}, ¿cuál es?",f"¿Con qué licencia sale {sv[1]['slug']}?"]),lic_de(sv[1])))
        if vivos:
            reciente=max(vivos,key=lambda m:m['push']); pool.append((RQ(['¿Qué repo empujó más recientemente?','¿Cuál fue el último repo del grupo en empujar código?','De la pieza, ¿quién empujó más cerca de hoy?','¿De quién es el empuje más fresco del grupo?']),f"{reciente['slug']} — {reciente['push']}"))
            dor=[m for m in vivos if dias(m['push'])>180]
            if dor:
                viejo=min(dor,key=lambda m:m['push']); pool.append((RQ(['¿Qué repo del grupo lleva más tiempo sin empujar?','¿Quién es el más dormido de la pieza?','El repo más quieto del grupo, ¿cuál es?']),f"{viejo['slug']} — {viejo['push']}"))
        if pool:
            orden=sorted(range(len(pool)),key=lambda k:(sem>>k)%7)
            qs=[pool[k] for k in orden[:3]]
        if qs:
            rev='REV|'+'|REV|'.join(f'{i+1}={a}'[::-1] for i,(_q,a) in enumerate(qs))
            preguntas='\n\n'.join(f'*{i+1}.* {q}' for i,(q,_a) in enumerate(qs))
            quiz=f"\n\n*🎯 MINI-QUIZ DE HOY*\n\n{preguntas}\n\n*Respuestas al revés (léelas de atrás para adelante):*\n\n{rev}"
    pie=f"\n\n💓 Hoy, {FECHA_LARGA}, se midieron en vivo {len(ms)} repos y {len(v['urls'])} enlaces de esta pieza: {len(vivos)} vivos, {len(caidos)} firmados con su estado en la ficha. El texto es el de la casa; la ficha, la de hoy."
    base=re.sub(r'\*La Bandita · [^*]*· edición', '*La Bandita · 29 de octubre de 2026 · edición', base, count=1)
    base=re.sub(r'_\w+ \d+ de \w+ de 20\d\d · La Bandita_', f'_{FECHA_LARGA} · La Bandita_', base, count=1)
    base=re.sub(r'\*\*La Bandita · [^*]*\*\*', '**La Bandita · 29 de octubre de 2026**', base, count=1)
    texto=base.rstrip()
    if bloque and '⟦FICHA⟧' in texto: texto=texto.replace('⟦FICHA⟧', bloque, 1)
    elif bloque: texto=texto+'\n\n'+bloque
    texto=texto+seccion_enl+quiz+pie+'\n'
    f.write_text(texto,encoding='utf-8'); escritas+=1
print(f'piezas fusionadas: {escritas} · sin original: {len(sin_original)} {sin_original[:3]}')
