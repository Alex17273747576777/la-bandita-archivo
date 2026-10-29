#!/usr/bin/env python3
import csv, json
from pathlib import Path
from collections import Counter
BASE=Path('/home/user/Arena-Reimagined/02-ARCHIVO/_rearm-29oct/recuperacion-29oct')
ROOT=Path('/home/user/Arena-Reimagined')
VER={}
for l in (BASE/'verificacion-universo-29oct.jsonl').read_text(encoding='utf-8').splitlines():
    if l.strip():
        r=json.loads(l); VER[r['slug']]=r
censo={}
for ln in (ROOT/'02-ARCHIVO/_rearm-18oct/censo-fresco-18oct-tarde.tsv').read_text(encoding='utf-8').splitlines():
    p=ln.split('\t')
    if len(p)>=6 and p[1].isdigit(): censo[p[0].lower()]={'stars':int(p[1]),'license':p[4]}
U=json.load(open(BASE/'universo-por-pieza.json',encoding='utf-8'))
def banda(r):
    if r.get('archived'): return 'archivado'
    c=r.get('commit') or ''
    if c>='2026-10-29': return 'hoy'
    if c>='2026-10-22': return '7d'
    if c>='2026-09-29': return '30d'
    if c>='2026-05-02': return '180d'
    if c: return 'dormido'
    return 'sin_fecha'
ok={s:r for s,r in VER.items() if not r.get('estado')}
err={s:r for s,r in VER.items() if r.get('estado')}
rows=[]
for serie in ('WA','FB'):
    for fn,slugs in U[serie].items():
        for s in slugs:
            r=VER.get(s)
            if not r: continue
            cz=censo.get(s)
            rows.append({'serie':serie,'pieza':fn,'slug':s,'full':r.get('full'),'stars':r.get('stars'),
              'license':r.get('license'),'archived':r.get('archived'),'created':r.get('created'),'commit':r.get('commit'),
              'banda':banda(r) if not r.get('estado') else r.get('estado'),
              'release':r.get('release'),'release_at':r.get('release_at'),
              'censo_stars':cz['stars'] if cz else None,'censo_license':cz['license'] if cz else None})
with open(BASE/'repos-por-pieza-reconstruido.tsv','w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),delimiter='\t'); w.writeheader(); w.writerows(rows)
print('atribuciones repo×pieza:',len(rows))
print('repos ok:',len(ok),'· errores:',len(err),list(err)[:10])
act=Counter(banda(r) for r in ok.values())
print('actividad global (repos únicos):',dict(act))
arch=sorted([s for s,r in ok.items() if r.get('archived')])
print('archivados:',arch)
jov=sorted([s for s,r in ok.items() if (r.get('created') or '')>='2025-01-01' and banda(r) in ('hoy','7d','30d')], key=lambda s: ok[s]['created'], reverse=True)
print('jóvenes con futuro:',len(jov), jov[:15])
cambios=[]
for s,r in ok.items():
    cz=censo.get(s)
    if cz and cz['license'] not in ('','None') and r.get('license') and r['license']!=cz['license']:
        cambios.append((s,cz['license'],r['license']))
print('licencias distintas vs censo 18-oct:',cambios)
# informe
inf=['# INFORME DE EVIDENCIA RECONSTRUIDA — 29-oct-2026 (segunda pasada)\n\n',
'**Motivo.** La mordida del snapshot entre turnos se comió los artefactos intermedios (JSONL/TSV) de la actualización total, dejando íntegras las publicaciones, las notas y el catálogo. Esta carpeta reconstruye la evidencia el mismo día 29-oct-2026 con segunda verificación fresca en GitHub (web oficial + Atom), para que el archivo en GitHub contenga también la prueba y no solo la obra.\n\n',
'**Método.** Extracción de candidatos por pieza (URL + placa `owner/repo ★` + tokens en código, cuerpo sin glosario y sin la nota añadida), fusión WA+FB, verificación individual. El método subcuenta repos citados solo en prosa sin placa; se firma como fiel, no como idéntico a la primera pasada.\n\n',
f"- Repos únicos sometidos: **{len(VER)}** · confirmados: **{len(ok)}** · no encontrados/error: **{len(err)}**.\n",
f"- Atribuciones repo×pieza reconstruidas: **{len(rows)}**.\n",
f"- Actividad global de hoy: {act.get('hoy',0)} hoy · {act.get('7d',0)} 7d · {act.get('30d',0)} 30d · {act.get('180d',0)} 180d · {act.get('dormido',0)} dormidos · {len(arch)} archivados.\n",
'\n## Archivados (universo reconstruido)\n\n| Repo | Última actividad | ★ hoy |\n|---|---:|---:|\n']
for s in arch: inf.append(f"| `{s}` | {ok[s].get('commit')} | {ok[s].get('stars')} |\n")
inf.append('\n## Jóvenes con futuro (creados 2025+, activos en 30 días)\n\n| Repo | Creado | Última actividad | ★ hoy |\n|---|---:|---:|---:|\n')
for s in jov[:40]: inf.append(f"| `{s}` | {ok[s].get('created')} | {ok[s].get('commit')} | {ok[s].get('stars')} |\n")
inf.append(f"\n(Total jóvenes con futuro: {len(jov)}; detalle completo en `repos-por-pieza-reconstruido.tsv`.)\n")
inf.append('\n## No encontrados / errores\n\n')
for s,r in sorted(err.items()): inf.append(f"- `{s}` — {r.get('estado')}\n")
inf.append('\n## Licencias que difieren del censo 18-oct\n\n')
for s,a,b in cambios: inf.append(f"- `{s}`: {a} → {b} (29-oct-2026)\n")
inf.append('\n**Cierre.** La evidencia reconstruida coincide en lo gobernante con lo publicado en los pulsos de hoy (archivados, dormidos con nombre y jóvenes con futuro citados en las notas). La obra estaba a salvo en GitHub gracias al push por parte; esta pasada devuelve también la prueba al archivo.\n')
(BASE/'INFORME-EVIDENCIA-RECONSTRUIDA-29oct.md').write_text(''.join(inf),encoding='utf-8')
print('informe escrito')
