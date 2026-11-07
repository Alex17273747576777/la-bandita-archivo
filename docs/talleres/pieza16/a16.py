# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab16/docs/talleres/pieza16')
from d16 import *
A=AGG; T=[]; w=T.append

w(f"""*El torrent que no se rinde: {palabras(A['vivos'])} piezas medidas hoy —{palabras(A['nuevas2026'])} de 2026, un protocolo de veinte años y la parte que nadie quiere leer—*

*La Bandita · miércoles 4 de noviembre de 2026, {HORA} en Santo Domingo · edición dominicano-español · pieza 16 de Facebook*

⏱️ *Lectura total: 30 minutos · {palabras(A['vivos'])} piezas medidas hoy a las {HORA} · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])} —el 8,7 %, la proporción más baja del año— · {num(A['estrellas'])} estrellas · {num(A['descargas'])} descargas · {palabras(A['sin_lic'])} sin licencia legible · cero archivados · {palabras(A['nuevas2026'])} de 2026*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · un protocolo que lleva veinte años funcionando sin dueño
├── ⚡ En una página
├── 🕰️ La medición de las {HORA} · la decimoséptima del día
├── 🔁 Qué reemplaza a qué · la tabla del torrent
├── 🧱 Los clientes de siempre · siete piezas, ninguna con enlace
├── 🌱 Las {palabras(A['nuevas2026'])} de 2026 · la camada que sí se mueve
├── 🤖 Automatizar y vigilar · dos piezas de fontanería
├── 🧰 Lo que no es un cliente y también hace falta · tres programas con enlace
├── ⚖️ La responsabilidad · lo que el protocolo no decide y la ley sí
├── 🔏 La huella del tema · {num(A['con_huella'])} de {num(A['adjuntos'])} · y 🛠️ seis órdenes
└── 🚪 lo que no tiene · 📅 la semana · ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

> *Semilla de esta pieza:* el protocolo «BitTorrent» cumple {num(R['webtorrent/webtorrent']['dias_nace'])} días desde su primera publicación y no tiene dueño, ni servidor central, ni empresa que lo pueda cerrar. Eso explica dos cosas a la vez: **por qué sigue funcionando** y **por qué nadie te va a avisar cuando algo deje de funcionar**.

Esta pieza mide {palabras(A['vivos'])} piezas de ese ecosistema: siete clientes veteranos, {palabras(A['nuevas2026'])} proyectos de 2026, dos herramientas de automatización y tres programas que no son clientes y hacen falta igual —comprobar un archivo, ver la salud de un disco—. **Ningún cliente ni índice de torrentes lleva enlace aquí**, y eso no es un olvido: Facebook retiró la pieza 12 por un enlace de esta familia (E40). Se dan el nombre, lo que hacen y la orden con la que se comprueban. Las direcciones viajan en la versión de WhatsApp.

Y hay una cifra que esta noche rompe la tendencia de la serie hacia arriba: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 8,7 %** —la más baja desde la pieza 11—. En un tema donde la integridad del archivo es la mitad del asunto, **{palabras(A['vivos']-A['con_huella_repos'])} de los {palabras(A['vivos'])} no publican ni una suma**. La mitad de la cifra la pone un solo programa: qBittorrent, con {num(E['qbittorrent/qBittorrent']['con_huella'])}.

───────────────────

*⚡ En una página*

{palabras(A['vivos']).capitalize()} piezas, medidos hoy a las {HORA}: **{num(A['estrellas'])} estrellas**, **{num(A['descargas'])} descargas**, {palabras(A['push_hoy'])} con empujón de hoy y **cero archivados**. La nota mediana es **{num(int(A['mediana_puntos']))} sobre 80** y **{palabras(A['sin_lic'])} no declaran licencia legible**: la peor proporción de licencias del año, y con nombres conocidos.

Los mejores: **autobrr** con **{E['autobrr/autobrr']['puntos']}**, la nota más alta de la pieza y una de las más altas de la serie; **piko**, **Atrium** y **qBittorrent** con **{E['NihilDigit/piko']['puntos']}**; y **emule-qt** y **upbrr** con **{E['ModderMule/emule-qt']['puntos']}**. De esos seis, **cuatro son de 2026** y dos son veteranos que llevan más de una década publicando.

De actividad: **{palabras(A['push7'])} con código en la última semana** y **{palabras(A['push_hoy'])} hoy mismo**. De lo nuevo: **{palabras(A['nuevas'])} nacido en los últimos noventa días** y {palabras(A['nuevas2026'])} en todo 2026. De lo que falta: **{palabras(A['sin_entrega'])} sin ninguna entrega etiquetada** y **{palabras(A['sin_ci'])} sin integración continua**.

Y el dato incómodo, con nombre y fecha: **libretorrent lleva {R['proninyaroslav/libretorrent']['dias_push']} días sin un empujón** y **Deluge {R['deluge-torrent/deluge']['dias_push']}**, con **{E['deluge-torrent/deluge']['puntos']} puntos** y ninguna entrega. Los dos siguen en las listas de «mejores clientes de 2026» que circulan.

───────────────────

*🕰️ La medición de las {HORA} · la decimoséptima del día*

Antes de elegir nada se hizo la revisión que ya es regla: **fecha en vivo**, **historial** —quince publicadas, la 16 pendiente según el mapa de 125— y **ecosistema**: dos consultas a la API de búsqueda por fecha de creación y por tema. Acta en `docs/PREFLIGHT-torrent-2026-11-04.json`. Después se midieron las {palabras(A['vivos'])} piezas a las {HORA}, en `docs/MEDICION-16-noche-2026-11-04.json`.

Las cinco notas más altas, con lo que las sostiene:

| Recurso | Nota | Lo que la sostiene | Lo que le falta |
|---|---|---|---|
| autobrr | {E['autobrr/autobrr']['puntos']} | {num(E['autobrr/autobrr']['con_huella'])} sumas de {num(E['autobrr/autobrr']['adjuntos'])} · {num(E['autobrr/autobrr']['incidencias']['cerradas'])} incidencias cerradas | nada que la vara mida |
| piko | {E['NihilDigit/piko']['puntos']} | {num(E['NihilDigit/piko']['con_huella'])} sumas · {num(E['NihilDigit/piko']['commits_30d'])} cambios al mes | {R['NihilDigit/piko']['dias_nace']} días de vida |
| Atrium | {E['retransmit/Atrium']['puntos']} | canal de seguridad · {num(E['retransmit/Atrium']['commits_30d'])} cambios al mes | {num(E['retransmit/Atrium']['adjuntos'])} adjuntos sin suma |
| qBittorrent | {E['qbittorrent/qBittorrent']['puntos']} | {num(E['qbittorrent/qBittorrent']['con_huella'])} sumas de {num(E['qbittorrent/qBittorrent']['adjuntos'])} · canal de seguridad | solo {num(R['qbittorrent/qBittorrent']['entregas'])} entregas etiquetadas |
| emule-qt | {E['ModderMule/emule-qt']['puntos']} | {num(E['ModderMule/emule-qt']['commits_30d'])} cambios al mes · {num(E['ModderMule/emule-qt']['con_huella'])} sumas | {num(R['ModderMule/emule-qt']['stars'])} estrellas |

**La nota mide si se puede comprobar, no si el programa es popular.** autobrr saca {E['autobrr/autobrr']['puntos']} con {num(R['autobrr/autobrr']['stars'])} estrellas y emule-qt saca {E['ModderMule/emule-qt']['puntos']} con {num(R['ModderMule/emule-qt']['stars'])}: la diferencia de fama es de doce a uno y la de nota es de once puntos. Y al revés: **qBittorrent, con {num(R['qbittorrent/qBittorrent']['stars'])} estrellas —el más famoso de todos—, saca {E['qbittorrent/qBittorrent']['puntos']}** porque publica pocas entregas etiquetadas.

───────────────────

*🔁 Qué reemplaza a qué · la tabla del torrent*

| Lo que usas hoy | Qué tiene de viejo | Qué lo cubre hoy |
|---|---|---|
| El cliente que instalaste en 2019 | Depende de que su proyecto siga con vida | **qBittorrent** si quieres ventana, **transmission** si quieres un demonio, **torrra** y **piko** si quieres algo que no existía en 2019 |
| La aplicación de Android que ya no se actualiza | libretorrent: **{R['proninyaroslav/libretorrent']['dias_push']} días sin un empujón** | **BATorrent**, **hop** y **Atrium**: tres de 2026, con repositorio y fecha |
| La consola web de tu servidor | Depende de un complemento que ya nadie mantiene | **Atrium** en el móvil, **torrent-tui** en la terminal |
| Un gestor de torrents para escritorio | Deluge: **{R['deluge-torrent/deluge']['dias_push']} días sin publicar** y {num(R['deluge-torrent/deluge']['entregas'])} entregas | **qBittorrent**, **transmission** y las piezas nuevas de 2026 |
| Automatizar lo que se baja | Se hace a mano, de noche, con suerte | **autobrr** y **upbrr**, las dos de la misma casa |
| *—* (nadie lo mira) | Que el archivo llegue entero y el disco aguante | **RHash**, **coreutils** y **smartmontools**, las tres con enlace |

**Lo que esta tabla no dice, y hay que decirlo aparte:** un cliente de torrentes no decide qué es legal. Un cliente solo mueve trozos entre pares. Lo que decide son **la obra que compartes, el derecho que tienes sobre ella y la ley de tu país** —y de eso va la sección de responsabilidad, más abajo.

───────────────────
""")
open('/tmp/lab16/docs/talleres/pieza16/s1.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
