*43 — EL TÚNEL*
*WireGuard ★1.640 (pulso 16-oct-2026) mete el viaje entero del barrio en un candado de cuatro
mil líneas: el caserón cifrado, del café ajeno a tu casa (WhatsApp · La Bandita ·
dominicano-ES)*

───────────────────

*⚡ EN UN RESPIRO*

La noche pasada el faro cifró la PREGUNTA de tu teléfono — esta noche muda el VIAJE completo:
WireGuard es el candado que mete todo tu caserón en un sobre blindado mientras usas el wifi del
café, y su placa firme es una app libre de Apache-2.0 con el motor que el kernel de Linux
adoptó.

*🗺 MAPA DE ESTA GUÍA*

La fila de REDES sigue su camino: la 41 mudó la ventana, la 42 mudó el índice — esta pieza
veintitrés muda el CASERÓN entero. El recorrido de la noche: primero el viaje del café (la
escena que todos conocemos).

Después el censo de la familia WireGuard con sus cinco placas del pulso de hoy, las tres capas
del túnel y la vara de las licencias.

Luego la doctrina del punto de salida (la regla que separa la mudanza honesta del traspaso de confianza), la receta por pisos y los mitos desmontados. Y al cierre: las preguntas de la fila, los casos del barrio, las despensas, los riesgos con fecha, el ritual de siete días y las cartas de la mesa.

*🌱 LA SEMILLA*

La escena no tiene pérdida: el wifi gratuito del café, la contraseña en la pizarra, el teléfono conectando solo — y todo lo que viaja (el banco, el correo, las conversaciones, el índice entero) pasando por el router de un extraño. La 42 resolvió la pregunta (el índice cifrado); pero el resto del viaje — las páginas, las apps, el correo — seguía saliendo en la red del café.

El ecosistema libre lleva una década respondiendo con UNA pieza: WireGuard, el candado de viaje que Jason Donenfeld diseñó con una vara imposible de sencilla — que cupo en cuatro mil líneas y lo firmó el kernel de Linux completo. Esta es la historia del sobre blindado del barrio: quién lo forja, cómo se enciende, y la frontera honesta que ningún anuncio de VPN te va a contar.

*🗼 EL CENSO DEL TÚNEL (censo 16-oct-2026)*

La familia del túnel, medida con el pulso del mismo día en que nace esta pieza — cinco placas,
cuatro leyes, un solo oficio.

*La app del teléfono — WireGuard Android.* La placa del espejo: `WireGuard/wireguard-android`
★1.640 (pulso 16-oct-2026), nacida el 27-abr-2018, con aire hasta el 29-jun-2026, bajo
Apache-2.0. La placa lleva su letra chica honesta: es ESPEJO — el hogar oficial vive en
git.zx2c4.com, la casa de Donenfeld.

La app que enciende el túnel en el teléfono: un interruptor, un QR, y el viaje entero en el sobre.

*El motor en Go — wireguard-go.* ★4.453 (pulso 16-oct-2026), nacida el 16-may-2018, con aire
hasta el 6-oct-2026, bajo MIT. El motor que corre FUERA del kernel — el que la app del Android
usa por dentro para mover el sobre.

Cuando el kernel de Linux adoptó WireGuard, los teléfonos y las computadoras sin kernel propio
tomaron este camino: el mismo candado, en un lenguaje portátil.

*El motor en Rust — boringtun.* La placa de Cloudflare: `cloudflare/boringtun` ★7.221 (pulso
16-oct-2026), nacida el 12-oct-2018, con aire hasta el 29-jun-2026, bajo BSD-3. La
implementación del candado en Rust para servidores y fábricas grandes — la prueba de que el
protocolo es TAN pequeño y TAN firme que una empresa entera lo re-escribió por gusto y lo soltó
libre.

*Las herramientas de la mesa — wireguard-tools.* ★728 (pulso 16-oct-2026), nacida el 26-dic-2019, con aire hasta el 6-may-2026, bajo GPL-2.0. Los palos del oficio: `wg` (mira el túnel por dentro) y `wg-quick` (lo enciende con una línea). El taller de la consola — pa la casa del alambre, no pa el bolsillo.

*La malla amistosa — Tailscale Android.* `tailscale/tailscale-android` ★2.679 (pulso
16-oct-2026), nacida el 15-abr-2020, con aire hasta el 13-oct-2026, bajo BSD-3. La segunda fila
de esta pieza merece su placa desde el censo: la malla que administra los túneles de WireGuard
con empleados — las llaves que se reparten solas, la red de la casa que se arma sin alambre.

Cinco placas, un oficio: el sobre blindado. La familia completa del censo — y ninguna casa
muerta: todas con aire en 2026.

*🏛 LAS TRES CAPAS DEL TÚNEL*

El candado del viaje, por capas — de afuera hacia adentro, como se lee un sobre.

*La capa de afuera — el borrón.* Para el wifi del café y para el operador, tu teléfono habla con UNA dirección: la salida del túnel. Adentro no se lee nada — ni destinos, ni índice, ni contenido: todo viaja en el sobre cifrado.

La capa que la 42 dio solo pa la pregunta, esta la da pa TODO el caserón.

El borrón completo: el router ajeno ve humo, la torre del operador ve humo, y la conversación de
la casa viaja cerrada de punta a punta del túnel.

*La capa del candado — las cuatro mil líneas.* WireGuard no es una marca: es un protocolo
firmado en 2015 por Jason Donenfeld con una vara de sencillez brutal: criptografía moderna FIJA
(Curve25519 pa las llaves, ChaCha20-Poly1305 pa el sobre, BLAKE2s pa las huellas) y sin
negociación de algoritmos — nada que negociar mal.

El conjunto entero cabe en ~4.000 líneas de código frente a las cientos de miles de las suites
viejas. La línea de código es la vara de la forja: menos líneas, menos escondites.

El kernel de Linux la adoptó completa en 2020 (la versión 5.6) — el sello más duro que un
protocolo libre puede cargar.

*La capa de la llave — el routing criptográfico.* Cada aparato lleva un par de llaves (como el SSH de la 27) y una lista de AllowedIPs: qué viajes van por el sobre y cuáles no. La llave ES la dirección: si el sobre llega con una firma que no cuadra, la puerta ni se abre.

Y el roaming silencioso — la joya del oficio: el teléfono pasa del wifi del café a los datos y
el túnel NO se cae — el sobre sigue viajando como si nada. La capa que hace del candado un
mueble diario: nadie reinicia nada en la acera.

*⚖ LA VARA DE LA LICENCIA*

Cuatro leyes en la familia del túnel — el censo más variado de la fila de REDES.

*Apache-2.0* — la ley de la app del teléfono. La licencia de las patentes amarradas: el candado puede vivir en cualquier aparato, y nadie puede demandar por patentes después de usarlo.

La ley de la 31 (AFWall+) y de la 38 (el cerrojo), ahora en el bolsillo del viaje.

*MIT* — la ley del motor en Go. La ley corta: haz lo que quieras, deja el aviso.

El motor que los fabricantes pueden meter adentro de sus aparatos sin pedir permiso — y lo hacen: la mitad de los routers del barrio llevan este candado sin saberlo.

*BSD-3-Clause* — la ley de los dos motores grandes (boringtun de Cloudflare, la malla de Tailscale). Prima hermana del MIT: libre, con nombre, y con la cláusula de no usar el nombre de la casa pa vender.

Las dos placas más nuevas de la familia firman esta ley.

*GPL-2.0* — la ley de las herramientas de consola. La misma de la 41 (Cromite): lo que se
mejora, se comparte. Los palos del oficio, amarrados al oficio libre pa siempre.

La lectura de la vara: un protocolo tan pequeño que cada casa lo implementa a su manera — y cada
implementación firmó su ley sin pelearse. Cuatro leyes, cero guerras: la familia del túnel, la
más civilizada del censo.

*🎯 LA DOCTRINA DEL PUNTO DE SALIDA (las tres reglas del túnel)*

Aquí va la frontera honesta que ningún anuncio de VPN te cuenta — la doctrina de esta pieza.

*Regla uno — el túnel muda la confianza, no la borra.* Dentro del túnel, el café ya no ve nada. Pero la SALIDA del túnel ve lo que el café veía: tus destinos, tu índice, tu viaje completo.

Toda VPN es un traspaso: pasas de confiar en el operador a confiar en quien administra la salida. La pregunta nunca es «¿cifro o no cifro?» — es «¿en quién confío el índice HOY?».

El que te venda anonimato con una VPN, te está vendiendo la mudanza como si fuera la casa nueva.

*Regla dos — la vara completa es la salida PROPIA.* Un túnel a tu propia casa (la raspberry del
taller, el servidor de la nube de la fila 51-60, el router del salón) mueve la confianza al
único sitio que de veras controlas: tu casa.

El café ve borrón, el operador ve borrón, y el índice lo contesta TU salida — la pareja perfecta con el faro de la 42: el resolver propio contestando, el túnel propio protegiendo. La salida comercial con placa y política clara es la vara media: honesta SI está escrita la política.

*Regla tres — el túnel es una herramienta, no un estilo de vida.* En el café ajeno: encendido. En el wifi de tu casa: apagado (la casa manda — el viaje local no necesita sobre).

En el trabajo: según la faena. El que camina con el túnel encendido veinticuatro horas no está más seguro: está mudando su confianza al mismo sitio todos los días sin pensarlo.

La forja no fanatiza: administra. El interruptor del túnel es como el de la luz — se usa cuando
hace falta.

*🔧 LA RECETA DEL TÚNEL ENCENDIDO (una tarde, por pisos)*

Cómo se arma sin equivocarse:*

*Piso 1 — la app del interruptor (diez minutos).* Instala la app oficial del candado (la placa del censo — y si quieres la fuente de verdad, git.zx2c4.com). Ábrela: te pide crear un túnel desde cero o importar uno.

Sin servidor propio, este piso se queda en la repisa — la app sin configuración es un mueble vacío: no conecta a nada, porque WireGuard jamás vende salidas.

La app del candado no tiene «servidores gratis» — esa es la señal de su honestidad: el protocolo
es de la casa, las salidas las pones tú.

*Piso 2 — la salida propia en tu casa (la vara completa, una tarde).* En la raspberry del taller
(o en cualquier máquina siempre encendida): instala las herramientas (la placa GPL del censo),
genera el par de llaves del teléfono y el par de la casa, y firma los dos archivos de
configuración — el del teléfono lleva la dirección de TU casa como salida y las AllowedIPs del
viaje.

En el router del barrio: abre el puerto del candado hacia la raspberry. Prueba desde los datos
del teléfono: interruptor encendido — y tu índice ya sale por tu sala.

La receta fina de la obra: la 51-60 horneará la salida en la nube pa quien no tenga raspberry.

*Piso 3 — el perfil por barrio (la capa del detalle).* La app soporta varios túneles con nombres: «Casa» (la salida de tu sala), «Trabajo» (la red de la oficina si la faena lo pide), «Viaje» (la salida en la nube). Regla del mostrador: el nombre del túnel dice dónde confías — y el interruptor se lee como una lista de sitios, no como un amuleto.

*Piso 4 — el candado del candado (kill switch, cinco minutos).* En la app: bloquea el viaje sin túnel cuando el túnel seleccionado esté activo. Si el sobre se cae en la acera, el teléfono NO sale plano — se queda callado hasta que el sobre vuelve.

La regla de la póliza: el seguro vale cuando falla, no cuando funciona.

*Piso 5 — la prueba de la casa (media hora, la vara fina).* Con el túnel encendido: abre el registro del faro (la 42) — los destinos que ven ahora son los de TU salida. Visita un sitio de «cuál es mi IP»: tiene que decir la dirección de tu casa, no la del café.

Y la prueba del roaming: camina del wifi del café a los datos sin tocar nada — el túnel aguanta.

Si las tres pruebas pasan, el sobre está firmado.

*🧊 MITOS DESMONTADOS*

*«La VPN te hace anónimo».* Jamás. El túnel muda el punto de vista: el café deja de ver y la salida empieza a ver.

Anónimo no hay — hay mudanza de confianza. El anonimato de verdad es otra arquitectura (la cebolla de Orbot, la 31) y tiene su propio precio de lentitud.

El que prometa las dos cosas con un interruptor, miente en una.

*«Todas las VPN son iguales».* El protocolo manda. Las suites viejas arrastran décadas de parches y negociaciones (el IKE viejo, el OpenVPN con su OpenSSL de mil puertas); WireGuard firmó su criptografía de una vez, fija, en cuatro mil líneas auditables.

La diferencia no es de marca: es de oficio — la misma vara de toda la obra.

*«El túnel ralentiza el teléfono».* El mito del siglo pasado. El candado moderno pesa menos que el tráfico sin abrir en una red mala: el roaming silencioso ahorra las reconexiones, el sobre es liviano, y en el kernel (en las máquinas grandes) corre a la velocidad del resto del sistema.

En el wifi del café, el túnel suele LLEGAR antes que el viaje plano — el sobre directo tiene
menos trompezones.

*«Con HTTPS ya no hace falta túnel».* El https sella el CONTENIDO (nadie lee la carta); el túnel sella el VIAJE (nadie ve el sobre ni el índice ni el destino). Son capas distintas que se llevan bien: la carta sigue sellada por dentro, y ahora viaja en sobre blindado por fuera.

El que tenga el faro (42) ya cifró la pregunta — el túnel lleva el resto del caserón.

*❓ PREGUNTAS DE LA FILA*

*¿El túnel y el faro (la 42) se pelean por el teléfono?* Se turnan limpio: el faro usa su túnel
interno pa el índice, el candado lleva el resto del viaje — la app del candado tiene casillero
pa eximir al faro si el barrio quiere la pareja completa.

La firma de la forja: primero el faro (el índice, diez minutos), después el túnel (el caserón,
la tarde) — cada mueble su faena, la casa al completo.

*¿La app del candado sin salida propia pa qué sirve?* Pa nada sola — y eso es su honestidad. WireGuard no vende salidas: es el protocolo del sobre, no la empresa del viaje.

El que quiera salida ajena con marca, va a la tienda de las VPN comerciales (y lee la política de la salida ANTES de pagar — regla dos de la doctrina).

El que quiera la vara completa, firma su propia salida (piso 2 de la receta).

*¿Cuánta batería come el túnel encendido?* La del amuleto ligero: el candado moderno es el más barato de la familia de los sobres — sin reconexiones (el roaming silencioso), sin negociaciones, sin capas dobles. En el día del barrio el gasto se nota menos que el GPS, y menos todavía que la pantalla.

El mueble que más come del viaje es la pantalla: el candado ni se siente.

*¿Qué pasa si se me cae el túnel en plena calle?* Con el kill switch del piso 4: el teléfono se queda callado (el viaje no sale plano ni un segundo) hasta que el sobre vuelve. Sin kill switch: la apps se reconectan por su cuenta y unos segundos viajan descubiertos.

Por eso el piso 4 son cinco minutos que valen la tarde: el seguro del sobre.

*¿Puedo llevar el túnel a la laptop y a la tele?* El protocolo está en todas partes: la laptop
(la app de la casa de Donenfeld), el router (el candado que muchos traen de fábrica), la tele y
las cajas (los motores libres del censo).

Una salida propia en la casa puede llevar el sobre a TODOS los muebles del salón — el caserón
entero tras un solo candado, sin instalar nada en cada aparato.

*🧪 CASOS DEL BARRIO*

*Caso uno — la trabajadora del café del malecón.* Todos los mornings con el laptop en el wifi del café: el correo de la oficina, el banco del sueldo, el grupo del trabajo — todo en el router del extraño. Receta: túnel a su casa (la raspberry del closet que le montó su hermano con la receta del piso 2) + kill switch del piso 4.

El café ve borrón, el banco ve su casa, y el correo de la oficina viaja cerrado. La cuenta del
negocio: cero pesos al mes — la salida era suya desde el principio.

*Caso dos — el estudiante del captive portal.* El wifi de la universidad pide login en un portal que registra TODO, y el servidor del proyecto del tesis está bloqueado en la red del recinto. Receta: el túnel encendido DESPUÉS del portal (el portal tiene que verte entrar una vez), y desde el sobre el proyecto vive en tu casa: el recinto ve un sobre, el tesis avanza.

La nota fina: el portal que exige registro mira la PRIMERA conexión — el sobre blindado va
después, como debe ser.

*Caso tres — el negocio con dos colmados.* La dueña de los dos colmados con las cajas registradoras en dos edificios y el inventario en una sola hoja. Receta: túnel entre las dos sedes (los dos routers con el candado del censo — site-to-site se llama en el oficio): las cajas hablan como si estuvieran en la misma sala, sin pagar línea privada.

El alambre del negocio, amarrado con cuatro mil líneas — y la hoja del inventario, con la casa
mandando.

*Caso cuatro — el que vive fuera y quiere su barrio.* El dominicano en Nueva York con la cuenta
del banco de Santo Domingo que desconfía de las IP extranjeras.

Receta: salida propia EN la casa de la familia (la raspberry del colmado de la abuela, el piso 2 a distancia con un QR por el canal cifrado de la 27) — el banco ve su barrio de siempre, y la confianza del viaje vuelve a casa. La mudanza al revés: el sobre viaja pa acá pa que el índice salga pa allá.

La vara de la doctrina, funcionando en dos islas.

*Caso cinco — la iglesia del barrio con el wifi abierto.* El templo de la esquina con el wifi abierto pa la comunidad (la contraseña en el boletín del domingo): cien teléfonos en un router sin ton ni son. Receta: la salida propia del templo (una raspberry en la oficina del párroco, el piso 2 a escala de parroquia) + el perfil «Templo» en los teléfonos del consejo.

La congregación con el sobre puesto — y el router del templo viendo solo borrón. La caridad del
aire, amarrada con cuatro mil líneas: la puerta abierta, el viaje cerrado.

*Caso seis — la agencia de chóferes del mercado.* El dueño de la agencia con cinco chóferes en
la calle (el reparto del día en el teléfono, las rutas por el grupo): la cuenta del negocio
abierta en los cinco aparatos.

Receta: la malla de la segunda fila con la letra chica leída, o la salida propia del almacén — y la regla de la nafta de las llaves: a cada chófer, la suya, EN su aparato (jamás el QR compartido por el grupo). El reparto viaja en sobre, la flota habla como si estuviera en la misma oficina, y la llave de la casa se reparte como la nafta: a cada uno, la suya.

*¿Y si el café del barrio es de confianza — dueño conocido?* La confianza del dueño no amarra al
router: el wifi del salón comparte aire con cada aparato de la clientela y con el equipo del
propio café (que a veces ni el dueño administra).

El sobre no acusa al vecino: protege el viaje de los DOS — y al café le conviene también, con su
caja y su inventario en el mismo sobre (el alambre del negocio, el caso tres). El pan del vecino
se comparte con el sobre puesto.

*¿El candado sirve pa la tele y la consola del salón?* Sí — y ahí brilla la salida en el router: toda la casa tras un solo sobre (la segunda fila del alambre). La consola con el sobre viaja al servidor del juego sin que la torre del operador anote el destino; la tele del salón consulta sin que nadie del salón ajeno la mire.

El caserón al completo, sobre puesto — la vara completa servida una vez, pa todos los muebles.

*¿Y en mi salida propia — quién ve el índice?* El que administra la raspberry (el de la casa, el
hermano que la montó, el consejo del templo): la doctrina se aplica en escala chica — la
política escrita de la CASA (quién puede mirar el registro de la salida, y pa qué) vale tanto
como la del proveedor ajeno.

La forja la firma en la página del taller: la salida propia sin reglas escritas es la salida
ajena con otro dueño — la confianza, también en casa, se documenta.

*🏭 LA DESPENSA DE DATOS (todo lo medido, en una repisa)*

*El candado, por líneas:* ~4.000 líneas el protocolo WireGuard — frente a las cientos de miles
de las suites viejas de VPN. La vara de la forja: la línea de código como medida del escondite.

*El kernel, por fecha:* el kernel de Linux lo adoptó completo en la versión 5.6, marzo-2020 — la
primera vez que un protocolo de VPN nuevo entró al kernel de la casa grande de una pieza.

*La familia, por placas (censo 16-oct-2026):* la app ★1.640 · el motor Go ★4.453 · el motor Rust
★7.221 · las herramientas ★728 · la malla ★2.679 — cinco placas, todas con aire en 2026, ninguna
casa muerta.

*La familia, por leyes:* Apache-2.0 (la app) · MIT (el motor Go) · BSD-3 (el motor Rust y la
malla) · GPL-2.0 (las herramientas) — cuatro leyes, la familia más variada de la fila de REDES.

*El handshake:* cada dos minutos el sobre renueva su firma — la llave de la conversación cambia
mientras tú ni te enteras. El candado que rota su cerradura caminando.

*El roaming:* del wifi a los datos sin caer — la joya del oficio diario. El sobre no sabe de aceras.

*🕰 LA EDAD DEL TÚNEL*

El protocolo firmó su diseño en 2015 y el kernel lo abrazó en 2020: una década de madurez, media
década de corona. La app del Android nació en 2018 (la placa del censo lo firma: 27-abr-2018) y
lleva su aire hasta junio de 2026.

La familia es joven y vieja a la vez: el diseño lo bastante nuevo pa no cargar los 90, lo
bastante viejo pa estar auditado por el mundo entero.

La edad de la confianza — ni la novedad del mes ni el fósil del siglo pasado.

*💬 LA CONVERSACIÓN HONESTA*

Dígase claro: esta pieza NO vende la VPN de la tienda. La conversación del barrio con el anuncio de las VPN comerciales es la misma de siempre: «anonimato» prometen (mudanza venden), «no hay registros» susurran (la salida la tiene su servidor — el registro que importa es el de la SALIDA, y ese lo firma una política que nadie audita en tu nombre).

La doctrina de esta pieza es contraria al anuncio: la salida propia, el interruptor por barrio, la confianza administrada. Las VPN comerciales con placa y política clara tienen su sitio (el viaje del viajero sin casa pa meter una raspberry) — pero se contratan leyendo, no creyendo.

La forja no odia el negocio: exige la letra chica.

*🎞 LO QUE ESTA PIEZA NO DICE*

No dice que el túnel te vuelva anónimo — dice que muda el punto de vista: el café ve borrón; la
salida, el índice.

No dice que el candado sea magia — dice que son cuatro mil líneas firmadas: auditadas por el
kernel, copiadas por tres motores.

No dice que toda VPN valga lo mismo — dice que el protocolo manda: el sobre firmado en 2015 y
los vestidos de los 90 no son el mismo traje.

No dice que el túnel frene la casa — dice que suele empujar: en la red mala, el sobre directo
llega antes.

No dice que sea pa todo el día — dice que es una herramienta de barrio: encendida en el café
ajeno, callada en tu casa, administrada siempre.

*🩺 LA SALUD DEL TÚNEL AL CORTE (el parte del viaje)*

El parte del 16-oct-2026: la familia respirando — la app con aire de junio, el motor Go con aire de la semana pasada (push del 6-oct), la malla con aire de hace tres días (push del 13-oct), el motor Rust y las herramientas en su quietud productiva. Cinco placas, cero casas muertas: el bloque del túnel llega al censo más sano que ninguno.

La lectura fina del parte: la familia del túnel es la de las PLACAS MÁS PAREJAS EN AIRE — las cinco empujando en 2026, el protocolo en el kernel de la casa grande, y una empresa del tamaño de Cloudflare manteniendo SU implementación por gusto. La salud del ecosistema: un protocolo tan pequeño que cuidarlo no cuesta — y por eso nadie lo suelta.

*📐 LA MEDIDA DEL TÚNEL (lo que el censo deja leer y no se ve)*

Tres medidas finas de la noche.

La primera: la familia de las cuatro leyes. Ningún bloque de la serie firmó tanta variedad sin
guerra: Apache, MIT, BSD-3, GPL-2.0 — cada implementación con su ley, todas conviviendo en el
mismo protocolo.

La medida fina: el protocolo es TAN pequeño que la ley de cada casa no se pelea con la de la
vecina — la paz de las cuatro mil líneas.

La segunda: la pirámide del candado. ★7.221 (pulso 16-oct-2026) el motor Rust (la copia de la
empresa), ★4.453 el motor Go (el motor de los bolsillos), ★1.640 la app (la puerta del barrio) —
la placa más grande NO es la que usa la gente: es la que usan las fábricas.

La medida de la forja: en el túnel, el estrellado mide fábricas — el bolsillo se mide en
interruptores encendidos, que el censo de estrellas jamás verá.

La tercera: la edad doble. Diseño de 2015, corona del kernel en 2020, aire completo en 2026 —
once años sin una sola grieta de diseño grande.

En una fila donde los muebles se renuevan por temporadas, el candado lleva una década sin
cambiar de fundamento: la medida de lo firme — lo que no se reescribe, se hereda.

Y la nota fina del negocio del miedo: el mercado de las VPN comerciales mueve miles de millones
al año vendiendo la sombra del sobre — sin protocolo propio (casi todos usan el candado de esta
pieza por dentro), sin salida que el cliente controle, y con el anonimato de escaparate que la
doctrina desmonta.

El barrio que arma SU sobre con placa del censo, tiene lo que el anuncio finge vender: el
protocolo de verdad, la salida elegida, y la confianza administrada en casa.

*📻 LA SEGUNDA FILA (lo que quedó fuera del túnel)*

*La malla con empleados — Tailscale.* La placa ★2.679 (pulso 16-oct-2026) del censo merece su
caja: la red de la casa que se arma sin alambre — cada aparato con su llave, el coordinador
repartiendo direcciones, y los datos viajando de punta a punta SIN pasar por el medio.

La comodidad hecha placa BSD: la casa grande (la familia, el negocio con dos colmados del caso tres) armada en una tarde. Su letra chica está en los riesgos (el coordinador ajeno) y su salida libre (headscale) queda prometida pa el taller de la 51-60.

La malla es WireGuard con conserje: se paga en confianza ajena lo que se gana en no tocar el router.

*Orbot y la cebolla — la otra mudanza.* La 31 abrió la sala con la cebolla: el anonimato de verdad (nadie ve ni la salida ni el destino) pagado en lentitud. El túnel y la cebolla NO compiten: el sobre muda la confianza al sitio que tú eliges; la cebolla la reparte entre voluntarios del mundo entero.

El café con el sobre, el periodista con la cebolla — cada vara su faena, la caja de herramientas
del barrio completa.

*El candado del router — el caserón sin instalar nada.* Muchos routers del barrio ya traen el
candado de fábrica (el motor MIT del censo vive adentro de media fábrica del planeta): una
salida propia en el router muda el viaje de TODA la familia sin tocar un solo teléfono.

La vara completa con la faena una sola vez — y la desventaja clara: el router sin músculo a
veces come el candado a trompazones. Por eso la receta de esta pieza recomendó la raspberry: el
mueble chico dedicado, el router descansando.

*🗼 EL TÚNEL EN TU DÍA A DÍA (cuatro rutinas del oficio callado)*

*El morning del café.* Llegas, pides, te sientas — el teléfono agarra el wifi y el interruptor del «Café» se enciende solo (la app lo trae: encender al conectar a una red). El banco, el correo y el grupo de la familia viajan en sobre; el barista ve un borrón.

Ni un toque extra: la administración de la confianza, hecha costumbre.

*El trabajo desde la casa.* La faena de la oficina que pide la red interna: el túnel «Trabajo» encendido media jornada — los documentos de la firma viajando cerrados, y al terminar, interruptor abajo. La casa manda de nuevo.

El sobre no es amuleto: es herramienta con horario.

*El viaje de regreso.* El aeropuerto, el hotel, el wifi del extranjero: el sobre a tu casa de Santo Domingo encendido apenas aterrizas — el banco ve tu barrio, la familia ve tus fotos, y el wifi ajeno del otro lado del mar ve humo. El caso cuatro de la pieza, hecho costumbre: la isla llevada en el bolsillo.

*La madrugada del alambre.* Una vez por temporada: revisa que la raspberry sigue en pie, que las llaves no vencieron, que el kill switch sigue armado — cinco minutos con el café temprano. El alambre de la casa se cuida como el tanque de agua: nadie lo mira hasta que falta — y el que lo mira una vez por temporada, jamás se queda seco.

*🧵 GENEALOGÍAS DEL TÚNEL*

*El abuelo — el PPP de los modems.* Los 90: el viaje cifrado entre tu casa y el trabajo, por teléfono, con suites que negociaban su propia criptografía. El abuelo del sobre — lento, complicado, y con la semilla de la idea: la confianza muda de sitio cuando el viaje se cierra.

*El padre — IPsec y OpenVPN.* Los 2000 y los 2010: las dos suites que sostuvieron el mundo — una en el kernel (IPsec, la de las oficinas grandes), otra en el espacio de usuario (OpenVPN, la de los barrios y los cafés). El padre del sobre: firmes, probados...

y con cientos de miles de líneas cada uno. La vara de las líneas nació de compararlos.

*El hijo — WireGuard.* 2015: un desarrollador cansado de la negotiation se pregunta qué pasaría si la criptografía NO se negociara — si el traje viniera cosido de fábrica. Cuatro mil líneas después, el kernel de Linux lo abrazó (2020) y tres motores lo copiaron (Go, Rust, y el kernel mismo).

La generación que pasó del vestido a la medida al traje cosido: menos puertas, más casa.

*El nieto — la malla.* 2020 en adelante: Tailscale y sus hermanas toman el candado y le añaden el conserje (las llaves que se reparten solas, la red que se arma sin alambre). El nieto del sobre: el mismo candado de siempre, administrado como la familia de hoy administra — por apps, por invitaciones, por QR.

La genealogía completa: del modem al conserje, en tres generaciones y una sola idea.

*📦 LA DESPENSA DEL TÚNEL (tu viaje, ordenado como gente)*

*El interruptor con nombres* — «Casa», «Trabajo», «Nube»: la lista de sitios donde confías,
legible en la pantalla del candado. Si el interruptor tiene tres túneles y ninguno se llama
«Casa», la vara de la doctrina te está mirando.

*El kill switch armado* — el seguro del piso 4: sin sobre, sin viaje. El único seguro del barrio
que se contrata en cinco minutos y paga todas las lluvias.

*El QR del canal cifrado* — la llave de la casa viajando por el sobre de la 27, jamás por el
grupo abierto. La foto del QR es la llave del caserón: ni la cámara del barrio la ve.

*La fecha de la política* — si tu salida es ajena: el día en que leíste la política de
registros, anotado en la página del taller. La confianza que se documenta es la única que dura.

*El interruptor que se enciende solo* — la app que arma el «Café» apenas el wifi ajeno responde:
la administración de la confianza, hecha reflejo. El barrio ni toca el teléfono — y el sobre va
puesto.

*La fecha del censo* — el pulso del 16-oct-2026, firmado en esta pieza: cinco placas con aire,
cuatro leyes en paz. La casa que cita su censo con fecha, negocia con la verdad.

*El café temprano del alambre* — la revisión de temporada del día a día: raspberry en pie,
llaves vivas, seguro armado. Cinco minutos por temporada que valen el año.

*🪧 EL CARTEL DEL TÚNEL*

*El viaje entero en el sobre — no solo la pregunta: el caserón.*

*Cuatro mil líneas firmadas una vez — el traje cosido que el kernel abrazó.*

*La salida propia, la vara completa — y el interruptor que dice «Casa».*

*El seguro se arma antes de la lluvia — el kill switch, cinco minutos.*

*Y la confianza se administra, no se canta — el sobre se usa donde el suelo es ajeno.*

*😄 EL MEME DE LA CASA*

El anuncio de la VPN de la tienda: «SÉ INVISIBLE EN INTERNET» — con el tigre de fondo y la
estrella de cinco puntas. El barrio con la doctrina de esta pieza: «Invisible no — pero el café
ve un borrón y mi índice lo contesta mi sala».

El tigre calla. La casa administra.

*⚠ LOS RIESGOS DEL TÚNEL, CON FECHA*

*La salida ajena (el riesgo número uno, 16-oct-2026).* Todo túnel comercial deja tu índice en el servidor del que vende. La salida: la regla dos de la doctrina — salida propia cuando se pueda; salida ajena solo con política de registros escrita y firmeza de placa.

El anuncio que prometa anonimato, devuelve el sobre sin abrirlo.

*El túnel caído sin seguro (el riesgo callado).* Sin kill switch, la caída del sobre en la acera deja salir el viaje plano por segundos — justo cuando crees que vas cubierto. La salida: el piso 4 de la receta, cinco minutos.

La regla del seguro: se contrata ANTES de la lluvia.

*La llave copiada en el QR (el riesgo de la mesa).* El QR pa pasar la configuración es cómodo — y si la mesa tiene ojos, la llave privada del teléfono viaja en la foto. La salida: genera las llaves EN cada aparato (la app lo hace sola), y pasa el QR solo por el canal cifrado de la 27 — jamás por el grupo del barrio.

*La malla con empleados (el riesgo de la segunda fila).* Tailscale administra las llaves con su coordinador: las direcciones y las llaves públicas pasan por su servidor (los DATOS, jamás — van de punta a punta). Es la vara media de la doctrina con placa BSD: cómoda pa la casa grande, con la letra chica leída.

La salida: la malla libre que la fila 51-60 va a hornear (headscale, el coordinador propio) — la
misma malla, el coordinador en tu sala.

*📖 GLOSARIO DE LA COSECHA*

*Puente.* El cliente que no guarda música: la busca en el catálogo de otro y la trae al momento.
Debe su vida a un río ajeno — por eso la vara de esta escuela mira el push con fecha antes que
las estrellas.

*Cajón.* La escuela del archivo propio: MP3 y FLAC tuyos, tocados sin internet ni río ajeno.
Nunca depende de un provedor, jamás se corta en la loma, y su única obligación es que tus
etiquetas estén peinadas.

*Detective.* La escuela del descubrimiento: cruza fuentes, amarra discografías y te muestra
versiones. Muffon es su bandera en la cosecha — menos «ponme la playlist», más «enséñame el mapa
del artista».

*Cosecha.* El pase de vara ancho por una familia del censo: se mide casa por casa, con placa, y
lo que no pasa no se borra — se anota. La cosecha es la prueba de que el método de la casa
funciona.

*Placa.* El paquete completo de datos de una casa: estrellas con fecha, push con fecha, licencia
con nombre, fila de asuntos. Sin placa no hay censo — hay lista de apodos.

*Pulso.* La toma de datos con hora. El censo de la tarde no es el pulso de la noche: el #10 de
esta pieza midió a las ~23:12 UTC y cazó dos casas moviéndose en vivo. El censo no es una foto:
es un latido.

*Mapa vivo.* La numeración de los pulsos de la casa (#1 al #10 al corte de esta pieza). Cada
mapa vivo deja caja fechada para que el próximo lector compare su cuaderno con el nuestro.

*Censo vivo.* El barrido grande de la casa: 5.684 repositorios al 15-oct-2026, con estrellas,
pushes y licencias. Es la fuente de verdad de esta pieza — y crece por puerta verificada, no por
promesa.

*Vara.* La regla de la casa que decide qué entra al mapa: fuente abierta, licencia legible,
pulso con fecha. La vara no clasifica por gusto — mide por oficio.

*Corte.* El día y la hora en que se midió la verdad. Toda esta pieza es del corte 15-oct-2026;
mañana el corte dirá lo que viva mañana — y esa es su honestidad, no su debilidad.

*Quietud.* El silencio anotado: tronco grande sin empuje, con fecha de última actividad. No es
muerte ni abandono automático — es pausa con acta. Timber y InnerTune son las quietudes de esta
cosecha.

*Push.* El último empuje del taller: la fecha de la última actividad del repositorio. En la
escuela del puente, un push de esta semana vale más que mil estrellas — es la diferencia entre
taller vivo y museo.

*Release.* La versión publicada y firmada por el taller: la única forma del software que la casa
palomea. OuterTune al corte trae la v0.10.1 contándose en público — eso es salud de release.

*Asuntos.* Los issues del taller: la fila pública donde los problemas esperan turno. No cuenta
la cantidad — cuenta si se contestan. Trescientos con respuestas respiran; cuarenta en silencio,
no.

*Estrellas.* El aplauso del ecosistema: mide fama, no calidad. ★49.974 (15-oct-2026) hace a
Spotube el más aplaudido de la cosecha — la vara de la casa decide si ese aplauso viene con
contrato.

*Licencia.* El contrato escrito del taller: qué puedes hacer con su código. En esta cosecha
firman GPL-3.0, AGPL-3.0 y MIT — y tres casas viajan sin firma clara, con su vara marcada.

*GPL-3.0.* La licencia copyleft más común de la cosecha: usa el código, y lo que publiques con
él se abre con la misma placa. Es la firma que convierte un silencio en genealogía — InnerTune
la firmó, y OuterTune hereda con honor.

*AGPL-3.0.* La GPL para servicios: si el código corre como servicio, también se abre. muffon la
firma al 15-oct-2026 — la casa la lee con el mismo respeto que la GPL de sus hermanas.

*MIT.* La licencia más simple de leer: haz casi lo que quieras, conserva el aviso. Salt Player
la firma — garantía mínima, cadena limpia, cero letra chica.

*NOASSERTION.* La placa en blanco: el repositorio no declara licencia reconocida. No es delito —
es ausencia. Sin firma, el derecho por defecto es «todos los derechos reservados», y los
reempaques viajan sin freno legal.

*Copyleft.* La regla del recíproco: si tomas el código de un taller público para hacer el tuyo,
lo que agregues sale con la misma placa. Es el antídoto del reempaque silencioso.

*Fork.* La continuidad del software libre: un taller que nace del código de otro, respetando su
licencia. OuterTune es el fork vivo de InnerTune — no su imitación: su línea.

*Heredero.* El taller (o la línea) que toma el código de una casa quieta y sigue empujando. Para
heredar con honor hace falta una sola cosa: que la madre haya firmado licencia. Sin firma no hay
testamento.

*Reempaque.* El APK que toma la obra de un taller, le mete anuncios o peaje, y la reparte con
placa ajena. El enemigo viejo de la casa — y la razón de la vara: origen, firma, permisos, sin
prisa.

*Tienda legal.* La puerta de instalación que muestra el repositorio de origen: Droid-ify,
Neo-Store, Accrescent, el F-Droid de la pieza 01. Si la tienda no muestra el repo, no es tienda
— es grupo con carrocería bonita.

*Droid-ify.* El cliente F-Droid material de la casa (pieza 01): busca la casa por su nombre
exacto del censo y la instalación viaja con la placa a la vista. La primera puerta recomendada
de esta cosecha.

*Accrescent.* La tienda de estándares altos de la pieza 01: firmas estrictas, catálogo curado.
Segunda puerta legal — la que usa el que prefieren las varas cortas.

*F-Droid.* La casa madre de las tiendas libres: el catálogo histórico del ecosistema. Vieja,
sabida y firme — el anexo donde la mayoría de las catorce de esta cosecha tiene placa.

*APK.* El paquete instalable de Android. En sí mismo es neutro — como un sobre. La vara de la
casa pregunta siempre lo mismo: ¿quién lo selló? La respuesta separa la tienda legal del grupo
de siempre.

*Firma.* La marca criptográfica del taller en su release. La tienda legal la verifica por ti; el
APK de grupo, nadie sabe quién la puso. Sin firma verificable, no hay confianza — hay fe, y la
casa no trabaja con fe.

*Material You.* El lenguaje de diseño de Android moderno que sigue el color de tu fondo. Retro
Music lo lleva de bandera (★5.357, 18-oct-2026) — el mueble clásico vestido de esta década.

*Etiqueta.* La información adentro del archivo de música: título, artista, álbum, número, año.
El reproductor lee la etiqueta, no el nombre del archivo — peinar etiquetas es peinar la
biblioteca entera.

*FLAC.* El formato sin pérdida: suena exacto al master y pesa cinco veces más que un MP3. Para
el archivo maestro en la PC — no para el bolsillo del día a día.

*MP3.* El formato que movió el mundo y sigue mandando en el bolsillo: a 320 kilobits suena
igualito en auricular humilde y pesa como la palabra. La casa lo respeta sin nostalgia ni
complejo.

*Caché.* La memoria del río: las canciones que ya suenaste se guardan un tiempo para no volver a
bajar. Es la gracia económica del streaming libre — la mata de hilo del tercer día suena media
gratis.

*Scrobble.* El hábito del detective: registrar lo que suenas para amarrar historial y
descubrimiento. muffon lo trae de fábrica — el reproductor que también lleva el cuaderno de
campo.

*Discografía.* El mapa completo de un artista: álbumes, años, versiones. La vara del detective
es amarrarla bien — muffon la cruza entre fuentes al 18-oct-2026 con ★2.246 y AGPL firmado.

*Multi-fuente.* La casa que no se casa con un río: consulta varios provedores y te sirve la
versión que esté limpia. Spotube, Namida y muffon viven de esa libertad — con sus licencias
mirándose dos veces.

*Streaming.* El modelo del río: suena ahora, no guarda nada tuyo. Infinito mientras el río corra
— y por eso esta pieza repite: exporta lo que amas, streamea lo que descubres.

*Aleatorio.* El modo más honesto del reproductor: te enseña cuánto conoces tu propio archivo. En
el cajón con etiquetas peinadas, el aleatorio es un paseo; sin etiquetas, un secuestro.

*Lista.* La secuencia guardada: el arte del anfitrión y la herramienta del viajero. La lista
buena se exporta a archivo — la que solo vive dentro de la app es rehén de la app.

*Exportar.* Sacar tus listas y favoritos a archivo que otra casa pueda leer. La prueba de
propiedad de la escuela del río: si el mueble no exporta, eres inquilino con mueble bonito.

*Sincronía.* La rutina que mueve tu música entre PC y teléfono sin cable ni heroico: Syncthing y
su familia (viene en la serie). La copia maestra queda en casa; el teléfono lleva la de trabajo.

*Copia maestra.* El original en FLAC que vive en tu PC o disco, del que nacen las copias de
bolsillo. Convertir del maestro, nunca al revés: bordarle encaje a un saco de harina no lo
vuelve traje.

*Root.* El teléfono abierto de par en par. La casa lo trata en la pieza 20 con sus letreros — y
esta cosecha musical NO lo necesita ni un poquito: fuente abierta es taller público, no cirugía.

*Cuenta de prueba.* El casco de la obra: la cuenta sin nada personal que estrenas cualquier app
nueva. En esta cosecha ninguna de las catorce pide contraseña — la que la pida, desinstálala y
anota la fecha.

*Letrero anti-reempaques.* La regla que SimpMusic puso en su casa (pieza 08) y se volvió ley del
barrio: los reempaques no son míos y no los apoyo. El letrero que le quita al clonero su excusa
favorita — la duda.

*Genealogía.* El oficio de contar de dónde viene cada casa: troncos, forks, herederos,
quietudes. La pareja InnerTune→OuterTune es la lección viva de esta cosecha — misma sangre,
distinto pulso.

*Sucesión.* El relevo ordenado cuando un taller se duerme: la línea GPL continúa en el heredero
y el mapa anota el cambio con fecha. Sucesión limpia no tiene drama — tiene acta.

*Corte honesto.* El corte que declara sus huecos: faltan casas, el censo sigue creciendo, y la
pieza dice qué queda fuera. Sabe a lo que sabe — y lo que sabe, lo firma.

*Rumor con formato.* Lo que queda de una recomendación cuando se le recorta la fecha: «Timber es
el mejor» sin el 28-abr-2023 es un rumor con negritas. La casa comparte mapas con corte puesto.

*Taller público.* El repositorio abierto: el taller cuyas herramientas, filas y errores están a
la vista de todos. Las catorce de esta cosecha lo son — y por eso se les puede medir sin pedirle
permiso a nadie.

*Resurrección.* El regreso con fecha: tachiyomiJ2K volvió de dos años y medio de silencio (pieza
15). Por eso la quietud lleva acta y no lápida — la casa celebra el despertar el día que ocurre.

*Gemela FB.* La copia hermana de una pieza que nacía para Facebook. Por orden del dueño del 15-oct noche, la serie nueva (21 en adelante) viaja SIN gemela: WhatsApp puro — el muro de Facebook queda fuera de esta cosecha.

Ley anotada en la hoja de ruta, no en la discordia.

*LA LISTA.* El índice vivo de la biblioteca (la pieza 00): el mapa del mapa donde cada guía
nueva toma su número y su fila. Esta cosecha entra al corte siguiente de LA LISTA con su placa.

*Boleta.* El único requisito de entrada a la biblioteca: haber abierto el repositorio, la página
de versiones y la libreta de obra. Las catorce de esta cosecha pagaron boleta — por eso tienen
pieza.

*Lupa.* La herramienta de la casa que examina una pieza como un oficial de aduana: respiro,
cadencia, anclas de tiempo, dialecto. La v6 «aire» es la que exige bloques que respiren — esta
pieza nació bajo su vara.

*Respiro.* La ley del aire: ningún bloque de la pieza debía quedarse sin oxígeno — al corte del
15-oct la vara mide ~380 caracteres por bloque. La música también respira: es la diferencia
entre leer y ahogarse.

*Certificación.* Las baterías que la pieza corre antes de firmarse FINAL: la experta (v4), la
evolutiva (v5) y la de rarezas (fuzz) con semilla fija. Sin batería no hay sello — y sin sello,
la pieza no se llama final.

*Acta.* El documento fechado donde la casa anota lo que hizo: actas de corrección, actas de
censo, actas de push. Lo que no tiene acta no pasó — y lo que pasó con acta, no se puede negar.

*Registro.* El cuaderno mayor de la casa: registro-2026-10-15.md y sus hermanos por fecha,
append-only. Aquí vive el acta de esta cosecha, con su pulso #10 y su hora.

*Censo abierto.* La puerta del dueño: lo que encuentra un día, entra el MISMO día al censo con
prioridad. Los Hush de la pieza 17 entraron así — y esta cosecha tiene la puerta abierta para la
próxima casa musical que llegue.

*Hallazgo.* La puerta que alguien trae a la casa: un repositorio que merece mapa. No se necesita
vara de hierro para traerlo — se necesita fuente abierta: lo demás lo mide el censo.

*Cola.* El orden sin favor: lo que no pasa la vara hoy queda en cola anotada, no en silencio. La
cola tiene orden, no pena — y se revisa en cada corte.

*Anti-omisión.* La ley de la casa contra el dato sin fecha: lo que no se re-pulsó viaja FECHADO
como el corte en que se vio. Nunca «actualmente» sin hora — siempre «al 15-oct-2026».

*Triple lectura.* La lectura de la casa antes de publicar: la del técnico (¿el dato aguanta?), la del lector (¿se entiende al primer trago?) y la del rival (¿dónde me meto?). Esta pieza pasó las tres — y los mitos son puro oro de la tercera.

*Río.* El catálogo ajeno: YouTube Music, archive público, provedores varios. El río corre sin
pedirte permiso y se corta sin avisar — por eso la escuela del puente se mide por push fresco.

*Señal.* La torre que el río necesita y el cajón no. En la loma, la señal es la primera vara: lo
que no descargaste no existe en carretera — lección que el campo enseña gratis.

*Loma.* La geografía honesta del país: donde el streaming confiesa su dependencia. Toda la
escuela del puente se queda mudita en la loma — el cajón suena igualito.

*Modo avión.* La prueba de fuego del mueble local: ponerlo y que suene. Si tu lista de fiesta
necesita torre, no era lista — era esperanza.

*Anfitrión.* El que pone el teléfono en la fiesta. Su vara: lista corrida, pantalla bloqueada y
cero promesas de wifi ajeno. La casa le recomienda cajón — el río en fiesta es apuesta.

*Coleccionista.* El que suena, guarda, etiqueta y copia. No necesita FLAC de colección para
empezar: necesita la rutina — maestro en PC, copia en teléfono, lista exportada. La estructura
antes que el volumen.

*Oído con oficio.* El que escucha preguntando: qué versión, qué año, qué disco. La escuela del
detective existe para él — muffon al 18-oct-2026 con ★2.246 y AGPL firmado.

*Bitrate.* Los kilobits por segundo del audio: la medida de cuánto archivo pesa una canción. A
más bitrate, más fidelidad hasta donde el oído y el altavoz alcancen a distinguir — el 320 del
MP3 es el techo práctico del bolsillo.

*Pérdida.* Lo que un formato tira al comprimir. El MP3 la tiene (y bien administrada a 320
alcanza al bolsillo); el FLAC no la tiene — y por eso uno viaja y el otro archiva.

*Conversión.* Pasar del maestro a la copia de trabajo: FLAC a MP3, una vez, desde el original.
La conversión inversa no existe en la casa — no se inventa calidad que no bajó.

*Permiso.* Lo que la app te pide al entrar. La vara: permiso fuera de oficio = desinstalar y
volver al censo. Un reproductor que pide contactos no es reproductor — es huésped con maleta.

*Desinstalar.* El acto de higiene digital: quitar la app con fecha anotada. La casa lo
recomienda sin drama — la desinstalación honesta es la mitad de la vara que nadie cuenta.

*Actualizar.* Traer la nueva release del taller legal. En la escuela del puente, actualizar
semanal no es manía: es respirar — el río cambia de puerta y el taller contesta con push.

*Versión.* El número que el taller pone a su release (OuterTune v0.10.1 al corte). Con versión
hay historia: se puede comparar, se puede volver atrás, se puede exigir.

*Snapshot.* La foto del estado en un momento: la caja de pulso de esta pieza es un snapshot del
15-oct-2026 a las ~23:12 UTC. Mañana será historia fechada — que es el único tipo de historia
que la casa guarda.

*Dialecto.* La voz de la casa: dominicano de verdad, con clienta, barrio y chin chin — pero el
dato siempre en traje formal. El dialecto es la envoltura; la placa, el contenido.

*Chin chin.* El golpe de mesa de la moral del meme: la sentence final que clava la lección. No
es adorno — es la firma de la casa cuando el oficio quedó claro.

*Muro FB.* La fila de piezas gemelas que la casa publicaba en Facebook. Desde el 15-oct noche:
la serie 21+ va sin muro — WhatsApp puro. La ley del dueño, anotada con fecha y sin melcocha.

*Índice.* El mapa de una pieza: el árbol de esta guía. Un árbol único por pieza, con secciones y
tiempos — el lector sabe dónde está parado y cuánto falta pa la parada.

*Provedor.* El que sirve el río: la plataforma cuyo catálogo atraviesa el puente. No es socio de
nadie y no avisa cuando muda la puerta — por eso el taller que la sigue es la primera vara de
esta escuela.

*Fila viva.* La fila de asuntos que se contesta: la señal de taller respirando sin ambigüedad.
Los asuntos de esta cosecha van de 42 (Musify) a 868 (Spotube) al 15-oct-2026 — la vida no es la
cantidad, es la contesta.

*Publicar.* El acto de soltar la pieza con acta, pulso y hora. Publicar sin fecha es rumor;
publicar con fecha es mapa. Esta cosecha sale el 15-oct-2026 con pulso #10 — y su sello lo
cuenta.

*Colmado.* La bodega del barrio: lo tienes todo cerca, te fiarán la libreta, pero el catálogo es
el que cabe en el estante. En esta pieza, la escuela del puente con factura propia — respetada,
y ajena al censo.

*Puerta al viento.* Vivir de un solo río sin cajón propio: la casa abierta cuando el provedor
muda la puerta. El antídoto cabe en una línea — descarga lo que amas, streamea lo que descubres.

*Segunda fila.* Los vecinos que el censo vio y esta pieza no tomó: podcast, vídeo puro y
talleres bajo la vara del barrido. No es exclusión — es cola con orden, y se revisa en cada
corte.

*Oído del barrio.* El que escucha antes de opinar: prueba dos muebles, mira dos placas y
pregunta en la fila antes de palomear. No nace sabido — se hace con una semana de ritual bien
dada.

Túnel|El sobre blindado del viaje: todo el caserón cifrado entre tu teléfono y la salida. La
tercera mudanza del aire — después de la ventana y del índice.

Salida|El sitio donde el sobre se abre y tu índice se contesta: tu casa, tu nube, o el servidor
ajeno. La regla de la doctrina: la confianza se muda ahí — jamás se borra.

Kill switch|El seguro del sobre: sin túnel, sin viaje — el teléfono calla hasta que el candado
vuelve. Cinco minutos que valen todas las lluvias del año.

Roaming silencioso|La joya del oficio: del wifi a los datos sin que el sobre caiga. El candado
que no sabe de aceras.

AllowedIPs|La lista del casillero: qué viajes van por el sobre y cuáles no. El routing
criptográfico del candado — la llave que también es dirección.

Cryptokey routing|El oficio del candado: la llave pública ES la dirección del otro extremo. Si
la firma no cuadra, la puerta ni se abre.

Handshake|La firma de cada dos minutos: el sobre renueva su llave mientras el barrio ni se
entera. La cerradura que rota caminando.

Noise IK|El traje cosido del protocolo: el diseño de firmas fijas de WireGuard. Sin negociación
— menos puertas que dejar abiertas.

Curve25519|La firma de las llaves del sobre: la curva del SSH de la 27, firmando el viaje del
barrio.

ChaCha20-Poly1305|El sello del sobre: el par de cifrado y huella que lleva la carta dentro del
viaje. Rápido en el bolsillo, firme en la auditoría.

BLAKE2s|La huella del candado: el resumen que firma el protocolo de una vez, sin cambios de
algoritmo.

Kernel 5.6|La corona de 2020: el kernel de Linux abrazó el candado completo — la primera vez que
un protocolo de VPN nuevo entró de una pieza.

Mirror|La placa honesta del censo: el espejo de GitHub del candado — el hogar de verdad vive en
git.zx2c4.com, la casa de Donenfeld. La letra chica que la forja firma.

Donenfeld|Jason Donenfeld, el forjador del sobre: el que se preguntó en 2015 qué pasaría si la
criptografía no se negociara. Cuatro mil líneas después, el kernel le firmó la casa.

wireguard-go|El motor en Go del censo (★4.453, pulso 16-oct-2026, MIT): el candado fuera del
kernel — el que mueve el sobre en los bolsillos sin kernel propio.

boringtun|El motor en Rust de Cloudflare (★7.221, pulso 16-oct-2026, BSD-3): la copia de la
fábrica grande — la prueba de que el protocolo es tan pequeño que una empresa lo re-escribe por
gusto.

wireguard-tools|Los palos del oficio (★728, pulso 16-oct-2026, GPL-2.0): `wg` mira el túnel por
dentro, `wg-quick` lo enciende con una línea. La mesa de la consola.

Site-to-site|El túnel entre dos casas: los dos colmados del caso tres hablando como si
estuvieran en la misma sala. El alambre del negocio, sin línea privada.

Captive portal|El portal del recinto: registra la primera conexión y bloquea el resto. El sobre
va DESPUÉS del portal — como debe ser.

Coordinador|El conserje de la malla: reparte direcciones y llaves públicas — los datos jamás
pasan por él. La letra chica de la comodidad, leída antes de firmar.

Headscale|El coordinador libre: la misma malla con el conserje en tu sala. Prometido pa la fila
51-60 — la vara completa de la malla.

Cebolla|La otra mudanza (la 31): el anonimato repartido entre voluntarios, pagado en lentitud.
El sobre muda la confianza al sitio que eliges; la cebolla la reparte entre extraños firmes.

MTU|El número fino del sobre: el tamaño que pasa por la acera. Si el roaming se cae, bajarla dos
dedos — la cirugía del alambre.

Política de registros|La letra que importa: el compromiso escrito de la salida ajena sobre lo
que guarda. La confianza que se documenta es la única que dura.

IP extranjera|La desconfianza del banco lejano: la dirección del otro lado del mar que traba la
cuenta. El sobre a la casa de la familia la resuelve — el caso cuatro de la pieza.

Sobre blindado|El nombre de la casa pa el paquete cifrado completo: pregunta, carta y caserón
dentro. La mudanza que el café no lee.

Acera|El suelo ajeno: el wifi que no administra tu casa. El sobre se usa ahí — y se apaga al
llegar a la puerta.

Interruptor con nombres|La lista de la confianza: «Casa», «Trabajo», «Nube». El menú que la
forja recomienda — la administración hecha pantalla.

Pan del vecino|La confianza del dueño conocido: no amarra al router. El sobre protege el viaje
de los dos — la caja del café incluida.

Nafta de las llaves|El reparto del caso seis: a cada chófer su llave, EN su aparato. La llave de
la casa jamás se fotocopia — se reparte como la nafta: a cada uno, la suya.

Isla en el bolsillo|La del caso cuatro: el sobre a Santo Domingo desde Nueva York. El banco ve
el barrio de siempre — la mudanza al revés.

Caridad del aire|La del templo: el wifi abierto amarrado con el sobre propio. La congregación
viajando cerrada — la puerta del templo, abierta igual.

Traje cosido|El del candado: criptografía fija de fábrica, sin negociación. Menos puertas que el
vestido a la medida de las suites viejas.

Conserje|El de la malla: reparte llaves y direcciones sin leer las cartas. La comodidad que se
paga en confianza ajena — hasta que el coordinador libre llegue.

Corona del kernel|La de 2020: el Linux abrazando el candado de una pieza. El sello que ninguna
tienda de VPN puede comprar.

Cerrojo del sobre|El kill switch con nombre de la casa: sin sobre, sin viaje. El seguro que se
arma en cinco minutos y paga todas las lluvias.

Torre cosida|La genealogía del candado: del modem a la malla en tres generaciones. La idea que
no cambió: la confianza muda de sitio cuando el viaje se cierra.

Vara del mostrador|La de esta pieza: el sobre se usa donde el suelo es ajeno. La herramienta con
horario — el estilo de vida es la casa mandando.

Política de la casa|La de la salida propia: quién mira el registro de la raspberry, y pa qué. La
salida sin reglas escritas es la salida ajena con otro dueño.

Prueba de las tres puertas|La del piso cinco: el IP, el faro y la acera. Las tres pasan — el
sobre queda firmado. Una falla: media hora de taller.

Mercado del miedo|El de las VPN de escaparate: miles de millones vendiendo la sombra del sobre.
El barrio con placa del censo tiene lo que el anuncio finge — protocolo, salida y doctrina.

Alambre del negocio|El del caso tres: dos colmados, un túnel. Las cajas hablando como vecinas —
la línea privada, jubilada con dignidad.

*🗓 EL RITUAL DE SIETE DÍAS (del wifi del extraño al sobre de la casa)*

*Día uno — el interruptor.* Instala la app del censo. Mira el interruptor vacío sin ansiedad: el
mueble sin salida es honesto — no conecta a nada porque nada vende. Lee la receta del piso 2 con
el café de la mañana.

*Día dos — la salida.* Decide tu vara: la raspberry de la casa (piso 2) o la malla con empleados (la segunda fila, con la letra chica). El que pueda: el piso 2. El que no: la salida ajena CON política leída — y anota la fecha en que la leíste.

*Día tres — la firma.* Genera las llaves en el aparato (jamás en la mesa ajena), firma los dos
archivos, abre el puerto en el router. La tarde del alambre: una vez en la vida, repetida nunca.

*Día cuatro — el seguro.* El kill switch del piso 4. Cinco minutos que valen todas las lluvias
del año.

*Día cinco — la prueba de las tres puertas.* La del IP (¿dice tu casa?), la del faro (¿el índice sale por tu sala?), la del roaming (¿aguanta la acera?). Las tres pasan: el sobre está firmado.

Una falla: el registro del taller, media hora de arreglo.

*Día seis — el barrio por nombres.* Nombra los túneles como los sitios de tu confianza: «Casa»,
«Trabajo», «Nube». El interruptor se lee como una lista — la administración de la confianza,
hecha menú.

*Día siete — la Familia al completo.* Enciende el faro (la 42) y el candado juntos: el índice contestado por tu salida, el caserón viajando en sobre. La pareja del aire completa: pregunta y viaje, las dos mudanzas de la casa.

Y escribe en la página del taller la fecha de la firma — la casa que se documenta, se defiende.

*La regla del túnel:* el sobre se usa cuando el suelo es ajeno — y se apaga cuando llegas a
casa. La herramienta no es el estilo de vida: el estilo de vida es la casa mandando.

*📎 LOS APÉNDICES DEL TÚNEL (lo que queda de la noche)*

Apéndice A — el mapa del viaje, al corte. La fila del aire en tres mudanzas: la ventana (la 41)
mostró sin reportar; el índice (la 42) viajó en sobre cerrado; el caserón (esta pieza) muda el
viaje entero.

Tres faenas que se encadenan: la misma pregunta — ¿en quién confía mi casa hoy? — contestada
tres veces con la misma vara: placa, ley, y frontera honesta.

Apéndice B — las cinco preguntas del mostrador, en una línea. ¿Qué hace?

Mete el viaje entero en un sobre de cuatro mil líneas. ¿Qué no hace?

No te hace anónimo — muda la confianza. ¿Cuánto cuesta?

Nada: protocolo libre, app Apache, salidas propias. ¿Cuánto tarda?

Diez minutos el interruptor, una tarde la salida propia. ¿Y si se cae?

El kill switch calla el teléfono hasta que el sobre vuelve.

Apéndice C — la página en blanco. La que la forja deja abierta a propósito: la dirección de TU
salida (¿la tienes?

¿la contrataste? ¿la leíste?).

Esa respuesta — la tuya, fechada en tu taller — vale más que las cinco placas del censo: es la
vara midiendo TU confianza. La obra no termina en la lectura: termina cuando el interruptor del
barrio dice «Casa».

Apéndice D — la sala de los errores. Las tres fallas posibles y su salida.

Si el túnel no conecta: el puerto del router (el alambre del piso 3) es el sospechoso de siempre
— media hora de registro. Si el roaming se cae: la MTU del sobre (el número fino del oficio) —
bajarla dos dedos y el sobre pasa por la acera.

Si la batería sufre: repasa el casillero del faro (la pareja del aire se turna; si pelean, exime
al faro en la app del candado).

Apéndice E — la fila que viene.

La 44 tiende el alambre (la sincronía de la casa: el teléfono, la laptop y la familia con los mismos archivos — prometida desde la 36); la 45-50 completa el bloque de REDES con los muebles que faltan pa la casa al aire

y la fila 51-60 hornea el taller propio (la salida en la nube, el coordinador libre de la malla — la vara completa del túnel, servida en bandeja propia).

La casa no improvisa: programa. Y la noche firma: el viaje de la casa, cada vez más de la casa.

*🎯 EL MINIQUIZ DEL TÚNEL*

*LAS PREGUNTAS:*

*1.* ¿Qué muda el túnel que el faro de la 42 no movió?

*2.* ¿Cuántas líneas tiene el candado moderno — y qué firmó el kernel en 2020?

*3.* ¿Quién ve tu índice dentro de un túnel ajeno?

*4.* ¿Qué es la malla de Tailscale, en una línea de la forja?

*5.* ¿El túnel encendido en tu propia casa, pa qué sirve?

*Respuestas al revés (léelas de atrás para adelante):*

REV|.otnup ed adum ejaiv lE .ecidní le olos on :otelpmoc nóresac le — aretne y acreC

REV|.6.5 nóisrev al ne otelpmoc ózarba ol xuniL ed lenrek le y — saeníl lim ortauc ed acreC

REV|.aznadum :on ,otaminonA .néiuq a segile út — adilas al artsinimda neiuQ

REV|.retuor le racot nis ,alos amra es euq asac al ed der al :ejresnoc noc drauGeriW

REV|.oneja se oleus le ednod adnam atneimarreh al :olagápa — adan araP

*💌 LAS CARTAS AL LECTOR*

*PRIMERA CARTA — al que usa el wifi del café todos los mornings.* El router del café es de la casa del café: la contraseña de la pizarra no compra nada más que la entrada. Tu banco, tu correo y tus fotos pasan por allá.

El sobre de esta pieza existe exactamente pa esa acera: enciende el «Café», y el extraño ve humo. Diez minutos de interruptor — la acera entera, callada.

*SEGUNDA CARTA — al taller de la salida.* El que monta salidas pa el barrio (la raspberry del caso uno, el colmado de la abuela del caso cuatro): tu faena es la vara completa de la doctrina — la confianza que la gente te presta, se administra con placa, con fecha y con la política escrita en la pared. El día que la salida dude, dilo tú primero.

La forja te firma: el taller honesto es el mueble más raro y más caro del mercado — y el barrio
lo sabe cuidar.

*TERCERA CARTA — al que todavía cree en el tigre del anuncio.* La VPN de la estrella que promete invisibilidad: mándale esta pieza. Si su salida tiene política escrita, la usarás con letra chica; si solo tiene tigre, el tigre no firmó el sobre.

El anonimato no se vende por suscripción — y la confianza jamás por anuncio.

La casa manda: placa, ley, y el interruptor que dice «Casa».

*🪡 LA ÚLTIMA AGUJA (cosida al pie, como la casa cose)*

Si esta pieza sirvió para algo más que leer, fue para esto: dejar escrito que el viaje de la casa tiene sobre con placa — WireGuard ★1.640 (pulso 16-oct-2026) y su familia de cuatro leyes: el candado que el kernel abrazó, los tres motores que lo copiaron, y la doctrina que ningún anuncio va a contar — la confianza se muda, se administra y se firma

jamás se canta.

La forja lo midió con el pulso del mismo día en que nace esta pieza, y lo firma: el café ve
borrón, el operador ve borrón, y el índice lo contesta tu sala — la tercera mudanza del aire,
cosida con las cuatro mil líneas más firmes del barrio.

Enciende el interruptor. Arma el seguro.

Prueba las tres puertas. Y cuando el anuncio del tigre prometa invisibilidad por suscripción,
recuerda: tu sobre ya viaja cerrado — porque la salida es tuya, y la casa manda.

Eso no lo canta la tienda: se firma con Apache, y se administra en el mostrador de tu sala.

───────────────────

#LaBandita #ElTunel #WireGuard #VPN #FOSS #DominicanoES

───────────────────

💓 *PULSO 29-OCT-2026 — verificación profunda de La Bandita (pieza 43).*

Alcance de esta nota: se re-verificaron el 29-oct-2026 los repos y enlaces atribuidos a esta
pieza: 4 repos GitHub confirmados. La historia original no se reescribe: conserva su fecha y su
texto; esta nota solo añade el estado medido hoy.

Actividad medida hoy: 1 con actividad hoy · 1 en 7 días · 0 en 30 días · 1 en 180 días · 1
dormidos · 0 archivados.

*Alertas de continuidad (verificadas el 29-oct-2026):*

• `wireguard/wireguard-android` — dormido · última actividad 2026-03-17 · ★1.656 (verificado 29-oct-2026). Queda como historia/medición, no como recomendación fresca.

*Placas de control (selección por actividad reciente y juventud, no por fama):*

• `tailscale/tailscale` — ★38.289 (verificado 29-oct-2026) · última actividad 2026-10-29 · BSD-3-Clause · release v1.104.4 (2026-10-28).

• `tailscale/tailscale-android` — ★2.753 (verificado 29-oct-2026) · última actividad 2026-10-28 · BSD-3-Clause · release v1.104.4 (2026-10-28).

• `cloudflare/boringtun` — ★7.237 (verificado 29-oct-2026) · última actividad 2026-06-15 · BSD-3-Clause.

• `wireguard/wireguard-android` — ★1.656 (verificado 29-oct-2026) · última actividad 2026-03-17 · Apache-2.0.

Enlaces web: esta pieza no trae URL explícitas fuera de los repos citados; su verificación es la
de los repos de arriba y la del universo del censo cuando cita agregados.

Vara de cierre: futuro y actividad comprobable antes que aplauso. Si un repo deja de empujar, la
próxima foto lo dirá con fecha; si nace una rama viva, entrará por la misma puerta: fuente,
fecha y pulso.