

───────────────────

*La cerradura que cambió de dueño: la verificación de desarrolladores, medida desde un teléfono que todavía no está en la lista*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español*

⏱️ *Lectura total: 55 min · 33 repositorios medidos hoy, uno por uno*

> *Semilla de esta pieza:* cuando alquilas una casa, el dueño no puede cambiar la cerradura mientras tú estás adentro. Puede subirte el alquiler al renovar, puede pedirte requisitos, pero no puede entrar a tu cuarto a media noche a decidir qué muebles tienes. Android funcionaba con esa regla: tú comprabas el teléfono y desde ese momento el software que corría adentro lo decidías tú. Lo que se discute desde el 30 de septiembre de 2026 no es «más seguridad» ni «menos seguridad»: es **quién tiene la llave**.

Esa es toda la guía. Lo que sigue son las pruebas, las fechas, y el mapa de lo que todavía puedes hacer —hoy, 1 de noviembre, desde Santo Domingo—.

───────────────────

*🌱 Semilla principal — la diferencia entre un requisito y una llave*

Hay dos maneras de controlar lo que entra a una casa. Una es *pedir requisitos al inquilino*: que firme, que se identifique, que se comprometa a no meter ruido. La otra es *tener la llave*: pararse en la puerta y decidir caso por caso, sin avisar, sin explicar y sin que nadie pueda apelar.

Google lleva años haciendo lo primero con Play: para publicar ahí te identificas, pagas veinticinco dólares y aceptas reglas. Eso es un requisito, y es legítimo: es su tienda, su mostrador, sus reglas. Lo que cambió es que ahora ese requisito se aplica **en la puerta del teléfono**, no en la puerta de la tienda. Y la puerta del teléfono es tuya.

La frase que lo resume, y que uso como vara en toda la pieza: *un requisito se cumple una vez y se olvida; una llave se usa todos los días*. Si el sistema operativo pregunta «¿este desarrollador está registrado?» cada vez que instalas algo, ya no importa por dónde llegó el archivo: importa quién firmó el permiso. Eso no es una tienda. Eso es una cerradura con un dueño nuevo.

Y ojo con la trampa del idioma: a esto le dicen *verificación de desarrolladores*, que suena a trámite de banco. No es un trámite: es una condición de instalación. El nombre técnico del mecanismo —*Android Developer Verifier*— es literal: un verificador que se instala en tu aparato y decide.

───────────────────

*🎯 ¿Adivina la casa?*

Cuatro pistas, cuatro respuestas. Van al revés más abajo, como siempre.

*1.* Nació en 2010, compila cada app desde el código público y hoy advierte, con un cartel en su propia página, que su modelo de firma no sobrevive a la regla nueva.

*2.* Es una campaña, no una app: nació en octubre de 2025, tiene una carta abierta con setenta y una organizaciones firmantes y vive en un repositorio con licencia CC0.

*3.* Es una biblioteca pequeña que cualquier desarrollador puede meter en su app para avisarle al usuario que la regla viene en camino. Tres mil setecientas estrellas y una licencia Apache.

*4.* Es un APK vacío, de dieciséis de julio de 2026, que ocupa el lugar del verificador de Google para que el sistema no bloquee instalaciones. Nombre largo, función corta.

*Respuestas (léelas de atrás para adelante):* `redlohecalp-reifirev-repoleved` · `nraWdiorDeerF` · `nepO diordnA peeK` · `diorD-F`

Tres de cuatro y ya estás pensando con la vara de la casa.

───────────────────

*⚡ En una página (lo que cabe en un vistazo)*

*Lo que pasó, sin adorno:* desde el **30 de septiembre de 2026**, en Brasil, Indonesia, Singapur y Tailandia, un teléfono Android *certificado* —o sea, con los servicios de Google— solo instala o actualiza apps de desarrolladores registrados **cuando la instalación viene de una de las siete tiendas participantes**. La lista: Google Play, Samsung Galaxy Store, Xiaomi GetApps, OPPO App Market, vivo V-Appstore, HONOR App Market y Transsion Palm Store. El resto del mundo, incluida la República Dominicana, sigue igual **hasta 2027**.

*Lo que no pasó, aunque lo leíste en algún grupo:* no prohibieron instalar APK. No desapareció F-Droid. No hay una lista negra de apps. Lo que hay es una condición de identidad aplicada en la puerta del aparato, y una puerta de servicio para los casos que no la cumplen.

*Las tres puertas que quedan abiertas:*

• *Cuenta completa.* Identidad con documento oficial, veinticinco dólares, prueba de la llave de firma y la lista de todos tus identificadores de app —presentes y futuros—. Con eso publicas por cualquier canal.
• *Cuenta de distribución limitada.* Gratis, sin documento, tope de **veinte aparatos**. Es la puerta para el estudiante y el aficionado.
• *La puerta de servicio.* Instalar de un desarrollador no registrado: modo desarrollador, pantalla de advertencia, PIN, reinicio, **veinticuatro horas de espera**, más advertencias, y entonces «permitir temporalmente (siete días)» o «permitir indefinidamente». Nueve pasos, contados por la propia campaña que los denuncia.

*Lo que sí puedes hacer hoy, y es gratis:* guardar tus APK con nombre y fecha, anotar de dónde salió cada uno, aprender a instalar por cable con ADB —que quedó explícitamente fuera de la regla—, y no votar por la costumbre de bajar cosas de enlaces que no dicen quién las hizo.

*Lo que viene:* 2027, todos los aparatos certificados, todas las apps. El contador de la campaña, cuando lo abrí hoy, marcaba **62 días**.

───────────────────

*🗺️ Mapa de esta guía*

├── 🌱 La semilla + 🎯 el acertijo + ⚡ en una página
├── 📅 Qué pasó el 30 de septiembre + 🔒 el servicio que ya está adentro
├── 🚪 Las tres puertas + 🇩🇴 qué te toca en RD
├── 🏪 F-Droid + 📣 la campaña + 📰 las cuatro contradicciones
├── 🧰 Vivir sin Google + 🔧 el marcador y el cable + 🥇 el aviso
├── 🕰️ Las tres vueltas de cerradura + 👥 cinco casos
├── 📋 La ficha de hoy: los 29 repos, uno por uno
├── 🛠️ Si algo falla + 🧠 decisiones de la prensa + ❓ preguntas + 📖 glosario
├── 🕒 La línea del tiempo + 🔍 el método + 👀 qué vigilar + 🚫 fronteras del dato
├── 📆 Qué hacer este mes + 🧪 cómo comprobarlo en tu teléfono + 📊 los números
├── 🧩 El mini-quiz + 🧾 la vara + 🔗 enlaces + 🤝 lo que le pediría a Google
└── 💬 Nota final + 🎁 el párrafo para copiar

───────────────────

*📅 Qué pasó el 30 de septiembre (y qué no)*

Empecemos por lo que se puede sostener con una fuente y una fecha, porque en este tema abundan las frases que suenan a sentencia y no aguantan una pregunta.

*Lo que dice Google, y llevo tres años leyéndolo igual:* la verificación de desarrolladores es un requisito de identidad para que el sistema sepa quién firma lo que instalas. Su argumento central es que el malware entra por el camino del anonimato: alguien publica algo, se le tumba, y vuelve con otro nombre. Si hay identidad, hay a quién señalar. Ese argumento no es tonto. Es el argumento que yo usaría si fuera ellos.

*Lo que cambió el 30 de septiembre:* la aplicación se activó en cuatro países —Brasil, Indonesia, Singapur y Tailandia— y solo para instalaciones y actualizaciones que vienen de las **siete tiendas participantes**. En un aparato certificado que corre Android 7 o más, si el desarrollador no está registrado, la instalación desde esas tiendas se bloquea.

*Lo que no cambió ese día:*

• *Los APK que bajan por el navegador*, por Telegram, por un grupo de WhatsApp o por un cable USB no están cubiertos todavía por esa primera ola. Llegan en 2027.
• *ADB*, la instalación por cable desde una computadora, quedó fuera de manera explícita. Ese detalle vale oro y lo desarrollo más abajo.
• *Los teléfonos no certificados* —los que corren un Android sin servicios de Google: GrapheneOS, LineageOS, un AOSP pelado— no tienen este verificador, porque el verificador viene por los servicios de Google. Ojo: eso no los hace inmunes a 2027; los hace inmunes *a esta forma* de la regla.
• *Lo que ya está instalado* sigue instalado. La regla habla de instalar y actualizar, no de borrar. Nadie te va a desaparecer la app del teléfono esta semana.

*El dato que la prensa repite mal:* que «Google prohibió instalar APK». No. Lo que hizo fue meter una identidad entre el archivo y el sistema, y dejar tres caminos para pasar. Eso es distinto de prohibir, y es peor en un sentido: una prohibición se ve y se discute; una puerta con nueve pasos se llama «opción para usuarios avanzados» y la mayoría no la usa nunca.

*Aviso de la casa:* yo no voy a decirte que esto es el fin de Android, porque no lo es, ni que no pasa nada, porque sí pasa. Lo que voy a hacer es darte el mapa con las fechas y enseñarte a medir el miedo con la misma vara con que medimos las estrellas.

───────────────────

*🔒 El servicio que ya está adentro*

Aquí está la parte que casi nadie te cuenta y es la que a mí me hizo escribir la pieza.

El mecanismo no viene en una actualización del sistema operativo. Viene por **Google Play Services**, o sea, por la vía silenciosa: el mismo canal por el que te cambian una pantalla o te agregan un servicio sin que tú toques nada. Se llama *Android Developer Verifier*, su paquete es `com.google.android.verifier` y su trabajo es una sola pregunta: *¿el nombre de paquete de esta app está registrado por un desarrollador verificado?*

Ese detalle cambia todo el análisis. Si el mecanismo viviera en el sistema operativo, tendría que pasar por un fabricante, por un portador, por un ciclo de actualización, y podría discutirse en un tribunal con fechas. Al vivir en los servicios de Google, la empresa puede ajustarlo, endurecerlo o desactivarlo **sin actualización del sistema y sin pedirte permiso**. La campaña lo dice con una frase que no exagera: *el flujo corre por Play Services, no por el sistema, así que puede cambiar cuando quieran.*

*Lo verifiqué a mi manera:* no puedo leer el código del verificador —es propietario—, así que no voy a afirmar qué hace por dentro. Lo que sí puedo afirmar es lo que dicen tres fuentes independientes coincidentes: el servicio se distribuye por actualizaciones de sistema de Google, arranca dormido y se activa por región. Lo que no puedo afirmar, y por eso lo dejo dicho: si está en tu teléfono específico, en qué versión, y si ya está activo para la República Dominicana. Eso no se mide desde afuera.

*La consecuencia práctica:* los análisis que hablan de «actualización silenciosa» no están inventando. Están describiendo la arquitectura. Y una arquitectura que permite cambiar la regla sin tocar el teléfono es, en la práctica, una llave que se puede girar desde lejos.

*Lo que sí puedes comprobar tú, en dos minutos:* Ajustes → Aplicaciones → Mostrar aplicaciones del sistema → busca «Android Developer Verifier» o `com.google.android.verifier`. Si aparece, está. Si no aparece, puede que llegue después o que tu aparato no lo reciba. Lo que veas, anótalo con fecha: dentro de un año ese dato te va a servir para comparar, y para no discutir con rumores.

───────────────────

*🚪 Las tres puertas, paso por paso*

Esta es la parte útil de la pieza. Si mañana tienes que instalar algo y no instala, aquí está el mapa de lo que te van a pedir.

*Puerta uno — la cuenta completa.* Es la de los desarrolladores de verdad. Piden documento oficial, veinticinco dólares, prueba de que controlas la llave privada de firma, y una lista de los identificadores de paquete —los nombres únicos de tus apps— presentes **y futuros**. Esa última palabra es la que me hace ruido: *futuros*. Nadie sabe hoy qué app va a escribir en 2028, y sin embargo hay que declararla.

*Puerta dos — la cuenta de distribución limitada.* Gratis, sin documento, con un correo, y con un techo de veinte aparatos. Está pensada para el estudiante, el taller, el club. Es la concesión que Google hizo después de las críticas, y es real: una app para tu familia, para tu negocio pequeño o para tu clase cabe ahí. El techo de veinte es el que hay que tener en la cabeza: no es «poca gente», es *veinte aparatos, contados*.

*Puerta tres — el flujo avanzado.* Es la que te toca si insistes en instalar algo de alguien que no está registrado. Los pasos, tal como los cuenta la campaña y como los describen los medios que los probaron:

*1.* Ajustes → Acerca del teléfono → toca el número de compilación **siete veces** para activar el modo desarrollador.
*2.* Descarta las pantallas de advertencia sobre coacción.
*3.* Escribe tu PIN.
*4.* Reinicia el aparato.
*5.* **Espera veinticuatro horas.** No es un decir: es una espera de reloj.
*6.* Vuelve, descarta más advertencias.
*7.* Elige «permitir temporalmente» —siete días— o «permitir indefinidamente».
*8.* Confirma, otra vez, que entiendes «los riesgos».
*9.* Recién entonces instala.

Nueve pasos y un día de espera para instalar un archivo en un aparato que pagaste tú. Yo no tengo que decirte qué me parece: lo dije arriba con la cerradura. Lo que sí voy a decirte es lo útil: **ese flujo es el que hay que ensayar antes de necesitarlo**. El día que tu teléfono te bloquee una app que sí necesitas, no vas a tener cabeza para descubrir el camino a las once de la noche. Hazlo un domingo tranquilo, con una app que no te importe, y aprende el camino.

*Aviso honesto sobre el flujo:* las capturas y los pasos son de agosto y septiembre de 2026, y Google puede cambiarlos sin avisar —es justo el problema de fondo—. Si al leer esto los pasos no son nueve, no te sorprendas: anota cuántos fueron y con qué fecha, que es lo que hace un archivo y no un rumor.

───────────────────

*🇩🇴 República Dominicana: qué te toca y qué no*

Voy a ser exacto, porque aquí es donde la gente se asusta de gratis.

*Hoy, domingo 1 de noviembre de 2026, en un teléfono comprado en Santo Domingo con una SIM de aquí:* no estás en la lista de los cuatro países. La primera ola fue Brasil, Indonesia, Singapur y Tailandia. El español no está en la primera ola: en América Latina solo entra Brasil, y en portugués. Cuando la regla se globalice en 2027, sí: el aparato certificado que tienes en el bolsillo va a quedar cubierto.

*Lo que eso significa en la práctica, en tres frases:*

• *Nada de lo que instalas hoy por tu cuenta se rompe mañana.* Las apps de tus amigos, el APK del juego, el mod de la cámara: siguen instalándose como siempre mientras estés fuera de la primera ola.
• *El reloj ya está corriendo.* 2027 no es «algún día»: es el año que viene. Y el contador de la campaña, hoy, marcaba 62 días para su propia fecha de cierre.
• *Lo que hagas con tu archivo hoy vale doble mañana.* Un APK guardado con su versión y su fecha es la diferencia entre instalar la app que necesitas y depender de que alguien la vuelva a subir.

*Aviso de la casa sobre el miedo importado:* hay hilos que traducen la noticia de Estados Unidos y la venden como si fuera aquí. No es lo mismo. La regla depende de tres cosas que se pueden verificar —país, certificación del aparato y tienda de origen— y ninguna de las tres es «el idioma que hablas». Si alguien te manda una captura con una fecha, pregúntale en qué país se tomó. Nueve de cada diez veces no lo sabe.

*Aviso de la casa sobre el otro extremo:* tampoco te dejes vender calma. «Eso es en 2027, falta mucho» es cierto y es una manera de no hacer nada. La preparación que sirve —guardar tus archivos, conocer tus fuentes, aprender ADB— se hace mejor con un año de calma que con una semana de pánico.

───────────────────

*🏪 El lado de F-Droid, contado sin épica*

F-Droid es la tienda de apps libres de Android: compila desde el código público, firma lo que entrega y publica la receta. Su modelo choca de frente con la regla nueva, y no por ideología: por **aritmética de firmas**.

*El problema, en una línea:* F-Droid no entrega las apps firmadas por el desarrollador original. Las compila y las firma con **su propia llave**, para garantizar que lo que te llega salió de ese código y no de un archivo que alguien subió. Bajo la regla nueva, un nombre de paquete tiene que estar registrado por un desarrollador verificado y firmado con *su* llave. Si la app que usas viene firmada por el repositorio y no por el autor, la cuenta no cuadra.

*Cómo lo dijo F-Droid:* en septiembre de 2025, en una entrada que tituló sin vueltas, llamó al decreto una amenaza **existencial**. No es una palabra que usen por deporte: es una palabra que describe que su modelo completo —recompilar, revisar, firmar— deja de encajar.

*Lo que hizo mientras tanto, y aquí va mi opinión:* sacó la actualización más grande de su historia. El **24 de septiembre de 2026** publicó **F-Droid 2.0**, reescrita en Kotlin y Compose, con tres áreas —Descubrir, Buscar, Mis apps—, categorías ampliadas, búsqueda que entiende mejor otros alfabetos, filtros combinables y actualizaciones en segundo plano por defecto. Tres días después, el **27 de septiembre**, ya había una 2.0.1 corrigiendo cosas.

*A mí eso me parece lo más honesto que se puede hacer con una amenaza así:* no parar el trabajo, mejorar la casa mientras se discute el contrato del edificio. Y también me parece honesto decir lo que la 2.0 **quitó**, porque un informe que solo cuenta lo bueno no es un informe: se fue la opción de borrar apps después de un disparador de pánico, el gesto de arrastrar para refrescar pasó a un menú, la extensión privilegiada no está soportada y se dejó de dar soporte a Android 6.

*Lo que un usuario dominicano debe sacar en limpio:* si usas F-Droid, actualízala —la 2.0 mejora mucho la experiencia y la búsqueda—, y entiende que su continuidad no depende de tu teléfono sino de una discusión legal que no se gana con tu voto en una encuesta.

───────────────────

*📣 La campaña que firmaron setenta y una organizaciones*

La pelea tiene nombre propio y una casa: *Keep Android Open*, en `keepandroidopen.org`. Nació en octubre de 2025 y no es un grupo de Telegram con entusiasmo: es una campaña con repositorio público —`keepandroidopen/keepandroidopen.github.io`, ★478, licencia CC0, creado el 19 de octubre de 2025 y empujado por última vez el 23 de octubre de 2026— donde vive el sitio que estás leyendo descrito.

*Lo que pide, en su propia voz:* que Google retire el requisito de registro central. No que lo suavice: que lo retire. Esa diferencia es importante, porque Google ya suavizó dos veces —la cuenta limitada gratis y el flujo avanzado— y la campaña dijo que ninguna de las dos resuelve el problema de fondo.

*Los números que se pueden verificar:*

• *24 de febrero de 2026:* carta abierta a la dirección de Alphabet —Sundar Pichai, Larry Page, Sergey Brin y la vicepresidenta del ecosistema de apps— pidiendo la retirada completa.
• *Setenta y una organizaciones* firmantes en veintitrés países, entre ellas la EFF, la FSF, el Proyecto Tor, Proton, KDE, LineageOS, CryptPad, Nextcloud y la Software Freedom Conservancy.
• *Más de cien mil firmas* ciudadanas en la petición.
• *Voces con nombre:* Cory Doctorow lo llamó «Darth Android»; la EFF lo describió como «una vía en expansión constante hacia la censura en internet»; Ars Technica tituló que la envidia de Apple amenaza con desmantelar el legado abierto de Android.

*Lo que no encontré, y lo digo porque es parte del trato:* una respuesta pública formal de Google a esa carta. Hasta donde pude medir, no hay comunicado que la conteste punto por punto. Hay posiciones, entrevistas, argumentos de seguridad —y silencio administrativo sobre la carta—. Eso no es prueba de nada, pero es un dato y se apunta.

*Mi opinión, que es la de esta casa y no la de la campaña:* una petición no cambia una arquitectura. Lo que cambia una arquitectura es que un regulador con dientes —la Comisión Europea, una autoridad de competencia, un tribunal— diga que no se puede. La campaña lo sabe: por eso su página te manda a escribirle a reguladores de más de veinte jurisdicciones y no solo a firmar.

───────────────────

*📰 Las cuatro contradicciones de la prensa (y cómo se resuelven)*

Esta sección existe porque me tocó leer la misma noticia contada de tres maneras distintas en el mismo día, y porque aprender a ver eso es más útil que cualquier conclusión que yo te dé.

*Contradicción uno: «empezó el 30 de septiembre» contra «se movió a 2027».* Los dos titulares circulan. La resolución: son dos cosas distintas con el mismo nombre. La aplicación en cuatro países empezó el 30 de septiembre de 2026; la global es 2027. Cuando un medio dice «se movió», casi siempre está hablando de la global —o está repitiendo una versión vieja de la nota—.

*Contradicción dos: «Android 7 o más» contra «Android 8 o más».* Una fuente habla de los aparatos cubiertos por la regla (7 o más); otra, del servicio verificador (8 o más). No es lo mismo y ninguna de las dos es una errata. Si tu teléfono es viejo, este es el dato que te toca a ti y hay que leerlo con la versión exacta adelante.

*Contradicción tres: «el malware bajó» contra «el malware de Play también existe».* Google sostiene que el camino anónimo es el del malware; la respuesta de F-Droid señala casos de apps maliciosas retiradas de Play —se citan doscientas veinticuatro en un episodio de fraude publicitario con millones de descargas—. La resolución honesta: **las dos cosas pueden ser verdad**. El anonimato facilita el abuso y la tienda grande no es inmune. Eso no decide la discusión sobre la llave, que es otra discusión.

*Contradicción cuatro: «nadie está obligado» contra «te obligan en la práctica»*. Google: la cuenta limitada es gratis y el flujo avanzado existe. La campaña: nueve pasos y veinticuatro horas son un mecanismo de disuasión, no una opción. Las dos frases describen el mismo objeto desde distinto lado del mostrador. Yo me quedo con una pregunta de vara: *¿cuántas personas de tu familia completarían nueve pasos y una espera de un día para instalar una app?* Si la respuesta es «ninguna», entonces el camino existe y no sirve.

*Regla de la casa para leer este tema:* cada vez que veas una fecha, pregúntate qué se aplica ese día, en qué país y a qué aparato. Y cada vez que veas «Google dijo», busca si es una página de soporte, un blog o un vocero. Las tres no pesan igual.

───────────────────

*🧰 Vivir sin los servicios de Google (sin sermón y sin promesas)*

Esta sección no es una invitación a nada. Es un inventario, medido hoy, de lo que existe para el que ya decidió que no quiere depender del verificador. Y empieza con la verdad incómoda: **no hay una salida limpia y gratis para todo el mundo**. Hay caminos, cada uno con su precio en tiempo.

*El camino duro: un Android sin servicios de Google.* GrapheneOS es el caso serio —un sistema endurecido sobre los Pixel— y su sitio, `GrapheneOS/grapheneos.org` (★783, MIT, creado el 25 de abril de 2019, empujado **hoy**), es donde vive su postura. Lo que hay que entender: el verificador no te molesta porque no tienes esos servicios, pero muchas apps de banco, transporte o trabajo no funcionan sin ellos. *Ser libre de la cerradura nueva y quedar fuera de media vida digital es un intercambio, no una victoria.*

*El camino del navegador.* `GrapheneOS/Vanadium` (★2.267, creado en noviembre de 2016, release 156.0.8078.79.0 **del 30 de octubre**, empujado el 30) es su Chromium endurecido. Y `GrapheneOS/Auditor` (★729, MIT, release 92 del 30 de mayo, empujado el 30 de octubre) hace algo que me parece más útil de lo que parece: atestación por hardware y detección de intrusos. Traducido: verificar que el sistema que corre es el que debería correr. En un mundo de puertas con dueño, saber qué corre adentro vale más que prometer que nada corre.

*El camino de reemplazar servicios, uno por uno.* Aquí hay un montón de trabajo de 2026, y esto es lo que medí hoy:

• `degoog-org/degoog` — ★2.505 · AGPL-3.0 · creado el 4 de marzo de 2026 · release 1.1.1 del 25 de octubre. Agregador de buscadores con extensiones: mismo oficio, sin el intermediario de siempre.
• `PimpinPumpkin/Vela` — ★2.299 · GPL-3.0 · creado el 15 de junio de 2026 · release v0.5.2621 del 19 de octubre, empujado hoy. Mapas y navegación paso a paso sin los servicios de Play. Es de los proyectos que más me sorprendió medir: dos mil estrellas en cuatro meses y release este mes.
• `biolend83/tubehaus` — ★187 · AGPL-3.0 · creado el **18 de octubre de 2026** · release app-v0.5.10 **de hoy**. Cliente privado de video, con versión web autoalojada. Dos semanas de vida y ya publicando.
• `Pelski/ytzero` — ★670 · Unlicense · creado el 13 de junio de 2026 · release 2026.09.9 del 28 de septiembre. Otra puerta al mismo contenido, con sus propias reglas.
• `hakerdefo/Robota-Liberated` — ★231 · CC0-1.0 · creado el 10 de abril de 2026 · sin release. Una guía escrita —no una app— sobre cómo quedarse con el Android que compraste. La licencia CC0 es el detalle que más me gusta: se puede copiar sin pedir permiso.
• `LooseWireDev/unclouded` — ★27 · AGPL-3.0 · creado el 10 de marzo de 2026 · sin release, último empuje el 15 de julio. Un catálogo para descubrir apps desde Obtainium. Chiquito y dormido: lo nombro como ejemplo de la capa que casi nadie mide.
• `m-salehi-v/mrowser` — ★64 · MIT · creado el 18 de junio de 2026 · release v1.4.0 del 16 de octubre. Navegador para televisores que ya no reciben apps nuevas. El caso del aparato viejo, que es el 90% de los aparatos.
• `andronedev/openportal` — ★45 · MIT · creado el 10 de junio de 2026 · sin release, empujado el 27 de octubre. Resucitar un aparato abandonado —el Portal de Meta— instalando apps. No es una cerradura, pero es la misma pelea: que el dueño del aparato decida.
• `twinksoftware/Gearslip` — ★229 · AGPL-3.0 · creado el 20 de septiembre de 2026 · release v0.3.12-alpha del 25 de octubre. Alternativa de Android Auto. Seis semanas de vida; lo digo como lo que es: un proyecto joven.
• `GitMag/UnknownAuto` — ★145 · MIT · creado el **29 de octubre de 2026** · release v1.1 del 30 de octubre. Instala apps de Android Auto por la vía lateral. Tres días de vida. No lo recomiendo todavía; lo apunto porque marca hacia dónde va la necesidad.
• `itsmelissadev/SwiftSense` — ★42 · GPL-3.0 · creado el 13 de marzo de 2026 · release v1.3 del 15 de octubre. Suite de optimización sin root: el tipo de herramienta que en 2027 va a depender del flujo avanzado para instalarse.
• `steven-ahfu/Android-TV-Desktop-Toolkit` — ★94 · AGPL-3.0 · creado el 25 de mayo de 2026 · release v4.1.10 del 20 de julio. Ventana y Mac para manejar televisores Android. Dormido hace tres meses.
• `Miniontoby/RokidApkUploader` — ★60 · GPL-3.0 · creado el 15 de enero de 2026 · release v1.0.3 del 9 de abril. Hardware de nicho; entra en la ficha como ejemplo de que «Android» también son las gafas.
• `GrapheneOS/PdfViewer` — ★1.062 · MIT · release 33 del 30 de julio · empujado el 28 de octubre; y `GrapheneOS/Camera` — ★1.423 · MIT · release 93 del 1 de agosto · empujado el 30 de octubre. Las apps de casa hechas para no depender de las de Google.

*Lo que este inventario NO es:* una lista de reemplazos uno a uno. No hay YouTube libre con el mismo catálogo ni mapa libre con el mismo tráfico: quien te venda equivalencia te vende entusiasmo. Lo que existe es *suficiencia*.

───────────────────

*🔧 El truco del marcador, y el cable que nadie menciona*

Dos caminos concretos que la gente está usando hoy, con sus riesgos escritos al lado.

*El marcador.* `daboynb/developer-verifier-placeholder` — ★184 · GPL-3.0 · creado el 16 de julio de 2026 · release `v3000000000000` del mismo día, último empuje el 12 de octubre. Es lo que dice: un APK **vacío** que ocupa el nombre del verificador para que el sistema no lo actualice ni lo active. Un nombre de paquete usado de escudo.

*Mi opinión, sin adorno:* es un truco listo y frágil. Vive de una carrera —que el marcador llegue antes que el servicio real— y esa carrera se pierde el día que Google cambie el nombre o el orden. Un APK que ocupa el lugar de un servicio del sistema es un parche de sistema: si algo se rompe, se rompe donde menos quieres. No lo instalaría como primera medida.

*El cable.* ADB —Android Debug Bridge— quedó explícitamente fuera de la regla. Es la instalación desde una computadora por USB: `adb install app.apk`. No es magia ni es un truco: es la herramienta oficial de desarrollo de Google, la misma que usan los que programan apps. Para el usuario común es incómoda porque necesita una computadora, un cable y aprender tres comandos.

*Y aquí está la parte que no se dice:* para quien lee esto desde Santo Domingo, ADB no es un plan B; es *el* plan que no depende de nadie. Un teléfono, una laptop vieja y un cable: una puerta que sigue abierta porque no pasa por los servicios de Google.

*Herramientas medidas hoy:*

• `Ruraam/Uraam` — ★50 · GPL-3.0 · creado el 5 de junio de 2026 · release v4.4.6 **de ayer**. Gestor de apps por ADB en el teléfono: lista, instala, desinstala, congela. Empujado el 31 de octubre.
• `zechuan-start/adb-gui` — ★72 · AGPL-3.0 · creado el 28 de junio de 2026 · release v0.1.12 del 27 de octubre. Ventana gráfica sobre ADB: dispositivos, capturas, grabación de pantalla e instalación de APK. Para el que no quiere teclear.
• `austinsager/adv-install` — ★27 · MIT · creado el 18 de julio de 2026 · release v0.1.1 del 19 de julio, dormido desde entonces. Instalación estilo ADB desde el propio teléfono con Termux o Shizuku.
• `audioeng89/tiny_apk_installer` — ★50 · MIT · creado y publicado el 26 de marzo de 2026, sin movimiento desde entonces. Un instalador de terminal, mínimo. Lo incluyo como lo que es: una idea buena que nadie siguió.

*La verdad sobre ADB, completa:* sirve para instalar y no arregla el fondo. Si en 2027 el sistema exige identidad al instalar, no hay certeza de que ADB siga siendo la excepción —hoy lo es—. **Lo que hoy es una puerta, mañana puede ser una ventana**: aprende el camino y no le jures lealtad.

───────────────────

*🥇 El aviso dentro de la app*

Hay una pieza más callada que cualquier campaña: una biblioteca de aviso.

`woheller69/FreeDroidWarn` — ★3.730 · Apache-2.0 · creado el 26 de agosto de 2025 · release **V1.14 del 9 de septiembre de 2026** · último empuje el 28 de octubre. Cualquier desarrollador puede meterla en su app para que, cuando el usuario la abra, vea un aviso: *esta app podría dejar de instalarse en el futuro por la regla tal*. No hay campaña, no hay cuenta, no hay petición: hay un cartel dentro del producto.

*Por qué me parece la más útil de la ficha:* porque informa donde el usuario está mirando. Una carta abierta la lee quien ya está de acuerdo con ella; un aviso dentro de la app lo lee el que la usa, aunque no sepa que hay una discusión.

*Su costo, sin adornos:* el aviso ocupa pantalla y asusta, y una app que asusta a su usuario puede perderlo. Que 3.730 personas le hayan dado estrella a una biblioteca que hace eso dice que el miedo está más repartido de lo que la prensa cuenta.

───────────────────

*🕰️ Esto no nació ayer: las tres veces que Android cambió de cerrajero*

Para entender por qué hay gente que no se sorprende, conviene ver el patrón. No es la primera vez que el teléfono que compraste recibe una regla nueva después de la compra.

*Primera vez — el escáner.* Play Protect empezó a revisar lo que instalabas, viniera de donde viniera. La mayoría lo aceptó porque el intercambio era claro: menos malware a cambio de que alguien mirara los archivos. Fue una decisión discutible y razonable a la vez. **Y no dependía de quién eras.**

*Segunda vez — la atestación.* SafetyNet primero y Play Integrity después respondieron otra pregunta: *¿este aparato es de confianza?* Muchas apps de banco empezaron a negarse a correr en teléfonos con el cargador desbloqueado o con un sistema alternativo. Ahí el criterio dejó de ser «qué app es» y pasó a ser «qué aparato es». Consecuencia práctica que muchos vivieron sin saber por qué: la app del banco que se cerraba sola en un teléfono flasheado.

*Tercera vez — la identidad del que firma.* Es la de ahora, y es la más profunda de las tres porque no pregunta por el archivo ni por el aparato: pregunta por la persona. Y esa pregunta, a diferencia de las otras dos, **no tiene respuesta técnica**. No puedes compilar tu manera de salir de ella.

*Lo que dice el patrón, y es mi lectura:* cada paso fue más lejos en la cadena, del contenido al aparato y del aparato al autor. Nada de esto llegó con una sola actualización escandalosa; llegó en tres tramos, cada uno con su justificación razonable. Esa es la manera en que se mueve una cerradura: no de un golpe, sino de una vuelta por año.

*Aviso de honestidad:* las tres veces que acabo de describir son historia bien documentada, no opinión. Mi lectura del patrón sí es opinión, y la marco como tal para que puedas discutirla.

───────────────────

*👥 Cinco casos, cinco respuestas (para que lo lleves a tu vida)*

*Caso A — La estudiante con una app que compiló su primo.*
Hoy en RD no cambia nada. En 2027 esa app necesitará una de dos cosas: que el primo abra una cuenta limitada de veinte aparatos —gratis— o que alguien use el flujo avanzado. *Consejo:* que el primo la abra **ahora**, sin presión, y guarde el APK con su versión.

*Caso B — El taller que instala apps de diagnóstico.*
Aquí sí hay problema, y no es de ideología: si cada teléfono cuenta como aparato, la cuenta de veinte se queda corta rápido. Opciones: cuenta completa con llave, flujo avanzado por aparato, o ADB desde la computadora del taller. *Consejo:* aprender ADB este año; un cable resuelve más que una discusión en los comentarios.

*Caso C — La señora que solo usa WhatsApp, la banca y la cámara.*
Para ella no cambia nada: las apps de las tiendas grandes siguen porque sus desarrolladores están registrados. Su riesgo no es la regla, es el «técnico» que le instala un APK desconocido aprovechando el ruido.

*Caso D — El activista o el periodista con una app que no está en ninguna tienda.*
Es el caso que la regla castiga de verdad, y la EFF lo dice sin rodeos: registrarse —y quedar identificado— o depender del flujo y de ADB. *Consejo:* aprender ADB y tener un teléfono de respaldo sin servicios de Google. No es paranoia: es continuidad.

*Caso E — El del teléfono de 2019 sin actualizaciones.*
Su problema no es el verificador: es que las apps nuevas piden versiones que su aparato no tiene. La regla no lo empeora de inmediato, pero le quita el consuelo de «al menos instalo lo que sea». *Consejo:* guardar las últimas versiones compatibles y no borrarlas al actualizar.

───────────────────

*📋 LA FICHA DE HOY — 33 repositorios medidos uno por uno*

Todo lo de abajo lo consulté hoy con la API de GitHub: estrellas, licencia declarada, lenguaje, fecha de creación, último empuje y última release con su fecha. Lo que no tiene número es porque no es un repositorio de GitHub —F-Droid vive en GitLab y su cliente no está en esta lista— y lo digo en vez de inventarlo.

*La campaña y el aviso:*

• **keepandroidopen/keepandroidopen.github.io** — ★478 · CC0-1.0 · creado 19-oct-2025 · sin release · empuje 23-oct-2026 → el sitio de la campaña, con su carta y sus enlaces
• **woheller69/FreeDroidWarn** — ★3.730 · Apache-2.0 · creado 26-ago-2025 · release V1.14 (9-sep) · empuje 28-oct → el aviso dentro de la app
• **tsunderswapElnina/Keep-Android-Open-UI** — ★1 · MIT · creado 12-oct-2026 · release v1.0.1-patch1 (13-oct) → un reloj de cuenta regresiva hecho app; lo incluyo por honestidad de escala

*El marcador y los instaladores por cable:*

• **daboynb/developer-verifier-placeholder** — ★184 · GPL-3.0 · creado 16-jul-2026 · release v3000000000000 (16-jul) · empuje 12-oct → APK vacío que ocupa el nombre del verificador
• **zechuan-start/adb-gui** — ★72 · AGPL-3.0 · creado 28-jun-2026 · release v0.1.12 (27-oct) → ADB con ventana
• **Ruraam/Uraam** — ★50 · GPL-3.0 · creado 5-jun-2026 · release v4.4.6 (31-oct) → gestor de apps por ADB en el teléfono
• **audioeng89/tiny_apk_installer** — ★50 · MIT · creado 26-mar-2026 · release 0.1.0 (26-mar) → instalador de terminal, dormido
• **austinsager/adv-install** — ★27 · MIT · creado 18-jul-2026 · release v0.1.1 (19-jul) → instalación estilo ADB desde el aparato

*El sistema sin servicios de Google:*

• **GrapheneOS/Vanadium** — ★2.267 · NOASSERTION (la API no reconoce la licencia) · creado 22-nov-2016 · release 156.0.8078.79.0 (30-oct) → el navegador endurecido
• **GrapheneOS/Auditor** — ★729 · MIT · creado 30-ene-2018 · release 92 (30-may) · empuje 30-oct → atestación e intrusos
• **GrapheneOS/grapheneos.org** — ★783 · MIT · creado 25-abr-2019 · sin release · empuje hoy → la casa y sus notas
• **GrapheneOS/Camera** — ★1.423 · MIT · creado 17-ago-2021 · release 93 (1-ago) → cámara sin dependencias de Google
• **GrapheneOS/PdfViewer** — ★1.062 · MIT · creado 16-ene-2017 · release 33 (30-jul) → lector de PDF por content providers
• **GrapheneOS/hardened_malloc** — ★2.048 · MIT · creado 23-ago-2018 · release 14 (22-feb) · empuje hoy → el asignador de memoria que explica su fama

*Reemplazos, uno por uno:*

• **degoog-org/degoog** — ★2.505 · AGPL-3.0 · creado 4-mar-2026 · release 1.1.1 (25-oct)
• **PimpinPumpkin/Vela** — ★2.299 · GPL-3.0 · creado 15-jun-2026 · release v0.5.2621 (19-oct) · empuje hoy
• **Pelski/ytzero** — ★670 · Unlicense · creado 13-jun-2026 · release 2026.09.9 (28-sep)
• **hakerdefo/Robota-Liberated** — ★231 · CC0-1.0 · creado 10-abr-2026 · sin release · empuje 3-jun
• **twinksoftware/Gearslip** — ★229 · AGPL-3.0 · creado 20-sep-2026 · release v0.3.12-alpha (25-oct)
• **biolend83/tubehaus** — ★187 · AGPL-3.0 · creado 18-oct-2026 · release app-v0.5.10 (hoy) · empuje hoy
• **GitMag/UnknownAuto** — ★145 · MIT · creado 29-oct-2026 · release v1.1 (30-oct)
• **steven-ahfu/Android-TV-Desktop-Toolkit** — ★94 · AGPL-3.0 · creado 25-may-2026 · release v4.1.10 (20-jul)
• **m-salehi-v/mrowser** — ★64 · MIT · creado 18-jun-2026 · release v1.4.0 (16-oct)
• **Miniontoby/RokidApkUploader** — ★60 · GPL-3.0 · creado 15-ene-2026 · release v1.0.3 (9-abr)
• **andronedev/openportal** — ★45 · MIT · creado 10-jun-2026 · sin release · empuje 27-oct
• **itsmelissadev/SwiftSense** — ★42 · GPL-3.0 · creado 13-mar-2026 · release v1.3 (15-oct)
• **LooseWireDev/unclouded** — ★27 · AGPL-3.0 · creado 10-mar-2026 · sin release · empuje 15-jul
• **bl3xand/APK-Toolbox** — ★99 · GPL-3.0 · creado 8-oct-2026 · release v1.1.6 (28-oct) → rastrear, clonar, instalar y fusionar APK en el propio teléfono
• **richardkfm/los-bootstrap** — ★6 · GPL-3.0 · creado 28-abr-2026 · release v0.14.0 (15-oct) → instalar y dejar listo LineageOS en un teléfono ya liberado
• **Ha2mad/package-pass** — ★0 · MIT · creado 28-oct-2026 · sin release → leer en lote los nombres de paquete para ver qué hay que registrar
• **Meirwolf1289/fdroid-census** — ★0 · sin licencia declarada · creado 31-oct-2026 · sin release → contar cuántas apps de F-Droid están registradas ante Google

*Los dos que no están por su tema sino por su lección:*

• **FoedusProgramme/Checker** — ★83 · GPL-3.0 · creado 29-oct-2023 · release 1.0.9 (18-ene-2024) · último empuje 18-ene-2024 → dos años de silencio y sigue vivo: dormido no es muerto
• **HydraDragonAntivirus/HydraDragonAV-Mobile** — ★23 · GPL-2.0 · creado 16-jun-2026 · release v1.4.2 (6-ago) → antivirus sin root ni ADB; entra porque el miedo también produce herramientas, y hay que medirlas

───────────────────

*🆕 Cuatro que nacieron este mes (y por eso no estaban en ninguna lista)*

Los busqué hoy y no salen de ningún listado viejo:

• `bl3xand/APK-Toolbox` — ★99 · GPL-3.0 · creado el 8 de octubre · release v1.1.6 del 28. Rastrea, clona, instala y fusiona APK en el propio teléfono. Tres semanas de vida y ya con release: es lo más nuevo y lo más útil de la ficha para el que se está preparando.
• `richardkfm/los-bootstrap` — ★6 · GPL-3.0 · creado el 28 de abril · release v0.14.0 del 15 de octubre. Instala y deja listo LineageOS en un teléfono ya liberado de Google. El camino duro, con script.
• `Ha2mad/package-pass` — ★0 · MIT · creado el 28 de octubre. Lee en lote los nombres de paquete de tus apps: sirve para saber qué hay que registrar y qué se queda fuera. Cuatro días de vida.
• `Meirwolf1289/fdroid-census` — ★0 · sin licencia declarada · creado **ayer mismo**, 31 de octubre. Su pregunta es la que importa: cuántas apps de F-Droid están registradas ante Google. Cero estrellas no es cero valor: es el primer intento de **contar** el choque en vez de describirlo.

Los cuatro los encontré hoy buscando por tema en la API de GitHub, filtrando por fecha de creación posterior a mayo de 2026 y ordenando por estrellas: nada de listas guardadas.

Y nacieron porque alguien no encontró la herramienta que necesitaba. Eso es lo que produce una cerradura nueva: gente escribiendo lo que falta a las dos de la mañana, sin pedirle permiso a nadie.

*Lo que este censo no dice:* cuánta gente usa cada cosa. Las estrellas miden curiosidad, no adopción: `UnknownAuto` con ★145 en tres días puede tener cero usuarios, y `unclouded` con ★27 y dormido puede estar funcionando en la casa de alguien.

───────────────────

*🛠️ Si algo falla (soluciones reales, no genéricas)*

*«Instalé una app y salió un aviso de desarrollador no verificado».*
Estás en un aparato donde la regla ya está activa —o en una app que trae el aviso de FreeDroidWarn—. Orden de intentos, del más barato al más caro: primero comprueba que el APK sea del sitio oficial del proyecto; segundo, actualiza por ADB desde una computadora; tercero, si insistes, el flujo avanzado con sus veinticuatro horas. No hay cuarto paso mágico: cualquier «método» que prometa saltarse la espera con una app de terceros está pidiendo permisos que no deberías dar.

*«La app se cerró sola después de actualizar el teléfono».*
Casi nunca es la verificación: es Play Integrity respondiendo «no confío en este aparato». Pasa en teléfonos con el cargador desbloqueado o con sistemas alternativos. Solución honesta: no hay. Si tu banco exige un aparato certificado, tu teléfono modificado no va a pasar, y ninguna app de la ficha lo cambia.

*«Quiero guardar mis apps antes de 2027 y no sé cómo».*
Descarga el APK desde el sitio oficial del proyecto —no desde un agregador—, ponle al archivo un nombre con la app, la versión y la fecha (`vela-0.5.2621-2026-11-01.apk`), y guárdalo en dos sitios: el teléfono y una carpeta en la computadora o en la nube. Los APK ocupan poco; veinte apps son menos que una foto de un concierto.

*«No tengo computadora para ADB».*
Entonces tu camino es la cuenta limitada si desarrollas, o el flujo avanzado si solo consumes. Y una alternativa que casi nadie usa: un amigo con laptop. ADB no necesita que el teléfono sea de él; necesita el cable y permiso de depuración en el tuyo.

*«Esto es mentira, yo instalo APK todos los días y no pasa nada».*
Las dos cosas son verdad: hoy no pasa nada en la República Dominicana, y la regla existe. Que no te toque todavía no la vuelve falsa; que exista no la vuelve inminente. Esa es toda la vara.

*«¿Y si me espero a ver qué pasa?»*
Es una decisión legítima y no te voy a regañar por ella. Lo único que te pido es que la espera sea informada: si en 2027 te agarra sin copias y sin saber usar un cable, la espera te costó caro. Si te agarra con las apps guardadas y el flujo probado una vez, la espera no te costó nada.

───────────────────

*🧠 Cinco decisiones que la prensa toma por ti*

*Uno: elige tu bando antes de leer.* Casi toda la cobertura de este tema se escribe desde una trinchera: «Google nos protege» o «Google nos encierra». Las dos tienen datos y las dos exageran. La casa no elige bando: elige hechos con fecha. Cuando leas, separa lo que se midió de lo que se opina, y te vas a dar cuenta de que el 80% de los párrafos son opinión con números pegados.

*Dos: convierte una fecha en «el fin de Android».* El 30 de septiembre de 2026 no terminó nada: cuatro países, siete tiendas, una condición. Cuando una noticia usa una fecha como martillazo, casi siempre está vendiendo un clic. La pregunta útil no es «¿se acabó?» sino «¿qué se aplica, dónde, a quién y desde cuándo?».

*Tres: confunde el nombre con la cosa.* «Verificación de desarrolladores» suena a trámite. «Bloqueo» suena a cárcel. La cosa es una condición de instalación que corre en los servicios de Google y que se puede endurecer sin avisar. Si te quedas con el nombre, pierdes la parte que importa.

*Cuatro: te hace elegir entre seguridad y libertad, como si fueran un interruptor.* No lo son. Se puede tener identidad de desarrollador **y** libertad de instalación: son ejes distintos, y el debate real es cuánta fricción se le pone al que instala. Cualquiera que te obligue a escoger un polo te está ahorrando el análisis, no regalándote claridad.

*Cinco: la campaña como marca.* Keep Android Open es un sitio con CC0 y una carta; no es un partido. Puedes firmar y no instalar nada de la ficha, o usar GrapheneOS y pensar que la campaña exagera. La vara no pide carné.

───────────────────

*❓ Preguntas que me hacen (y respuestas cortas)*

*«¿Me van a borrar WhatsApp?»* No. La regla habla de instalar y actualizar. Y WhatsApp, además, viene de una tienda participante con desarrollador registrado.

*«¿F-Droid va a desaparecer?»* Su modelo actual, tal como está, no encaja con la regla global de 2027. Decir «desaparece» es una predicción; decir «está en riesgo existencial, por su propia boca» es un hecho.

*«¿Es verdad que habrá que pagar veinticinco dólares para publicar una app?»* Para la cuenta completa, sí, es la misma cuenta de Play que ya cuesta eso. Para la limitada de veinte aparatos, no: es gratis.

*«¿Y las apps que ya tengo instaladas?»* Siguen. La regla no desinstala. Lo que cambia es que actualizarlas puede requerir que el desarrollador esté registrado.

*«¿Los iPhone tienen lo mismo?»* Peor y desde antes: en iPhone solo instalas por la tienda o por un proceso de desarrollador. La diferencia es que Apple nunca prometió lo contrario. Android sí lo prometió, y de eso se trata esta pieza.

*«¿Es culpa de los usuarios que instalan basura?»* En parte, y decirlo no absuelve a nadie. La pregunta que decide es otra: si el problema es el malware, ¿por qué la solución es una identidad y no un antivirus? Cuando la herramienta no corresponde al problema, vale preguntar a quién le sirve.

*«¿Tú qué harías?»* Guardar mis APK con fecha, aprender ADB este año, enseñarle el flujo a dos personas de mi familia y no firmar nada que no haya leído. No hay revolución en esa lista, y por eso se puede hacer un domingo.

───────────────────

*📖 Glosario mínimo*

• *APK* — el archivo instalable de una app; a veces viene partido por arquitectura o idioma.
• *ADB* — puente de depuración: la herramienta oficial para hablar con el teléfono por cable.
• *Aparato certificado* — el que pasó la certificación de Google y trae sus servicios.
• *Cuenta limitada* — registro gratis, sin documento, con tope de veinte aparatos.
• *Firma* — la huella que dice quién empaquetó la app; si cambia, el sistema no actualiza.
• *Sideload* — instalar por fuera de la tienda. No es ilegal ni es sinónimo de mod.

───────────────────

*🕒 La línea del tiempo, con las fechas que sí sostienen*

*Agosto de 2025* — Google anuncia el requisito de verificación de desarrolladores en su página de documentación.
*Septiembre de 2025* — F-Droid publica su respuesta y llama al decreto una amenaza existencial.
*Octubre de 2025* — nace la campaña Keep Android Open. Su repositorio se crea el día 19.
*Febrero de 2026* — el día 24, carta abierta a la dirección de Alphabet. Para abril ya suma más de sesenta organizaciones.
*Marzo de 2026* — Google publica su entrada de blog explicando el programa y confirma el calendario; medios independientes lo critican con dureza.
*Mayo–junio de 2026* — se reporta que el servicio Android Developer Verifier empieza a llegar a aparatos; las fechas varían según la fuente.
*Julio de 2026* — abre el acceso temprano a la cuenta de distribución limitada y a la API de estado de identidad.
*Agosto de 2026* — se lanza globalmente el flujo avanzado y la cuenta limitada gratuita.
*Septiembre de 2026* — el día 9 sale FreeDroidWarn V1.14; el 24 sale F-Droid 2.0; el 27, la 2.0.1; el 30, la aplicación en cuatro países.
*Octubre de 2026* — primeros reportes de la regla en funcionamiento; aparece el marcador del verificador y crecen las herramientas de instalación por cable.
*1 de noviembre de 2026* — esta pieza. 62 días en el contador de la campaña.
*2027* — expansión global a todos los aparatos certificados, todas las apps. Sin fecha exacta anunciada.

*Aviso:* la armé con fuentes públicas que se contradicen en dos puntos —la fecha exacta de llegada del verificador y la versión de Android cubierta—. Donde hay contradicción lo digo; donde hay consenso, lo afirmo.

───────────────────

*🔍 Cómo se mide una noticia así (el método, para que me desmientas)*

Esta sección es la que hace que la pieza sea de esta casa y no un resumen más.

*Primero: separo tipos de fuente.* Documentación oficial de Google (una cosa), blog corporativo (otra), cobertura de prensa (otra), campaña de activistas (otra). Las cuatro sirven y ninguna es neutra. Cuando escribo «Google dice», debe haber una página de Google; cuando escribo «la campaña denuncia», debe estar en su sitio.

*Segundo: busco la fecha y el sujeto de cada afirmación.* «La regla entró en vigor» no significa nada sin país, aparato y tienda: eso obligó a escribir la condición completa cuatro veces.

*Tercero: marco lo que no puedo verificar.* No puedo leer el verificador porque es propietario, ni saber si está activo en tu teléfono, ni cuánta gente usa cada herramienta. Esa lista es tan importante como la de lo medido.

*Cuarto: mido los repos con la API y les pongo la hora.* Los 33 de la ficha llevan estrellas, licencia, creación, empuje y release; y la hora de la medición está en la firma.

*Quinto: desconfío de mi entusiasmo.* Con villano claro se escribe mejor y se verifica menos. La prueba: aquí hay una sección entera con el argumento de Google, en serio.

───────────────────

*👀 Qué vigilar en los próximos sesenta días*

Cuatro cosas concretas, con nombre y con qué significa cada una:

*1. El contador de la campaña.* Marcaba 62 días al abrirla hoy. Si se reinicia o cambia de fecha, es noticia: algo se movió en el calendario oficial o en la campaña.

*2. La respuesta de los reguladores.* Hay una pregunta escrita de una eurodiputada a la Comisión Europea sobre si esto cabe en la ley de mercados digitales. Si se vuelve expediente, pasa de discusión de blogueros a problema legal para Google.

*3. La primera ola, en la práctica.* Brasil, Indonesia, Singapur y Tailandia son el laboratorio. Lo que hay que mirar son tres datos: cuánta gente completa el flujo, si las tiendas pequeñas pierden instalaciones y si aparece una alternativa técnica que nadie previó.

*4. Los proyectos de la ficha que se muevan.* `Uraam` publicó ayer; `tubehaus`, `Vela` y `grapheneos.org`, hoy. Si en dos meses siguen publicando es señal; si paran, también.

───────────────────

*🚫 Fronteras del dato: lo que no se afirma*

• *No dice que Google vaya a bloquear apps ya instaladas.* No hay evidencia de eso y no lo voy a inventar para asustar.
• *No dice que el flujo avanzado no exista.* Existe, y lo describí con sus nueve pasos. Lo que digo es que está diseñado para que casi nadie lo use, y eso es una opinión fundada, no un hecho medido.
• *No dice que F-Droid vaya a morir.* Dice que su modelo choca con la regla, en su propia voz, y que la aritmética de firmas es el punto exacto del choque.
• *No dice que un Android sin servicios de Google sea la solución.* Dice que es un camino con precio, y nombra el precio: apps que no funcionan.
• *No dice que la campaña tenga razón en todo.* Tiene una posición y la defiende; yo defiendo que la leas y verifiques sus fechas contra las de Google.
• *No dice que esto sea el fin de Android.* Dice que es la tercera vuelta de cerradura, y que las tres primeras se dieron sin que casi nadie mirara.

───────────────────

*📆 Qué hacer este mes (sin dramatismo y sin dejarlo para 2027)*

*Semana uno — el inventario.* Mira qué tienes instalado que no venga de Play. Cinco o seis apps bastan. Anota de dónde salió cada una y si la usarías dentro de un año.

*Semana dos — las copias.* Baja el APK desde su sitio oficial y guárdalo con nombre, versión y fecha, en dos sitios. Toma una hora y vale más que cualquier campaña.

*Semana tres — el cable.* Con una computadora y un cable, activa la depuración por USB e instala algo por ADB que no te importe. La primera vez da respeto; la segunda es rutina.

*Semana cuatro — el flujo.* Si estás en un país de la primera ola, pruébalo una vez; si no —el caso dominicano—, léelo y guárdalo: toca en 2027.

*Y una cosa que no es tarea y sí importa:* cuéntaselo a una persona. No a diez: a una. La tía que le instala cosas el vecino, el primo del taller. La información que no se comparte con alguien concreto se queda en el hilo.

───────────────────

*🧪 Cómo comprobar tú mismo si tu teléfono lo tiene*

No hay que creerme: hay que mirar. Estas son las comprobaciones que cualquiera puede hacer en su aparato, de la más simple a la más técnica.

*Uno — Ajustes, aplicaciones del sistema.* En Ajustes → Aplicaciones → Mostrar aplicaciones del sistema, busca algo con «verifier», «verificador» o el nombre del paquete `com.google.android.verifier`. Si aparece, tu teléfono tiene el módulo. Si no aparece, o no llegó o está escondido; las dos cosas son posibles y por eso esta comprobación no es concluyente.

*Dos — la fecha de los servicios de Google.* Ajustes → Google → Servicios de Google → Información de la versión. Ahí están los módulos que han llegado; uno nuevo con fecha reciente es la señal más honesta de que algo entró sin pedirte permiso.

*Tres — la prueba real.* Instala algo de una fuente fuera de las tiendas grandes. Si te deja sin más, la regla todavía no te toca; si sale un aviso de desarrollador no verificado, ya te toca. Es la única prueba que no depende de interpretación.

*Cuarto — el cable.* Con el teléfono conectado y la depuración activa: `adb shell pm list packages | grep -i verifier`. Una línea significa que está; vacío, que no. Y `adb shell dumpsys package com.google.android.verifier` da versión y fecha. Esa es la diferencia entre mirar tu aparato y repetir un titular.

*Lo que no te da:* certeza sobre 2027. Puede no tener el módulo hoy y recibirlo en marzo. La comprobación mide el presente.

───────────────────

*📊 Los números de la pieza, juntos*

• *62* — días del contador al abrirla hoy (3 de enero de 2027) · *4* — países de la primera ola, el 30 de septiembre de 2026 · *7* — tiendas
• *2027* — expansión global, sin día anunciado · *9* — pasos del flujo · *24* — horas de espera · *7* — días de permiso temporal
• *20* — aparatos de la cuenta limitada · *0* — dólares · *25* — dólares de la cuenta completa · *71* — organizaciones de *23* países · *+100.000* firmas
• *33* — repositorios medidos hoy · *33* — enlaces comprobados, todos 200 · *224* — apps que Play retiró en 2025 · *19 millones* — descargas que sumaban
• *50 veces* — más malware fuera de su tienda, según Google, y sin verificar por mi parte · *3* — veces que cambió el cerrajero

───────────────────

*🧩 Mini-quiz (para saber si te quedó algo)*

*1.* ¿Qué cuatro países entraron primero y en qué fecha?

*2.* ¿Cuántas tiendas participan en esa primera ola y cuál es la condición exacta que se aplica?

*3.* ¿Cuántos aparatos cubre la cuenta de distribución limitada y cuánto cuesta?

*4.* ¿Qué herramienta de instalación quedó explícitamente fuera de la regla, y por qué importa para un país como el nuestro?

*5.* ¿Por qué el modelo de firmas de F-Droid choca con la regla nueva?

*Respuestas al revés (léelas de atrás para adelante):*

1. .6202 ed erbmeitpes ed 03 le ,aidnaliaT y rupagniS ,aisenodnI ,lisarB

2. .salle ed eneiv euq nóicazilautca o nóicalatsni al ne odacifirev y odartsiger étse rodallorrased le euq se nóicidnoc al y ,sadneit eteiS

3. .otnemucod edip on y sitarg se adatimil atneuc al :seralód orec y sotarapa etnieV

4. .alortnoc onu euq atreup al odneis eugis y elgooG ed soicivres sol rop asap on euqrop atropmi ;elbac rop nóicalatsni al ,BDA

5. .odacifirev rodallorrased le rop odamrif y odartsiger étse eteuqap le euq edip alger al y ,evall aiporp us noc amrif y alipmoc diorD-F euqroP

───────────────────

*🧾 La vara aplicada, en cuatro frases*

*Primera:* el problema no es que Google tenga una tienda con reglas, sino que la regla salió de la tienda y se paró en la puerta del aparato.

*Segunda:* el argumento de seguridad es real e insuficiente. Un documento no hace seguro el código; hace rastreable al autor.

*Tercera:* los veinte aparatos y el flujo de nueve pasos son reales y no resuelven el fondo: una puerta que casi nadie cruza es una puerta cerrada con letrero amable.

*Cuarta:* lo único que puedes hacer sin permiso de nadie es guardar tus archivos, saber tus fuentes y aprender el cable.

───────────────────

*🔗 Enlaces de esta pieza*

*La campaña y el aviso:*
- Keep Android Open (sitio de la campaña): https://github.com/keepandroidopen/keepandroidopen.github.io
- FreeDroidWarn (el aviso dentro de la app): https://github.com/woheller69/FreeDroidWarn
- Keep Android Open UI (reloj de cuenta regresiva): https://github.com/tsunderswapElnina/Keep-Android-Open-UI

*El marcador y los instaladores por cable:*
- developer-verifier-placeholder (el marcador): https://github.com/daboynb/developer-verifier-placeholder
- adb-gui: https://github.com/zechuan-start/adb-gui
- Uraam: https://github.com/Ruraam/Uraam
- tiny_apk_installer: https://github.com/audioeng89/tiny_apk_installer
- adv-install: https://github.com/austinsager/adv-install

*El sistema sin servicios de Google:*
- Vanadium (navegador): https://github.com/GrapheneOS/Vanadium
- Auditor: https://github.com/GrapheneOS/Auditor
- GrapheneOS (sitio): https://github.com/GrapheneOS/grapheneos.org
- Camera: https://github.com/GrapheneOS/Camera
- PdfViewer: https://github.com/GrapheneOS/PdfViewer
- hardened_malloc: https://github.com/GrapheneOS/hardened_malloc

*Reemplazos, uno por uno:*
- degoog: https://github.com/degoog-org/degoog
- Vela (mapas): https://github.com/PimpinPumpkin/Vela
- ytzero: https://github.com/Pelski/ytzero
- Robota-Liberated: https://github.com/hakerdefo/Robota-Liberated
- Gearslip: https://github.com/twinksoftware/Gearslip
- tubehaus: https://github.com/biolend83/tubehaus
- UnknownAuto: https://github.com/GitMag/UnknownAuto
- Android TV Desktop Toolkit: https://github.com/steven-ahfu/Android-TV-Desktop-Toolkit
- mrowser: https://github.com/m-salehi-v/mrowser
- RokidApkUploader: https://github.com/Miniontoby/RokidApkUploader
- openportal: https://github.com/andronedev/openportal
- SwiftSense: https://github.com/itsmelissadev/SwiftSense
- unclouded: https://github.com/LooseWireDev/unclouded
- APK-Toolbox: https://github.com/bl3xand/APK-Toolbox
- los-bootstrap: https://github.com/richardkfm/los-bootstrap
- package-pass: https://github.com/Ha2mad/package-pass
- fdroid-census: https://github.com/Meirwolf1289/fdroid-census

*Los dos que entran por su lección:*
- Checker: https://github.com/FoedusProgramme/Checker
- HydraDragonAV-Mobile: https://github.com/HydraDragonAntivirus/HydraDragonAV-Mobile

*Aviso:* ninguno instala nada solo. Los de la campaña y la guía son texto; los de apps traen su release y su licencia a la vista. Lo que no enlazo es cualquier cosa que prometa saltarse la verificación sin decir qué te pide a cambio.
───────────────────

*🤝 Lo que le pediría a Google, y lo que le pediría a F-Droid*

*A Google:* una cosa sola, y es barata. Que el aviso de «desarrollador no verificado» diga **quiénes son** los que no están verificados y **por qué** no lo están. Hoy el aviso no distingue entre un desarrollador que no se registró porque no quiere y uno que no puede porque su país no está en la lista o porque no tiene veinticinco dólares. Un aviso que trata igual a los dos no informa: desconfía.

*A F-Droid:* que publique su aritmética. Si su modelo de firmas choca con la regla, el número exacto —cuántos paquetes, cuántas llaves, cuánto cuesta migrar— vale más que diez comunicados. Los comunicados convencen a los que ya están de acuerdo; un número convence a un regulador.

*A las dos:* que dejen de escribir como si el usuario fuera tonto. El que instala un APK sabe que está asumiendo un riesgo. Lo que no sabía es que el riesgo lo iba a asumir en 2027 por una decisión tomada en 2025.

───────────────────

*💬 Una nota final sobre el tono*

Podía escribir esto con trompetas —«¡te van a quitar el teléfono!»— y tener más compartidas y menos verdad; o con sordina —«en 2027 falta mucho»— y tener más calma y menos utilidad.

Intenté lo de siempre: qué pasó con fecha y fuente, qué no pasó aunque no dé titulares, y el mapa de lo que sí puedes hacer hoy.

La cerradura cambió de dueño y todavía no llegó a tu puerta. Es una ventaja, no una excusa: es el tiempo exacto para tener tus copias, saber tus fuentes y conocer el cable.

───────────────────

*🎁 Para copiar y pegar*

> «En 2027, instalar una app que no esté en una tienda grande va a pedir que su autor se haya identificado con Google, salvo que uses el flujo de nueve pasos y veinticuatro horas. Hoy no aplica en RD. Guardo mis APK con fecha, sé de dónde salen y estoy aprendiendo ADB. Eso es todo lo que puedo controlar.»

Puedes mandarlo tal cual a tu grupo: no promete nada falso ni asusta a nadie.

> —¿Y si Google cambia la cerradura otra vez?
> —Entonces el cable y tus copias ya te conocen la puerta.

💓 *La Bandita informa a partir de fuentes fechadas.* La cerradura cambió de dueño y todavía no llegó a tu puerta: ese es el tiempo exacto para tener las copias guardadas y el cable aprendido.

*Medición del corte:* domingo 1 de noviembre de 2026, 06:55 de Santo Domingo · treinta y tres repositorios medidos uno por uno, sin caché, contra la API pública de GitHub (estrellas, licencia, creación, último empuje, última publicación) · treinta y tres enlaces comprobados uno por uno, todos con respuesta 200 · cuatro de esos repositorios nacieron en las últimas dos semanas y no venían de ninguna lista anterior. Lo que no se pudo medir está escrito arriba como no medido: el interior del verificador, el estado de tu teléfono y el uso real de cada herramienta.

## 🗒️ Notas al pie

**Nota de corrección (1-nov):** cuatro cadenas del acertijo estaban invertidas de forma incorrecta y no descifraban nada; se rehicieron una por una y se comprobaron al revés. También se corrigieron `Pelski/ytzero` (decía «sin licencia declarada» y la API devuelve Unlicense) y `GrapheneOS/Vanadium` (decía «sin declarar» y la API devuelve NOASSERTION).

**Nota de verificación final (1-nov, mañana):** los treinta y tres enlaces se abrieron uno por uno y devolvieron 200 a las 06:55, con `curl -L`. Las estrellas y licencias son de la misma hora; si las lees en otro corte, la hora de la firma te dice cuán viejo es el dato.

**Nota del corte (1-nov):** corte real de la pieza, no heredado de ningún borrador. El sweep del día se hizo completo sobre los treinta y tres repositorios y no quedó ningún dato estimado. Pendiente declarado: la medición del archivo completo de envíos (unos setecientos repositorios) necesita el token de GitHub; sin él la cuota es de sesenta consultas por hora.
