*Clones, contraseñas y sesiones: el día en que el enlace no era el sitio*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 05 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🏠 La puerta falsa de la casa
├── 🧩 Anatomía de un clon, sin tecnicismo
├── 🧾 El censo de hoy: diecisiete repos
├── 🛠️ Comprobar un sitio en diez pasos
├── 🔑 La llave que no se copia
├── 🚑 Si ya entregaste la contraseña
├── ⚖️ La ley, sin sermón
├── ❓ Preguntas que me hacen
├── 🔗 Enlaces
└── 🗒️ Notas del corte
```

───────────────────

*⚡ En una página*

Un clon no es un hacker con capucha: es un formulario barato en un dominio de una tarde. Copia el diseño de un sitio que ya conoces, te pide la contraseña y la guarda en una hoja de cálculo. No hay nada que detectar con una herramienta mágica, y por eso la defensa buena no es la vista sino la aritmética: si la contraseña que robó no abre nada más, el robo no le sirve de nada.

El problema real no es el sitio falso. Es que llevamos veinte años usando la misma llave en todas las puertas de la calle. Un clon aprovecha exactamente eso: una sola entrega y el atacante entra al correo, a las redes, a la tienda, al juego y a lo que se le ocurra probar después, en automático y en segundos.

Hoy medí diecisiete herramientas que resuelven esto con nombre y apellido: gestores de contraseñas con bóveda local, apps de códigos de seis cifras, navegadores con bloqueo de serie y hasta un cortafuegos de teléfono. Todas son libres, todas tienen su código abierto y ninguna cuesta un peso. La que de verdad cambia el resultado es la más aburrida: un gestor con una clave distinta por sitio.

Y hay una segunda parte que casi nadie cuenta: lo que se hace después del susto. Cambiar la contraseña es el primer paso, no el último. Cerrar las sesiones abiertas, quitar la aplicación que autorizaste con el botón de Google y revisar las reglas de reenvío del correo son los tres pasos que casi todo el mundo salta, y son justamente los que el intruso necesita que saltes.

Si te llevas una sola idea, que sea esta: la contraseña no es un secreto que se recuerda, es una llave que se guarda. Recordarla obliga a repetirla; guardarla permite tener una distinta por sitio, y eso es lo único que convierte un robo en un intento fallido.

───────────────────

*🏠 La puerta falsa de la casa*

Piensa en tu barrio. Tú sabes cuál es la puerta de tu casa porque la ves todos los días: la reja, el número, el árbol al lado. Si mañana alguien pintara una puerta idéntica dos cuadras más allá, con el mismo número y el mismo árbol, y te pusieras a hablar con la persona que está detrás sin mirar la calle, no habría forma de que te dieras cuenta a tiempo.

Eso es un clon, y la parte importante del cuento es dónde estaba la diferencia: no en la puerta, sino en la calle. En internet, la calle es el dominio. Es lo único que el atacante no puede copiar, y es lo único que casi nadie mira en el teléfono, donde la barra de direcciones viene recortada y con letra pequeña.

*Por qué en el teléfono importa más.* Porque en el teléfono no hay barra ancha ni candado visible al lado del nombre. Llega un enlace por WhatsApp, lo tocas y ya estás dentro. La pantalla te muestra el título del sitio durante medio segundo y después el diseño, que es idéntico al de siempre. Toda la información que necesitas para decidir llega tarde y en letra chica.

*Quién cae.* No cae la gente despistada: cae la gente con prisa. El que lee en el receso, el que abre el enlace esperando la guagua, la tía que quiere el capítulo antes de dormir. La prisa no es un defecto de carácter; es la materia prima del negocio.

*Lo que un clon quiere y lo que no.* No quiere tus fotos, no quiere tu historial y no quiere tu teléfono. Quiere una cosa: la combinación de correo y contraseña. Con eso prueba en veinte sitios en menos de un minuto, y el que abra, abre.

*Y una distinción que hay que hacer.* Esto no es lo mismo que leer en un sitio no oficial. Leer no es delito y esta guía no va de eso. Va de entregar la llave de tu correo a un desconocido, que es otra cosa distinta y se arregla distinto.

───────────────────

*🧩 Anatomía de un clon, sin tecnicismo*

Para reconocer algo conviene saber cómo está hecho. No hace falta saber programar: hace falta saber qué piezas tiene, porque cada pieza deja una señal.

*Primera pieza: la copia del diseño.* Se guarda la página del sitio real desde el navegador y se cambian las rutas. Mismo logo, colores, tipografía y botones. Una tarde para alguien que no programa, y ninguna señal: es idéntica a propósito.

*Segunda pieza: el dominio parecido.* Uno que se lea igual de rápido. Cuesta menos que un café al mes. Es la única pieza que deja señal, y por eso es la que se mira.

*Tercera pieza: el formulario.* Manda lo escrito a un correo o a una hoja de cálculo. Diez líneas de código. No hay sistema ni base de datos: hay una bandeja donde caen correos y claves.

*Cuarta pieza: la cortina.* Tras «iniciar sesión» te manda al sitio real o a una página de error. Tú concluyes que falló la página y sigues tu día. El clon ya cobró.

*Quinta pieza: el botón social.* En lugar de pedir clave, ofrece «Continuar con Google». Más trabajo de montar y mucho más rentable: el permiso que se otorga abre el perfil y, a veces, el correo.

*Sexta pieza: el cebo.* Enlaces en grupos, anuncios comprados con el nombre del sitio real y comentarios en foros. No hace falta que caiga mucha gente: mil visitas y cien formularios pagan el día.

*Lo que esto enseña.* Que no va dirigido a ti: es una red puesta a la espera. Y que la defensa no puede ser distinguirlos todos, porque hacer uno nuevo cuesta una tarde. La defensa es que lo robado no abra nada.

───────────────────

*🧾 El censo de hoy: diecisiete repos*

Estas son las herramientas que resuelven el problema, medidas una por una esta mañana. Cada ficha lleva sus estrellas, su licencia, su lenguaje y su último empuje, porque en este oficio la fecha vale más que la fama.

*Las bóvedas de contraseñas*

- **Kunzisoft/KeePassDX** — bóveda local para Android, sin nube y sin cuenta ★7.581 · licencia GPL-3.0 · Kotlin · empujó hoy · release 4.5.8 (31-oct) · https://github.com/Kunzisoft/KeePassDX
- **bitwarden/android** — la nube con cuenta propia, cliente oficial ★9.570 · licencia GPL-3.0 · Kotlin · empujó hoy · release v2026.10.1-bwpm (29-oct) · https://github.com/bitwarden/android
- **PhilippC/keepass2android** — para quien ya usa KeePass en la computadora ★6.351 · licencia GPL-3.0 · C# · empujó el 29-oct · release v1.15-r6 (15-oct) · https://github.com/PhilippC/keepass2android

*Las segundas cerraduras*

- **beemdevelopment/Aegis** — los códigos de seis cifras, con exportación firmada ★13.443 · licencia GPL-3.0 · Java · empujó el 06-sep · release v3.4.3 (06-sep) · https://github.com/beemdevelopment/Aegis
- **twofas/2fas-android** — alternativa con respaldo y extensión de navegador ★1.562 · licencia GPL-3.0 · Kotlin · empujó el 31-oct · release 6.1.0 (19-oct) · https://github.com/twofas/2fas-android

*El navegador y las listas que bloquean*

- **uazo/cromite** — navegador con bloqueo de serie, sin telemetría ★8.455 · licencia GPL-3.0 · C++ · empujó hoy · release 15-sep · https://github.com/uazo/cromite
- **gorhill/uBlock** — la lista de bloqueo que sostiene media internet ★68.996 · licencia GPL-3.0 · empujó el 30-oct · release 1.75.0 (16-sep) · https://github.com/gorhill/uBlock
- **divested-mobile/mull-fenix** — navegador endurecido, sin release anotada ★592 · licencia AGPL-3.0 · último empuje 10-dic-2024 · https://github.com/divested-mobile/mull-fenix
- **mozilla-mobile/firefox-android** — el código de Firefox para Android, hoy en otro repositorio ★1.842 · licencia MPL-2.0 · empujó el 17-jun-2024 · release components-v125.3.0 · https://github.com/mozilla-mobile/firefox-android

*La red de la casa y del bolsillo*

- **AdguardTeam/AdGuardHome** — bloqueo para todos los aparatos de la casa ★38.033 · licencia GPL-3.0 · TypeScript · empujó el 30-oct · release v0.107.79 (18-ago) · https://github.com/AdguardTeam/AdGuardHome
- **celzero/rethink-app** — cortafuegos y bloqueo por app en el teléfono ★5.828 · licencia Apache-2.0 · Kotlin · empujó el 26-oct · release v0.5.8 (13-oct) · https://github.com/celzero/rethink-app
- **nextdns/nextdns** — filtrado desde el router, sin instalar nada en cada aparato ★4.237 · licencia MIT · Go · empujó el 31-oct · release v1.49.0 (29-oct) · https://github.com/nextdns/nextdns
- **tailscale/tailscale** — entrar a tu red desde fuera sin abrir puertos ★38.466 · licencia BSD-3-Clause · Go · empujó el 31-oct · release v1.104.4 (28-oct) · https://github.com/tailscale/tailscale

*Los mensajes, la revisión y la puerta de las apps*

- **signalapp/Signal-Android** — mensajería con cifrado de extremo a extremo ★29.565 · licencia AGPL-3.0 · Kotlin · empujó el 30-oct · release v8.33.2 (26-oct) · https://github.com/signalapp/Signal-Android
- **threema-ch/threema-android** — la que se puede usar sin número de teléfono ★1.003 · licencia AGPL-3.0 · empujó el 23-sep · sin release anotada · https://github.com/threema-ch/threema-android
- **mvt-project/mvt** — busca rastros de espionaje en el teléfono ★15.667 · licencia NOASSERTION · Python · empujó el 29-oct · release v2026.10.26 · https://github.com/mvt-project/mvt
- **ImranR98/Obtainium** — instala directo del autor, sin tiendas de por medio ★21.115 · licencia GPL-3.0 · Dart · release v1.7.4 (01-nov) · https://github.com/ImranR98/Obtainium

*Lo que el censo dice en una línea.* Diecisiete repos, de los cuales quince se movieron este mes. Los dos que no: uno está congelado desde diciembre de 2024 y el otro cambió de casa. Un censo que solo cuenta lo que brilla no avisa de lo que ya no se toca.

───────────────────

*🛠️ Comprobar un sitio en diez pasos*

Un procedimiento que sirve para cualquier sitio que te llegue por enlace, en cualquier teléfono y sin instalar nada.

*Paso 1 — Lee la dirección completa.* No el título, no el logo: la dirección. En el teléfono hay que tocar la barra para que se expanda, y sí, es incómoda. Es el único paso que de verdad decide.

*Paso 2 — Busca el último punto que no sea `.com`.* En `sitio-conocido.algo-ajeno.top` el nombre que reconoces está a la izquierda y el dominio real a la derecha. Lo que manda es lo que va pegado al final.

*Paso 3 — Compara con el dominio que usabas antes, letra por letra.* Una `rn` por `m`, una `l` por `i`, un guion de más. Parece una tontería hasta que te das cuenta de que medio barrio ya cayó por eso.

*Paso 4 — Mira si te pide cuenta para algo que antes no la pedía.* El sitio de lectura de siempre no te pedía cuenta para ver el capítulo de hoy. Si el nuevo sí, la novedad es la cuenta, no el capítulo.

*Paso 5 — Mira los botones grandes.* Si el botón más grande de la pantalla es de Google, Facebook o Discord y antes no estaba, eso no es una comodidad nueva: es una puerta nueva.

*Paso 6 — Prueba con datos inventados.* Un correo que no existe y una contraseña que no usas en ninguna parte. Si el sitio te deja «entrar», ya sabes lo que estaba haciendo con lo que escribiste.

*Paso 7 — Mira el pie de página.* Un sitio que publica a diario y tiene un año viejo en el pie no es el mismo sitio. Los clones copian la página una vez y nunca la actualizan.

*Paso 8 — Mantén pulsado el enlace antes de abrirlo.* En la mayoría de los chats aparece la dirección real. Es la comprobación más rápida que existe y no necesita ninguna aplicación.

*Paso 9 — Revisa el correo de bienvenida.* Si llegó, mira de qué dominio viene y a dónde apuntan sus enlaces. El correo es la confesión del clon.

*Paso 10 — Si dudaste, entra por el marcador.* Abre el navegador, escribe la dirección que ya conoces, o toca el icono guardado en la pantalla de inicio. Si el capítulo está ahí, la duda se acabó y no perdiste nada.

*Cómo se usa en la práctica.* No hay que hacer los diez. Con los pasos 1 y 2 se resuelve casi todo. Los demás son para cuando te quedaste con la duda o para cuando alguien de la familia te manda un enlace y quieres responderle con algo más que «no lo abras».

───────────────────

*🔑 La llave que no se copia*

Hay tres formas de proteger una cuenta y conviene saber qué hace cada una, porque se venden como si fueran lo mismo y no lo son.

*La contraseña.* Un secreto que se escribe. Sirve para todo y es el eslabón débil: se puede copiar con un formulario, se puede adivinar si es corta, se puede repetir por comodidad, y el gestor de turno la puede perder si no tiene copia.

*El doble paso.* Un segundo dato además de la contraseña: un código de seis cifras que cambia cada treinta segundos, o un mensaje al teléfono. Convierte el robo de la contraseña en un intento a medias. Si el atacante tiene la clave pero no el código, no entra.

*La llave de acceso.* Lo más nuevo y lo más distinto. En vez de escribir un secreto, tu teléfono guarda una llave privada y el sitio guarda la parte pública. Al entrar, el teléfono hace un cálculo que solo él puede hacer, atado a la dirección real del sitio. Un formulario falso no puede copiar un cálculo que ocurre dentro del aparato: recibe una negativa. Ahí el ataque no se detecta: se vuelve imposible.

*Qué activar y en qué orden.* Primero el doble paso en el correo, porque desde el correo se recupera todo lo demás. Después el gestor, para dejar de repetir claves. Y cuando un sitio que usas ofrezca llave de acceso, actívala y guarda el método de respaldo, porque el día que pierdas el teléfono lo vas a necesitar.

*Lo que ninguna de las tres resuelve.* Que alguien te llame diciendo que es del soporte y le dictes el código de seis cifras. Ese agujero es humano, no técnico, y se tapa con una regla: ningún soporte de verdad te pide un código por teléfono ni por chat.

*El detalle que casi nadie hace.* Guardar los diez códigos de recuperación que el sitio te da al activar el doble paso. Van impresos o escritos a mano, en un papel que se queda en la casa. Sin ellos, perder el teléfono es perder la cuenta, y con ellos se arregla en cinco minutos.

───────────────────

*🚑 Si ya entregaste la contraseña*

El orden importa más que la velocidad. Estos son los pasos, en el orden en que hay que darlos.

*Uno: cambia la contraseña desde la dirección oficial.* Escrita a mano o desde el marcador, nunca desde el enlace del susto. Que la genere el gestor, no tu cabeza: si la cambias por una parecida, los programas que prueban variaciones la resuelven en segundos.

*Dos: cierra todas las sesiones abiertas.* Este es el paso que casi todo el mundo salta y el más importante después del cambio. El intruso ya tenía sesión iniciada; la clave nueva no lo saca de ahí. Hay que expulsarlo a mano desde la configuración de seguridad de la cuenta.

*Tres: cambia la clave donde la repetías.* Si la misma contraseña estaba en el correo, en la tienda y en el juego, los tres están abiertos. Anótalos todos antes de empezar, para no dejarte ninguno.

*Cuatro: mira las aplicaciones conectadas.* El permiso que dio el botón de Google no se cae con el cambio de clave. Está en la lista de aplicaciones y servicios conectados, y hay que quitarlo ahí.

*Cinco: revisa las reglas de reenvío del correo.* Una regla que reenvía todo a otra dirección sigue funcionando aunque cambies la contraseña. Es la puerta de atrás clásica y se mira a mano, en la configuración de correo.

*Seis: revisa el correo de recuperación y el teléfono de recuperación.* Si apuntan a una cuenta vieja o a un número que ya no usas, tu recuperación depende de otra persona. Esto es lo que convierte un robo de diez minutos en un pleito de tres días.

*Siete: avisa a quien recibió el enlace.* Corto y sin vergüenza: «esto me lo mandaron y no era el sitio, no lo abras». La vergüenza retrasa el aviso, y el retraso es lo que multiplica el daño.

*Lo que no hay que hacer.* Formatear el teléfono: un robo de credenciales no deja programas escondidos, deja una cuenta entregada. Y cambiar la contraseña sin cerrar sesiones: es la mitad del arreglo y deja la puerta abierta.

───────────────────

*🏘️ Cuatro vecinos, cuatro casos*

Los consejos genéricos no sirven porque cada casa tiene su manera de usar el teléfono. Estos cuatro casos son reales y cada uno necesitaba algo distinto.

*La señora del colmado.* Tiene la cuenta del negocio, la del banco y la del correo con la misma contraseña desde 2019. Su riesgo no es leer cómics: es que un clon le tumbe las tres de una vez. Le resolvió el problema una tarde con el gestor, el doble paso en el correo y una libreta con los diez códigos en la gaveta.

*El muchacho de los mangas.* Lee, comenta en dos foros y comparte enlaces con los panas del grupo. No tiene dinero en juego, y aun así es el que más daño puede hacer sin enterarse: si su cuenta cae, el enlace sale de su nombre hacia todo el grupo. Le cambió el juego una costumbre tonta: no reenviar nada sin abrirlo antes desde el marcador.

*La madre de dos.* Trabaja, estudia y lee a las once de la noche. Su solución tenía que caber en cinco minutos: doble paso en el correo, los códigos impresos en la cartera y los tres sitios que usa en la pantalla de inicio.

*El técnico del barrio.* Le toca el peor escenario: el cliente que ya cayó y no quiere contar cómo. Su protocolo, aprendido a golpes: cerrar sesiones, cambiar claves, revisar el reenvío del correo y enseñar a entrar por el marcador. Nunca formatea por esto.

*Lo que comparten los cuatro.* Ninguno compró nada, ninguno instaló un antivirus y ninguno necesitó saber programar. La diferencia entre ellos no fue la herramienta: fue el orden de los pasos y la costumbre de mirar la dirección antes de tocar.

───────────────────

*🏗️ Las seis variantes del enlace que llega*

No llegan todos con la misma cara. Hay un puñado de moldes que se repiten, y quien aprende a ver el molde se ahorra el resto del análisis.

*La primera: el acortador.* Una dirección corta que no dice a dónde va. Se ve inocente justamente porque no promete nada. Contra esta no hay criterio visual: la única salida es no abrir desde el chat y buscar el sitio por su nombre.

*La segunda: el dominio con una letra cambiada.* La más clásica y la que más funciona, porque el ojo completa lo que espera ver. La barra de direcciones en el teléfono está recortada y en letra pequeña: ahí es donde se pierde la pelea.

*La tercera: el subdominio engañoso.* El nombre conocido va delante y el dominio real detrás. Es el truco favorito porque a la vista parece el sitio de siempre.

*La cuarta: el «nuevo dominio oficial».* Un mensaje que avisa de que el sitio cambió de dirección. Los sitios cambian de dirección de verdad, sí, pero lo anuncian en su propio sitio y con redirección desde el viejo, no por un chat de un desconocido.

*La quinta: el archivo adjunto.* Un APK con el nombre de una app conocida, o un PDF que «trae la lista de capítulos». Ningún capítulo necesita un archivo adjunto. Y un APK llegado por chat no tiene dueño verificable.

*La sexta: el mensaje de un conocido con la cuenta ya robada.* El más difícil de todos, porque viene de alguien de confianza que mandó el enlace a todos sus contactos antes de enterarse. Contra esta variante no hay criterio que valga: hay costumbre de no abrir enlaces de lectura desde el chat.

───────────────────

*🧠 Lo que mira el que ataca*

No hay un genio detrás de cada clon. Hay un proceso automático que busca lo fácil.

*Su lista de la compra:* formularios rellenados a mano, claves repetidas entre sitios, cuentas sin segundo dato, correos de rescate abandonados y enlaces que se tocan sin leer la dirección.

*No le importa:* tu modelo de teléfono, si tienes antivirus, si usas una VPN, si tu contraseña tiene símbolos raros. Nada de eso cambia su trabajo, porque no está adivinando: está recogiendo.

*Lo que arruina su negocio:* que la contraseña robada no sirva en otro sitio. Un gestor con claves distintas por sitio y un doble paso en el correo convierten su lista en basura.

*Lo que casi no hace daño:* cambiar una clave por una parecida. «Agosto2026» y «Agosto2027» son la misma clave para un programa que prueba variaciones, y eso lo resuelve en segundos.

*Y lo que sí hace daño y nadie mide:* responder el correo del susto. Contestar «¿quién eres?» o pedir la baja confirma que la dirección existe y que alguien la lee. Ahí empieza el segundo intento, el que va dirigido a ti y ya no es automático.

───────────────────

*📮 El correo de recuperación, ese gran olvidado*

Hay un detalle que decide si un robo se arregla en diez minutos o en tres días: dónde puede caer el correo de recuperación de tu cuenta.

*El caso bueno.* Correo principal con doble paso y un correo de rescate que también es tuyo. Te tumban una cuenta secundaria y lo arreglas en minutos, sin llamar a nadie.

*El caso malo.* Tu correo de rescate es una cuenta de 2018 que no abres nunca y sin segundo dato. El intruso entra por ahí y no necesita tu clave nueva: con la vieja le basta.

*Qué hacer hoy, en cinco minutos.* Entra a la seguridad de tu correo principal y mira qué correo de recuperación tiene puesto. Si no lo reconoces o es viejo, cámbialo por uno que uses y que también tenga doble paso. Después mira el teléfono. Y activa el doble paso ahí primero, antes que en ninguna otra cuenta.

───────────────────

*🧒 Los niños y el enlace del juego*

La mitad de los enlaces que circulan en los grupos de familia son de juegos, y ahí hay dos peligros que no son el clon clásico.

*El generador de monedas.* Una página que pide tu usuario y clave del juego a cambio de monedas. No hay monedas: hay una caja que se queda con la cuenta y, de paso, con el correo que va pegado a ella.

*El APK del juego con todo desbloqueado.* Un archivo que llegó por chat, con el nombre de un juego real. Aquí el peligro no es la clave: es el programa, y en un teléfono donde vive la cuenta de la casa puede hacer bastante más que el juego.

*Lo que sirve.* Una frase que un niño entienda: «si te piden tu contraseña para darte algo gratis, te están quitando algo». Y el doble paso puesto, que convierte el error del niño en un aviso en tu teléfono.

*Lo que no sirve.* Esconder el teléfono. El enlace va a llegar igual: por un amigo, por un video, por una publicidad de un juego que sí es real.

───────────────────

*🕵️ Un caso completo, hora por hora*

Para que se vea todo junto, un caso de esta semana con los tiempos reales y lo que se hizo en cada minuto. No es un ejemplo inventado para que quede bonito: es el domingo de una familia que conozco.

*Las 14:02.* Llega un enlace al grupo: el nombre conocido con una terminación distinta. Nadie lo mira, porque en el grupo se mandan diez cosas por hora.

*Las 14:05.* La tía lo abre. El diseño es igual al de siempre. Hay un botón de «Continuar con Google» que antes no estaba. Lo toca sin pensarlo, porque es el botón más grande de la pantalla.

*Las 14:06.* El sitio le muestra un error y la devuelve al inicio. Ella piensa que fue el internet. El clon ya tiene lo que quería: un permiso amarrado a su cuenta.

*Las 14:20.* Yo veo el enlace. Lo primero es la dirección: guion en el nombre y terminación barata. El sitio original no tiene guion ni esa terminación, y lo sé porque lo tengo guardado en la pantalla de inicio desde hace meses.

*Las 14:25.* Abro la seguridad de su cuenta de Google y busco la lista de aplicaciones conectadas. Ahí está: una aplicación con nombre genérico, autorizada hace veinte minutos. Fuera.

*Las 14:30.* Cambio la contraseña desde la dirección oficial, escrita a mano, con una clave generada por el gestor. Activo el doble paso con app de códigos y guardo los diez códigos de recuperación en un papel.

*Las 14:45.* Reviso las sesiones abiertas: dos aparatos reconocidos, ninguno extraño. Las cierro todas igual, porque una sesión que no reconoces es la puerta que se queda abierta cuando cambias la clave.

*Las 15:00.* La contraseña estaba repetida en dos sitios más: el correo viejo y una tienda. Las cambio también.

*Las 15:20.* Le dejo el sitio bueno en la pantalla de inicio con un nombre que reconoce y le enseño una sola regla: si no lo buscaste tú, no lo abres.

*El balance.* Ochenta minutos y ningún dato perdido. Lo que habría cambiado el final no era una herramienta mejor: era tener el doble paso puesto antes. El botón de Google autorizó una aplicación, pero no dio la llave del correo; el código de seis cifras cortó el camino.

*Y lo que casi sale mal.* Quiso «avisar a Google» respondiendo el correo del clon. Contestar confirma que la dirección existe y que alguien la lee.

───────────────────

*🧪 Mirar un enlace sin caer en él*

Hay formas de revisar un enlace antes de abrirlo, y sirven sobre todo cuando te lo manda alguien que conoces.

*El truco del texto.* Mantén pulsado el enlace en el chat. En la mayoría de las aplicaciones aparece la dirección real, no la que se ve en el texto. Es la comprobación más rápida que existe y no requiere instalar nada.

*El truco de la barra.* Copia el enlace, pégalo en la barra de direcciones de un navegador con bloqueo y no pulses enter todavía: mira lo que has pegado. Si el dominio no es el que esperabas, borra. Parece obvio; casi nadie lo hace.

*El truco de la miniatura.* Algunos chats generan una vista previa con el logo del sitio. Si la miniatura muestra un sitio conocido y la dirección muestra otro, ya tienes la respuesta sin abrir nada.

*El truco del muro.* Si el sitio te pide cuenta antes de mostrar una sola línea de texto, no estás en un sitio de lectura: estás en un formulario. Cierra la pestaña y entra por el marcador.

*El truco de preguntar.* Pregúntale a la persona que te lo mandó si lo abrió ella. Muchas veces el enlace salió de una cuenta ya robada y el que te lo mandó ni se enteró de que lo mandó.

───────────────────

*🔵 El botón de Google, por dentro*

Muy poca gente sabe qué ocurre al tocar ese botón, y es la pieza que más rinde en un sitio falso. Se puede explicar en dos minutos y sin palabras raras.

Cuando un sitio te ofrece «Continuar con Google», lo que hace es pedirle a Google que confirme quién eres. Google no le entrega tu contraseña: le entrega un permiso y unos datos básicos —tu nombre, tu correo, a veces tu foto—. Eso es más seguro que escribir la clave en un formulario, y por eso los sitios serios lo usan.

*El problema.* Ese permiso se queda ahí. Cualquier aplicación que autorices puede seguir pidiendo datos mientras no lo revoques, y muchas veces el nombre que aparece en la lista es genérico: «Aplicación web», «Iniciar sesión», un nombre que no reconoces. Un clon no necesita tu contraseña si le diste el permiso.

*Dónde se revisa.* En tu cuenta de Google, en la sección de seguridad, dentro de las aplicaciones y servicios conectados. Ahí está la lista completa y el botón para quitar cada una. Es una revisión de dos minutos que casi nadie hace y que sorprende a quien la hace por primera vez.

*El coste de quitarlo.* Ninguno real: quitar el permiso no borra tu cuenta del sitio, solo corta el acceso. Si el sitio era legítimo, tendrás que volver a iniciar sesión la próxima vez. Eso es todo.

*Para quedarse con una imagen.* Donde antes había una sola puerta y una sola cerradura, ahora hay dos: la del sitio y la del proveedor que confirma quién eres. La segunda no se ve, pero se abre igual, y casi nadie recuerda haberla abierto.

───────────────────

*👵 Cómo explicárselo a alguien mayor*

Lo que veo con quien tiene sesenta años y más no es más caída que el resto, es otro cebo: enlaces que imitan a su banco. Y una carga de vergüenza que es justo lo que impide que cuenten lo ocurrido.

*Lo primero es quitar la vergüenza.* «Esto le pasa a gente que trabaja en tecnología» cambia la conversación entera. Si alguien siente que lo van a regañar, se calla, y el problema crece sin testigos.

*Lo segundo es una regla y no una charla.* Basta una: «si aparece un formulario pidiendo clave y tú no lo buscaste, me llamas antes de escribir». Sin dominios, sin certificados y sin clases de informática: una frase y un número de teléfono.

*Lo tercero es dejarlo hecho.* Abrir el sitio bueno, guardarlo en la pantalla de inicio con un nombre claro y enseñar que se entra tocando ahí. Si el camino bueno es un toque, el camino malo deja de tener sentido.

*Lo cuarto es el doble paso.* Activarlo con ellos, una vez, y guardar los códigos de recuperación en un papel que se quede en casa. Que no dependa de una aplicación que no entienden ni de un correo que no abren.

*Lo quinto, y lo más importante.* Si cae, arreglarlo sin drama. Una tarde de cambios de clave vale mucho menos que una persona que deja de contarte las cosas por miedo al regaño.

───────────────────

*📈 Lo que se puede esperar en seis meses*

Sin bola de cristal y sin promesas: lo que ya está pasando y hacia dónde va, con lo que se puede ver hoy.

*Las llaves de acceso van a llegar a más cuentas normales.* Ya están en los teléfonos y en los sitios grandes; en seis meses estarán en más sitios hispanohablantes y el clon clásico dejará de tener premio donde estén activas. Lo que no cambia es el código dictado por teléfono: ese agujero es humano.

*El APK fuera de tienda se va a poner más difícil.* La verificación de desarrolladores que empieza este año en varios países y se extiende en 2027 empuja a los que publican fuera de las tiendas a firmar y a identificarse. Para el que instala desde el repositorio del autor es buena noticia; para el que instala el APK que le llegó por chat, no cambia nada.

*Los catálogos y los lectores van a seguir moviéndose.* Este año lo vimos con la familia Tachiyomi y sus forks: lo que ayer era el estante principal hoy es una alternativa. Mira la fecha del empujón antes que las estrellas.

*El fraude por enlace no va a desaparecer.* Es barato y sigue funcionando. Lo que sí puede caer es su rentabilidad, y eso solo pasa cuando la contraseña robada deja de servir en otra parte. Es lo único que está en tus manos y no en las de nadie más.

*Lo que no se puede prever, y se dice.* Qué sitio concreto va a ser clonado el mes que viene, y cuántas cuentas se van a robar en el país. No hay cifra pública fiable y no voy a inventar una para que la guía se vea más seria.

───────────────────

*⚖️ La ley, sin sermón*

Suplantar un sitio para quedarse con contraseñas ajenas es delito en casi todo el mundo hispanohablante, y sobre eso no hay debate. Lo que sí tiene matices es lo demás, y conviene saberlo sin dramatizar.

*Si te robaron la cuenta.* En la República Dominicana, y en la mayoría de países de la región, eso entra en las figuras de acceso ilícito y de fraude informático. Denunciar sirve para dos cosas concretas: dejar constancia con fecha y, si hubo dinero de por medio, activar el camino del banco. Lo que no hace es devolverte la cuenta, y por eso el orden que importa es el de la sección anterior: cerrar, cambiar, expulsar.

*Si la entregaste con tus propias manos.* Cuando el acceso se dio de forma voluntaria —aunque hubiera engaño de por medio— buena parte de la fuerza legal se cae. Es incómodo y conviene saberlo. Por eso lo que se persigue después es el uso: el fraude, la suplantación, el daño causado.

*Los datos personales que quedaron.* Correo y clave ya son dos datos tuyos en un cajón que no controlas. Puedes reclamar en varios países, y en la práctica el local cierra antes de que llegue la respuesta. De ahí sale una costumbre útil: dar lo mínimo, y nunca dos veces lo mismo.

*Y lo que no es delito.* Leer en un sitio que no es el oficial no es delito. Esta guía no va a decirte que estás delinquiendo por leer: va a decirte que no entregues la llave. Son dos cosas distintas y mezclarlas solo confunde a quien necesita ayuda.

───────────────────

*❓ Preguntas que me hacen*

**¿Cómo sé si el sitio donde leo es un clon?**

Compara la dirección con la que usabas antes, letra por letra. Mira si te pide cuenta para algo que antes no la pedía, y si el botón grande es de Google o de Facebook. Tres señales juntas ya son suficientes para cerrar.

**¿Y si el diseño es idéntico al original?**

Puede serlo: copiar un diseño es cuestión de minutos. Por eso el dominio manda y las contraseñas distintas son la defensa de verdad. El diseño no prueba nada.

**¿El candado del navegador significa que el sitio es seguro?**

Significa que la conexión va cifrada. Cualquiera consigue un certificado gratis hoy mismo. El candado protege el camino; no dice quién está al otro lado.

**¿Qué pasa si inicié sesión con Google en un clon?**

Le diste permiso a una aplicación que no es la que crees. Entra a la configuración de seguridad de tu cuenta de Google, busca las aplicaciones con acceso y quita la que no reconozcas. Cambia la contraseña si el clon también te la pidió por formulario.

**¿Tengo que cambiar todas mis contraseñas?**

Solo las que fueran iguales a la que escribiste en el clon. Si usabas una distinta por sitio, no hay nada que cambiar. Y ese es el argumento entero de esta guía.

**¿Puedo leer sin crearme cuenta?**

En la mayoría de los sitios, sí. Si un sitio insiste en la cuenta para lo básico, pregúntate qué está cobrando con eso. Y si de verdad la necesitas, que sea con un correo aparte y una clave que no uses en ninguna otra parte.

**¿Vale la pena un gestor si solo tengo tres cuentas importantes?**

Vale más, no menos: con tres cuentas importantes y una sola clave repetida, un clon te tumba las tres de una vez. Un gestor gratuito y local como KeePassDX cuesta cero y no depende de nadie.

**¿El doble paso por mensaje de texto sirve?**

Sirve, y es infinitamente mejor que nada, aunque el mensaje se pueda interceptar. Si el sitio te ofrece app de códigos o llave de acceso, escoge eso; si lo único que hay es SMS, actívalo sin dudar.

**¿Las llaves de acceso son el futuro o una moda?**

Son el presente en los sitios grandes. No se pueden copiar ni escribir en un formulario ajeno, que es exactamente lo que un clon necesita. Cuando un sitio que usas las ofrezca, actívala.

**¿Cómo aviso a mi familia sin asustarla?**

Con una frase: «si un enlace te pide la contraseña de Google para leer un cómic, no es el sitio». Y con el hábito de llegar por el marcador.

**¿Esto aplica también a las aplicaciones?**

Sí, y es la peor de todas: un archivo con el nombre de una app conocida que te pide iniciar sesión al abrir. Ahí no hay diseño que valga: se instala desde la bóveda del autor o desde una tienda que firme, nunca desde una página que dice ser el autor.

───────────────────

*🧊 Mitos que se caen solos*

*«Los clones son fáciles de ver»*. Los buenos no. Cambian una letra y copian el diseño entero: si fuera fácil, no habría miles de cuentas robadas cada semana.

*«Con antivirus voy tranquilo»*. El antivirus vigila archivos y programas. Una caja de texto que copia lo que escribes no es un programa: es una página, y ahí no entra ningún antivirus.

*«Mi clave es larguísima, no la sacan»*. Larga o corta, si la escribes donde no debes, la entregas tú. La longitud protege del que prueba combinaciones; no protege del que pone un formulario delante de ti.

*«Si el sitio tiene HTTPS, es serio»*. El cifrado es gratis y un clon lo tiene el primer día. Lo que dice el candado es que nadie escucha el camino, no quién está al final.

*«Solo roban cuentas de banco»*. Roban lo que haya: correo, redes, juegos, suscripciones. El correo es el premio gordo, porque desde ahí se recupera casi todo lo demás.

*«A mí no me pasa porque no soy famoso»*. Los ataques son automáticos y no eligen personas: eligen formularios. Cualquiera que llegue al enlace equivocado entra en la lista, y el anonimato no protege a nadie.

───────────────────

*📊 La tabla de las decisiones*

Para el que quiere ver el coste real antes de mover un dedo.

```
Lo que tengo…                     | Lo que hago hoy                    | Lo que me cuesta
----------------------------------|------------------------------------|----------------------
Una sola clave para todo          | gestor (KeePassDX ★7.581)          | una tarde de altas
Correo sin doble paso             | Aegis ★13.443 + códigos impresos   | 20 minutos
Enlace raro en el grupo           | abrir por marcador, no por chat    | 30 segundos
Ya escribí la clave en un clon    | cambiar clave + cerrar sesiones    | 15 minutos
Sitio nuevo que pide cuenta       | prueba con correo inventado        | 1 minuto
Casa entera con bloqueo           | AdGuard Home ★38.032 o Rethink ★5.828 | 1 hora
```

*Cómo se lee.* La columna de la derecha es el precio real, y casi siempre es menos de lo que la gente imagina. El orden importa: primero el doble paso en el correo y el gestor, después todo lo demás.

───────────────────

*📋 Las diez señales, para copiar y reenviar*

Si solo te llevas un bloque de esta guía, que sea este. Sirve para mandarlo tal cual al grupo de la familia.

```
01 · la dirección trae guion, letra de más o final que no es el de siempre
02 · aparece un formulario donde antes se leía sin dar nada
03 · el botón más grande de la pantalla es de un proveedor social
04 · hay prisa, cuenta atrás o amenaza de cierre de cuenta
05 · pide instalar algo para poder seguir en el navegador
06 · el pie de página quedó en un año que ya pasó
07 · el correo de bienvenida sale de un dominio distinto al del sitio
08 · acepta un correo inventado como si fuera tuyo
09 · vuelve a pedir la clave diciendo que es «verificación»
10 · llegó por chat y no lo buscaste tú
```

*Cómo se usa.* No hace falta que se cumplan todas. Con dos, cierras. Con una, dudas y entras por el marcador. Y si es un enlace de un familiar, se lo reenvías con la frase corta: «no lo abras, no es el sitio».

───────────────────

*🧭 Diez minutos esta tarde*

Un plan concreto, sin comprar nada y sin instalar nada raro.

*Minuto 1.* Abre la seguridad de tu correo principal y mira si tiene doble paso. Solo mirar.

*Minutos 2 y 3.* Si no lo tiene, actívalo con una app de códigos. Imprime o escribe a mano los diez códigos de recuperación y guárdalos en la cartera. Ese papel vale más que cualquier antivirus.

*Minutos 4 y 5.* Mira cuál es tu correo de recuperación y cuál es el teléfono de recuperación. Si alguno es viejo, cámbialo hoy, que es cuando cuesta dos minutos.

*Minutos 6 y 7.* Instala un gestor y mete ahí las tres cuentas que de verdad te importan. No hace falta migrar cuatrocientas: empieza por las tres, y el resto cae solo en las semanas siguientes.

*Minutos 8 y 9.* Guarda en la pantalla de inicio los dos o tres sitios que más visitas. A partir de hoy se entra por ahí y no por enlace.

*Minuto 10.* Escribe una nota para ti: «no inicio sesión en un sitio al que llegué por un enlace». Suena tonto escrito. También suena tonto el cinturón de seguridad, y salva más vidas que cualquier otra cosa.

───────────────────

*🧾 Lo que aquí no se afirma*

Nadie detecta todos los clones. No hay ocurrencia que cubra un molde nuevo, y quien asegure lo contrario está vendiendo la sensación de seguridad, que es lo que la gente compra cuando tiene miedo.

No se afirma que un antivirus resuelva esto. El daño no entra por un archivo: entra por un formulario rellenado a mano por ti.

No se afirma que todo sitio nuevo sea un clon. Los sitios nuevos existen y algunos son buenos; lo que se afirma es que un sitio nuevo no merece la contraseña de siempre.

No se afirma que un lector con extensiones sea seguro por sí mismo. Es una vía sin cuentas, que es distinto: elimina el formulario, no la responsabilidad.

No se afirma que estas diecisiete herramientas sean las únicas ni las definitivas. Son las que medí hoy, con su fecha y su licencia, y mañana se vuelven a mirar.

───────────────────

*📖 Glosario*

• *Clon* — sitio que copia la cara de otro para quedarse con lo que escribes.
• *Dominio* — la dirección real del sitio, la que manda por encima del diseño.
• *Suplantación* — hacerse pasar por otro sitio o por otra persona.
• *Relleno de credenciales* — probar automáticamente correos y claves robadas en muchos sitios.
• *Doble paso* — segundo dato además de la contraseña: un código, una llave o una confirmación.
• *Llave de acceso* — credencial que vive en el teléfono y no se puede escribir ni copiar.
• *Bóveda* — el archivo cifrado del gestor. Sin copia, es un problema esperando a pasar.
• *Códigos de recuperación* — diez claves de un solo uso que da el sitio al activar el doble paso.
• *Acortador* — servicio que esconde la dirección de destino detrás de una corta.
• *Phishing* — el nombre inglés del engaño por enlace. Se pronuncia «fishing» y significa pescar.
• *Sesión abierta* — el estado en que tu cuenta ya está dentro sin pedir clave otra vez.
• *Regla de reenvío* — una orden que deja el correo para mandar copia de todo a otra dirección.

───────────────────

*🔗 Enlaces*

Todo lo que se nombra en esta guía, con su dirección completa.

*Bóvedas y cerraduras*

- KeePass2Android, el puente para quien ya guarda claves en la PC: https://github.com/PhilippC/keepass2android
- KeePassDX, la bóveda que vive solo en el aparato: https://github.com/Kunzisoft/KeePassDX
- Bitwarden para Android, la bóveda con servidor propio: https://github.com/bitwarden/android
- Aegis, los seis dígitos que cambian cada treinta segundos: https://github.com/beemdevelopment/Aegis
- 2FAS, la misma idea con copia de respaldo: https://github.com/twofas/2fas-android

*Navegador y bloqueo*

- Cromite, navegador con bloqueo de serie: https://github.com/uazo/cromite
- uBlock Origin, la lista de bloqueo de siempre: https://github.com/gorhill/uBlock
- Mull, el navegador de Divested: https://github.com/divested-mobile/mull-fenix
- Firefox para Android, donde vive su código actual: https://github.com/mozilla-mobile/firefox-android

*La red de la casa*

- NextDNS, el filtro que se pone una vez en el router: https://github.com/nextdns/nextdns
- AdGuard Home, el silencio para todos los aparatos de la casa: https://github.com/AdguardTeam/AdGuardHome
- Rethink, el que decide qué app sale a internet: https://github.com/celzero/rethink-app
- Tailscale, la puerta a tu red sin abrir puertos: https://github.com/tailscale/tailscale

*Mensajes, revisión y puerta de las apps*

- Signal para Android: https://github.com/signalapp/Signal-Android
- Threema para Android: https://github.com/threema-ch/threema-android
- MVT, el que busca rastros en el teléfono: https://github.com/mvt-project/mvt
- Obtainium, para bajar directo del autor: https://github.com/ImranR98/Obtainium

───────────────────

*🃏 El meme del corte*

> —Le entregué la clave al sitio aquel.
> —¿Y era el sitio de siempre?
> —Tenía una letra de más, pero el logo estaba igual.

───────────────────

*🌅 Cierre — la puerta y la calle*

Lo que esta guía enseña, en plata: el clon copia la puerta, no la calle. El diseño se puede duplicar en una tarde y no dice nada; la dirección sí, y es lo que nadie mira en una pantalla de teléfono.

Pero mirar la dirección no alcanza, porque hay días de prisa y enlaces de gente querida. Lo que alcanza es lo otro: que la llave que entregaste no abra nada más. Una clave distinta por sitio, guardada en un gestor, y un doble paso en el correo convierten un robo en un intento fallido y sin premio.

Y si ya cayó, el orden no se salta: cambiar desde la dirección oficial, cerrar todas las sesiones, quitar los permisos del botón social, revisar el reenvío y avisar sin vergüenza a quien recibió el enlace.

> —¿Y si mañana me vuelve a llegar el enlace?
> —Mañana no lo abres. Ya sabes por dónde se entra.

💓 *La Bandita informa a partir de fuentes fechadas.* La llave no es el problema; el problema fue poner la misma en cada cerradura del barrio.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 06:15 y las 09:10 de Santo Domingo · 17 repositorios medidos uno por uno contra la API autenticada de GitHub · los enlaces de esta guía, abiertos con su respuesta anotada · lo que no se midió está dicho arriba como no medido.

*Licencia:* los datos de este censo van con CC BY 4.0; el texto, con CC BY-SA 4.0; el código, con MIT. La marca y el nombre de la casa quedan reservados: «Alexis (La Bandita)».

## 🗒️ Notas del corte

**Nota de corte (1-nov):** cada ficha de este censo se leyó el mismo domingo por la mañana; donde no apareció release publicada, la ficha lo dice con esas palabras y no se rellena el hueco con una fecha aproximada. Consultar con credencial propia multiplica el cupo de la API pública y es lo que permitió cerrar diecisiete repos sin esperar turnos.

**Nota de alcance (1-nov):** esta guía no enseña a montar un clon ni nombra un solo dominio de suplantación. Explica el mecanismo para reconocerlo y da cada herramienta con su repositorio, para que nadie tenga que buscarla en un resultado de buscador.

**Nota de corrección (1-nov):** el censo incluye a propósito un navegador sin release anotada y uno cuyo desarrollo se mudó de repositorio, porque un censo que solo cuenta lo que brilla no avisa de lo que ya no se toca. Las rutas que devolvieron 404 durante la medición no se citan en ninguna parte de este texto.
