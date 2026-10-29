#!/usr/bin/env python3
"""REHECHURA SIN MOLDE · 29-oct-2026 · generador por tandas v2.
[RECONSTRUIDO el 29-oct-2026 tras la mordida que se comió la carpeta
evidencia-29oct-rehechura en proyecto y espejo: la carpeta no viajaba en guardar.py.
La reconstrucción se probó igual que la original: la puerta caza el molde
viejo del 29-oct en piezas extraídas del historial git y queda EN PIE sobre
el corpus rehecho. Desarrollo en INFORME-REHECHURA-SIN-MOLDE-31oct.md.]
Uso: LB_TOKEN=... python3 generar-v2.py <WhatsApp|Facebook> <desde> <hasta>
Cada pieza se compone desde los datos medidos hoy de SUS repos: descripción
oficial (la que escribió el autor del repo), temas, última release, licencias,
actividad y caídos. Sin párrafos rituales: apertura y lectura comparativa salen
de los hechos de la pieza; la procedencia es una sola línea al final.
404 firmado, 451 existe bloqueado, 403/429 = bot/cuota (reintento), licencia sin
SPDX fresco no se inventa (respaldo: texto leído el 29-oct-2026, así firmado)."""
import concurrent.futures, csv, hashlib, json, os, re, sys, time, urllib.request, urllib.error
from datetime import date
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
HOY='2026-10-29'; HOY_D=date(2026,10,29); FECHA_LARGA='jueves 29 de octubre de 2026'
SERIE={'WhatsApp':'WhatsApp-dominicano-ES','Facebook':'Facebook-dominicano-ES'}[sys.argv[1]]
DESDE, HASTA = int(sys.argv[2]), int(sys.argv[3])
INV=json.loads((R/'02-ARCHIVO/evidencia-29oct/reescritura-29oct/inventario-enlaces.json').read_text(encoding='utf-8'))
LICDS={}
with open(R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv',encoding='utf-8',newline='') as fh:
    for r in csv.DictReader(fh,delimiter='\t'): LICDS[r['slug'].lower()]=r['licencia']
H={'User-Agent':'LaBanditaPulso/rehacer-sin-molde','Accept':'application/vnd.github+json'}
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
                    'creado':d['created_at'][:10],'archivado':bool(d['archived']),
                    'licencia':(d.get('license') or {}).get('spdx_id') or '',
                    'desc':(d.get('description') or '').strip(),'temas':d.get('topics') or [],
                    'lenguaje':d.get('language') or '','web':(d.get('homepage') or '').strip(),'release':rel}
        except urllib.error.HTTPError as e:
            if e.code in (403,429) and intento==0: time.sleep(20); continue
            return {'slug':slug,'estado':{404:'caído (404)',451:'bloqueado legal (451): existe'}.get(e.code,f'http {e.code}')}
        except Exception as e: return {'slug':slug,'estado':f'error de red: {type(e).__name__}'}
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
def dias(push):
    y,m,d=int(push[:4]),int(push[5:7]),int(push[8:10]); return (HOY_D-date(y,m,d)).days
def fmt(n): return f'{n:,}'.replace(',','.')
def lic_de(m):
    if m.get('licencia') and m['licencia'].upper()!='NOASSERTION': return m['licencia']
    v=LICDS.get(m['slug'].lower())
    if v:
        if v.startswith('sin archivo LICENSE'): return 'sin archivo LICENSE en su repo (verificado)'
        if v.startswith('presente-no-clasificado'): return 'licencia presente en su repo, no clasificada como SPDX (texto leído el 29-oct-2026)'
        return v+' (según texto de su repo, 29-oct-2026)'
    return 'sin SPDX de GitHub: no se inventa'
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
outdir=R/'02-ARCHIVO/evidencia-29oct-rehechura'; outdir.mkdir(parents=True,exist_ok=True)
(outdir/f'pulso-{SERIE[:2]}-{DESDE}-{HASTA}.json').write_text(json.dumps({'repos':repos,'urls':urlst},ensure_ascii=False,indent=1),encoding='utf-8')

def desc_corta(m):
    d=re.sub(r'\s+',' ',m.get('desc') or '').strip()
    if not d: return ''
    return (d[:177].rsplit(' ',1)[0]+'…') if len(d)>180 else d
def ficha(m):
    if m['estado']!='vivo':
        return f"- **{m['slug']}** — {m['estado']} al medir hoy: queda firmado, no recomendado. https://github.com/{m['slug']}"
    dd=dias(m['push'])
    act='empujó hoy' if dd==0 else ('empujó ayer' if dd==1 else f"su último empuje fue el {m['push']} (hace {dd} días)")
    datos=[f"★{fmt(m['stars'])}", act, f"licencia {lic_de(m)}"]
    if m.get('lenguaje'): datos.append(m['lenguaje'])
    if m.get('release'): datos.append(f"última release {m['release']}")
    if m['archivado']: datos.append('ARCHIVADO: historia, no opción viva')
    d=desc_corta(m)
    cab=f"- **{m['slug']}** — «{d}»" if d else f"- **{m['slug']}** — su repo no trae descripción oficial"
    temas=f"\n  Temas: {' · '.join(m['temas'][:6])}" if m.get('temas') else ''
    web=f" · Web: {m['web']}" if m.get('web') else ''
    return f"{cab}\n  {' · '.join(datos)} · https://github.com/{m['slug']}{web}{temas}"

def apertura(ms,vivos,titulo,f):
    # Se compone desde los hechos de ESTA pieza; marcos rotados por hash del archivo.
    h=int(hashlib.md5(f.name.encode()).hexdigest(),16)%3
    sv=sorted(vivos,key=lambda m:-m['stars'])
    con_desc=[m for m in sv if desc_corta(m)]
    top=sv[0] if sv else None
    activos=sum(1 for m in vivos if dias(m['push'])<=30)
    temas=set()
    for m in vivos: temas.update(m.get('temas') or [])
    ttxt=(' Temas que se repiten en el grupo: '+', '.join(sorted(temas)[:4])+'.') if len(temas)>=3 else ''
    if not vivos:
        from collections import Counter
        estados=', '.join(f'{k} ×{v}' for k,v in Counter(m['estado'] for m in ms).most_common()) if ms else 'ningún repo enlazado'
        return [f"Medición de hoy, sin anestesia: de los {len(ms)} repos que esta pieza enlaza, ninguno respondió vivo ({estados}). Abajo queda cada uno firmado con el estado exacto que devolvió.",
                f"Hoy esta pieza no trae herramientas vivas que recomendar: sus {len(ms)} repos contestaron {estados}. El parte completo, firmado, va en la lista.",
                f"Parte de bajas del {FECHA_LARGA}: los {len(ms)} repos enlazados aquí devolvieron {estados}. No se maquilla: se firma."][h]
    d1=f" «{desc_corta(con_desc[0])}»" if con_desc else ''
    seg=''
    if len(sv)>=2:
        d2=f" «{desc_corta(sv[1])}»" if len(con_desc)>1 and sv[1] in con_desc else ''
        seg=f" Le sigue **{sv[1]['slug']}** (★{fmt(sv[1]['stars'])}){d2}."
    if h==0:
        return (f"Medición del {FECHA_LARGA}: esta pieza reúne {len(ms)} repos, {len(vivos)} vivos. "
                f"El mayor es **{top['slug']}** (★{fmt(top['stars'])}){d1}.{seg} "
                f"Con actividad en los últimos 30 días: {activos} de {len(vivos)}.{ttxt}")
    if h==1:
        return (f"**{top['slug']}** encabeza esta entrega con ★{fmt(top['stars'])} medidos hoy{d1}. "
                f"La pieza cita {len(ms)} repos ({len(vivos)} vivos) y {activos} empujaron en los últimos 30 días.{seg}{ttxt}")
    return (f"Pulso de hoy sobre los {len(ms)} repos de la pieza: {len(vivos)} vivos, {activos} activos este mes. "
            f"Manda **{top['slug']}** (★{fmt(top['stars'])}){d1}.{seg}{ttxt}")

def lectura(ms,vivos,caidos,sem=0):
    # Se compone UNA lectura cuyo hecho TITULAR lo eligen los datos de la pieza
    # (bajas > release fresca > empuje de hoy > pulso general) y cuyos hechos
    # secundarios entran como cláusulas en orden rotado. No hay frase única.
    def R(op): return op[sem % len(op)]
    from collections import Counter
    clausulas=[]; titular=''
    if vivos:
        reciente=max(vivos,key=lambda m:m['push']); dd=dias(reciente['push'])
        cuando='hoy mismo' if dd==0 else ('ayer' if dd==1 else f'hace {dd} días')
        conrel=[m for m in vivos if m.get('release')]
        def f_rel(m):
            mm=re.search(r'(\d{4}-\d{2}-\d{2})',m['release'] or ''); return mm.group(1) if mm else '0000-00-00'
        dor=[m for m in vivos if dias(m['push'])>180]
        if caidos:
            lista=', '.join('**'+m['slug']+'** ('+m['estado']+')' for m in caidos[:3]) + ('…' if len(caidos)>3 else '')
            titular=R([f"La noticia amarga: {lista} ya no respondieron",
                       f"Empieza por las bajas: {lista} no contestaron hoy",
                       f"Lo primero, lo que se cayó: {lista}"])
        elif conrel and dias(f_rel(max(conrel,key=f_rel)))<=7:
            ult=max(conrel,key=f_rel)
            titular=R([f"La noticia fresca es de **{ult['slug']}**: release {ult['release']}",
                       f"Hay release de esta semana: **{ult['slug']}** publicó {ult['release']}",
                       f"**{ult['slug']}** trae la novedad del grupo, su release {ult['release']}"])
        elif dd==0:
            titular=R([f"El grupo se movió hoy: **{reciente['slug']}** empujó hace nada",
                       f"Hay código de hoy en **{reciente['slug']}**",
                       f"**{reciente['slug']}** empujó hoy mismo y mueve al grupo"])
        else:
            titular=R([f"Sin sobresaltos: el empuje más cercano es de **{reciente['slug']}** ({cuando})",
                       f"Pulso tranquilo: lo último que se movió fue **{reciente['slug']}**, {cuando}",
                       f"El grupo respira despacio; su empuje más reciente, **{reciente['slug']}**, fue {cuando}"])
        titular_bajas = bool(caidos) and titular.startswith(('La noticia','Empieza','Lo primero'))
        titular_fresco = (dd==0 and not caidos) or (not caidos and not (conrel and dias(f_rel(max(conrel,key=f_rel)))<=7) and dd>0)
        if titular_bajas:
            clausulas.append(f"del resto, el que más cerca empujó es **{reciente['slug']}** ({cuando})")
        elif not titular_fresco:
            clausulas.append(R([f"el empuje más reciente es de **{reciente['slug']}** ({cuando})",
                                f"lo último empujado lo firmó **{reciente['slug']}** {cuando}",
                                f"la actividad más fresca es de **{reciente['slug']}** ({cuando})"]))
        if dor:
            viejo=min(dor,key=lambda m:m['push'])
            clausulas.append(R([f"**{viejo['slug']}** duerme desde el {viejo['push']}",
                                f"el más quieto es **{viejo['slug']}**, parado desde el {viejo['push']}",
                                f"**{viejo['slug']}** no se mueve desde el {viejo['push']}"]))
        if conrel:
            ult=max(conrel,key=f_rel)
            clausulas.append(R([f"{len(conrel)} repos tienen release y la más reciente es la de **{ult['slug']}** ({ult['release']})",
                                f"con releases publicadas hay {len(conrel)}; manda la de **{ult['slug']}** ({ult['release']})",
                                f"**{ult['slug']}** firmó la release de fecha más reciente ({ult['release']}) de las {len(conrel)} del grupo"]))
        lic=Counter(lic_de(m) for m in vivos)
        lic_txt=', '.join(f'{k} ×{v}' for k,v in lic.most_common(3))
        ojo='; ojo, «sin archivo LICENSE» es mirar sí, reutilizar no' if any('sin archivo LICENSE' in k for k in lic) else ''
        clausulas.append(R([f"en licencias: {lic_txt}{ojo}",
                            f"el parte legal dice {lic_txt}{ojo}",
                            f"legalmente el grupo se reparte así: {lic_txt}{ojo}"]))
        arc=[m for m in vivos if m['archivado']]
        if arc: clausulas.append(f"archivado{'s' if len(arc)>1 else ''} por su autor: {', '.join('**'+m['slug']+'**' for m in arc[:3])}")
    rot=sem % max(1,len(clausulas))
    clausulas=clausulas[rot:]+clausulas[:rot]
    cuerpo='; '.join(clausulas)
    return (titular+'. '+cuerpo[:1].upper()+cuerpo[1:]+'.') if cuerpo else (titular+'.')

escritas=0
for f in tanda:
    key=f'{SERIE}/{f.name}'; v=INV[key]
    viejo=f.read_text(encoding='utf-8'); titulo=titulo_de(viejo,f.name)
    ms=[repos[s.lower()] for s in v['slugs']]
    vivos=[m for m in ms if m['estado']=='vivo']; caidos=[m for m in ms if m['estado']!='vivo']
    fichas=[ficha(m) for m in sorted(ms,key=lambda m:-(m.get('stars') or 0))]
    enlaces=[]
    for u in v['urls']:
        st=urlst.get(u,0)
        txt=('respondió viva hoy' if 200<=st<400 else ('tras muro de bot/cuota ('+str(st)+'): no se declara muerta' if st in (401,403,429)
             else ('no respondió hoy ('+str(st)+')' if st else 'sin respuesta de red hoy')))
        enlaces.append(f'- {u} — {txt}')
    seccion_enlaces=("\n\n## Enlaces externos de la pieza\n\n"+'\n'.join(enlaces)) if enlaces else ''
    lect=lectura(ms,vivos,caidos,sem=int(hashlib.md5(f.name.encode()).hexdigest(),16))
    seccion_lect=("\n\n## Lectura de la medición\n\n"+lect) if lect else ''
    pie=(f"💓 {len(ms)} repos y {len(v['urls'])} enlaces medidos el 29-oct-2026 (API oficial de GitHub y web); "
         f"{len(vivos)} vivos, {len(caidos)} firmado{'s' if len(caidos)!=1 else ''} arriba con su estado.")
    if SERIE.startswith('WhatsApp'):
        qs=[]; sv=sorted(vivos,key=lambda m:-m['stars']); sem=int(hashlib.md5(f.name.encode()).hexdigest(),16)
        def RQ(op): return op[sem % len(op)]
        pool=[]
        if sv: pool.append((RQ(['¿Qué repo de esta pieza tiene más estrellas medidas hoy?','¿Cuál es el repo con más ★ de la pieza, según la medición de hoy?','De esta pieza, ¿qué repo mide más estrellas hoy?','¿Quién manda en estrellas dentro de esta pieza?','Con los números de hoy, ¿qué repo de la pieza va primero en ★?']),f"{sv[0]['slug']} — ★{fmt(sv[0]['stars'])}"))
        if len(sv)>=2: pool.append((RQ([f"¿Qué licencia firma {sv[1]['slug']}?",f"¿Bajo qué licencia se publica {sv[1]['slug']}?",f"La licencia de {sv[1]['slug']}, ¿cuál es?",f"¿Con qué licencia sale {sv[1]['slug']}?"]),lic_de(sv[1])))
        if vivos:
            reciente=max(vivos,key=lambda m:m['push']); pool.append((RQ(['¿Qué repo empujó más recientemente?','¿Cuál fue el último repo del grupo en empujar código?','De la pieza, ¿quién empujó más cerca de hoy?','¿De quién es el empuje más fresco del grupo?']),f"{reciente['slug']} — {reciente['push']}"))
            conrel=[m for m in vivos if m.get('release')]
            if conrel:
                def f_rel2(m):
                    mm=re.search(r'(\d{4}-\d{2}-\d{2})',m['release'] or ''); return mm.group(1) if mm else '0000-00-00'
                ult=max(conrel,key=f_rel2); pool.append((RQ(['¿Qué release es la de fecha más reciente del grupo y de quién?','La release más nueva de la pieza, ¿de qué repo es?','¿Quién publicó la release más reciente del grupo?']),f"{ult['slug']} — {ult['release']}"))
            dor=[m for m in vivos if dias(m['push'])>180]
            if dor:
                viejo=min(dor,key=lambda m:m['push']); pool.append((RQ(['¿Qué repo del grupo lleva más tiempo sin empujar?','¿Quién es el más dormido de la pieza?','El repo más quieto del grupo, ¿cuál es?']),f"{viejo['slug']} — {viejo['push']}"))
        if caidos: pool.append((RQ(['¿Qué repo enlazado por la pieza ya no respondió hoy?','De los repos de la pieza, ¿cuál quedó firmado como caído o bloqueado?']),f"{caidos[0]['slug']} — {caidos[0]['estado']}"))
        if pool:
            orden=sorted(range(len(pool)),key=lambda k:(sem>>k)%7)
            qs=[pool[k] for k in orden[:3]]
        quiz=''
        if qs:
            rev='REV|'+'|REV|'.join(f'{i+1}={a}'[::-1] for i,(_q,a) in enumerate(qs))
            preguntas='\n\n'.join(f'*{i+1}.* {q}' for i,(q,_a) in enumerate(qs))
            quiz=f"\n\n---\n\n*🎯 MINI-QUIZ DE HOY*\n\n{preguntas}\n\n*Respuestas al revés (léelas de atrás para adelante):*\n\n{rev}"
        texto=(f"*{titulo}*\n\n_{FECHA_LARGA} · La Bandita_\n\n{apertura(ms,vivos,titulo,f)}\n\n"
               f"## Los repos de esta pieza, medidos hoy\n\n"+'\n\n'.join(fichas)+seccion_enlaces+seccion_lect+quiz+f"\n\n{pie}\n")
    else:
        num=int(re.match(r'(\d+)',f.name).group(1))
        texto=(f"# Publicación {num} — {titulo}\n\n_{FECHA_LARGA} · La Bandita_\n\n{apertura(ms,vivos,titulo,f)}\n\n"
               f"## Los repos de esta pieza, medidos hoy\n\n"+'\n\n'.join(fichas)+seccion_enlaces+seccion_lect+f"\n\n{pie}\n")
    f.write_text(texto,encoding='utf-8'); escritas+=1
print('piezas rehechas:',escritas)
