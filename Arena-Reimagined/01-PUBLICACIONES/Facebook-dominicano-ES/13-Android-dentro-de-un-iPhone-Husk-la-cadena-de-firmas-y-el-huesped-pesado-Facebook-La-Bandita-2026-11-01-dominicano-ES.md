*Android dentro de un iPhone: Husk, la cadena de firmas y el huésped pesado*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 13 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🍎 Qué significa «Android en un iPhone»
├── 🧰 La cadena: del APK al icono
├── 🎬 Cuatro escenas y el censo de esta tarde
├── 🍏 Las tres puertas del iPhone
├── ⚙️ La capa de traducción y el huésped pesado
├── 🧱 Lo que no va a funcionar bien nunca
├── 🔍 El caso del juego que no pasa del logo
├── ⚖️ La ley, la manzana y las firmas
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas al pie
```

*⚡ En una página*

Hay un proyecto que se llama Husk, que se describe en una línea como «Android en iOS, nativo o emulado», que tiene ★2.937, licencia GPL-2.0-or-later, está escrito en Java y sacó su versión 3.3 hoy mismo, 1 de noviembre. Pide iOS 15.5 o superior y se instala por las vías de siempre del teléfono de la manzana: SideStore, AltStore o TrollStore. Con eso ya se puede decir lo esencial, y lo esencial es que esto no es magia ni es un Android completo: es una capa que hace de Android alrededor de un programa que corre en el iPhone.

Lo interesante no es Husk solo, es la cadena que hace falta para que un APK termine con icono en la pantalla de un iPhone. Hay una pieza que firma, una que instala, una que mantiene el permiso vivo y una que emula cuando la traducción no alcanza. Este censo mide ocho de esas piezas, y la más grande no es Husk: es UTM, con ★36.633 y empujón de hoy.

Lo que casi nadie dice y conviene decir el primero: el iPhone no permite instalar programas que no vengan de su tienda, y todo lo que hay aquí existe para rodear ese límite con firmas, perfiles y trucos que caducan. La cadena funciona, y funciona con fecha de vencimiento. Quien no quiera renovar cada semana, no es su camino.

Si te llevas una idea: pasar de Android a iPhone es posible, es más frágil de lo que parece en los videos y exige entender tres cosas —firma, instalación y traducción— antes de bajar el primer archivo. Lo demás es paciencia.

───────────────────

*🍎 Qué significa «Android en un iPhone»*

Significa cuatro cosas distintas y la gente las mete en la misma frase. Conviene separarlas porque cada una promete algo diferente.

La primera es *traducir*: el programa de Android viene compilado para un procesador y unas bibliotecas que el iPhone no tiene, así que alguien escribe las piezas que faltan —la biblioteca de C, el entorno de Java, los gráficos, el audio y la entrada— y deja que el código original corra encima. No hay Android arrancado en ninguna parte; hay un programa de Android que cree estar en un Android.

La segunda es *emular*: se levanta un sistema Android completo dentro de un programa que simula el teléfono, con su arranque, su memoria y sus servicios. Es lo que hace UTM cuando hospeda un sistema invitado. Es más compatible y mucho más lento.

La tercera es *firmar y instalar*: el iPhone solo abre programas con una firma que acepta, así que alguien tiene que firmar el paquete con una cuenta de desarrollador y renovar ese permiso cada cierto tiempo. SideStore, AltStore y SignTools viven de esto.

La cuarta es *mantener vivo el permiso*: la firma de desarrollador caduca, y con ella el icono deja de abrir. Los programas se conectan a un servicio del teléfono para renovar, y cuando ese servicio no está, hay que volver a la computadora.

Cuando alguien dice «tengo Android en mi iPhone», hay que preguntar cuál de las cuatro tiene. La respuesta cambia todo: traducir es rápido y limitado, emular es lento y compatible, firmar es la puerta, y renovar es la cuota mensual de paciencia.

───────────────────

*🧰 La cadena: del APK al icono*

El recorrido completo tiene cinco estaciones y cada una puede fallar por su cuenta.

*Estación uno: el archivo.* Un APK que se quiere abrir. Aquí ya hay un filtro: los paquetes con código nativo de 32 bits, los que dependen de servicios del sistema y los que usan protección anticopia no van a funcionar, y no hay cadena que lo arregle.

*Estación dos: la firma.* El paquete iOS que envuelve todo necesita una firma aceptada por el teléfono. Ahí entran SignTools para firmar en un servidor propio, Dadoum/Sideloader para hacerlo desde cualquier sistema, y las cuentas de desarrollador con sus límites de aplicaciones y de días.

*Estación tres: la instalación.* SideStore y AltStore son las dos puertas clásicas, con la diferencia de que SideStore busca no depender de una computadora cada semana. AltStore tiene ★14.821 y SideStore ★7.188: la segunda es más joven y más cómoda; la primera, más vieja y más conocida.

*Estación cuatro: el contenedor.* LiveContainer, ★13.674, resuelve un problema aparte: instalar una vez el contenedor y abrir dentro varias apps, para no gastar los cupos de la firma en cada una. Es la pieza que hace manejable el límite de aplicaciones del teléfono.

*Estación cinco: la traducción o la emulación.* Ahí está Husk, y ahí está UTM cuando lo que se quiere es un sistema completo y no una app suelta. Husk intenta lo rápido; UTM hace lo pesado; y ninguno de los dos convierte tu iPhone en un Android de verdad.

Cinco estaciones, cinco proyectos distintos y cinco fechas que se pueden mirar antes de empezar. Quien las tiene claras no se pasa la tarde instalando un archivo que su cadena no iba a aceptar nunca.

───────────────────

*🎬 Cuatro escenas y el censo de esta tarde*

*El que quería un juego de Android en su iPhone.* Leyó que era posible, bajó un APK, lo abrió con Husk y el juego arrancó en segundos con un mando bluetooth. Su sorpresa fue que funcionara tan bien y su segunda sorpresa, que la mitad de las opciones del juego no respondieran porque dependían de servicios que el iPhone no tiene. Con lo que sí funcionaba, jugó tres horas seguidas.

*La que se cansó de renovar.* Instaló una app por SideStore, la usó dos semanas y un día el icono dejó de abrir. Le explicaron que la firma había caducado y que había que renovarla con el servicio del teléfono encendido. Lo hizo una vez, dos veces, y a la tercera decidió que no valía la pena para lo que era. La app era un juego de espera.

*El que quiso el sistema completo.* Probó UTM con un sistema invitado para usar una app de trabajo que necesitaba servicios de Android. Funcionó, con dos avisos: la batería se iba en dos horas y el teléfono se calentaba como una plancha. Lo dejó instalado para emergencias y no para el día a día.

*La que administra el teléfono de la casa.* Su hijo quería una app que solo existe para Android. Su solución no fue técnica: buscar la versión web, que existía y hacía lo mismo. Se ahorró la cadena entera, y esa es la respuesta correcta más veces de las que parece.

───────────────────

*🧾 El censo de esta tarde*

*Husk*, el que da título: ★2.937, GPL-2.0-or-later, Java, empujón y versión del 1 de noviembre —la 3.3—. Se instala desde las tiendas de siempre del iPhone y pide iOS 15.5 o superior. Su promesa escrita es concreta: una capa de traducción para el código de 64 bits, un huésped completo bajo emulación cuando hace falta y un añadido curioso para paquetes de consola.

*UTM*, el grande: ★36.633, Apache-2.0 en la ficha y MIT en su README, Swift, empujón de hoy y versión v5.0.8 del 17 de octubre. Es el emulador de referencia en el teléfono de la manzana y la razón por la que las cifras de Husk no deben leerse como comparación de popularidad, sino de propósito.

*AltStore*, la puerta vieja: ★14.821, AGPL-3.0, Swift, empujón del 21 de octubre y versión v2.3 del 30 de septiembre. Sigue siendo el nombre que todo el mundo conoce y el que más tutoriales arrastra.

*SideStore*, la puerta sin computadora: ★7.188, AGPL-3.0, Swift, empujón del 27 de octubre y versión 0.7.0-alpha del 15 de septiembre. Su contador en cero punto siete dice lo que es: una apuesta joven que intenta quitar de la ecuación el cable y la computadora.

*LiveContainer*, el contenedor: ★13.674, AGPL-3.0 en la ficha y MIT en su README, Swift, empujón del 17 de octubre y versión 3.8.0 del 17 de julio. Resuelve el cupo de instalaciones envolviendo varias apps dentro de una sola firma.

*SignTools*, la firma de servidor: ★2.242, AGPL-3.0, Go, empujón del 12 de octubre y versión v3.0.12 del 16 de julio. Para quien quiere firmar sus propios paquetes en una máquina propia sin depender de nadie.

*Dadoum/Sideloader*, la firma desde cualquier sitio: ★1.063, GPL-3.0, escrito en D, empujón del 18 de septiembre y sin versión pública anotada. Es la alternativa multiplataforma menos conocida y la más interesante para quien no tiene Windows ni Mac.

*ipaverse*, el paquete completo: ★689, MIT, Swift, empujón del 22 de septiembre y versión v2.5.3 del mismo día. Descarga, refirma e instala, que es la cadena entera en un solo programa.

───────────────────
*🍏 Las tres puertas del iPhone*

El teléfono de la manzana no deja abrir programas que no vengan firmados por quien él acepta, y ese es el hecho del que salen todas las demás reglas. Hay tres formas conocidas de rodearlo y cada una tiene un precio distinto.

*La primera puerta es la cuenta de desarrollador gratuita.* Permite firmar unas pocas aplicaciones, con un permiso que caduca a los siete días y hay que renovar. Es la puerta que usan AltStore y SideStore, y su ventaja es que funciona en cualquier iPhone sin nada especial. Su precio es la renovación: quien instala diez cosas para probar, vive firmando.

*La segunda puerta es el permiso de empresa.* Permite instalar sin caducidad semanal y es la vía que usan las empresas para repartir sus programas internos. Su precio es que depende de un certificado ajeno, y cuando ese certificado se revoca, todos los iconos dejan de abrir a la vez. Es la puerta que más disgustos ha dado a la gente que instala por ahí.

*La tercera puerta es el aparato con el arranque abierto.* En algunos iPhone antiguos y en modelos con versiones concretas del sistema existe un estado que permite instalar sin firma. Es la puerta más cómoda y la más cerrada: se limita a aparatos viejos o a versiones que ya no se actualizan. En ella se apoya la instalación llamada TrollStore, que Husk menciona entre sus formas de instalarse.

Con las tres puertas claras, se entiende por qué el ecosistema de esta guía es tan pequeño y tan activo: es un ecosistema de mantenimiento. SignTools existe para firmar en casa, Dadoum/Sideloader para firmar desde cualquier sistema, SideStore para renovar sin cable e ipaverse para hacer las tres cosas en un solo programa. Ninguna de ellas crea una cuarta puerta: todas administran mejor las que ya hay.

───────────────────

*⚙️ La capa de traducción y el huésped pesado*

La traducción es la parte que suena a ciencia ficción y es la más sencilla de explicar. Un juego de Android viene compilado para un procesador ARM de 64 bits, y el chip del iPhone también es ARM de 64 bits. Ahí se acaba la coincidencia: todo lo demás —las bibliotecas del sistema, el entorno de ejecución de Java, los gráficos, el sonido, la entrada táctil— es distinto.

La capa de traducción escribe esas piezas para el iPhone y deja que el código original corra encima. El programa cree que habla con Android; habla con alguien que imita a Android. No hay arranque, no hay escritorio, no hay servicios del sistema: hay un juego que empieza en segundos, que es exactamente lo que Husk promete con su frase de «sin arranque de Android».

El límite de la traducción es lo que no imita. Un juego que pide la tienda de aplicaciones, el servicio de notificaciones o una biblioteca concreta de realidad aumentada encontrará una pared. Y como la capa es nueva y está en construcción, cada versión arregla un grupo de programas y deja otro igual.

El huésped pesado es la otra mitad. Cuando la traducción no alcanza, Husk levanta un sistema Android completo bajo emulación —su propia descripción menciona un sistema LineageOS invitado sobre QEMU—, y entonces la compatibilidad sube y la velocidad baja. Es el mismo compromiso que en el escritorio: emular es compatible y lento, traducir es rápido y limitado.

La consecuencia práctica es que Husk no es una app: es un programa con dos motores y una decisión que se toma por aplicación. El juego ligero va por traducción; la app que necesita servicios va por emulación; y hay cosas que no van por ninguno de los dos.

───────────────────

*🧱 Lo que no va a funcionar bien nunca*

Hay cuatro familias de programas que conviene descartar antes de probar, para no gastar la tarde en una cadena que no podía funcionar.

*Las que dependen de servicios de Google.* Un programa que pide notificaciones por el servicio de la casa de Google, o que verifica la compra dentro de la aplicación, encontrará una pared. El servicio no está y no hay capa que lo supla sin modificarlo, y modificarlo es otra historia con otro nombre.

*Las que usan protección anticopia o comprobación de integridad.* Esas comprueban si el aparato es el que dice ser, y un aparato emulado o traducido no lo es. Fallan por diseño, con un mensaje que casi nunca explica la razón.

*Las de 32 bits.* La traducción se apoya en código de 64 bits; un paquete antiguo compilado para 32 tiene que ir por emulación, y la emulación en un teléfono es lenta incluso para lo simple.

*Las que son solo un lanzador de otra cosa.* Un programa que abre un servicio en la nube y no hace nada por sí mismo puede funcionar y aun así no servir de nada, porque lo que se quería estaba en el servidor y no en el paquete.

A esas cuatro se suma una quinta, la más común y la menos técnica: el programa existe, pero su versión web hace lo mismo. Antes de montar la cadena, vale la pena comprobarlo.

───────────────────

*🔍 El caso del juego que no pasa del logo*

Un juego bajado de un APK, abierto con Husk en un iPhone de 2021, se queda en la pantalla del logo y se cierra a los cuatro segundos. El usuario concluyó que el proyecto era humo. No lo era: era el caso más previsible de todos.

Primero se comprobó la versión: la 3.3, publicada ese mismo día. Segundo, el tipo de paquete: el juego incluía una biblioteca de comprobación de licencia. Tercero, la alternativa: el mismo juego, por emulación, arrancó y llegó al menú en dos minutos, con una temperatura de teléfono incómoda y una batería en caída libre.

La conclusión del caso es útil: cuando un programa se cierra sin mensaje en la capa de traducción, casi siempre es una comprobación de integridad o una biblioteca que la capa no imita. Probar por emulación separa el diagnóstico en un minuto: si ahí funciona, el paquete está bien y el problema es la capa; si ahí tampoco, el problema es el paquete o el aparato.

Y hay un tercer resultado posible, que es el que más gente encuentra: funciona por emulación, va lento y no vale la pena. Ahí la respuesta honesta no es una app mejor, es que ese juego no es para ese teléfono.

───────────────────

*⚖️ La ley, la manzana y las firmas*

Hay tres capas de reglas y conviene no mezclarlas, porque la gente las discute como si fueran una sola.

La primera es la licencia del software libre que se usa. Husk es GPL-2.0-or-later, UTM es Apache-2.0 en su ficha y MIT en su README, LiveContainer es AGPL-3.0 en su ficha y MIT en su README. Esas licencias dicen qué se puede hacer con el código: usarlo, modificarlo y redistribuirlo bajo condiciones. No dicen nada sobre el teléfono.

La segunda son las condiciones del sistema. El iPhone no permite instalar programas de fuera de su tienda, y rodearlo con firmas de desarrollador, certificados de empresa o aparatos con el arranque abierto es una decisión del dueño del aparato con consecuencias técnicas: caducidades, revocaciones y, en algunos casos, pérdida de garantía o de soporte.

La tercera son los derechos de lo que se instala. Un APK de un juego de pago obtenido fuera de su tienda no se convierte en legal por correr dentro de una capa de traducción; y una app de trabajo instalada por vías alternativas puede violar el acuerdo con el empleador aunque el programa sea libre.

Las tres capas se pueden resumir en una frase que no es consejo legal: el código libre te da permiso sobre el código, no sobre el teléfono ni sobre el contenido. Y cada capa se paga en un sitio distinto.

───────────────────

*🧭 Cuándo vale la pena y cuándo no*

Vale la pena cuando hay un programa concreto, de los que no dependen de servicios ajenos, y el iPhone es el único aparato disponible. Un juego de un jugador, una herramienta de cálculo, un lector de archivos: cosas que no piden permiso a nadie y que se agradecen en el bolsillo.

No vale la pena cuando el objetivo es tener «Android en el iPhone» como concepto. Eso no existe: existe un programa suelto que corre con una capa encima, y la ilusión se cae en la primera app que pide notificaciones.

Vale la pena cuando la persona tolera renovar. Si le molesta que un icono deje de abrir cada semana, este ecosistema no es para ella, porque la renovación no es un fallo: es la forma en que la puerta se mantiene abierta.

No vale la pena cuando el teléfono es el aparato de trabajo y de las cuentas. Modificar el estado de un aparato con datos sensibles para jugar a algo es una mala ecuación, y la ecuación se puede escribir en una línea antes de empezar.

Y hay un caso intermedio que mucha gente descubre tarde: vale la pena tener la cadena montada y no usarla. Firmar, instalar y renovar una sola app de pruebas enseña cómo funciona todo, y después la decisión de cada programa nuevo se toma en dos minutos.

───────────────────
*🕰️ La cronología de las puertas*

Este ecosistema se entiende mejor por lo que se fue cerrando que por lo que se fue inventando.

Al principio el teléfono de la manzana instalaba programas con un cable y una computadora, y el permiso duraba mientras durara la confianza en el certificado. Fue la época en que «sideload» significaba una tarde y un tutorial.

Después llegaron las tiendas alternativas, que pusieron interfaz y menú a lo que antes era un comando. AltStore tiene hoy ★14.821 y una versión v2.3 del 30 de septiembre; su papel fue convertir la ceremonia en un botón.

Luego llegó la idea de renovar sin cable. SideStore, con ★7.188 y su versión 0.7.0-alpha del 15 de septiembre, intenta que el teléfono se renueve a sí mismo aprovechando la depuración inalámbrica, y esa idea —que ya vimos funcionar en Android con Shizuku— es la misma en los dos mundos: prestar un permiso del sistema para no depender de la computadora.

En paralelo, la firma se volvió un servicio. SignTools, ★2.242 y AGPL-3.0, permite montar un firmador propio; Dadoum/Sideloader, ★1.063, lo hace desde cualquier sistema operativo; ipaverse, ★689, junta descarga, refirma e instalación en un programa.

Y en los últimos años apareció lo que nadie esperaba: capas que hacen correr programas de un sistema en el otro. Husk, con ★2.937 y versión 3.3 de hoy, es el ejemplo del lado del iPhone; en el lado de Android, el camino inverso se hace con sistemas invitados, como VegaBobo/DSU-Sideloader, ★2.353 y Apache-2.0, cuya última versión es de 2023 y que sigue sirviendo para probar un sistema sin tocar el que se usa a diario.

El patrón es el mismo en los dos mundos: cuando el sistema cierra una puerta, la comunidad abre una puerta más pequeña, y las puertas pequeñas se mantienen con proyectos de dos mil estrellas y una persona.

───────────────────

*🧮 Los cupos de la firma, en números*

La firma gratuita de desarrollador tiene tres límites que conviene tener escritos: un número pequeño de aplicaciones activas a la vez, un número de días antes de caducar y un número de aparatos por cuenta. Los tres cambian con el tiempo y con la región, y los tres son la razón por la que existen los contenedores.

De ahí sale la aritmética del ecosistema. Si cada app gasta un cupo y la caducidad llega en una semana, entonces la única forma de tener diez cosas instaladas es tenerlas dentro de una o dos firmas. Eso es exactamente lo que hace LiveContainer, ★13.674, y por eso su cifra es alta para un programa que casi nadie menciona: resuelve el problema más aburrido y más real.

También de ahí sale la costumbre de rotar. Mucha gente tiene dos juegos instalados que se turnan: instala uno, juega dos semanas, lo borra e instala el otro. No es una limitación técnica del teléfono, es la contabilidad de la firma metida en la vida diaria.

Y de ahí sale el último dato, el que decide a mucha gente: la renovación no es opcional ni es un fallo del programa. Un icono que deja de abrir el día nueve no está roto; está esperando que alguien vuelva a firmar.

───────────────────

*💬 Las frases que se repiten*

«¿Esto es legal?» Es una pregunta de tres capas: la licencia del programa, las condiciones del teléfono y los derechos del contenido. Casi siempre la persona pregunta por la segunda y la respuesta está en la primera.

«A mí me funcionó, así que sirve». Sirve para ese programa, en ese aparato, con esa versión. Es el tipo de prueba más común y el que menos se puede generalizar.

«Se me borró todo al actualizar». Con la cadena del iPhone, actualizar a veces significa volver a firmar y reinstalar, y ahí se va el estado de la app. Respaldar antes no es opcional.

«Ya no abre ninguna app». Un certificado revocado hace exactamente eso, a la vez y sin mensaje. No es una app rota: es la puerta cerrada para todas.

«Es que el iPhone no deja». El iPhone no deja, y por eso existe todo este ecosistema. Decirlo así ahorra la discusión sobre si el proyecto es bueno.

───────────────────

*🛠️ Montar la cadena en una tarde*

La primera hora se va en preparar el teléfono y no en instalar nada. Hace falta la versión del sistema —Husk pide 15.5 o superior—, una cuenta que sirva para firmar y una decisión sobre la puerta: cuenta gratuita, certificado ajeno o aparato con el arranque abierto.

La segunda hora es la puerta. Se instala la tienda alternativa que se haya elegido, se conecta el teléfono una vez y se firma el primer programa de prueba, que conviene que sea pequeño y conocido: si el programa de prueba no abre, no tiene sentido seguir con el que importa.

La tercera hora es el contenedor. Si se van a instalar varias cosas, LiveContainer se monta antes y ahorra tres renovaciones futuras. Si solo es una app, se puede saltar y hacerlo a mano.

La cuarta hora es Husk y su paquete. Se abre el APK, se elige motor —traducción para lo ligero, emulación para lo que necesita servicios— y se acepta que la primera vez tarda más de lo que tardará después.

Al final de la tarde hay un icono que abre y una lista de cosas pendientes: qué programas funcionaron, cuáles no y por qué. Esa lista vale más que la instalación, porque es lo que evita repetir la tarde la semana que viene.

───────────────────

*🗂️ Qué hacer cuando caduca*

La caducidad no avisa con un mensaje claro: el icono se queda en la pantalla, se toca y no pasa nada, o se cierra al instante. Cuando pasa en todas las apps a la vez, la causa es la firma; cuando pasa en una sola, es la app o el paquete.

Si la firma era gratuita y caducó, la solución es renovar con el servicio del teléfono encendido y la app de la tienda alternativa abierta. Tarda un minuto y no borra los datos.

Si la firma era de un certificado ajeno y fue revocada, no hay renovación posible: hay que esperar a que su dueño publique otro o cambiar de puerta. Es el escenario donde la gente pierde las partidas guardadas, y por eso el respaldo dentro de cada app importa antes de instalar.

Si el aparato tenía el arranque abierto y una actualización del sistema lo cerró, la respuesta honesta es que esa puerta ya no está. Algunas instalaciones sobreviven a la actualización y otras no, y no hay manera de saberlo antes de actualizar.

En los tres casos la lección es la misma: la cadena tiene fecha, y esa fecha se escribe en el calendario el día que se instala, no el día que falla.

───────────────────

*🧪 Probar sin romper el teléfono*

El teléfono de las pruebas no tiene que ser el teléfono de la vida. Un aparato viejo, con la sesión de la tienda cerrada y sin cuentas dentro, es el banco de pruebas ideal, y en esta cadena la recomendación no es un lujo: es la única forma de probar sin arriesgar los datos de las cuentas.

Con un aparato así se puede hacer lo que en el bueno sería imprudente: instalar tres paquetes de origen dudoso, romper la cadena y volver a montarla, cambiar de puerta y comparar. Ese aprendizaje no se paga con nada, y después se aplica una sola vez en el aparato importante.

Si no hay aparato viejo, el orden cambia: primero el programa de prueba inocuo, después el que importa, y nunca al revés. Y antes de cada paso, un respaldo de lo que haya dentro de la app que se va a tocar.

La tercera opción es no probar. Suena a derrota y a veces es la respuesta correcta: para una app que se usa una vez al mes, la cadena entera cuesta más que la app.

───────────────────

*📶 La depuración inalámbrica, esa gran olvidada*

En los dos mundos —Android con Shizuku y iPhone con SideStore— la pieza que hace posible no depender de una computadora es la misma: el permiso de depuración inalámbrica. Es la función menos glamorosa del sistema y la que sostiene la mitad de este ecosistema.

En el iPhone, SideStore la usa para renovar la firma desde el propio teléfono, con un aparato auxiliar o un servicio local que hace de puente. En Android, Shizuku la usa para arrancar su servicio tras cada reinicio. En los dos casos, el permiso se activa en un menú escondido, se empareja una vez y se mantiene vivo mientras el sistema quiera.

Cuando falla, falla en silencio: el emparejamiento caduca, el servicio no arranca, la renovación se queda a medias. Y como no da un mensaje claro, la gente concluye que el proyecto está roto cuando lo que está roto es el emparejamiento.

La costumbre que sirve es revisarlo el mismo día que se revisa el respaldo: abrir el menú, ver si el emparejamiento sigue ahí, y si no, volver a hacerlo. Dos minutos al mes que ahorran una tarde al trimestre.

───────────────────

*🧭 Cinco cosas que se pueden probar hoy*

Para quien quiera empezar sin teoría, cinco programas que históricamente han funcionado bien en capas de traducción, por ser de un jugador y no pedir servicios a nadie: un juego de plataformas antiguo, un emulador de consola de ocho bits, una calculadora científica, un lector de archivos comprimidos y un reproductor de música local.

Los cinco comparten la misma virtud: no preguntan nada al sistema fuera de lo que la capa ya imita. Y los cinco sirven para medir la salud de una versión nueva de la capa: si dejan de funcionar los cinco, el problema es la capa; si falla uno, es ese programa.

La lista no es una recomendación de contenido: es un banco de pruebas. Y como banco de pruebas, lo que importa no es que funcionen, sino que sirvan para comparar la versión de ayer con la de hoy.

───────────────────

*🔋 Batería, calor y las tres horas que nadie cuenta*

Una capa de traducción consume como un juego: el procesador del iPhone es rápido y el programa original no fue escrito para ahorrar en un aparato de bolsillo. Media hora de juego deja el teléfono tibio; una hora lo deja caliente y con un veinte por ciento menos de batería.

El huésped emulado es otra liga. Levantar un sistema completo dentro de otro significa simular instrucciones, y eso se paga en calor y en batería antes que en fluidez. Es la razón por la que la emulación sirve para una app que se necesita una vez y no para el uso diario.

Hay tres costumbres que alargan la sesión. La primera, jugar con el teléfono enchufado y sin funda, porque la funda es un abrigo. La segunda, bajar el brillo y desactivar el modo de alta frecuencia de pantalla si el aparato lo tiene. La tercera, cerrar lo que no se está usando: en un teléfono pequeño, cada cosa abierta compite por la misma memoria.

Ninguna de las tres arregla el problema de fondo, que es que se está pidiendo a un aparato de bolsillo el trabajo de otro. Las tres, juntas, sí convierten una sesión de veinte minutos en una de cuarenta.

───────────────────

*🕹️ El añadido de consola*

La descripción de Husk incluye una tercera función que no tiene nada que ver con Android: paquetes y carpetas de juego de consola en versiones recientes del sistema. Es un detalle curioso y explica una parte del público del proyecto.

Lo que enseña ese detalle es que estos programas crecen por donde su comunidad los empuja y no por donde su descripción original apuntaba. Un proyecto que empieza llevando apps de Android a un iPhone acaba con una función de consola porque alguien la pidió y alguien la escribió.

Para quien lee estas guías, la consecuencia es práctica: la descripción de un repositorio no es su frontera. Antes de descartar un proyecto por su nombre, se lee su lista de versiones, que es donde aparece lo que de verdad hace hoy.

Y para quien escribe, la lección contraria: un proyecto con una función extra y bien mantenida atrae público que no venía por la función principal. Eso no lo hace mejor ni peor; lo hace más difícil de describir en una línea, que es el problema de casi todo lo que crece.

───────────────────

*🧑🔧 El que ayuda a otros*

Hay un personaje que aparece en todos los grupos: el que ya montó la cadena y la explica a los demás. Su utilidad no está en instalar el paquete ajeno, está en decir tres cosas antes de que el otro pierda la tarde: qué versión del sistema tiene, qué puerta le toca y qué esperar del programa que quiere.

Las tres respuestas se pueden dar sin tocar el teléfono de nadie. La primera se lee en los ajustes; la segunda depende de si tiene cuenta de desarrollador, certificado ajeno o un aparato con el arranque abierto; la tercera se contesta mirando el programa y su lista de dependencias.

El error del que ayuda es ponerse a instalar. Cuando la persona se lleva el teléfono con un icono que abre, no aprendió nada, y la semana que viene vuelve con el mismo problema y el icono cerrado. Cuando se lleva las tres respuestas, la próxima vez no vuelve.

Esa es la regla que esta casa aplica también a sus guías: antes de tocar, entender qué se está tocando y quién paga cuando falla.

───────────────────

*📚 Lo que se aprende en el camino*

Después de montar esta cadena una vez, tres ideas quedan claras y sirven para cualquier otro ecosistema.

La primera es que el sistema operativo no es el aparato: es una política. Lo que se puede instalar lo decide una firma, y la firma se administra. Entender eso cambia la relación con el teléfono, sea de la manzana o del robot.

La segunda es que las puertas pequeñas se mantienen con proyectos pequeños. UTM tiene ★36.633 y Husk ★2.937; las dos cifras conviven porque las dos puertas son distintas. Buscar el proyecto grande que resuelva todo es no haber entendido la forma del ecosistema.

La tercera es que la fecha manda. Un repositorio con versión de hoy es una promesa de esta semana; un repositorio con versión de hace tres años es una pieza que funciona hoy y que nadie va a arreglar mañana. Con esas tres ideas, la mitad de las preguntas de esta guía se contestan solas.

───────────────────

*📝 Los apuntes de la tarde, tal como quedaron*

Tres líneas de libreta que resumen la cadena y que sirven de plantilla para la próxima vez. La primera: qué aparato, qué versión del sistema y qué puerta. La segunda: qué programa, qué motor y qué funcionó. La tercera: qué caduca y cuándo.

Con esas tres líneas escritas, la próxima instalación no empieza de cero. Y si alguien pregunta en un grupo cómo se hace, la respuesta se copia de la libreta en lugar de reconstruirse de memoria, que es como se propagan los errores.

*🔎 Cuatro preguntas que se hacen antes de bajar el archivo*

¿Qué programa es y qué pide? Un programa que pide acceso a la red para nada es el primer aviso.

¿Qué versión del sistema tengo? Husk pide iOS 15.5 o superior, y por debajo de eso la conversación termina.

¿Qué puerta me toca? Sin cuenta de desarrollador ni aparato con el arranque abierto, no hay cadena posible.

¿Cuánto voy a renovar? Si la respuesta a esa pregunta ya cansa, la cadena no es para esa persona y es mejor saberlo antes de empezar.

Cuatro preguntas, dos minutos, y la tarde se salva o se gasta con conocimiento de causa.

───────────────────

*❓ Preguntas que me hacen*

**¿Husk es un emulador de Android?** Es un programa con dos motores: una capa de traducción que hace correr el código de 64 bits del paquete sin arrancar Android, y un huésped completo bajo emulación para lo que la capa no alcanza. Decir que es solo un emulador es impreciso, y decir que no emula nada, también.

**¿Necesito jailbreak para usar Husk?** No. Se instala por las puertas de siempre del iPhone —SideStore, AltStore o un aparato con TrollStore— y pide iOS 15.5 o superior.

**¿Puedo usar las apps de Google dentro de Husk?** No de forma fiable. Lo que depende de servicios de la casa de Google encuentra una pared que la capa no suple.

**¿Por qué se cierra un juego al arrancar?** Casi siempre por una comprobación de integridad o una biblioteca que la capa no imita. Probarlo por emulación separa el diagnóstico en un minuto.

**¿SideStore o AltStore?** AltStore es más viejo y más documentado; SideStore intenta renovar sin computadora y su versión 0.7.0-alpha del 15 de septiembre dice que está en construcción. Con las dos se firma; la diferencia es cuántas veces hay que buscar el cable.

**¿Para qué sirve LiveContainer si ya tengo SideStore?** Para gastar menos cupos de firma: metes varias apps dentro de un contenedor y renuevas una sola vez. Es la pieza que hace manejable el límite de aplicaciones.

**¿Por qué se firma con cupos si el programa es libre?** Porque el cupo no lo pone la licencia del programa, lo pone el sistema del teléfono. El código te da permiso sobre el código y no sobre la puerta.

**¿Sirve para el teléfono de trabajo?** Solo con autorización de quien administra ese teléfono, y casi nunca vale la pena. Las políticas de empresa y las garantías tienen más peso que la comodidad de una app.

**¿Cuánto pesa todo esto?** El emulador con su sistema invitado ocupa varios gigas y la batería se resiente. La capa de traducción pesa mucho menos y va a la velocidad del aparato, que es su ventaja real.

**¿Y al revés: Android con un sistema de iPhone?** No existe en ningún sentido práctico. El camino inverso que sí funciona es el sistema invitado dentro de Android, con DSU-Sideloader, y sirve para probar un sistema sin tocar el de todos los días.

───────────────────

*📊 Tabla, mitos y glosario*

*Los ocho medidos, en una línea*

| Proyecto | Papel en la cadena | Licencia | Empujón | Estrellas |
|---|---|---|---|---|
| Husk | traducir y emular Android en iOS | GPL-2.0-or-later | 01-nov | ★2.937 |
| UTM | emulador de sistemas en iOS | Apache-2.0 (README MIT) | 01-nov | ★36.633 |
| AltStore | instalar y renovar | AGPL-3.0 | 21-oct | ★14.821 |
| SideStore | instalar y renovar sin cable | AGPL-3.0 | 27-oct | ★7.188 |
| LiveContainer | contenedor de apps | AGPL-3.0 (README MIT) | 17-oct | ★13.674 |
| SignTools | firmar en servidor propio | AGPL-3.0 | 12-oct | ★2.242 |
| Dadoum/Sideloader | firmar desde cualquier sistema | GPL-3.0 | 18-sep | ★1.063 |
| ipaverse | descargar, refirmar e instalar | MIT | 22-sep | ★689 |

*Cinco mitos del teléfono ajeno*

**Mito uno: «con esto tienes Android en el iPhone».** Tienes un programa de Android corriendo sobre una capa, o un sistema lento dentro de un emulador. Ni escritorio, ni servicios, ni notificaciones.

**Mito dos: «una vez instalado, ya está».** La firma caduca. Instalar es la mitad del trabajo y renovar es la otra.

**Mito tres: «es igual que en Android».** En Android se instala un APK y punto; aquí hay una cadena de cinco estaciones y tres puertas. La diferencia de esfuerzo es de una tarde contra cinco minutos.

**Mito cuatro: «más estrellas, mejor». ** UTM tiene ★36.633 y sirve para otra cosa: emular sistemas. Husk tiene ★2.937 y es el que traduce paquetes de Android. La cifra sin propósito no dice nada.

**Mito cinco: «si es libre, es legal en todas partes».** La licencia cubre el código. El teléfono tiene sus reglas y el contenido tiene sus dueños.

*Glosario*

**Sideload** — instalar un programa por fuera de la tienda del sistema.

**Firma de desarrollador** — permiso temporal que el teléfono acepta para abrir programas no oficiales.

**Contenedor** — programa que envuelve varias apps para gastar una sola firma.

**Capa de traducción** — conjunto de piezas que imitan el sistema que el programa espera.

**Huésped** — sistema completo que corre dentro de un emulador.

**Revocación** — cierre de un certificado que deja sin abrir todos los programas firmados con él.

───────────────────

*🔗 Enlaces*

Todas las direcciones se abrieron esta tarde.

- Husk, Android en el iPhone: https://github.com/Leviidev/Husk
- UTM, el emulador: https://github.com/utmapp/UTM
- AltStore: https://github.com/altstoreio/AltStore
- SideStore: https://github.com/SideStore/SideStore
- LiveContainer: https://github.com/LiveContainer/LiveContainer
- SignTools: https://github.com/SignTools/SignTools
- Dadoum/Sideloader: https://github.com/Dadoum/Sideloader
- ipaverse: https://github.com/bahattinkoc/ipaverse
- DSU-Sideloader, el camino inverso en Android: https://github.com/VegaBobo/DSU-Sideloader

*Lo que quedó fuera.* Dos direcciones se probaron y no dieron ficha: una devolvió 404 y otra no tenía README legible. Se nombran como huecos en las notas del corte.

*Cómo se midió.* Ocho proyectos con las tres lecturas completas —búsqueda de la forja, página del repositorio y README crudo— y el orden rotado; las versiones se pidieron una por una. Dos fichas declaran una licencia y su README otra, y las dos versiones van publicadas.

───────────────────

*🌅 Cierre — la puerta pequeña*

Lo que deja esta guía es una cadena, no una app. El iPhone no deja instalar; alguien firma, alguien instala, alguien renueva y alguien traduce. Husk pone la última pieza con ★2.937 y una versión de hoy; las demás llevan su propia fecha y su propio papel.

El hallazgo del corte es simple: la pieza más famosa de esta cadena no es la que hace funcionar Android, es la que emula sistemas, y la que hace manejable todo el resto es un contenedor de ★13.674 que casi nadie menciona en los videos. Esa es la forma que tiene este ecosistema de esconder lo importante en el sitio menos vistoso.

Y el aviso que hay que dejar escrito: aquí todo caduca. Un icono que deja de abrir no es una traición del proyecto, es la puerta cerrándose donde siempre se cierra.

> —¿Y si dentro de un año ya no funciona nada de esto?
> —Entonces alguien habrá abierto otra puerta más pequeña. Y tú ya sabrás leer su fecha.

💓 *La Bandita informa a partir de fuentes fechadas.* Un sistema no se mete en otro teléfono sin pagar peaje: el peaje se llama firma.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 17:41 y las 17:52 de Santo Domingo · ocho proyectos medidos tres veces con el orden rotado · cinco releases consultadas aparte con su fecha · dos direcciones sin ficha, anotadas como huecos.

*Licencia de esta entrega:* texto en CC BY-SA 4.0, datos en CC BY 4.0, código de ejemplo en MIT; la marca y el nombre de la casa quedan reservados a «Alexis (La Bandita)».

## 🗒️ Notas al pie

**Nota de corte (1-nov):** Husk publicó la 3.3 el mismo día del corte y UTM empujó ese día; las dos fechas van escritas y no se redondearon.

**Nota de licencia (1-nov):** UTM, LiveContainer y Husk tienen ficha y README que no coinciden del todo. Se publican las dos versiones, como en el resto de la serie.

**Nota de hueco (1-nov):** dos direcciones probadas no dieron ficha: una respondió 404 y otra no tenía README legible en ninguna rama. Quedan como hueco y no como ficha incompleta.

**Nota de alcance (1-nov):** la guía no explica cómo saltarse las firmas ni cómo obtener programas de pago fuera de su tienda; cuenta qué piezas existen, con qué licencia y con qué fecha.

**Nota de corrección (1-nov):** la versión anterior describía Husk con datos del 15 de octubre y sin la cadena de firma alrededor, que es la mitad del asunto. Se reescribió con el censo de esta tarde.
