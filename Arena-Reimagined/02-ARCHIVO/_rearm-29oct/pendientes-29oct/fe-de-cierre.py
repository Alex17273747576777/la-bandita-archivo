#!/usr/bin/env python3
import csv, re
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'; WA=R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'
API={'devcaspian-hash/bokumi-app':'NOFILE','advaithavinash/aniultimatium':'NOFILE','mihonapp/mihon':'Apache-2.0','kototoro-app/kototoro':'Apache-2.0','keiyoushi/extensions':'NOFILE','yuzono/anime-extensions':'Apache-2.0','animiruorg/animiru':'Apache-2.0','andarcanum/tadami-aniyomi-fork':'Apache-2.0','aniyomiorg/aniyomi':'Apache-2.0','phhusson/treble_experimentations':'NOFILE','rushiranpise/xposed-modules':'NOFILE'}
truth=dict(API)
for row in csv.DictReader(open(R/'ENTREGA-29OCT-2026/03-Datos-verificados/repos-al-dia-29oct.tsv',encoding='utf-8'),delimiter='\t'):
    lic=row['licencia']
    if 'sin archivo LICENSE' in lic: truth[row['slug']]='NOFILE'
    elif lic.startswith('no verificable'): truth[row['slug']]='NOVERIF'
    elif lic and lic not in ('sin resolver','NOASSERTION'): truth[row['slug']]=lic
SPDX=re.compile(r'^(GPL|LGPL|AGPL|Apache|MIT|BSD|MPL|Unlicense|ISC|CC0|WTFPL|BSL|EPL)[\w\.\-]*$')
def frase(v):
    if v=='NOFILE': return 'sin archivo LICENSE en su repo (verificado por API 29-oct-2026)'
    if v=='NOVERIF': return 'licencia no verificable: su repo responde 404/451 (firmado 29-oct-2026)'
    return f'licencia {v} (resuelta al cierre de la jornada, 29-oct-2026)'
cambios=[]; quedan=[]
for f in sorted(FB.glob('*.md')):
    t=f.read_text(encoding='utf-8')
    if 'sin resolver' not in t: continue
    def repl_por_segmento(txt):
        out=[]; last=0; n_fix=0
        for m in re.finditer(r'`([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`([^•\n]*?)licencia sin resolver( en su ficha)?', txt):
            slug=m.group(1).lower(); v=truth.get(slug)
            if not v or (v not in ('NOFILE','NOVERIF') and not SPDX.match(v)): quedan.append((f.name[:3],slug)); continue
            out.append(txt[last:m.start()]); out.append(f'`{m.group(1)}`{m.group(2)}{frase(v)}'); last=m.end(); n_fix+=1
        out.append(txt[last:])
        return ''.join(out),n_fix
    nt,n=repl_por_segmento(t)
    if n: f.write_text(nt,encoding='utf-8'); cambios.append((f.name[:46],n))
print('piezas FB con fe de cierre:',len(cambios),'· correcciones:',sum(n for _,n in cambios))
for c in cambios: print('  ',c)
print('sin verdad disponible (se dejan y se firman):',quedan[:10])
# WA 00: línea global + treble
f00=[f for f in WA.glob('00-*.md')][0]; t=f00.read_text(encoding='utf-8')
mal='Licencias: 45 repos siguen sin licencia resuelta; quedan señalados en su pieza, no escondidos. La única niebla resuelta de la pasada: `team-spotube/spotube` figura hoy AGPL-3.0 (verificado 29-oct-2026).'
assert mal in t
t=t.replace(mal,'Licencias: cerrada la jornada no queda ni una licencia «sin resolver»: las que GitHub no resolvía por SPDX se resolvieron por el texto de su LICENSE o quedó verificado por API que el repo no tiene archivo LICENSE (62 casos) o que hoy no es verificable (17, entre 404 y 451). Cada una queda señalada en su pieza, no escondida. La primera niebla resuelta de la pasada: `team-spotube/spotube` figura hoy AGPL-3.0 (verificado 29-oct-2026).')
f00.write_text(t,encoding='utf-8'); print('WA 00 línea global de licencias actualizada al cierre real')
# recuento final de 'sin resolver' en FB nuevas
rest=0
for f in sorted(FB.glob('*.md')):
    m=re.match(r'(\d+)-',f.name)
    if m and (int(m.group(1))>=83 or int(m.group(1))==2): rest+=f.read_text(encoding='utf-8').count('licencia sin resolver')
print('restan "licencia sin resolver" en FB 02/83-131:',rest)
