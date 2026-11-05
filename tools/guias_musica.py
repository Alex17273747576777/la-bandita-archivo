#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_musica.py · las guías escritas a mano del racimo «clientes-de-musica» (27 recursos)."""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "clientes-de-musica"

GUIA = {}

GUIA["Clash-Projects/LastWave-Desktop"] = """
### Para qué sirve

Reproductor de música de escritorio pensado para archivos sin pérdida, con generación de listas por reglas
—por tempo, por año, por parecido—, letras sincronizadas en tiempo real y envío de lo escuchado a un servicio
de estadísticas. Es la versión de ordenador del mismo proyecto que tiene aplicación de Android.

### Cómo se usa

1. Se instala la entrega `v2.0.1`, del 4 de noviembre de 2026.
2. Se eligen las carpetas de música; el programa las indexa y lee los metadatos de los archivos.
3. Las listas se crean solas según las reglas que actives, o a mano; las letras se buscan por pista.

### Lo que conviene saber antes

938 estrellas y **sin licencia declarada**: GitHub no le reconoce ninguna, así que si quieres reutilizar su
código, pregunta antes. El proyecto nació el 10 de septiembre de 2026 —dos meses— y aunque publica versiones
casi a diario, su texto promete bastante para su edad. La parte de estadísticas necesita cuenta en un servicio
ajeno.

### Cuándo no vale la pena

Si tu música está en un servicio y no en archivos, no hay nada que ordenar. Y si sólo quieres darle al play
a cuatro discos, la aplicación de fábrica del sistema hace eso sin instalar nada.
"""

GUIA["Clash-Projects/LastWave-Native"] = """
### Para qué sirve

Cliente de música para Android que toma el catálogo de un servicio de vídeo conocido, con una interfaz
cuidada, generador de listas por reglas, letras sincronizadas y envío de lo escuchado a un servicio de
estadísticas. Es el hermano de móvil del reproductor de escritorio de la misma casa.

### Cómo se usa

1. Se instala la APK de la entrega `5.0.0`, del 30 de octubre de 2026.
2. Se abre sin cuenta; la búsqueda va contra el catálogo del servicio, no contra una biblioteca propia.
3. Las descargas se marcan por pista o por lista y quedan disponibles sin conexión.

### Lo que conviene saber antes

2.523 estrellas, GPL-3.0 y entregas de esta semana. Nació el 30 de julio de 2026: tres meses. Al depender de
un servicio ajeno, cuando ese servicio cambia algo, el programa falla de formas que su autor no controla. El
envío de estadísticas es opcional, pero si lo activas, tu historial de escucha sale del teléfono.

### Cuándo no vale la pena

Si tienes tu música en archivos, aquí no la verás: este cliente vive de un catálogo que no es suyo. Y si ya
pagas el servicio y su aplicación te sirve, esto es la misma música con otra piel.
"""

GUIA["EchoMusicApp/Echo-Music"] = """
### Para qué sirve

Cliente de música para Android sobre el catálogo de un servicio de vídeo: escucha sin anuncios, listas,
búsqueda y descarga para oír sin conexión, con una interfaz que sigue el sistema de diseño de moda.

### Cómo se usa

1. Se instala la APK de la entrega `v1.4.4`, del 23 de octubre de 2026.
2. Se busca por canción o artista y se reproduce; no pide cuenta.
3. En el menú de cada elemento aparece la opción de descargar; lo bajado queda en su pantalla.

### Lo que conviene saber antes

2.295 estrellas, GPL-3.0, creado el 15 de agosto de 2026: menos de tres meses. Su propio texto se presenta
como experiencia «premium» sin anuncios, y esa palabra la pone su autor, no una medición. Como todos los de
esta familia, no tiene catálogo propio: si el servicio cambia sus reglas, el programa deja de funcionar.

### Cuándo no vale la pena

Para escuchar tu propia biblioteca no sirve. Y si buscas algo con historial largo y arreglos probados, tres
meses de vida son pocos.
"""

GUIA["HemantKArya/BloomeeTunes"] = """
### Para qué sirve

Reproductor multiplataforma con una idea distinta a la de sus vecinos: en vez de un catálogo fijo, admite
**complementos** que añaden fuentes, y a la vez reproduce lo que tengas en el teléfono. Está escrito en Flutter
por fuera y Rust por dentro.

### Cómo se usa

1. Se instala desde la entrega `v3.1.0`, del 21 de octubre de 2026; hay paquete para Android, Windows y Linux.
2. Se añaden las fuentes como complementos, una por una, o se apunta a la carpeta de música local.
3. Se navega por las pestañas y se encola; lo que venga de una fuente se puede descargar.

### Lo que conviene saber antes

2.301 estrellas, GPL-2.0, y nació el 7 de diciembre de 2023: casi tres años, de los pocos con recorrido. Su
arquitectura de complementos es su fuerza y su desgracia: cuando una fuente cambia, el complemento se rompe y
hay que esperar a que alguien lo arregle. Nunca ha superado la versión 3.

### Cuándo no vale la pena

Si quieres instalar y escuchar sin configurar nada, esto pide montar fuentes a mano. Y si sólo usas archivos
locales, hay reproductores más directos en este mismo racimo.
"""

GUIA["LUC4N3X/Levyra-deepsound"] = """
### Para qué sirve

Reproductor de música para Android y Windows que junta dos mundos: lo que escuchas en un servicio y lo que ya
tienes en archivos, en la misma biblioteca y con la misma cola. Su propia descripción lo resume mejor que
cualquier resumen: hecho para escuchar, no para iniciar sesión.

### Cómo se usa

1. Se instala la entrega `v3.0.7`, del 3 de noviembre de 2026.
2. Se elige la carpeta de música local y, si quieres, se conecta el servicio.
3. La búsqueda recorre las dos fuentes a la vez; las descargas se marcan por lista o por canción.

### Lo que conviene saber antes

2.084 estrellas, GPL-3.0, creado el 28 de junio de 2026 y con entregas de esta semana. Tiene versión de
escritorio además de la de Android, cosa poco habitual en esta familia. La mitad del servicio depende de un
tercero; la mitad local no.

### Cuándo no vale la pena

Si no mezclas las dos cosas, hay reproductores más simples para cada una. Y si tu prioridad es la estabilidad
a años, el proyecto aún no los tiene.
"""

GUIA["Lelonio/Square"] = """
### Para qué sirve

Cliente de Android que **te deja elegir el servicio en el primer arranque** —uno de música o uno de vídeo— y
cambiar después en los ajustes, con la misma interfaz para los dos: inicio, búsqueda, biblioteca y reproductor.
Añade efectos de audio y control remoto del reproductor en otros aparatos.

### Cómo se usa

1. Se instala la APK de la entrega `v2.8.0`, del 3 de noviembre de 2026.
2. Al abrir por primera vez se elige el servicio; se puede cambiar luego en ajustes.
3. Se conecta la cuenta de ese servicio y se navega; los efectos de audio están en el reproductor.

### Lo que conviene saber antes

485 estrellas, GPL-3.0, creado el 6 de agosto de 2026. Es un cliente no oficial de dos servicios a la vez, y su
propio texto lo dice: «no oficial». Eso significa que puede dejar de funcionar si cualquiera de los dos cambia
sus condiciones, y que pedir soporte al servicio no sirve de nada.

### Cuándo no vale la pena

Si usas sólo uno de los dos servicios, hay clientes más maduros para cada uno. Y si te preocupa que una
aplicación de este tipo desaparezca, tres meses de vida es el dato que manda.
"""

GUIA["MuwMx/YumaPlayer"] = """
### Para qué sirve

Reproductor de Android que mezcla tres cosas en una: el descubrimiento y la interfaz de un servicio de música,
la biblioteca de un servicio de vídeo, y reproducción de archivos sin pérdida cuando la fuente los tiene. Es
la variante más ambiciosa de su familia y también la más frágil.

### Cómo se usa

1. Se instala la APK de la entrega `v1.2.0-RC.1`, del 17 de octubre de 2026.
2. Se conectan las cuentas o se navega sin ellas, según lo que permita cada servicio.
3. Se busca, se encola y se marca lo que quieras descargar.

### Lo que conviene saber antes

1.120 estrellas, GPL-3.0, creado el 24 de julio de 2026 y con etiqueta `RC` —candidata, todavía no final—. Su
propio texto se declara «independiente», y eso importa: no tiene relación con ninguno de los dos servicios que
usa, así que ninguno le va a dar permiso ni soporte.

### Cuándo no vale la pena

Con dos servicios ajenos y cuatro meses de vida, es un programa para mirar, no para depender de él. Si lo que
quieres es escuchar tu música sin sobresaltos, hay opciones más aburridas y más firmes.
"""

GUIA["OpenSelena/omniget"] = """
### Para qué sirve

Gestor de descargas de escritorio que, además de vídeo y música de muchos sitios, está pensado para **cursos**:
descarga lecciones completas de plataformas de formación en línea y las ordena. Está hecho con Rust y una
interfaz web empaquetada.

### Cómo se usa

1. Se instala la entrega `v0.14.0`, del 31 de octubre de 2026.
2. Se pega la dirección del curso o del vídeo; el programa detecta de dónde viene y propone qué bajar.
3. Se elige calidad y carpeta; las descargas se encolan y se reanudan si se cortan.

### Lo que conviene saber antes

3.978 estrellas, GPL-3.0, creado el 8 de julio de 2026. Su lista de etiquetas del repositorio está llena de
sinónimos de descargador de vídeo: el proyecto se presenta por lo que hace, no por una función concreta. Ahí
está también su frontera: bajar un curso que has pagado es una cosa y bajar uno que no, otra; el programa no
distingue.

### Cuándo no vale la pena

Si sólo descargas vídeos sueltos, un descargador de terminal hace lo mismo con menos peso. Omniget se elige
cuando quieres ordenar series completas o cursos con su estructura de carpetas.
"""

GUIA["Rigellute/spotify-tui"] = """
### Para qué sirve

Cliente de música para la terminal, escrito en Rust: se conecta a tu cuenta de un servicio de música y permite
buscar, navegar listas, ver el reproductor actual y controlar la reproducción sin salir de la consola. Fue,
durante años, la forma de usar ese servicio desde un servidor sin escritorio.

### Cómo se usa

1. Se instala con el gestor de paquetes de tu sistema o con las herramientas de Rust; la entrega medida es la
`v0.25.0`, del 24 de agosto de 2021.
2. Se crea una credencial de aplicación en el panel del servicio y se pega en el archivo de configuración.
3. Se abre `spt` en la terminal, se elige el aparato de reproducción y se navega con el teclado.

### Lo que conviene saber antes

19.416 estrellas, MIT, y **su último cambio es de abril de 2024**: dos años y medio sin tocarlo. Para un cliente
de un servicio que cambia sus reglas a menudo, eso es mucho. La autenticación exige crear credenciales propias
en el panel del servicio, y ese trámite ha cambiado varias veces desde que el programa se escribió.

### Cuándo no vale la pena

Hoy, en la mayoría de los casos: hay clientes de terminal con el mismo enfoque que siguen publicando. Esta
ficha existe porque el programa existe, se midió y mucha gente lo busca todavía por su nombre.
"""

GUIA["SimoHypers/limusic"] = """
### Para qué sirve

Cliente de escritorio para un servicio de música, nativo y sin navegador dentro: interfaz propia, búsqueda,
listas, descargas y letras, construido con Rust y una capa web ligera. Su autor presume —y es comprobable en el
archivo de compilación— de no arrastrar Electron.

### Cómo se usa

1. Se instala la entrega `v1.3.0`, del 19 de octubre de 2026, para Windows, macOS o Linux.
2. Se busca por canción, artista o lista; el reproductor vive en una ventana propia.
3. Lo descargado queda en la carpeta configurada, con los metadatos que traiga la fuente.

### Lo que conviene saber antes

1.809 estrellas, GPL-3.0, creado el 3 de julio de 2026. Cuatro meses y entregas regulares. Al ser nativo pesa
menos que sus competidores hechos con navegador, y a cambio pierde algo de compatibilidad en equipos antiguos.
Como todos, depende de un servicio ajeno.

### Cuándo no vale la pena

Si no te importa que la aplicación ocupe 300 MB, este ahorro no te dice nada. Y si tu música está en archivos
locales, hay reproductores de escritorio que no dependen de nadie.
"""

GUIA["TeamNewPipe/NewPipeExtractor"] = """
### Para qué sirve

No es una aplicación: es la **biblioteca** que hay debajo de un conocido cliente libre de vídeo, y sirve para
sacar de un sitio de vídeos lo que hace falta para reproducirlo sin su aplicación oficial: direcciones, pistas
de audio, subtítulos y metadatos. En este racimo entra por el audio.

### Cómo se usa

1. Se incluye como dependencia en un proyecto de Java o Android; la entrega medida es la `v0.26.5`, del 15 de
agosto de 2026.
2. Desde código se pide la información de un enlace y se reciben los objetos con las pistas disponibles.
3. Hay una aplicación de prueba en el repositorio para ver qué devuelve la biblioteca sin escribir código.

### Lo que conviene saber antes

2.039 estrellas, GPL-3.0, y desarrollo vivo: su último cambio es de noviembre de 2026. La versión importa
mucho: la biblioteca se publica y los clientes se atan a una versión concreta, porque los cambios internos
rompen. Si programas un cliente, esto te ahorra la parte más frágil y más sujeta a cambios.

### Cuándo no vale la pena

Si no programas, no hay nada que hacer aquí: usa uno de los clientes que ya la llevan dentro. Esta ficha está
para entender de dónde salen y por qué se rompen a la vez varios programas cuando el sitio cambia.
"""

GUIA["aome510/spotify-player"] = """
### Para qué sirve

Cliente de un servicio de música para la terminal, con la ambición de tener todo lo que tiene el cliente
oficial: búsqueda, biblioteca, listas, cola, control de aparatos y letras. Es la alternativa viva al cliente de
terminal que quedó parado.

### Cómo se usa

1. Se instala con las herramientas de Rust, desde el gestor de paquetes o con el binario de la entrega
   `v0.25.1`, del 9 de septiembre de 2026.
2. La primera vez pide autorización: abre el navegador, se concede el permiso y se guarda el testigo.
3. Se maneja con el teclado; su documentación trae un mapa de atajos que conviene imprimir o tener al lado.

### Lo que conviene saber antes

7.302 estrellas, MIT, y última entrega de septiembre. La autenticación es la parte que más preguntas genera en
su propio proyecto: el testigo caduca y hay que volver a autorizar cada cierto tiempo, y su documentación lo
explica con detalle. Necesita cuenta de pago del servicio, como casi todo lo de esta familia.

### Cuándo no vale la pena

Si no vives en la terminal, la curva de atajos no compensa. Y si no tienes cuenta de pago, no funciona: no hay
plan para cuentas gratuitas.
"""

GUIA["devgianlu/go-librespot"] = """
### Para qué sirve

Programa que hace que un equipo aparezca como **altavoz** dentro de un servicio de música: se monta en una
Raspberry Pi o en un ordenador sin pantalla, y desde la aplicación oficial del teléfono se le manda la música.
Está escrito en Go, que en este caso significa un solo binario sin dependencias.

### Cómo se usa

1. Se descarga el binario de la entrega `v0.10.5`, del 16 de octubre de 2026, o se compila.
2. Se escribe un archivo de configuración con el nombre del aparato y la salida de audio.
3. Se arranca como servicio; en la aplicación oficial aparece como un dispositivo más de la red.

### Lo que conviene saber antes

386 estrellas, GPL-3.0 y entregas de este mes. Admite varias salidas de audio y, a diferencia de otras piezas
parecidas, su autor lo documenta con ejemplos. Necesita cuenta de pago del servicio. Y hay que tener claro qué
es: no reproduce tu propia biblioteca, reproduce lo que le manden desde la aplicación oficial.

### Cuándo no vale la pena

Si no tienes un equipo dedicado sin pantalla, no aporta nada frente a usar el teléfono. Y en una red inestable,
el aparato aparece y desaparece de la lista.
"""

GUIA["dubeyKartikay/lazyspotify"] = """
### Para qué sirve

Cliente de terminal para un servicio de música, pensado para **macOS y Linux**, con una pieza aparte que hace
de puente para que el aparato aparezca como reproductor. La idea es la misma de sus vecinos: escuchar sin salir
de la consola.

### Cómo se usa

1. Se instala la entrega `v0.5.2`, del 15 de octubre de 2026.
2. Hace falta cuenta de pago y un llavero del sistema funcionando, que es donde guarda el testigo.
3. Se arranca el acompañante y luego el cliente; el aparato aparece en la aplicación oficial.

### Lo que conviene saber antes

445 estrellas, MIT, creado el 18 de marzo de 2026: ocho meses. Su propia documentación lista tres requisitos
estrictos —cuenta de pago, llavero del sistema y el acompañante modificado—, y quien no los cumpla se queda
fuera sin un mensaje claro. Ese acompañante es una pieza separada que hay que instalar aparte.

### Cuándo no vale la pena

Es el más exigente de su familia en instalación. Si buscas un cliente de terminal que funcione a la primera,
hay otros dos en este racimo con menos requisitos.
"""

GUIA["gokadzev/Musify"] = """
### Para qué sirve

Reproductor de música para Android con biblioteca local, búsqueda en línea, descargas y reproducción en
segundo plano, con una interfaz que sigue el sistema de diseño actual y varios idiomas, entre ellos el español.

### Cómo se usa

1. Se instala la APK de la entrega `10.6.0`, del 23 de octubre de 2026.
2. La primera vez se concede permiso al almacenamiento y se elige qué carpetas entran en la biblioteca.
3. La búsqueda en línea trae resultados del servicio que uses; lo que quieras guardar se descarga.

### Lo que conviene saber antes

4.403 estrellas, GPL-3.0, y nació el 5 de diciembre de 2021: es de los veteranos de este racimo y ha
sobrevivido a varias roturas del servicio en el que se apoya. Su descripción y su texto de presentación son la
misma frase, así que de ahí no se saca más información: lo que hay es lo que se ve al usarlo.

### Cuándo no vale la pena

Si sólo quieres tu música local, la mitad de la aplicación sobra. Y si el servicio del que toma la música
cambia sus reglas, la parte en línea se apaga y queda el reproductor local.
"""

GUIA["hrkfdn/ncspot"] = """
### Para qué sirve

Cliente de terminal para un servicio de música, con la mirada puesta en los reproductores de consola clásicos:
pantalla única, teclas de siempre, cola y biblioteca. Funciona en Linux, macOS y Windows, y usa por debajo la
biblioteca libre que implementa el protocolo del servicio.

### Cómo se usa

1. Se instala desde el gestor de paquetes de tu distribución o con las herramientas de Rust; la entrega medida
   es la `v1.5.0`, del 1 de octubre de 2026.
2. Se arranca y se sigue el enlace de autorización que muestra; hay soporte para teclas multimedia.
3. Se navega con el teclado: buscar, añadir a la cola, cambiar de lista.

### Lo que conviene saber antes

6.806 estrellas, licencia BSD de dos cláusulas —permisiva y poco habitual—, con ocho años de historia y
entregas este año. Necesita cuenta de pago. Su ventaja sobre otros clientes de terminal es que compila en casi
cualquier sistema y su configuración cabe en un archivo de texto.

### Cuándo no vale la pena

Si no tienes cuenta de pago, no hay nada que hacer. Y si prefieres ver carátulas y mover cosas con el ratón,
esto no es para ti: aquí todo es texto y teclas.
"""

GUIA["jpochyla/psst"] = """
### Para qué sirve

Cliente de escritorio para un servicio de música con **interfaz gráfica nativa**, sin navegador dentro: rápido
de arrancar, ligero y con lo esencial —búsqueda, listas, cola y reproducción—. Su autor lo empezó justamente
para tener eso sin la pesadez de las aplicaciones hechas con tecnologías web.

### Cómo se usa

1. Se instala la entrega `rolling`, del 28 de junio de 2025, o se compila, que es lo que su documentación
   recomienda para tener lo último.
2. Se inicia sesión con la cuenta del servicio; las credenciales se guardan en el llavero del sistema.
3. Se navega por la biblioteca y se reproduce desde la ventana principal.

### Lo que conviene saber antes

9.506 estrellas, MIT, y su propio texto lo dice sin rodeos: **está en desarrollo temprano, le faltan funciones,
estabilidad y cosas en general**. Tiene cinco años de vida y su última entrega es de junio de 2025, con cambios
en agosto de 2026: va despacio. Necesita cuenta de pago.

### Cuándo no vale la pena

Si quieres un cliente de escritorio completo y terminado, este no lo es y su autor lo admite. Se elige por su
ligereza, a sabiendas de que le falta la mitad de lo que un cliente maduro tiene.
"""

GUIA["kota-zo/myspoti"] = """
### Para qué sirve

Cliente de Android para un servicio de música, construido con las herramientas modernas de interfaz, que se
presenta como la forma de escuchar **con la cuenta gratuita sin anuncios**, con descargas para oír sin conexión
y el resumen anual del servicio incluido.

### Cómo se usa

1. Se instala la APK de la entrega `v2.3.0`, del 1 de noviembre de 2026.
2. Se inicia sesión con la cuenta propia del servicio; el programa lee listas y biblioteca.
3. Las descargas se marcan por lista o por canción y quedan disponibles sin red.

### Lo que conviene saber antes

1.330 estrellas, GPL-3.0 y creado el 14 de octubre de 2026: **tres semanas**. Su propuesta —bloquear los
anuncios de una cuenta gratuita— va contra las condiciones del servicio, y eso hay que decirlo con todas las
letras: lo que hace el programa es técnicamente posible y comercialmente prohibido. Cada quien decide, pero la
cuenta que se juega es la suya.

### Cuándo no vale la pena

Si pagas el servicio, no necesitas esto. Y si tu cuenta te importa —listas de años, historial, recomendaciones—
puedes perderla por usar un cliente que rompe las condiciones.
"""

GUIA["kraxarn/spotify-qt"] = """
### Para qué sirve

Cliente de escritorio para un servicio de música hecho con Qt: ventana ligera, interfaz nativa, biblioteca,
listas y reproductor. Es una de las pocas opciones de esta familia que se siente como un programa de escritorio
y no como una página web en una caja.

### Cómo se usa

1. Se instala la entrega `v4.0.4`, del 1 de mayo de 2026, o el paquete de tu distribución.
2. Se conecta la cuenta; para ciertas funciones hace falta crear credenciales propias en el panel del servicio.
3. Se navega la biblioteca y se controla la reproducción desde la ventana o desde la bandeja del sistema.

### Lo que conviene saber antes

1.496 estrellas, GPL-3.0, seis años de proyecto y cambios de octubre de 2026. Es de los pocos que funciona
igual en Windows, macOS y Linux con la misma interfaz. La parte de credenciales es la que más confunde a quien
lo instala la primera vez.

### Cuándo no vale la pena

Si escuchas en el teléfono y no en el ordenador, no hay nada que hacer. Y si quieres funciones avanzadas de
descubrimiento, las aplicaciones oficiales siguen teniendo más.
"""

GUIA["kushagrasinghx/BitChord"] = """
### Para qué sirve

Cliente de música para Android que toma el catálogo de un servicio de vídeo y lo presenta con una estética
prestada de otro servicio de música: limpia, con carátulas grandes y sin adornos. Reproduce, busca, hace listas
y descarga.

### Cómo se usa

1. Se instala la APK de la entrega `v1.9`, del 30 de octubre de 2026.
2. Se busca por canción, artista o lista; no pide cuenta.
3. Las descargas se marcan desde el menú de cada elemento.

### Lo que conviene saber antes

5.726 estrellas en **tres meses** de vida —creado el 11 de agosto de 2026—, GPL-3.0, y su propio texto trae un
aviso importante: **no tiene relación con el servicio del que toma la música ni con su empresa**, y el uso corre
por cuenta de quien lo hace. Ese aviso no es cortesía legal: es la advertencia de que nadie te cubre si algo va
mal.

### Cuándo no vale la pena

Si lo que quieres es tu música local, no la ve. Y con tres meses de vida y sin catálogo propio, es un programa
para probar, no para montar tu biblioteca encima.
"""

GUIA["libre-tube/LibreTube"] = """
### Para qué sirve

Cliente alternativo de un sitio de vídeo para Android, hecho para ver y escuchar sin cuenta, sin anuncios y sin
el rastreo de la aplicación oficial. En este racimo entra por el audio: permite suscribirse a canales, escuchar
sólo el sonido y descargar para oír sin conexión.

### Cómo se usa

1. Se instala la APK de la entrega `v32.1`, del 20 de agosto de 2026.
2. Se abre sin cuenta; se pueden importar las suscripciones desde un archivo o desde la cuenta del sitio.
3. En el reproductor se elige la calidad y el modo de audio; las descargas se marcan por elemento.

### Lo que conviene saber antes

12.945 estrellas, GPL-3.0, y cinco años de historia. Su proyecto pide expresamente que los fallos y las
peticiones se manden por su repositorio y no por otras plataformas, una señal de que la bandeja de entrada se
les desborda. Se apoya en la biblioteca de extracción que también está en este racimo: cuando esa cambia, aquí
se nota.

### Cuándo no vale la pena

Si quieres ver vídeo con la máxima calidad y funciones modernas, la aplicación oficial está mejor hecha para
eso. LibreTube se elige por privacidad y por escuchar sin anuncios, aceptando que la interfaz va un paso por
detrás.
"""

GUIA["lladlam/MeloX-Android"] = """
### Para qué sirve

Cliente de música para Android que se presenta como derivado de otro proyecto y con estética tomada de un
servicio de música comercial: catálogo de un servicio de vídeo, interfaz clara, listas y descargas, más algunas
funciones propias sobre la base.

### Cómo se usa

1. Se instala la APK de la entrega `0.7.1`, del 27 de octubre de 2026.
2. Se busca y se reproduce sin cuenta; la biblioteca se arma con listas propias.
3. Las descargas se marcan por lista, y lo bajado queda en una pantalla aparte.

### Lo que conviene saber antes

288 estrellas, GPL-3.0, creado el 9 de agosto de 2026. Su texto avisa de que las ediciones de Windows y Linux
están «en verificación final» y pide estrellas para desbloquear su publicación: es una forma de hacer campaña
que conviene conocer antes de fiarse de las cifras. La versión `0.7` dice por sí sola en qué punto está.

### Cuándo no vale la pena

Hoy, para uso serio: es una versión temprana de un derivado de otro proyecto, con una plataforma resuelta y dos
anunciadas. Si buscas algo estable, mira el original del que sale.
"""

GUIA["missuo/kumone"] = """
### Para qué sirve

Reproductor de música nativo para **macOS e iOS**, escrito en SwiftUI, que reproduce la biblioteca del aparato y
permite buscar y escuchar en línea desde un catálogo que el propio programa arma. Su nombre significa «sonido de
nube» y su interfaz está pensada para el ecosistema de Apple.

### Cómo se usa

1. Se instala desde la entrega `v0.3.28`, del 4 de noviembre de 2026.
2. Se concede permiso a la biblioteca de música del sistema, si quieres verla dentro.
3. Se busca por canción o artista y se encola; las listas se guardan en el propio aparato.

### Lo que conviene saber antes

1.286 estrellas, LGPL-3.0, creado el 16 de agosto de 2026. Su texto trae un aviso explícito: **no tiene relación
con el servicio chino del que toma el nombre ni contiene sus dominios ni sus direcciones**. Ese cuidado por
desmarcarse dice mucho de cómo funciona esta familia de programas, y conviene leerlo antes de instalarlo en un
aparato con la cuenta de Apple configurada.

### Cuándo no vale la pena

Sólo existe para Apple: fuera de ese ecosistema no hay nada. Y si quieres escuchar tu música local sin
sorpresas, la aplicación de fábrica ya lo hace.
"""

GUIA["rootscripts/riff"] = """
### Para qué sirve

Reproductor de música con dos bibliotecas —un servicio de vídeo y otro de sonido— en la misma aplicación, con
visualizaciones hechas con sombreadores en tiempo real y una interfaz muy cuidada. Se instala desde el
navegador o como programa de escritorio.

### Cómo se usa

1. Se abre su versión web o se instala la entrega `v44.2.0`, del 4 de noviembre de 2026.
2. Se busca por canción o artista; los resultados de las dos fuentes aparecen juntos.
3. Se encola y se reproduce; las visualizaciones se activan en el reproductor.

### Lo que conviene saber antes

825 estrellas, MIT, creado el 4 de octubre de 2026: **un mes**. Su texto avisa de que el proyecto lo mantiene
sólo su equipo y que **no acepta contribuciones externas**: los fallos se reportan, los cambios no. Eso no lo
hace peor, pero sí más dependiente de una sola voluntad.

### Cuándo no vale la pena

Para escuchar música con calma y sin distracciones, las visualizaciones sobran. Y con un mes de vida y sin
contribuciones abiertas, es un programa que puede quedarse quieto cualquier día.
"""

GUIA["sigma67/ytmusicapi"] = """
### Para qué sirve

Biblioteca de Python que habla con la interfaz no oficial de un servicio de música: buscar, leer listas,
obtener la información de un álbum o de un artista y gestionar la biblioteca de una cuenta. Es la pieza que
usan muchos de los clientes y programas de este racimo por debajo.

### Cómo se usa

1. Se instala con `pip install ytmusicapi`; la entrega medida es la `1.12.3`, del 16 de septiembre de 2026.
2. Para leer datos públicos basta con crear el objeto y llamar a sus métodos.
3. Para lo que requiere cuenta hay que generar un archivo de autenticación con su orden de configuración.

### Lo que conviene saber antes

3.103 estrellas, MIT, y mantenimiento activo con cambios de noviembre de 2026. Es una biblioteca, no un
programa: sin escribir código no hace nada. Y su objeto de trabajo es una interfaz no documentada, así que los
cambios del servicio la rompen con cierta regularidad.

### Cuándo no vale la pena

Si no programas, no hay nada que hacer aquí. Su utilidad es para quien quiere automatizar algo —una lista, un
archivo, un informe— sin montar una aplicación entera.
"""

GUIA["sonorahq/sonora"] = """
### Para qué sirve

Cliente de música de escritorio nativo que reúne en una sola ventana la reproducción de **archivos locales** y
el catálogo de varios servicios, con la misma biblioteca, la misma cola y los mismos controles. Su propia
presentación lo resume: transmite desde tus servicios y reproduce tus archivos, todo en una aplicación nativa.

### Cómo se usa

1. Se instala la entrega `v0.47.0`, del 2 de noviembre de 2026.
2. Se apunta a la carpeta de música y se conectan las cuentas de los servicios que quieras.
3. La búsqueda recorre ambos mundos; la cola mezcla canciones de cualquier origen.

### Lo que conviene saber antes

2.643 estrellas, GPL-3.0, creado el 3 de agosto de 2026 y con versiones casi semanales: la `0.47` en tres meses
da idea del ritmo. Es de los pocos de este racimo con esa mezcla tan limpia entre local y servicios, y también
de los más jóvenes.

### Cuándo no vale la pena

Con tres meses y medio y una versión `0.x`, es un programa en construcción. Si tu biblioteca local es lo único
que te importa, hay reproductores con años encima en este mismo racimo.
"""

GUIA["spotipy-dev/spotipy"] = """
### Para qué sirve

Biblioteca de Python para la interfaz pública de un servicio de música: consultar artistas, álbumes, listas,
gestionar la reproducción y automatizar cualquier cosa que esa interfaz permita. Es la vía más corta para
escribir un programa de pocas líneas que haga algo con tu cuenta.

### Cómo se usa

1. Se instala con `pip install spotipy`; la entrega medida es la `2.26.0`, del 3 de marzo de 2026.
2. Se crea una aplicación en el panel del servicio y se obtienen dos claves.
3. Desde código se instancia el cliente con esas claves y se llaman sus métodos; para acciones de cuenta hace
   falta el flujo de autorización.

### Lo que conviene saber antes

5.486 estrellas, MIT, doce años de proyecto y cambios de junio de 2026. Necesita que el usuario cree sus propias
credenciales en el servicio, y eso ha cambiado de sitio varias veces. Los límites de peticiones del servicio son
reales y hay que respetarlos.

### Cuándo no vale la pena

Si no escribes código, no sirve. Y si sólo quieres escuchar, un cliente de este racimo te ahorra todo el
trámite de credenciales.
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
