───────────────────

*Tiendas de APK: la tienda con dueño, el letrero de mods y el reloj que ya está corriendo*

*La Bandita · sábado 31 de octubre de 2026 · edición dominicano-español*

⏱️ *Lectura total: 56 min · 30 repositorios medidos hoy, uno por uno*

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

*La que revisa, firma y responde:*

• *F-Droid* — el estándar. Compila del código, firma, publica las recetas de construcción. Si no está aquí, pregúntate por qué.
• *IzzyOnDroid* — el anexo respetado de F-Droid. Apps que aún no cumplen todo lo de la casa madre.
• *Accrescent* — joven, estándar alto, sin firmas ajenas.
• *Neo-Store* y *Droid-ify* — dos clientes de F-Droid, más cómodos que el original, con la misma fuente de verdad.
• *Orion Store* — catálogo abierto en JSON, descarga directa del release del desarrollador, sin servidor de por medio.

*La que instala desde donde el desarrollador publica:*

• *Obtainium* — le sigue el rastro a cualquier repo (GitHub, GitLab, Codeberg, F-Droid) y te avisa cuando hay versión nueva.
• *komi-store* y *ObtainX* — primos de Obtainium con otra cara y otro flujo.
• *yuki*, *ShizuStore*, *ShizuCoreFetch* — tiendas específicas del mundo Shizuku.

*Las listas curadas (no son tiendas, son yacimientos):*

• *AAA*, *awesome-fdroid*, *awesome-shizuku*, *best-root-apps* — catálogos mantenidos a mano. Sirven para descubrir; no sustituyen al que firma.

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
├── 🏪 Orion, GrapheneOS Apps · ~5 min
├── 🔁 Obtainium, komi, ObtainX · ~7 min
├── 📱 Appteka, yuki, ShizuStore · ~6 min
├── 📚 Las listas curadas (AAA, awesome-*, best-root) · ~5 min
├── 🧭 FMHY: qué sirve y qué no · ~4 min
├── 🧰 AntiSplit-M, InstallerX, APKeep · ~5 min
├── 🚫 Los letreros de mods · ~3 min
├── 🕐 El reloj del registro (2027) · ~2 min
├── 🔍 Cómo verificar tú mismo · ~5 min
├── 📊 Tabla de decisión · ~2 min
├── ❓ Preguntas frecuentes · ~4 min
├── 🧊 Mitos y 🧪 casos · ~4 min
├── 🪴 Si una app desaparece · ~2 min
├── 🌍 El ecosistema en una imagen · ~2 min
├── 📋 La ficha de hoy (30 repos medidos) · ~5 min
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

*Dato para entender su escala real:* en la ficha de hoy medí 30 repositorios de esta pieza y F-Droid no aparece como repositorio de GitHub porque no vive ahí: su código está en GitLab y su catálogo se publica como un índice firmado que cualquier cliente puede leer. Por eso el ecosistema de clientes —Droid-ify, Neo-Store— existe: el índice es abierto y cualquiera puede dibujarlo mejor.

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

Medido hoy: *★7.678 · GPL-3.0 · Kotlin · último empuje el 12 de septiembre de 2026 (hace 49 días) · última release v0.7.8 del 12 de septiembre.* Es decir: está *dormido*, no muerto. La diferencia importa y es una de las cosas que esta guía te quiere enseñar a leer.

*El detalle que casi nadie nota:* su repositorio de GitHub es un *espejo*. La descripción lo dice con todas sus letras: «Clutterfree F-Droid client, [mirror] https://codeberg.org/droidify/client». La casa madre está en Codeberg. Esto no es un tecnicismo: significa que si un día el espejo de GitHub desaparece —y pasa— la app no desaparece con él. Y significa que las *issues* de verdad se discuten allá, no acá.

*Por qué esto es la lección:* cuando midas un proyecto, mira si el repositorio que tienes delante es la casa o el escaparate. Un escaparate cerrado no mata al proyecto, pero confunde a quien lo mide desde afuera. En la ficha de hoy hay un caso hermano que sí está muerto de verdad: `droidify/client` en GitHub responde **404**. El nombre se parece tanto que confunde; por eso lo nombro: *`Droid-ify/client` sigue vivo; `droidify/client` no existe.* Copiar el enlace equivocado es el error más común y el más tonto.

───────────────────

*🏪 Neo-Store — el cliente con brújula de rastreadores*

Neo-Store es el otro cliente moderno de F-Droid, del mismo equipo que hace Neo-Launcher. Medido hoy: *★5.589 · GPL-3.0 · Kotlin · último empuje el 23 de octubre de 2026 · última release 1.3.3 del mismo día.* Vivo y con actividad reciente.

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

*🏪 Orion Store — la tienda con nada que esconder (y su propia fecha vencida)*

Orion Store es la más interesante de las nuevas, y también la que mejor enseña cómo se mide una promesa.

Su idea es simple y buena: *no tener servidor*. El catálogo es un archivo JSON público en un repositorio (`RookieEnough/Orion-Data`), y la app descarga cada aplicación directamente del release del desarrollador en GitHub, GitLab o Codeberg. No hay CDN de Orion en el medio, no hay cuenta, no hay rastreador. El código es GPL-3.0 y se puede auditar entero.

Medido hoy, con la API, en la casa de verdad:

• `RookieEnough/Orion-Store` — *★3.883 · GPL-3.0 · Kotlin · último empuje el 29 de octubre · última release **2.6.5** del 27 de octubre*
• `RookieEnough/Orion-Data` — *★91 · GPL-3.0 · último empuje **hoy**, 31 de octubre*

Y aquí viene la parte que me hace confiar más en esta pieza que en cualquier folleto: **su propio sitio web dice otra cosa**. En `orionstore.pages.dev`, hoy, se lee «Latest release 1.5.0 · The Monolith Update, Oct 3, 2026», «3.561 estrellas», «1.100+ apps» y, debajo, en letra chiquita y honesta: *«Figures as of Oct 6, 2026»*.

Traducido: la página que presenta la tienda tiene **casi un mes de retraso respecto a su propio repositorio**, que ya va por la 2.6.5. No es mentira —lo dicen— pero es exactamente el tipo de cosa que esta casa mide y cuenta. La lección vale más que la tienda: *cuando un proyecto te da un número, pregúntale de cuándo es*. Si no te lo dice, el número no es un dato: es una impresión con buena letra.

*Lo que ganas:* actualizaciones al instante, porque el release del desarrollador es la fuente. Si el desarrollador publica a las 3 de la mañana, tú lo ves a las 3 y cinco.
*Lo que pierdes:* nadie compila nada por ti. Confías en el archivo del release tal como lo subió el desarrollador. Orion te da el camino limpio, no la verificación independiente.
*Un detalle de su catálogo:* su descripción menciona apps «Morphe» —parches de YouTube y YouTube Music— que es territorio gris: el parche es libre, la app parcheada no lo es. Si vas a usar Orion solo para eso, entiende lo que estás haciendo; para el resto del catálogo libre, la tienda es tan limpia como promete.

───────────────────

*🏪 GrapheneOS Apps — la tienda del sistema endurecido*

GrapheneOS es un sistema operativo para teléfonos Pixel que se toma la seguridad en serio. Su tienda de apps —`GrapheneOS/AppStore`, *★624 · MIT · Kotlin · último empuje hoy, 31 de octubre · release 37*— es el caso más raro de esta lista: *una tienda hecha por el mismo equipo que hace el sistema*, y que funciona fuera de él.

*Qué vende:* sus propias apps (Cámara, Visor de PDF, Reloj, Calculadora…), más un catálogo pequeño y verificado. Nada de terceros sin revisar.
*Por qué importa a quien no tiene GrapheneOS:* porque sus apps están escritas para no depender de los servicios de Google, y varias funcionan perfectamente en un teléfono normal. Su cámara, por ejemplo, es una de las pocas que no te pide la nube para nada.
*Lo que no es:* no es una tienda general. No vas a llenar el teléfono desde ahí. Es una despensa de barrio, no un supermercado.

*El detalle que la hace confiable:* la misma gente que publica el sistema publica la tienda, con la misma llave y la misma política. Cuando el que hace el suelo también hace los muebles, la casa se cae o se sostiene entera.

───────────────────

*🔁 Obtainium — el que no es una tienda y es la mejor de todas*

Obtainium no vende nada. No tiene catálogo. No tiene servidor. Lo que hace es una sola cosa, y la hace mejor que cualquier tienda: *le sigue el rastro a una app donde su propio desarrollador la publica* —GitHub, GitLab, Codeberg, Forgejo, un índice de F-Droid, una página web— y te avisa cuando sale versión nueva.

Medido hoy: *★21.095 · GPL-3.0 · Dart · empujó en las últimas horas (la API lo fecha el 1 de noviembre porque va en UTC; en Santo Domingo seguimos el 31 de octubre) · última release v1.7.3.*

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

*🔁 komi-store — el catálogo de releases, con estética*

komi-store hace casi lo mismo que Obtainium, pero al revés: en vez de que tú le des las direcciones, te da un catálogo navegable de apps que viven en GitHub, Codeberg y Forgejo, y las instalas con un toque. Antes se llamaba GitHub Store y el cambio de nombre le sentó bien: ahora no promete ser solo de GitHub.

Medido hoy: *★20.176 · Apache-2.0 · Kotlin · último empuje el 25 de octubre · última release v1.9.4 del 24 de octubre.*

*Lo bueno:* descubres cosas que no sabías que existían, y cada instalación apunta al release del desarrollador, no a un espejo.
*Lo malo:* el catálogo es lo que la comunidad ha ido metiendo, y eso incluye cosas a medio hacer. La ficha de cada app te dice lo que hay; no lo que falta.
*El detalle que me gusta:* es Apache-2.0, no GPL. Eso significa que cualquiera puede tomar el código y hacer su versión sin publicar los cambios. No es un defecto —es una elección— pero es una elección distinta a la de F-Droid, y conviene saber qué licencia tiene la herramienta que usas para bajar software libre. Hay una ironía ahí que no voy a disimular.

───────────────────

*🔁 ObtainX — el primo que instala como quiere*

ObtainX nació de la misma idea que Obtainium y se separó con una promesa más ancha: no solo actualiza, también *instala como tú quieras* —con opciones extra, con permisos, sin las restricciones que Android pone por defecto a los instaladores normales.

Medido hoy: *★1.567 · GPL-3.0 · Dart · último empuje el 5 de octubre · última release v2.21.0 del 4 de octubre.*

*Cuándo tiene sentido:* cuando necesitas instalar algo que el instalador del sistema rechaza por una razón técnica tonta (una versión más vieja que la instalada, un paquete con un permiso que Android 14 ya no deja pedir, una app que se llama igual que otra).
*Cuándo no:* cuando no sabes lo que estás haciendo. Un instalador con opciones extra es una llave inglesa: sirve para apretar y para romper.

───────────────────

*📱 Appteka — el mercado que dice tener 334 mil apps*

Aquí hay que tener cuidado con las palabras, porque Appteka no es una tienda de software libre y tampoco es un sitio de mods: es un *mercado abierto* donde cualquiera publica, con revisión automatizada y escaneo de seguridad.

Lo que su propio sitio declara hoy, leído en vivo: *«334K+ apps & games · 42 categorías · 100 % gratis · publica cualquiera · descargas directas · escaneadas al subir · código abierto»*.

Su cliente oficial, `solkin/appteka-android`, medido hoy: *★1.367 · GPL-3.0 · Kotlin · último empuje el 21 de octubre · última release v23.0 del 13 de agosto.*

*El análisis honesto:* 334.000 apps en 42 categorías con revisión automatizada es, matemáticamente, imposible de revisar a mano. Eso no la hace mala: la hace *una plaza de mercado*, no una tienda con dueño detrás de cada puesto. El escaneo de seguridad detecta lo obvio —troyanos conocidos, firmas de malware— y no detecta lo sutil: un SDK de publicidad metido a propósito, una app que pide más permisos de los que necesita.

*Cómo usarla sin quemarte:*

• *Bájate el cliente oficial*, no un APK de «Appteka premium» de otro sitio. El cliente es GPL-3.0 y está en un repositorio público: si algo no cuadra, se puede leer.
• *Mira quién publicó.* En un mercado abierto, el vendedor es el dato más importante. Un desarrollador con historial no es garantía, pero un paquete sin autor sí es una advertencia.
• *Desconfía del tamaño.* Una app de 300 KB que promete «todas las funciones premium» de una app de 80 MB no es una app: es un envoltorio.
• *Compara con la fuente.* Antes de instalar algo de Appteka, busca si esa misma app tiene repositorio público. Si lo tiene, instálala de ahí y ahórrate la duda.

*Por qué la incluyo en esta guía:* porque la alternativa real de mucha gente no es F-Droid: es un grupo de WhatsApp con APKs. Appteka es un escalón por encima de eso, y merece estar nombrada con sus límites, no escondida.

───────────────────

*📱 yuki, ShizuStore y ShizuCoreFetch — el rincón de Shizuku*

Shizuku es una pieza de software que presta permisos del sistema sin root: le pides permiso a un proceso que ya los tiene, y desde ahí puedes hacer cosas que Android normalmente no deja. Alrededor de eso creció un ecosistema chiquito de tiendas, y cada una tiene su carácter.

*yuki* — `carlelieser/yuki`: *★157 · MIT · Kotlin · último empuje el 12 de octubre · release android-v1.11.1 del 12 de octubre.* Es un **catálogo**, no una tienda: una lista de apps libres que usan Shizuku, con ficha y enlace. Su sitio, yukistore.org, responde hoy. Si quieres saber qué existe en ese mundo, empieza aquí, porque la lista está curada a mano y se nota.

*ShizuStore* — `timschneeb/ShizuStore`: *★501 · GPL-3.0 · Kotlin · empujó en las últimas horas · release 1.5.0 del 5 de octubre.* Esta sí instala: toma los APK de las fuentes originales de cada proyecto y los pone a un toque. Se apoya en la lista `awesome-shizuku` del mismo autor. La combinación lista + instalador es elegante: descubres en una y ejecutas en la otra.

*ShizuCoreFetch* — `elhizazi1/ShizuCoreFetch`: *★519 · GPL-3.0 · Kotlin · último empuje el 15 de septiembre · release 2.4.0 del 3 de septiembre.* Plataforma centralizada para buscar y gestionar apps que piden permisos de núcleo. Su sitio, shizucorefetch.siwane.xyz, respondió hoy. Es la más ambiciosa de las tres y la que menos se mueve: 46 días sin empujar. Dormida, no muerta.

*Una advertencia de la casa, y va en serio:* el mundo Shizuku no es magia gratis. Darle Shizuku a una app es darle llaves que Android no le daría. Instala solo apps cuyo código puedas leer, y desconfía de cualquier app de este ecosistema que no tenga repositorio. Un permiso de núcleo en manos de un desconocido es peor que un anuncio.

───────────────────

*📚 Las listas curadas — el yacimiento, no la mina*

Una lista curada no es una tienda. Es una persona —o dos— que se sentó a ordenar el mundo. Sirven para descubrir, no para confiar: lo que aparece en una lista todavía tiene que pasar por tu vara.

*AAA — `Psyhackological/AAA`:* *★3.141 · CC-BY-4.0 · último empuje el 29 de septiembre.* Las tres A son de *Android App Alternatives*: para cada app famosa y privativa, una alternativa libre. Es la lista que yo le daría a alguien que acaba de decidir que no quiere Google en el teléfono y no sabe por dónde empezar. *Ojo con la licencia:* CC-BY-4.0 es la licencia de **la lista**, no de las apps que recomienda. Cada app tiene la suya y hay que ir a verla.

*awesome-fdroid — `moneytoo/awesome-fdroid`:* *★200 · Unlicense · último empuje hoy.* Lista de apps de F-Droid organizada por uso. Pequeña, ordenada y sin florituras. Su licencia (Unlicense) es el equivalente a «esto es de todos»: puedes copiarla entera sin pedir permiso.

*awesome-shizuku — `timschneeb/awesome-shizuku`:* *★10.666 · sin licencia declarada por la API (NOASSERTION) · último empuje hoy.* Diez mil estrellas para una lista: es la puerta de entrada al mundo Shizuku y el motor de ShizuStore. Que un catálogo de enlaces tenga más estrellas que la mayoría de las apps que recomienda dice mucho de cómo funciona este ecosistema: *la información ordenada vale más que el software suelto*.

*El detalle incómodo:* NOASSERTION significa que GitHub no reconoce una licencia clara. Para una lista de enlaces eso es casi irrelevante —los hechos no se licencian— pero es exactamente el tipo de cosa que esta casa apunta cuando mide. Lo apunto.

*🧨 Los tres repositorios de krishna3163 — el mismo autor, tres puertas*

Esto merece sección propia porque es un caso que se repite en el ecosistema y casi nadie lo mira: *un solo desarrollador manteniendo tres catálogos distintos sobre el mismo tema*.

*`krishna3163/best_shizuku_apps_for_android_no_root`* — *★158 · sin archivo de licencia, pero el README declara CC BY-SA 3.0 (verificado leyendo la sección License, no buscando la palabra «MIT» en cualquier parte) · creado el 7 de noviembre de 2025 · empujó hoy.*
Es una lista enorme: alrededor de cuarenta catálogos temáticos (agentes de IA, Android TV, device owner, privacidad, terminales, shell Rish, código cerrado, apps no listadas…) con **1.273 repositorios distintos** citados. Es un yacimiento de verdad. Y como todo yacimiento, hay que filtrar: hay de todo, y la lista no opina sobre calidad.

*`krishna3163/best-root-apps-for-android`* — *★50 · MIT · Python · creado el 22 de agosto de 2026 · empujó hoy · release `brene-v0.0.74` del 31 de octubre.*
Directorio curado de apps de root, Magisk, KernelSU, módulos LSPosed, herramientas de sistema, utilidades de privacidad y —fíjate— también apps de Shizuku sin root. Un repo de hace dos meses con una release que se movió hoy: está vivo y trabajando.

*`krishna3163/OmniShizuku`* — *★10 · Apache-2.0 · Kotlin · creado el 24 de octubre de 2026 · empujó hoy · release `latest` del 25 de octubre.*
La app: utilidad para flujos de Shizuku, ADB y Dhizuku, con soporte para teléfono, Android TV y Wear OS. Diez estrellas y seis días de vida: es un proyecto nuevo, no un consagrado.

*Lo que este trío enseña, y es la razón por la que lo pongo aquí:* cuando un mismo autor mantiene tres listas, la tentación es tratarlas como una sola fuente. No lo son. Cada una tiene su licencia, su fecha, su criterio y su nivel de mantenimiento. Medí las tres por separado y las tres dieron resultados distintos —MIT, CC BY-SA 3.0 declarada, Apache-2.0—. *Un autor no es una fuente: es una persona con tres cuadernos.*

───────────────────

*🧭 FMHY — qué sirve y qué no de la lista más grande de internet*

FMHY (*Free Media Heck Yeah*) es la colección de «cosas gratis de internet» más grande que hay: películas, música, juegos, libros, herramientas… y una sección de Android. Su página de móviles es, hoy, una de las puertas más transitadas del ecosistema.

Leí su sección de Android hoy. Esto es lo que encontré, sin adornos.

*Lo que sí sirve, y mucho:*

• *Su bloque de FOSS APKs.* Nombra y enlaza los índices que valen: AAA, awesome-fdroid, awesome-shizuku, Droid-ify, Neo Store, F-Droid, FossifyOrg, Goodwy, Orion Store, IzzyOnDroid, komi, ShizuStore, GrapheneOS Apps. Once nombres, once enlaces, once casas distintas. Ese bloque solo ya justifica la visita.
• *Su bloque de herramientas de APK.* App Manager, Obtainium, ObtainX, AntiSplit-M, InstallerX-Revived, InstallWithOptions, APKeep. Es la caja de herramientas del que quiere entender el empaquetado en vez de sufrirlo.
• *Su advertencia sobre los APK modificados*, escrita por ellos mismos: «ten en cuenta que algunos sitios de APKs modificados listan apps con nombres falsos que generalmente no vale la pena usar». Es la misma advertencia que hace esta guía.

*Lo que no sirve para esta casa:*

• *Su bloque de mods.* Ahí están los nombres que esta guía no enlaza: los patchers, las vitrinas, los canales de Telegram con APKs modificados. FMHY los lista con un criterio de utilidad, no de seguridad. No es lo mismo.
• *Su criterio de «gratis»* no es el criterio de «libre». Una app pirata y una app libre son las dos gratis, y no se parecen en nada.

*Cómo usarla bien:* entra por la sección FOSS, sal con nombres de proyectos, y luego mide cada uno como mides todo lo demás. Si entras por el bloque de mods, ya sabes lo que hay.

───────────────────

*🧰 AntiSplit-M, InstallerX, InstallWithOptions, APKeep — la caja de herramientas*

Hay un problema que ninguna tienda resuelve y que aparece siempre que instalas fuera de Play: *el archivo no es un archivo*. Los APK divididos (`.apkm`, `.apks`, `.apkx`) son varias piezas que hay que unir; los paquetes traen metadatos; el instalador del sistema se niega por razones que no te explica. Estas cuatro herramientas existen para eso.

*AntiSplit-M* — `AbdurazaaqMohammed/AntiSplit-M`: *★4.938 · Apache-2.0 · Java · empujó hoy · release 2.3.3.* Convierte un APK dividido en un APK normal instalable. Es la herramienta que evita el clásico «descargué la app y dice que el paquete es inválido».

*InstallerX-Revived* — `wxxsfxyzm/InstallerX-Revived`: *★7.255 · GPL-3.0 · Kotlin · empujó hoy · release 26.09.* Reemplazo del instalador del sistema, con opciones: instalar sin verificación de firma en la sesión, elegir usuario, conservar datos. Es potente y hay que usarla sabiendo.

*InstallWithOptions* — `zacharee/InstallWithOptions`: *★3.393 · MIT · Kotlin · último empuje el 24 de octubre · release 0.9.2.* La versión moderada de lo anterior: instala con opciones extra sin reemplazar nada del sistema.

*APKeep* — `EFForg/apkeep`: *★2.148 · MIT · Rust · último empuje el 1 de octubre · release 1.1.0.* De la Electronic Frontier Foundation: una herramienta de línea de comandos para bajar APKs desde Play, sin cuenta, con control fino. Para quien quiere automatizar, no para quien quiere un botón.

*La regla de la caja de herramientas:* ninguna de estas cuatro te dice si una app es segura. Solo te dejan instalarla como debe instalarse. La seguridad sigue siendo tuya.

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
Necesito…                          | Usa esto              | Por qué
-----------------------------------|-----------------------|---------------------------
App libre, revisada y firmada      | F-Droid               | Compila del código
App libre que F-Droid no acepta    | IzzyOnDroid           | Anexo con sello propio
Cliente más cómodo de F-Droid      | Droid-ify / Neo-Store | Misma fuente, mejor cara
App que solo está en Google Play   | Aurora Store          | Mensajero, sin cuenta Google
App del equipo GrapheneOS          | GrapheneOS AppStore   | Misma llave que el sistema
Actualizar desde el release        | Obtainium             | Sin intermediario
Descubrir apps de repos públicos   | komi-store / Orion    | Catálogo navegable
Apps del mundo Shizuku             | yuki + ShizuStore     | Lista curada + instalador
Mercado abierto, muchas apps       | Appteka               | Con las advertencias de arriba
APK dividido que no instala        | AntiSplit-M           | Une las piezas
Instalar con opciones              | InstallerX-Revived    | Reemplazo del instalador
Bajar APKs por línea de comandos   | APKeep                | De la EFF, sin cuenta
«Lo de pago, gratis»               | NADA                  | No existe. Es el cebo
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
`RikkaApps/Shizuku` tiene ★32.552 y lleva 500 días sin empujar. `GrapheneOS/AppStore` tiene ★624 y empujó hoy. La seguridad no se mide en estrellas: se mide en quién firma y qué tan rápido responde.

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
komi-store o Orion para navegar, Obtainium para lo que ya conoce. La combinación cubre los dos movimientos: descubrir y mantener.

*Caso E — El del archivo que no instala.*
«Paquete inválido» o «app no instalada» casi siempre es APK dividido. AntiSplit-M lo une, InstallerX-Revived lo instala. Cinco minutos y se resuelve.

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
Casi siempre: APK dividido o firma distinta. Prueba AntiSplit-M; si ya tenías la app, desinstala antes (perderás datos) o instala la versión del mismo firmante.

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
              ┌─────────────────────────────┐
              │   El desarrollador publica  │
              │   código + release firmado  │
              └───────────┬─────────────────┘
                          │
        ┌─────────────────┼──────────────────┐
        │                 │                  │
   ┌────▼─────┐     ┌─────▼──────┐    ┌──────▼───────┐
   │ F-Droid  │     │  Release   │    │  Mercado     │
   │ compila  │     │  directo   │    │  abierto     │
   │ y firma  │     │ (GitHub…)  │    │ (Appteka…)   │
   └────┬─────┘     └─────┬──────┘    └──────┬───────┘
        │                 │                  │
   Droid-ify          Obtainium          Sin revisión
   Neo-Store          komi / Orion       de nadie
   IzzyOnDroid        ShizuStore
        │                 │                  │
        └────────┬────────┴──────────────────┘
                 │
          ┌──────▼───────┐
          │  TU TELÉFONO │
          │  ¿quién      │
          │  responde?   │
          └──────────────┘
```

La columna de la izquierda te da verificación; la del medio, frescura; la de la derecha, cantidad. Ninguna te da las tres. Esa es la decisión de esta guía, resumida en un dibujo.

───────────────────

*📋 LA FICHA DE HOY — 30 repositorios medidos uno por uno*

Medido el sábado 31 de octubre de 2026 con la API de GitHub y con peticiones HTTP directas. Las estrellas son las de hoy; la fecha de empuje es la del último commit que la API declara; la licencia es la que el repositorio reconoce.

*Tiendas y clientes:*

• *ImranR98/Obtainium* — ★21.095 · GPL-3.0 · Dart · empujó en las últimas horas · release v1.7.3 → instalador que sigue releases
• *komi-store/komi-store* — ★20.176 · Apache-2.0 · Kotlin · empuje 25-oct · release v1.9.4 (24-oct) → catálogo de repos públicos
• *RookieEnough/Orion-Store* — ★3.883 · GPL-3.0 · Kotlin · empuje 29-oct · release 2.6.5 (27-oct) → sin servidor, catálogo JSON
• *RookieEnough/Orion-Data* — ★91 · GPL-3.0 · empujó hoy → el catálogo de Orion, en abierto
• *Droid-ify/client* — ★7.678 · GPL-3.0 · Kotlin · empuje 12-sep · release v0.7.8 → cliente F-Droid (espejo de Codeberg)
• *NeoApplications/Neo-Store* — ★5.589 · GPL-3.0 · Kotlin · empuje 23-oct · release 1.3.3 → cliente F-Droid con rastreadores
• *bikram-agarwal/ObtainX* — ★1.567 · GPL-3.0 · Dart · empuje 5-oct · release v2.21.0 → primo de Obtainium
• *solkin/appteka-android* — ★1.367 · GPL-3.0 · Kotlin · empuje 21-oct · release v23.0 (13-ago) → cliente de Appteka
• *Victor-root/Omnify* — ★95 · GPL-3.0 · Kotlin · empujó hoy · release 1.0.7-beta.8 → cliente F-Droid sin ruido
• *GrapheneOS/AppStore* — ★624 · MIT · Kotlin · empujó hoy · release 37 → tienda del sistema endurecido
• *AuroraOSS/AuroraStore* — ★71 · GPL-3.0 · Kotlin · empuje 2-oct → **espejo**; la casa está en GitLab

*Mundo Shizuku:*

• *RikkaApps/Shizuku* — ★32.552 · Apache-2.0 · Kotlin · **sin empujar desde el 18-jun-2025 (500 días)** · release v13.6.0 → el que presta permisos
• *iamr0s/Dhizuku* — ★4.067 · GPL-3.0 · Kotlin · empujó hoy · release v2.13.0 → la alternativa a Shizuku
• *timschneeb/ShizuStore* — ★501 · GPL-3.0 · Kotlin · empujó en las últimas horas · release 1.5.0 → tienda de apps Shizuku
• *elhizazi1/ShizuCoreFetch* — ★519 · GPL-3.0 · Kotlin · empuje 15-sep · release 2.4.0 → plataforma centralizada
• *carlelieser/yuki* — ★157 · MIT · Kotlin · empuje 12-oct · release android-v1.11.1 → catálogo curado

*Listas curadas:*

• *timschneeb/awesome-shizuku* — ★10.666 · sin licencia clara (NOASSERTION) · empujó hoy → el índice del mundo Shizuku
• *nyas1/Material-You-app-list* — ★5.250 · sin licencia declarada · empuje 4-ago → lista de apps con Material You
• *Psyhackological/AAA* — ★3.141 · CC-BY-4.0 · empuje 29-sep · release 250 → alternativas libres a apps privativas
• *moneytoo/awesome-fdroid* — ★200 · Unlicense · empujó hoy → apps de F-Droid por uso
• *krishna3163/best_shizuku_apps_for_android_no_root* — ★158 · CC BY-SA 3.0 **declarada en el README** (no hay archivo LICENSE) · creado 7-nov-2025 · empujó hoy → ~40 catálogos, 1.273 repos
• *krishna3163/best-root-apps-for-android* — ★50 · MIT · Python · empujó hoy · release brene-v0.0.74 (hoy) → root, Magisk, KernelSU, LSPosed
• *krishna3163/OmniShizuku* — ★10 · Apache-2.0 · Kotlin · creado 24-oct · empujó hoy · release «latest» (25-oct) → Shizuku/ADB/Dhizuku en móvil, TV y Wear OS

*Herramientas de empaquetado:*

• *wxxsfxyzm/InstallerX-Revived* — ★7.255 · GPL-3.0 · Kotlin · empujó hoy · release 26.09 → instalador con opciones
• *AbdurazaaqMohammed/AntiSplit-M* — ★4.938 · Apache-2.0 · Java · empujó hoy · release 2.3.3 → une APK divididos
• *zacharee/InstallWithOptions* — ★3.393 · MIT · Kotlin · empuje 24-oct · release 0.9.2 → instalar con opciones, sin reemplazar
• *EFForg/apkeep* — ★2.148 · MIT · Rust · empuje 1-oct · release 1.1.0 → APKs desde Play por consola

*Los dos que enseñan por qué hay que medir:*

• *droidify/client* — **404. Muerto.** Se nombra para esquivarlo. No se confunde con `Droid-ify/client`, que está vivo.
• *Developer-For-Git/MOD-STORE* — ★6 · **sin archivo LICENSE** · empuje 17-abr (197 días) · release «New» (7-abr) → un proyecto con nombre de vitrina, seis estrellas y siete meses dormido. Ni lo recomiendo ni lo condeno: lo mido.
• *sunO2/GStore* — ★4 · GPL-3.0 · Dart · empuje 17-oct · release v1.0.34 → cuatro estrellas y un mes de vida. Chiquito, actualizado y con licencia. Eso también es el ecosistema.

*Nota de método, para que puedas repetirlo:* un 404 se registra como muerto; un 403 o un 429 **nunca** se convierten en muerte, porque significan que el servidor no me dejó preguntar, no que el proyecto no exista. Las licencias se leen primero en la sección License del repositorio; si hay varias candidatas, se declara la ambigüedad en vez de elegir la primera que aparezca.

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

*1.* ¿Qué tienda se declara «la tienda con nada que esconder» y en qué formato publica su catálogo?

*2.* De los dos repositorios que se llaman casi igual, ¿cuál está muerto hoy y cuál está vivo?

*3.* ¿Cuánto lleva sin empujar el repositorio que presta permisos a media Android moderna?

*4.* ¿Bajo qué licencia se publica la lista `best_root_apps` y cuál declara —sin archivo— la lista de Shizuku del mismo autor?

*5.* El sitio de Orion dice una versión y su repositorio dice otra. ¿Cuál es la diferencia exacta?

*Respuestas al revés (léelas de atrás para adelante):*

1. REV|oidem rop ed rodivres yah on ,ataD-noirO/hguonEeikooR ne otreiba NOSJ ne av ogolátac le :erotS noirO
2. REV|grebedoC se erdam asac us y ,oviv átse tneilc/yfi-diorD ;)yoh 404( otreum átse tneilc/yfidiord
3. REV|5202 ed oinuj ed 81 le edsed ,rajupme nis saíd 005 avell ukuzihS/sppAakkiR
4. REV|ESNECIL ovihcra nis ,EMDAER us ne 0.3 AS-YB CC aralced rotua omsim led ukuzihS ed atsil al ;TIM se sppa-toor-tseb
5. REV|erbutco ed 72 led 5.6.2 al rop av oirotisoper le ;erbutco ed 6 la sarfic noc erbutco ed 3 led 0.5.1 al ne ódeuq es oitis le

───────────────────

*🌅 Cierre — el mapa vivo*

Lo que esta guía te da no es una lista de tiendas: es una forma de mirar. Las tiendas cambian de nombre, se archivan, se venden, se mueren. La vara no. Si mañana `droidify/client` resucita y `Droid-ify/client` se muere, tú no tienes que volver a leer esto: te basta con mirar la fecha del último empuje y quién firma.

Y una cosa más, que es la razón por la que el archivo existe: *todo lo que aquí se afirma se puede comprobar*. Los números tienen fecha, los enlaces se pueden abrir, las licencias se pueden leer en su repositorio. Nada está aquí porque suena bien.

───────────────────

*🔗 Enlaces de esta pieza (los canónicos, sin espejos)*

*Tiendas y clientes:*
https://f-droid.org
https://apt.izzysoft.de/fdroid
https://accrescent.app
https://github.com/Droid-ify/client
https://codeberg.org/droidify/client
https://github.com/NeoApplications/Neo-Store
https://gitlab.com/AuroraOSS/AuroraStore
https://github.com/RookieEnough/Orion-Store
https://github.com/RookieEnough/Orion-Data
https://github.com/GrapheneOS/AppStore
https://github.com/ImranR98/Obtainium
https://github.com/komi-store/komi-store
https://github.com/bikram-agarwal/ObtainX
https://github.com/Victor-root/Omnify
https://appteka.store
https://github.com/solkin/appteka-android

*Mundo Shizuku:*
https://github.com/RikkaApps/Shizuku
https://github.com/iamr0s/Dhizuku
https://github.com/timschneeb/ShizuStore
https://github.com/elhizazi1/ShizuCoreFetch
https://github.com/carlelieser/yuki
https://yukistore.org

*Listas curadas:*
https://github.com/Psyhackological/AAA
https://github.com/moneytoo/awesome-fdroid
https://github.com/timschneeb/awesome-shizuku
https://github.com/krishna3163/best-root-apps-for-android
https://github.com/krishna3163/best_shizuku_apps_for_android_no_root
https://github.com/krishna3163/OmniShizuku
https://fmhy.net/mobile

*Herramientas:*
https://github.com/AbdurazaaqMohammed/AntiSplit-M
https://github.com/wxxsfxyzm/InstallerX-Revived
https://github.com/zacharee/InstallWithOptions
https://github.com/EFForg/apkeep

*Para verificar por tu cuenta:*
https://reports.exodus-privacy.eu.org
https://www.virustotal.com
https://developer.android.com/developer-verification

───────────────────

💓 *La Bandita · sábado 31 de octubre de 2026.* Medí hoy, uno por uno, los 30 repositorios de esta pieza y sus 36 enlaces: 29 vivos, 1 muerto (`droidify/client`, 404), 0 archivados entre los recomendados. El texto es el de la casa; los números, los de hoy. Si mañana cambian, la fecha está aquí para que no te engañen.
