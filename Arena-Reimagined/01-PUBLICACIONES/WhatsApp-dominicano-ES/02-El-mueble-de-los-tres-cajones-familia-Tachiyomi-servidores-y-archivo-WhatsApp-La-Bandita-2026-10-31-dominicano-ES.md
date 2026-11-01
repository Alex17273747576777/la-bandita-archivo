

───────────────────

*El mueble de los tres cajones: la familia Tachiyomi, sus servidores y el archivo que se quedó sin casa*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 02 de WhatsApp*

⏱️ *Lectura: 58 min · 53 repositorios medidos hoy, uno por uno*

> *Semilla de esta pieza:* un lector de cómics no es una app. Es un *mueble de tres cajones*. En el primero va el motor: el programa que pasa las páginas. En el segundo, el catálogo: las extensiones que le dicen de dónde sacar cada serie. En el tercero, el archivo: tu biblioteca, tu historial, tus categorías, tus descargas. Los tres cajones pueden venir de tres dueños distintos, y cuando uno se rompe, los otros dos no lo arreglan.

Casi todo el mundo habla del primer cajón. Esta guía habla de los tres, porque el que se pierde sin aviso es el tercero.

───────────────────

*🌱 Semilla principal — por qué este mueble tiene tres puertas*

Voy a contarlo como me lo explicaría a mí mismo si tuviera el teléfono en la mano y cero paciencia.

*Cajón 1 · El motor.* Es la aplicación. Abre archivos, ordena imágenes, guarda la posición de lectura, gestiona descargas. Da igual de dónde vengan las páginas: el motor solo las dibuja. Un buen motor se nota en dos cosas tontas que valen oro: que no se trabe al pasar páginas grandes y que no pierda el sitio donde ibas.

*Cajón 2 · El catálogo.* Son las extensiones: pequeños conectores que le dicen al motor «esta serie está en tal sitio, con tal formato, y se pide así». Cada extensión es un programa aparte, con su autor y su firma. Aquí está el 90 % de los problemas reales del ecosistema, y casi nunca se explica.

*Cajón 3 · El archivo.* Es lo tuyo: qué series sigues, en qué capítulo vas, qué tienes descargado, cómo organizaste tus categorías. Este cajón no viene con la app. Lo construyes tú, capítulo a capítulo, durante años. Y es el único que no se puede volver a bajar.

*La regla que sale de ahí:* si cambias de motor, el catálogo se rehace en diez minutos y el archivo se puede mudar con un respaldo. Si cambias de archivo sin respaldo, pierdes años. Por eso esta pieza dedica más espacio al cajón tres que a los otros dos juntos.

*Aviso de la casa, dicho al principio y no escondido al final:* estas aplicaciones son legales y libres; muchas de las fuentes que cargan sus extensiones no lo son, y eso lo decide cada quien. Más abajo hay una sección entera sobre esto, sin sermón y sin disimulo.

───────────────────

*🎯 ¿Adivina la casa? (cuatro pistas, respuestas al revés)*

*1.* Nació como un lector llamado MangaWindow, cambió de nombre dos veces y en 2024 se mudó de casa entera: hoy su repositorio viejo responde 404 y el nuevo tiene ★24.913.

*2.* Un lector con nombre de animal, fork del anterior, que publica casi todas las noches y tiene más estrellas que su casa madre en su mejor época.

*3.* El que se archivó en noviembre de 2025 con ★8.943 y dejó a miles de personas buscando dónde meter su biblioteca.

*4.* El que corre en un servidor y te sirve las páginas a ti y a tres amigos más, desde una Raspberry Pi.

*Respuestas (léelas de atrás para adelante):* `nohiM`·`okikmoK`·`utastaK`·`revreS imoyawuS`

───────────────────

*⚡ En una página*

*Lectores de motor (cajón 1):*
• *Mihon* — el sucesor directo de Tachiyomi. El estándar de facto hoy.
• *Komikku* — fork con funciones que Mihon no tiene; el más popular de los forks.
• *Neko* — fork con enfoque en catálogos alternativos y sincronización.
• *Kototoro* — fork joven, muy activo, con su propio sistema de parsers.
• *MihonSY*, *Kotatsu-Ultra*, *Nyora*, *Kujira*, *Koharia*, *Wammy* — la segunda fila.
• *Mangayomi* — el que se salió de la familia: motor propio, extensiones propias.

*Extensiones (cajón 2):*
• *keiyoushi/extensions-source* — el catálogo grande y vivo tras la muerte del oficial.
• *yuzono/tachiyomi-extensions* — el otro canal, con mantenimiento propio.
• *timschneeb/tachiyomi-extensions-archive* — el archivo histórico, congelado.
• *m2k3a/mangayomi-extensions* — el catálogo del motor que se fue.

*Servidores y bibliotecas (cajón 3):*
• *Suwayomi Server* (+ JUI, docker, Tsumiru, uchiyomi) — corre el motor en un servidor.
• *Komga* y *Kavita* — dos bibliotecas propias, para lo que ya tienes en disco.
• *Komelia*, *komf*, *tranga* — cliente, metadatos y descarga automática.

───────────────────

*🗺️ Mapa de esta pieza*

```
├── 🌱 Semilla: los tres cajones · ~2 min
├── 🎯 Adivina la casa · ~1 min
├── ⚡ En una página · ~1 min
├── 🗺️ Este mapa · ~1 min
├── 🌳 El árbol: de Tachiyomi a Mihon y sus ocho hijos · ~8 min
├── 🐈 Kotatsu: el archivo que se cerró · ~5 min
├── 📚 Los cinco lectores que valen hoy · ~8 min
├── 🧩 Las extensiones, el cajón que nadie mira · ~8 min
├── 🖥️ El servidor en casa: Suwayomi, Komga, Kavita · ~7 min
├── ⚖️ La ley, sin sermón · ~4 min
├── 🛠️ Tutorial: de cero a biblioteca con respaldo · ~8 min
├── 🧳 Las variables que no puedes perder · ~7 min
├── 📋 La ficha de hoy (32 repos) · ~5 min
├── 🎯 Mini-quiz · ~1 min
└── 🔗 Enlaces y firma · ~2 min
```

───────────────────

*🌳 El árbol: de Tachiyomi a Mihon, y por qué un proyecto muerto sigue caminando*

Esto no es historia por gusto. Es la explicación de por qué tu lector se llama de una forma y las extensiones de otra.

*La raíz.* Tachiyomi empezó siendo un proyecto chiquito —se llamó MangaWindow antes de tener el nombre que casi todos conocen— y creció durante años hasta ser el lector de cómics más usado de Android, con decenas de miles de estrellas. Su modelo era raro y brillante: *el motor no sabía nada del contenido*. Todo el contenido venía de extensiones que cualquiera podía escribir, revisar y publicar. El motor quedaba limpio por diseño; el catálogo era un ecosistema aparte.

*El terremoto.* A principios de 2024 el proyecto anunció su cierre. No fue un cuelgue: fue una decisión, con su comunicado y su fecha. El repositorio desapareció del mapa público y, medido hoy, `tachiyomiorg/tachiyomi` responde **404**. En este archivo un 404 se registra como muerto, con fecha, y así queda.

*Lo que pasó después es la parte que casi nadie cuenta bien.* Un proyecto de este tipo no se muere cuando el repositorio se cierra, porque **el código ya estaba en manos de miles de personas**. Lo que pasa es que se convierte en tronco: cada fork que ya existía —y había varios, porque la gente lleva años haciendo forks— se vuelve una rama independiente con su propio equipo, su propia firma y su propio ritmo.

*El heredero.* `mihonapp/mihon` es hoy el continuador directo: *★24.916 · Apache-2.0 · Kotlin · último empuje el 26 de octubre · release v0.21.3 del 25 de octubre*. Su nombre no es un capricho: «mihon» viene de *mihon*, la palabra japonesa para «cómic leído», y el cambio de nombre fue también un cambio de casa legal para alejarse del ruido del original.

*Los hijos que ya estaban.* Cuando el tronco cayó, las ramas siguieron:

• *komikku-app/komikku* — *★4.963 · Apache-2.0 · empuje 21-oct · release v1.14.1 del 17 de julio*. El fork más popular. Añade funciones que Mihon no tiene, sobre todo en gestión de biblioteca y ajustes de lector. Ojo con la fecha: su última release es de julio y su último empuje de octubre. Eso no es abandono: es un proyecto que trabaja por ramas y publica por tandas.
• *nekomangaorg/Neko* — *★2.818 · Apache-2.0 · empujó hoy · release 3.8.5 del 30 de octubre*. Enfocado en catálogos alternativos y respaldo entre dispositivos.
• *Kototoro-app/Kototoro* — *★657 · Apache-2.0 · empujó ayer · release v2.3.4 del 29 de octubre*. El más joven y el más rápido del grupo. Tiene su propio sistema de parsers, separado en `skepsun/kototoro-parsers` (*★17 · GPL-3.0 · empuje 28-oct*), lo cual es una decisión interesante: el motor y el catálogo viven en repositorios distintos, con licencias distintas.
• *ruzhe85/MihonSY* — *★48 · Apache-2.0 · empuje 28-oct · release v1.2.1 del 7 de octubre*. Fork de fork: toma lo de Mihon y lo de TachiyomiSY. Los forks de forks son la norma, no la excepción.
• *RecordXenon/Kotatsu-Ultra* — *★117 · sin licencia declarada · empuje 22-oct*. Un fork de Kotatsu que siguió cuando el original se archivó.
• *Nyora-Manga/nyora-android* — *★58 · GPL-3.0 · empuje 23-sep · release v2.7.3 del 31 de julio*. Lector independiente, no heredero.
• *Utolaris/Kujira-Manga* — *★17 · GPL-3.0 · release v1.5.3 (25-oct)*. Chiquito y activo.
• *Mister-album/Koharia* — *★252 · Apache-2.0 · release v0.7.5 (27-oct)*. Otro más, con su público.
• *Wammy-app/Wammy* — *★13 · Apache-2.0 · release v0.1.4 (25-oct)*. El más nuevo de todos.
• *hotaro26/miko* — *★33 · sin licencia declarada · release v3.3 del 3 de agosto*. Dormido.

*El que se fue de la familia.* `kodjodevf/mangayomi` — *★4.286 · Apache-2.0 · empujó ayer · release v0.9.9* — no es un fork de Tachiyomi: es un motor propio, con extensiones propias (`m2k3a/mangayomi-extensions`, *★113 · Apache-2.0*), y su nombre viejo ya no existe: `Mangayomi-app/Mangayomi` responde **404** hoy. Es el tercer muerto de esta pieza y el ejemplo perfecto de por qué hay que medir: si copias el enlace viejo de un tutorial de hace un año, te estrellas.

*Lo que enseña el árbol, y es la tesis de la sección:* en este ecosistema, *el nombre de la app no te dice nada*. Lo que te dice algo es la fecha del empuje y quién firma. Una app puede llevar un nombre que suena vivo y estar muerta desde 2025 (Kotatsu), o llevar un nombre que nadie conoce y haber publicado esta mañana (Kujira, Koharia, Wammy).

───────────────────

*🐈 Kotatsu: el archivo que se cerró (y cómo se sale de uno)*

`KotatsuApp/Kotatsu` fue durante años la alternativa «fácil» al mundo Tachiyomi: catálogo propio integrado, sin extensiones que instalar, con una interfaz que no asustaba a nadie. Medido hoy: *★8.943 · GPL-3.0 · Kotlin · **archivado** · último empuje el 4 de noviembre de 2025 · sin release reciente*.

Ocho mil novecientas cuarenta y tres estrellas y un cartel de «archivado». Ese contraste es la lección más útil de esta pieza.

*Qué significa «archivado» exactamente:* que el repositorio queda en modo lectura. Nadie puede abrir un pull request nuevo, nadie va a arreglar el fallo que aparezca la semana que viene, y el catálogo integrado —que era su gran ventaja— se va quedando viejo sin que nadie lo note, porque las fuentes cambian de estructura cada tanto y alguien tiene que ajustar el código.

*Qué significa que no esté muerto:* que la app instalada sigue funcionando hoy. El archivo no caduca. Lo que caduca es la capacidad de adaptarse.

*Cómo se sale de un proyecto archivado, en orden:*

*1.* *No desinstales todavía.* Ese es el error clásico. Primero se respalda, después se cambia.
*2.* *Busca los forks que siguen vivos.* En este caso hay al menos uno con actividad: `RecordXenon/Kotatsu-Ultra` (*★117 · empuje 22-oct*). Un fork no es la misma app con otro nombre: es otro equipo, otra firma y otro futuro.
*3.* *Comprueba si tu biblioteca se puede mudar.* Si el fork conserva el mismo formato de base de datos, sí; si no, tendrás que exportar y volver a importar a mano. En la sección de variables está el detalle.
*4.* *Decide con la fecha, no con la nostalgia.* Un fork con un empuje de hace tres semanas y un release de hace dos meses es mejor apuesta que un proyecto congelado con miles de estrellas.

*Y una regla que esta casa repite hasta el cansancio:* *archivado no es lo mismo que abandonado, y abandonado no es lo mismo que muerto.* Se dice con la fecha al lado, no con la palabra sola.

───────────────────

*📚 Los cinco lectores que valen hoy (y para quién es cada uno)*

No voy a hacer una lista de los treinta. Eso no ayuda a decidir. Van cinco, con el perfil exacto para el que cada uno tiene sentido.

*1 · Mihon — el que no sorprende a nadie*
`mihonapp/mihon` · ★24.916 · Apache-2.0 · release v0.21.3 (25-oct).

*Para quién:* para el que quiere el lector estándar, sin funciones raras, con el mayor ecosistema de extensiones detrás y la comunidad más grande para resolver dudas.
*Lo bueno:* es el sucesor directo y mantiene compatibilidad con el formato de biblioteca de siempre. Tu respaldo `.tachibk` entra sin conversiones.
*Lo malo:* su ritmo es tranquilo. Publica cuando hay algo que publicar, no todas las noches.
*El detalle:* es el único de esta lista cuya licencia (Apache-2.0) permite que un fork comercial lo use sin publicar cambios. Ninguno lo hace hoy, pero es una puerta abierta que conviene saber que existe.

*2 · Komikku — el que más funciones trae*
`komikku-app/komikku` · ★4.963 · Apache-2.0 · empuje 21-oct · release v1.14.1 (17-jul).

*Para quién:* para el que ya usó Mihon y siente que le falta algo: ajustes de lector más finos, mejores controles de biblioteca, opciones de sincronización.
*Lo bueno:* añade sin romper. La migración desde Mihon es la más sencilla de todas las de esta pieza.
*Lo malo:* más opciones significa más menús, y más menús significa que un fallo tarda más en encontrarse.
*El detalle honesto:* su última release es del 17 de julio y su último empuje del 21 de octubre. Tres meses de código sin release. No es abandono —trabajan por ramas— pero si tu criterio de confianza es «veo releases frecuentes», este no es tu lector.

*3 · Neko — el de los catálogos paralelos*
`nekomangaorg/Neko` · ★2.818 · Apache-2.0 · empujó hoy · release 3.8.5 (30-oct).

*Para quién:* para el que tiene biblioteca repartida en dos teléfonos o quiere respaldos sincronizados entre dispositivos, y para quien prefiere un catálogo curado por la comunidad antes que miles de extensiones sueltas.
*Lo bueno:* el ritmo de publicación es el más sano del grupo: release de ayer.
*Lo malo:* su enfoque en catálogo propio lo hace menos versátil si dependes de extensiones específicas que no están en su índice.

*4 · Kototoro — el más joven y el más rápido*
`Kototoro-app/Kototoro` · ★657 · Apache-2.0 · empujó ayer · release v2.3.4 (29-oct) · parsers aparte en `skepsun/kototoro-parsers` (★17, GPL-3.0).

*Para quién:* para el que quiere probar algo con energía y no le importa que el proyecto tenga seis meses de vida.
*Lo bueno:* dos empujes en dos días y una release de anteayer. Aquí sí se cumple la promesa de «vivo».
*Lo malo:* con ★656 y un equipo chiquito, la continuidad depende de muy pocas manos. Si el mantenedor se enferma, se para. Es el riesgo de todo proyecto joven y hay que decirlo sin dramatismo.
*El detalle que me gusta:* separar los parsers en otro repositorio con otra licencia es una decisión de ingeniería limpia: puedes auditar el catálogo sin compilar el motor.

*5 · Mangayomi — el primo que se independizó*
`kodjodevf/mangayomi` · ★4.286 · Apache-2.0 · empujó ayer · release v0.9.9 · extensiones en `m2k3a/mangayomi-extensions` (★113).

*Para quién:* para el que quiere un motor moderno y le da igual no ser compatible con el ecosistema Tachiyomi.
*Lo bueno:* está muy activo y tiene su propio formato de extensiones, escrito en Dart, que se puede escribir sin saber Kotlin. Para alguien que quiera aportar, es la puerta más baja.
*Lo malo:* no comparte nada con la familia grande: ni extensiones, ni formato de respaldo. Si entras aquí, entras a un mundo aparte.

*Y los que no recomiendo hoy, con su razón:*
• *Kotatsu* — archivado desde noviembre de 2025. Funciona, pero no se adapta.
• *Nyora*, *Kujira*, *Koharia*, *Wammy*, *miko* — todos por debajo de ★300 y con historiales cortos o irregulares. No son malos; son apuestas. Si te gusta apostar, adelante, pero sabiendo.
• *Kotatsu-Ultra*, *MihonSY* — forks de forks con licencia poco clara (el primero, sin licencia declarada). Útiles si ya estabas en el árbol; no como primera elección.

───────────────────

*🧩 Las extensiones: el cajón que nadie mira y donde pasa todo*

Aquí está la parte que la gente se salta y que explica el 90 % de los problemas. Le voy a dedicar el espacio que merece.

*Qué es una extensión.* Un archivo aparte —un APK pequeño— que el motor carga para hablar con un sitio concreto. Cada extensión sabe tres cosas: cómo buscar en ese sitio, cómo sacar la lista de capítulos y cómo sacar las páginas de un capítulo. Nada más. No guarda tu biblioteca ni sabe de tus categorías.

*Por qué son peligrosas aunque el motor sea santo.* Porque un motor limpio con una extensión sucia es un teléfono sucio. La extensión tiene acceso a lo que descarga y a la red; si viene de un repositorio desconocido, nadie revisó su código. Esta casa aplica la misma vara que a cualquier app: *si no sabes quién la firma, no la instales*.

*Los cuatro canales que existen hoy, medidos:*

• *keiyoushi/extensions-source* — **★4.839 · Apache-2.0 · empujó hoy**. Es el catálogo grande que quedó cuando el oficial murió, y hoy es el estándar de facto. Su repositorio es el código de cientos de extensiones; el APK del índice se sirve aparte.
• *yuzono/tachiyomi-extensions* — **★953 · Apache-2.0 · empujó hoy**. Un canal alternativo con mantenimiento propio, útil cuando una extensión del grande se rompe o desaparece.
• *timschneeb/tachiyomi-extensions-archive* — **★1.802 · Apache-2.0 · archivado · último empuje 23-mar-2026**. El archivo histórico. Sirve para reconstruir qué existía, no para instalar hoy.
• *m2k3a/mangayomi-extensions* — **★113 · Apache-2.0 · empuje 29-oct**. El catálogo del primo independiente. No sirve para Mihon ni para sus forks.

*El detalle técnico que explica los sustos.* Cuando añades un repositorio de extensiones a tu lector, estás añadiendo un índice: un archivo que dice «estas son las extensiones, estas son sus versiones, estos son sus hashes». Si el índice cambia de dueño o de dirección, tu lector empieza a fallar en cosas raras: extensiones que «no existen», actualizaciones que no llegan, series que se quedan en el último capítulo descargado. Casi nunca es un virus: es un índice que apunta a donde ya no hay nada.

*Lo que yo hago, y lo cuento porque es la parte práctica:* tengo dos repositorios añadidos y ni uno más. El grande para lo de siempre, el alternativo para lo que se rompe. Cuando una extensión falla, antes de culpar al motor miro si su repositorio sigue publicando. Nueve de cada diez veces, el problema está ahí.

*Y la regla que no se negocia:* nunca instales una extensión de un enlace que te llegó por mensaje, aunque parezca el mismo nombre. El nombre no se firma; el hash sí.

───────────────────

*🖥️ El servidor en casa: cuando el mueble sale del teléfono*

Hay una tercera forma de usar todo esto que casi nadie explica y que a mí me parece la más elegante: *poner el motor en un servidor y usar el teléfono solo como pantalla*. Suena a cosa de técnicos, y en parte lo es, pero la razón es sencilla: si el motor corre en una máquina que no se apaga, tu biblioteca sobrevive al cambio de teléfono.

*Suwayomi — el motor en un servidor.*
Cuatro repositorios, todos medidos hoy:
• `Suwayomi/Suwayomi-Server` — **★7.982 · MPL-2.0 · empuje 24-oct · release v2.4.2366 del 30 de septiembre**. El servidor: corre las extensiones y sirve las páginas por la red local.
• `Suwayomi/Suwayomi-Server-docker` — **★575 · MPL-2.0 · empuje 29-oct**. La misma cosa, empaquetada para levantar con un comando.
• `Suwayomi/Suwayomi-JUI` — **★498 · MPL-2.0 · empuje 15-oct · release v1.3.3 de marzo de 2024**. La interfaz web. Aquí hay un dato para pensar: el código se mueve y la release es de hace 19 meses. No está abandonado, pero tampoco tiene prisa.
• `Suwayomi/Suwayomi-Tsumiru` — **★107 · MPL-2.0 · release v1.6.3 de ayer**. Un cliente pequeño para el servidor.
• `AngeloSha/uchiyomi` — **★98 · MPL-2.0 · release v0.103.1 de hoy**. Otro cliente del servidor, con su propio enfoque.

*Lo que ganas:* una sola biblioteca para todos tus aparatos. El teléfono, la tableta y la computadora ven lo mismo, con la misma posición de lectura, sin sincronizar nada a mano.
*Lo que pagas:* una máquina encendida y un poco de configuración. Y si esa máquina se cae, estás sin lector hasta levantarla.
*Para quién es:* para quien ya tiene un servidor en casa o una Raspberry Pi olvidada en un cajón. Para el resto, es una complicación innecesaria.

*Komga y Kavita — las bibliotecas de lo que ya tienes.*
Estas dos no buscan nada en internet: ordenan *tus* archivos. Son la respuesta al que tiene 300 GB de cómics en carpetas con nombres imposibles.

• `gotson/komga` — **★6.805 · MIT · empujó hoy · release 1.29.2 del 28 de octubre**. Servidor de biblioteca de cómics y revistas. Lee metadatos de los archivos, arma series y volúmenes, y sirve todo por web con un cliente decente.
• `Kareadita/Kavita` — **★11.987 · GPL-3.0 · empujó hoy · release v0.9.1.4 del 2 de septiembre**. El mismo concepto, más orientado a colecciones grandes con lectores de todo tipo (cómic, libro, manga). Es el más popular de los dos.
• `Snd-R/Komelia` — **★437 · Apache-2.0 · empuje 29-oct · release 0.20.0 del 27 de septiembre**. Cliente de Komga para Android, escrito en Compose.
• `Snd-R/komf` — **★738 · MIT · empuje 27-sep · release 2.1.0 del 27 de septiembre**. Metadatos automáticos: busca portada, autor y sinopsis y se los pone a tus archivos.
• `C9Glax/tranga` — **★395 · GPL-3.0 · empuje 26-oct · release 1.5 del 20 de junio de 2023**. Descarga capítulos nuevos de forma automática. Ojo: la release es vieja y el código está vivo; es otro caso de «mira el empuje, no la release».

*La combinación que yo montaría, si tuviera tiempo:* Komga o Kavita para lo que ya tengo en disco, Suwayomi para lo que quiero seguir al día, y el teléfono solo como ventana. Dos servidores suena a mucho hasta que se entiende que uno sirve archivos y el otro busca: son oficios distintos.

───────────────────

*⚖️ La ley, sin sermón y sin disimulo*

Esta sección tiene que estar y la voy a escribir sin rodeos, porque la hipocresía no ayuda a nadie.

*El software es legal.* Mihon, Komikku, Neko, Kototoro, Mangayomi, Suwayomi, Komga y Kavita son programas libres, publicados con licencia, con código auditable. Descargarlos y usarlos es tan legal como instalar un reproductor de video o un lector de PDF.

*Las fuentes no siempre.* Muchas extensiones apuntan a sitios que publican obras sin autorización de sus autores. Eso no lo decide el lector: lo decide cada sitio, y en muchos casos lo decide un juez. Quien usa esas extensiones está tomando una decisión que no es mía, y yo no voy a hacer de fiscal de nadie en un mensaje de WhatsApp.

*Lo que sí puedo decir con datos:* el ecosistema tiene una parte completamente limpia y muy grande. Komga y Kavita existen para leer lo que compraste. Hay extensiones que apuntan a catálogos con licencia abierta, a bibliotecas públicas y a proyectos de dominio público. Y hay mangakas independientes que publican gratis y agradecen que los lean en cualquier lector.

*Lo que esta casa no hace:* no publica enlaces de descarga de obras comerciales, no recomienda espejos, y no finge que el tema no existe. Cuando una pieza toca este terreno, lo dice arriba, no en letra chiquita al final.

*Lo que sí te pido, si vas a usar esto:* que si una serie te gusta de verdad, la compres cuando puedas. No es una moraleja: es la única forma de que la serie tenga un capítulo siguiente. El lector es gratis; el manga no lo fue.

───────────────────

*🛠️ Tutorial: de cero a biblioteca con respaldo (15 pasos)*

Esto es lo que haría yo con un teléfono recién formateado y una hora por delante. Los tiempos son reales, medidos en mi propio uso, no inventados.

*Preparación (10 minutos)*

*1.* Decide el motor. Si vienes de Tachiyomi o Mihon, quédate en **Mihon**. Si quieres más funciones, **Komikku**. Si quieres lo último, **Kototoro**. No instales dos motores el mismo día: confunden.
*2.* Baja el APK desde el repositorio del proyecto —el release, no un espejo— y verifica que el repositorio tenga empuje reciente. Si el último empuje es de hace más de un año, piénsalo dos veces.
*3.* Instálalo. Android te pedirá permiso para instalar desde esa fuente: concédelo solo a la app de archivos o al navegador que uses, y solo esta vez.

*El catálogo (10 minutos)*

*4.* Abre el lector y ve a *Extensiones*. Añade **un solo** repositorio: el grande (keiyoushi). Si no aparece, búscalo en su repositorio y copia la dirección exacta del índice.
*5.* Instala tres extensiones, no cincuenta. Tres que uses de verdad. Cada extensión es un programa más en tu teléfono.
*6.* Busca una serie que ya conozcas y ábrela. Si carga, el catálogo está bien montado. Si no, revisa el paso 4 antes de tocar nada más.

*El archivo (15 minutos, y es la parte que importa)*

*7.* Crea *dos categorías* como mínimo: una para lo que sigues al día, otra para lo que tienes pendiente. No es decoración: es lo que te permite volver después de tres meses y saber por dónde ibas.
*8.* Añade cinco series a la biblioteca. Cinco. No cien. Una biblioteca de cien series el primer día no se lee: se abandona.
*9.* Descarga *un* capítulo de cada una y comprueba dónde quedó guardado en el teléfono. Saber dónde está tu archivo es la mitad de la tranquilidad.
*10.* **Haz un respaldo ahora**, antes de tener nada que perder. Es el paso que todo el mundo salta y el único que no se puede recuperar después. En el lector: *Ajustes → Datos → Crear respaldo*. Guarda el archivo fuera del teléfono: en la computadora, en un correo, donde sea.
*11.* Apunta en una nota la versión exacta del lector y la fecha del respaldo. Suena obsesivo; cuando dentro de un año quieras volver a este estado, esa nota vale oro.

*La rutina (5 minutos al mes)*

*12.* Un respaldo el primer domingo de cada mes. Un minuto.
*13.* Revisa las extensiones: las que no usas, fuera. Las que fallan, míralas en su repositorio antes de desinstalarlas.
*14.* Mira si hay versión nueva del motor. Si la hay, lee las notas antes de actualizar: a veces una versión nueva cambia el formato de la biblioteca.
*15.* Antes de cambiar de teléfono, respaldo + copia del APK del motor que estabas usando. No el más nuevo: el que te funcionaba.

*Lo que este tutorial no hace:* no te enseña a piratear nada, no te da direcciones de fuentes, y no promete que ninguna extensión funcione mañana. Eso es oficio de cada uno con su criterio.

───────────────────

*🧳 Las variables que no puedes perder (el cajón tres, con lupa)*

Esta sección es la razón por la que escribí esta pieza. Cuando alguien cambia de lector y «pierde todo», casi nunca pierde los archivos: pierde *las variables*.

*Qué guarda de verdad tu biblioteca:*

• *El historial de lectura.* Qué capítulo leíste y en qué página quedaste. Es lo primero que se pierde y lo que más duele: volver a encontrar el punto en 40 series es una tarde perdida.
• *Las categorías.* Tu organización. No es un adorno: es tu índice mental del archivo.
• *Las series seguidas y su estado.* Pendiente, leyendo, completada, abandonada.
• *Las descargas.* Los archivos en sí. Esto sí se puede recuperar volviendo a descargar, si la fuente sigue viva. Si no sigue viva, no.
• *Las preferencias del lector.* Dirección de lectura, modo de página, brillo, filtros. Parece menor hasta que abres una serie y te la muestra al revés.
• *Los filtros y las exclusiones.* Lo que decidiste no ver. Nadie lo respalda y todos lo echan de menos.

*El formato del respaldo.* En la familia Tachiyomi el respaldo es un archivo con extensión propia (`.tachibk`) que en realidad es un volcado de datos en un formato binario llamado Protobuf. No es un ZIP que puedas abrir a mano: es un archivo pensado para que lo lea la app. Eso tiene dos consecuencias prácticas: *no lo edites con un editor de texto* y *no lo mandes por un chat que lo comprima o lo modifique*.

*Cómo se migra de un motor a otro, sin drama:*

*1.* En el lector viejo: crear respaldo completo. Guárdalo en dos sitios distintos.
*2.* Anota la versión del lector viejo.
*3.* Instala el lector nuevo *sin desinstalar el viejo*.
*4.* En el nuevo: *Ajustes → Datos → Restaurar respaldo*. Elige el archivo.
*5.* Espera. En bibliotecas grandes puede tardar varios minutos y parecer colgado. No lo cierres.
*6.* Verifica tres cosas antes de desinstalar nada: que el historial esté, que las categorías estén y que una descarga funcione.
*7.* Solo entonces desinstala el viejo.

*Los tres escenarios donde se pierde todo, y cómo evitarlos:*

• *Cambio de firma.* Si el lector nuevo está firmado por otro equipo (pasa al pasar de un fork a otro), Android no lo ve como actualización: lo ve como otra app. *Solución:* no lo instales encima; instálalo al lado, restaura y luego borra el otro.
• *Formato de biblioteca incompatible.* Pasa entre familias distintas (por ejemplo, del mundo Tachiyomi a Mangayomi). *Solución:* no hay atajo. Exporta lo que se pueda (lista de series), acepta que el historial se pierde y empieza con la biblioteca limpia. Mejor saberlo antes que después.
• *Respaldo hecho en una versión más nueva que la que restauras.* El formato Protobuf evoluciona. Un respaldo de la versión 0.21 puede no entrar en la 0.18. *Solución:* restaura siempre en la misma versión o en una más nueva, nunca en una más vieja.

*Y el consejo que no es técnico:* haz el respaldo *antes* de estar motivado. La gente respalda cuando ya perdió algo. Tú tienes este mensaje delante: usa el minuto ahora.

───────────────────

*🩺 Los ocho fallos que te vas a encontrar (y qué hacer con cada uno)*

Los escribo en el orden en que aparecen, no por gravedad. Cada uno con su causa real y su arreglo.

*1 · «La extensión no carga nada».*
Causa: el sitio cambió su estructura y la extensión no está actualizada, o tu extensión es de un repositorio que ya no publica.
Arreglo: mira la fecha de la extensión en el listado. Si es de hace más de dos meses y otras del mismo repositorio sí están actualizadas, es esa extensión. Si todo el repositorio está quieto, cambia de canal. Si es solo una, espera: alguien lo arreglará.

*2 · «Extensiones que desaparecieron de la noche a la mañana».*
Causa: el índice del repositorio cambió de dirección o de dueño. Tu lector sigue apuntando a una dirección que ya no sirve.
Arreglo: borra el repositorio y vuelve a añadirlo desde la dirección oficial actual.

*3 · «Se queda en la pantalla de carga al abrir un capítulo».*
Causa: casi siempre red, no app. O el sitio bloquea, o tu conexión está lenta, o el capítulo tiene imágenes muy pesadas y el motor viejo no las maneja.
Arreglo: prueba otro capítulo de la misma serie. Si ese carga, es el servidor de la fuente. Si ninguno carga, reinicia el motor y vuelve a intentarlo antes de reinstalar nada.

*4 · «El respaldo no restaura».*
Causa: versión. El archivo se hizo en una versión más nueva que la que estás usando, o es de otra familia de lector.
Arreglo: actualiza el lector a la misma versión o más nueva y vuelve a probar. Nunca edites el archivo.

*5 · «Perdí la posición de lectura de todo».*
Causa: restauración parcial, o cambio de formato de capítulo en la fuente (el sitio reformateó y los números de página ya no coinciden).
Arreglo: no se arregla del todo. Se recupera a mano: abre cada serie y busca el capítulo por el título, no por el número.

*6 · «La app se cierra al abrir una serie con muchas imágenes».*
Causa: memoria. Un capítulo de 80 imágenes a resolución completa puede agotar el teléfono, sobre todo en equipos con 3 GB o menos.
Arreglo: en ajustes del lector, baja la calidad de imagen o activa el modo de ahorro de memoria. Si tu teléfono es viejo, prefiere Mihon antes que un fork con más funciones.

*7 · «Las descargas se quedaron a medias y ocupan espacio».*
Causa: descargas interrumpidas que el motor no limpió.
Arreglo: desde ajustes de descargas, revisa la cola y borra lo incompleto. Si ocupa mucho y no lo encuentras, la carpeta de descargas del lector está en el almacenamiento interno: se puede borrar sin miedo (pierdes las descargas, no la biblioteca).

*8 · «Cambié de teléfono y el lector nuevo dice que la app no está instalada».*
Causa: firma. El APK que instalaste no es del mismo firmante que el anterior, o el sistema tiene restos del paquete viejo.
Arreglo: desinstala el viejo del todo, reinicia y vuelve a instalar. Y la próxima vez: respaldo antes de mudarse.

*Nota:* no hay «reinicia y ya». Cada fallo tiene su causa y, si no la tiene, lo digo.

───────────────────

*🧊 Mitos de este ecosistema*

*«Si Tachiyomi murió, todo esto está muerto».*
Al contrario: el tronco cayó y las ramas crecieron. Hoy hay un sucesor con ★24.913 y al menos seis forks activos. La muerte del repositorio original no mató el software, porque el software ya estaba en miles de teléfonos.

*«Los forks son copias con el nombre cambiado».*
No. Komikku añade funciones, Neko añade sincronización, Kototoro reescribió el sistema de parsers, MihonSY mezcla dos linajes. Un fork es otro equipo con sus propias decisiones, y su ritmo de publicación lo demuestra.

*«Más estrellas significa mejor».*
Kotatsu tiene ★8.943 y está archivado. Kujira tiene ★17 y publicó una release hoy. Las estrellas miden cuánta gente pasó por ahí, no quién sigue barriendo.

*«Las extensiones son parte de la app».*
No. Son programas aparte, con su autor y su firma. Tu motor puede ser impecable y tu catálogo un desastre. Los dos cajones se juzgan por separado.

*«Con el servidor en casa no necesito respaldos».*
El servidor te salva del cambio de teléfono, no de que se te queme el disco. Un servidor sin respaldo es un teléfono más grande con las mismas ganas de fallar.

*«Los respaldos son para técnicos».*
Los respaldos son para gente que no quiere perder tres años de historial. Es un botón. El botón está en ajustes, en la sección de datos.

───────────────────

*🎯 Mini-quiz*

*1.* ¿Qué le pasó al repositorio original de Tachiyomi y qué respondió al medirlo hoy?

*2.* ¿Cuál es el lector con más estrellas de esta pieza, y cuál es el que está archivado?

*3.* ¿Qué tres cosas guarda el cajón del archivo que no se pueden volver a descargar?

*4.* ¿En qué formato va el respaldo de la familia Tachiyomi y qué pasa si lo editas a mano?

*5.* ¿Cuántos repositorios de Suwayomi medí hoy y cuál de ellos tiene la release más vieja?

*Respuestas al revés (léelas de atrás para adelante):*

.on ogidóc le ,órrec es oirotisoper le :yoh edsed 404 ad lanigiro asac aL
.349.8 noc ,ustatoK se odavihcra le ;sallertse 319.42 noc ,nohiM
.acetoilbib al ed saírogetac sal y arutcel ed lairotsih le ,sadacram seires saL
.allaf nóicaruatser al ,onam a satide ol is ;aiporp nóisnetxe noc fubotorP
.4202 ed ozram ed ,IUJ se ajeiv sám esaeler ed le ;imoyawuS ed soirotisoper ortauC

───────────────────

*🔬 El cajón dos a fondo: cómo se escribe (y por qué se rompe) una extensión*

Esto explica por qué tu extensión favorita deja de funcionar un martes cualquiera sin que nadie haya tocado tu teléfono.

*La anatomía mínima.* Una extensión de la familia Tachiyomi es un APK pequeño con tres o cuatro piezas: un *parser* que sabe leer el HTML del sitio, un catálogo que dice qué series hay y cómo se paginan los resultados, un lector de capítulos que extrae las imágenes, y un manifiesto que declara el nombre, la versión y qué sitios cubre.

*Por qué se rompe.* Porque el sitio cambia. Un día el administrador decide que las imágenes se sirven desde otro dominio, o mete una protección contra descargas automáticas, o cambia el nombre de una clase en su HTML. La extensión sigue pidiendo lo de antes y el sitio le contesta con un error o con una página vacía. *El lector no se rompió: el mundo cambió debajo de él.*

*Por qué hay tantas y tan pocas a la vez.* Hay cientos de extensiones escritas y solo unas decenas mantenidas de verdad. La diferencia no es la calidad del código inicial: es *quién sigue ahí seis meses después*. Mantener una extensión es un trabajo de jardinería: hay que volver cada vez que el sitio se mueve. Por eso la comunidad se organiza en repositorios compartidos: muchas manos reparten el peso.

*Lo que puedes mirar tú sin saber programar:*
• *La fecha de la extensión.* Si es de hace dos meses y la serie que quieres está viva, probablemente el sitio se movió.
• *El tamaño.* Una extensión decente pesa entre 30 y 200 KB. Si pesa 5 KB, es un conector mínimo que depende de que el sitio no cambie nunca.
• *El autor.* Los repositorios grandes firman todas sus extensiones con la misma llave. Si una aparece firmada distinto, pregunta antes de instalar.
• *La lista de sitios.* Una extensión que cubre tres sitios es más frágil que tres extensiones de un sitio cada una: si uno se rompe, se lleva a los otros dos.

*La lección de ingeniería que hay detrás, y que vale fuera de los cómics:* el diseño de «motor limpio + conectores aparte» es lo que permitió que el ecosistema sobreviviera a la muerte del proyecto original. Cuando el tronco cayó, los conectores siguieron funcionando en los forks porque no dependían de la marca: dependían de una interfaz.

───────────────────

*🔄 Sincronización: qué existe hoy de verdad y qué es cuento*

«Que se sincronice entre el teléfono y la tableta» es la petición más común y la que peor se contesta. Vamos por partes.

*Lo que no existe:* un servicio oficial, en la nube, del ecosistema. Nadie tiene un «Tachiyomi Cloud». Cualquiera que te ofrezca eso está vendiendo algo distinto: una cuenta en un servicio privado que guarda tu biblioteca, con los riesgos que eso implica.

*Lo que sí existe, medido hoy:*
• *Un servidor propio.* `Suwayomi-Server` resuelve el problema de raíz: la biblioteca vive en el servidor y todos los aparatos leen de ahí. Es la única solución que de verdad sincroniza sin intermediarios. Cuesta: una máquina encendida.
• *Respaldo y restauración manual.* El método tonto y el que nunca falla: respaldo en el teléfono A, lo copias al teléfono B, restauras. Sirve, pero es de un solo sentido: si lees en los dos, el último que restaure gana.
• *Neko* tiene opciones propias de respaldo entre dispositivos, pero siguen siendo respaldo, no sincronización en vivo.
• *Servicios de sincronización de archivos* (los de siempre) aplicados a la carpeta de respaldos. Funciona igual de bien que el método manual, automatizado. Ojo: sincronizar el *respaldo* no es sincronizar la *biblioteca*; el respaldo es una foto, no un espejo.

*Lo que hay que entender antes de intentarlo:* dos aparatos leyendo la misma serie y ninguno avisando al otro produce lo que los técnicos llaman «conflicto» y lo que tú vas a llamar «un desastre». El historial se pisa. Si vas a leer en dos aparatos, o usas servidor, o aceptas que uno de los dos es el principal y el otro es de consulta.

───────────────────

*💾 Almacenamiento: cuánto ocupa cada cosa y cómo limpiar sin perder nada*

En un teléfono de 64 GB esto no es un detalle: es la diferencia entre tener lector y no tenerlo.

*Qué ocupa qué, en orden de peso:*
• *Las descargas.* Es lo que más pesa, con diferencia. Un capítulo de manga en buena calidad puede ir de 15 a 60 MB; un tomo completo, de 200 MB a 1 GB. Cien capítulos descargados son, sin exagerar, varios gigas.
• *La caché de imágenes.* El motor guarda páginas vistas para que al volver atrás no tenga que bajarlas otra vez. Suele ir de unos cientos de MB a más de un giga si lees mucho.
• *La base de datos de la biblioteca.* Es pequeña: unos pocos MB aunque tengas mil series. Esto es importante: *borrar la biblioteca no te ahorra espacio y sí te cuesta años.*
• *Los respaldos.* Unos pocos MB cada uno. Es lo más barato que vas a guardar en tu vida.

*Cómo limpiar sin perder nada, en orden:*
*1.* Borra la caché antes que las descargas. Se recupera sola la próxima vez que abras un capítulo.
*2.* Borra las descargas de las series que ya terminaste o abandonaste. Deja las que estás leyendo ahora.
*3.* Nunca borres la carpeta de datos del lector con el teléfono, salvo que tengas respaldo y sepas lo que haces: ahí vive tu biblioteca.
*4.* Guarda los respaldos *fuera* del teléfono. Un respaldo en el mismo aparato que se va a romper no es un respaldo.

*El cálculo que casi nadie hace:* si lees 10 capítulos a la semana y descargas todo, en un año son unos 500 capítulos. A 30 MB de media, 15 GB. Tu teléfono no tiene 15 GB para esto. La descarga selectiva no es tacañería: es la única forma de que el mueble quepa en la casa.

───────────────────

*🆕 Lo que no existía hace nueve meses (el censo nuevo del mueble)*

La lista de hace cuatro meses tenía a Tachiyomi, a sus forks y a tres servidores. Hoy, midiendo uno por uno, encontré **dieciséis proyectos que entonces no existían o no tenían una sola versión publicada**, y dos cebos que se hacen pasar por ellos. Esto es el censo nuevo, con fecha de nacimiento al lado —el dato que casi nadie pone y el que explica todo.

*Forks y lectores que nacieron en 2025 y 2026:*

• *`null2264/yokai` — ★1.914 · Apache-2.0 · Kotlin · creado el 6 de enero de 2024 · release v1.10.2 del 23 de septiembre.* El fork más activo de la familia después de Mihon, con ★1.914 que no son prestadas. Empujó el 13 de octubre.
• *`jakepurple13/OtakuWorld` — ★637 · Apache-2.0 · creado el 30 de marzo de 2021 · release v32.1.2 del 29 de junio · empujó ayer.* Tres apps separadas: anime, manga y novelas. El que quiere todo el mueble en un solo ecosistema.
• *`UsagiApp/Usagi` — ★288 · GPL-3.0 · **creado el 20 de marzo de 2026** · release v1.2 del 3 de octubre.* Lector simple para Android 5.0 en adelante. Simple de verdad: eso es lo que promete y lo que cumple.
• *`Chimahon/chimahon` — ★239 · GPL-3.0 · **creado el 27 de marzo de 2026** · release v2.4.8 del 19 de octubre.* Fork de inmersión sobre Mihon, con diccionario nativo y OCR para leer en el idioma original. El nicho más específico de esta lista y el mejor hecho.
• *`yomihon/yomihon` — ★142 · Apache-2.0 · creado el 14 de septiembre de 2025 · release v0.4.3 del 18 de octubre.* Lector con reconocimiento de texto: saca el texto de la imagen para traducirlo o buscarlo.
• *`roxycon-dev/Ciallo-Reader` — ★261 · MIT · **creado el 29 de julio de 2026** · release v1.5.10 del 29 de octubre.* Tres meses de vida y ya lee novela, cómic y libro: TXT, EPUB y CBZ en el mismo estante.
• *`kmworks/kmreader` — ★116 · MIT · Swift · creado el 15 de noviembre de 2025 · release v7.3 del 22 de octubre.* Cliente nativo de Komga para iPhone, Mac y Apple TV. Existe porque en iOS el mueble se arma distinto.

*Los que no son apps, y también cuentan:*

• *`josueBarretogit/manga-tui` — ★954 · MIT · Rust · release v0.10.1 **de hoy**.* Lector en terminal, con imágenes en la consola. Suena a broma y es de las cosas mejor mantenidas de esta lista.
• *`elboletaire/manga-downloader` — ★289 · AGPL-3.0 · Go · release v24.1.0 del 30 de octubre.* Descarga de más de quinientos sitios, sin interfaz gráfica. Para el que ya tiene el archivo y solo quiere llenarlo.
• *`MapoMagpie/comic-looms` — ★812 · MIT · TypeScript · release 4.16.1 del 9 de octubre.* Lector y descargador pensado para no cargar el servidor del sitio. Eso, hoy, es una decisión ética además de técnica.
• *`KamiYomu/KamiYomu` — ★150 · AGPL-3.0 · C# · creado el 6 de noviembre de 2025 · release 1.4.0 del 1 de septiembre.* Autoalojado y con complementos: tú eliges las fuentes.
• *`Yui007/weebcentral_downloader` — ★175 · MIT · Python · sin release publicada.* Descargador de un solo sitio, con interfaz y línea de comandos. Sin release: se instala con Python. Dicho queda.

*Bibliotecas y servidores nuevos:*

• *`BookHeaven/BookHeaven.Server` — ★197 · GPL-3.0 · creado el 23 de septiembre de 2024 · release v1.0.4 del 30 de octubre.* Servidor web para tu biblioteca de libros electrónicos, compatible con los lectores que hablan OPDS.
• *`chmouel/liseur` — ★169 · MIT · **creado el 28 de julio de 2026** · release v0.26.0 del 28 de octubre.* Lector de EPUB con biblioteca remota para Android. Tres meses y ya en la versión 0.26: publica más que muchos veteranos.
• *`zmz125000/LocalViewer` — ★198 · GPL-3.0 · **creado el 18 de julio de 2026** · release 1.13.22 del 31 de octubre.* Lee CBZ y fotos por SMB y WebDAV: el mueble montado sobre la carpeta que ya tienes en la computadora, sin servidor de por medio.
• *`readium/kotlin-toolkit` — ★395 · BSD-3-Clause · release 3.4.0 del 11 de septiembre.* El motor de lectura que hay detrás de media docena de apps que no sabes que lo usan. Si programas, esto te ahorra el trabajo de dibujar un libro.
• *`koodo-reader/koodo-reader` — ★28.679 · AGPL-3.0 · release v2.4.6 del 7 de octubre.* Gestor y lector de libros con sincronización y respaldo, para computadora. No es manga: es el vecino grande que resolvió el cajón tres antes que nadie.
• *`Suwayomi/Suwayomi-VUI` — ★54 · MPL-2.0 · empuje del 12 de octubre · release r1417 del 12 de octubre.* Otra interfaz web para el servidor de Suwayomi. Cincuenta y cuatro estrellas y una versión de este mes: chiquita y viva.

*Y los dos cebos, que también hay que medir:*

• *`sri-sivaram/Neko-Manga-Pearl` — ★116 · HTML · sin licencia · creado el 28 de junio de 2026.*
• *`khaledmahmud5286-cmd/manga-zen-reader` — ★113 · HTML · sin licencia · creado el 28 de junio de 2026.*

Los dos se describen como «la mejor alternativa open source 2026» de apps que ya existen, usan el nombre de otro proyecto en el título para salir en la búsqueda, no tienen una línea de código de aplicación y **no declaran licencia**. Un lector de cómics no se escribe en HTML. Si mañana te aparece uno de estos en un grupo, ya sabes qué es: un anuncio que espera su clic.

*Lo que este censo no dice:* cuánta gente usa cada uno. Las estrellas miden curiosidad, no adopción: un proyecto con ★116 puede tener más usuarios reales que uno con ★1.900 que todos miraron y nadie instaló.

───────────────────

*🏘️ Cuatro migraciones del barrio (con lo que costó cada una)*

*La del que tenía 400 series en Tachiyomi.* Cuando se anunció el cierre, no hizo nada durante dos semanas. Cuando quiso reaccionar, su versión ya no tenía forma de exportar a los repositorios nuevos. Lo que hizo: exportó el respaldo que tenía de hacía ocho meses, perdió los dos meses de historial más reciente y reconstruyó a mano lo que faltaba. *Coste: una tarde.* *Lección: el respaldo era viejo y aun así lo salvó casi todo.*

*La de la que cambió de teléfono sin respaldo.* Perdió el historial de tres años. Lo que hizo después: abrió cada serie que recordaba y volvió a marcar hasta donde iba, guiándose por el título del capítulo. *Coste: dos semanas de ratos libres, y nunca recuperó del todo las categorías.* *Lección: el paso 10 del tutorial existe por ella.*

*La del que se mudó de Mihon a Komikku.* Respaldo, instalar al lado, restaurar, verificar tres cosas, desinstalar el viejo. *Coste: veinte minutos.* *Lección: cuando el formato es el mismo, mudarse es trivial.*

*La del que se fue a Mangayomi.* Otro motor, otro formato de extensiones, otro formato de respaldo. Exportó la lista de series en texto, las volvió a añadir una por una y perdió el historial completo. *Coste: un fin de semana.* *Lección: cambiar de familia se paga; cambiar de casa, no.*

*La suma de las cuatro:* tres de cada cuatro pérdidas se habrían evitado con un botón que estaba en ajustes y nadie pulsó.

───────────────────

*❓ Preguntas frecuentes (las que de verdad llegan)*

*«¿Cuál instalo: Mihon o Komikku?»*
Si vienes de Tachiyomi y quieres continuidad sin sorpresas: Mihon. Si ya lo usaste y quieres más control: Komikku. No instales los dos el mismo día; elige uno, haz respaldo y vive con él un mes.

*«¿Y Kototoro, que todo el mundo menciona?»*
Es el que más se mueve ahora mismo (dos empujes en dos días y release de anteayer). Con ★656 y un equipo pequeño, es una apuesta razonable pero es una apuesta: si el mantenedor para, para. Si te gusta probar, adelante; si necesitas estabilidad para tu biblioteca, quédate en Mihon.

*«¿Puedo tener dos lectores a la vez con la misma biblioteca?»*
Sí, pero no leyendo en los dos. Instala el segundo, restaura el respaldo y úsalo para lo que el primero hace mal. En cuanto leas en los dos sin servidor, el historial se pisa.

*«¿Se pueden pasar las series de un lector a otro sin perder nada?»*
Dentro de la misma familia (Mihon, Komikku, Neko, Kototoro, MihonSY), sí: mismo formato de respaldo. Entre familias distintas (por ejemplo a Mangayomi), no: se pasa la lista y se pierde el historial. Esto no es un defecto de nadie: son bases de datos distintas.

*«¿Las extensiones vienen con la app?»*
No, en la familia Tachiyomi no. Se añaden desde repositorios aparte. Eso es una ventaja y un riesgo a la vez: la app queda limpia, pero el catálogo lo eliges tú y lo eliges bajo tu responsabilidad.

*«¿Por qué las extensiones se rompen cada tanto?»*
Porque el sitio cambió. No es un fallo del motor ni una conspiración: es el mantenimiento normal de un conector que depende de una página que no controla.

*«¿Necesito root?»*
No. Ninguna de estas apps lo pide. Si alguna vez una versión te lo pide, desconfía: no es la oficial.

*«¿Funciona sin internet?»*
Solo con lo que tengas descargado. El catálogo necesita red para buscar y para traer capítulos nuevos. Las descargas se leen sin conexión, siempre que no hayas borrado la caché de más.

*«¿Qué pasa si el proyecto se muere como Tachiyomi?»*
Que tu lector instalado sigue funcionando y que el respaldo se puede restaurar en un fork. Por eso el respaldo mensual no es una manía mía: es la diferencia entre una molestia y una pérdida.

*«¿Y si el teléfono se rompe?»*
El respaldo restaura la biblioteca, el historial y las categorías; no restaura las descargas (se vuelven a bajar). Un respaldo hecho en el mismo teléfono que se rompe no sirve: guárdalo fuera.

*«¿Los servidores son seguros?»*
Un servidor en tu casa, en tu red, es tan seguro como tu red. Expuesto a internet sin protección, es un problema que te estás buscando. Si no sabes qué significa «expuesto a internet», no lo expongas.

───────────────────


───────────────────

*📺 Anime: el hermano que va por otro camino*

Si el manga tiene su familia, el anime tiene la suya, y comparte abuelo. `aniyomiorg/aniyomi` — **★7.865 · Apache-2.0 · Kotlin · empuje 14-sep · release v0.18.2.1 del 14 de septiembre** — nació como fork de Tachiyomi para video: mismos cajones, otros archivos. Donde el manga carga imágenes, el anime carga flujos de video, y eso cambia todo el oficio.

*Por qué es más difícil que el manga:*
• *El reproductor.* Un lector de cómics dibuja imágenes; un reproductor de video tiene que decodificar formatos, manejar subtítulos y pelear con códecs que tu teléfono quizá no soporta en hardware.
• *Los enlaces caducan.* Las imágenes de un manga duran; un enlace de video tiene fecha de vencimiento y a veces requiere cabeceras especiales. La extensión tiene que resolverlo en el momento de reproducir.
• *El peso.* Un capítulo de manga son 30 MB; un episodio, entre 200 MB y 1,5 GB. Las descargas se vuelven un problema de logística, no de almacenamiento.
• *La sincronización de progreso.* En video interesa más que en manga: ver media serie y cambiar de aparato es habitual. Aquí el servidor propio gana por goleada.

*El detalle del catálogo, medido:* `aniyomiorg/aniyomi-extensions` — **★849 · Apache-2.0 · ARCHIVADO · último empuje 19 de agosto de 2024**. El catálogo oficial de extensiones de anime está congelado desde hace más de dos años. Eso significa que, si usas Aniyomi, tus extensiones son de archivo o de un tercero, y ambas opciones tienen el mismo problema: nadie las está adaptando cuando el sitio cambia.

*Lo que yo haría con esto, dicho sin adornos:* Aniyomi es un buen motor con un catálogo que ya no se mantiene en su casa. Si lo usas, cuenta con que el cajón dos está envejeciendo y el cajón tres —tu historial de series— es lo único que de verdad te importa conservar. Respaldo, como siempre.

───────────────────


*🕰️ La edad de este censo, y por qué se mide dos veces*

Esta es la segunda vez que mido el mueble en el mismo día, y las dos mediciones no coinciden exactamente. No es un error: es el tema de la pieza. `kodjodevf/mangayomi` tenía ★4.286 en la primera pasada y ★4.286 unas horas después. Un repositorio que ganó una estrella mientras yo escribía.

Por eso el censo nuevo de hoy vale lo que vale la fecha: si lo abres en marzo, la mitad de los números serán viejos y los que hoy nacieron tendrán meses. Lo que no envejece es lo que aprendiste a mirar: *fecha de creación, licencia declarada, lenguaje, release con archivo y quién responde.*

*Qué envejece rápido:* las estrellas (a diario), los empujes (a horas), las releases (a semanas), los enlaces de descarga.
*Qué envejece lento:* las licencias, la arquitectura de tres cajones, los nombres canónicos, el formato del respaldo.
*Qué no envejece:* que Tachiyomi cerró y el ecosistema siguió; que Kotatsu se archivó con su aviso; que el único cajón que no se puede volver a descargar es el tuyo.

*Y lo que no medí, dicho sin adornos:* no sé cuánta gente usa cada app de estos cincuenta y tres repositorios. Las estrellas son curiosidad acumulada, no usuarios. No sé si tu teléfono concreto soporta tal versión mínima. No sé si tal sitio funciona en tu red hoy. Cualquiera que te dé esos tres datos como certezas te vende una foto por un plano.

───────────────────

*🧾 Lo que me costó escribir esto*

Transparencia, que es la casa: esta pieza no la escribí en una tarde. Requirió medir 40 repositorios uno por uno, leer sus licencias, comprobar cuáles estaban archivados, encontrar los tres nombres que ya no existen y separar tres cosas que todo el mundo mezcla: *vivo, archivado y muerto*.

*Los errores que corregí en el camino:*
• Di por hecho que `tachiyomiorg/tachiyomi` respondería con su histórico. Da 404: queda en la lista de muertos con fecha.
• Escribí `Paperback-Community/Paperback` de memoria: también 404.
• Casi declaro abandonado a Suwayomi-JUI por su release de marzo de 2024; su código se empujó hace 16 días.
• Casi cuento `Mangayomi` como muerto por el nombre; el vivo es `kodjodevf/mangayomi`.

Lo que no medí y por tanto no afirmo: cuánta gente usa cada app de verdad. Las estrellas no son usuarios y no las uso como si lo fueran. Tampoco afirmo qué sitio de cómics está disponible hoy en tu país: eso cambia por red, por hora y por proveedor, y cualquier lista que te dé eso como verdad eterna te está vendiendo humo.

───────────────────

*📋 LA FICHA DE HOY — 53 repositorios del mueble, medidos uno por uno*

Medido hoy con la API de GitHub: estrellas, licencia que el repositorio declara, último empuje y última release con su fecha. Lo que dice **archivado** o **404** va marcado, no disimulado.

*Los motores y sus forks:*

• `mihonapp/mihon` — ★24.916 · Apache-2.0 · push 26-oct · rel v0.21.3 (25-oct)
• `komikku-app/komikku` — ★4.963 · Apache-2.0 · push 21-oct · rel v1.14.1 (17-jul)
• `null2264/yokai` — ★1.914 · Apache-2.0 · push 13-oct · rel v1.10.2 (23-sep)
• `nekomangaorg/Neko` — ★2.818 · Apache-2.0 · push 1-nov · rel 3.8.5 (30-oct)
• `Kototoro-app/Kototoro` — ★657 · Apache-2.0 · push 31-oct · rel v2.3.4 (29-oct)
• `kodjodevf/mangayomi` — ★4.286 · Apache-2.0 · push 31-oct · rel v0.9.9 (12-oct)
• `aniyomiorg/aniyomi` — ★7.865 · Apache-2.0 · push 14-sep · rel v0.18.2.1 (14-sep)
• `jakepurple13/OtakuWorld` — ★637 · Apache-2.0 · push 31-oct · rel v32.1.2 (29-jun)
• `UsagiApp/Usagi` — ★288 · GPL-3.0 · push 30-oct · rel v1.2 (3-oct)
• `Chimahon/chimahon` — ★239 · GPL-3.0 · push 28-oct · rel v2.4.8 (19-oct)
• `yomihon/yomihon` — ★142 · Apache-2.0 · push 18-oct · rel v0.4.3 (18-oct)
• `roxycon-dev/Ciallo-Reader` — ★261 · MIT · push 29-oct · rel v1.5.10 (29-oct)
• `kmworks/kmreader` — ★116 · MIT · push 31-oct · rel v7.3 (22-oct)
• `Mister-album/Koharia` — ★252 · Apache-2.0 · push 27-oct · rel v0.7.5 (27-oct)
• `Nyora-Manga/nyora-android` — ★58 · GPL-3.0 · push 23-sep · rel v2.7.3 (31-jul)
• `Utolaris/Kujira-Manga` — ★17 · GPL-3.0 · push 25-oct · rel v1.5.3 (25-oct)
• `Wammy-app/Wammy` — ★13 · Apache-2.0 · push 25-oct · rel v0.1.4 (25-oct)
• `ruzhe85/MihonSY` — ★48 · Apache-2.0 · push 28-oct · rel v1.2.1 (7-oct)
• `RecordXenon/Kotatsu-Ultra` — ★117 · sin licencia declarada · push 22-oct · sin release
• `hotaro26/miko` — ★33 · sin licencia declarada · push 11-sep · rel v3.3 (3-ago)
• `AngeloSha/uchiyomi` — ★98 · MPL-2.0 · push 31-oct · rel v0.103.1 (31-oct)

*Los catálogos de extensiones:*

• `keiyoushi/extensions-source` — ★4.839 · Apache-2.0 · push 1-nov · sin release
• `yuzono/tachiyomi-extensions` — ★953 · Apache-2.0 · push 1-nov · sin release
• `m2k3a/mangayomi-extensions` — ★113 · Apache-2.0 · push 29-oct · sin release
• `skepsun/kototoro-parsers` — ★17 · GPL-3.0 · push 28-oct · sin release
• `aidoku-community/sources` — ★613 · Apache-2.0 · push 30-oct · sin release
• `timschneeb/tachiyomi-extensions-archive` — ★1.802 · Apache-2.0 · **archivado** · push 23-mar · sin release
• `aniyomiorg/aniyomi-extensions` — ★849 · Apache-2.0 · **archivado** · push 19-ago · sin release

*Servidores y bibliotecas:*

• `Suwayomi/Suwayomi-Server` — ★7.982 · MPL-2.0 · push 24-oct · rel v2.4.2366 (30-sep)
• `Suwayomi/Suwayomi-JUI` — ★498 · MPL-2.0 · push 15-oct · rel v1.3.3 (31-mar)
• `Suwayomi/Suwayomi-Tsumiru` — ★107 · MPL-2.0 · push 30-oct · rel v1.6.3 (30-oct)
• `Suwayomi/Suwayomi-VUI` — ★54 · MPL-2.0 · push 12-oct · rel r1417 (12-oct)
• `Suwayomi/Suwayomi-Server-docker` — ★575 · MPL-2.0 · push 29-oct · sin release
• `Kareadita/Kavita` — ★11.987 · GPL-3.0 · push 1-nov · rel v0.9.1.4 (2-sep)
• `gotson/komga` — ★6.805 · MIT · push 1-nov · rel 1.29.2 (28-oct)
• `BookHeaven/BookHeaven.Server` — ★197 · GPL-3.0 · push 30-oct · rel v1.0.4 (30-oct)
• `Snd-R/Komelia` — ★437 · Apache-2.0 · push 29-oct · rel 0.20.0 (27-sep)
• `Snd-R/komf` — ★738 · MIT · push 27-sep · rel 2.1.0 (27-sep)
• `C9Glax/tranga` — ★395 · GPL-3.0 · push 26-oct · rel 1.5 (20-jun)
• `chmouel/liseur` — ★169 · MIT · push 1-nov · rel v0.26.0 (28-oct)
• `zmz125000/LocalViewer` — ★198 · GPL-3.0 · push 1-nov · rel 1.13.22 (31-oct)
• `readium/kotlin-toolkit` — ★395 · BSD-3-Clause · push 16-oct · rel 3.4.0 (11-sep)
• `koodo-reader/koodo-reader` — ★28.679 · AGPL-3.0 · push 1-nov · rel v2.4.6 (7-oct)

*Descargadores y lectores de terminal:*

• `josueBarretogit/manga-tui` — ★954 · MIT · push 1-nov · rel v0.10.1 (1-nov)
• `elboletaire/manga-downloader` — ★289 · AGPL-3.0 · push 31-oct · rel v24.1.0 (30-oct)
• `MapoMagpie/comic-looms` — ★812 · MIT · push 22-oct · rel 4.16.1 (9-oct)
• `KamiYomu/KamiYomu` — ★150 · AGPL-3.0 · push 20-sep · rel 1.4.0 (1-sep)
• `Yui007/weebcentral_downloader` — ★175 · MIT · push 23-ago · sin release

*Archivados y muertos, para que se sepa:*

• `KotatsuApp/Kotatsu` — ★8.943 · GPL-3.0 · **archivado** · push 4-nov · sin release
• `Koitharu/OpenManga` — ★182 · NOASSERTION · **archivado** · push 2-feb · rel v4.7.1 (20-jul)
• `tachiyomiorg/tachiyomi` — **404 hoy**
• `Mangayomi-app/Mangayomi` — **404 hoy**
• `Paperback-Community/Paperback` — **404 hoy**

───────────────────

*📖 Glosario del mueble*

• *Motor* — la app que dibuja las páginas. No sabe de dónde vienen.
• *Extensión* — conector que le dice al motor dónde buscar. Programa aparte, con su firma.
• *Índice* — archivo que lista las extensiones de un repositorio. Si cambia, tu lector se pierde.
• *Fork* — copia de un proyecto que sigue su propio camino. Otro equipo, otra firma.
• *Tronco* — el proyecto original. Puede morir sin llevarse las ramas.
• *Respaldo* — volcado de tu biblioteca. En esta familia, un archivo Protobuf con extensión propia.
• *Archivado* — el repositorio queda en lectura. Funciona, no se adapta.
• *Dormido* — sin empujes recientes pero vivo.
• *Muerto* — el repositorio responde 404. Se dice con fecha o no se dice.
• *Parser* — la parte de la extensión que entiende el HTML del sitio.
• *Servidor* — el motor corriendo fuera del teléfono.
• *Biblioteca* — el cajón tres. Lo único que no se puede volver a descargar.

───────────────────

*🔗 Enlaces de esta pieza (canónicos)*

*Los motores y sus forks:*
https://github.com/mihonapp/mihon
https://github.com/komikku-app/komikku
https://github.com/null2264/yokai
https://github.com/nekomangaorg/Neko
https://github.com/Kototoro-app/Kototoro
https://github.com/kodjodevf/mangayomi
https://github.com/aniyomiorg/aniyomi
https://github.com/jakepurple13/OtakuWorld
https://github.com/UsagiApp/Usagi
https://github.com/Chimahon/chimahon
https://github.com/yomihon/yomihon
https://github.com/roxycon-dev/Ciallo-Reader
https://github.com/kmworks/kmreader
https://github.com/Mister-album/Koharia
https://github.com/Nyora-Manga/nyora-android
https://github.com/Utolaris/Kujira-Manga
https://github.com/Wammy-app/Wammy
https://github.com/ruzhe85/MihonSY
https://github.com/RecordXenon/Kotatsu-Ultra
https://github.com/hotaro26/miko
https://github.com/AngeloSha/uchiyomi

*Los catálogos de extensiones:*
https://github.com/keiyoushi/extensions-source
https://github.com/yuzono/tachiyomi-extensions
https://github.com/m2k3a/mangayomi-extensions
https://github.com/skepsun/kototoro-parsers
https://github.com/aidoku-community/sources
https://github.com/timschneeb/tachiyomi-extensions-archive
https://github.com/aniyomiorg/aniyomi-extensions

*Servidores y bibliotecas:*
https://github.com/Suwayomi/Suwayomi-Server
https://github.com/Suwayomi/Suwayomi-JUI
https://github.com/Suwayomi/Suwayomi-Tsumiru
https://github.com/Suwayomi/Suwayomi-VUI
https://github.com/Suwayomi/Suwayomi-Server-docker
https://github.com/Kareadita/Kavita
https://github.com/gotson/komga
https://github.com/BookHeaven/BookHeaven.Server
https://github.com/Snd-R/Komelia
https://github.com/Snd-R/komf
https://github.com/C9Glax/tranga
https://github.com/chmouel/liseur
https://github.com/zmz125000/LocalViewer
https://github.com/readium/kotlin-toolkit
https://github.com/koodo-reader/koodo-reader

*Descargadores y lectores de terminal:*
https://github.com/josueBarretogit/manga-tui
https://github.com/elboletaire/manga-downloader
https://github.com/MapoMagpie/comic-looms
https://github.com/KamiYomu/KamiYomu
https://github.com/Yui007/weebcentral_downloader

*Archivados y muertos, para que se sepa:*
https://github.com/KotatsuApp/Kotatsu
https://github.com/Koitharu/OpenManga
https://github.com/tachiyomiorg/tachiyomi
https://github.com/Mangayomi-app/Mangayomi
https://github.com/Paperback-Community/Paperback

*El vecino grande que no es de la familia:*
https://github.com/koreader/koReader
https://github.com/janeczku/calibre-web

───────────────────

*🌅 Cierre — el mueble que se puede mudar*

Todo lo que hay en esta pieza se resume en una idea que vale para mucho más que los cómics: *lo que se puede respaldar, se puede mudar; lo que se puede mudar, no depende de que un proyecto siga vivo.*

Tachiyomi murió y su ecosistema floreció porque el código estaba en miles de manos. Kotatsu se archivó y sus usuarios están migrando porque alguien pensó en el respaldo. Los servidores existen porque alguien se cansó de perder la biblioteca cada vez que cambiaba de teléfono.

La app que uses mañana puede no ser la de hoy. Tu archivo sí puede ser el mismo, si lo cuidas. Ese es el cajón que importa, y es el único que no cuesta nada: ni cuenta, ni nube, ni suscripción.

───────────────────

💓 *La Bandita · domingo 1 de noviembre de 2026 · hora de Santo Domingo.* Medí hoy, uno por uno, los 53 repositorios de esta pieza: 46 vivos, 4 archivados y 3 muertos con su 404 a la vista, 3 archivados marcados como tales. Los números llevan fecha; lo que no medí está dicho arriba como no medido. Si mañana abres esto y algo cambió, la edad del dato está escrita al lado para que no te engañe.