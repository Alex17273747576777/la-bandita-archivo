#!/usr/bin/env python3
"""HABILIDAD · AUTOEVOLUCIÓN (la casa aprende de cada experiencia)
Registra una lección en la bitácora, sube la versión del sistema de habilidades y deja
la regla lista para que la próxima sesión la aplique sin re-descubrirla.
Uso: python3 aprender.py "contexto" "qué falló" "regla nueva" """
import re, sys
from datetime import datetime
from pathlib import Path
HAB=Path(__file__).resolve().parent.parent
bit=HAB/'bitacora-lecciones.md'; evo=HAB/'EVOLUCION.md'
ctx,fallo,regla=sys.argv[1],sys.argv[2],sys.argv[3]
hoy=datetime.now().strftime('%Y-%m-%d')
t=bit.read_text(encoding='utf-8')
n=len(re.findall(r'^## L-\d+',t,re.M))+1
t+=f'\n## L-{n:02d} · {hoy}\n- **Contexto:** {ctx}\n- **Fallo/experiencia:** {fallo}\n- **Regla que queda:** {regla}\n'
bit.write_text(t,encoding='utf-8')
e=evo.read_text(encoding='utf-8')
m=re.search(r'v(\d+)\.(\d+)',e); nueva=f'v{int(m.group(1))}.{int(m.group(2))+1}'
e=re.sub(r'v\d+\.\d+',nueva,e,count=1)
e+=f'\n- **{nueva} ({hoy})** · L-{n:02d}: {regla}\n'
evo.write_text(e,encoding='utf-8')
print(f'lección L-{n:02d} registrada · sistema de habilidades ahora en {nueva}')
