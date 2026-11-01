*El taller de parches: lo que se toca, lo que se firma y lo que no se receta*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 10 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🎬 Seis escenas del taller
├── 🧾 El censo de hoy
├── 🔧 Qué es un parche y qué no lo es
├── 🧩 Las tres puertas del permiso
├── 🏪 Las tiendas que no son la tienda
├── 🚫 Lo que no se receta
├── 🛠️ Parchear lo propio en siete pasos
├── ⚖️ La ley, sin sermón
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas del corte
```

───────────────────

*⚡ En una página*

Cada cierto tiempo alguien pregunta por el programa que «mejora los gráficos del juego» o por el paquete que quita los anuncios de una app de pago. La pregunta llega casi siempre con una captura de pantalla y sin la palabra licencia en ningún lado. Esta guía trata de lo que sí se puede hacer con herramientas libres y de por qué media pregunta se contesta sola cuando se mira quién firma el paquete.

Esta mañana leí dieciséis proyectos del taller, tres veces cada uno y por tres caminos distintos. Los números grandes son jadx con ★51.439, Magisk con ★63.665, SmartTube con ★35.801, Shizuku con ★32.577, ReVanced Manager con ★30.029, Apktool con ★26.888 y LSPosed con ★25.287. Y apareció un caso que no había visto en este censo: un repositorio de parches que la forja devuelve con código 451, el de «no disponible por razones legales», y por lo tanto no se pudo leer. Queda anotado como hueco, no como ausencia.

Lo que el taller enseña, más allá de los números, es que hay tres permisos distintos y la gente los confunde todo el tiempo. Uno es el del sistema, que se consigue con root y hoy se reparte entre Magisk y los kernels con su propia vía. Otro es el de la depuración, que Shizuku abre sin tocar el arranque y sin perder la garantía. El tercero es el de la aplicación misma, que LSPosed y LSPatch consiguen colgándose de su proceso. Cada puerta da cosas distintas y ninguna convierte al teléfono en otra cosa.

Y está la parte que no se receta: los paquetes de mods que prometen rendimiento, los que inyectan cuentas ajenas y los que reparten apps de pago. Aquí no hay enlaces de eso, no porque no existan, sino porque publicar un enlace así convierte esta página en parte del problema. Lo que sí hay es el método para hacer las cosas uno mismo sobre lo que tiene licencia para tocarse.

La idea que hay que llevarse: un parche no es magia, es una edición del paquete que cambia la firma. Quien entiende eso entiende también por qué la app deja de actualizarse sola, por qué un mod rara vez sobrevive a la siguiente versión y por qué el origen del paquete importa más que su nombre.

───────────────────

*🎬 Seis escenas del taller*

**El juego que va lento.** Un muchacho llega con un juego que se traba y una captura de un programa que «duplica los FPS» cambiando el modelo de la GPU. El programa es cerrado, se instala como administrador y no se sabe qué toca. La conversación honesta es otra: bajar los gráficos, cerrar lo que corre en segundo plano, liberar espacio, y si el aparato no da, no da. Un cambio de identificador de GPU no crea memoria donde no hay.

**Los anuncios del reproductor.** Una señora ve videos con cinco cortes cada diez minutos. Su teléfono no está rooteado y no quiere rootearlo. La salida razonable es un cliente libre alternativo, como SmartTube o los reproductores de la familia libre, que se instalan como app aparte y no tocan la que vino con el teléfono. Sin root, sin parches raros y sin cuentas que se compartan.

**La app que pide cuenta de Google y el teléfono no la tiene.** Un aparato sin servicios de Google necesita un puente para que ciertas apps crean que están en un teléfono con ellos. Ese puente es microG, que hoy se publica en su repositorio propio con ★15.152 y licencia Apache-2.0. No es un mod ni un truco: es una implementación libre de esas interfaces, y por eso se puede auditar.

**El paquete que no se instala.** Alguien baja un APK, lo instala y el sistema responde que la aplicación no está disponible o que el paquete entra en conflicto con otro existente. Casi siempre es la firma: el paquete nuevo viene firmado por otra persona y Android no deja poner uno encima de otro si no coinciden. Se resuelve desinstalando el anterior, o no se resuelve, y ahí se acaba el experimento.

**El teléfono prestado.** Un técnico necesita mirar el interior de una app en un aparato ajeno, con el dueño delante y sin rootear nada. Con la depuración activada y Shizuku puede hacer varias de esas operaciones sin tocar el arranque, y al terminar se revoca el permiso y el aparato queda como estaba. Esa es la diferencia entre revisar y modificar.

**El archivo que llegó sin extensión.** Un cliente manda un archivo que el teléfono no reconoce. Con Apktool o con jadx se abre, se mira qué es y se decide si se instala o se borra. Esas dos herramientas no son para todos los días: son el destornillador que se usa tres veces al año y salva la tarde.

───────────────────

*🧾 El censo de hoy*

Dieciséis proyectos medidos tres veces cada uno, más un hueco declarado. Estrellas, licencia, lenguaje y último empujón son de esta mañana; la versión sale del último release publicado y su fecha va al lado.

*El parche y su motor*

- **ReVanced Manager** — la aplicación que aplica parches a un APK que el usuario ya tiene ★30.028 · licencia GPL-3.0 · Kotlin · empujó el 29-jul (hace 95 días) · release v2.6.0 (26-abr) · https://github.com/ReVanced/revanced-manager
- **ReVanced CLI** — la misma tarea desde la línea de órdenes, sin interfaz ★1.600 · licencia GPL-3.0 · Kotlin · empujó el 02-jun (hace 152 días) · release v6.0.0 (14-mar) · https://github.com/ReVanced/revanced-cli
- **ReVanced Patcher** — el motor que aplica y revierte los parches ★3.550 · licencia GPL-3.0 · Kotlin · empujó el 09-jun (hace 145 días) · release v22.0.1 (13-mar) · https://github.com/ReVanced/revanced-patcher
- **Parches de una rama alternativa** — el conjunto de parches del proyecto de inotia00, con sus propias reglas ★2.260 · licencia GPL-3.0 · Java · empujó el 10-mar (hace 236 días) · release v5.14.1 (31-dic-2025) · https://github.com/inotia00/revanced-patches
- **El repositorio que no se pudo leer** — el conjunto de parches del proyecto grande contestó hoy con código 451, «no disponible por razones legales». No hay ficha: hay un hueco anotado, y no se rellena con lo que uno recuerde de la última vez.

*El permiso del sistema*

- **Magisk** — el sistema de root que trabaja por encima del arranque y reparte permisos por módulos ★63.671 · licencia GPL-3.0 · Kotlin · empujó el 27-oct (hace 5 días) · release v31.1 (25-oct) · https://github.com/topjohnwu/Magisk
- **LSPosed** — el marco que inyecta cambios en el proceso de una app concreta, sin tocar las demás ★25.288 · licencia GPL-3.0 · Java · empujó el 14-oct (hace 18 días) · su release público es v1.9.2 (11-oct-2023) y las compilaciones nuevas salen por integración continua · https://github.com/LSPosed/LSPosed
- **LSPatch** — la variante que aplica esos cambios sin root, metiéndolos en el paquete ★9.453 · licencia GPL-3.0 · Java · último empujón 13-dic-2023 (hace 1.054 días) · release v0.6 (23-nov-2023) · https://github.com/LSPosed/LSPatch

*El permiso sin rootear*

- **Shizuku** — abre la depuración del sistema a las apps que la piden, sin tocar el arranque ★32.585 · licencia Apache-2.0 · Kotlin · empujó el 18-jun-2025 (hace 501 días) · release v13.6.0 (25-may-2025) · https://github.com/RikkaApps/Shizuku

*El destornillador*

- **jadx** — descompilador que convierte un APK en código legible para revisarlo ★51.442 · licencia Apache-2.0 · Java · empujó el 30-oct (hace 2 días) · release v1.5.6 (10-jul) · https://github.com/skylot/jadx
- **Apktool** — abre el paquete, separa recursos y volver a cerrarlo ★26.891 · licencia Apache-2.0 · Java · empujó el 28-oct (hace 4 días) · release v3.0.3 (20-jul) · https://github.com/iBotPeaches/Apktool

*El puente de los servicios*

- **microG (GmsCore)** — implementación libre de las interfaces que muchas apps esperan encontrar ★15.152 · licencia Apache-2.0 · Java · empujó el 26-oct (hace 6 días) · release v0.3.17.252432 (29-sep) · https://github.com/microg/GmsCore

*Las tiendas que no son la tienda*

- **Aurora Store** — cliente de la tienda de Google sin cuenta de Google ★3.216 · licencia GPL-3.0 · Kotlin · empujó hoy · release v2.0.5-β sin fecha publicada en la ficha · https://github.com/whyorean/AuroraStore
- **Droid-ify** — cliente de F-Droid con búsqueda rápida y firma verificada ★7.678 · licencia GPL-3.0 · Kotlin · empujó el 12-sep (hace 50 días) · release v0.7.8 (12-sep) · https://github.com/Droid-ify/client

*El cliente aparte y el instalador*

- **SmartTube** — reproductor de video para televisores y cajas, con su propio control de lo que se ve ★35.806 · licencia MIT · Java · empujó hoy · release 32.68s (20-oct) · https://github.com/yuliskov/SmartTube
- **SAI (Split APKs Installer)** — instala paquetes divididos en varias partes ★3.956 · licencia GPL-3.0 · Java · último empujón 03-jun-2024 (hace 881 días) · release 4.5 (25-feb-2021) · https://github.com/Aefyr/SAI

*Lo que el censo dice en cuatro líneas.* Cinco de los dieciséis empujaron esta semana y dos empujaron hoy, pero el grupo del parche lleva meses de calma: el Manager no publica versión desde abril y el motor desde marzo. Dos proyectos están claramente parados —LSPatch desde diciembre de 2023 y SAI desde junio de 2024— y siguen teniendo miles de estrellas, lo que dice mucho de cuánto tarda el vecindario en enterarse. Y hay un hueco declarado: el repositorio de parches del proyecto grande responde 451 hoy, y sin lectura no hay ficha.

*Lo que quedó fuera, y por qué.* Se intentó leer también dos proyectos de root alternativo por kernel y ninguno entregó README crudo legible en ninguna de las ramas ni de los nombres habituales, así que no aparecen en la tabla ni se citan sus números. Un repositorio que no se deja leer no se recomienda de memoria: se deja dicho y se sigue con los que sí respondieron.

───────────────────

*🔧 Qué es un parche y qué no lo es*

Un APK es un comprimido: adentro hay código compilado, imágenes, textos, configuración y una firma. Un parche es una lista de cambios que se aplica sobre ese comprimido y produce otro, con el mismo nombre y otra firma. Nada más, y nada menos. Ese «otra firma» es la clave de todas las preguntas que llegan después.

Cuando alguien parchea una app, lo que obtiene es un paquete nuevo que el sistema ve como distinto del original. Por eso Android no deja instalarlo encima sin desinstalar antes: para el sistema son dos aplicaciones. Por eso tampoco se actualiza solo, aunque la app original sí lo haga. Y por eso los datos se pierden al cambiar de uno a otro si no se exportan antes.

Lo que un parche puede hacer es amplio: quitar una comprobación que molesta, cambiar un comportamiento por defecto, añadir una función que el autor no puso, traducir textos, cerrar una vía de rastreo. Lo que no puede hacer es crear contenido, saltarse un servidor que cobra por algo, ni darte una cuenta que no tienes. Cuando alguien promete eso, no está parcheando: está falsificando una identidad frente a un servicio, y eso es otra cosa con otras consecuencias.

La diferencia entre parchear y modear es de origen y de permiso. Un parche se aplica con herramientas cuyo código se puede leer, sobre un paquete que el usuario obtuvo legalmente, y el resultado se queda en el teléfono de esa persona. Un mod, en la práctica, es un paquete cerrado que alguien ya parcheó y reparte como archivo, sin código, sin registro de qué le cambió y sin forma de comprobar qué más trae adentro.

Hay un tercer caso que conviene nombrar: los parches que se aplican a servicios de pago para obtener lo que se cobra. Ahí no hay debate técnico. El programa funciona, el servicio deja de cobrar y quien lo usa queda expuesto a que le cierren la cuenta, además de que quien reparte el paquete sabe exactamente quién lo instaló. Es la razón por la que esta guía no reparte esos enlaces ni los va a repartir.

Y hay un cuarto caso, el más común de todos: parchear una app propia para quitarle algo que a uno le estorba. Un reproductor que arranca con publicidad en la pantalla de inicio, un lector que pide iniciar sesión para leer lo descargado, una calculadora que manda estadísticas. Eso es lo que se puede hacer con las herramientas de esta lista, y eso es lo que se explica en los pasos de más abajo.

Conviene saber también qué se pierde. Un paquete parcheado no recibe las actualizaciones del autor, y con el tiempo eso deja de ser una molestia y pasa a ser un problema: los arreglos de seguridad que el autor publique no llegan, y la versión instalada envejece sola en un aparato conectado a internet. Cada cierto tiempo hay que repetir el procedimiento sobre la versión nueva, con el trabajo que eso implica.

Y hay un detalle técnico que explica la mitad de los fracasos: los parches se escriben contra una versión concreta. Cuando el autor cambia una función o cambia el nombre de un recurso, el parche deja de encontrarlo y falla, o peor, se aplica a medias. Por eso las herramientas serias avisan qué versión esperan y por eso conviene anotar con qué versión se trabajó, para saber qué repetir cuando toque.

───────────────────

*🧩 Las tres puertas del permiso*

La confusión más común del taller es creer que todo lo que modifica el teléfono necesita root. No es así, y separar las tres puertas ahorra sustos.

**La puerta del sistema: root.** Magisk, con ★63.665 y versión v31.1 del 25 de octubre, trabaja por encima del arranque y reparte permisos a módulos. Su ventaja es que no toca la partición del sistema: los cambios viven aparte y se pueden desactivar. Su costo es real: se abre una puerta que algunas apps bancarias detectan, se pierde la garantía en la mayoría de los casos y un módulo mal hecho puede dejar el aparato sin arrancar. La versión importa: un Magisk viejo con un Android nuevo es una receta de problemas.

**La puerta de la app: LSPosed y LSPatch.** LSPosed, con ★25.287, inyecta cambios en el proceso de una aplicación concreta sin tocar a las demás. Su repositorio empujó el 14 de octubre, y su último release público es de octubre de 2023: el trabajo reciente sale por compilaciones de integración continua, que no llevan número bonito. LSPatch, con ★9.453, hace algo parecido sin root, metiendo el andamio dentro del paquete; dejó de empujar en diciembre de 2023 y su última versión es la v0.6, de noviembre de ese año. Sirve, y hay que saber que nadie lo está manteniendo.

**La puerta de la depuración: Shizuku.** Con ★32.577, licencia Apache-2.0 y versión v13.6.0 del 25 de mayo de 2025, Shizuku no rootea: pide prestado el permiso que el propio Android da a los desarrolladores y lo reparte a las apps que lo solicitan, con el usuario aprobando cada una. Su último empujón es del 18 de junio de 2025, así que también está en pausa, y sigue funcionando porque el permiso que usa es del sistema y no cambia todos los meses.

El orden de preferencia que funciona en la práctica es este: primero Shizuku, porque se revierte apagando la depuración; después LSPosed, si hace falta tocar una app concreta; y al final Magisk, solo si hay una razón que valga el riesgo. Empezar por el final es lo que convierte un teléfono que funciona en un fin de semana de recuperación.

Hay una cuarta puerta que no es puerta: la de cambiar de programa. Buena parte de las consultas que empiezan por «cómo parcheo esto» terminan en «instala la versión libre que ya hace lo mismo». Es la salida menos vistosa y la que menos cuesta, porque no rompe la firma de nada ni obliga a repetir el procedimiento en cada actualización. El taller sirve para lo que no tiene reemplazo; para lo demás, hay vecinos.

───────────────────

*🏪 Las tiendas que no son la tienda*

La mitad de los problemas que llegan al taller se resuelven antes de parchear nada, solo cambiando por dónde se instala. Hay tres puertas de entrada y cada una tiene su carácter.

La tienda del sistema es cómoda y actualiza sola, pero decide qué se publica y con qué permisos. Aurora Store, con ★3.215, licencia GPL-3.0 y empujón de hoy, ofrece otro camino al mismo catálogo: se conecta sin cuenta de Google, permite bajar la versión que uno quiera y avisa cuando una app pide permisos de más. Su versión publicada es una beta sin fecha en la ficha, y eso hay que decirlo: lo que se instala hoy es una versión de prueba de un proyecto vivo.

F-Droid y sus clientes son el otro extremo. Droid-ify, con ★7.678, licencia GPL-3.0 y versión v0.7.8 del 12 de septiembre, es una interfaz rápida para el repositorio libre: muestra la licencia de cada app, la versión y el historial, y comprueba firmas. Lo que hay ahí está compilado a partir del código publicado, y por eso a veces llega unos días después que el release del autor.

La tercera puerta es la forja, el APK que el propio autor publica. Llega el mismo día, no hay intermediario y actualizar es a mano. Su ventaja es la trazabilidad: el release tiene fecha, número y a veces una firma verificable. Su riesgo es que la descarga se hace desde un enlace que hay que comprobar cada vez, porque los sitios que imitan a las forjas existen y se parecen demasiado.

Antes de instalar conviene hacerse tres preguntas de treinta segundos: quién firma este paquete, qué gano con esta puerta y qué pasa el día que la app se rompa. Las respuestas cambian poco entre proyectos y evitan casi todos los arrepentimientos. Una app que se firma con la llave de un repositorio se puede rastrear; un archivo que llegó por un grupo de mensajería, no.

El error clásico es mezclar las tres en la misma app. Una app instalada desde F-Droid no se actualiza con el APK del autor, porque la firma es distinta; el sistema lo rechaza o, peor, ofrece desinstalar y perder los datos. Antes de instalar conviene decidir la puerta y quedarse ahí. Para las que se usan todos los días, la puerta que actualiza sola; para las que se prueban, la forja.

Y hay un detalle que ahorra disgustos: las tres puertas no se miden por lo que entregan el primer día sino por lo que resuelven el día del fallo. Cuando una app se rompe tras una actualización, la tienda del sistema suele ofrecer volver atrás, la forja exige buscar el release anterior a mano y el repositorio libre tarda un poco más en tener la versión nueva. Saber eso antes de elegir evita la tarde de buscar APKs en sitios turbios con el teléfono a medio funcionar.

Y hay un cuarto caso que no es tienda pero funciona como tal: el paquete dividido. Las apps modernas a veces vienen en varias partes —una base y varios añadidos por idioma y por pantalla— y el instalador del sistema no siempre las maneja. SAI, con ★3.955 y licencia GPL-3.0, resuelve eso, aunque su último empujón fue en junio de 2024 y su versión publicada es de febrero de 2021: sirve para lo que sirve y no se le puede pedir más.

───────────────────

*🚫 Lo que no se receta*

Esta es la sección que algunas personas van a leer buscando otra cosa, y conviene ser claro desde el primer renglón: aquí no hay enlaces a paquetes modificados, ni a programas que dicen duplicar el rendimiento, ni a mods de aplicaciones de pago. La razón no es moralina. Es que publicar un enlace así convierte a quien lo publica en parte de la cadena que después no se puede auditar.

Lo primero que hay que entender de los programas que prometen «acelerar» el teléfono cambiando el modelo de la tarjeta gráfica es que son cerrados. No se puede leer su código, no se sabe qué modifican ni qué más hacen mientras están abiertos. En un aparato que tiene la banca, el correo y las conversaciones de la familia, instalar un programa cerrado con permisos de administrador para ganar unos cuadros por segundo es un cambio que no se justifica con ningún resultado.

Lo segundo es que el rendimiento no aparece por cambiar un nombre. Un juego que se traba lo hace por memoria, por calor o por un procesador que no da más. Cambiar el identificador de la GPU puede hacer que el juego elija ajustes distintos, y a veces eso se siente como una mejora; otras veces empeora, y el que lo instaló no tiene forma de revertirlo porque no sabe qué cambió.

Lo tercero es el paquete de mods de una app de pago. Ahí hay tres problemas a la vez: se está usando un servicio sin pagarlo, el paquete lo firma alguien que no es el autor y no se sabe qué añadió, y la cuenta del usuario queda a la vista de quien reparte el archivo. Cualquiera de los tres basta para no hacerlo.

Lo cuarto es la cuenta prestada. Los paquetes que inyectan sesiones ajenas para acceder a un servicio convierten al que los usa en un intruso en la cuenta de otra persona. Que técnicamente funcione no cambia lo que es.

Lo que sí se receta, y está en los pasos de abajo, es lo contrario: aprender a mirar qué pide un paquete antes de instalarlo, usar herramientas con código visible y aplicar cambios sobre lo propio. Eso no da resultados de captura de pantalla, pero no deja deuda. Y cuando algo se rompe, se puede volver atrás porque se sabe qué se hizo.

Para reconocer un paquete cerrado hay tres señales que se ven en dos minutos. La primera: no hay repositorio o el repositorio no tiene el código del programa, solo capturas y un archivo de descarga. La segunda: la descarga pasa por un acortador, un canal de mensajería o una nube con clave. La tercera: el texto promete resultados medibles —«triplica los FPS», «todo desbloqueado»— en vez de explicar qué cambia. Con dos de esas tres señales, no hay nada que discutir.

Y hay una señal que se ve después, cuando ya está instalado: pide permisos que no tienen que ver con lo que hace. Una herramienta que dice mejorar gráficos y pide leer los mensajes o los contactos no está mejorando nada. En un teléfono con la banca adentro, eso es una puerta abierta con el nombre de un adorno.

───────────────────

*🛠️ Parchear lo propio en siete pasos*

Los siete pasos de abajo son para el caso limpio: un paquete que se obtuvo por una puerta conocida, un teléfono propio y un cambio que se entiende. Si alguno de los tres falta, el procedimiento no se salta: se detiene, porque el taller no arregla un origen dudoso ni devuelve lo que se rompió por saltarse una comprobación.

**Paso uno: saber qué paquete se tiene.** Antes de tocar nada, apuntar la versión exacta de la app, de dónde salió y qué datos guarda. Si es una app de mensajería, exportar la conversación; si es un juego, guardar el avance; si es un lector, anotar qué se descargó. El parche va a producir un paquete distinto y el paso entre uno y otro puede llevarse los datos.

**Paso dos: tener el APK original en el teléfono.** El parche se aplica sobre el archivo, no sobre la app instalada. Si el aparato no lo tiene a mano, se baja de la puerta que corresponda —la forja del autor o el repositorio libre— y se comprueba la fecha y el número de versión antes de seguir. Un APK de un sitio que imita a la forja arruina el resto del procedimiento.

**Paso tres: mirar antes de aplicar.** Con jadx o con Apktool se abre el paquete y se ve qué contiene: permisos declarados, servicios, librerías de rastreo, textos. Es la parte que casi nadie hace y la que más enseña. Un paquete que pide acceso a los contactos para una calculadora se explica solo, y a veces la conclusión es no instalar nada.

**Paso cuatro: elegir la puerta correcta.** Si el objetivo es cambiar una app concreta y el teléfono no está rooteado, Shizuku o LSPatch. Si el teléfono ya está rooteado y el cambio es de sistema, LSPosed o Magisk. Si no hay root y no hay ganas de meterse en la depuración, la respuesta honesta es buscar una app libre que ya haga lo que se necesita.

**Paso cinco: aplicar el parche y probar en pequeño.** Se selecciona el parche, se genera el paquete y se instala. Antes de confiar, se prueba lo esencial: que abra, que conserve la sesión, que no se caiga al cambiar de pantalla. Si algo falla, se desinstala y se vuelve al original; el paquete original no se borra hasta comprobar que el nuevo sirve.

**Paso seis: aceptar el costo de la firma.** El paquete parcheado no se actualiza solo y no puede convivir con el original. Eso significa que cada actualización de la app exige repetir el procedimiento, y que los datos hay que respaldarlos antes de cada salto. Quien no quiera ese mantenimiento debe quedarse con la app original y buscar la función en otro lado.

**Paso siete: dejar el teléfono como estaba si se abandona.** Desinstalar el paquete parcheado, revocar el permiso de depuración o desactivar el módulo, y comprobar que el aparato arranca y que las apps sensibles vuelven a abrir. Un taller ordenado se conoce en cómo queda la mesa al final, no en las herramientas que tiene.

───────────────────

*⚖️ La ley, sin sermón*

Las herramientas de esta guía son libres y eso permite leer qué hacen: GPL-3.0 en el Manager, en el motor, en Magisk, en LSPosed, en LSPatch, en Aurora y en Droid-ify; Apache-2.0 en Shizuku, microG, jadx y Apktool; MIT en SmartTube. La licencia del programa no es la licencia de lo que se parchea, y ahí está el punto que suele confundirse.

Una licencia libre permite modificar el programa y, según el caso, obliga a publicar los cambios si se distribuyen. Lo que no permite es tocar otro programa que no es de uno. Si la app que se quiere parchear es propietaria, modificarla para uso propio es una zona gris que cada país trata distinto, y distribuir el resultado ya es otra cosa: es repartir una obra derivada de algo ajeno, sin permiso y con la firma de otro.

El caso del repositorio que hoy contesta 451 es el ejemplo más claro de que ese límite existe y tiene consecuencias. Un código 451 en una forja no es un error técnico: es una respuesta legal. Cuando eso pasa, el proyecto no desaparece del teléfono de quien ya lo tenía, pero deja de poder instalarse desde ahí, y el hueco se anota.

Hay un matiz que a veces se pasa por alto y que cambia la conversación: la licencia del parche no es la licencia del paquete parcheado. Las herramientas de este taller son libres y sus parches también, pero eso solo autoriza a tocar lo que se puede tocar. Con una app propietaria, el permiso no viene del código de la herramienta: viene del dueño de la app, y casi nunca está escrito en ningún lado.

Hay además una regla que no viene de ninguna ley y funciona igual: la trazabilidad. Un paquete del que se sabe quién lo firmó, cuándo se publicó y qué contiene se puede auditar; un paquete repartido por un canal de mensajería, no. En un teléfono con datos de la familia, la trazabilidad vale más que cualquier función añadida.

───────────────────

*❓ Preguntas que me hacen*

**¿Parchear una app la vuelve más rápida?** Casi nunca. Un parche cambia comportamientos, no añade memoria ni enfría el procesador. Cuando alguien nota una mejora suele ser porque el parche desactivó algo que consumía recursos en segundo plano, y eso se puede saber mirando qué se aplicó. Si la promesa es «el doble de velocidad», no es un parche: es publicidad.

**¿Instalo Magisk en un teléfono que uso para trabajar?** Solo si hay una razón concreta y si se acepta el costo: algunas apps de banca y de pago dejan de abrir, la garantía se pierde en la mayoría de los casos y un módulo mal hecho puede impedir que arranque. Para revisar o cambiar una app puntual, Shizuku hace buena parte del trabajo sin esa factura.

**¿Shizuku necesita root?** No. Aprovecha el permiso de depuración que el propio sistema ofrece a los desarrolladores, y se activa una vez con cable o por inalámbrico; después el usuario aprueba qué apps lo usan. Si se apaga la depuración o se reinicia sin repetir la activación, el permiso se pierde y hay que volver a darlo.

**¿Por qué el paquete parcheado no se actualiza solo?** Porque lo firma otra persona: para Android es otra aplicación. El sistema solo actualiza paquetes con la misma firma que el instalado, y el parcheado rompe esa cadena. Cada versión nueva de la app original exige repetir el procedimiento y volver a instalar.

**¿Qué pasó con el repositorio de parches que no aparece en la tabla?** Que hoy responde con código 451, el de «no disponible por razones legales». Sin lectura no hay ficha, y poner números de memoria sería inventar. El hueco queda anotado y, si mañana vuelve a responder, se mide y se publica.

**¿LSPatch sigue vivo?** No. Su último empujón es del 13 de diciembre de 2023 y su última versión es la v0.6 del 23 de noviembre de ese año. Funciona en lo que funcionaba, pero no recibe arreglos, y en un Android nuevo eso significa que puede dejar de servir sin aviso.

**¿Y LSPosed, con un release de 2023?** Es otro caso: su repositorio empujó el 14 de octubre, lo que indica trabajo reciente, pero sus compilaciones nuevas salen por integración continua y no llevan número de versión. Quien lo use tiene que decidir si confía en una compilación automática o se queda en la última versión publicada, que es la v1.9.2 de octubre de 2023.

**¿Para qué sirve microG si el teléfono no tiene servicios de Google?** Para que ciertas apps que esperan encontrarlos funcionen sin ellos. Es una implementación libre de esas interfaces, con licencia Apache-2.0 y versión v0.3.17 del 29 de septiembre. No es un parche ni un truco: es un programa que ocupa el lugar de otro y que se puede leer.

**¿Aurora Store da las mismas apps que la tienda?** Da acceso al mismo catálogo y permite bajar versiones anteriores, sin cuenta de Google. Su versión publicada es una beta sin fecha en la ficha, y conviene tenerlo presente: es un proyecto vivo con releases de prueba, no un producto terminado.

**¿Puedo usar dos versiones de la misma app, una original y una parcheada?** No con el mismo nombre de paquete. Android identifica la app por su identificador, y dos paquetes iguales no conviven. Algunos parches permiten cambiar el identificador para instalar la copia al lado, y eso funciona a veces, con el costo de que la copia queda fuera de las actualizaciones y de las copias de seguridad del sistema.

**¿Cómo sé si un APK que me pasaron es el original?** Comparando la firma con la del release del autor y con el tamaño del archivo. Si no hay forma de comparar, la respuesta práctica es no instalarlo: un paquete sin origen comprobable no se vuelve confiable porque el que lo manda sea conocido.

**¿Vale la pena rootear hoy?** Para la mayoría de la gente, no. Casi todo lo que se hacía con root en 2015 se resuelve ahora con la depuración, con una app libre alternativa o con una tienda distinta. El root sigue teniendo sentido para quien administra varios aparatos o investiga, y ese público ya sabe lo que cuesta.

───────────────────

*📊 Tabla, mitos y glosario*

*Los dieciséis del taller*

| Proyecto | Para qué | Licencia | Último empujón | Estrellas |
|---|---|---|---|---|
| Magisk | root por módulos, sin tocar el sistema | GPL-3.0 | 27-oct | ★63.665 |
| jadx | leer el código de un APK | Apache-2.0 | 30-oct | ★51.439 |
| SmartTube | reproductor de video aparte | MIT | hoy | ★35.801 |
| Shizuku | depuración sin root | Apache-2.0 | 18-jun-2025 | ★32.577 |
| ReVanced Manager | aplicar parches desde el teléfono | GPL-3.0 | 29-jul | ★30.029 |
| Apktool | abrir y cerrar paquetes | Apache-2.0 | 28-oct | ★26.888 |
| LSPosed | cambios dentro de una app, con root | GPL-3.0 | 14-oct | ★25.287 |
| microG | puente de servicios libres | Apache-2.0 | 26-oct | ★15.152 |
| LSPatch | lo mismo que LSPosed, sin root | GPL-3.0 | 13-dic-2023 | ★9.453 |
| Droid-ify | cliente de F-Droid | GPL-3.0 | 12-sep | ★7.678 |
| SAI | instalar paquetes divididos | GPL-3.0 | 03-jun-2024 | ★3.955 |
| ReVanced Patcher | el motor de los parches | GPL-3.0 | 09-jun | ★3.550 |
| Aurora Store | catálogo de la tienda sin cuenta | GPL-3.0 | hoy | ★3.215 |
| Parches de rama alternativa | otro conjunto de parches | GPL-3.0 | 10-mar | ★2.260 |
| ReVanced CLI | parchear desde la línea de órdenes | GPL-3.0 | 02-jun | ★1.600 |
| Parches del proyecto grande | **sin medir hoy: la forja responde 451** | — | — | — |

*Cinco mitos del taller*

**Mito uno: «un mod es una versión mejorada».** Un mod es otro paquete, con otra firma y sin registro de cambios. Puede ser útil y puede traer de todo; lo que no es, es la misma aplicación. La versión mejorada de una app se llama actualización y la publica su autor.

**Mito dos: «con root se arregla todo».** Con root se accede a todo, incluido lo que rompe el teléfono. La mayoría de los problemas del taller —una app que no abre un formato, un reproductor que corta, un paquete que no instala— no se arreglan con root: se arreglan con otra app o con la versión correcta.

**Mito tres: «si tiene muchas estrellas, está mantenido».** LSPatch tiene ★9.453 y no recibe un empujón desde diciembre de 2023. SAI tiene ★3.955 y su última versión es de 2021. Las estrellas miden cuánta gente lo usó, no cuánta lo cuida.

**Mito cuatro: «el APK es el mismo en todos lados».** El mismo número de versión puede venir firmado por personas distintas, y con la firma cambia lo que el sistema permite y lo que el paquete puede hacer. El número dice qué versión es; la firma dice quién la hizo.

**Mito cinco: «parchear es ilegal».** Parchear un programa libre es parte de su licencia. Modificar software propietario para uso propio es una zona gris según el país, y distribuir el resultado sin permiso es otra cosa. La línea no está en la herramienta: está en qué se toca y qué se reparte.

*Glosario del taller*

**APK** — el paquete de una aplicación de Android; por dentro es un comprimido con código, recursos y firma.

**Parche** — lista de cambios que se aplica sobre un paquete y produce otro, con otra firma.

**Firma** — sello criptográfico del paquete. Dos firmas distintas no se instalan una encima de otra.

**Root** — permiso total sobre el sistema, por encima del arranque.

**Módulo** — pieza que Magisk carga al arrancar para cambiar algo del sistema sin tocar la partición.

**Inyección** — técnica de LSPosed y LSPatch: meter código en el proceso de una app concreta.

**Depuración** — canal de administración que Android ofrece a los desarrolladores, con cable o por inalámbrico.

**Paquete dividido** — app repartida en varias partes: una base y añadidos por idioma o por pantalla.

**Beta** — versión de prueba que se publica antes de la estable, a veces sin fecha en la ficha.

**451** — código que devuelve un servidor cuando el contenido no está disponible por razones legales.

───────────────────

*🔗 Enlaces y notas del corte*

Cada dirección de abajo se abrió hoy. Ninguna sale de una lista vieja ni de una deducción por parecido.

*El parche y su motor*

- ReVanced Manager: https://github.com/ReVanced/revanced-manager
- ReVanced CLI: https://github.com/ReVanced/revanced-cli
- ReVanced Patcher: https://github.com/ReVanced/revanced-patcher
- Parches de rama alternativa: https://github.com/inotia00/revanced-patches

*El permiso*

- Magisk: https://github.com/topjohnwu/Magisk
- LSPosed: https://github.com/LSPosed/LSPosed
- LSPatch: https://github.com/LSPosed/LSPatch
- Shizuku: https://github.com/RikkaApps/Shizuku

Los enlaces de arriba son los de los proyectos que se midieron hoy. Los dos que no se pudieron leer no aparecen como enlace vacío: se nombran en la nota de hueco, con el motivo, y quedan pendientes para la próxima pasada. Esa es la única forma de mantener la lista honesta sin congelarla.

*El destornillador y el puente*

- jadx: https://github.com/skylot/jadx
- Apktool: https://github.com/iBotPeaches/Apktool
- microG: https://github.com/microg/GmsCore

*Tiendas, cliente e instalador*

- Aurora Store: https://github.com/whyorean/AuroraStore
- Droid-ify: https://github.com/Droid-ify/client
- SmartTube: https://github.com/yuliskov/SmartTube
- SAI: https://github.com/Aefyr/SAI

*Lo que no se pudo medir.* El conjunto de parches del proyecto grande respondió hoy con código 451 desde la forja, y dos proyectos de root alternativo por kernel no entregaron README crudo legible en ninguna rama ni con ninguno de los nombres habituales. Los tres quedan fuera de la tabla, con el motivo dicho. Un censo que rellena sus huecos con memoria deja de ser un censo.

*Cómo se mide este taller, para poder repetirlo.* Cada proyecto se leyó tres veces: por el buscador de la forja, por la página del repositorio y por el archivo crudo del README. Las estrellas y el último empujón se cotejaron entre las tres lecturas; cuando la página y el buscador no coincidieron, se publicó el número de la página y se dejó dicho. La licencia se copia de la ficha, y cuando el README declara otra se escriben las dos. La versión sale del último release publicado, con su fecha, y si el proyecto no fecha sus releases se dice.

───────────────────

*🌅 Cierre — la mesa ordenada*

Lo que deja este recorrido, en plata: el taller de parches no es un cuarto oscuro, es una mesa con tres puertas y tres herramientas. La puerta del sistema pide root y cobra caro; la de la app inyecta cambios en un proceso concreto; la de la depuración presta un permiso que el propio Android ofrece. Elegir por la última y no por la primera es lo que separa un experimento de un fin de semana perdido.

El hallazgo del día no es un número grande sino una respuesta: un repositorio que devuelve 451 recuerda que estas herramientas viven en un terreno con dueños y con abogados. Cuando algo así pasa, la guía honesta no inventa la ficha que falta: la declara y sigue.

Y el tercer hallazgo es de método: casi todo lo que se preguntó esta semana se resolvía mirando el paquete antes de instalarlo. Quien abre un APK con jadx y ve qué permisos declara se ahorra la mitad de las dudas, y esa costumbre no requiere root ni asume riesgo: requiere veinte minutos y curiosidad.

Y el otro hallazgo es de calendario: LSPatch sin empujones desde diciembre de 2023, SAI con una versión de 2021, el conjunto de parches del proyecto grande sin leerse hoy, mientras Magisk, jadx y Apktool empujan esta semana. En este taller, la pregunta que hay que hacer antes de instalar no es cuántas estrellas tiene, sino cuándo fue la última vez que alguien lo tocó.

> —¿Y el programa que duplica los gráficos?
> —Ese no lo tengo, y si lo tuviera no te lo pasaría por aquí: cámbiale los ajustes al juego y ahorras el riesgo.

💓 *La Bandita informa a partir de fuentes fechadas.* Un parche cambia el paquete; no cambia de dueño la firma.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 09:20 y las 09:58 de Santo Domingo, y repasada a las 10:52· dieciséis proyectos leídos tres veces cada uno (buscador, página y archivo crudo) · un repositorio con respuesta 451 y dos sin README legible quedan fuera de la tabla, con el motivo escrito · una release sin fecha publicada se anota como tal

*Licencia:* el contenido va con CC BY-SA 4.0, los datos medidos con CC BY 4.0 y el código con MIT; el nombre de la casa y su marca quedan reservados para «Alexis (La Bandita)».

## 🗒️ Notas del corte

**Nota de corte (1-nov):** todas las estrellas, licencias y empujones son de esta mañana, medidas tres veces por proyecto. Donde el último release público no refleja el trabajo reciente —LSPosed es el caso claro— se escriben las dos cosas: la fecha del release y la del empujón.

**Nota de límite (1-nov):** esta guía no reparte paquetes modificados, ni enlaces de descarga de mods, ni programas que prometen rendimiento. Explica el método y los permisos, y deja dicho por qué los paquetes cerrados con permisos de administrador no se recomiendan para un teléfono que se usa para trabajar.

**Nota de hueco (1-nov):** el conjunto de parches del proyecto más conocido respondió con código 451 y no se pudo medir. Se anota el hueco en la tabla y en el texto, sin completar los números a mano y sin citar de memoria lo que decía la última vez que se leyó.

**Nota de sucesión (1-nov):** LSPatch y SAI siguen descargables y siguen funcionando en lo que funcionaban, pero no reciben empujones desde 2023 y 2024. Quien los use debe saber que no habrá arreglos, y que el reemplazo hay que buscarlo antes de que haga falta, no después.

**Nota de repaso (1-nov, 10:52):** el taller se repasó a las 10:52: quince repositorios citados, dos con empujón de hoy y dos archivados —LSPatch e inotia00— además del hueco del 451 que sigue sin abrirse. Nueve cifras se movieron desde la primera lectura.
