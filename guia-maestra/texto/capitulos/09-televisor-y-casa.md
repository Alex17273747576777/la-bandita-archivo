# Capítulo 9 · El televisor y la casa

## Qué vas a poder hacer al terminar

Limpiar el televisor de la publicidad y de las aplicaciones que vinieron con él, ponerle un reproductor que abra todo lo que tenés en el servidor de casa, y controlar los aparatos de tu hogar de forma que **sigan funcionando si se cae internet**.

Y vas a poder hacerte la pregunta que separa una casa inteligente de una casa alquilada: cuando se corta la conexión, ¿tu casa sigue obedeciendo? Al final del capítulo vas a tener una prueba de dos minutos para saberlo, y la vas a poder aplicar a cada aparato que compraste.

## La regla que ordena el capítulo: el televisor es un Android con mando

Un televisor moderno —Android TV, Google TV, y en buena medida los demás— es un teléfono sin pantalla táctil: mismo sistema, mismas aplicaciones, mismos paquetes, mismos permisos. Todo lo que aprendiste en los capítulos 2 y 3 se aplica igual, con dos diferencias que cambian la estrategia.

**No hay teclado.** Escribir una orden en un televisor con un mando es una tortura, y por eso el trabajo se hace desde otro aparato: desde la computadora o desde el teléfono, por red, con la misma depuración del capítulo 3.

**Hay menos que perder.** Nadie guarda su vida en el televisor. Eso lo vuelve el aparato más seguro para practicar: si algo se rompe, se restablece de fábrica y no se perdió nada. Es el sitio donde conviene aprender antes de tocar el teléfono.

Y la casa es lo contrario: no tiene pantalla, casi nunca tiene teclado, y en cambio tiene cosas que importan —la puerta, la luz, la calefacción, la cámara—. Ahí la regla es otra: **lo que controla la casa tiene que funcionar sin internet**. Un interruptor que necesita un servidor en otro país para encender la luz no es un interruptor inteligente: es un interruptor con dueño.

## La ruta de decisión, en cuatro preguntas

**Si el televisor vino con publicidad y aplicaciones que no pediste** → **TVSlim**. Conecta por red, muestra lo que hay instalado y **desactiva** en lugar de desinstalar, con un registro de cada cambio para poder volver atrás.

**Si querés ver vídeo en el televisor, desde tu servidor o desde un disco** → **Kodi** para todo lo que ya tenés en archivos, **Jellyfin** si querés un servidor que sirva a varios aparatos a la vez y recuerde por dónde ibas en cada uno.

**Si lo que te molesta son los anuncios de la aplicación de vídeos del televisor** → **SmartTube**, con una advertencia que este capítulo explica con detalle porque es un caso real de seguridad.

**Si querés que la casa obedezca sin depender de nadie** → **Home Assistant** para el cerebro y **ESPHome** para los aparatos que vos mismo construyes o reescribes.

## El televisor: lo mismo que el teléfono, desde otro sitio

La depuración por red es la puerta. En Android TV se abre igual que en un teléfono: se activan las opciones de desarrollador —en los televisores suele estar escondido en el apartado de información del aparato, tocando varias veces la versión del sistema— y se habilita la depuración por red. A partir de ahí, el televisor acepta órdenes desde la computadora o desde el teléfono, en el mismo puerto de siempre.

Esa puerta tiene las mismas reglas del capítulo 3, y una más: **la red del televisor es la de la casa**, así que esa puerta queda abierta para cualquier aparato de la red mientras esté habilitada. Se abre para trabajar y se cierra después.

Con la puerta abierta, lo que se puede hacer es exactamente lo del capítulo 2: ver qué paquetes hay, cuáles son del sistema, y **desactivar** los que no hacen falta. Desactivar no es desinstalar: el paquete sigue en el aparato, deja de ejecutarse, y la vuelta atrás es una orden. En un televisor esa distinción importa todavía más, porque el aparato no se puede rescatar con un cable: si algo se rompe, la salida es el restablecimiento de fábrica y la pérdida de todas las cuentas configuradas.

## La economía del vídeo: quién decide y quién paga

Acá hay un concepto que resuelve casi todos los problemas de este capítulo, y casi nadie lo tiene claro.

Un servidor de vídeo casero tiene que decidir, para cada reproducción, entre dos caminos: **entregar el archivo tal cual** y que el televisor lo decodifique —directo, rápido, sin gasto— o **convertirlo sobre la marcha** a un formato que el televisor entienda. La conversión, que en el oficio se llama transcodificación, la paga el servidor: procesador a fondo, calor, ventilador, y a veces ni así alcanza.

El televisor decide sin preguntar: si no entiende el códec, pide la conversión. Y ahí empieza el síntoma que la gente describe mal: «el servidor va lento», «se corta cada tanto», «la película tarda en arrancar». No es la red: es el procesador convirtiendo vídeo en tiempo real.

De esa economía salen tres reglas prácticas:

- **El formato del archivo decide quién paga.** Un archivo que el televisor entiende se sirve sin gasto; uno exótico obliga al servidor a trabajar en cada reproducción.
- **Un televisor nuevo no necesita conversión; uno viejo sí.** Y un aparato barato conectado al televisor por cable puede hacer ese trabajo mejor que el servidor.
- **Si el servidor sufre, la solución casi nunca es más procesador**: es un archivo mejor, o un reproductor que entienda el original.

## La casa: la prueba del router apagado

Esta es la prueba central del capítulo y lleva dos minutos.

Apagá el aparato que te da internet —el router— dejando encendida la red de casa. Después probá, uno por uno: encender una luz, subir una persiana, ver la cámara, abrir la puerta, leer la temperatura. Todo lo que deje de funcionar depende de un servidor que no está en tu casa.

Lo que sobrevive a esa prueba es control local. Lo que se cae, aunque sea cómodo, es una casa alquilada por mes.

La tecnología que hace posible el control local ya está resuelta y es aburrida: los aparatos hablan por la red de casa con protocolos abiertos, y el cerebro que los coordina corre en tu equipo. Lo que falta no es técnica, es decisión al comprar: **antes de comprar un aparato para la casa, preguntá si funciona sin la nube del fabricante**. No siempre se puede; casi siempre se puede saber antes de pagar.

## Los tres errores que se pagan

**Desinstalar en lugar de desactivar, en el televisor.** Sin una copia del sistema y sin poder conectar un teclado, recuperar un paquete del sistema es complicado. Desactivar da el mismo resultado en el uso diario y la vuelta atrás es instantánea.

**Poner la casa entera en una nube.** Además de la dependencia, hay un problema de vida útil: cuando el fabricante deja de mantener el servicio, el aparato deja de existir aunque siga enchufado y funcionando. Los aparatos de casa duran diez o quince años; los servicios en la nube, mucho menos.

**Automatizar antes de entender.** Una automatización que apaga la calefacción a cierta hora es magnífica hasta el día que la casa está vacía en invierno. Las reglas se escriben pensando en lo que puede salir mal, y se prueban con la mano en el interruptor.

## Una historia real que este capítulo no puede callar

La aplicación de vídeos para televisor más usada de esta guía —SmartTube, treinta y cinco mil ochocientas noventa estrellas— publica en la primera línea del archivo de presentación de su repositorio un aviso de seguridad: su entorno de desarrollo estuvo infectado por software malicioso, **algunas compilaciones pueden haber quedado afectadas**, las llaves públicas pueden haber quedado comprometidas, y desde entonces todo se analiza antes de publicar.

Está escrito por el propio autor, con el detalle suficiente para que el usuario decida: qué pasó, qué puede haber quedado afectado, qué hacer si se usó una versión afectada y cómo revocar los accesos que la aplicación pudo haber obtenido.

Esta guía lo publica tal cual, y saca tres lecciones que valen para todo lo demás:

- **La cadena de confianza llega hasta el teclado de quien compila.** No importa cuán libre sea el código: si el equipo donde se compila está comprometido, el resultado también.
- **Un aviso así es una señal de salud, no de enfermedad.** Un proyecto que publica esto se puede auditar; uno que lo esconde, no.
- **Y es la razón por la que los capítulos 4 y 7 existen.** Comprobar la firma de lo que instalás no es paranoia de manual: es la única defensa que tenés cuando el otro lado se rompe.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que acaba de comprar un televisor: si consigue quitarle la publicidad de la pantalla de inicio y entiende por qué se desactiva en lugar de desinstalar, el capítulo sirve.

Y dalo a alguien que lleva años con esto: si no encuentra al menos un dato que no supiera —que la biblioteca de Kodi vive en una base de datos y no en las carpetas, que la transcodificación la paga el servidor y no la red, que el identificador de una entidad de Home Assistant no cambia aunque le cambies el nombre, que ESPHome publica su código Python con una licencia y su código de ejecución con otra, que la aplicación de vídeos más usada del capítulo arrastra un aviso de compromiso de sus compilaciones—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Van del aparato a la casa: primero el televisor, después lo que se ve en él, y al final el cerebro y los aparatos del hogar. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas, sus licencias y sus repositorios.
