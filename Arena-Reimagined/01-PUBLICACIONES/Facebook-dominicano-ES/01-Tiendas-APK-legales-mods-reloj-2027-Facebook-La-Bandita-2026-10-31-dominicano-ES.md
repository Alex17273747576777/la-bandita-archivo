*Tiendas de APK: la tienda con dueño, el letrero de mods y el reloj que ya está corriendo*

*La Bandita · sábado 31 de octubre de 2026 · edición dominicano-español · pieza 01 de Facebook*

Una vez me preguntaron en un grupo: «¿y cuál es la tienda buena?». Contesté con otra pregunta: «¿quién te la recomienda?». Porque el problema nunca fue la tienda. El problema es que la mayoría de la gente instala lo que le llegó, no lo que buscó.

Esto no es una guía de tiendas. Es una guía de *decisiones*. Cinco escenas reales, doce casas medidas hoy, un tutorial y una vara para que la uses sin mí.

───────────────────

*ESCENA 1 — La tía que tiene el teléfono lleno*

La tía tiene un teléfono de 2019. Le instalaron «una tienda» en el colmado: un APK que promete «todo gratis». Tiene cuarenta apps que no recuerda haber instalado, el teléfono calienta y la batería no llega a la tarde.

Lo primero que hay que entender es que *eso no es un problema de apps, es un problema de origen*. Ninguna de esas cuarenta vino de un lugar donde alguien respondiera por ellas. Y el daño no fue instalarlas: fue no poder preguntar quién las firmó.

La receta, en tres pasos, sin tecnicismos:

*1.* Desinstalar todo lo que no reconozca. Si no sabes qué es una app, no la necesitas.
*2.* Instalar *Neo-Store* —es un cliente de F-Droid, la tienda libre, y tiene una función que a mí me parece la más útil de todo el ecosistema: te dice qué rastreadores trae cada app—.
*3.* Explicarle una sola regla: *si no sabes de dónde salió, no se instala*.

Media hora. No hace falta más, y no hace falta hablar de root, de ADB ni de nada que suene a taller.

───────────────────

*ESCENA 2 — El del colmado que quiere la app del banco*

Aquí no hay software libre que valga: el banco publica su app en Google Play y punto. Y el teléfono del colmado no tiene los servicios de Google porque se los quitaron para que fuera más rápido.

La respuesta honesta es *Aurora Store*. No es una tienda libre: es un mensajero. Se hace pasar por un teléfono normal, le pide el archivo a Google Play y te lo entrega. No necesitas cuenta de Google, no necesitas los servicios de Google, no le das tu identidad a Google.

Lo que hay que decir del mensajero, y casi nadie lo dice: *la cuenta anónima es una cuenta compartida por mucha gente*, y por eso a veces «no funciona» y hay que esperar. No es un fallo: es el precio de no dar tu nombre. Y cuando la app del banco tiene sus propios detectores de seguridad, puede negarse a correr en un teléfono sin servicios de Google. Eso no lo arregla ninguna tienda.

Medido hoy: el repositorio `AuroraOSS/AuroraStore` en GitHub tiene *★71* y GPL-3.0. Setenta y una estrellas para una app que usa medio mundo sin saberlo, porque *ese GitHub es un espejo* y su casa de verdad está en GitLab. Es el primer dato incómodo de esta pieza: las estrellas no miden lo que la gente cree que miden.

───────────────────

*ESCENA 3 — El estudiante que quiere YouTube sin anuncios*

Esta es la pregunta más frecuente y la que menos me gusta contestar, porque la respuesta honesta es incómoda para todos.

Hay dos cosas distintas metidas en la misma frase. Una: *el parche*, que es código libre, público, con autor y con historial. Otra: *la app parcheada*, que es la app original de Google con el parche encima, y que técnicamente es una copia modificada de un producto privativo.

Mi posición, que es mía y no la impongo: yo no recomiendo distribuir apps parcheadas. Lo que sí recomiendo es que *sepas exactamente qué estás instalando* cuando lo hagas. Y que no lo bajes de un canal donde nadie firma nada: si el parche es libre, el camino limpio existe y se puede auditar.

El resto de esta guía no depende de esa decisión. Pero la escena va aquí porque es la puerta por la que entra la mitad de la gente, y prefiero que entren sabiendo qué hay del otro lado.

───────────────────

*ESCENA 4 — El técnico que dice «eso se arregla con root»*

Falso, casi siempre. Y esta es una de las cosas que más daño le hace a la gente: creer que para tener control del teléfono hay que rootearlo.

Hay un camino intermedio que casi nadie explica bien y que hoy está maduro: *Shizuku*. No es root. Es un puente: un proceso que ya tiene permisos de sistema los presta a una app normal, con tu permiso explícito, y ese préstamo *muere cada vez que reinicias el teléfono*. Por eso Shizuku hay que volver a activarlo; no es un fallo, es la garantía.

Medido hoy, en el mundo que hay alrededor:

• `RikkaApps/Shizuku` — *★32.552 · Apache-2.0 · sin empujar desde el 18 de junio de 2025: 500 días*. Dormido. Y aun así es el estándar de facto. Esto es lo que significa «dormido no es muerto»: una pieza de infraestructura terminada puede estar años quieta y funcionar igual.
• `iamr0s/Dhizuku` — *★4.067 · GPL-3.0 · empujó hoy · release v2.13.0*. La alternativa, viva y moviéndose.
• `timschneeb/ShizuStore` — *★501 · GPL-3.0 · empujó en las últimas horas*. La tienda de apps que usan Shizuku.
• `carlelieser/yuki` — *★157 · MIT · empuje del 12 de octubre*. El catálogo curado, no instalador.

*La advertencia que va con esto y va en serio:* darle Shizuku a una app es darle llaves que Android no le daría. Instala solo apps cuyo código puedas leer. Un permiso de núcleo en manos de un desconocido es peor que un anuncio.

───────────────────

*ESCENA 5 — El que vuelve de un mod y no sabe qué perdió*

Le instalaron «el WhatsApp modificado» en el colmado. Funcionaba. Seis meses después, el teléfono empezó a mostrar anuncios en el bloqueo y la batería duraba la mitad.

Lo que perdió no fue el teléfono: fue *la trazabilidad*. Ese archivo no tiene repositorio, no tiene autor, no tiene historial. Cuando algo empieza a ir mal, no hay a quién preguntar, y no hay forma de saber qué cambió entre la versión que funcionaba y la que no.

Lo que hay que hacer en ese caso, en orden:

*1.* Hacer copia de los chats —la exportación de WhatsApp funciona y no depende del mod—.
*2.* Desinstalar el mod.
*3.* Instalar la app oficial desde su sitio o desde Aurora Store.
*4.* Restaurar la copia.
*5.* Revisar los permisos que quedaron concedidos a apps que ya no existen.

Y la lección, que es la tesis de esta pieza entera: *lo barato se paga con la llave de la puerta*.

───────────────────

*LAS DOCE CASAS — qué te cuesta cada una*

Ninguna tienda es gratis. Todas cuestan algo: tiempo, confianza, catálogo o comodidad. Aquí está el precio de cada una, medido hoy, para que elijas sabiendo qué pagas.

*1 · F-Droid — te cuesta tiempo*
Es la tienda libre de referencia desde 2010. Compila cada app desde su código y la firma con su propia llave. El precio es el que nadie menciona: *una actualización puede tardar semanas*, porque reconstruir no es copiar. Lo que compras con ese tiempo es verificación: si instalas de aquí, alguien revisó antes que tú. Si una app no está, casi siempre es porque usa código privativo, depende de Google o su receta de construcción no pasa.

*2 · IzzyOnDroid — te cuesta un poco de criterio*
Es el anexo de F-Droid. Ahí entran apps que la casa madre todavía no acepta. El detalle que hay que saber: muchas veces *no compila*, sino que firma el APK que publica el desarrollador. Es un estándar más flojo, no un estándar malo. Se añade como repositorio extra y desde ese momento ves las dos casas en la misma lista.

*3 · Droid-ify — te cuesta nada*
Cliente de F-Droid, más rápido y más bonito que el original. Medido hoy: *★7.678 · GPL-3.0 · último empuje el 12 de septiembre · release v0.7.8*. Lleva 49 días quieto: dormido, no muerto. Su repositorio de GitHub es un *espejo* —su casa es Codeberg—, y ese detalle es la primera lección de esta pieza: el espejo no es la casa.

*4 · Neo-Store — te cuesta nada y te da una brújula*
El otro cliente moderno. Medido hoy: *★5.589 · GPL-3.0 · empuje del 23 de octubre · release 1.3.3*. Su aporte real es la sección de rastreadores: te dice qué bibliotecas de seguimiento trae cada app, con nombre y apellido, apoyándose en el trabajo de Exodus Privacy. Cero rastreadores no garantiza nada; cinco en una calculadora sí dice algo.

*5 · Aurora Store — te cuesta un poco de tu identidad o un poco de paciencia*
El mensajero de Google Play. O usas la cuenta anónima compartida —y esperas cuando se cae— o pones tu cuenta y aceptas el trato. Te da apps que solo existen en Play; no te da el ecosistema de Google que muchas de ellas necesitan para funcionar del todo.

*6 · Accrescent — te cuesta catálogo*
Joven, exigente, con verificación de identidad del desarrollador por DNS y firmas modernas. Pide Android 12 o más. Lo que compras es la tranquilidad de un catálogo pequeño y limpio; lo que pagas es no encontrar casi nada de lo que buscabas.

*7 · Orion Store — te cuesta la verificación de un tercero*
Catálogo en JSON abierto, sin servidor propio, descarga directa del release del desarrollador. Medido hoy: *★3.883 · GPL-3.0 · empuje del 29 de octubre · release 2.6.5 del 27 de octubre*. Su propia web, hoy, sigue anunciando la 1.5.0 con «cifras al 6 de octubre»: casi un mes de retraso, declarado por ellos. No es mentira, pero es exactamente lo que hay que mirar siempre: *¿de cuándo es el número que me estás dando?*

*8 · GrapheneOS Apps — te cuesta tener un catálogo chiquito*
La tienda del sistema endurecido de GrapheneOS. *★624 · MIT · empujó hoy · release 37*. Sus apps (cámara, visor de PDF, reloj, calculadora) están escritas para no depender de Google y varias funcionan en cualquier teléfono moderno. Es una despensa de barrio, no un supermercado.

*9 · Obtainium — te cuesta entender un concepto*
No es una tienda: es una libreta de direcciones que vigila releases. *★21.095 · GPL-3.0 · empujó en las últimas horas · release v1.7.3*. Le das el repositorio de una app y te avisa cuando hay versión nueva, bajándola del propio desarrollador. Sin intermediario: máxima frescura, cero verificación de terceros.

*10 · komi-store — te cuesta caer en la tentación*
Catálogo navegable de apps publicadas en GitHub, Codeberg y Forgejo. *★20.176 · Apache-2.0 · release v1.9.4 del 24 de octubre*. Bueno para descubrir; malo si confundes «está en el catálogo» con «está revisado».

*11 · Appteka — te cuesta la revisión que no existe*
Mercado abierto: su propio sitio declara hoy *334.000 apps, 42 categorías, publica cualquiera, escaneo de seguridad al subir*. Su cliente oficial, `solkin/appteka-android`: *★1.367 · GPL-3.0 · release v23.0 del 13 de agosto*. Es un escalón por encima de un grupo de WhatsApp con APKs y varios escalones por debajo de F-Droid.

*12 · Las listas curadas — te cuestan una hora de lectura y ninguna confianza*
AAA (*★3.141 · CC-BY-4.0*), awesome-fdroid (*★200 · Unlicense*), awesome-shizuku (*★10.666 · sin licencia clara*), best-root-apps (*★50 · MIT*), best_shizuku_apps (*★158 · CC BY-SA 3.0 declarada en el README*). Sirven para descubrir nombres; no sustituyen al que firma. Y ojo con la licencia de una lista: la CC de la lista no es la licencia de las apps que recomienda.

───────────────────

*EL TUTORIAL — de cero a un teléfono que no te espía*

Esto es lo que yo haría, en orden, con un teléfono recién formateado. Tiempo total: unos 40 minutos, contando las descargas.

*Paso 1 — La tienda base (5 minutos)*
Entra a la página de F-Droid, baja el APK, instálalo. Android te va a decir que la app no es de una fuente verificada: es normal, estás instalando la tienda que *no* viene con el teléfono. Activa el permiso para ese instalador y solo para ese.

*Paso 2 — El cliente cómodo (3 minutos)*
Desde F-Droid, instala *Neo-Store*. Añade el repositorio de IzzyOnDroid (lo encuentras en su sitio, en la sección de repositorios). Ahora tienes dos casas en una sola lista.

*Paso 3 — La brújula (2 minutos)*
En Neo-Store, abre cualquier app y busca la sección de rastreadores. Hazlo con tres apps que ya uses. No vas a desinstalarlas todas hoy: vas a empezar a ver.

*Paso 4 — El actualizador (5 minutos)*
Instala *Obtainium*. Añade las tres o cuatro apps que más te importan y que no están en F-Droid. Empieza por una sola: la que más rabia te dé actualizar a mano. Cuando le cojas el truco, añades las demás.

*Paso 5 — El mensajero, solo si hace falta (5 minutos)*
Si necesitas una app que solo vive en Google Play, instala *Aurora Store*. Si no la necesitas, no la instales: cada cosa que añades es una cosa más que mantener.

*Paso 6 — El cinturón de seguridad (5 minutos)*
Revisa qué apps tienen permiso de instalación. En Android moderno es Ajustes → Aplicaciones → Acceso especial → Instalar apps desconocidas. Deja ahí solo las tiendas que reconozcas. Todo lo demás, fuera.

*Paso 7 — La prueba de fuego (10 minutos)*
Abre las tres apps que instalaste desde F-Droid y comprueba que funcionan. Si alguna no arranca, no es la tienda: casi siempre es una versión que pide más Android del que tienes, o un APK dividido que hay que unir con *AntiSplit-M* (*★4.938 · Apache-2.0 · release 2.3.3 de hoy*).

*Paso 8 — La regla escrita (1 minuto)*
Pega esto en una nota del teléfono: «No instalo nada cuyo origen no pueda nombrar». Suena tonto. Es lo único que de verdad importa de toda esta pieza.

───────────────────

*LA FICHA DE HOY — catorce apps donde la fecha que ves no es la fecha que crees*

Cuando una tienda funciona, lo que baja por ella son apps. Medí hoy catorce, y las elegí a propósito: son las que más gente instala después de poner una tienda, y son las que mejor enseñan un problema que casi nadie mira.

*Las del paquete Fossify (la suite libre que reemplaza a las apps de Google):*

• `FossifyOrg/Gallery` — *★3.870 · GPL-3.0 · empujó hoy · release 1.14.1 del 24 de octubre*. Galería sin nube, sin reconocimiento facial enviado a ningún lado.
• `FossifyOrg/Messages` — *★1.627 · GPL-3.0 · empuje del 26 de octubre · release 1.10.2 del 24 de octubre*. SMS sin telemetría.
• `FossifyOrg/Phone` — *★1.397 · GPL-3.0 · empujó hoy · **release 1.11.1 fechada el 3 de febrero de 2026***. Ojo aquí: el proyecto empuja código casi todos los días y su «última release» según GitHub tiene ocho meses. No está muerto ni dormido: *publica por otro canal*. La fecha de la última release no es la fecha del proyecto.
• `FossifyOrg/File-Manager` — *★1.846 · GPL-3.0 · release 1.6.3 del 24 de octubre*.
• `FossifyOrg/Voice-Recorder` — *★1.034 · GPL-3.0 · release 1.7.4 del 24 de octubre*.

*Las de Goodwy (el otro paquete, más viejo):*

• `Goodwy/Gallery` — *★196 · GPL-3.0 · último empuje el 23 de mayo · release 8.3.0*. Cinco meses quieta. Dormida.
• `Goodwy/PlayBook` — *★138 · GPL-3.0 · último empuje el 18 de abril de 2025 · release 4.1.1*. Un año y medio sin moverse. Aquí ya no es «dormida»: es *abandonada con honra* —funciona, pero no esperes parches—. La diferencia entre dormida y abandonada no la marca el calendario solo: la marca si el proyecto tiene quién lo recoja.

*Las del sistema GrapheneOS (funcionan fuera de él):*

• `GrapheneOS/Camera` — *★1.423 · MIT · empuje del 30 de octubre · release 93 del 1 de agosto*. Una cámara que no manda fotos a ninguna nube y no pide los servicios de Google.
• `GrapheneOS/PdfViewer` — *★1.062 · MIT · empuje del 28 de octubre · release 33 del 30 de julio*. Un visor de PDF que no abre una conexión para «verificar la licencia».

*Los lanzadores (esto es lo que la gente cambia primero cuando sale de Google):*

• `LawnchairLauncher/lawnchair` — *★13.832 · sin licencia clara (NOASSERTION) · empujó en las últimas horas · **«última release 1.2.0.1884» con fecha de 2018***. Trece mil estrellas para un proyecto vivo que publica por canales nocturnos: la API de GitHub toma la release más alta por número de versión y te enseña una de hace ocho años. Si te fías de ese número, concluyes lo contrario de la verdad.
• `MM2-0/Kvaesitso` — *★5.335 · GPL-3.0 · empujó hoy · release v1.41.0 del 15 de septiembre*. Lanzador con búsqueda; el más activo del grupo.
• `NeoApplications/Neo-Launcher` — *★2.153 · GPL-3.0 · empuje del 25 de octubre · «release 0.9.3» de diciembre de 2023*. Mismo patrón que Lawnchair: empuja cada semana y su release «oficial» es de hace casi tres años.
• `georgeclensy/Escape-Launcher` — *★465 · sin licencia clara · empujó hoy · release v2.3.1 del 2 de enero*. Minimalista, vivo, con licencia por aclarar.
• `iamrasel/lunar-launcher` — *★548 · GPL-3.0 · último empuje el 27 de abril de 2024 · release 2.8.2*. Dos años y medio. Este sí está muerto, y lo digo con la fecha.

*Lo que estas catorce enseñan, y es la razón de ponerlas juntas:*

*1.* La fecha de la «última release» puede mentir sin que nadie mienta. Los proyectos serios publican por canales que GitHub no marca como release principal.
*2.* Empujar código no es publicar versión, y publicar versión no es empujar código. Hay que mirar las dos cosas.
*3.* Una app sin licencia clara (NOASSERTION) no es ilegal: es *indeterminada*. Puedes usarla; no puedes saber qué te permite hacer con ella.
*4.* Y la más importante: *el estado de un proyecto no se lee en una cifra, se lee en dos*. Estrellas y fecha juntas dicen algo; por separado, casi nada.

───────────────────

*LA VARA EN CUATRO PASOS — para que no dependas de mí*

*Paso 1 — ¿Quién firma?*
Busca el repositorio. Dentro, el archivo LICENSE. Si no hay archivo, lee la sección «License» del README —la sección, no la primera vez que aparece la palabra MIT en cualquier parte del texto, que es el error que yo mismo cometí y tuve que corregir en público—. Sin licencia no significa «peligroso»: significa «indeterminado».

*Paso 2 — ¿Cuándo se movió?*
Último empuje y última release. Menos de 45 días: vivo. Entre 45 y 180: dormido. Más de 180: probablemente abandonado. Y si la release es vieja pero el empuje es de ayer, mira si publican por otro canal antes de concluir nada.

*Paso 3 — ¿Qué pide?*
Los permisos, uno por uno. La pregunta correcta no es «¿son muchos?», es «¿este permiso tiene que ver con lo que la app hace?». Una linterna que pide contactos ya te contestó.

*Paso 4 — ¿Puedo reconstruirlo?*
Si está en F-Droid, ya lo hizo otro por ti. Si está solo en un release de GitHub, estás confiando en el desarrollador y no en un tercero. Las dos son confianzas legítimas y distintas; lo que no se vale es creer que estás haciendo la primera cuando estás haciendo la segunda.

*Los cuatro pasos tardan cuatro minutos.* Y con ellos ya puedes auditar cualquier cosa que te manden por WhatsApp, incluida esta pieza.

───────────────────

*LOS LETREROS DE MODS — cómo se reconocen sin abrirlos*

Voy a nombrar las categorías y no los sitios, por una razón simple: los sitios cambian de nombre cada temporada y las categorías no. Si aprendes a reconocer la estructura, no te hace falta la lista negra.

*Categoría 1 — La vitrina de «APK mod».*
Promete «lo de pago, gratis». Cambia el archivo original por uno propio, le mete publicidad, rastreadores y a veces algo peor. Se reconoce porque no tiene repositorio, no tiene autor y su sección «VIP» cobra por bajar más rápido algo que dice ser gratis.

*Categoría 2 — El canal de Telegram.*
Lo más común en República Dominicana y en medio mundo. Un archivo, un mensaje, cero trazabilidad. El que lo subió no firma y no responde. No digo que todo lo que se comparte ahí sea malo: digo que no hay forma de saberlo, y eso es el problema.

*Categoría 3 — El «premium desbloqueado».*
Casi siempre es una app reempaquetada: misma cara, distinto cuerpo. La forma de detectarlo es el tamaño. Una app de 80 MB que pesa 12 MB no está optimizada: está incompleta. Una app de 3 MB que promete «todas las funciones» de una de 80 MB no es la app.

*Categoría 4 — El nombre prestado.*
Ponerle a un archivo el nombre y el icono de una app famosa. Es el truco más viejo y el que más funciona. Si el icono es idéntico y el nombre es idéntico pero el tamaño o el autor no coinciden, no es la app.

*Categoría 5 — El «optimizador».*
Apps que prometen acelerar el teléfono, limpiar la RAM o «enfriar el procesador». En Android moderno no hacen nada bueno y casi siempre piden permisos que no necesitan. El teléfono ya administra su memoria; lo que hace falta es desinstalar lo que no usas.

*Las cinco señales de alarma, en una lista que puedes repetir de memoria:*

*1.* No hay repositorio ni autor con nombre.
*2.* No dice la versión de la app original ni la fecha del archivo.
*3.* Te pide desactivar Play Protect «porque es un falso positivo».
*4.* Tiene sección premium o de pago dentro de algo que prometió ser gratis.
*5.* El tamaño no cuadra con lo que la app dice ser.

*Cinco señales. Con dos que aparezcan, no instales.*

───────────────────

*LOS SIETE ERRORES QUE YO COMETÍ (y que tú puedes no repetir)*

Esto no es una lista de consejos abstractos: son errores que cometí midiendo el ecosistema, con la corrección que cada uno exigió.

*Error 1 — Buscar la palabra «MIT» en todo el README.*
Marcó como MIT una lista que en su sección License decía CC BY-SA 3.0. El «MIT» aparecía dentro de una tabla de apps. *Corrección:* leer primero la sección de licencia; si hay varias candidatas, declarar la ambigüedad en vez de elegir la primera.

*Error 2 — Leer el README por la API equivocada.*
La API de GitHub, sin la cabecera que pide el archivo en crudo, devuelve un JSON con el texto en base64. Resultado: el texto de la licencia no se encontraba y se firmaba una ausencia falsa. *Corrección:* pedir siempre el archivo en crudo.

*Error 3 — Descartar los 404 en silencio.*
Un barrido de mil repos tira los que no existen y sigue. Eso perdía el dato más valioso: *el proyecto está muerto*. *Corrección:* un 404 se registra como muerto, con su fecha. Un 403 o un 429 nunca: significan que el servidor no me dejó preguntar, no que el proyecto no exista.

*Error 4 — Creer que un sello firmado sigue valiendo.*
Un archivo sellado deja de valer en cuanto se re-sella. Si publicas un cambio y no vuelves a firmar, la firma que tienes corresponde al estado anterior. *Corrección:* firmar después de cada cambio, y verificar el digest del archivo contra el que la firma declara.

*Error 5 — Sellar solo lo que debía existir.*
Mi sello cubría los archivos que había cuando se creó. Un archivo *nuevo* entraba al repositorio sin firma y las herramientas seguían diciendo «todo bien». *Corrección:* comparar el conjunto de disco con el del manifiesto: las altas y las bajas se cantan, no solo las alteraciones.

*Error 6 — Escribir un quiz cifrado a mano.*
Salió ilegible e invertido. *Corrección:* generarlo con código y verificarlo descifrándolo con un script antes de publicarlo. El de esta pieza está verificado así.

*Error 7 — Fechar con UTC.*
Un empuje de las 9 de la noche en Santo Domingo aparece con fecha del día siguiente. Si el texto dice «hoy», se está firmando un día que todavía no llegó para el lector. *Corrección:* fechar con la zona de la casa, y avisar cuando una fecha de la API pertenece a otro día.

*Por qué cuento mis errores en una guía de tiendas:* porque la vara que te estoy pidiendo que uses no vale nada si el que la usa no la aplica a sí mismo. Un archivo que no se corrige a sí mismo es propaganda.

───────────────────

*EL RELOJ — lo que viene en 2027*

Desde el 30 de septiembre de 2026, Google pide verificación de desarrollador para instalar apps en Android en varios países, y la lista de países crece. La fecha que de verdad cambia las cosas para nosotros es *2027*, cuando ese requisito se extienda del todo.

Qué significa, sin alarmismo:

• *Para el que instala:* más pasos en el teléfono para permitir una instalación fuera de las tiendas. No es el fin del sideloading: es un peaje nuevo.
• *Para el que desarrolla:* más trámite para publicar, y los proyectos chiquitos son los que más lo sufren.
• *Para este archivo:* que cualquier guía de instalación caduca más rápido. Por eso cada pieza lleva fecha, y cada dato lleva su edad escrita al lado.

Mi opinión, que para eso estás leyendo: el ecosistema libre no se salva por una tienda, se salva porque hay varias y porque el código está a la vista. Si F-Droid desapareciera mañana, su índice se podría replicar; si desapareciera Google Play, no quedaría nada que replicar. Esa asimetría es la razón por la que escribo esto.

───────────────────

*PREGUNTAS QUE ME HACEN DE VERDAD*

*«¿Cuál es la mejor tienda?»*
F-Droid, si tu prioridad es que alguien haya verificado. Obtainium, si tu prioridad es tener la última versión. No hay una respuesta única porque no hay una sola necesidad. Quien te dé una sola respuesta para todos los casos te está vendiendo algo.

*«¿Instalar APKs es legal?»*
Instalar software en tu propio teléfono es legal en casi todo el mundo. Lo que puede ser ilegal es el contenido: una app pirateada, un juego crackeado. El software libre es legal por definición: su licencia te da permiso explícito de copiarlo y compartirlo.

*«¿Me pueden hackear por instalar un APK?»*
Sí, exactamente igual que te pueden estafar por teléfono. El vector no es el formato del archivo: es el origen. Un APK de F-Droid pasó por una reconstrucción y una firma; un APK de un grupo de WhatsApp no pasó por nada. La probabilidad no es la misma ni de lejos.

*«¿Necesito rootear?»*
No. Nada de esta guía requiere root. Y si alguien te dice que para instalar una tienda hace falta root, te está vendiendo un servicio que no necesitas.

*«¿Por qué F-Droid tarda tanto en actualizar?»*
Porque compila. Cada versión se reconstruye desde el código en su infraestructura antes de publicarse. Ese retraso es el precio de la verificación, no un descuido.

*«¿Puedo tener dos tiendas a la vez?»*
Sí, y es lo normal: F-Droid para lo libre, Aurora para lo que solo está en Play. Conviven sin problema. Lo que no conviene es tener cinco: cada tienda es una puerta más que mantener.

*«¿Qué hago si una app que uso desaparece de la tienda?»*
Nada urgente. Lo que ya tienes instalado sigue funcionando. Lo que no debes hacer es actualizarla desde otro sitio a ciegas: si desapareció del catálogo por un problema, ese problema no se resolvió bajándola de un canal de Telegram.

*«¿Las apps libres son feas?»*
Mira la ficha de arriba: Fossify, GrapheneOS Camera, Kvaesitso. La fealdad del software libre es un recuerdo de 2012. Lo que sí es cierto es que hay menos apps libres con diseño pulido, porque nadie paga por hacerlas.

*«¿Y si la app que necesito no existe en libre?»*
Entonces usa la privativa, con los ojos abiertos. Esta guía no es una religión: es una vara. Hay cosas que solo existen en Play y usarlas no te hace peor persona; lo que te hace vulnerable es no saber qué estás usando.

*«¿Por qué tanto texto para decir "instala F-Droid"?»*
Porque «instala F-Droid» no es una respuesta: es un eslogan. La respuesta es que sepas por qué, y que puedas comprobarlo sin mí. Eso no cabe en una línea.

───────────────────

*MITOS QUE SE CAEN SOLOS*

*«Si es gratis, es que te están robando los datos».*
Falso como regla general. El software libre es gratis porque su licencia lo permite, no porque te cobre en datos. Lo que sí es cierto es que *«gratis» en una vitrina de mods* casi siempre significa que el pago eres tú.

*«Los APKs son de piratas».*
Los APK son el formato de instalación de Android. Todo lo que tienes instalado en el teléfono —WhatsApp, el banco, la calculadora— llegó en un APK. La palabra no es el problema; el origen sí.

*«Más estrellas, más seguro».*
Hoy mismo medí `RikkaApps/Shizuku` con ★32.552 y 500 días sin empujar, y `GrapheneOS/AppStore` con ★624 y un empuje de hoy. La seguridad se mide en quién firma y qué tan rápido responde, no en popularidad.

*«Los teléfonos viejos no aguantan nada».*
Aguantan casi todo si no les metes veinte apps. Un teléfono de 2018 con seis apps bien elegidas funciona mejor que uno de 2024 con sesenta.

*«Actualizar siempre es bueno».*
Actualizar es bueno cuando la actualización arregla algo y viene de la misma fuente. Actualizar porque el teléfono lo pide, desde donde sea, es la forma más común de meterse un problema en casa.

───────────────────

*CASOS DEL BARRIO — cuatro decisiones, cuatro resultados*

*El del colmado.* Le instalaron una «tienda» con cuarenta apps. Solución: desinstalar todo lo que no reconoce, poner Neo-Store, explicarle una regla. Resultado: el teléfono le dura el día entero y no ha vuelto a quejarse.

*La estudiante.* Quería una app de notas que sincronizara. En F-Droid encontró tres; eligió la que tenía más rastreadores declarados como cero y mejor historial de releases. Resultado: hace lo mismo que la app de pago que le recomendaron, sin cuenta y sin nube.

*El técnico del barrio.* Instalaba APKs de todo el mundo y «funcionaban». Un día uno no funcionó y no supo de dónde había salido. Solución: desde ese día, cada APK que instala lo baja él del repositorio del proyecto. Resultado: tarda cinco minutos más y puede responder cuando algo falla.

*El que volvió del mod.* Seis meses con un WhatsApp modificado, anuncios en el bloqueo, batería a la mitad. Solución: copia de chats, desinstalar, oficial desde Aurora, restaurar. Resultado: perdió dos horas y recuperó el teléfono.

*Ninguno de los cuatro necesitó root, ni conocimientos de programación, ni un curso.* Ese es el punto de todo esto.

───────────────────

*PERFILES — qué hacer según quién eres*

*Si eres el que arregla los teléfonos de la familia:* no les instales diez cosas. Instala tres y dales una regla. La regla que se repite es la que se recuerda.

*Si eres el que quiere control total:* tu riesgo no es rootear: es la cantidad de módulos de fuentes distintas. Cada módulo tiene permisos de sistema. Aplica la vara con más razón, no con menos.

*Si eres el que solo quiere que el teléfono funcione:* F-Droid, Neo-Store, y nada más. Con eso ya estás mejor que el 90 % de los teléfonos del barrio.

*Si eres el que publica o comparte APKs:* nunca compartas uno que no puedas rastrear hasta su repositorio. Un archivo suelto en un grupo es una cadena que se rompe en el primer eslabón, y el que la recibe no tiene cómo saberlo.

───────────────────

*EL VIAJE DE UNA APP — del código a tu teléfono, en cinco estaciones*

Esto explica por qué F-Droid tarda y por qué un mod tarda cero. Si entiendes el viaje, entiendes todo lo demás.

*Estación 1 — El código.* El desarrollador escribe el programa y lo publica en un repositorio. Ahí está todo: lo que hace, lo que pide, lo que envía. Mientras esté en el repositorio, cualquiera puede leerlo. Ese es el único momento en que el software es realmente auditable.

*Estación 2 — La construcción.* Alguien toma ese código y lo convierte en un archivo instalable. Esa conversión se llama compilar y produce un APK. Aquí hay una bifurcación que lo cambia todo: *si lo compila el desarrollador, confías en el desarrollador; si lo compila un tercero, confías en el tercero*. F-Droid compila por su cuenta, en su infraestructura, para no tener que confiar.

*Estación 3 — La firma.* El APK se firma con una llave. Esa llave es la identidad del paquete: mientras sea la misma, Android acepta las actualizaciones; si cambia, te obliga a desinstalar. Por eso una app que cambia de firmante es una app nueva, aunque se llame igual.

*Estación 4 — La publicación.* El APK firmado se pone donde la gente lo pueda bajar: un release de GitHub, un índice de F-Droid, una tienda, un canal. Aquí es donde se rompe la cadena en el 90 % de los casos que salen mal: el archivo llega a un sitio donde nadie dice quién lo puso.

*Estación 5 — La instalación.* Tu teléfono verifica la firma, comprueba que el paquete no tenga conflictos y lo instala. Si venía de otro firmante, se niega. Esa negativa es la última defensa del sistema, y es la razón por la que cambiar de tienda a mitad de camino a veces obliga a empezar de cero.

*Dónde se pierde la trazabilidad:* entre la estación 4 y la 5, cuando alguien toma el archivo y lo reparte por su cuenta. Ahí ya no hay repositorio, no hay firma reconocible y no hay autor. Y es exactamente donde vive el 90 % de los APKs que circulan por WhatsApp.

───────────────────

*LAS SIETE PREGUNTAS QUE HAY QUE HACERLE A CUALQUIER TIENDA NUEVA*

Esto sirve para cualquier tienda que aparezca el año que viene, incluso para las que todavía no existen. Siete preguntas, y con las respuestas se decide en cinco minutos.

*1. ¿Dónde está el código?* Si no hay repositorio público, no hay auditoría. Puede ser una tienda honesta y aun así no ser verificable. Sin repositorio, la respuesta es «confianza ciega».

*2. ¿Quién firma los APKs?* Tres respuestas posibles y todas distintas: «el desarrollador», «nosotros, recompilando» o «nosotros, tomando el archivo que nos mandan». La primera y la segunda son legítimas; la tercera es la más común y la que menos garantiza.

*3. ¿De dónde saca las apps?* Si la respuesta es «de los releases oficiales de cada proyecto», bien. Si es «de donde las encontramos», es un agregador, no una tienda.

*4. ¿Con qué licencia se publica la propia tienda?* Una tienda que distribuye software libre y no publica su código bajo licencia libre tiene una coherencia pendiente. No es delito, es una señal.

*5. ¿Cómo se mantiene?* Si es gratis y no hay publicidad, ni donaciones, ni una empresa detrás, pregúntate quién paga el servidor. A veces la respuesta es buena —una persona con tiempo y ganas— y a veces es la respuesta que no quieres oír.

*6. ¿Qué hace cuando se equivoca?* Busca su historial público: ¿alguna vez retiró una app por un problema de seguridad y lo dijo? Un proyecto que nunca se ha equivocado en público no es perfecto: es opaco.

*7. ¿Cuándo fue la última vez que alguien miró?* Fecha del último commit y del último release. Si las dos son de hace un año, la tienda es un archivo, no un servicio.

*Las siete juntas tardan lo que tarda un café.* Y sirven para cualquier cosa que te aparezca en el teléfono, no solo para tiendas.

───────────────────

*TABLA DE DECISIÓN*

```
Lo que quiero                        | Lo que uso              | Lo que pago
-------------------------------------|-------------------------|----------------------------
Que alguien haya verificado la app   | F-Droid                 | Tiempo de espera
Lo que F-Droid no acepta todavía     | IzzyOnDroid             | Un estándar más flojo
Un cliente rápido y bonito           | Neo-Store / Droid-ify   | Nada
Una app que solo vive en Play        | Aurora Store            | Paciencia o identidad
Última versión, sin intermediarios   | Obtainium               | La verificación de un tercero
Descubrir proyectos nuevos           | komi-store / Orion      | Criterio propio
Apps del ecosistema GrapheneOS       | GrapheneOS AppStore     | Catálogo chiquito
Apps que usan Shizuku                | yuki + ShizuStore       | Permisos de núcleo
Muchas apps, poca revisión           | Appteka                 | La revisión que no existe
Un APK dividido que no instala       | AntiSplit-M             | Cinco minutos
Instalar con opciones avanzadas      | InstallerX-Revived      | Saber lo que haces
Bajar APKs por consola               | APKeep                  | Ninguno
«Lo de pago, gratis»                 | NADA                    | Tu teléfono
```

───────────────────

*SI ALGO FALLA — respuestas concretas*

*«App no instalada» o «paquete inválido».*
Casi siempre es un APK dividido o una firma distinta. Prueba *AntiSplit-M* para unirlo. Si la app ya estaba instalada y viene de otra fuente, tendrás que desinstalar antes (y perder datos).

*«Play Protect no me deja instalar».*
Play Protect a veces marca apps libres sin razón. Puedes desactivarlo temporalmente desde Play Store → perfil → Play Protect. Hazlo solo si sabes de dónde viene el archivo: si viene de F-Droid, es un falso positivo conocido; si viene de un grupo de Telegram, no lo desactives: no instales.

*«F-Droid no me muestra una app que existe».*
Actualiza los repositorios a mano desde el menú. Si sigue sin aparecer, probablemente vive en IzzyOnDroid y no lo tienes añadido.

*«Obtainium dejó de detectar las actualizaciones».*
Cambió el patrón del nombre de los archivos en el release. Edita la regla de esa app en Obtainium o espera a que el desarrollador vuelva a su esquema. No es un fallo de Obtainium: es que el proyecto cambió de costumbre.

*«La app de Shizuku no arranca».*
Shizuku se apaga en cada reinicio: hay que volver a activarlo. No es un error, es su diseño: presta permisos, no los da.

*«El teléfono va lento después de instalar una tienda».*
Poco probable que sea la tienda. Mira cuántas apps tienes y cuántas se inician solas. En Android, Ajustes → Aplicaciones → ver por uso de batería te dice más que cualquier «optimizador».

───────────────────

*CÓMO SE MIDIÓ ESTA PIEZA (y qué no promete)*

Todo lo que tiene número aquí salió de una consulta a la API de GitHub hecha el sábado 31 de octubre de 2026, o de leer el sitio del proyecto ese mismo día. Nada está copiado de otra pieza, y nada está estimado a ojo.

*Lo que medí:* estrellas, fecha del último empuje, licencia que el repositorio reconoce, lenguaje principal, última release y su fecha, para 14 aplicaciones y 12 tiendas. Y el texto de dos sitios oficiales (Appteka y Orion) para contrastar lo que declaran con lo que su repositorio dice.

*Lo que no medí:* no instalé ninguna de estas apps en un teléfono limpio para cronometrar su comportamiento. No analicé los APK con un desensamblador. No verifiqué las firmas criptográficas una por una. Eso está fuera de lo que esta pieza hace, y lo digo antes de que alguien lo descubra por su cuenta.

*Lo que puede cambiar mañana:* todo. Las estrellas suben, los proyectos se archivan, las licencias se aclaran o se ensucian. Por eso cada dato lleva fecha, y por eso esta pieza no dice «es así»: dice «esto es lo que había el 31 de octubre de 2026, medido así».

*La regla de la casa, dicha una vez más:* si un dato está viejo, se dice su edad; si no hay dato, se dice que no hay. Lo demás es relleno.

───────────────────

*GLOSARIO PARA EL QUE LLEGA NUEVO*

• *APK* — el archivo instalable de Android: un ZIP con la app dentro y una firma encima.
• *Firma* — la huella criptográfica de quien empaquetó. Si cambia, Android te obliga a desinstalar.
• *Sideloading* — instalar fuera de la tienda oficial. Es una opción del sistema, no un delito.
• *Repositorio* — donde vive el código y su historia. Sin repositorio no hay nada que auditar.
• *Espejo* — copia de un repositorio en otra plataforma. El espejo no es la casa.
• *Release* — la versión publicada. Puede ser más vieja que el código: hay proyectos que publican por otros canales.
• *Dormido* — sin empujes recientes pero vivo. La casa lo marca a partir de 45 días.
• *Archivado* — el proyecto no se moverá más, pero puede seguir funcionando años.
• *Muerto* — el repositorio responde 404. Se dice con fecha o no se dice.
• *Rastreador* — biblioteca que envía datos a un tercero. Neo-Store te dice cuántos trae cada app.
• *Shizuku* — puente que presta permisos de sistema sin root y muere en cada reinicio.
• *Repackaging* — tomar una app ajena, modificarla y publicarla como si fuera. La base del mod anónimo.

───────────────────

*MINI-QUIZ*

*1.* ¿Qué dos repositorios que se llaman casi igual existen, y cuál está muerto hoy?

*2.* ¿Cuál es la diferencia entre *dormido* y *abandonado* según la vara de esta casa?

*3.* ¿Qué app de las medidas hoy tiene ★13.832 y una «última release» de 2018 sin estar muerta?

*4.* ¿Qué significa que una licencia sea NOASSERTION?

*5.* ¿Cuántos días lleva sin empujar el repositorio que presta permisos sin root a media Android?

*Respuestas al revés (léelas de atrás para adelante):*

1. REV|grebedoC se erdam asac us y oviv átse tneilc/yfi-diorD ;404 noc otreum átse tneilc/yfidiord
2. REV|ajocer ol neiuq yah on ay sámeda odnauc se odanodnaba ;oviv orep setneicer sejupme nis se odimrod
3. REV|8102 ed se buHtiG artseum euq esaeler al y sonrutcon selanac rop acilbup :riahcnwal/rehcnuaLriahcnwaL
4. REV|etimrep éuq ebas es on orep ,rasu edeup es ppa al :oirotisoper le ne aralc aicnecil anu econocer on buHtiG euq
5. REV|nedneped sodot euq led radnátse le se ísa nua y ,5202 ed oinuj ed 81 le edsed ,saíd 005

───────────────────

*ENLACES DE ESTA PIEZA*

*Tiendas:*
https://f-droid.org
https://apt.izzysoft.de/fdroid
https://accrescent.app
https://github.com/RookieEnough/Orion-Store
https://github.com/NeoApplications/Neo-Store
https://github.com/Droid-ify/client
https://gitlab.com/AuroraOSS/AuroraStore
https://github.com/GrapheneOS/AppStore
https://github.com/ImranR98/Obtainium
https://github.com/komi-store/komi-store
https://appteka.store

*Apps y herramientas de la ficha:*
https://github.com/FossifyOrg/Gallery
https://github.com/FossifyOrg/Messages
https://github.com/FossifyOrg/Phone
https://github.com/FossifyOrg/File-Manager
https://github.com/FossifyOrg/Voice-Recorder
https://github.com/GrapheneOS/Camera
https://github.com/GrapheneOS/PdfViewer
https://github.com/MM2-0/Kvaesitso
https://github.com/LawnchairLauncher/lawnchair
https://github.com/NeoApplications/Neo-Launcher
https://github.com/georgeclensy/Escape-Launcher
https://github.com/iamrasel/lunar-launcher
https://github.com/Goodwy/Gallery
https://github.com/Goodwy/PlayBook
https://github.com/AbdurazaaqMohammed/AntiSplit-M
https://github.com/wxxsfxyzm/InstallerX-Revived
https://github.com/EFForg/apkeep

*Mundo Shizuku y listas:*
https://github.com/RikkaApps/Shizuku
https://github.com/iamr0s/Dhizuku
https://github.com/timschneeb/ShizuStore
https://github.com/carlelieser/yuki
https://github.com/timschneeb/awesome-shizuku
https://github.com/Psyhackological/AAA
https://github.com/moneytoo/awesome-fdroid
https://github.com/krishna3163/best-root-apps-for-android
https://fmhy.net/mobile

*Para verificar por tu cuenta:*
https://reports.exodus-privacy.eu.org
https://developer.android.com/developer-verification

───────────────────

*CIERRE*

Si te quedas con una sola frase de todo esto, que sea esta: *el problema nunca fue la tienda, fue el origen*. Cualquier tienda de esta lista puede fallar mañana; lo que no puede es sorprenderte mintiendo sobre lo que es, porque todo lo que dicen se puede ir a comprobar.

Y si algún día alguien te manda un APK por WhatsApp y te dice «es el mismo pero mejor», ya sabes lo que hay que preguntar: *¿quién lo firma?* Si la respuesta tarda más de dos segundos, la respuesta es nadie.

💓 *La Bandita · sábado 31 de octubre de 2026.* Pieza 01 de Facebook. Medí hoy 33 repositorios —12 casas, 14 apps de la ficha y las herramientas— y 39 enlaces: los 33 están vivos y los 39 responden. Los números de esta pieza son de esta mañana y llevan su fecha al lado. Lo que no medí, está dicho arriba como no medido.
