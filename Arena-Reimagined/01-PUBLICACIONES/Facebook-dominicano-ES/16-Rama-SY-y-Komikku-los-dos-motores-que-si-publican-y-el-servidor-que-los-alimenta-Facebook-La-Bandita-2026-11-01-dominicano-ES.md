*Rama SY y Komikku: los dos motores que sí publican (y el servidor que los alimenta)*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 16 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🏛️ Dos escuelas, un mismo esqueleto
├── 🎬 Cuatro escenas y el censo de esta tarde
├── 🧾 Las nueve piezas, con su fecha al lado
├── 🖥️ El servidor: leer desde la computadora
├── 🔌 El catálogo que los alimenta a todos
├── 🧨 Cuando abre y no ve nada, y qué se guarda dónde
├── 🛠️ Elegir motor en cinco preguntas
├── ⚖️ La ley, la licencia y el nombre
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas al pie
```

*⚡ En una página*

Hay dos motores de manga que, a diferencia de la familia de la pieza anterior, publican paquete con regularidad y empujan código cada semana. Uno es *TachiyomiSY*: ★4.200, Apache-2.0, Kotlin, empujón de hoy y versión 1.13.2 del 13 de julio. El otro es *Komikku*: ★4.966, Apache-2.0, empujón de hoy y versión v1.14.1 del 17 de julio. Alrededor de ellos hay tres piezas menores —*MihonSY* con ★48, *ShinKu* con ★45 y versión de hoy, y *Mikku* con ★0 y empujón de ayer—, un servidor de escritorio que lleva la lectura a la computadora —*Suwayomi-Server*, ★7.989 y MPL-2.0— y el catálogo de extensiones más grande de todos, ★15.408, que hoy no declara licencia.

Y al lado, la vara de siempre: *Mihon*, ★24.939, Apache-2.0, empujón del 26 de octubre y versión v0.21.3 del 25. No es un fork de nadie: es el motor del que salieron casi todos los demás, y por eso conviene tenerlo en la misma tabla.

Lo interesante de esta tarde no son las cifras, es la diferencia de conducta con la familia de la pieza anterior. Allá, nueve herederos con un tronco callado. Aquí, dos motores que publican, cuatro proyectos pequeños que orbitan y un servidor que permite leer lo mismo desde el teléfono y la computadora sin llevar la biblioteca a cuestas.

Si te llevas una idea: cuando el motor publica, la discusión deja de ser sobre fechas y pasa a ser sobre funciones. Esa es la diferencia entre un ecosistema que aguanta y uno que sobrevive a copias.

───────────────────

*🏛️ Dos escuelas, un mismo esqueleto*

Los dos motores grandes de esta tarde comparten base y no comparten escuela. Entender la diferencia ahorra la mitad de las preguntas.

*SY es la escuela de la biblioteca.* Su empeño está en lo que pasa alrededor de la lectura: categorías anidadas, filtros, ordenaciones, estadísticas, historial. Quien tiene trescientos títulos y quiere encontrarlos por tres criterios a la vez, está en su casa. Su versión 1.13.2 lleva desde el 13 de julio publicada y su código empujó hoy, así que hay trabajo en curso.

*Komikku es la escuela del lector.* Su empeño está en lo que pasa dentro de la pantalla: cómo se pagina, cómo se ajusta la imagen, cómo se maneja una serie larga. Komikku tiene ★4.966 y su código también empujó hoy; su versión v1.14.1 es del 17 de julio. Nació como un proyecto que quería ser más que un fork y hoy tiene hasta un cliente de anime propio, Anikku, con ★1.127.

Las dos escuelas comparten el esqueleto heredado: la misma manera de conectar extensiones, la misma carpeta de descargas por nombre de paquete y el mismo formato de respaldo mientras nadie lo cambie. Esa compatibilidad es lo que permite que un usuario pruebe los dos sin perder la biblioteca, y es también la razón por la que los dos se rompen a la vez cuando el catálogo cambia de forma.

Alrededor de las dos escuelas está la tercera vía: *Mihon*, ★24.939, la base de la que salieron ambas. Su versión v0.21.3 del 25 de octubre y su empujón del 26 lo ponen al día, y su público es el más grande de todos porque es la puerta de entrada que aparece en todos los tutoriales.

───────────────────

*🎬 Cuatro escenas y el censo de esta tarde*

*La que ordenó trescientas series.* Tenía la biblioteca como un montón y no encontraba nada. Con SY descubrió las categorías anidadas y los filtros combinados, y se pasó una tarde ordenando lo que llevaba tres años acumulando. Al final no cambió de lector: cambió de costumbre. Y esa tarde le ahorró las siguientes cien búsquedas.

*El que leía en dos aparatos.* Leía en el teléfono por la calle y en la computadora por la noche. Antes copiaba respaldos; ahora tiene un servidor en la computadora y los dos aparatos apuntan ahí. La biblioteca vive en un solo sitio y los aparatos son ventanas. Su conclusión: si tienes computadora encendida a diario, esta es la forma más ordenada de leer.

*El de la versión de julio.* Instaló Komikku, vio que la versión era del 17 de julio y anunció que el proyecto estaba abandonado. Le señalaron el empujón de hoy y la cantidad de cambios en curso. La confusión es la misma de la pieza anterior y tiene la misma respuesta: dos fechas, no una.

*El que se quedó con Mihon.* Probó los dos motores nuevos, le gustaron y volvió al de siempre. Su razón fue la más honesta de las cuatro: las extensiones que usa las entiende su lector actual, y cambiarlo le costaba una tarde sin darle nada que le faltara. La novedad no es una necesidad.

───────────────────

*🧾 Las nueve piezas, con su fecha al lado*

*Mihon*, la base: ★24.939, Apache-2.0, Kotlin, empujón del 26 de octubre y versión v0.21.3 del 25. Es el motor más instalado del ecosistema y la referencia contra la que se mide todo lo demás.

*Suwayomi-Server*, el servidor: ★7.989, MPL-2.0, Java, empujón de hoy y versión v2.4.2366 del 30 de septiembre. Lleva la biblioteca a la computadora y sirve a los aparatos; se apoya en la misma familia de extensiones y por eso entra en este censo.

*Komikku*, la escuela del lector: ★4.966, Apache-2.0, empujón de hoy, versión v1.14.1 del 17 de julio. Su casa tiene además un cliente de anime, Anikku, con ★1.127 y v0.2.0 del 11 de septiembre.

*TachiyomiSY*, la escuela de la biblioteca: ★4.200, Apache-2.0, empujón de hoy, versión 1.13.2 del 13 de julio. Su familia tiene un hijo pequeño, MihonSY.

*MihonSY*: ★48, Apache-2.0, empujón del 28 de octubre y versión v1.2.1 del 7. Un fork que nació sobre SY para aparatos y gustos concretos, con un contador de versión que dice que está en la primera etapa.

*ShinKu*: ★45, Apache-2.0, empujón y versión del 1 de noviembre —v2.8.0—. El más rápido de los pequeños: publicó el mismo día que empujó.

*Mikku*: ★0, Apache-2.0, empujón del 31 de octubre y sin versión publicada. Un proyecto de un día antes del corte, con licencia clara y ningún público todavía.

*Keiyoushi/extensions*, el catálogo: ★15.408, sin licencia declarada, HTML, empujón de hoy. No es un lector: es el índice del que comen casi todos los motores de esta tabla. Su licencia ausente se publica como ausente.

*Syncyomi*: ★741, GPL-2.0, escrito en Go, empujón y versión del 29 de octubre —v1.7.4—. Sincroniza lo que el servidor guarda, para que dos aparatos vean el mismo progreso sin exportar nada a mano.

───────────────────
*🖥️ El servidor: leer desde la computadora*

Suwayomi-Server es la pieza que cambia la forma de usar todo esto. Su cifra —★7.989, MPL-2.0, Java, empujón de hoy y versión v2.4.2366 del 30 de septiembre— no es la más alta de la tabla y su papel es el más grande.

La idea es sencilla: en vez de tener la biblioteca repartida en dos teléfonos y una tableta, se instala un programa en la computadora que guarda la biblioteca, baja los capítulos y sirve la lectura a cualquier aparato de la casa por el navegador o por la red local. Los teléfonos dejan de ser archivos y pasan a ser ventanas.

La ventaja práctica es triple. La primera: la biblioteca vive en un solo sitio y el progreso se ve desde cualquier aparato, sin exportar nada a mano. La segunda: las descargas las hace la computadora, que tiene disco y corriente, en vez de gastar el almacenamiento del teléfono. La tercera: cuando el teléfono se cambia, no se muda nada.

El costo también es triple. Hace falta una computadora encendida —o un aparato pequeño que haga de servidor— para leer lo que esté ahí. Hace falta configurar la red de la casa, que en algunos routers es la parte difícil. Y hace falta aceptar que el servidor tiene su propio ciclo: si se actualiza y rompe algo, los aparatos se quedan mirando una pantalla vacía hasta que se arregle.

Su licencia, MPL-2.0, es la única del censo que no es Apache ni GPL, y su obligación es más suave: los archivos modificados se comparten, el resto puede quedar cerrado. Para el usuario no cambia nada; para quien quiera modificarlo, cambia bastante.

───────────────────

*🔌 El catálogo que los alimenta a todos*

Ningún motor de esta tabla sirve de nada sin el índice de extensiones, y el índice más grande es *Keiyoushi*: ★15.408, HTML, empujón de hoy, sin licencia declarada en la ficha.

Su función es la misma que la del colmado de la pieza 04 de esta serie: un archivo pequeño que dice qué extensiones existen y de dónde se baja cada una. Cuando algo deja de aparecer, en la mitad de los casos el problema está ahí y no en el motor.

Su licencia es el detalle incómodo de la tarde. ★15.408 y ninguna licencia declarada significa que el índice se puede leer y no está claro bajo qué condiciones se puede reutilizar. Los motores lo consultan igual porque es el que todos usan, y esa costumbre es la que hace que el ecosistema dependa de un proyecto cuya letra pequeña nadie ha leído.

Hay una segunda parte que casi nadie mira: el catálogo no es el contenido, es la lista. Y las listas envejecen rápido, porque cada sitio que cambia de diseño rompe una extensión. El empujón de hoy de este repositorio no significa que todo funcione: significa que alguien tocó el índice hoy.

───────────────────

*🧨 Cuando el motor abre y no ve nada*

El síntoma más común de esta familia y el que más reinstalaciones provoca. Cinco causas, en orden de probabilidad.

*Primera: el índice está viejo.* Se pegó hace meses y las extensiones nuevas no están. Se actualiza desde los ajustes y aparece todo.

*Segunda: el índice se pegó mal.* Un enlace incompleto o con un espacio al final devuelve una lista vacía sin decir nada. Se vuelve a pegar y se comprueba que la lista aparece.

*Tercera: la extensión está instalada y el sitio no responde.* El motor la lista y al abrir no hay nada, porque el sitio cambió o está caído. Se prueba el sitio en el navegador antes de tocar el lector.

*Cuarta: el motor es más nuevo o más viejo que la interfaz de extensiones.* Aquí no hay arreglo desde los ajustes: hay que actualizar el motor o cambiar de rama, como en la familia de la pieza 15.

*Quinta: el paquete de la extensión se instaló a mano desde otro sitio.* Es la causa menos común y la más peligrosa, porque el origen no está en ningún índice y nadie ha mirado su firma.

Las cinco se distinguen en diez minutos, y en cuatro de las cinco no hay que reinstalar nada.

───────────────────

*🧹 Biblioteca, descargas y respaldos*

Las tres carpetas de siempre, con los nombres de esta familia.

*La biblioteca* es pequeña y vive en la base de datos del motor. Se exporta a mano y viaja entre motores de la misma familia mientras el formato no cambie. Es lo único que hay que salvar antes de cualquier mudanza.

*Las descargas* viven en una carpeta con el nombre del paquete de la app y no viajan. En un teléfono de 128 gigas, con trescientos capítulos, esa carpeta puede llegar a la mitad del almacenamiento, y es la primera que hay que mirar cuando el aparato se pone lento.

*La caché* es la que se puede borrar sin miedo: portadas, miniaturas y fragmentos. Se llena sola de nuevo y es la que hace que el teléfono respire después de un año sin limpieza.

Con un servidor de por medio, la cosa cambia: la biblioteca y las descargas viven en la computadora y el teléfono solo guarda su caché. Es la configuración más limpia de todas y exige tener la computadora encendida, que es el precio.

───────────────────

*🛠️ Elegir motor en cinco preguntas*

**¿Cuántos títulos tienes?** Menos de cincuenta: cualquiera. Más de doscientos: SY, que es el que ordena mejor.

**¿Qué te molesta del lector que usas?** Si es la biblioteca, SY. Si es la pantalla, Komikku. Si es el desorden entre aparatos, un servidor.

**¿Tienes computadora encendida a diario?** Sí: servidor. No: motor en el teléfono y respaldo mensual.

**¿Tu teléfono es viejo?** Entonces el motor más sobrio, y el que menos memoria ocupe. Mihon es el más probado en aparatos modestos.

**¿Vas a probar cosas nuevas cada mes?** Si la respuesta es sí, elige el que empuja hoy y sigue su tabla de versiones. Si es no, elige el que tenga paquete reciente y no lo toques más.

Cinco preguntas y ninguna menciona las estrellas, que es exactamente el punto de esta guía.

───────────────────

*⚖️ La ley, la licencia y el nombre*

Las licencias de esta tabla son cuatro y conviene tenerlas escritas juntas.

*Apache-2.0* cubre a Mihon, Komikku, TachiyomiSY, MihonSY, ShinKu y Mikku: usar, modificar y distribuir, con aviso de autoría y mención de cambios.

*MPL-2.0* cubre a Suwayomi-Server: lo mismo, con la obligación limitada a los archivos modificados.

*GPL-2.0* cubre a Syncyomi: si se distribuye una versión modificada, se comparte el código.

*Y una ausencia*: el catálogo de ★15.408 no declara licencia, y eso se publica tal cual sin inventar la que le gustaría a nadie.

El nombre, como siempre, no va con el código. Los dos motores grandes llevan apellidos que evocan la familia y ninguno puede reclamar el nombre original; el contenido tampoco va con la licencia y esta guía no reparte direcciones de lectura.

───────────────────
*🧭 El servidor, montado en una tarde*

Para quien tenga computadora y quiera probar, el camino tiene cuatro estaciones y la cuarta es la que casi todos saltan.

*Estación uno: el programa.* Se instala Suwayomi-Server en la computadora —un ejecutable o un contenedor, según el sistema— y se abre en el navegador desde la propia máquina. Esa primera prueba confirma que arrancó.

*Estación dos: el catálogo.* Se pega el índice de extensiones en los ajustes del servidor, igual que se haría en el teléfono. El servidor instala las extensiones, que es lo que muchos no esperan: no hace falta instalarlas en cada aparato.

*Estación tres: la red de la casa.* Se le da una dirección fija a la computadora y se abre el puerto desde la red local. Aquí está la parte difícil: en algunos routers se llama de una manera y en otros de otra, y en los más cerrados hay que tocar dos ajustes.

*Estación cuatro: cerrar la puerta.* Si el servidor va a estar encendido siempre, no debe quedar abierto a internet sin contraseña. Un servidor casero mal cerrado es una biblioteca con la puerta de la calle abierta, y esa es la estación que casi nadie hace.

Con las cuatro, el teléfono se conecta por el navegador y ve la biblioteca del servidor. Sin la cuarta, el experimento funciona los primeros días y se convierte en un problema después.

───────────────────

*🕰️ Cómo se llegó a dos escuelas*

La historia de esta familia explica por qué hay dos motores grandes vivos y no uno.

El motor base creció como proyecto único durante años y su público se acostumbró a una sola manera de hacer las cosas. Cuando el tronco original dejó de publicar, la comunidad se dividió entre los que querían continuidad y los que querían cambios de fondo.

Los de continuidad se quedaron con el esqueleto y mejoraron lo que ya había. Ahí está SY: biblioteca, filtros, orden. Su versión 1.13.2 y su código de hoy dicen que la línea sigue.

Los de cambios de fondo se llevaron el esqueleto y rehicieron el lector. Ahí está Komikku: la pantalla, la paginación, la lectura. Su v1.14.1 y su empujón de hoy dicen lo mismo.

En medio quedó Mihon, que es el que la mayoría instala porque es el que aparece primero en las búsquedas y el que arrastra ★24.939.

Y alrededor, una capa de proyectos pequeños que nacen sobre uno u otro: MihonSY con ★48, ShinKu con ★45 y versión de hoy, Mikku con ★0 y un día de vida. Son la prueba de que las dos escuelas siguen tan vivas como para tener herederos propios.

───────────────────

*🔍 El caso del progreso que no aparecía*

Un usuario leyó veinte capítulos en el teléfono, abrió la computadora y encontró la biblioteca intacta y el progreso en cero. Concluyó que el servidor era malo.

El diagnóstico real: había dos bibliotecas. La del teléfono, con su base de datos, y la del servidor, que tenía los títulos pero no el progreso de ese aparato. Ninguna estaba mal: no estaban sincronizadas.

La solución tiene tres caminos. El primero, usar el servidor como única fuente y leer desde el navegador en el teléfono, con lo que el progreso se guarda donde se ve. El segundo, añadir la pieza de sincronización —Syncyomi, ★741, GPL-2.0, versión v1.7.4 del 29 de octubre— que existe exactamente para esto. El tercero, exportar y unir a mano, que es el camino de siempre y el que menos se automatiza.

El caso deja una lección que vale más que la herramienta: en cuanto hay dos aparatos, el progreso deja de ser un detalle y pasa a ser el problema principal. Y se resuelve eligiendo una fuente de verdad, no sumando aparatos.

───────────────────

*📶 Leer sin conexión cuando hay servidor*

La ventaja que casi nadie considera de esta configuración es la lectura sin red. Con los capítulos descargados en la computadora, el teléfono puede leerlos desde la red local aunque no haya internet, siempre que esté en casa. Y con los capítulos descargados en el teléfono, se leen en cualquier parte.

La combinación que mejor funciona es la de dos capas: el servidor baja y guarda lo que se lee en casa, y el teléfono descarga solo lo que se va a leer fuera. Cada capa hace lo que sabe hacer: el disco grande guarda, el bolsillo lleva.

El límite es el de siempre: si el servidor está apagado y no hay descarga local, no hay lectura. Y el servidor casero se apaga cuando se va la luz, que en esta isla es una consideración práctica y no una hipótesis.

───────────────────

*🧮 Tres cuentas del servidor*

La primera es de disco: un servidor casero con trescientos títulos y sus capítulos puede pedir entre cien y trescientos gigas. Es lo que un teléfono no tiene y lo que un disco externo sí.

La segunda es de corriente: una computadora encendida todo el día consume, y un aparato pequeño dedicado consume menos. Si el servidor va a estar siempre arriba, el aparato importa más que el programa.

La tercera es de tiempo: la primera configuración de red es una tarde; el mantenimiento, un rato cada tanto. Quien no quiera tocar un router una vez al año, se queda con el teléfono y el respaldo mensual.

Las tres cuentas juntas explican por qué esta configuración es la mejor para unos y un estorbo para otros, sin que ninguna de las dos opiniones esté equivocada.

───────────────────
*🎚️ Las funciones que de verdad se usan*

Después de leer foros durante meses, hay un patrón en lo que la gente usa de verdad, y no coincide con lo que los README destacan.

*Lo que se usa todos los días:* abrir la biblioteca, ver lo último leído, buscar una serie, descargar capítulos, marcar como leído y actualizar el catálogo. Siete acciones que cualquier motor de esta tabla hace bien.

*Lo que se usa una vez y nunca más:* los ajustes de lector, los temas, el tamaño de la letra, la dirección de paginación. Se configuran en la primera tarde y no se vuelven a tocar.

*Lo que se usa cuando la biblioteca crece:* filtros, categorías, ordenaciones y búsqueda dentro de lo descargado. Es el terreno de SY, y es donde un motor mediocre se vuelve insoportable con trescientos títulos.

*Lo que casi nadie usa y todos piden:* estadísticas, historial detallado, exportación a formatos raros. Son funciones que existen porque alguien las quiso, no porque alguien las necesite.

La consecuencia para quien elige motor es simple y ahorra horas: mira tu biblioteca, no la lista de funciones. Menos de cincuenta títulos se administran en cualquier motor; más de doscientos exigen uno que ordene bien, y ese es el único criterio que de verdad pesa.

───────────────────

*🧷 Los cuatro detalles de la sincronización*

Cuando hay dos aparatos, el progreso se convierte en el problema principal. Cuatro detalles explican casi todos los disgustos.

*El primero: la marca de leído no es un archivo.* Vive en la base de datos de cada motor. Exportar la biblioteca la lleva consigo; leer en dos aparatos sin exportar, no.

*El segundo: el capítulo leído se guarda por identificador de extensión.* Si un aparato usa la extensión de un catálogo y el otro la de otro, los dos pueden marcar el mismo capítulo como cosas distintas y el progreso se duplica o se pierde.

*El tercero: la sincronización llega tarde.* Un servicio de sincronización no es magia: guarda cuando puede. Si se lee en el avión y se abre el otro aparato antes de volver a la red, el progreso no está y hay que esperar.

*El cuarto: las descargas no se sincronizan nunca.* Cada aparato baja lo suyo. Confundir sincronización de progreso con sincronización de archivos es la causa de la mitad de las quejas de almacenamiento.

───────────────────

*🛠️ Montar el servidor sin abrir la casa*

Cinco reglas mínimas para quien se anime, y ninguna es opcional si el servidor va a estar encendido.

*Regla uno: contraseña desde el primer día.* El servidor tiene su propio usuario y su propia clave. Un servidor casero sin contraseña en una red compartida es una biblioteca abierta.

*Regla dos: solo en la red de la casa.* No abrir el puerto a internet salvo que se sepa exactamente lo que se está haciendo. Para leer fuera de casa hay caminos más seguros y más lentos.

*Regla tres: copia de la carpeta del servidor.* La biblioteca del servidor es un archivo más y se puede perder con el disco. Una copia mensual a otro disco resuelve el 90% de los desastres.

*Regla cuatro: actualizar con respaldo.* El servidor también cambia de versión y también puede romper algo. La versión v2.4.2366 del 30 de septiembre está en un proyecto que empuja hoy: hay trabajo y eso significa cambios.

*Regla cinco: anotar la dirección.* Cuando la computadora cambie de dirección de red, el teléfono pierde la biblioteca y el usuario cree que se borró. Una nota con la dirección fija ahorra ese susto.

───────────────────

*📱 El teléfono modesto y los dos motores*

En un aparato de 2019, la diferencia entre los dos motores se nota antes que en uno nuevo, y no siempre a favor del que más funciones tiene.

SY, con su biblioteca cargada de filtros y estadísticas, pide más memoria cuando hay cientos de títulos. En un aparato con tres gigas, esa diferencia se ve en que la biblioteca tarda en abrir y en que el sistema cierra la app cuando se cambia a otra cosa.

Komikku, centrado en el lector, pesa menos en la pantalla de biblioteca y más en la de lectura, y su comportamiento en aparatos modestos depende más de la imagen que de la lista.

La regla práctica es la de siempre: instalar, importar el respaldo de prueba, mirar cuánta memoria queda libre y decidir con eso. Un motor con menos funciones que abre en dos segundos vale más que uno completo que tarda seis.

───────────────────

*🗣️ Las frases que se repiten*

«SY es el de las funciones». Es cierto y hay que añadir: y el que más memoria pide con bibliotecas grandes.

«Komikku es más moderno». Es más reciente como proyecto y no necesariamente mejor para tu uso. Moderno y útil no son sinónimos.

«El servidor es para expertos». Es para quien tenga computadora encendida y ganas de configurar una red una vez.

«Mihon es el original». Es la base más usada y no el original de la familia. El original dejó de publicar hace años.

«Con dos aparatos ya no necesito respaldo». Al contrario: con dos aparatos el respaldo importa el doble, porque hay dos sitios donde perderlo.

*🧪 Cuatro pruebas antes de decidirte*

*Prueba uno: la biblioteca.* Importa tu respaldo en el motor candidato y cronometra cuánto tarda en abrir. Con trescientos títulos, la diferencia entre dos motores es de segundos que se sienten como minutos cada día.

*Prueba dos: la extensión que más usas.* Abre una serie de la extensión que lees a diario, no de la más conocida. Ahí se ve si el motor entiende el catálogo de hoy.

*Prueba tres: la descarga.* Baja tres capítulos y comprueba dónde quedaron y cuánto ocuparon. Es el dato que decide si el teléfono aguanta el año.

*Prueba cuatro: el respaldo de vuelta.* Exporta desde el candidato e importa en el motor de siempre. Si el viaje de ida y vuelta funciona, la mudanza es reversible, y eso es lo que da tranquilidad para probar.

Las cuatro ocupan una hora y contestan lo que ninguna tabla contesta: cómo se comporta ese motor en tu teléfono con tu biblioteca.

───────────────────

*🧾 Lo que costó medir esta familia*

Las cifras de esta tabla vinieron de tres caminos distintos por cada proyecto, y en dos casos la página del repositorio dio un número de estrellas mayor que la búsqueda por unos minutos de diferencia: se publicó el de la página, que es el que ve una persona al entrar.

La parte difícil fue el catálogo. Es el proyecto con más estrellas de la tabla —★15.408— y el único sin licencia declarada, y esa casilla vacía se publica vacía aunque quede fea en una tabla ordenada.

La segunda parte difícil fue el servidor. Su cifra no se puede comparar con la de un lector de teléfono: ★7.989 para un programa de computadora que alimenta a todos los demás no significa menos importancia, significa otro papel. Ponerlo en la misma tabla es una decisión de esta guía y va explicada en la columna «qué hace».

───────────────────

*🔁 El viaje de ida y vuelta del respaldo*

El respaldo es el único seguro de esta familia y casi nadie lo prueba en los dos sentidos. Exportar es la mitad; importar de vuelta es la prueba de que sirve.

El viaje completo tiene tres tramos. En el primero se exporta desde el motor actual y se guarda el archivo fuera del teléfono. En el segundo se importa en el motor candidato y se comprueban tres cosas: los títulos, el progreso y las categorías. En el tercero se exporta desde el candidato y se importa otra vez en el original.

Si el tercer tramo funciona, la mudanza es reversible, y eso es lo que permite probar sin miedo. Si falla, se ha descubierto algo importante antes de borrar nada: ese motor cambia el formato y la vuelta atrás no existe.

El error clásico es hacer solo el primer tramo y creer que el archivo está bien. Un respaldo que nunca se ha importado es una promesa, no una copia.

───────────────────

*🧭 Cinco señales de que hay que mudarse*

Mudarse de motor cuesta una tarde y no se hace por gusto. Estas cinco señales justifican el gasto.

*Señal uno: el motor dejó de entender el catálogo.* Aparecen extensiones y no abren, o el índice actualizado no lista nada. Es la señal más clara y no tiene arreglo desde los ajustes.

*Señal dos: el paquete lleva más de un año y el código también.* El proyecto está quieto y no hay nadie al otro lado. Llegará el día en que algo se rompa y no habrá quien lo arregle.

*Señal tres: la biblioteca se volvió inmanejable.* Cientos de títulos sin orden y un motor sin filtros ni categorías. Aquí la mudanza no es por salud del proyecto, es por salud de la persona.

*Señal cuatro: el teléfono cambió y el motor no arranca.* Un aparato nuevo o viejo que no soporta la versión que hay. Cambiar de motor es más barato que cambiar de teléfono.

*Señal cinco: hay dos aparatos y el progreso no coincide.* Cuando exportar a mano deja de ser sostenible, toca servidor o pieza de sincronización.

Fuera de esas cinco, mudarse es probar, y probar está bien mientras haya respaldo y un motor al que volver.

───────────────────

*📚 Lo que esta familia enseña sobre elegir software*

Nueve proyectos, dos escuelas y una ausencia de licencia. Tres lecciones que sirven más allá de los lectores de manga.

La primera: cuando un ecosistema tiene dos proyectos vivos que publican, el usuario gana. La competencia no reparte el público de forma dañina; reparte funciones y cada uno elige. Es lo contrario de lo que pasa en una familia de copias quietas.

La segunda: el componente del que todos dependen es el que menos se mira. El índice de ★15.408 alimenta a todos los motores de esta tabla y es el único sin licencia declarada. Nadie elige su lector pensando en el índice, y el índice decide si el lector sirve.

La tercera: la comodidad tiene un precio medible en configuración. El servidor de ★7.989 es la opción más ordenada y la que más trabajo pide la primera vez. No hay una opción mejor en abstracto: hay una mejor para cada casa.

───────────────────

*🧷 El detalle del nombre y de la cuenta*

Los dos motores grandes llevan apellidos que evocan la familia y publican desde cuentas propias. Esa distinción importa el día que alguien busca el proyecto y encuentra una copia.

La cuenta que publica es el dato más estable de todos: un repositorio puede cambiar de nombre, una cuenta rara vez. Cuando dos proyectos se llaman casi igual, se compara la cuenta y la fecha, y con eso se acaba la duda.

───────────────────

*🖱️ La computadora como lectora*

Usar el servidor cambia también el aparato con el que se lee, y hay un público que casi nunca se nombra: el que prefiere leer en la pantalla grande.

Con la biblioteca en la computadora, la lectura se hace en el navegador, con teclado para pasar páginas y una pantalla que no se cansa la vista. Para series largas y sesiones de dos horas, es más cómodo que cualquier teléfono, y no requiere instalar nada más.

La ventaja secundaria es el orden: la misma biblioteca que se ve en el teléfono aparece en la computadora, con las mismas categorías y el mismo progreso. Cuando una serie se pone interesante a las once de la noche en el teléfono, se continúa al día siguiente en la computadora sin buscar dónde se quedó.

El límite es el de siempre y no se puede rodear: la computadora tiene que estar encendida y en la misma red, o el navegador no encuentra la biblioteca.

───────────────────

*🧮 Tres formas de tener lo mismo en dos aparatos*

Hay tres maneras de que dos aparatos vean la misma biblioteca, y conviene saber cuál se está usando antes de quejarse de que no funciona.

*La primera es exportar e importar.* Un archivo que viaja a mano cada cierto tiempo. Es la más simple, la que no depende de nada y la que se olvida siempre. Sirve para dos aparatos que se usan de forma alterna y con disciplina.

*La segunda es un servidor.* Una fuente única que los dos aparatos consultan. Es la más ordenada y la que exige una computadora encendida. Cuando funciona, desaparece el problema; cuando no, desaparecen los dos aparatos a la vez.

*La tercera es una pieza de sincronización.* Un programa que copia el progreso de un sitio al otro sin mover la biblioteca. Es el camino intermedio y el que menos se documenta, y en esta familia tiene nombre propio: Syncyomi, ★741, GPL-2.0, versión v1.7.4 del 29 de octubre.

Las tres conviven y ninguna es la correcta en abstracto. La pregunta es cuántos aparatos, cuánta disciplina y cuánta computadora hay en la casa.

───────────────────

*🧯 El servidor que se cae y lo que se pierde*

Cuando el servidor se apaga, los aparatos que dependen de él no pierden la biblioteca: pierden el acceso. Esa diferencia es la que hay que entender antes de asustarse.

Lo que se pierde: el catálogo en pantalla, la lectura de lo no descargado y la sincronización del progreso. Lo que no se pierde: la biblioteca guardada en el disco del servidor, que sigue ahí esperando.

La consecuencia práctica es que un servidor casero necesita dos costumbres. La primera, la copia del disco, porque un servidor caído se arregla y un disco perdido no. La segunda, una lista de qué está descargado en el teléfono, para saber qué se puede leer mientras el servidor vuelve.

───────────────────

*🎯 El caso del catálogo que se pegó dos veces*

Un usuario pegó el índice en dos motores y en uno apareció todo y en el otro la lista vacía. El enlace era el mismo y la conclusión fácil era que el segundo motor era malo.

La causa real: había un espacio pegado al final del enlace. El primer motor toleraba el espacio, el segundo no. Dos minutos de mirar el texto, cinco de borrar un carácter y el problema resuelto.

El caso vale como recordatorio: en esta familia, la mitad de los fallos que parecen del motor están en la línea de texto que alguien pegó, y la otra mitad están en la fecha del paquete.

───────────────────

*📌 Lo que hay que apuntar del motor propio*

Cuatro líneas y no más: qué motor, qué versión, qué catálogo y cuándo se exportó el último respaldo.

Con esas cuatro, cualquier problema futuro se diagnostica en dos minutos, y cualquier pregunta en un grupo se contesta con datos en lugar de con impresiones.

───────────────────

*🧷 Dos palabras para llevarse*

Motor y catálogo. El primero dibuja; el segundo dice de dónde. Cuando algo no aparece, casi siempre es el segundo.

───────────────────

*🗂️ Una fecha en el calendario*

Una vez al mes: actualizar el catálogo, exportar el respaldo y mirar si los dos motores publicaron algo nuevo. Tres tareas de cinco minutos que mantienen el sistema sano sin leer una guía entera.

───────────────────

*🧷 Lo que queda dicho*

Ninguna de las nueve piezas de esta tabla promete nada que no se pueda comprobar en su repositorio, y esa es toda su garantía.

───────────────────

*📎 Y una costumbre más*

Antes de instalar cualquier motor, escribir en una nota la fecha del día. Dentro de un año, esa línea es la que explica por qué el teléfono tiene el lector que tiene.

───────────────────

*❓ Preguntas que me hacen*

**¿SY o Komikku?** Depende de tu biblioteca y de tu pantalla. Con muchos títulos, SY ordena mejor; si lo que te molesta es el lector, Komikku. Los dos empujaron hoy y los dos publican con regularidad.

**¿Por qué las versiones son de julio si empujan hoy?** Porque el código y el paquete son dos relojes. Los dos motores trabajan en algo que todavía no han publicado, y esa diferencia se ve en la tabla.

**¿Qué gano con un servidor?** Una biblioteca única para varios aparatos, descargas en un disco grande y nada que mudar cuando cambias de teléfono. Lo pagas con una computadora encendida.

**¿Puedo usar el servidor sin internet?** En la red de la casa, sí, si los capítulos están descargados. Fuera de casa depende de cómo se haya configurado, y ahí conviene no improvisar.

**¿Qué es Syncyomi y lo necesito?** Es la pieza que sincroniza el progreso entre aparatos, ★741, GPL-2.0, versión del 29 de octubre. Si lees en dos sitios y quieres el progreso igual en los dos, sí la necesitas.

**¿Por qué el catálogo no tiene licencia?** Porque su ficha no la declara. Se publica el dato tal cual y se advierte, como en toda la serie.

**¿Cambiar de motor borra mis descargas?** Las deja en la carpeta del motor viejo, donde el nuevo no las ve. Se borran a mano o se vuelven a bajar.

───────────────────

*📊 Tabla, mitos y glosario*

*Las nueve medidas, en una línea*

| Repositorio | Qué hace | Licencia | Empujón | Versión | Estrellas |
|---|---|---|---|---|---|
| Mihon | el motor base más instalado | Apache-2.0 | 26-oct | v0.21.3 (25-oct) | ★24.939 |
| Keiyoushi/extensions | el índice de extensiones | sin licencia | hoy | — | ★15.408 |
| Suwayomi-Server | biblioteca en la computadora | MPL-2.0 | hoy | v2.4.2366 (30-sep) | ★7.989 |
| Komikku | la escuela del lector | Apache-2.0 | hoy | v1.14.1 (17-jul) | ★4.966 |
| TachiyomiSY | la escuela de la biblioteca | Apache-2.0 | hoy | 1.13.2 (13-jul) | ★4.200 |
| Syncyomi | sincroniza el progreso | GPL-2.0 | 29-oct | v1.7.4 (29-oct) | ★741 |
| MihonSY | hijo pequeño de SY | Apache-2.0 | 28-oct | v1.2.1 (07-oct) | ★48 |
| ShinKu | el más rápido de los pequeños | Apache-2.0 | 01-nov | v2.8.0 (01-nov) | ★45 |
| Mikku | el que nadie miró | Apache-2.0 | 31-oct | sin versión | ★0 |

*Cinco mitos de los motores*

**Mito uno: «el que tiene más estrellas es el más completo».** Mihon tiene ★24.939 y SY, con menos, ordena mejor una biblioteca grande. La función y la fama no van juntas.

**Mito dos: «versión de julio es abandono».** Los dos motores empujaron hoy con versión de julio. El paquete es más viejo que el trabajo.

**Mito tres: «el servidor es para técnicos».** Es para quien tenga computadora encendida. Lo técnico es la primera tarde de red, no el uso diario.

**Mito cuatro: «con dos aparatos no hace falta respaldo».** Con dos aparatos hay dos sitios donde perder la biblioteca.

**Mito cinco: «el catálogo es el contenido».** El catálogo es la lista de direcciones; el contenido lo pone cada extensión y cada sitio.

*Glosario*

**Motor** — el programa que dibuja la biblioteca y la lectura.

**Catálogo** — índice de extensiones que el motor entiende.

**Servidor** — programa en una computadora que guarda la biblioteca y la sirve por la red.

**Sincronización** — igualar el progreso entre aparatos.

**Respaldo** — archivo con biblioteca y progreso.

**MPL-2.0** — licencia que obliga a compartir solo los archivos modificados.

───────────────────

*🔗 Enlaces*

Todas las direcciones se abrieron esta tarde.

- Mihon, el motor base: https://github.com/mihonapp/mihon
- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY
- Komikku: https://github.com/komikku-app/komikku
- MihonSY: https://github.com/ruzhe85/MihonSY
- ShinKu: https://github.com/Harrys-HQ/ShinKu
- Mikku: https://github.com/nas3ts/mikku
- Suwayomi-Server: https://github.com/Suwayomi/Suwayomi-Server
- Syncyomi: https://github.com/syncyomi/syncyomi
- El catálogo de extensiones: https://github.com/keiyoushi/extensions

*Cómo se midió.* Nueve repositorios, tres lecturas cada uno por tres caminos distintos y el orden rotado; las versiones se pidieron una por una y las que no existen se anotan como «sin versión». Donde la página del repositorio y la búsqueda discreparon en estrellas, se publicó la de la página.

───────────────────

*🌅 Cierre — dos motores que sí entregan*

Esta familia es lo contrario de la anterior: aquí el tronco publica, los herederos publican y hasta los proyectos de ★0 empujan ayer. Eso cambia la conversación: ya no se trata de buscar quién sigue vivo, sino de elegir entre dos escuelas que funcionan.

La escuela de la biblioteca —SY, ★4.200, versión 1.13.2— y la escuela del lector —Komikku, ★4.966, v1.14.1— comparten esqueleto y no comparten empeño. Alrededor, Mihon con ★24.939 sigue siendo la puerta de entrada, Suwayomi-Server con ★7.989 lleva todo a la computadora y Syncyomi con ★741 hace que dos aparatos cuenten la misma historia.

Y el detalle de la tarde: el proyecto con más estrellas de la tabla no es un lector, es el índice ★15.408 que los alimenta a todos y que no declara licencia. El ecosistema depende de una lista, y las listas no juran lealtad a nadie.

> —¿Y si los dos motores se cansan?
> —Hay tres proyectos de ★48, ★45 y ★0 esperando. El ecosistema siempre tiene relevo, aunque el relevo no tenga público.

💓 *La Bandita informa a partir de fuentes fechadas.* Un motor se elige por lo que hace con tu biblioteca, no por lo que promete en su README.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 19:06 y las 19:18 de Santo Domingo · nueve repositorios con las tres lecturas completas y el orden rotado · nueve versiones consultadas una por una, una de ellas inexistente y anotada como tal.

*Licencia de esta entrega:* prosa en CC BY-SA 4.0, cifras en CC BY 4.0 y ejemplos de código en MIT; la marca y el nombre de la casa siguen reservados a «Alexis (La Bandita)».

## 🗒️ Notas al pie

**Nota de corte (1-nov):** los dos motores grandes empujaron el mismo día del corte y sus paquetes son de julio; las dos fechas van en la tabla para que no se confundan.

**Nota de licencia (1-nov):** el proyecto con más estrellas de la tabla no declara licencia. Se publica así, sin rellenar el campo con la del vecino.

**Nota de alcance (1-nov):** la guía no reparte enlaces de contenido ni catálogos concretos de sitios; mide proyectos de software y explica cómo comprobar uno antes de usarlo.

**Nota de corrección (1-nov):** la versión anterior de esta pieza era un listado del 15 de septiembre con cuatro nombres y sin el servidor. Se reescribió con las nueve piezas medidas hoy, incluidos los tres proyectos pequeños y el índice que los alimenta.
