#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_teclados.py · las guías escritas a mano del racimo «teclados-y-dictado» (34 recursos).

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
RACIMO = "teclados-y-dictado"

GUIA = {}

GUIA["Akshayykadam/PixelBoard"] = """
### Para qué sirve

Es una **modificación del teclado de Google** que desbloquea en teléfonos de otras marcas la voz nueva del
asistente y las herramientas de redacción, con la promesa de que no hace falta root. Se instala como una
aplicación aparte y se activa como teclado.

### Cómo se usa

1. Se descarga el paquete de la entrega `1.3.3`, del 28 de octubre de 2026.
2. Se instala con el permiso de «instalar aplicaciones desconocidas» activado, que el sistema pedirá una vez.
3. Se activa en los ajustes de teclado del teléfono y se elige como método de entrada.
4. La voz del asistente necesita además el paquete de idioma correspondiente, que el programa descarga por su
   cuenta.

### Lo que conviene saber antes

Aquí hay que ser claro, porque es lo más importante de esta ficha. **El código no es de quien lo publica**: es
el teclado de Google, empaquetado de nuevo. Eso significa dos cosas. La primera, que estás instalando una
compilación hecha por una persona a la que no conoces, sobre una aplicación que **ve todo lo que escribes**.
La segunda, que la condición legal de redistribuir así un paquete ajeno no está resuelta en ningún sitio. El
proyecto nació el 17 de septiembre de 2026 y tiene 1.423 estrellas: es muy nuevo para algo que pide tanta
confianza. Si decides probarlo, no lo pongas en el teléfono donde entras a tu banco.

### Cuándo no vale la pena

Casi siempre. Si lo que quieres es dictar sin conexión y sin depender de nadie, en este mismo racimo hay
teclados con su código a la vista y sin red, y esa diferencia —código propio frente a paquete ajeno
reempaquetado— pesa más que cualquier función desbloqueada.
"""

GUIA["AnySoftKeyboard/AnySoftKeyboard"] = """
### Para qué sirve

Teclado de Android con una idea vieja y sólida: **muchos idiomas y ningún permiso de red**. Trae corrección,
predicción y diccionarios por idioma como paquetes separados, y su propio texto presume de que no tiene acceso
a internet, cosa que se puede comprobar en su manifiesto.

### Cómo se usa

1. Se instala la APK de la entrega `1.13-r2`, del 8 de septiembre de 2026.
2. Se activa como teclado y, en su asistente, se añaden los idiomas: cada uno descarga su diccionario.
3. En ajustes se decide la distribución de teclas, el tamaño, la predicción y el gesto de deslizar.

### Lo que conviene saber antes

3.393 estrellas, Apache-2.0 y catorce años de vida: es de los proyectos más veteranos de este racimo. Su
interfaz no es la más moderna —se nota que viene de otra época— y en un teléfono grande las teclas pueden
parecer pequeñas hasta que se ajustan. A cambio, no hay nada que envíe lo que escribes a ningún sitio.

### Cuándo no vale la pena

Si escribes en un solo idioma y el teclado de fábrica ya te corrige bien, no hay razón para cambiar. Tiene
sentido si escribes en varios idiomas mezclados o si no quieres un teclado con red en el teléfono.
"""

GUIA["Automattic/harper"] = """
### Para qué sirve

Corrector gramatical que funciona **sin conexión**: revisa lo que escribes y señala errores y frases torpes
mientras escribes, sin enviar el texto a ningún servidor. Se puede usar como programa de escritorio, como
extensión del navegador o dentro de tu editor de código.

### Cómo se usa

1. Se instala la entrega `v3.0.0`, del 27 de octubre de 2026, o la extensión desde la tienda del navegador.
2. En escritorio, se escribe en su ventana o se activa la revisión en las aplicaciones compatibles.
3. En el editor de código se instala como complemento y revisa comentarios y documentación.

### Lo que conviene saber antes

17.416 estrellas, Apache-2.0, escrito en Rust: rápido y con muy poco consumo. Su límite grande es el idioma:
**trabaja en inglés**, y en español no te sirve. Su autor lo presenta como alternativa a los correctores
comerciales, y esa comparación es suya, no una medición de esta ficha.

### Cuándo no vale la pena

Si escribes en español, hoy no hay nada que hacer aquí. Y si no te importa que la revisión pase por un
servicio en línea, los correctores de siempre siguen siendo más cómodos de integrar.
"""

GUIA["Batmancpu/Dictator-"] = """
### Para qué sirve

Es un paquete de instalación de un teclado de dictado por voz, **recompilado por una persona que declara no
ser programadora** y que lo dice en su propia descripción, atribuyendo el trabajo al autor original.

### Cómo se usa

Se instala el paquete de la entrega `dictator-40297638051`, del 26 de octubre de 2026, y se activa como
teclado igual que cualquier otro.

### Lo que conviene saber antes

Tiene **3 estrellas**. No es un proyecto: es la recompilación de otro. En este mismo racimo está el original
—con su código, sus autores y su historial— y aquí lo que hay es una copia de un paquete ajeno hecha por
alguien sin relación con él. Instalar un teclado es dar acceso a todo lo que escribes: la regla razonable es
descargarlo de quien lo escribe.

### Cuándo no vale la pena

Siempre. Esta entrada está en el catálogo porque el recurso existe y se midió; la guía sirve para que nadie
lo confunda con el proyecto del que sale.
"""

GUIA["BryceWG/BiBi-Keyboard"] = """
### Para qué sirve

Teclado de dictado por voz para Android construido alrededor de un motor de reconocimiento: se mantiene
pulsada la tecla, se habla y el texto aparece. Admite varios proveedores de reconocimiento, unos en la nube y
otros en el propio teléfono, y modelos locales de varios fabricantes.

### Cómo se usa

1. Se instala la APK de la entrega `v4.5.3`, del 26 de octubre de 2026.
2. En sus ajustes se elige el motor: en la nube hace falta una clave del proveedor; en local hay que
   descargar el modelo, que ocupa bastante.
3. Se activa como teclado y se pulsa la tecla de micrófono; el envío es al soltar, y se puede configurar el
   silencio para que corte solo.

### Lo que conviene saber antes

862 estrellas, Apache-2.0, y su documentación está en chino; la interfaz tiene traducción parcial al inglés.
Su propio texto dice que admite **18 motores** —doce en la nube y seis locales—, y eso es una declaración del
autor: aquí no se ha probado ninguno. Los motores en la nube implican mandar tu voz fuera; los locales,
descargar cientos de megas y depender de la potencia del teléfono.

### Cuándo no vale la pena

Si no escribes chino ni necesitas dictado, es una aplicación grande para usar una sola tecla. Y si lo que
quieres es privacidad, elige un motor local desde el principio y no configures ninguno en la nube.
"""

GUIA["Cyletix/CyIME"] = """
### Para qué sirve

Teclado chino para Android construido sobre el motor Rime, con todo lo que ese motor permite: varios métodos
de entrada —pinyin, doble pinyin, wubi, trazos, cangjie, zhuyin—, diccionarios propios, escritura a mano,
voz y reconocimiento de texto en fotos, todo hecho en el propio teléfono. Trae además un modo de subtítulos en
vivo pensado para personas con problemas de audición.

### Cómo se usa

1. Se instala la APK de la entrega `1.15.63`, publicada hoy mismo, 5 de noviembre de 2026.
2. Se activa como teclado; la primera vez tarda en preparar los diccionarios.
3. En ajustes se eligen los métodos de entrada y se añaden diccionarios o esquemas de Rime.
4. El modo de subtítulos se abre como pantalla aparte y transcribe lo que se oye por el micrófono.

### Lo que conviene saber antes

664 estrellas, GPL-3.0, y entregas casi diarias: es un proyecto en plena construcción, nacido el 22 de
septiembre de 2026. Su propio texto dice que aspira a ser un teclado de referencia entre los chinos; eso es una
aspiración del autor, no un dato. Su público es quien escribe en chino: para español el diccionario y la predicción no
están al mismo nivel.

### Cuándo no vale la pena

Si no escribes chino, la mitad del programa sobra. Y si buscas un teclado estable para años, uno con seis
semanas de vida no es la elección.
"""

GUIA["DevEmperor/DictateKeyboard"] = """
### Para qué sirve

Teclado de Android cuyo eje es el dictado: pulsas el micrófono, hablas y el texto entra donde estés
escribiendo. Admite varios motores de reconocimiento, incluido Whisper, unos en la nube y otros en el propio
teléfono, y guarda historial de lo dictado.

### Cómo se usa

1. Se instala la APK de la entrega `v6.4.0`, del 7 de octubre de 2026.
2. En ajustes se elige el motor y el modelo; para los motores en la nube se pega la clave del proveedor.
3. Se activa como teclado y se dicta; también funciona en el modo de escritura normal, con su distribución de
   teclas.

### Lo que conviene saber antes

315 estrellas, Apache-2.0, con desarrollo activo desde 2024. Es el **original** del que salen las copias que
circulan por ahí, y por eso mismo es el que conviene instalar. Su punto delicado es el de todo dictado: si
usas un motor en la nube, tu voz sale del teléfono; si usas uno local, cambias privacidad por paciencia,
porque el modelo pesa y el teléfono tiene que moverlo.

### Cuándo no vale la pena

Si escribes más de lo que hablas, un teclado con buena predicción te rendirá más. Y si tu teléfono tiene poca
memoria, los motores locales no van a ir cómodos.
"""

GUIA["ElishaAz/Sayboard"] = """
### Para qué sirve

Teclado de voz para Android que reconoce **en el propio aparato** con la biblioteca Vosk: se pulsa el
micrófono, se habla y el texto se escribe en la aplicación que tengas abierta. Sin conexión y sin enviar
audio a ningún sitio.

### Cómo se usa

1. Se instala la APK de la entrega `v4.2.1`, del 23 de agosto de 2024.
2. En su asistente se descarga el modelo del idioma: hay que elegirlo bien, porque cada uno ocupa espacio y
   determina lo que entiende.
3. Se activa como teclado y se dicta; la primera carga del modelo tarda unos segundos.

### Lo que conviene saber antes

586 estrellas, GPL-3.0, y **su último cambio es de julio de 2025**: año y medio sin tocarlo. Su última
entrega es de agosto de 2024. Como se apoya en Vosk, su precisión no es la de los motores grandes: sirve para
frases cortas y claras, no para dictar un capítulo. En un Android actual conviene comprobar que sigue
activándose como teclado.

### Cuándo no vale la pena

Si necesitas dictar textos largos, la calidad no acompaña. Hoy hay teclados de este racimo, más nuevos y con
motores mejores, que hacen lo mismo.
"""

GUIA["HeliBorg/HeliBoard"] = """
### Para qué sirve

Teclado de Android sin conexión a internet, heredero de un teclado libre clásico: distribución ajustable,
deslizar para escribir, corrección y diccionarios por idioma, temas y ninguna llamada a la red. Es la opción
de referencia para quien quiere un teclado normal que no hable con nadie.

### Cómo se usa

1. Se instala la APK de la entrega `v4.2`, del 12 de octubre de 2026.
2. Se activa como teclado y se elige el idioma; el diccionario se descarga aparte, como archivo, y se importa.
3. En ajustes se afinan la altura, el número de filas, el gesto de deslizar y el tema.

### Lo que conviene saber antes

6.501 estrellas, GPL-3.0, y desarrollo vivo. Su gran ventaja es que **no pide permiso de red**, así que lo que
escribes no puede salir de ahí ni por descuido. Su pega es la de siempre en este tipo de teclado: la
predicción no es la de los gigantes, y la configuración inicial tiene más pasos de los que apetece.

### Cuándo no vale la pena

Si quieres deslizar el dedo y que acierte casi siempre, un teclado comercial lo hace mejor. HeliBoard se
elige por privacidad y por control, no por comodidad máxima.
"""

GUIA["Julow/Unexpected-Keyboard"] = """
### Para qué sirve

Teclado pensado para quien escribe **código y símbolos en el teléfono**: teclas extra en filas adicionales,
muchos caracteres por tecla con pulsación larga, gestos para mover el cursor y atajos. Ocupa muy poco y no
tiene red.

### Cómo se usa

1. Se instala la APK de la entrega `2.2.0`, del 1 de noviembre de 2026.
2. Se activa como teclado y se elige la distribución: la de programación, la de terminal o la normal.
3. Los símbolos se alcanzan con pulsación larga o deslizando desde las teclas de la esquina.

### Lo que conviene saber antes

3.337 estrellas, GPL-3.0, once años de historia y una entrega de hace cuatro días. Su diseño va contra la
moda: sin predicción agresiva, sin corrección que adivine, sin diccionario que aprenda. Eso es exactamente lo
que se quiere al escribir una orden en una terminal, y exactamente lo que no se quiere al mandar mensajes.

### Cuándo no vale la pena

Para escribir mensajes largos en español, la falta de corrección se nota mucho. Se elige para lo que fue
hecho: símbolos, terminales y administración desde el teléfono.
"""

GUIA["LeanBitLab/LeanType"] = """
### Para qué sirve

Teclado de Android derivado de HeliBoard que añade herramientas de inteligencia artificial a la escritura:
corrección con modelos, reescritura, tono y plantillas, además de lo que ya traía el teclado original
—diccionarios, deslizar, temas—.

### Cómo se usa

1. Se instala la APK de la entrega `v4.3.1`, del 4 de noviembre de 2026.
2. Se activa como teclado y se elige el idioma y su diccionario.
3. En ajustes se conectan los modelos: cada uno pide su clave y sus datos; el teclado avisa de que lo que
   escribas se envía a quien presta el modelo.
4. Las funciones de IA se colocan en teclas propias, y su configuración es donde se decide qué hay en cada una.

### Lo que conviene saber antes

1.143 estrellas, GPL-3.0, nacido el 15 de enero de 2026. **Aquí hay que corregir un dato que circula**: se ha
escrito por ahí que este teclado tiene «75 teclas de IA», una «armadura universal» y porcentajes de obediencia
forzada. No es cierto. En su código hay **diez** huecos de tecla para funciones propias —`CUSTOM_AI_1` a
`CUSTOM_AI_10`— y las llamadas «etiquetas mágicas» son diez palabras clave de su pantalla de ajustes. Lo
demás eran cifras sin ejecución detrás.

### Cuándo no vale la pena

Si no vas a usar las funciones de IA, HeliBoard, del que deriva, hace lo mismo con menos piezas. Y si las vas
a usar, ten claro que cada pulsación puede salir de tu teléfono hacia el proveedor del modelo.
"""

GUIA["Open-Less/openless"] = """
### Para qué sirve

Aplicación de dictado para **macOS y Windows**: se mantiene pulsada una tecla, se habla y al soltar aparece el
texto —ya pulido— en la aplicación donde estuvieras escribiendo. Usa modelos de reconocimiento locales y un
paso de modelo de lenguaje para quitar muletillas y ordenar la frase.

### Cómo se usa

1. Se instala la entrega `v2.0.1-tauri`, del 16 de octubre de 2026.
2. Se elige la combinación de teclas y el modelo de reconocimiento; en la primera ejecución se descarga.
3. Se concede permiso de micrófono y de accesibilidad, que es el que le permite escribir en otras ventanas.
4. Se mantiene la tecla, se habla, se suelta.

### Lo que conviene saber antes

4.053 estrellas, AGPL-3.0, escrito en Rust. Su propio texto lo sitúa como alternativa libre a herramientas
comerciales de dictado, y esa comparación es suya. La versión medida es la `2.0.1`, reciente y con cambios de
esta semana. Su requisito real es un equipo con memoria suficiente para mover el modelo sin esperas.

### Cuándo no vale la pena

Si usas Linux, aquí no hay nada: el proyecto es para los dos sistemas grandes de escritorio. Y si escribes
poco, el dictado con pulso mantenido no compensa el hábito de teclear.
"""

GUIA["SYSTRAN/faster-whisper"] = """
### Para qué sirve

Biblioteca en Python que ejecuta los modelos de reconocimiento de voz de Whisper **mucho más rápido** que la
implementación original, usando un motor de inferencia optimizado. Es la pieza que usan muchos programas de
dictado de este racimo por debajo.

### Cómo se usa

1. Se instala con `pip install faster-whisper`; la entrega medida es la `v1.2.1`, del 31 de octubre de 2025.
2. Desde código se carga un modelo —hay varios tamaños— y se le pasa el audio, o se usa su orden de ejemplo
   para transcribir un archivo.
3. En una tarjeta gráfica compatible va muy rápido; en procesador, más lento pero funciona.

### Lo que conviene saber antes

26.496 estrellas, licencia MIT, y su última entrega es de **octubre de 2025**, aunque el repositorio recibe
cambios en noviembre de 2026. No es un programa: no tiene ventana ni teclado. Se usa desde otro programa o
desde un guion. Su límite es la memoria de tu equipo: los modelos grandes piden varios gigas.

### Cuándo no vale la pena

Si lo que quieres es dictar, no empieces aquí: instala una de las aplicaciones de este racimo que ya lo
llevan dentro. Esta ficha existe porque es la pieza que hace posibles a las demás.
"""

GUIA["VocaHQ/vocalinux"] = """
### Para qué sirve

Dictado por voz para **Linux**, sin conexión: se habla y el texto se escribe en la ventana que tenga el foco,
funcione con X11 o con Wayland. Admite varios motores locales —el de referencia es `whisper.cpp`, pero
también Whisper y VOSK— y aprovecha la tarjeta gráfica cuando la hay.

### Cómo se usa

1. Se instala desde la entrega `v0.18.5`, del 27 de octubre de 2026, o desde el paquete de tu distribución.
2. La primera vez se descarga un modelo; el tamaño decide la precisión y la memoria que ocupa.
3. Se elige el atajo de teclado y el motor; al pulsarlo se empieza a dictar y al soltarlo se escribe.
4. En Wayland conviene revisar los permisos de la sesión: es la parte que más falla en ese entorno.

### Lo que conviene saber antes

994 estrellas, AGPL-3.0, escrito en Python, y versión `0.18`: está en construcción activa desde abril de 2025.
Es de los pocos proyectos de dictado que trata Wayland como ciudadano de primera, y eso ya justifica su
existencia. Su dependencia del modelo hace que en un equipo modesto la primera frase tarde.

### Cuándo no vale la pena

Si usas Windows o macOS, aquí no hay nada. Y si tu equipo es muy antiguo, mover el modelo en el procesador va
a ser más lento que escribir.
"""

GUIA["altic-dev/FluidVoice"] = """
### Para qué sirve

Aplicación de dictado para **macOS** con reconocimiento hecho en el propio equipo y un paso de mejora con un
modelo de lenguaje también local: se pulsa un atajo, se habla y el texto aparece donde estabas escribiendo,
con puntuación y sin muletillas.

### Cómo se usa

1. Se instala la entrega `v1.6.12`, del 22 de octubre de 2026.
2. Se concede permiso de micrófono y de accesibilidad, que es el que le deja escribir en otras aplicaciones.
3. Se elige el atajo y el modelo; en la primera ejecución se descargan los archivos.
4. Se mantiene el atajo, se habla y se suelta.

### Lo que conviene saber antes

12.818 estrellas, GPL-3.0, escrito en Swift, y nacido en septiembre de 2025: creció muy rápido. Su descripción
promete versiones para Windows, iOS, Android y Linux; medido hoy, **sólo hay versión para macOS y una prueba
para iOS**. Es decir: lo anunciado no es lo entregado, y esa distancia conviene tenerla delante antes de
instalarlo con expectativas. Su propio texto dice ser «el más rápido y el único» de su clase: eso es una
declaración del autor, no una medición de esta ficha.

### Cuándo no vale la pena

Si no usas Mac, hoy no hay versión que instalar por mucho que la descripción lo anuncie. Y en un Mac con poca
memoria, el paso de mejora con modelo de lenguaje se come el beneficio.
"""

GUIA["amicalhq/amical"] = """
### Para qué sirve

Aplicación de dictado para escritorio que además **toma notas**: se habla, el texto se escribe en la ventana
activa y queda un registro de lo dictado que se puede organizar en notas y resúmenes. Funciona con modelos
locales y avisa de cuándo algo sale a la red.

### Cómo se usa

1. Se instala la entrega `v1.12.5`, del 25 de septiembre de 2026.
2. Se conecta el modelo —local o por clave de un proveedor— y se elige el atajo de dictado.
3. Se habla; lo dictado entra en la aplicación activa y, además, en su historial de notas.
4. Las notas se ordenan por proyecto dentro de la propia aplicación.

### Lo que conviene saber antes

1.598 estrellas, MIT, escrito en TypeScript y nacido en mayo de 2025. Es de los pocos que añade algo al dictado
en vez de sólo transcribir, y eso lo hace útil para reuniones. Su parte delicada es la de siempre: si eliges
un modelo en la nube, lo que dices sale de tu equipo, y con reuniones eso significa conversaciones de otras
personas.

### Cuándo no vale la pena

Si sólo quieres dictar frases sueltas, la mitad de la aplicación —las notas— no la vas a usar. Y si no puedes
grabar a los demás con permiso, no es tu herramienta.
"""

GUIA["anomalyco/hex"] = """
### Para qué sirve

Dictado por voz para **macOS, Windows y Linux**, local: se mantiene una tecla, se habla y al soltar el texto
se pega donde estés escribiendo. Sin cuenta, sin nube y sin ventana que estorbe.

### Cómo se usa

1. Se instala la entrega `v3.3.0`, del 2 de noviembre de 2026.
2. Se elige el atajo, el modelo y el idioma; la primera vez se descarga el modelo.
3. Se concede el permiso de accesibilidad —o el equivalente en cada sistema— y se prueba en un editor de texto.
4. Se mantiene la tecla, se habla y se suelta.

### Lo que conviene saber antes

5.181 estrellas, MIT, escrito en Rust, y creado el 17 de julio de 2026: tiene cuatro meses. Es el ejemplo de la
tanda de aplicaciones de dictado que aparecieron en 2026, todas parecidas por fuera y distintas por dentro.
Su alcance multiplataforma es real, cosa que no se puede decir de todos los de este racimo.

### Cuándo no vale la pena

Si quieres algo con años de rodaje, cuatro meses son pocos. Y si tu equipo no tiene memoria para el modelo,
la espera entre hablar y ver el texto va a ser incómoda.
"""

GUIA["cjpais/Handy"] = """
### Para qué sirve

Transcripción de voz a texto que funciona **sin conexión**, multiplataforma y con la idea de ser extensible: se
pulsa un atajo, se habla y el texto aparece en la aplicación activa. Se puede ampliar con modelos y con
ajustes de puntuación.

### Cómo se usa

1. Se instala la entrega `v0.10.0`, del 2 de noviembre de 2026, para Windows, macOS o Linux.
2. Se descarga un modelo en la primera ejecución y se elige el atajo.
3. Se habla y se suelta; el texto se escribe solo, y en ajustes se añade puntuación automática.
4. Su documentación explica cómo cambiar de modelo y cómo ampliarlo.

### Lo que conviene saber antes

37.597 estrellas, MIT, escrito en Rust: es el más popular de su familia en este racimo y eso se nota en la
cantidad de incidencias resueltas. Sigue siendo una versión `0.x`, así que la interfaz cambia entre entregas.
Su punto fuerte es que **todo ocurre en el equipo**: nada de tu voz sale a un servidor ajeno.

### Cuándo no vale la pena

Si tu equipo va justo de memoria, el modelo local se va a llevar la peor parte. Y si dictas en un idioma con
pocos datos, la precisión baja como en todos los motores abiertos.
"""

GUIA["espanso/espanso"] = """
### Para qué sirve

Expansor de texto: escribes una palabra corta y el programa la sustituye por lo que hayas definido —una firma,
una dirección, una plantilla entera, la fecha de hoy—. Funciona en Windows, macOS y Linux, y en cualquier
aplicación donde escribas.

### Cómo se usa

1. Se instala la entrega `v2.4.1`, del 2 de septiembre de 2026.
2. Se editan sus archivos de configuración, que son texto legible: cada sustitución es un par de líneas.
3. Se recargan los cambios y se prueba en cualquier campo de texto.
4. Admite fechas, formularios con campos y órdenes del sistema, lo que permite plantillas bastante elaboradas.

### Lo que conviene saber antes

14.718 estrellas, GPL-3.0, escrito en Rust, siete años de proyecto. Su privacidad es real: las sustituciones
ocurren en tu equipo y las reglas son archivos tuyos. Su parte delicada es que **lee lo que escribes** para
detectar la palabra clave, así que es un programa con acceso de teclado: se instala a sabiendas.

### Cuándo no vale la pena

Si escribes las mismas cinco cosas al mes, no compensa configurarlo. Y si compartes el equipo, un expansor con
acceso al teclado es una decisión que hay que tomar entre todos.
"""

GUIA["florisboard/florisboard"] = """
### Para qué sirve

Teclado de Android que respeta la privacidad, con predicción, deslizar para escribir, temas y una arquitectura
pensada para añadir funciones sin pedir permiso de red. Su propio proyecto lo declara en estado de prueba.

### Cómo se usa

1. Se instala la APK de la entrega `v0.5.2`, del 28 de noviembre de 2025.
2. Se activa como teclado; el asistente guía los permisos y la descarga de diccionarios.
3. En ajustes se eligen idiomas, distribución, gestos y temas; el editor de temas permite cambiar colores y
   formas sin tocar código.

### Lo que conviene saber antes

8.755 estrellas, Apache-2.0, seis años de proyecto. El dato incómodo: **su última entrega es de noviembre de
2025**, aunque el repositorio sigue recibiendo cambios en noviembre de 2026; el programa que se descarga no
lleva un año de arreglos. Y sigue diciendo «beta» en su propia descripción, después de todo este tiempo.

### Cuándo no vale la pena

Si quieres un teclado que se actualice con frecuencia, la entrega vieja pesa. Hoy `HeliBoard` cubre lo mismo
con entregas más recientes, y por eso mucha gente ha hecho ese cambio.
"""

GUIA["futo-org/voice-input"] = """
### Para qué sirve

Aplicación de dictado para Android que **se integra con el teclado que ya usas**: no sustituye tu teclado, sino
que se ofrece como servicio de reconocimiento al botón de micrófono del sistema. Reconocimiento en el propio
teléfono, sin enviar el audio fuera.

### Cómo se usa

1. Se instala el paquete desde la fuente que indica su proyecto; aquí **no hay entregas publicadas**, porque
   este repositorio es un espejo del original que vive en GitLab y sirve sobre todo para reportar fallos.
2. Se activa como servicio de reconocimiento de voz en los ajustes del sistema.
3. Se pulsa el micrófono en tu teclado de siempre y se dicta.
4. Se descarga el modelo de idioma que corresponda dentro de la propia aplicación.

### Lo que conviene saber antes

350 estrellas y **GitHub no le reconoce la licencia** en la ficha. Su ventaja es enorme y sencilla: no tienes
que cambiar de teclado para dictar. Su límite es que la instalación no está en este repositorio, así que hay
que ir a la fuente del proyecto, y eso es un paso más del que apetece.

### Cuándo no vale la pena

Si no te importa cambiar de teclado, un teclado de dictado de este racimo te da lo mismo en una sola
instalación. Y si tu teléfono es viejo, el modelo local va a ir lento.
"""

GUIA["ggml-org/whisper.cpp"] = """
### Para qué sirve

Implementación de los modelos de reconocimiento de voz de Whisper en C y C++, sin dependencias y capaz de
correr en un teléfono, una Raspberry Pi o un portátil modesto. Es la pieza que hace posible el dictado local en
casi todas las aplicaciones de este racimo.

### Cómo se usa

1. Se compila —son dos órdenes con `cmake`— o se toma el binario de la entrega `v1.9.5`, del 6 de octubre de
   2026.
2. Se descarga un modelo en el formato del proyecto; hay varios tamaños, de unos cientos de megas a varios
   gigas.
3. Se transcribe un archivo con la orden de ejemplo, o se levanta su servidor local para que otros programas le
   manden audio.
4. Admite el micrófono del sistema para dictado en vivo.

### Lo que conviene saber antes

54.948 estrellas, licencia MIT, y desarrollo diario. Su virtud es correr donde otros no corren; su precio es
que hay que compilar y elegir el modelo a mano, y que la calidad depende de ese tamaño. En un equipo sin
tarjeta gráfica, los modelos grandes tardan lo suyo.

### Cuándo no vale la pena

Si lo que quieres es dictar y ya, instala una aplicación que lo lleve dentro: esto es el motor, no el
volante.
"""

GUIA["karansinghgit/speaktype"] = """
### Para qué sirve

Aplicación de dictado por voz que se presenta como **sin conexión y para cualquier sistema**: se habla y el
texto se escribe en la aplicación activa.

### Cómo se usa

1. Se instala la entrega `v2.0.0`, del 22 de septiembre de 2026.
2. Se concede el permiso de micrófono y el de escribir en otras ventanas.
3. Se elige el atajo y el modelo; se dicta manteniendo la tecla.

### Lo que conviene saber antes

573 estrellas, MIT, y un detalle que conviene mirar antes de descargar: el proyecto está escrito en **Swift** y
nació el 6 de enero de 2026, así que su alcance real es el ecosistema de Apple, por mucho que su descripción
hable de «cualquier sistema». Su última entrega es de septiembre de 2026.

### Cuándo no vale la pena

Si no estás en un Mac, comprueba los requisitos antes de instalar nada: lo escrito en Swift no corre en
Windows ni en Linux. Y para dictar cuatro frases al día, el teclado del sistema ya trae micrófono.
"""

GUIA["languagetool-org/languagetool"] = """
### Para qué sirve

Corrector de gramática y estilo para escritorio, con servidor propio y extensiones: revisa textos en más de
veinticinco idiomas, entre ellos el español, y señala errores que un corrector ortográfico no ve —concordancias,
preposiciones, frases mal construidas—.

### Cómo se usa

1. Se descarga desde la web del proyecto: **este repositorio no publica entregas**. Hay paquete de escritorio y
   servidor.
2. En escritorio se pega el texto o se abre un archivo; las sugerencias aparecen subrayadas.
3. Como servidor, se levanta en el equipo y las suyas propias —editor de código, procesador de textos— se
   conectan a él.
4. Las extensiones del navegador y del procesador de textos usan la instancia pública o la tuya.

### Lo que conviene saber antes

15.234 estrellas, LGPL-2.1, escrito en Java, y trece años de proyecto. Su versión libre tiene menos reglas que
el servicio comercial del mismo nombre: si comparas, mira qué conjunto de reglas estás usando. Y en español
funciona de verdad, que es más de lo que se puede decir de casi todo lo demás de este racimo.

### Cuándo no vale la pena

Si buscas revisión en tu procesador de textos y no te importa que el texto salga a internet, la extensión del
servicio público basta. Montar el servidor tiene sentido si el texto no puede salir de tu red.
"""

GUIA["notune/android_transcribe_app"] = """
### Para qué sirve

Herramienta de Android con dos caras: dictado sin conexión que se ofrece al micrófono del teclado que ya usas,
y **subtítulos en vivo** en pantalla para lo que se oye por el micrófono. El reconocimiento ocurre en el propio
teléfono.

### Cómo se usa

1. Se instala la APK de la entrega `v0.2.3`, del 17 de octubre de 2026.
2. Se activa como servicio de reconocimiento de voz, o se abre el modo de subtítulos.
3. En el modo de subtítulos se elige el tamaño del texto y el idioma; la transcripción va apareciendo mientras
   se habla.

### Lo que conviene saber antes

338 estrellas, MIT, escrito en Rust, con versión `0.2.x` y nacido en noviembre de 2025: es un proyecto joven y
pequeño. Su punto interesante es el modo de subtítulos, útil para ver una charla sin sonido o para quien tiene
dificultades de audición. Su límite es la precisión de un motor pequeño corriendo en un teléfono.

### Cuándo no vale la pena

Si quieres dictar textos largos con precisión alta, aquí no está. Y si tu teléfono tiene poca memoria, el
modelo local va a cortar frases.
"""

GUIA["openai/whisper"] = """
### Para qué sirve

El modelo de reconocimiento de voz que cambió el terreno: transcribe audio en decenas de idiomas, traduce al
inglés lo que oye en otro idioma y funciona razonablemente con ruido y acentos. Este repositorio trae el modelo
y una orden de terminal para usarlo.

### Cómo se usa

1. Se instala con `pip install -U openai-whisper`; la entrega medida es `v20250625`, del 26 de junio de 2025.
2. Se transcribe un archivo: `whisper audio.mp3 --model medium --language es`.
3. Con `--task translate` traduce al inglés; con `--output_format srt` saca subtítulos.
4. Para dictado en vivo hace falta otra pieza: esto trabaja sobre archivos o sobre una entrada de audio
   continua que hay que preparar.

### Lo que conviene saber antes

112.000 estrellas y licencia MIT: es la referencia de todo el racimo, y casi todos los demás programas lo usan
por debajo, en alguna de sus versiones optimizadas. Su último cambio es de **agosto de 2026** y su entrega de
junio de 2025: el proyecto va despacio porque el modelo ya está publicado y lo que evoluciona son las
reimplementaciones.

### Cuándo no vale la pena

Si tienes tarjeta gráfica, hay reimplementaciones de este mismo racimo que van mucho más rápido. Y si no
quieres tocar una terminal, usa una aplicación que lo lleve dentro.
"""

GUIA["opennookorg/betterwispr"] = """
### Para qué sirve

Aplicación de dictado para **macOS**, local: se mantiene una combinación de teclas, se habla y el texto entra en
la aplicación donde estés escribiendo, sin pasar por ningún servicio.

### Cómo se usa

1. Se instala la entrega `v0.1.5`, del 12 de octubre de 2026.
2. Se concede permiso de micrófono y de accesibilidad.
3. Se elige el atajo y el modelo; en la primera ejecución se descargan los archivos.
4. Se mantiene el atajo, se habla y se suelta.

### Lo que conviene saber antes

506 estrellas, Apache-2.0. El dato que manda: **el repositorio se creó el 7 de octubre de 2026**, o sea, un mes
antes de esta medición, y va por la `0.1.5`. Es un proyecto recién nacido, con todo lo que eso significa:
puede cambiar entero en la próxima entrega y puede no haber una próxima. Está escrito en Swift, así que sólo
existe en Mac.

### Cuándo no vale la pena

Hoy, para uso diario: un mes de vida no da para confiarle el dictado de tu trabajo. Si quieres algo parecido con
más rodaje, en este racimo hay varias opciones con más historia.
"""

GUIA["osfans/trime"] = """
### Para qué sirve

Teclado chino para Android construido sobre el motor Rime: lleva los esquemas de entrada tradicionales —pinyin,
zhuyin, cangjie, wubi, trazos— y permite añadir o escribir los tuyos. Su objetivo declarado es proteger la
lengua china en el teléfono, con diccionarios que el usuario controla.

### Cómo se usa

1. Se instala la APK de la entrega `v3.3.13`, del 1 de noviembre de 2026.
2. Se activa como teclado; la primera vez hay que dejar que prepare los esquemas.
3. Los esquemas y diccionarios viven en una carpeta accesible: se pueden copiar, editar y compartir.
4. En su pantalla de ajustes se elige el esquema activo y el aspecto del teclado.

### Lo que conviene saber antes

4.771 estrellas, GPL-3.0, once años de proyecto, y nació como interfaz de un teclado tradicional chino sobre
Rime. Es potente y exigente: configurar un esquema nuevo requiere editar archivos de texto. Para español no
sirve.

### Cuándo no vale la pena

Si no escribes chino, no hay nada que hacer aquí. Y si escribes chino pero quieres algo que funcione sin
configurar, un teclado comercial lo hace en dos toques.
"""

GUIA["peteonrails/voxtype"] = """
### Para qué sirve

Dictado por voz con pulsar-para-hablar en **Wayland**, el sistema de ventanas de las distribuciones Linux
modernas: se mantiene una tecla, se habla y el texto aparece en la ventana activa. Todo en el equipo, sin
servicios.

### Cómo se usa

1. Se instala la entrega `v1.1.1`, del 15 de octubre de 2026, o se compila.
2. Se elige el atajo y el modelo; el programa descarga lo que necesite.
3. Se concede permiso al compositor —GNOME, Hyprland y otros están contemplados— y se prueba en un editor.
4. Se mantiene la tecla, se habla y se suelta.

### Lo que conviene saber antes

1.745 estrellas, MIT, escrito en Rust, nacido en noviembre de 2025. Es de los pocos que declara trabajar sobre
Wayland de forma explícita, que es justo donde fallan casi todas las herramientas de este tipo en Linux. Su
propio texto habla de velocidad en tiempo real sobre el procesador; eso es una declaración del autor.

### Cuándo no vale la pena

Si sigues con X11, busca otra opción de este racimo: aquí el objetivo es Wayland. Y si tu compositor no está
entre los contemplados, la integración del atajo puede no funcionar.
"""

GUIA["rkkr/simple-keyboard"] = """
### Para qué sirve

Teclado de Android minúsculo —menos de un mega— con lo esencial: altura ajustable, fila de números, deslizar
la barra espaciadora para mover el cursor, borrado por gesto y colores de tema propios. Sus permisos se reducen
a la vibración.

### Cómo se usa

1. Se instala la APK de la entrega `149`, del 22 de octubre de 2026.
2. Se activa como teclado y se elige el tema y la altura en sus ajustes.
3. Los gestos: deslizar sobre la barra espaciadora mueve el cursor; deslizar sobre la tecla de borrar selecciona
   texto hacia atrás.

### Lo que conviene saber antes

1.607 estrellas, Apache-2.0, y nueve años de proyecto. Su descripción está vacía en GitHub, así que lo que se
sabe de él es su lista de funciones y su código. No tiene predicción ni descarga de diccionarios: es un teclado
para escribir a mano, no para que adivine.

### Cuándo no vale la pena

Si escribes rápido con deslizamiento y corrección, aquí vas a echar de menos todo eso. Se elige por tamaño, por
permisos y porque no aprende nada de lo que escribes.
"""

GUIA["scholay-xsime/xsime"] = """
### Para qué sirve

Entorno de escritura chino multiplataforma construido sobre Rime, con tres ideas propias: una memoria del texto
que va escribiendo, un archivo de lo copiado y de capturas, y una ventana aparte que recibe lo que llega de
fuera. En la práctica, un teclado chino con herramientas alrededor.

### Cómo se usa

1. Se instala la entrega `v1.2.0`, del 27 de octubre de 2026.
2. Se activa como método de entrada en el sistema y se eligen los esquemas de Rime.
3. Las herramientas —historial de copiado, capturas, cuaderno— se abren desde su propia ventana.

### Lo que conviene saber antes

1.179 estrellas, Apache-2.0, creado el 8 de agosto de 2026: menos de tres meses de vida y entregas seguidas. Su
texto está íntegramente en chino, y su código base de entrada procede del motor Rime, cosa que el proyecto
declara. Es un proyecto ambicioso y joven; la ambición, hoy, va por delante de la estabilidad.

### Cuándo no vale la pena

Si no escribes chino, no hay nada que hacer. Y si escribes chino en Mac o Windows y quieres algo probado, hay
proyectos de este mismo racimo con años encima.
"""

GUIA["soupslurpr/Transcribro"] = """
### Para qué sirve

Teclado de Android que reconoce la voz **en el propio aparato**: incluye la detección de cuándo empiezas y
acabas de hablar, de modo que no hay que pulsar nada para empezar ni para cortar. Se puede usar como teclado
completo o sólo como servicio de reconocimiento para el teclado que ya tengas.

### Cómo se usa

1. Se instala la APK de la entrega `7`, del 7 de agosto de 2025.
2. En la primera ejecución se descarga un modelo; hay varios tamaños.
3. Se activa como teclado o como servicio de voz, y se habla: la detección de voz corta sola cuando callas.

### Lo que conviene saber antes

761 estrellas, licencia ISC —permisiva y poco habitual—, con desarrollo en 2026 pero **entrega de agosto de
2025**. Es decir: el código va por delante de lo que puedes descargar. Su mezcla de reconocimiento local y
detección de actividad de voz es lo que lo hace cómodo, y su límite es la precisión de los modelos pequeños.

### Cuándo no vale la pena

Si buscas la última versión de cada arreglo, la entrega tiene más de un año. Y si tu teléfono es modesto, el
modelo local y la detección de voz compiten por la misma memoria.
"""

GUIA["wasi-master/wmkeyboard"] = """
### Para qué sirve

Teclado de Android con ambición de sustituir al de fábrica: predicción, escritura deslizando, transliteración,
búsqueda de emojis y una caja de herramientas con muchas utilidades, todo hecho en el teléfono y con la promesa
de no enviar nada fuera. Presume de cubrir más de seiscientos idiomas.

### Cómo se usa

1. Se instala la APK de la entrega `v0.6.5`, publicada hoy, 5 de noviembre de 2026.
2. Se activa como teclado y se eligen los idiomas; cada uno trae su diccionario.
3. Las herramientas se abren desde su propia caja: conversores, cálculos, textos de plantilla.
4. En ajustes se activa o desactiva la predicción y el deslizamiento, que consumen memoria.

### Lo que conviene saber antes

736 estrellas, MIT, creado el 10 de agosto de 2026: tres meses. Su texto habla de **seiscientos idiomas** y de
**89 herramientas**; son cifras del autor y aquí no se han contado una por una. En un teclado, la cantidad de
funciones no es una ventaja por sí sola: cada una ocupa sitio en la memoria y en la atención de quien mantiene
el proyecto.

### Cuándo no vale la pena

Un teclado con tres meses de vida es lo primero que se rompe cuando el sistema cambia. Si quieres estabilidad,
elige uno con años; si te apetece probar, empieza por desactivar lo que no uses.
"""

GUIA["zoolapp/aime"] = """
### Para qué sirve

Método de entrada chino para **macOS**, construido sobre el motor Rime, con lo local por delante y funciones de
asistencia opcionales. Escribe en chino con los esquemas de siempre y añade ayudas que se pueden desconectar.

### Cómo se usa

1. Se instala la entrega `v0.1.10`, del 20 de octubre de 2026.
2. Se añade como método de entrada en los ajustes del sistema y se eligen los esquemas.
3. Las funciones opcionales se activan una por una en sus preferencias.

### Lo que conviene saber antes

255 estrellas, MIT, creado el 1 de octubre de 2026: un mes. Su propio proyecto avisa de que es una versión
temprana `0.1.x` en iteración rápida, y a la vez indica algo poco habitual en proyectos tan jóvenes: el paquete
va firmado y notarizado por Apple, y publica archivo de verificación para comprobarlo. Declara además no ser
una bifurcación del teclado chino clásico de Mac, sino un proyecto aparte que puede convivir con él.

### Cuándo no vale la pena

Si no escribes chino, no aplica. Y si buscas un método de entrada para años, un mes de vida es poco, por muy
bien firmado que venga el paquete.
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
