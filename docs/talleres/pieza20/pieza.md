*El teclado que obedece: once teclados clonados y leídos esta mañana —dos que llevan tus instrucciones dentro, nueve que no, y veintidós textos que pasan once comprobaciones*

*La Bandita · jueves 5 de noviembre de 2026, 06:41 de la mañana en Santo Domingo (10:41 UTC) · edición dominicano-español · pieza 20 de Facebook*

⏱️ *Lectura total: 24 minutos · once repositorios clonados entre las 10:16 y las 10:41 UTC · dos teclados con ejecución de instrucciones · diez teclas de IA medidas en el código · veintidós textos y cinco macros · once comprobaciones ejecutadas · quince fallos corregidos en el primer borrador*

*🗺️ Mapa de esta guía*

```
├── 🧱 La semilla · setenta y cinco comandos que no caben en ningún teclado
├── ⚡ En una página · 🕰️ la medición de las 06:41
├── 📱 Los once teclados · qué hace cada uno, con la prueba en el código
├── 🔟 El techo de diez · lo que el teclado admite y lo que no
├── ✍️ Los veintidós textos · ocho ejemplos completos y por qué están escritos así
├── 🔧 Cuatro errores que hunden un prompt · y 📲 cómo se configuran las diez teclas
├── 📐 El catálogo de contratos · 🩺 cuando la tecla responde mal
├── 🧪 Las once comprobaciones · y los quince fallos que salieron del primer borrador
├── 🗂️ El taller en Git · cuatro programas, un JSON y un script que pone al día los créditos
├── 🔐 Lo que cuesta de verdad · privacidad, batería y el modelo que ve tu texto
├── 🚫 Lo que no funciona aquí · deuda declarada con nombre
└── ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

───────────────────

*🧱 La semilla · setenta y cinco comandos que no caben en ningún teclado*

Circula un texto que promete setenta y cinco comandos dentro del teclado, una «armadura universal» que obliga a la IA a callarse y un «100 % de obediencia forzada». Tiene una cosa buena —no usa tablas de Markdown, que en un teléfono son un castigo— y una cosa peor que fea: **casi todos sus números son inventados**.

No hace falta creerlo ni desmentirlo por intuición. Se clona el teclado que ese texto está describiendo y se mira el código. LeanType es un teclado libre para Android, derivado de HeliBoard, con dos funciones que el texto menciona pero no entiende: **teclas de IA configurables** y un **expansor de texto**. En su código hay literalmente diez teclas: `CUSTOM_AI_1` hasta `CUSTOM_AI_10`, una por cada acción que el teclado puede disparar. Diez, no setenta y cinco.

Y las «etiquetas mágicas» que el texto vende como un hallazgo —#resultonly, #append, #proofread, #summarize, #adjusttone, #generate— son la lista de **palabras clave del propio teclado**, que está en sus cadenas de texto traducidas y que se configura desde sus ajustes. El texto no descubrió nada: copió la pantalla de ajustes y la presentó como método.

Queda la pregunta que importa, y es la que esta pieza intenta responder: **si un teclado solo puede guardar diez instrucciones, cómo se organiza el trabajo de verdad**. La respuesta no es setenta y cinco atajos sin criterio. Es diez teclas que hacen lo que se repite todos los días, un puñado de atajos largos para cuando la instrucción no cabe en una tecla, y un sistema que **viva en Git** para que no se pierda cuando cambies de teléfono.

───────────────────

*⚡ En una página*

Se clonaron **once teclados** y se buscó la función en el código, no en la descripción del repositorio. Resultado: **dos ejecutan instrucciones** (LeanType, con diez teclas, y Deskdrop, con modelos locales de Ollama) y **dos expanden texto** (LeanType y AnySoftKeyboard). Los otros siete —HeliBoard, FlorisBoard, Unexpected Keyboard, Thumb-Key, Trime, Fcitx5, Simple Keyboard, y el FUTO que GitHub marca con licencia NOASSERTION porque usa una suya— **no llevan nada de eso**: son teclados, y punto. Eso no los hace peores; los hace otra cosa.

La biblioteca que sale de aquí tiene **veintidós textos y cinco macros**: diez teclas de IA (el máximo que el teclado admite), doce atajos largos para pegar donde haga falta y cinco macros que no gastan un solo token. Cada texto mide entre 221 y 300 caracteres, y esa franja no es casual: por debajo de 200 el modelo rellena con lo que le parece, y por encima de 400 la tecla se vuelve un párrafo que no se puede revisar en la pantalla del teléfono.

Los textos pasan **once comprobaciones** ejecutables: destino válido, tope físico, longitud, verbo en imperativo, contrato de salida, cero cortesía, cero marcadores sin resolver, cero promesas imposibles, cero duplicados por parecido, idioma libre y atajos con forma. En el primer borrador salieron **quince fallos** —siete textos sin contrato de salida y cuatro que empezaban hablando de sí mismos en vez de dar una orden—. Se corrigieron uno por uno; el programa que los encontró está en el repositorio y se puede volver a ejecutar.

Y el detalle que separa esto de una lista de prompts: **la biblioteca no vive en una publicación, vive en un archivo**. `prompts.json`, con once comprobaciones que lo vigilan, tres exportadores que la convierten al formato de cada teclado y un sincronizador que pone al día las versiones y los créditos preguntando a GitHub. Si mañana el teclado cambia de dueño, el archivo no se entera y sigue sirviendo.

───────────────────

*🕰️ La medición de las 06:41 · clonar antes de escribir una línea*

La fecha se comprobó en vivo al empezar —revisión de historial y de ecosistema, como manda la casa— y otra vez al cerrar. El reloj de fuera dio las **10:41 UTC**, que en Santo Domingo son las **06:41**.

Once `git clone --depth 1`, uno por teclado, entre las 10:16 y las 10:41. Cada clon pesó entre **5,6 MB y 311 MB** —AnySoftKeyboard es el grande, porque arrastra diccionarios de todos sus idiomas— y **ninguno se quedó en el disco**: se lee, se anota lo que se encuentra y se borra. Lo que queda es `FUENTES.json`, con la evidencia de cada función, y `VERSIONES.json`, con la última entrega etiquetada de cada proyecto.

El método fue siempre el mismo, y es el que faltaba en el texto que circula. **Primero** se busca la función en el código con tres familias de palabras —expansión, texto rápido, IA— y se anota el archivo donde aparece. **Segundo** se lee ese archivo para ver qué hace de verdad, porque una coincidencia de texto no es una función. **Tercero** se cuenta lo que hay: teclas, palabras clave, entradas. **Cuarto** se pregunta a la API por la licencia, el último empujón y la última entrega, para que la ficha diga también cuándo se comprobó.

**La búsqueda encuentra lo que alguien escribió en un README; el clon encuentra lo que el programa hace.** Tres ejemplos. AnySoftKeyboard tiene textos rápidos desde hace años y su formato real es un add-on compilado con un `QuickTextKeys` lleno de `QuickTextKey`, no una lista que se pega en un cuadro de texto. FlorisBoard, con ★8.755, no expande frases: su diccionario de usuario llega a la palabra y se acaba ahí. Y el teclado de FUTO, que sí es serio y tiene ★3.440, usa una licencia propia —FUTO Source First 1.1— que GitHub marca como NOASSERTION porque no es una licencia estándar: quien lo reutilice tiene que leerla, no suponerla.

───────────────────

*📱 Los once teclados · qué hace cada uno, con la prueba en el código*

Las fichas van con lo que se vio dentro. «Ejecuta» significa que el teclado puede mandar una instrucción a un modelo; «expande» significa que convierte un atajo en un texto largo; «—» es que no se encontró la función en el código.

```
TECLADO            ★        LICENCIA      EJECUTA  EXPANDE  MADUREZ
LeanType           ★1.143   GPL-3.0       sí (10)  sí       1 día
Deskdrop              ★59   GPL-3.0       sí       —        198 días
AnySoftKeyboard    ★3.393   Apache-2.0    —        sí       58 días
HeliBoard          ★6.501   GPL-3.0       —        —        24 días
FlorisBoard        ★8.755   Apache-2.0    —        —        342 días
Unexpected Kbd.    ★3.337   GPL-3.0       —        —        4 días
Thumb-Key          ★1.572   AGPL-3.0      —        —        3 días
Trime              ★4.771   GPL-3.0       —        —        4 días
Fcitx5 Android     ★5.842   LGPL-2.1      —        —        102 días
FUTO Keyboard      ★3.440   FUTO SFL 1.1  —        —        93 días
Simple Keyboard    ★1.607   Apache-2.0    —        —        14 días
```

La madurez se cuenta como días desde la última entrega etiquetada: no dice si el proyecto es bueno, dice si alguien lo tocó hace poco. FlorisBoard lleva 342 días sin entrega y sigue siendo el más popular de la lista; LeanType entregó ayer y tiene ★1.143. Las dos cosas son verdad a la vez y ninguna decide por sí sola.

**LeanType · el único que hace las dos cosas.** Fork de HeliBoard, ★1.143, GPL-3.0, empujón de hoy mismo. En `InputLogic.kt` están las diez teclas (`CUSTOM_AI_1` a `CUSTOM_AI_10`); en `strings.xml`, las diez palabras clave con su descripción oficial; en `TextExpanderScreen.kt`, un expansor con prefijo opcional, patrón de expresión regular y **plantillas con marcadores** —`%clipboard%`, `%date%`, `%list%`— que convierten un atajo en el portapapeles o en la fecha de hoy. Y en `CustomAIKeyText.kt` está la clave de todo lo demás: cuando se elige una palabra clave, sus instrucciones **se ponen delante del prompt**, no detrás. Eso explica por qué un prompt que termina en «Respuesta:» sigue funcionando.

**Deskdrop · el que ejecuta en tu casa.** ★59, GPL-3.0, madurez de 198 días y un solo autor: fork de HeliBoard con IA local: habla con Ollama en tu propia red, admite Whisper para dictado y algo llamado MCP. Su asistente de modelos tiene un campo de instrucción por modelo, y avisa en la interfaz cuando un modelo trae su propio prompt incorporado y no se puede tocar. Es el teclado de quien tiene una máquina encendida en casa; sin esa máquina, no hace nada.

**AnySoftKeyboard · el de los textos rápidos de verdad.** ★3.393, Apache-2.0, décadas de desarrollo. Su función se llama QuickText y su formato está en `ime/addons/quick_text/res/xml/quick_text_keys.xml`: un `QuickTextKeys` con entradas `QuickTextKey` que llevan `keyLabel`, `keyOutputText` y `index`. No hay IA, pero se le pueden meter cientos de textos con teclas propias y teclados emergentes. La trampa: es un add-on que hay que compilar, no un archivo que se suelta.

**HeliBoard · el motor del que nacen los otros.** ★6.501, GPL-3.0, el más seguido de la lista. Tiene historial de portapapeles y una personalización de diseño enorme, y **no tiene expansor**: se buscó y no aparece. LeanType y Deskdrop son sus hijos; lo que ellos añaden, HeliBoard no lo trae.

**FlorisBoard · el más popular y el más cerrado en esto.** ★8.755, Apache-2.0, y su diccionario de usuario llega a la palabra. Para corregir cómo escribe el corrector, perfecto; para guardar una instrucción de doscientas letras, no sirve.

**Unexpected Keyboard, Thumb-Key, Simple Keyboard · teclados sin extras.** ★3.337, ★1.572 y ★1.607. Ligeros, con layouts en JSON o definidos a mano, sin una sola coincidencia de expansión. Son la prueba de que un teclado puede ser excelente sin tener nada que ver con la IA.

**Trime y Fcitx5 · motores, no teclados.** ★4.771 y ★5.842. Traen Rime y Fcitx5 a Android: diccionarios, esquemas, motores de entrada. Se les puede pedir casi cualquier cosa, pero hay que configurarlos en YAML y su diccionario de frases no se comprobó aquí: queda como deuda, no como afirmación.

**FUTO Keyboard · la licencia que hay que leer.** ★3.440, fork de AOSP LatinIME, con IA de voz propia. Su licencia es la FUTO Source First 1.1: el código se puede leer, y reutilizarlo tiene condiciones que no son las de una GPL. Quien copie de ahí sin leer, se equivoca.

───────────────────

*🔟 El techo de diez · lo que el teclado admite y lo que no*

Diez teclas. Ese es el número real, y no es una limitación tonta: una tecla de IA ocupa un hueco en la barra superior del teclado, y esa barra se ve por encima del texto que estás escribiendo. Con diez ya hay que deslizar.

El texto que circula promete setenta y cinco comandos dentro del teclado. En LeanType eso es imposible; en los demás, ni existe. Pero la pregunta interesante no es si caben, sino **si sirven**: setenta y cinco acciones en una barra que hay que recorrer con el pulgar acaban usándose tres. La cuenta que importa no es cuántas guardas, sino cuántas recuerdas sin mirar. Nadie recuerda setenta y cinco.

De ahí sale el reparto que esta biblioteca usa, y que cabe en cualquier teclado:

**Diez teclas de IA**, una por cada cosa que se hace varias veces al día sobre un texto que ya está escrito: corregir, reescribir, resumir, expandir, cambiar el tono, traducir al inglés, traducir al portugués, sacar tareas, escribir una expresión regular y dar el comando de terminal.

**Doce atajos largos**, para instrucciones que no caben en una tecla y no necesitan ejecutarse desde el teclado: revisar código, escribir el mensaje de un pull request, redactar un informe de error, pedir una consulta SQL, pedir pruebas, revisar seguridad, rescatar un repositorio de Git, comprobar una licencia, verificar datos antes de publicar, redactar un acta, escribir un correo que dice no y explicar algo sin jerga. Se escriben en cualquier parte con `;` y tres letras.

**Cinco macros sin IA**: la firma, el correo propio, un atajo para pegar el portapapeles, la fecha y el encogido de hombros. Cuestan cero tokens y responden en cero milisegundos, que es exactamente lo que hay que hacer con lo que no necesita pensar.

Ese reparto explica por qué la lista de setenta y cinco era tan larga y tan inútil: **mezclaba tres cosas** —acciones, textos que se pegan y macros— y así ni cabía ni se sabía cuál estaba haciendo qué.

Y una advertencia sobre los modelos: la tecla traduce lo que le mandes al modelo que tengas configurado. Si ese modelo está en la nube, **el texto que selecciones viaja**. Si está en tu red con Ollama, no. Ninguna palabra clave evita eso: no es un problema de instrucciones, es un problema de a dónde apunta la conexión.

───────────────────

───────────────────

*🔧 Cuatro errores que hunden un prompt · con el antes y el después*

Casi ningún prompt falla por lo que dice; falla por lo que deja abierto. Estos cuatro se repiten en todas las listas que circulan, y los cuatro se arreglan con una frase.

**El error de las dos tareas.** «Corrige y resume» no es una instrucción: son dos, y el modelo hará la que le parezca más fácil —normalmente resumir, que da menos trabajo—. Si necesitas las dos cosas, se hacen en dos teclas, en orden, mirando el resultado de la primera. Un teclado de diez teclas está pensado para eso.

**El error del texto implícito.** «Mejora esto» supone que el modelo sabe qué es «esto». Cuando la tecla manda solo el texto seleccionado, lo sabe; cuando manda el prompt y el texto, no hay problema; cuando manda el prompt a secas porque no seleccionaste nada, el modelo inventa un texto sobre el que trabajar y lo devuelve con toda la seguridad del mundo. La regla: **si el prompt no puede funcionar con el texto vacío, no es una tecla de texto**.

**El error del formato libre.** «Hazme un resumen» deja el formato a decisiones que no has tomado: ¿cuántas líneas, con viñetas, con negritas, con introducción? Un modelo conversacional elige el formato que más luce. Por eso todos los textos de esta biblioteca dicen cuántas líneas, si hay viñetas y qué va primero.

**El error del papel disfrazado.** «Actúa como un experto en marketing digital con veinte años de experiencia» no aporta información: aporta tono. Un papel sirve cuando define un criterio —«como si fueras a aprobar un cambio en producción», «como corrector de pruebas de un periódico»— porque entonces el modelo sabe qué mirar y qué ignorar. El papel que solo adula ocupa cuarenta caracteres y no cambia nada.

Y un quinto, que es de fontanería y no de redacción: **pegar un prompt de cuatro mil caracteres en una tecla de trescientos**. Por encima de cierto tamaño el texto deja de caber en el campo de la aplicación, o cabe y no se puede revisar. Los textos largos van a los atajos, que están hechos de texto y no de teclas.

───────────────────

*📲 Configurar las diez teclas · el orden importa más que el texto*

La primera vez se tarda una hora, y esa hora se hace una sola vez. La aplicación llama a esto **Custom AI Keys** —«teclas de IA personalizadas»— y a la pantalla de textos largos, **Text Expander**. Cada tecla se configura con dos cosas: la palabra clave que define el comportamiento y tu texto, que va detrás. Sin las dos, la tecla no se guarda; la propia aplicación lo dice cuando falta una.

El orden de la barra no es decorativo. Las teclas se recorren con el pulgar y las primeras son las que se ven sin deslizar, así que van por frecuencia de uso y no por categoría. Un orden que funciona:

```
1  Corregir            lo que más se usa, con diferencia
2  Reescribir claro    cuando la corrección no basta
3  Resumir en tres     para textos que llegan largos
4  Pasar a formal      trabajo y clientes
5  Sacar tareas        mensajes y reuniones
6  Traducir a inglés   la mitad de los correos
7  Traducir a port.    la otra mitad
8  El comando exacto   terminal, servidores
9  Escribir una regex  cuando hay que buscar en un registro
10 Expandir sin inv.   la que menos se usa, al final
```

Los atajos, en cambio, no se ordenan: se recuerdan por su `;` y tres letras. Doce atajos son pocos para confundirlos y suficientes para no volver a escribir una instrucción larga a mano. Si algún día son treinta, el orden deja de importar y aparece el problema contrario: el que no recuerdas no existe.

*Y una advertencia de fontanería:* al copiar los textos desde el archivo hay que llevarse también el final. Un prompt cortado por la mitad —porque el campo no admitía más o porque se seleccionó mal— no falla con un error: falla con una respuesta rara, y eso cuesta más de diagnosticar que un fallo limpio.

───────────────────

*✍️ Los veintidós textos · ocho ejemplos completos y por qué están escritos así*

Los textos están en `corpus-la-bandita/teclado/prompts.json`. Aquí van cinco enteros, con la razón de cada decisión, porque un prompt sin su razón es una receta sin el fuego.

**La tecla de corregir.** La orden de conservar la longitud es lo que separa una corrección de una reescritura.

```
Corrige ortografía, concordancia, puntuación y nada más. Conserva la voz,
el registro y la longitud. Si una frase admite dos lecturas, no la
interpretes: déjala igual y márcala con [?]. Devuelve solo el texto
corregido; si hubo cambios, añade después una línea por cambio con el
antes y el después.
```

Tres decisiones. **«Y nada más»** cierra la puerta a la mejora de estilo que nadie pidió. **«No la interpretes: déjala igual»** evita el arreglo silencioso de una frase ambigua, que es donde un corrector te cambia el sentido sin avisar. Y **«una línea por cambio»** convierte la corrección en algo revisable: si no quieres el cambio, sabes cuál borrar.

**La tecla de resumir.** Tres líneas con una función fija cada una.

```
Resume en tres líneas exactas: la primera dice qué pasa, la segunda por
qué importa, la tercera qué hay que hacer. Cada línea empieza por un
verbo. Sin viñetas ni negritas. Devuelve solo esas tres líneas; si el
texto no permite responder una, escribe N/D en esa línea.
```

«Resume en cinco puntos» deja que el modelo elija lo fácil y te devuelve cinco sustantivos. Tres líneas con etiqueta —qué, por qué, qué hacer— le obligan a decidir. El **N/D** es la pieza fina: sin él, cuando el texto no dice qué hacer, el modelo se inventa una acción para no dejar el hueco, y una acción inventada en un resumen se convierte en una tarea real en la cabeza de quien lo lee.

**La tecla de expandir, que es la que más miente.**

```
Expande el texto con detalle concreto, sin inventar cifras, fechas,
nombres ni citas. Todo lo que añadas debe poder deducirse de lo que ya
está escrito. Marca con [ampliado] cada frase nueva. Duplica la longitud
como máximo.
```

Expandir es la única tecla que, por definición, añade algo que no estaba. Prohibir el invento del todo la dejaría sin oficio; así que se prohíben las cuatro cosas que no se pueden deducir —cifras, fechas, nombres, citas— y se pide la marca. La marca no evita el invento: **lo deja a la vista para borrarlo**, que es todo lo que se puede hacer sin leerlo entero.

**La tecla de las expresiones regulares.** Con casos de prueba, porque una regex sin pruebas no se puede comprobar.

```
Escribe una expresión regular para lo que se pide. Devuelve tres
bloques: el patrón, tres cadenas que deben coincidir y dos que no, y una
línea por grupo explicando qué captura. Sin motor concreto, usa sintaxis
compatible con PCRE y di dónde falla en JavaScript.
```

Pedir las dos cadenas que **no** deben coincidir es lo que convierte la respuesta en algo que se puede probar en diez segundos. Y la nota del motor evita el clásico: una regex que funciona en el navegador y revienta en `grep` porque usa una construcción que solo existe en JavaScript.

**Un atajo largo: revisar código.** Este no cabe en una tecla, y por eso es un atajo.

```
Revisa este código como si fueras a aprobar un cambio en producción.
Ordena los hallazgos por gravedad. Para cada uno: archivo y línea, qué
se rompe en un caso real, y el parche mínimo. Devuelve solo la lista; si
no hay nada grave, dilo y señala las dos cosas que no se pueden
comprobar sin ejecutar.
```

«Como si fueras a aprobar un cambio en producción» cambia el registro de la respuesta entera: sin esa frase, la mitad de las revisiones automáticas son comentarios de estilo. «Qué se rompe en un caso real» obliga a un escenario, no a una categoría. Y la última frase —**decir lo que no se puede comprobar sin ejecutar**— es la que hace honesta la revisión: un modelo que afirma «esto funciona» sin poder ejecutarlo está adivinando con buena letra.

**Un atajo para el informe de error.** El que se pega en la incidencia de cualquier repositorio.

```
Convierte esto en un informe de error reproducible: versión y sistema,
pasos numerados que fallan, resultado esperado, resultado obtenido y la
primera línea del registro que lo delata. Devuelve solo el informe. Si
falta la versión, escribe FALTA en vez de suponerla.
```

La orden de **no suponer la versión** es la que evita el informe inútil: un informe con una versión inventada hace que quien lo lea busque el fallo en el sitio equivocado. Escribir FALTA cuesta una pregunta; suponer cuesta tres días.

**Un atajo para comprobar una licencia antes de copiar código.**

```
Separa, con esta licencia y este uso: si puedo reutilizar el código, qué
obligaciones me impone al distribuir, si puedo cambiar la licencia y qué
debo poner en los créditos. Devuelve solo esos cuatro puntos, cita la
cláusula en la que te apoyas y di lo que no puedes afirmar sin un abogado.
```

Cuatro preguntas concretas en vez de «explícame esta licencia». Y la última frase —**lo que no se puede afirmar sin un abogado**— separa lo que es información de lo que es consejo, que es justo donde una IA se pone a opinar con demasiada seguridad.

**Un atajo para verificar datos antes de publicar.**

```
Revisa estas afirmaciones y separa las que tienen fuente de las que no.
Para cada una: la fecha del dato, la fuente que lo sostiene y qué
cambiaría si el dato tuviera un año más. Marca con NO VERIFICADO todo lo
que no puedas comprobar hoy, y no rellenes huecos con estimaciones.
```

«Qué cambiaría si el dato tuviera un año más» es la pregunta que desmonta la mitad de las cifras que circulan: una estrella, un recuento o un precio de hace un año no es falso, es viejo, y casi siempre se presenta como de hoy.

*Lo que NO lleva ninguno de los veintidós:* ni «actúa como un experto» genérico, ni «eres el mejor», ni listas de adjetivos sobre lo bueno que es el modelo. Los papeles se dan con una tarea concreta («corrector de pruebas de un periódico», «como si fueras a aprobar un cambio»), porque un papel sin contexto es un disfraz. Y ninguno lleva la palabra «por favor»: no es descortesía, es que una instrucción condicional invita a conversar.

───────────────────

*📐 El catálogo de contratos · las frases que deciden una respuesta*

Un contrato de salida no es una fórmula mágica: es la frase que impide que el modelo elija el formato. En los veintidós textos hay cinco familias, y cada una resuelve un problema distinto. Estas son, con lo que previene cada una y cuántas veces aparece en la biblioteca.

**«Devuelve solo…» — 15 de 22.** La más usada y la que más cambia el resultado. Sin ella, el modelo abre con «¡Claro! Aquí tienes la corrección:» y cierra con «Espero que te sirva». Con ella, devuelve el texto y se calla. Su variante fina es decir **qué** devuelve: no «devuelve solo el resultado», sino «devuelve solo esas tres líneas», porque entonces el formato también queda cerrado.

**«Una línea por…» — 3 de 22.** Sirve para lo que tiene partes: un cambio de corrección, una opción de comando, un hallazgo de revisión. Obliga a una estructura repetible, y una estructura repetible se puede leer en diagonal. Cuando el modelo elige la estructura, la cambia a mitad de la respuesta.

**«Si no hay…, escribe NINGUNA» — 3 de 22.** La más importante de todas y la que casi nadie pone. Sin ella, un modelo al que le pides tareas de un texto sin tareas **inventa tareas** antes que devolver una lista vacía: prefiere cumplir el encargo a decir que no había nada que hacer. El hueco explícito —NINGUNA, N/D, FALTA— le da permiso para no rellenar.

**«Máximo / como máximo» — 2 de 22.** Para lo que tiene tope numérico: longitud, palabras, líneas. Un límite blando («breve») se interpreta de diez maneras; un número, de una.

**«Di lo que no puedes comprobar» — 3 de 22.** La única que no habla del formato sino de la honestidad. En una revisión de seguridad, en una de licencias o en una de código, la respuesta vale más por lo que declara no saber que por lo que afirma. Un modelo al que no se le pide esto tiende a terminar con una conclusión segura aunque no haya podido comprobar nada.

Y la frase que **no** aparece ni una vez, a propósito: «sé creativo». No significa nada, no restringe nada y no se puede comprobar. Cuando hace falta soltura se pide algo concreto —«un ejemplo con números pequeños», «tres metáforas visuales»—, que al menos se puede evaluar al leerlo.

───────────────────

*🩺 Cuando la tecla responde mal · cinco síntomas y su arreglo*

**Devuelve charla antes y después de la respuesta.** La palabra clave de «solo resultado» no está activa, o el modelo está configurado para conversar. Se comprueba en tres segundos: mira si la tecla tiene la palabra clave puesta y si el prompt empieza con un verbo. Si las dos cosas están bien y sigue pasando, el modelo es el problema, y se arregla cambiando de modelo, no de texto.

**Duplica el texto en vez de reemplazarlo.** Está activa la palabra clave de añadir resultado, que pega la respuesta **debajo** del original. Es correcta para responder un mensaje largo y es un desastre para corregir. Se cambia a la de solo resultado y se vuelve a configurar la tecla.

**Corta el texto o lo alarga sin que se lo pidas.** Falta la orden de conservar la longitud. Es el fallo más caro porque es invisible: el resultado parece bueno y ya no dice lo mismo que el original.

**Devuelve una lista de tareas que no estaban en el texto.** Falta el hueco explícito: sin «si no hay tareas, escribe NINGUNA», el modelo rellena. Se añade la frase y se prueba con un texto sin tareas, que es justo el caso que falla.

**Contesta en español un texto en inglés.** El prompt fija el idioma. Se quita la frase y se deja que el texto lo decida; solo los dos atajos de traducción nombran un idioma de destino, y por eso son los únicos que lo hacen.

───────────────────

*🧪 Las once comprobaciones · y los quince fallos que salieron del primer borrador*

Un texto de instrucciones se puede revisar a mano, y así se hace casi siempre. El problema es que a la tercera revisión ya no ves lo que escribiste: ves lo que quisiste escribir. Por eso la biblioteca pasa por un programa, `tools/lint_teclado.py`, que hace once preguntas que se pueden leer y que no dependen de ninguna opinión.

**T01 · destino.** ¿Cada entrada declara si es tecla, atajo o macro? Una instrucción sin destino es un texto que se copia y se pega mal.

**T02 · tope físico.** ¿Caben las teclas en el teclado? El programa compara con diez, el número medido en LeanType. Si mañana otro teclado admite más, se cambia el número en una línea y el resto sigue igual.

**T03 · longitud.** Teclas hasta 400 caracteres, atajos hasta 700. Por debajo de 200 el modelo rellena con lo que le parece; por encima de 400 el texto ya no se puede revisar en una pantalla de teléfono, y lo que no se revisa se pega sin leer.

**T04 · arranque.** ¿La primera palabra es un verbo en imperativo? «Estoy en este estado de git» no es una instrucción, es un relato; «Da el comando exacto» sí. En el primer borrador, **cuatro textos** empezaban contando algo.

**T05 · contrato de salida.** ¿Dice qué devuelve y qué no? Sin contrato, el modelo elige el formato, y el formato por defecto de un modelo conversacional es un párrafo de cortesía con la respuesta dentro. **Siete textos** no lo tenían en el primer borrador; es el fallo más frecuente con diferencia.

**T06 · cortesía.** ¿Pide las cosas por favor, o con un condicional? «Si puedes, revisa» deja abierta la posibilidad de no hacerlo; un modelo no la usa, pero gasta atención en decidir.

**T07 · marcadores sin resolver.** Nada de `TODO`, `XXX` ni `<>` vacíos. Un prompt con un hueco sin rellenar se ejecuta igual y produce basura con forma de respuesta.

**T08 · promesas imposibles.** Prohibidas «100 %», «infalible», «garantizado», «perfecto». No cambian el resultado y sí cambian la confianza de quien lo lee, que es peor.

**T09 · parecido.** Dos textos con más del 75 % de palabras en común son el mismo texto con otro nombre. Se comparan todos contra todos, y el que se parece a otro se queda fuera aunque parezca bueno.

**T10 · idioma.** Ningún texto fija el idioma de salida salvo los dos de traducción. Si escribes en español y la instrucción dice «responde en español», en cuanto pegues un texto en inglés obtendrás español: el idioma debe seguirlo el texto, no la tecla.

**T11 · forma de los atajos.** `;` y entre dos y ocho letras, sin repetirse. Un atajo de nueve letras se escribe más despacio que la palabra que sustituye.

Ejecutado sobre el primer borrador, el programa devolvió **quince fallos**: siete por contrato de salida, cuatro por arrancar sin verbo y cuatro por detalles de forma. Se arreglaron uno a uno y la segunda pasada salió limpia. Eso es lo que un recuento honesto puede decir de una biblioteca de instrucciones: **que cumple sus propias reglas**. Lo que no puede decir —y nadie debería decirlo— es que el modelo vaya a obedecer.

───────────────────

*🗂️ El taller en Git · cuatro programas, un JSON y un script que pone al día los créditos*

Lo que queda es una carpeta del repositorio, `corpus-la-bandita/teclado/`, con todo lo necesario para rehacer esto sin volver a empezar.

**`prompts.json`** es la biblioteca. Veintidós textos y cinco macros, cada uno con su identificador, su nombre, su palabra clave y una línea que explica **por qué** está escrito así. Esa última línea es la que casi nunca se guarda y la que se necesita dentro de seis meses.

**`tools/lint_teclado.py`** es el revisor: las once comprobaciones y nada más. Se ejecuta sin dependencias, tarda menos de un segundo y devuelve 1 si algo falla, así que puede entrar en cualquier cadena de comprobación. Con `--exportar`, además, escribe los formatos de cada teclado.

**`tools/sync_fuentes.py`** es el que evita el trabajo aburrido. Lee `FUENTES.json` —once teclados, su papel y la evidencia de cada función—, pregunta a GitHub por cada repositorio y por su última entrega, y reescribe `VERSIONES.json` y `CREDITOS.md`. Cuando una licencia declarada no coincide con la que devuelve GitHub, avisa. Los créditos de esta carpeta no se escriben a mano: se generan, y llevan la fecha de la consulta.

**Los tres exportadores** convierten la misma biblioteca en tres cosas distintas sin copiar y pegar: un archivo con las diez teclas numeradas para LeanType, un archivo con los diecisiete atajos del expansor —doce largos y cinco macros— y un fragmento XML con el esquema real de `QuickTextKey` para quien quiera compilarse un add-on de AnySoftKeyboard. La misma fuente, tres salidas; si cambias un texto, las tres cambian.

**Y por qué todo esto vive en Git.** Un teclado guarda sus ajustes dentro del teléfono, en las preferencias de la aplicación. Eso significa tres cosas: que se pierden al cambiar de teléfono, que no se pueden revisar sin tocar la pantalla y que no hay manera de ver qué cambió entre ayer y hoy. Un archivo JSON con su historial resuelve las tres. La versión en el teléfono pasa a ser una copia de la que está en el repositorio, no al revés.

*Lo que este taller no hace:* no escribe dentro de la aplicación. Los ajustes del teclado se tocan a mano, y las diez teclas se configuran una por una la primera vez. Tampoco sincroniza entre teléfonos: eso lo hace Git cuando clonas el repositorio en el otro aparato, y no hay más magia.

───────────────────

*🔐 Lo que cuesta de verdad · privacidad, batería y el modelo que ve tu texto*

Un teclado es la aplicación que más sabe de ti. Ve lo que escribes en el banco, en el chat y en el buscador. Cuando a eso se le añade un modelo, la pregunta deja de ser qué instrucciones le das y pasa a ser **quién lee lo que seleccionas**.

**El camino del texto.** Al pulsar una tecla de IA, el teclado toma lo seleccionado, le antepone las instrucciones de la palabra clave y lo manda al servidor que tengas configurado. Si el servidor es un modelo en la nube, ese texto sale del teléfono. Si es Ollama en tu red, no sale de casa. No hay término medio y no lo arregla ninguna palabra clave: es una decisión de configuración, y se toma una vez.

**Lo que se queda en el teléfono.** Deskdrop y LeanType guardan las conversaciones y los resultados en la memoria de la aplicación —Deskdrop tiene incluso un almacén de conversaciones y una vista de resultados para revisar lo último—. Eso es cómodo y es una superficie más: un registro de lo que has ido pidiendo, dentro de un aparato que puede perderse.

**El coste real.** Un modelo local en un teléfono gasta batería y memoria; los modelos de tres y siete mil millones de parámetros que caben en un móvil moderno responden despacio y no son los mejores escribiendo. Un modelo en la nube responde rápido y cobra en datos. Ninguna de las dos cosas se arregla con prompts: son decisiones de arquitectura, y conviene tomarlas antes de configurar diez teclas.

**Lo que sí se puede hacer sin gastar nada.** Las cinco macros y los doce atajos largos no tocan ningún modelo. Un atajo que pega un texto en el cuadro de cualquier IA no envía nada por sí mismo: eres tú quien decide cuándo y dónde. Para el trabajo delicado —documentos de clientes, datos de salud, cosas de trabajo con cláusulas— el atajo es la opción sensata y la tecla de IA es la cómoda, y no son la misma.

───────────────────

*🚫 Lo que no funciona aquí · deuda declarada con nombre*

**No se probó la obediencia.** Nadie ha comprobado desde aquí que el modelo devuelva solo el texto, ni que respete la longitud, ni que no invente la cifra. Eso pide ejecutar cada tecla contra un modelo concreto y leer la respuesta; se puede hacer, pero no se ha hecho, y quien diga lo contrario está vendiendo humo. Lo que sí está comprobado es que los textos cumplen las once reglas y que el teclado puede guardarlos.

**Trime y Fcitx5 quedaron a medias.** Son motores con diccionarios y esquemas propios, y su expansión de frases no se comprobó. Aparecen con «—» en la tabla, que significa «no se encontró en el código», no «no existe».

**AnySoftKeyboard no está exportado de verdad.** El script genera el XML con el esquema correcto, pero instalarlo exige compilar un add-on. Se entrega el formato, no un archivo mágico que se pega en el teléfono.

**LeanType es un fork, y los forks se mueren.** Hoy tiene ★1.143 y un empujón de esta mañana; su padre tiene ★6.501. El día que el fork se pare, la biblioteca sigue sirviendo para cualquier teclado que acepte texto, y esa es la razón de que viva en un JSON y no en los ajustes de una aplicación.

**Nada de esto te organiza la vida.** Diez teclas bien puestas ahorran unos segundos al día. Si el problema es que escribes demasiado, la solución es escribir menos, no una tecla más rápida.

───────────────────

*❓ Preguntas frecuentes*

**¿Puedo tener setenta y cinco teclas de IA como dice ese texto?** No. LeanType, el teclado que ese texto describe, tiene diez y se cuentan en su código. Lo demás que se puede guardar son atajos de texto, que no ejecutan nada: pegan.

**¿Qué teclado instalo si quiero ejecutar instrucciones desde el teclado?** LeanType si quieres todo en uno y te parece bien su licencia y su tamaño; Deskdrop si tienes Ollama en casa y quieres que nada salga de tu red.

**¿Y si solo quiero pegar textos largos y no gastar tokens?** Cualquiera de los dos, con el expansor, o AnySoftKeyboard con sus textos rápidos. La diferencia es que el expansor de LeanType admite plantillas y el de AnySoftKeyboard no.

**¿La palabra clave hace falta o basta con el texto?** Hace falta. La palabra clave aporta las instrucciones base del teclado y tu texto va detrás; sin ella, la tecla manda solo tu texto y el modelo decide por su cuenta si corrige, resume o traduce.

**¿Por qué los textos no dicen «responde en español»?** Porque el idioma debe seguirlo el texto que pegas, no la tecla. Si lo fijas, un párrafo en inglés sale traducido al español cuando solo querías corregirlo.

**¿Sirve esto en un iPhone?** No tal cual. La biblioteca de textos es texto y se puede usar en cualquier parte; las teclas de IA con instrucciones son de Android y de estos teclados concretos.

**¿Cada cuánto hay que volver a medir?** Cuando cambie algo grande: una versión nueva del teclado, un cambio de licencia o un fork que se pare. `tools/sync_fuentes.py` deja la fecha de cada comprobación en `VERSIONES.json`, así que se sabe cuándo fue la última.

**¿Esto es una lista de prompts para copiar?** No: son veintidós textos con su razón, once reglas que los vigilan y tres exportadores. Una lista se copia una vez; esto se mantiene.

**¿Y si el modelo ignora la instrucción de no añadir saludos?** Es lo más probable la primera vez. La instrucción reduce la frecuencia; no la elimina. La solución definitiva es usar un modelo que respete el formato o un teclado que recorte la respuesta antes de pegarla.

───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **el techo de un teclado son diez instrucciones**, y eso se comprueba abriendo el código, no repitiendo lo que dice un post. Setenta y cinco comandos en una barra que se recorre con el pulgar no son un arsenal: son una lista que nadie lee.

Lo segundo: **el teclado no es el sistema, es el disparador**. Lo que de verdad se conserva es la biblioteca: veintidós textos con su razón, once reglas que los vigilan y una carpeta en Git que sobrevive al teléfono, al fork y al modelo de turno.

Lo tercero: **un prompt se juzga por lo que prohíbe**. «Devuelve solo el texto», «no inventes cifras», «si no hay tareas escribe NINGUNA»: las tres frases que más cambian una respuesta son restricciones, no instrucciones. Y se pueden comprobar con un programa, que es más de lo que se puede decir de casi todo lo que circula.

Y lo cuarto: cuando alguien te venda un método con porcentajes de obediencia, pídele el archivo. Si el método existe, existe en algún sitio y se puede leer. Si solo existe en el texto que lo explica, es publicidad.

───────────────────
— Diez teclas de IA medidas en el código de LeanType: el techo real, no el que promete un post.
— Once teclados clonados y leídos: dos ejecutan instrucciones, dos expanden texto y siete son solo teclados.
— Veintidós textos con once comprobaciones ejecutables, y los quince fallos que salieron del primer borrador.

💓 *La Bandita informa a partir de fuentes fechadas.* once teclados clonados y leídos esta mañana, diez teclas medidas en el código, veintidós textos con su razón y once reglas que se pueden volver a ejecutar. Sin porcentajes inventados y sin una sola lista que copiar.

───────────────────

*Medición del corte:* jueves 5 de noviembre de 2026, 06:41 de la mañana en Santo Domingo (10:41 UTC) · once repositorios clonados entre las 10:16 y las 10:41 UTC · once comprobaciones ejecutadas sobre veintidós textos y cinco macros · once fuentes sincronizadas con su última entrega y su licencia · cero cifras de memoria.

───────────────────

*🔗 Enlaces*

*Los once teclados medidos hoy, en el orden de la tabla:*

- LeanType, el que ejecuta y expande: https://github.com/LeanBitLab/LeanType
- Deskdrop, el de la IA en tu red: https://github.com/SvReenen/Deskdrop
- AnySoftKeyboard, los textos rápidos: https://github.com/AnySoftKeyboard/AnySoftKeyboard
- HeliBoard, el motor del que nacen los otros: https://github.com/HeliBorg/HeliBoard
- FlorisBoard: https://github.com/florisboard/florisboard
- Unexpected Keyboard: https://github.com/Julow/Unexpected-Keyboard
- Thumb-Key: https://github.com/dessalines/thumb-key
- Trime, Rime en Android: https://github.com/osfans/trime
- Fcitx5 para Android: https://github.com/fcitx5-android/fcitx5-android
- FUTO Keyboard, con su licencia propia: https://github.com/futo-org/android-keyboard
- Simple Keyboard: https://github.com/rkkr/simple-keyboard

*Las tres piezas del teclado que se citan en el texto:*

- la clave de las instrucciones que van delante: https://github.com/LeanBitLab/LeanType/blob/main/app/src/main/java/helium314/keyboard/latin/utils/CustomAIKeyText.kt
- el expansor con prefijo, regex y plantillas: https://github.com/LeanBitLab/LeanType/blob/main/app/src/main/java/helium314/keyboard/settings/screens/TextExpanderScreen.kt
- el esquema real de los textos rápidos: https://github.com/AnySoftKeyboard/AnySoftKeyboard/blob/main/ime/addons/quick_text/src/main/res/xml/quick_text_keys.xml

───────────────────

*🗒️ Notas al pie*

(5-nov) **La fecha, en vivo.** Comprobada al empezar —con la revisión de historial y de ecosistema que precede a cualquier medición— y al cerrar. Reloj de fuera: 10:41 UTC, 06:41 en Santo Domingo. Los once clones cayeron entre las 10:16 y las 10:41 de ese mismo reloj.

(5-nov) **Cómo se comprobó cada función.** Buscando en el código clonado tres familias de palabras —expansión, texto rápido, IA— y leyendo después el archivo donde aparecen. Una coincidencia de texto no es una función: `TextKeyData.kt` de HeliBoard menciona texto y no expande nada, y por eso HeliBoard queda con «—» en la tabla.

(5-nov) **El número diez no es una opinión.** Sale de `KeyCode.CUSTOM_AI_1` a `CUSTOM_AI_10` en `InputLogic.kt`, y de las diez palabras clave con su descripción en `strings.xml`. Si una versión futura cambia el número, el programa de comprobación lo detecta porque el tope está en una línea y no repartido por el texto.

(5-nov) **Los quince fallos del primer borrador.** Siete por contrato de salida ausente, cuatro por empezar sin verbo y cuatro por forma de los atajos. Se corrigieron y la segunda pasada salió limpia. El detalle está en el acta del corte, no solo en el resultado: un método que nunca encuentra fallos no está comprobando nada.

(5-nov) **Lo que no se midió.** Si el modelo obedece. Si Trime y Fcitx5 expanden frases con su diccionario. Si el add-on de AnySoftKeyboard compila en un teléfono de hoy. Las tres cosas piden ejecutar, no leer, y quedan como deuda con nombre en la sección 🚫.

(5-nov) **Dónde vive todo.** `corpus-la-bandita/teclado/` en el repositorio: `prompts.json`, `FUENTES.json`, `VERSIONES.json`, `CREDITOS.md` y `exportado/` con los tres formatos. Los programas, en `tools/`. Los créditos y las versiones los escribe `sync_fuentes.py`; el resto se edita a mano y se revisa con `lint_teclado.py`.

*#task*

#task 095 · ejecutar las diez teclas contra dos modelos —uno local con Ollama y uno en la nube— con un texto de prueba de 200 palabras, y anotar en un acta cuántas devuelven solo el texto y cuántas respetan la longitud.

#task 096 · comprobar en un teléfono el add-on de AnySoftKeyboard generado: si compila, cuántos textos admite de verdad y si el teclado emergente los muestra todos.

#task 097 · mirar el diccionario de frases de Trime y de Fcitx5 con el mismo método de esta pieza —clonar, buscar, leer— y cerrar el «—» que hoy tienen en la tabla.

#task 098 · escribir la pieza 21 —los subtítulos y el doblaje, que llevan dos cortes esperando— con el método de hoy: clonar antes de escribir una línea y ninguna cifra de memoria.

───────────────────

🏷️ Etiquetas estratégicas

#LeanType #HeliBoard #FlorisBoard #AnySoftKeyboard #Deskdrop #Ollama #TextExpander #Rime #Fcitx5 #Whisper
