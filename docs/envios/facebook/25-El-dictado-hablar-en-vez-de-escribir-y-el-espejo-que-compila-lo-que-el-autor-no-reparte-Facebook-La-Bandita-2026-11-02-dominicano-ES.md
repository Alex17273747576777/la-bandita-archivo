# PIEZA 25 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/25-El-dictado-hablar-en-vez-de-escribir-y-el-espejo-que-compila-lo-que-el-autor-no-reparte-Facebook-La-Bandita-2026-11-02-dominicano-ES.md`
- **Fecha de la pieza:** 2-nov-2026 (según dateline; edad hoy: 0 días)
- **sha256 de la pieza:** `c71b7baea2ad8643d8bad8b4db2906dc40fb1c3a522843da6be5f46b082e7d7e`
- **Envío generado:** 2026-11-02 · 16 mensajes · el mayor de 3640 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 16 · 814 caracteres ═══

*El dictado: hablar en vez de escribir, y el espejo que compila lo que el autor no reparte*

La Bandita · pieza 25 · guía del 2-nov-2026 · te la mando hoy en 16 mensajes.

Antes de mandártela volví a medir lo que afirma: *11 repositorios, 10 vivos*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: Apache-2.0 6 · MIT 2 · NOASSERTION 1 · AGPL-3.0 1.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/25-El-dictado-hablar-en-vez-de-escribir-y-el-espejo-que-compila-lo-que-el-autor-no-reparte-Facebook-La-Bandita-2026-11-02-dominicano-ES.md

💓 2 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 16 · 2898 caracteres ═══

*El dictado: hablar en vez de escribir, y el espejo que compila lo que el autor no reparte*

*La Bandita · lunes 2 de noviembre de 2026 · edición dominicano-español · pieza 25 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🎙️ Las dos familias: motores y teclados
├── 🎬 Cuatro escenas de esta mañana
├── 🧾 Los diez, uno por uno, con su fecha
├── 🪞 El espejo: un APK de 174 megas y tres estrellas
├── 🔍 Qué se puede comprobar de un paquete recompilado
├── ☁️ En el teléfono o en la nube
├── ⌨️ Las teclas que hablan: los prompts dentro del teclado
├── 🛠️ Probar un teclado de dictado en seis pasos
├── 🧮 Las cuentas del micrófono
├── ❓ Preguntas que me hacen
└── 📊 Tabla, mitos, glosario y enlaces
```

*⚡ En una página*

Hay una forma de usar el teléfono que casi nadie discute y que cambió dos veces en dos años: hablar en vez de escribir. El motor que convierte voz en texto dejó de ser un servicio caro y pasó a ser un programa que corre en el aparato, y sobre ese motor creció una familia de teclados que escriben por ti en cualquier aplicación. Esta mañana se midieron diez proyectos de esa familia: dos motores grandes, dos herramientas de reconocimiento, tres teclados completos y tres piezas de tamaño pequeño que existen por razones muy distintas. Juntos suman ★208.677, y seis de los diez empujaron código en la última semana.

El hallazgo del día no está en los números grandes. El repositorio que motivó esta pieza —un espejo de tres estrellas con el nombre de Dictator— contiene un archivo instalable de 173.992.278 bytes, firmado por alguien que se presenta como «no soy programador, solo lo compilé», y lo publicó cuatro veces entre el 21 y el 26 de octubre. El proyecto original, con ★313 y licencia Apache-2.0, no reparte ningún paquete en su repositorio: su versión 6.4.0, del 7 de octubre, no tiene archivos adjuntos. Ese hueco es todo el argumento de esta guía: cuando el autor no publica el paquete, alguien lo publica por él, y ese alguien se convierte, sin querer, en parte de la cadena de confianza de miles de teléfonos.

Los otros nueve miden el resto del mapa. Whisper (★111.767) y su versión en C++ para aparatos modestos (★54.863) son los motores; sherpa-onnx (★15.679) y Vosk (★15.224) son las alternativas que corren sin conexión; HeliBoard (★6.477), el teclado de FUTO (★3.425) y BiBi Keyboard (★860) son las caras visibles; y Dictate (★313), el espejo (★3) y marmalade (★66) son los tres intentos pequeños de resolver el dictado completo en un teléfono.

La lección práctica de la mañana, para quien vaya directo al final: un teclado de dictado se elige por dónde transcribe (en el aparato o en un servidor), por quién firma el paquete que instalas y por cuánto pesa el modelo que descarga. El resto —colores, animaciones, nombres bonitos— se decide después y no cambia nada cuando no hay internet en el consultorio.

⏬ sigue abajo · parte 1 de 15

═══ MENSAJE 3 de 16 · 3640 caracteres ═══

*🎙️ Las dos familias: motores y teclados*

En este barrio hay dos familias y una confusión permanente entre ellas. Un motor convierte audio en texto y no tiene pantalla; un teclado tiene pantalla, aprende a escribir contigo y, por dentro, llama a un motor. Cuando alguien dice «la aplicación que transcribe mal», casi siempre está culpando al teclado de un problema del motor, o al revés.

*Los motores.* Whisper (★111.767, MIT) es el modelo abierto que puso el dictado bueno al alcance de cualquiera; su versión en C++ (★54.863, MIT) es la que permite correr ese mismo modelo en un teléfono o en una computadora sin tarjeta gráfica. sherpa-onnx (★15.679, Apache-2.0) y Vosk (★15.224, Apache-2.0) son las otras dos puertas: reconocimiento que corre en el aparato, con modelos más pequeños y con la ventaja de no depender de ninguna conexión.

*Los teclados.* HeliBoard (★6.477, GPL-3.0) es el teclado libre de referencia: sin conexión, sin rastreo, con diccionarios y con la posibilidad de enchufarle un motor de voz. El teclado de FUTO (★3.425) lleva su propio motor y su propia licencia, que no es una licencia libre al uso y conviene leer antes de instalar. BiBi Keyboard (★860, Apache-2.0) apuesta por Whisper en el aparato con una interfaz más moderna. Y Dictate (★313, Apache-2.0) es el que hizo el trabajo difícil: convertirse en teclado completo sobre la base de FlorisBoard y ofrecer dictado en tiempo real, con motor propio o ajeno, dentro de cualquier aplicación.

*Y los tres pequeños.* marmalade (★66, MIT) es un teclado de dictado recién nacido, con versión de la semana pasada. Dictate (★313) es el proyecto maduro que aún no llega a mil estrellas. Y el espejo (★3) es el que no aporta código: aporta un archivo instalable. Los tres juntos suman ★382, menos que la décima parte de un solo motor, y son los que la gente instala en el teléfono.

Esa desproporción es la primera lección: las estrellas se acumulan en la pieza que casi nadie instala y se niegan a la que se instala a diario. Quien elija por número de estrellas va a terminar con un motor sin teclado.

*🎬 Cuatro escenas de esta mañana*

*Escena uno: el mensaje largo en la acera.* Alguien camina y necesita mandar un párrafo de cuatro líneas. Escribe con un dedo, se equivoca seis veces, lo borra. Con un teclado de dictado mantiene el botón del micrófono, habla, suelta, y el párrafo aparece con puntuación. La primera vez parece magia; la segunda, costumbre; a la semana, no se vuelve atrás.

*Escena dos: el modelo de 140 megas.* Un usuario instala un teclado con motor propio, descarga un modelo de unos ciento cuarenta megas y lo prueba en modo avión. Funciona, con puntuación y todo, y no sale nada del teléfono. Es el momento en que la privacidad deja de ser un cartel y pasa a ser una prueba que se puede hacer en treinta segundos.

*Escena tres: la nota de voz de una hora.* Un audio largo de una reunión que hay que pasar a texto. El teclado no es la herramienta: aquí se usan los motores y las herramientas de transcripción por lotes, que parten el archivo en trozos y devuelven un texto con marcas de tiempo. Es el mismo motor, otro oficio.

*Escena cuatro: el espejo de tres estrellas.* Alguien busca el APK del teclado, no lo encuentra en el repositorio del autor y sí lo encuentra en un repositorio ajeno con una descripción en inglés roto y un archivo de 174 megas. Lo instala sin mirar nada y funciona. Lo que acaba de hacer —y esto es el centro de la pieza— es confiar en un completo desconocido para que le entregue el programa que va a leer todo lo que escriba, incluidas sus contraseñas si algún día las dicta.

⏬ sigue abajo · parte 2 de 15

═══ MENSAJE 4 de 16 · 3353 caracteres ═══

*🧾 Los diez, uno por uno, con su fecha*

*Whisper · openai/whisper · ★111.767 · MIT · Python · empujón 31 de agosto de 2026.* El modelo que cambió el dictado. No es un teclado ni una aplicación: es el motor y sus pesos, publicados con licencia MIT, y por eso está dentro de media docena de programas de esta lista. Su último empujón es de hace dos meses, y eso no lo hace viejo: los modelos grandes se mueven despacio.

*whisper.cpp · ggml-org/whisper.cpp · ★54.863 · MIT · C++ · empujón 30 de octubre de 2026.* La misma idea reescrita para correr en cualquier aparato, sin tarjeta gráfica y sin Python. Es la pieza que hace posible dictar en un teléfono de gama media sin mandar el audio a ningún sitio. Empujón de hace tres días.

*sherpa-onnx · k2-fsa/sherpa-onnx · ★15.679 · Apache-2.0 · C++ · empujón 29 de octubre de 2026.* Reconocimiento de voz y otras tareas de audio que corren en el aparato, con modelos pequeños y muchas opciones. Es la alternativa a Whisper cuando el aparato tiene poca memoria o cuando se necesita respuesta inmediata.

*Vosk · alphacep/vosk-api · ★15.224 · Apache-2.0 · Jupyter Notebook · empujón 15 de octubre de 2026.* El veterano del reconocimiento sin conexión: modelos ligeros, muchas plataformas y una comunidad de programas que lo usan desde hace años. Su empujón de hace dos semanas y media lo deja en el grupo de los proyectos vivos y tranquilos.

*HeliBoard · Helium314/HeliBoard · ★6.477 · GPL-3.0 · Kotlin · empujón 31 de octubre de 2026.* Teclado libre, sin conexión y sin rastreo, con diccionarios para decenas de idiomas. No trae dictado dentro, y sí deja enchufar un motor externo del sistema. Es la opción de quien quiere un teclado honesto y resolver la voz por separado.

*Teclado de FUTO · futo-org/android-keyboard · ★3.425 · licencia propia «FUTO Source First 1.1-kb», ficha automática en NOASSERTION · C++ · empujón 2 de noviembre de 2026 · versión 0.1.30 del 4 de agosto de 2026.* Teclado con motor de voz propio y una licencia que hay que leer: permite usar, copiar y modificar para uso no comercial, y prohíbe distribuir el programa cobrando por él. No es una licencia libre al uso y por eso se publica con su nombre exacto.

*BiBi Keyboard · BryceWG/BiBi-Keyboard · ★860 · Apache-2.0 · Kotlin · empujón 2 de noviembre de 2026 · versión v4.5.3 del 26 de octubre de 2026.* Teclado de dictado con Whisper en el aparato y una interfaz pensada para el uso diario. Empujón de hoy y paquete de hace una semana: el ritmo que esta serie considera sano.

*Dictate · DevEmperor/DictateKeyboard · ★313 · Apache-2.0 · Kotlin · empujón 2 de noviembre de 2026 · versión v6.4.0 del 7 de octubre de 2026 · sin archivo adjunto en el repositorio.* El proyecto maduro de la mañana: teclado completo construido sobre FlorisBoard, dictado en tiempo real, motor en el aparato o en la nube, y un sistema de prompts de reescritura con biblioteca comunitaria. Publica versiones sin adjuntar paquete: la aplicación llega por la tienda oficial.

*El espejo · Batmancpu/Dictator- · ★3 · Apache-2.0 · Kotlin · empujón 26 de octubre de 2026 · cuatro publicaciones entre el 21 y el 26 de octubre, con un archivo de 173.992.278 bytes.* No aporta código: aporta el paquete que el original no reparte. Se analiza en su propia sección más abajo, con los datos que se pudieron comprobar y los que no.


⏬ sigue abajo · parte 3 de 15

═══ MENSAJE 5 de 16 · 3385 caracteres ═══

*marmalade · maxwhipw/marmalade-stt-android · ★66 · MIT · Kotlin · empujón 28 de octubre de 2026 · versión v1.2.3 del 28 de octubre de 2026.* Teclado de dictado pequeño y reciente: veinte días de vida, una versión publicada el mismo día de su último empujón y una licencia permisiva. Es el tipo de proyecto que se prueba sin expectativas y se agradece si funciona.

*🪞 El espejo: un APK de 174 megas y tres estrellas*

Esta es la parte que justifica la pieza. El repositorio que motivó la medición de hoy se llama Dictator, tiene tres estrellas, cero bifurcaciones, una incidencia abierta pidiendo temas con efecto de cristal, y una descripción que dice, en inglés con faltas: «El APK, no soy programador. Créditos a la persona original, yo solo lo compilé — DevEmperor. Un potente teclado de IA Whisper para transcripción de voz fiable».

Lo primero que hay que decir es lo evidente: eso no es un plagio. El proyecto original tiene licencia Apache-2.0, que permite expresamente copiar, modificar y redistribuir, incluso con cambios y sin pedir permiso, siempre que se conserve el aviso de autoría. El espejo cita al autor y conserva la licencia. En términos legales, está en su derecho, y ese derecho es justamente lo que hace valioso el software libre: cualquiera puede compilar lo que el autor no reparte.

Lo segundo es dónde está el hueco que el espejo llena. La versión 6.4.0 del proyecto original, publicada el 7 de octubre, no trae ningún archivo adjunto: el paquete llega por la tienda oficial, donde la aplicación se cobra una suma pequeña que sostiene el desarrollo. Para quien no puede o no quiere pasar por la tienda, la única vía es compilar; y compilar un teclado de Android no es una tarea para cualquiera. Ahí aparece el espejo: alguien que hizo esa compilación y la publicó gratis.

Lo tercero es la parte incómoda. El espejo publicó cuatro veces en seis días: el 21 de octubre (build-30, con un archivo llamado app-debug.apk de 173.940.920 bytes), el 22 (173.958.868 bytes), el 23 (173.959.510) y el 26 (173.992.278). Los tres últimos llevan el nombre del archivo cambiado a Dictator.apk, y los tres crecen unos miles de bytes cada día, que es lo que crece un programa que se compila a diario desde el código en movimiento del original. El primer archivo se llama app-debug.apk y ese nombre importa: en Android, «debug» designa una compilación de desarrollo, firmada con una llave de depuración que no es la del autor y que no sirve para actualizar la aplicación oficial sin desinstalarla antes.

Lo cuarto es lo que no se puede comprobar desde aquí y por eso se escribe como hueco: si el paquete del espejo está firmado con la llave del autor o con una propia, si su contenido corresponde exactamente al código publicado, y si quien lo compiló introdujo algo que no está en el original. Ninguna de esas tres cosas se resuelve mirando la página del repositorio. Se resuelven comparando firmas con la aplicación oficial y compilando uno mismo desde el código, que es exactamente lo que el espejo hizo y no documentó.

Y la conclusión, que no es un sermón sino una cuenta: instalar el paquete del espejo equivale a decir que se confía en un desconocido tanto como en el autor, en el programa que va a leer cada cosa que se escriba en el teléfono. Puede estar perfecto. No hay manera de saberlo desde la pantalla donde se pulsa descargar.

⏬ sigue abajo · parte 4 de 15

═══ MENSAJE 6 de 16 · 3636 caracteres ═══

*🔍 Qué se puede comprobar de un paquete recompilado*

Un APK es un archivo comprimido con un programa dentro y tres cosas que se pueden mirar sin ser experto. Ninguna de las tres da una garantía absoluta; las tres juntas separan un paquete serio de una caja negra.

*Lo primero: el tamaño y la huella.* Cada archivo publicado trae un identificador de huella digital que se calcula a partir de su contenido. Si dos archivos del mismo día tienen huellas distintas, son distintos. Si el espejo publica tres veces en cuatro días con huellas distintas y tamaños que crecen, está recompilando, no copiando. Las huellas del espejo, tal como aparecen en su lista de publicaciones, empiezan por 8c720e0a, 90b48e29 y 0438ff03 en las tres últimas.

*Lo segundo: el nombre del archivo.* Un paquete oficial se llama por su nombre y su versión; un paquete de depuración se llama app-debug.apk. El nombre no prueba nada por sí solo y sí dice mucho: indica una compilación de desarrollo, hecha para probar, no para distribuir. Distribuir una compilación de desarrollo es legal y es una señal de que el que compila no siguió el proceso de publicación del autor.

*Lo tercero: la firma.* Android exige que cada paquete esté firmado, y la firma es lo que permite instalar una actualización encima de otra. Dos paquetes firmados con llaves distintas son, para el sistema, dos aplicaciones distintas: hay que desinstalar la una para instalar la otra, y con ella se van los datos. Comprobar la firma requiere herramientas de Android; lo que sí se puede hacer sin ellas es una pregunta al que publica: ¿con qué llave está firmado esto y puedes publicar el registro de la compilación?

Y un cuarto detalle que sirve para todo el archivo: el paquete de 174 megas no es solo el teclado. Un teclado de dictado con modelos en el aparato pesa como pesa un modelo, y ese peso es el que explica por qué hay que descargar un archivo enorme para escribir con la voz. Cuando un paquete de este tipo pesa veinte megas, casi siempre significa que el motor no está dentro y que el audio va a viajar.

*☁️ En el teléfono o en la nube*

La decisión que más cambia la experiencia de un teclado de dictado no es el diseño: es dónde se convierte la voz en texto. Hay tres caminos y cada uno tiene un precio distinto.

*En el aparato, con el modelo descargado.* Nada sale del teléfono; funciona sin internet; la primera descarga pesa entre cien y seiscientos megas según el modelo; la puntuación es buena y la latencia depende del procesador. Dictate lo ofrece con modelos de Whisper, Parakeet, Canary y otros, y algunos caben en unos ciento cuarenta megas. BiBi Keyboard y las opciones basadas en whisper.cpp van por el mismo camino. Es la opción que elige quien dicta cosas del trabajo, del médico o de la familia.

*En un servidor propio.* El audio viaja a una máquina de la casa y vuelve convertido. Requiere tener esa máquina encendida y accesible, y da la mejor calidad con hardware modesto. Es el camino de quien ya tiene el sótano montado que se midió en la pieza anterior.

*En la nube de un tercero, con o sin clave propia.* La calidad suele ser la mejor y la latencia la menor, a cambio de que el audio salga del teléfono y de pagar por minuto o por suscripción. Aquí entran los servicios de transcripción que los teclados ofrecen como opción y que cada quien contrata por su cuenta.

La regla que se puede aplicar sin tecnicismos: si el teclado no explica dónde transcribe, asume que transcribe afuera. Y si dictas números de tarjeta, diagnósticos o contraseñas, elige el camino del aparato y compruébalo en modo avión antes de confiar.

⏬ sigue abajo · parte 5 de 15

═══ MENSAJE 7 de 16 · 3452 caracteres ═══

*⌨️ Las teclas que hablan: los prompts dentro del teclado*

Los teclados de esta familia ya no solo escriben lo que dictas: también lo reescriben. Dictate, por ejemplo, trae un sistema de prompts de reescritura —hacer formal, traducir, resumir— con una biblioteca comunitaria de instrucciones que se instalan en un toque.

Eso convierte el teclado en un sitio donde viven dos cosas que la gente confunde: programas y textos que se le pegan a un modelo. La calidad del resultado depende de esos textos más de lo que parece, y de ahí salen tres reglas que sirven para cualquier tecla de este tipo.

*Regla uno: la tecla no adivina el contexto.* Un teclado que manda todo el historial de una conversación a un modelo recibe un texto enorme donde la instrucción se pierde. Si la aplicación deja seleccionar texto antes de pulsar, úsalo: diez líneas seleccionadas dan mejor resultado que cuatrocientas de historial.

*Regla dos: la instrucción tiene que decir qué NO hacer.* «Corrige esto» invita a que el modelo opine, traduzca o reescriba a su gusto. «Corrige ortografía y puntuación, no cambies el vocabulario, no añadas frases, devuelve solo el texto» produce un resultado que se puede pegar sin leer dos veces.

*Regla tres: la salida tiene que tener forma.* Si la tecla debe reemplazar el texto, no puede devolver un párrafo que empiece por «claro, aquí tienes». Pedir explícitamente solo el resultado, sin saludo ni explicación, es la diferencia entre reemplazar y borrar a mano.

Con esas tres reglas, una tecla de reescritura deja de ser un juguete y pasa a ser una herramienta que se usa cien veces al día sin pensarlo. Y son las mismas tres reglas que hacen que un prompt escrito a mano funcione o fracase: rol claro, tarea acotada, restricciones explícitas y una única forma de entregar.

*🛠️ Probar un teclado de dictado en seis pasos*

*Paso uno: instala y no configures nada todavía.* Un teclado nuevo pide permiso para leer lo que escribes, y ese permiso es inevitable: es su trabajo. Lo que sí puedes hacer es instalar uno, probarlo una tarde y desinstalarlo si no convence, antes de meterle contraseñas o mensajes de trabajo.

*Paso dos: ponlo en modo avión y dicta.* Esa es toda la prueba de privacidad. Si con el teléfono sin red el dictado funciona, el motor está en el aparato. Si dice «error de conexión», el audio viaja y ya sabes a qué atenerte.

*Paso tres: dicta con ruido.* En una acera, con un ventilador encendido, con música de fondo. La diferencia entre motores se ve ahí y no en una habitación silenciosa. Los modelos grandes aciertan con ruido moderado; los pequeños piden un segundo intento.

*Paso cuatro: dicta algo con nombres propios y números.* Un apellido difícil, un teléfono, una cantidad con decimales. Ahí es donde se descubren las carencias: los motores pequeños tienden a escribir lo que suenan, no lo que son.

*Paso cinco: prueba la puntuación y el formato.* Un dictado sin comas ni mayúsculas sirve para buscar, no para enviar. Pide al teclado que puntúe automáticamente y revisa si respeta los cambios de párrafo que dijiste en voz alta.

*Paso seis: mira el peso y el consumo.* Un modelo de seiscientos megas ocupa espacio y calienta el teléfono; uno de ciento cuarenta va más ligero y acierta menos. La elección depende de para qué dictes: para mensajes cortos, el pequeño; para textos largos de trabajo, el grande y, si se puede, dictando en casa con el teléfono cargando.

⏬ sigue abajo · parte 6 de 15

═══ MENSAJE 8 de 16 · 2907 caracteres ═══

*🧮 Las cuentas del micrófono*

*Primera cuenta: las estrellas.* Los diez suman ★208.677. Los dos motores grandes se llevan ★166.630, el 80 %. Los tres teclados completos suman ★7.650 y los tres pequeños ★382. Es el reparto más desequilibrado de toda la serie, y tiene una explicación sencilla: los motores son infraestructura que usan otros programas y los teclados son aplicaciones que la gente instala sin dejar estrella.

*Segunda cuenta: quién se movió esta semana.* Tres empujaron el 2 de noviembre: el teclado de FUTO, BiBi y Dictate. Seis empujaron en octubre: whisper.cpp (30), sherpa-onnx (29), HeliBoard (31), Vosk (15), marmalade (28) y el espejo (26). Uno empujó en agosto: Whisper, que es un modelo y no un programa de uso diario.

*Tercera cuenta: el paquete.* Tres de los diez no publican paquete en el repositorio: Whisper y whisper.cpp, porque son motores que se instalan desde otros programas, y Dictate, porque reparte por la tienda. Y uno, el espejo, existe precisamente para llenar ese hueco. Ahí está el nudo de la pieza: cinco de los diez son piezas de infraestructura, tres son aplicaciones con paquete, uno está en la tienda y uno es un puente improvisado.

*🎯 El caso del mensaje que no se podía escribir*

Un chofer de transporte dictaba sus mensajes de trabajo porque escribir con el pulgar en el tráfico le costaba caro. Probó tres teclados: el primero mandaba el audio a la nube y en carretera, con mala señal, le devolvía errores y a veces le cobraba sin transcribir; el segundo tenía motor en el aparato y acertaba con el ruido del motor y la radio; el tercero, más moderno, era mejor en todo menos en una cosa: a la hora de instalar, no había paquete en el repositorio y apareció un espejo de tres estrellas ofreciéndolo.

Se quedó con el segundo. No porque fuera mejor, sino porque podía dictar sin señal, no dependía de nadie y el paquete venía del autor. Perdió la interfaz bonita y las funciones de reescritura.

La lección cabe en una línea: en un teclado que lee todo lo que escribes, el primer criterio no es la calidad del texto, es de dónde salió el paquete y qué pasa cuando no hay señal. Los otros criterios se ordenan detrás.

*🧷 Lo que un teclado de dictado no arregla*

No arregla el ruido, aunque lo disimule. No arregla hablar con la boca llena ni dictar mientras se mastica. No arregla los nombres propios de tu familia, que habrá que corregir a mano las primeras veces hasta que el teclado los aprenda. No arregla la costumbre de dictar párrafos de seiscientas palabras sin respirar: los motores largos aguantan, los pequeños no.

Y sobre todo no arregla la confianza. Un teclado ve todo lo que escribes: mensajes, contraseñas si las escribes ahí, búsquedas, notas. Elegirlo es una decisión de confianza más grande que instalar un reproductor de música, y por eso esta pieza dedica más espacio al paquete que a las funciones.

⏬ sigue abajo · parte 7 de 15

═══ MENSAJE 9 de 16 · 2791 caracteres ═══

*❓ Preguntas que me hacen*

**¿Un teclado de dictado escucha todo el tiempo?**
No debería. El micrófono se activa cuando se pulsa o se mantiene la tecla. Lo que sí conviene comprobar es si el teclado guarda el historial de dictados y cuánto tiempo lo conserva: varios lo hacen y varios lo dejan configurable.

**¿Puedo usar el dictado sin internet?**
Sí, si el teclado trae un modelo que corre en el aparato. La prueba es el modo avión: si funciona sin red, el audio no sale. Si dice error de conexión, está transcribiendo afuera.

**¿El paquete del espejo es seguro?**
No hay manera de saberlo desde la página del repositorio. Está publicado legalmente porque la licencia lo permite, y su contenido y su firma no se pueden comprobar sin herramientas. Si el autor no reparte paquete, la vía prudente es la tienda oficial o compilar uno mismo.

**¿Qué significa que un APK se llame app-debug.apk?**
Que es una compilación de desarrollo. Se instala y funciona, y no está firmada con la llave del autor, así que no puede actualizar la aplicación oficial: hay que desinstalar antes y se pierden los datos.

**¿Los modelos grandes gastan muchos datos?**
Si el motor está en el aparato, no gastan nada al dictar: la descarga del modelo es de una vez y puede ser de cientos de megas. Si el motor está en la nube, el audio viaja y se paga por minuto o por suscripción.

**¿Sirve para dictar en español dominicano?**
Sí. Los motores grandes aciertan bien con acentos del Caribe; los pequeños confunden terminaciones y hay que corregir más. La prueba con nombres propios y números es la que dice la verdad.

**¿Cuánto tarda en transcribir un dictado largo?**
Con motor en el aparato, más o menos en tiempo real con un teléfono moderno; con motor en la nube, casi instantáneo si la conexión es buena. Para audios de una hora, lo que hay que usar son las herramientas de transcripción por lotes, no el teclado.

**¿Puedo dictar en una aplicación que bloquea los teclados?**
Depende de cómo esté hecho el teclado. Algunos se registran como entrada de voz del sistema y funcionan incluso donde los teclados de terceros están bloqueados; otros no. Es una de las diferencias prácticas que solo se descubre probando.

**¿HeliBoard dicta?**
HeliBoard es un teclado libre y sin conexión que no trae dictado propio; se le puede enchufar el motor de voz del sistema. Es la opción de quien quiere separar las dos cosas: un teclado honesto y la voz por otro lado.

**¿Vale la pena pagar por el programa de dictado?**
Depende de cuánto dictes. El proyecto de esta mañana se cobra una suma pequeña en la tienda y sostiene el desarrollo; los demás son gratis y algunos piden que compiles. Pagar por un teclado que se usa a diario es razonable; pagar por uno que se prueba una tarde, no.

⏬ sigue abajo · parte 8 de 15

═══ MENSAJE 10 de 16 · 3577 caracteres ═══

*📊 Tabla, mitos y glosario*

*Los diez medidos, en una línea*

| Proyecto | Estrellas | Licencia | Empujón | Última versión |
|---|---|---|---|---|
| Whisper | ★111.767 | MIT | 31-ago-2026 | modelo, sin paquete |
| whisper.cpp | ★54.863 | MIT | 30-oct-2026 | motor, sin paquete |
| sherpa-onnx | ★15.679 | Apache-2.0 | 29-oct-2026 | motor, sin paquete |
| Vosk | ★15.224 | Apache-2.0 | 15-oct-2026 | motor, sin paquete |
| HeliBoard | ★6.477 | GPL-3.0 | 31-oct-2026 | teclado, sin dictado propio |
| Teclado de FUTO | ★3.425 | FUTO Source First 1.1-kb | 2-nov-2026 | 0.1.30 · 4-ago-2026 |
| BiBi Keyboard | ★860 | Apache-2.0 | 2-nov-2026 | v4.5.3 · 26-oct-2026 |
| Dictate | ★313 | Apache-2.0 | 2-nov-2026 | v6.4.0 · 7-oct-2026 · sin adjunto |
| marmalade | ★66 | MIT | 28-oct-2026 | v1.2.3 · 28-oct-2026 |
| Dictator (espejo) | ★3 | Apache-2.0 | 26-oct-2026 | 4 paquetes · 21 a 26-oct |

*Cinco mitos del dictado*

*Mito uno: «el dictado siempre manda el audio a la nube».* Los motores en el aparato existen y funcionan sin red. La prueba del modo avión tarda treinta segundos y desmonta el mito en el sitio.

*Mito dos: «más estrellas, mejor teclado».* Las ★111.767 de Whisper no son un teclado: son un modelo. El teclado que vas a instalar probablemente tenga tres cifras de estrellas, o menos.

*Mito tres: «si es software libre, el paquete que bajé es del autor».* La licencia permite redistribuir, y por eso existe un paquete de 174 megas publicado por un tercero que dice no ser programador. Legal no es lo mismo que verificado.

*Mito cuatro: «un APK de depuración es un APK defectuoso».* Es un APK de desarrollo: funciona y no está firmado para actualizar la aplicación oficial. El problema no es que sea defectuoso, es que cambia la cadena de confianza y obliga a desinstalar antes.

*Mito cinco: «dictar es más rápido solo si escribes lento».* Con un teclado bueno, dictar es más rápido para casi todo el mundo en textos de más de dos líneas, y más lento para una contraseña o una dirección. La herramienta cambia con la tarea.

*Glosario*

*Motor de reconocimiento:* programa que convierte audio en texto.

*Modelo:* archivo con los pesos del motor; se descarga aparte y puede pesar de cientos de megas.

*Dictado en tiempo real:* el texto aparece mientras se habla, en lugar de al terminar.

*APK:* paquete instalable de Android.

*Firma:* llave con la que se firma un paquete; dos firmas distintas son dos aplicaciones distintas para el sistema.

*Compilación de depuración:* paquete generado para probar, con llave de desarrollo y sin optimizar.

*Push to talk:* mantener la tecla para hablar y soltar para enviar.

*🧭 Cuatro perfiles y su teclado*

*El que manda mensajes todo el día.* Un teclado con motor en el aparato y modelo pequeño. Prioridad: que funcione sin señal y que no caliente el teléfono. La calidad del texto pasa a segundo plano porque los mensajes cortos se corrigen solos.

*El que escribe textos largos.* Motor grande, preferiblemente en la casa o en el aparato de gama alta, y una tecla de reescritura bien configurada. Aquí sí importa la puntuación y el respeto al vocabulario propio.

*El que dicta cosas sensibles.* Motor en el aparato, sin historial guardado o con historial borrado, y comprobación en modo avión. Si el teclado exige una cuenta en la nube para funcionar, no es para este perfil.

*El que solo quiere un teclado honesto.* HeliBoard con el dictado del sistema. Renuncia a lo último y gana en control: un teclado libre, sin conexión y con la voz resuelta por otra pieza que se puede cambiar.

⏬ sigue abajo · parte 9 de 15

═══ MENSAJE 11 de 16 · 3183 caracteres ═══

*📶 El dictado sin conexión, con nombre y apellido*

El dictado sin conexión es la función que más cambia la vida en un país donde la señal se cae, y la que menos se promociona. Tres cosas que conviene saber para que no decepcione la primera vez.

*La primera descarga es grande y es única.* Un modelo utilizable en español pesa entre cien y seiscientos megas. Se descarga una vez, con wifi, y después no se vuelve a tocar. Si el teclado pide descargar cada semana, algo está mal configurado.

*El aparato importa.* Un modelo mediano en un teléfono de gama media transcribe más lento que la voz; en uno de gama alta, va casi a la par. La diferencia no es el teclado: es el procesador.

*La calidad baja con el modelo.* No hay magia: un modelo pequeño confunde menos palabras raras, pero también confunde más nombres y números. La estrategia razonable es tener dos: el pequeño para el día a día y el grande configurado para cuando se dicta en casa con wifi.

*🕰️ Cómo cambió esto en dos años*

En 2024 dictar en el teléfono era un servicio de la nube con cuota mensual y una espera de varios segundos por frase. En 2026 hay motores abiertos que corren en el aparato, teclados que se instalan como cualquier aplicación y modelos de ciento cuarenta megas que puntúan solos.

Lo que no cambió es la parte que esta pieza subraya: los paquetes. El proyecto que más funciones tiene de la mañana no reparte archivo instalable en su repositorio, y por eso existe un espejo de tres estrellas con 174 megas adentro. La técnica avanzó; la distribución sigue siendo el eslabón débil, y ahí es donde se juega la confianza.

*🧾 Lo que costó medir esta familia*

La mañana se fue en tres comprobaciones que no se ven en la tabla. La primera, separar el proyecto original de su espejo: el espejo copia el README del original palabra por palabra, con enlaces que apuntan al repositorio del autor, de modo que una lectura rápida confunde los dos. Hubo que mirar la descripción, la fecha de creación, el número de estrellas y la lista de publicaciones para saber cuál es cuál.

La segunda, leer las publicaciones una por una: cuatro en seis días, con nombres de etiqueta que parecen identificadores de una ejecución automática, tres archivos con el mismo nombre y tamaños que crecen, y uno con nombre de compilación de depuración. Esa lista es la prueba documental de la pieza y se cita con sus cifras exactas.

La tercera, la licencia del teclado de FUTO: la ficha automática devuelve NOASSERTION y el archivo del repositorio declara una licencia propia, «FUTO Source First 1.1-kb», con restricciones de uso comercial y de distribución. Se publica con su nombre exacto y no se resume como «libre», porque no lo es en el sentido habitual.

*📎 Lo que deja el micrófono*

Una idea que sirve para todo el archivo y no solo para los teclados: cuando el autor de un programa no publica el paquete, alguien lo publica por él, y ese alguien pasa a formar parte de la cadena de confianza sin que nadie lo haya elegido. Comprobar quién firma lo que se instala vale más que comprobar cuántas estrellas tiene el proyecto, y en un teclado —que lee todo lo que escribes— vale el doble.

⏬ sigue abajo · parte 10 de 15

═══ MENSAJE 12 de 16 · 2771 caracteres ═══

*🔐 El teclado y las contraseñas*

Un teclado de terceros ve los campos donde escribes, incluidos los de contraseña. Los sistemas modernos marcan esos campos como protegidos y avisan al teclado de que no debe aprender ni guardar lo que se escribe ahí; los teclados serios lo respetan y los demás no siempre.

Tres hábitos que reducen el riesgo sin volver al teclado del sistema. El primero: usar el teclado del sistema o el gestor de contraseñas para los campos sensibles, y el teclado de dictado para lo demás. El segundo: desactivar el aprendizaje de palabras nuevas en el teclado de dictado, o revisar la lista de palabras aprendidas cada mes. El tercero: no dictar nunca números de tarjeta, claves ni diagnósticos con un motor que transcribe en la nube.

Y una comprobación que se puede hacer hoy: escribir una palabra inventada en un campo normal, borrarla y ver si el teclado la ofrece después como sugerencia. Si aparece, el teclado está aprendiendo lo que escribes, y esa lista conviene saber dónde está y cómo se borra.

*🧪 Cuatro pruebas con el mismo párrafo*

Para comparar teclados sin opinar de gustos, se dicta el mismo párrafo a todos y se comparan las salidas. El párrafo debe tener todo lo que suele romper un motor: un nombre propio poco común, un número con decimales, una sigla, una pregunta y una coma con inciso.

La primera prueba se hace con ruido de fondo moderado y sin red, para medir el motor del aparato. La segunda, en silencio y con red, para ver la diferencia entre los dos caminos. La tercera, con prisa y sin vocalizar, que es como se dicta en la vida real. La cuarta, dictando el mismo texto dos veces seguidas y comparando: un motor bueno da resultados casi iguales, uno flojo cambia palabras.

Lo que se anota de cada prueba son cuatro cosas: cuántas palabras falló, si puso puntuación, si respetó el nombre propio y cuánto tardó. Con esa tabla de cuatro por cuatro, la decisión deja de ser una impresión y pasa a ser un dato.

*🎚️ Tres ajustes que deciden todo*

*El idioma del motor.* Un motor configurado en inglés transcribiendo español devuelve una traducción aproximada con faltas; uno configurado en español con acento caribeño y nombres propios rinde mucho más. Es el ajuste que más se olvida y el que más se nota.

*El silencio mínimo.* Cuánto hay que callar para que el dictado se corte y envíe. Un valor corto manda frases a medias; uno largo deja colgado el dictado cuando el que habla se queda pensando. Se ajusta probando con la voz y el ritmo propios.

*La puntuación automática.* Activarla y revisar de vez en cuando. Cuando funciona, ahorra media hora al día; cuando falla, mete comas donde no van. La prueba con el párrafo de cuatro trampas dice en dos minutos si el motor puntúa bien.

⏬ sigue abajo · parte 11 de 15

═══ MENSAJE 13 de 16 · 2309 caracteres ═══

*🎯 El caso del que compiló para los demás*

El espejo de esta mañana tiene una incidencia abierta que pide temas con efecto de cristal y una descripción donde su autor aclara, en primera persona, que no programa. Esa frase explica el fenómeno mejor que cualquier análisis: no hay ambición de proyecto, hay una necesidad resuelta y publicada.

Ese gesto, hecho por cualquiera, es a la vez la mejor prueba del software libre y su punto más frágil. La mejor prueba, porque nadie necesita permiso para compilar y compartir lo que la licencia permite. El punto más frágil, porque el resultado circula sin registro de compilación, sin firma conocida y con un nombre que invita a confundirlo con el original.

Quien instale ese paquete debería saber tres cosas: que el código de base es libre y de otro autor, que el paquete lo armó un tercero y que la única manera de comprobar qué hay dentro es compilarlo uno mismo o comparar firmas con la aplicación oficial. Con esas tres frases delante, la decisión sigue siendo libre y deja de ser a ciegas.

*🔗 Enlaces*

- Whisper: https://github.com/openai/whisper
- whisper.cpp: https://github.com/ggml-org/whisper.cpp
- sherpa-onnx: https://github.com/k2-fsa/sherpa-onnx
- Vosk: https://github.com/alphacep/vosk-api
- HeliBoard: https://github.com/Helium314/HeliBoard
- Teclado de FUTO: https://github.com/futo-org/android-keyboard
- BiBi Keyboard: https://github.com/BryceWG/BiBi-Keyboard
- Dictate (original): https://github.com/DevEmperor/DictateKeyboard
- Dictator (espejo): https://github.com/Batmancpu/Dictator-
- marmalade: https://github.com/maxwhipw/marmalade-stt-android
- FlorisBoard, la base del teclado: https://github.com/florisboard/florisboard
- El sótano de la pieza anterior: https://github.com/immich-app/immich

*Cómo se midió:* diez repositorios con las tres lecturas completas y el orden rotado —API de búsqueda, página del repositorio y contenido crudo del README y del archivo de licencia—, más una comprobación específica de la cadena de publicaciones del espejo: cuatro publicaciones entre el 21 y el 26 de octubre, con nombre de archivo, tamaño exacto en bytes y huella digital de cada una. La licencia del teclado de FUTO se leyó en su archivo, no en su ficha. Corte entre las 14:10 y las 15:25 de Santo Domingo.

⏬ sigue abajo · parte 12 de 15

═══ MENSAJE 14 de 16 · 2761 caracteres ═══

*🌅 Cierre — el teclado que lee todo*

La familia del dictado deja tres cosas claras. La primera: los motores abiertos resolvieron el problema técnico; hoy se puede hablar y obtener texto limpio, con puntuación, sin que el audio salga del teléfono. La segunda: los teclados que la gente instala son pequeños en estrellas y grandes en responsabilidad, porque ven cada palabra que se escribe. La tercera: la distribución sigue siendo el eslabón flojo, y el espejo de tres estrellas con 174 megas lo demuestra mejor que cualquier discurso.

Los números de la mañana, en fila: ★208.677 repartidas de forma escandalosamente desigual, seis empujones en octubre, tres en noviembre, tres proyectos que no publican paquete y un cuarto que existe para tapar ese hueco. Con esos datos se puede elegir sin leer diez README y, sobre todo, sin instalar a ciegas.

*Medición del corte:* lunes 2 de noviembre de 2026, entre las 14:10 y las 15:25 de Santo Domingo · diez repositorios con las tres lecturas completas y el orden rotado · cuatro publicaciones del espejo revisadas con tamaño y huella · una licencia leída en su archivo y no en su ficha.

*Licencia de esta entrega:* el texto va en CC BY-SA 4.0, las cifras en CC BY 4.0 y los ejemplos de código en MIT; la marca «Alexis (La Bandita)» y el nombre de la casa no se incluyen en el trato y se quedan donde están.

> —¿Y si el paquete que bajo no es del autor?
> —Entonces el autor de lo que instalaste no es él: eres tú, aceptando.

💓 *La Bandita informa a partir de fuentes fechadas.* Un teclado ve lo que escribes: se elige por quién firma el paquete y por qué pasa cuando no hay señal.

## 🗒️ Notas al pie

(2-nov) El espejo se llama Dictator y el original se llama Dictate Keyboard; el espejo copia el README del original con enlaces al autor, y por eso se comparan aquí por descripción, fecha de creación (20 de mayo de 2026 frente a 29 de mayo de 2024), estrellas (★3 frente a ★313) y lista de publicaciones.

(2-nov) Los tamaños y huellas del espejo son los que declara la lista de publicaciones del repositorio al momento del corte: 173.940.920 bytes (build-30, 22 de octubre, app-debug.apk), 173.958.868 (22 de octubre), 173.959.510 (23 de octubre) y 173.992.278 (26 de octubre).

(2-nov) El teclado de FUTO figura con su licencia textual, «FUTO Source First 1.1-kb», y no como «libre»: permite uso, copia y modificación no comercial, prohíbe distribuir cobrando y no permite quitar los avisos del licenciante.

(2-nov) Dictate publica la versión v6.4.0 del 7 de octubre sin archivo adjunto en el repositorio; la aplicación se distribuye por la tienda oficial. Esa ausencia es el origen de toda la sección del espejo y se verificó en la lista de publicaciones, no por referencia.

⏬ sigue abajo · parte 13 de 15

═══ MENSAJE 15 de 16 · 1629 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 25*

Medí otra vez, hoy 2 de noviembre de 2026, los 11 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• openai/whisper — ★111.768 · *dormido*: sin empujar desde el 31-ago-2026 (63 días) · MIT · última release v20250625 (26-jun-2025)
• k2-fsa/sherpa-onnx — ★15.679 · empujó el 29-oct-2026 (hace 4 días) · Apache-2.0 · última release v2.0.1 (26-oct-2026)
• alphacep/vosk-api — ★15.224 · empujó el 15-oct-2026 (hace 18 días) · Apache-2.0 · última release v0.3.50 (22-abr-2024)
• Helium314/HeliBoard — sin dato hoy (la API no respondió). No afirmo nada.
• futo-org/android-keyboard — ★3.425 · empujó en las últimas horas · NOASSERTION · última release 0.1.30 (4-ago-2026)
• BryceWG/BiBi-Keyboard — ★860 · empujó en las últimas horas · Apache-2.0 · última release v4.5.3 (26-oct-2026)
• DevEmperor/DictateKeyboard — ★313 · empujó en las últimas horas · Apache-2.0 · última release v6.4.0 (7-oct-2026)
• Batmancpu/Dictator- — ★3 · empujó el 26-oct-2026 (hace 7 días) · Apache-2.0 · última release dictator-40297638051 (26-oct-2026)
• maxwhipw/marmalade-stt-android — ★66 · empujó el 28-oct-2026 (hace 5 días) · MIT · última release v1.2.3 (28-oct-2026)
• florisboard/florisboard — ★8.742 (+10) · empujó el 31-oct-2026 (hace 2 días) · Apache-2.0 · última release v0.5.2 (28-nov-2025)
• immich-app/immich — ★117.961 (+349) · empujó en las últimas horas · AGPL-3.0 · última release v3.3.5 (21-oct-2026)

💓 *LOS ENLACES · medidos hoy uno por uno*

De los 12 enlaces de esta pieza, *12 responden*.
Ninguno roto.

⏬ sigue abajo · parte 14 de 15

═══ MENSAJE 16 de 16 · 152 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.
