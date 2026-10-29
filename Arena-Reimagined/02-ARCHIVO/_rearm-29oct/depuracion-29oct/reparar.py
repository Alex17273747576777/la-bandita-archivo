#!/usr/bin/env python3
import collections, hashlib
from pathlib import Path
R=Path('/home/user/Arena-Reimagined'); WA=R/'01-PUBLICACIONES/WhatsApp-dominicano-ES'; FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
cambios=[]
# 1) mojibake WA 10
f10=[f for f in WA.glob('10-GLTools*.md')][0]
t=f10.read_text(encoding='utf-8')
mal='con sobre riesgo alto (desactivaciones automáticas a causa del sello de garantía detectado en aand�現絶のp; treaties metacarpáleas, placas samadas, el barco Criscal)'
assert '�' in t and '現絶' in t
t=t.replace(mal,'con riesgo alto para quien no sabe lo que toca (pérdida de garantía y de soporte del fabricante). En República Dominicana ninguna ley lo prohíbe: es responsabilidad de quien decide hacerlo con conocimiento')
f10.write_text(t,encoding='utf-8'); cambios.append(('WAREPARADA',f10.name,'mojibake corregido'))
# 2) deduplicar párrafos exactos >120 chars (WA+FB)
def dedupe(carp):
    for f in sorted(carp.glob('*.md')):
        t=f.read_text(encoding='utf-8')
        paras=t.split('\n\n'); vistos=set(); out=[]; quitados=0; chars=0
        for p in paras:
            s=p.strip()
            if len(s)>120:
                if s in vistos: quitados+=1; chars+=len(s); continue
                vistos.add(s)
            out.append(p)
        if quitados:
            nt='\n\n'.join(out)
            f.write_text(nt,encoding='utf-8')
            cambios.append((f.parent.name[:2],f.name,f'dedup: -{quitados} párrafos ({chars:,} chars) · {len(t):,}→{len(nt):,}'))
dedupe(WA); dedupe(FB)
tot=[c for c in cambios if 'dedup' in c[2]]
print('piezas reparadas en total:',len(cambios),'· con dedupe:',len(tot))
for c in sorted(tot,key=lambda x:-int(x[2].split('(')[1].split()[0].replace(',','')))[:10]: print(c[1][:60],c[2])
# largos resultantes WA canónicas
lens=[]
for f in sorted(WA.glob('*.md')):
    n=len(f.read_text(encoding='utf-8'))
    lens.append((n,f.name[:3]))
lens.sort(); print('WA min:',lens[0],'· max:',lens[-1])
Path('02-ARCHIVO/_rearm-29oct/depuracion-29oct/reparacion.json').write_text(__import__('json').dumps(cambios,ensure_ascii=False,indent=1),encoding='utf-8')
