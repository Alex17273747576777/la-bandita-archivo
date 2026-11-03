# Capítulo 8 · La red

## Qué vas a poder hacer al terminar

Entrar a los servidores de tu casa desde la calle como si estuvieras sentado en el living, salir a internet desde otro lugar sin que tu proveedor sepa a qué sitios vas, y entender —sin humo— qué te da y qué no te da cada una de esas cosas.

Y vas a poder descartar lo que no hace falta. La mitad de este capítulo es una lista de cosas que la gente configura sin necesidad, paga sin necesidad o teme sin necesidad. Saber qué sobra vale tanto como saber qué poner.

## La regla que ordena el capítulo: una VPN es un túnel, no un escudo

Una red privada virtual hace una sola cosa: **mover tu tráfico dentro de un túnel cifrado entre dos extremos que vos elegís**. En un extremo estás vos; en el otro, alguien. Todo lo demás —privacidad, anonimato, saltarse un bloqueo, acceder a la casa— es una consecuencia de quién está en ese otro extremo, y no una propiedad del túnel.

De ahí salen las tres preguntas que resuelven cualquier caso, y que conviene hacerse antes de instalar nada:

- **¿Quién está en el otro extremo?** Si es tu casa, te estás dando acceso a tus cosas. Si es una empresa, le estás entregando tu tráfico a ella en lugar de a tu proveedor.
- **¿Qué querés proteger?** Lo que va por el túnel, o el hecho de que estás conectado. No es lo mismo.
- **¿De quién te protegés?** Del wifi del café, de tu proveedor, de un bloqueo, o de un sitio que quiere saber dónde estás. Cada respuesta pide una configuración distinta.

Un túnel bien puesto contesta las tres con claridad. Un túnel mal puesto deja la sensación de estar protegido y el problema intacto.

## La ruta de decisión, en cuatro preguntas

**Si querés entrar a tu casa desde afuera** —el servidor de fotos, la biblioteca, el equipo de escritorio— → **wg-easy** para empezar: es WireGuard con una pantalla web para generar los accesos. Si querés además que todos tus aparatos se vean entre sí estén donde estén, **Headscale**, que coordina los clientes oficiales de Tailscale desde tu propio servidor.

**Si lo que querés es salir a internet desde otro sitio** → un servicio de pago con cliente libre, como **Mullvad**. Y acá va la advertencia del capítulo: las redes privadas virtuales gratuitas no son gratis; alguien paga el servidor, y si no pagás vos, el producto sos vos.

**Si lo que querés es esquivar un bloqueo en tu país o en tu red** → **Hiddify** si querés algo que funcione sin entenderlo, **sing-box** si querés configurar cada detalle y saber exactamente qué regla manda cada conexión.

**Si tenés un equipo con varios aparatos y querés administrarlos como una sola red** → **NetBird**, que hace la red privada entre máquinas y además controla quién entra.

## Los tres túneles que la gente confunde

**La red privada comercial.** Te conecta a un servidor de una empresa. Te protege del wifi del café y de tu proveedor; no te protege de la empresa, que ahora ve lo que antes veía tu proveedor. No te hace anónimo, y su publicidad lo insinúa todos los días.

**La red privada hacia tu casa.** Te conecta a tu propio servidor. Ahí no hay nadie mirando: el extremo es tuyo. Es lo que sirve para entrar a tus archivos desde la calle, y es la única de las tres que mejora tu privacidad sin empeorarla en otro lado.

**El proxy.** No crea un túnel para todo el aparato: desvía conexiones concretas por otro camino, con reglas. Es más fino y más frágil, y es lo que se usa cuando lo que hay que resolver es un bloqueo y no una red entera.

Las tres ocupan el mismo recurso del teléfono: **un solo túnel de red privada por usuario**, como quedó explicado en el capítulo 5. Y eso tiene una consecuencia práctica que se sufre a diario: activar la red privada comercial **apaga** el bloqueo de anuncios, y al revés. Quien quiera las dos cosas a la vez necesita una aplicación que haga las dos —Rethink, o un proxy con reglas—, o root.

## Lo que no hace falta

Esta lista vale más que muchas recomendaciones.

**No hace falta una red privada para navegar por wifi en tu casa.** El tráfico ya va cifrado por el sitio al que entrás, salvo el nombre del sitio. Lo que se gana con un túnel casero es poco y lo que se paga en complejidad es mucho.

**No hace falta un túnel para cada objetivo.** Tres aplicaciones instaladas, una activa, dos peleándose por el mismo recurso: es el error más común que se ve en los teléfonos de la gente que se interesa por esto.

**No hace falta abrir nada a internet si el túnel alcanza.** Un servidor de casa con puerto abierto es una puerta; un túnel es una puerta que sólo se abre desde adentro. Casi todo lo que la gente abre al mundo se puede resolver con un túnel, y eso reduce el riesgo a la mitad.

**No hace falta creer que el túnel arregla el sitio que visitás.** Si entrás a un sitio con tu cuenta, ese sitio sabe quién sos, tengas túnel o no.

## Cómo se comprueba que un túnel funciona

No hay que creerle a la aplicación: hay que preguntarle al sistema y a la red.

**El túnel está arriba.** En el teléfono, el icono de llave en la barra; en la computadora, la interfaz de red que aparece. Si no está, no hay túnel, por más que la aplicación diga «conectado».

**La dirección de salida cambió.** Antes de activar, anotá la dirección con la que te ve internet; después de activar, mirala otra vez. Si es la misma, el túnel no está pasando tu tráfico.

**El otro extremo contesta.** Si el túnel va a tu casa, pedile algo a un equipo de tu casa. Si contesta, el túnel sirve para lo que lo pusiste; si no, tenés una conexión que existe y no lleva a ninguna parte.

**La prueba del corte.** Desconectá el túnel y comprobá que el acceso a tu casa se corta. Un túnel que no se nota al apagarlo es un túnel que no estaba haciendo nada.

## Los cuatro errores que se pagan

**Abrir puertos por comodidad.** El servidor de fotos con el puerto abierto a internet es la forma más común de perder una biblioteca entera: los escaneos automáticos encuentran esos puertos en horas, no en meses. El túnel existe para no tener que hacerlo.

**Dejar el túnel abierto en redes ajenas sin límites.** Un túnel hacia tu casa desde el wifi de un hotel es un camino abierto en las dos direcciones: mientras está activo, también se puede entrar a tu casa por ahí si las reglas están mal puestas.

**Guardar las llaves en el chat.** Las configuraciones de estos programas son llaves: quien la tiene, entra. Se comparten por un canal que se pueda borrar y se revocan cuando alguien deja de necesitarlas.

**Confiar en el «no registra nada».** Un servicio puede no guardar registros y aun así verte en tiempo real. La afirmación que vale es la que se puede auditar, y por eso el capítulo 5 existe.

## Una nota sobre las licencias, que acá importa

Tres de las seis fichas de este capítulo declaran licencias que no son un simple nombre, y conviene leerlas antes de adoptar el programa en serio.

**Hiddify** se publica bajo la licencia pública general de GNU **con condiciones adicionales** al amparo de su sección 7: no es exactamente GPL a secas, y el proyecto lo dice en la primera línea de su archivo de licencia. **sing-box** es GPL, pero su rama principal se llama `testing` y sus entregas son versiones de prueba: quien instala la última está usando software en movimiento. Y **NetBird** aplica una licencia permisiva a la mayor parte del repositorio **excepto** a las carpetas del servidor de administración, la señalización y el relé, que van bajo una licencia copyleft fuerte.

Ninguna de las tres es una trampa: son formas legítimas de publicar. Lo que no es legítimo es un catálogo que escriba «open source» y no diga cuál de las tres es. Esta guía la escribe, y el dato está en cada ficha con su enlace al archivo.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca configuró una red privada: si consigue entrar a una carpeta de su computadora desde el teléfono con los datos móviles, y sabe explicar por qué eso no es lo mismo que contratar una red privada comercial, el capítulo sirve.

Y dalo a alguien que administra redes: si no encuentra al menos un dato que no supiera —que Tailscale se puede usar con un servidor propio porque su protocolo está reimplementado en Headscale, que Hiddify publica una GPL con condiciones adicionales, que la rama principal de sing-box es la de pruebas, que NetBird separa la licencia por carpetas, que sólo hay un túnel por usuario y por eso todo se pelea con todo—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Van de lo más simple a lo más fino: primero entrar a tu casa, después salir de la tuya, después esquivar un bloqueo, y al final administrar una red entera. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas, sus licencias y sus repositorios.
