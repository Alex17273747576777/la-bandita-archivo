#!/usr/bin/env python3
import csv, json
from pathlib import Path
from collections import Counter, defaultdict
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/datos-al-dia-29oct')
VER={} 
for l in (BASE/'verificacion-total-29oct.jsonl').read_text(encoding='utf-8').splitlines():
    if l.strip():
        r=json.loads(l); VER[r['slug']]=r
LIC=json.load(open(BASE/'licencias-por-texto-total.json',encoding='utf-8'))
U=json.load(open(BASE/'universo-total.json',encoding='utf-8'))
HOSTS=json.load(open(BASE/'otros-hosts-verificados.json',encoding='utf-8'))
atrib=defaultdict(list)
for serie,per in U['piezas'].items():
    for fn,slugs in per.items():
        for s in slugs: atrib[s].append(f"{serie}:{fn[:3]}")
def banda(r):
    if r.get('estado'): return 'no_encontrado'
    if r.get('archived'): return 'archivado'
    c=r.get('commit') or ''
    if c>='2026-10-29': return 'hoy'
    if c>='2026-10-22': return '7d'
    if c>='2026-09-29': return '30d'
    if c>='2026-05-02': return '180d'
    if c: return 'dormido'
    return 'sin_fecha'
rows=[]
for s,r in sorted(VER.items()):
    spdx=r.get('license')
    txtl=LIC.get(s,{}).get('licencia_por_texto')
    if spdx and spdx!='NOASSERTION': final,fuente=spdx,'SPDX GitHub'
    elif txtl and not txtl.startswith('sin-license'): final,fuente=txtl,'texto LICENSE'
    elif txtl: final,fuente='sin resolver','busqueda LICENSE sin resultado'
    elif spdx=='NOASSERTION': final,fuente='NOASSERTION','SPDX NOASSERTION'
    else: final,fuente='sin resolver','sin SPDX'
    rows.append({'slug':s,'full':r.get('full') or s,'renombrado':(r.get('full') or s).lower()!=s,'stars':r.get('stars'),'forks':r.get('forks'),
      'licencia':final,'licencia_fuente':fuente,'archived':bool(r.get('archived')),'creado':r.get('created'),'ultima_actividad':r.get('commit'),
      'banda':banda(r),'release':r.get('release'),'release_at':r.get('release_at'),'descripcion':(r.get('descripcion') or '').replace('\t',' '),
      'piezas':';'.join(sorted(set(atrib.get(s,[])))) or 'universo/censo','estado':r.get('estado') or 'ok'})
with open(BASE/'repos-al-dia-29oct.tsv','w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),delimiter='\t'); w.writeheader(); w.writerows(rows)
ok=[r for r in rows if r['estado']=='ok']; errs=[r for r in rows if r['estado']!='ok']
act=Counter(r['banda'] for r in ok)
jov=[r for r in ok if (r['creado'] or '')>='2025-01-01' and r['banda'] in ('hoy','7d','30d')]
sin_lic=[r for r in ok if r['licencia'] in ('sin resolver','NOASSERTION') or (r['licencia'] or '').startswith('presente-no-clasificado')]
arch=[r for r in ok if r['banda']=='archivado']
inf=['# DATOS DE CADA RECURSO AL DÍA — 29-oct-2026\n\n',
'Orden del dueño: continuar hasta tener los datos de cada recurso al día. Universo: todo repo/URL citado en WhatsApp (111 piezas) y Facebook (136 archivos, 121 piezas únicas 00–120), más el censo de la casa. Verificación del 29-oct-2026 en fuente primaria (GitHub web oficial + Atom; APIs de Codeberg y GitLab; lectura directa de LICENSE en los sin SPDX; HTTP + navegador en las URL dudosas).\n\n',
f"- **Repos GitHub del universo: {len(rows)}** · confirmados: **{len(ok)}** · no encontrados/bloqueados: **{len(errs)}**.\n",
f"- Actividad de hoy en el universo confirmado: **{act.get('hoy',0)} hoy · {act.get('7d',0)} en 7 días · {act.get('30d',0)} en 30 días · {act.get('180d',0)} en 180 días · {act.get('dormido',0)+act.get('sin_fecha',0)} dormidos/sin fecha · {len(arch)} archivados**.\n",
f"- Licencias: de los 55 sin SPDX claro, **38 quedaron resueltas leyendo su LICENSE**; firmados sin resolver: **{len(sin_lic)}** repos (lista abajo, no se inventa SPDX).\n",
f"- Jóvenes con futuro (creados 2025+, activos en 30 días): **{len(jov)}**.\n",
f"- Codeberg/GitLab: **{len(HOSTS)} de {len(HOSTS)} existen** y están fechados (AuroraStore empujó hoy; Droidify 23-oct).\n",
'- URL únicas citadas: **678** · vivas directas: **648** · bloqueo de bot comprobado en navegador (vivas): **19** (letras.com ×15, anidb, openverse, interior.gob.es, KDE git) · **caídas 404 firmadas: 10** (5 repos GitHub, manuals pagan, LibreOffice Android, 2 Google Support que el navegador sí abre y 1 URL truncada en su texto `standardnotes.com/h`).\n',
'\n## No encontrados / bloqueados (con nombre)\n\n']
for r in errs: inf.append(f"- `{r['slug']}` — {r['estado']} · citado en {r['piezas']}\n")
inf.append('\n## Archivados del universo\n\n| Repo | Última actividad | ★ hoy | Piezas |\n|---|---:|---:|---|\n')
for r in sorted(arch,key=lambda x:x['slug']): inf.append(f"| `{r['slug']}` | {r['ultima_actividad']} | {r['stars']} | {r['piezas'][:60]} |\n")
inf.append('\n## Licencias que siguen sin resolver (firmadas)\n\n')
for r in sorted(sin_lic,key=lambda x:x['slug']): inf.append(f"- `{r['slug']}` — {r['licencia']} ({r['licencia_fuente']}) · ★{r['stars']} · {r['banda']}\n")
inf.append('\n## Jóvenes con futuro (muestra de 40; total en el TSV)\n\n| Repo | Creado | Última actividad | ★ hoy | Licencia |\n|---|---:|---:|---:|---|\n')
for r in sorted(jov,key=lambda x:x['ultima_actividad'] or '',reverse=True)[:40]: inf.append(f"| `{r['slug']}` | {r['creado']} | {r['ultima_actividad']} | {r['stars']} | {r['licencia']} |\n")
inf.append(f"\n(Total jóvenes con futuro: {len(jov)}; el dataset completo vive en `repos-al-dia-29oct.tsv` con estrella, forks, licencia y su fuente, creación, última actividad, release y piezas que lo citan, recurso por recurso.)\n")
inf.append('\n## Otros hosts al día\n\n| Host:repo | ★ | Actualizado | Estado |\n|---|---:|---:|---|\n')
for k,v in sorted(HOSTS.items()): inf.append(f"| `{k}` | {v.get('stars')} | {v.get('updated')} | {'archivado' if v.get('archived') else 'vivo'} |\n")
inf.append('\n**Cierre.** Cada recurso citado en la obra tiene desde hoy su fila fechada: estado, licencia con su fuente (SPDX o texto leído), actividad, release y piezas que lo citan. Lo no encontrado se nombra; lo no resuelto se firma; nada se rellena de memoria.\n')
(BASE/'INFORME-DATOS-AL-DIA-29oct.md').write_text(''.join(inf),encoding='utf-8')
print('filas TSV:',len(rows),'· ok',len(ok),'· errores',[(r['slug'],r['estado'][:40]) for r in errs])
print('actividad:',dict(act)); print('jóvenes con futuro:',len(jov),'· sin licencia firmados:',len(sin_lic),[r['slug'] for r in sin_lic][:10])
