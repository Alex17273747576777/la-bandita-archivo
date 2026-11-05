#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_descargas.py · las guías escritas a mano del racimo «descargas» (30 recursos).

La ficha se genera; la guía se escribe. Este archivo solo rellena el bloque
GUIA:INICIO…GUIA:FIN de las fichas ya medidas.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "descargas"

GUIA = {}

GUIA["AnInsomniacy/rayburst"] = """
### Para qué sirve

Gestor de descargas de escritorio con motor de línea de órdenes por debajo y ventana propia. Es lo que
antes se llamaba **Motrix Next**, con nombre nuevo y a partir de aquí con vida propia: descarga por HTTP
y por enlaces de una sola vía, reparte el archivo en varios trozos a la vez y permite pausar y reanudar
sin perder lo bajado.

### Cómo se instala

1. Desde la última entrega —`v4.1.1`, del 25 de octubre de 2026— hay paquete para Windows, macOS y Linux.
2. Si tenías la versión anterior, **desinstálala primero**: lo pide el propio proyecto. Los ajustes, las
   tareas y el historial **no se importan**, y los archivos descargados se quedan donde estaban.
3. La primera vez se elige la carpeta de destino y, si vas a usar el navegador, se instala la extensión que
   empuja los enlaces a la aplicación.

### Lo que conviene saber antes

Es un proyecto **de marzo de 2026**. Tiene 11.383 estrellas y entrega reciente, pero su historial es de
meses, no de años: si buscas algo que lleve una década funcionando igual, no es éste. La licencia es MIT,
así que puedes mirarlo por dentro con tranquilidad.

### Cuándo no vale la pena

En un teléfono no existe: es escritorio. Y si lo único que descargas son archivos aislados de una web que
nunca falla, la descarga del propio navegador ya hace eso y no hay nada que configurar.
"""

GUIA["BareBrowser/bare-browser"] = """
### Para qué sirve

Un navegador Chromium para Android **sin la parte de Google**: sin inicio de sesión, sin telemetría, sin
los añadidos de inteligencia artificial que Chromium trae hoy. A cambio mantiene lo que casi ningún
navegador de Android conserva: extensiones de escritorio y un bloqueador instalado desde el primer día.
En este racimo entra por lo suyo de descargas: guarda el vídeo que la página intenta no dejar guardar y
deja elegir con qué descargador lo hace.

### Cómo se instala

1. La entrega es la `v1.0.1`, del 21 de octubre de 2026; se instala la APK.
2. Al abrir por primera vez se importa el marcador que quieras y se revisa el bloqueador, que ya va puesto.
3. Para descargar un vídeo incrustado se mantiene pulsado sobre él o se usa el menú del propio navegador;
   si hay un gestor de descargas instalado, se puede mandar ahí.

### Lo que conviene saber antes

El proyecto nació en **agosto de 2026** y tiene **125 incidencias abiertas** con 714 estrellas: mucha gente
probándolo a la vez y bastante sin resolver todavía. La licencia BSD-3-Clause permite reutilizarlo. No
sustituye a tu banco, ni a la aplicación de tu trabajo, ni a nada donde guardes sesiones: un navegador
recién nacido no es todavía un sitio donde dejar las contraseñas.

### Cuándo no vale la pena

Si no te importan las extensiones en el móvil y Chrome o Firefox ya te sirven, es un cambio de navegador
para ganar dos cosas concretas. Y si lo que quieres es descargar vídeo de páginas, hay aplicaciones de este
mismo racimo que lo hacen mejor y sin cambiar de navegador.
"""

GUIA["Downvid/downvid"] = """
### Para qué sirve

Ventana para `yt-dlp` y `FFmpeg` en el escritorio: las dos herramientas de siempre, pero sin escribir
órdenes ni recordar opciones. Se pega la dirección, se elige formato y calidad, y el programa arma por
debajo la orden que haría falta escribir a mano.

### Cómo se usa

1. Se descarga la entrega `v1.9.1`, del 4 de noviembre de 2026, para Windows, macOS o Linux.
2. Se pega la dirección en la barra de arriba y se pulsa analizar; el programa pregunta a la web qué
   calidades hay y las lista.
3. Se marca la que quieras —vídeo, solo audio, o los dos— y se le da a descargar. La cola permite varias
   cosas a la vez y deja el historial a la vista.

### Lo que conviene saber antes

Está escrito en Go, con licencia MIT, y es de **agosto de 2026**: joven, aunque con 1.201 estrellas y
entregas muy seguidas. Su interfaz y su documentación están en chino y en inglés; el español no aparece.
Su propio texto, que aquí se copia sin adornos, se parece más a un anuncio de formas de donar que a una
descripción del programa, así que de la ficha no se puede sacar más de lo medido.

### Cuándo no vale la pena

Si ya usas `yt-dlp` en una terminal, esto te ahorra la memoria de las opciones y te quita el control fino.
Y si vas a descargar tres cosas al año, la versión web de cualquier servicio hace lo mismo sin instalar
nada.
"""

GUIA["FortoGraphy/prism-download-manager"] = """
### Para qué sirve

Gestor de descargas con conexiones en paralelo —hasta 32 por archivo, según su autor—, pensado para
archivos grandes que se cortan: sobrevive a un cierre inesperado, a la suspensión del equipo y al cable
desconectado, y retoma por el byte exacto donde se quedó. Trae además extensión de navegador y un botón
que aparece sobre los vídeos de una página para bajarlos en MP4 o en MP3.

### Cómo se usa

1. Se instala la entrega `v1.2.4`, del 1 de noviembre de 2026, y se elige la carpeta de descargas.
2. Se instala la extensión en el navegador; a partir de ahí, cada descarga del navegador se ofrece a Prism
   en vez de irse por su cuenta.
3. Para un vídeo incrustado se pasa el ratón por encima y se elige la calidad en el menú que aparece.

### Lo que conviene saber antes

El repositorio se creó el **15 de octubre de 2026**: tres semanas de vida y 752 estrellas. Es un proyecto
que está empezando, escrito en Rust y con licencia MIT, y su propio texto promete bastante —«bonito»,
«líquido», «rápido»—; eso es lo que dice su autor, no una medición. Si lo pruebas, que sea con archivos
que puedas volver a bajar.

### Cuándo no vale la pena

Con archivos pequeños o con una conexión que no se cae nunca, 32 conexiones no cambian nada: el cuello de
botella es el servidor, no tu programa. Y en Linux mucha gente acaba antes con el gestor que ya trae su
escritorio.
"""

GUIA["GopeedLab/gopeed"] = """
### Para qué sirve

Gestor de descargas multiplataforma —escritorio, móvil y navegador— que además de HTTP acepta enlaces
BitTorrent, magnet y ed2k. Está escrito en Go por dentro y Flutter por fuera, así que la misma aplicación
existe en Android, en Windows y en macOS. Es de los pocos de este racimo con versión de teléfono seria.

### Cómo se usa

1. Se instala desde la última entrega, `v1.9.3`, publicada el **18 de marzo de 2026** pese a que el
   repositorio sigue recibiendo cambios.
2. Se pega la dirección o se abre el enlace desde el navegador; el programa pregunta dónde guardar y con
   cuántas conexiones.
3. En el móvil, la aplicación se queda escuchando y las descargas se añaden desde ahí o desde su extensión
   de navegador.

### Lo que conviene saber antes

La entrega tiene **ocho meses** y el repositorio 356 incidencias abiertas: se usa mucho y se mantiene,
pero conviene saber que lo que instalarás no es de esta semana. Licencia GPL-3.0. Sobre los enlaces
BitTorrent y magnet, aquí no se enlaza ningún cliente ni ningún índice: se nombran, se explican y se deja
fuera todo lo demás.

### Cuándo no vale la pena

Si sólo descargas por HTTP desde Linux, `aria2` y una ventana para manejarlo ocupan menos y consumen menos.
Gopeed se justifica cuando quieres **la misma aplicación** en el teléfono y en el ordenador.
"""

GUIA["JunkFood02/Seal"] = """
### Para qué sirve

Descargador de vídeo y audio para Android: pega una dirección y guarda el vídeo en la calidad que elijas o
sólo el sonido en MP3. Por dentro es `yt-dlp`, así que hereda su lista de sitios, y su interfaz está
pensada para el dedo y no para la terminal.

### Cómo se usa

1. Se instala la APK de la entrega `v1.13.1`. Ojo: esa entrega es del **16 de octubre de 2024**, aunque el
   repositorio haya recibido cambios en 2026; el programa instalado no lleva dos años de arreglos.
2. Se pega la dirección; Seal consulta la web y ofrece las calidades disponibles.
3. Se elige vídeo o audio, se marca la carpeta y se descarga. Si el sitio necesita sesión, se puede pasar
   la cookie del navegador.
4. La primera vez que se usa una web que necesita combinar audio y vídeo, el programa pide un componente
   extra y lo instala por su cuenta.

### Lo que conviene saber antes

Es el más conocido de su clase: 30.353 estrellas, GPL-3.0, y sirve en cualquier Android moderno. Pero la
distancia entre la última entrega y el último cambio es el dato que de verdad importa aquí: si algo deja
de funcionar porque la web cambió, el arreglo ya está en el código y no en la versión que se descarga.

### Cuándo no vale la pena

Para bajar una canción suelta cada mucho tiempo, hay aplicaciones más ligeras. Y si tu teléfono es viejo y
con poca memoria, `yt-dlp` en una terminal de Android hace lo mismo gastando menos.
"""

GUIA["Tyrrrz/YoutubeDownloader"] = """
### Para qué sirve

Programa de escritorio para bajar vídeos y listas **sólo de YouTube**: vídeo suelto, lista entera o el
canal, en la calidad y el contenedor que elijas, con carátula y metadatos dentro del archivo cuando el
formato lo admite.

### Cómo se usa

1. Se descarga la entrega `1.17.1`, del 25 de octubre de 2026, para Windows, macOS o Linux.
2. Se pega la dirección del vídeo o de la lista en la caja de arriba y se pulsa buscar.
3. Se elige entre vídeo y sólo audio, la calidad y la carpeta; si es una lista, se pueden marcar elementos
   concretos en lugar de bajarla entera.

### Lo que conviene saber antes

Tiene 16.631 estrellas, licencia MIT y está escrito en C#: eso significa que en Linux necesita el entorno
de .NET o la versión publicada como ejecutable autónomo. Su alcance es deliberadamente estrecho —YouTube y
nada más—, cosa que a cambio le permite cuidar los detalles de esa única web. Su repositorio no trae texto
de presentación medido: lo que se sabe de él es lo que declara su descripción y lo que se ve en sus
entregas.

### Cuándo no vale la pena

Fuera de YouTube no sirve, y si tu lista de sitios es larga acabarás necesitando `yt-dlp` igualmente. Para
bajar dos vídeos en Windows, es más rápido que cualquier instalación.
"""

GUIA["Xmader/aria-ng-gui"] = """
### Para qué sirve

Ventana de escritorio para `aria2`: la terminal desaparece y queda una lista de descargas con barra de
progreso, cola, historial y límite de velocidad. Trae `aria2` dentro, así que no hay que instalarlo aparte.

### Cómo se usa

1. Se descarga la entrega `v3.1.2` —del **27 de septiembre de 2020**, con el repositorio parado desde ese
   mismo día— y se instala.
2. Se añade una descarga pegando la dirección, o arrastrando un archivo de torrente.
3. En ajustes se fijan conexiones por archivo, carpeta de destino y límite de velocidad.

### Lo que conviene saber antes

**Está abandonado desde 2020.** No es que vaya mal: es que no ha recibido un solo cambio en seis años y
las webs de hoy no son las de entonces. Se puede usar para descargar archivos directos, que es una técnica
que no ha cambiado, pero no esperes arreglos. La licencia es MIT y funciona en Windows, Linux y macOS.

### Cuándo no vale la pena

Hoy, casi siempre. Para lo mismo con mantenimiento vivo está `AriaNg`, o `Motrix` si prefieres algo con
ventana propia y desarrollo reciente. Esta entrada existe en el catálogo porque el recurso existe, no
porque se recomiende.
"""

GUIA["Xmader/aria-ng-gui-android"] = """
### Para qué sirve

La misma idea que su versión de escritorio, en Android: una pantalla para manejar `aria2` desde el teléfono,
con `aria2` incluido, cola de descargas y tema oscuro.

### Cómo se usa

1. Se instala la APK de la entrega `v1.3.1`, del **18 de abril de 2021**.
2. Se pega la dirección y se pulsa añadir; la descarga sigue aunque cierres la pantalla.
3. En ajustes se cambia el número de conexiones y la carpeta, que por defecto es la del almacenamiento
   compartido.

### Lo que conviene saber antes

Está **parado desde enero de 2023** y su última entrega tiene más de cinco años. Además su propio proyecto
marca varias funciones como pendientes y arrastra un fallo conocido: hay que pausar una tarea para que
guarde el progreso. En un Android actual puede fallar por permisos de almacenamiento, que han cambiado
desde 2021. Licencia MIT.

### Cuándo no vale la pena

Salvo que ya lo conozcas y te sirva para archivos directos, hoy no: `Gopeed` o `YTDLnis` hacen lo mismo en
el teléfono y siguen vivos.
"""

GUIA["agalwood/Motrix"] = """
### Para qué sirve

Gestor de descargas con ventana propia, cómodo para el uso diario: HTTP, FTP y enlaces de una sola vía, con
cola, categorías por tipo de archivo, límite de velocidad y bandeja del sistema. Por debajo lleva `aria2`,
así que la fiabilidad viene de ahí y lo que añade es la comodidad.

### Cómo se usa

1. Se instala la entrega `v2.3.0`, publicada **hoy mismo, 5 de noviembre de 2026**, con paquetes para
   Windows, macOS y Linux.
2. Se elige la carpeta de descargas y, si quieres, se instala la extensión del navegador para que capture
   los enlaces.
3. Las descargas se añaden pegando la dirección o arrastrando el archivo; la cola de la izquierda agrupa
   por tipo.

### Lo que conviene saber antes

Es el más usado de su clase en escritorio: 57.830 estrellas y 5.135 bifurcaciones. GitHub **no le reconoce
la licencia** —aparece como «NOASSERTION»—, aunque su proyecto declare que es abierta; si la licencia te
importa para reutilizar código, mira el archivo antes de fiarte. Y hay un detalle de familia: su autor
impulsa también `rayburst`, el antiguo Motrix Next, que hoy va por separado.

### Cuándo no vale la pena

En un equipo con poca memoria, `aria2` a secas gasta una cuarta parte. Y en Linux, si sólo bajas cosas de
vez en cuando, el gestor del escritorio ya lo hace.
"""

GUIA["aria2/aria2"] = """
### Para qué sirve

El motor. Una orden que descarga por HTTP, HTTPS, FTP, SFTP y por enlaces de una sola vía, partiendo cada
archivo en varios trozos y usando varias fuentes a la vez. No tiene ventana: se maneja por comandos o
dejándolo como servicio y hablándole por su interfaz de control, que es lo que usan casi todas las ventanas
de este racimo.

### Cómo se usa

1. Se instala desde el gestor de paquetes de tu sistema —está en todas las distribuciones— o se compila; la
   última entrega etiquetada es `release-1.37.0`, del 15 de noviembre de 2023.
2. Una descarga normal: `aria2c` seguido de la dirección y el número de conexiones (`-x 8 -s 8`).
3. Para dejarlo de servicio se arranca con el control remoto activo y un secreto; desde ahí, `AriaNg` o
   cualquier otra ventana se conecta a él.

### Lo que conviene saber antes

Que las entregas estén paradas desde 2023 **no significa abandono**: el repositorio recibe cambios en 2026
y el programa está terminado, no a medias. Tiene 43.414 estrellas, licencia GPL-2.0 y 1.186 incidencias
abiertas, la mayoría dudas de uso. No es un programa para principiantes: es la pieza que hay debajo de los
programas para principiantes.

### Cuándo no vale la pena

Si no quieres abrir una terminal, no empieces por aquí: instala una de las ventanas del racimo, que ya lo
llevan dentro. `aria2` se justifica en un servidor, en un equipo sin escritorio o para automatizar.
"""

GUIA["arnoldhao/xiadown"] = """
### Para qué sirve

Aplicación de escritorio que junta dos cosas que suelen ir separadas: una biblioteca de lo que descargas
—con ficha, portada y orden propio— y las descargas en sí, incluidas las que detecta mientras navegas.
Además funciona como cliente de YouTube y de fuentes de sindicación, de modo que puedes ver algo y guardarlo
desde la misma pantalla.

### Cómo se usa

1. Se instala la entrega `v1.0.4`, del 27 de julio de 2026.
2. Se pega la dirección en la barra de búsqueda o se navega por las fuentes que trae.
3. Lo descargado entra en la biblioteca, donde se etiqueta y se ordena.

### Lo que conviene saber antes

Su último cambio fue el **27 de julio de 2026**: tres meses sin tocarlo, con 759 estrellas y licencia
Apache-2.0. Su documentación está en chino. Y la versión es 1.0.4, es decir, el proyecto aún está
asentándose. Es de los pocos del racimo que piensa en la biblioteca y no sólo en la cola.

### Cuándo no vale la pena

Si sólo quieres bajar archivos sueltos, aquí hay demasiadas cosas encima. Y si tu biblioteca ya vive en
otro sitio —un servidor de medios, por ejemplo— no vas a querer una segunda.
"""

GUIA["axel-download-accelerator/axel"] = """
### Para qué sirve

Acelerador de descargas de terminal, minúsculo: abre varias conexiones contra el mismo archivo para que la
descarga no dependa de la lentitud de una sola. También reparte la carga entre varios servidores espejo del
mismo archivo, que es donde de verdad se nota.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución; si no está, se compila, que son dos órdenes.
2. Descarga normal: `axel` y la dirección. Con `-n` se fija el número de conexiones, con `-o` el nombre de
   salida.
3. Para reanudar algo cortado se vuelve a lanzar la misma orden con el archivo a medias en la carpeta: lo
   detecta y sigue.

### Lo que conviene saber antes

Tiene 3.423 estrellas, licencia GPL-2.0 y una entrega `v2.17.14` de **abril de 2024**, aunque el
repositorio recibe cambios en septiembre de 2026. Es una herramienta vieja y estable; no espera interfaz,
ni cola, ni historial decorado.

### Cuándo no vale la pena

Contra servidores que limitan por conexión —los que te cortan si abres varias—, `axel` empeora las cosas.
Para una descarga suelta, `wget2` o `curl` hacen el trabajo sin multiplicar conexiones.
"""

GUIA["binux/yaaw"] = """
### Para qué sirve

Página web suelta que se conecta a un `aria2` ya en marcha y lo maneja desde el navegador: lista de
descargas, progreso, pausa, reanudar y borrar. No trae servidor, ni programa que instalar: es un archivo que
se abre y habla con el motor por su interfaz de control.

### Cómo se usa

1. Hay que tener `aria2` arrancado con el control remoto activo y un secreto configurado.
2. Se abre la página —o su demostración pública— y se pega la dirección del motor y el secreto en ajustes.
3. A partir de ahí se añaden descargas desde la propia página.

### Lo que conviene saber antes

**No declara licencia**, así que no se sabe qué puedes hacer con su código; GitHub la marca como ausente.
Su último cambio es de **octubre de 2023** y **no tiene ninguna entrega publicada**. Funciona, pero es una
página de hace años y hoy cualquier cosa que exponga el control de `aria2` fuera de tu red es un riesgo: el
secreto tiene que ser largo y el acceso, local.

### Cuándo no vale la pena

Hoy, casi siempre: `AriaNg` hace lo mismo, con licencia declarada, entregas y mantenimiento. `yaaw` se
entiende como pieza histórica de cómo se manejaba `aria2` desde el navegador.
"""

GUIA["deniscerri/ytdlnis"] = """
### Para qué sirve

Descargador de vídeo y audio para Android con la idea contraria a la de sus competidores: en vez de
esconder el motor, deja al usuario elegir y actualizar cada pieza por separado —el intérprete de Python, el
motor de JavaScript, `FFmpeg` y `aria2c`—. Cuando una web cambia y algo deja de funcionar, se actualiza el
componente y se sigue, sin esperar a que salga versión.

### Cómo se usa

1. Se instala la APK de la entrega `v1.9.1.1`, del 19 de octubre de 2026.
2. En ajustes, sección de componentes, se descargan las piezas: Python, `FFmpeg` y, si quieres, `aria2c`.
3. Se pega la dirección, se eligen formato y calidad, y se descarga. Tiene cola, descargas simultáneas y
   guarda el historial.

### Lo que conviene saber antes

10.974 estrellas, GPL-3.0, escrita en Kotlin y con desarrollo diario. Es más exigente que `Seal` al
principio —hay que entender qué es cada componente— y a cambio envejece mejor. Su web propia mantiene la
documentación al día.

### Cuándo no vale la pena

Si quieres instalar y usar, sin tocar nada más, `Seal` es más corto. YTDlnis se justifica cuando descargas
mucho y de sitios variados, o cuando te has cansado de que una aplicación deje de funcionar de golpe.
"""

GUIA["iawia002/lux"] = """
### Para qué sirve

Programa de terminal escrito en Go para bajar vídeo de bastantes sitios —los chinos, sobre todo— sin
dependencias: un solo archivo ejecutable. Hace listas de reproducción, varias direcciones a la vez, reanudar
y reintentar solo.

### Cómo se usa

1. Se instala desde el gestor de paquetes de tu sistema, con `go install`, o se baja el binario de la
   entrega `v0.24.1`, del 6 de mayo de 2024.
2. `lux` y la dirección muestra las calidades disponibles sin descargar nada.
3. Con `-f` se elige la calidad; con `-p` se baja la lista entera; `-o` fija la carpeta.

### Lo que conviene saber antes

31.827 estrellas, licencia MIT, pero su entrega es de **mayo de 2024** y su último cambio, de marzo de 2026.
Para sitios que cambian a menudo eso es un problema: cuando la web cambia, `lux` falla y no siempre hay
prisa por arreglarlo. Es muy bueno en lo suyo —Go, un binario, sin instalar nada más— y flojo en
actualidad.

### Cuándo no vale la pena

Si tu sitio principal es YouTube, `yt-dlp` lo cubre mejor y con más mantenimiento. `lux` se elige por sus
sitios y por no necesitar intérprete.
"""

GUIA["lwthiker/curl-impersonate"] = """
### Para qué sirve

Una compilación de `curl` que se presenta ante el servidor **igual que un navegador de verdad**: mismo
saludo de cifrado, mismas cabeceras, mismo orden. Sirve para los sitios que responden distinto según quién
llama, no según lo que pide.

### Cómo se usa

1. Hay paquetes para varias distribuciones y una imagen de contenedor; también se puede compilar.
2. Se usa como `curl`, con un guion añadido al nombre del ejecutable para elegir a quién imita: el de Chrome,
   el de Edge, el de Safari o el de Firefox.
3. Las mismas opciones de siempre —`-o`, `-H`, `-L`— valen igual.

### Lo que conviene saber antes

Su último cambio es de **julio de 2024** y su última entrega, `v0.6.1`, de marzo de 2024: los navegadores
han cambiado de versión muchas veces desde entonces, y la huella que imita se queda atrás. Licencia MIT.
No es un descargador: es una herramienta para que otro programa pueda pasar por navegador. Y sirve para
entender por qué tu descargador falla en una web concreta.

### Cuándo no vale la pena

Si el sitio no te bloquea, esto no cambia nada. Y si lo que quieres es bajar vídeo, no empieces por aquí:
esto es fontanería, no una aplicación.
"""

GUIA["mayswind/AriaNg"] = """
### Para qué sirve

La ventana web de referencia para `aria2`: una página que se conecta al motor y lo maneja entera —cola,
progreso por archivo, velocidad, historial, ajustes del propio `aria2`— sin instalar nada más que un
archivo. Es la que más se usa cuando `aria2` corre en un servidor o en un equipo sin escritorio.

### Cómo se usa

1. Se descarga el paquete de la entrega `1.3.15`, del 5 de octubre de 2026, y se sirve como página, o se
   usa la versión publicada en su web.
2. Se configura la dirección del motor y el secreto; si están en la misma máquina, basta el valor por
   defecto.
3. Ya se pueden añadir descargas, cambiar la velocidad global y ver el reparto de conexiones.

### Lo que conviene saber antes

13.272 estrellas, licencia MIT, y sigue viva: la última entrega es de este octubre. Hay dos versiones, una
completa y otra mínima, y también compilaciones diarias para quien quiera lo último. Su punto débil es el
de todas: si expones el control de `aria2` en una red abierta, cualquiera manda en tu equipo. Secreto largo
y acceso cerrado.

### Cuándo no vale la pena

Si no tienes `aria2` funcionando, esto no hace nada: es la ventana, no el motor. Y si usas el escritorio con
ventanas propias como `Motrix`, tener otra pestaña abierta para lo mismo es un estorbo.
"""

GUIA["mayswind/AriaNg-Native"] = """
### Para qué sirve

La misma ventana que `AriaNg`, pero empaquetada como programa de escritorio: se abre como una aplicación
más, arranca `aria2` si hace falta y añade lo que una página no puede —abrir un torrente o un metalink
desde el explorador de archivos, y abrir la carpeta de la descarga terminada.

### Cómo se usa

1. Se instala la entrega `1.3.15`, del 5 de octubre de 2026; hay paquete para Windows, macOS y Linux.
2. Al abrir, busca un `aria2` local; si no lo encuentra, se le indica dónde está o se deja que lo use
   incluido.
3. Se arrastra el archivo de torrente a la ventana, o se pasa la dirección desde el navegador.

### Lo que conviene saber antes

2.729 estrellas, MIT, del mismo autor que `AriaNg` y con la misma numeración de versión: lo que aprendas en
una vale en la otra. Su ventaja sobre el motor suelto es que aquí, al terminar, puedes abrir la carpeta con
un clic. Su desventaja es el peso: lleva un navegador entero dentro.

### Cuándo no vale la pena

En un equipo con poca memoria, la versión web conectada al motor gasta mucho menos. Y si ya usas `Motrix` o
`Gopeed`, esto es otra aplicación para lo mismo.
"""

GUIA["mesamirh/MovieBox-Tui"] = """
### Para qué sirve

Programa de terminal que busca películas, series y emisiones en directo, y las reproduce o descarga usando
los reproductores que ya tienes instalados. La gracia es que no tiene interfaz gráfica: se maneja con el
teclado y se ve igual en una terminal remota.

### Cómo se usa

1. Se instala desde la entrega `v0.1.28`, del 29 de octubre de 2026, o con el gestor de paquetes de tu
   sistema si lo tiene.
2. Al abrirlo, se busca por nombre; los resultados se navegan con las flechas.
3. Al elegir uno se puede reproducir —delegando en el reproductor del sistema— o descargar el archivo.

### Lo que conviene saber antes

Tres cosas, y las tres importan. **Una:** la versión es `0.1.x`, o sea, que el proyecto aún no se considera
terminado, pese a sus 2.764 estrellas. **Dos:** la fuente de donde saca el catálogo no es pública ni
verificable aquí; este catálogo describe el programa y **no enlaza ninguna fuente de contenido**, y la
decisión de qué se descarga con él es de quien lo use. **Tres:** buena parte de ese catálogo es material con
derechos, así que el uso que se le dé es cosa tuya y de la ley de tu país. Licencia Apache-2.0.

### Cuándo no vale la pena

Si no vives en una terminal, la curva no compensa. Y si lo que quieres es ver algo hoy, un reproductor
normal es más rápido que cualquier descarga.
"""

GUIA["mikf/gallery-dl"] = """
### Para qué sirve

Descargador de **colecciones de imágenes**, no de vídeos: recorre un perfil, un álbum o una etiqueta de un
sitio de imágenes y se trae todo, con los nombres y la estructura de carpetas que le pidas. Es la
herramienta de referencia para archivar galerías enteras sin ir clic a clic.

### Cómo se usa

1. Se instala con `pip install gallery-dl`, o desde el gestor de paquetes de tu sistema.
2. `gallery-dl` y la dirección del perfil o del álbum: descarga lo que encuentra con la configuración por
   defecto.
3. Con un archivo de configuración se ajustan carpeta, nombre de archivo, filtros por etiqueta, número de
   elementos y cookies para lo que exige sesión.

### Lo que conviene saber antes

20.384 estrellas, GPL-2.0, entrega `v1.32.19` del 31 de octubre de 2026 y **1.085 incidencias abiertas**:
se usa muchísimo y se mantiene al día. No publica binarios —su entrega no lleva adjuntos—, así que se
instala como paquete de Python. Cada sitio tiene sus límites; su documentación los explica uno por uno y
conviene leerla antes de lanzarlo contra un perfil con miles de imágenes.

### Cuándo no vale la pena

Para cuatro imágenes, cualquiera lo hace a mano. Y contra un sitio que no permite descargar en serie, esto
tampoco: ni es lo que promete ni es lo que quieres.
"""

GUIA["nilaoda/N_m3u8DL-RE"] = """
### Para qué sirve

Descargador de **emisiones por trozos**: toma la lista de fragmentos de una emisión (HLS, DASH o ISM) y los
une en un solo archivo, con las pistas de audio y subtítulos que elijas. Es lo que se usa cuando el vídeo no
es un archivo sino una retransmisión partida en mil pedazos.

### Cómo se usa

1. Se descarga el binario de la entrega `v0.6.0-beta`, del 28 de junio de 2026, para Windows, Linux o macOS.
2. Se le pasa la dirección de la lista de fragmentos y, opcionalmente, la del audio por separado.
3. Se eligen pistas con `--select-video`, `--select-audio` y `--select-subtitle`, y el programa descarga en
   paralelo y une con `FFmpeg`.

### Lo que conviene saber antes

La etiqueta dice **beta** y así hay que tomarlo, aunque lleve 9.038 estrellas y dos años de entregas. Su
documentación está en chino, inglés y chino tradicional; la ayuda de la propia orden, en inglés. Aquí **no
se enlaza ninguna lista de fragmentos ni ninguna emisión concreta**: la herramienta vale para lo que sea
que tengas derecho a descargar, y eso no lo decide el programa.

### Cuándo no vale la pena

Si el vídeo ya es un archivo, esto es un rodeo: usa `aria2` o el navegador. Y sin `FFmpeg` instalado no une
nada, así que la instalación son dos piezas, no una.
"""

GUIA["persepolisdm/persepolis"] = """
### Para qué sirve

Gestor de descargas con ventana, escrito en Python, para Linux, BSD, macOS y Windows. Su rasgo propio es que
puede añadir una descarga a un programa de cola —`aria2` u otro— en vez de hacerla él, y que cuida la
integración con el entorno: icono de bandeja y notificaciones del sistema.

### Cómo se usa

1. En Linux se instala desde el paquete de la distribución o con el instalador de su web; la entrega es la
   `5.2.0`, del 14 de julio de 2025.
2. Se pega la dirección y se elige si la descarga la hace el propio programa o se delega en el motor.
3. En ajustes se fijan conexiones, carpeta y comportamiento de la cola.

### Lo que conviene saber antes

Su último cambio es de **octubre de 2025** y su entrega, de julio de 2025: lleva un año sin movimiento, con
7.491 estrellas y 320 incidencias abiertas. Como el programa está en Python, arrastra las versiones de las
bibliotecas de tu sistema, y es lo primero que se rompe tras una actualización grande de la distribución.
Licencia GPL-3.0.

### Cuándo no vale la pena

Si no usas Linux ni BSD, hay opciones más vivas. Y si ya usas `aria2`, esta ventana añade comodidad pero no
capacidad: el motor es el mismo.
"""

GUIA["pixel-point/media-downloader"] = """
### Para qué sirve

Aplicación nativa para macOS que descarga vídeo **y lo recorta en la misma ventana**: se pega la dirección,
se elige la calidad y, antes de guardar, se marcan los minutos de entrada y salida. Para bajar un fragmento
de una charla larga sin abrir un editor aparte.

### Cómo se usa

1. Se instala la entrega `v0.2.0`, del 7 de mayo de 2026, en un Mac.
2. Se pega la dirección y se espera a que analice las calidades.
3. Se elige la calidad, se marcan los extremos del recorte y se guarda.

### Lo que conviene saber antes

**No declara licencia**, así que no se sabe qué se puede hacer con su código. Su versión es `0.2.0` y su
último cambio, el mismo día de la entrega: **mayo de 2026**, sin movimiento desde entonces. Es un proyecto
pequeño —1.220 estrellas— y con una sola plataforma: fuera de macOS no existe.

### Cuándo no vale la pena

Si no tienes Mac, no hay nada que hablar. Y si tienes Mac y no necesitas recortar, `yt-dlp` instalado con
un gestor de paquetes hace lo mismo y se mantiene solo.
"""

GUIA["rawnaldclark/Stash"] = """
### Para qué sirve

Aplicación de Android que toma tus listas de música de dos servicios conocidos y las **trae al teléfono**:
las descarga, las mantiene ordenadas y las reproduce, con las mezclas diarias incluidas y audio de alta
resolución cuando el archivo lo trae. Es una biblioteca musical local construida a partir de lo que ya
escuchas.

### Cómo se usa

1. Se instala la APK de la entrega `v0.9.123`, del 3 de noviembre de 2026.
2. Se conectan las cuentas de los servicios en ajustes; el programa lee las listas y busca las pistas.
3. Se elige qué listas bajar y con qué calidad; lo descargado queda disponible sin conexión.

### Lo que conviene saber antes

Dos avisos. **El primero:** la versión es `0.9.x`, todavía por debajo de la 1.0, y cambia casi a diario
—tres entregas en una semana—, así que es un programa que se está haciendo. **El segundo:** que un archivo
se pueda descargar no significa que su licencia lo permita; la aplicación facilita la operación, la
responsabilidad de lo que guardes es de quien la usa. Licencia GPL-3.0.

### Cuándo no vale la pena

Si no pagas ninguno de esos dos servicios, no hay biblioteca que traer. Y si te basta con escuchar en línea,
descargar sólo te complica la vida.
"""

GUIA["rockdaboot/wget2"] = """
### Para qué sirve

El sucesor de `wget`: descarga archivos y **sitios completos**, con soporte de conexiones en paralelo,
compresión y reanudación. Es la herramienta de terminal para espejar una web entera o para automatizar
descargas dentro de un guion.

### Cómo se usa

1. Está en el gestor de paquetes de casi todas las distribuciones; si no, se compila. La entrega es la
   `v2.3.0`, del 21 de septiembre de 2026.
2. Un archivo: `wget2` y la dirección. Un sitio: `--recursive` con los límites que quieras —profundidad,
   tipo de archivo, dominio.
3. Con `--continue` se retoma lo cortado y con `--max-threads` se fija el paralelismo.

### Lo que conviene saber antes

El desarrollo principal vive en **GitLab**, no aquí: este repositorio es un espejo que acepta
contribuciones, y así lo dice su propio texto. 800 estrellas, licencia LGPL-3.0. Para espejar un sitio hay
que ser cuidadoso: sin límites, `wget2` se trae la web entera y también lo que no querías.

### Cuándo no vale la pena

Para bajar un archivo suelto, `curl` es más corto de recordar. Y contra sitios que generan el contenido al
vuelo, un espejo no sirve: se trae el cascarón.
"""

GUIA["soimort/you-get"] = """
### Para qué sirve

Descargador de terminal escrito en Python, veterano y de una sola orden: le das una dirección de vídeo o de
audio y lo baja, con las calidades que encuentre. Su fuerte histórico son los sitios chinos, aunque cubre
muchos más.

### Cómo se usa

1. Se instala con `pip install you-get`, o desde el gestor de paquetes del sistema.
2. `you-get -i` y la dirección muestra lo que hay disponible, sin descargar.
3. `you-get` y la dirección descarga; con `-o` se fija la carpeta y con `--format` la calidad.

### Lo que conviene saber antes

56.862 estrellas y una entrega `v0.4.1743` de **enero de 2025**, con cambios en el repositorio hasta
octubre de 2026. **GitHub no le reconoce la licencia** —aparece como «NOASSERTION»—, así que si vas a
reutilizar su código, mira el archivo antes. Su propio texto avisa de que dejará de admitir versiones viejas
de Python; conviene tener una versión reciente.

### Cuándo no vale la pena

Para YouTube y los sitios grandes, `yt-dlp` está más al día. `you-get` sigue teniendo sentido en su terreno
—los sitios chinos— y por la sencillez: una orden, sin configuración.
"""

GUIA["subhra74/xdm"] = """
### Para qué sirve

Gestor de descargas con ventana y extensión de navegador, con una idea muy clara: **la descarga se captura
donde nace**. La extensión detecta el archivo o el vídeo en la página y lo pasa al programa, que lo baja en
varios trozos y lo retoma exacto si se corta.

### Cómo se usa

1. Se instala la entrega `v9.0.9`, del 1 de noviembre de 2026, y su extensión desde la tienda del navegador
   que uses.
2. La primera vez, la extensión pide permiso para enviar las descargas al programa; a partir de ahí, cada
   descarga del navegador pasa por XDM.
3. Para un vídeo incrustado, el botón de la extensión se ilumina y ofrece las calidades detectadas.

### Lo que conviene saber antes

Es veterano —8.301 estrellas, con entregas desde 2013— y sigue vivo, con entrega de este mes. Está escrito
en Kotlin y su licencia es GPL-3.0. Su instalación en Linux tiene más pasos que en Windows, y la extensión
puede pedir más permisos de los que apetece darle: se instala a sabiendas o no se instala.

### Cuándo no vale la pena

Si tu navegador ya baja bien y no te importa no reanudar, esto es una capa más. Y si no quieres una
extensión con acceso a todas las pestañas, no es para ti.
"""

GUIA["uget/uget"] = """
### Para qué sirve

Pretendía ser un descargador universal escrito en Go, desde la terminal, con una sola orden para cualquier
fuente. Fichado aquí por completitud del racimo, no por utilidad: su propio texto lo presenta como trabajo
en curso.

### Cómo se usa

Según su documentación: compilación con las herramientas de Go y ejecución desde la terminal con la
dirección del archivo.

### Lo que conviene saber antes

**Está parado desde mayo de 2019.** Tiene **50 estrellas**, **no tiene ninguna entrega publicada** y su
licencia tampoco aparece reconocida por GitHub. No se ha probado, porque no hay nada que instalar: no hay
binarios. No es un recurso recomendable en 2026 y esta ficha lo dice sin rodeos en lugar de disimularlo.

### Cuándo no vale la pena

Siempre, hoy. Para lo mismo y con mantenimiento: `wget2`, `aria2` o `curl`. Esta entrada se conserva para
que quien llegue aquí sepa que el proyecto existió y en qué estado quedó, no para que lo use.
"""

GUIA["yausername/youtubedl-android"] = """
### Para qué sirve

No es una aplicación: es una **biblioteca para programadores** que quieran meter `yt-dlp` dentro de su app
de Android sin pelearse con Python. Trae los binarios y un envoltorio para llamarlos desde Java o Kotlin.

### Cómo se usa

1. Se añade como dependencia en el proyecto de Android, siguiendo lo que indica su documentación.
2. Se inicializa la biblioteca en la aplicación, que descarga las piezas la primera vez.
3. Desde el código se lanza una orden de `yt-dlp` y se recoge la salida para mostrarla en tu interfaz.
4. El archivo de configuración se coloca como `config.txt` dentro de la carpeta de la biblioteca.

### Lo que conviene saber antes

1.381 estrellas, GPL-3.0, último cambio en **noviembre de 2025**. **No tiene entregas** porque no es un
programa: se integra en el tuyo. Y si lo integras, heredas su licencia y su mantenimiento: cuando una web
cambie, tendrás que actualizar tú.

### Cuándo no vale la pena

Si no programas para Android, no hay nada que hacer con esto. Y si programas, valora antes si te conviene
llevar Python dentro de tu aplicación: pesa y complica la publicación en la tienda.
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
