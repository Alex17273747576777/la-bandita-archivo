# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab18/docs/talleres/pieza18')
from d18 import *
A=AGG; T=[]; w=T.append

w(f"""*La radio y el directo: {palabras(A['vivos'])} piezas medidas hoy —el enlace que dura un minuto, la guía que hay que mantener a mano y la proporción de firma del 14,1 %—*

*La Bandita · jueves 5 de noviembre de 2026, {HORA} de la mañana en Santo Domingo · edición dominicano-español · pieza 18 de Facebook*

⏱️ *Lectura total: 30 minutos · {palabras(A['vivos'])} piezas medidas hoy a las {HORA} · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])} —el 14,1 %— · {num(A['estrellas'])} estrellas · {num(A['descargas'])} descargas · {palabras(A['sin_lic'])} sin licencia legible · cero archivados · {palabras(A['nuevas2026'])} de 2026*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · el enlace que dura un minuto
├── ⚡ En una página
├── 🕰️ La medición de las {HORA} · la decimonovena del día
├── 🧠 Cómo funciona el directo · la lista, la guía y el trozo
├── 🔁 Qué reemplaza a qué · la tabla de la radio
├── 📻 La radio de siempre · cuatro piezas, una parada hace {R['segler-alex/RadioDroid']['dias_push']} días
├── 📱 Radio en el bolsillo · la camada de 2026 · y 💻 la radio en la computadora
├── 📺 El directo · once programas de televisión por lista
├── 🔧 Las herramientas del directo · la lista y la guía · y 🎙️ emitir tú
├── 📊 La tabla completa · 🎓 glosario · ⚖️ la responsabilidad
└── 🔏 la huella · 🛠️ seis órdenes · 🚪 lo que no tiene · 📅 la semana · ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

> *Semilla de esta pieza:* un enlace de radio por internet **no es un archivo**: es una dirección a la que te conectas y que deja de existir cuando el servidor cambia de dueño, de puerto o de ánimo. La mitad de los programas de esta pieza sirven para lo mismo —volver a encontrar el enlace cuando se rompe— y ninguno lo resuelve del todo. Ese es el tema: **la radio no se descarga, se persigue**.

Mide {palabras(A['vivos'])} piezas, todas vivas y ninguna archivada: cuatro de la radio de siempre, siete de bolsillo nacidas casi todas este año, tres de escritorio, once reproductores de televisión por lista, tres herramientas del directo y cuatro para **emitir tú mismo**. **{palabras(A['nuevas2026'])} son de 2026** y tres nacieron en los últimos noventa días, así que este no es un tema cerrado: es un tema que volvió.

Y la cifra: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}: el 14,1 %**. Por encima de los torrentes de la 16 y de la descarga de la 15, por debajo del kit de la 12. En un tema donde se instala software para **recibir una señal ajena**, que el instalador se pueda comprobar sigue siendo la asignatura pendiente.

───────────────────

*⚡ En una página*

{palabras(A['vivos']).capitalize()} piezas, medidas hoy a las {HORA}: **{num(A['estrellas'])} estrellas**, **{num(A['descargas'])} descargas**, {palabras(A['push7'])} con empujón de la última semana y **cero archivados**. La nota mediana es **{num(int(A['mediana_puntos']))} sobre 80** —la más baja de la serie desde la 15— y **{palabras(A['sin_lic'])} no declaran licencia legible**.

Los mejores: **streamlink** con **{E['streamlink/streamlink']['puntos']}**, la nota más alta del tema y una de las más altas del año, con {num(E['streamlink/streamlink']['incidencias']['cerradas'])} incidencias cerradas; **OKVideoMac** y **aerial** con **{E['yaolin-dev/OKVideoMac']['puntos']}** y **{E['shapeshed/aerial']['puntos']}**, dos proyectos de este año con {num(E['yaolin-dev/OKVideoMac']['adjuntos'])} y {num(E['shapeshed/aerial']['adjuntos'])} adjuntos; y **libretime** con **{E['libretime/libretime']['puntos']}**, la plataforma de emisión que lleva {num(R['libretime/libretime']['dias_nace'])} días publicando.

De actividad: **{palabras(A['push7'])} con código de la última semana** y {palabras(A['push_hoy'])} hoy mismo, pero solo {palabras(A['ci'])} flujos de integración en total. De lo nuevo: **{palabras(A['nuevas'])} nacidos en los últimos noventa días** y {palabras(A['nuevas2026'])} en 2026. De lo que falta: **{palabras(A['sin_entrega'])} sin ninguna entrega etiquetada** y **{palabras(A['sin_ci'])} sin integración continua**.

Y el dato incómodo, con nombre y fecha: **RadioDroid**, la aplicación de radio por internet con más historia del ecosistema abierto —{num(R['segler-alex/RadioDroid']['stars'])} estrellas— lleva **{R['segler-alex/RadioDroid']['dias_push']} días sin un empujón** y **cero cambios en treinta días**. Sigue en todas las listas de «mejores apps de radio» de 2026.

───────────────────

*🕰️ La medición de las {HORA} · la decimonovena del día*

Antes de elegir nada, la revisión que ya es regla: **fecha en vivo**, **historial** —diecisiete publicadas y la 18 en el mapa de 125— y **ecosistema**, con dos consultas a la API por fecha de creación. Acta en `docs/PREFLIGHT-radio-2026-11-05.json`. Después se midieron las {palabras(A['vivos'])} piezas a las {HORA}, en `docs/MEDICION-18-noche-2026-11-04.json`.

**Esta sí es la pieza del mapa.** La 17 se adelantó al teclado con IA porque el dueño lo pidió; esta retoma el número que quedó libre y lo hace con el mismo método.

Las cinco notas más altas, con lo que las sostiene:

| Recurso | Nota | Lo que la sostiene | Lo que le falta |
|---|---|---|---|
| streamlink | {E['streamlink/streamlink']['puntos']} | {num(E['streamlink/streamlink']['con_huella'])} sumas · {num(E['streamlink/streamlink']['incidencias']['cerradas'])} cerradas | {num(E['streamlink/streamlink']['incidencias']['abiertas'])} abiertas |
| OKVideoMac | {E['yaolin-dev/OKVideoMac']['puntos']} | {num(E['yaolin-dev/OKVideoMac']['con_huella'])} sumas de {num(E['yaolin-dev/OKVideoMac']['adjuntos'])} · sin incidencias abiertas | {R['yaolin-dev/OKVideoMac']['dias_nace']} días de vida |
| aerial | {E['shapeshed/aerial']['puntos']} | {num(E['shapeshed/aerial']['con_huella'])} sumas · empujón de hoy | sin canal de seguridad |
| libretime | {E['libretime/libretime']['puntos']} | plataforma completa · {num(E['libretime/libretime']['commits_30d'])} cambios | {num(E['libretime/libretime']['incidencias']['abiertas'])} abiertas |
| OwnTV | {E['ahXN00/OwnTV']['puntos']} | {num(R['ahXN00/OwnTV']['entregas'])} entregas · {num(E['ahXN00/OwnTV']['commits_30d'])} cambios | {num(E['ahXN00/OwnTV']['adjuntos'])} adjuntos sin suma |

**La nota premia que se pueda comprobar, no que sea famoso.** **AntennaPod**, con {num(R['AntennaPod/AntennaPod']['stars'])} estrellas y {num(R['AntennaPod/AntennaPod']['dias_nace'])} días de historia, saca **{E['AntennaPod/AntennaPod']['puntos']}** porque no publica un solo adjunto: {num(R['AntennaPod/AntennaPod']['entregas'])} entregas sin archivo que comprobar. Y **OKVideoMac**, con {num(R['yaolin-dev/OKVideoMac']['stars'])} estrellas, saca **{E['yaolin-dev/OKVideoMac']['puntos']}** porque firma {num(E['yaolin-dev/OKVideoMac']['con_huella'])} de sus {num(E['yaolin-dev/OKVideoMac']['adjuntos'])} archivos.

───────────────────

*🧠 Cómo funciona el directo · la lista, la guía y el trozo*

Antes de las fichas, el mecanismo. Un reproductor de radio o de televisión por internet hace tres cosas, y **cada una puede romperse por su cuenta** —de ahí que el tema sea un mantenimiento perpetuo y no una instalación—.

**Primero: la lista.** Un enlace de radio no apunta a un archivo, apunta a un **manifiesto**. En radio suele ser una dirección de un flujo continuo —`.../stream`— o una lista `.pls`/`.m3u` con varias direcciones de respaldo. En televisión es un `.m3u` con cientos de líneas, y cada línea lleva el nombre del canal y su dirección. **Ese archivo es el 90 % del problema**: no lo genera nadie que tú conozcas, cambia sin avisar y suele apuntar a servidores privados. Un reproductor bueno no es el que tiene más canales: es el que **te dice cuál está muerto**.

**Segundo: el trozo.** La televisión moderna por internet no se emite como un archivo continuo sino por **trozos** —HLS, casi siempre—: el servidor publica un índice que se reescribe cada pocos segundos y una serie de fragmentos de dos a diez segundos. Eso permite adaptar la calidad a tu conexión y también explica los dos síntomas clásicos del directo: **el retraso de treinta segundos** respecto a la emisión real y **el salto atrás** cuando la conexión se corta y el reproductor vuelve a pedir el índice. No es un fallo de tu teléfono: es cómo está construido el formato.

**Tercero: la guía.** Para saber qué están dando ahora hace falta un **EPG**, un archivo XML —`XMLTV`— que trae la programación con horas. La lista de canales y la guía **son dos archivos distintos y se desincronizan siempre**: los canales de la lista se llaman «Canal 4 HD» y los de la guía «C4», y emparejarlos es un trabajo manual que casi nadie hace. Por eso las tres herramientas de esta pieza existen, y por eso una de ellas —**iptv-doctor**— es lo más útil del lote: quita los enlaces muertos y arregla los nombres de la guía.

**Y cuarto, el que no es técnico: el catálogo de radio.** La radio por internet tiene una infraestructura abierta y curiosa: **radio-browser.info**, un catálogo comunitario con decenas de miles de emisoras, votos y comprobaciones de estado. Casi todas las aplicaciones de bolsillo de esta pieza comen de ahí. Eso es lo que hace que un proyecto de {num(R['renyijiu/tune-roam']['dias_nace'])} días pueda arrancar con miles de emisoras sin negociar con nadie —y también lo que hace que, cuando ese catálogo tiene un dato malo, lo tengan malo veinte aplicaciones a la vez—.

**Lo que se cae, en una frase:** la radio por internet no se cae porque el software sea malo, se cae porque **la dirección caduca**. Por eso esta pieza mide mantenimiento y no catálogo.

───────────────────

*🔁 Qué reemplaza a qué · la tabla de la radio*

| Lo que usas hoy | Qué tiene de viejo | Qué lo cubre hoy |
|---|---|---|
| La app de radio que instalaste hace años | RadioDroid: **{R['segler-alex/RadioDroid']['dias_push']} días sin publicar** | **aerial**, **InternetRadio**, **omnibeat**, **tune-roam**: cuatro de 2026 |
| La aplicación del fabricante para ver la tele | Pide cuenta y manda tu lista a un servidor | **OwnTV**, **opentv**, **mytv-android**: lista propia, sin cuenta |
| Un reproductor de escritorio con la lista pegada a mano | thirty días de prueba y un aviso cada vez que cambia un canal | **Traydio**, **receiver**, **AetherTune**; y **streamlink** para lo que no tiene reproductor |
| La guía de programación que nunca coincide | Los nombres de la lista y los de la guía no son los mismos | **iptv-doctor**, **epg-tools**, **xmltv-splitter** |
| Un servicio de streaming para tu emisora | Se paga por oyente y se cae con el pico | **AzuraCast**, **LibreTime** e **Icecast**: en tu casa o en un servidor de cinco dólares |
| Bajar el audio de un directo | Se graba con el altavoz y suena a eso | **streamlink**: saca el flujo sin recodificar |

**Una advertencia sobre esa tabla, y es la de siempre en este tema.** Ninguna de estas piezas trae contenido. Un reproductor es un reproductor: lo que se ve depende de la lista que le pongas. Las listas gratuitas que circulan por ahí suelen ser **redifusiones sin permiso**, y de eso va la sección de responsabilidad, que en esta pieza no es un apéndice.

───────────────────
""")
open('/tmp/lab18/docs/talleres/pieza18/s1.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
