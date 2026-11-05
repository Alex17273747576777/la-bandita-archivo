# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab/docs/talleres/pieza15')
from d15 import *
A=AGG; T=[]; w=T.append
def f(r,nombre,texto): T.append(f"{ficha(r,nombre)}. {texto}\n")

w(f"""*⚙️ El motor bajo todo · cinco piezas que casi nadie instala*

Debajo de cada gestor bonito hay un motor que hace el trabajo sucio: abre conexiones, parte el archivo en trozos, los pide en paralelo, reanuda lo que se cortó y comprueba que lo que llegó sirve. Estos cinco son los motores del tema, y su estado dice más del ecosistema que cualquier captura de pantalla.

""")
f('aria2/aria2','aria2',
  f"**{num(R['aria2/aria2']['descargas'])} descargas** y {num(R['aria2/aria2']['stars'])} estrellas: el motor que usan por dentro media docena de programas de esta lista, con trozos en paralelo, reanudación y verificación. **{R['aria2/aria2']['dias_push']} días sin un empujón** y cero cambios en treinta días: el motor más usado del tema está quieto, y no se ha roto")
f('nilaoda/N_m3u8DL-RE','N_m3u8DL-RE',
  f"**{num(R['nilaoda/N_m3u8DL-RE']['stars'])} estrellas** y {num(E['nilaoda/N_m3u8DL-RE']['commits_30d'])} cambios en treinta días: el que resuelve la descarga por trozos de vídeo en directo, que es el problema técnico de verdad. **Empujón de hoy**, {num(E['nilaoda/N_m3u8DL-RE']['adjuntos'])} adjuntos y ninguna suma")
f('rockdaboot/wget2','Wget2',
  f"**{num(E['rockdaboot/wget2']['con_huella'])} sumas de {num(E['rockdaboot/wget2']['adjuntos'])} adjuntos**: el nieto de wget, con descarga en paralelo y verificación. {num(E['rockdaboot/wget2']['commits_30d'])} cambios en treinta días y {num(R['rockdaboot/wget2']['descargas'])} descargas")
f('axel-download-accelerator/axel','Axel',
  f"**Cuatro mil cien días de vida** y {num(E['axel-download-accelerator/axel']['adjuntos'])} adjuntos: el acelerador de descargas ligero que muchos dan por muerto y sigue publicando. {R['axel-download-accelerator/axel']['dias_push']} días sin empujón y cero cambios en treinta días")
f('lwthiker/curl-impersonate','curl-impersonate',
  f"**{num(R['lwthiker/curl-impersonate']['stars'])} estrellas** y {num(E['lwthiker/curl-impersonate']['adjuntos'])} adjuntos: un curl que se hace pasar por un navegador de verdad, para las webs que solo responden a quien lo parece. **{R['lwthiker/curl-impersonate']['dias_push']} días sin un empujón**: el problema que resolvía lo resolvieron los demás")

w(f"""
Los cinco, juntos, cuentan una verdad del oficio: **el motor no se actualiza porque no hace falta**. aria2 lleva {R['aria2/aria2']['dias_push']} días sin tocar y sigue bajando {num(R['aria2/aria2']['descargas'])} archivos para quién sabe cuántos programas. Lo que cambia cada semana no es el motor, es **la web de enfrente** —y por eso yt-dlp publica casi a diario y aria2 no.

───────────────────

*🎛️ Las caras del motor clásico · cinco interfaces para el mismo motor*

Aria2 no tiene ventana. Durante quince años hubo una docena de proyectos dedicados a ponerle una, y aquí están los cinco que importan: los dos vivos, los dos congelados y el que enseña por qué una interfaz se muere.

""")
f('mayswind/AriaNg','AriaNg',
  f"**{num(R['mayswind/AriaNg']['descargas'])} descargas** y {num(R['mayswind/AriaNg']['stars'])} estrellas: la cara web que se abre en el navegador y gobierna el motor desde cualquier aparato de la casa. {num(E['mayswind/AriaNg']['commits_30d'])} cambio en treinta días y {num(E['mayswind/AriaNg']['adjuntos'])} adjuntos sin suma")
f('mayswind/AriaNg-Native','AriaNg Native',
  f"La misma cara, empaquetada como programa de escritorio: {num(R['mayswind/AriaNg-Native']['stars'])} estrellas y {num(E['mayswind/AriaNg-Native']['adjuntos'])} adjuntos. {num(E['mayswind/AriaNg-Native']['commits_30d'])} cambios en treinta días y **cero sumas**")
f('Xmader/aria-ng-gui','aria-ng-gui',
  f"**{num(R['Xmader/aria-ng-gui']['descargas'])} descargas y {R['Xmader/aria-ng-gui']['dias_push']} días sin un empujón**: fue la cara de escritorio más usada del motor y hoy está congelada. {num(E['Xmader/aria-ng-gui']['con_huella'])} sumas de {num(E['Xmader/aria-ng-gui']['adjuntos'])} adjuntos y **cero puntos** en actividad")
f('Xmader/aria-ng-gui-android','aria-ng-gui (Android)',
  f"**{R['Xmader/aria-ng-gui-android']['dias_push']} días sin empujón** y {num(E['Xmader/aria-ng-gui-android']['adjuntos'])} adjuntos: la versión de bolsillo del mismo proyecto, con {num(R['Xmader/aria-ng-gui-android']['descargas'])} descargas. Una persona detrás y {num(E['Xmader/aria-ng-gui-android']['puntos'])} puntos")
f('binux/yaaw','YAAW',
  f"**{num(R['binux/yaaw']['stars'])} estrellas, {R['binux/yaaw']['dias_push']} días sin un empujón y ninguna entrega**: «Yet Another Aria2 Webfrontend», la abuela de todas estas caras. **{E['binux/yaaw']['puntos']} puntos** y sin licencia legible: se lista como pieza de museo, no como descarga")

w("""
De las cinco, solo dos se mueven y ninguna firma. Es el patrón de toda la pieza: **la interfaz es lo que se abandona primero**, porque depende de un motor que no cambia y de una moda que sí.

───────────────────

*💻 Gestores de escritorio · seis programas y una sorpresa desagradable*

Aquí está el grupo que todo el mundo instala y casi nadie mira: los gestores con ventana, cola, velocidad y categorías. Seis fichas, y la primera es la noticia incómoda de la noche.

""")
f('GopeedLab/gopeed','Gopeed',
  f"**{num(R['GopeedLab/gopeed']['stars'])} estrellas y {num(R['GopeedLab/gopeed']['descargas'])} descargas**, con **empujón de hoy** y {num(E['GopeedLab/gopeed']['commits_30d'])} cambios en treinta días: el gestor moderno que corre en Windows, macOS, Linux, Android y en el navegador. {num(E['GopeedLab/gopeed']['adjuntos'])} adjuntos y ninguna suma")
f('agalwood/Motrix','Motrix',
  f"**{num(R['agalwood/Motrix']['stars'])} estrellas y {num(R['agalwood/Motrix']['descargas'])} descargas** —el más instalado con diferencia— y **cero cambios en treinta días**, con **sin licencia legible** en la API. {num(E['agalwood/Motrix']['adjuntos'])} adjuntos, ni una suma y {num(E['agalwood/Motrix']['incidencias']['abiertas'])} incidencias abiertas. **La sorpresa desagradable de la noche**: el gestor que recomienda medio internet no se está tocando")
f('subhra74/xdm','XDM',
  f"**Empujón de hoy** y {num(E['subhra74/xdm']['commits_30d'])} cambios en treinta días: el gestor con captura desde el navegador y aceleración por trozos, con {num(R['subhra74/xdm']['descargas'])} descargas y {num(E['subhra74/xdm']['adjuntos'])} adjuntos sin firma")
f('Tyrrrz/YoutubeDownloader','YoutubeDownloader',
  f"**{num(R['Tyrrrz/YoutubeDownloader']['stars'])} estrellas** y {num(R['Tyrrrz/YoutubeDownloader']['entregas'])} entregas: la cara de escritorio multiplataforma más pulida del tema, con **empujón de hoy** y solo {num(E['Tyrrrz/YoutubeDownloader']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['Tyrrrz/YoutubeDownloader']['incidencias']['cerradas'])} cerradas")
f('persepolisdm/persepolis','Persepolis',
  f"**{num(R['persepolisdm/persepolis']['descargas'])} descargas** y {num(E['persepolisdm/persepolis']['incidencias']['cerradas'])} incidencias cerradas: el gestor con interfaz para aria2, el más completo de los seis en funciones. **{R['persepolisdm/persepolis']['dias_push']} días sin un empujón** y {num(E['persepolisdm/persepolis']['puntos'])} puntos: vivo, pero quieto")
f('uget/uget','uGet',
  f"**{R['uget/uget']['dias_push']} días sin un empujón y {num(R['uget/uget']['stars'])} estrellas**: el gestor de la vieja guardia, sin entregas, sin licencia legible y con una sola persona. **{E['uget/uget']['puntos']} puntos**: cero. Se lista para que nadie lo instale creyendo que está vivo")

w(f"""
Hay un detalle de estos seis que sirve para entender el resto de la pieza: **ninguno de los seis firma un solo archivo**. Ni el que publica hoy, ni el que lleva una década, ni el más instalado de todos. En un tema donde el programa que descarga es justamente el que debería dar ejemplo de verificación, **{num(E['GopeedLab/gopeed']['adjuntos']+E['agalwood/Motrix']['adjuntos']+E['subhra74/xdm']['adjuntos']+E['Tyrrrz/YoutubeDownloader']['adjuntos']+E['persepolisdm/persepolis']['adjuntos']+E['uget/uget']['adjuntos'])} adjuntos publicados y ni una suma**.

Eso no los hace malos programas; los hace programas que **no te permiten comprobar qué bajaste**, que es exactamente la mitad del acto técnico. Y explica por qué la camada de 2026, con todo lo que le falta, aparece mejor parada: cuatro de los ocho publican sumas.

Siete días de diferencia separan a **Gopeed** —que publicó hoy— de **Motrix** —que no publica desde hace un mes y tiene el doble de estrellas—. Y uGet, que fue la respuesta estándar durante una década, hoy no tiene ni una entrega etiquetada. El escritorio no se muere de golpe: se queda quieto y la gente sigue instalándolo.

───────────────────
""")
open('/tmp/lab/docs/talleres/pieza15/s2.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
