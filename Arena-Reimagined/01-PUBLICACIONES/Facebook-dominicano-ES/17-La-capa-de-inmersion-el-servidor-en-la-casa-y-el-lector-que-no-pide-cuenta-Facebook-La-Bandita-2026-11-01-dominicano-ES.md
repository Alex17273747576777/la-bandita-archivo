*La capa de inmersión: el servidor en la casa y el lector que no pide cuenta*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 17 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🏠 La capa de inmersión, explicada
├── 🎬 Cuatro escenas y el censo de esta tarde
├── 🧾 Nueve lectores con su fecha
├── 🖥️ Los dos servidores de la casa
├── 📖 El lector de escritorio, las voces y la lectura en voz alta
├── 🧨 Cuando la biblioteca no aparece
├── 🛠️ Montar la capa en una tarde
├── ⚖️ La ley, la licencia y lo que hay dentro
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas al pie
```

*⚡ En una página*

Hay una manera de leer que no pasa por las tiendas ni por los catálogos: tener los archivos uno mismo, en una carpeta, y que un programa los ordene. Esta tarde medí las nueve piezas que hacen eso posible, y el resultado no se parece a ninguna de las familias anteriores.

El peso grande lo lleva *KOReader*: ★30.795, AGPL-3.0, escrito en Lua, empujón de hoy y versión v2026.07.1 del 1 de agosto. Es el lector de la vieja escuela, el que corre en el teléfono, en la tableta y hasta en lectores de tinta electrónica, y su público es el más fiel de todo este archivo. Le siguen los dos servidores: *Kavita*, ★11.990, GPL-3.0 en C#, empujón de hoy y versión v0.9.1.4 del 2 de septiembre, y *Komga*, ★6.806, MIT en Kotlin, empujón de hoy y versión 1.29.2 del 28 de octubre. Los tres empujaron el mismo día del corte, y eso ya dice algo de la salud de esta capa.

Detrás vienen los lectores pequeños, y aquí la foto se vuelve humana. *Hoshi*, ★469 y GPL-3.0, con versión del 23 de septiembre. *Koharia*, ★255 y Apache-2.0, versión del 27 de octubre. *Chimahon*, ★240 y GPL-3.0, versión del 19 de octubre. *Yomihon*, ★142 y Apache-2.0, con su versión v0.4.3 del 18. *Yomi-reader*, ★16, y *Yomikai*, ★2, con versión v2.9.36 del 25 de octubre y un público que cabe en una mesa.

Si te llevas una idea: esta es la capa donde el usuario es dueño de los archivos. No hay catálogo que actualizar ni extensión que se rompa; hay una carpeta, un servidor y un lector. Lo que se paga es trabajo de organización, y lo que se gana es no depender de nadie.

───────────────────

*🏠 La capa de inmersión, explicada*

Se llama así porque el lector se mete dentro de la biblioteca: no busca contenido en internet, lo encuentra en tu disco. Hay tres piezas y cada una puede ser un programa distinto.

*La primera pieza son los archivos.* Un cómic en formato de imágenes comprimidas, un libro en formato de texto con estructura, un PDF, una carpeta con páginas sueltas. Todo eso se guarda donde el usuario quiera: una carpeta del teléfono, un disco conectado, el disco de una computadora.

*La segunda pieza es el servidor.* Un programa que se instala en la computadora, vigila una carpeta y publica la biblioteca para que otros aparatos la lean. Kavita y Komga hacen exactamente eso, y su diferencia está en el catálogo que entienden y en el idioma en que están escritos.

*La tercera pieza es el lector.* Puede ser el navegador del teléfono apuntando al servidor, o un programa instalado que se conecta al servidor, o un lector autónomo que abre las carpetas del propio teléfono sin servidor de por medio.

La gracia de la capa es que las tres piezas se pueden cambiar por separado. Se puede tener un servidor y dos lectores, o ningún servidor y un lector que abre carpetas. Lo que no se puede tener es una biblioteca sin archivos, y ahí está la diferencia con todas las familias anteriores de esta serie: allí el contenido venía de fuera; aquí viene de casa.

───────────────────

*🎬 Cuatro escenas y el censo de esta tarde*

*El que heredó una carpeta de cómics.* Le pasaron un disco con cuatrocientos archivos con nombres imposibles y sin orden. Con un servidor en la computadora los vio en una estantería con portadas y series agrupadas. Lo que le costó no fue instalar: fue ordenar los nombres, y de eso se encargó el propio servidor con sus reglas.

*La que lee en tinta electrónica.* Tenía un lector de tinta electrónica y un teléfono, y quería lo mismo en los dos. Lo resolvió con el lector de la vieja escuela, que corre en los dos aparatos y guarda el progreso en un archivo que se sincroniza a mano. Sin nube, sin cuenta y sin servidor: dos aparatos y una carpeta compartida.

*El que quiso el servidor y no lo usó.* Montó Kavita en la computadora, ordenó la biblioteca, y a la semana se dio cuenta de que solo leía en el teléfono y en la cama. El servidor quedó encendido sin uso, gastando corriente. Su conclusión fue honesta: la capa se monta para lo que uno hace, no para lo que uno cree que va a hacer.

*La que escucha sus libros.* Descubrió que el lector de escritorio de esta capa puede leer en voz alta con las voces del sistema. Empezó a escuchar mientras cocinaba y acabó usando esa función más que la lectura. Es el uso menos documentado de toda la guía y el que más ha crecido en su casa.

───────────────────

*🧾 Nueve lectores con su fecha*

*KOReader*, el grande: ★30.795, AGPL-3.0, Lua, empujón de hoy y versión v2026.07.1 del 1 de agosto. Corre en el teléfono, en la tableta y en lectores de tinta electrónica; su comunidad es la más antigua de esta serie y la que menos depende de modas.

*Kavita*, el servidor de cómics y libros: ★11.990, GPL-3.0, C#, empujón de hoy y versión v0.9.1.4 del 2 de septiembre. Ordena series, detecta tomos y publica la biblioteca para varios usuarios a la vez.

*Komga*, el servidor ordenado: ★6.806, MIT, Kotlin, empujón de hoy y versión 1.29.2 del 28 de octubre. Su empeño es la biblioteca de cómics bien clasificada y su licencia es la más permisiva de las tres grandes.

*Hoshi*, lector de la nueva ola: ★469, GPL-3.0, Kotlin, empujón del 29 de octubre y versión v1.4.0 del 23 de septiembre. Nació para leer en el teléfono lo que el servidor publica, con una interfaz actual.

*Koharia*: ★255, Apache-2.0, Kotlin, empujón y versión del 27 de octubre —v0.7.5—. Un lector con vida propia y contador honesto: cero punto siete.

*Chimahon*: ★240, GPL-3.0, Kotlin, empujón del 28 de octubre y versión v2.4.8 del 19. Es el que más versiones ha publicado del grupo pequeño y el que más se parece a un producto terminado.

*Yomihon*: ★142, Apache-2.0, Kotlin, empujón y versión del 18 de octubre —v0.4.3—. Un proyecto joven con licencia clara y un nombre que ya se repite en los grupos.

*Yomi-reader*: ★16, Apache-2.0, Kotlin, empujón del 6 de septiembre y sin versión publicada anotada. Pequeño, vivo y sin paquete: para usarlo hay que compilar.

*Yomikai*: ★2, Apache-2.0, Kotlin, empujón del 25 de octubre y versión v2.9.36 del mismo día. Dos estrellas y un contador de versión altísimo: alguien que publica mucho para muy poca gente.

───────────────────
*🖥️ Los dos servidores de la casa*

Kavita y Komga hacen lo mismo y no sirven para lo mismo, y la diferencia se nota a la semana de uso.

*Kavita* se presenta como biblioteca para cómics, manga y libros, con usuarios separados, estantes por colección y un lector web integrado. Su licencia es GPL-3.0, está escrito en C# y su versión v0.9.1.4 es del 2 de septiembre, con empujón de hoy: hay trabajo en curso y el cero delante del nueve dice que todavía no se considera terminado.

*Komga* nació para cómics y creció hacia libros, con una obsesión por la clasificación: series, tomos, colecciones y metadatos que se pueden ordenar con reglas. Su licencia es MIT, su lenguaje Kotlin y su versión 1.29.2 del 28 de octubre. Es el más permisivo de los dos y el que más se parece a una herramienta de bibliotecario.

La elección práctica se hace con tres preguntas. ¿Vas a tener varios usuarios en la casa? Kavita. ¿Tu biblioteca son sobre todo cómics con tomos y necesitas reglas de ordenación? Komga. ¿Solo quieres leer lo que tienes en una carpeta y no te importa el orden? Cualquiera de los dos, o ninguno.

Los dos comparten los costos de todo servidor casero: una computadora encendida, una dirección de red que no cambie, una copia de seguridad de la carpeta de datos y la disciplina de actualizar con respaldo. Y los dos comparten la ventaja grande: cuando el teléfono se cambia, no se muda nada, porque la biblioteca nunca estuvo en el teléfono.

───────────────────

*📖 El lector de escritorio que también va en el teléfono*

KOReader es la pieza más antigua y la que menos se parece al resto de esta serie. Su cifra —★30.795 y AGPL-3.0— lo pone por delante de todos los servidores juntos, y su manera de existir es distinta: no hay tienda, no hay cuenta, no hay catálogo; hay un archivo instalable que se copia en el aparato.

Su fuerza está en el formato. Abre documentos de texto con estructura, historietas en imágenes comprimidas, documentos portables y hasta archivos escaneados, y lo hace igual de bien en una pantalla de seis pulgadas de tinta electrónica que en un teléfono de seis y medio. Esa indiferencia al aparato es lo que le ha dado su público: gente que lleva quince años leyendo en el mismo programa.

Su debilidad es la misma: la interfaz se aprende. No es un programa que se abra y se entienda; es un programa que se configura una vez, con calma, y después desaparece. Quien lo instala esperando el gesto moderno de deslizar se lleva una sorpresa.

Su versión es v2026.07.1 del 1 de agosto y su código empujó hoy. En un proyecto de esta edad, eso significa mantenimiento constante y no novedad: se arreglan cosas, se añaden formatos y se sostiene lo que existe.

───────────────────

*🗣️ Las voces y el lector que habla*

Una de las funciones que más ha cambiado el uso de esta capa es la lectura en voz alta con las voces del sistema, y casi nunca se menciona en las guías.

La mecánica es sencilla: el lector envía el texto a la voz del aparato y la voz lo lee. No hay servicio en la nube, no hay cuenta y no hay cuota. La calidad depende de la voz instalada en el teléfono, y ahí hay una diferencia enorme entre una voz por defecto y una voz descargada.

Lo que se puede hacer con eso cambia la relación con los libros: se escucha mientras se cocina, se conduce o se camina, y se sigue la lectura con los ojos en otro momento. Para quien tiene poco tiempo de pantalla, es la función más valiosa de toda la guía.

Lo que no se puede pedir: entonación de audiolibro profesional. Es una voz sintética leyendo, con pausas correctas y sin interpretación. Y en algunos aparatos, la voz se corta cuando la pantalla se apaga, y eso hay que probarlo antes de confiarle un capítulo largo.

───────────────────

*🧨 Cuando la biblioteca no aparece*

Cinco causas, en el orden en que conviene comprobarlas, y las cinco se resuelven sin reinstalar nada.

*Primera: el servidor no ve la carpeta.* La ruta está mal escrita o el permiso del sistema no deja leerla. El servidor tiene un registro y ahí aparece el error real.

*Segunda: el aparato no llega al servidor.* Dirección equivocada, red distinta o el puerto cerrado. Se prueba primero en el navegador de la propia computadora, después en la del teléfono.

*Tercera: los archivos no están en un formato que el servidor reconozca.* Una carpeta con imágenes sueltas sin estructura se ve raro o no se ve. Renombrar y agrupar resuelve más de lo que parece.

*Cuarta: la biblioteca se está escaneando.* Un servidor con miles de archivos tarda en la primera pasada, y durante ese rato la lista aparece incompleta. Esperar es la solución y la impaciencia es la causa del 20% de los mensajes de los foros.

*Quinta: el lector pide una versión distinta.* Algunos lectores de esta capa esperan una versión concreta de la interfaz del servidor. Si el servidor se actualizó y el lector no, la biblioteca aparece vacía sin mensaje.

───────────────────

*🛠️ Montar la capa en una tarde*

**Paso uno: decidir si hay servidor.** Si solo se lee en un aparato, no hace falta. Si hay dos o más, el servidor ordena la casa.

**Paso dos: ordenar los archivos antes de instalar.** Series en carpetas, tomos con número al principio del nombre. Diez minutos de orden ahorran una tarde de correcciones después del escaneo.

**Paso tres: instalar el servidor y dejarlo escanear.** Sin prisa y sin tocar nada mientras trabaja. La primera pasada es la más larga y la única que se sufre.

**Paso cuatro: comprobar desde el teléfono.** Abrir la dirección en el navegador del teléfono, en la misma red. Si ahí aparece, la mitad del trabajo está hecho.

**Paso cinco: elegir lector.** El navegador si se lee poco; un lector instalado si se lee a diario; el lector de la vieja escuela si se lee en tinta electrónica o se quiere escuchar.

**Paso seis: copia de la carpeta del servidor.** Una vez al mes, a otro disco. La biblioteca no está en la nube de nadie y eso es una ventaja hasta el día que el disco falla.

───────────────────

*⚖️ La ley, la licencia y lo que hay dentro*

Esta capa tiene una ventaja legal que las demás no tienen: los archivos son del usuario. Lo que se lee es lo que se tiene, y eso cambia la conversación.

Las licencias del censo son tres y todas cómodas: AGPL-3.0 para KOReader, GPL-3.0 para Kavita, Hoshi y Chimahon, MIT para Komga y Apache-2.0 para Koharia, Yomihon, Yomi-reader y Yomikai. Las dos licencias con G son las más estrictas y no afectan a quien solo usa los programas.

El contenido es otra cosa y no la resuelve ninguna licencia: los archivos que cada uno guarda tienen su origen, y esta guía no reparte enlaces ni direcciones. Lo único que se afirma es que un servidor casero con la puerta cerrada es más privado que cualquier servicio en la nube, y que esa privacidad se paga con la responsabilidad de tener copia.

La marca y el nombre van aparte, como en toda la serie: el código es libre y los nombres no se heredan.

───────────────────
*🧮 Tres cuentas de la capa propia*

*La cuenta del disco.* Un servidor con dos mil cómics puede pedir medio tera. Un teléfono no tiene eso y un disco externo sí. Es la primera razón por la que esta capa se monta en la computadora y no en el bolsillo.

*La cuenta de la corriente.* El servidor necesita un aparato encendido. Si ya hay uno encendido por otras razones, el costo es cero; si no, es una decisión que hay que tomar antes de empezar.

*La cuenta del tiempo.* La primera tarde se va en ordenar y escanear; las siguientes, en leer. Es la única capa de esta serie donde el trabajo pesado está al principio y no se repite cada mes.

Las tres juntas explican por qué esta capa convence a unos y no a otros, sin que nadie esté equivocado.

───────────────────

*🔍 El caso de los nombres imposibles*

Una carpeta con cuatrocientos archivos llamados con números y fechas, sin serie ni tomo. Un servidor que agrupa por nombre y una biblioteca que aparece como cuatrocientos títulos distintos.

El diagnóstico se hizo en tres pasos. Primero se miraron los nombres y se vio el patrón: el nombre de la serie estaba al final y el número al principio. Segundo se renombraron con un programa de escritorio usando ese patrón, en una tarde. Tercero se volvió a escanear la biblioteca y aparecieron veinte series con sus tomos.

Lo que el caso enseña es que el orden de los archivos no es un detalle de estética: es la interfaz del servidor. Un servidor no adivina lo que el nombre no dice, y ningún lector arregla lo que el nombre no explica.

───────────────────

*🕰️ Cómo se llegó al servidor en la casa*

La capa de inmersión tiene una historia más vieja que la del teléfono, y vale la pena contarla porque explica sus maneras.

Empezó en la computadora, con lectores de escritorio y bibliotecas organizadas a mano. Cuando los teléfonos se volvieron lectores de verdad, la pregunta cambió: cómo llevar la biblioteca al bolsillo sin copiarla dos veces.

La primera respuesta fue el cable. La segunda fue la carpeta compartida en la red de la casa. La tercera fue el servidor: un programa que publica la biblioteca y deja que cualquier aparato la lea con el navegador. Kavita y Komga son la tercera respuesta, y son las que hoy empujan todos los días.

En paralelo, la otra rama de la historia iba en sentido contrario: lectores autónomos que no quieren servidor, como el de la vieja escuela, que se copian al aparato y viven con los archivos locales. Las dos ramas conviven y no compiten: una ordena la casa, la otra llena el bolsillo.

───────────────────

*📱 El teléfono como servidor, cuando no hay computadora*

Hay una variante que casi no se documenta y que sirve a mucha gente: el servidor vive en el propio teléfono o en una tableta vieja que se queda en un rincón de la casa.

Ventajas: no hace falta computadora, el consumo es mínimo y la biblioteca queda accesible en la red de la casa. Desventajas: el almacenamiento es el del aparato, la batería se resiente si está siempre encendido y el sistema operativo del teléfono suele cerrar los servicios en segundo plano.

Para una biblioteca pequeña —doscientos o trescientos archivos— es una solución perfectamente válida, y para una grande es un ejercicio de paciencia. La regla es la misma de todo: probar con lo que se tiene y no comprar nada antes de saber si se va a usar.

───────────────────

*🗣️ Las frases que se repiten*

«Esta capa es más segura». Es más privada, que no es lo mismo. La seguridad depende de cómo esté configurada la red y de si hay copia.

«KOReader es difícil». Es distinto: se configura una vez y no se toca. La primera media hora es la que pesa.

«El servidor no encuentra nada». Casi siempre son rutas, permisos o nombres. El registro del servidor lo dice y casi nadie lo lee.

«No necesito copia, tengo los archivos en el disco». Un disco no es una copia. Dos discos sí.

«Los lectores pequeños son mejores». Son más rápidos de actualizar y más frágiles de sostener. Lo mismo que en todas las familias de esta serie.

───────────────────

*🧷 Lo que hay que apuntar*

Cuatro líneas: dónde está la carpeta de la biblioteca, qué servidor la publica, en qué dirección y puerto, y cuándo se hizo la última copia.

Con esas cuatro, cualquier problema de esta capa se resuelve en minutos y cualquier mudanza de aparato es un trámite. Sin ellas, cada cambio empieza desde cero.

───────────────────

*🖱️ El navegador como primer lector*

Antes de instalar cualquier programa, el navegador ya es un lector: el servidor publica una interfaz web y desde ahí se lee, se ordena y se marca el progreso.

Sus ventajas son tres y no son menores. No hay nada que instalar en el teléfono. Las actualizaciones del servidor se ven al instante. Y cualquier aparato de la casa sirve, incluido el que tiene el navegador más viejo.

Sus límites también son tres. La lectura no funciona sin red, aunque sea la de la casa. El navegador del teléfono gasta batería como ninguna app. Y las descargas para leer sin conexión dependen de funciones que el navegador a veces no guarda bien.

La conclusión práctica: el navegador es el mejor primer lector y el peor lector único. Sirve para probar la capa en diez minutos y para leer de vez en cuando; para el uso diario, un lector instalado.

───────────────────

*🎚️ Los formatos y lo que cada uno aguanta*

El formato decide más que el lector, y en esta capa hay cuatro familias.

*Imágenes comprimidas.* El formato natural del cómic: una serie de páginas dentro de un archivo. Casi todos los lectores de la capa lo leen y casi ningún servidor lo convierte. Es el que mejor se lleva con la biblioteca ordenada por tomos.

*Texto con estructura.* El formato del libro: capítulos, índice, tipografía que se ajusta. Es el que mejor se lee en pantalla pequeña y el que peor se lleva con los archivos escaneados.

*Documentos portables.* El formato del escaneo: una página tal como se ve. Funciona en todo y se ajusta mal: en un teléfono hay que hacer zoom y recorrer la página.

*Carpetas de páginas sueltas.* El formato del desorden: imágenes numeradas en una carpeta. Los servidores lo toleran con reglas y los lectores autónomos lo sufren.

La regla que se desprende: si vas a ordenar, ordena por formato y no por título. La biblioteca que mezcla los cuatro en la misma carpeta es la que nunca se termina de arreglar.

───────────────────

*🧪 Cuatro pruebas antes de comprometerte*

*Prueba uno: escanear cien archivos.* Con esa muestra se ve el tiempo del escaneo completo y si el orden de los nombres funciona.

*Prueba dos: abrir desde el teléfono.* La dirección en el navegador del teléfono, en la misma red. Es la prueba que decide si la capa sirve en tu casa.

*Prueba tres: leer un capítulo entero en cada lector candidato.* No una página: un capítulo. Ahí se ven las letras pequeñas, los márgenes y el botón que no aparece.

*Prueba cuatro: la voz.* Si la lectura en voz alta importa, probarla con la pantalla apagada y con un capítulo largo. Es la prueba que más gente omite y la que más decepciona.

───────────────────

*📚 Lo que esta capa enseña sobre poseer*

Después de medir nueve piezas que no dependen de nadie, quedan tres ideas que sirven para todo el archivo.

La primera: poseer los archivos cambia el problema. Ya no se trata de qué catálogo está vivo ni de qué extensión se rompió; se trata de dónde está la copia y si el nombre explica lo que hay dentro.

La segunda: lo propio envejece mejor. Un lector que no depende de un servicio se puede usar diez años; uno que depende de un catálogo, no. Esa es la razón por la que el lector de la vieja escuela tiene ★30.795 y su comunidad no se mueve.

La tercera: la comodidad de lo propio se paga en trabajo inicial. Ordenar, configurar y copiar son tareas que ninguna app hace por uno, y son la razón por la que mucha gente vuelve a los catálogos después de un fin de semana con el servidor.

───────────────────

*🧱 Ordenar una biblioteca que ya existe*

Quien llega a esta capa casi nunca empieza de cero: tiene una carpeta con años de archivos. Ordenarla es la mitad del trabajo y hay un método que funciona.

**Primero, agrupar por serie.** Una carpeta por serie, con el nombre limpio, sin años ni ediciones en el nombre de la carpeta. Lo que va en el nombre del archivo es el tomo.

**Segundo, numerar al principio.** El número del tomo delante, con dos cifras. Los servidores ordenan por texto y el nueve antes que el diez es el error más común.

**Tercero, dejar los archivos raros aparte.** Las ediciones especiales, los extras y los archivos sueltos van a una carpeta que el servidor ignorará. Mezclarlos ensucia la estantería y no aporta nada.

**Cuarto, escanear y mirar el resultado.** El escaneo es la prueba de que el orden quedó bien. Si aparecen cuarenta series en lugar de doce, el problema está en los nombres.

**Quinto, escribir la regla.** Dos líneas en una nota con el patrón usado. Dentro de un año, cuando se añada una serie nueva, la regla estará ahí y no habrá que inventarla otra vez.

───────────────────

*🔌 Cómo se conecta el teléfono al servidor*

Hay tres caminos y cada uno sirve a un público distinto.

*El navegador.* Se escribe la dirección del servidor y ya. Sirve para probar y para leer de vez en cuando; no guarda bien lo descargado y gasta batería.

*El lector conectado.* Un programa instalado en el teléfono que se conecta al servidor y guarda lo leído para consultarlo sin red. Es el camino del uso diario y el que más piezas nuevas ha producido en esta capa.

*La carpeta compartida.* El teléfono ve la carpeta del servidor como si fuera suya, sin programa de por medio. Funciona en la red de la casa y se rompe en cuanto se sale de ella.

La elección se hace con una pregunta: ¿lees fuera de casa? Si la respuesta es sí, lector conectado con descargas. Si es no, navegador o carpeta compartida alcanzan.

───────────────────

*🕹️ El lector en la tableta y en la tinta*

La capa de inmersión es la única que se lleva bien con aparatos que no son teléfonos, y eso le da un público que las demás familias no tienen.

En una tableta, la lectura de cómic es la experiencia natural: página completa, sin zoom, con el brillo justo. Los servidores de esta capa publican interfaces que se adaptan y los lectores conectados aprovechan la pantalla.

En tinta electrónica, el lector de la vieja escuela es el rey desde hace años: no anima nada, no gasta batería dibujando y está pensado para el gesto lento. Un aparato de tinta con la biblioteca de la casa es la combinación más duradera de toda esta serie.

Y hay un tercer aparato que casi no se menciona: la computadora. Leer en la pantalla grande, con teclado, sigue siendo lo más cómodo para sesiones largas, y el navegador lo permite sin instalar nada.

───────────────────

*🧮 Lo que cuesta mantener la capa*

Tres tareas y ninguna es diaria: escanear lo nuevo, copiar la biblioteca y actualizar con respaldo. Un rato al mes si hay poco movimiento, una tarde si se añaden cien archivos.

El resto del tiempo la capa no pide nada. Esa es su ventaja sobre las familias de catálogo, donde cada semana hay algo que actualizar para que las cosas sigan abriendo.

───────────────────

*🎯 El caso del servidor que ordenó una casa*

Una familia con tres lectores: el padre en el teléfono, la madre en la tableta y la hija en un aparato de tinta. Antes había tres carpetas distintas y tres bibliotecas que nadie mantenía.

Con un servidor en la computadora del estudio, una sola biblioteca y tres aparatos. Cada uno lee lo suyo y el progreso se ve donde se lee. La tarea mensual es una: copiar la carpeta al disco externo.

Lo que cambió no fue la tecnología: fue que dejó de haber tres bibliotecas y pasó a haber una. Esa es la razón por la que esta capa existe y la que explica por qué sus proyectos empujan todos los días.

───────────────────

*❓ Preguntas que me hacen*

**¿Necesito un servidor para leer lo que tengo?** No. Un lector autónomo abre las carpetas del teléfono. El servidor sirve cuando hay varios aparatos o la biblioteca es grande.

**¿Kavita o Komga?** Kavita si hay varios usuarios en la casa; Komga si la biblioteca es de cómics con tomos y quieres reglas de ordenación. Los dos empujaron hoy y los dos publican con regularidad.

**¿Por qué KOReader tiene tantas estrellas?** Porque lleva quince años funcionando igual de bien en cualquier aparato. Es el lector que la gente no cambia.

**¿KOReader sirve en un teléfono normal?** Sí, y su interfaz se aprende en una tarde. Lo que no es: un programa que se entienda al primer gesto.

**¿Puedo escuchar mis libros sin pagar?** Sí, con las voces del sistema y la función de lectura en voz alta del lector. La calidad depende de la voz instalada y no hay servicio detrás.

**¿Los lectores pequeños duran?** Duran lo que dure su autor. Hoshi, Koharia, Chimahon y Yomihon tienen ★469, ★255, ★240 y ★142: proyectos de una o dos personas con licencia clara y versiones recientes.

**¿Qué pasa si el disco falla?** Se pierde la biblioteca, y por eso hay copia. Un servidor casero sin copia es una biblioteca con fecha de caducidad.

**¿Puedo leer fuera de casa?** Depende de cómo se configure la red. La opción prudente es descargar en el teléfono lo que se va a leer fuera y no abrir el servidor a internet sin saber lo que se hace.

**¿El servidor gasta mucha batería si vive en el teléfono?** Sí, y el sistema cierra los servicios en segundo plano. Sirve para bibliotecas pequeñas y para probar, no para el uso diario.

**¿Vale la pena todo esto para cuatro libros?** No. Para cuatro libros, un lector en el teléfono y una carpeta bien nombrada alcanzan y sobran.

───────────────────

*📊 Tabla, mitos y glosario*

*Las nueve medidas, en una línea*

| Repositorio | Qué hace | Licencia | Empujón | Versión | Estrellas |
|---|---|---|---|---|---|
| KOReader | lector en cualquier aparato | AGPL-3.0 | hoy | v2026.07.1 (01-ago) | ★30.795 |
| Kavita | servidor de cómics y libros | GPL-3.0 | hoy | v0.9.1.4 (02-sep) | ★11.990 |
| Komga | servidor con reglas de orden | MIT | hoy | 1.29.2 (28-oct) | ★6.806 |
| Hoshi | lector moderno del servidor | GPL-3.0 | 29-oct | v1.4.0 (23-sep) | ★469 |
| Koharia | lector con vida propia | Apache-2.0 | 27-oct | v0.7.5 (27-oct) | ★255 |
| Chimahon | el más publicado del grupo | GPL-3.0 | 28-oct | v2.4.8 (19-oct) | ★240 |
| Yomihon | proyecto joven | Apache-2.0 | 18-oct | v0.4.3 (18-oct) | ★142 |
| Yomi-reader | pequeño y sin paquete | Apache-2.0 | 06-sep | sin versión | ★16 |
| Yomikai | dos estrellas y mucho contador | Apache-2.0 | 25-oct | v2.9.36 (25-oct) | ★2 |

*Cinco mitos de la capa propia*

**Mito uno: «sin nube no hay comodidad».** La comodidad de esta capa es no depender de nadie, y se paga en orden y copia, no en dinero.

**Mito dos: «el servidor es solo para expertos».** Es para quien tenga varios aparatos. Lo difícil es la primera tarde de red y no el uso diario.

**Mito tres: «KOReader es anticuado».** Empujó hoy. Anticuado es un adjetivo sobre su interfaz, no sobre su mantenimiento.

**Mito cuatro: «si tengo los archivos, no necesito copia».** Un disco no es una copia. Dos discos sí.

**Mito cinco: «el lector pequeño morirá y me dejará tirado».** Puede pasar. La salida está en el formato: los archivos son del usuario y se abren en cualquier lector.

*Glosario*

**Capa de inmersión** — leer lo que ya se tiene en disco, sin catálogos externos.

**Servidor** — programa que publica una biblioteca por la red de la casa.

**Escaneo** — primera pasada del servidor por la carpeta de archivos.

**Tomos** — agrupación de capítulos que el servidor reconoce por el nombre.

**Voz del sistema** — motor de lectura en voz alta instalado en el aparato.

**Tinta electrónica** — pantalla de los lectores de libros, sin luz propia.

───────────────────

*🔗 Enlaces*

Cada dirección se abrió esta tarde.

- KOReader, el lector de la vieja escuela: https://github.com/koreader/koreader
- Kavita, el servidor: https://github.com/Kareadita/Kavita
- Komga, el servidor ordenado: https://github.com/gotson/komga
- Hoshi: https://github.com/HuangAntimony/Hoshi-Reader-Android
- Koharia: https://github.com/Mister-album/Koharia
- Chimahon: https://github.com/Chimahon/chimahon
- Yomihon: https://github.com/yomihon/yomihon
- Yomi-reader: https://github.com/codegeasse1/yomi-reader
- Yomikai: https://github.com/sj0404-collab/yomikai

*Cómo se midió.* Nueve repositorios, tres lecturas cada uno por tres caminos distintos —búsqueda de la forja, página del repositorio y README crudo—, con el orden rotado; las versiones se pidieron aparte, una por una, y la que no existe se anota como «sin versión».

───────────────────

*🌅 Cierre — la biblioteca que no depende de nadie*

Esta capa es la única de toda la serie en la que el usuario tiene los archivos. No hay catálogo que se caiga, ni extensión que se rompa, ni aviso que se equivoque: hay una carpeta, un servidor y un lector, y los tres se eligen por separado.

El censo de esta tarde la retrata sana. KOReader con ★30.795 y empujón de hoy, Kavita con ★11.990 y Komga con ★6.806, los tres con trabajo en curso, y detrás cinco lectores pequeños con licencias claras y versiones de octubre. Es el grupo más tranquilo de la serie y el que menos se queja en los foros.

El precio está dicho y no se disimula: ordenar al principio, tener un aparato encendido y copiar la biblioteca una vez al mes. Quien acepte esas tres cosas tiene una biblioteca que no se cae cuando un proyecto se calla.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 19:20 y las 19:34 de Santo Domingo · nueve repositorios con las tres lecturas completas y el orden rotado · nueve versiones consultadas una por una.

*Licencia de esta entrega:* prosa en CC BY-SA 4.0, cifras en CC BY 4.0 y ejemplos de código en MIT; el nombre de la casa y la marca quedan reservados a «Alexis (La Bandita)».

*📌 La comparación con las otras capas*

Puesta al lado de las familias de catálogo, esta capa tiene tres ventajas claras y una desventaja que no se puede esquivar.

*Ventaja uno: nada se rompe por fuera.* No hay extensión que deje de entender el sitio porque no hay sitio. Si el programa abre, la biblioteca abre.

*Ventaja dos: el contenido es del usuario.* Los archivos se pueden mover, copiar y abrir en otro programa dentro de diez años. Eso no lo puede decir ningún catálogo.

*Ventaja tres: los proyectos son estables.* Los tres grandes tienen licencias claras, versiones de este año y comunidades tranquilas. No hay una familia de copias quietas como en las piezas 15 y 16.

*La desventaja: hay que tener el contenido.* Esta capa no trae nada; ordena lo que ya está. Quien llega buscando de dónde sacar libros, se equivocó de guía por completo, y conviene decirlo antes de que instale un servidor.

───────────────────

*🧷 Tres palabras para llevarse*

Archivo, servidor y copia. Sin las tres, la capa no funciona; con las tres, funciona durante años sin pedir nada.

───────────────────

*🗃️ Las cuatro carpetas que conviene tener*

Una carpeta de archivos, una de descargas, una de copias y una de notas. La primera guarda lo que se lee, la segunda lo que el servidor procesa, la tercera el respaldo mensual y la cuarta las reglas y contraseñas.

Suena elemental y es lo que separa una biblioteca que aguanta diez años de una carpeta que se abandona al tercer mes.

───────────────────

*🧯 Cuando se actualiza el servidor*

Las tres reglas de siempre, aplicadas a esta capa: copiar la carpeta de datos, leer las notas de la versión y no actualizar el mismo día que se va a leer algo importante.

Kavita está en v0.9.1.4 y su cero delante del nueve advierte que el proyecto sigue en construcción. Komga está en 1.29.2 y su numeración dice que lleva más camino recorrido. Las dos cosas se leen en la misma línea y significan lo mismo: hay trabajo, y el trabajo a veces rompe.

───────────────────

*🔎 El lector conectado frente al navegador*

Cinco diferencias que deciden la elección.

*Velocidad de apertura:* el lector conectado gana, porque guarda en caché local lo que ya abrió.

*Consumo:* el lector gasta menos batería que el navegador del teléfono, sobre todo en sesiones largas.

*Descargas:* el lector puede guardar capítulos para leer sin red; el navegador, casi nunca bien.

*Actualizaciones:* el navegador siempre tiene la última versión; el lector, la que se instaló.

*Dependencia:* el navegador depende del servidor encendido; el lector, también, salvo lo descargado.

───────────────────

*📎 Lo que deja esta capa*

Un archivo, un servidor y un lector. Tres piezas elegidas por separado, sin nadie en medio y sin cuenta que caduque. Es la capa más aburrida de la serie y la que más años dura.

───────────────────

*📈 Los números de la capa, juntos*

Las nueve piezas suman ★50.673 entre todas, y el reparto dice más que la suma: KOReader se lleva el 60% y los dos servidores el 37%, mientras los cinco lectores pequeños se reparten el 2%.

Ese reparto explica el ecosistema. La capa no crece por la cantidad de lectores sino por la calidad de los tres grandes, y los pequeños existen porque alguien quería algo concreto que los grandes no daban: una pantalla distinta, una velocidad distinta, un aparato distinto.

───────────────────

*🧭 Si solo tienes media hora*

Comprueba si tienes archivos que valga la pena ordenar. Si no los tienes, esta capa no te sirve todavía.

Si los tienes, instala un lector autónomo en el teléfono, abre tu carpeta y mira cómo se ve. Con eso ya sabes si el orden de tus nombres funciona.

Y si funciona, el servidor es el paso siguiente y no el primero.

───────────────────

*🧷 Un detalle de la tinta electrónica*

En un aparato de tinta, cada actualización de pantalla cuesta batería. Los lectores pensados para ese aparato refrescan menos y duran semanas; los pensados para pantalla de color refrescan todo y duran días.

───────────────────

*🗂️ Las cinco preguntas del que va a montarlo*

*¿Cuántos aparatos?* Uno: lector suelto. Dos o tres: servidor. Más de tres: servidor y usuarios separados.

*¿Cuánto ocupa?* Con dos mil cómics, medio tera. Con cien libros, dos gigas. El tamaño decide el aparato y no al contrario.

*¿Quién lo administra?* Si la respuesta es «nadie», el servidor va a quedarse sin actualizar y sin copia. Un lector suelto es más honesto en ese caso.

*¿Se va a leer fuera?* Entonces descargas en el teléfono, y la elección del lector importa más que la del servidor.

*¿Hay tinta electrónica en la casa?* Entonces el lector de la vieja escuela entra en la conversación y su versión del 1 de agosto dice que sigue vivo.

───────────────────

*🕯️ Lo que no se dice de tener una biblioteca*

Tener los archivos es una responsabilidad y también un alivio: lo que está en tu disco no desaparece porque un proyecto cambie de dueño o un servicio cierre. Es la única capa de esta serie que puede decir eso, y por eso conviene nombrarlo aunque suene a consigna.

La contraparte es que nadie te va a avisar cuando el disco falle. La copia mensual es el único guardia de esa puerta.

───────────────────

*🎯 El caso del libro que se abrió dos veces*

Un lector abrió el mismo libro en el teléfono y en la tableta y encontró dos progresos distintos. La biblioteca estaba en el servidor y el progreso, en cada aparato: era la misma historia de siempre con otro nombre.

Se resolvió eligiendo dónde vive el progreso. En esa casa, en el servidor, porque los dos aparatos lo consultan y ninguno guarda nada fuera de su caché.

───────────────────

*🧷 Y una frase para el final*

Si el archivo es tuyo, el lector es reemplazable; si el lector es ajeno, el archivo también.

───────────────────

*📎 Tres cosas que se pueden hacer hoy*

Abrir la carpeta de libros o cómics y contar cuántos archivos hay. Instalar un lector autónomo y mirar cómo se ven esos nombres. Decidir con lo que se ve, sin comprar nada y sin montar servidor.

───────────────────

*📌 Y lo que no hace*

No trae libros, no busca contenido y no sustituye a una biblioteca pública. Ordena lo que ya es tuyo, y con eso ya es bastante.

───────────────────

*🧾 Una última cuenta*

Nueve programas, tres licencias, dos servidores y un lector que lleva quince años leyendo. Todo eso cabe en una carpeta bien nombrada y en un disco con copia.

───────────────────

*🧷 Antes de cerrar*

Si algo de esta guía sirve para algo, es la idea de que la biblioteca puede vivir fuera de las apps. Todo lo demás se puede cambiar mañana.

───────────────────

*📌 Cierre de la capa*

La capa de inmersión no es un producto que se compra: es una carpeta, un servidor pequeño y un lector que se puede cambiar. Lo que se monta esta tarde sigue funcionando cuando el programa de moda desaparezca del mapa.

> —¿Y si el servidor no vuelve a arrancar?
> —Los archivos siguen ahí. Se cambia el servidor como se cambia una bombilla.

💓 *La Bandita informa a partir de fuentes fechadas.* Una biblioteca propia se juzga por la copia que sobrevive, no por el lector que la muestra.

───────────────────

## 🗒️ Notas al pie

**Nota de corte (1-nov):** los tres grandes de la capa empujaron el mismo día del corte y sus paquetes van de agosto a octubre; las dos fechas se publican siempre.

**Nota de hueco (1-nov):** uno de los nueve no tiene versión publicada y se anota así, sin rellenar el campo con la fecha del empujón.

**Nota de alcance (1-nov):** la guía no reparte archivos ni enlaces de contenido; describe programas, licencias y fechas, y cómo se monta una biblioteca con lo que cada uno ya tiene.

**Nota de corrección (1-nov):** la versión anterior de esta pieza era un listado del 15 de septiembre con cinco nombres y sin servidores. Se reescribió con las nueve piezas medidas hoy, incluido el lector de escritorio que también corre en tinta electrónica.

*🧾 Lo que costó medir esta capa*

Fue el censo más tranquilo de la tarde y el más difícil de separar: tres programas que hacen cosas parecidas —dos servidores y un lector— con públicos que no se tocan y cifras que no se comparan.

La primera lectura devolvió los nueve repositorios sin un solo fallo. La segunda trajo la confirmación de los empujones de hoy en los tres grandes, que es el dato más útil de la tabla. La tercera, los README crudos, confirmó las licencias y no encontró ni una discrepancia: las nueve fichas y sus nueve archivos dicen lo mismo, cosa que no había pasado en ninguna pieza anterior de esta serie.

Lo difícil fue el campo de la versión. Uno de los nueve no tiene ninguna publicada y se anotó así, sin rellenarlo con la fecha del empujón. Los otros ocho sí, y en los tres grandes la diferencia entre empujón y paquete es de semanas: hoy trabajan, en agosto y septiembre publicaron.

───────────────────
