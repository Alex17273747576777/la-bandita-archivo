#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_audio.py · las guías escritas a mano del racimo «audio» (52 recursos).

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
RACIMO = "audio"

GUIA = {}

GUIA["AntennaPod/AntennaPod"] = """
### Para qué sirve

Gestor de pódcast para Android, de los que llevan más tiempo vivos: suscripciones, cola, descarga automática
de los episodios nuevos, velocidad de reproducción y sincronización de lo escuchado con un servidor que
elijas. Sin cuenta, sin publicidad y sin nada que pida registro.

### Cómo se usa

1. Se instala la APK de la entrega `3.12.3`, del 13 de octubre de 2026.
2. Se busca el pódcast por nombre, o se pega su dirección de fuente; con un archivo de suscripciones se
   importa la lista entera de golpe.
3. En ajustes se decide qué se descarga solo, cuándo y con qué límite de espacio; eso es lo que evita que el
   teléfono se llene de episodios que no vas a oír.

### Lo que conviene saber antes

8.266 estrellas, GPL-3.0 y catorce años de historia. La sincronización no va contra un servicio del proyecto:
necesita un servidor compatible que pongas tú (por ejemplo, uno de los que tienen ficha en este mismo
racimo), y esa pieza la tienes que montar aparte.

### Cuándo no vale la pena

Si oyes dos pódcast al mes, la aplicación que ya trae el teléfono hace eso y no ocupa sitio. AntennaPod se
justifica cuando sigues diez y quieres cola, descargas y velocidad fina.
"""

GUIA["FFmpeg/FFmpeg"] = """
### Para qué sirve

El juego de programas que convierte, corta, une, recodifica y mide audio y vídeo. No es una aplicación con
ventana: es la pieza que hay dentro de casi todas las demás de este racimo. Cuando un programa te pregunta
«¿con qué convierto esto?», la respuesta suele ser `ffmpeg`.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución, o se descarga una compilación ya hecha. Este
   repositorio es **un espejo**: el original vive en `git.ffmpeg.org` y así lo dice su descripción.
2. Convertir un archivo: `ffmpeg -i entrada.wav -codec:a libopus -b:a 96k salida.opus`.
3. Sacar sólo el sonido de un vídeo: `ffmpeg -i video.mp4 -vn -codec:a copy audio.m4a`.
4. Mirar qué trae un archivo, sin tocar nada: `ffprobe archivo.mp3`.

### Lo que conviene saber antes

66.537 estrellas y **ninguna entrega publicada en GitHub**: las versiones se cogen de la web del proyecto o
del paquete de tu sistema. GitHub **no le reconoce la licencia** («NOASSERTION») porque convive con
bibliotecas de varias condiciones; si vas a distribuirlo dentro de algo tuyo, revisa qué compilación coges,
porque no todas tienen las mismas.

### Cuándo no vale la pena

Para convertir una canción una vez, cualquier web lo hace sin instalar 300 MB de herramientas. `FFmpeg` se
justifica cuando repites la operación, cuando automatizas, o cuando quieres saber exactamente qué se le hace
al archivo.
"""

GUIA["GNOME/easytag"] = """
### Para qué sirve

Editor de etiquetas de audio para el escritorio de GNOME: abre un archivo o una carpeta entera y permite
escribir título, artista, álbum, año, número de pista, carátula y letra, con renombrado de los archivos a
partir de esas etiquetas.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución; **aquí no hay entregas**, porque este
   repositorio es un espejo de sólo lectura de GitLab.
2. Se abre la carpeta; los archivos aparecen en una lista con los campos a la derecha.
3. Se rellenan los que falten y se guarda; si hay varias pistas iguales, se aplica el mismo valor a todas de
   una vez.

### Lo que conviene saber antes

83 estrellas y GPL-2.0. Está en modo mantenimiento desde hace años: se arregla lo que se rompe, no se añaden
funciones. Su último cambio es de octubre de 2026, así que sigue compilando. Su punto flojo es el mismo que
el de todos los editores manuales: no busca los datos por ti.

### Cuándo no vale la pena

Si tu biblioteca es grande, escribir etiquetas a mano es un castigo: `Picard` o `beets` las buscan en una
base de datos y las rellenan solas. Easytag se elige cuando sabes exactamente lo que quieres escribir.
"""

GUIA["KDE/elisa"] = """
### Para qué sirve

Reproductor de música del escritorio KDE, sencillo a propósito: abre la carpeta que le indiques, la ordena
por artista y álbum, y reproduce. Sin biblioteca complicada, sin ajustes escondidos, con la estética del
entorno al que pertenece.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución, o desde la tienda de aplicaciones de KDE. Aquí
   no hay entregas: el repositorio es de desarrollo.
2. La primera vez se elige la carpeta de música; el programa la indexa y tarda un rato según el tamaño.
3. Se reproduce, se encola y se busca por el panel lateral.

### Lo que conviene saber antes

370 estrellas, LGPL-3.0, escrito en C++ y con cambios de esta semana. Está pensado para un escritorio
concreto: fuera de KDE funciona, pero arrastra sus bibliotecas. No lleva etiquetado, ni conversión, ni
sincronización con el teléfono: sólo reproduce lo que ya está bien ordenado.

### Cuándo no vale la pena

Si tu música está revuelta o sin etiquetas, aquí se va a ver exactamente así. Y si quieres escuchar en el
móvil lo mismo que en el ordenador, necesitas además un servidor, que es otra pieza.
"""

GUIA["LMS-Community/slimserver"] = """
### Para qué sirve

Servidor de música pensado para los aparatos de Logitech —Squeezebox, Boom, Radio, Transporter— y para todo
lo que hable su protocolo. Hoy se llama **Lyrion Music Server** y sigue sirviendo música a esos aparatos,
que llevan más de una década descatalogados y siguen funcionando gracias a él.

### Cómo se usa

1. Se instala en el equipo que hará de servidor: hay paquetes para varias distribuciones y para Windows y
   macOS. Aquí no hay entregas; el proyecto publica fuera de GitHub.
2. Se abre su panel en el navegador, se añade la carpeta de música y se espera a que indexe.
3. Los aparatos de la red se encuentran solos; desde el panel se les manda música o se controlan uno por uno.

### Lo que conviene saber antes

1.815 estrellas y está escrito en Perl, lo cual explica que su instalación sea más delicada que la de otros
servidores de este racimo. GitHub **no le reconoce la licencia**. Su valor es único: sin este programa, los
aparatos de Logitech quedan inservibles, y con él vuelven a ser lo que eran.

### Cuándo no vale la pena

Si no tienes un aparato de esos, no hay razón para montarlo: para lo demás hay servidores más modernos y
más fáciles de instalar en este mismo racimo.
"""

GUIA["MetrolistGroup/Metrolist"] = """
### Para qué sirve

Cliente de YouTube Music para Android, escrito en Kotlin y con la interfaz del sistema de diseño actual:
escucha, listas, radio, letras y descarga para oír sin conexión.

### Cómo se usa

1. Se instala la APK de la entrega `v13.7.0`, del 7 de septiembre de 2026.
2. Se abre y se navega sin cuenta; si quieres que se guarden tus listas, se puede iniciar sesión con la
   cuenta del servicio.
3. La descarga se activa por lista o por canción en el menú de cada elemento; lo bajado queda en la pantalla
   de descargas.

### Lo que conviene saber antes

**El propio proyecto avisa de que está en modo mantenimiento**: se arreglan fallos y se hacen mejoras
pequeñas, y no se aceptan funciones nuevas. No está muerto, dice, pero tampoco crece. Tiene 14.026 estrellas
y licencia GPL-3.0. Y conviene recordar lo de siempre en este racimo: es un cliente de un servicio ajeno,
no un catálogo propio, y el servicio puede cambiar cuando quiera.

### Cuándo no vale la pena

Si ya pagas el servicio y su aplicación te sirve, esto es la misma música con otra piel. Se elige cuando
quieres descargar y escuchar sin anuncios, a sabiendas de que el proyecto no va a evolucionar.
"""

GUIA["MusicPlayerDaemon/MPD"] = """
### Para qué sirve

Demonio reproductor: se queda corriendo en el equipo, tiene tu música indexada y la reproduce por la salida
de sonido del servidor. No tiene ventana propia; se le controla desde cualquier cliente —hay decenas— por
red, y por eso es la pieza que sostiene a otros programas de este racimo.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución; aquí no hay entregas.
2. Se edita su archivo de configuración con la carpeta de música, la salida de audio y, si hace falta, el
   acceso por red.
3. Se arranca el servicio y se conecta un cliente; desde él se busca, se encola y se reproduce.

### Lo que conviene saber antes

2.812 estrellas, GPL-2.0, y una estabilidad que viene de su edad: nació en 2003 y su interfaz no ha cambiado.
Todo se configura en un archivo de texto, y eso es a la vez su virtud —se puede automatizar entero— y su
pega —si te equivocas en una línea, no hay ventana que te lo diga.

### Cuándo no vale la pena

Para escuchar música en el ordenador de casa, es fontanería innecesaria: un reproductor con ventana hace
eso. MPD tiene sentido en un equipo sin pantalla, en una casa con varios clientes, o cuando quieres que la
música siga sonando al cerrar la sesión.
"""

GUIA["OuterTune/OuterTune"] = """
### Para qué sirve

Reproductor de Android para música local y para YouTube Music, con interfaz Material 3 y buena parte de las
comodidades que la gente busca hoy: cola, letras, descargas y controles en la pantalla de bloqueo.

### Cómo se usa

1. Se instala la APK de la entrega `v0.10.1`, del 19 de diciembre de 2025.
2. Se elige la carpeta de música local, o se conecta la cuenta del servicio para lo de la nube.
3. La cola se arma con pulsación larga; el resto se parece bastante a cualquier reproductor moderno.

### Lo que conviene saber antes

Su propio texto lo dice sin rodeos: **el proyecto ya no está en desarrollo activo**, y remite a otros
clientes derivados para quien busque uno mantenido. Tiene 5.443 estrellas y GPL-3.0. Funciona, y funcionará
mientras el servicio no cambie, pero no esperes arreglos.

### Cuándo no vale la pena

Hoy, si buscas algo vivo: usa uno de los que el propio proyecto señala. Sigue teniendo sentido si ya lo
tienes configurado y te va bien, o si lo que quieres es sobre todo música local con una interfaz agradable.
"""

GUIA["OxygenCobalt/Auxio"] = """
### Para qué sirve

Reproductor de música **local** para Android, deliberadamente estrecho: ordena tu biblioteca por carpetas,
álbumes, artistas y etiquetas, y reproduce bien. Su autor lo presenta como el reproductor sin las funciones
que no usa nadie, y eso es exactamente lo que es.

### Cómo se usa

1. Se instala la APK de la entrega `v4.1.5`, del 4 de agosto de 2026.
2. La primera vez se concede permiso al almacenamiento y se elige qué carpetas entran en la biblioteca.
3. Se navega por las pestañas; la búsqueda está arriba y el menú de cada pista ofrece encolar, añadir a
   lista y ver la ruta del archivo.

### Lo que conviene saber antes

4.425 estrellas, GPL-3.0, y desarrollo activo con cambios de esta misma semana. No hay nube, ni cuentas, ni
sincronización: sólo lo que hay en el teléfono. Al no arrastrar servicios ajenos, es de los pocos de este
racimo que no puede romperse porque otra empresa cambie algo.

### Cuándo no vale la pena

Si tu música está en un servidor y quieres oírla desde el móvil, esto no la ve. Y si te gustan las listas
compartidas en línea, aquí no hay.
"""

GUIA["PaulWoitaschek/Voice"] = """
### Para qué sirve

Reproductor de **audiolibros** para Android, pensado para lo que necesita ese formato y no tiene un
reproductor de música: pausa automática al dormirte, salto por capítulo, velocidad fina, memoria de la
posición exacta y un valor de posición que no se pierde al cambiar de archivo.

### Cómo se usa

1. Se instala la APK de la entrega `26.10.8`, del 29 de octubre de 2026.
2. Se elige la carpeta donde están los audiolibros; cada subcarpeta se toma como un libro y los archivos se
   ordenan por nombre.
3. Se marca el temporizador de sueño, la velocidad y el salto; el progreso se guarda solo.

### Lo que conviene saber antes

3.246 estrellas, GPL-3.0 y doce años de desarrollo. Su enfoque es la carpeta, no la nube: no hay descargas ni
sincronización de posición entre aparatos. Eso lo cumple otro de los recursos de este racimo, el servidor
que se monta por separado.

### Cuándo no vale la pena

Si oyes audiolibros desde una aplicación de tienda con su propia reproducción, el cambio tiene sentido sólo
si tus archivos son tuyos y están en el teléfono. Y para música no sirve: cada libro es una carpeta y una
posición.
"""

GUIA["RetroMusicPlayer/RetroMusicPlayer"] = """
### Para qué sirve

Reproductor de música local para Android con mucha atención a la presentación: temas, colores que salen de
la carátula, ecualizador, etiquetas editables y una pantalla de reproducción cuidada.

### Cómo se usa

1. Se instala la APK de la entrega `v7.0.3`, del 13 de agosto de 2026.
2. Se concede permiso al almacenamiento y se elige qué carpetas entran.
3. En ajustes se cambia el tema, se activa el ecualizador y se decide qué pestañas aparecen.

### Lo que conviene saber antes

5.384 estrellas y GPL-3.0. Su propio texto pide colaboradores y **mantenedores**: es la señal de que el
proyecto se sostiene con esfuerzo. Funciona bien y se actualiza, pero conviene saber que su continuidad no
está asegurada por un equipo grande.

### Cuándo no vale la pena

Si quieres reproducir y ya, trae demasiadas cosas. Y si tu prioridad es la estabilidad a cinco años, otros
reproductores de este racimo tienen un equipo detrás más claro.
"""

GUIA["Spotifyd/spotifyd"] = """
### Para qué sirve

Demonio que hace que un equipo —una Raspberry Pi, un ordenador sin pantalla— aparezca como **dispositivo de
Spotify** en la aplicación oficial. Se controla desde el teléfono, suena por el equipo, y no necesita
interfaz en él.

### Cómo se usa

1. Se instala desde el gestor de paquetes o se compila; la entrega es la `v0.4.2`, del 19 de noviembre de
   2025.
2. Se crea un archivo de configuración con el usuario, el nombre del aparato y la salida de audio.
3. Se arranca como servicio y, en la aplicación oficial, el equipo aparece en la lista de dispositivos.

### Lo que conviene saber antes

10.822 estrellas, GPL-3.0, escrito en Rust. Su último cambio es de **mayo de 2026** y su entrega de noviembre
de 2025: va despacio. Y hay algo que su propio proyecto deja claro en el ecosistema: este tipo de cliente
necesita cuenta de pago; la versión gratuita no se soporta.

### Cuándo no vale la pena

Si no tienes un equipo dedicado sin pantalla, no aporta nada frente a la aplicación oficial. Y si no pagas
la cuenta, directamente no funciona.
"""

GUIA["Taiko2k/Tauon"] = """
### Para qué sirve

Reproductor de música de escritorio con una pretensión poco habitual: sonar bien y no estorbar. Trae
ecualizador, visualizaciones, reproducción sin cortes entre pistas, listas por carpetas y por etiquetas, y
una paleta que cambia con la carátula. Está escrito en Python.

### Cómo se usa

1. Se instala desde la entrega `v13.1.1`, del 30 de octubre de 2026, o con el paquete de tu distribución.
2. La primera vez se añaden las carpetas de música; el indexado tarda según el tamaño.
3. Se ordena por álbum, artista o carpeta, y se arrastran pistas a la cola.

### Lo que conviene saber antes

2.954 estrellas, GPL-3.0, y desarrollo vivo con entrega de esta semana. En Linux se instala fácil; en Windows
y macOS requiere más pasos porque arrastra Python y sus bibliotecas. Es un programa de autor, no de
comunidad grande: eso explica tanto su carácter como su ritmo.

### Cuándo no vale la pena

Si tu biblioteca es enorme y sólo quieres buscar y darle al play, otros reproductores de este racimo son más
directos. Y si no te importan las visualizaciones ni el aspecto, la mitad de lo que ofrece no la vas a usar.
"""

GUIA["TortugaPower/BookPlayer"] = """
### Para qué sirve

Reproductor de audiolibros **sin protección** para iPhone y iPad, con lo que hace falta en ese formato:
posición por libro, velocidad, temporizador de sueño, lista de reproducción y una biblioteca que se ordena
sola. Se le pasan los archivos por el explorador, por el cable o desde un servidor de archivos.

### Cómo se usa

1. Se instala desde la entrega `6.0.0`, del 24 de octubre de 2026, o desde la tienda de Apple.
2. Se añaden los archivos con el botón de importar, o se conecta una carpeta en red.
3. Se empieza a oír y la posición queda guardada por libro; la velocidad se ajusta en la barra inferior.

### Lo que conviene saber antes

2.275 estrellas, GPL-3.0 y escrito en Swift, o sea, sólo Apple. Es uno de los pocos reproductores de
audiolibros libres para ese sistema, y su comunidad mantiene una wiki con guías de temas e iconos. No hay
versión para Android: si tu casa es mixta, necesitarás dos programas.

### Cuándo no vale la pena

Si compras los audiolibros en una tienda con su propia aplicación, esta no los lee: es para archivos que ya
son tuyos y sin protección.
"""

GUIA["XilinJia/Podcini"] = """
### Para qué sirve

Gestor de pódcast para Android que, además de las fuentes de siempre, acepta canales y listas de vídeo como
si fueran pódcast: suscripción, descarga y reproducción en la misma aplicación. Nace como derivado de
AntennaPod y conserva su forma de trabajar.

### Cómo se usa

1. Se instala la APK de la entrega `7.3.5`, del 13 de enero de 2025.
2. Se añade una fuente normal por su dirección, o un canal por su enlace; cada uno aparece como una
   suscripción más.
3. Se marca la descarga automática por suscripción y se escucha desde la cola.

### Lo que conviene saber antes

**Su último cambio es de enero de 2025**: no se ha tocado desde entonces, y tiene 238 estrellas. Es decir:
un proyecto pequeño, parado, sobre una base buena. Funcionará mientras las fuentes no cambien y mientras
Android no apriete los permisos.

### Cuándo no vale la pena

Hoy, para uso nuevo: AntennaPod, del que deriva, sigue vivo y hace lo mismo con los pódcast normales. Podcini
tiene sentido si te interesa mezclar canales de vídeo en la misma cola.
"""

GUIA["acoustid/chromaprint"] = """
### Para qué sirve

Biblioteca en C que calcula la **huella acústica** de un archivo de audio: un resumen matemático del sonido
que permite reconocer la misma canción aunque esté recomprimida, cortada o con otro nombre. Es la pieza que
usan los programas de reconocimiento para decir «esto es tal tema».

### Cómo se usa

1. Normalmente no se usa sola: se instala como dependencia del programa que la necesita, o se compila con
   `cmake` y se enlaza desde tu propio código.
2. Trae una orden de ejemplo en sus herramientas que calcula la huella de un archivo.
3. Para identificar de verdad hace falta además consultar la base de datos pública del proyecto AcoustID, con
   la huella y la duración.

### Lo que conviene saber antes

1.415 estrellas y entrega `v1.6.2` publicada el 15 de octubre de 2026, la misma semana en que se midió. Su
texto aclara que **no es una huella de propósito general**: sirve para audio casi idéntico, no para
parecidos. GitHub **no le reconoce la licencia** en la ficha, aunque el proyecto declare la suya.

### Cuándo no vale la pena

Si lo que quieres es etiquetar música, no empieces aquí: usa un programa que ya lo haga, como `Picard`. Esta
biblioteca es para quien escribe el programa.
"""

GUIA["advplyr/audiobookshelf"] = """
### Para qué sirve

Servidor autoalojado de **audiolibros y pódcast**: guarda los archivos, ordena la biblioteca por autor y
serie, guarda la posición de escucha y sirve todo a sus aplicaciones de Android e iOS. Es la pieza central
si quieres oír tus audiolibros desde varios aparatos sin copiarlos.

### Cómo se usa

1. Se instala con contenedor o con el paquete de su web; la versión medida es la `v2.37.2`, del 23 de octubre
   de 2026.
2. Se crea una biblioteca y se apunta a la carpeta donde están los libros, ordenada por autor y título.
3. Se instalan las aplicaciones para el teléfono, se conecta cada una al servidor y se descarga lo que se
   quiera oír sin conexión.

### Lo que conviene saber antes

14.918 estrellas, GPL-3.0, escrito en JavaScript. Su punto fuerte es la posición de escucha compartida entre
aparatos; su punto débil, que hay que mantener un servidor encendido y con copia de seguridad: si se pierde
la base de datos, se pierde el progreso de todo lo escuchado.

### Cuándo no vale la pena

Con cuatro libros y un solo teléfono, es demasiada infraestructura para lo que da. Se justifica cuando la
biblioteca crece o cuando son varias personas las que escuchan.
"""

GUIA["airsonic-advanced/airsonic-advanced"] = """
### Para qué sirve

Servidor de música por web compatible con el protocolo Subsonic: se instala en un equipo, apunta a una
carpeta de música y sirve la biblioteca a cualquier cliente que hable ese protocolo, con reproducción en el
navegador y listas.

### Cómo se usa

1. Se instala con contenedor o con el paquete de Java; la entrega medida es la `v10.6.0`, del 24 de abril de
   2020.
2. Se configura la carpeta, el usuario y la contraseña en el panel.
3. Se conecta un cliente Subsonic —hay varios en este racimo— y se escucha desde cualquier sitio.

### Lo que conviene saber antes

**Está parado**: su último cambio es de abril de 2024 y su última entrega de 2020, con 1.404 estrellas y
licencia GPL-3.0. Es un proyecto que en su día mejoró a Airsonic y que hoy no recibe arreglos. Instalarlo en
2026 significa asumir su mantenimiento: piezas antiguas de Java, y sin nadie al otro lado.

### Cuándo no vale la pena

Hoy, para empezar de cero: `Navidrome` y `supersonic` cubren lo mismo y siguen vivos. Esta entrada está en el
catálogo porque el recurso existe y se midió, no porque se recomiende.
"""

GUIA["ampache/ampache"] = """
### Para qué sirve

Servidor de música y vídeo por web, escrito en PHP: se instala en un alojamiento normal, apunta a la carpeta
de archivos y da acceso a la colección desde el navegador o desde clientes que hablen su interfaz. Lleva
años en el ecosistema y tiene fama de aguantar bibliotecas grandes.

### Cómo se usa

1. Se despliega en un servidor web con PHP y base de datos; la entrega medida es la `8.3.0`, del 20 de octubre
   de 2026.
2. En el instalador se define la carpeta de música, el usuario administrador y el modo de catalogación.
3. Se añade un cliente o se usa la web; la catalogación inicial hay que lanzarla a mano y puede tardar.

### Lo que conviene saber antes

3.845 estrellas, AGPL-3.0. Su texto avisa de que la versión 8 es la línea principal y todavía está en
construcción, así que conviene leer las notas de cada entrega. Al ser PHP, se instala en cualquier
alojamiento barato, y eso es justo lo que otros servidores de este racimo no permiten.

### Cuándo no vale la pena

Si no tienes ya un servidor web con PHP, montar el entorno cuesta más que instalar otro servidor con un solo
comando. Y si tu colección es pequeña, sobra potencia.
"""

GUIA["anandnet/Harmony-Music"] = """
### Para qué sirve

Aplicación de música multiplataforma escrita en Flutter, con la idea de ser un reproductor y buscador propio:
interfaz para buscar, listas, descarga y reproducción en Android, escritorio y web, con un módulo que
reconoce la canción que está sonando.

### Cómo se usa

1. Se instala desde la entrega `v1.12.2`, del 7 de diciembre de 2025.
2. Se busca por canción o artista y se reproduce en streaming; las listas se crean dentro de la aplicación.
3. Lo descargado queda disponible sin conexión desde la pestaña de descargas.

### Lo que conviene saber antes

3.087 estrellas, GPL-3.0, con traducciones gestionadas en una plataforma abierta, señal de comunidad
internacional. Su último cambio es de **diciembre de 2025**: casi un año sin movimiento. Y como todos los de
esta familia, no tiene catálogo propio: toma la música de servicios ajenos, que pueden cambiar de reglas.

### Cuándo no vale la pena

Si buscas algo que se mantenga al día, hay opciones más activas en este racimo. Y si tienes tu música en
local, este programa no es para eso.
"""

GUIA["beetbox/beets"] = """
### Para qué sirve

Gestor de biblioteca musical desde la terminal: importa carpetas, **identifica cada disco en una base de
datos pública**, escribe las etiquetas correctas, renombra y ordena los archivos según un patrón que tú
definas, y mantiene un catálogo consultable. Es la herramienta de quien tiene miles de archivos y quiere
dejarlos en orden de una vez.

### Cómo se usa

1. Se instala con `pip install beets` o desde el gestor de paquetes; la entrega es la `v2.14.1`, del 17 de
   septiembre de 2026.
2. Se escribe un archivo de configuración con la carpeta de la biblioteca y el patrón de nombres.
3. `beet import` sobre una carpeta: pregunta por cada disco dudoso y escribe lo que confirmes.
4. `beet ls`, `beet stats` y `beet modify` sirven para consultar y corregir en bloque.

### Lo que conviene saber antes

15.895 estrellas, licencia MIT, dieciséis años de historia. Su fuerza son los complementos: hay decenas para
traer letras, portadas, estadísticas o sincronizar con otros reproductores. Su riesgo es el contrario al de
un programa con ventana: una orden mal escrita toca cientos de archivos a la vez, así que la primera prueba
se hace sobre una copia.

### Cuándo no vale la pena

Con dos discos, no: es más tiempo configurarlo que ordenarlo a mano. Y si no te sientes cómodo con la
terminal, `Picard` hace la mitad del trabajo con ventana.
"""

GUIA["blackcandy-org/blackcandy"] = """
### Para qué sirve

Servidor de música autoalojado con interfaz web moderna: se instala, apunta a la carpeta de música y sirve la
biblioteca desde el navegador o desde sus aplicaciones, con listas, búsqueda y reproducción en continuo.

### Cómo se usa

1. Se despliega con contenedor; la entrega medida es la `v3.2.1`, del 26 de agosto de 2026.
2. En el panel se añaden las carpetas de música y se espera a que indexe.
3. Se escucha desde la web o se conecta la aplicación móvil con la dirección del servidor y el usuario.

### Lo que conviene saber antes

4.429 estrellas, MIT, escrito en Ruby. Es de los servidores más fáciles de levantar de este racimo y su
licencia permisiva permite adaptarlo. No habla el protocolo Subsonic, así que no vale con cualquier cliente:
hay que usar el suyo o la web.

### Cuándo no vale la pena

Si ya tienes clientes que hablan ese protocolo, mejor un servidor compatible. Y si sólo escuchas en el
ordenador donde está la música, no necesitas servidor.
"""

GUIA["gpodder/gpodder"] = """
### Para qué sirve

Cliente de pódcast de escritorio: suscripciones, descarga de episodios, cola y reproducción, además de una
herramienta aparte para bajar los archivos sin el reproductor. Existe para Linux, Windows y macOS, y es de
los pocos de su clase con esa cobertura.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución o desde su web; la entrega es la `3.11.5`, del
   20 de diciembre de 2024.
2. Se añaden las direcciones de las fuentes o se importa una lista de suscripciones.
3. Se marcan las descargas y la carpeta de destino; los episodios se escuchan en el programa o se abren en
   otro reproductor.

### Lo que conviene saber antes

1.455 estrellas y GPL-3.0. La entrega es de **diciembre de 2024**, aunque el repositorio recibe cambios en
noviembre de 2026: el programa se arregla y no se publica. La sincronización entre aparatos no depende de un
servidor del proyecto: hace falta uno compatible que pongas tú.

### Cuándo no vale la pena

Si escuchas pódcast en el teléfono, un cliente de Android de este racimo es más directo. gPodder se elige
para el ordenador, sobre todo en Linux.
"""

GUIA["harmonoid/harmonoid"] = """
### Para qué sirve

Reproductor y gestor de biblioteca escrito en Flutter: la misma aplicación en Windows, Linux, macOS, Android
e iOS. Lee la música local, la ordena, muestra carátulas y letras, y permite listas y cola.

### Cómo se usa

1. Se instala desde la entrega `v0.3.37`, del 4 de noviembre de 2026.
2. Se elige la carpeta de música; el programa indexa y muestra la biblioteca por álbum, artista y carpeta.
3. Se reproduce desde la cola, y en las plataformas que lo permiten aparecen controles del sistema.

### Lo que conviene saber antes

4.801 estrellas y versión `0.3.x`, todavía por debajo de la 1.0 después de seis años de proyecto: es el dato
que mejor lo describe. GitHub **no le reconoce la licencia** en la ficha. Funciona en muchas plataformas a
la vez justamente porque Flutter lo permite, y eso mismo hace que en algunas se sienta menos nativo.

### Cuándo no vale la pena

Si quieres un reproductor maduro y terminado, la versión `0.3` lo dice todo. Y si sólo usas un sistema, hay
programas hechos para él que funcionan mejor.
"""

GUIA["imputnet/cobalt"] = """
### Para qué sirve

Servicio web para **guardar lo que quieres**, sin anuncios, sin rastreo y sin ventanas emergentes: se pega
una dirección y devuelve el archivo. Su proyecto se ofrece como servicio público, y también se puede montar
en un servidor propio si prefieres no depender de nadie.

### Cómo se usa

1. Desde su web: se pega la dirección, se elige el formato y se descarga.
2. Para montarlo: se despliega con contenedor siguiendo su documentación; es una aplicación web con su parte
   de servidor.
3. En la instancia propia se pueden limitar formatos y servicios permitidos, que es lo que hace viable
   mantenerla abierta a otras personas.

### Lo que conviene saber antes

45.812 estrellas, AGPL-3.0, **sin ninguna entrega publicada en GitHub**: se consume como servicio, no como
programa que se instala. Su último cambio es de **abril de 2026**. Vive de depender de servicios ajenos, así
que cuando uno cambia, la instancia pública falla hasta que se arregla, y las instancias propias también.

### Cuándo no vale la pena

Si lo que quieres es un programa en tu equipo, no es esto: es una web. Y para un uso intensivo, un
descargador de terminal de este racimo te dará más control y menos esperas.
"""

GUIA["jeffvli/feishin"] = """
### Para qué sirve

Reproductor de escritorio para servidores de música autoalojados: se conecta a uno que ya tengas —de los que
hablan el protocolo habitual o Jellyfin— y da una interfaz moderna con cola, letras, listas inteligentes y
envío de lo escuchado al servidor.

### Cómo se usa

1. Se instala la entrega `v1.17.0`, del 15 de septiembre de 2026, para Windows, macOS o Linux.
2. Al abrir, se introduce la dirección del servidor y las credenciales.
3. Se navega la biblioteca del servidor; la reproducción puede usar el motor del sistema o el del navegador,
   y se elige en ajustes.

### Lo que conviene saber antes

10.332 estrellas, GPL-3.0. Su autor lo tiene además como reemplazo de su programa anterior, que quedó
archivado. Es un cliente, no un servidor: sin uno de esos funcionando no hace nada, y eso es lo primero que
hay que tener claro antes de instalarlo.

### Cuándo no vale la pena

Si tu música está en el disco de tu ordenador, esto no la ve. Y si ya usas la web del servidor, el cliente de
escritorio añade comodidad, no contenido.
"""

GUIA["jeffvli/sonixd"] = """
### Para qué sirve

Reproductor de escritorio para servidores de música compatibles, con biblioteca, listas, cola y controles
finos. Fue durante años la opción de referencia para ese protocolo en Windows y Linux.

### Cómo se usa

Se instalaba desde la entrega `v0.15.5`, del 14 de marzo de 2023, se conectaba al servidor con su dirección y
usuario, y se navegaba la biblioteca del servidor.

### Lo que conviene saber antes

**El repositorio está archivado** y su propio texto lo dice: la aplicación se está reescribiendo entera con
otro nombre, y ese otro nombre es el programa del mismo autor que sí está vivo en este racimo. Tiene 1.907
estrellas y su última entrega es de 2023. No recibirá más cambios.

### Cuándo no vale la pena

Hoy, siempre: su sucesor hace lo mismo, se mantiene y está en este mismo racimo. Esta ficha se conserva
porque el recurso existe, está medido y hay quien todavía lo busca por su nombre viejo.
"""

GUIA["jellyfin/jellyfin"] = """
### Para qué sirve

Servidor de medios libre: organiza películas, series, música y libros, y los sirve a aplicaciones en
televisores, móviles, consolas y navegadores. En este racimo entra por la música: es uno de los servidores a
los que se conectan varios clientes de los que tienen ficha aquí.

### Cómo se usa

1. Se instala con contenedor, paquete o instalador; la entrega medida es la `v12.4`, del 26 de octubre de
   2026.
2. En el asistente se crean las bibliotecas —una de música, por ejemplo— y se apunta a sus carpetas.
3. Se instalan las aplicaciones cliente y se conectan al servidor por su dirección local o por fuera, con
   acceso remoto configurado a conciencia.

### Lo que conviene saber antes

59.028 estrellas, GPL-2.0, escrito en C#. Es grande y maduro, y eso tiene un precio: mantenerlo pide un
equipo encendido, copias de seguridad y actualizaciones con cuidado. Su catálogo se construye con tus
archivos: no trae contenido, sólo lo ordena.

### Cuándo no vale la pena

Si sólo quieres oír música en casa, hay servidores de este racimo mucho más ligeros. Jellyfin se justifica
cuando además hay vídeo y varios aparatos en la casa.
"""

GUIA["kawaiiDango/pano-scrobbler"] = """
### Para qué sirve

Programa que **anota lo que escuchas** en un servicio de estadísticas musicales, para Windows, Linux y
Android. Toma lo que suena en el reproductor del sistema y lo envía, con corrección de nombres por reglas,
gráficas de lo escuchado y presencia en el chat.

### Cómo se usa

1. Se instala la entrega `447`, del 6 de octubre de 2026.
2. Se conecta la cuenta del servicio en ajustes y se autoriza.
3. En escritorio se activa el modo que lee el reproductor del sistema; en Android se concede el permiso de
   notificaciones, que es de donde saca qué suena.

### Lo que conviene saber antes

2.344 estrellas, GPL-3.0, y desarrollo activo. Su punto delicado son las reglas de corrección: si tu
reproductor informa mal el artista, el programa anota mal, y hay que escribir reglas a mano para arreglarlo.
En Android, además, el ahorro de batería del sistema puede desconectar el servicio.

### Cuándo no vale la pena

Si no llevas estadísticas de lo que escuchas, no hay nada que anotar. Y si usas un servidor de música, muchos
ya envían esas estadísticas por su cuenta.
"""

GUIA["koel/koel"] = """
### Para qué sirve

Servidor de música por web, escrito en PHP y pensado para instalar en un alojamiento normal: sube tu
colección, la ordena por artista y álbum, y la reproduce desde el navegador con listas y búsqueda.

### Cómo se usa

1. Se despliega en un servidor con PHP y base de datos; la entrega medida es la `v9.15.0`, del 28 de
   septiembre de 2026.
2. Se ejecuta su orden de inicialización, se crea el usuario administrador y se apunta a la carpeta de música.
3. Se lanza la exploración y, cuando termina, la biblioteca aparece en la web y en sus aplicaciones.

### Lo que conviene saber antes

17.334 estrellas, licencia MIT, once años de proyecto y entregas regulares. Es de los pocos servidores de
este racimo que corre en alojamiento compartido sin contenedores, y esa es su ventaja práctica. Su límite es
que la reproducción es sobre todo por web: no habla el protocolo de los clientes de música móviles.

### Cuándo no vale la pena

Si quieres escuchar en el teléfono con una aplicación de verdad y descargas sin conexión, necesitas otro
servidor. Koel es para escuchar en el navegador, en cualquier parte, sin instalar nada.
"""

GUIA["librespot-org/librespot"] = """
### Para qué sirve

Biblioteca en Rust que implementa el protocolo del reproductor de Spotify: sirve para construir un cliente
propio, para montar un aparato que aparezca como dispositivo en la aplicación oficial, o para entender cómo
funciona ese protocolo por dentro.

### Cómo se usa

1. Se compila con las herramientas de Rust, o se instala el paquete de tu distribución; la entrega medida es
   la `v0.8.0`, del 10 de noviembre de 2025.
2. Trae una orden de ejemplo que arranca como dispositivo: se le dan credenciales y una salida de audio.
3. Para integrarlo en un programa propio se usa como biblioteca y se controlan sus eventos desde el código.

### Lo que conviene saber antes

7.369 estrellas, MIT. Su propio texto lo dice sin ambigüedad: **sólo funciona con cuentas de pago**, y no
habrá soporte para las gratuitas. Eso no es un detalle, es la premisa del proyecto. Como biblioteca es muy
buena; como programa para el usuario final, no está pensada.

### Cuándo no vale la pena

Si no programas y no tienes cuenta de pago, no hay nada que hacer con esto. Para el caso de «aparato que
aparece en la aplicación oficial» hay un programa ya hecho en este racimo, y es más corto de instalar.
"""

GUIA["maxrave-dev/SimpMusic"] = """
### Para qué sirve

Aplicación de música multiplataforma —Android y ahora también escritorio— que usa un servicio de música como
fuente: busca, reproduce, hace listas y descarga. Trae letras sincronizadas y una interfaz cuidada, y su
proyecto presume de funcionar sin cuenta.

### Cómo se usa

1. Se instala la entrega `v2.5.0`, del 1 de noviembre de 2026.
2. Se busca por canción, artista o lista; todo se reproduce en continuo.
3. Las descargas se activan por elemento y quedan disponibles sin conexión.

### Lo que conviene saber antes

12.797 estrellas, GPL-3.0 y entregas muy seguidas: es de los más vivos de su familia en este racimo. No tiene
catálogo propio: depende de un servicio ajeno, así que su continuidad no la decide su equipo. Y conviene
saber que su texto de presentación mezcla la aplicación con notas técnicas del desarrollo, que no sirven para
decidir si instalarla.

### Cuándo no vale la pena

Si quieres escuchar tu propia biblioteca, esto no la ve. Y si el servicio cambia sus reglas, la aplicación
puede dejar de funcionar aunque siga publicando versiones.
"""

GUIA["metabrainz/listenbrainz-server"] = """
### Para qué sirve

Servidor del proyecto ListenBrainz: guarda el historial de lo que escuchas y lo convierte en estadísticas e
recomendaciones, con los datos publicados en abierto. Aquí está el código del servidor, no una aplicación
para el usuario.

### Cómo se usa

1. Para usarlo, lo normal es **no instalarlo**: el proyecto ofrece su instancia pública y basta con conectar
   un programa que envíe lo escuchado.
2. Para montarlo, se despliega con contenedores y una base de datos; la entrega medida es la
   `v-2026-10-28.0`, del 28 de octubre de 2026.
3. Una vez arriba, los clientes se conectan con un testigo de usuario y le envían cada escucha.

### Lo que conviene saber antes

1.052 estrellas y GPL-2.0. Es infraestructura, no aplicación: pesa, necesita base de datos y su instalación
es un trabajo de administración. Su valor es el contrario del de los servicios comerciales: los datos son
tuyos y además se publican para que cualquiera los analice.

### Cuándo no vale la pena

Montarlo por gusto, casi nunca: para llevar tus propias estadísticas basta la instancia pública. Se justifica
si quieres los datos en casa o si investigas con ellos.
"""

GUIA["metabrainz/musicbrainz-server"] = """
### Para qué sirve

El código del servidor de la base de datos musical abierta más usada del ecosistema libre: artistas, discos,
pistas, sellos y relaciones entre ellos, con todo editado por voluntarios y publicado sin restricciones.

### Cómo se usa

1. Casi nadie lo instala: se usa la instancia pública, y los programas de etiquetado consultan su interfaz de
   datos. Este repositorio es el del servidor.
2. Para montarlo hace falta una base de datos grande, un servidor de búsqueda y horas de preparación.
3. Para consultarlo desde un programa propio basta su interfaz pública, que no requiere instalación.

### Lo que conviene saber antes

1.112 estrellas y está escrito en Perl, con una base de datos que ocupa mucho más que el programa. **No tiene
entregas publicadas** en GitHub y **GitHub no le reconoce la licencia**. Es la fuente que hace posible que
`Picard` o `beets` identifiquen discos enteros sin que nadie teclee nada.

### Cuándo no vale la pena

Instalarlo, para casi cualquier persona: hay un servicio público con los mismos datos. Esta ficha está para
que se sepa de dónde vienen los datos que usan los demás programas del racimo.
"""

GUIA["metabrainz/picard"] = """
### Para qué sirve

Etiquetador oficial de la base de datos abierta: abre tus archivos, calcula una huella del audio, busca el
disco al que pertenecen y **escribe las etiquetas correctas** —título, artista, álbum, año, carátula— en
todos los archivos de una vez. También ordena y renombra según un patrón.

### Cómo se usa

1. Se instala desde la entrega `release-3.0.4`, del 1 de noviembre de 2026, para Windows, macOS y Linux.
2. Se arrastran los archivos o la carpeta; el programa agrupa por disco y consulta la base de datos.
3. Se revisa lo que propone —a veces hay varias ediciones del mismo disco—, se elige y se guarda.
4. En opciones se define el patrón de nombres y qué etiquetas se escriben.

### Lo que conviene saber antes

5.350 estrellas, GPL-2.0, y entrega de este mes. Es la puerta de entrada al etiquetado automático para quien
no quiere terminal. Su límite es el de la base de datos: lo que no esté catalogado allí, hay que escribirlo a
mano.

### Cuándo no vale la pena

Si vas a ordenar miles de discos y no te importa la terminal, `beets` hace el trabajo en bloque. Picard
brilla con doscientos discos y paciencia.
"""

GUIA["mopidy/mopidy"] = """
### Para qué sirve

Servidor de música escrito en Python, pensado para ser **extensible**: reproduce archivos locales, radio por
internet y fuentes que se añaden con extensiones, y se controla desde cualquier cliente compatible con el
protocolo del reproductor de siempre.

### Cómo se usa

1. Se instala con `pip` o desde el gestor de paquetes de la distribución; la entrega medida es la `v4.0.5`,
   del 16 de octubre de 2026.
2. Se escribe un archivo de configuración con las fuentes activadas y el modo de control.
3. Se arranca el servicio y se conecta un cliente —web o móvil— para buscar y encolar.

### Lo que conviene saber antes

8.610 estrellas, Apache-2.0, nacido en 2009. Su fuerza son las extensiones; su pega, que cada extensión trae
sus propias dependencias y a veces se rompen entre versiones. Y hay que tener claro qué es: un servidor que
suena en el equipo donde corre, no un servicio de música.

### Cuándo no vale la pena

Si sólo quieres oír música en el ordenador, un reproductor con ventana es más corto. Mopidy se elige cuando
quieres mezclar fuentes distintas en una sola cola controlada desde el móvil.
"""

GUIA["namidaco/namida"] = """
### Para qué sirve

Reproductor de música y vídeo para Android escrito en Flutter, con una ambición poco común: además de la
biblioteca local, busca y reproduce vídeo de un servicio conocido, con letras, cola, temas y edición de
etiquetas dentro de la misma aplicación.

### Cómo se usa

1. Se instala la APK de la entrega `v7.1.2`, del 19 de septiembre de 2026.
2. Se elige la carpeta de música local; el programa indexa y muestra pestañas por álbum, artista y carpeta.
3. Para el vídeo, se busca desde la propia aplicación y se reproduce o se descarga.

### Lo que conviene saber antes

6.788 estrellas y **GitHub no le reconoce la licencia**, así que si vas a reutilizar su código mira el
archivo antes. Su versión va por la 7 y las entregas son regulares. Al juntar música local con vídeo de un
servicio ajeno, es más frágil que un reproductor puro: cuando ese servicio cambia, la parte de vídeo es la
que se rompe.

### Cuándo no vale la pena

Si lo que quieres es sólo tu música, `Auxio` o `RetroMusicPlayer` hacen eso con menos piezas y menos
sorpresas. Namida se elige por tener las dos cosas en un solo sitio.
"""

GUIA["navidrome/navidrome"] = """
### Para qué sirve

Servidor de música autoalojado, ligero y con interfaz web: indexa tu colección, la sirve por el protocolo
habitual y permite escuchar desde cualquier sitio con decenas de clientes ya hechos, para móvil y escritorio.

### Cómo se usa

1. Se instala con un solo contenedor o con el binario; la entrega medida es la `v0.64.2`, del 24 de septiembre
   de 2026.
2. Se apunta a la carpeta de música con un archivo de configuración o variables de entorno; indexa solo.
3. Se conecta un cliente con la dirección y el usuario, o se usa la web para comprobar que responde.

### Lo que conviene saber antes

24.535 estrellas, GPL-3.0, escrito en Go: un solo archivo ejecutable y muy poco consumo, que es justo lo que
otros servidores de este racimo no ofrecen. Su versión sigue por debajo de la 1.0, así que hay cambios entre
entregas que conviene leer. No tiene aplicación propia: vive de los clientes compatibles.

### Cuándo no vale la pena

Si escuchas sólo en el equipo donde tienes la música, sobra. Y si tu red no sale de casa, un reproductor
local hace lo mismo sin montar nada.
"""

GUIA["nukeop/nuclear"] = """
### Para qué sirve

Reproductor de escritorio que **busca música por su cuenta**: se escribe un artista o un tema y el programa
consulta servicios públicos para encontrar el audio y reproducirlo, con listas, cola y scrobbling.

### Cómo se usa

1. Se instala la entrega `player@1.54.1`, del 4 de noviembre de 2026.
2. Se busca en la caja superior; los resultados se añaden a la cola.
3. Las listas se guardan en local y se pueden enviar a un servicio de estadísticas.

### Lo que conviene saber antes

18.878 estrellas y AGPL-3.0, con entrega de esta misma semana. Aquí no se enlaza ninguna de las fuentes que
usa, y conviene decirlo claro: la condición legal de lo que reproduce depende de esos servicios y de tu país,
no del programa. El programa, en sí, es un reproductor con una capa de búsqueda.

### Cuándo no vale la pena

Si tienes tu música en local o pagas un servicio con su aplicación, esto añade incertidumbre. Se elige por
la búsqueda inmediata, a sabiendas de lo que ello implica.
"""

GUIA["owntone/owntone-server"] = """
### Para qué sirve

Servidor de audio que reparte el sonido por la casa: envía lo que suena a altavoces AirPlay 1 y 2, a
Chromecast y al equipo donde corre, con varios destinos a la vez y sincronizados. Lee archivos locales, radio
por internet y alguna fuente conectada.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución o se compila; la entrega medida es la `29.3`, del
   22 de julio de 2026.
2. Se configura la carpeta de música y los nombres de los aparatos de la red.
3. Se controla por su interfaz web o desde un cliente compatible; los altavoces aparecen como destinos.

### Lo que conviene saber antes

2.585 estrellas, GPL-2.0, escrito en C y con una configuración por archivo. Funciona muy bien en Linux y en
una Raspberry Pi, y es más exigente en otros sistemas. Al ser un servidor de red, su calidad depende de tu
red: con cable va mejor que con wifi.

### Cuándo no vale la pena

Si sólo escuchas en un aparato, no hay nada que repartir. Y si tus altavoces no hablan ninguno de esos
protocolos, esto no los va a hacer compatibles.
"""

GUIA["quodlibet/quodlibet"] = """
### Para qué sirve

Reproductor y gestor de biblioteca para Linux, Windows y macOS: ordenar, buscar con consultas escritas,
etiquetar en bloque, editar patrones de nombre y reproducir. Su motor de búsqueda es lo que lo distingue de un
reproductor corriente: se le pueden pedir cosas como «discos de 1998 que tengan menos de diez temas».

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución; la entrega medida es la `release-4.7.1`, del 31
   de mayo de 2025.
2. La primera vez se apunta a la carpeta de música y se deja indexar.
3. Se busca con la barra superior, y las vistas de álbum, artista o explorador de archivos se cambian con las
   pestañas.

### Lo que conviene saber antes

1.771 estrellas, GPL-2.0 y escrito en Python. Su entrega es de **mayo de 2025**, aunque el repositorio recibe
cambios en octubre de 2026. Es un programa de escritorio clásico: teclado, atajos y configuración por
ventanas, sin nada de nube.

### Cuándo no vale la pena

Si no vas a usar la búsqueda por consultas ni el etiquetado en bloque, un reproductor más simple basta. Y en
Windows su instalación es menos cómoda que en Linux.
"""

GUIA["rmcrackan/Libation"] = """
### Para qué sirve

Programa de escritorio para **descargar y ordenar los audiolibros comprados en Audible**: entra en la cuenta,
baja los archivos, quita la protección del archivo y los deja en una carpeta con nombres legibles, además de
mantener una copia de la biblioteca y del historial.

### Cómo se usa

1. Se instala la entrega `v14.2.5`, del 27 de octubre de 2026, en Windows, macOS o Linux.
2. Se conecta la cuenta del servicio; el programa lista lo comprado.
3. Se elige qué bajar y el formato; los archivos quedan en la carpeta configurada.

### Lo que conviene saber antes

6.401 estrellas, GPL-3.0, escrito en C#. Su función incluye **retirar la protección del archivo**, algo
legalmente distinto según el país: en algunos sitios es válido para uso propio sobre lo que has comprado y en
otros no. Aquí se describe lo que el programa hace; la decisión y la responsabilidad son de quien lo use.

### Cuándo no vale la pena

Si tus audiolibros no vienen de esa tienda, no sirve. Y si te vale escuchar dentro de la aplicación oficial,
no hay nada que liberar.
"""

GUIA["snapcast/snapcast"] = """
### Para qué sirve

Sistema de audio **multisala sincronizado**: un servidor toma el sonido de un reproductor y lo reparte a
varios clientes —Raspberry Pi, ordenadores, móviles— de modo que todos suenan a la vez y sin eco entre
habitaciones.

### Cómo se usa

1. Se instala el servidor en el equipo que tenga la música y un cliente en cada aparato que vaya a sonar; la
   entrega medida es la `v0.35.0`, del 10 de marzo de 2026.
2. Se configura el servidor para que tome la entrada de audio del reproductor que uses.
3. Los clientes se conectan solos por la red; desde una aplicación de control se ajusta el volumen de cada uno
   y el retardo, que es lo que corrige la diferencia entre aparatos.

### Lo que conviene saber antes

8.044 estrellas, GPL-3.0. **No es un reproductor**: sin una fuente de audio no hace nada, y eso hay que
entenderlo antes de instalarlo. En redes wifi inestables el retardo hay que ajustarlo a mano, y el resultado
nunca es tan fino como con cable.

### Cuándo no vale la pena

Con un solo altavoz o con dos aparatos que ya suenan juntos, esto es complicación sin premio. Se justifica en
una casa con varias habitaciones y cable donde se pueda.
"""

GUIA["strawberrymusicplayer/strawberry"] = """
### Para qué sirve

Reproductor y organizador de colecciones para quien cuida el archivo: lee FLAC, ALAC y demás formatos sin
pérdida, escribe etiquetas, muestra información técnica del archivo, convierte y ordena. Nació como
continuación de un reproductor clásico y conserva su forma de trabajar.

### Cómo se usa

1. Se instala desde la entrega `1.2.31`, del 2 de octubre de 2026, o desde el gestor de paquetes.
2. Se añaden las carpetas; en ajustes se decide qué formatos entran y cómo se nombran los archivos.
3. Se reproduce, se encola y se editan etiquetas desde el propio programa.

### Lo que conviene saber antes

4.059 estrellas, GPL-3.0, escrito en C++ con Qt. Es de los pocos de este racimo que piensa en el **archivo**
—calidad, formatos, etiquetas— y no en el servicio. Trae además transcodificación para reproductores
portátiles antiguos, cosa rara hoy.

### Cuándo no vale la pena

Si tu música está en un servicio y no en archivos, no hay nada que ordenar. Y si sólo quieres darle al play a
unos mp3, es más programa del que necesitas.
"""

GUIA["supersonic-app/supersonic"] = """
### Para qué sirve

Cliente de escritorio ligero para servidores de música autoalojados: se conecta a uno compatible con el
protocolo habitual o a Jellyfin y ofrece biblioteca, cola, letras, listas y descarga para oír sin conexión.
Está escrito en Go y se nota en lo poco que pesa.

### Cómo se usa

1. Se instala la entrega `v0.22.1`, del 9 de agosto de 2026, para Windows, macOS o Linux.
2. Al abrir, se introduce la dirección del servidor y las credenciales.
3. Se navega la biblioteca remota; se puede marcar música para tenerla en el equipo y escucharla sin red.

### Lo que conviene saber antes

2.416 estrellas, GPL-3.0, versión `0.22` y desarrollo activo. Su ventaja frente a otros clientes del racimo es
el peso: arranca rápido y no lleva un navegador dentro. Su límite, el de todos: sin servidor no hay música.

### Cuándo no vale la pena

Si no tienes servidor montado, no sirve de nada. Y si ya usas la web del servidor, esto añade comodidad de
escritorio y descarga local, nada más.
"""

GUIA["taglib/taglib"] = """
### Para qué sirve

Biblioteca en C++ para **leer y escribir metadatos** de audio: etiquetas, carátulas, propiedades técnicas del
archivo. Es la pieza que hay debajo de muchos reproductores y etiquetadores, incluidos varios de este racimo.

### Cómo se usa

1. Normalmente se instala como dependencia del programa que la usa, o se compila con `cmake`; la entrega
   medida es la `v2.3.2`, del 5 de septiembre de 2026.
2. Desde código se abre el archivo, se leen o escriben las etiquetas y se guarda.
3. Las herramientas de ejemplo que trae permiten ver y cambiar etiquetas desde la terminal.

### Lo que conviene saber antes

1.467 estrellas, LGPL-2.1, quince años de historia. Su límite es el que declara su propio texto: cubre
contenedores y etiquetas conocidos, no cualquier formato exótico. Si escribes un programa que toca etiquetas,
usar esto te ahorra implementar cinco formatos a mano.

### Cuándo no vale la pena

Si no programas, no hay nada que hacer aquí: usa `Picard` o `easytag`. Esta ficha existe porque es la pieza
que sostiene a los demás.
"""

GUIA["team-spotube/spotube"] = """
### Para qué sirve

Aplicación de música multiplataforma que **separa las dos cosas que un servicio junta**: toma los datos de
tus listas de un servicio y el audio de otra fuente, con la idea de que la aplicación sea sólo la capa de
control. Trae además complementos de la comunidad.

### Cómo se usa

1. Se instala la entrega `v6.0.0-beta.0`, del 30 de octubre de 2026.
2. Se conecta la cuenta de donde vienen las listas y se elige la fuente de audio.
3. Se navega y se reproduce; las descargas se marcan desde el menú de cada lista.

### Lo que conviene saber antes

50.610 estrellas, AGPL-3.0, y una etiqueta que dice **beta**: la versión 6 todavía se está probando. Su
planteamiento depende de que las dos mitades —datos y audio— sigan disponibles, y ninguna de las dos es suya.
Cuando una cambia, la aplicación falla de formas que el usuario no puede arreglar.

### Cuándo no vale la pena

Si quieres algo que simplemente suene, hay programas en este racimo con menos piezas móviles. Spotube se
elige por su idea, no por su estabilidad.
"""

GUIA["vfsfitvnm/ViMusic"] = """
### Para qué sirve

Fue el cliente de música de Android que puso de moda la interfaz limpia para escuchar desde un servicio sin
cuenta y con descarga. Ligero, sin publicidad y con buen manejo de listas y cola.

### Cómo se usa

Se instalaba desde la entrega `v0.5.4`, del 4 de noviembre de 2022, y se usaba sin configurar nada: buscar,
reproducir, descargar.

### Lo que conviene saber antes

**El repositorio está archivado desde julio de 2024** y su última entrega es de 2022: no habrá más cambios.
Tiene 9.468 estrellas y GPL-3.0, y de él salieron varios derivados, alguno con ficha en este mismo racimo.
Instalarlo hoy en un Android actual puede fallar por permisos o por cambios del servicio.

### Cuándo no vale la pena

Para uso nuevo, no: usa uno de sus derivados vivos. Esta ficha se conserva porque el recurso existió, se
midió y mucha gente lo busca todavía por su nombre.
"""

GUIA["xiph/Icecast-Server"] = """
### Para qué sirve

Servidor de **radiodifusión por internet**: recibe un flujo de audio de un programa emisor y lo reparte a
tantos oyentes como aguante el equipo, en varios formatos. Es la pieza clásica para montar una radio propia o
para retransmitir una señal interna.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución. Este repositorio es **un espejo**: los fallos se
   reportan en GitLab y aquí no hay entregas.
2. Se configura el punto de montaje, la contraseña de emisión y los límites de oyentes.
3. Se conecta un programa emisor con esas credenciales y se comprueba desde la página de estado del servidor.

### Lo que conviene saber antes

557 estrellas, GPL-2.0, con cambios en agosto de 2026. Es infraestructura con veinte años encima: fiable y
sin sorpresas si se configura bien, y expuesta a abuso si se deja abierta, porque cualquiera con la
contraseña emite. Ojo con el ancho de banda: cada oyente consume lo suyo.

### Cuándo no vale la pena

Para escuchar tu música en casa no hace falta: esto es para emitir a otros. Y si sólo quieres oír una radio,
eres oyente, no servidor.
"""

GUIA["y20k/escapepod"] = """
### Para qué sirve

Fue un reproductor de pódcast para Android, pequeño y sin adornos: suscripciones, descarga, cola y
reproducción. Su código sigue disponible como referencia para quien quiera ver cómo se hace un cliente de
pódcast sencillo.

### Cómo se usa

Se instalaba desde la entrega `v1.1.0`, del 12 de abril de 2022, se añadían fuentes por su dirección y se
escuchaba.

### Lo que conviene saber antes

**El repositorio está archivado** desde julio de 2022 y no habrá más versiones. Tiene 124 estrellas y licencia
MIT, lo cual lo hace cómodo de leer y reutilizar. Su último cambio es de hace más de cuatro años, así que no
esperes que aguante los cambios de Android de estos años.

### Cuándo no vale la pena

Para escuchar pódcast hoy, no. Está aquí como pieza histórica y como código de ejemplo, y la ficha lo dice en
lugar de presentarlo como una opción viva.
"""

GUIA["yt-dlp/yt-dlp"] = """
### Para qué sirve

Descargador de audio y vídeo desde la línea de órdenes, con soporte de miles de sitios. En este racimo entra
por lo suyo de audio: sacar el sonido de cualquier dirección en el formato que quieras, con etiquetas y
carátula puestas si se lo pides.

### Cómo se usa

1. Se instala con `pip install yt-dlp`, desde el gestor de paquetes o bajando el binario de la entrega
   `2026.10.26`, del 26 de octubre de 2026.
2. Sólo el sonido, en el formato de más calidad disponible y convertido: `yt-dlp -x --audio-format opus <dirección>`.
3. Con `--embed-thumbnail` y `--embed-metadata` se añaden carátula y etiquetas al archivo.
4. Con `-f bestaudio` se elige directamente la pista de audio sin tocar el vídeo.

### Lo que conviene saber antes

205.397 estrellas, licencia Unlicense, entrega de hace diez días y cambios casi diarios: es el proyecto que
marca el ritmo de todo el ecosistema. Su ritmo es también su problema: las opciones cambian y lo que leíste
hace un año puede no valer. Su lista de sitios la mantiene la comunidad, y los sitios se defienden.

### Cuándo no vale la pena

Para una canción suelta, cualquier web hace el trabajo. `yt-dlp` se elige cuando repites, cuando quieres el
audio tal cual —sin recomprimir— o cuando quieres automatizar. Y siempre: descarga lo que tengas derecho a
descargar.
"""

GUIA["z-huang/InnerTune"] = """
### Para qué sirve

Cliente de música para Android con interfaz Material 3, pensado para escuchar desde un servicio sin cuenta,
con descarga, letras y listas. Fue la base de la que salieron varios derivados de este racimo.

### Cómo se usa

1. Se instala la APK de la entrega `v0.5.10`, del 1 de septiembre de 2024.
2. Se busca por canción o artista y se reproduce; no hace falta cuenta.
3. Lo que quieras guardar se marca para descarga y queda disponible sin conexión.

### Lo que conviene saber antes

6.139 estrellas, GPL-3.0, pero **su última entrega es de septiembre de 2024** y su último cambio, de noviembre
de 2025: medio proyecto parado. Su propio ecosistema ya lo sustituye por derivados con ficha en este racimo.
Además es un cliente de un servicio ajeno, así que no controla nada de lo que pasa al otro lado.

### Cuándo no vale la pena

Para uso nuevo, no: usa uno de sus derivados, que siguen publicando. Sigue sirviendo como referencia de
código y como opción si ya lo tienes instalado y te funciona.
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
