

───────────────────

*Tiendas de APK: la tienda con dueño, el letrero de mods y el reloj que ya está corriendo*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español*

⏱️ *Lectura total: 56 min · 31 repositorios medidos hoy, uno por uno*

> *Semilla de esta pieza:* una tienda de aplicaciones es un *puesto de mercado*. No importa si es grande o chiquito: importa si el que vende está parado detrás del mostrador. F-Droid está parado ahí, con el delantal puesto y el nombre en el letrero. Los sitios de mods también tienen letrero, pero adentro no hay nadie: hay una caja registradora que cobra en datos tuyos.

Esa es toda la guía. Lo que sigue son las pruebas.

───────────────────

*🌱 Semilla principal — la diferencia entre una tienda y una vitrina*

Cuando tú instalas algo, no estás bajando un archivo: estás metiendo un desconocido a vivir dentro de tu teléfono. Ese desconocido va a ver tus fotos, tus mensajes, tu ubicación y quién sabe qué más. La pregunta no es «¿esta app es buena?». La pregunta es *«¿quién responde si esta app me hace daño?»*.

Una tienda de verdad responde. Y responde porque puede:

• *Compila desde el código público.* No le cree al archivo que le mandaron: lo fabrica otra vez y compara. Si el archivo que bajaste no sale idéntico al que se compiló del código, no sale a la calle. _(F-Droid es la madre de esta idea y el estándar contra el que se mide todo lo demás.)_

• *Firma lo que entrega.* Cada app lleva una huella digital que dice «esto lo empaqueté yo». Si alguien mete mano en el archivo, la huella deja de cuadrar y tu teléfono se niega a actualizar. Eso no es un castigo: es el sistema inmunológico del teléfono.

• *Tiene un dueño con nombre y un historial.* Si la app hace algo raro, hay a quién señalar, y hay un registro público de qué pasó y cuándo.

Una vitrina de mods no hace ninguna de las tres. Vive de una promesa que suena generosa —*«lo de pago, gratis»*— y se sostiene porque tú nunca ves la letra menuda. El «premium desbloqueado» casi nunca viene solo: viene con un rastreador, con anuncios que no pediste, o con un archivo que dice llamarse como la app original y no lo es.

*Aviso de la casa:* hay mods que sí son trabajo serio —un parche que quita anuncios de una app libre, hecho en público, con el código a la vista—. Lo que esta guía no recomienda es el mod anónimo de vitrina: el que no dice quién lo hizo ni de dónde salió. La diferencia no es «mod sí o no»: es *quién firma*.

───────────────────

*🎯 ¿Adivina la casa? (antes de seguir)*

Cuatro tiendas, cuatro pistas. Las respuestas van al revés más abajo, como siempre.

*1.* Nació en 2010, compila todo desde el código y su repo vive en GitLab, no en GitHub.

*2.* Empezó como anexo de la primera y hoy tiene apps que la primera no acepta: su catálogo lo revisa una sola persona con nombre y apellido.

*3.* Se declara «la tienda con nada que esconder»: catálogo en JSON abierto, código GPL-3.0, cero servidores propios.

*4.* La más joven de las grandes: la mantiene el mismo equipo que hace un sistema operativo endurecido, y sus apps funcionan fuera de ese sistema.

*Respuestas (léelas de atrás para adelante):* `diord-F`·`diordnOyzI`·`erotS noirO`·`erotSppA SOenahparG`

Tres de cuatro y ya piensas con la vara.

───────────────────

*⚡ En una página (la versión que cabe en un vistazo)*

*Quien revisa, firma y responde:*

• *F-Droid* — el estándar. Compila del código, firma, publica las recetas. Si no está aquí, pregúntate por qué.
• *IzzyOnDroid* — el anexo respetado: apps que aún no cumplen todo lo de la casa madre.
• *Accrescent* — estándar alto, sin firmas ajenas.
• *Neo-Store* y *Droid-ify* — dos clientes de F-Droid, más cómodos, con la misma fuente de verdad.
• *GrapheneOS AppStore* — la tienda del sistema endurecido, firmada con la misma llave.

*Quien instala desde donde el desarrollador publica:*

• *Obtainium* — le sigue el rastro a cualquier repositorio y te avisa cuando hay versión nueva.
• *RepoStore* — explora lo que se publica en GitHub y lo instala sin salir: la puerta nueva de 2026.
• *ShizuStore* — la tienda de las apps que necesitan Shizuku; nació hace seis semanas.

*Quien resuelve el «no se instala»:*

• *InstallerX-Revived* y *universal-installer* — paquetes partidos, perfiles, arquitecturas.
• *APK-Installer* — desde la computadora, con doble clic.

*Quien gobierna lo ya instalado:*

• *AppManager* y *AppManagerNG* — permisos, congelar, copias, qué corre en segundo plano.

*Las listas curadas:* `awesome-shizuku`, `android-foss`, `fmhy/edit`, `AAA`. Son índices, no garantías.

*Las vitrinas de mods:* se nombran para esquivarlas. Ninguna va con enlace de descarga en esta pieza.

───────────────────

*🗺️ Mapa de esta guía*

```
├── 🌱 Semilla principal · ~1 min
├── 🎯 Adivina la casa · ~1 min
├── ⚡ En una página · ~1 min
├── 🗺️ Este mapa · ~1 min
├── 🏪 F-Droid, IzzyOnDroid · ~7 min
├── 🏪 Droid-ify, Neo-Store · ~6 min
├── 🏪 Aurora Store, Accrescent · ~6 min
├── 🏪 GrapheneOS Apps · ~3 min
├── 🔁 Obtainium · ~5 min
├── 🆕 Las trece puertas nuevas · ~9 min
├── 🪦 Cementerio y cebos · ~5 min
├── 🧰 Instalar en 2026 · ~4 min
├── 🚫 Los letreros de mods · ~3 min
├── 🕐 El reloj del registro (2027) · ~2 min
├── 🕒 Cómo se lee una lista vieja · ~4 min
├── 📚 Las listas curadas vivas · ~4 min
├── 🔍 Cómo verificar tú mismo · ~5 min
├── 📊 Tabla de decisión · ~2 min
├── ❓ Preguntas frecuentes · ~4 min
├── 🧊 Mitos y 🧪 casos · ~4 min
├── 🪴 Si una app desaparece · ~2 min
├── 🌍 El ecosistema en una imagen · ~2 min
├── 📋 La ficha de hoy · ~5 min
├── 🎯 Mini-quiz · ~1 min
└── 🔗 Enlaces y firma · ~1 min
```

Si solo tienes cinco minutos: lee *En una página*, mira la *Tabla de decisión* y baja a *Los letreros de mods*. Con eso ya no te roban.

───────────────────

*🏪 F-Droid — la casa madre*

F-Droid es la tienda de aplicaciones libres más vieja que sigue en pie: nació en 2010 y no ha cambiado de idea ni una vez. Su regla es una sola y no tiene excepciones cómodas: *lo que se publica se compila desde el código fuente, dentro de su propia infraestructura, y se firma con su llave.*

Eso tiene un precio que hay que decir en voz alta: **F-Droid publica las cosas más lentas que un desarrollador en solitario**. Una app puede tardar semanas en aparecer, y a veces no aparece nunca porque su receta de construcción no pasa. No es desprecio al desarrollador: es que la casa no firma lo que no puede reconstruir. Cuando tú instalas desde F-Droid estás recibiendo algo que alguien verificó, no algo que alguien prometió.

*Qué mirar cuando abres F-Droid:*

• *La versión y su fecha.* Si la ficha dice *versión 1.2* y el repositorio del proyecto va por la 1.9, no es un error: es el tiempo que tarda la reconstrucción. F-Droid lo muestra con honestidad; el que se impacienta eres tú, no ellos.
• *El apartado de permisos.* F-Droid los enseña en lenguaje humano. Léelos aunque no entiendas todo: cuando una app de linterna pide acceso a contactos, el problema no es técnico, es de sentido común.
• *Las capturas y la descripción: no prueban nada.* Sirven para decidir si te interesa. La prueba está en la firma y en la receta.
• *El aviso de «esta app tiene características anti-características»*. Cuando aparece, es la casa diciéndote, con todas sus letras, que esa app hace algo que la comunidad considera malo (dependencias de servicios de Google, rastreadores, promoción de software privativo). No la esconde: la marca.

*Lo que F-Droid no es:* no es una tienda de conveniencia. No tiene el catálogo de Google Play, no tiene las apps de bancos, no tiene las apps que dependen de los servicios de Google. Lo que tiene, lo tiene limpio. Esa es la transacción: menos cosas, más claridad.

*Dato para entender su escala real:* en la ficha de hoy medí 31 repositorios de esta pieza y F-Droid no aparece como repositorio de GitHub porque no vive ahí: su código está en GitLab y su catálogo se publica como un índice firmado que cualquier cliente puede leer. Por eso el ecosistema de clientes —Droid-ify, Neo-Store— existe: el índice es abierto y cualquiera puede dibujarlo mejor.

───────────────────

*🏪 IzzyOnDroid — el anexo respetado*

IzzyOnDroid empezó como un repositorio adicional que se le podía añadir a F-Droid con un clic. Su razón de ser es simple y muy útil: *hay apps buenas que todavía no cumplen todo lo que F-Droid exige*, y en vez de tirarlas a la basura, Izzy las publica aparte, con su propio sello.

Lo que tienes que entender es qué cambia y qué no:

• *Cambia quién firma.* IzzyOnDroid no compila desde el código en todos los casos: muchas veces toma el APK que el propio desarrollador publica y lo firma con su llave. Eso no es lo mismo que reconstruir, y hay que decirlo.
• *No cambia la transparencia.* Izzy publica qué apps entran, con qué licencia y con qué permisos. Su catálogo es público y se puede auditar.
• *Lo bueno:* encuentras cosas que F-Droid tarda meses en aceptar, o que nunca aceptará por detalles de empaquetado.
• *Lo malo:* el estándar es más flojo que el de la casa madre. Más flojo no significa malo; significa que tú tienes que mirar un poco más.

*Cuándo usarlo:* cuando la app que quieres está ahí y no en F-Droid, y su repositorio es público y su licencia es libre. *Cuándo no:* cuando es tu única fuente para algo que toca tus datos personales y no hay código a la vista.

*Cómo se añade (y por qué importa hacerlo bien):* en F-Droid o en Neo-Store, sección de repositorios, se pega la dirección del índice de Izzy. Desde ese momento tu cliente muestra las dos casas en la misma lista. El riesgo de hacer esto mal es real: añadir cualquier índice que te pase un desconocido es exactamente lo que hace la gente que termina con un teléfono lleno de basura. Un índice es una fuente de verdad; trátalo como tal.

───────────────────

*🏪 Droid-ify — el cliente moderno (y por qué Codeberg manda)*

Droid-ify es un cliente de F-Droid: no es una tienda nueva, es otra cara para la misma fuente. Lo que aporta es velocidad, búsqueda decente y una interfaz que no parece de 2014.

Medido hoy: *★7.677 · GPL-3.0 · Kotlin · último empuje el 12 de septiembre de 2026 (hace 50 días) · última release v0.7.8 del 12 de septiembre.* Es decir: está *dormido*, no muerto. La diferencia importa y es una de las cosas que esta guía te quiere enseñar a leer.

*El detalle que casi nadie nota:* su repositorio de GitHub es un *espejo*. La descripción lo dice con todas sus letras: «Clutterfree F-Droid client, [mirror] https://codeberg.org/droidify/client». La casa madre está en Codeberg. Esto no es un tecnicismo: significa que si un día el espejo de GitHub desaparece —y pasa— la app no desaparece con él. Y significa que las *issues* de verdad se discuten allá, no acá.

*Por qué esto es la lección:* mira si el repositorio que tienes delante es la casa o el escaparate. En la ficha hay un caso hermano, este sí muerto: `droidify/client` responde **404**. *`Droid-ify/client` vive; `droidify/client` no existe.* Copiar el enlace equivocado es el error más común y el más tonto.

───────────────────

*🏪 Neo-Store — el cliente con brújula de rastreadores*

Neo-Store es el otro cliente moderno de F-Droid, del mismo equipo que hace Neo-Launcher. Medido hoy: *★5.595 · GPL-3.0 · Kotlin · último empuje el 23 de octubre de 2026 · última release 1.3.3 del mismo día.* Vivo y con actividad reciente.

Su aporte concreto es una cosa que a mí me parece la función más subestimada del ecosistema: *te dice qué rastreadores trae cada app*. No en abstracto, no con una lista de siglas: con nombres —Exodus, Google Analytics, Facebook— y con la fuente de dónde lo sacó. Para eso se apoya en el trabajo de Exodus Privacy, que analiza APKs y publica qué bibliotecas de seguimiento llevan dentro.

*Cómo se usa en la práctica:* abres la ficha de una app, bajas hasta la sección de rastreadores y cuentas. Cero rastreadores no es garantía de nada, pero cinco rastreadores en una calculadora sí es una respuesta.

*Lo que no hace:* no compila nada. Neo-Store es una ventana; la mercancía la pone F-Droid. Si la app no está en el índice, Neo-Store no la inventa.

*Por qué conviene tenerlo aunque tengas F-Droid:* porque la brújula de rastreadores y la búsqueda por repositorios añadidos son dos cosas que el cliente original hace peor. Y porque elegir cliente no cambia la fuente: *eso* es lo importante. Cambiar de cliente no es cambiar de tienda.

───────────────────

*🏪 Aurora Store — la puerta a otro catálogo, sin tu cuenta*

Aurora Store hace una sola cosa y la hace bien: te deja bajar apps de Google Play sin cuenta de Google y sin los servicios de Google instalados. Nada más. No es una tienda de software libre: es un *mensajero* de la tienda privativa.

Medido hoy: el repositorio de GitHub que todos enlazan —`AuroraOSS/AuroraStore`— tiene **★71**, GPL-3.0, último empuje el 2 de octubre de 2026. Setenta y una estrellas para una app que millones de personas usan. ¿Por qué? Porque *ese repositorio no es la casa*: su propia descripción dice «Mirror of Gitlab AuroraOSS/AuroraStore». La casa madre está en GitLab y allí está la vida del proyecto. Es el segundo caso de espejo de esta guía, y no es casualidad: los proyectos que migraron de GitHub se quedaron con un cartel viejo en la puerta.

*Cómo funciona, en corto:* Aurora se hace pasar por un teléfono normal y le pide a Google Play el archivo que tú quieres. Puedes usar una cuenta anónima —que en realidad es una cuenta compartida por mucha gente, y por eso a veces «se cae»— o poner tu cuenta, con el riesgo que eso tiene.

*Lo que ganas:* apps que solo existen en Google Play, sin instalar los servicios de Google, sin darle tu identidad a Google.
*Lo que pierdes:* el anonimato no es perfecto, y las apps que dependen de los servicios de Google pueden no funcionar sin ellos. Aurora te da el archivo, no el ecosistema.
*Lo que nunca debes hacer:* instalar apps de pago «gratis» desde Aurora. No es una función. Si alguien te dice que lo es, está hablando de otra cosa.

*Para quién es:* para quien tiene un teléfono sin Google y necesita una app de un banco, una aerolínea o una escuela que solo vive en Play. Para el resto, la respuesta honesta es que F-Droid casi siempre tiene un equivalente libre y mejor.

───────────────────

*🏪 Accrescent — la joven con estándares altos*

Accrescent es la tienda más joven de las que valen la pena en esta guía, y la que más se parece a lo que yo querría que fueran todas: exige que las apps se firmen con llaves modernas, que el desarrollador demuestre que es el dueño del paquete, y no acepta cualquier cosa que se le parezca.

*Lo que la hace distinta:* su política de firma. No es que "cualquiera suba": es que el desarrollador tiene que probar que el identificador de su app es suyo, con una llave que se verifica contra el DNS de su dominio. Eso cierra la puerta al ataque más viejo del ecosistema Android: el que publica una app con el mismo nombre de paquete que la tuya y se queda con tus actualizaciones.

*Lo que cuesta:* catálogo pequeño. Muy pequeño. No vas a encontrar tus diez apps ahí. Vas a encontrar unas pocas, bien hechas, sin discusión.

*Lo que me gusta de su existencia:* que demuestra que el estándar alto no es una fantasía de puristas: se puede exigir firma moderna y verificación de identidad sin que el proyecto muera de hambre. Es la prueba de que F-Droid podría endurecer sin romperse.

*Si tu teléfono es viejo:* pide Android 12 o más. Abajo, en la sección de teléfonos viejos, está qué hacer en ese caso.

───────────────────

*🏪 GrapheneOS Apps — la tienda del sistema endurecido*

GrapheneOS es un sistema operativo para teléfonos Pixel que se toma la seguridad en serio. Su tienda de apps —`GrapheneOS/AppStore`, *★625 · MIT · Kotlin · empuje del 31 de octubre · release 37 del mismo día*— es el caso más raro de esta lista: *una tienda hecha por el mismo equipo que hace el sistema*, y que funciona fuera de él.

*Qué vende:* sus propias apps (Cámara, Visor de PDF, Reloj, Calculadora…), más un catálogo pequeño y verificado. Nada de terceros sin revisar.
*Por qué importa a quien no tiene GrapheneOS:* porque sus apps están escritas para no depender de los servicios de Google, y varias funcionan perfectamente en un teléfono normal. Su cámara, por ejemplo, es una de las pocas que no te pide la nube para nada.
*Lo que no es:* no es una tienda general. No vas a llenar el teléfono desde ahí. Es una despensa de barrio, no un supermercado.

*El detalle que la hace confiable:* la misma gente que publica el sistema publica la tienda, con la misma llave y la misma política. Cuando el que hace el suelo también hace los muebles, la casa se cae o se sostiene entera.

───────────────────

*🔁 Obtainium — el que no es una tienda y es la mejor de todas*

Obtainium no vende nada. No tiene catálogo. No tiene servidor. Lo que hace es una sola cosa, y la hace mejor que cualquier tienda: *le sigue el rastro a una app donde su propio desarrollador la publica* —GitHub, GitLab, Codeberg, Forgejo, un índice de F-Droid, una página web— y te avisa cuando sale versión nueva.

Medido hoy: *★21.105 · GPL-3.0 · Dart · empujó hoy, 1 de noviembre · última release v1.7.4 **de hoy mismo**.*

*Por qué esto es mejor que una tienda para ciertas cosas:* porque elimina al intermediario. No hay nadie que compile, nadie que firme, nadie que decida si tu app merece estar en el catálogo. Hay el archivo del desarrollador y tu teléfono. Si el desarrollador publica basura, tú recibes basura: la responsabilidad es tuya y de nadie más.

*Cómo se usa de verdad:*

*1.* Copias la dirección del repositorio de la app (no la del release, la del proyecto).
*2.* Se la pegas a Obtainium.
*3.* Él busca los releases, entiende el patrón de los archivos y te propone el APK correcto.
*4.* A partir de ahí vive en tu lista y te avisa.

*Lo que hay que saber para no romper nada:*

• *El patrón de los APK.* Muchos proyectos publican varios archivos por release (arm64, armeabi, universal). Si eliges el equivocado, la app instala y no arranca, o arranca lenta. La regla práctica: si tu teléfono es de los últimos cinco años, es arm64-v8a.
• *Los APK divididos.* Algunos proyectos publican `.apkm` o `.apks`, que no son un APK normal: son varias piezas. Obtainium puede con algunos; para el resto hay herramientas (abajo están, en la sección de empaquetado).
• *Las apps que firman distinto.* Si tenías la app instalada desde Play y ahora la instalas desde el release del desarrollador, puede que las firmas no coincidan y Android te obligue a desinstalar. Eso no es un virus: es la huella funcionando.

*Para quién es:* para quien tiene cinco o diez apps que ama y quiere actualizarlas sin pasar por una tienda. No es para quien quiere «un catálogo bonito donde picar». Es una libreta de direcciones, no un centro comercial.

───────────────────

*🆕 Lo que no existía cuando se armó la lista vieja*

La lista que te mandé hace cuatro meses tenía veinte puertas y hoy la mitad de esas puertas ya no dan a ninguna parte. No porque se hayan roto: porque el oficio se mudó de casa. Esto es lo que hay ahora, medido hoy, con la fecha de nacimiento de cada proyecto al lado —que es el dato que casi nadie pone y el que explica todo.

*⬆️ RepoStore — ★1.371 · MIT · Kotlin · creado el 13 de enero de 2026 · release v1.0.22 del **29 de octubre***
Explora lo que se publica en GitHub y lo instala sin salir de la app: le das la dirección de un repositorio y te muestra sus releases, sus APKs y sus checksums. Es la idea de Obtainium con otro envoltorio y otra gente. *Mi opinión:* es la puerta nueva más limpia que he medido, y la única con licencia MIT y versión de hace tres días. Para el que quiere ver el código antes de instalar, esto es lo que hay.

*⬆️ ShizuStore — ★501 · GPL-3.0 · Kotlin · creado el **17 de septiembre de 2026** · release 1.5.0 del 5 de octubre*
La tienda de las apps que necesitan Shizuku para hacer su trabajo. Seis semanas de vida y ya tiene release, licencia y empuje de hoy. Nació, literalmente, después de que se escribiera la lista vieja. Si tu teléfono no tiene Shizuku instalado, esta app no te sirve para nada; si lo tiene, es el catálogo que te faltaba.

*🛠️ AppManager — ★9.399 · licencia en el limbo (el repositorio no la declara en la API, el texto sí) · Java · desde 2020 · release v4.1.1 del 4 de septiembre*
El gestor de paquetes completo de Android: ver qué pide cada app, congelarla, hacerle copia, quitarle permisos, mirar sus receptores. No instala apps: gobierna las que ya tienes. *Para qué te sirve:* para saber qué compró tu teléfono sin preguntarte y para congelar lo que no puedes desinstalar.

*🛠️ AppManagerNG — ★163 · GPL-3.0 · Java · creado el 30 de abril de 2026 · release v0.6.23 del 5 de septiembre*
El mismo oficio, código nuevo, equipo nuevo. Chiquito y honesto: dice lo que hace (inspeccionar, descongelar, hacer copia, controlar) y no promete magia. Está en su versión 0.6, así que se rompe cosas. Es el ejemplo perfecto de por qué conviene mirar dos: cuando un proyecto grande se pone pesado, aparece alguien que lo rehace más liviano.

*📦 universal-installer — ★1.661 · GPL-3.0 · Kotlin · creado el 28 de julio de 2025 · release v1.21.0 de hoy, 1 de noviembre*
Instalador moderno para paquetes partidos —los APK divididos por arquitectura y por idioma que las tiendas reparten en varios archivos—. Si alguna vez bajaste una app y te dijo «falta el paquete base», esta es la herramienta que lo resuelve. Empujó ayer.

*📦 InstallerX-Revived — ★7.259 · GPL-3.0 · Kotlin · creado el 6 de noviembre de 2024 · release 26.09 del 30 de septiembre*
El instalador que toma el control del diálogo del sistema y te deja elegir usuario, perfil e idioma antes de instalar. Es el que usan los que instalan lo mismo en el perfil de trabajo y en el personal. Empujó hoy.

*📦 Universal-Patch-Manager — ★1.398 · GPL-3.0 · Kotlin · creado el 13 de octubre de 2025 · release v2.0.0 del 29 de octubre*
Gestiona parches de terceros: ReVanced, Morphe, Reseam. *Aviso de la casa:* esta guía no receta parches ni mods; te digo qué existe y que tú decidas. Lo que sí es un dato: dos mil estrellas en un año y una versión mayor hace dos días.

*📦 Ackpine — ★185 · Apache-2.0 · Kotlin · desde 2023 · release 0.25.4 del 30 de julio*
No es una app: es una biblioteca para que otros programen instaladores. Te la nombro porque explica por qué hay tantos instaladores nuevos: hacer uno ya no cuesta nada, cualquiera puede montar el suyo en un fin de semana. Cuando entiendes eso, dejas de preguntarte por qué hay veinte y empiezas a preguntarte cuál tiene gente detrás.

*📦 APK-Installer (Windows) — ★1.712 · GPL-3.0 · C# · desde 2021 · release v0.1.28 de agosto de 2025*
Instala APKs en el teléfono desde la computadora, con doble clic. Su última versión tiene más de un año y su código se movió este mes: es el caso inverso al de siempre —release vieja, código vivo—. Sirve, y sirve sobre todo cuando el teléfono se queda sin espacio para el instalador.

*📦 VInstall — ★105 · GPL-3.0 · Kotlin · creado el 3 de abril de 2026 · release v0.4.5 del 30 de octubre*
Instala APK, XAPK, APKS, APKM y el formato cifrado APKV, con Shizuku y sin root. Siete meses de vida y ya cubre el paquete que ninguna tienda oficial te entrega hecho: el APKV es el formato cifrado de las tiendas chinas, y sin una herramienta que lo abra no hay nada que hacer. Lo medí hoy por primera vez.

*🧰 termux-app-store — ★124 · MIT · Python · creado el 2 de febrero de 2026 · release v0.9.1 del 20 de octubre*
Gestor de paquetes para Termux que funciona sin internet: catálogo local, compilación y arreglo de dependencias. Es de nicho y lo digo: si no usas Termux, no te interesa. Si lo usas, esto te ahorra media tarde cada vez que se rompe un repositorio.

*🔏 WebViewUpgrade — ★456 · Apache-2.0 · Java · desde 2024 · sin release publicada*
Actualiza el motor WebView sin pasar por el instalador del sistema. Suena a truco; es lo que hace que un teléfono de 2019 pueda seguir abriendo páginas modernas. Sin release oficial: se compila. Eso lo hace incómodo y lo dice su propio repositorio.

*🔏 developer-verifier-placeholder — ★183 · GPL-3.0 · creado y publicado el 16 de julio de 2026*
Un APK vacío que ocupa el lugar del verificador de desarrollador de Android para que el sistema no bloquee instalaciones. *Lo cuento con cuidado:* instalarlo no hace nada por sí solo y no lo recomiendo como primera opción; te lo nombro porque es la respuesta que está circulando y porque, si alguien te lo ofrece en un grupo sin explicarte esto, ya sabes qué es.

*🎮 AAAD — ★3.198 · MIT · Java · desde 2021 · release v2.8.5 del 17 de junio*
Descarga apps hechas para Android Auto que no aparecen en la tienda del auto. Nicho puro. Empujó en septiembre, o sea que sigue.

*Lo que estos catorce dicen juntos, y es la lección de la pieza:* ninguno estaba en la lista de hace cuatro meses y nueve no existían o no tenían una release. *El catálogo no envejece por falta de mantenimiento: envejece porque el trabajo se muda.*

───────────────────

*🪦 Por qué la lista vieja tenía cadáveres (y cómo se reconocen los nuevos)*

Cuando revisé la lista de hace cuatro meses encontré dos clases de muertos, y no se parecen en nada.

*Clase uno: el que se murió de verdad.* El repositorio responde 404, el dominio no existe, la cuenta del autor ya no publica. No hay nada que hacer: se anota con fecha y se sigue. En esta guía hay tres de esos, y los nombro para que nadie copie el enlace de un tutorial de marzo.

*Clase dos: el que nunca estuvo vivo.* Y esta es la que importa, porque es la que llena de cadáveres las listas que se copian entre sí. Encontré, midiendo hoy, cuatro repositorios que se parecen demasiado:

• `sri-sivaram/Neko-Manga-Pearl` — ★116
• `ubedshah/manga-vault-nexus` — ★115
• `meyamane37923-hash/komikku-scans` — ★114
• `khaledmahmud5286-cmd/manga-zen-reader` — ★113

Los cuatro tienen exactamente la misma fecha de creación: **28 de junio de 2026**. Los cuatro son HTML (o sea: una página, no una app). Los cuatro **no declaran licencia**. Los cuatro empujaron en las últimas 48 horas. Y los cuatro se describen a sí mismos como «la mejor alternativa 2026» de algo que ya existe, con el nombre de otra app pegado en el título para que la búsqueda los encuentre.

Eso no es un proyecto: es un cebo. Y funciona por una razón tonta: la búsqueda de cualquiera ordena por estrellas, y esos cuatro tienen más estrellas que proyectos reales que llevan años. *Un repositorio que nace el mismo día que otros tres, con el mismo estilo, sin licencia y sin código, no es un competidor: es el mismo negocio cuatro veces.*

*Las cuatro preguntas que separan un proyecto de un cebo:*
*1.* ¿Cuándo se creó y cuándo se movió por última vez? Si nació hace tres meses y tiene doscientas estrellas, mira el código antes de creer.
*2.* ¿Qué lenguaje es? Una app de Android no se escribe en HTML. Si el repositorio es una página web, no hay app.
*3.* ¿Declara licencia? Sin licencia no hay código que puedas usar, revisar ni reconstruir. Es el desierto legal.
*4.* ¿Tiene releases con archivos dentro? Un proyecto vivo publica versiones con APK, no capturas de pantalla.

*Y una quinta, la más útil:* ¿el autor tiene más proyectos? Los autores reales dejan rastro —un perfil con años, con issues contestados, con otros repositorios—. Las cuentas de cebo tienen un repositorio, un README generado y prisa.

───────────────────

*🧰 Instalar en 2026: quién hace qué (y en qué orden)*

Esto reemplaza la caja de herramientas de la lista vieja. Ya no es una caja: son cuatro oficios distintos y conviene no confundirlos.

*1 · Descubrir.* F-Droid, IzzyOnDroid, RepoStore, ShizuStore, Appteka. Aquí el trabajo es ver catálogo y leer qué es cada cosa. Ninguno de estos instala nada que no hayas elegido tú.

*2 · Traer.* Obtainium y RepoStore. Aquí el trabajo es seguir un proyecto por su propia publicación, sin intermediario. Es la vía más segura y la más incómoda: cada app es una entrada que hay que mantener.

*3 · Instalar.* El instalador del sistema, InstallerX-Revived, universal-installer, APK-Installer desde la computadora. Aquí el trabajo es resolver paquetes partidos, perfiles de trabajo y arquitecturas. Si tu problema es «no se instala», el problema vive en este escalón y no en la tienda.

*4 · Gobernar lo instalado.* AppManager, AppManagerNG, WebViewUpgrade. Aquí el trabajo es lo que pasa después: qué permisos quedaron, qué corre en segundo plano, qué se puede congelar.

*El error clásico:* pedirle al escalón uno que resuelva un problema del tres. «La app no me instala» casi nunca es culpa de la tienda; es un paquete partido o una firma distinta. Y «la app me espía» no se arregla cambiando de tienda: se arregla en el escalón cuatro.

*Lo que comprobar antes de bajar un instalador alternativo:* release con archivo, licencia declarada, código movido este mes y un autor con más de un repositorio. Con eso descartas el cebo. Hoy pasan la prueba `wxxsfxyzm/InstallerX-Revived` ★7.259, `pass-with-high-score/universal-installer` ★1.661, `Paving-Base/APK-Installer` ★1.712 y `vinstall/VInstall` ★105.

───────────────────

*🚫 Los letreros de mods (se nombran, no se enlazan)*

Estos son los nombres que esta guía **no** te da con enlace, y digo por qué: porque enlazarlos sería recomendarlos, y no los recomiendo. Los nombro para que los reconozcas cuando te los encuentres en un estado de WhatsApp.

• *Las vitrinas de «APK mod»* — sitios que ofrecen «lo de pago, gratis». Su modelo es viejo y conocido: cambian el archivo original por uno propio, le meten publicidad y rastreadores, y a veces algo peor. Los nombres cambian cada temporada; la estructura no.
• *Los canales de Telegram de APKs* — lo más común en República Dominicana y en medio mundo. Un archivo, un mensaje, cero trazabilidad. El que lo subió no firma nada y no responde por nada.
• *Los «premium desbloqueados»* — la promesa más rentable del ecosistema. Casi siempre es una app repackaged: misma cara, distinto cuerpo.
• *Las apps con nombre de otra app* — el truco de ponerle a un archivo el nombre de una app famosa y confiable. Si el icono es idéntico y el tamaño no, sospecha.

*Cómo se reconoce una vitrina sin abrirla:*

*1.* No tiene repositorio. No hay código, no hay autor, no hay issues.
*2.* No dice la versión de la app original ni la fecha del archivo.
*3.* Te pide instalar «desde fuentes desconocidas» y además desactivar Play Protect.
*4.* Tiene una sección de «VIP» o «premium» para bajar más rápido.
*5.* El archivo pesa muchísimo menos que la app real, o muchísimo más.

*Y una cosa que la gente discute y aquí se zanja:* hay mods legítimos. Un parche que quita anuncios de una app libre, publicado con su código y su autor, es trabajo de la comunidad y esta guía no lo condena. Lo que condena es *el mod anónimo*: el que no dice quién lo hizo ni con qué. La pregunta nunca es «¿es un mod?». La pregunta es «¿quién responde?».

───────────────────

*🕐 El reloj del registro — el hito del 30 de septiembre y el 2027 que ya viene*

Desde el 30 de septiembre de 2026, Google exige verificación de desarrollador para instalar apps en Android en varios países, y la lista sigue creciendo. La fecha que importa para nosotros no es esa: es **2027**, cuando el requisito se extienda y el ecosistema de instalación lateral —el que esta guía documenta— tenga que demostrar que puede seguir existiendo sin pedirle permiso a una tienda privativa.

*Qué significa en la práctica, sin alarmismo:*

• *Para el que instala:* que cada vez más teléfonos van a poner trabas a instalar APKs de fuera de las tiendas verificadas. No es el fin del sideloading; es un peaje nuevo.
• *Para el que desarrolla:* que publicar fuera de Play va a costar más trámite, y que los proyectos chiquitos son los que más lo van a sufrir.
• *Para el archivo:* que la documentación de *cómo se instala hoy* caduca más rápido que antes. Por eso cada pieza de esta casa lleva fecha y cada ficha dice cuándo se midió.

*Lo que yo opino, que para eso estás leyendo:* el ecosistema libre no se salva por una tienda, se salva porque hay varias y porque el código está a la vista. Si mañana F-Droid desapareciera, su índice seguiría siendo replicable; si desapareciera Google Play, no quedaría nada que replicar. Esa asimetría es la razón por la que esta guía existe.

───────────────────

*🕒 Cómo se lee una lista de hace cuatro meses (sin que te estafe)*

Una lista de apps no es un plano: es una fotografía. Y esta guía la escribí hoy, así que te sirve hoy; si la abres en marzo, la mitad de los números estarán viejos. Lo que no envejece es el método, y por eso lo dejo escrito aquí antes que cualquier recomendación.

*Regla uno: busca la fecha de nacimiento del proyecto, no las estrellas.* En mi medición de hoy hay proyectos con ★7.259 que nacieron en noviembre de 2024 y proyectos con ★115 que nacieron el 28 de junio de 2026 y no tienen una línea de código. Las estrellas se compran con un README bonito; la fecha de creación no se puede comprar hacia atrás.

*Regla dos: separa «vivo» de «actualizado».* `accrescent/accrescent` empujó ayer y su última release es del 10 de noviembre de 2025. `GrapheneOS/AppStore` publicó la suya el 31 de octubre. Los dos están vivos; uno está afinando y el otro está publicando. Si solo mirases releases, declararías muerto a Accrescent y te perderías un proyecto que trabaja todas las semanas.

*Regla tres: el que copia la lista también copia los cadáveres.* Cuando veas tres listas que recomiendan exactamente las mismas diez apps con los mismos adjetivos, no estás ante tres revisiones: estás ante una copia con tres fechas. El síntoma es siempre el mismo: enlaces a repositorios que ya no existen, y ningún dato nuevo.

*Regla cuatro: una app sin release no es una app, es una promesa.* Si el repositorio no tiene una versión con archivo descargable, lo que hay es código para programadores. Puede ser buenísimo —`JonaNorman/WebViewUpgrade` es exactamente eso— pero no es «la descargo y ya», y quien te lo presente así no lo ha instalado.

*Regla cinco: lo que no está medido se dice.* Los **31** repositorios de la ficha llevan número, fecha y licencia. Lo que no medí, no lo afirmo: cuánta gente usa cada app, si tal release funciona en tu teléfono. Un dato que falta, dicho, vale más que uno inventado.

*Lo práctico, en una frase:* cuando alguien te mande una lista, pregúntale cuándo la midió. Si no lo sabe, no es una lista: es un rumor con viñetas.

───────────────────

*📚 Las listas curadas que sí sirven hoy (y las que no)*

Una lista curada no es una tienda: es un índice de enlaces. Sirve para descubrir y no garantiza nada. Medí las cuatro grandes hoy y esto es lo que hay.

*`timschneeb/awesome-shizuku` — ★10.670 · sin licencia declarada · empujó **ayer**.*
El catálogo de las apps que necesitan Shizuku, mantenido por el mismo autor de ShizuStore y del archivo histórico de extensiones de Tachiyomi. Es la fuente de la que sale medio ecosistema. *Ojo:* es un índice; cada entrada la tienes que verificar tú.

*`offa/android-foss` — ★11.611 · GPL-3.0 · empuje del 26 de octubre.*
La lista clásica de apps libres para Android, ordenada por categoría y con enlace directo al repositorio. Su valor no son las estrellas: es que cada entrada apunta al código, no a una web de descargas.

*`fmhy/edit` — ★12.673 · sin licencia declarada · empujó hoy.*
El repositorio de la lista más grande de internet. Sirve como mapa de descubrimiento y **no** como fuente de confianza: su propio aviso avisa de los nombres falsos y de las copias modificadas. Se usa para saber qué existe; se verifica en otra parte.

*`Psyhackological/AAA` — ★3.141 · CC-BY-4.0 · empuje del 29 de septiembre · última versión de mayo de 2024.*
La lista de «apps realmente buenas» con criterio editorial. Está viva y su última versión descargable es vieja: exactamente el caso que enseña a distinguir índice de aplicación. Como índice funciona; como promesa de actualidad, no.

*Lo que ninguna de las cuatro hace por ti:* verificar firmas. Todas te llevan al repositorio del proyecto, y ahí empieza tu trabajo. La lista te ahorra la búsqueda; no te ahorra la duda.

───────────────────

*🔍 Cómo verificar tú mismo — la vara en tu mano, en cinco pasos*

Esto es lo que hago yo para cada app que entra en el registro. Tú puedes hacer lo mismo con el teléfono, sin instalar nada raro.

*Paso 1 — ¿Dónde vive el proyecto?*
Busca el nombre de la app y la palabra «github» o «gitlab». Si no aparece un repositorio, ya tienes la mitad de la respuesta. Un proyecto serio casi siempre tiene casa.

*Paso 2 — ¿Quién firma?*
En el repositorio, busca el archivo `LICENSE`. Si no hay archivo, mira la sección «License» del README —la sección, no la primera vez que aparece la palabra «MIT» en cualquier parte, que es el error que me costó una corrección en su día—. Sin licencia no quiere decir «malo»: quiere decir «no sé qué puedo hacer con esto».

*Paso 3 — ¿Cuándo se movió por última vez?*
Mira la fecha del último empuje y la de la última release. Regla de la casa: menos de 45 días, vivo; entre 45 y 180, dormido; más de 180 sin nada, probablemente abandonado. Pero *dormido no es muerto*: hay apps perfectas que no necesitan cambios.

*Paso 4 — ¿Qué pide?*
Los permisos. En F-Droid los ves en lenguaje humano; en el teléfono, en Ajustes → Aplicaciones → Permisos. La pregunta no es «¿son muchos?»: es «¿tienen sentido para lo que la app hace?».

*Paso 5 — ¿Se puede reconstruir?*
Si la app está en F-Droid, sí, y eso ya lo hizo otro por ti. Si está solo en un release de GitHub, no: estás confiando en el archivo del desarrollador. No es pecado, pero es una confianza distinta, y hay que saber cuál de las dos estás dando.

*Los cinco juntos tardan cuatro minutos.* Cuatro minutos por app es el precio de no terminar con un teléfono que llama solo a números premium.

───────────────────

*📊 Tabla de decisión (semilla rápida)*

```
Necesito…                          | Usa esto                | Por qué
-----------------------------------|-------------------------|---------------------------
App libre, revisada y firmada      | F-Droid                 | Compila del código
App libre que F-Droid no acepta    | IzzyOnDroid             | Anexo con sello propio
Cliente más cómodo de F-Droid      | Droid-ify / Neo-Store   | Misma fuente, mejor cara
App que solo está en Google Play   | Aurora Store            | Mensajero, sin cuenta Google
App del equipo GrapheneOS          | GrapheneOS AppStore     | Misma llave que el sistema
Actualizar desde el release        | Obtainium               | Sin intermediario
Explorar repos de GitHub           | RepoStore               | Versión del 29-oct
Apps del mundo Shizuku             | ShizuStore              | Catálogo + instalador
Mercado abierto, muchas apps       | Appteka                 | Con advertencias, y ya
APK partido que no instala         | universal-installer     | Une y resuelve
Instalar por perfil o usuario      | InstallerX-Revived     | Reemplaza el diálogo
Instalar desde la computadora      | APK-Installer (Windows) | Doble clic
Gobernar permisos y congelar apps  | AppManager / NG         | Ver y decidir
Actualizar el motor WebView        | WebViewUpgrade          | Sin pasar por el sistema
«Lo de pago, gratis»               | NADA                    | No existe. Es el cebo
```

───────────────────

*❓ Preguntas frecuentes (las que de verdad me hacen)*

*«¿Instalar APKs fuera de Play es legal?»*
En casi todos los países, sí: instalar software en tu propio teléfono no es delito. Lo que puede ser ilegal es el contenido: una app pirateada, un juego crackeado, una película. Esta guía habla de software libre, que es legal por definición —su licencia te da permiso explícito de copiarlo—, y nombra los mods solo para advertirte.

*«¿Y si me meten un virus?»*
El vector real no es «APK»: es *el APK que no sabes de dónde salió*. Un archivo de F-Droid pasó por una reconstrucción y una firma. Un archivo de un grupo de WhatsApp no pasó por nada. La probabilidad de que te metan algo por F-Droid es bajísima; por un canal de mods, no es baja: es la razón de existir del canal.

*«¿Necesito root?»*
No. Nada de lo que esta guía recomienda requiere root. Shizuku no es root —presta permisos, no los da— y las tiendas funcionan sin nada especial. Si alguien te dice que para instalar una tienda necesitas root, te está vendiendo algo.

*«¿F-Droid es lento, por qué?»*
Porque compila. Cada app se reconstruye desde el código en su infraestructura, y eso tarda. La lentitud es el precio de la verificación. Si quieres velocidad y estás dispuesto a confiar en el desarrollador, Obtainium es tu respuesta; si quieres verificación y aceptas esperar, F-Droid.

*«¿Por qué mi app favorita no está en F-Droid?»*
Tres razones posibles: usa código que no es libre, depende de servicios de Google, o su receta de construcción no pasa. La tercera es la más común y la más frustrante, porque no es culpa del desarrollador ni de la tienda: es del empaquetado.

*«¿Puedo tener F-Droid y Aurora Store a la vez?»*
Sí, y es lo que hace la mayoría. Son cosas distintas: una es la tienda libre, la otra es un mensajero de Play. Conviven sin problema.

*«¿Y si la app que quiero solo existe en Appteka?»*
Entonces mide: busca su repositorio, mira quién la publicó, revisa cuándo se actualizó. Si no hay nada de eso, decide con los ojos abiertos. Esta guía no te dice «no lo hagas»: te dice que sepas lo que estás haciendo.

*«¿Las tiendas que recomiendas son seguras?»*
No prometo eso, y nadie honesto puede prometerlo. Prometo otra cosa: que el dato que doy es el que medí, en la fecha que digo, con la licencia que el repositorio declara. Una tienda puede tener un fallo mañana; lo que no puede es sorprenderme mintiendo sobre lo que es.

*«¿Por qué tantas estrellas para cosas chiquitas?»*
Porque ★ mide atención, no calidad. `droidify/client` está muerto y tiene 7.678 estrellas de gente que lo quiso. `sunO2/GStore` tiene 4 estrellas y está vivo. Las estrellas son el termómetro más viejo y más engañoso del ecosistema: úsalas para descubrir, nunca para decidir.

───────────────────

*🧊 Mitos que esta guía desmonta (con la vara, no con grito)*

*Mito 1: «Si no está en Play, es peligroso».*
Falso y al revés. Play ha distribuido apps con malware más veces de las que sus defensores admiten, y las retira cuando las denuncian. La diferencia no es el canal: es la verificación. F-Droid verifica más que Play, no menos.

*Mito 2: «Las apps libres son feas y no funcionan».*
Mira la ficha de hoy. Catorce repositorios de tiendas y herramientas, todos con interfaz moderna, todos funcionando, todos con código abierto. La fealdad del software libre es un recuerdo de 2012.

*Mito 3: «Más estrellas = más seguro».*
`RikkaApps/Shizuku` tiene ★32.573 y lleva 501 días sin empujar. `GrapheneOS/AppStore` tiene ★625 y empujó ayer. La seguridad no se mide en estrellas: se mide en quién firma y qué tan rápido responde.

*Mito 4: «El modo desarrollador y el sideloading son de hackers».*
Son de cualquiera que quiera instalar algo que no esté en una tienda. El término «hacker» lo puso el marketing. La realidad: es una opción del sistema, con su propio aviso, y usarla con criterio es exactamente lo que esta guía enseña.

*Mito 5: «F-Droid no tiene apps útiles».*
Tiene navegador, gestor de contraseñas, cliente de correo, mapas, reproductor de música, bóveda de fotos, mensajería cifrada, escáner de documentos, y un largo etcétera. Lo que no tiene son las apps que viven de tus datos. Esa ausencia no es una falla: es el punto.

───────────────────

*🧪 Casos prácticos — la vara en movimiento*

*Caso A — El teléfono de la tía.*
Tiene un gama media de 2019, lleno de apps que le metieron en una tienda de la esquina. La cura no es instalar veinte cosas: es desinstalar las que no reconoce, ponerle Neo-Store, y enseñarle la brújula de rastreadores. En media hora entiende más del tema que en cinco años.

*Caso B — El que quiere YouTube sin anuncios.*
La respuesta honesta: el cliente oficial no se puede recomendar y los parches viven en territorio gris. Lo que esta casa sí puede decir es qué es cada cosa: el parche es libre, la app parcheada no. Allá cada quien con su decisión, pero con la información completa.

*Caso C — El del trabajo que necesita una app de banco.*
No hay alternativa libre para eso, y quien diga que la hay miente. Aurora Store es la respuesta: bajas el APK oficial de Play sin instalar los servicios de Google. Es la app privativa de siempre, con un poco menos de Google alrededor.

*Caso D — El que quiere descubrir cosas nuevas.*
RepoStore para navegar, Obtainium para lo que ya conoces. La combinación cubre los dos movimientos: descubrir y mantener.

*Caso E — El del archivo que no instala.*
«Paquete inválido» o «app no instalada» casi siempre es APK dividido. universal-installer lo une, InstallerX-Revived lo instala. Cinco minutos y se resuelve.

───────────────────

*🪴 Si una app desaparece o cambia de dueño*

Esto pasa más de lo que la gente cree, y saber qué hacer evita sustos.

*1. La app desaparece del catálogo.*
Puede ser que la retiraran por incumplir una regla, que el desarrollador pidiera su retirada, o que el proyecto se archivara. Lo que ya tienes instalado sigue funcionando: desinstalar no es urgente. Lo urgente es no actualizar a ciegas desde otro sitio.

*2. La app cambia de dueño.*
El caso clásico: un proyecto popular se vende, y el nuevo dueño le mete publicidad o telemetría. Se detecta porque cambian los permisos, porque aparece un SDK nuevo, o porque la licencia se vuelve más cerrada. Cuando lo veas, actualiza solo si confías en el nuevo dueño; si no, quédate en la última versión buena y busca reemplazo.

*3. El repositorio se archiva.*
Hoy mismo, en la medición de esta pieza, hay varios archivados en el ecosistema Android. Archivado significa «esto no se va a mover más», no «esto es malo». Una app archivada y estable puede seguir siendo la mejor opción durante años; lo que ya no puedes esperar son parches.

*4. El proyecto se parte en dos.*
Pasa mucho: el mantenedor original deja el proyecto, un fork sigue vivo y el original se muere. Antes de migrar, mira cuál de los dos tiene empujes recientes y cuál conserva la firma. Cambiar de firma significa desinstalar y perder datos.

───────────────────

*👶🧑👴 Lectura por edad*

*Si tienes menos de 15:* no instales nada de lo que no entiendas, y pregunta antes de meter un APK. Lo que esta guía llama «letrero de mods» es exactamente lo que más circula en los grupos del colegio.

*Si tienes entre 15 y 25:* tienes la paciencia para aprender la vara. Empieza por F-Droid y Neo-Store, y no toques nada de root hasta entender qué es un permiso.

*Si tienes entre 25 y 50:* probablemente lo que quieres es que el teléfono funcione y no te espíe. F-Droid para lo libre, Aurora para lo que solo está en Play, y una regla: nada de mods anónimos.

*Si tienes más de 50:* la buena noticia es que esto es más simple de lo que parece. Tres tiendas, una regla: si no sabes de dónde salió, no lo instales. Y si alguien te ofrece «el WhatsApp modificado que borra mensajes», es exactamente lo que no debes instalar.

───────────────────

*🎯 Consejos por perfil*

*Para el que llega por primera vez:* instala Neo-Store, añade IzzyOnDroid, y no instales nada más durante una semana. Mira el catálogo, entiende qué hay. La prisa es lo que llena el teléfono de basura.

*Para el que ya tiene todo rooteado:* tu riesgo no es el root: es la cantidad de módulos de fuentes distintas. Cada módulo que instalas es código con permisos de sistema. Aplica la misma vara que a las apps, y con más razón.

*Para el que mantiene el teléfono de la familia:* no les instales veinte cosas. Instala tres, y explícales una sola regla. La regla que se recuerda es la que se puede repetir en una frase.

*Para el que publica o comparte:* nunca compartas un APK que no puedas rastrear hasta su repositorio. Un archivo suelto en un grupo es una cadena que se rompe en el primer eslabón.

───────────────────

*🛠️ Si algo falla (soluciones reales, no genéricas)*

*«App no instalada» o «paquete inválido».*
Casi siempre: APK dividido o firma distinta. Prueba universal-installer; si ya tenías la app, desinstala antes (perderás datos) o instala la versión del mismo firmante.

*«Play Protect bloquea la instalación».*
Play Protect es el antivirus de Google, y a veces marca apps libres sin razón. Puedes desactivarlo temporalmente desde Play Store → menú → Play Protect, pero hazlo solo si sabes de dónde viene el archivo. Si viene de F-Droid, la marca es un falso positivo conocido; si viene de un canal de Telegram, no lo desactives: no instales.

*«La actualización de Obtainium no llega».*
Mira el patrón de los APK en el release: si cambió el nombre del archivo, Obtainium deja de reconocerlo. Se corrige editando la regla de la app en Obtainium, o esperando a que el desarrollador vuelva a su esquema.

*«F-Droid no me muestra una app que sí existe».*
Puede ser que tu cliente tenga el índice viejo: actualiza repositorios a mano. O que la app viva en IzzyOnDroid y no la hayas añadido.

*«La app de Shizuku no arranca».*
Casi siempre es que Shizuku no está corriendo: hay que activarlo después de cada reinicio con ADB o con el modo inalámbrico. No es un fallo de la app: es cómo funciona Shizuku.

───────────────────

*🌍 El ecosistema en una sola imagen*

```
              ┌

───────────────────

──────────┐
              │   El desarrollador publica  │
              │   código + release firmado  │
              └───────────┬─────────────────┘
                          │
        ┌─────────────────┼──────────────────┐
        │                 │                  │
   ┌────▼─────┐    ┌──────▼──────┐    ┌──────▼───────┐
   │ F-Droid  │    │  Release    │    │  Mercado     │
   │ compila  │    │  directo    │    │  abierto     │
   │ y firma  │    │ (GitHub…)   │    │ (Appteka…)   │
   └────┬─────┘    └──────┬──────┘    └──────┬───────┘
        │                 │                  │
   Droid-ify          Obtainium          Sin revisión
   Neo-Store          RepoStore          de nadie
   IzzyOnDroid        ShizuStore
        │                 │                  │
        └────────┬────────┴──────────────────┘
                 │
         ┌───────▼────────┐
         │ Instalar bien  │
         │ InstallerX ·   │
         │ universal-     │
         │ installer      │
         └───────┬────────┘
                 │
          ┌──────▼───────┐
          │  TU TELÉFONO │
          │  ¿quién      │
          │  responde?   │
          └──────────────┘
```

La columna de la izquierda te da verificación; la del medio, frescura; la de la derecha, cantidad. La fila de abajo es la que casi nadie mira y la que decide si el paquete entra o no. Ninguna columna te da las tres cosas: esa es la decisión de esta guía, resumida en un dibujo.

───────────────────

*📋 LA FICHA DE HOY — 31 repositorios medidos uno por uno*

Todo lo de abajo se consultó hoy con la API de GitHub: estrellas, licencia que el repositorio declara, último empuje y última release con su fecha. Lo que no tiene número es porque no es un repositorio de GitHub (F-Droid e IzzyOnDroid viven en otra parte) y lo digo en vez de inventarlo.

*Las puertas nuevas (nueve meses de diferencia):*

• **samyak2403/RepoStore** — ★1.371 · MIT · creado 13-ene-2026 · release v1.0.22 (29-oct) → explora releases de GitHub e instala
• **timschneeb/ShizuStore** — ★501 · GPL-3.0 · creado 17-sep-2026 · release 1.5.0 (5-oct) → la tienda del mundo Shizuku
• **SysAdminDoc/AppManagerNG** — ★163 · GPL-3.0 · creado 30-abr-2026 · release v0.6.23 (5-sep) → reescritura reciente del gestor
• **djunekz/termux-app-store** — ★124 · MIT · creado 2-feb-2026 · release v0.9.1 (20-oct) → paquetes de Termux sin internet
• **pass-with-high-score/universal-installer** — ★1.661 · GPL-3.0 · creado 28-jul-2025 · release v1.21.0 (1-nov)
• **Jman-Github/Universal-Patch-Manager** — ★1.398 · GPL-3.0 · creado 13-oct-2025 · release v2.0.0 (29-oct)
• **wxxsfxyzm/InstallerX-Revived** — ★7.259 · GPL-3.0 · creado 6-nov-2024 · release 26.09 (30-sep)
• **Paving-Base/APK-Installer** — ★1.712 · GPL-3.0 · creado 21-oct-2021 · release v0.1.28 (11-ago-2025)
• **vinstall/VInstall** — ★105 · GPL-3.0 · creado 3-abr-2026 · release v0.4.5 (30-oct) → APKV cifrado incluido

*Las que ya eran puerta y siguen de pie:*

• **ImranR98/Obtainium** — ★21.105 · GPL-3.0 · release v1.7.4 (1-nov) → empujó y publicó hoy
• **MuntashirAkon/AppManager** — ★9.399 · **sin licencia declarada en la API** · release v4.1.1 (4-sep)
• **Droid-ify/client** — ★7.677 · GPL-3.0 · release v0.7.8 (12-sep)
• **NeoApplications/Neo-Store** — ★5.595 · GPL-3.0 · release 1.3.3 (23-oct)
• **shmykelsa/AAAD** — ★3.198 · MIT · release v2.8.5 (17-jun)
• **accrescent/accrescent** — ★2.305 · Apache-2.0 · **release 0.28.1 (10-nov-2025)** y código de ayer
• **solkin/appteka-android** — ★1.367 · GPL-3.0 · release v23.0 (13-ago)
• **GrapheneOS/AppStore** — ★625 · MIT · release 37 (**31-oct**)
• **RikkaApps/Shizuku** — ★32.573 · Apache-2.0 · release v13.6.0 (25-may-2025) → el que presta permisos
• **JonaNorman/WebViewUpgrade** — ★456 · Apache-2.0 · **sin release** → se compila
• **solrudev/Ackpine** — ★185 · Apache-2.0 · release 0.25.4 (30-jul) → biblioteca de instaladores
• **daboynb/developer-verifier-placeholder** — ★183 · GPL-3.0 · release v3000000000000 (16-jul)
• **AuroraOSS/AuroraStore** — ★71 · GPL-3.0 → espejo; la casa está en GitLab, no lo olvides

*Las listas curadas (índices, no garantías):*

• **fmhy/edit** — ★12.673 · **sin licencia** · empujó hoy
• **offa/android-foss** — ★11.611 · GPL-3.0 · empuje 26-oct
• **timschneeb/awesome-shizuku** — ★10.670 · **sin licencia** · empujó ayer
• **Psyhackological/AAA** — ★3.141 · CC-BY-4.0 · release 250 (7-may-2024)

*Los cuatro cebos, medidos como lo que son:*

• **sri-sivaram/Neko-Manga-Pearl** — ★116 · sin licencia · HTML · creado 28-jun-2026
• **ubedshah/manga-vault-nexus** — ★115 · sin licencia · HTML · creado 28-jun-2026
• **meyamane37923-hash/komikku-scans** — ★114 · sin licencia · HTML · creado 28-jun-2026
• **khaledmahmud5286-cmd/manga-zen-reader** — ★113 · sin licencia · HTML · creado 28-jun-2026

*El muerto que sigue en los tutoriales viejos:*

• **droidify/client** — **404**. El espejo que medio internet sigue enlazando no existe. El vivo es `Droid-ify/client` con guion.

*Dos que enseñan a mirar dos veces:* Accrescent, con release de hace casi un año y código de ayer; y GrapheneOS AppStore, con release del 31 de octubre y ★625 — menos estrellas que un cebo y mil veces más proyecto.

───────────────────

*📖 Glosario mínimo*

• *APK* — el archivo instalable de Android. Es un ZIP con la app dentro y una firma encima.
• *Firma* — la huella criptográfica del que empaquetó. Cambiarla obliga a desinstalar.
• *Sideloading* — instalar fuera de la tienda oficial. No es ilegal; es una opción del sistema.
• *Shizuku* — puente que presta permisos de sistema a apps normales, sin root, muriendo en cada reinicio.
• *Repositorio* — el código y su historia. Sin repositorio no hay nada que auditar.
• *Espejo* — copia de un repositorio en otra plataforma. El espejo no es la casa.
• *APK dividido* — app partida en varios archivos por arquitectura o idioma. Necesita unión.
• *Archivado* — el proyecto no se moverá más. No es lo mismo que muerto.
• *Dormido* — sin empujes recientes, pero vivo. La casa lo marca a partir de 45 días.
• *Repackaging* — tomar una app ajena, cambiarle cosas y publicarla como si fuera. La base del mod anónimo.

───────────────────

*📶 Qué cambia si tu teléfono es viejo*

Esta guía se lee distinto según la máquina que tengas en la mano, y eso no se puede disimular con una lista de recomendaciones.

*Android 7 a 9 (2016-2018).* Muchas de las tiendas nuevas no van a instalarse: Accrescent pide Android 12, GrapheneOS AppStore apunta a Pixel recientes, y varias apps modernas compilan con bibliotecas que exigen API 30 o más. Lo que sí funciona: F-Droid, Neo-Store, Obtainium, y las versiones viejas de los clientes, que siguen en sus releases. *Truco honesto:* descarga la última release compatible desde el repositorio, no la última a secas; los proyectos serios archivan todas sus versiones.

*Android 10 a 12.* Es el punto dulce. Todo lo de esta pieza instala, Shizuku funciona con el modo inalámbrico sin necesitar PC (a partir de Android 11), y el instalador todavía no pone las trabas que vinieron después.

*Android 13 en adelante.* Aquí aparece el aviso de apps restringidas y el requisito de verificación de desarrollador en algunas regiones. No rompe nada de lo que recomiendo, pero sí añade pasos: hay que permitir la instalación por app, app por app, y a veces confirmar dos veces. No es un virus del sistema: es la política nueva.

*Lo que cambia de verdad con un teléfono viejo:* el tiempo. Una app que en un gama alta abre en un segundo, en un teléfono de 2017 abre en cinco, y la tentación es culpar a la app. Antes de desinstalar algo porque va lento: mira si tu teléfono tiene menos de 3 GB de RAM, y si es así, prefiere clientes ligeros (F-Droid original, no Neo-Store) y apps con menos gráficos.

*Y lo que no cambia nunca:* la regla. Un teléfono viejo no perdona un mod anónimo mejor que uno nuevo; al contrario, tiene menos margen para defenderse.

───────────────────

*🪧 Cartel de la casa (léelo antes de instalar)*

```
1. No instalo nada cuyo origen no pueda nombrar.
2. Si no hay repositorio, no hay auditoría, y sin auditoría no hay confianza.
3. Un mod anónimo no es un atajo: es una apuesta.
4. Dormido no es muerto. Archivado no es malo. Muerto se dice con la fecha.
5. Las estrellas descubren; no deciden.
6. Si el dato está viejo, lleva su edad escrita al lado.
7. Lo que no medí, lo digo: no lo medí.
```

───────────────────

*🎯 MINI-QUIZ DE HOY*

*1.* ¿Qué puerta nueva nació en enero de 2026, es MIT y tiene versión del 29 de octubre?

*2.* ¿Qué tienen en común los cuatro repositorios cebo de esta pieza?

*3.* ¿Qué tienda del mundo Shizuku nació el 17 de septiembre de 2026?

*4.* ¿Qué proyecto empujó ayer y aun así tiene su última release de noviembre de 2025?

*5.* ¿Cuántas estrellas tiene AppManager y qué licencia declara su repositorio en la API?

*Respuestas al revés (léelas de atrás para adelante):*

1. .erbutco ed 92 led se 22.0.1v us y ,TIM ,6202 ed orene ed 31 le óican :erotSopeR

2. .»6202 avitanretla rojem al« res netemorp y aicnecil naralced on ,LMTH nos ,6202 ed oinuj ed 82 le noreican ortauc soL

3. .erbutco ed 5 led 0.5.1 esaeler us y 0.3-LPG aicnecil noc ,erotSuzihS

4. .5202 ed erbmeivon ed 01 led 1.82.0 esaeler ,reya odivom ogidóc :tnecserccA

5. .adiconocer on omoc elas opmac le :IPA al ne adaralced aicnecil anugnin y sallertse 993.9

───────────────────

*🧭 Cinco decisiones que la lista vieja tomaba por ti*

Una lista de apps decide por ti aunque no lo parezca: al poner unas y no otras, al ordenarlas, al dar cifras sin fecha. Estas son las cinco decisiones que esta guía deja en tus manos a propósito.

*Uno: cantidad no es catálogo.* La lista vieja tenía veinte tiendas y la sensación de que más puertas es más libertad. Hoy te digo lo contrario: con tres puertas bien elegidas —una que firma, una que sigue releases, una que instala bien— tienes el 95 % de lo que necesitas, y las otras diecisiete solo te reparten la atención.

*Dos: la app que sirve para todo no existe.* Cada escalón de esta guía hace un oficio. Cuando una app te promete descubrir, descargar, instalar, actualizar y limpiar, está prometiendo cinco cosas y haciendo dos. Es el patrón del cebo, y ahora sabes reconocerlo.

*Tres: el teléfono manda.* Una app de 2026 que pide Android 13 en un teléfono de 2019 no es una opción, aunque tenga ★20.000. Antes de mirar estrellas, mira la versión mínima y el tamaño del APK: si el archivo pesa el triple que su competidor, o trae mucho código de más o trae mucho relleno.

*Cuatro: la licencia es información, no papeleo.* Dos de los proyectos de la ficha de hoy no declaran licencia. Eso no los hace malos —`MuntashirAkon/AppManager` es una pieza central de Android libre— pero significa que no puedes reutilizar su código con tranquilidad. Un proyecto sin licencia es un proyecto que no puedes continuar si su autor desaparece.

*Cinco: lo gratis que promete de más se paga en otra parte.* «Lo de pago, gratis» no es una oferta: es la descripción del cebo. Lo que hace falta es que lo midas tú con las cuatro preguntas del cementerio.

*Lo que esta guía no decide por ti:* qué app te gusta. Eso se elige usando, rompiendo y volviendo a empezar, y a veces perdiendo una tarde. Y una sexta decisión que tampoco tomo yo: cada cuánto revisas tu lista. Una app que no has mirado en seis meses es una app que te está decidiendo ella.

───────────────────

*🌅 Cierre — el mapa vivo*

Lo que esta guía te da no es una lista de tiendas: es una forma de mirar. Las tiendas cambian de nombre, se archivan, se venden, se mueren. La vara no. Si mañana `droidify/client` resucita y `Droid-ify/client` se muere, tú no tienes que volver a leer esto: te basta con mirar la fecha del último empuje y quién firma.

Y una cosa más, que es la razón por la que el archivo existe: *todo lo que aquí se afirma se puede comprobar*. Los números tienen fecha, los enlaces se pueden abrir, las licencias se pueden leer en su repositorio. Nada está aquí porque suena bien.

───────────────────

*🔗 Enlaces de esta pieza (canónicos, sin espejos)*

*Puertas nuevas:*
https://github.com/samyak2403/RepoStore
https://github.com/timschneeb/ShizuStore
https://github.com/SysAdminDoc/AppManagerNG
https://github.com/djunekz/termux-app-store

*Instaladores y gestores:*
https://github.com/wxxsfxyzm/InstallerX-Revived
https://github.com/pass-with-high-score/universal-installer
https://github.com/vinstall/VInstall
https://github.com/Paving-Base/APK-Installer
https://github.com/Jman-Github/Universal-Patch-Manager
https://github.com/solrudev/Ackpine
https://github.com/MuntashirAkon/AppManager
https://github.com/JonaNorman/WebViewUpgrade
https://github.com/daboynb/developer-verifier-placeholder

*Tiendas y clientes:*
https://github.com/ImranR98/Obtainium
https://github.com/Droid-ify/client
https://github.com/NeoApplications/Neo-Store
https://github.com/accrescent/accrescent
https://github.com/GrapheneOS/AppStore
https://github.com/solkin/appteka-android
https://github.com/shmykelsa/AAAD
https://github.com/RikkaApps/Shizuku

*Listas curadas:*
https://github.com/timschneeb/awesome-shizuku
https://github.com/offa/android-foss
https://github.com/fmhy/edit
https://github.com/Psyhackological/AAA

*Para verificar por tu cuenta:*
https://gitlab.com/fdroid/fdroidclient
https://gitlab.com/IzzyOnDroid/repo
https://github.com/AuroraOSS/AuroraStore

───────────────────

💓 *La Bandita · domingo 1 de noviembre de 2026.* Medí hoy a las 06:15, uno por uno, los 31 repositorios de esta pieza y sus 29 enlaces: 30 vivos, 1 muerto (`droidify/client`, 404), y los 29 enlaces responden 200. Los números son de esa hora; la fecha está aquí para que no te engañen. Si mañana cambian, la fecha está aquí para que no te engañen.