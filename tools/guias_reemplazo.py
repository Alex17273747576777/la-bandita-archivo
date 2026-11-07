#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_reemplazo.py · las guías escritas a mano del racimo «reemplazo-del-stack».

Igual que en el racimo de Shizuku: la ficha se genera, la guía se escribe. Este archivo
solo rellena el bloque GUIA:INICIO…GUIA:FIN de las fichas ya medidas.
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "reemplazo-del-stack"

GUIA = {}

GUIA["iptv-org/iptv"] = """
### Para qué sirve

Es el mayor índice de listas de canales IPTV públicas que existe: ★143.288, licencia Unlicense, actualizado
cada día. No es un reproductor ni una lista de canales de pago: es un repositorio de archivos de texto
donde cada cadena es una dirección de emisión que alguien encontró publicada.

### Cómo se usa

1. Necesitas un reproductor que lea listas M3U: en Android, un reproductor IPTV cualquiera de los que
   tienen ficha en este mismo racimo.
2. Del repositorio se toma el archivo de la región que te interese, no el «todo».
3. En el reproductor se importa la dirección del archivo —o el archivo descargado— y se refresca cuando
   haga falta: las direcciones caducan a diario.

### Lo que conviene saber antes

Dos advertencias serias. **La primera:** de cada cien direcciones, muchas no responden y otras emiten sin
permiso del titular; el repositorio lo dice en su propio aviso. Aquí no se enlaza ninguna lista ni se
señala ninguna cadena concreta: se describe el programa y se deja la decisión a quien lo use. **La
segunda:** una lista de canales no es una app; si conectas eso a un televisor y no funciona, el
repositorio no tiene la culpa, porque nunca prometió emisión, solo direcciones.
"""

GUIA["koreader/koreader"] = """
### Para qué sirve

Es el lector de libros electrónicos de referencia para aparatos con tinta electrónica —Kindle, Kobo,
PocketBook, Cervantes, reMarkable— y también corre en Android y en Linux. Lee PDF, EPUB, DJVU, FB2 y casi
cualquier formato de libro, y su fuerte es el PDF: reflow, recorte de márgenes y contraste que ningún
lector de fábrica hace bien.

### Cómo se instala en un lector

1. En Kindle o Kobo hay que **desbloquear el aparato** por el camino de cada fabricante (jailbreak); en
   Kobo, además, hay que copiar una carpeta y reiniciar.
2. En Android se instala la APK de la última entrega, que hoy es la `v2026.07.1` del 1 de agosto de 2026.
3. La primera vez hay que dejar que genere su base de datos: tarda unos minutos y en ese rato el lector
   va lento.

### Cuándo no vale la pena

Si lees EPUB en un teléfono y con la app de fábrica te apañas, KOReader es una molestia: su interfaz es
de otra época y su configuración tiene cien opciones. Se justifica en tinta electrónica, con PDF, o
cuando quieres diccionario, traducción y estadísticas de lectura en el mismo sitio.
"""

GUIA["koodo-reader/koodo-reader"] = """
### Para qué sirve

Gestor y lector de libros con sincronización y copia de seguridad, en Windows, macOS, Linux, Android, iOS
y navegador. Su gracia frente a un lector simple es que ordena una biblioteca grande: portadas,
metadatos, estanterías y progreso de lectura que viaja de un aparato a otro.

### Cómo se usa

1. Se instala desde la última entrega —`v2.4.6`, del 7 de octubre de 2026— o se abre la versión web.
2. Se importa la carpeta donde estén los libros; el programa extrae portada y datos de los EPUB y PDF.
3. La sincronización se activa en ajustes y guarda el progreso; el respaldo se puede hacer a un archivo
   local o a la nube que ya uses.

### Lo que conviene saber antes

Abre sin problema formatos sin DRM; los libros comprados con protección no los va a abrir, y conviene
saberlo antes de mover una biblioteca entera. Su licencia es AGPL-3.0, la más estricta de la familia: si
alguien la modifica y la publica como servicio, tiene que publicar el código.
"""

GUIA["kovidgoyal/calibre"] = """
### Para qué sirve

No es un lector: es **el taller** de los libros electrónicos. Convierte entre formatos, corrige
metadatos, edita el EPUB por dentro, genera catálogos, descarga portadas y noticias, y sincroniza con
casi cualquier lector que se le ponga delante. ★26.352 y una entrega nueva cada pocas semanas: `v9.17.0`
del 23 de octubre de 2026.

### Cómo se usa

1. Se instala el paquete de la web oficial o el de la distribución; en Linux está en los repositorios de
   todas.
2. Se añaden libros arrastrándolos o por la carpeta de «Añadir libros».
3. La conversión está en «Convertir libros»: se elige formato de salida y, en «Buscar y reemplazar»,
   los ajustes finos de cada aparato.
4. Para servir la biblioteca por wifi a un lector o a la app de un teléfono, está el «servidor de
   contenido» que trae dentro.

### Cuándo no vale la pena

Para leer un libro, no: Calibre es pesado, su interfaz es densa y arranca lento. Se instala cuando hay
que **arreglar** libros, no cuando hay que leerlos.
"""

GUIA["readest/readest"] = """
### Para qué sirve

Lector moderno, multiplataforma y reescritura de Foliate: interfaz nueva, sincronización entre aparatos,
notas, diccionario, traducción y modo de lectura doble para pantallas grandes. En Android, iOS, Windows,
macOS, Linux y navegador, con licencia AGPL-3.0.

### Cómo se usa

1. Se descarga de su web o de la última entrega (`v0.12.16`, del 13 de octubre de 2026).
2. Se importan los EPUB y PDF desde el propio lector; la biblioteca se queda local hasta que actives la
   sincronización.
3. Los atajos y el diseño de lectura están en ajustes, y el diccionario y la traducción funcionan
   offline una vez descargados los paquetes.

### Cuándo no vale la pena

Su versión sigue en `0.12`, y eso se traduce en detalles: algún formato raro se abre torcido y la
sincronización depende de su servicio. Para PDF técnico, KOReader hace más; para EPUB de novela, este
es más bonito y más rápido.
"""

GUIA["ImranR98/Obtainium"] = """
### Para qué sirve

Instala y actualiza aplicaciones de Android **directamente desde la página de entregas del proyecto**, sin
tienda de por medio. Es la pieza que hace usable todo lo demás: si una app publica sus APK en GitHub,
Obtainium la sigue, avisa cuando hay versión nueva y la instala.

### Cómo se usa

1. Se instala la APK de su última entrega (`v1.7.4`, del 1 de noviembre de 2026).
2. Se pulsa «Añadir aplicación» y se pega la dirección del repositorio; Obtainium detecta las entregas y
   elige el archivo que corresponde al teléfono.
3. En «Ajustes» se pone cada cuánto comprueba y si quiere instalar sola o solo avisar.

### Lo que conviene saber antes

Requiere permitir la instalación desde fuentes desconocidas, que es exactamente lo que hace falta para
cualquier app que no venga de una tienda. Y una advertencia de paciencia: si el proyecto publica
archivos con nombres irregulares, Obtainium puede elegir el equivocado; se revisa al añadirlo, no
después.
"""

GUIA["ahrm/sioyek"] = """
### Para qué sirve

Visor de PDF pensado para estudiar: salto entre referencias y figuras, historial de navegación por
teclado, marcas en los márgenes y vista de dos páginas. Es el lector de quien lee artículos y manuales,
no novelas.

### Cómo se usa

1. Instalador para Windows, macOS y Linux desde la página de entregas; en macOS también por `brew`.
2. Se abre el PDF y se maneja con teclado: `j` y `k` para moverse, `o` para saltar a una figura, `f` para
   buscar.
3. Las teclas se cambian en su archivo de configuración, y hay un modo de presentación para dar clase.

### Lo que conviene saber antes

Su última entrega etiquetada es `v2.0.0`, del 16 de diciembre de 2022, y el repositorio se movió en
noviembre de 2026: hay trabajo sin etiquetar, así que quien quiera lo último tiene que compilar. La
versión de 2022 sigue funcionando, y es lo que instala casi todo el mundo.
"""

GUIA["johnfactotum/foliate"] = """
### Para qué sirve

Lector de libros para el escritorio de Linux, con interfaz de GNOME: limpio, con tipografía cuidada,
anotaciones, diccionario y lectura en voz alta si el sistema tiene las voces instaladas. Fue el punto de
partida de Readest.

### Cómo se usa

1. En Debian y Ubuntu se instala el paquete `foliate`; si no está, hay Flatpak oficial.
2. Necesita las bibliotecas de GNOME que su README lista —`gjs`, `gtk4`, `libadwaita` y `webkitgtk-6.0`—;
   sin ellas no arranca, y ese es el fallo más común.
3. Para la voz hay que instalar `speech-dispatcher` y una voz como `espeak-ng`.

### Lo que conviene saber antes

El repositorio se movió por última vez en abril de 2026 y su última entrega es del 1 de abril de 2025:
va despacio, porque su autor está trabajando en Readest. No está muerto; está en segundo plano, y eso en
una ficha se escribe.
"""

GUIA["4gray/iptvnator"] = """
### Para qué sirve

Reproductor IPTV de escritorio y navegador: lee listas M3U, cuentas Xtream Codes y portales Stalker, con
favoritos, guía de programación y varias fuentes a la vez. Es la pieza que convierte una lista de
direcciones en algo que se puede ver cómodamente en un ordenador.

### Cómo se usa

1. Se descarga de su página de entregas (`v0.24.0`, del 24 de septiembre de 2026).
2. Al abrir, se añade una playlist por dirección o por archivo; el programa pide el tipo de fuente
   —M3U, Xtream o Stalker— porque cada una se lee distinto.
3. La guía de programación se activa por fuente y tarda en cargar la primera vez.

### Lo que conviene saber antes

El reproductor no trae contenido: lo pone quien lo usa. Aquí no se enlaza ninguna lista. Su licencia es
MIT, la más permisiva del racimo, y su repositorio está vivo.
"""

GUIA["grimmory-tools/grimmory"] = """
### Para qué sirve

Biblioteca autoalojada para libros, cómics y audiolibros, con estanterías, metadatos automáticos y
sincronización con lectores. Se instala en un servidor de casa o en un NAS y se usa desde el navegador o
desde la app de lectura que ya tengas.

### Cómo se usa

1. Hace falta Docker y Docker Compose, nada más.
2. Se levanta con su archivo de composición y se abre en el navegador del equipo de la red.
3. Se apunta a la carpeta donde están los libros; el programa indexa, busca portadas y ordena por autor
   y serie.

### Lo que conviene saber antes

Es un servicio con autenticación: si lo publicas en internet sin HTTPS ni contraseña decente, estás
regalando tu biblioteca. Y su licencia AGPL-3.0 obliga a publicar cambios si lo ofreces como servicio.
"""

GUIA["NuvioMedia/NuvioMobile"] = """
### Para qué sirve

Cliente de vídeo para Android y iOS del ecosistema Nuvio: reproduce lo que le den los complementos que
elijas, con biblioteca, historial y controles de reproducción. Es la puerta de entrada a esa familia, y
la que más se instala.

### Cómo se usa

1. En Android, la APK de su última entrega (`0.6.7-beta`, del 4 de noviembre de 2026) o desde su tienda.
2. En iOS, por AltStore o SideStore: se añade la dirección de su fuente y se instala desde ahí, porque no
   está en la App Store.
3. Al abrir, se añaden complementos por dirección; **el programa no trae ninguno**, y las fuentes que se
   añadan son responsabilidad de quien las añade.

### Lo que conviene saber antes

La versión lleva `beta` en el nombre: la aplicación está en obras y cambia de comportamiento entre
semanas. Aquí se describe el programa y no se enlaza ninguna fuente de contenido.
"""

GUIA["NuvioMedia/NuvioTV"] = """
### Para qué sirve

La versión para **Android TV** del cliente Nuvio, pensada para manejarse con el mando a distancia:
filas horizontales, foco grande y reanudación de lo que estabas viendo.

### Cómo se usa

1. La APK se instala en el televisor o en el aparato de TV —en Android TV se copia y se abre con un
   explorador—, o se compila desde el código con Gradle.
2. Se añaden los complementos por dirección igual que en el móvil, y se sincroniza la biblioteca si usas
   cuenta.
3. El mando hace casi todo; el teclado en pantalla aparece solo para escribir direcciones.

### Lo que conviene saber antes

Android TV tiene menos memoria que un teléfono y apps así se notan: si el aparato es de 2019 con 1 GB,
va a ir mal. Su última entrega es la 1.0.0, del 19 de septiembre de 2026, y el repositorio está vivo.
"""

GUIA["f-droid/fdroidclient"] = """
### Para qué sirve

El cliente oficial de F-Droid: la tienda de aplicaciones libres de Android. Firma las actualizaciones con
la clave del repositorio, avisa de versiones con cambios de permisos y no pide cuenta. Es el «otro
camino» completo frente a la tienda de Google.

### Cómo se usa

1. Se descarga el APK desde su web y se instala —es el único momento en que hace falta permitir fuentes
   desconocidas—.
2. Al abrir, se actualiza el índice; tarda un rato la primera vez.
3. Para apps que no están en el repositorio principal, se añaden repositorios de terceros con su
   dirección, sabiendo lo que eso significa: firmas y decisiones de otros.

### Lo que conviene saber antes

Dos cosas que su propia web explica y que casi nadie lee: la tienda prioriza software libre y su catálogo
es más pequeño que el de Google; y las apps que llegan por F-Droid se actualizan por F-Droid, así que
mezclar tiendas con la misma app instalada dos veces es una fuente de líos.
"""

GUIA["Viren070/AIOStreams"] = """
### Para qué sirve

Junta muchos complementos de Stremio, servicios de nube y fuentes en **una sola lista**, filtrada y
ordenada por sus propias reglas. En vez de instalar diez complementos que devuelven resultados
desordenados, se configura este una vez y se instala como si fuera el único.

### Cómo se usa

1. Se despliega la instancia —propia o la que su proyecto ofrece— y se abre el configurador.
2. Se conectan las cuentas y servicios que se quieran usar, y se eligen las plantillas de filtros.
3. Se instala el complemento resultante en Stremio o en cualquier app compatible, y desde ese momento
   las listas se actualizan solas.

### Lo que conviene saber antes

Es un **agregador**: no tiene contenido propio y depende por completo de lo que le conectes. Con una
instancia pública, tus claves pasan por un servidor ajeno; con la tuya, no. Su licencia es AGPL-3.0 y
su repositorio se mueve a diario.
"""

GUIA["edrlab/thorium-reader"] = """
### Para qué sirve

Lector de EPUB de escritorio con estándares por delante: lo mantiene EDRLab, la organización que empuja
la lectura digital accesible, y su fuerte son los EPUB con diseño complejo, los audiolibros y las
funciones de accesibilidad —lectura en voz alta, navegación por teclado, contraste—.

### Cómo se usa

1. Instalador para Windows, macOS y Linux desde su página de entregas (`v3.5.1`, del 2 de septiembre de
   2026).
2. Se importan libros desde una carpeta o desde una fuente OPDS; la biblioteca se ordena por estanterías.
3. Para leer en voz alta hay que activar la síntesis del sistema y elegir voz.

### Cuándo no vale la pena

Su interfaz es sobria hasta lo austero y no sincroniza entre aparatos. Si lo que quieres es leer novelas
en el móvil, Readest o Koodo son más cómodos; Thorium se justifica con libros técnicos, con
accesibilidad o con EPUB que otros lectores rompen.
"""

GUIA["TrackerControl/tracker-control-android"] = """
### Para qué sirve

Mide y corta los rastreadores que llevan dentro las aplicaciones de Android. Usa la red privada local
—una VPN que corre en el propio teléfono— para ver a qué servidores llama cada app, y deja bloquear por
aplicación o por rastreador.

### Cómo se usa

1. Se instala la APK de su última entrega (`2026110101`, del 1 de noviembre de 2026).
2. Se concede el permiso de VPN local cuando lo pida; no hay que contratar nada.
3. En la lista de aplicaciones se ve cuántos rastreadores tiene cada una, quién los firma y qué dominios
   toca; se bloquea con un interruptor.
4. Con root se puede además bloquear a nivel de sistema, pero **no es necesario**.

### Lo que conviene saber antes

Solo puede vigilar una VPN a la vez: si usas otra, la sustituye. Y no es un antivirus: ve conexiones, no
intenciones.
"""

GUIA["stupside/castor"] = """
### Para qué sirve

Manda a la televisión un vídeo que está incrustado en una página web que no ofrece Chromecast. Encuentra
el vídeo en la página que le indiques, lo transcodifica al vuelo y lo emite a un Chromecast o a un
televisor compatible.

### Cómo se usa

1. Se instala con `brew install --cask stupside/tap/castor` en macOS, con `npm install -g @castor-dev/cli`
   en cualquier sistema con Node 20 o superior, o desde su última entrega (`v2.5.0`, del 27 de octubre de
   2026).
2. Se le pasa la dirección de la página y el destino; opcionalmente, subtítulos para incrustar.
3. La transcodificación se hace en el equipo donde corre: con vídeo pesado, el ventilador se entera.

### Lo que conviene saber antes

Solo sirve para contenido que la propia página te deja ver: no salta muros de pago ni protecciones. Y
hace falta estar en la misma red que el televisor.
"""

GUIA["Accrescent/Accrescent"] = """
### Para qué sirve

Tienda de aplicaciones de Android que apuesta por la seguridad: verificación de paquetes, sin cuentas, sin
telemetría y con un método de firma que impide que un tercero publique en nombre de un desarrollador.
Es pequeña a propósito: su catálogo es corto y curado.

### Cómo se usa

1. Se instala su APK desde la web o desde su última entrega (`0.29.1`, del 4 de noviembre de 2026).
2. Al abrir, se añade su repositorio y se navega por el catálogo; no hay que registrarse.
3. Las actualizaciones llegan por la propia tienda, como en cualquier otra.

### Cuándo no vale la pena

Si esperas encontrar ahí todo lo que usas, no: su catálogo es corto y muchas apps conocidas no están. Su
valor es el contrario del de una tienda grande: menos apps, más comprobadas.
"""

GUIA["doctorhetfield-cmd/simpleui.koplugin"] = """
### Para qué sirve

Reemplaza la interfaz de KOReader por una de pantalla de inicio con barra inferior, barra superior y
modo escritorio. Es un complemento —termina en `.koplugin`— y su público es quien ya usa KOReader y
quiere que se parezca a un lector moderno.

### Cómo se instala

1. Hace falta tener KOReader funcionando y una versión reciente del lector.
2. Se descarga el archivo `.koplugin` de su última entrega (`3.0.2`, del 30 de octubre de 2026).
3. Se copia dentro de la carpeta `koreader/plugins/` del aparato y se reinicia KOReader.
4. Se activa desde el menú de complementos del propio lector.

### Cuándo no vale la pena

En un lector con pantalla pequeña, la barra inferior se come la página. Y si KOReader te parece feo pero
funciona, este complemento no arregla lo que molesta: solo lo tapa.
"""

GUIA["NuvioMedia/NuvioDesktop"] = """
### Para qué sirve

El cliente Nuvio para escritorio, en Windows, macOS y Linux. Misma biblioteca y mismos complementos que
la versión móvil, con ventana grande y atajos de teclado.

### Cómo se usa

1. Se descarga el instalador de la última entrega (`0.1.34-alpha`, del 4 de noviembre de 2026):
   `.msi` en Windows, paquete de sistema en macOS y Linux.
2. En Arch hay un empaquetado no oficial con ficha propia en este racimo.
3. Al abrir, se añaden complementos por dirección, igual que en el móvil.

### Lo que conviene saber antes

Su propio repositorio lo dice en la primera línea: **«Alpha Software - Testers Only»**. Se cae, cambia y
a veces no arranca; no es para el salón de casa. Las versiones `alpha` del proyecto son la norma, no la
excepción.
"""

GUIA["samyak2403/RepoStore"] = """
### Para qué sirve

Explorador de aplicaciones publicadas en GitHub: busca repositorios que publiquen APK en sus entregas,
muestra qué versión hay y las instala. Es como Obtainium pero con catálogo, en vez de tener que añadir
cada repositorio a mano.

### Cómo se usa

1. Se instala la APK de su última entrega (`v1.0.22`, del 29 de octubre de 2026).
2. En la pantalla principal se busca por nombre; el programa solo muestra repositorios que de verdad
   tengan APK descargables, según su propia descripción.
3. Al elegir una app se ve la versión instalada y la disponible, y se actualiza desde ahí.

### Lo que conviene saber antes

Encontrar una app en un catálogo no la hace buena: el programa muestra lo que hay en GitHub, sin filtro de
calidad. Y su lista de APK la decide un programa, no una persona: conviene mirar la fecha del último
empujón antes de instalar.
"""

GUIA["booklore-app/booklore"] = """
### Para qué sirve

Biblioteca digital autoalojada y multiusuario: estanterías inteligentes, metadatos automáticos,
sincronización con Kobo y KOReader, importación por carpeta («BookDrop»), OPDS y una interfaz web para
toda la casa.

### Cómo se usa

1. Hace falta Docker y Docker Compose.
2. Se levanta el servicio y se abre en el navegador; el primer arranque crea la cuenta de administración.
3. Se apunta a la carpeta de libros y se deja que indexe; las estanterías se pueden hacer por reglas.
4. Para el Kobo o el KOReader se usa la sincronización que trae, que es su función más apreciada.

### Lo que conviene saber antes

Es un servicio con cuentas y datos: fuera de casa, con HTTPS y contraseñas decentes. Su licencia es
AGPL-3.0.
"""

GUIA["cenodude/CrossWatch"] = """
### Para qué sirve

Sincroniza el historial de lo que ves entre servidores de medios y servicios de seguimiento: lo que
marcas visto en Jellyfin aparece en Plex, y lo que puntúas en un rastreador llega al otro. Su terreno es
la casa con varias fuentes de reproducción.

### Cómo se usa

1. Se despliega en un servidor con Docker.
2. Se conectan los servicios por su API —cada uno con su token— y se eligen qué datos se sincronizan.
3. La primera sincronización tarda: está emparejando bibliotecas enteras.

### Lo que conviene saber antes

Su propia documentación avisa de que **no todas las integraciones soportan todo**: unas sincronizan
listas, otras historial, otras solo actividad. Antes de fiarse, se prueba con una serie y se mira qué
llegó al otro lado.
"""

GUIA["NuvioMedia/NuvioTVSmart"] = """
### Para qué sirve

La versión de Nuvio para televisores **webOS (LG) y Tizen (Samsung)**, que no son Android y por eso
necesitan un empaquetado distinto. Incluye además un instalador para Windows, macOS y Linux que sirve
para cargar la app en el televisor.

### Cómo se usa

1. Se descarga el instalador de escritorio o el paquete `wgt` para Tizen de la última entrega
   (`1.3.6`, del 5 de noviembre de 2026).
2. En LG se instala en modo desarrollador; en Samsung, con el instalador y el televisor en el mismo modo.
3. Los complementos se añaden después, igual que en las otras versiones.

### Lo que conviene saber antes

El modo desarrollador de estos televisores **caduca** y hay que renovarlo cada cierto tiempo; eso no lo
arregla la app. Y cada televisor es un mundo: lo que funciona en un LG de 2023 puede no arrancar en uno de
2020.
"""

GUIA["Exodus-Privacy/exodus"] = """
### Para qué sirve

Es el motor del análisis de rastreadores de Exodus Privacy: una plataforma para auditar qué bibliotecas de
seguimiento lleva dentro una aplicación de Android, con un catálogo público de informes por app. No es
una app para el usuario final: es el servicio que produce los informes que consultan otras.

### Cómo se usa

1. Se despliega con Docker o a mano, siguiendo su documentación de entorno de desarrollo.
2. Se le dan APK y devuelve el análisis: rastreadores detectados, firmas y permisos.
3. Para consultar resultados ya hechos, se usa su sitio público; para generarlos tú, esto.

### Cuándo no vale la pena

Si solo quieres saber qué lleva una app, el informe público existe y no hay que montar nada. Esto se
instala cuando quieres análisis propios, en lote, o en una red cerrada.
"""

GUIA["ahXN00/OwnTV"] = """
### Para qué sirve

Reproductor IPTV nativo para **Android TV**, escrito en Kotlin con Compose y reproductores ExoPlayer y
mpv: admite Xtream, M3U y portales Stalker, con guía de programación, catch-up, perfiles y descargas.

### Cómo se usa

1. Se instala la APK de su última entrega (`v5.2.1`, del 4 de noviembre de 2026) en el televisor o en la
   caja de Android TV.
2. Se añade el perfil con los datos de la fuente; cada perfil guarda su propio orden de filas y sus
   favoritos.
3. La guía se carga por perfil y el catch-up solo aparece si la fuente lo soporta.

### Lo que conviene saber antes

El programa no trae ni enlaza ninguna lista: lo que se ve es lo que se configure. Su repositorio está vivo
y su licencia es GPL-3.0.
"""

GUIA["ellite/scrob"] = """
### Para qué sirve

Rastreador de series y películas autoalojado: toma las bibliotecas de Jellyfin, Plex o Emby y lleva el
historial, las notas y las listas personales, en web y como aplicación instalable (PWA) en cualquier
aparato.

### Cómo se usa

1. Se despliega con Docker y se abre en el navegador.
2. Se conectan los servidores de medios con su dirección y su token.
3. Se instala como PWA desde el propio navegador para tener icono y pantalla completa.

### Lo que conviene saber antes

Su punto fuerte y su límite son el mismo: depende de los servidores que conectes, así que si no tienes
ninguno, no hay nada que rastrear. Alternativa con más funciones: Trakt; con más privacidad: esto.
"""

GUIA["frederikemmer/MediaLyze"] = """
### Para qué sirve

Analiza bibliotecas de medios grandes y dice qué está mal: archivos duplicados, faltantes de una serie,
metadatos inconsistentes, tamaños desproporcionados. Tiene versión de escritorio y versión web.

### Cómo se usa

1. Se descarga el programa de escritorio de su última entrega (`v0.20.0`, del 2 de noviembre de 2026), o
   se despliega la versión web.
2. Se apunta a la carpeta o a la biblioteca del servidor de medios.
3. El análisis se puede lanzar entero o por secciones, y el resultado se exporta.

### Cuándo no vale la pena

Con doscientas películas bien ordenadas, un listado a mano basta. MediaLyze se justifica a partir de
miles de archivos, que es cuando los duplicados se vuelven invisibles.
"""

GUIA["Chimahon/chimahon"] = """
### Para qué sirve

Fork de Mihon centrado en el estudio de idiomas: diccionario nativo tipo Yomitan, soporte de manga
digitalizado con Mokuro, lector de novelas en EPUB y creación de tarjetas de Anki sin salir de la
pantalla. Es la herramienta de quien lee para aprender, no solo para entretenerse.

### Cómo se usa

1. Se instala la APK de su última entrega (`v2.4.8`, del 3 de noviembre de 2026).
2. Se añaden las extensiones de Mihon como en cualquier Mihon —las fuentes no cambian—.
3. Se configura el diccionario y, si se usa, la conexión con Anki o AnkiDroid.
4. Para Mokuro hay que haber procesado antes el manga con esa herramienta.

### Lo que conviene saber antes

Un fork más significa una app más que se puede quedar atrás: si Mihon cambia su formato de copia de
seguridad, este fork tarda en seguirlo. Y hereda del original todo lo que se dice en su ficha.
"""

GUIA["s4pp1/stremhu-source"] = """
### Para qué sirve

Servidor autoalojado que sirve como fuente a Stremio, Nuvio o Kodi y que, según su descripción, trabaja
con **trackers privados húngaros**. Es una pieza muy concreta de un ecosistema muy concreto.

### Lo que conviene saber antes

Esta ficha se queda corta a propósito: el recurso depende de acceso a trackers privados —cuentas que se
piden por invitación— y su función es enlazar torrentes. Aquí no se enlaza ninguna fuente de contenido ni
se explica cómo obtener acceso, y esa no es una decisión técnica: es la misma raya que separa este
catálogo de una lista de enlaces.

### Cuándo no vale la pena

Para casi todo el mundo. Si no tienes cuenta en esos trackers, el programa no tiene nada que servir, y
montarlo para descubrirlo cuesta una tarde.
"""

GUIA["coveninja/cove"] = """
### Para qué sirve

Aplicación de vídeo para escritorio, Android y Android TV que descubre, rastrea y reproduce películas y
series con metadatos de TMDB y, según su descripción, fuentes de Stremio. Su propia instalación dice algo
importante: **no incluye fuentes de terceros**.

### Cómo se usa

1. Se descarga la versión de su última entrega (`v1.6.0`, del 30 de octubre de 2026).
2. Se conectan las fuentes que se quieran usar; sin ellas, el programa es un catálogo bonito de fichas.
3. El historial y las listas se guardan en local.

### Lo que conviene saber antes

Es de los pocos que lo dice por escrito en su README: la instalación no trae fuentes. Eso lo deja del lado
de las herramientas y no del de los enlaces, que es donde este catálogo puede hablar de él.
"""

GUIA["debpalash/Opal"] = """
### Para qué sirve

Reproductor y explorador de medios para escritorio —macOS, Linux y Windows— que junta en una ventana la
biblioteca local, las fuentes de Stremio o Kodi y la reproducción con subtítulos y pistas de audio.

### Cómo se usa

1. Se descarga de su última entrega (`v0.9.3`, del 4 de noviembre de 2026).
2. Se abre un archivo local o se añade una fuente; el reproductor guarda la sesión para retomarla.
3. Los subtítulos se cargan por archivo o por búsqueda, según la fuente.

### Lo que conviene saber antes

Está en `0.9`, sin llegar a 1.0, y se nota en los detalles. Su licencia GPL-3.0 y su repositorio vivo son
lo mejor que tiene; la estabilidad, lo que le falta.
"""

GUIA["Eful97/Pictorium"] = """
### Para qué sirve

Genera carteles alternativos para películas y series a partir de fotogramas: se le dice qué título y
devuelve una imagen con estilo de póster, que luego se usa en Stremio o en un centro de medios para que
la biblioteca no parezca toda igual.

### Cómo se usa

1. Se usa su instancia pública para probar, sin instalar nada.
2. Para tenerlo en casa, se despliega y se configura el PIN de administrador en el asistente, paso 3.
3. En Stremio o en el centro de medios se añade como fuente de metadatos de carteles.

### Lo que conviene saber antes

Depende de servicios externos para las imágenes y el reconocimiento de títulos: si esos servicios cambian
o cierran, el programa se queda sin materia prima. Es un adorno, y conviene tratarlo como tal.
"""

GUIA["alpinezx/easy-aiostreams"] = """
### Para qué sirve

Instalador de un comando para levantar AIOStreams en un servidor propio o en un ordenador de casa, sin
tener que escribir el archivo de composición ni recordar los pasos.

### Cómo se usa

1. En un VPS o en un equipo con Docker, se ejecuta el instalador de su última entrega (`v1.5.2`, del 4 de
   noviembre de 2026).
2. El asistente pide dominio o IP, puerto y poco más, y deja el servicio levantado.
3. Después se entra en el configurador de AIOStreams y se sigue por ahí.

### Cuándo no vale la pena

Si no vas a usar AIOStreams, esto no sirve para nada: es su instalador. Y si ya sabes usar Docker
Compose, sus veinte líneas hacen lo mismo con menos capas de confianza.
"""

GUIA["JJDizz1L/NuvioLinux-unofficial"] = """
### Para qué sirve

Empaquetado **no oficial** de Nuvio Desktop para Arch Linux: paquete firmado, publicado también en AUR,
construido desde el código original sin modificarlo.

### Lo que conviene saber antes

Tres cosas que su propio nombre admite. **No es oficial**: si algo falla, el proyecto de Nuvio no te debe
soporte. **Depende de un proyecto en fase alpha**, así que el paquete envejece rápido. Y **hay que
comprobar la firma** antes de instalar: el propio proyecto publica la clave con la que firma, y ese paso
no es opcional cuando se instala un binario ajeno.

### Cuándo no vale la pena

Si usas otra distribución, o si prefieres compilar el original. Se justifica en Arch, donde no hay paquete
oficial.
"""

GUIA["mochi-plugins/repository"] = """
### Para qué sirve

Es —o era— el repositorio de artefactos de complementos para la aplicación Usagi y sus derivados. Su
descripción dice «archivo», y esa palabra es exacta.

### Lo que se midió

Hoy tiene **dos archivos**: una licencia y un README. Cero complementos, cero catálogo, una sola rama. La
medición de esta ficha lo dejó así de claro, y la pieza 19 lo contó con nombre y motivo. Si alguien llega
aquí buscando «los complementos de Usagi», esto no es.

### Qué hacer en su lugar

La propia organización de Usagi publica la plantilla y la biblioteca para escribir complementos; los
repositorios de autores concretos son los que tienen contenido. Un repositorio vacío con ★49 se repite en
las listas por copia, no por comprobación: esta ficha existe para cortar esa cadena.
"""

GUIA["SkipDB-TV/skipdb"] = """
### Para qué sirve

Base de datos abierta y colaborativa de marcas de tiempo para saltar intros, resúmenes y avances de
series y películas. Las apps compatibles la consultan y ponen un botón de «saltar» donde toca.

### Cómo se usa

1. No se instala: se consume. Las apps compatibles traen una dirección que apunta aquí.
2. Para contribuir hay que crear cuenta en su instancia, o levantar una propia y editar desde ahí.
3. Las marcas se revisan por la comunidad antes de publicarse.

### Lo que conviene saber antes

Su valor depende de cuánta gente contribuya: en series populares acierta, en el resto hay huecos. Y no es
una app: si buscas el botón de saltar, lo tiene que traer tu reproductor.
"""

GUIA["MegaNexusMediaPlayer/MegaNexus"] = """
### Para qué sirve

Convierte Kodi en otra cosa: reemplaza inicio, menús, fichas, reproductor y salvapantallas por una
interfaz pensada para el mando a distancia, con complementos de Stremio y Nuvio, nube, subtítulos por IA
y fiesta de visionado.

### Cómo se usa

1. Se instala su repositorio en Kodi desde un zip: Ajustes → Complementos → Instalar desde archivo zip.
2. Se instala después el complemento MegaNexus y se reinicia Kodi.
3. La primera vez pide configurar las fuentes; sin ellas, la interfaz está pero no hay nada que ver.

### Lo que conviene saber antes

Es un envoltorio completo: quien no conozca Kodi se va a perder y quien lo conozca va a echar de menos sus
menús. Su licencia aparece como NOASSERTION porque usa una propia; quien reutilice código, la lee.
"""

GUIA["atharvkharbade/anisync-addon"] = """
### Para qué sirve

Complemento de metadatos para anime en Stremio y Nuvio: seguimiento, fichas ricas, recomendaciones y
calendario de emisión. No emite nada; ordena y describe.

### Cómo se usa

1. Se copia la dirección de su manifiesto.
2. En Stremio o en Nuvio se añade como complemento por esa dirección.
3. Para el seguimiento hay que conectar la cuenta del rastreador; sin cuenta funciona igual, con menos
   funciones, según su propio README.

### Cuándo no vale la pena

Si no ves anime, es un complemento que añade ruido a la pantalla de inicio. Si ves mucho, es de los pocos
que entiende temporadas y películas de una franquicia como lo que son.
"""

GUIA["ohadhaviv92/streamgram"] = """
### Para qué sirve

Complemento autoalojado que sirve a Stremio y a apps compatibles el contenido de **tu propio canal de
Telegram**. Se despliega en un servidor y se instala con una dirección privada por usuario.

### Cómo se usa

1. Se levanta con Docker o en su plataforma de despliegue.
2. Se configuran las credenciales del canal en las variables de entorno.
3. Se instala con la dirección `/:token/manifest.json` que genera para tu cuenta.

### Lo que conviene saber antes

Ese token privado **es la llave**: quien lo tenga ve tu catálogo. No se comparte, no se pega en un chat y
se cambia si se filtra. Y no publica entregas etiquetadas: para actualizarlo hay que seguir su repositorio.
"""

GUIA["HatriGt/flix-launcher"] = """
### Para qué sirve

Lanzador para Android TV sin anuncios ni apps promocionadas: al encender, muestra lo que estabas viendo,
tus películas y el acceso directo a las apps de streaming, en vez de la pantalla llena de recomendaciones
de Google.

### Cómo se usa

1. Se descarga el APK de su última entrega (`v1.0.14`, del 3 de noviembre de 2026).
2. Se instala y, en el televisor, se elige como lanzador predeterminado.
3. Se ordenan las apps y se eligen qué filas se muestran.

### Cuándo no vale la pena

Si el televisor es rápido y no te molesta la pantalla de Google. Y si el aparato es lento, ningún lanzador
lo hace rápido: cambia la sensación, no el hardware.
"""

GUIA["joaotolovi/m3u-mux-addon-stremio"] = """
### Para qué sirve

Convierte una lista M3U en un complemento de Stremio. En lugar de abrir un reproductor aparte para la
televisión por internet, la lista aparece como un catálogo más dentro de la app que ya usas.

### Cómo se usa

1. Se abre su configurador basado en navegador —sin exponer la lista en la dirección de instalación, que
   es su ventaja—.
2. Se pega la lista, se deja indexar y se genera la dirección del complemento.
3. Se instala esa dirección en Stremio o en una app compatible.

### Lo que conviene saber antes

Indexar una lista grande tarda, y el resultado hereda todos sus problemas: direcciones muertas incluidas.
Y no tiene entregas etiquetadas: se actualiza siguiendo el repositorio.
"""

GUIA["kuiti/manga-source-index"] = """
### Para qué sirve

Índice cruzado de fuentes de manga de siete lectores distintos —Mihon, Aidoku, Kotatsu, Legado, Venera,
Cimoc y otros—, con la idea de que una fuente escrita para uno se pueda aprovechar en otro. Trae una guía
de inicio de tres pasos pensada para quien no programa.

### Cómo se usa

1. Se lee su `START-HERE.md`, que existe justo para no tener que clonar nada.
2. Se pega una dirección en el lector correspondiente y se añaden las fuentes de una en una.
3. Las que ya están instaladas aparecen marcadas.

### Lo que conviene saber antes

Su propio texto admite que **solo una parte está lista y el resto hay que escribirlo**: es un índice en
construcción, con ★6 y tres meses de vida. Y es de los proyectos que mezclan fuentes de varios
ecosistemas, así que la calidad de cada entrada depende de su autor original, no de este.
"""

GUIA["janlery/MANGA-TENSEI"] = """
### Para qué sirve

Convierte archivos de copia de seguridad de lectores de manga entre sí: Mihon y Tachiyomi, Tachimanga
(`.tmb`) y Aidoku (`.aib`). Todo se hace **en el navegador**, sin subir los archivos a ningún servidor.

### Cómo se usa

1. Se abre la página del proyecto.
2. Se arrastra el archivo de copia de seguridad y se elige el formato de destino.
3. Se descarga el resultado y se restaura en el lector nuevo.

### Lo que conviene saber antes

Es la herramienta exacta para el momento de cambiar de app sin perder la biblioteca, y ese momento llega:
los lectores se archivan y la gente migra. Tiene ★3 y su interfaz está en chino, con traducción en la
descripción; el código es corto y se puede leer.
"""

GUIA["arranoust/yomu"] = """
### Para qué sirve

Repositorio de complementos en indonesio para Usagi y otros derivados de Kotatsu. Cubre fuentes locales
que no están en ningún catálogo grande.

### Cómo se usa

1. Se abre Usagi y se va a la sección de complementos.
2. Se importa desde GitHub, que es su método recomendado, o desde un archivo descargado.
3. Los complementos aparecen como una lista más dentro de la app.

### Lo que conviene saber antes

★2 y última actividad en agosto de 2026: es un proyecto personal de un solo autor, y eso hay que saberlo
antes de depender de él. Su valor es la cobertura de un idioma que los catálogos grandes no tocan.
"""

GUIA["ito-community/sources"] = """
### Para qué sirve

Fuentes de la comunidad para **Ito**, un lector que se maneja por paquetes de fuente firmados en lugar de
extensiones. Su README avisa de un detalle de versión: algunas fuentes exigen Ito 1.4.0 o superior.

### Cómo se usa

1. Se instalan con la herramienta de paquetes de Ito: `cargo install --force --git …ito-pkg`.
2. Se añaden al lector los paquetes que se quieran.
3. Si un sitio cambia su cliente web, la fuente se actualiza y hay que volver a instalarla.

### Cuándo no vale la pena

Si no usas Ito, esto no sirve para nada: no es compatible con Mihon ni con ningún otro lector. Es un
catálogo de nicho dentro de un lector de nicho, y así se dice.
"""

GUIA["lipexama/lipex-reader"] = """
### Para qué sirve

Lector de novelas ligeras para iOS: biblioteca con categorías, búsqueda, progreso, temas y tipografías
personalizables, y lectura en voz alta.

### Cómo se usa

1. Se instala desde la App Store, que es el único camino en iOS.
2. Se importan los archivos o se añaden fuentes; el lector recuerda el punto exacto de cada libro.
3. El modo de lectura y la voz se configuran por libro o de forma global.

### Lo que conviene saber antes

Tiene ★1, una sola entrega (`v1.21`, del 24 de julio de 2026) y **no declara licencia**: tres señales que
en este catálogo significan «proyecto de una persona, sin garantías». En iOS, además, el código no se
puede auditar desde el teléfono, así que la confianza depende del desarrollador.
"""

GUIA["Pulsariums/pulsar-trmangahub"] = """
### Para qué sirve

Repositorio de fuentes de manga en turco, con formato doble: APK para Mihon y Tachiyomi, y JAR para
Kototoro. Su público es quien lee en turco, que no está bien cubierto en los catálogos generales.

### Cómo se usa

1. En Mihon se añade la dirección del índice del repositorio.
2. En Kototoro se usa el archivo JAR correspondiente.
3. Las fuentes aparecen como una lista más; se eligen las que tengan el contenido que buscas.

### Lo que conviene saber antes

★0, sin licencia declarada y sin entregas etiquetadas: es un repositorio nuevo que puede desaparecer sin
avisar. Aquí está porque el hueco idiomático es real, no porque tenga historial.
"""

GUIA["Stiven-Gjekaj/Moekoma"] = """
### Para qué sirve

Lector tranquilo de manga, cómics, novelas ligeras y web novels para Android y tinta electrónica, que
acepta fuentes de Mihon, Kotatsu, OPDS y LNReader en la misma aplicación.

### Cómo se usa

1. Se instala la APK de su última entrega (`v2.1.0`, del 24 de octubre de 2026).
2. Al abrir, instala sus fuentes en inglés; las demás se añaden por dirección.
3. La búsqueda pregunta a todas las fuentes a la vez, que es su rasgo más útil.

### Lo que conviene saber antes

★0 y una entrega reciente: es un proyecto joven con una idea buena —mezclar ecosistemas— y poca gente
detrás. Para tinta electrónica es de los pocos que lo intenta, y eso vale la pena decirlo.
"""

GUIA["TaisenDev/aidoku-bridge-builder"] = """
### Para qué sirve

Convierte el catálogo de extensiones de un servidor Suwayomi en un repositorio de fuentes para **Aidoku**
(iOS), con un archivo `.aix` por sitio y actualización cada hora. Evita tener que compilar extensiones a
mano para leer en un iPhone.

### Cómo se usa

1. Se despliega junto a un servidor Suwayomi.
2. Se elige qué extensiones compilar; el programa las descubre del catálogo del servidor.
3. Se añade la dirección del repositorio resultante en Aidoku, y este se actualiza solo.

### Lo que conviene saber antes

Añade una capa más entre el sitio y tu lector: si Suwayomi falla, el puente falla. Y compilar cada hora
consume recursos del servidor donde corra.
"""

GUIA["akachiina/wotoha"] = """
### Para qué sirve

Descargador de manga por línea de órdenes que usa las extensiones WebAssembly de Aidoku: más de 140
fuentes y salida en cinco formatos —raw, EPUB, CBZ, CB7 y PDF— con metadatos `ComicInfo.xml`.

### Cómo se usa

1. Se instala con Python; no necesita Java, que es su ventaja frente a otros descargadores.
2. Se busca el título, se elige la fuente y se descarga la serie o los capítulos.
3. El formato se elige al final, y se puede reconvertir una carpeta ya descargada sin volver a bajar.

### Cuándo no vale la pena

Si lo que quieres es leer al vuelo, un lector es mejor. Esto es para archivar, y para quien se maneja en
una terminal.
"""

GUIA["lnreader/cli"] = """
### Para qué sirve

Lleva los complementos de LNReader a la terminal: busca en cientos de fuentes de novelas web y descarga
el resultado como EPUB 3 limpio para Apple Books, Calibre o KOReader. Incluye además un servidor MCP para
que un asistente pueda usarlo.

### Cómo se usa

1. Sin instalar nada: `npx @lnreader/cli --help`. O con `npm i -g @lnreader/cli`.
2. Se busca por título, se elige la fuente y se descarga; el EPUB lleva portada, índice y capítulos.
3. Para automatizar, el modo MCP se levanta como servidor y se conecta desde el cliente que se use.

### Lo que conviene saber antes

Las fuentes son las de LNReader: funcionan mientras funcionen, y dependen de que alguien mantenga el
complemento del sitio. ★0 y sin entregas etiquetadas: es nuevo, y se puede leer entero porque es corto.
"""


def main() -> int:
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    escritas = 0
    for repo, texto in GUIA.items():
        f = medido.get(repo)
        if not f or f.get("racimo") != RACIMO:
            print("  ! sin medir en el racimo:", repo)
            continue
        p = CATALOGO / repo.replace("/", "--").lower() / "FICHA.md"
        if not p.exists():
            print("  ! sin ficha:", repo)
            continue
        t = p.read_text(encoding="utf-8")
        if INICIO not in t or FIN not in t:
            print("  ! sin marcadores:", repo)
            continue
        nuevo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN),
                       INICIO + "\n" + texto.strip() + "\n" + FIN, t, flags=re.S)
        if nuevo != t:
            p.write_text(nuevo, encoding="utf-8")
            escritas += 1
    print(f"guías escritas: {escritas} de {len(GUIA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
