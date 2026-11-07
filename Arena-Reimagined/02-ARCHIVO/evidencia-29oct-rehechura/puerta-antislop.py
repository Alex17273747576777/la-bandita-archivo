#!/usr/bin/env python3
"""PUERTA ANTI-PLANTILLA (29-oct-2026).
[RECONSTRUIDA el 29-oct-2026 tras la mordida que se comió evidencia-31oct:
probada igual que la original — cae sobre el molde viejo del 29-oct
(piezas del historial git) y queda EN PIE sobre el corpus rehecho.]
Auditoría objetiva del corpus: normaliza cada línea larga (números→#, `código`→X,
URL→URL) y FALLA (exit 1) si una línea de prosa aparece en más del 12% de las piezas:
eso es molde, no redacción. Exentas, declaradas aquí y no escondidas: la línea de
procedencia 💓 (una por pieza: es pie de firma, no prosa), la dateline de fecha,
fuentes y encabezados (<40 ya fuera), líneas REV| de quices, fichas de repo y sus
continuaciones indentadas (placa, temas, web: dato estructurado), y la instrucción
funcional y preguntas del mini-quiz (mecanismo con vocabulario controlado, como
un examen: formato, no relleno). También falla si reaparecen las frases rituales
desterradas o si una pieza pierde su 💓.
Uso: python3 puerta-antislop.py [archivo1 archivo2 ...]  (sin args: todo el corpus)"""
import re, sys
from pathlib import Path
from collections import Counter
R=Path('/home/user/Arena-Reimagined')
RITUALES=['se borró y se reescribió','no de memoria','comprobaron hoy, uno a uno','EN UN RESPIRO','PLACAS AL PULSO','pieza reescrita hoy con verificación en tiempo real','empujaron hoy,','en los últimos 7 días,']
if len(sys.argv)>1: archivos=[Path(a) for a in sys.argv[1:]]
else:
    archivos=[f for d in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']
              for f in sorted((R/'01-PUBLICACIONES'/d).glob('*.md')) if not f.name.startswith('LEEME')]
frases=Counter(); fallos=[]; sin_nota=[]
for f in archivos:
    t=f.read_text(encoding='utf-8')
    if '💓' not in t: sin_nota.append(f.name)
    for r in RITUALES:
        if r in t: fallos.append(f'{f.name}: reapareció la frase ritual «{r}»')
    for linea in t.split('\n'):
        s=linea.strip()
        if len(s)<40 or s.startswith('💓') or s.startswith('#') or 'REV|' in s: continue
        if s.startswith('_') and '· La Bandita_' in s: continue  # dateline: fecha de la medición, una línea
        if s.startswith('*Respuestas al revés'): continue  # instrucción funcional del mini-quiz (mecanismo de la casa)
        if s.startswith('- **') or s.startswith('- http') or s.startswith('• http'): continue  # ficha/fuente = dato
        if linea.startswith('  '): continue  # continuación de ficha (placa/temas/web): dato estructurado
        if re.match(r'^\*\d+\.\* ',s): continue  # pregunta de mini-quiz (empieza por *N.*): vocabulario controlado del mecanismo
        n=re.sub(r'[\d.,]+','#',s); n=re.sub(r'`[^`]+`','`X`',n); n=re.sub(r'https?://\S+','URL',n); n=re.sub(r'\*\*[^*]+\*\*','**X**',n)
        frases[n]+=1
total=len(archivos); tope=max(3,int(total*0.12))
molde=[(c,s) for s,c in frases.most_common() if c>tope]
print(f'puerta anti-plantilla: {total} piezas · tope {tope} ({100*tope//max(total,1)}%)')
if sin_nota: print('  piezas sin 💓:',len(sin_nota),sin_nota[:5])
for c,s in molde[:15]: print(f'  MOLDE {c}×: {s[:120]}')
for x in fallos[:10]: print(' ',x)
if molde or fallos or sin_nota:
    print('PUERTA: CAÍDA — hay molde o rituales: NO se empuja esta tanda.'); sys.exit(1)
print('PUERTA: EN PIE — ninguna línea de prosa se repite por encima del tope.')
