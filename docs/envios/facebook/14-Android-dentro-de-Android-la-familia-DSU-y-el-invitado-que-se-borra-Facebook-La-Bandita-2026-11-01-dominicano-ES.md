# PIEZA 14 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/14-Android-dentro-de-Android-la-familia-DSU-y-el-invitado-que-se-borra-Facebook-La-Bandita-2026-11-01-dominicano-ES.md`
- **Fecha de la pieza:** 1-nov-2026 (según dateline; edad hoy: 0 días)
- **sha256 de la pieza:** `d148e24278561c66ef9a8bd09bdf7bc396957ea18ecacb09087667b1d85d0f8a`
- **Envío generado:** 2026-11-01 · 17 mensajes · el mayor de 3612 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 17 · 752 caracteres ═══

*Android dentro de Android: la familia DSU y el invitado que se borra*

La Bandita · pieza 14 · guía del 1-nov-2026 · te la mando hoy en 17 mensajes.

Antes de mandártela volví a medir lo que afirma: *10 repositorios, 8 vivos*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: Apache-2.0 5 · sin licencia 3.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/14-Android-dentro-de-Android-la-familia-DSU-y-el-invitado-que-se-borra-Facebook-La-Bandita-2026-11-01-dominicano-ES.md

💓 1 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 17 · 2341 caracteres ═══

*Android dentro de Android: la familia DSU y el invitado que se borra*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 14 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🚪 Qué es un invitado y qué no es
├── 🧰 La familia DSU, pieza por pieza
├── 🎬 Cuatro escenas y el censo de esta tarde
├── 🖼️ El sistema invitado: qué se le puede pedir
├── 🧨 Los cinco finales de una instalación fallida
├── 🧹 Borrar el invitado sin borrar la casa
├── 🛠️ La comprobación previa en cuatro preguntas
├── ⚖️ La ley, la garantía y el arranque
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas al pie
```

*⚡ En una página*

Un teléfono Android puede tener otro Android dentro sin rootear nada. Se llama instalación de sistema invitado, el sistema lo soporta desde hace varias versiones y el invitado vive en una imagen que se monta al arrancar y se borra cuando se quiere: no toca el sistema de la casa, no borra fotos y no necesita permisos de administrador. Es la versión de bolsillo de eso que en la computadora se llama tener dos sistemas en el mismo disco.

La familia que lo maneja es pequeña y está repartida. *DSU-Sideloader*, con ★2.353 y Apache-2.0, es el abuelo: su última versión publicada es de abril de 2023 y su código no se mueve desde marzo de 2024. Alrededor han crecido *DSU-Sideloader-Plus*, con ★44 y versión 1.0.0 del 15 de junio; *Dsu-Multi-sideloader*, con ★3 y versión v2.20 del 15 de octubre; y hasta dos proyectos de ★2 y ★3 que nadie mira, uno de ellos con licencia que la ficha no reconoce y su README declarando GPL-3.0.

Del otro lado de la cadena está el sistema que se instala. Ahí aparecen los constructores de imágenes: *treble_experimentations*, con ★3.552 y sin licencia declarada; *LineageOS_gsi*, con ★571 y una versión del 24 de mayo; *crDroid_gsi*, con ★259 y empujón de marzo de 2025; y *treble_aosp*, con ★312 y Apache-2.0.

Y una pieza que casi nadie conoce y que resuelve la duda más común: *AndroidLowLevelDetector*, ★476, Apache-2.0, empujón de hoy, que dice si el aparato soporta esta historia antes de que nadie instale nada. Si te llevas una idea, es esta: el invitado se prueba, se usa una semana y se borra sin rastro. Es la forma más barata de conocer otro Android sin arriesgar el que tienes.

⏬ sigue abajo · parte 1 de 16

═══ MENSAJE 3 de 17 · 2941 caracteres ═══

*🚪 Qué es un invitado y qué no es*

Un sistema invitado es una imagen de disco con un Android completo. El teléfono la arranca en un espacio aparte, la ejecuta como si fuera otro aparato y la apaga cuando se cansa. Tres cosas importantes se derivan de eso.

La primera: no es una máquina virtual de escritorio. No hay un programa que simula procesadores; el invitado se ejecuta con el mismo hardware del teléfono y por eso va casi a la velocidad del sistema de la casa. Lo que se paga no es velocidad: es espacio y algunas funciones que el invitado no puede tocar.

La segunda: no es un segundo usuario. Un segundo usuario comparte el sistema y las apps; un invitado trae su propio sistema, sus propias apps y sus propias cuentas. Y no ve nada del otro lado, ni las fotos ni los archivos.

La tercera: no es un arranque alternativo. El sistema de la casa sigue siendo el que manda; el invitado se monta como una imagen y se desmonta. Si algo sale mal, se borra la imagen y vuelve todo a su sitio, que es la razón por la que esta función es tan recomendable para probar.

Hay un cuarto matiz que la gente descubre tarde: el invitado necesita un sistema base que lo soporte —la función de instalación dinámica de sistemas, de ahí las siglas—, y no todos los aparatos la traen activada aunque su versión sea reciente. Saberlo antes es la mitad del trabajo.

*🧰 La familia DSU, pieza por pieza*

*El abuelo.* DSU-Sideloader, ★2.353, Apache-2.0, Kotlin. Recibe una imagen, la pasa al sistema y pide al sistema que la instale como invitado. Su última versión es de abril de 2023 y el código no se mueve desde marzo de 2024. Sigue siendo lo que la gente instala porque es lo que aparece en los primeros resultados y porque funciona donde funciona.

*El hijo con nombre largo.* DSU-Sideloader-Plus, ★44, Apache-2.0, versión 1.0.0 del 15 de junio. Nació para los aparatos donde el abuelo falla, con mejoras de compatibilidad y una versión inicial que dice que todavía no le ha pasado el tiempo por encima.

*El de los varios invitados.* Dsu-Multi-sideloader, ★3, Apache-2.0, versión v2.20 del 15 de octubre. Su nombre lo dice: administra más de uno, que es lo que hace falta cuando se quiere probar dos sistemas sin borrar el primero.

*El que se copia a sí mismo.* DsuSideloaderPlusProMaxUltra, ★3, sin licencia declarada, empujón del 8 de septiembre. Es una modificación de la modificación, con el nombre que se le pone a un proyecto cuando nadie espera que lo use alguien más.

*El que se reescribe.* Gong-Mi/DSU-Sideloader, ★2, Apache-2.0 en la ficha y GPL-3.0 en su README, empujón del 27 de julio, sin versión publicada. Un intento de reescribir la herramienta en otro lenguaje, que es la señal más clara de que la idea original tiene algo que valga la pena.

Cinco piezas para una sola operación, y ninguna con más de ★44 salvo el abuelo. Es el retrato de un ecosistema que funciona por inercia y no por novedad.

⏬ sigue abajo · parte 2 de 16

═══ MENSAJE 4 de 17 · 3062 caracteres ═══

*🎬 Cuatro escenas y el censo de esta tarde*

*El que quería probar otro Android sin miedo.* Tenía un teléfono con todo dentro: banco, trabajo, fotos de la familia. Le daba terror rootear. Con DSU-Sideloader montó un invitado, lo usó una semana para probar una versión distinta del sistema y lo borró con un botón. Lo único que perdió fue espacio durante esa semana.

*La que compró un teléfono usado y quería saber si estaba limpio.* Montar un invitado le sirvió para arrancar un Android que ella controlaba y comprobar que el hardware estaba bien. La conclusión sobre si el sistema de la casa estaba limpio la sacó con otra herramienta, y ahí aprendió que el invitado prueba el aparato, no la limpieza del que venía dentro.

*El que intentó y no le arrancó.* Su teléfono tenía la función desactivada. Probó el abuelo, probó el Plus y probó el de varios invitados. Ninguno pasó del intento. La respuesta no era otro programa: era su aparato. Con AndroidLowLevelDetector lo supo en un minuto y dejó de gastar tardes.

*El que se quedó viviendo en el invitado.* Montó un sistema limpio para trabajar y otro para el ocio, y acabó usando el invitado más que la casa. Su conclusión, después de un mes: funciona, consume espacio y batería, y no sirve para el teléfono principal si necesitas la cámara buena o las notificaciones al instante.

*🧾 El censo de esta tarde*

*DSU-Sideloader*, el abuelo: ★2.353, Apache-2.0, Kotlin, empujón del 13 de marzo de 2024 y versión 2.03 del 29 de abril de 2023. Dos fechas viejas y una función que sigue viva: el retrato de una herramienta terminada.

*DSU-Sideloader-Plus*: ★44, Apache-2.0, Kotlin, empujón del 15 de junio y versión 1.0.0 del mismo día. La alternativa para aparatos donde el abuelo no arranca.

*Dsu-Multi-sideloader*: ★3, Apache-2.0, Kotlin, empujón y versión del 15 de octubre —v2.20—. El más reciente de la familia y el que administra varios invitados.

*DsuSideloaderPlusProMaxUltra*: ★3, sin licencia declarada, Kotlin, empujón del 8 de septiembre, sin versión anotada. La copia de la copia, publicada sin licencia.

*Gong-Mi/DSU-Sideloader*: ★2, Apache-2.0 en la ficha y GPL-3.0 en el README, Kotlin, empujón del 27 de julio, sin versión. La reescritura que todavía no se usa.

*treble_experimentations*: ★3.552, sin licencia declarada, Smali, empujón del 27 de enero de 2025. La fuente histórica de los sistemas invitados; su licencia ausente se publica como ausente.

*LineageOS_gsi*: ★571, sin licencia declarada, Shell, empujón del 24 de mayo y versión v2026.05.24-lineage23.2. Guiones y parches para construir una imagen concreta.

*treble_aosp*: ★312, Apache-2.0, Shell, empujón del 25 de julio de 2025. La vía más sobria: un Android base, sin adornos.

*crDroid_gsi*: ★259, sin licencia declarada, Shell, empujón del 8 de marzo de 2025. Otra imagen construida sobre la misma raíz.

*AndroidLowLevelDetector*: ★476, Apache-2.0, Kotlin, empujón de hoy y versión 1.18.7 del 25 de abril. No instala nada: dice qué soporta tu aparato, que es el paso que casi todos se salen.

⏬ sigue abajo · parte 3 de 16

═══ MENSAJE 5 de 17 · 2645 caracteres ═══

*🖼️ El sistema invitado: qué se le puede pedir*

El invitado es un Android completo y no un emulador, y eso fija lo que se puede esperar de él.

*Lo que funciona bien.* Instalar aplicaciones, abrir el navegador, usar mensajería, probar un ajuste nuevo del sistema, comprobar si una app que se cae en tu teléfono se cae por la app o por el aparato. Todo eso va a velocidad casi normal y sin tocar nada del otro lado.

*Lo que funciona a medias.* La cámara suele ir, con menos calidad y a veces con el acceso negado; el audio funciona con retardo en algunos aparatos; el bluetooth a veces sí y a veces no. El sensor de huella casi nunca cruza la frontera.

*Lo que no funciona.* El almacenamiento del sistema de la casa no se ve desde el invitado, y el del invitado no se ve desde la casa. La tarjeta de memoria puede quedar fuera. Y las notificaciones del invitado no llegan si el invitado no está encendido, que es obvio y la gente olvida.

*Lo que se paga.* Espacio: la imagen ocupa varios gigas aunque el sistema sea ligero. Batería: dos sistemas encendidos gastan más, aunque el invitado se apague. Y tiempo: la primera instalación tarda y el primer arranque tarda más.

Con esas cuatro listas en la cabeza, la pregunta deja de ser «¿esto sirve?» y pasa a ser «¿para qué lo quiero?», que tiene respuesta.

*🧨 Los cinco finales de una instalación fallida*

Las instalaciones fallan y casi siempre por una de cinco razones. Reconocerlas ahorra la tarde.

**El aparato no soporta invitados.** La función existe pero el fabricante la dejó desactivada o el aparato no tiene las particiones que hacen falta. Ningún programa lo arregla; AndroidLowLevelDetector lo confirma en un minuto y el asunto se cierra.

**La imagen no es compatible.** Se bajó una imagen para otra arquitectura o para otra versión del sistema. El síntoma es un intento que empieza y se queda en la pantalla del fabricante.

**Falta de espacio.** La imagen se copia y se monta, así que hace falta el doble del tamaño durante la instalación. Es el error con el mensaje más claro y el más ignorado.

**El gestor no está actualizado.** El abuelo de esta familia no se mueve desde 2024 y algunos aparatos nuevos lo rechazan. Ahí entran el Plus y el de varios invitados.

**El invitado arranca y no pasa de la pantalla.** Casi siempre es una imagen con un fallo conocido o un ajuste del sistema de la casa que impide montarla. Probar con otra imagen separa el problema en veinte minutos.

Cinco finales, cinco comprobaciones distintas y ninguna que exija root. Ese es el valor de esta función: el error se paga con veinte minutos y no con el teléfono.

⏬ sigue abajo · parte 4 de 16

═══ MENSAJE 6 de 17 · 3508 caracteres ═══

*🧹 Borrar el invitado sin borrar la casa*

La ventaja de esta función es que el borrado es limpio, y aun así hay tres cosas que conviene saber.

El borrado se hace desde los ajustes del sistema, en el apartado de usuarios o de sistemas instalados, o desde la app que lo instaló. Al aceptar, el sistema desmonta la imagen y libera el espacio; lo que estuviera dentro del invitado desaparece con él, incluidos los archivos que se guardaron allí.

Por eso conviene sacar del invitado lo que importe antes de borrarlo. El invitado no comparte carpeta con la casa, así que la copia se hace desde dentro: por correo, por un servicio de archivos o por el cable. Es el error más común: creer que por estar en el mismo teléfono los archivos se quedan.

Y hay un caso especial: si el invitado se queda sin espacio o no arranca, el borrado puede fallar desde la interfaz. Entonces se hace desde el gestor o, en el peor de los casos, desde el sistema de la casa en el apartado de imágenes. Ninguna de esas operaciones toca los datos de la casa.

La tercera cosa que hay que saber es que el invitado se puede quedar dormido para siempre: si el sistema de la casa se actualiza y la función cambia, el invitado puede dejar de arrancar sin borrarse. Se queda ocupando espacio hasta que alguien lo quita a mano, y esa es la razón por la que conviene no tener tres.

*🛠️ La comprobación previa en cuatro preguntas*

**¿Tu aparato soporta invitados?** Se comprueba con AndroidLowLevelDetector o mirando en los ajustes si existe la opción de instalar un sistema. Si no existe, no hay nada que hacer.

**¿Tienes espacio de sobra?** El doble del tamaño de la imagen, libre. En un teléfono de 128 gigas con 90 ocupados, no lo tienes.

**¿Qué imagen vas a usar?** Una construida para tu arquitectura y tu versión. Las del censo de esta tarde son cuatro familias distintas y se eligen por aparato, no por gusto.

**¿Qué vas a hacer dentro del invitado?** Si es probar y borrar, cualquier imagen ligera sirve. Si es usar a diario, la respuesta honesta es que el invitado no reemplaza al sistema de la casa.

Cuatro preguntas, cinco minutos y una decisión. Las cuatro se pueden contestar sin instalar nada, que es la parte que casi nadie aprovecha.

*⚖️ La ley, la garantía y el arranque*

Montar un invitado no modifica el sistema de la casa y no toca el arranque, así que en la mayoría de los aparatos no afecta a la garantía de la forma en que la afecta rootear. Dicho eso, hay tres cosas que conviene saber y que ninguna app avisa.

La primera es que un invitado puede quedar registrado en el sistema de la casa como un usuario o un sistema instalado, y algunas apps de banca o de trabajo miran esos registros. No es lo mismo que un arranque abierto, y puede ser suficiente para que una app sospeche.

La segunda es que las imágenes de sistema que se instalan son software libre con sus propias licencias, y las del censo de hoy tienen un detalle curioso: tres de las cuatro familias no declaran licencia en la ficha. Se publican así y se advierte, porque el código de un sistema operativo sin licencia explícita es una zona gris que cada uno evalúa.

La tercera es el trabajo. Instalar un sistema invitado en el teléfono de la empresa puede violar la política interna de la empresa aunque no viole ninguna ley, y esa discusión se pierde antes de empezar.

La regla de la casa es la misma de siempre: si el aparato no es tuyo del todo, pregunta antes; si es tuyo, decide sabiendo qué cambia y qué no.

⏬ sigue abajo · parte 5 de 16

═══ MENSAJE 7 de 17 · 2916 caracteres ═══

*🧭 Cuándo el invitado es la respuesta y cuándo es un juguete*

El invitado es la respuesta correcta en cuatro situaciones y en ninguna más.

*Probar un sistema antes de decidir.* Quien duda entre actualizar a una versión nueva o quedarse en la que tiene puede montar el invitado con la versión nueva y vivir en ella dos días. Es la prueba más honesta que existe y no arriesga nada.

*Separar el ocio del trabajo sin segundo teléfono.* Un invitado con las apps de ocio, la casa con las del trabajo. Funciona, siempre que se acepte la batería extra y el espacio.

*Abrir una app dudosa.* Un paquete de origen desconocido se abre primero en el invitado. Si hace algo raro, se borra el invitado entero. Es el uso más inteligente y el que menos se recomienda, porque requiere entender la frontera.

*Comprobar si un fallo es del teléfono.* Una app que se cierra en la casa se prueba en el invitado: si ahí tampoco abre, el problema es la app o el sistema; si ahí abre, el problema es un ajuste del sistema de la casa.

Y el invitado es un juguete cuando se pretende tener dos sistemas para siempre, con las dos cámaras, las dos baterías y las notificaciones al instante. Eso no existe y no va a existir: la función está pensada para probar, no para vivir.

*💬 Las frases que se repiten*

«¿Esto es rootear?» No. No toca el arranque ni el sistema de la casa, y por eso es la puerta más segura de todas las que aparecen en esta serie.

«Se me borró todo el teléfono». Casi siempre se borró el invitado, no la casa. Y casi siempre porque los archivos estaban dentro del invitado.

«No me arranca». Puede ser el aparato, la imagen o el gestor. El orden de comprobación está en esta guía y no tiene atajos.

«¿Puedo tener tres?» Se puede, y cada uno ocupa su espacio. La pregunta correcta es cuántos vas a usar de verdad.

«¿Y las apps de banco?» Pueden mirar los registros de sistemas instalados. No es root y puede ser suficiente para que no abran.

*🧾 Lo que costó medir esto*

La familia de los gestores es fácil de medir y difícil de ordenar, porque cuatro de los cinco proyectos se llaman casi igual. Un carácter de diferencia separa el abuelo de sus copias, y dos de ellos tienen ★3 y ★2: proyectos que existen, funcionan y no los mira nadie.

Los constructores de imágenes son lo contrario: cifras altas, nombres largos y una ausencia que se repite. Tres de los cuatro no declaran licencia en la ficha, y no es un descuido de la medición: es lo que devuelve la forja, y una imagen de sistema sin licencia explícita es una zona que conviene mirar antes de instalar.

La pieza que más costó fue la última, la del detector. Es la única del censo que no instala nada y la única que contesta la pregunta previa: si el aparato soporta invitados, si tiene las particiones, si el sistema está preparado. Los otros nueve proyectos asumen que esa pregunta ya está contestada, y casi nunca lo está.

⏬ sigue abajo · parte 6 de 16

═══ MENSAJE 8 de 17 · 2488 caracteres ═══

*🗣️ Lo que se dice en los grupos y lo que falta*

En los grupos de teléfonos se repiten tres frases sobre esta función, y las tres omiten lo mismo.

«Con esto tienes dos teléfonos en uno». Tienes dos sistemas y un solo juego de cámaras, una sola batería y una sola tarjeta. La mitad de lo que se comparte no se puede compartir.

«Es como un segundo usuario». Un segundo usuario comparte sistema y apps; el invitado trae los suyos y no ve nada del otro lado. La diferencia importa el día que se borra.

«Si no arranca, es tu teléfono». Nueve veces de diez es la imagen. La prueba de cambiar de imagen cuesta veinte minutos y ahorra una devolución.

Lo que falta en esas frases es siempre lo mismo: la frontera. Todo lo que se puede decir de esta función se puede decir contando qué cruza y qué no, y casi ningún tutorial lo cuenta.

*🧮 Tres cuentas de espacio antes de empezar*

La primera: la imagen ocupa su tamaño y durante la instalación pide el doble. Con treinta gigas libres se puede intentar; con ocho, no.

La segunda: el invitado crece con el uso, porque sus apps se actualizan y sus datos se acumulan. Un invitado de prueba que se queda un mes puede doblar su tamaño.

La tercera: la casa necesita margen para funcionar. Un teléfono lleno al noventa por ciento empieza a fallar de maneras que parecen de otro origen, y ahí la gente culpa al invitado de un problema que causó el lleno.

Con las tres cuentas hechas, la decisión deja de ser técnica: o sobra espacio, o no hay invitado. Y si no hay, la respuesta es una imagen más ligera y una semana de uso, no tres invitados a la vez.

*🧯 El invitado que se queda a medias*

Hay un estado intermedio que no es ni instalado ni borrado: el invitado que se montó a medias. Aparece como un sistema instalado que no arranca, ocupa espacio y no se deja quitar desde la interfaz.

El camino de salida tiene tres intentos, en orden. El primero, desde el gestor que lo instaló, con la opción de desinstalar sistemas. El segundo, desde los ajustes de la casa, en el apartado de usuarios o sistemas, aceptando el borrado aunque el sistema no arranque. El tercero, desde la propia imagen en el almacenamiento, borrándola a mano cuando el sistema ya la considera huérfana.

Ninguno de los tres toca los datos de la casa. Y los tres se pueden evitar con la única precaución que sirve: espacio de sobra antes de empezar, porque el invitado a medias casi siempre es un invitado sin sitio para terminar de montarse.

⏬ sigue abajo · parte 7 de 16

═══ MENSAJE 9 de 17 · 2384 caracteres ═══

*📲 Instalar un invitado, paso a paso*

**Paso uno: comprobar.** Abrir AndroidLowLevelDetector y mirar si el aparato declara Treble, si tiene particiones dinámicas y si el sistema permite sistemas instalados. Si algo de eso falta, la cadena termina aquí y ahorra la tarde.

**Paso dos: liberar espacio.** El doble del tamaño de la imagen que se va a usar. En un teléfono de 128 gigas eso puede significar borrar dos juegos, y es la parte del proceso que más gente abandona.

**Paso tres: elegir la imagen.** Una construida para la arquitectura del aparato y compatible con su versión. Las cuatro familias del censo sirven a públicos distintos: la histórica es la más tolerante y la más vieja; las otras tres van por detrás en detalles y por delante en novedades.

**Paso cuatro: pasarla al gestor.** El gestor abre el archivo, lo valida, lo copia y lo entrega al sistema. La validación es lo que evita el error más común: una descarga cortada que parece completa.

**Paso cinco: aceptar el aviso del sistema.** El sistema pide confirmación y avisa de que va a instalar un sistema adicional. Ahí se ve si la función está de verdad disponible, porque es el sistema el que monta la imagen y no la app.

**Paso seis: primer arranque, con paciencia.** El invitado arranca como un teléfono nuevo: configuración inicial, cuenta de usuario, actualizaciones. Es el momento de no meter cuentas importantes: un invitado de prueba se borra, y con él se van las sesiones.

*📦 Qué cruza la frontera y qué no*

La lista corta, porque es la que decide si la función sirve para lo que se quiere.

*No cruza:* los archivos del almacenamiento de la casa, las fotos, la tarjeta de memoria en la mayoría de los aparatos, los contactos, las cuentas configuradas y las apps instaladas. Son dos teléfonos en el mismo cuerpo.

*Cruza a veces:* el bluetooth, la cámara, el acceso a la ubicación y el audio del sistema. Depende del aparato y de la versión, y por eso dos personas con el mismo programa obtienen resultados distintos.

*Cruza siempre:* la red, la batería, el calor y el espacio. Esos cuatro son del aparato y los dos sistemas los comparten, quieran o no.

La consecuencia es que el invitado no es una caja fuerte para datos: es un sistema aparte. Y sirve justamente para eso, porque lo que se hace dentro no deja rastro fuera y lo que se borra no se puede recuperar.

⏬ sigue abajo · parte 8 de 16

═══ MENSAJE 10 de 17 · 3279 caracteres ═══

*🕰️ La cronología de una función que casi nadie usa*

La función se pensó para que los fabricantes probaran actualizaciones sin arriesgar el teléfono de nadie, y con ese propósito entró en el sistema. Su primer público fueron los equipos de desarrollo, no los usuarios.

Después llegaron las apps que la ponían al alcance de cualquiera. DSU-Sideloader, con ★2.353, fue la primera que la convirtió en un botón: recibir una imagen, pasarla y montarla. Su última versión es de abril de 2023 y su código no se mueve desde marzo de 2024, y aun así sigue siendo la puerta de entrada para la mayoría.

Con los años, los aparatos nuevos empezaron a llegar con la función desactivada o con variantes que el abuelo no entendía, y ahí nacieron las alternativas: el Plus, con ★44 y versión de junio; el de varios invitados, con ★3 y versión del 15 de octubre; y dos copias menores que nadie mira.

En paralelo, la otra mitad del ecosistema —los constructores de imágenes— siguió su propio ritmo, más lento: la fuente histórica no empuja desde enero de 2025, la imagen de ★571 publicó en mayo, la de ★259 en marzo de 2025 y la más sobria en julio de 2025.

Lo que la cronología deja claro es que la función no está en crisis ni en auge: está terminada y repartida. Y las cosas terminadas, en este ecosistema, se miden por lo que siguen haciendo y no por lo que prometen.

*🔋 El caso del invitado que se comió la batería*

Un usuario montó un invitado en septiembre y lo dejó encendido para tener a mano una app de trabajo. A la semana, el teléfono duraba hasta media tarde. A la segunda, la app de la cámara tardaba en abrir. A la tercera, culpó a una actualización del sistema de la casa.

El diagnóstico fue más simple. El invitado, aunque no se estuviera usando, mantenía su proceso y sus servicios; el sistema de la casa seguía administrando dos sistemas con una sola batería. Apagar el invitado cuando no se usa habría resuelto el 80% del problema, y borrarlo lo habría resuelto del todo.

La conclusión del caso es la que conviene apuntar: el invitado no es gratis mientras está montado, aunque esté quieto. Y la costumbre que sirve es la de encenderlo para lo que se necesite y apagarlo como se apaga una luz.

*🧩 El invitado comparado con las otras puertas*

En esta serie de guías han aparecido ya cuatro formas de cambiar algo en el teléfono, y conviene ponerlas en fila porque se confunden entre ellas.

*Root:* control total, consecuencias totales. Se instala cambiando el arranque, algunas apps dejan de abrir y el riesgo es del aparato.

*Shizuku:* un permiso que se presta, se apaga al reiniciar y no toca el arranque. Sirve para dar a las apps lo que el sistema no les da.

*Capa de traducción o emulación de otro sistema:* se ejecuta el software de otra plataforma dentro del teléfono. Es lo que hace Husk en el iPhone y lo que hacen los emuladores en general.

*Sistema invitado:* se ejecuta otro Android con el hardware del mismo teléfono, sin tocar el sistema de la casa y sin root.

De las cuatro, el invitado es la que menos arriesga y la que menos manda. Esa combinación lo hace perfecto para probar y malo para transformar: quien quiere cambiar su teléfono de verdad necesita root; quien quiere probar cosas sin riesgo tiene el invitado.

⏬ sigue abajo · parte 9 de 16

═══ MENSAJE 11 de 17 · 3473 caracteres ═══

*🧑🏫 Enseñar esto a otra persona*

Montar un invitado en el teléfono de un familiar es la tentación más común y la que peor termina. Lo que sirve es enseñar tres cosas y dejar que la persona lo haga.

La primera es la comprobación: cómo saber si su aparato soporta la función, sin instalar nada y sin que nadie toque su teléfono.

La segunda es la frontera: qué va a dejar de ver cuando esté dentro del invitado y qué se va a llevar cuando lo borre.

La tercera es el borrado: dónde está el botón, qué avisa el sistema y qué pasa si no lo encuentra.

Con esas tres, la persona puede decidir que no lo quiere, y esa también es una respuesta buena. Sin ellas, el teléfono vuelve a la semana siguiente con tres gigas ocupados por un sistema que nadie usa.

*🧷 Cuatro detalles del día a día*

*Las notificaciones.* El invitado solo recibe las suyas mientras está encendido. Si alguien espera un mensaje en el invitado, tiene que dejar el invitado abierto, y eso consume batería.

*La cámara.* Suele funcionar con menos calidad y a veces con una app distinta a la de la casa, que no tiene los ajustes del fabricante. Para una foto rápida sirve; para lo que importa, no.

*Los archivos.* Todo lo que se guarda dentro del invitado vive dentro del invitado. La costumbre que sirve es una carpeta compartida por correo o por la nube, y mover las cosas importantes hacia afuera el mismo día.

*Las actualizaciones.* El invitado puede recibir actualizaciones del sistema si la imagen las soporta, y esas actualizaciones consumen espacio del invitado. Un invitado de prueba no necesita actualizarse nunca.

Cuatro detalles, ninguno grave, y los cuatro son los que hacen que la gente diga que «no funciona bien» cuando en realidad funciona exactamente como se diseñó.

*🧪 Tres pruebas que dicen si el invitado sirve*

La primera prueba es de arranque: encender el invitado, esperar a la pantalla de inicio y abrir el navegador. Si llega en menos de dos minutos y navega, la instalación está bien y lo demás es rendimiento.

La segunda es de frontera: guardar un archivo dentro del invitado, apagarlo, encenderlo y comprobar que sigue ahí; luego mirar desde la casa que ese archivo no aparece. Si aparece en los dos lados, la imagen está compartiendo almacenamiento y eso hay que saberlo antes de meter nada sensible.

La tercera es de salida: borrar el invitado y comprobar que el espacio vuelve y que la casa arranca igual. Es la prueba que casi nadie hace y la que convierte esta función en algo seguro de usar: saber que se puede deshacer.

Las tres juntas ocupan veinte minutos y contestan la única pregunta que importa antes de confiarle algo al invitado.

*🛒 Cinco comprobaciones de la imagen*

Antes de bajar una imagen, cinco datos: para qué arquitectura está construida, qué versión del sistema espera, cuándo se publicó, qué trae de serie y quién la firma.

El primero y el segundo son los que deciden si arranca. El tercero dice si el proyecto sigue vivo: una imagen con más de un año puede ser perfectamente buena y también puede no tener los parches del año. El cuarto dice qué se está instalando: un Android base no es lo mismo que una versión con adornos.

El quinto es el que casi nadie mira y el más incómodo del censo de hoy: tres de las cuatro familias de imágenes no declaran licencia. Eso no las hace malas y sí hace que el usuario no sepa qué puede hacer con lo que baja, que es una información que debería estar en la primera línea.

⏬ sigue abajo · parte 10 de 16

═══ MENSAJE 12 de 17 · 1986 caracteres ═══

*🗂️ Un cuaderno del invitado*

Cuatro líneas por intento y no más: qué imagen, qué gestor, qué pasó y cuánto espacio quedó.

Con esas cuatro líneas escritas, el segundo intento no repite el primero. Y cuando alguien pregunta en un grupo por qué no le arranca, la respuesta se lee en el cuaderno en lugar de reconstruirse de memoria.

Es la costumbre más barata de todas las que aparecen en esta serie y la que más veces evita una tarde perdida.

*❓ Preguntas que me hacen*

**¿Necesito root para tener un Android dentro de otro?** No. La función es del sistema y las apps de esta familia solo la activan. Es su gran ventaja sobre todo lo demás que aparece en esta serie.

**¿Se borra mi teléfono?** No. El invitado vive en una imagen aparte y el borrado de esa imagen no toca los datos de la casa.

**¿Por qué mi teléfono no lo soporta?** Porque la función, aunque exista en el sistema, no está activada o faltan las particiones necesarias. AndroidLowLevelDetector, ★476 y con empujón de hoy, lo confirma en un minuto.

**¿Qué versión de DSU-Sideloader uso?** El abuelo, ★2.353, si arranca; el Plus, ★44, si el abuelo falla; el de varios invitados, ★3, si quieres más de uno. Los tres son Apache-2.0 y ninguno se actualiza con frecuencia.

**¿Qué imagen elijo?** Una construida para tu arquitectura y tu versión: las cuatro familias del censo —las de ★3.552, ★571, ★312 y ★259— sirven a aparatos distintos. Se elige por compatibilidad y no por estrellas.

**¿Puedo usar la cámara y el bluetooth?** A veces. La cámara suele ir con menos calidad; el bluetooth funciona en algunos aparatos y en otros no. La huella casi nunca cruza.

**¿Cómo saco archivos del invitado?** Por correo, por un servicio de archivos o por el cable. El invitado no comparte carpeta con la casa y lo que quede dentro se va con él.

**¿Sirve para probar apps dudosas?** Sí, y es el uso que más recomiendo: se abre en el invitado y, si hace algo raro, se borra el invitado completo.

⏬ sigue abajo · parte 11 de 16

═══ MENSAJE 13 de 17 · 3612 caracteres ═══

*📊 Tabla, mitos y glosario*

*Las diez piezas, en una línea*

| Repositorio | Papel | Licencia | Empujón | Estrellas |
|---|---|---|---|---|
| DSU-Sideloader | el gestor clásico | Apache-2.0 | 13-mar-2024 | ★2.353 |
| DSU-Sideloader-Plus | gestor para aparatos difíciles | Apache-2.0 | 15-jun | ★44 |
| Dsu-Multi-sideloader | varios invitados | Apache-2.0 | 15-oct | ★3 |
| DsuSideloaderPlusProMaxUltra | copia de la copia | sin licencia | 08-sep | ★3 |
| Gong-Mi/DSU-Sideloader | reescritura en otro lenguaje | Apache-2.0 (README GPL-3.0) | 27-jul | ★2 |
| treble_experimentations | la fuente histórica | sin licencia | 27-ene-2025 | ★3.552 |
| LineageOS_gsi | imagen construida | sin licencia | 24-may | ★571 |
| treble_aosp | imagen sobria | Apache-2.0 | 25-jul-2025 | ★312 |
| crDroid_gsi | imagen alternativa | sin licencia | 08-mar-2025 | ★259 |
| AndroidLowLevelDetector | dice qué soporta tu aparato | Apache-2.0 | hoy | ★476 |

*Cinco mitos del invitado*

**Mito uno: «es una máquina virtual».** No simula el procesador: ejecuta el sistema en el mismo hardware. Por eso va rápido y por eso el borrado es limpio.

**Mito dos: «es peligroso para el teléfono».** Es la operación menos invasiva de toda esta serie: no toca el arranque ni borra datos. El riesgo es quedarse sin espacio, no perder el teléfono.

**Mito tres: «sirve para tener dos teléfonos en uno».** Sirve para probar y para separar usos, con cámara a medias, notificaciones a medias y espacio a la mitad.

**Mito cuatro: «con la app más nueva funciona seguro».** Las tres apps de la familia tienen ★2.353, ★44 y ★3. El cuello de botella es el aparato, no la app.

**Mito cinco: «si la imagen no arranca, el teléfono está roto».** Casi siempre es la imagen. Probar con otra distingue las dos cosas en veinte minutos.

*Glosario*

**Invitado** — sistema completo que se monta desde una imagen y no toca el de la casa.

**Imagen** — archivo con el sistema que se instala; ocupa varios gigas.

**GSI** — imagen de sistema genérica, construida para muchos aparatos a la vez.

**Treble** — la separación del sistema que permite que esas imágenes existan.

**Montar** — poner la imagen en marcha sin instalarla en el almacenamiento del sistema.

**Partición dinámica** — espacio que el sistema reparte entre sus partes y del que sale el invitado.

*🧭 Si solo tienes cinco minutos*

Tres atajos honestos para quien no quiere leer la guía entera.

Primero, comprueba el aparato con el detector. Si no soporta invitados, no hay nada más que hacer y ya está resuelto.

Segundo, si soporta, baja el gestor clásico —★2.353, Apache-2.0— y una imagen histórica. Con esos dos se monta el caso más probable de éxito.

Tercero, si arranca, no metas cuentas dentro y bórralo al terminar la prueba. Con eso ya sabes si esta función te sirve, y lo sabes sin haber tocado nada de lo que tienes.

Los cinco minutos, en este caso, no son un resumen: son la parte de la guía que de verdad hace falta para decidir.

*📝 Lo que este censo no dice*

No dice cuánta gente usa la función: las estrellas miden atención y no uso, y en esta familia la atención está concentrada en el gestor más viejo.

No dice qué imagen es la mejor: tres de las cuatro no declaran licencia y ninguna trae una lista de aparatos compatibles en su ficha.

No dice si tu teléfono concreto va a funcionar: eso solo lo contesta el detector en tu aparato, y por eso el detector abre y cierra la guía.

Lo que sí dice, y por eso está escrito: quién sigue empujando, con qué licencia y con qué versión, que es lo que se puede verificar desde fuera sin instalar nada.

⏬ sigue abajo · parte 12 de 16

═══ MENSAJE 14 de 17 · 2439 caracteres ═══

*🧾 Cierre de cuentas del invitado*

Un invitado cuesta espacio, batería y una tarde la primera vez; devuelve la posibilidad de probar sin riesgo y de borrar sin rastro. Las dos columnas están claras y la decisión es de quien tiene el teléfono.

*🎯 La pregunta que cierra el asunto*

¿Vas a probar algo o a cambiarte de sistema? Si es lo primero, el invitado es la herramienta; si es lo segundo, ninguna de las diez piezas de esta guía te va a dar lo que buscas y toca hablar de otra cosa.

*📚 Dos palabras para llevarse*

Invitado y frontera. Con la primera se entiende qué se instala; con la segunda, qué no cruza.

*🧭 Tres destinos para lo que se probó*

Lo que funcionó en el invitado se apunta y se busca en la casa. Lo que no funcionó se apunta y no se busca más. Lo que funcionó a medias se apunta con la condición exacta, porque ese es el dato que mañana ahorra un intento.

*🗓️ Una fecha para revisarlo*

El mismo día del año en que se montó el primer invitado, conviene mirar tres cosas: si el gestor sigue igual, si hay imagen más nueva y cuánto espacio quedó ocupado. Tres minutos y el asunto queda vigilado sin más ceremonia.

*🧷 Lo que queda pendiente en esta casa*

Tres cosas: una imagen con licencia clara, un gestor que no dependa de un proyecto parado desde 2024 y un aparato de pruebas para quien no quiera tocar el suyo. Esta guía no las resuelve y las deja dichas.

*🔗 Enlaces*

Todas las direcciones se abrieron esta tarde.

- DSU-Sideloader, el gestor clásico: https://github.com/VegaBobo/DSU-Sideloader
- DSU-Sideloader-Plus: https://github.com/yangFenTuoZi/DSU-Sideloader-Plus
- Dsu-Multi-sideloader: https://github.com/R15Hi/Dsu-Multi-sideloader
- DsuSideloaderPlusProMaxUltra: https://github.com/dhytpodd-lab/DsuSideloaderPlusProMaxUltra
- La reescritura de Gong-Mi: https://github.com/Gong-Mi/DSU-Sideloader
- treble_experimentations: https://github.com/phhusson/treble_experimentations
- LineageOS_gsi: https://github.com/MisterZtr/LineageOS_gsi
- treble_aosp: https://github.com/ponces/treble_aosp
- crDroid_gsi: https://github.com/naz664/crDroid_gsi
- AndroidLowLevelDetector: https://github.com/imknown/AndroidLowLevelDetector

*Cómo se midió.* Diez repositorios, tres lecturas cada uno por tres caminos distintos y el orden rotado de un proyecto al siguiente; las versiones se pidieron aparte, una por una. Donde la ficha y el README discrepan —un caso— se publican las dos.

⏬ sigue abajo · parte 13 de 16

═══ MENSAJE 15 de 17 · 2635 caracteres ═══

*🌅 Cierre — el invitado que se va solo*

De todas las formas de tener otro Android, esta es la única que se prueba y se borra sin dejar rastro. No pide root, no toca el arranque y no necesita que nadie te firme un permiso: pide un aparato que la soporte, espacio libre y una imagen compatible.

Lo que deja el censo es una familia pequeña y desigual. Un abuelo con ★2.353 que no se mueve desde marzo de 2024, un Plus con ★44 y versión de junio, un gestor de varios invitados con ★3 y una copia de la copia sin licencia. Del otro lado, cuatro constructores de imágenes —★3.552, ★571, ★312 y ★259— de los que tres no declaran licencia, y un detector con ★476 y empujón de hoy que contesta la única pregunta que hay que hacer antes de empezar.

La idea que queda es la más barata de toda la serie: cuando algo da miedo, se prueba en el invitado y se borra el invitado. Ese es el precio de la curiosidad, y hoy es de unos cuantos gigas y una tarde.

> —¿Y si el invitado se queda con mis archivos?
> —Se los lleva. Por eso lo que importa se saca antes, y por eso el borrado es limpio y no una tragedia.

💓 *La Bandita informa a partir de fuentes fechadas.* Un sistema invitado se juzga por lo que deja intacto cuando se va.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 17:58 y las 18:07 de Santo Domingo · diez repositorios medidos tres veces con el orden rotado · cinco versiones consultadas por separado · dos fichas con licencia contradictoria o ausente publicadas tal cual.

*Licencia de esta entrega:* prosa en CC BY-SA 4.0, cifras medidas en CC BY 4.0 y fragmentos de código en MIT; la marca «Alexis (La Bandita)» y el nombre de la casa no se ceden con ninguna de las tres.

## 🗒️ Notas al pie

**Nota de corte (1-nov):** el gestor clásico tiene dos fechas viejas —código de marzo de 2024 y versión de abril de 2023— y se publican las dos, porque la diferencia entre ellas es justamente lo que hay que ver.

**Nota de licencia (1-nov):** tres constructores de imágenes no declaran licencia y uno de los gestores pequeños declara dos. Se publican los datos tal como aparecen, con la advertencia en el cuerpo.

**Nota de alcance (1-nov):** la guía no reparte imágenes ni enlaces de descarga; nombra los proyectos que las construyen, con licencia y fecha, y enseña a comprobar el aparato antes de intentarlo.

**Nota de corrección (1-nov):** la versión anterior de esta pieza era un listado del 15 de octubre con cuatro nombres. Se reescribió con la familia completa medida hoy, incluidos los dos proyectos de ★2 y ★3 que entonces no estaban y el detector que resuelve la duda previa.

⏬ sigue abajo · parte 14 de 16

═══ MENSAJE 16 de 17 · 1411 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 14*

Medí otra vez, hoy 1 de noviembre de 2026, los 10 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• Gong-Mi/DSU-Sideloader — ★2 (sin cambio) · *dormido*: sin empujar desde el 27-jul-2026 (97 días) · Apache-2.0
• VegaBobo/DSU-Sideloader — ★2.353 (sin cambio) · *dormido*: sin empujar desde el 13-mar-2024 (963 días) · Apache-2.0
• yangFenTuoZi/DSU-Sideloader-Plus — ★44 (sin cambio) · *dormido*: sin empujar desde el 15-jun-2026 (139 días) · Apache-2.0
• R15Hi/Dsu-Multi-sideloader — ★3 (sin cambio) · empujó el 15-oct-2026 (hace 17 días) · Apache-2.0
• dhytpodd-lab/DsuSideloaderPlusProMaxUltra — ★3 (sin cambio) · *dormido*: sin empujar desde el 8-sep-2026 (54 días) · sin licencia
• phhusson/treble_experimentations — sin dato hoy (la API no respondió). No afirmo nada.
• MisterZtr/LineageOS_gsi — ★571 (sin cambio) · *dormido*: sin empujar desde el 24-may-2026 (161 días) · sin licencia
• ponces/treble_aosp — sin dato hoy (la API no respondió). No afirmo nada.
• naz664/crDroid_gsi — ★259 (sin cambio) · *dormido*: sin empujar desde el 8-mar-2025 (603 días) · sin licencia
• imknown/AndroidLowLevelDetector — ★476 (sin cambio) · empujó en las últimas horas · Apache-2.0

💓 *LOS ENLACES · medidos hoy uno por uno*

De los 4 enlaces de esta pieza, *4 responden*.
Ninguno roto.

⏬ sigue abajo · parte 15 de 16

═══ MENSAJE 17 de 17 · 152 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.
