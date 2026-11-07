# Capítulo 11 · Cuando algo se rompe

## Qué vas a poder hacer al terminar

Diagnosticar sin adivinar. Cuando una aplicación se cierra sola, cuando el teléfono se queda sin espacio y no sabés dónde, cuando la batería dura la mitad que antes, cuando el wifi dice «conectado sin internet» o cuando una aplicación nueva no arranca porque le falta un permiso, vas a tener un orden para mirar y una forma de contarlo.

Y vas a poder hacer lo que casi nadie hace: **armar un parte de avería que sirva**. Un registro, la versión exacta, el aparato, lo que hiciste antes y lo que esperabas. Con eso, quien mantiene el programa puede arreglarlo; sin eso, tu reporte es un lamento.

## La regla que ordena el capítulo: el aparato casi nunca miente, el diagnóstico sí

Un teléfono no se rompe por brujería. Se queda sin inodos, se queda sin memoria, mata un proceso por consumo excesivo, pierde la conexión porque el punto de acceso cambió de canal, o le niegan un permiso que la aplicación da por concedido. Todas esas son causas con nombre, y las cinco tienen una pantalla donde se ven.

La regla del capítulo es una sola: **primero se mide, después se toca.** Y su forma práctica son dos preguntas en este orden:

1. **¿Qué cambió justo antes?** Una instalación, una actualización, un ajuste, un módulo, un cable distinto. El noventa por ciento de las averías tienen fecha.
2. **¿Se puede reproducir?** Si el fallo aparece siempre que hacés lo mismo, hay causa. Si aparece al azar, lo que hay que medir es el momento, y para eso está el registro.

Reinstalar es lo que se hace cuando ya se miró y no se encontró. Nunca antes.

## Los cinco sitios donde se rompe

Esta guía se rompió siempre en los mismos cinco lugares, en este orden de frecuencia:

- **El arranque.** El aparato no pasa de la marca, arranca en bucle, o una aplicación concreta se cierra al abrirse.
- **El almacenamiento.** Dice que está lleno y el administrador de archivos no muestra al culpable.
- **La batería.** Dura menos y el panel del sistema acusa a la aplicación equivocada.
- **La red.** «Conectado sin internet», lentitud por la mañana, cortes en una sola habitación.
- **Los permisos.** Una aplicación que pide algo que ya le diste, o que el sistema le quitó sin avisar.

Cada uno tiene su señal, su herramienta y su primer comando. El resto del capítulo es eso.

## La ruta de decisión, en cinco preguntas

**¿Se cierra sola una aplicación o el teléfono se reinicia?** → **LogFox**, para leer el registro del sistema en el propio aparato, con notificación de cierres y de bloqueos de interfaz, y exportación a un archivo comprimido junto con los datos del aparato.

**¿Dice que no hay espacio y no sabés de qué?** → **disky**, que mide el árbol de carpetas y muestra en segundos qué ocupa. Y si querés el detalle fino —tamaño de bases de datos, cachés, aplicaciones— sin instalar nada, la orden del apartado de almacenamiento.

**¿Querés saber qué permiso tiene de verdad cada aplicación, incluidos los ocultos?** → **Permission Manager X**, que muestra permisos del manifiesto y operaciones de aplicación que el panel normal de Android no lista.

**¿El problema es la red inalámbrica?** → **WiFi Analyzer**, que dibuja los canales, la potencia de cada red y los vecinos que te están estorbando.

**¿La batería es el problema?** → **Battery Monitor**, para ver carga, temperatura, voltaje y salud con el número real y no con el icono.

Y si el aparato ya no arranca o querés mandar un parte completo a quien programa, la respuesta es una computadora y **QADB**: registro en vivo, orden directa y el informe del sistema en un solo programa de escritorio.

## El arranque: el aparato que no pasa de la marca

Hay tres clases de «no arranca», y se tratan distinto:

- **No enciende nada.** No hay pantalla ni vibración. Es carga, cable o batería; ningún programa del teléfono sirve porque el teléfono no está corriendo.
- **Enciende y se queda en la marca o en bucle.** El sistema arranca y algo que se carga al inicio lo tumba. Casi siempre es un módulo o un ajuste recién puesto. La salida se llama **modo seguro**: se mantiene apretado el botón de bajar volumen durante el arranque hasta que el sistema entra sin cargar lo que agregaste. Si en modo seguro arranca, la culpa es de lo último que instalaste, y ya sabés qué quitar.
- **Arranca y una aplicación se cierra al abrirse.** Ahí sí hay registro, y está a mano.

El registro de Android tiene varios canales y el bueno para un cierre es el de fallos: la línea de la excepción dice el nombre del paquete, la clase y —esto es lo que casi nadie lee— la causa encadenada, que es la última de la lista y no la primera. Un registro sin la primera línea de la excepción no sirve para nada.

Y una advertencia que vale para todo este capítulo: **el registro contiene datos personales**. Nombres de cuentas, direcciones, rutas de archivos, identificadores del aparato. Antes de pegarlo en un foro o mandarlo a un desarrollador, se lee y se tacha lo que no hace falta. LogFox exporta un archivo con los datos del aparato incluidos justamente para no tener que adivinar de qué teléfono se habla, y eso mismo es lo que hay que revisar antes de compartirlo.

## El almacenamiento: el espacio que no aparece

El teléfono dice «almacenamiento casi lleno», abrís el administrador de archivos y no hay nada grande. La explicación es casi siempre la misma: **lo que ocupa no son tus archivos, son las cachés y los datos de las aplicaciones**, que el administrador no muestra porque no son archivos que puedas tocar.

`disky` mide el árbol completo y lo pone en barras: ahí aparece la carpeta que nadie mira. Con eso se decide: se limpia la caché de la aplicación que creció, se saca el video, se mueve la copia de fotos. Y una cosa que no se hace: borrar la carpeta de datos de una aplicación sin copia. Eso no es limpiar, es perder la cuenta.

## La batería: el número que engaña

El panel de batería de Android reparte culpas por tiempo de uso, y eso confunde: una aplicación que despierta el aparato cada minuto puede salir con un porcentaje bajo y ser la culpable. Los tres números que sí dicen algo son **temperatura**, **ciclos** y **capacidad estimada**; el porcentaje de uso es el cuarto.

La temperatura explica más de lo que parece: un aparato que se calienta en reposo tiene algo corriendo. Y una batería con dos años y medio de ciclos tiene menos capacidad aunque el icono diga cien por ciento, porque el sistema estima, no mide la química.

## La red: cuando «no hay internet» es otra cosa

«Conectado sin internet» significa una sola cosa: el teléfono tiene enlace con el punto de acceso y no logró resolver un nombre. Puede ser el router, puede ser el proveedor, puede ser el DNS que elegiste en el capítulo 5, o puede ser un bloqueo que configuraste vos. Se separa en tres pasos y no hay cuarto:

1. **¿Hay enlace?** Si el wifi muestra la red y la intensidad, sí.
2. **¿Hay dirección?** Si el aparato tiene dirección asignada, sí.
3. **¿Resuelve y responde?** Con una consulta de nombre y una prueba al servidor público más cercano.

Y para la calidad, el instrumento es el canal: en la banda de 2,4 GHz hay tres canales que no se pisan y todos los vecinos usan el mismo. **WiFi Analyzer** muestra cuáles están ocupados y cuál conviene. La mitad de los «el wifi va lento» de un edificio se arreglan cambiando el canal del router, que no es un aparato del teléfono y por eso nadie lo mira.

## Los permisos: lo que pide y lo que el sistema concede

Un permiso declarado en el manifiesto no es un permiso concedido. Y hay una segunda capa, las **operaciones de aplicación**, que el sistema usa internamente para cosas como leer el portapapeles, dibujar encima de otras aplicaciones o acceder a los registros de llamadas. El panel normal de Android muestra la primera capa; la segunda queda escondida, y es donde se entiende por qué una aplicación se comporta raro después de una actualización del sistema.

Ahí es donde Permission Manager X gana: lista las dos capas por aplicación, deja buscar por permiso y avisa cuando algo cambia. Su precio es la nota más baja de este capítulo —**veintiocho puntos**, dos personas en el proyecto, sin integración continua—, y se dice tal cual: es la mejor herramienta de su clase y no es un proyecto con relevo. Se usa para mirar, y se tiene presente que un día puede no actualizarse.

Para diagnosticar alcanza con tres reglas: **un permiso negado se ve**, **un permiso revocado por el sistema también**, y **una aplicación que funciona en otro teléfono y no en el tuyo casi siempre tiene un permiso de más, no de menos**.

## El parte de avería: cómo se cuenta un fallo para que lo puedan arreglar

Esta es la parte que separa a quien usa el ecosistema libre de quien lo sostiene. Un parte que sirve tiene seis líneas y ninguna sobra:

1. **Qué programa y qué versión exacta**, con el número que aparece en su entrega, no «la última».
2. **Qué aparato y qué versión de Android**, con el modelo y la compilación.
3. **Qué hiciste**, paso por paso, en el orden en que lo hiciste.
4. **Qué esperabas** que pasara.
5. **Qué pasó**, con el texto exacto del mensaje.
6. **El registro**, recortado al momento del fallo y sin datos personales.

Con eso, un mantenedor puede reproducirlo. Sin eso, tiene que adivinar, y adivinar es lo que hace que un proyecto libre se canse de sus usuarios.

Y una regla de conducta: **antes de reportar, se comprueba si ya está reportado.** Casi todos los proyectos que aparecen en esta guía tienen su lista de incidencias abierta y buscable, y el sesenta por ciento de los reportes repetidos ya tienen respuesta. Buscar primero es respeto, y además es más rápido.

## Lo que dejé fuera, y por qué

En la búsqueda de este capítulo apareció un inspector de sistema con **novecientas una estrellas** y una lista de funciones que daba envidia: ver aplicaciones, leer bases de datos, observar los avisos internos del sistema. No entró, y el motivo es el criterio de toda la guía: **no publica una sola entrega**. Sin una entrega con archivo no hay forma de instalarlo sin compilar, y esta guía no recomienda lo que no se puede bajar y comprobar. No es un mal programa: es un programa que hoy no cumple la condición de entrada, y queda anotado por si la cumple mañana.

También quedaron fuera dos que sí existen y funcionan, por no repetir: el lector de registros de escritorio, que hace lo mismo que LogFox con un cable, y el inspector de interfaces, que sirve a quien programa y no a quien repara.

## Los cuatro errores que se pagan

**Reinstalar como primer movimiento.** Se pierde la escena del crimen: el registro, la caché, la versión anterior. Y en la mitad de los casos el fallo vuelve porque la causa estaba fuera del teléfono.

**Mandar el registro entero.** Además de exponer datos personales, un archivo de cien mil líneas no se lee. Se recorta al momento y se explica qué buscar.

**Confundir el síntoma con la causa.** «Se cierra al abrir la cámara» no dice nada; «se cierra al abrir la cámara desde la pantalla de bloqueo, con la versión tal, en un aparato tal» dice todo.

**Tocar cinco cosas a la vez.** Si cambiás el canal del wifi, el DNS, la aplicación y el ajuste de batería en la misma tarde y algo se arregla, no vas a saber qué fue, y la próxima vez empezás de cero.

## Tres cosas que se dicen y no son verdad

**«El teléfono ya no da, hay que cambiarlo».** Un aparato de tres años con batería cambiada y sin aplicaciones de más rinde como nuevo. Lo que se gasta no es el aparato: es la batería y el espacio.

**«El antivirus lo arregla».** Los programas de «limpieza y velocidad» de las tiendas hacen exactamente lo que el sistema ya hace, con publicidad encima. El diagnóstico de este capítulo es gratis y se puede leer.

**«Si el wifi falla, es el proveedor».** La mitad de las veces es el canal, el router o un DNS que alguien configuró y olvidó. Hay tres pasos para saberlo y ninguno requiere llamar a nadie.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca miró un registro: si logra encontrar por qué se le cierra una aplicación y lo puede contar en seis líneas, el capítulo sirve.

Y dalo a alguien que lleva años manteniendo aparatos: si no encuentra al menos un dato que no supiera —que el modo seguro se entra con la tecla de bajar volumen y separa el culpable, que «conectado sin internet» es un fallo de resolución de nombres y no de enlace, que hay dos capas de permisos y la segunda está escondida, que el panel de batería reparte culpas por tiempo y no por consumo, que el permiso denegado se ve en el registro con su paquete—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Van del registro al parte de avería: el lector del registro del sistema, el medidor de espacio, el inspector de permisos, el analizador de la red inalámbrica, el medidor de batería y, al final, el programa de escritorio que junta todo cuando el aparato ya no ayuda. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas y sus licencias.
