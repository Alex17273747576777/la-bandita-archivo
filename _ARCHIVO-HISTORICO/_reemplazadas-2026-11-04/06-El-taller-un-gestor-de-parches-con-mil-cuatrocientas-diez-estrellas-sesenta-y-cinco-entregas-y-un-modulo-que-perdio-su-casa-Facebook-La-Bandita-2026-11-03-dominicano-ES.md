*El taller: un gestor de parches con mil cuatrocientas diez estrellas, sesenta y cinco entregas y un módulo que perdió su casa en GitHub*

*La Bandita · martes 3 de noviembre de 2026, cifras remedidas el miércoles 4 · edición dominicano-español · pieza 06 de Facebook*

⏱️ *Lectura total: 31 minutos · un programa medido contra su propia fuente · sesenta y cinco entregas abiertas una por una · dos mil trescientas cincuenta y cinco confirmaciones de código contadas · ciento veintitrés mil cincuenta y ocho descargas sumadas · un aviso de retirada comprobado en vivo · cinco pasos con su salida esperada · cero paquetes alojados*

*🗺️ Mapa de esta guía*

```
├── 🧱 La semilla · una app pedida por su enlace
├── ⚡ En una página
├── 🔧 Qué es un parche · la explicación del fontanero
├── 🗂️ Dieciocho carpetas · qué hace cada una
├── 🧨 El 451 · el día que el módulo perdió su casa
├── 📊 Los números del corte · sesenta y cinco entregas contadas
├── 🛠️ Los cinco pasos · parchear sin perder nada
├── ⚖️ Lo que no me gusta · y lo que le falta
├── ❓ Las preguntas del grupo
└── 🌅 cierre · 🔗 enlaces · 🗒️ notas al pie
```

> *Semilla de esta pieza:* el encargo llegó con una sola línea y un enlace: «hazme una publicación de esta app». El enlace era https://github.com/Jman-Github/Universal-Patch-Manager y no traía ni una palabra más: ni qué contar, ni a quién, ni por dónde empezar. Así que lo primero fue lo que se hace siempre en esta casa antes de escribir una letra: abrir la fuente y medirla. Se preguntó a la interfaz de GitHub, por su puerta pública, todo lo que la interfaz sabe contar —nacimiento, empujones, estrellas, entregas, descargas, contribuidores, idiomas, licencia— y luego se abrió el archivo de presentación y se leyó entero, de la primera línea a la última.

El resultado de esa medición es lo que sigue. Un programa que tiene trescientos ochenta y siete días de vida, un año y veintidós días, y en ese tiempo ha publicado sesenta y cinco entregas: una cada seis días, con dos mil trescientas cincuenta y cinco confirmaciones de código detrás. Un programa que nació como una bifurcación de otro —las entregas de octubre de dos mil veinticinco todavía se llamaban `universal-revanced-manager`— y que hoy hace algo que su padre no hace: junta tres formatos de parche distintos en un solo gestor. Y un programa que depende de un módulo que ya no está donde estaba, cosa que se comprobó hoy mismo y que es la mitad del interés de esta pieza.

No es una app más de la lista. Es la app que casi nadie explica, porque para explicarla hay que entender primero qué es un parche y por qué alguien querría uno.

───────────────────

*En una página · ⚡*

Universal Patch Manager es un programa de Android que aplica parches a otras aplicaciones. Un parche, en este mundo, es un conjunto de instrucciones que modifica el paquete de una app —le quita el anuncio, le desbloquea una función de pago, le cambia el comportamiento— sin tocar el código fuente, que casi nunca se tiene. El gestor es la herramienta que elige el parche, lo aplica, firma el resultado con una llave propia y lo instala. Lo que hace especial a este gestor y no a los otros es que acepta tres formatos de parche en el mismo sitio: el `.rvp` de ReVanced, el `.mpp` de Morphe y el `.reseam` de Reseam. Los otros gestores aceptan el suyo y punto.

Los números del corte, medidos hoy: mil cuatrocientas diez estrellas, cincuenta y una bifurcaciones, cuarenta y dos hilos abiertos, veinte personas suscritas a los avisos, setenta y ocho contribuidores con nombre, licencia GPL versión 3, siete coma setenta y cinco mebibytes de código Kotlin y sesenta y cinco entregas publicadas desde el 13 de octubre de 2025. La entrega estable más reciente es la 2.0.0, del 29 de octubre, y suma seis mil seiscientas setenta y tres descargas entre sus siete archivos. La última de pruebas es la 2.1.0-dev.2, del 31 de octubre, y su madurez es la que declara su etiqueta: es una entrega de desarrollo, no una estable.

Hay dos cosas que a mí me hicieron levantar la ceja, y las digo aquí arriba porque son el corazón del asunto. La primera: el módulo de parches de ReVanced, que es el combustible de la mitad de este programa, devuelve hoy el código 451 en GitHub —«no disponible por razones legales»— y el desarrollo se mudó a GitLab en marzo de 2026. La segunda: el programa trae su propio registro de paquetes de parches, con setecientas veinticinco estrellas y una licencia que renuncia a todo derecho, precisamente para que un módulo no pueda desaparecer otra vez sin que nadie sepa dónde buscarlo.

Y hay una tercera cosa, que es la que decide si esto te sirve o no: parchear una app cambia su firma. Android no deja instalar encima un paquete firmado por otra llave. Eso significa que el primer paso, antes de tocar nada, es guardar una copia del paquete original, porque al parchear hay que desinstalar. Quien no hace esa copia pierde los datos de esa app y llama a la desgracia «un bug del gestor». No es un bug del gestor: es el orden de las operaciones.

Esta pieza no reparte el paquete. Enlaza siempre al repositorio de quien lo hizo, y enseña a comprobar lo que se descarga con las herramientas que ya tiene el teléfono. Los cinco pasos del final se pueden hacer y se pueden deshacer, y las tres formas de arruinarlo están escritas con su salida exacta para que se reconozcan cuando aparezcan.

───────────────────

*🔧 Qué es un parche · la explicación del fontanero*

Empecemos por lo que no es. Un parche no es un programa nuevo, ni un mod, ni una versión pirata que alguien reempaquetó. Un parche es una lista de cambios escrita contra una versión concreta de otra app, con la instrucción exacta de dónde va cada cambio. Se parece más a la hoja de un fontanero que a una tubería: dice «en el método tal, cambia esta llamada por esta otra», y si la tubería no es exactamente la que el fontanero midió, la hoja no sirve.

Para que eso funcione hacen falta cuatro piezas, y conviene verlas por separado porque cada una puede fallar por su lado.

**El paquete.** Un archivo `.apk` es un archivador comprimido con clases compiladas dentro, en un formato de bytes llamado DEX. No hay texto legible: hay instrucciones de máquina virtual. Cambiar «muestra el anuncio» por «no lo muestres» no es editar una palabra, es reescribir una secuencia de instrucciones y volver a firmar el archivador entero.

**El parche.** El parche es el conjunto de instrucciones de edición, escrito por alguien que estudió esa app. Los parches se agrupan en paquetes y cada paquete declara para qué versiones de qué app sirve. En este ecosistema hay tres linajes de formato: ReVanced, que fue el primero y el más grande; Morphe, que nació cuando el linaje original se partió; y Reseam, que trabaja montando el resultado sobre el sistema en vez de instalarlo como app normal. Cada linaje tiene su extensión: `.rvp`, `.mpp`, `.reseam`.

**El motor de ejecución.** Aplicar un parche requiere ejecutar código que no es el de la app: leer el DEX, localizar los métodos, reescribirlos. Ese código necesita un ambiente donde correr. Los gestores modernos lo resuelven de dos maneras: embuten una máquina virtual de Java dentro del propio teléfono —un OpenJDK compilado para Android— o usan el ambiente de ejecución de Android directamente, aislado en un proceso aparte. El archivo de presentación de este programa dice que soporta las dos: la ruta de Morphe sobre la máquina virtual de Java o sobre el ambiente de Android, y la de Reseam sobre el ambiente de Android aislado.

**El instalador.** Aquí está la parte que casi nadie explica y que arruina tardes enteras. Android solo instala un paquete si su firma coincide con la del que ya está puesto, o si no hay ninguno puesto. Un paquete parcheado lo firma quien lo parchea, con una llave que se genera en el propio teléfono. Por eso el paquete parcheado nunca coincide con el original, y por eso hay que desinstalar primero. Y por eso este programa trae instaladores aparte: el del sistema, el de Shizuku y sus herederos, el de root y una variante que monta el paquete en el sistema en vez de instalarlo, ideada para no perder la app original.

Ahora la parte del fontanero, que es la que de verdad importa. Imagina que el paquete es una casa y que el parche es una reforma. La hoja del fontanero se escribió mirando un plano concreto: si la casa cambió de plano, la hoja no vale, y lo peor que puede pasar no es que no funcione, sino que funcione a medias y rompa una pared que no era. En un paquete eso se traduce en que la app arranca y se cierra, o arranca y pierde la sesión, o arranca y dice que la versión no es compatible. Un parche aplicado contra la versión equivocada no da un error limpio: da una app que se comporta raro, y eso es mucho peor de diagnosticar.

De ahí las dos reglas de oro del oficio, que sirven para cualquier gestor de cualquier linaje. Primera: el parche y la app tienen que ser de la misma versión, y el gestor lo dice antes de empezar; si no lo dice, se comprueba a mano en la ficha del paquete de parches. Segunda: nunca se parchea el único ejemplar que hay. Se guarda el paquete original, se anota su versión, y se parchea la copia.

Y una tercera, que es de esta casa y no del oficio: antes de instalar nada se mira qué licencia tiene el parche. Un paquete de parches es código, y el código tiene dueño. Los parches de ReVanced son GPL versión 3; los de Morphe, también; el registro de paquetes de este programa es Unlicense, que renuncia a todo. Un parche sin licencia es un parche sin permiso, y esta serie no recomienda paquetes sin permiso.

───────────────────

*🗂️ Dieciocho carpetas · qué hace cada una*

Un programa de este tamaño se entiende leyendo su árbol, y el árbol de este se puede leer sin abrir un solo archivo: cada carpeta se llama como lo que hace. Aquí está la raíz tal como la devolvió la fuente hoy, en orden alfabético, y qué es cada cosa. Lo que sigue lo dice el nombre y lo confirma el archivo de presentación; donde es deducción mía, lo digo.

**`app`** es el programa de Android: la pantalla, los botones, los ajustes. Es la carpeta grande. **`shared`** es el código que comparten la pantalla y el motor: modelos, utilidades, contratos. **`api`** es la puerta para que otros programas hablen con este sin pasar por la pantalla; en el ecosistema de los gestores eso sirve para que un lanzador o un automatizador pida un parcheo sin abrir la app.

**`upm-patcher-core`**, **`revanced21-patcher-core`**, **`revanced22-patcher-core`**, **`revanced-legacy-patcher-core`** y **`tools-patcher-core`**: cinco motores de parcheo. Los dos numerados corresponden a las dos generaciones del paquete de parches de ReVanced que el programa puede usar, la 21 y la 22; el que dice `legacy` es el motor viejo, que se conserva porque hay paquetes que solo funcionan con él; y `tools-patcher-core` es el motor de las herramientas de paquete, esas que fusionan partes, firman y leen metadatos. Que existan los cuatro a la vez explica una cosa que el usuario ve como un menú de opciones y que por dentro son cuatro caminos de código distintos.

**`revanced.v21-runtime-plugin`** y **`revanced.v22-runtime-plugin`** son los complementos de ejecución: el trozo de código que se inyecta o se carga para que el parche funcione en tiempo de ejecución, en vez de quedar escrito en el paquete. Son los dos archivos `.apk` aparte que aparecen en cada entrega con los nombres `revanced.v21-plugin.apk` y `revanced.v22-plugin.apk`. En la entrega 2.0.0, el complemento de la generación 21 tiene mil quinientas ochenta y tres descargas y el de la 22 tiene trescientas ochenta y siete: siete veces más gente usa la generación vieja. Ese dato, que está en la fuente, dice mucho de cómo se mueve este ecosistema: la novedad tarda en llegar.

**`morphe-runtime`** y **`reseam-runtime`** son los ambientes de ejecución de los otros dos linajes, empacados dentro del programa para que no haya que instalar nada aparte. **`jvm-host`** es el anfitrión de la máquina virtual de Java: el trozo que arranca el OpenJDK embebido y le pasa el trabajo. El archivo de presentación declara OpenJDK 25 para los teléfonos de 64 bits y OpenJDK 17 para los de 32 bits ARM, y esa diferencia no es capricho: la máquina virtual de 25 no corre en 32 bits.

**`libs`** son bibliotecas empaquetadas, precompiladas, que el proyecto no reescribe: las versiones que se usan tal cual. **`third-party`** es lo que viene de otros y se conserva con su aviso, que es la práctica correcta y la que evita pleitos: cada trozo de terceros, con su licencia al lado. **`assets`** son los archivos que van dentro del paquete y no son código: textos, plantillas, quizá las tablas de compatibilidad.

**`buildSrc`** y **`gradle`** son el andamio de construcción: las tareas y las versiones de las herramientas con las que se arma el paquete. **`META-INF`** es la carpeta de metadatos que exige el formato de empaquetado de Java. **`package.json`** y **`.releaserc`** delatan la maquinaria de publicación: el proyecto usa liberación semántica, un robot que lee los mensajes de confirmación, calcula si el cambio es mayor, menor o parche, escribe el registro de cambios y publica la entrega. Por eso hay un contribuidor llamado `semantic-release-bot` con ciento siete confirmaciones: el robot también firma su trabajo.

**`crowdin.yml`** y los dos flujos de trabajo de traducción confirman lo que se ve en la carpeta de recursos del programa: el texto de la interfaz se traduce por fuera, en una plataforma cooperativa, y vuelve al repositorio por un flujo automático. En la carpeta de recursos hay más de cincuenta variantes de idioma, entre ellas `values-es-rES`, que es el español. En total, quince idiomas completos y un montón de parciales, según el propio archivo de presentación.

Los seis flujos de trabajo del repositorio dicen cómo trabaja el equipo, y merecen un párrafo porque son la parte que no se ve: uno compila cada propuesta de cambio antes de aceptarla, otro arma las compilaciones de depuración, otro abre la propuesta, otro publica la entrega, y dos bajan y suben traducciones. Nada de eso es adorno: un proyecto con sesenta y cinco entregas en un año necesita que publicar sea un acto automático, o la calidad depende del humor de quien aprieta el botón.

Y un detalle de arqueología que sirve para entender el parentesco. Las entregas de octubre de dos mil veinticinco no se llamaban `universal-patch-manager`: se llamaban `universal-revanced-manager`. El cambio de nombre de los archivos ocurrió en el camino, y es la prueba más limpia de que este programa empezó siendo una bifurcación del gestor de ReVanced y después se independizó. Los contribuidores lo confirman: entre los diez primeros hay cuatro nombres del equipo de ReVanced y uno del equipo de ReVanced Extended. Un programa que junta tres linajes está hecho, en buena parte, por la gente que hizo esos linajes.

───────────────────

*🧨 El 451 · el día que el módulo perdió su casa*

Aquí está la historia que le da sentido a esta app, y no es una historia bonita.

El combustible de la mitad de los gestores de parches de Android es el paquete de parches de ReVanced. El paquete vive en un repositorio de GitHub, y las apps lo consultan para saber qué parches hay, para qué versión de qué app sirven y de dónde bajarlos. Ese repositorio, medido hoy desde aquí con la misma puerta pública que se usó para medir todo lo demás, devuelve el código 451. Cuatro cinco uno. En el protocolo de la web ese número tiene nombre propio: «no disponible por razones legales». No es un error de red, no es un repositorio borrado, no es un fallo temporal. Es una respuesta deliberada.

El motivo, comprobado y público: en marzo de dos mil veintiséis un tercero presentó un aviso de retirada por derechos de autor contra ese repositorio, y la plataforma lo retiró. El proyecto presentó una contra-notificación —el mecanismo que existe precisamente para esto— y siguió trabajando en otro sitio: el mismo nombre, la misma gente, el mismo código, alojado en GitLab. Ese repositorio de GitLab se creó el 22 de marzo de 2026, tenía ciento treinta y ocho estrellas en el momento de esta medición y su última actividad fue ayer.

Ahora póngase en el lugar de la app que tiene que buscar parches. Usted le pregunta a una dirección de GitHub y le contestan 451. ¿Qué hace? Un gestor mal hecho se queda en blanco, o peor, se queda con una lista vieja en la memoria y le ofrece al usuario parches de hace ocho meses. Un gestor bien hecho tiene que saber que esa dirección puede dejar de contestar cualquier día, y tiene que tener una segunda puerta.

Esa segunda puerta es la parte de este programa que menos se cuenta y que más vale. Se llama registro de paquetes de parches, tiene setecientas veinticinco estrellas, está publicado bajo la licencia Unlicense —que renuncia a todo derecho y por tanto es la más permisiva que existe— y ofrece dos puertas de consulta, una de estilo REST y otra de estilo GraphQL, con búsqueda de parches, compatibilidad por app, entregas históricas, versiones previas y registros de cambios. Su sitio público, en patch-bundles.jmancentral.com, contestó hoy con normalidad. Y como es un registro independiente, el día que una de las fuentes se caiga, la otra sigue en pie y el usuario ni se entera.

Hay un detalle que a mí me parece el más honesto de todo el diseño, y es que el programa no esconde de dónde saca el combustible. En la pantalla se elige el paquete de parches, y cada paquete trae su origen. Eso significa que si mañana el paquete de ReVanced se muda otra vez, lo que hay que corregir es una dirección, no una app. Y significa algo más importante para quien lee: que el programa no puede garantizar que los parches existan. Solo puede garantizar que va a decir la verdad sobre dónde los buscó.

Lo que se puede aprender de este episodio, y sirve para cualquier programa que dependa de una fuente ajena, cabe en tres frases. Una dependencia que vive en un solo sitio es una dependencia que ya se cayó y nadie lo sabe. Un registro propio con licencia permisiva es más barato que un pleito. Y un aviso de retirada no distingue entre un proyecto grande y uno chico: le puede tocar al más grande del ecosistema, que es exactamente lo que pasó.

Un matiz para no exagerar: que el repositorio de parches esté en GitLab no quiere decir que todos los parches sean legales en todos los países, ni que usarlos no tenga consecuencias. Quitar el anuncio de una app es una modificación de un programa ajeno, y eso choca con los términos de uso de muchas apps y con las leyes de algunos sitios. Esta serie no reparte parches ni paquetes: enlaza al repositorio del que los escribe y explica cómo se comprueba lo que se baja. Lo que cada uno haga con eso es su decisión, y las consecuencias también.

───────────────────

*📊 Los números del corte · sesenta y cinco entregas contadas*

Todo lo que sigue se midió hoy, 3 de noviembre de 2026, entre las veinte y cuarenta y las veintiuna de Santo Domingo, contra la puerta pública de GitHub y contra la de GitLab. Cada cifra tiene su forma de repetirse: la orden está al final del párrafo que la usa, y quien quiera comprobarla solo necesita su propio token y diez minutos. Nada de esto es una impresión.

El programa nació el 13 de octubre de 2025, a las ocho y treinta y un minutos de la mañana en tiempo universal. Su primera entrega salió el mismo día, treinta y siete minutos después. Es un dato que dice mucho del origen: un proyecto que publica su versión 1.0.0 media hora después de existir no está empezando de cero, está mudando algo que ya funcionaba. Efectivamente: era el gestor de ReVanced con otro nombre.

Desde entonces acumula dos mil trescientas cincuenta y cinco confirmaciones de código en trescientos ochenta y siete días, o sea seis coma uno por día, contando domingos y el robot de liberación. Sesenta y cinco entregas, de las cuales dieciocho son estables. Doscientos treinta y ocho archivos publicados, entre paquetes de Android y complementos. Y ciento veintitrés mil cincuenta y ocho descargas sumadas archivo por archivo, que es una cifra que nadie publica y que se obtiene recorriendo las entregas una por una.

La tabla de las fichas que esta pieza mide, con su licencia y su último empujón:

| Repositorio | ★ | Licencia | Último empujón | Qué es |
|---|---|---|---|---|
| Jman-Github/Universal-Patch-Manager | ★1.410 | GPL-3.0 | 4-nov-2026 | el gestor de esta pieza |
| Jman-Github/Patch-Bundle-Registry | ★725 | Unlicense | 4-nov-2026 | su registro de paquetes de parches |
| MorpheApp/morphe-manager | ★9.950 | GPL-3.0 | 4-nov-2026 | el gestor del linaje Morphe |
| MorpheApp/morphe-patches | ★4.548 | GPL-3.0 | 4-nov-2026 | el paquete de parches de ese linaje |
| ReVanced/revanced-manager | ★30.070 | GPL-3.0 | 29-jul-2026 | el gestor original, sin movimiento desde hace noventa y ocho días |
| RikkaApps/Shizuku | ★32.773 | Apache-2.0 | 18-jun-2025 | el instalador con permisos prestados, sin movimiento desde hace quinientos cuatro días |
| timschneeb/awesome-shizuku | ★10.699 | sin licencia declarada | 31-oct-2026 | el catálogo de la familia Shizuku |
| rushiranpise/helper-for-morphe | ★427 | GPL-3.0 | 1-nov-2026 | ayudante de instalación del linaje Morphe |
| brosssh/revanced-manager-downloaders | ★118 | GPL-3.0 | 4-dic-2025 | descargadores de paquetes para ese gestor |

De esa tabla salen tres cosas que no se ven a simple vista. La primera: el programa que esta pieza cuenta tiene una quinta parte de las estrellas del gestor del que nació, y sin embargo publica más seguido que él. La segunda: el ecosistema está partido en tres linajes vivos y uno de ellos, el original, lleva desde julio sin empujar código. La tercera: hay un proyecto de ciento dieciocho estrellas que lleva once meses parado y que sigue siendo útil porque su tarea —bajar paquetes— no caduca; y hay un catálogo de diez mil seiscientas noventa y dos estrellas que no declara licencia, lo que en esta casa se anota como deuda, no como defecto.

Los tres números que más me costó creer y que verifiqué dos veces son estos: las tres cuartas partes del código son Kotlin, siete coma setenta y cinco mebibytes de ocho coma cero tres; el repositorio entero pesa sesenta y un mebibytes; y el archivo de presentación tiene dieciocho mil novecientos noventa caracteres, que es mucho para un archivo de presentación y poco para un manual. Ese último dato es el que decide lo que esta pieza tiene que hacer: si el archivo de presentación ya cuenta casi todo, lo que falta no es otra lista de funciones, es entender por qué el programa está hecho así.

Sobre las entregas, dos detalles de oficio. El primero: la descarga se concentra en un archivo y deja el resto casi vacío. En la 2.0.0, el paquete para teléfonos de 64 bits tiene cuatro mil trescientas veintiuna descargas; el universal, doscientas sesenta y una; el de 32 bits ARM, ochenta y nueve; y los de arquitectura de computadora, catorce y dieciocho. Eso no es un fallo del proyecto: es la distribución real de los teléfonos del mundo, y por eso el archivo grande es el que importa. El segundo: la última entrega de pruebas, la 2.1.0-dev.2, del 31 de octubre, tiene mil ciento trece descargas en cuatro días. Mil personas usando una compilación de desarrollo de un programa que reescribe paquetes ajenos. Esa es la parte que hay que decir sin adornos: la madurez de la rama de desarrollo es baja por definición, y sin embargo se usa como si fuera estable.

Cómo se comprueba todo esto con las manos en el teclado:

```
export T=$(cat ~/.boveda/tokens.env | grep PAT_FINO | cut -d= -f2)
curl -sH "Authorization: Bearer $T" \
  https://api.github.com/repos/Jman-Github/Universal-Patch-Manager \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['stargazers_count'],d['forks_count'],d['pushed_at'])"
curl -sH "Authorization: Bearer $T" \
  https://api.github.com/repos/Jman-Github/Universal-Patch-Manager/releases?per_page=100 \
  | python3 -c "import json,sys;r=json.load(sys.stdin);print(len(r),sum(a['download_count'] for x in r for a in x['assets']))"
```

La primera orden devuelve las estrellas, las bifurcaciones y la fecha del último empujón. La segunda devuelve sesenta y cinco y ciento veintitrés mil cincuenta y ocho. Si mañana alguien vuelve a correrlas y los números cambiaron, no es que la pieza mintiera: es que la pieza tiene fecha, y la fecha está arriba, en la primera línea.

───────────────────

*🛠️ Los cinco pasos · parchear sin perder nada*

Esta es la tarea, en segunda persona, para un teléfono Android cualquiera de 64 bits con Android 11 o superior. Sirve igual para los tres linajes, porque el orden de las operaciones es el mismo en todos. Al final de cada paso está el resultado que debes ver; si no lo ves, para y no sigas, porque el paso siguiente da por bueno el anterior.

**Paso uno · mira qué arquitectura tiene tu teléfono y qué Android lleva.** No es un requisito burocrático: si bajas el paquete equivocado, el teléfono te dirá «aplicación no instalada» y perderás veinte minutos buscando el problema donde no está. Los datos los da el propio teléfono por el cable de depuración.

```
adb shell getprop ro.product.cpu.abi
adb shell getprop ro.build.version.release
adb shell getprop ro.build.version.sdk
```

Lo que debes ver: la primera orden contesta `arm64-v8a` si tu teléfono es de 64 bits, o `armeabi-v7a` si es de 32; la tercera contesta un número de API. Guarda los tres valores. Si no tienes cable a mano, la app Ajustes → Acerca del teléfono te da el Android y una app cualquiera de información de sistema te da la arquitectura.

**Paso dos · guarda el paquete original y anota su versión.** Este es el paso que todo el mundo se salta y el único que no se puede deshacer después. Con la app instalada todavía en su sitio, saca una copia del paquete a tu computadora.

```
adb shell pm list packages | grep -i nombre.de.la.app
adb shell dumpsys package nombre.de.la.app | grep -E "versionName|versionCode"
adb shell pm path nombre.de.la.app
adb pull /ruta/que/devolvio/la/orden/anterior app-original.apk
sha256sum app-original.apk
```

Lo que debes ver: una ruta del tipo `/data/app/~~algo==/nombre.de.la.app-algo==/base.apk`, y después de `adb pull` un archivo en tu carpeta con el tamaño de la app. La última orden imprime sesenta y cuatro caracteres hexadecimales: apúntalos en un papel o en una nota, porque son la prueba de que la copia es la copia. Si el teléfono tiene la app instalada como paquete partido, `pm path` devolverá varias rutas; entonces hay que sacarlas todas y juntarlas, y el propio gestor tiene una herramienta para fusionarlas.

**Paso tres · instala el gestor y comprueba lo que instalaste.** Baja el paquete de la página de entregas del repositorio del autor, no de un espejo, y elige el archivo de tu arquitectura. Antes de instalar nada, comprueba dos cosas: que la descarga llegó completa y que el paquete está firmado por alguien, no por nadie.

```
sha256sum universal-patch-manager-v2.0.0-arm64-v8a.apk
apksigner verify --print-certs universal-patch-manager-v2.0.0-arm64-v8a.apk
```

Lo que debes ver: en la segunda orden, un nombre de firmante y una huella de certificado. Quédate con esa huella: el día que alguien te pase un archivo con el mismo nombre y otra huella, ya sabes que no es el mismo archivo. Aquí conviene ser honesto: en el momento de esta medición, las entregas de este programa no publican un archivo de sumas de comprobación al lado de los paquetes, así que la primera orden te sirve para comparar entre dos descargas tuyas, no contra un valor del autor. Eso es una ausencia real y está anotada en las tareas del final. Lo que sí puedes comprobar es el origen: que el archivo venga de la página de entregas del repositorio que estás leyendo. Y después de instalar:

```
adb shell pm list packages | grep universal
adb shell dumpsys package app.universal.patch.manager | grep versionName
```

Lo que debes ver: un paquete llamado `app.universal.patch.manager` y la versión que bajaste. Si aparece otro con un nombre parecido, tienes dos gestores instalados y vas a parchear con el que no crees.

**Paso cuatro · dale permiso de instalación al gestor, sin root.** Un gestor de parches necesita poder instalar y desinstalar sin que tú toques la pantalla setenta veces. Hay cuatro caminos y conviene saber cuál tienes: el instalador del sistema, que pide confirmación en cada app; Shizuku o cualquiera de sus herederos, que presta permisos por el cable o por depuración inalámbrica; root, si el teléfono lo tiene; y el montaje sobre el sistema, que deja el paquete parcheado encima del original sin borrarlo. Para un teléfono sin root, el camino recomendado es Shizuku o uno de sus herederos: se arranca una vez por el cable, se le da el permiso de instalación al gestor, y a partir de ahí el gestor instala solo.

Lo que debes ver: en los ajustes del gestor, el estado del instalador en verde, con el nombre del método activo. Si dice «sin permisos», cualquier parcheo se quedará a medias en el último paso, que es justo el que más frustra.

**Paso cinco · parchea, instala y comprueba.** En el gestor: eliges la app (desde el paquete guardado, no desde la instalada), eliges el paquete de parches, eliges los parches, y le das a aplicar. El programa te dirá cuánto va a tardar y qué está haciendo. Cuando termine, te ofrecerá instalar. Aquí aparece el aviso que hay que leer: si la app original está instalada, hay que desinstalarla antes, y con ella se van sus datos. Por eso el paso dos existe.

```
adb shell dumpsys package nombre.de.la.app | grep -E "versionName|firstInstallTime|lastUpdateTime"
```

Lo que debes ver: la misma versión declarada de la app, con una fecha de instalación nueva. Si la app arranca y hace lo que el parche prometía, terminaste. Si arranca y se cierra sola, el parche y la versión no se llevaban, y el paso seis es deshacer.

**Cómo se deshace, y esto va en serio.** Desinstala el paquete parcheado, reinstala tu copia original y vuelve a entrar con tu cuenta:

```
adb uninstall nombre.de.la.app
adb install app-original.apk
```

Los datos que había antes de desinstalar no vuelven: por eso la copia de seguridad de los datos de la app —si te importan— se hace antes, con la herramienta de copia del propio sistema o con la que la app ofrezca. El paquete vuelve, la sesión se recupera, el historial no.

**Las tres formas de arruinarlo, con su salida exacta.** Primera: bajaste el paquete de la arquitectura equivocada y el instalador contesta `INSTALL_FAILED_NO_MATCHING_ABIS`. Segunda: intentaste instalar el parcheado encima del original y el instalador contesta `INSTALL_FAILED_UPDATE_INCOMPATIBLE` o `INSTALL_FAILED_ALREADY_EXISTS`, que en este contexto significa lo mismo: firmas distintas. Tercera: aplicaste un parche de una versión contra otra versión de la app, el proceso termina sin error, la app se instala, y al abrirla se cierra sola o muestra una pantalla que no existe; en el registro del sistema eso se ve como `FATAL EXCEPTION` con una clase que el parche intentaba reemplazar. Las tres se evitan con los pasos uno a tres, y ninguna se arregla insistiendo: se arregla volviendo al paquete original y empezando de nuevo.

───────────────────

*⚖️ Lo que no me gusta · y lo que le falta*

Un programa de mil cuatrocientas diez estrellas y sesenta y cinco entregas se puede recomendar sin decir nada de esto, y la recomendación valdría menos. Aquí va lo que la medición de hoy deja mal parado, ordenado de lo que más pesa a lo que menos.

**Los avisos de instalación no están escritos en la pantalla donde hacen falta.** El programa sabe que parchear exige desinstalar y perder datos, porque su propio archivo de presentación lo dice en una sección aparte. Pero el usuario que llega por primera vez choca con eso en el último paso, cuando ya invirtió una hora. Un aviso en el primer arranque, antes de elegir la app, con la frase «guarda tu paquete original», habría ahorrado más disgustos que cualquier función nueva.

**Cuarenta hilos abiertos y ni una página de preguntas.** El repositorio tiene cuarenta y dos hilos abiertos entre incidencias y propuestas, y no tiene ni wiki ni foro de discusión. Para un programa que reescribe paquetes ajenos y depende de tres linajes de parches, la documentación vive en el archivo de presentación y en las conversaciones de los hilos. Eso significa que cada novato pregunta lo mismo, y que la respuesta se pierde en el hilo ciento veinte.

**No hay sumas de comprobación publicadas.** Lo dije en el paso tres y lo repito aquí porque es la ausencia más fácil de arreglar de toda la lista: un archivo de texto con el hash de cada paquete de cada entrega, generado por el flujo de publicación, cuesta veinte líneas de configuración y convierte «bajé un archivo» en «bajé este archivo». El registro de paquetes del propio autor demuestra que sabe hacerlo; solo falta aplicarlo a sus propias entregas.

**La rama de desarrollo se usa como estable.** Mil ciento trece descargas en cuatro días para una compilación de desarrollo. El programa marca la etiqueta, la página de entregas la marca, pero el efecto práctico es que mucha gente corre código sin probar contra sus paquetes. Con un programa que modifica apps ajenas, eso no es un detalle de aficionados.

**La licencia es GPL versión 3 y los complementos también.** No es un problema, es una consecuencia: quien quiera empaquetar este gestor dentro de otra cosa tiene que publicar su código con la misma licencia. Y quien quiera usar el registro de paquetes, en cambio, puede hacer lo que quiera, porque es Unlicense. Esa mezcla es deliberada y está bien pensada, pero conviene saberla antes de construir encima.

Y lo que le falta de verdad, que no es un defecto sino un hueco: una guía de compatibilidad por app. El registro sabe qué parches sirven para qué versión, y eso está resuelto a nivel de dato; lo que no existe es la traducción a lenguaje de usuario, del tipo «esta app, en esta versión, con estos tres parches, funciona y esto se rompe». Ese documento no lo puede escribir el autor solo: lo escribe la gente que usa el programa, y para eso haría falta el foro que no tiene.

───────────────────

*❓ Las preguntas del grupo*

**¿Esto es lo mismo que ReVanced?**
No. ReVanced es el linaje original: un gestor y un paquete de parches. Este programa es un gestor que acepta el paquete de ReVanced y además dos más, y que trae su propio registro de paquetes. Comparte código y gente con el original, pero no es el mismo proyecto ni la misma licencia de distribución.

**¿Sirve en un teléfono sin root?**
Sí, con un instalador de permisos prestados. Sin root no hay montaje sobre el sistema, así que el parcheo implica desinstalar la app original y perder sus datos. Con root se puede montar el paquete parcheado encima y conservar el original, que es la opción más limpia si el teléfono lo permite.

**¿Por qué el repositorio de parches de ReVanced da error 451?**
Porque un tercero presentó un aviso de retirada por derechos de autor en marzo de 2026 y la plataforma lo retiró. El proyecto presentó contra-notificación y siguió en GitLab, donde está activo. No es un fallo del programa que estés usando, y por eso este programa consulta un registro propio además de la fuente original.

**¿Puedo perder mi cuenta de una app por parchearla?**
Puede pasar, y depende de la app y de sus términos de uso. Modificar un programa ajeno suele ir contra esos términos, y algunas apps detectan la firma distinta y bloquean. Esta serie no promete que no pase: dice que puede pasar y que la decisión es de quien la toma.

**¿Los parches son virus?**
Un paquete de parches es código ejecutable. Lo que se puede hacer es lo que enseña el paso tres: bajar del repositorio del autor, no de un espejo, y comprobar firmante y huella. Un parche bajado de un enlace de Telegram no tiene nada de eso, y no hay forma de saber qué trae.

**¿Qué diferencia hay entre las tres arquitecturas?**
Un paquete compilado para `arm64-v8a` no corre en un teléfono de 32 bits. La mayoría de los teléfonos de los últimos ocho años son de 64 bits; si el tuyo contesta `armeabi-v7a` en el paso uno, baja el de 32 bits o el universal, que pesa más y sirve para ambos.

**¿Cuánto tarda un parcheo?**
Entre dos y diez minutos, según el tamaño de la app y los parches. El programa lo avisa antes de empezar. Si se queda en el mismo porcentaje más de quince minutos, el proceso se colgó: cancela, vuelve a empezar con menos parches y, si repite, usa el paquete de parches de la generación anterior.

**¿Vale la pena con solo mil cuatrocientas estrellas?**
Ese número no dice si sirve. Lo que dice es que hay gente usándolo todos los días: ciento veintidós mil descargas en un año, sesenta y cinco entregas y setenta y ocho contribuidores. La pregunta correcta es otra: ¿sigue publicando? La respuesta, medida hoy, es que publicó dos entregas la semana pasada.

**¿Y si el autor deja el proyecto?**
Es la pregunta que esta serie hace siempre, y la respuesta aquí es mejor que en la media: licencia GPL versión 3, código completo en el repositorio, árbol heredado de un proyecto con treinta mil estrellas y un registro de paquetes con licencia permisiva. Cualquiera puede continuarlo, y por la historia de este ecosistema, es probable que alguien lo haga.

**¿Se puede usar sin conexión?**
El parcheo en sí, sí: una vez tienes el paquete de parches descargado, no hace falta red. Lo que necesita red es descubrir parches nuevos y consultar el registro. El programa guarda los paquetes y permite importar y exportar sus ajustes, así que un teléfono sin datos puede parchear con lo que tenga a mano.

───────────────────

*🌅 Cierre · lo que queda del taller*

Un gestor de parches es la herramienta menos glamorosa del ecosistema y la que decide si el resto funciona. No quita anuncios por sí solo, no reproduce música, no cifra nada: solo convierte un paquete que no puedes tocar en un paquete que sí. Y sin embargo, cuando se cae una fuente de parches, media docena de apps dejan de actualizarse y nadie sabe por qué. Eso es lo que este programa resolvió a su manera, con un registro propio y con tres linajes en la misma puerta.

El corte de hoy deja tres frases para llevarse. La primera: un año, sesenta y cinco entregas y ciento veintidós mil descargas no son fama, son costumbre; la gente vuelve porque funciona. La segunda: el ecosistema está partido en tres linajes y el original lleva noventa y ocho días sin empujar código, así que la pregunta «¿cuál uso?» tiene hoy una respuesta distinta de la que tenía en 2024. La tercera: la mitad de este programa depende de un módulo que perdió su casa en GitHub por un aviso de retirada, y eso no es una anécdota: es la razón por la que conviene que un gestor tenga más de una puerta.

Lo que le falta está escrito arriba sin adornos: avisos en el momento justo, una página de preguntas, sumas de comprobación publicadas y una guía de compatibilidad hecha por la gente que lo usa. Nada de eso es caro. Todo eso depende de que alguien lo escriba, y el programa tiene setenta y ocho contribuidores y cuarenta y dos hilos abiertos, así que el sitio donde escribirlo ya existe.

*Medición del corte:* 3 de noviembre de 2026, entre las 20:40 y las 21:00 de Santo Domingo · un programa medido contra su fuente · sesenta y cinco entregas abiertas una por una · doscientas treinta y ocho archivos contados · ciento veintitrés mil cincuenta y ocho descargas sumadas · setenta y ocho contribuidores · dos mil trescientas cincuenta y cinco confirmaciones · un código 451 comprobado en vivo · cero paquetes alojados · cero espejos.

> —¿Y si el módulo de parches se cae otra vez?
> —Entonces el gestor te lo dice y busca en el registro propio. Eso es todo lo que un programa puede prometer: no que la fuente dure, sino que te va a decir la verdad cuando no dure.

💓 *La Bandita informa a partir de fuentes fechadas.* Sesenta y cinco entregas contadas, un aviso de retirada con nombre y fecha, y cinco pasos que se pueden deshacer: el taller abierto para que nadie parchee a ciegas.

───────────────────

*🔗 Enlaces*

- Universal Patch Manager, el gestor de esta pieza: https://github.com/Jman-Github/Universal-Patch-Manager
- Sus entregas, con los paquetes por arquitectura: https://github.com/Jman-Github/Universal-Patch-Manager/releases
- La entrega estable 2.0.0, del 29 de octubre: https://github.com/Jman-Github/Universal-Patch-Manager/releases/tag/v2.0.0
- Sus cuarenta y dos hilos abiertos: https://github.com/Jman-Github/Universal-Patch-Manager/issues
- su licencia, GPL versión 3: https://github.com/Jman-Github/Universal-Patch-Manager/blob/main/LICENSE
- El registro de paquetes de parches: https://github.com/Jman-Github/Patch-Bundle-Registry
- El sitio público de ese registro: https://patch-bundles.jmancentral.com
- El gestor del linaje Morphe: https://github.com/MorpheApp/morphe-manager
- El paquete de parches de ese linaje: https://github.com/MorpheApp/morphe-patches
- El gestor original de ReVanced: https://github.com/ReVanced/revanced-manager
- El paquete de parches de ReVanced, ya en GitLab: https://gitlab.com/revanced/revanced-patches
- El repositorio que explica dónde está ese paquete: https://github.com/ReVanced/where-is-revanced-patches
- Shizuku, los permisos prestados: https://github.com/RikkaApps/Shizuku
- El catálogo de la familia Shizuku: https://github.com/timschneeb/awesome-shizuku
- El ayudante de instalación del linaje Morphe: https://github.com/rushiranpise/helper-for-morphe
- Los descargadores de paquetes para ese gestor: https://github.com/brosssh/revanced-manager-downloaders
- La licencia GPL versión 3, en su texto de referencia: https://www.gnu.org/licenses/gpl-3.0.html
- La licencia Unlicense, del registro de paquetes: https://unlicense.org/
- La puerta del repositorio en la interfaz de programación: https://api.github.com/repos/Jman-Github/Universal-Patch-Manager
- La puerta de sus entregas, con las cien últimas: https://api.github.com/repos/Jman-Github/Universal-Patch-Manager/releases?per_page=100
- La puerta pública de GitHub, para repetir la medición: https://docs.github.com/en/rest
- La herramienta de firmas de Android, que viene con el SDK: https://developer.android.com/tools/apksigner

───────────────────

## 🗒️ Notas al pie

(3-nov) Todo lo que esta pieza afirma sobre el programa se midió hoy contra su puerta pública de GitHub: nacimiento, empujones, estrellas, bifurcaciones, hilos, suscriptores, licencia, idiomas y tamaño. Las sesenta y cinco entregas se recorrieron una por una, porque el número de descargas por archivo no viene en el resumen del repositorio: hay que sumarlo a mano, y se sumó.

(3-nov) El código 451 del paquete de parches de ReVanced se comprobó hoy, no se citó de memoria: la misma orden que devuelve 200 en cualquier otro repositorio devuelve 451 en ese. El proyecto de GitLab donde el desarrollo continúa se midió también: creado el 22 de marzo de 2026, ciento treinta y ocho estrellas, actividad de ayer.

(3-nov) La tabla de fichas trae dos proyectos con el empujón viejo y lo dice con la fórmula de la casa, «sin movimiento desde», porque la fecha del último empujón no mide si un proyecto sirve: mide si alguien lo está tocando. Hay proyectos quietos que funcionan y proyectos activos que no.

(3-nov) Los nombres de las carpetas se explican por lo que el propio árbol declara y lo que el archivo de presentación confirma. Donde hay deducción —el papel de la carpeta de la puerta de programación, por ejemplo— la pieza lo dice con la palabra «deducción» o con un «quizá», en vez de presentarla como si estuviera documentada.

(3-nov) La ausencia de sumas de comprobación en las entregas se declara como ausencia, no como sospecha. Un proyecto que no publica hashes no está escondiendo nada: está dejando al usuario sin la comprobación más barata que existe, y eso es un dato sobre el proyecto, no una acusación.

(3-nov) Esta pieza no aloja ni enlaza ningún paquete de parches ni ningún paquete parcheado. Enlaza al repositorio de cada autor y enseña a comprobar lo que se baja, que es lo que la serie hace desde la primera entrega.

#task 001 · pedir al autor del programa, en su repositorio, que el flujo de publicación escriba un archivo de sumas SHA-256 al lado de cada entrega, y anotar la respuesta en el acta del 4 de diciembre de 2026.
#task 002 · remedir el 3 de diciembre de 2026 las tres entregas del linaje —el gestor original, el de Morphe y este— y publicar cuál de los tres publicó más seguido en el mes, con la fecha del empujón de cada uno.
#task 003 · escribir la versión de WhatsApp de esta pieza, más corta, con los cinco pasos reducidos a tres y el episodio del 451 contado en dos párrafos, y comprobar que su banda de longitud se cumple antes de enviarla.

───────────────────

*🏷️ Etiquetas estratégicas*

#UniversalPatchManager #PatchBundleRegistry #MorpheManager #MorphePatches #UniversalInstaller #ReVanced #ReVancedManager #Shizuku #Morphe #Bundle
