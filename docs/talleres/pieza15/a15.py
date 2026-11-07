# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab/docs/talleres/pieza15')
from d15 import *
A=AGG; T=[]; w=T.append

w(f"""*Descargar es un acto técnico: {palabras(A['vivos'])} programas medidos hoy —{palabras(A['nuevas2026'])} nacidos en 2026, las dos aplicaciones más famosas del tema paradas y lo que la ley no dice—*

*La Bandita · miércoles 4 de noviembre de 2026, {HORA} en Santo Domingo · edición dominicano-español · pieza 15 de Facebook*

⏱️ *Lectura total: 30 minutos · {palabras(A['vivos'])} programas medidos hoy a las {HORA} · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])} —el 10,6 %— · {num(A['estrellas'])} estrellas · {num(A['descargas'])} descargas · {palabras(A['sin_lic'])} sin licencia legible · cero archivados · {palabras(A['nuevas2026'])} de 2026*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · bajar un archivo no es un delito, y tampoco es un accidente
├── ⚡ En una página
├── 🕰️ La medición de las {HORA} · la decimosexta del día
├── 🔁 Qué reemplaza a qué · la tabla de la descarga
├── ⚙️ El motor bajo todo · cinco piezas que nadie instala (cinco)
├── 🎛️ Las caras del motor clásico (cinco)
├── 💻 Gestores de escritorio (seis) y 🕹️ en el bolsillo (tres)
├── 💬 La línea de órdenes · cuatro programas que sí se auditan
├── 🌱 Los {palabras(A['nuevas2026'])} nacidos en 2026 · la camada de la descarga
├── ⚖️ Lo que la ley permite, lo que la app permite y lo que el archivo dice de sí mismo
├── 🔏 La huella del tema · {num(A['con_huella'])} de {num(A['adjuntos'])} · y 🛠️ seis órdenes
└── 🚪 lo que no tiene · 📅 la semana · ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

> *Semilla de esta pieza:* bajar un archivo es la operación más vieja de internet y la que peor se cuenta. La conversación pública la trata como un delito o como una hazaña, y casi nunca como lo que es: **un acto técnico con tres decisiones** —de dónde sale, cómo se comprueba y qué se hace con lo que llega—.

Esta pieza mide los programas que hacen esas tres cosas. No dice qué bajar; dice **con qué**, y sobre todo **cómo saber que lo que llegó es lo que se pidió**. Y trae dos sorpresas que no esperaba al empezar el censo.

La primera: **las dos aplicaciones más famosas del tema están paradas**. Seal, la cara amable de yt-dlp en Android, con {num(R['JunkFood02/Seal']['stars'])} estrellas y {num(R['JunkFood02/Seal']['descargas'])} descargas, lleva **{R['JunkFood02/Seal']['dias_push']} días sin un empujón y cero cambios en treinta días**, con **{num(E['JunkFood02/Seal']['incidencias']['abiertas'])} incidencias abiertas**. Motrix, el gestor de escritorio que todo el mundo instala primero, tiene {num(R['agalwood/Motrix']['stars'])} estrellas y también **cero cambios en treinta días**.

La segunda: **lo nuevo, otra vez, firma mejor que lo viejo**. De los {palabras(A['nuevas2026'])} nacidos en 2026, {palabras(sum(1 for r in VIVOS if R[r]['dias_nace']<=300 and E[r]['con_huella']))} publican sumas de comprobación; de los veintitrés veteranos, {palabras(A['con_huella_repos']-sum(1 for r in VIVOS if R[r]['dias_nace']<=300 and E[r]['con_huella']))}. La camada de este año entiende algo que la de 2018 no: que un instalador sin suma es un acto de fe.

───────────────────

*⚡ En una página*

{palabras(A['vivos']).capitalize()} programas, medidos hoy a las {HORA}: **{num(A['estrellas'])} estrellas**, **{num(A['descargas'])} descargas**, {palabras(A['push_hoy'])} con empujón de hoy, **cero archivados**. La nota mediana es **{num(int(A['mediana_puntos']))} sobre 80** y **{palabras(A['sin_lic'])}** no declaran licencia legible.

Los mejores: **rayburst** con **{E['AnInsomniacy/rayburst']['puntos']}**, **yt-dlp**, **Stash** y **downvid** con **{E['yt-dlp/yt-dlp']['puntos']}**, **ytdlnis** con **{E['deniscerri/ytdlnis']['puntos']}** y **MovieBox-Tui** con **{E['mesamirh/MovieBox-Tui']['puntos']}**. Cuatro de esos seis **nacieron este año**. El más veterano de todos, **yt-dlp**, tiene {num(R['yt-dlp/yt-dlp']['stars'])} estrellas y {num(E['yt-dlp/yt-dlp']['incidencias']['cerradas'])} incidencias cerradas: es el motor que mueve media lista.

Y el dato que da el tono: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 10,6 %** —por debajo del 20 % de los clientes de música de ayer y muy por encima del 0,08 % de las tiendas de extensiones—. Lo sostienen diez proyectos, y **uno solo pone cien**: rayburst, con tres meses de vida.

Lo que le falta al tema: **{palabras(A['sin_entrega'])} sin ninguna entrega etiquetada** y **{palabras(A['sin_ci'])} sin integración continua**. Y lo que le sobra, en el buen sentido: **ningún archivado**, la primera pieza desde la 12 que puede decir eso.

Hay una tercera cosa que no esperaba y que es la que más me ha costado escribir: **de los {palabras(A['vivos'])}, {palabras(A['vivos']-A['con_huella_repos'])} no publican ni una sola suma de comprobación** —ni uno de los seis gestores de escritorio, ni una de las cinco caras del motor clásico, ni las tres apps de Android—. Es decir: la mitad del ecosistema de la descarga no te deja comprobar el archivo que te da. Un tema sobre cómo saber qué llegó, donde casi nadie publica cómo saberlo.

───────────────────

*🕰️ La medición de las {HORA} · la decimosexta del día*

Antes de sondear nada se hizo la revisión que ahora es regla: **la fecha en vivo a las 22:28**, el **historial** —catorce piezas publicadas, la 15 pendiente según el mapa de 125— y el **ecosistema**: seis consultas a la API de búsqueda por fecha de creación antes de elegir un solo candidato. Todo eso queda en `docs/PREFLIGHT-descarga-2026-11-04.json`. Después se midieron los {palabras(A['vivos'])} a las {HORA}, en `docs/MEDICION-15b-noche-2026-11-04.json`.

Las cinco notas más altas, con lo que las sostiene:

| Recurso | Nota | Lo que la sostiene | Lo que le falta |
|---|---|---|---|
| rayburst | {E['AnInsomniacy/rayburst']['puntos']} | {num(E['AnInsomniacy/rayburst']['con_huella'])} sumas de {num(E['AnInsomniacy/rayburst']['adjuntos'])} · {num(E['AnInsomniacy/rayburst']['commits_30d'])} cambios al mes | {R['AnInsomniacy/rayburst']['dias_nace']} días de vida |
| Stash | {E['rawnaldclark/Stash']['puntos']} | {num(E['rawnaldclark/Stash']['commits_30d'])} cambios al mes · canal de seguridad | {num(E['rawnaldclark/Stash']['adjuntos'])} adjuntos sin una suma |
| downvid | {E['Downvid/downvid']['puntos']} | {num(E['Downvid/downvid']['adjuntos'])} adjuntos · canal de seguridad · {R['Downvid/downvid']['dias_nace']} días | sin una suma publicada |
| yt-dlp | {E['yt-dlp/yt-dlp']['puntos']} | {num(E['yt-dlp/yt-dlp']['con_huella'])} sumas · {num(E['yt-dlp/yt-dlp']['incidencias']['cerradas'])} incidencias cerradas | nada que la vara mida |
| ytdlnis | {E['deniscerri/ytdlnis']['puntos']} | {num(E['deniscerri/ytdlnis']['commits_30d'])} cambios al mes · canal de seguridad | {num(E['deniscerri/ytdlnis']['adjuntos'])} adjuntos sin una suma |

**La nota no mide si el programa baja lo que tú quieres: mide si se puede comprobar.** Stash y downvid sacan 70 sin firmar un archivo porque publican, atienden y mantienen un canal de seguridad; y Seal, con treinta mil estrellas, saca 42 porque lleva un mes sin moverse.

───────────────────

*🔁 Qué reemplaza a qué · la tabla de la descarga*

| Lo que usas hoy | Qué tiene de viejo | Qué lo cubre hoy |
|---|---|---|
| Un gestor de escritorio que no recuerda | Motrix: {num(R['agalwood/Motrix']['stars'])} estrellas y **cero cambios en treinta días** | **Gopeed**, **XDM**, **Persepolis**, **YoutubeDownloader** y los nuevos **prism** y **downvid** |
| La app de Android para bajar vídeo | Seal: {num(R['JunkFood02/Seal']['stars'])} estrellas y **{R['JunkFood02/Seal']['dias_push']} días sin empujón** | **ytdlnis**, la bifurcación que sí publica: {num(E['deniscerri/ytdlnis']['commits_30d'])} cambios al mes |
| Una web con ventanas y botones | Sin versión, sin suma y sin código | **yt-dlp**, **lux**, **you-get**, **gallery-dl**: línea de órdenes, auditable |
| Un cliente de escritorio para todo | Pesa cientos de megas y no dice de dónde baja | **rayburst**, **Stash**, **MovieBox-Tui**: tres de 2026, con notas de 68 a 71 |
| Copiar la dirección del vídeo a mano | Se rompe cada vez que la web cambia | **N_m3u8DL-RE** y **curl-impersonate**: los dos que resuelven lo que los demás no |
| *—* (nadie lo mira) | Que el archivo llegue entero | **{num(A['con_huella'])} sumas de {num(A['adjuntos'])} archivos**: la columna que casi nadie publica |

**Una regla que esta pieza no se salta:** no se enlaza **ningún** cliente ni índice de torrentes. Ese es el tema de la pieza 16 y, además, la familia que Facebook vetó en la 12 (E40, H20). Aquí se mide software de descarga directa y se dice lo que hace; nada más.

───────────────────
""")
open('/tmp/lab/docs/talleres/pieza15/s1.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
