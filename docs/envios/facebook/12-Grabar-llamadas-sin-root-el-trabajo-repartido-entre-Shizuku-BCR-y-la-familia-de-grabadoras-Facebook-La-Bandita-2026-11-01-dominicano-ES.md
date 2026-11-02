# PIEZA 12 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/12-Grabar-llamadas-sin-root-el-trabajo-repartido-entre-Shizuku-BCR-y-la-familia-de-grabadoras-Facebook-La-Bandita-2026-11-01-dominicano-ES.md`
- **Fecha de la pieza:** 1-nov-2026 (según dateline; edad hoy: 1 días)
- **sha256 de la pieza:** `5988df07458924ab210b5c66588f46a5b9014819e7da0a074f5f170becb5cb76`
- **Envío generado:** 2026-11-02 · 16 mensajes · el mayor de 3657 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 16 · 996 caracteres ═══

*Grabar llamadas sin root: el trabajo repartido entre Shizuku, BCR y la familia de grabadoras*

La Bandita · pieza 12 · guía del 1-nov-2026 · te la mando hoy en 16 mensajes.

Antes de mandártela volví a medir lo que afirma: *8 repositorios, 8 vivos*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: GPL-3.0 5 · MIT 1 · NOASSERTION 1 · Apache-2.0 1.

⚠️ *Aviso de fecha:* este texto se escribió el 1-nov-2026. Todo lo que dice «hoy» dentro se refiere a ese día, no a este. La medición de hoy va al final, firmada y con su fecha.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/12-Grabar-llamadas-sin-root-el-trabajo-repartido-entre-Shizuku-BCR-y-la-familia-de-grabadoras-Facebook-La-Bandita-2026-11-01-dominicano-ES.md

💓 2 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 16 · 2368 caracteres ═══

[Texto del 1-nov-2026: cuando dice «hoy», es ese día. La medición de hoy está al final.]

*Grabar llamadas sin root: el trabajo repartido entre Shizuku, BCR y la familia de grabadoras*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 12 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🎙️ Por qué grabar una llamada es difícil en Android
├── 🧰 Las tres familias que se reparten el trabajo
├── 🎬 Cuatro escenas y el censo de esta tarde
├── 🔌 Shizuku: la llave que se presta
├── 🖥️ La mitad de escritorio
├── 🧨 Cuando la grabación sale muda
├── 🎧 El archivo, el espacio y la batería
├── ⚖️ La ley, el consentimiento y los aparatos que no dejan
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas al pie
```

*⚡ En una página*

Grabar una llamada en Android dejó de ser una función del teléfono y pasó a ser un trabajo de fontanería: alguien tiene que conseguir que el sistema entregue el audio de las dos partes, y el sistema no lo entrega por gusto. Hay tres maneras de conseguirlo y esta tarde las tres están vivas: un módulo de sistema para aparatos con root, una app que usa el permiso de depuración prestado por Shizuku y un par de apps que se apoyan en las API de accesibilidad y de captura de audio.

El censo de hoy da una foto curiosa. El módulo de sistema, *BCR*, tiene ★2.958, licencia GPL-3.0 y versión v3.11 del 15 de octubre. La app que funciona con Shizuku, *ShizuCallRecorder*, tiene ★1.970, GPL-3.0 y versión v2.0.0 del 24 de octubre. Las dos nuevas que aparecieron este año, *AVault* y *CallVault*, empujaron las dos el 1 de noviembre, publicaron el 31 de octubre y suman entre las dos ★629. Y detrás de todas, *Shizuku* con ★32.594, Apache-2.0 y su último empujón en junio de 2025.

La lección que sale de ahí no es «instala la que más estrellas tiene». Es que la grabación sin root vive de una llave que se presta, y esa llave tiene su propio mantenimiento, su propia fecha y su propio riesgo. Quien quiera grabar sus llamadas debería entender primero qué permiso está pidiendo y por qué el sistema lo niega por defecto.

Si te llevas una idea: en Android moderno, grabar las dos partes de una llamada es posible y no es gratis. Se paga con un permiso, con una app que lo administre y con la obligación de avisar a quien está al otro lado.

⏬ sigue abajo · parte 1 de 15

═══ MENSAJE 3 de 16 · 3546 caracteres ═══

*🎙️ Por qué grabar una llamada es difícil en Android*

Cuando suena una llamada, el audio no pasa por el mismo sitio que la música. El sistema lo enruta por un camino protegido, y las apps normales no pueden leerlo: si pudieran, cualquier aplicación del teléfono podría escuchar conversaciones ajenas sin pedir permiso. Esa protección es una buena noticia disfrazada de obstáculo.

Históricamente hubo dos formas de saltarla. La primera era una API oficial de grabación que muchos fabricantes incluyeron y que Google fue retirando versión tras versión, hasta dejarla inservible en casi todo lo que se vendió después de 2021. La segunda era root: con permisos de administrador se puede leer el flujo de audio y guardarlo, y de ahí viven las grabadoras de la vieja escuela.

Con la API cerrada y el root cada vez menos común, quedaron tres huecos. El primero, aprovechar que el audio se puede capturar si la llamada va por altavoz: funciona, baja la calidad y obliga a gritar. El segundo, usar las API de accesibilidad para leer y manipular la interfaz del teléfono, que es lo que hacen algunas grabadoras modernas para activarse y para ganar tiempo. El tercero, pedir prestado el permiso de depuración con Shizuku, que es el que da acceso a las funciones de sistema que normalmente exigen root sin rootear el teléfono.

Ninguno de los tres es magia. Los tres dependen de algo que el usuario concede, y en los tres el día que el sistema cierre esa puerta, la app se queda sin trabajo.

Hay un cuarto factor que casi nadie considera: la llamada por internet. Cuando la conversación va por datos en vez de por la red telefónica, el audio sale por el altavoz del sistema y la captura cambia de reglas, a veces a favor y a veces en contra. Por eso hay teléfonos donde la grabadora funciona con la llamada normal y falla con la de la aplicación de mensajería.

*🧰 Las tres familias que se reparten el trabajo*

*La familia del módulo de sistema.* Aquí está BCR, Basic Call Recorder: un módulo que se instala en un aparato con root y que se engancha al sistema mucho antes de que las apps existan. Graba sin app visible, guarda en una carpeta y su ajuste vive en una app pequeña. Su ventaja es la calidad y la estabilidad; su precio es el root, con todo lo que eso implica para las apps que se niegan a abrir en aparatos modificados.

*La familia del permiso prestado.* ShizuCallRecorder es su mejor ejemplo: no necesita root, necesita Shizuku, que se arranca una vez por reinicio y presta el permiso de depuración. Con eso la app consigue lo que el sistema no le da a una app común. Su ventaja es enorme —cero modificaciones al sistema— y su precio es una ceremonia: cada vez que el teléfono arranca hay que volver a activar Shizuku, y algunas apps del sistema no se dejan manejar por ahí.

*La familia de las API de accesibilidad.* AVault y CallVault se presentan como grabadoras sin root y sin PC, apoyadas en lo que el sistema permite a una app con accesibilidad y captura de audio. Su ventaja es no depender de nada externo; su límite es que la calidad y la fiabilidad dependen del aparato, y ahí es donde las opiniones se dividen. Las dos empujaron el 1 de noviembre y publicaron versión el 31 de octubre: son las más nuevas del censo y las que menos historial tienen.

Las tres familias conviven y no compiten del todo. Un aparato con root usa BCR y no necesita nada más; uno sin root usa ShizuCallRecorder o una de las nuevas; y quien graba en el escritorio usa bcr-gui para escuchar lo que BCR dejó en el teléfono.

⏬ sigue abajo · parte 2 de 15

═══ MENSAJE 4 de 16 · 3534 caracteres ═══

*🎬 Cuatro escenas de teléfono*

*El que graba por trabajo.* Recibe llamadas de clientes y necesitaba volver a escuchar lo pactado. Tenía un teléfono con root y usaba BCR desde hacía dos años: la grabación se hacía sola, sin abrir nada, y cada archivo llevaba número y hora. Su problema no era técnico: era que nunca avisó que grababa. Cuando un cliente lo supo, la confianza se rompió más que por la grabación, por el silencio.

*La que no quería rootear.* Le daba miedo modificar el arranque de un teléfono que usa para el banco. ShizuCallRecorder le resolvió el caso con una condición: cada reinicio, abrir Shizuku y darle el permiso. Lo convirtió en costumbre de la mañana, como cargar el teléfono, y en tres meses solo falló una vez, el día que reinició en el trabajo y olvidó activarlo.

*El que probó la nueva y volvió.* Instaló CallVault el día que salió su versión, grabó dos llamadas y notó que una salió con su voz muy baja. Volvió a la que tenía, no porque la nueva fuera mala, sino porque su teléfono es de los que no entregan bien el audio del otro lado. La conclusión que sacó es la que vale: en grabación, el aparato manda.

*La que guarda todo en el teléfono.* Tenía ocho gigas de grabaciones de dos años, sin nombre y sin orden. Lo que le cambió el juego no fue una app nueva: fue una regla de tres pasos con bcr-gui, que lee la carpeta del teléfono desde la computadora, ordena por fecha y permite borrar sin miedo lo que ya no necesita.

*🧾 El censo de esta tarde*

*BCR*, el módulo de sistema: ★2.958, GPL-3.0, Kotlin, empujón del 15 de octubre y versión v3.11 del mismo día. Es el estándar de facto de la grabación con root y su ritmo es tranquilo: una versión cada pocos meses, sin sobresaltos.

*ShizuCallRecorder*, la app del permiso prestado: ★1.970, GPL-3.0, Kotlin, empujón del 30 de octubre y versión v2.0.0 del 24. Su v2 indica un cambio de fondo, no un retoque: conviene leer la nota de la release antes de actualizar, sobre todo si la versión anterior funcionaba.

*AVault*, la nueva con cifrado: ★445, licencia que la ficha de la forja no reconoce y que su README declara MIT, Kotlin, empujón del 1 de noviembre y versión v2.0.0 del 31 de octubre. Se presenta como grabadora sin root con cifrado por hardware; las dos licencias se publican porque las dos existen.

*CallVault*, la otra nueva: ★184, GPL-3.0 en la ficha y Apache-2.0 en su README, Kotlin, empujón del 1 de noviembre y versión v2.4.8 del 31 de octubre. Su descripción promete grabar los dos lados sin root ni PC, que es exactamente la promesa que hay que probar en el aparato de uno.

*bcr-gui*, la mitad de escritorio: ★381, GPL-3.0, TypeScript, empujón del 26 de octubre y versión v1.16.0 del 25. No graba nada: lee, ordena y reproduce lo que BCR dejó, y su utilidad crece con el número de archivos.

*Shizuku*, la llave: ★32.594, Apache-2.0, Kotlin, empujón del 18 de junio de 2025 y versión v13.6.0 del 25 de mayo de 2025. Lleva más de un año sin moverse y sigue siendo la pieza de la que dependen varias apps sin root; su estabilidad es su mejor argumento.

*Benojir/Android-Call-Recorder*, el clásico pequeño: ★54, GPL-3.0, Java, empujón del 25 de octubre, sin versión publicada. Graba en aparatos con root y sirve de recordatorio de que este ecosistema tiene piezas minúsculas y activas.

*aykuttasil/CallRecorder*, el dormido: ★791, MIT, Kotlin, último empujón del 18 de octubre de 2023. Tres años sin tocar y sigue teniendo más estrellas que las dos nuevas juntas: la estrella es memoria, no salud.

⏬ sigue abajo · parte 3 de 15

═══ MENSAJE 5 de 16 · 2768 caracteres ═══

*🔌 Shizuku: la llave que se presta*

Shizuku no graba llamadas. Lo que hace es arrancar un servicio con el permiso de depuración del sistema —el mismo que se activa para conectar el teléfono a una computadora— y prestarlo a las apps que saben pedírselo. Con ese permiso, una app puede hacer cosas que el sistema solo permite a root.

Su cifra lo dice todo: ★32.594, Apache-2.0, último empujón del 18 de junio de 2025 y versión v13.6.0 del 25 de mayo de 2025. Un proyecto parado hace más de un año y convertido en infraestructura. Eso es posible porque lo que expone es una API del propio sistema, y mientras esa API exista, la llave sirve.

La ceremonia importa más de lo que parece. Al reiniciar el teléfono el servicio muere, y hay que volver a arrancarlo con una computadora, con la depuración inalámbrica o con una app que lo haga sola. Quien no tiene computadora cerca depende de la depuración inalámbrica, que en algunos aparatos hay que volver a emparejar después de cada reinicio.

Y hay un límite que se descubre tarde: algunas apps del sistema se niegan a operar bajo el permiso de Shizuku, porque comprueban el contexto en el que corren. La grabadora puede funcionar y el lector de notificaciones no, o al revés, y no hay ajuste que lo arregle.

Por eso la pregunta correcta no es «¿Shizuku es seguro?» sino «¿qué apps tengo prestando ese permiso?». La respuesta se ve en la propia app de Shizuku: una lista corta, y cada nombre debería ser una decisión recordada y no un resto de instalación.

*🖥️ La mitad de escritorio*

Hay una pieza del ecosistema que casi nunca se menciona y que arregla el problema más común de todos: escuchar lo grabado. bcr-gui tiene ★381, GPL-3.0, está escrito en TypeScript, empujó el 26 de octubre y publicó v1.16.0 el 25. No es una grabadora: es la ventana desde la computadora a la carpeta que BCR llenó de noche.

Su utilidad real aparece cuando el teléfono acumula cientos de archivos. Lo que hace es leer la carpeta, ordenar por fecha y por contacto, reproducir con nombre y permitir borrar con criterio. En un teléfono con ocho gigas de grabaciones viejas, esa ventana convierte una tarea imposible en una tarde de domingo.

Tiene además un efecto secundario que vale la pena: la copia. Las grabaciones que solo existen en el teléfono se pierden el día que el teléfono se cae. Un programa de escritorio que lee la carpeta invita a copiarla, y la copia es lo único que hace que una grabación sirva de algo dos años después.

El límite es obvio: asume que usas BCR y que conectas el teléfono. Para las otras familias —ShizuCallRecorder, AVault, CallVault— cada app guarda en su carpeta y no hay ventana de escritorio; la copia se hace a mano, con el cable o con una sincronización cualquiera.

⏬ sigue abajo · parte 4 de 15

═══ MENSAJE 6 de 16 · 3107 caracteres ═══

*🧨 Cuando la grabación sale muda*

El fracaso más frustrante de esta categoría no es un error: es un archivo con cinco minutos de silencio. La app dijo que grabó, el archivo existe, pesa lo que debe, y al escucharlo solo está tu voz o nada. Hay cuatro causas y se comprueban en un orden fijo.

**La primera es la ruta de audio.** Algunos aparatos entregan a la app solo el micrófono y nunca el flujo de la llamada. La comprobación es sencilla: graba una llamada hablando tú y verifica si tu voz se oye. Si tu voz está y la otra no, la ruta está negada y no hay ajuste de la app que lo arregle.

**La segunda es el altavoz.** Varias grabadoras capturan bien solo cuando la llamada va por altavoz, porque el sistema entonces deja el audio sonar hacia fuera. Quien graba en privado con el teléfono en la oreja descubre que el archivo está vacío del otro lado.

**La tercera es el momento del permiso.** Con Shizuku, si el servicio murió tras un reinicio, la app arranca igual y graba sin los permisos que necesita. El resultado es un archivo mudo con toda la apariencia de estar bien.

**La cuarta es el códec.** Un archivo en un formato que el reproductor del teléfono no entiende suena a mudo sin serlo. Cambiar el formato de salida a uno común resuelve el diagnóstico en un minuto.

La regla que se desprende es incómoda y cierta: hay que probar la grabadora con una llamada de prueba antes de confiar en ella para algo que importe. Y esa prueba incluye escuchar el archivo, no solo verlo en la lista.

*🎧 El archivo, el espacio y la batería*

Una hora de llamada comprimida en un formato razonable ocupa entre veinte y sesenta megas según la calidad. Con eso se puede hacer la cuenta que casi nadie hace: quien habla dos horas al día por trabajo junta entre cuarenta y setenta gigas al año, y eso en un teléfono de 128 gigas es un tercio del almacenamiento.

De ahí salen tres costumbres que ahorran disgustos. La primera, fijar una calidad media y no la máxima: la diferencia para escuchar una voz no se nota y el espacio se reduce a la mitad. La segunda, una regla de retención: las grabaciones de trabajo se guardan tres meses y las personales se borran al mes, o al revés, pero se decide una vez. La tercera, sacar las grabaciones del teléfono en un día fijo del mes, porque el teléfono es un mal archivo.

La batería es el otro costo. Grabar en segundo plano con un servicio permanente consume poco durante la llamada —la pantalla está apagada y la red ya está en uso— pero el servicio en sí mantiene el aparato despierto. Los teléfonos con ahorro de energía agresivo matan ese servicio a la media hora, y esa es la causa de las grabaciones que se cortan solas.

El cifrado es la tercera pieza y la que menos se mira. AVault lo anuncia como cifrado por hardware, que en la práctica significa que los archivos quedan protegidos por la clave del aparato. Suena bien y tiene una consecuencia que hay que saber: si el teléfono se pierde, los archivos se van con él, y sin respaldo no hay manera de recuperarlos. Un archivo cifrado sin copia no es un archivo: es una promesa.

⏬ sigue abajo · parte 5 de 15

═══ MENSAJE 7 de 16 · 3657 caracteres ═══

*⚖️ La ley y el consentimiento*

Esta guía no da consejo jurídico y sí una regla de convivencia que vale en casi todas partes: avisa. La grabación de una conversación en la que participas tiene tratamientos distintos según el país; en unos basta con que una parte lo sepa —tú—, en otros se exige el consentimiento de todos, y en muchos el uso de la grabación posterior tiene reglas propias aunque la grabación fuera legal.

Lo que cambia de verdad la práctica no es la ley, es el momento del aviso. Avisar al inicio convierte una grabación en un acuerdo; avisar después la convierte en una prueba incómoda. Y hay un tercer caso peor: no avisar nunca y que la otra persona lo descubra, que es la única situación donde la grabación puede costarte más de lo que te da.

Hay dos contextos donde la regla se tensa. El primero es el trabajo con clientes: muchas empresas prohíben grabar sin autorización escrita, y el teléfono de la empresa es de la empresa. El segundo es la familia: la grabación de una discusión doméstica puede ser un instrumento legítimo de defensa y también una bomba de tiempo, y ninguna app resuelve ese juicio.

La consecuencia práctica es una sola: la grabadora es una herramienta, la decisión de usarla es de quien la tiene en la mano. Y esa decisión se toma mejor con la otra persona enterada que sin ella.

*🛠️ Instalar y comprobar en seis pasos*

**Paso uno: saber si tu teléfono tiene root.** Casi siempre se sabe; quien no lo sabe, no lo tiene. Si tiene root, la familia del módulo de sistema es la que mejor calidad da y la que menos ceremonia exige después.

**Paso dos: elegir la familia.** Root: BCR. Sin root y con computadora cerca de vez en cuando: ShizuCallRecorder con Shizuku. Sin root, sin computadora y con ganas de probar: AVault o CallVault, sabiendo que la calidad depende del aparato.

**Paso tres: dar solo los permisos que la app pide y entender para qué.** Micrófono, almacenamiento y, si es el caso, el permiso de depuración por Shizuku. Un permiso de accesibilidad en una grabadora se concede solo si su función lo explica.

**Paso cuatro: una llamada de prueba real.** No una nota de voz: una llamada, de dos minutos, con alguien que sepa que estás probando. Después se escucha el archivo entero.

**Paso cinco: la ruta de los archivos.** Anotar dónde guarda, con qué nombre y en qué formato. Sin ese dato, la copia mensual no existe.

**Paso seis: decidir la retención.** Cuánto tiempo se guarda, quién lo escucha y cuándo se borra. Seis pasos, media hora, y la grabadora deja de ser una promesa y pasa a ser una herramienta.

*🧭 Cómo se elige, en tres preguntas*

La primera pregunta es por el aparato: ¿tiene root? Con root, BCR y su ventana de escritorio; sin root, las familias del permiso prestado y de las API modernas.

La segunda pregunta es por la molestia que se tolera. ShizuCallRecorder es la más fiable sin root y la que más ceremonia tiene: cada reinicio, activar Shizuku. Las dos nuevas prometen menos ceremonia y menos historial; a cambio, la configuración fina suele ser más corta y la resolución de problemas, más solitaria.

La tercera pregunta es por las consecuencias: si la grabación se va a usar para algo importante, el camino es el aparato con la mejor ruta de audio y el respaldo probado, aunque sea más incómodo. Si es para acordarse de lo que se pactó, casi cualquier opción que funcione tres veces seguidas sirve.

Y una pregunta de cierre que no es técnica: ¿qué pasa si esta grabación se filtra? Si la respuesta da miedo, el problema no es la app, es el archivo, y el cifrado sin copia o la copia sin cifrado son las dos únicas opciones honestas.

⏬ sigue abajo · parte 6 de 15

═══ MENSAJE 8 de 16 · 3240 caracteres ═══

*🗃️ Un archivo de grabaciones que sirva dentro de dos años*

La grabación sin orden no vale nada. El día que hace falta, uno recuerda que habló con alguien en marzo y no recuerda ni la fecha ni el nombre del archivo. Un esquema mínimo lo resuelve.

El nombre del archivo debería llevar tres cosas: fecha en formato que ordene solo, número o contacto y una palabra de contexto. Un archivo llamado con año, mes, día y hora por delante se ordena sin ayuda de nadie y sobrevive a cualquier programa.

La carpeta debería tener dos niveles como mucho: un año y un mes. Más niveles se abandonan a la tercera semana; menos niveles se vuelven una lista de cuatro mil archivos.

La copia debería ir a dos sitios, y uno de ellos fuera de la casa. Un disco conectado al mismo escritorio no protege de un robo ni de un incendio, y esa es exactamente la clase de desastre que se lleva las grabaciones.

Y una nota de texto con tres líneas —qué se guarda, dónde y hasta cuándo— vale más que cualquier app de archivado, porque se lee cuando ya nadie recuerda el sistema.

*📞 La llamada que va por internet*

Cuando la conversación no pasa por la red telefónica, la grabación cambia de terreno. Las llamadas por datos no usan la ruta protegida del sistema, así que las reglas son otras: a veces se pueden capturar sin permiso especial y a veces el sistema las trata como audio de aplicación y no deja.

La consecuencia práctica es que la misma grabadora puede funcionar perfecto con la llamada normal y fallar con la llamada de una app de mensajería. No es un fallo del proyecto: es un camino distinto del audio.

Lo que sí se puede hacer siempre es grabar la pantalla con sonido del sistema, que en muchos aparatos recoge el audio de la aplicación. Suena a truco y funciona; el precio es un archivo de video pesado en vez de un audio pequeño, y un aviso en pantalla que la otra persona no ve.

Para quien graba reuniones por internet, la conclusión es que el teléfono es el peor sitio. Una computadora con un programa de escritorio graba mejor, ordena mejor y avisa mejor, y el teléfono queda para lo que no se puede planificar.

*📱 Los aparatos que no dejan*

Hay teléfonos donde ninguna de estas familias funciona bien, y conviene saberlo antes de gastar la tarde. Los tres casos se repiten.

El primero son los aparatos con la ruta de audio cerrada por el fabricante. En ellos la app recibe solo el micrófono, y por más permisos que se den, la otra parte nunca entra al archivo. La prueba de la llamada corta lo revela en dos minutos.

El segundo son los sistemas con ahorro de energía agresivo, que matan el servicio en segundo plano y cortan la grabación sin avisar. Se mitiga excluyendo la app del ahorro, y en algunos aparatos no hay manera.

El tercero son los sistemas que se niegan a operar con permisos prestados: aplicaciones del sistema que comprueban si corren bajo una sesión de depuración y se cierran. Ahí ni Shizuku ni root ayudan, porque el que se niega es el propio componente.

En los tres casos la respuesta honesta es la misma: ese aparato no es para esto. Y la alternativa —grabar por altavoz con otra grabadora, o usar un aparato viejo solo para las llamadas de trabajo— es menos elegante y funciona.

⏬ sigue abajo · parte 7 de 15

═══ MENSAJE 9 de 16 · 3017 caracteres ═══

*🕰️ Cómo llegamos hasta aquí*

La historia de esta función explica por qué hoy hay tantas piezas pequeñas en lugar de un botón.

Durante años, muchos fabricantes incluyeron grabación de llamadas en su marcador, y funcionaba sin permiso especial porque el propio fabricante controlaba la ruta del audio. Fue una función de teléfono, no una app.

Después el sistema fue cerrando esa API por razones de privacidad, y cada versión nueva la dejó más restringida hasta hacerla inútil en la mayoría de los aparatos que se vendieron después de 2021.

El root ocupó el hueco con módulos como BCR, que se enganchan al sistema y graban con calidad. Su público era técnico y su costo, el de siempre: un aparato modificado que algunas apps se niegan a aceptar.

Y cuando el root empezó a escasear, apareció el permiso prestado de Shizuku, que abrió la puerta a grabar sin tocar el arranque. De ahí salió ShizuCallRecorder y, este año, las dos nuevas que empujan el 1 de noviembre.

Lo que la cronología deja ver es el patrón: cada vez que el sistema cierra una puerta, la comunidad abre una ventana más estrecha. Y las ventanas estrechas se cierran solas con el tiempo, así que conviene no encariñarse con ninguna.

*🔍 El caso de la llamada de once minutos*

Llamada de trabajo, once minutos, todo dicho y nada firmado. Al día siguiente, el archivo existe, pesa, y al escucharlo solo se oye un lado: el de quien grabó. Ocurrió tres veces y el usuario concluyó que la app era mala.

El diagnóstico, en orden, fue este. Primero se comprobó el aparato: un modelo con la ruta de audio cerrada, de los que entregan solo micrófono. La app estaba haciendo lo único que podía hacer. Segundo se comprobó la versión: era la última, publicada hacia dos semanas. Tercero se comprobó el ajuste de fuente de audio, que en esa app permite elegir entre micrófono y llamada; estaba en el valor por defecto.

Con el ajuste cambiado a la fuente de llamada, el archivo salió con las dos voces y sonó algo bajo, que es el precio de esa ruta. Con el altavoz activado, salió mejor y con más ruido de ambiente. Las dos soluciones eran mejores que la app nueva que iba a comprar.

Lo que el caso enseña es que en grabación la primera pregunta no es qué app, sino qué ruta de audio tiene el aparato. Y que la segunda no es cuál es la mejor, sino cuál se probó dos veces y se escuchó entera.

*💬 Las frases que se repiten*

«Mi teléfono grababa las llamadas y ya no». Grababa cuando el fabricante lo permitía. La puerta se cerró y no la cierra el usuario.

«Con root es mejor». Es más fiable en la calidad y más caro en las consecuencias: hay apps que se niegan a abrir en un aparato modificado.

«Shizuku es un root». No lo es: presta un permiso del sistema y se apaga al reiniciar. Es menos potente y por eso menos peligroso.

«Compré una app de pago y tampoco». El pago no cambia la ruta del audio. Cambia el soporte y la interfaz.

«Grabé sin avisar y ahora no sé si puedo usarlo». Esa pregunta no la contesta el teléfono.

⏬ sigue abajo · parte 8 de 15

═══ MENSAJE 10 de 16 · 3201 caracteres ═══

*🧮 Cuatro cuentas antes de instalar*

La primera cuenta es de espacio: dos horas de llamada al día, a cuarenta megas la hora, son unos dos gigas y medio al mes y treinta al año. Ese número conviene tenerlo antes de elegir la calidad máxima.

La segunda es de batería: un servicio de grabación permanente consume poco durante la llamada y algo más cuando el teléfono duerme. Si el aparato ya llega apurado a la noche, la grabadora le quita otra media hora de margen.

La tercera es de tiempo: comprobar que la app graba de verdad cuesta dos minutos de llamada y otros dos de escucha. Comprobarlo después de perder una llamada importante cuesta la llamada.

La cuarta es de confianza: cada permiso que se concede a una grabadora es un permiso que hay que recordar. Una lista de dos apps es manejable; una lista de siete es un archivo de decisiones viejas que nadie revisa.

Las cuatro cuentas juntas ocupan menos que el cajón de ajustes de la app, y sirven para decidir sin probar cinco opciones distintas.

*📶 Grabar sin computadora, cuando no hay otra*

El escenario es común: se quiere grabar sin root, no se tiene computadora a mano y el teléfono se reinicia por cualquier cosa. Ahí la ceremonia de Shizuku se vuelve el problema principal, y las dos familias nuevas son la única salida razonable.

La depuración inalámbrica del propio sistema permite volver a arrancar el servicio sin cables, y en aparatos recientes se puede automatizar con una app que lo haga al encender. Es la solución intermedia que casi nadie documenta y que funciona en la mayoría de los teléfonos de los últimos tres años.

La otra vía es aceptar que la grabación solo existe mientras el teléfono no se reinicie, y convertir el reinicio en el recordatorio: se reinicia, se arranca el servicio y se prueba con una llamada corta. Un aparato que se reinicia solo una vez al mes convierte ese mes en el plazo de fiabilidad del sistema.

Y la tercera, para quien no quiere nada de esto, es una grabadora que use el altavoz y una costumbre: llamadas importantes, con altavoz y con aviso. Es peor calidad, es más honesto y no depende de ninguna llave.

*🎚️ La calidad, explicada sin tecnicismos*

Las grabadoras suelen ofrecer tres ajustes de calidad y la gente elige el más alto por reflejo. En una conversación de voz, la diferencia entre el ajuste medio y el alto casi no se oye: lo que se oye es el ruido de fondo, y eso no lo arregla el bitrate.

Lo que sí importa es la fuente. Un archivo capturado del flujo de la llamada suena limpio y sin ambiente; uno capturado del micrófono con altavoz suena con la sala, el ventilador y el eco. El mismo ajuste de calidad en las dos fuentes da resultados que parecen de aparatos distintos.

El formato también importa menos de lo que se cree para escuchar y más de lo que se cree para archivar. Un formato abierto y difundido se puede abrir dentro de diez años con cualquier programa; uno propietario depende de que alguien mantenga el reproductor.

Y el nombre del archivo importa más que todo lo anterior. Un archivo con la fecha delante y el nombre de la persona detrás se encuentra; uno llamado con un número de serie se pierde aunque suene perfecto.

⏬ sigue abajo · parte 9 de 15

═══ MENSAJE 11 de 16 · 3338 caracteres ═══

*🧩 Cuatro piezas que la gente confunde*

En grabación de llamadas se confunden cuatro cosas con una facilidad pasmosa, y de esa confusión salen las compras equivocadas.

La primera es la grabadora y el módulo: BCR no es una app que se instala y ya, es un módulo que se instala en el sistema y deja una app pequeña para ajustarlo. Quien lo busca en la tienda de aplicaciones no lo encuentra, y concluye que el proyecto no existe.

La segunda es el permiso y el root. Shizuku presta un permiso de depuración; el root da control del sistema. Con el primero se puede grabar y no se puede leer el disco entero; con el segundo, sí, y se paga con un aparato que muchas apps miran mal.

La tercera es el archivo y la copia. Tener el archivo en el teléfono no es tenerlo: la copia es lo que sobrevive al robo, a la caída y al cambio de aparato.

La cuarta es el aviso y la legalidad. Avisar al inicio no hace la grabación legal en todos los países y sí hace que casi nunca sea un problema. No avisar no la hace ilegal en todas partes y sí la convierte en un problema el día que se descubre.

Cuatro parejas de conceptos, y con ellas separadas la conversación sobre grabadoras se vuelve corta: qué permite tu aparato, qué permiso hace falta, dónde está la copia y a quién avisaste.

*🧷 El detalle del reinicio, que arruina más grabaciones que todo lo demás*

Hay un fallo que no aparece en ninguna lista de problemas y que se lleva por delante más grabaciones que la calidad o el espacio: el servicio murió y nadie lo notó.

Ocurre así. El teléfono se reinicia por una actualización de madrugada. Shizuku no arranca solo. La grabadora sí arranca sola, porque está configurada para empezar con el sistema. La llamada del día entra, la app intenta grabar sin los permisos que necesita, y hace lo único que puede: escribe un archivo vacío o con la única fuente que sí tiene. El usuario ve el archivo en la lista y cree que tiene la llamada.

La contramedida es doble. La primera, un recordatorio en la mañana después de cada actualización del sistema. La segunda, una llamada de prueba de diez segundos después de cada reinicio, escuchada, que es la única prueba que no engaña.

En los aparatos donde la depuración inalámbrica se puede automatizar, la contramedida se vuelve invisible: el servicio arranca solo y el recordatorio sobra. Es la diferencia entre un sistema que funciona por disciplina y otro que funciona por configuración, y la segunda se sostiene mejor en el tiempo.

*🧑⚖️ Tres preguntas que conviene hacerse antes del primer minuto*

Antes de darle a grabar hay tres preguntas que ahorran disgustos y que no aparecen en ningún tutorial.

La primera: ¿esto lo va a escuchar alguien más? Si la respuesta es sí, el archivo necesita nombre, carpeta y copia desde el primer día, porque el que lo escucha después no tuvo la conversación y no sabe de qué se habla.

La segunda: ¿cuánto tiempo lo necesito? Una grabación de trabajo se guarda tres meses; una personal, a veces ni una semana. Decidirlo antes evita el archivo de ocho gigas que nadie ordena.

La tercera: ¿qué pasa si esto se hace público? No es paranoia: es la pregunta que cambia el formato, el cifrado y la costumbre de avisar.

Con las tres respondidas, la app deja de ser el centro de la decisión y pasa a ser el instrumento, que es su sitio.

⏬ sigue abajo · parte 10 de 15

═══ MENSAJE 12 de 16 · 2632 caracteres ═══

*🗣️ Lo que se oye en la calle*

En los grupos donde se pregunta por grabadoras, tres respuestas se repiten y las tres son incompletas. «Instala la del módulo y ya» sirve si hay root. «Ponle Shizuku» sirve si el aparato entrega la ruta de audio. «Compra la de pago» sirve si el problema era el soporte y no la grabación.

La respuesta que sí sirve es una pregunta: ¿qué teléfono tienes y qué te salió la última vez que grabaste? Con eso, cualquiera que haya pasado por el camino puede decir en dos líneas qué esperar, y el que pregunta deja de probar cinco apps para descubrir lo que su aparato ya decidió.

*❓ Preguntas que me hacen*

**¿Puedo grabar llamadas sin root en un teléfono de 2026?** Sí, con dos condiciones: una app que use el permiso de depuración prestado por Shizuku, o una de las nuevas que se apoyan en las API de accesibilidad. En ambos casos hay que probar el aparato, porque la ruta del audio manda.

**¿Cuál graba mejor, BCR o ShizuCallRecorder?** BCR, en un aparato con root, por acceso directo al audio. ShizuCallRecorder es la mejor opción sin root y su calidad depende del teléfono.

**¿AVault y CallVault son de fiar?** Las dos empujaron el 1 de noviembre, publicaron versión el 31 de octubre y suman ★629 entre las dos. Son nuevas: su código es público y su historial corto, y eso se dice tal cual.

**¿Por qué CallVault declara dos licencias?** Porque su ficha en la forja dice GPL-3.0 y su README dice Apache-2.0. Se publican las dos y no se elige por el lector.

**¿Shizuku tiene que estar activo siempre?** Después de cada reinicio hay que volver a arrancarlo. Mientras está activo, las apps que lo usan funcionan; cuando muere, algunas siguen abriéndose y graban sin los permisos, que es peor que fallar.

**¿Se puede grabar una llamada de WhatsApp?** A veces, y no de la misma manera que una llamada normal. En muchos aparatos la única vía es grabar la pantalla con sonido del sistema.

**¿Cuánto ocupa una hora de grabación?** Entre veinte y sesenta megas según la calidad elegida. Dos horas diarias al año son decenas de gigas, y por eso el formato y la retención importan antes que la app.

**¿Cómo sé que la grabación sirve antes de necesitarla?** Haciendo una llamada de prueba de dos minutos y escuchando el archivo completo. Verlo en la lista no prueba nada.

**¿Puedo usar bcr-gui con otras grabadoras?** No: lee la carpeta de BCR. Para las demás, la copia se hace a mano o con una sincronización.

**¿Grabar mis propias llamadas es legal?** Depende del país y del uso posterior. La regla de la casa es avisar al inicio: convierte una grabación en un acuerdo.

⏬ sigue abajo · parte 11 de 15

═══ MENSAJE 13 de 16 · 3123 caracteres ═══

*📊 Tabla, mitos y glosario*

*Los ocho medidos, en una línea*

| Repositorio | Qué hace | Licencia | Empujón | Estrellas |
|---|---|---|---|---|
| BCR | módulo de grabación con root | GPL-3.0 | 15-oct | ★2.958 |
| ShizuCallRecorder | graba con el permiso de Shizuku | GPL-3.0 | 30-oct | ★1.970 |
| AVault | grabadora nueva con cifrado | ficha sin reconocer, README MIT | 01-nov | ★445 |
| CallVault | grabadora nueva sin root | GPL-3.0 (README Apache-2.0) | 01-nov | ★184 |
| bcr-gui | escritorio para leer lo grabado | GPL-3.0 | 26-oct | ★381 |
| Shizuku | presta el permiso de depuración | Apache-2.0 | 18-jun-2025 | ★32.594 |
| Android-Call-Recorder | grabadora pequeña con root | GPL-3.0 | 25-oct | ★54 |
| CallRecorder (aykuttasil) | el clásico dormido | MIT | 18-oct-2023 | ★791 |

*Cinco mitos de la grabadora*

**Mito uno: «sin root no se puede».** Se puede, con una llave prestada y con las API modernas. Lo que no se puede es garantizar que funcione en todos los aparatos.

**Mito dos: «una app de pago graba mejor».** La calidad la decide la ruta del audio del aparato, no el precio de la app.

**Mito tres: «si el archivo existe, se grabó».** Un archivo mudo pesa lo mismo que uno bueno. La prueba es escucharlo.

**Mito cuatro: «Shizuku es root con otro nombre».** Es un permiso de depuración que se apaga al reiniciar y que el usuario ve en una lista. La diferencia es la que hay entre una llave y un plano.

**Mito cinco: «basta con grabar».** Sin aviso, sin nombre y sin copia, la grabación es un archivo que no sirve el día que hace falta.

*Glosario*

**Ruta de audio** — camino por el que el sistema entrega el sonido de una llamada a las apps.

**Permiso de depuración** — canal de administración que se activa para desarrolladores y que Shizuku presta a otras apps.

**Módulo de sistema** — pieza que se instala en un aparato con root y se engancha al sistema.

**Códec** — formato en el que se guarda el audio; si el reproductor no lo entiende, el archivo suena mudo.

**Retención** — cuánto tiempo se guarda una grabación y cuándo se borra.

**Cifrado por hardware** — protección de los archivos con la clave del aparato; sin copia, se pierden con el teléfono.

*🔗 Enlaces*

Todas las direcciones se abrieron esta tarde.

- BCR, el módulo de sistema: https://github.com/chenxiaolong/BCR
- ShizuCallRecorder: https://github.com/kitsumed/ShizuCallRecorder
- AVault: https://github.com/arpanjot-coding/AVault
- CallVault: https://github.com/madkongo/CallVault
- bcr-gui, la mitad de escritorio: https://github.com/nicorac/bcr-gui
- Shizuku, la llave que se presta: https://github.com/RikkaApps/Shizuku
- Android-Call-Recorder: https://github.com/Benojir/Android-Call-Recorder
- CallRecorder, el dormido: https://github.com/aykuttasil/CallRecorder

*Cómo se midió.* Ocho proyectos, tres lecturas cada uno por tres caminos distintos —búsqueda de la forja, página del repositorio y README crudo—, con el orden rotado de un proyecto al siguiente. Donde la ficha y el README declaran licencias distintas, van las dos. Las versiones se pidieron una por una y se anotó su fecha.

⏬ sigue abajo · parte 12 de 15

═══ MENSAJE 14 de 16 · 2393 caracteres ═══

*🌅 Cierre — la llave, la ruta y el aviso*

Grabar una llamada en 2026 es un trabajo de tres piezas: una llave que el sistema presta, una ruta de audio que el aparato decide y un aviso que la persona elige dar. Ninguna de las tres se resuelve comprando la app más cara.

Lo que deja el censo de hoy es una fila corta y sana: BCR con ★2.958 empujando en octubre, ShizuCallRecorder con ★1.970 y versión v2.0.0 del 24, dos recién llegadas que empujaron el 1 de noviembre, una ventana de escritorio con ★381 y una llave con ★32.594 que lleva más de un año quieta y sigue sirviendo.

El resto es costumbre: probar con una llamada de dos minutos, escuchar el archivo, nombrarlo bien y sacarlo del teléfono una vez al mes. Nada de eso es emocionante y todo eso es lo que hace que una grabación valga algo el día que hace falta.

> —¿Y si el teléfono no deja grabar?
> —Entonces cambias de teléfono o cambias de costumbre. Lo que no se hace es creer que el archivo está bien sin escucharlo.

💓 *La Bandita informa a partir de fuentes fechadas.* Una grabadora no se juzga por su promesa, sino por el archivo mudo que no hizo.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 17:33 y las 17:38 de Santo Domingo · ocho repositorios con las tres lecturas hechas y el orden rotado · dos discrepancias de licencia publicadas con sus dos versiones · las versiones, consultadas aparte, con fecha.

*Licencia de esta entrega:* texto en CC BY-SA 4.0, datos en CC BY 4.0, ejemplos de código en MIT; la marca y el nombre de la casa siguen siendo de «Alexis (La Bandita)».

## 🗒️ Notas al pie

**Nota de corte (1-nov):** los números son de la tarde; dos de las grabadoras empujaron ese mismo día y sus versiones son del 31 de octubre, un día antes del corte.

**Nota de licencia (1-nov):** AVault y CallVault no coinciden entre ficha y README. Se publican las dos versiones, sin elegir, que es la regla desde el primer día.

**Nota de alcance (1-nov):** la guía no enseña a grabar sin consentimiento ni da instrucciones para saltarse la ruta protegida del audio; explica qué permite el sistema y qué se paga por ello.

**Nota de corrección (1-nov):** la versión anterior se centraba solo en ShizuCallRecorder y en números del 15 de octubre. Se reescribió con las tres familias medidas hoy y se añadieron las dos grabadoras nuevas que entonces no existían en el censo.

⏬ sigue abajo · parte 13 de 15

═══ MENSAJE 15 de 16 · 1303 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 12*

Medí otra vez, hoy 2 de noviembre de 2026, los 8 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• Benojir/Android-Call-Recorder — ★54 · empujó el 25-oct-2026 (hace 8 días) · GPL-3.0 · última release 1.5 (23-ago-2024)
• aykuttasil/CallRecorder — ★791 · *dormido*: sin empujar desde el 18-oct-2023 (1111 días) · MIT · última release v1.5.3 (29-jul-2019)
• chenxiaolong/BCR — ★2.961 · empujó el 15-oct-2026 (hace 18 días) · GPL-3.0 · última release v3.11 (15-oct-2026)
• kitsumed/ShizuCallRecorder — ★1.979 (+47) · empujó en las últimas horas · GPL-3.0 · última release v2.0.0 (24-oct-2026)
• arpanjot-coding/AVault — ★527 · empujó en las últimas horas · NOASSERTION · última release v2.0.1 (2-nov-2026)
• madkongo/CallVault — ★186 · empujó en las últimas horas · GPL-3.0 · última release v2.4.8 (31-oct-2026)
• nicorac/bcr-gui — ★381 · empujó el 26-oct-2026 (hace 7 días) · GPL-3.0 · última release v1.16.0 (25-oct-2026)
• RikkaApps/Shizuku — ★32.636 (+251) · *dormido*: sin empujar desde el 18-jun-2025 (502 días) · Apache-2.0 · última release v13.6.0 (25-may-2025)

💓 *LOS ENLACES · medidos hoy uno por uno*

De los 8 enlaces de esta pieza, *8 responden*.
Ninguno roto.

⏬ sigue abajo · parte 14 de 15

═══ MENSAJE 16 de 16 · 152 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.
