#!/usr/bin/env python3
"""Auditoría objetiva offline: codificación, duplicados, marcadores, URL y sintaxis.
No declara sano nada por exit 0: escribe conteos y muestras para corregir de verdad."""
import re, json, hashlib
from pathlib import Path
from collections import Counter
R=Path('/home/user/Arena-Reimagined')
SERIES=['WhatsApp-dominicano-ES','Facebook-dominicano-ES']
MOJI=['Ã','Â','â€','�','\ufffd']
res={}
def norm(s): return re.sub(r'\s+',' ',s).strip()
allfiles=[]
for serie in SERIES:
 for f in sorted((R/'01-PUBLICACIONES'/serie).glob('*.md')):
  if f.name.startswith('LEEME'): continue
  allfiles.append((serie,f))
# codificación y caracteres
cod={'replacement':[], 'mojibake':[], 'control':[], 'zerowidth':[], 'sin_nota':[], 'nota_multiple':[]}
dupbloques={}; hashes={}
for serie,f in allfiles:
 b=f.read_bytes()
 try: t=b.decode('utf-8')
 except UnicodeDecodeError as e: cod['replacement'].append((serie,f.name,str(e))); continue
 if '�' in t: cod['replacement'].append((serie,f.name,t.count('�')))
 if any(m in t for m in MOJI): cod['mojibake'].append((serie,f.name,[m for m in MOJI if m in t][:3]))
 ctrl=[c for c in t if ord(c)<32 and c not in '\n\t']
 if ctrl: cod['control'].append((serie,f.name,Counter(map(hex,map(ord,ctrl))).most_common(3)))
 if any(c in t for c in '\u200b\u200c\u200d\ufeff'): cod['zerowidth'].append((serie,f.name,''))
 if t.count('💓')==0: cod['sin_nota'].append((serie,f.name,''))
 if t.count('💓')>1: cod['nota_multiple'].append((serie,f.name,t.count('💓')))
 hashes.setdefault(hashlib.sha256(b).hexdigest(),[]).append((serie,f.name))
 blocks=[norm(x) for x in re.split(r'\n\s*\n',t) if len(norm(x))>=120]
 c=Counter(blocks); d={k:v for k,v in c.items() if v>1}
 if d: dupbloques[f'{serie}/{f.name}']={'bloques_distintos_duplicados':len(d),'sobrantes':sum(v-1 for v in d.values())}
res['codificacion']=cod
res['archivos_identicos']=[v for v in hashes.values() if len(v)>1]
res['duplicados_bloques']={'archivos':len(dupbloques),'detalle':dupbloques}
# marcadores y frases
patrones={
 'licencia_sin_resolver':'Licencias sin resolver hoy',
 'estrella_sin_medir':'★—',
 'usuario_repositorio':'usuario/repositorio',
 'todo_marcador':r'\bTODO\b|\bTBD\b',
 'lorem':'Lorem ipsum',
 'sin_licencia_declarada':'sin licencia declarada',
 'licencia_sin_clasificar':'licencia sin clasificar (NOASSERTION)',
}
marc={}
for nombre,pat in patrones.items():
 hits=[]
 for serie,f in allfiles:
  t=f.read_text(encoding='utf-8')
  n=len(re.findall(pat,t))
  if n: hits.append((serie,f.name,n))
 marc[nombre]={'ocurrencias':sum(x[2] for x in hits),'archivos':len(hits),'muestra':hits[:12]}
res['marcadores']=marc
# URL sintaxis
urls=Counter(); malas=[]
urlre=re.compile(r'https?://[^\s<>\]\)\}"\'·]+')
for serie,f in allfiles:
 t=f.read_text(encoding='utf-8')
 for u in urlre.findall(t):
  u2=u.rstrip('.,;:')
  urls[u2]+=1
  if any(c in u2 for c in 'áéíóúñ') or u2.startswith('http://github.com/') and False: pass
  parts=u2.split('/')
  if u2.startswith('https://github.com/') and len(parts)>=5:
   slug='/'.join(parts[3:5])
   if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',slug): malas.append((serie,f.name,u2))
res['urls']={'unicas':len(urls),'apariciones':sum(urls.values()),'github_malformadas':malas[:20]}
# encabezados repetidos (posible ritual)
heads=Counter(); headfiles={}
for serie,f in allfiles:
 t=f.read_text(encoding='utf-8')
 for l in t.splitlines():
  s=l.strip()
  if re.match(r'^(\*[^*]{4,80}\*|## .{4,80}|[A-ZÁÉÍÓÚÑ0-9][A-ZÁÉÍÓÚÑ0-9 ,:;·—-]{8,80})$',s):
   heads[s]+=1; headfiles.setdefault(s,set()).add(f.name)
res['encabezados_repetidos']=[{'h':h,'veces':n,'archivos':len(headfiles[h])} for h,n in heads.most_common(40)]
out=R/'02-ARCHIVO/evidencia-29oct/correccion-final-29oct/auditoria-objetiva.json'
out.write_text(json.dumps(res,ensure_ascii=False,indent=1),encoding='utf-8')
print('archivos auditados:',len(allfiles))
print('codificación:',{k:len(v) for k,v in cod.items()})
print('archivos idénticos:',len(res['archivos_identicos']),'· con bloques duplicados:',len(dupbloques))
print('marcadores:',{k:(v['ocurrencias'],v['archivos']) for k,v in marc.items()})
print('urls únicas:',res['urls']['unicas'],'malformadas:',len(malas))
print('informe:',out)
