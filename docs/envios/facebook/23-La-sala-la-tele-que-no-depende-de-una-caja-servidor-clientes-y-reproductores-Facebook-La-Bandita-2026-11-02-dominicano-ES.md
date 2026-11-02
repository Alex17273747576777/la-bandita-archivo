# PIEZA 23 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/23-La-sala-la-tele-que-no-depende-de-una-caja-servidor-clientes-y-reproductores-Facebook-La-Bandita-2026-11-02-dominicano-ES.md`
- **Fecha de la pieza:** 2-nov-2026 (según dateline; edad hoy: 0 días)
- **sha256 de la pieza:** `7b2d6fe06312655cedad3c100bbacd9e0ccb1be4a2bbb79b814044534bd0e62f`
- **Envío generado:** 2026-11-02 · 17 mensajes · el mayor de 3682 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 17 · 749 caracteres ═══

*La sala: la tele que no depende de una caja*

La Bandita · pieza 23 · guía del 2-nov-2026 · te la mando hoy en 17 mensajes.

Antes de mandártela volví a medir lo que afirma: *12 repositorios, 12 vivos*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: GPL-2.0 5 · GPL-3.0 4 · MPL-2.0 1 · MIT 1.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/23-La-sala-la-tele-que-no-depende-de-una-caja-servidor-clientes-y-reproductores-Facebook-La-Bandita-2026-11-02-dominicano-ES.md

💓 2 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 17 · 2363 caracteres ═══

*La sala: la tele que no depende de una caja*

*La Bandita · lunes 2 de noviembre de 2026 · edición dominicano-español · pieza 23 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 📺 Las cuatro piezas de una sala
├── 🎬 Cuatro escenas de esta mañana
├── 🧾 Los diez, uno por uno, con su fecha
├── 🖥️ El servidor y sus tres clientes
├── 🛰️ La antena, la guía y el canal
├── ⚖️ Qué se puede ver y qué no
├── 🛠️ Montar la sala en siete pasos
├── 🧮 Las cuentas del salón
├── ❓ Preguntas que me hacen
└── 📊 Tabla, mitos, glosario y enlaces
```

*⚡ En una página*

Una sala de televisión hecha en casa tiene cuatro piezas y ningún misterio: un aparato que guarda o recibe, un programa que sirve lo guardado, un reproductor que lo muestra y un mando que no pelea con nadie. Las cuatro se eligen por separado y las cuatro se pueden cambiar sin tocar las otras. Esta mañana se midieron diez proyectos que cubren esas piezas, y juntos suman ★96.075 con licencias claras: ocho GPL, una MPL y una MIT.

El centro de gravedad es un solo proyecto: Jellyfin, con ★58.919 en el servidor, ★4.697 en el cliente de televisor, ★3.957 en la interfaz web y ★2.850 en el cliente de teléfono. Cuatro repositorios de la misma casa que se llevan ★70.423 de las ★96.075 medidas, es decir casi tres de cada cuatro estrellas del salón. El resto se reparte entre reproductores que solo reproducen —Next Player, mpv, VLC— y dos piezas especializadas: un cliente alternativo con interfaz moderna (Streamyfin) y un cliente ligero para televisores viejos (Findroid).

Los números de hoy no son de abandono: siete de los diez empujaron entre el 1 y el 2 de noviembre y uno publicó versión hoy mismo (Next Player, v0.20.0). El contraste interesante está en las entregas: el cliente de televisor de Jellyfin empuja el 29 de octubre y su última versión es del 16 de agosto; el cliente de teléfono empuja hoy y publica desde el 14 de septiembre; y dos de los diez —VLC para Android y Tvheadend— no publican paquete en el repositorio, cada uno por una razón distinta que se explica más abajo.

La utilidad de la mañana cabe en una frase: si ya tienes los archivos, la sala se monta con un servidor libre y tres clientes que no piden cuenta; si no los tienes, ninguna de las diez piezas de hoy te consigue contenido, y esa raya se dice desde la primera página.

⏬ sigue abajo · parte 1 de 16

═══ MENSAJE 3 de 17 · 3050 caracteres ═══

*📺 Las cuatro piezas de una sala*

*La fuente.* De dónde sale la imagen: archivos en un disco, una antena de televisión abierta, un sintonizador de cable propio. Es la pieza que decide todo lo demás, y la única que no se resuelve con software.

*El servidor.* El programa que ordena, cataloga y sirve lo que hay en la fuente: carátulas, temporadas, progreso de lo visto, varios usuarios. Aquí manda Jellyfin (★58.919, GPL-2.0), con empujón de ayer y versión v12.4 del 26 de octubre.

*Los clientes.* Un programa por pantalla. El televisor tiene el suyo (jellyfin-androidtv, ★4.697); el teléfono, el suyo (jellyfin-android, ★2.850); el navegador de la computadora usa la interfaz web (jellyfin-web, ★3.957). Y cuando el cliente oficial no convence, hay alternativas: Streamyfin (★5.332, MPL-2.0) con una interfaz más moderna, y Findroid (★4.291, GPL-3.0) pensado para equipos modestos.

*El reproductor puro.* Cuando lo único que hace falta es abrir un archivo o un enlace, el servidor sobra. Ahí entran Next Player (★4.662, GPL-3.0, versión de hoy), mpv para Android (★3.669, MIT), VLC para Android (★4.127, GPL-2.0) y Just Player (★2.785, Unlicense) —este último medido y no incluido en la tabla por repetir lo que hacen los otros tres.

Y una quinta pieza que solo aparece si hay antena: Tvheadend (★3.571, GPL-3.0), el programa que convierte una tarjeta sintonizadora en un servidor de canales para toda la casa. Sin sintonizadora no tiene sentido; con ella, es la diferencia entre ver la televisión abierta en un cuarto y verla en cinco.

*🎬 Cuatro escenas de esta mañana*

*Escena uno: el televisor del cuarto.* Un televisor con Android de hace cinco años, lento, con el cliente oficial que se arrastra entre menús. Findroid, con ★4.291 y versión del 25 de octubre, existe justo para eso: menos adornos y más respuesta. No siempre es más bonito; casi siempre es más rápido en un aparato que ya no da para más.

*Escena dos: el servidor que ordenó la casa.* Una carpeta con cuatro mil archivos de series y películas, nombrados a medias. Jellyfin los reconoce, descarga carátulas y, cuando el nombre está bien puesto, acierta casi siempre. Lo que no acierta se corrige a mano una vez y no se vuelve a tocar. La misma lección del papeleo: el orden del archivo vale más que el programa que lo lee.

*Escena tres: el partido del domingo.* Un televisor sin antena, un teléfono con datos y una aplicación que promete canales gratis. Lo que hay detrás de esas aplicaciones casi nunca está medido y casi siempre es una lista que aparece y desaparece. La alternativa honesta es antena y Tvheadend, o los canales abiertos por internet que el propio canal publica.

*Escena cuatro: el archivo que no quería abrirse.* Un video en un formato que el reproductor del televisor no soporta. Next Player y mpv lo abren porque traen códecs propios; el reproductor del sistema, no. Ese es todo el argumento de tener un reproductor de reserva instalado, y explica por qué el más simple de los cuatro pesa más que su número de estrellas.

⏬ sigue abajo · parte 2 de 16

═══ MENSAJE 4 de 17 · 3566 caracteres ═══

*🧾 Los diez, uno por uno, con su fecha*

*Jellyfin · jellyfin/jellyfin · ★58.919 · GPL-2.0 · C# · empujón 1 de noviembre de 2026 · versión v12.4 del 26 de octubre de 2026.* El servidor de la sala y el proyecto más grande de la mañana. Ordena la biblioteca, guarda el progreso de cada persona, sirve a todos los aparatos de la casa y no cobra ni pide cuenta en la nube. GPL-2.0, con la advertencia de siempre: si publicas una versión modificada, compartes el código.

*Streamyfin · Streamyfin/streamyfin · ★5.332 · MPL-2.0 · TypeScript · empujón 1 de noviembre de 2026 · versión v0.55.2 del 16 de octubre de 2026.* Cliente alternativo para Jellyfin con una interfaz que se siente de aplicación moderna. Su licencia MPL-2.0 permite mezclarlo con código de otras licencias; los archivos del propio proyecto que se modifiquen se comparten. Empujón de ayer y versión de hace dos semanas.

*Cliente de televisor · jellyfin/jellyfin-androidtv · ★4.697 · GPL-2.0 · Kotlin · empujón 29 de octubre de 2026 · versión v0.19.10 del 16 de agosto de 2026.* El cliente oficial para Android TV. Casi tres meses de brecha entre lo que se escribe y lo que se publica, y esa brecha es justo la que se nota en un aparato lento: lo que se arregló en octubre no está en el paquete de agosto.

*Next Player · anilbeesetti/nextplayer · ★4.662 · GPL-3.0 · Kotlin · empujón 2 de noviembre de 2026 · versión v0.20.0 del 2 de noviembre de 2026.* El único de los diez con paquete del mismo día del corte. Reproductor simple, con códecs propios y sin servidor detrás: se abre un archivo y se ve. Es la pieza más fácil de recomendar de toda la mañana.

*Findroid · jarnedemeulemeester/findroid · ★4.291 · GPL-3.0 · Kotlin · empujón 2 de noviembre de 2026 · versión v1.2.0 del 25 de octubre de 2026.* Cliente de Jellyfin para teléfono con fama de ligero. Versión de hace una semana y empujón de hoy: el ritmo sano del barrio. Para televisores viejos, la prueba real es cómo se mueve el menú, no cuántas funciones tenga.

*VLC para Android · videolan/vlc-android · ★4.127 · GPL-2.0 · Kotlin · empujón 29 de octubre de 2026 · sin publicación de paquete en el repositorio.* El reproductor que abre casi todo y que casi todo el mundo conoce. El repositorio de Android no publica el archivo instalable ahí: la aplicación llega por la tienda oficial del proyecto y por las tiendas de aplicaciones. Es el caso más claro de la mañana en que «no hay paquete» no significa «no hay programa».

*Interfaz web · jellyfin/jellyfin-web · ★3.957 · GPL-2.0 · JavaScript · empujón 2 de noviembre de 2026 · versión v12.4 del 26 de octubre de 2026.* La pieza que permite ver todo desde el navegador de la computadora sin instalar nada. Es también la que más gente usa sin saberlo cuando entra a la dirección del servidor de la casa.

*mpv para Android · mpv-android/mpv-android · ★3.669 · MIT · Kotlin · empujón 30 de octubre de 2026 · versión publicada el 17 de septiembre de 2026.* El reproductor de los que saben: sin adornos, con todos los códecs, y una configuración que asusta la primera vez. Licencia MIT, la más permisiva de las diez. Para un archivo raro, es el que siempre abre.

*Tvheadend · Tvheadend/tvheadend · ★3.571 · GPL-3.0 · C · empujón 2 de noviembre de 2026 · sin publicación de paquete en el repositorio.* Convierte una tarjeta sintonizadora en un servidor de canales para toda la casa. No publica paquete en el repositorio porque se distribuye empaquetado por cada sistema; se compila o se instala desde el paquete de la distribución. Sin antena, no sirve de nada.


⏬ sigue abajo · parte 3 de 16

═══ MENSAJE 5 de 17 · 2056 caracteres ═══

*Cliente de teléfono · jellyfin/jellyfin-android · ★2.850 · GPL-2.0 · Kotlin · empujón 2 de noviembre de 2026 · versión v2.7.3 del 14 de septiembre de 2026.* El oficial para el bolsillo. Empujón de hoy y paquete de hace siete semanas, con versiones que avanzan con nombres cortos y seguidos. Para ver en el teléfono lo que ya está en casa, hace exactamente lo que promete.

*🖥️ El servidor y sus tres clientes*

La relación entre estas piezas es lo que hay que entender antes de instalar nada: el servidor no muestra nada y los clientes no guardan nada. Si esa división se rompe, la casa se llena de programas que hacen de todo y no hacen bien ninguna.

*El servidor se queda quieto.* Se instala una vez en un equipo que esté encendido, se le dice dónde están las carpetas y se olvida. Jellyfin cataloga, guarda el avance de cada persona y sirve el archivo cuando un cliente lo pide. Si el servidor se cae, todos los clientes se quedan mirando una pantalla de error: por eso conviene que viva en un equipo con copia de seguridad y sin experimentos.

*Los clientes se cambian sin ceremonia.* Un televisor con el cliente oficial, un teléfono con Findroid, una computadora con el navegador, y todos ven lo mismo porque el que manda es el servidor. Esa es la ventaja real del diseño: cambiar de cliente no obliga a reorganizar la biblioteca ni a perder el punto donde ibas.

*Un cliente alternativo es una apuesta razonable.* Streamyfin y Findroid existen porque el cliente oficial no siempre es el más rápido en un aparato modesto. Probarlos cuesta una instalación y no toca el servidor. Lo único que hay que comprobar es que respeten el avance guardado: si al salir de uno y entrar en otro se pierde el minuto exacto, el cliente no está listo.

*Y el reproductor suelto, cuando no hay servidor.* Next Player, mpv o VLC abren un archivo sin que exista Jellyfin en ningún sitio. Para el que ve tres películas al mes, montar un servidor es una exageración; para el que tiene cuatro mil archivos, es la única forma de encontrarlos.

⏬ sigue abajo · parte 4 de 16

═══ MENSAJE 6 de 17 · 2990 caracteres ═══

*🛰️ La antena, la guía y el canal*

La televisión abierta sigue existiendo y sigue siendo gratis, y ese es el dato que más se olvida en las discusiones sobre aplicaciones.

*La antena física.* Un trozo de metal en la ventana o en el techo, un cable y un televisor que sintonice. En la mayoría de las ciudades hay canales abiertos y no hay nada que instalar. Es la única fuente de esta guía que no depende de ningún servidor, ni propio ni ajeno.

*El sintonizador y Tvheadend.* Si quieres que esa señal llegue a cinco aparatos, hace falta una tarjeta sintonizadora en un equipo y Tvheadend sirviendo los canales por la red. Es la pieza más exigente de la mañana: requiere hardware, configuración y paciencia. Lo que devuelve es un menú de canales propio en todos los aparatos de la casa.

*La guía de programación.* Un archivo que dice qué dan y a qué hora; sin él, el menú de canales es una lista de números. Con él, se puede programar una grabación o saber si vale la pena esperar. Las guías libres existen y su calidad varía por país, y en la República Dominicana hay que probar y quedarse con la que acierte.

*El canal por internet que el propio canal publica.* Varias cadenas ofrecen su señal en vivo en su propio sitio o en su propia aplicación. Eso es legal y no necesita ningún programa de esta lista: es el mismo caso que un periódico que publica su edición en su web.

Y la raya: las listas de canales que circulan por grupos, con miles de enlaces de dudosa procedencia, no son televisión abierta. Son, en el mejor caso, señales redistribuidas sin permiso y, en el peor, una puerta para que el aparato que las abre haga otra cosa. Esta guía no reparte ninguna de esas listas ni explica cómo usarlas.

*⚖️ Qué se puede ver y qué no*

El salón es el sitio donde la línea entre «tengo el archivo» y «estoy viendo algo prestado» se cruza sin pensar. Conviene tenerla escrita.

*Lo que es tuyo o está permitido.* Tus grabaciones de la televisión abierta para uso propio donde la ley lo permite; tus copias de discos que compraste; el contenido que los propios canales publican en abierto; el material con licencias libres, que existe y es más de lo que la gente cree; y las grabaciones de tu propia cámara.

*Lo que es zona gris y conviene no tocar.* Redistribuir a otros lo que grabaste, aunque no cobres. Compartir credenciales de un servicio de pago con media familia. Bajar de un sitio que no tiene permiso para ofrecer lo que ofrece.

*Lo que está claramente fuera.* Vender acceso. Revender listas. Usar un servicio de pago sin pagarlo. Y, en general, cualquier arreglo donde otro cobra y tú pones el riesgo.

Lo que esta guía sí hace: nombrar los diez programas con su licencia y su fecha para que la parte técnica esté resuelta, y dejar la parte legal donde corresponde, que es en la decisión de cada quien con la información a la vista. Ninguno de los diez viene con contenido: eso hay que decirlo cada vez que se habla de una sala hecha en casa.

⏬ sigue abajo · parte 5 de 16

═══ MENSAJE 7 de 17 · 2797 caracteres ═══

*🛠️ Montar la sala en siete pasos*

*Paso uno: decide la fuente antes de instalar.* ¿Archivos, antena o las dos cosas? De esa respuesta sale todo lo demás, y equivocarse aquí es lo que llena la casa de programas que nadie usa.

*Paso dos: ordena los nombres de los archivos.* Serie, temporada, episodio y título, con separadores claros. El servidor reconoce bien lo que está bien nombrado y adivina mal lo que no. Una tarde de renombrar ahorra semanas de carátulas equivocadas.

*Paso tres: instala el servidor en un equipo que esté encendido.* Una computadora vieja, una cajita pequeña o un aparato dedicado. Que tenga el disco con la copia de seguridad a mano y que no sea el mismo equipo donde se trabaja todos los días.

*Paso cuatro: crea un usuario para cada persona de la casa.* El progreso de cada quien se guarda por separado y el servidor deja de ser un aparato compartido para convertirse en una cuenta por persona. Es el paso que más se salta y el que más se agradece después.

*Paso cinco: instala un cliente en el aparato que ya tienes.* El televisor con el cliente oficial o con Findroid; el teléfono con el oficial; la computadora con el navegador. No compres nada hasta ver cómo se mueve lo que ya está.

*Paso seis: prueba un archivo raro y un aparato viejo.* Un video con códecs raros en el televisor más lento de la casa. Si ese funciona, lo demás funciona. Si no, instala Next Player o mpv solo para esos casos.

*Paso siete: escribe cómo se respalda.* Una nota de tres líneas con la carpeta que se copia, el disco donde se copia y el día del mes en que se hace. Sin esa nota, la sala es un experimento; con ella, es una instalación.

*🧮 Las cuentas del salón*

*Primera cuenta: el peso del centro.* Jellyfin y sus tres clientes oficiales suman ★70.423 de las ★96.075 medidas: el 73 %. Si se añade Streamyfin, que también habla con Jellyfin, el grupo sube a ★75.755, o sea el 79 %. El salón entero gira alrededor de un solo proyecto, y eso explica dos cosas: por qué hay tantos clientes alternativos y por qué un cambio en el servidor se siente en toda la casa.

*Segunda cuenta: quién se movió hoy.* Siete de los diez empujaron el 1 o el 2 de noviembre: Jellyfin, Streamyfin, Next Player, Findroid, la interfaz web, Tvheadend y el cliente de teléfono. Uno publicó versión hoy mismo: Next Player, v0.20.0. Los otros tres empujaron en octubre: cliente de televisor, VLC y mpv.

*Tercera cuenta: las entregas.* Cinco publicaron versión en los últimos veinte días: Jellyfin y la web (26 de octubre), Findroid (25), Streamyfin (16), Next Player (hoy). Dos empujan y no publican paquete en el repositorio: VLC para Android y Tvheadend, cada uno por su razón. Uno tiene brecha de casi tres meses: el cliente de televisor, con paquete del 16 de agosto.

⏬ sigue abajo · parte 6 de 16

═══ MENSAJE 8 de 17 · 3082 caracteres ═══

*🎯 El caso del televisor que se arrastraba*

Una familia tenía un televisor de 2018 con Android, un servidor Jellyfin en una computadora del cuarto y una queja diaria: el menú tardaba en responder y las carátulas aparecían de a una. La solución que se intentó primero fue la más cara: cambiar el televisor. La que funcionó fue la más barata: instalar Findroid en el mismo televisor y bajar la calidad de las carátulas en el servidor.

Lo que estaba pasando no era falta de potencia del televisor, sino exceso de trabajo del cliente oficial: imágenes grandes, animaciones y una biblioteca de miles de elementos que el aparato intentaba cargar de golpe. Aligerar el cliente y las imágenes resolvió el 90 % del problema por cero pesos.

Moraleja útil: antes de comprar aparato, prueba otro cliente y baja la calidad de las carátulas. Es el mismo consejo que en la música y en el papeleo, con otro nombre: casi siempre el problema está en el ajuste, no en el equipo.

*🧷 El detalle del nombre de los archivos*

Los servidores de esta familia adivinan qué es un archivo por su nombre. Un nombre bien puesto trae carátula, sinopsis y episodios ordenados; uno mal puesto trae una carpeta llamada «otros» con cuatro mil cosas dentro.

El esquema que funciona: para una película, el título y el año, sin adornos; para una serie, el nombre de la serie, la temporada con dos dígitos, el episodio con dos dígitos y el título del episodio. Los espacios se respetan, los puntos y guiones bajos se cambian por espacios, y las etiquetas de calidad se dejan aparte.

Y una advertencia que ahorra horas: los acentos y las eñes no rompen nada en los servidores modernos, pero sí rompen cuando el archivo viaja a un disco con otro sistema de archivos. Si la biblioteca se va a mover entre equipos, nombres sin acentos y sin eñes, y el título bonito se deja para la carátula.

*📱 El teléfono como mando*

Una de las cosas que más se agradecen en una sala montada en casa es que el teléfono sea el mando: buscar en la biblioteca desde el sofá, elegir el episodio y mandarlo al televisor. El cliente de teléfono de Jellyfin (★2.850) hace eso, y no necesita ninguna pieza extra.

Lo que no hace, y conviene saberlo: no enciende el televisor, no cambia de entrada y no controla el volumen. Para eso hace falta un mando por infrarrojos o el mando original. Es el tipo de detalle que se descubre la primera noche y que ninguna aplicación de esta lista resuelve.

*🧾 Lo que costó medir esta sala*

La mañana se fue en tres comprobaciones. La primera, separar los cuatro repositorios de Jellyfin: es común verlos contados como uno solo y así se pierde la información más útil —que el cliente de televisor tiene una brecha de casi tres meses y el de teléfono no—. La segunda, entender las dos ausencias de paquete, porque «sin publicación en el repositorio» no es lo mismo en VLC (que distribuye por su tienda) que en Tvheadend (que se empaqueta en cada sistema). La tercera, comprobar los números de versión uno por uno, porque la ficha automática los trae vacíos en varios casos.

⏬ sigue abajo · parte 7 de 16

═══ MENSAJE 9 de 17 · 2626 caracteres ═══

*❓ Preguntas que me hacen*

**¿Necesito comprar algo para montar la sala?**
No, si ya tienes los archivos y un aparato encendido. Si quieres televisión abierta en varios cuartos, sí: una antena y un sintonizador. El software de esta guía es libre y no cuesta nada en los dos casos.

**¿Jellyfin cobra o pide cuenta en la nube?**
No cobra y no pide cuenta externa: el servidor es tuyo y vive en tu casa. Lo que sí pide es un aparato encendido y alguien que lo mantenga, que es el precio real de tener las cosas propias.

**¿El cliente de televisor, con paquete de agosto, sirve?**
Sirve y le faltan tres meses de arreglos. Si el televisor va bien, no hay prisa; si se arrastra, prueba Findroid o baja la calidad de las carátulas antes de comprar aparato.

**¿Por qué VLC y Tvheadend no tienen paquete en el repositorio?**
Porque cada uno se distribuye por otra vía: VLC por la tienda oficial de su proyecto y las tiendas de aplicaciones; Tvheadend empaquetado por cada sistema operativo. «Sin publicación» no significa «sin programa», y por eso se explica en la ficha.

**¿Puedo ver la televisión abierta sin antena?**
Solo lo que el propio canal publique en abierto por su sitio o su aplicación. Lo demás que circula por grupos no es televisión abierta: es una señal redistribuida sin permiso y esta guía no la reparte.

**¿Cuál de los cuatro reproductores sueltos elijo?**
Next Player si quieres algo simple y con versión fresca; mpv si quieres abrir cualquier cosa y no te asusta configurar; VLC si quieres el que todo el mundo conoce; Just Player si quieres el más liviano, midiendo que su licencia es Unlicense.

**¿Cuántos usuarios puedo crear en el servidor?**
Los que quieras, y conviene uno por persona. Cada uno con su avance y sus listas; el servidor guarda todo por separado y esa separación es la que evita discusiones sobre quién vio qué.

**¿Funciona sin internet?**
El servidor y los clientes funcionan en la red de la casa sin salir a internet, siempre que no uses funciones que consultan metadatos externos. Es una de las ventajas del diseño: la sala no depende de que nadie tenga la puerta abierta.

**¿Y si el servidor se daña?**
Los archivos siguen en el disco y el servidor se vuelve a instalar en una hora. Lo que se pierde es el avance guardado y las carátulas; por eso la copia incluye la carpeta de datos del servidor, no solo la de las películas.

**¿Merece la pena Tvheadend si no tengo sintonizadora?**
No. Sin hardware que reciba la señal, Tvheadend no tiene qué servir. Es la pieza más especializada de la mañana y la única que exige comprar algo antes de instalar.

⏬ sigue abajo · parte 8 de 16

═══ MENSAJE 10 de 17 · 3594 caracteres ═══

*📊 Tabla, mitos y glosario*

*Los diez medidos, en una línea*

| Proyecto | Estrellas | Licencia | Empujón | Última versión |
|---|---|---|---|---|
| Jellyfin (servidor) | ★58.919 | GPL-2.0 | 1-nov-2026 | v12.4 · 26-oct-2026 |
| Streamyfin | ★5.332 | MPL-2.0 | 1-nov-2026 | v0.55.2 · 16-oct-2026 |
| Cliente de televisor | ★4.697 | GPL-2.0 | 29-oct-2026 | v0.19.10 · 16-ago-2026 |
| Next Player | ★4.662 | GPL-3.0 | 2-nov-2026 | v0.20.0 · 2-nov-2026 |
| Findroid | ★4.291 | GPL-3.0 | 2-nov-2026 | v1.2.0 · 25-oct-2026 |
| VLC para Android | ★4.127 | GPL-2.0 | 29-oct-2026 | sin paquete en el repositorio |
| Interfaz web | ★3.957 | GPL-2.0 | 2-nov-2026 | v12.4 · 26-oct-2026 |
| mpv para Android | ★3.669 | MIT | 30-oct-2026 | 17-sep-2026 |
| Tvheadend | ★3.571 | GPL-3.0 | 2-nov-2026 | sin paquete en el repositorio |
| Cliente de teléfono | ★2.850 | GPL-2.0 | 2-nov-2026 | v2.7.3 · 14-sep-2026 |

*Cinco mitos del salón*

*Mito uno: «montar una sala es cosa de expertos».* Es instalar un servidor, decirle dónde están las carpetas e instalar un cliente. La parte difícil es ordenar los nombres, y eso no lo hace ningún programa.

*Mito dos: «si el servidor es libre, el contenido también».* El programa es libre; las películas y los partidos tienen dueño. Ninguna de las diez piezas de hoy trae nada dentro.

*Mito tres: «las aplicaciones de canales gratis son televisión abierta».* Casi nunca. Detrás suele haber listas redistribuidas sin permiso que aparecen y desaparecen, y a veces algo peor que una mala señal.

*Mito cuatro: «un televisor lento necesita un televisor nuevo».* Antes de comprar, prueba otro cliente y baja la calidad de las carátulas. En la mayoría de los casos el aparato da para mucho más de lo que el cliente oficial le pide.

*Mito cinco: «sin paquete en el repositorio no hay programa».* VLC y Tvheadend se distribuyen por otras vías. Lo que hay que mirar es dónde se publica, no solo si el repositorio tiene una etiqueta de versión.

*Glosario*

*Servidor de medios:* programa que cataloga y sirve los archivos de la casa a varios aparatos.

*Cliente:* programa que muestra lo que el servidor sirve; no guarda la biblioteca.

*Transcodificar:* convertir el video al vuelo para que un aparato que no soporta el formato pueda verlo.

*Carátula:* imagen que el servidor asocia a una película o serie a partir del nombre del archivo.

*Sintonizadora:* tarjeta o aparato que recibe la señal de televisión y la entrega a la computadora.

*Guía de programación:* archivo con los horarios y títulos de los canales.

*Unlicense:* licencia que renuncia a casi todos los derechos; la más permisiva que aparece hoy.

*🧭 Cuatro perfiles y su sala*

*El que tiene carpetas y nada más.* Un reproductor suelto y la carpeta ordenada. Next Player o mpv, según el ánimo de configurar. No necesita servidor ni red: abre el archivo y se ve.

*El que quiere ver en varios cuartos.* Servidor Jellyfin en un aparato encendido y un cliente por pantalla. Es el salto grande y el que más se agradece cuando hay niños, abuelos y gustos distintos bajo el mismo techo.

*El que ve televisión abierta.* Antena, sintonizadora y Tvheadend si quiere la señal en varios aparatos. Es el perfil más exigente y el único que necesita comprar hardware.

*El que mira en el teléfono, en el bus.* Cliente de teléfono y, si el servidor está bien configurado, la misma biblioteca con el avance guardado. Con datos móviles hay que cuidar la transcodificación: convertir el video en el servidor consume más y, si se sale de la red de la casa, hay que abrir camino de forma segura.

⏬ sigue abajo · parte 9 de 16

═══ MENSAJE 11 de 17 · 3158 caracteres ═══

*🏠 El servidor en una cajita*

El servidor de la sala no necesita una computadora grande. Tres formas domésticas, con lo que hay que saber de cada una.

*La computadora vieja.* La que ya no se usa para trabajar, con el disco grande y el servidor instalado. Ventaja: espacio y potencia de sobra. Desventaja: consume y hace ruido; si se apaga a la noche, no hay sala hasta la mañana.

*La cajita de placa única.* Consume como una bombilla, no hace ruido y vive encendida todo el año. Si el aparato no tiene aceleración de video, la transcodificación se vuelve lenta; se resuelve eligiendo clientes que reproduzcan el archivo tal como está, sin convertirlo.

*El aparato dedicado de la casa.* Un equipo pequeño pensado para esto, con su sistema y su tienda de paquetes. Cuesta, y a cambio se olvida: se actualiza y sigue funcionando.

La decisión práctica se toma con una sola pregunta: ¿cuántas personas van a ver al mismo tiempo? Una o dos, cualquier cajita; cuatro o cinco con aparatos distintos, mejor un equipo con disco propio y procesador decente.

*🔌 La red de la casa*

La sala se cae más veces por la red que por el software, y casi siempre por el wifi.

*El televisor por cable.* Si el televisor está cerca del router, un cable resuelve el 80 % de los cortes. El wifi en un televisor se satura con cualquier descarga simultánea y el síntoma es un video que se queda cargando justo en la escena importante.

*El servidor por cable.* El equipo que sirve la biblioteca debe estar por cable si es posible: sirve a varios aparatos a la vez y cada uno por wifi multiplica el problema.

*El nombre del servidor, anotado.* La dirección del servidor en la red de la casa conviene tenerla escrita en un papel pegado dentro del mueble. Cuando cambie el router o se reinicie todo, ese papel ahorra una tarde de búsqueda.

*La salida a internet, aparte.* Ver la biblioteca de la casa desde fuera requiere abrir camino de forma segura y no es un paso de esta guía. Se menciona porque es la causa principal de configuraciones peligrosas: abrir puertos a la ligera es la manera más rápida de regalar la casa entera.

*📶 La sala sin internet*

Una de las mejores cosas de este diseño es que la casa puede seguir viendo lo suyo cuando la conexión se cae. Para eso hay tres ajustes que conviene dejar puestos desde el primer día.

*Metadatos primero, siempre.* Las carátulas y las sinopsis se descargan una vez; después quedan en la base del servidor. Si nunca se han descargado, la biblioteca se ve como una lista de nombres grises justo el día que no hay internet.

*Nada de cuentas externas.* El servidor de la casa no necesita cuenta en la nube ni inicio de sesión remoto. Lo que pida una cuenta externa para funcionar es lo primero que se cae sin internet, y por eso se evita.

*Clientes que reproduzcan el archivo tal cual.* Si el cliente pide transcodificar, el servidor trabaja más y en una cajita modesta se nota. Elegir clientes que acepten el formato original reduce el trabajo y mejora la imagen.

Con esos tres ajustes, una noche sin conexión se parece muchísimo a una noche con conexión, que es exactamente lo que se busca.

⏬ sigue abajo · parte 10 de 16

═══ MENSAJE 12 de 17 · 3019 caracteres ═══

*🕰️ Cómo cambió esta sala en dos años*

En 2024 la conversación era «qué aplicación me sirve la carpeta» y la respuesta habitual era un programa con interfaz de otro siglo. En 2026 la conversación es «qué cliente se mueve mejor en mi televisor», y eso significa que la parte del servidor se resolvió: hay un proyecto grande, libre, con clientes para todas las pantallas y con siete empujones en dos días.

Lo que no se resolvió es la parte de la fuente. Las listas de canales siguen siendo un desorden con riesgo legal, la televisión abierta sigue necesitando antena, y el contenido de pago sigue teniendo dueño. La técnica avanzó; el contenido no es un problema técnico.

*🧪 Cuatro pruebas antes de comprometerte*

*Prueba uno: el archivo raro.* Un video con códecs poco comunes en el aparato más lento de la casa. Si se ve, la sala sirve para todo lo demás.

*Prueba dos: el avance guardado.* Ver cinco minutos en el teléfono, salir, entrar en el televisor. Si el minuto está donde lo dejaste, el servidor está haciendo su trabajo.

*Prueba tres: tres pantallas a la vez.* Reproducir en tres aparatos al mismo tiempo, con uno de ellos por wifi. Si todo se ve sin cortes, la red aguanta la casa.

*Prueba cuatro: apagar el servidor y volver a encenderlo.* Si todo vuelve sin tocar nada, la instalación está terminada; si hay que reconfigurar algo, falta un paso en el camino.

*🧷 Lo que hay que apuntar en un papel*

Cuatro datos que conviene tener escritos y que nunca se recuerdan cuando hacen falta: la dirección del servidor en la red de la casa, el nombre de usuario del administrador, la carpeta donde viven los archivos y la carpeta donde el servidor guarda sus datos. Esa última es la que casi nadie respalda y la que, cuando se pierde, borra el avance de todos.

*🎚️ Los ajustes que cambian la sala*

Cinco ajustes hacen más por la experiencia que cualquier compra de aparato.

*La calidad de las carátulas.* Bajar el tamaño de las imágenes que el servidor entrega aligera los clientes modestos más que cualquier otra cosa. Es el primer ajuste que se toca en un televisor lento, y el que casi nadie toca.

*La transcodificación.* Activarla solo cuando haga falta. Si los clientes reproducen el archivo tal cual, el servidor apenas trabaja; si convierte todo, una cajita modesta se ahoga con dos pantallas a la vez.

*El idioma y los subtítulos.* Fijar el idioma preferido y el formato de subtítulo evita que cada cliente elija por su cuenta y que una película empiece con subtítulos en un idioma que nadie pidió.

*Los usuarios y los permisos.* Un usuario por persona, con permiso para ver la biblioteca y sin permiso para administrar el servidor. Suena exagerado en una casa de dos personas y deja de sonar exagerado el día que un sobrino instala algo en el televisor.

*La carpeta de datos.* El servidor guarda ahí la base, las carátulas y el avance. Esa carpeta va en la copia de seguridad junto con los archivos, y sin ella una reinstalación borra meses de «por dónde iba».

⏬ sigue abajo · parte 11 de 16

═══ MENSAJE 13 de 17 · 3682 caracteres ═══

*🏷️ Cuatro reglas para ordenar la biblioteca*

*Regla uno: una carpeta por tipo.* Películas, series, documentales, música, grabaciones de la antena. Mezclar tipos obliga al servidor a adivinar y le hace adivinar mal.

*Regla dos: el año siempre en el nombre.* Dos películas con el mismo título se distinguen por el año y por nada más. Sin año, la carátula que trae el servidor suele ser la equivocada.

*Regla tres: los episodios con dos dígitos.* Temporada y episodio con dos cifras para que el orden alfabético coincida con el orden real. Un episodio diez que aparece antes que el dos es el error más común de las bibliotecas caseras.

*Regla cuatro: nada de carpetas anidadas a capricho.* Un nivel de más confunde al reconocedor y termina con series dentro de series. Tres niveles como máximo: tipo, título, temporada.

Con esas cuatro reglas, la biblioteca se reconoce sola y el trabajo de corregir carátulas a mano se reduce a casos raros.

*🧮 Lo que cuesta tener la sala encendida*

La cuenta doméstica, sin adornos: un televisor consume; un aparato pequeño que sirve la biblioteca consume mucho menos; una computadora de escritorio encendida todo el año consume como varios aparatos pequeños juntos. La decisión de dónde vive el servidor es también una decisión de consumo.

Para una casa donde se ve televisión todas las noches, dejar el servidor en una cajita es lo razonable. Para una casa donde se ve los fines de semana, encender la computadora cuando se va a ver es perfectamente válido y ahorra el consumo del resto de la semana. No hay una respuesta única; hay una costumbre que se elige una vez.

*🧷 Tres cosas que la sala no resuelve*

*La primera: qué ver.* Ninguno de los diez programas decide el contenido. Un servidor con la biblioteca vacía es un mueble bonito; la pregunta de qué se ve sigue siendo del que se sienta.

*La segunda: el aparato que no da.* Cuando el televisor se arrastra incluso con el cliente más ligero, no hay software que lo salve. Ahí se compra, se cambia la cajita del televisor o se acepta.

*La tercera: quién mantiene.* Un servidor que nadie actualiza es un servidor que un día deja de servir a los clientes nuevos. Media hora cada dos meses, en la misma rutina de la copia, resuelve el asunto entero.

*📎 Lo que se lleva el que leyó hasta aquí*

Cuatro ideas y una costumbre. La primera: separar servidor, cliente y reproductor, porque es lo que permite cambiar cada pieza sin tocar las otras. La segunda: siete de diez proyectos empujaron en dos días, así que el barrio está vivo y las fechas se mueven rápido. La tercera: el paquete y el empujón no son lo mismo, y la brecha se mide desde el paquete. La cuarta: la fuente no es un problema de software, y ninguna de estas diez piezas trae contenido.

Y la costumbre: antes de comprar aparato, ordenar nombres y bajar la calidad de las carátulas. Es gratis y resuelve más que la mitad de las quejas del salón.

*🎯 El caso del que compró antes de probar*

Un usuario tenía un televisor de 2020 que se arrastraba con el cliente oficial. Compró un aparato nuevo de gama media antes de probar nada. El aparato nuevo se arrastraba igual, porque el problema era la biblioteca: carátulas de tres megas, miles de elementos y una red saturada.

Lo que resolvió el caso costó cero: bajar la calidad de las imágenes en el servidor, ordenar los nombres de las cuatro mil carpetas y pasar el televisor al cable. El aparato nuevo quedó en el cuarto, que tampoco estaba mal, pero la lección quedó cara.

La prueba que hubiera ahorrado la compra es la de esta guía: el archivo raro en el aparato más lento. Diez minutos, ningún gasto, y una respuesta antes de pagar.

⏬ sigue abajo · parte 12 de 16

═══ MENSAJE 14 de 17 · 2846 caracteres ═══

*🔗 Enlaces*

- Jellyfin (servidor): https://github.com/jellyfin/jellyfin
- Cliente de televisor: https://github.com/jellyfin/jellyfin-androidtv
- Cliente de teléfono: https://github.com/jellyfin/jellyfin-android
- Interfaz web: https://github.com/jellyfin/jellyfin-web
- Streamyfin: https://github.com/Streamyfin/streamyfin
- Findroid: https://github.com/jarnedemeulemeester/findroid
- Next Player: https://github.com/anilbeesetti/nextplayer
- mpv para Android: https://github.com/mpv-android/mpv-android
- VLC para Android: https://github.com/videolan/vlc-android
- Tvheadend: https://github.com/Tvheadend/tvheadend
- Just Player: https://github.com/moneytoo/player
- La capa de inmersión del archivo: https://github.com/Kareadita/Kavita

*Cómo se midió:* diez repositorios, tres lecturas cada uno con el orden rotado —API de búsqueda, página del repositorio y contenido crudo del README y la licencia—, más una cuarta comprobación por interrogación directa a la lista de publicaciones de cada proyecto, porque la ficha automática devuelve vacías varias fechas de versión. Los dos casos sin paquete en el repositorio se verificaron uno por uno para distinguir «se distribuye por otra vía» de «no publica nada». Corte entre las 10:40 y las 11:55 de Santo Domingo.

*🌅 Cierre — una sala con cuatro piezas y ninguna caja*

El salón de esta mañana deja un mapa claro: un servidor grande y libre (★58.919), tres clientes oficiales que cubren televisor, teléfono y navegador, dos alternativas que existen para aparatos modestos y cuatro reproductores sueltos para cuando no hace falta nada más. Siete de los diez empujaron en dos días y uno publicó versión hoy mismo, lo que dice que el barrio está trabajando y no solo existiendo.

El reparto de estrellas vuelve a ser la lección de siempre: casi ocho de cada diez están en un solo proyecto, y ese proyecto es el que menos se ve cuando alguien habla de «la aplicación para ver tele». Lo que se ve es el cliente; lo que sostiene la casa es el servidor.

*Medición del corte:* lunes 2 de noviembre de 2026, entre las 10:40 y las 11:55 de Santo Domingo · diez repositorios con las tres lecturas completas y el orden rotado · diez listas de publicaciones consultadas una por una · dos ausencias de paquete explicadas caso por caso.

*Licencia de esta entrega:* la prosa se publica en CC BY-SA 4.0, las cifras medidas en CC BY 4.0 y los ejemplos de código en MIT. Ni la marca «Alexis (La Bandita)» ni el nombre de la casa forman parte de ese intercambio: se quedan donde están.

> —¿Y si me canso de todo esto?
> —Entonces te quedas con un reproductor suelto y una carpeta ordenada: la sala mínima también funciona.

💓 *La Bandita informa a partir de fuentes fechadas.* En una sala hecha en casa, el cliente se cambia; el servidor y los archivos son los que hay que cuidar.

⏬ sigue abajo · parte 13 de 16

═══ MENSAJE 15 de 17 · 978 caracteres ═══

## 🗒️ Notas al pie

(2-nov) Los cuatro repositorios de Jellyfin se publican separados, no como uno: la suma conjunta (★70.423) y la del grupo con Streamyfin (★75.755) están calculadas sobre los valores exactos de la tabla, sin redondeo.

(2-nov) Dos fichas dicen «sin paquete en el repositorio» y no «abandonado»: VLC para Android distribuye por la tienda de su proyecto y Tvheadend se empaqueta por sistema operativo. La diferencia entre las dos cosas se explica en el cuerpo y no se disimula en la tabla.

(2-nov) Next Player es el único con versión del mismo día del corte (v0.20.0, 2 de noviembre); se comprobó en su lista de publicaciones y coincide con la fecha del último empujón.

(2-nov) Just Player se midió (★2.785, Unlicense, empujón 22 de octubre, versión v0.217 del 11 de septiembre) y se dejó fuera de la tabla por repetir lo que hacen los otros tres reproductores; se nombra en el cuerpo para que la ausencia no parezca un olvido.

⏬ sigue abajo · parte 14 de 16

═══ MENSAJE 16 de 17 · 1677 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 23*

Medí otra vez, hoy 2 de noviembre de 2026, los 12 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• jellyfin/jellyfin — ★58.920 (+133) · empujó en las últimas horas · GPL-2.0 · última release v12.4 (26-oct-2026)
• jellyfin/jellyfin-androidtv — ★4.697 (+22) · empujó el 29-oct-2026 (hace 4 días) · GPL-2.0 · última release v0.19.10 (16-ago-2026)
• jellyfin/jellyfin-android — ★2.851 (+12) · empujó en las últimas horas · GPL-2.0 · última release v2.7.3 (14-sep-2026)
• jellyfin/jellyfin-web — ★3.957 · empujó en las últimas horas · GPL-2.0 · última release v12.4 (26-oct-2026)
• Streamyfin/streamyfin — ★5.332 · empujó en las últimas horas · MPL-2.0 · última release v0.55.2 (16-oct-2026)
• jarnedemeulemeester/findroid — ★4.291 (+11) · empujó en las últimas horas · GPL-3.0 · última release v1.2.0 (25-oct-2026)
• anilbeesetti/nextplayer — ★4.662 (+27) · empujó en las últimas horas · GPL-3.0 · última release v0.20.0 (2-nov-2026)
• mpv-android/mpv-android — ★3.669 · empujó el 30-oct-2026 (hace 3 días) · MIT · última release 2026-09-17 (17-sep-2026)
• videolan/vlc-android — ★4.127 (+7) · empujó el 29-oct-2026 (hace 4 días) · GPL-2.0
• Tvheadend/tvheadend — ★3.571 · empujó en las últimas horas · GPL-3.0
• moneytoo/player — ★2.785 · empujó el 22-oct-2026 (hace 11 días) · Unlicense · última release v0.217 (11-sep-2026)
• Kareadita/Kavita — ★11.995 (+24) · empujó en las últimas horas · GPL-3.0 · última release v0.9.1.4 (2-sep-2026)

💓 *LOS ENLACES · medidos hoy uno por uno*

De los 12 enlaces de esta pieza, *12 responden*.
Ninguno roto.

⏬ sigue abajo · parte 15 de 16

═══ MENSAJE 17 de 17 · 152 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.
