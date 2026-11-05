# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab18/docs/talleres/pieza18')
from d18 import *
A=AGG; T=[]; w=T.append
def f(r,nombre,texto): T.append(f"{ficha(r,nombre)}. {texto}\n")

w(f"""*📻 La radio de siempre · cuatro piezas, y una parada hace {R['segler-alex/RadioDroid']['dias_push']} días*

La radio por internet es el tema más viejo de esta serie: hay aplicaciones que llevan más de una década abiertas y emisoras que llevan más de una década emitiendo la misma dirección. Aquí van las cuatro que sostienen el resto, con su fecha al lado y sin adornos.

""")
f('mytv-android/mytv-android','MyTV',
  f"**{num(R['mytv-android/mytv-android']['stars'])} estrellas** y {num(R['mytv-android/mytv-android']['entregas'])} entregas: reproductor de listas para Android y Android TV con tres motores dentro —Media3, IJK y VLC—, y **{num(E['mytv-android/mytv-android']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['mytv-android/mytv-android']['incidencias']['cerradas'])} cerradas. Es el nombre que el mapa de 125 daba para esta pieza y el que casi todo el mundo instala primero")
f('AntennaPod/AntennaPod','AntennaPod',
  f"**{num(R['AntennaPod/AntennaPod']['stars'])} estrellas y {num(R['AntennaPod/AntennaPod']['dias_nace'])} días de historia**: el gestor de pódcast de referencia, con {num(R['AntennaPod/AntennaPod']['entregas'])} entregas y {num(E['AntennaPod/AntennaPod']['incidencias']['cerradas'])} incidencias cerradas. **Cero adjuntos publicados**, así que su nota se queda en **{E['AntennaPod/AntennaPod']['puntos']}**: no hay archivo que comprobar. Se instala desde F-Droid, y ese es su argumento")
f('segler-alex/RadioDroid','RadioDroid',
  f"**{num(R['segler-alex/RadioDroid']['dias_push'])} días sin un empujón y cero cambios en treinta días**: la aplicación histórica de radio sobre el catálogo de radio-browser, con {num(R['segler-alex/RadioDroid']['stars'])} estrellas, {num(R['segler-alex/RadioDroid']['descargas'])} descargas y **{E['segler-alex/RadioDroid']['puntos']} puntos**. Funciona hoy y no se va a arreglar: es la misma historia que Seal en la 15 y LibreTorrent en la 16")
f('deutsia/deutsia-radio','Deutsia Radio',
  f"**{R['deutsia/deutsia-radio']['dias_push']} días sin publicar**, {num(R['deutsia/deutsia-radio']['entregas'])} entregas y **{num(E['deutsia/deutsia-radio']['con_huella'])} sumas de {num(E['deutsia/deutsia-radio']['adjuntos'])} adjuntos**: radio por varias redes —incluidas las que no pasan por el internet de siempre—, con licencia Apache y **canal de seguridad**. Nació en 2025 y se enfrió; se lista con la fecha delante")

w(f"""
**Lo que dicen las cuatro juntas:** el tema no está huérfano, está **desigualmente mantenido**. MyTV publica cada pocos días y AntennaPod lleva {num(R['AntennaPod/AntennaPod']['dias_nace'])} días sin morirse; RadioDroid, que es la que más gente tiene instalada, lleva **{R['segler-alex/RadioDroid']['dias_push']} días** quieta. Y de las cuatro, **solo una firma** —Deutsia, {num(E['deutsia/deutsia-radio']['con_huella'])} de {num(E['deutsia/deutsia-radio']['adjuntos'])}—, que es la que menos gente usa.

───────────────────

*📱 Radio en el bolsillo · la camada de 2026*

Siete aplicaciones de radio para el teléfono, seis de ellas nacidas este año y una de hace nueve meses. Casi todas comen del mismo catálogo abierto —radio-browser— y se diferencian en dos cosas: **cómo buscan** y **qué hacen cuando el enlace se cae**.

""")
f('shapeshed/aerial','aerial',
  f"**{R['shapeshed/aerial']['dias_nace']} días de vida y la tercera nota del tema ({E['shapeshed/aerial']['puntos']})**: reproductor de radio para Android, con **{num(E['shapeshed/aerial']['con_huella'])} sumas de {num(E['shapeshed/aerial']['adjuntos'])} adjuntos**, {num(R['shapeshed/aerial']['entregas'])} entregas y **empujón de hoy**. {num(E['shapeshed/aerial']['commits_30d'])} cambios en treinta días y {num(E['shapeshed/aerial']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['shapeshed/aerial']['incidencias']['abiertas'])} abiertas")
f('armanmaurya/InternetRadio','InternetRadio',
  f"**{num(R['armanmaurya/InternetRadio']['stars'])} estrellas en {num(R['armanmaurya/InternetRadio']['dias_nace'])} días**: la más usada de la camada, con {num(R['armanmaurya/InternetRadio']['entregas'])} entregas y {num(E['armanmaurya/InternetRadio']['commits_30d'])} cambios en treinta días. **{num(E['armanmaurya/InternetRadio']['adjuntos'])} adjuntos sin una suma** y **sin canal de seguridad**: el que más gente prueba y el que menos deja comprobar")
f('renyijiu/tune-roam','Tune Roam',
  f"**Solo {R['renyijiu/tune-roam']['dias_nace']} días de vida** —el más nuevo de toda la pieza—: radio por internet en Kotlin multiplataforma sobre Media3 y el catálogo abierto, con **{num(E['renyijiu/tune-roam']['con_huella'])} sumas de {num(E['renyijiu/tune-roam']['adjuntos'])} adjuntos**, {num(R['renyijiu/tune-roam']['entregas'])} entregas y **canal de seguridad**. {num(E['renyijiu/tune-roam']['commits_30d'])} cambios en treinta días")
f('vikindor/omnibeat','omnibeat',
  f"**{num(R['vikindor/omnibeat']['dias_nace'])} días y {num(R['vikindor/omnibeat']['stars'])} estrellas**: radio para Android con soporte de las emisoras modernas —las que emiten por trozos y no por flujo continuo, que es donde fallan las aplicaciones viejas—. {num(R['vikindor/omnibeat']['entregas'])} entregas y **{num(E['vikindor/omnibeat']['adjuntos'])} adjuntos sin suma**; **sin integración continua**")
f('z0rats/freqcast','freqcast',
  f"**{num(R['z0rats/freqcast']['entregas'])} entregas en {num(R['z0rats/freqcast']['dias_nace'])} días**: en vez de buscar en un catálogo, **extrae el flujo de la propia página de la emisora**. {num(R['z0rats/freqcast']['stars'])} estrellas, {num(E['z0rats/freqcast']['commits_30d'])} cambios en treinta días y {num(E['z0rats/freqcast']['adjuntos'])} adjuntos sin una suma")
f('hyliankid14/British-Radio-Player','British Radio Player',
  f"**{num(R['hyliankid14/British-Radio-Player']['entregas'])} entregas en {num(R['hyliankid14/British-Radio-Player']['dias_nace'])} días**: ochenta emisoras y más de mil pódcast en una sola aplicación, con integración de Android Auto. **Sin licencia legible**, {num(E['hyliankid14/British-Radio-Player']['adjuntos'])} adjuntos sin suma y {num(E['hyliankid14/British-Radio-Player']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['hyliankid14/British-Radio-Player']['incidencias']['abiertas'])} abierta")
f('Woodic-Way/WoodicIPTV','WoodicIPTV',
  f"**{E['Woodic-Way/WoodicIPTV']['puntos']} puntos —la nota más baja de la pieza—**, {R['Woodic-Way/WoodicIPTV']['dias_push']} días sin publicar, **una entrega, un adjunto y sin licencia legible**: nació y se apagó en el mismo mes. Se lista para que se vea que lo nuevo también puede no arrancar")

w(f"""
**El reparto de la camada, en una frase:** de las siete, **{palabras(sum(1 for r in ['shapeshed/aerial','armanmaurya/InternetRadio','renyijiu/tune-roam','vikindor/omnibeat','z0rats/freqcast','hyliankid14/British-Radio-Player','Woodic-Way/WoodicIPTV'] if E[r]['con_huella']))} firman algún archivo** y **cuatro no tienen canal de seguridad ni integración completa**. Lo nuevo de este tema llega con prisa y con poca ceremonia —lo cual está bien para probar y mal para confiar—.

───────────────────

*💻 La radio en la computadora · tres piezas pequeñas y vivas*

En el ordenador la radio se resuelve con programas que casi nadie mira: una ventana que vive en la bandeja del sistema, una aplicación de GNOME y un reproductor de terminal con visualizador. Son tres, y las tres tienen algo que las de teléfono no tienen: se pueden leer enteras en una tarde.

""")
f('TheJoeFin/Traydio','Traydio',
  f"**{num(R['TheJoeFin/Traydio']['stars'])} estrellas** y {num(R['TheJoeFin/Traydio']['entregas'])} entregas: radio por internet para Windows que **vive entera en la bandeja del sistema**, sin ventana ni cuenta. **Canal de seguridad**, {num(E['TheJoeFin/Traydio']['commits_30d'])} cambios en treinta días y {num(E['TheJoeFin/Traydio']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['TheJoeFin/Traydio']['incidencias']['cerradas'])} cerradas. **{num(E['TheJoeFin/Traydio']['adjuntos'])} adjuntos sin suma**")
f('meehow/receiver','Receiver',
  f"**{num(R['meehow/receiver']['stars'])} estrellas** y {num(R['meehow/receiver']['entregas'])} entregas: radio para GNOME con más de treinta mil emisoras del catálogo abierto. **{R['meehow/receiver']['dias_push']} días sin un empujón y cero cambios en treinta días**: el más parado de los tres, con {num(E['meehow/receiver']['adjuntos'])} adjuntos sin firma")
f('nevermore23274/AetherTune','AetherTune',
  f"**{num(R['nevermore23274/AetherTune']['stars'])} estrellas en {num(R['nevermore23274/AetherTune']['dias_nace'])} días**: radio en la terminal, escrita en Rust, **con visualizador de audio en tiempo real** —lo que no hace ninguno de los otros treinta y uno—. {num(R['nevermore23274/AetherTune']['entregas'])} entregas y {num(E['nevermore23274/AetherTune']['adjuntos'])} adjuntos sin suma; **un cambio en treinta días**")

w(f"""
**Lo que este bloque enseña, y vale para todo el tema:** en el escritorio la radio está resuelta con **tres programas de menos de cinco mil líneas** y ninguno de los tres publica una suma. Es un tema donde nadie gana dinero y, por tanto, donde nadie paga la ceremonia de firmar. Eso no los hace peores: los hace **más fáciles de leer enteros**, que es la otra forma de comprobar.

───────────────────

*📺 El directo · once programas de televisión por lista*

Aquí está lo que la gente llama «IPTV»: programas que abren una lista `.m3u` con cientos de canales, muestran una guía si la hay y reproducen el trozo. **Ninguno trae canales.** La lista la pones tú, y de dónde salga es tu problema y tu responsabilidad —de eso va la sección siguiente—. Once programas, de los cuales ocho nacieron en 2026.

""")
f('ahXN00/OwnTV','OwnTV',
  f"**{num(R['ahXN00/OwnTV']['stars'])} estrellas en {num(R['ahXN00/OwnTV']['dias_nace'])} días** y la quinta nota del tema: nativo para Android TV, con dos motores de reproducción y soporte de los tres formatos de lista que se usan de verdad. **{num(R['ahXN00/OwnTV']['entregas'])} entregas**, {num(E['ahXN00/OwnTV']['commits_30d'])} cambios en treinta días y solo {num(E['ahXN00/OwnTV']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['ahXN00/OwnTV']['incidencias']['cerradas'])} cerradas. **{num(E['ahXN00/OwnTV']['adjuntos'])} adjuntos sin suma**")
f('yaolin-dev/OKVideoMac','OKVideoMac',
  f"**{num(R['yaolin-dev/OKVideoMac']['dias_nace'])} días de vida y la segunda nota del tema ({E['yaolin-dev/OKVideoMac']['puntos']})**: reproductor nativo para Mac con **{num(E['yaolin-dev/OKVideoMac']['con_huella'])} sumas de {num(E['yaolin-dev/OKVideoMac']['adjuntos'])} adjuntos** —la mejor proporción del bloque—, {num(R['yaolin-dev/OKVideoMac']['entregas'])} entregas, **canal de seguridad** y **{num(E['yaolin-dev/OKVideoMac']['commits_30d'])} cambios en treinta días**")
f('Davidona/StreamVault-IPTV','StreamVault',
  f"**{num(R['Davidona/StreamVault-IPTV']['stars'])} estrellas** y {num(R['Davidona/StreamVault-IPTV']['entregas'])} entregas: reproductor pensado para Android TV desde el mando, con {num(E['Davidona/StreamVault-IPTV']['commits_30d'])} cambios en treinta días. **Sin licencia legible** y {num(E['Davidona/StreamVault-IPTV']['adjuntos'])} adjuntos sin una suma: el más popular del bloque y el que menos deja comprobar")
f('bilipp/Lume','Lume',
  f"**{num(R['bilipp/Lume']['stars'])} estrellas en {num(R['bilipp/Lume']['dias_nace'])} días**: reproductor nativo para las plataformas de Apple, con **canal de seguridad** y {num(R['bilipp/Lume']['entregas'])} entregas. {num(E['bilipp/Lume']['commits_30d'])} cambios en treinta días y {num(E['bilipp/Lume']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['bilipp/Lume']['incidencias']['cerradas'])} cerradas; **{num(E['bilipp/Lume']['adjuntos'])} adjuntos sin suma**")
f('infinitel8p/Extreme-InfiniTV','Extreme-InfiniTV',
  f"**{num(E['infinitel8p/Extreme-InfiniTV']['adjuntos'])} adjuntos y {num(E['infinitel8p/Extreme-InfiniTV']['con_huella'])} con suma** —el que más publica del tema con diferencia—: {num(R['infinitel8p/Extreme-InfiniTV']['entregas'])} entregas, **canal de seguridad** y guía integrada. El pero está medido: **cero cambios en treinta días** y {num(E['infinitel8p/Extreme-InfiniTV']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['infinitel8p/Extreme-InfiniTV']['incidencias']['cerradas'])} cerradas")
f('clubanderson/clubTivi','clubTivi',
  f"**{num(E['clubanderson/clubTivi']['adjuntos'])} adjuntos en {num(R['clubanderson/clubTivi']['dias_nace'])} días**: reproductor multiplataforma con emparejamiento automático de la guía y conmutación entre varias fuentes del mismo canal. **Un solo cambio en treinta días** y **{num(E['clubanderson/clubTivi']['incidencias']['abiertas'])} incidencias abiertas** sin ninguna cerrada: una idea buena aparcada")
f('mewset/better-iptv','better-iptv',
  f"**{num(E['mewset/better-iptv']['adjuntos'])} adjuntos y {num(E['mewset/better-iptv']['commits_30d'])} cambios en treinta días**: reproductor para Linux, Windows y macOS que presume de «funcionar sin más», con **canal de seguridad** y {num(R['mewset/better-iptv']['entregas'])} entregas. {num(R['mewset/better-iptv']['stars'])} estrellas y **ninguna suma** en sus adjuntos")
f('lennylxx/webos-iptv-player','webOS IPTV Player',
  f"**{num(R['lennylxx/webos-iptv-player']['dias_nace'])} días y {num(E['lennylxx/webos-iptv-player']['commits_30d'])} cambios en treinta días**: la única pieza del tema para **televisores LG**, con {num(R['lennylxx/webos-iptv-player']['entregas'])} entregas y {num(E['lennylxx/webos-iptv-player']['adjuntos'])} adjuntos sin suma. {num(E['lennylxx/webos-iptv-player']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['lennylxx/webos-iptv-player']['incidencias']['abiertas'])} abiertas")
f('opentvproject/opentv','OpenTV',
  f"**{num(R['opentvproject/opentv']['dias_nace'])} días de vida**: reproductor para Android TV, Fire TV y teléfono, sin cuenta y sin suscripción, con {num(R['opentvproject/opentv']['entregas'])} entregas y {num(R['opentvproject/opentv']['descargas'])} descargas. **Dos cambios en treinta días** y **{num(E['opentvproject/opentv']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['opentvproject/opentv']['incidencias']['cerradas'])} cerradas")
f('bsogulcan/another-iptv-player','another-iptv-player',
  f"**{num(R['bsogulcan/another-iptv-player']['dias_nace'])} días de historia y {num(R['bsogulcan/another-iptv-player']['entregas'])} entregas**: reproductor ligero multiplataforma, con {num(E['bsogulcan/another-iptv-player']['commits_30d'])} cambios en treinta días y {num(E['bsogulcan/another-iptv-player']['adjuntos'])} adjuntos sin suma. Su cola está al revés: {num(E['bsogulcan/another-iptv-player']['incidencias']['abiertas'])} abiertas contra {num(E['bsogulcan/another-iptv-player']['incidencias']['cerradas'])} cerradas")
f('dereferencex/prysm','Prysm',
  f"**{num(R['dereferencex/prysm']['stars'])} estrellas en {num(R['dereferencex/prysm']['dias_nace'])} días**: reproductor de listas para Android y Android TV construido sobre una base web —lo que lo hace pequeño y lo que lo hace lento al abrir—. {num(R['dereferencex/prysm']['entregas'])} entregas, {num(E['dereferencex/prysm']['commits_30d'])} cambios en treinta días y **{R['dereferencex/prysm']['dias_push']} días sin publicar**")

w(f"""
**El retrato del bloque:** ocho de los once son de 2026, cuatro llevan menos de un año de vida y **solo uno firma en cantidad** —Extreme-InfiniTV, {num(E['infinitel8p/Extreme-InfiniTV']['con_huella'])} de {num(E['infinitel8p/Extreme-InfiniTV']['adjuntos'])}—. Y ese, a la vez, lleva un mes sin un cambio. La pieza que mejor combina juventud, mantenimiento y firma es **OKVideoMac**, con {num(R['yaolin-dev/OKVideoMac']['stars'])} estrellas: el más pequeño de los once y el único que se puede comprobar al instalar.

───────────────────

*🔧 Las herramientas del directo · la lista y la guía*

Tres programas que no reproducen nada y sirven para que lo demás funcione. Son las piezas más pequeñas de la serie —{num(R['suuhm/xmltv-splitter']['stars'])} estrella entre dos de ellas— y las que más tiempo ahorran.

""")
f('xyzs996/iptv-doctor','iptv-doctor',
  f"**{num(E['xyzs996/iptv-doctor']['commits_30d'])} cambios en treinta días** —el ritmo más alto del tema, con {num(R['xyzs996/iptv-doctor']['stars'])} estrellas y {R['xyzs996/iptv-doctor']['dias_nace']} días—: quita de la lista los enlaces muertos, arregla los nombres de la guía y devuelve un archivo que sí abre. {num(R['xyzs996/iptv-doctor']['entregas'])} entrega y {num(E['xyzs996/iptv-doctor']['adjuntos'])} adjuntos sin suma")
f('Ruby184/epg-tools','epg-tools',
  f"**{num(E['Ruby184/epg-tools']['commits_30d'])} cambios en treinta días** y {num(R['Ruby184/epg-tools']['entregas'])} entregas: herramientas de guía para Node que leen XMLTV, listas y fuentes privadas y recortan por día. **{R['Ruby184/epg-tools']['dias_nace']} días de vida** y **sin adjuntos ni descargas**: es una biblioteca")
f('suuhm/xmltv-splitter','xmltv-splitter',
  f"**{R['suuhm/xmltv-splitter']['dias_push']} días sin publicar y cero entregas**: filtra un archivo de guía por canales, que es exactamente lo que hace falta cuando la guía completa pesa cien megas y tu televisor tiene veinte canales. **{num(R['suuhm/xmltv-splitter']['dias_nace'])} días**, una estrella y **{E['suuhm/xmltv-splitter']['puntos']} puntos**: útil y abandonado")

w(f"""
**Por qué estas tres importan más de lo que parecen:** el 90 % de los problemas del directo no son de reproducción, son de **datos** —un enlace que caducó, un canal con dos nombres, una guía que pesa más que el disco—. Un reproductor bonito con una lista rota no sirve para nada; estas tres arreglan la lista. Y son las tres que nadie recomienda, porque no tienen captura de pantalla que enseñar.

───────────────────

*🎙️ Emitir tú · el servidor, la automatización y la captura*

El tema tiene una mitad que casi nunca se cuenta: **poner tu propia señal**. Cuatro piezas, todas vivas, todas para gente que quiere emitir radio desde casa o desde un servidor de cinco dólares sin pedirle permiso a una plataforma.

""")
f('AzuraCast/AzuraCast','AzuraCast',
  f"**{num(R['AzuraCast/AzuraCast']['stars'])} estrellas y {num(R['AzuraCast/AzuraCast']['dias_nace'])} días**: suite completa de radio por internet —emisión, programación, estadísticas, varios canales a la vez— que se instala con un comando. **Empujón de hoy**, {num(E['AzuraCast/AzuraCast']['commits_30d'])} cambios en treinta días y **canal de seguridad**. **Cero adjuntos publicados**: se despliega con Docker, no se descarga un instalador")
f('libretime/libretime','LibreTime',
  f"**{num(R['libretime/libretime']['entregas'])} entregas y {num(E['libretime/libretime']['con_huella'])} sumas de {num(E['libretime/libretime']['adjuntos'])} adjuntos**: plataforma de emisión y automatización de parrilla —la sucesora libre de Airtime—, con **canal de seguridad** y {num(E['libretime/libretime']['commits_30d'])} cambios en treinta días. {num(R['libretime/libretime']['stars'])} estrellas y {num(R['libretime/libretime']['dias_nace'])} días de historia")
f('xiph/Icecast-Server','Icecast',
  f"**El servidor que hace posible casi toda la radio abierta**: {num(R['xiph/Icecast-Server']['dias_nace'])} días de historia, {num(R['xiph/Icecast-Server']['stars'])} estrellas y **cero entregas etiquetadas en GitHub** —es un espejo de un repositorio que vive en gitlab.xiph.org, y eso hay que decirlo—. **Sin integración continua** y {R['xiph/Icecast-Server']['dias_push']} días desde el último empujón")
f('streamlink/streamlink','streamlink',
  f"**La nota más alta de la pieza ({E['streamlink/streamlink']['puntos']})**: saca el flujo de un directo y lo pasa a un reproductor sin recodificar, desde la terminal. **{num(R['streamlink/streamlink']['stars'])} estrellas**, {num(R['streamlink/streamlink']['entregas'])} entregas, **{num(E['streamlink/streamlink']['con_huella'])} sumas de {num(E['streamlink/streamlink']['adjuntos'])} adjuntos**, **canal de seguridad** y **{num(E['streamlink/streamlink']['incidencias']['cerradas'])} incidencias cerradas** contra {num(E['streamlink/streamlink']['incidencias']['abiertas'])} abiertas")

w(f"""
**Lo que este bloque cambia del tema:** con estas cuatro, la radio deja de ser algo que se recibe y pasa a ser algo que **se emite**. Es la diferencia entre usar la infraestructura de otro y tener la tuya —y es la misma distinción que la pieza 9 hacía con las nubes y la 12 con el kit de reemplazo—. **Icecast + AzuraCast o LibreTime** es una emisora completa y gratis; **streamlink** es la herramienta que evita depender de la página web de nadie para oír un directo.

**Y el detalle honesto:** de las cuatro, la que peor se deja comprobar es la más importante —Icecast— porque su código vive fuera de GitHub y aquí no hay ni una entrega que medir.

───────────────────
""")
open('/tmp/lab18/docs/talleres/pieza18/s2.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
