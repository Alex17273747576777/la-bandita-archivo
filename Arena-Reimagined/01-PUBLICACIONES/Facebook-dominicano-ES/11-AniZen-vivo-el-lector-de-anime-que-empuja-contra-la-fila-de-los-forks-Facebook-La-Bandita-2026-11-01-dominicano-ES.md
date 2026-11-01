*AniZen vivo: el lector de anime que empuja contra la fila de los forks*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 11 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🏷️ Tres nombres que la gente confunde
├── 📅 «Vivo» no es «con versión nueva»
├── 🎬 Cuatro escenas y el censo de esta tarde
├── 🔀 La familia del anime y su tronco quieto
├── 🧪 El canal de pruebas y los huecos del censo
├── 🛠️ Comprobar un lector y mudarse sin perder nada
├── 📺 El video y sus tres finales
├── 📱 El teléfono viejo y la ley
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
├── 🔗 Enlaces y notas al pie
```

*⚡ En una página*

Hay un lector de anime que sacó una versión ayer y lleva doscientos veinte números en el contador. Se llama AniZen, es Apache-2.0, está escrito en Kotlin, tiene ★200 y empujó su código el 31 de octubre. Al lado conviven un motor de ★7.866 que no empuja desde el 14 de septiembre, un fork de ★287 que empujó el 29 de octubre, una casa que saca versiones cada semana y no declara licencia, y un lector de manga de ★24.939 que sirve de vara para comparar. Ese es el mapa real del anime en el teléfono esta tarde.

La confusión que más escucho es de vocabulario: la gente dice «se cayó el lector» cuando se rompió una extensión, y dice «cambié de app» cuando solo cambió de motor. Son tres piezas distintas con tres dueños distintos, y el anime tiene la mala suerte de que su pieza central —el motor grande— es la que se quedó quieta.

Lo segundo que hay que aprender es a separar dos fechas: la del último empujón de código y la del último paquete publicado. No siempre coinciden, y la que le sirve a quien usa el teléfono es la segunda. AniZen empuja y publica casi al mismo ritmo; otros empujan y no publican; otros publican sin empujar nada visible.

Si te llevas una idea: el anime en Android no está muerto ni resucitó, está repartido. Hay un tronco que dejó de latir y una fila de forks que lo mantienen con vida a empujones, cada uno con su público y su manera de romperse.

───────────────────

*🏷️ Tres nombres que la gente confunde*

El motor es el programa que abre las series, dibuja las portadas y guarda tu biblioteca. Es lo que se instala y lo que se ve en el cajón de apps. Se le puede llamar lector, cliente o reproductor; da igual mientras se entienda que es el que manda sobre tus datos.

La extensión es un añadido que sabe hablar con un sitio concreto. No sirve para otro sitio, no abre sola y no actualiza nada por su cuenta: cuando la página cambia de diseño, la extensión se queda devolviendo errores y hay que reemplazarla. En el anime, además, la extensión suele tener dos mitades: la que lista capítulos y la que resuelve el video.

El catálogo es la lista de direcciones desde donde se bajan las extensiones. Es un archivo pequeño, se pega una vez en los ajustes del lector y desde ahí se actualiza. Cuando alguien dice que «no aparecen las extensiones», en la mitad de los casos el problema está en el catálogo viejo y no en el motor.

Con esas tres piezas separadas, casi todo lo demás se ordena. Una extensión rota se arregla en un minuto; un motor abandonado se arregla mudándose, que es una tarde; un catálogo muerto se arregla pegando otro y actualizando. Confundirlos es lo que convierte un problema de un minuto en una tarde perdida.

───────────────────

*📅 «Vivo» no es «con versión nueva»*

Un repositorio puede tener actividad todos los días y no publicar nada durante meses: eso pasa cuando el trabajo va a una rama que todavía no se empaqueta. Y puede tener un paquete nuevo cada semana mientras el código lleva un año igual, que es lo que ocurre cuando cada versión solo cambia un número y una firma.

Por eso el censo de esta guía anota siempre las dos columnas. Un ejemplo de la casa: Komikku empujó código hoy mismo, 1 de noviembre, y su última versión pública es v1.14.1 del 17 de julio. Las dos cosas son verdad al mismo tiempo. Quien mire solo la versión dirá que el proyecto duerme; quien mire solo el empujón dirá que acaba de cambiar lo que tiene instalado, y ninguna de las dos frases es correcta.

En el anime pasa lo contrario con más frecuencia: hay motores que publican release sobre release sin que el empujón visible cambie, porque la release se construye desde una rama de mantenimiento. AniZen, en cambio, empuja y publica a la vez: v0.5.220 salió el 31 de octubre, el mismo día del último empujón.

El número 220 tampoco significa veinte versiones grandes. Los contadores de versión no son una medida de madurez, del mismo modo que el kilometraje de un carro no dice si el motor está bien. Un contador alto suele indicar compilaciones frecuentes y un solo mantenedor probando rápido, que es bueno para los arreglos y malo para la estabilidad.

La cifra que sí dice algo es la diferencia entre las dos fechas. Si el paquete tiene más de un año y el código lleva nueve meses sin moverse, ese proyecto está terminado o abandonado, y en los dos casos conviene saberlo antes de meter la biblioteca dentro. Si el paquete es de esta semana, hay alguien pendiente, aunque sea una sola persona en su tiempo libre.

───────────────────

*🎬 Cuatro escenas de esta semana*

*El que perdió la biblioteca mudándose.* Tenía doscientos títulos guardados en un lector de anime y quiso probar otro. Instaló, importó el respaldo, y las descargas no aparecieron. La biblioteca sí: los títulos y el progreso viajaron en el archivo de respaldo. Lo que no viaja son los capítulos descargados, porque viven en una carpeta propia de cada app. Su conclusión, después de la tarde perdida, fue buena: cambiar de motor es barato si se hace con respaldo y caro si se hace a ciegas.

*La que instaló el canal de pruebas sin saberlo.* Bajó un paquete desde la página de versiones y eligió sin mirar la que decía «pre-release». Al día siguiente tenía funciones nuevas y un fallo que cerraba la app al abrir la biblioteca. No era un lector malo: era el canal donde se publican las pruebas. Volver atrás fue fácil porque el paquete anterior seguía publicado, y esa es la razón por la que conviene no borrar la versión que funciona.

*El que creía que el motor estaba muerto.* Vio el repositorio del motor grande del anime sin paquete nuevo desde septiembre y anunció en un grupo que el proyecto había terminado. Lo que había terminado era el ritmo, no el proyecto: el fork seguía empujando, la casa seguía publicando y las extensiones seguían actualizándose desde el catálogo. La confusión no fue de datos, fue de interpretación.

*La que administra tres teléfonos en casa.* Necesitaba que los tres tuvieran lo mismo y que las actualizaciones no rompieran nada. Su método: la misma versión en los tres, la actualización del sistema operativo del teléfono —no la del lector— congelada, y solo el lector actualizado cuando aparece una versión que arregla algo concreto que le pasó a ella. Tres teléfonos, tres copias de la misma carpeta de respaldo, cero sorpresas en dos meses.

───────────────────

*🧾 El censo de esta tarde*

*AniZen*, el que da título a la pieza: ★200, Apache-2.0, Kotlin, empujón del 31 de octubre, versión v0.5.220 del mismo día. Un mantenedor con ritmo alto y un contador que crece rápido. Su segunda casa, *anizen-preview*, tiene ★9, no declara licencia y empujó el mismo 31 de octubre: es el canal de pruebas, y ahí sí conviene que quien entre sepa que está en el canal de pruebas.

*Anikku*, el lector de anime de la casa de Komikku: ★1.127, Apache-2.0, Kotlin, empujón del 22 de octubre y versión v0.2.0 del 11 de septiembre. Es el intento más serio de tener un cliente de anime con base de mantenimiento detrás, y su contador de versión todavía corto dice lo que es: un proyecto en pañales con apoyo de un proyecto grande.

*Komikku*, el motor de manga de esa misma casa: ★4.966, Apache-2.0, empujón de hoy y versión v1.14.1 del 17 de julio. No es un lector de anime, y aparece en este censo porque es la referencia de lo que significa «mantenido»: código de hoy, paquete de hace tres meses, funciones de biblioteca muy por encima del promedio.

*Aniyomi*, el tronco del anime: ★7.866, Apache-2.0, Kotlin, empujón del 14 de septiembre y versión v0.18.2.1 del mismo día. Sigue siendo la base de casi todos los forks de la familia y su última publicación tiene ya casi dos meses. Es el número más alto del censo y el más quieto de los grandes.

*Tadami*, el fork que se separó con casa propia: ★287 en la versión que se presenta como fork de Aniyomi, Apache-2.0, empujón del 29 de octubre, versión v0.63.2 del 27. Y su casa matriz, *tadamiorg/tadami*, ★61, sin licencia declarada, empujón del 30 de octubre, versión v1.17.0 del mismo día. Dos repositorios para el mismo trabajo: uno cuenta la historia y el otro lleva el pulso.

*Mihon*, la vara del manga: ★24.939, Apache-2.0, Kotlin, empujón del 26 de octubre y versión v0.21.3 del 25. No lee anime, y está aquí porque cualquier discusión sobre forks de anime termina comparando con él, y conviene que la comparación se haga con números a la vista.

*Yokai-T*, el intento sin público: ★0, Apache-2.0, Kotlin, empujón del 26 de septiembre, sin versión publicada. Un repositorio con dos meses de vida, licencia clara y nadie mirando. Se publica para no dibujar un ecosistema donde solo existen los que tienen estrellas.

───────────────────

*🔀 La familia del anime y su tronco quieto*

La familia viene de la misma raíz que el manga: un motor que definió cómo se conectan las extensiones y una comunidad que aprendió a escribir las suyas. Esa raíz se bifurcó hace años y hoy tiene tres formas vivas: el tronco original, los forks que heredaron su interfaz y las casas nuevas que nacieron con su propia idea de la biblioteca.

El tronco original conserva el número más alto del censo y la fecha de publicación más vieja de los grandes. Su última versión, v0.18.2.1, salió el 14 de septiembre. No es abandono declarado: es velocidad cero con el cartel puesto. Un proyecto así sigue funcionando mientras el sistema no cambie nada que le afecte, y la familia de extensiones siga sirviendo paquetes compatibles.

Los forks son la parte que se mueve. Tadami empujó el 29 y el 30 de octubre según el repositorio que se mire, publicó v0.63.2 el 27 y v1.17.0 el 30, y es el que la gente usa cuando quiere funciones que el tronco no tiene. AniZen es el más nuevo del grupo con diferencia: ★200, versión del 31 de octubre y un canal de pruebas separado, que es una señal de que su autor espera que algo se rompa.

La tercera forma son las casas nuevas. Anikku, de la casa de Komikku, no hereda la interfaz del tronco: nace con la idea de que el anime debería compartir estantería con el manga en el mismo lector. Tiene ★1.127 y su versión es de septiembre. Es la apuesta que más papeletas tiene de crecer, y también la que más depende de que su casa grande siga viva.

Lo que no ha aparecido este año, y conviene decirlo, es un motor de anime con mantenimiento estable, ritmo tranquilo y documentación para quien quiera escribir extensiones. El hueco existe. Mientras exista, la fila de forks va a seguir siendo la forma normal del ecosistema y no una anomalía.

───────────────────

*🧪 El canal de pruebas: por qué el número no para*

Un contador que llega a 220 dice algo del método: el autor compila seguido y publica seguido, sin esperar a tener un lote grande de cambios. En proyectos pequeños eso es una decisión sensata, porque el que reporta un fallo puede probar el arreglo esa misma noche. En proyectos con muchos usuarios es una decisión que reparte el riesgo: cada paquete nuevo puede romper algo para todos.

Por eso la existencia de un segundo repositorio de pruebas no es un detalle administrativo. `anizen-preview`, ★9, sin licencia declarada, empujón del 31 de octubre, es la puerta por donde entra lo que todavía no se ha probado. La regla que se desprende es simple: el paquete de la casa principal para el teléfono de todos los días, el del canal de pruebas para el teléfono de las pruebas.

Hay un detalle que casi nadie mira y que vale más que la fecha: qué trae la versión nueva. Las notas de una release contestan tres preguntas en dos líneas: qué se arregló, qué se rompió y qué cambió de sitio. Un paquete que solo dice «mejoras de rendimiento» y no nombra un solo archivo tocado es un paquete que se instala por confianza, y la confianza se paga con respaldos.

El canal de pruebas también explica la cifra que más engaña: las estrellas. ★9 para el canal de pruebas no significa que el proyecto valga nueve estrellas; significa que la gente que lo probó es poca. La estrella mide atención, no calidad, y la atención se concentra en la puerta principal.

───────────────────
*🕳️ Los huecos del censo*

Un censo honesto incluye lo que no se pudo leer. Hoy hubo dos.

El primero es *Gaijin81/anizen*, un repositorio con el mismo nombre del lector y sin README legible en ninguna de las ramas que se probaron. Sin archivo de presentación no hay licencia que citar, ni cifra de versión, ni descripción que se pueda publicar. Se nombra y se deja fuera de la tabla, porque una ficha sin datos es peor que un hueco confesado.

El segundo no es un hueco de lectura sino de público: *Yokai-T*, ★0, Apache-2.0, empujón del 26 de septiembre, sin versión. Tiene todo lo que se le pide a un proyecto —licencia clara, código reciente y un nombre— y no tiene una sola persona mirándolo. En estos censos aparecen siempre dos o tres así, y son la parte que impide creer que el ecosistema crece solo.

Hay un tercer hueco, este de otra clase: el motor grande del anime no publica desde el 14 de septiembre y su repositorio de extensiones tampoco es el que la mayoría usa hoy. Eso deja a los usuarios nuevos en una situación rara, porque el camino que encuentran en los tutoriales viejos ya no es el camino que funciona.

Y un cuarto, el más importante para quien lee: no existe hoy forma de saber, mirando el repositorio, si un fork va a seguir vivo en marzo. La fecha del empujón dice lo de esta semana. Lo demás es fe.

───────────────────

*🛠️ Comprobar un lector en cinco pasos*

**Paso uno: la ficha del repositorio.** Se abre la dirección del proyecto y se miran tres cosas en la misma pantalla: la licencia en la columna derecha, la fecha del último empujón arriba y la pestaña de versiones. Si la licencia no aparece, se anota «sin licencia» y se sigue; si la fecha tiene más de un año, se anota y se sigue también, porque lo que decide no es una sola señal.

**Paso dos: la última versión, con su nota.** No basta con leer el número. La nota de la release dice qué se arregló; si está vacía o solo dice mejoras, el paquete es una caja cerrada y hay que tratarlo como tal.

**Paso tres: el paquete descargado.** Se mira el tamaño y se compara con lo que la nota anuncia. Un APK de tres megas para un lector que siempre pesó veinte es una rareza que se pregunta antes de instalar.

**Paso cuatro: la firma.** Con AppManager, con un visor de paquetes o con el propio sistema al actualizar, se comprueba que la versión nueva viene firmada por la misma llave que la vieja. Si la firma cambió, hay dos historias posibles y las dos merecen una pausa.

**Paso cinco: el respaldo.** Antes de actualizar, un archivo de respaldo de la biblioteca guardado fuera del teléfono. No es desconfianza del proyecto: es que el respaldo cuesta dos minutos y la biblioteca cuesta años.

Cinco pasos, quince minutos, y el resultado no es una garantía: es una decisión informada. La diferencia entre las dos cosas se nota el día que algo falla, porque quien decidió informado tiene a dónde volver.

───────────────────

*💾 Lo que se pierde al cambiar de motor*

Mudarse de lector no es como cambiar de funda. Hay tres cosas que viajan, dos que no y una que se pierde para siempre si no se respalda antes.

Lo que viaja: la lista de títulos de la biblioteca, el progreso de lectura y las categorías. Todo eso cabe en un archivo de respaldo que el propio lector exporta y que el nuevo importa, siempre que el formato sea compatible. En la familia del manga y del anime esa compatibilidad existe desde hace años; en lectores nuevos fuera de la familia, a veces hay que usar un formato intermedio y reordenar categorías a mano.

Lo que no viaja: las descargas y los ajustes finos. Las descargas viven en una carpeta con el nombre del paquete de la app vieja; el lector nuevo no las ve y las vuelve a bajar si hace falta. Los ajustes de lector —tamaño de letra, dirección de lectura, filtros— se pueden exportar aparte en algunos motores y en otros hay que rehacerlos a mano.

Lo que se pierde: los historiales propios de cada extensión, como la marca de «visto» de una serie que no estaba en la biblioteca. Eso no se exporta en ninguna parte, porque pertenece al sitio y no al lector.

La consecuencia práctica es una regla que sirve para todo: antes de mudarse, exportar, copiar el archivo al correo o al almacenamiento, y no borrar la app vieja hasta comprobar que la biblioteca nueva abre con todos los títulos. Borrar primero es el único error que no tiene arreglo.

───────────────────

*📱 El teléfono viejo y el lector nuevo*

Una parte del público de estas herramientas tiene aparatos de 2018 y 2019, y ese dato cambia las recomendaciones. Un motor con funciones nuevas suele pedir una versión de Android más alta y más memoria; un fork conservador funciona donde el grande ya no arranca.

La señal que hay que mirar en la ficha de la release es el requisito de sistema. Está escrito en las notas o en el nombre del archivo, y se puede leer antes de instalar. AniZen, por ejemplo, con su ritmo de compilación alto, arrastra lo que arrastre su base; un fork que se separó hace dos años puede exigir menos, y también puede no arreglar nada de lo que se rompió este año.

Hay una tercera vía que casi nadie considera: quedarse quieto. Un teléfono de 2019 con un lector de 2024 que funciona, extensiones actualizadas y biblioteca respaldada es un aparato perfectamente útil. La novedad no es un valor por sí misma, y en un aparato lento, cada actualización del motor es una apuesta a que el rendimiento no empeore.

Lo que si conviene actualizar en un teléfono viejo es la extensión que se rompió, y solo esa. Es un cambio pequeño, se revierte y no toca la biblioteca.

───────────────────

*🧩 Qué hace buena a una extensión de anime*

Una extensión de anime tiene dos trabajos y por eso falla el doble. El primero es listar: encontrar la serie, los capítulos y sus nombres. El segundo es resolver el video, que es donde la mayoría de los problemas aparecen, porque los sitios cambian de reproductor, de dominio y de truco con más frecuencia que de diseño.

Una extensión bien hecha declara su versión, tiene un nombre que se puede buscar en el catálogo y no intenta nada raro fuera de su trabajo: no pide permisos, no abre anuncios propios y no guarda nada que no sea la dirección del video. Una extensión mal hecha puede hacer lo mismo y además pedir cosas que no necesita.

La comprobación que sirve es la del origen. Las extensiones llegan desde un catálogo y ese catálogo tiene repositorio público con fecha; si la extensión que tienes no está en ninguno de los catálogos vivos, vino de otro sitio y las preguntas cambian.

Cuando una serie no abre y otra sí, el problema es la extensión. Cuando ninguna abre, el problema es el motor o el catálogo. Cuando abre y se corta a los dos minutos, casi siempre es el sitio. Tres síntomas, tres culpables distintos, y saber cuál es ahorra la reinstalación inútil.

───────────────────

*⚖️ La ley, sin sermón*

Esta guía no reparte direcciones de contenido ni receta sitios. Lo que hace es contar de dónde salen los programas y con qué reglas se comportan, que es lo que se puede afirmar sin mentir.

Las licencias del censo son de código: Apache-2.0 en casi todos los motores de esta familia, que permite usar, modificar y redistribuir el programa siempre que se conserve el aviso y se diga qué se cambió. Eso cubre el software. No cubre lo que el software muestra, que tiene sus propias reglas y sus propios dueños.

La marca es otra cosa. El nombre de un lector y su logo no van con el código: un fork puede copiar la licencia y no puede usar el nombre para confundir. Cuando dos repositorios se llaman casi igual, la pregunta correcta no es cuál es el bueno sino cuál publica desde la cuenta original.

Y hay una regla de convivencia que no es legal y sí importa: nada de lo que hay aquí justifica instalar software de origen desconocido en el teléfono de otra persona. La casa prefiere el hueco confesado a la recomendación cómoda.

───────────────────

*🧨 Cuando el lector se cae en mitad del capítulo*

El síntoma es siempre el mismo: la app se cierra, o se queda en negro, o vuelve a la biblioteca sin decir nada. La causa puede estar en tres sitios y el orden de comprobación evita adivinar.

Primero el motor: ¿la app abrió al menos? Si abrió, arrancó el motor y el problema está más adentro. Si no abrió, se mira si el paquete se instaló con la firma correcta y si el teléfono tiene espacio.

Segundo la extensión: se prueba otra serie del mismo sitio y una serie del mismo nombre en otro sitio. Si la primera falla y la segunda funciona, la extensión de ese sitio está rota y hay que actualizarla o esperar. Si las dos fallan, el problema es más grande.

Tercero el sitio: se comprueba si el sitio responde en el navegador. Muchas «caídas» del lector son sitios caídos, dominios cambiados o bloqueos regionales, y el lector solo está informando con la única cara que sabe poner.

Cuando los tres están bien y aun así se cae, queda el registro de la app y el reporte al proyecto. Un reporte útil lleva tres cosas: la versión exacta del motor, la versión exacta de la extensión y lo que se estaba haciendo. Con eso el que mantiene puede reproducirlo; sin eso, el reporte se parece a todos los demás.

───────────────────
*🧭 Cuál te toca según lo que ya tengas*

Si vienes del tronco y todo te funciona, la respuesta honesta es no mudarte. El motor grande tiene ★7.866, licencia Apache-2.0 y una comunidad que escribió miles de extensiones; su última versión es de septiembre y mientras no aparezca un fallo que te toque, cambiar de casa es riesgo sin beneficio.

Si vienes del tronco y algo se rompió que el tronco no va a arreglar, el fork es la salida natural. Tadami es el que más empuja de la familia —29 y 30 de octubre, dos versiones en cuatro días— y su precio es la dispersión: dos repositorios, dos contadores y una comunidad que hay que seguir en el sitio correcto.

Si estás empezando y no tienes biblioteca, AniZen entra por los ojos: ★200, licencia clara, versión de ayer y un ritmo que hace pensar que el autor va a estar ahí el mes que viene. Su riesgo es el de todo proyecto de una sola persona: si se cansa, no hay relevo anunciado. Empezar por ahí está bien; poner la biblioteca entera sin respaldo, no.

Si lo que quieres es una sola app para anime y manga, Anikku es la única apuesta de esta lista que lo intenta con una casa grande detrás. Su versión es de septiembre, su contador está en 0.2 y su techo depende de que Komikku, con ★4.966 y empujón de hoy, siga su ritmo.

Si tu teléfono es de 2018 o 2019, la respuesta cambia otra vez: quédate en lo que arranca. Un lector que se abre en dos segundos vale más que uno con funciones que el aparato no puede mover.

───────────────────

*🗓️ Un calendario de revisión que cabe en el año*

Cuatro fechas y no más, porque un calendario que no se cumple no sirve de nada. Estas cuatro caben en cualquier agenda y cubren el 90% de lo que se rompe.

**La primera semana de cada mes:** abrir el catálogo de extensiones y actualizar. Es la operación más barata del año y evita la mitad de los «no abre».

**Al cambiar de estación:** exportar el respaldo de la biblioteca y guardarlo fuera del teléfono. Dos minutos, y es el único seguro contra la mudanza mal hecha.

**Una vez al año, en la fecha que sea fácil de recordar:** revisar si el motor que usas sigue publicando. No hace falta leer el código: la pestaña de versiones y la fecha del empujón bastan, y si las dos llevan más de un año quietas, es el momento de mirar la fila.

**Cuando algo se rompa y no se arregle en una semana:** ese es el día de mirar los forks, no antes. Mudarse por curiosidad se paga en tardes; mudarse por necesidad se paga con un respaldo y una hora.

Con esas cuatro, la conversación deja de ser «¿cuál es el mejor lector?» y pasa a ser «¿cuándo revisé esto por última vez?», que es una pregunta que sí tiene respuesta.

───────────────────

*💬 Las frases que se repiten*

«Es que ese lector está muerto». Casi nunca lo está: está quieto. Muerto es cuando el paquete ya no instala y las extensiones ya no cargan.

«Me bajé el bueno, el de las pruebas». El canal de pruebas no es el bueno ni el malo: es el que cambia cada semana. Si te gusta probar, es tu sitio; si quieres que el teléfono abra siempre, no.

«Perdí todo al actualizar». Casi siempre: firmas distintas o un borrado previo. Las dos se evitan con lo mismo, que es el respaldo.

«Ese fork es igual, pero mejor». Casi siempre es el mismo código con dos funciones más y una versión menos probada.

«No entiendo por qué hay tantos». Porque el tronco se quedó quieto y cada grupo con una necesidad distinta abrió su puerta. Es más fácil de entender así que como una guerra de proyectos.

───────────────────

*📺 El video y sus tres finales*

En un lector de manga el final del camino es una imagen. En uno de anime el final es un reproductor, y ahí se juntan tres aparatos distintos: el contenedor que trae el capítulo, el reproductor del sistema y el decodificador del teléfono. Cualquiera de los tres puede negarse, y cada negativa tiene su cara.

*La primera negativa es el formato.* Un capítulo en un contenedor que el reproductor del sistema no reconoce se queda en negro con sonido, o al revés. La prueba es llevar el mismo archivo a un reproductor de escritorio: si ahí se ve, el problema es el reproductor del teléfono y no la extensión.

*La segunda es la pista.* Los capítulos modernos suelen traer audio en dos idiomas y subtítulos en tres. Un teléfono que no encuentra la pista correcta muestra el video mudo o con subtítulos que no corresponden. Casi siempre se arregla cambiando de pista a mano y recordando la elección.

*La tercera es la memoria.* Un teléfono de 2019 con tres gigas reproduciendo un capítulo en calidad alta se queda sin margen y el sistema cierra la app sin pedir permiso. Bajar la calidad en el ajuste del lector arregla lo que ninguna actualización arregla.

Hay una cuarta negativa que no es del aparato: el enlace del video caduca. Media hora después de listarlo, el servidor del sitio lo invalida y el lector devuelve un error que parece del reproductor. Volver a la lista de capítulos y abrir otra vez suele resolverlo, y es la razón por la que «se cae cada dos capítulos» casi nunca es un fallo del proyecto.

La consecuencia para quien elige lector: preguntar por reproductor integrado o externo no es un detalle de preferencia. Un lector que deja el video al reproductor del sistema es más frágil en formatos raros y más fácil de diagnosticar; uno con reproductor propio controla la experiencia y hereda todos los fallos del suyo.

───────────────────

*🧱 Lo que no se ve: la biblioteca y sus carpetas*

La biblioteca de un lector de anime parece una lista y por dentro son tres carpetas distintas. Entenderlas es lo que separa a quien se muda en una hora de quien pierde una tarde.

*La primera es la base de datos.* Ahí viven los títulos, las categorías, el progreso y las fechas. Es pequeña, se exporta en un archivo y es la que hay que salvar antes de cualquier cambio.

*La segunda es la de descargas.* Cada capítulo es un archivo pesado guardado con el nombre del paquete de la app que lo bajó. No se exporta con la base y no la ve el lector nuevo. Si el teléfono tiene poco espacio, esas carpetas son también la mitad del problema de almacenamiento.

*La tercera es la de caché.* Portadas, miniaturas y fragmentos de video. Se puede borrar sin miedo y se vuelve a llenar sola; es la primera que hay que limpiar cuando el teléfono se pone lento.

Con esas tres separadas, el mantenimiento se vuelve obvio: la base se respalda, las descargas se administran y la caché se borra cuando estorba. Y el diagnóstico también: un lector que abre lento con veinte gigas de caché no está mal hecho, está sucio.

Hay un cuarto archivo que casi nadie mira y que conviene conocer: el de registro. Cuando algo falla sin mensaje claro, el registro dice qué estaba pidiendo el lector en el momento del fallo. Copiar ese texto es lo que convierte un «no funciona» en un reporte que alguien puede usar.

───────────────────

*🤝 El que escribe extensiones*

Detrás de cada extensión de anime hay alguien que leyó una página y escribió la manera de leerla. Ese trabajo no lo ve nadie mientras funciona y lo ve todo el mundo cuando se rompe.

Escribir una extensión nueva empieza por entender el formato del motor al que va: cómo se declara el nombre, cómo se piden los capítulos, cómo se resuelve el video. La familia del anime heredó ese formato del manga, y por eso muchas extensiones de manga se parecen tanto a las de anime en su primera versión.

Lo difícil no es la primera versión: es el mantenimiento. Un sitio de anime cambia de reproductor tres veces al año y de dominio dos; cada cambio es una tarde de trabajo no pagado. Los catálogos viven de esas tardes, y por eso la salud de un catálogo se mide mejor por su número de contribuidores que por su número de extensiones.

Si alguien quiere ayudar y no programa, hay dos cosas que sirven y no requieren código: reportar con detalle la extensión y el síntoma exacto, y probar los arreglos cuando el que mantiene pide confirmación. Un reporte bueno vale más que diez «no me funciona».

Para quien sí programa, la recomendación de la casa es empezar por arreglar una extensión rota antes que escribir una nueva. Arreglar enseña el formato, el estilo del proyecto y el ritmo de publicación, y deja al ecosistema mejor de como estaba.

───────────────────

*🎯 El caso del capítulo doce*

Una serie, un capítulo que no aparece, y once que sí. Es el caso más común y el que mejor enseña a diagnosticar.

Si los once primeros están y el doce no, la extensión no está rota: el sitio no lo ha publicado, o lo publicó con un nombre que la extensión no reconoce, o lo publicó en una temporada que la extensión lista aparte. Se comprueba en el navegador en treinta segundos y se acaba la duda.

Si el doce aparece y al abrirlo vuelve a la lista, el problema es el video y no el listado: el enlace caducó, el servidor cambió o la calidad pedida no está disponible. Cambiar de servidor en el mismo capítulo resuelve la mitad de los casos.

Si el doce aparece, se abre y se corta a la mitad, es memoria o red. Memoria cuando pasa siempre en la misma marca, red cuando pasa en momentos distintos del mismo capítulo.

Y si el doce aparece dos veces con nombres casi iguales, el sitio está republicando: la extensión lista lo que hay. Ahí no hay nada que arreglar y sí algo que entender, porque la culpa no es del lector.

Cuatro síntomas del mismo capítulo, cuatro culpables distintos. La costumbre de probarlo en el navegador antes de tocar el lector es lo que convierte una tarde de reinstalaciones en dos minutos de mirada.

───────────────────

*🧾 Lo que costó medir esto*

Lo primero que costó fue el nombre: tres repositorios contienen la palabra del lector en su dirección y solo uno es el proyecto que publica. Lo segundo, la licencia: uno de los repositorios de la familia no declara ninguna, y esa casilla vacía se publica como vacía en vez de rellenarla con la del padre.

Lo tercero fue el tiempo. Las versiones se piden una por una y algunas tardan; las que no tienen ninguna devuelven un mensaje que hay que distinguir de un error de red. Ese mensaje se anota como «sin versión publicada», que es un dato, y no como «no se pudo leer», que sería otro.

Lo cuarto fue la tentación. Con nueve proyectos y una tabla por delante, lo fácil es escribir solo los que tienen estrellas y dejar los ceros fuera. Aquí están los dos ceros, el de las nueve estrellas y el de las sesenta y una, porque un censo que solo cuenta a los grandes termina dibujando un ecosistema que no existe.

───────────────────

*❓ Preguntas que me hacen*

**¿AniZen es el mismo proyecto que el motor grande del anime?** No. Es un lector propio, con su repositorio y su licencia, y su única relación con la familia es la raíz común de cómo se conectan las extensiones.

**¿AniZen es seguro?** Es Apache-2.0, tiene el código público y publica desde su cuenta; eso es lo que se puede verificar. Lo que no se puede verificar desde fuera es lo que hace en tu teléfono, y por eso existe el paso de la firma y el del respaldo.

**¿Por qué la versión se llama v0.5.220 y no v1?** Porque el autor no ha decidido que esté maduro. El cero delante no es un defecto: es una promesa de que la interfaz todavía puede cambiar.

**¿Vale la pena instalar el canal de pruebas?** Solo si tu teléfono de pruebas no es el teléfono de todos los días y te gusta reportar fallos con detalle.

**¿Puedo tener dos lectores a la vez?** Sí, y es la forma más sana de probar. Los dos comparten biblioteca solo si importas el mismo respaldo, y conviene no hacerlo hasta estar decidido.

**¿Qué pasa con mis descargas si cambio de lector?** Se quedan donde estaban y el lector nuevo no las ve. Si el espacio importa, hay que borrarlas a mano antes de mudarse.

**¿Anikku lee también manga?** Es la intención con la que nace: un lector de anime de la casa de Komikku, con la idea de compartir estantería. Su versión v0.2.0 y su empujón del 22 de octubre dicen que la idea está en marcha, no terminada.

**¿Por qué los forks tienen números tan distintos del tronco?** Porque cada uno lleva su propio contador desde el día que se separó. Las cifras no se comparan entre sí: se leen como la historia de cada casa.

**¿Mihon lee anime?** No. Está en el censo porque es la vara de comparación del manga: ★24.939, versión del 25 de octubre. Cuando alguien dice que un fork de anime «va bien», se mide contra esto.

**¿Qué hago con un lector que lleva un año sin versión?** Nada mientras funcione. El día que falle algo y no haya arreglo, se mira la fila con el respaldo ya exportado.

───────────────────

*📊 Tabla, mitos y glosario*

*Los nueve medidos, en una línea*

| Repositorio | Qué es | Licencia | Empujón | Estrellas |
|---|---|---|---|---|
| AniZen | lector de anime con ritmo alto | Apache-2.0 | 31-oct | ★200 |
| anizen-preview | canal de pruebas de AniZen | sin licencia | 31-oct | ★9 |
| Anikku | anime de la casa de Komikku | Apache-2.0 | 22-oct | ★1.127 |
| Komikku | motor de manga de esa casa | Apache-2.0 | hoy | ★4.966 |
| Aniyomi | el tronco del anime | Apache-2.0 | 14-sep | ★7.866 |
| Tadami (fork) | fork con casa propia | Apache-2.0 | 29-oct | ★287 |
| tadami (org) | la casa nueva del fork | sin licencia | 30-oct | ★61 |
| Yokai-T | intento sin público | Apache-2.0 | 26-sep | ★0 |
| Mihon | la vara del manga | Apache-2.0 | 26-oct | ★24.939 |

*Cinco mitos de la fila*

**Mito uno: «más estrellas, más vivo».** Mihon tiene ★24.939 y publicó el 25 de octubre; AniZen tiene ★200 y publicó el 31. La estrella mide cuánta gente miró, no cuándo alguien arregló algo.

**Mito dos: «un fork es una copia».** Un fork con casa propia es otro proyecto: otro contador, otras decisiones y otras manos. Tadami lo demuestra con dos repositorios y dos versiones en cuatro días.

**Mito tres: «si no hay versión, está abandonado».** Komikku empujó hoy con su última versión en julio. El código y el paquete son dos relojes distintos.

**Mito cuatro: «todos los lectores de anime son lo mismo».** Comparten la forma de conectar extensiones y no comparten la biblioteca, los ajustes ni las descargas. Mudarse tiene costo.

**Mito cinco: «el que tiene el número más alto es el más estable».** Un contador alto suele querer decir compilaciones frecuentes, y compilaciones frecuentes es lo contrario de estabilidad.

*Glosario de la fila*

**Tronco** — el motor del que salieron los demás, siga vivo o quieto.

**Fork** — copia que tomó su propio camino y su propio contador.

**Canal de pruebas** — repositorio separado donde se publica lo que todavía no se ha probado.

**Release** — paquete publicado, con número y fecha.

**Empujón** — último cambio de código visible en el repositorio.

**Respaldo** — archivo con la biblioteca y el progreso, exportado a mano.

**Contador de versión** — número que crece con cada compilación, no con cada avance.

───────────────────

*🔗 Enlaces*

Cada dirección se abrió esta tarde; ninguna viene de una lista guardada.

- AniZen: https://github.com/salmanbappi/AniZen
- El canal de pruebas de AniZen: https://github.com/salmanbappi/anizen-preview
- Anikku: https://github.com/komikku-app/anikku
- Komikku: https://github.com/komikku-app/komikku
- Aniyomi, el tronco: https://github.com/aniyomiorg/aniyomi
- Tadami, el fork: https://github.com/andarcanum/Tadami-Aniyomi-fork
- La casa nueva de Tadami: https://github.com/tadamiorg/tadami
- Yokai-T: https://github.com/KakarottoCake/yokai-T
- Mihon, la vara del manga: https://github.com/mihonapp/mihon

*Lo que quedó fuera.* El repositorio *Gaijin81/anizen* no tiene README legible en ninguna rama, así que no hay licencia, versión ni presentación que publicar. Se nombra el hueco y no se inventa la ficha.

*Cómo se midió.* Nueve proyectos leídos tres veces cada uno y por tres caminos distintos: la búsqueda de la forja, la página del repositorio y el archivo crudo del README. El orden de los tres caminos se rotó de un proyecto al siguiente, y las versiones se pidieron aparte, una por una, para no confundir el paquete con el código.

───────────────────

*🌅 Cierre — el que cuenta los empujones*

El anime en el teléfono no tiene hoy un dueño claro, y ese es el dato. Tiene un tronco de ★7.866 que publicó en septiembre, un fork de ★287 que publicó dos veces en cuatro días, un lector de ★200 que sacó una versión ayer y una casa nueva de ★61 que empuja mientras discute consigo misma en dos repositorios.

Lo que sí tiene dueño es la manera de mirarlo: dos fechas por proyecto, licencia a la vista y respaldo antes de tocar. Con eso, la pregunta deja de ser cuál es el mejor y pasa a ser cuál está trabajando hoy, que se contesta en treinta segundos.

> —¿Y si el que estoy usando se queda quieto?
> —Se queda quieto, no se muere. Y el día que se muera, ya tienes el respaldo en el correo.

💓 *La Bandita informa a partir de fuentes fechadas.* Un lector vivo se mide por la fecha de su paquete, no por el número de sus estrellas.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 17:24 y las 17:31 de Santo Domingo · nueve repositorios medidos con el orden de las tres lecturas rotado · las versiones se consultaron por separado y se anotó su fecha, no solo su número.

*Licencia de esta entrega:* el texto va en CC BY-SA 4.0, los datos medidos en CC BY 4.0 y el código de ejemplo en MIT; el nombre de la casa y la marca quedan reservados a «Alexis (La Bandita)».

## 🗒️ Notas al pie

**Nota de corte (1-nov):** estrellas, licencia, lenguaje y empujón son de la misma hora; las versiones se anotaron con su fecha de publicación y, cuando no había ninguna, se dejó escrito que no había, y ninguna fecha se completó por cálculo.

**Nota de hueco (1-nov):** un repositorio con el mismo nombre del lector no tiene README legible y se quedó fuera de la tabla. Un proyecto con ★0 entró en la tabla para que el censo no parezca más grande de lo que es.

**Nota de alcance (1-nov):** la pieza no recomienda sitios ni extensiones de contenido; cuenta de dónde salen los programas, con qué licencia y con qué fecha.

**Nota de corrección (1-nov):** la versión anterior de esta pieza se apoyaba en un incidente del 15 de septiembre y en números de ese día. Se reescribió con la fila completa medida esta tarde y se quitó el episodio, que ya no informa de nada nuevo.
