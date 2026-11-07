#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_radio.py · las guías escritas a mano del racimo «radio-y-directo» (29 recursos)."""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "radio-y-directo"

GUIA = {}

GUIA["AzuraCast/AzuraCast"] = """
### Para qué sirve

Suite completa para montar una emisora de radio por internet en un servidor: panel de control, gestión de la
música, programación de parrilla, estadísticas de oyentes y todo lo necesario para emitir en continuo. Su propio
texto la presenta como una emisora «en una caja», y eso es literal: con un contenedor queda funcionando.

### Cómo se usa

1. Se despliega con contenedores; el proyecto **no publica entregas etiquetadas**, así que se instala desde su
   imagen o desde su instalador.
2. En el asistente se crea la emisora, se sube la música y se define la parrilla.
3. Se conecta un programa emisor externo o se deja que la propia suite emita en continuo.
4. El panel muestra oyentes, histórico y salud del servidor.

### Lo que conviene saber antes

4.085 estrellas, AGPL-3.0, escrito en PHP y con cambios de hoy mismo. Es infraestructura de verdad: pide un
servidor, base de datos y algo de administración. Y hay un límite que no se puede olvidar: emitir consume ancho
de banda por cada oyente, así que el coste crece con la audiencia.

### Cuándo no vale la pena

Si sólo quieres oír radio, esto es del lado del que emite. Y si vas a emitir para veinte amigos una vez al mes,
un servicio ya montado te ahorra la administración entera.
"""

GUIA["Davidona/StreamVault-IPTV"] = """
### Para qué sirve

Reproductor de televisión por internet pensado primero para **televisores y Android TV**: interfaz manejable con
mando a distancia, guía de programación y reproducción con el motor del sistema. Está hecho en Kotlin con las
herramientas modernas de interfaz de Android.

### Cómo se usa

1. Se instala la APK de la entrega `v1.2.4`, del 2 de noviembre de 2026, en el televisor o en el aparato de TV.
2. Se añaden las fuentes que tengas derecho a usar; el reproductor no trae ninguna.
3. Se navega por la guía con el mando: canales, favoritos y lo que se está emitiendo.

### Lo que conviene saber antes

1.004 estrellas y **sin licencia declarada**: GitHub no le reconoce ninguna, así que si quieres reutilizar su
código, pregunta antes. Nació el 21 de marzo de 2026 y se actualizó esta semana. Aquí **no se enlaza ninguna
lista, ningún portal ni ninguna fuente de contenido**: el programa se describe, el catálogo lo pone quien lo use.

### Cuándo no vale la pena

Si no tienes televisor Android ni mando, su diseño no aporta nada frente a un reproductor de teléfono. Y si
nunca has configurado una fuente de televisión por internet, la primera media hora es cuesta arriba.
"""

GUIA["Ruby184/epg-tools"] = """
### Para qué sirve

Juego de herramientas para la **guía de programación**: recoge los datos de una o varias fuentes, los guarda por
días con caché, y los une y valida en un archivo único que cualquier reproductor pueda leer. Es fontanería para
quien mantiene una lista grande y no quiere volver a descargarla entera cada vez.

### Cómo se usa

1. Se instala con las herramientas de Node; la entrega medida es la `v0.9.0`, del 16 de octubre de 2026.
2. Se escriben las fuentes en su configuración, una por una.
3. Se ejecuta el recogedor; los días ya descargados se reutilizan y sólo se piden los que faltan.
4. El resultado se sirve al reproductor como una guía más.

### Lo que conviene saber antes

**Una estrella** y licencia MIT: es una herramienta recién nacida, de agosto de 2026, hecha por una persona para
su propio problema. Lo interesante no es su tamaño sino su idea: la caché por día y por canal, que es lo que
hace viable una guía de dos semanas sin descargar un archivo enorme cada mañana.

### Cuándo no vale la pena

Si tienes cuatro canales, el reproductor se apaña con su propia descarga. Esto se justifica con listas grandes o
con fuentes que tardan en responder.
"""

GUIA["TheJoeFin/Traydio"] = """
### Para qué sirve

Reproductor de radio por internet para Windows que vive **en la bandeja del sistema**: no tiene ventana grande,
se abre desde el icono y deja sonando la emisora mientras trabajas. Su nombre anterior era Trdo y cambió en la
versión 2.0.

### Cómo se usa

1. Se instala la entrega `v2.2.3`, del 4 de noviembre de 2026, en Windows.
2. Se busca la emisora por nombre o se pega su dirección; las favoritas quedan guardadas.
3. Se controla desde la bandeja: play, pausa, siguiente y volumen.

### Lo que conviene saber antes

204 estrellas, escrito en C#, creado el 25 de septiembre de 2025 y actualizado hoy mismo. Es pequeño y hace una
sola cosa, que es exactamente lo que promete. Su límite es el del sistema: sólo Windows, y depende de las
libertades que dé la bandeja de notificaciones en cada versión.

### Cuándo no vale la pena

En Linux o macOS no existe. Y si quieres buscar emisoras por país, idioma y etiqueta, hay programas de este
racimo con catálogo propio; aquí buscas por nombre o pegas la dirección.
"""

GUIA["Woodic-Way/WoodicIPTV"] = """
### Para qué sirve

Reproductor de televisión y radio por internet para Android con interfaz Material, pensado para listas en formato
de texto: canales de televisión y emisoras de radio en la misma aplicación.

### Cómo se usa

1. Se instala la entrega `v2.0`, del 30 de julio de 2026.
2. Se añade la fuente de canales que tengas derecho a usar.
3. Se navega por la lista y se reproduce; los canales de radio aparecen separados de los de vídeo.

### Lo que conviene saber antes

**5 estrellas** y **sin licencia declarada**, creado y publicado el mismo día: el 30 de julio de 2026, sin un solo
cambio desde entonces. Es, con los datos en la mano, el recurso menos sostenido de este racimo. Aquí no se enlaza
ninguna lista ni ninguna fuente: sólo se describe el programa, y la advertencia va delante porque el proyecto no
tiene con qué responder si algo falla.

### Cuándo no vale la pena

Hoy, casi siempre. En este mismo racimo hay reproductores con años, licencia y mantenimiento; este existe en el
catálogo porque se midió, no porque se recomiende.
"""

GUIA["armanmaurya/InternetRadio"] = """
### Para qué sirve

Aplicación de Android para descubrir y escuchar emisoras de radio de todo el mundo: catálogo por países e
idiomas, favoritas, historial y búsqueda. Usa una base pública de emisoras, así que no hay que pegar direcciones
a mano.

### Cómo se usa

1. Se instala la APK de la entrega `v0.9.0`, del 22 de octubre de 2026.
2. Se elige país o idioma y se navega; al tocar una emisora, suena.
3. Las que te gusten se marcan como favoritas y quedan en la pantalla de inicio.

### Lo que conviene saber antes

180 estrellas, GPL-3.0, creado el 12 de junio de 2026, versión `0.9`: un paso antes de la primera. La calidad
depende de la base pública de emisoras, que es mantenida por voluntarios: hay estaciones que aparecen y ya no
emiten, y nadie las quita el mismo día.

### Cuándo no vale la pena

Si escuchas dos emisoras concretas, guárdalas en el navegador y evítate la aplicación. Y si quieres grabar o
programar, aquí no hay nada de eso.
"""

GUIA["bilipp/Lume"] = """
### Para qué sirve

Reproductor de televisión por internet para **Apple**, con interfaz nativa en SwiftUI: navega, busca y reproduce
listas de canales y portales, con guía de programación, metadatos de películas y series, y reproducción en
directo.

### Cómo se usa

1. Se instala la entrega `v3.0.0`, del 1 de noviembre de 2026.
2. Se añaden las fuentes que tengas derecho a usar: el programa no trae ninguna.
3. Se navega por el catálogo: directo, películas y series, con la guía al lado.

### Lo que conviene saber antes

176 estrellas, AGPL-3.0, creado el 9 de abril de 2026 y con entrega mayor —la 3.0— esta semana. Es de los pocos
de su clase para el ecosistema de Apple, y eso lo hace útil a quien tiene un televisor o un aparato de esa casa.
Aquí **no se enlaza ninguna fuente ni ninguna lista**: se describe el reproductor y la responsabilidad sobre el
contenido queda donde corresponde.

### Cuándo no vale la pena

Fuera de Apple no existe. Y si no tienes fuentes propias con derecho de uso, la aplicación se queda vacía: es
un reproductor, no un catálogo.
"""

GUIA["bsogulcan/another-iptv-player"] = """
### Para qué sirve

Reproductor de televisión por internet ligero y multiplataforma: lee listas de canales y las reproduce con una
interfaz sencilla, sin adornos ni funciones de más. Existe para iOS, Android y escritorio.

### Cómo se usa

1. Se instala la entrega `ios-v2.4.0`, del 1 de agosto de 2026.
2. Se añade la lista de canales que tengas derecho a usar.
3. Se navega por la lista y se elige canal; la reproducción usa el motor del sistema.

### Lo que conviene saber antes

157 estrellas, MIT, creado el 10 de junio de 2025 y con cambios de finales de octubre de 2026. Su nombre lo dice
todo: es «otro» reproductor más, y su ventaja es la sencillez y la licencia permisiva. Su punto flojo es que no
hay guía de programación elaborada ni metadatos: es una lista y un reproductor.

### Cuándo no vale la pena

Si quieres guía, metadatos y ordenar películas y series, aquí no están. Se elige cuando lo único que hace falta
es abrir una lista y verla.
"""

GUIA["clubanderson/clubTivi"] = """
### Para qué sirve

Reproductor de televisión por internet multiplataforma que presume de dos cosas técnicas: **cambio automático de
fuente cuando una se cae** y mapeo inteligente de la guía de programación. Reúne varias fuentes en una sola
interfaz con canales unificados.

### Cómo se usa

1. Se instala la entrega semanal `weekly-2026.43`, del 1 de noviembre de 2026.
2. Se añaden las fuentes que tengas derecho a usar; el programa no trae ninguna.
3. Se navega por los canales unificados; si una fuente falla, el reproductor prueba la siguiente.
4. Se puede controlar desde el móvil como mando a distancia de la pantalla.

### Lo que conviene saber antes

108 estrellas, Apache-2.0, creado el 21 de febrero de 2026, con entregas semanales. Su texto presume de «no
almacenar nunca» —eso es lo que dice su autor, no una medición—. Y su descripción menciona servicios de descarga
y fuentes de pago: aquí se nombran **sin enlazar ninguna**, y se advierte de que combinar fuentes de pago con
otras gratuitas puede acabar en un catálogo que no es lo que uno cree.

### Cuándo no vale la pena

Si tienes una sola fuente estable, el cambio automático no se nota. Y si te preocupa de dónde sale lo que ves,
una aplicación que junta muchas fuentes hace esa pregunta más difícil, no más fácil.
"""

GUIA["dereferencex/prysm"] = """
### Para qué sirve

Reproductor de televisión por internet para Android y Android TV hecho con herramientas web empaquetadas:
interfaz moderna, guía de programación y reproducción de listas de canales.

### Cómo se usa

1. Se instala la entrega `v1.5.0`, del 15 de octubre de 2026.
2. Se añade la lista que tengas derecho a usar.
3. Se navega por la guía y se reproduce; la interfaz se maneja igual con dedo o con mando.

### Lo que conviene saber antes

50 estrellas, MIT, creado el 15 de febrero de 2026 y con su última entrega en octubre. El detalle técnico que
importa: al estar hecho con tecnologías web dentro de una aplicación, pesa más y consume más batería que uno
nativo, y la reproducción depende del motor que use por debajo. Aquí no se enlaza ninguna lista ni fuente.

### Cuándo no vale la pena

En un televisor con poca memoria, un reproductor nativo de este racimo va a ir mejor. Y si sólo quieres ver la
lista de casa, cualquier reproductor sencillo hace lo mismo.
"""

GUIA["deutsia/deutsia-radio"] = """
### Para qué sirve

Reproductor de radio para Android que se presenta como resistente a la censura: además de la red normal, puede
usar **redes alternativas** para alcanzar emisoras que en la red abierta no responden. Tiene interfaz Material
You y catálogo propio.

### Cómo se usa

1. Se instala la APK de la entrega `v1.8.1`, del 25 de mayo de 2026.
2. Se elige la red por la que salir, si hace falta una alternativa.
3. Se busca la emisora y se reproduce; las favoritas se guardan.

### Lo que conviene saber antes

78 estrellas, Apache-2.0, y su último cambio es de **mayo de 2026**: medio año quieto. Su propio texto declara
que se construyó con ayuda de un asistente de programación, y eso no lo hace peor, pero explica el ritmo y el
estado. Las redes alternativas que ofrece añaden latencia: la emisora puede tardar en sonar más de lo normal.

### Cuándo no vale la pena

Si tu emisora se oye por la red normal, la mitad de la aplicación sobra. Y si necesitas que arranque rápido y
nunca falle, medio año sin mantenimiento es un dato a tener en cuenta.
"""

GUIA["hyliankid14/British-Radio-Player"] = """
### Para qué sirve

Cliente no oficial de la radio pública británica y de sus pódcast: reúne más de ochenta emisoras y más de mil
programas, con metadatos del directo, favoritos y compatibilidad con el sistema de infoentretenimiento del
coche.

### Cómo se usa

1. Se instala la entrega `v2.1.4`, del 2 de noviembre de 2026.
2. Se navega por emisoras o por programas; el directo muestra qué suena en cada momento.
3. Se marcan favoritos y se descargan episodios de pódcast para oír sin conexión.

### Lo que conviene saber antes

23 estrellas y **licencia que GitHub no reconoce**: si quieres reutilizar su código, lee el archivo antes.
Creado el 30 de diciembre de 2025. Su punto fuerte es la integración con el coche y lo cuidado del directo; su
límite, que sólo sirve para un país y depende de que la emisora pública mantenga sus direcciones.

### Cuándo no vale la pena

Si no te interesa la radio británica, no hay nada que hacer aquí. Y si escuchas desde el teléfono, la aplicación
oficial de esa emisora cubre lo mismo sin depender de un tercero.
"""

GUIA["infinitel8p/Extreme-InfiniTV"] = """
### Para qué sirve

Reproductor de televisión por internet multiplataforma: lee listas de canales y portales, trae guía de
programación, permite descargar para ver sin conexión y se maneja con el mando del televisor. Tiene versión para
Windows, Linux y Android.

### Cómo se usa

1. Se instala la entrega `v1.9.0`, del 31 de agosto de 2026.
2. Se añaden las fuentes que tengas derecho a usar; el programa no incluye ninguna.
3. Se navega por la guía y se reproduce; lo que quieras ver después se descarga.

### Lo que conviene saber antes

208 estrellas, GPL-3.0, creado el 25 de agosto de 2025 y con cambios de hoy mismo aunque su última entrega es de
agosto. Es de los pocos que ofrece descarga para ver sin conexión, algo poco común en esta familia. Aquí no se
enlaza ninguna lista, ningún portal ni ninguna fuente de contenido.

### Cuándo no vale la pena

Si no vas a usar la descarga ni el mando, un reproductor más simple basta. Y si tu fuente es una sola lista
pequeña, tanta función alrededor es peso muerto.
"""

GUIA["lennylxx/webos-iptv-player"] = """
### Para qué sirve

Reproductor de televisión por internet para **televisores LG con webOS**: se instala en el propio televisor y
lee listas de canales y cuentas de portal, con guía de programación y subtítulos en línea.

### Cómo se usa

1. Se instala siguiendo las instrucciones de su repositorio —en webOS se instala por el modo de desarrollo del
   televisor—; la entrega medida es la `v1.17.0`, del 20 de octubre de 2026.
2. Se cargan las listas o cuentas que tengas derecho a usar.
3. Se navega con el mando del televisor: canales, favoritos y guía.

### Lo que conviene saber antes

145 estrellas, Apache-2.0, creado el 28 de marzo de 2026 y con entregas regulares. Es de los pocos proyectos que
ataca un televisor concreto en vez de Android en general, y eso se agradece; a cambio, el proceso de instalación
en webOS no es el de una tienda y hay que activar el modo de desarrollo del aparato.

### Cuándo no vale la pena

Si tu televisor no es LG con webOS, no sirve. Y si no quieres activar el modo de desarrollo del televisor, mejor
un aparato externo con Android.
"""

GUIA["libretime/libretime"] = """
### Para qué sirve

Plataforma para emitir radio: programación de parrilla, gestión de la biblioteca de audio, emisión automática,
estadísticas y publicación de pódcast. Nació como bifurcación mantenida por la comunidad de un proyecto anterior
y hoy es la opción libre de referencia para montar una emisora completa.

### Cómo se usa

1. Se despliega con contenedores o con el instalador de su documentación; la entrega medida es la `4.5.0`, del 16
   de julio de 2025.
2. En el panel se sube la música, se definen bloques horarios y se programa la parrilla.
3. Se conecta con el servidor de emisión que tengas y se comprueba la señal.

### Lo que conviene saber antes

938 estrellas, AGPL-3.0, escrito en PHP, con cambios de noviembre de 2026 pero **entrega de julio de 2025**: el
programa se arregla y no se publica. Es infraestructura de verdad: pide servidor, base de datos y paciencia. Su
ventaja frente a otras suites es que no obliga a un servicio de pago para empezar.

### Cuándo no vale la pena

Si vas a emitir unas horas al mes, montar una plataforma entera es desproporcionado. Y si no tienes un servidor
donde dejarla corriendo, no llegará el primer día.
"""

GUIA["meehow/receiver"] = """
### Para qué sirve

Reproductor de radio por internet para el escritorio de GNOME que, en vez de obligarte a buscar emisoras por
nombre, **trae más de treinta mil** ya organizadas por país, idioma y etiqueta, con una colección curada para
descubrir.

### Cómo se usa

1. Se instala la entrega `v0.8.0`, del 12 de julio de 2026, o el paquete de tu distribución.
2. Al abrir, se navega por las colecciones o se busca por país e idioma.
3. Se reproduce y se guardan favoritas; el historial queda en la ventana.

### Lo que conviene saber antes

51 estrellas, GPL-3.0, creado el 18 de febrero de 2026, escrito en un lenguaje poco frecuente para aplicaciones
de escritorio. Su planteamiento —catálogo primero, búsqueda después— es justo lo contrario de casi todo lo demás
de este racimo, y para quien no sabe qué poner, es una ventaja real.

### Cuándo no vale la pena

Está hecho para GNOME: fuera de ese entorno funciona, pero arrastra bibliotecas. Y si ya sabes qué emisora
quieres, la búsqueda por nombre de cualquier otro reproductor es más corta.
"""

GUIA["mewset/better-iptv"] = """
### Para qué sirve

Reproductor de televisión por internet para escritorio —Linux, Windows y macOS— con idea de «abrir y ver»:
listas de canales y cuentas de portal, guía de programación y biblioteca de series y películas, todo con una
interfaz oscura pensada para el contenido.

### Cómo se usa

1. Se instala la entrega `v3.2.2`, del 27 de octubre de 2026.
2. Se añaden las fuentes que tengas derecho a usar.
3. Se navega por la guía o por la biblioteca y se reproduce.

### Lo que conviene saber antes

71 estrellas, GPL-2.0, creado el 15 de noviembre de 2025, escrito en Rust y con entregas regulares. Al ser
nativo, arranca rápido y gasta poca memoria: es de los pocos de esta familia en escritorio que no lleva un
navegador dentro. Aquí no se enlaza ninguna lista ni ninguna cuenta.

### Cuándo no vale la pena

Si ves la televisión en el teléfono o en el televisor, para qué el ordenador. Y si sólo tienes una lista de
canales pequeña, la biblioteca de series y películas no se va a llenar nunca.
"""

GUIA["mytv-android/mytv-android"] = """
### Para qué sirve

Reproductor de televisión por internet para Android y Android TV, con tres motores de reproducción distintos
—el del sistema, uno alternativo y uno que reproduce casi cualquier cosa— para que los canales que fallan en un
motor funcionen en otro. Su interfaz sigue el estilo visual más reciente de Android.

### Cómo se usa

1. Se instala la APK de la entrega `V2.2.0.219`, del 21 de agosto de 2026.
2. Se añade la lista de canales que tengas derecho a usar.
3. Si un canal no se ve, se cambia el motor de reproducción en los ajustes de ese canal.
4. La guía de programación se carga aparte, si la fuente la trae.

### Lo que conviene saber antes

3.006 estrellas, MIT, creado el 20 de febrero de 2025. Su documentación y su comunidad están en chino; la
interfaz tiene traducción parcial. La combinación de tres motores es lo que lo hace útil con listas
desiguales, y también lo que lo hace más pesado que un reproductor simple. Aquí no se enlaza ninguna lista.

### Cuándo no vale la pena

Si tu lista es estable y se ve bien con un motor normal, los otros dos no aportan. Y si no lees chino, algunas
pantallas de configuración se hacen cuesta arriba.
"""

GUIA["nevermore23274/AetherTune"] = """
### Para qué sirve

Reproductor de radio por internet para la **terminal**, con visualización del audio en tiempo real: busca
emisoras en una base pública, las reproduce en consola y pinta el espectro mientras suena. Es una curiosidad
deliberada, y funciona.

### Cómo se usa

1. Se instala con las herramientas de Rust o desde la entrega `v0.12.0`, del 1 de octubre de 2026.
2. Se busca por nombre, país o etiqueta desde la propia terminal.
3. Se elige emisora y suena; el espectro se dibuja en la misma pantalla.

### Lo que conviene saber antes

129 estrellas, MIT, creado el 14 de marzo de 2026 y con cambios de octubre. Su descripción y su texto de
presentación son la misma frase, así que no hay más documentación que la del propio programa. Las emisoras
salen de una base mantenida por voluntarios: hay estaciones muertas que nadie retira.

### Cuándo no vale la pena

Si no vives en una terminal, no hay razón para escuchar radio ahí. Y si quieres carátulas y favoritas visuales,
este no es el sitio.
"""

GUIA["opentvproject/opentv"] = """
### Para qué sirve

Reproductor de televisión por internet para Android TV, aparatos de televisión y tablets que se presenta con una
promesa sencilla y comprobable en su texto: **sin cuenta, sin suscripción y sin servidor propio**. Se instala y
se le da una lista.

### Cómo se usa

1. Se instala la APK de la entrega `v0.11.10`, del 28 de octubre de 2026.
2. Se añade la lista de canales que tengas derecho a usar.
3. Se navega con el mando; la guía aparece si la fuente la incluye.

### Lo que conviene saber antes

146 estrellas, GPL-3.0, creado el 30 de julio de 2026, versión `0.11` y entregas frecuentes. Su propuesta de no
pedir cuenta ni montar servidor es lo contrario de casi todo lo demás de este racimo, y para mucha gente es
justo lo que busca. Aquí no se enlaza ninguna lista ni ninguna fuente.

### Cuándo no vale la pena

Si quieres funciones de grabación o de biblioteca de películas, esto no las tiene. Y con cuatro meses de vida,
la estabilidad aún se está haciendo.
"""

GUIA["renyijiu/tune-roam"] = """
### Para qué sirve

Reproductor de radio por internet para Android construido con tecnología multiplataforma, de modo que su núcleo
no depende de Android y puede reutilizarse. Toma las emisoras de una base pública y organiza por país, idioma y
etiqueta.

### Cómo se usa

1. Se instala la APK de la entrega `v0.4.0`, del 25 de octubre de 2026.
2. Se navega por países y etiquetas, o se busca por nombre.
3. Se reproduce y se guardan favoritas; el historial queda en la pantalla principal.

### Lo que conviene saber antes

**10 estrellas**, MIT, creado el **21 de octubre de 2026**: dos semanas antes de esta medición. Su
documentación está en chino y su texto avisa de que la parte de iOS es un plan, no un hecho. Es el recurso más
joven de este racimo con diferencia, y eso se nota en todo: versión `0.4`, diez estrellas y una sola persona
detrás.

### Cuándo no vale la pena

Hoy, para uso diario. Tiene sentido si te interesa cómo se escribe una aplicación de radio con núcleo
compartido, o si quieres seguir su desarrollo desde el principio.
"""

GUIA["segler-alex/RadioDroid"] = """
### Para qué sirve

Reproductor de radio por internet para Android que usa la base pública de emisoras más conocida: busca por
nombre, país, idioma y etiqueta, guarda favoritas y permite grabar lo que suena. Fue durante años la aplicación
de referencia de su categoría.

### Cómo se usa

1. Se instala la APK de la entrega `0.86`, del 28 de septiembre de 2023.
2. Se busca por país o por nombre; los resultados vienen de esa base pública.
3. Se marca favorita y se reproduce; la grabación se activa desde el menú.

### Lo que conviene saber antes

1.081 estrellas, GPL-3.0, creado en 2013 y **sin cambios desde junio de 2024**: dos años parado. Su última
entrega es de 2023, y Android ha cambiado lo suficiente desde entonces como para que los permisos y la
reproducción en segundo plano den problemas en versiones recientes.

### Cuándo no vale la pena

Hoy, para instalar de nuevo: hay reproductores de este racimo que usan la misma base de emisoras y siguen
publicando. Esta ficha se conserva porque el programa existe, se midió y mucha gente lo busca por su nombre.
"""

GUIA["shapeshed/aerial"] = """
### Para qué sirve

Reproductor de radio por internet para Android con una idea de curaduría: en vez de un buscador con miles de
emisoras, presenta colecciones hechas a mano para estados de ánimo y actividades —trabajar, cocinar, dormir—,
con carátula y datos de lo que suena.

### Cómo se usa

1. Se instala la APK de la entrega `v0.7.4`, del 7 de octubre de 2026.
2. Se elige una colección y se navega por las emisoras que la componen.
3. Se reproduce en segundo plano; los datos del tema suenan en la pantalla de bloqueo.

### Lo que conviene saber antes

165 estrellas, Apache-2.0, creado el 17 de junio de 2026 y con cambios de hoy mismo. Su apuesta por la curaduría
va contra la moda del catálogo infinito, y para quien no sabe qué poner es más cómodo; a cambio, si buscas una
emisora concreta, el camino es más largo que en otros programas.

### Cuándo no vale la pena

Si ya tienes tus tres emisoras de siempre, la curaduría no te aporta. Y si quieres buscar por país e idioma con
filtros finos, hay opciones más completas.
"""

GUIA["streamlink/streamlink"] = """
### Para qué sirve

Herramienta de terminal que toma una emisión de vídeo de un servicio y la **manda a un reproductor** que tú
elijas, sin navegador y sin anuncios. No descarga el archivo: abre el flujo y lo pasa al reproductor que tengas
instalado, que es lo que permite ver una emisión en directo con un programa ligero.

### Cómo se usa

1. Se instala con el gestor de paquetes, con `pip` o desde la entrega `8.6.3`, del 29 de octubre de 2026.
2. `streamlink <dirección> best` abre la calidad más alta en el reproductor por defecto.
3. Con `--player` se elige el reproductor y con la calidad en lugar de `best` se fija la resolución.
4. Admite varias salidas a la vez y guardar el flujo en un archivo si se le pide.

### Lo que conviene saber antes

11.896 estrellas, licencia BSD de dos cláusulas, y diez años de proyecto con entregas de este mes. Su lista de
servicios compatibles la mantiene la comunidad y cambia a menudo. No es un programa con ventana: si no tienes un
reproductor instalado, no verás nada.

### Cuándo no vale la pena

Si quieres una aplicación con botones, esto no es. Y si el servicio que te interesa no está en su lista, no hay
nada que hacer: la herramienta no adivina.
"""

GUIA["suuhm/xmltv-splitter"] = """
### Para qué sirve

Guion de Python que **filtra un archivo enorme de guía de programación** y deja sólo los canales que te
interesan, por nombre o desde una fuente remota. Sirve para que el reproductor no cargue una guía de decenas de
megas cuando sólo ves quince canales.

### Cómo se usa

1. Se ejecuta con Python; **no tiene entregas publicadas**, así que se toma el código del repositorio.
2. Se le pasa el archivo de guía y la lista de canales que quieres conservar.
3. El resultado es un archivo más pequeño que se le da al reproductor.

### Lo que conviene saber antes

**Una estrella** y licencia Apache-2.0, creado en mayo de 2025 y sin cambios desde julio de 2026. Es una
herramienta de una sola tarea, escrita para resolver el problema de alguien concreto, y su propio texto lo dice
sin adornos: ideal para servidores de televisión y programas compatibles con ese formato de guía.

### Cuándo no vale la pena

Si tu guía ya es pequeña, no hay nada que recortar. Y si no quieres tocar un archivo por línea de órdenes, esto
no es para ti.
"""

GUIA["vikindor/omnibeat"] = """
### Para qué sirve

Reproductor de radio por internet para Android pensado para emisoras modernas: las que emiten con tecnologías
recientes y no con el formato antiguo. Busca, reproduce y guarda favoritas, con una interfaz limpia.

### Cómo se usa

1. Se instala la APK de la entrega `v1.17.1`, del 4 de noviembre de 2026.
2. Se busca la emisora por nombre o se navega por categorías.
3. Se reproduce en segundo plano con controles en la notificación.

### Lo que conviene saber antes

13 estrellas, AGPL-3.0, creado el 10 de mayo de 2026 y con versiones casi semanales: la `1.17` en seis meses dice
mucho del ritmo de su autor. Su enfoque en las emisiones modernas lo hace útil donde otros fallan, y también lo
limita: hay emisoras antiguas que no va a poder abrir.

### Cuándo no vale la pena

Si tus emisoras son antiguas o emiten en un formato que este programa no contempla, no sonará nada. Y con trece
estrellas, la comunidad es una sola persona.
"""

GUIA["xyzs996/iptv-doctor"] = """
### Para qué sirve

Herramienta para **revisar y limpiar listas de canales**: comprueba qué direcciones siguen respondiendo, quita
las muertas, arregla la guía de programación y deja un archivo más sano. Es mantenimiento de listas, no
reproducción.

### Cómo se usa

1. Se abre su versión web o se ejecuta desde el repositorio; la entrega medida es la `v0.1.0`, del 20 de junio
   de 2026.
2. Se le da la lista y, si se quiere, la guía.
3. El programa prueba cada dirección, marca las que no responden y devuelve la lista limpia.

### Lo que conviene saber antes

**6 estrellas**, MIT, creado y entregado el mismo día: el 20 de junio de 2026, con cambios en noviembre. Su
utilidad es real y muy concreta: una lista de mil canales tiene siempre un tercio de direcciones muertas, y
probarlas a mano es imposible. Su versión `0.1` avisa de que aún puede cambiar todo.

### Cuándo no vale la pena

Si tu lista es de veinte canales, se revisa a mano en diez minutos. Y si no quieres que un programa haga
peticiones a todas las direcciones de tu lista, hazlo tú mismo.
"""

GUIA["yaolin-dev/OKVideoMac"] = """
### Para qué sirve

Reproductor de televisión por internet nativo para **macOS con chip de Apple**: reproduce listas de canales y
cuentas de portal, con guía, catálogo de películas y series, y compatibilidad con varios formatos de fuente muy
usados en ese ecosistema.

### Cómo se usa

1. Se instala la entrega `v0.9.2`, del 5 de noviembre de 2026, en un Mac con chip de Apple.
2. Se añaden las fuentes que tengas derecho a usar; el programa no trae ninguna.
3. Se navega por directo, películas y series; la guía aparece cuando la fuente la trae.

### Lo que conviene saber antes

119 estrellas, GPL-3.0, creado el 15 de agosto de 2026 y con entrega de hoy mismo. Sólo funciona en chips de
Apple: no hay versión para los Mac antiguos. Aquí no se enlaza ninguna lista ni ninguna cuenta, y su propio texto
menciona formatos de fuente que circulan por la red sin que su origen esté claro: eso queda del lado de quien lo
use.

### Cuándo no vale la pena

Si tu Mac no es de chip Apple, no existe para ti. Y si no tienes fuentes propias con derecho de uso, la
aplicación se queda vacía.
"""

GUIA["z0rats/freqcast"] = """
### Para qué sirve

Reproductor de radio por internet para Android que, en vez de tirar de una base de datos, **busca la emisión en
la propia página de la emisora**: se le da el nombre o la dirección del sitio y encuentra el flujo de audio que
hay dentro. Eso le permite alcanzar emisoras que no están en ningún catálogo.

### Cómo se usa

1. Se instala la APK de la entrega `v3.17.2`, del 2 de noviembre de 2026.
2. Se busca la emisora por nombre o se pega la dirección de su página.
3. El programa encuentra el flujo, lo guarda como favorita y lo reproduce.

### Lo que conviene saber antes

14 estrellas, GPL-3.0, creado el 18 de enero de 2026 y con versiones constantes. Su método tiene una ventaja
grande —no depende de ninguna base de datos de terceros— y una pega del mismo tamaño: si la página de la emisora
cambia su reproductor, la búsqueda puede dejar de encontrarlo hasta que se actualice el programa.

### Cuándo no vale la pena

Si tus emisoras están en los catálogos de siempre, otros reproductores las encuentran en un toque. Esta se
elige para las que no aparecen en ningún sitio.
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
