# Capítulo 12 · El oficio

## Qué vas a poder hacer al terminar

Verificar por tu cuenta lo que esta guía afirma. No creerme: comprobarme. Al terminar este capítulo vas a poder leer la licencia de un proyecto sin que nadie te la cuente, medir su salud con un número que se puede repetir, comprobar que un archivo es el que su autor firmó, mirar qué lleva dentro un paquete, consultar la fuente sin pasar por una página web y revisar el cifrado de tus propios servidores.

Y algo que no se compra ni se descarga: **criterio**. Saber cuándo una herramienta está viva y cuándo sólo parece viva; cuándo una estrella significa algo y cuándo es una campaña; cuándo un proyecto merece que le pongas tus datos encima.

## La regla que ordena el capítulo: una afirmación sin fuente es una opinión

Todo lo que se dijo en once capítulos —que este programa es libre, que aquel proyecto sigue vivo, que esta entrega es de tal fecha, que ese permiso hace tal cosa— tiene detrás una fuente que se puede abrir. Ese es el único mérito de esta guía: **no pide fe**.

De ahí salen las tres reglas del oficio, y con ellas termina la serie:

1. **La fuente primaria manda.** El repositorio de quien hizo el programa está por encima de la tienda, la tienda por encima del blog, y el blog por encima del video. Cuando dos fuentes se contradicen, gana la que produce el archivo.
2. **Lo que no se puede comprobar se dice.** «No lo pude comprobar» es una respuesta honesta; «seguramente sí» no lo es.
3. **El número sin fecha no es un número.** Cien mil estrellas de hace tres años no dicen nada de hoy. Toda señal de esta guía lleva el día en que se midió, y por eso cada ficha cierra con una fecha.

## Las seis preguntas que se hacen antes de instalar

Este es el método completo, el mismo que se usó para las setenta fichas. Seis preguntas, en este orden, y ninguna se salta:

1. **¿Quién lo hizo y dónde está su casa?** Un repositorio con nombre y apellido, no una página de descargas.
2. **¿Con qué licencia?** Escrita y legible. Sin licencia no hay permiso para nada, por bueno que sea el programa.
3. **¿Se movió este año?** Última entrega, cambios recientes, gente distinta empujando.
4. **¿Se puede bajar hoy y comprobar lo que bajaste?** Una entrega con archivo y, si hay suerte, con su huella o su firma.
5. **¿Quién responde cuando algo se rompe?** Incidencias contestadas, un canal de seguridad, un equipo detrás.
6. **¿Qué precio tiene en datos y en dependencias?** Qué pide, a qué llama, y de cuántas piezas ajenas cuelga.

Las seis se contestan en diez minutos con las herramientas de este capítulo y se contestan igual el año que viene. Eso es un criterio: un método que otra persona puede repetir y discutir.

## Licencia: el permiso que nadie lee

La licencia es lo primero porque es lo único que convierte un programa en algo que podés usar sin pedir permiso. Y es lo que casi nadie mira: se instala, se usa, y el archivo de texto que dice qué se puede hacer queda sin abrir para siempre.

Tres cosas cambian la vida según la licencia, y conviene tenerlas claras antes de construir encima de algo:

- **Permisiva** (MIT, Apache-2.0, BSD): podés usar el código en lo que quieras, incluso cerrado, conservando el aviso de autoría. Es la licencia de casi todas las herramientas de este capítulo.
- **Copyleft** (GPL, AGPL): si lo modificás y lo distribuís, tenés que publicar tu versión con la misma licencia. La AGPL añade: también si lo ofrecés como servicio por red.
- **Dual** (libre más comercial): el mismo código con dos puertas, una gratis con obligaciones y otra de pago sin ellas. APKiD, en este capítulo, es así.

Y una cuarta cosa que no es una licencia pero se comporta como tal: el proyecto que no tiene ninguna. En ese caso la ley es clara y contraintuitiva: **sin licencia no hay permiso**, ni siquiera para copiar el archivo. Cuando en esta guía aparece un proyecto así, se dice y no entra.

Para medir esto a escala existe **OSS Review Toolkit**: analiza un proyecto entero, encuentra las licencias de sus dependencias —que también tienen dueño— y produce el informe que hace falta para cumplir. Es la herramienta que usan las empresas que de verdad respetan el crédito ajeno, y sirve igual para una persona sola que quiere saber de qué está hecho lo que instala.

## Salud: el número que se puede repetir

**OpenSSF Scorecard** hace una sola cosa y la hace bien: le hace dieciocho preguntas a un repositorio y devuelve un número. ¿Están las dependencias fijadas? ¿Los flujos de integración piden los permisos mínimos? ¿Hay revisión antes de fusionar? ¿Hay archivo de seguridad? ¿Se firman las entregas?

Lo importante no es el número: es que **cualquiera puede correrlo y obtener el mismo**. Eso convierte una discusión de opiniones en una discusión sobre hechos, y es exactamente lo que esta guía intentó hacer con su propio baremo en cada ficha.

Una advertencia de oficio: el número mide **prácticas**, no calidad del programa. Un proyecto pequeñísimo y excelente puede sacar menos que uno grande y descuidado que sólo sigue las modas de la industria. Se lee como lo que es: una señal, no un veredicto.

## Firma: la diferencia entre bajarlo y saber de quién es

Una entrega sin firma es un archivo en un servidor. Con firma es un archivo del que se puede decir quién lo publicó y cuándo. La forma moderna de esto se llama **Sigstore**: el que publica firma con su identidad de siempre, la firma queda anotada en un registro público que sólo crece, y cualquiera puede comprobar después que ese archivo existía ese día y salió de esa cuenta.

**cosign** es el programa que hace esa comprobación. Y su primera consecuencia es filosófica: **una firma no se puede fechar hacia atrás**. Si mañana alguien publica un archivo diciendo que es de la semana pasada, el registro lo desmiente.

Del otro lado está el oficio viejo, el de las huellas: un archivo con la suma de verificación publicado junto a la entrega. No dice quién lo hizo, pero dice si lo que tenés es lo que se publicó. Las dos cosas son mejores que nada, y la segunda es la que esta guía pudo comprobar en la mayoría de sus setenta fichas.

## Contenido: qué lleva dentro un paquete

**APKiD** responde una pregunta que casi nadie se hace: ¿cómo se hizo este archivo? Identifica compiladores, empaquetadores y ofuscadores, es decir, las herramientas con las que alguien construyó la aplicación.

Sirve para dos cosas opuestas y las dos importan. Para **defenderte**: un paquete popular reconstruido por un tercero suele llevar un empaquetador que el original no tenía, y eso es una señal de alarma. Y para **entender**: saber que una aplicación está protegida explica por qué no se puede leer con las herramientas del capítulo 10, y evita conclusiones falsas.

APKiD es el único proyecto de la guía con doble licencia: GPL-3.0 para uso libre o una comercial para quien no quiera las obligaciones del copyleft. Se declara tal cual, y su nota —treinta y uno— es la más baja del capítulo por razones de equipo y de huellas, no por su utilidad.

## La fuente sin intermediarios

**GitHub CLI** es la línea de órdenes de la plataforma donde vive casi todo lo de esta guía. Con una orden se piden los datos que una página web te muestra con adornos: la última entrega, su fecha, sus archivos, sus descargas, las incidencias abiertas.

Su valor para el oficio es que **elimina al intermediario**. Cuando alguien dice «esta aplicación ya no se actualiza», la orden contesta con una fecha. Cuando alguien dice «tiene un millón de descargas», la orden contesta con el número exacto y el día en que se contó. Todas las señales de las setenta fichas de esta guía salieron de órdenes como esta, y cualquiera puede repetirlas.

## Tu servidor también se comprueba

El oficio no termina en el teléfono. Todo lo que se montó en los capítulos 7, 8 y 9 —copias, servidores, la casa— está expuesto a internet, y su cifrado se puede revisar con **testssl.sh**: un solo archivo de órdenes de sistema que habla con el servidor como hablaría un atacante y cuenta qué protocolos acepta, qué cifrados ofrece, si el certificado es válido y si hay algo viejo encendido que no debería estar.

Corre en Linux, macOS y en Windows con el entorno adecuado; no necesita instalar nada en el servidor ni tener acceso a él. Y su resultado es de los que se guardan: una línea de base de cómo estaba todo el día que lo revisaste, para comparar dentro de seis meses.

## La ruta de decisión, en seis preguntas

**¿Necesito saber de qué está hecho un proyecto y qué licencias arrastra?** → **OSS Review Toolkit**.

**¿Necesito saber si un proyecto está bien mantenido, con un número que otros puedan repetir?** → **Scorecard**.

**¿Necesito comprobar que un archivo lo publicó quien dice?** → **cosign**, cuando el proyecto firma; y la huella publicada cuando no.

**¿Necesito un dato exacto de una entrega, sin abrir el navegador?** → **GitHub CLI**.

**¿Necesito saber cómo se construyó un paquete y si lo tocó un tercero?** → **APKiD**.

**¿Necesito revisar el cifrado de mi servidor?** → **testssl.sh**.

## El crédito: cómo se nombra a quien hizo

Esta guía entera existe porque alguien, sin cobrar, escribió el programa. El crédito no es un adorno legal: es la única moneda que tiene ese trabajo.

Se nombra con cuatro datos, y los cuatro van juntos: **quién** (persona u organización, con el nombre que usa), **qué licencia**, **qué versión** y **qué día se midió**. Un crédito sin fecha envejece mal; un crédito sin licencia no informa; un crédito sin nombre no agradece.

Y después hay una parte que no se escribe en ninguna ficha y es la que de verdad sostiene el ecosistema: **devolver**. Reportar un fallo con un parte que sirva —capítulo 11—, traducir una cadena de texto, contestar a alguien en un foro con la respuesta exacta, mandar diez pesos al que mantiene la herramienta que usás todos los días. Nada de eso es obligatorio y todo eso es lo que hace que el próximo año siga habiendo qué instalar.

## La raya legal, otra vez y por última vez

Esta guía recomienda software libre y explica cómo comprobarlo, cómo instalarlo y cómo repararlo. No reparte programas ajenos, no aloja archivos que no le pertenecen y no enseña a saltarse pagos. Cuando un programa se puede usar para copiar contenido sin permiso —los lectores de manga, los reproductores, los analizadores de red— se dice qué hace y se deja la decisión, con su consecuencia, en manos de quien lo usa.

Lo que sí hace, y lo hace sin ambigüedad: **nombrar a todos los autores, con su licencia, su versión y su fecha**. Eso es lo que separa una guía de un catálogo de enlaces.

## Lo que dejé fuera, y por qué

Dos herramientas se quedaron afuera de este capítulo y las dos por el mismo motivo, que es el método del capítulo aplicado a mí mismo.

La primera es un comparador de archivos que muestra, línea por línea, en qué se diferencian dos paquetes. Es la herramienta perfecta para responder «¿este archivo es el mismo que el del repositorio?» y **no tiene su casa en la plataforma que esta guía mide**: pedirla en el sitio equivocado es exactamente el error que el capítulo 4 enseña a no cometer.

La segunda es un gestor de llaves de cifrado para el teléfono, el clásico para firmar y comprobar con GPG. Tiene repositorio, tiene equipo y tiene años, y **no publica entregas ahí**: se distribuye por tiendas y por su propio sitio. Sin entrega que bajar y comprobar en la fuente que medimos, no entra.

Las dos quedarían bien en una lista de recomendaciones. Esta guía no es una lista de recomendaciones.

## Los cuatro errores que se pagan

**Confundir estrellas con salud.** Una campaña de estrellas se compra; un equipo de diez personas empujando código todas las semanas, no.

**Creer que la licencia del programa cubre todo lo que lleva dentro.** Un programa libre puede incluir iconos con otra licencia, como el medidor de batería del capítulo anterior declara en su propio archivo. Se lee el aviso completo, no el nombre de la licencia.

**Comprobar una vez y para siempre.** Todo lo que se midió en estas setenta fichas se midió el 3 de noviembre de 2026. El año que viene hay que volver a medirlo, y el método es el de este capítulo.

**Bajar de donde es más cómodo.** El buscador pone primero lo que paga publicidad, no lo que es oficial. La fuente es el repositorio, escrito por quien lo hizo.

## Tres cosas que se dicen y no son verdad

**«Si es gratis, algo esconde».** Lo que esconde un programa libre está a la vista de cualquiera que quiera leerlo, y este capítulo enseña a hacerlo. Lo que esconde uno cerrado y gratis no se puede leer: hay que confiar.

**«El código abierto no tiene dueño».** Tiene dueño, tiene licencia y tiene obligaciones. Justamente por eso se puede usar: porque alguien dejó por escrito qué permite.

**«Verificar es de desconfiados».** Verificar es el gesto de respeto más grande que existe en este oficio: el que comprueba está diciendo que el trabajo del otro merece ser mirado de cerca.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca leyó una licencia: si al terminar puede decirte con qué licencia está el programa que usa todos los días, y qué le permite, el capítulo sirve.

Y dalo a alguien que programa: si no encuentra al menos un dato que no supiera —que sin licencia no hay permiso ni para copiar un archivo, que la AGPL también obliga cuando el programa se ofrece por red, que una firma de Sigstore queda anclada en un registro público que no se puede fechar hacia atrás, que Scorecard mide prácticas y no calidad, que hay programas con dos licencias y una es de pago—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas, y el final de la serie

Van del permiso al servidor: el que ordena las licencias de todo un proyecto, el que mide la salud con un número repetible, el que comprueba firmas, el que pregunta a la fuente, el que mira dentro de un paquete y el que revisa el cifrado de lo que montaste. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas y sus licencias.

Con estas seis, la guía cierra en **setenta fichas y doce capítulos**. Setenta programas, cada uno con su autor, su licencia, su versión y su fecha; cada uno con sus manos, sus límites, lo que sale mal y cómo se deshace. No es un catálogo: es un método con ejemplos dentro.

Y una última cosa, la que de verdad importa: si dentro de un año esta guía está vieja, es porque el ecosistema siguió vivo. Ese es el objetivo. Ahora sabés medirlo tú.
