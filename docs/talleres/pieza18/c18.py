# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab18/docs/talleres/pieza18')
from d18 import *
A=AGG; T=[]; w=T.append

w(f"""*📊 La tabla completa de las {palabras(A['vivos'])} · lo medido, fila por fila*

El registro entero, ordenado por nota. La columna de firmas se repite en toda la pieza: **{num(A['con_huella'])} de {num(A['adjuntos'])}**.

| # | Recurso | Nota | ★ | Último empujón | Entregas | Sumas / adjuntos |
|---|---|---|---|---|---|---|
""")
for i,r in enumerate(sorted(VIVOS,key=lambda x:(-E[x]['puntos'],x)),1):
    e=E[r]; ea=R[r]
    w(f"| {i} | {r} | **{e['puntos']}** | {num(ea['stars'])} | {cuando(r).replace('**','')} | {num(ea['entregas'])} | {num(e['con_huella'])} / {num(e['adjuntos'])} |\n")
w(f"""
Leída en vertical dice tres cosas: **{palabras(A['con_huella_repos'])} de {palabras(A['vivos'])} firman algún archivo**, **{palabras(A['sin_ci'])} no tienen integración continua** y **{palabras(A['sin_entrega'])} no han etiquetado una sola versión**. Leída en horizontal deja ver el hueco de la pieza: entre **streamlink ({E['streamlink/streamlink']['puntos']})** y **WoodicIPTV ({E['Woodic-Way/WoodicIPTV']['puntos']})** no hay una diferencia de público, hay una de **{num(E['streamlink/streamlink']['con_huella'])} archivos firmados** frente a ninguno. **Lo que no mide:** si el canal se ve, si la emisora sigue emitiendo o si la guía coincide. Eso depende de la lista, no del programa.

───────────────────

*🎓 Glosario mínimo · diez palabras del directo*

- **Flujo** (*stream*): una dirección que emite sin parar. No se descarga: se escucha mientras dura la conexión.
- **Lista** (`.m3u`): el archivo con los canales y sus direcciones. Es el 90 % de los problemas del directo.
- **Manifiesto**: el índice que dice qué trozos hay ahora. Cambia cada pocos segundos.
- **HLS**: el formato por trozos del directo moderno. Explica el retraso de treinta segundos y el salto atrás.
- **EPG**: la guía de programación. Vive en un XML aparte y **siempre** se desincroniza de la lista.
- **XMLTV**: el formato de esa guía. Pesa; por eso existen las herramientas que la recortan.
- **Xtream**: el formato de lista más extendido entre los servicios de pago. Los reproductores lo aceptan como si fuera abierto.
- **radio-browser**: el catálogo comunitario de emisoras del que comen casi todas las apps de radio. Abierto, con votos y comprobaciones.
- **Tiempo real** (*live*): lo que se emite ahora. En HLS llega siempre unos segundos tarde, y no hay ajuste que lo arregle del todo.
- **Codificar** (*transcodificar*): convertir el flujo a otro formato. Es lo que **no** hace streamlink, y por eso suena igual que el original.

───────────────────

*⚖️ La responsabilidad · la señal de quién es*

Este tema tiene una parte legal más visible que la de los torrentes y conviene ponerla en el centro, no al final. **Un reproductor es neutral; una lista no lo es.**

**La radio abierta existe y es legítima.** Hay decenas de miles de emisoras que emiten por internet **a propósito**, con su dirección publicada en su propia página, para que las escuches. Copiar esa dirección en tu reproductor es exactamente lo que la emisora quiere. Casi todas las aplicaciones de bolsillo de esta pieza viven de eso, y el catálogo comunitario que las alimenta es una infraestructura pública. **Ese es el uso normal de esta pieza y el que recomiendo.**

**Las listas de televisión son otro asunto.** Una lista `.m3u` de miles de canales no la publica ningún canal: la arma alguien que **está redifundiendo una señal que no le pertenece**. Comprar, regalar o encontrar una lista así no cambia la naturaleza del asunto. En la República Dominicana la **Ley 65-00** sobre derecho de autor protege las emisiones, y el **INDOTEL** regula el espectro y los servicios de telecomunicaciones; en otros países cambia el organismo, no la idea. **Esta pieza no da consejo legal** y no enlaza ninguna lista: enlaza **programas**, que es lo que se puede medir.

**Lo que sí se puede hacer sin discusión, y está en esta lista:** ver la televisión **abierta** de tu país por internet, que cada vez más canales ofrecen; escuchar radio; montar **tu propia emisora** con AzuraCast o LibreTime; y usar estas herramientas para **organizar lo que ya tienes derecho a ver** —una lista de canales públicos, una guía recortada, un enlace propio—.

**Y una advertencia técnica con consecuencias legales:** un reproductor de listas **abre direcciones que le mandan**. Una lista de origen desconocido es una lista de direcciones desconocidas; algunas hacen peticiones raras, y el reproductor, por diseño, las obedece. No es paranoia: es el mismo consejo de siempre, aplicado a un archivo que se pasa por WhatsApp.

**La raya de esta casa, otra vez.** No se publica aquí cómo conseguir una lista de pago sin pagarla, ni qué servicio la vende. Se miden programas con fecha y con firma, y se dice qué lado de la línea es cuál.

───────────────────

*🔏 La huella del tema · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}*

**{num(A['adjuntos'])} archivos publicados por las {palabras(A['vivos'])} piezas. {num(A['con_huella'])} con suma de comprobación. El 14,1 %.**

En su escala, donde ya está todo el año: tiendas de la 10, **0,08 %**; aplicaciones de la 11, **5,5 %**; torrentes de la 16, **8,7 %**; descarga de la 15, **10,6 %**; audio de la 13, **11,4 %**; **radio y directo, 14,1 %**; kit de la 12, **17,0 %**; teclados de la 17, **19,0 %**; música de la 14, **20,0 %**.

**{palabras(A['vivos']-A['con_huella_repos'])} de los {palabras(A['vivos'])} no publican ni una suma.** Los que sí:

""")
w("| Recurso | Adjuntos | Con suma | Nota |\n|---|---|---|---|\n")
for c_,a_,r in sorted([(E[r]['con_huella'],E[r]['adjuntos'],r) for r in VIVOS if E[r]['con_huella']],reverse=True):
    w(f"| {r.split('/')[1]} | {num(a_)} | **{num(c_)}** | {E[r]['puntos']} |\n")
w(f"""
Dos lecturas. **Extreme-InfiniTV firma {num(E['infinitel8p/Extreme-InfiniTV']['con_huella'])} archivos** y **OKVideoMac {num(E['yaolin-dev/OKVideoMac']['con_huella'])}**, y entre los dos ponen **más de dos tercios** de las {num(A['con_huella'])} sumas del tema; el primero lleva un mes sin cambiar y el segundo tiene {R['yaolin-dev/OKVideoMac']['dias_nace']} días. Y **AntennaPod, AzuraCast e Icecast —las tres más conocidas— no firman nada aquí**: las dos primeras no publican adjuntos y la tercera es un espejo.

**Lo que se puede hacer hoy:** verificar la suma cuando existe; instalar desde **F-Droid** o el gestor de paquetes de la distribución, que al menos pasa por un mantenedor; y desconfiar del APK que llega por chat, que es la vía normal de los reproductores de listas.

───────────────────

*🛠️ Seis órdenes para revisar el directo tú mismo*

1. **Probar un enlace antes de cargarlo.** `curl -sI -m 10 "<dirección>" | head -3` — si no responde 200 o 302 en diez segundos, ese canal está muerto y no es culpa del reproductor.
2. **Ver si la lista está viva de verdad.** `curl -s -m 20 "<lista>.m3u" | grep -c '^http'` — cuántas direcciones trae. Después se compara con las que abren, y la diferencia es la basura.
3. **Mirar el tamaño de la guía antes de dársela al televisor.** `curl -s -m 30 "<guia>.xml.gz" | gunzip | wc -c` — cien megas de guía en un televisor de 1 GB de memoria es una mala idea.
4. **Cortar la guía por canales.** `python3 -m xmltv --help` o las herramientas de esta pieza: se queda uno con los veinte canales que ve y tira el resto.
5. **Saber de dónde viene un flujo sin abrir el navegador.** `streamlink --stream-url "<dirección>" best` — devuelve la dirección real del flujo, que es lo que se pega en el reproductor que sí quieres usar.
6. **Comprobar quién es el dueño de la señal.** `whois <dominio>` y la página oficial del canal: si la dirección no está publicada por la emisora, la señal no es tuya para verla así.

Las órdenes **1 a 5** se ejecutan en tu equipo; la sexta es la que evita el problema legal y la que casi nadie hace.

───────────────────

*🚪 Lo que esta pieza no tiene*

**Ni una sola lista, ni un canal, ni una dirección de emisión.** Esta pieza enlaza **programas** —los {palabras(A['vivos'])} de arriba— y nada más. No hay `.m3u`, no hay guía, no hay servicio de pago ni forma de conseguir uno.

**No es una lista de lo más nuevo.** Es un censo con fechas: {palabras(A['nuevas2026'])} piezas de 2026 ganan en nota, pero también se dice que **RadioDroid lleva {R['segler-alex/RadioDroid']['dias_push']} días** quieta y que **WoodicIPTV** nació y se apagó en el mismo mes.

**No hay aplicaciones cerradas.** Ni una. Las grandes plataformas de radio y de televisión de pago no están porque no se pueden medir: sin repositorio, sin licencia y sin archivo que comprobar.

*📅 La semana de prueba · cinco días para tener la radio y el directo bajo control*

- **Día uno.** Prueba las tres órdenes primeras con tu lista actual: cuántos canales trae, cuántos abren y cuánto pesa la guía. La mayoría de la gente descubre que ve veinte canales de una lista de ochocientos.
- **Día dos.** Instala **aerial** o **InternetRadio** y escucha una emisora de tu país por su dirección oficial. Ese es el uso limpio del tema y el que no tiene letra pequeña.
- **Día tres.** En la computadora, **Traydio** si usas Windows o **receiver** si usas GNOME, y **streamlink** para el directo que la web no te deja sacar.
- **Día cuatro.** Pasa tu lista por **iptv-doctor** y recorta la guía con las herramientas del bloque. Si el televisor va más rápido, era eso.
- **Día cinco.** Si te interesa emitir, monta **Icecast** en un equipo de casa y conéctale **AzuraCast**. No hace falta público: hace falta entender la diferencia entre recibir y emitir.

───────────────────

*❓ Las preguntas del grupo*

**¿Es legal escuchar radio por internet?**
Sí, cuando la emisora publica su dirección para eso, que es el caso normal: hay decenas de miles de emisoras que emiten para ser escuchadas. El problema nunca es el reproductor.

**¿Y las listas de televisión que circulan?**
Son redifusiones de señales ajenas. Esta pieza enlaza programas, no listas, y no explica cómo conseguir ninguna. La televisión **abierta** de tu país por su web oficial sí es un uso limpio.

**¿Por qué se corta el directo cada dos por tres?**
Porque el enlace apunta a un servidor que cambia, o porque el reproductor pide el trozo siguiente y el manifiesto ya cambió. Las órdenes 1 y 2 lo separan en un minuto.

**¿Por qué la tele va treinta segundos por detrás?**
Porque el directo moderno se emite por trozos y el reproductor guarda unos cuantos de margen. Es el precio de que no se congele con mala conexión.

**¿Cuál instalo para ver la tele en el televisor?**
**OwnTV** u **opentv** si es Android TV; **webOS IPTV Player** si es un LG. Y si es Apple, **Lume** o **OKVideoMac**, el único del bloque que firma {num(E['yaolin-dev/OKVideoMac']['con_huella'])} de {num(E['yaolin-dev/OKVideoMac']['adjuntos'])} archivos.

**¿Puedo tener mi propia emisora?**
Sí, y es de las cosas más satisfactorias de esta lista: **Icecast** como servidor y **AzuraCast** o **LibreTime** encima. Lo que no se puede es emitir música con derechos sin pagarlos; eso se llama licencia y no lo arregla el software.

───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **la radio no se descarga, se persigue**. {palabras(A['vivos'])} piezas, {num(A['estrellas'])} estrellas y ninguna archivada, y el problema del tema sigue siendo el mismo que hace quince años: el enlace que dura un minuto. Lo que ha cambiado es quién lo mantiene.

Lo segundo: **lo nuevo llegó con prisa a este tema**. **{palabras(A['nuevas2026'])} piezas de 2026**, {palabras(A['push7'])} con código de la última semana, y a la vez {palabras(A['sin_ci'])} sin integración continua: mucha gente escribiendo reproductores y poca gente poniendo compuertas.

Lo tercero: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 14,1 %**, por encima de los torrentes y de la descarga y por debajo del resto. Las dos más conocidas del tema —AntennaPod y AzuraCast— **no publican un solo adjunto**, así que no hay nada que comprobar.

Y lo cuarto: **la mitad del tema es emitir, no ver**. **AzuraCast**, **LibreTime** e **Icecast** son la diferencia entre consumir la infraestructura de otro y tener la tuya, y esa es la idea que esta serie viene repitiendo desde la pieza 9.

───────────────────
""")
w(f"""— {num(A['adjuntos'])} archivos publicados por {palabras(A['vivos'])} piezas y {num(A['con_huella'])} firmados: el 14,1 %, con dos programas poniendo más de dos tercios.
— Cuatro de la radio de siempre, siete de bolsillo, tres de escritorio, once del directo, tres herramientas y cuatro para emitir: nombre, fecha, licencia y nota, sin una sola lista ni un solo canal.
— La parte legal puesta en el centro —la radio abierta es legítima; las listas de televisión no lo son— y seis órdenes para comprobar un enlace, una guía y un dueño antes de cargarlos.

💓 *La Bandita informa a partir de fuentes fechadas.* {palabras(A['vivos'])} piezas medidas hoy una por una —de la emisora de siempre al reproductor de tres meses, del servidor que emite al programa que saca el flujo—, la tabla completa, los {num(A['con_huella'])} archivos firmados contados uno por uno y el enlace que hay que comprobar antes de dárselo al televisor.

───────────────────

*Medición del corte:* jueves 5 de noviembre de 2026, {HORA} de la mañana en Santo Domingo, con la fecha comprobada en vivo antes de empezar y al terminar · decimonovena medición del día · {palabras(A['vivos'])} piezas vivas, ninguna archivada, {palabras(A['sin_lic'])} sin licencia legible · {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas · {num(A['descargas'])} descargas · {palabras(A['con_huella_repos'])} repositorios firmando.

*🔗 Enlaces*

*La radio de siempre:*
""")
GRUPOS=[("La radio de siempre",['mytv-android/mytv-android','AntennaPod/AntennaPod','segler-alex/RadioDroid','deutsia/deutsia-radio']),
        ("Radio en el bolsillo · 2026",['shapeshed/aerial','armanmaurya/InternetRadio','vikindor/omnibeat','z0rats/freqcast','renyijiu/tune-roam','hyliankid14/British-Radio-Player','Woodic-Way/WoodicIPTV']),
        ("La radio en la computadora",['TheJoeFin/Traydio','meehow/receiver','nevermore23274/AetherTune']),
        ("El directo · televisión por lista",['ahXN00/OwnTV','Davidona/StreamVault-IPTV','opentvproject/opentv','bilipp/Lume','clubanderson/clubTivi','infinitel8p/Extreme-InfiniTV','lennylxx/webos-iptv-player','yaolin-dev/OKVideoMac','bsogulcan/another-iptv-player','mewset/better-iptv','dereferencex/prysm']),
        ("Las herramientas del directo",['xyzs996/iptv-doctor','suuhm/xmltv-splitter','Ruby184/epg-tools']),
        ("Emitir tú",['AzuraCast/AzuraCast','libretime/libretime','xiph/Icecast-Server','streamlink/streamlink'])]
usados=set()
for titulo,rs in GRUPOS:
    w(f"\n*{titulo}:*\n\n")
    for r in rs:
        usados.add(r); w(f"- https://github.com/{r}\n")
assert set(VIVOS)==usados, (set(VIVOS)-usados, usados-set(VIVOS))
w(f"""
*Las direcciones de las órdenes:*

- api de un repositorio cualquiera: https://api.github.com/repos/AzuraCast/AzuraCast
- api de las entregas: https://api.github.com/repos/yaolin-dev/OKVideoMac/releases?per_page=100

───────────────────

*🗒️ Notas al pie*

(5-nov) La fecha se comprobó **en vivo antes de empezar y al terminar**: `tools/fecha_viva.py --inicio` y `--fin` al cerrar. **Antes de sondear** se hizo la revisión obligatoria —fecha, historial y ecosistema— con `tools/preflight.py --tema radio`; su acta está en `docs/PREFLIGHT-radio-2026-11-05.json`. La medición es de las {HORA} y vive en `docs/MEDICION-18-noche-2026-11-04.json`.

(5-nov) **Esta es la pieza que el mapa de 125 ponía en el número 18.** La 17 se adelantó al teclado con IA por petición del dueño; aquí se retoma el orden con el mismo método y el mismo preflight.

(5-nov) La cuenta de **huella** es la de toda la serie: `sha256`, `sha512`, `sha1`, `checksum`, `.sig`, `.asc` o `sums` en el nombre de cada adjunto de las últimas cien entregas. Escala del año: 0,08 % · 5,5 % · 8,7 % · 10,6 % · 11,4 % · **14,1 %** · 17,0 % · 19,0 % · 20,0 %.

(5-nov) Las **notas** se calculan con los nueve pesos de la casa y las cuatro penalizaciones: **streamlink saca {E['streamlink/streamlink']['puntos']} con {num(R['streamlink/streamlink']['stars'])} estrellas** y **AntennaPod {E['AntennaPod/AntennaPod']['puntos']} con {num(R['AntennaPod/AntennaPod']['stars'])}**. La vara no premia la fama: premia que haya algo que comprobar.

(5-nov) **Ninguna lista ni canal en esta pieza.** Se enlazan programas, no contenido: es la misma norma que en la 16 y aquí pesa más porque el uso legítimo y el otro se parecen demasiado desde fuera.

(5-nov) **El taller queda en `docs/talleres/pieza18/`**, con los generadores del texto, para que las cifras se puedan repetir desde el repositorio (H22).

*#task*

#task 083 · volver a medir las {palabras(A['vivos'])} el 5 de diciembre y decir si RadioDroid, receiver y WoodicIPTV publicaron: si no, salen de la recomendación.

#task 084 · probar iptv-doctor con una lista propia de canales abiertos y contar cuántos enlaces muertos quita y cuántos nombres de guía arregla.

#task 085 · montar Icecast más AzuraCast en un equipo de casa y medir cuánto pesa una emisora de una sola calidad durante una hora.

#task 086 · escribir la pieza 19 —el vídeo que abre todo— con el mismo método: preflight previo, medición fechada y ninguna cifra escrita a mano.

───────────────────

🏷️ Etiquetas estratégicas

#RadioPorInternet #IPTV #Streamlink #AzuraCast #Icecast #Aerial #OwnTV #AntennaPod #RadioBrowser #LibreTime #OpenSourceDominicano #Directo
""")
open('/tmp/lab18/docs/talleres/pieza18/s3.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
