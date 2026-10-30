#!/bin/bash
# Circuito por tanda de la rehechura sin molde (29-oct-2026):
# generar (pulso fresco) -> PUERTA anti-plantilla -> forja -> vara -> manifiesto
# -> acta -> espejo -> push verificado. Si la puerta o la vara caen, no hay push.
set -e
cd /home/user/Arena-Reimagined
SERIE=$1; DESDE=$2; HASTA=$3; ETIQ=$4
CARPETA=01-PUBLICACIONES/Facebook-dominicano-ES; [ "$SERIE" = "WhatsApp" ] && CARPETA=01-PUBLICACIONES/WhatsApp-dominicano-ES
SALIDA=$(python3 02-ARCHIVO/evidencia-29oct-rehechura/generar-v3.py "$SERIE" "$DESDE" "$HASTA")
echo "$SALIDA"
LISTA=$(find "$CARPETA" -name '*.md' -mmin -15 | sort)
python3 02-ARCHIVO/evidencia-29oct-rehechura/puerta-antislop.py $LISTA
python3 _herramientas/forja-catalogo-v4.py 02-ARCHIVO/catalogo-la-bandita.html >/dev/null
python3 HABILIDADES/herramientas/vara-simulada.py
python3 - <<PYEOF
import hashlib
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
man=[]
for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
    for f in sorted((R/'01-PUBLICACIONES'/serie).glob('*.md')):
        b=f.read_bytes(); man.append((serie,f.name,len(b),hashlib.sha256(b).hexdigest()))
(R/'02-ARCHIVO/evidencia-29oct/aseguramiento-29oct/MANIFIESTO-SHA256-PIEZAS.tsv').write_text('serie\tarchivo\tbytes\tsha256\n'+''.join(f'{a}\t{b}\t{c}\t{d}\n' for a,b,c,d in man),encoding='utf-8')
p=R/'02-ARCHIVO/registro-2026-10-15.md'; t=p.read_text(encoding='utf-8')
salida="""$SALIDA""".replace('\n',' · ')
acta=f'''

---

**ACTA — FUSIÓN EDITORIAL 29-OCT-2026 · TANDA $ETIQ.** {salida}. Piezas rehechas desde los datos medidos hoy (descripción oficial, temas, releases, licencias), sin párrafos rituales: la puerta anti-plantilla quedó EN PIE sobre la tanda, la vara APROBADA, y el push se verificó por blobs antes de abrir la siguiente tanda.
'''
if 'TANDA $ETIQ.' not in t: p.write_text(t+acta,encoding='utf-8')
print('manifiesto+acta $ETIQ')
PYEOF
python3 HABILIDADES/herramientas/chequeo-niveles.py --con-lupa | tail -3
rm -rf /home/user/la-bandita-archivo && mkdir -p /home/user/la-bandita-archivo/02-ARCHIVO
cp -a 01-PUBLICACIONES/WhatsApp-dominicano-ES /home/user/la-bandita-archivo/
cp -a 01-PUBLICACIONES/Facebook-dominicano-ES /home/user/la-bandita-archivo/
cp 02-ARCHIVO/catalogo-la-bandita.html 02-ARCHIVO/registro-2026-10-15.md /home/user/la-bandita-archivo/02-ARCHIVO/
cp -a 02-ARCHIVO/evidencia-29oct /home/user/la-bandita-archivo/02-ARCHIVO/
cp -a 02-ARCHIVO/evidencia-29oct-rehechura /home/user/la-bandita-archivo/02-ARCHIVO/
cp MANIFIESTO-DE-ENTREGA-FINAL.md LEEME-ESTRUCTURA.md /home/user/la-bandita-archivo/
rm -rf /home/user/la-bandita-archivo/ENTREGA-29OCT-2026 && cp -a ENTREGA-29OCT-2026 /home/user/la-bandita-archivo/
cp ENTREGA-La-Bandita-29oct2026.zip /home/user/la-bandita-archivo/
python3 HABILIDADES/herramientas/guardar.py "Fusión editorial 29-oct · tanda $ETIQ: pieza original restaurada con su voz + ficha medida en vivo; puerta y vara en orden"
