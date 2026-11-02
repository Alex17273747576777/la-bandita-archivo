# PIEZA 22 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/22-El-papeleo-del-telefono-escanear-ordenar-y-leer-lo-que-llega-en-PDF-Facebook-La-Bandita-2026-11-02-dominicano-ES.md`
- **Fecha de la pieza:** 2-nov-2026 (según dateline; edad hoy: 0 días)
- **sha256 de la pieza:** `629c00c8e3d02f970d613019acdd1612947a751773e4fdb1e1825b99b6027507`
- **Envío generado:** 2026-11-02 · 17 mensajes · el mayor de 3564 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 17 · 784 caracteres ═══

*El papeleo del teléfono: escanear, ordenar y leer lo que llega en PDF*

La Bandita · pieza 22 · guía del 2-nov-2026 · te la mando hoy en 17 mensajes.

Antes de mandártela volví a medir lo que afirma: *13 repositorios, 12 vivos y 1 muerto*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: NOASSERTION 3 · Apache-2.0 2 · GPL-3.0 2 · MIT 2.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/22-El-papeleo-del-telefono-escanear-ordenar-y-leer-lo-que-llega-en-PDF-Facebook-La-Bandita-2026-11-02-dominicano-ES.md

💓 2 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 17 · 2506 caracteres ═══

*El papeleo del teléfono: escanear, ordenar y leer lo que llega en PDF*

*La Bandita · lunes 2 de noviembre de 2026 · edición dominicano-español · pieza 22 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 📄 Los tres trabajos del papeleo
├── 🎬 Cuatro escenas de esta mañana
├── 🧾 Los diez, uno por uno, con su fecha
├── 📷 Del papel al PDF con texto
├── 🗄️ El archivo que se busca solo
├── ⚖️ La raya de los papeles con datos
├── 🛠️ Probar el papeleo en seis pasos
├── 🧮 Las cuentas del escritorio
├── ❓ Preguntas que me hacen
└── 📊 Tabla, mitos, glosario y enlaces
```

*⚡ En una página*

Casi todo lo que llega hoy a un teléfono llega en PDF: una factura, una receta, un contrato de trabajo, el recibo de la luz, la carta del banco, la tarea del muchacho. Y casi nadie tiene con qué leerlo bien, menos aún con qué escanearlo y muchísimo menos con qué encontrarlo tres meses después. Ese es el papeleo, y esta mañana se midieron diez programas que lo resuelven por partes: dos que escanean, cinco que leen, tres que ordenan y buscan dentro de lo leído. Juntos suman ★311.355, y ninguno de los diez cuesta un centavo.

Los números de la mañana dicen dónde está el trabajo pesado. Los dos gigantes —Stirling PDF con ★95.558 y Tesseract con ★77.298— no son aplicaciones de teléfono: son el motor y la caja de herramientas que otros usan. Los dos con empujón de hoy. Y en el otro extremo está un escáner con ★1.544 cuya última publicación de paquete es del 22 de julio de 2020: sigue instalándose, sigue escaneando y nadie lo ha tocado en más de seis años. Entre esos extremos vive todo lo demás.

Hay un dato que ordena la decisión mejor que cualquier recomendación: cuatro de los diez no publican paquete nunca o casi nunca y hay que compilarlos, mientras tres publicaron versión en los últimos cuatro días. Y hay dos licencias que la ficha automática no supo leer —Stirling PDF y OpenNoteScanner— y que el archivo del repositorio sí declara: MIT el primero, GPL-3.0 el segundo. Esas dos se publican con las dos versiones, como manda la casa.

La utilidad práctica de esta guía es corta: si lo que quieres es leer un PDF y ya, hay un lector de ★1.062 que hace una sola cosa; si quieres escanear el papeleo de la casa, hay dos caminos, uno que se instala y uno que se compila; y si quieres encontrar dentro del papel lo que dice, hay dos programas que convierten imagen en texto y uno que además guarda, etiqueta y busca. Lo demás es fecha, licencia y paciencia.

⏬ sigue abajo · parte 1 de 16

═══ MENSAJE 3 de 17 · 2251 caracteres ═══

*📄 Los tres trabajos del papeleo*

El papeleo no es una sola tarea y por eso no tiene una sola herramienta. Son tres trabajos distintos, con tres clases de programa distinta, y confundirlos es la razón por la que la gente termina con cinco aplicaciones instaladas y ninguna que sirva.

*Primer trabajo: capturar.* Convertir un papel en una imagen decente. Aquí manda la cámara: luz, ángulo, sombra y pulso. Un escáner bueno corrige la perspectiva, recorta los bordes, endereza el texto y convierte todo en un PDF de una página por hoja. OpenNoteScanner (★1.544) hace exactamente eso y nada más, y lo hace desde 2016 con el último paquete firmado en 2020. La otra vía es la cámara de una aplicación de notas que ya tengas, y no es despreciable: la mitad de los escaneos del mundo se hacen así.

*Segundo trabajo: reconocer.* Convertir la imagen en texto que se pueda buscar y copiar. Aquí el nombre que aparece en todas partes es Tesseract (★77.298, Apache-2.0), el motor de reconocimiento óptico que llevan dentro muchísimos otros programas; y por encima de él, OCRmyPDF (★35.209, MPL-2.0), que toma un PDF escaneado y le añade una capa de texto invisible sin tocar la imagen original. Ese detalle —no tocar la imagen— es lo que hace que un PDF siga siendo el documento y a la vez sea buscable.

*Tercer trabajo: ordenar y encontrar.* Guardar miles de documentos y poder preguntar «la factura de la luz de marzo» y que aparezca. Ahí está paperless-ngx (★47.563, GPL-3.0), que vigila una carpeta, reconoce el texto, adivina el tipo de documento y lo archiva con etiquetas; y a su lado, en la parte más artesanal, dos lectores de teléfono que abren el PDF y lo dejan legible: GrapheneOS PdfViewer (★1.062, MIT) y Parchment (★3.590, Apache-2.0).

A esos tres trabajos se suman dos programas que sirven para lo mismo por otro camino: Pandoc (★46.784, GPL-2.0), que convierte documentos entre formatos y es el cuchillo suizo del que escribe, y las dos herramientas de escritorio que completan la caja: Stirling PDF (★95.558) para partir, unir, firmar, comprimir y rotar sin subir nada a internet, y OpenPDF (★4.385, con su propia discrepancia de licencia anotada) para quien programa en Java y necesita leer PDF desde código.

⏬ sigue abajo · parte 2 de 16

═══ MENSAJE 4 de 17 · 1863 caracteres ═══

*🎬 Cuatro escenas de esta mañana*

*Escena uno: la factura de la luz.* Llega un PDF al correo, se abre en el teléfono, se ve pequeño, se hace zoom, se pierde el renglón, se cierra. Diez minutos después hay que enseñarlo en una oficina y no aparece. Un lector de PDF sencillo de los que se midieron hoy resuelve la mitad del problema: abre rápido, recuerda la última página, permite girar y no pide nada. La otra mitad la resuelve el nombre del archivo, que es gratis y casi nadie usa.

*Escena dos: el contrato firmado a mano.* Un contrato llega impreso, se firma con bolígrafo, hay que devolverlo. Se fotografía con el teléfono torcido, con sombra de la mano y el borde de la mesa. OpenNoteScanner, si está instalado, endereza y aclara; si no está, la foto torcida se manda igual y vuelve rechazada. Ese es todo el argumento del escáner, y con eso basta.

*Escena tres: la carpeta de los estudios.* Alguien tiene trescientos documentos: títulos, certificados, recibos, cartas del seguro. Los tiene en el teléfono con nombres como «IMG_20240312» y una carpeta llamada «documentos importantes» con todo revuelto. paperless-ngx, montado en una computadora o en una cajita siempre encendida, los indexa y permite buscar dentro del texto. La primera tarde cuesta; la primera búsqueda que devuelve un certificado de hace cuatro años en dos segundos paga la tarde.

*Escena cuatro: el PDF que no abre.* Un PDF pesa cuarenta megas, el teléfono lo abre a medias y se cierra. Aquí entra Stirling PDF, que se instala en la computadora o se corre en un contenedor y parte el documento en tres, lo comprime o extrae solo las páginas que hacen falta. No es una aplicación de teléfono y no pretende serlo; es la caja de herramientas del escritorio, y como casi todo lo bueno de esta guía, funciona sin mandar el documento a ningún servidor ajeno.

⏬ sigue abajo · parte 3 de 16

═══ MENSAJE 5 de 17 · 3540 caracteres ═══

*🧾 Los diez, uno por uno, con su fecha*

*Stirling PDF · Stirling-Tools/Stirling-PDF · ★95.558 · licencia declarada en el archivo: MIT, con partes bajo otras licencias · la ficha automática dice NOASSERTION · TypeScript · empujón 2 de noviembre de 2026 · versión v3.2.2 del 24 de octubre de 2026.* El número más alto de la mañana y el que más gente usa sin saber su nombre. Se corre en la computadora, en un contenedor o en una cajita de la casa; une, parte, comprime, firma, rota y reconoce texto, y no manda el documento afuera salvo que uno lo configure para eso. La discrepancia de licencia se debe a que el archivo de licencia contiene el texto del MIT y, a continuación, un párrafo de excepciones por partes; la ficha automática no lo resume y devuelve «sin conclusión».

*Tesseract · tesseract-ocr/tesseract · ★77.298 · Apache-2.0 · C++ · empujón 2 de noviembre de 2026 · versión 5.5.4 del 28 de octubre de 2026.* El motor de reconocimiento que está debajo de media docena de programas que la gente usa a diario. No tiene interfaz: es la pieza que mira una imagen y devuelve letras. Apache-2.0 lo hace amigable para cualquiera que quiera meterlo en su programa, y por eso está en tantos sitios.

*paperless-ngx · paperless-ngx/paperless-ngx · ★47.563 · GPL-3.0 · Python · empujón 2 de noviembre de 2026 · versión v3.4.1 del 31 de octubre de 2026.* El archivo del papeleo, en el sentido literal: vigila una carpeta, lee lo que entra, propone etiqueta, guarda el original y deja buscar dentro del texto. Empujón de hoy y paquete del sábado: el proyecto más cuidado de los diez en términos de entrega.

*Pandoc · jgm/pandoc · ★46.784 · GPL-2.0 · Haskell · empujón 2 de noviembre de 2026 · versión 3.13 del 26 de octubre de 2026.* El conversor universal de documentos: de Markdown a PDF, de Word a texto, de HTML a lo que sea. No es un lector ni un escáner: es el programa que evita tener que abrir un formato raro para sacarle lo que dice. GPL-2.0 y una vida de más de una década.

*OCRmyPDF · ocrmypdf/OCRmyPDF · ★35.209 · MPL-2.0 · Python · empujón 25 de octubre de 2026 · versión v17.13.0 del 28 de septiembre de 2026.* Añade a un PDF escaneado una capa de texto invisible, sin tocar la imagen. Su licencia MPL-2.0 es menos común en esta serie y conviene saber qué significa: los archivos modificados del propio proyecto se comparten, y se puede usar dentro de programas más grandes con otras licencias.

*OpenPDF · LibrePDF/OpenPDF · ★4.385 · licencia declarada en el archivo, ficha automática en NOASSERTION · Java · empujón 12 de octubre de 2026.* La pieza para quien programa: leer, escribir y manipular PDF desde código Java. Se nombra aquí para que nadie confunda el motor con la aplicación; si tu interés es leer facturas, no es tu programa.

*Parchment · AhmadHassan-BTed/Parchment · ★3.590 · Apache-2.0 · Kotlin · empujón 30 de junio de 2026 · sin publicación de paquete.* Lector de PDF para Android con cuatro meses de silencio y ninguna versión publicada: para usarlo hay que compilarlo. Es el caso más claro de la mañana sobre lo que significa «no hay paquete»: miles de personas interesadas y ningún archivo instalable.

*book-story · Acclorite/book-story · ★1.418 · GPL-3.0 · Kotlin · empujón 1 de noviembre de 2026 · versión v1.8.0 del 13 de octubre de 2025.* Lector de libros y documentos en el teléfono; empuja ayer y su último paquete tiene más de un año. Un año de código sin entrega es exactamente lo que hay que saber antes de instalarlo: lo que bajes no es lo que están haciendo.


⏬ sigue abajo · parte 4 de 16

═══ MENSAJE 6 de 17 · 2743 caracteres ═══

*episteme · Aryan-Raj3112/episteme · ★1.329 · AGPL-3.0 · Kotlin · empujón 10 de octubre de 2026 · versión v1.0.58-oss del 9 de octubre de 2026.* Lector con vida de versiones numerosas y pequeñas, paquete del mismo día de su último empujón. La AGPL-3.0 importa si alguien piensa ofrecerlo como servicio; para uso propio, no cambia nada.

*OpenNoteScanner · allgood/OpenNoteScanner · ★1.544 · licencia declarada en el archivo: GPL-3.0 · la ficha automática dice NOASSERTION · Kotlin · empujón 23 de abril de 2025 · versión 1.0.35-fdroid del 22 de julio de 2020.* El escáner de la vieja escuela: enfoca, detecta el borde del papel, lo endereza y arma el PDF. Seis años sin paquete nuevo y sigue instalándose en teléfonos de hoy, lo que dice mucho del programa y muy poco del mantenimiento.

*📷 Del papel al PDF con texto*

El recorrido completo, para quien tenga el papeleo encima de la mesa y quiera terminar hoy.

*El original siempre se guarda.* El primer error es tirar el papel después de escanear. La foto del teléfono sirve para casi todo, y no sirve como prueba legal cuando alguien discute una firma. Guarda el original un tiempo prudente; el archivo digital es una copia cómoda, no un sustituto absoluto.

*La foto se hace con luz de día y sin sombra de mano.* Suena obvio y es la diferencia entre un reconocimiento que funciona y uno que devuelve basura. Papel sobre mesa, luz de ventana, teléfono paralelo y quieto. Si el escáner detecta bordes, deja que los detecte; si no, recorta después y no antes.

*El reconocimiento va después, no antes.* Primero el PDF con las imágenes en orden; luego la capa de texto. Hacerlo al revés obliga a repetir el trabajo cuando una página sale torcida. Con OCRmyPDF el comando típico toma el PDF, lo procesa y devuelve el mismo documento con texto seleccionable, y si una página ya tenía texto no la vuelve a procesar.

*El nombre del archivo es la mitad del archivo.* Un criterio que funciona y no requiere programa: año, mes, día, tipo y quien lo emite, separados por guiones, en ese orden. Así se ordenan solos y se buscan sin abrir. Lo que no se nombra se pierde, aunque el texto esté reconocido.

*La carpeta vigilada es la que hace la magia.* paperless-ngx consume lo que entra a una carpeta; si el documento se llama bien y viene de un escáner, la etiqueta se acierta casi siempre. La primera semana hay que corregir etiquetas a mano; después el sistema aprende de sus propios errores y acierta más.

Y un consejo que ahorra discusiones: el papeleo de la casa no necesita estar en el teléfono. Necesita estar en un sitio con copia y poder consultarse desde el teléfono. Esa distinción evita llenar el aparato de fotos de facturas que nadie va a volver a mirar.

⏬ sigue abajo · parte 5 de 16

═══ MENSAJE 7 de 17 · 2447 caracteres ═══

*🗄️ El archivo que se busca solo*

Tener los documentos no es tener el archivo. El archivo empieza cuando puedes responder tres preguntas sin abrir carpetas: qué tengo, de cuándo es y dónde está.

*Qué tengo.* Un índice por tipo: identidad, vivienda, salud, trabajo, vehículo, escuela, impuestos. Cada tipo con su carpeta y su año. Parece burocracia y es lo que permite, en una emergencia, saber en treinta segundos si falta un papel.

*De cuándo es.* La fecha del documento, no la del escaneo. Un recibo escaneado en 2026 puede ser de 2019. Si el archivo guarda solo la fecha en que entró, la cronología se vuelve inútil.

*Dónde está.* Una copia en el equipo principal y una copia fuera: un disco externo, otra computadora de la casa o un servicio que cifre antes de subir. La regla de la casa es simple: dos copias y un sitio distinto; una sola copia no es una copia.

Con esas tres cosas, paperless-ngx deja de ser un lujo y pasa a ser la herramienta que responde. Sin ellas, es un programa más que guarda desorden con mejor interfaz.

*⚖️ La raya de los papeles con datos*

El papeleo es la parte de esta serie donde la privacidad no es un tema abstracto: son números de cuenta, diagnósticos, contratos y firmas.

*Lo que se sube a un servicio gratuito de conversión de PDF se está entregando.* Los conversores en línea resuelven en treinta segundos y cobran con el documento. Para una receta médica o un contrato, eso no es un intercambio razonable. La alternativa de esta mañana —Stirling PDF en la computadora, OCRmyPDF en la computadora, paperless-ngx en la casa— existe precisamente para eso.

*Cifrar antes de sacar de casa.* Un disco externo que viaja sin cifrar es un documento perdido esperando. Un archivo comprimido con contraseña decente y la contraseña por otro canal resuelve el 90 % de los casos domésticos, y no requiere saber nada de criptografía.

*Compartir es una decisión, no un gesto.* Mandar una foto del carné por mensajería para «que me ayuden con el trámite» es entregar el documento a un grupo. Recortar, tapar lo que no hace falta y preferir un enlace que caduque son hábitos de treinta segundos.

Y la raya de la casa, dicha sin sermón: no se publican documentos personales ajenos, no se reparten plantillas falsas de facturas ni de certificados, y no se enseña a fabricar un papel que parezca oficial. Lo que hay aquí son programas para leer, reconocer y ordenar lo que ya es tuyo.

⏬ sigue abajo · parte 6 de 16

═══ MENSAJE 8 de 17 · 3564 caracteres ═══

*🛠️ Probar el papeleo en seis pasos*

*Paso uno: elige el lector antes que el escáner.* Un lector ligero y libre en el teléfono resuelve el 80 % de los PDF que llegan. GrapheneOS PdfViewer hace una sola cosa y la hace sin pedir permisos raros; Parchment promete más y exige compilar. Empieza por el que se instala en un minuto.

*Paso dos: prueba con el PDF más feo que tengas.* El de cuarenta megas, el escaneado torcido, el que tiene doscientas páginas. Si el lector abre ese, abre todos. Si se cierra, ya sabes que el problema no era el documento.

*Paso tres: escanea una página y mira el resultado con lupa.* ¿El borde está recto? ¿Se lee el pie de página? ¿Pesa menos de dos megas? Un escáner que devuelve imágenes de ocho megas por hoja te va a llenar el teléfono en una semana.

*Paso cuatro: añade texto y busca dentro.* Pasa el PDF escaneado por OCRmyPDF en la computadora y luego busca una palabra que sepas que está en la página tres. Si aparece, el reconocimiento sirvió; si no, suele ser la foto y no el programa.

*Paso cinco: monta la carpeta vigilada con diez documentos, no con trescientos.* Un archivo pequeño enseña las mañas del sistema sin arruinar la tarde. Cuando las etiquetas salgan bien en esos diez, entra el resto.

*Paso seis: prueba la copia antes de confiar.* Copia la carpeta a un disco externo, borra un documento del original y recupéralo del disco. La copia que no se ha probado no es una copia: es una esperanza.

*🧮 Las cuentas del escritorio*

*Primera cuenta: el peso de las estrellas.* Los diez suman ★311.355. Los cinco primeros —Stirling, Tesseract, paperless, Pandoc, OCRmyPDF— se llevan ★302.412, es decir el 97 %. Los cinco pequeños de teléfono y escritorio se reparten ★8.943. El interés del público está en las herramientas de escritorio que casi nadie instala en el teléfono, y las aplicaciones que la gente sí usa a diario son las que menos estrellas tienen.

*Segunda cuenta: quién trabaja hoy.* Cinco empujaron entre el 1 y el 2 de noviembre: Stirling, Tesseract, paperless, Pandoc y book-story. Tres empujaron en octubre: OCRmyPDF, PdfViewer y episteme. Dos llevan meses o años callados: Parchment desde el 30 de junio y OpenNoteScanner desde abril de 2025, con paquete de julio de 2020.

*Tercera cuenta: las entregas.* Cinco de los diez publicaron versión en las últimas dos semanas: Stirling (24 de octubre), Tesseract (28), paperless (31), Pandoc (26) y episteme (9 de octubre). Uno no ha publicado nunca (Parchment), uno tiene año y medio de brecha (OpenNoteScanner, seis años) y uno tiene más de un año (book-story).

*🎯 El caso del certificado que apareció en dos segundos*

Un hombre necesitaba un certificado de estudios de hace once años para un trámite. Lo tenía escaneado, sabía que lo tenía, y llevaba dos horas abriendo carpetas con nombres como «documentos», «documentos 2» y «escaneos viejos». Lo encontró cuando alguien le preguntó si su archivo tenía texto buscable. No lo tenía: eran fotos.

La tarde siguiente pasó por reconocimiento trescientos documentos y los metió en una carpeta vigilada. Al día siguiente escribió «certificado» en el buscador y salió en dos segundos, con la fecha del documento y el nombre del centro. Lo que cambió no fue la suerte: fue que el archivo dejó de ser un montón de imágenes y pasó a ser un archivo con texto dentro.

Moraleja práctica: si tu papeleo son fotos, tienes imágenes; si tiene texto reconocido y un índice, tienes archivo. La diferencia se paga una vez, en una tarde, y se cobra cada vez que alguien pide un papel.

⏬ sigue abajo · parte 7 de 16

═══ MENSAJE 9 de 17 · 3541 caracteres ═══

*🧷 Lo que no hace ninguno de los diez*

Ninguno de los diez arregla el problema de fondo, que es que el papel sigue llegando. Ninguno impide que el banco mande el estado de cuenta en un formato que solo su aplicación abre. Ninguno sustituye a la carpeta física de los originales que hay que conservar por ley. Y ninguno decide por ti qué vale la pena guardar.

Lo que sí hacen, y ya es bastante: leer lo que llega, convertir lo que se fotografía, encontrar lo que se guardó y no mandar nada afuera si uno no lo autoriza. Con eso, el papeleo deja de ser una caja de zapatos y pasa a ser un archivo que responde.

*❓ Preguntas que me hacen*

**¿Necesito instalar los diez?**
No. Con un lector en el teléfono y uno de los dos caminos de reconocimiento en la computadora se resuelve el 95 % del papeleo doméstico. Los demás son especialidades: partir PDF, convertir formatos, programar.

**¿Puedo escanear solo con el teléfono, sin computadora?**
Sí, y para la mayoría de la gente es suficiente: escáner en el teléfono, PDF en la carpeta, nombre correcto y copia en un disco. Lo que se pierde es el texto buscable dentro de los documentos viejos, que se recupera después en una sola tanda.

**¿Qué es exactamente el reconocimiento óptico de caracteres?**
El programa mira la imagen de una página, identifica formas de letras y escribe el texto que ve en una capa aparte, encima de la imagen. La imagen no se toca: por eso el documento sigue viéndose igual y además se puede buscar y copiar.

**¿OpenNoteScanner, con paquete de 2020, todavía sirve?**
En teléfonos donde se instala, sí: escanea, endereza y arma el PDF. El riesgo es que no habrá arreglos si una versión nueva de Android rompe algo. Se usa con esa advertencia y con la copia de los originales a mano.

**¿Y Parchment, que no publica paquete?**
Significa que para usarlo hay que compilar, con lo que eso implica: instalar herramientas, seguir instrucciones y firmar el paquete uno mismo. El dato de las ★3.590 dice que hay interés; la falta de publicación dice que ese interés no se traduce en un archivo instalable.

**¿Stirling PDF manda mis documentos a algún sitio?**
Tal como se instala en la casa, no: procesa en el equipo donde corre. La advertencia es para las versiones alojadas por terceros y para los conversores gratuitos de la web, que son otra cosa aunque tengan el mismo nombre en la pantalla.

**¿Por qué dos fichas dicen NOASSERTION si tienen licencia?**
Porque la ficha automática lee el archivo de licencia y, cuando encuentra texto adicional, no se atreve a resumir. En los dos casos el archivo del repositorio lo dice claro: MIT en Stirling PDF y GPL-3.0 en OpenNoteScanner. Se publican las dos versiones para que nadie discuta con la ficha.

**¿paperless-ngx necesita un servidor?**
Necesita un equipo encendido donde correr. Puede ser una computadora de la casa, una cajita pequeña o incluso un teléfono viejo con un entorno adecuado. Si no hay equipo encendido, la alternativa es la carpeta bien nombrada y el buscador del sistema.

**¿Cómo se comparte un documento sensible sin regalarlo?**
Recortando lo que no hace falta, tapando números y mandando por un canal que no sea un grupo. Si hay que dar acceso, un enlace que caduque o un archivo cifrado con contraseña dicha por otro medio.

**¿Qué hago con los originales en papel?**
Guardarlos un tiempo prudente en una carpeta física por tipo y año, con lo que la ley exija conservar. El escaneo es la copia cómoda; el original sigue siendo el original cuando alguien discute.

⏬ sigue abajo · parte 8 de 16

═══ MENSAJE 10 de 17 · 3524 caracteres ═══

*📊 Tabla, mitos y glosario*

*Los diez medidos, en una línea*

| Proyecto | Estrellas | Licencia | Empujón | Última versión |
|---|---|---|---|---|
| Stirling PDF | ★95.558 | MIT (ficha: NOASSERTION) | 2-nov-2026 | v3.2.2 · 24-oct-2026 |
| Tesseract | ★77.298 | Apache-2.0 | 2-nov-2026 | 5.5.4 · 28-oct-2026 |
| paperless-ngx | ★47.563 | GPL-3.0 | 2-nov-2026 | v3.4.1 · 31-oct-2026 |
| Pandoc | ★46.784 | GPL-2.0 | 2-nov-2026 | 3.13 · 26-oct-2026 |
| OCRmyPDF | ★35.209 | MPL-2.0 | 25-oct-2026 | v17.13.0 · 28-sep-2026 |
| OpenPDF | ★4.385 | ficha: NOASSERTION | 12-oct-2026 | — |
| Parchment | ★3.590 | Apache-2.0 | 30-jun-2026 | sin paquete |
| OpenNoteScanner | ★1.544 | GPL-3.0 (ficha: NOASSERTION) | 23-abr-2025 | 1.0.35 · 22-jul-2020 |
| book-story | ★1.418 | GPL-3.0 | 1-nov-2026 | v1.8.0 · 13-oct-2025 |
| episteme | ★1.329 | AGPL-3.0 | 10-oct-2026 | v1.0.58-oss · 9-oct-2026 |

*Cinco mitos del papeleo*

*Mito uno: «si lo escaneé, ya está guardado».* Guardado en el teléfono no es guardado. Sin copia en otro sitio, es una foto más esperando el día que el aparato se pierda.

*Mito dos: «un PDF es un PDF».* Un PDF de imágenes no se puede buscar; uno con capa de texto, sí. La diferencia se nota la primera vez que hay que encontrar una cláusula.

*Mito tres: «los conversores en línea son inofensivos».* Treinta segundos y un documento con datos personales entregado a un tercero que no firmó nada contigo. Para papeles sensibles, la conversión se hace en casa.

*Mito cuatro: «más estrellas quiere decir mejor para mi caso».* Los dos más grandes de hoy ni siquiera son aplicaciones de teléfono. Un motor con ★77.298 no abre un PDF: hay que saber usarlo desde otro programa.

*Mito cinco: «lo que no se ha actualizado ya no sirve».* OpenNoteScanner no recibe paquete desde 2020 y sigue escaneando. Lo que no tiene es futuro: si una versión de Android lo rompe, se queda roto.

*Glosario*

*OCR:* reconocimiento óptico de caracteres; convierte la imagen de un texto en texto que se puede buscar.

*Capa de texto:* texto invisible añadido sobre la imagen de una página escaneada.

*Carpeta vigilada:* carpeta que un programa revisa de forma continua y procesa lo que entra.

*PDF/A:* variante de PDF pensada para conservación a largo plazo.

*Compresión:* reducción del tamaño del archivo, casi siempre a costa de calidad de imagen.

*Escáner de documentos:* programa que fotografía papel, corrige la perspectiva y arma un PDF.

*Archivo:* conjunto ordenado y con copia; no es lo mismo que una carpeta con archivos dentro.

*🧭 Cuatro perfiles y su papeleo*

*El que solo recibe papeles.* Un lector ligero en el teléfono, una carpeta por año y la costumbre de renombrar lo que llega. No necesita servidor, no necesita reconocimiento y no necesita más de diez minutos al mes. Es el perfil más común y el que menos herramientas exige.

*El que escanea todo.* Escáner en el teléfono, reconocimiento en la computadora y una carpeta vigilada que ordena. Una tarde de montaje y diez minutos por semana. Es el perfil que más se beneficia de paperless-ngx.

*El que trabaja con documentos.* Stirling PDF para partir, unir y firmar, Pandoc para convertir formatos, OpenPDF cuando hay que programar. Este perfil vive en el escritorio y solo usa el teléfono para leer y para firmar.

*El que guarda por ley.* El que tiene que conservar originales: contabilidad, contratos, historiales. Aquí la regla es doble archivo —digital con copia y papel ordenado— y ningún programa sustituye la disciplina.

⏬ sigue abajo · parte 9 de 16

═══ MENSAJE 11 de 17 · 2918 caracteres ═══

*📱 El teléfono como escáner de bolsillo*

La cámara del teléfono, bien usada, sustituye a un escáner plano para casi todo el papeleo doméstico. Tres trucos y ningún programa nuevo.

*El truco de la ventana.* Luz de día indirecta, papel sobre superficie oscura y lisa, teléfono paralelo al papel. La superficie oscura hace que el borde del papel se vea y el recorte automático acierte. La luz directa del sol quema el papel blanco y arruina el reconocimiento.

*El truco de la mano quieta.* Apoyar los codos en la mesa o poner el teléfono boca abajo sobre un vaso para hacer de trípode improvisado. La nitidez importa más que los megapíxeles: una foto de 12 megas borrosa es peor que una de 5 nítida.

*El truco del orden.* Escanear un documento completo de una vez, página por página, sin interrupciones, y nombrarlo al final. Interrumpir el escaneo para contestar y volver después es la causa principal de documentos con páginas mezcladas.

Y el consejo que ahorra disgustos: cuando el documento es importante, revisa el PDF completo antes de archivar. Una página que falta se descubre en la oficina, no en la casa.

*🕰️ Cómo era esto hace cinco años*

En 2020 escanear en el teléfono era una aventura: aplicaciones con anuncios, marcas de agua y permisos excesivos, y conversores en línea que devolvían un PDF con publicidad en la esquina. El archivo del papeleo era una carpeta de la computadora y la búsqueda dentro del texto, un lujo de oficina.

Hoy el panorama es otro y no por una aplicación milagrosa: porque las piezas se separaron. El motor de reconocimiento es libre y está en todas partes (Tesseract); el conversor de imágenes en texto con capa invisible es libre y corre en la casa (OCRmyPDF); el archivador con búsqueda es libre y se monta en una cajita (paperless-ngx); y la caja de herramientas del escritorio, que antes costaba una licencia, hoy se corre en un contenedor (Stirling PDF).

Lo que no cambió es la parte humana. La gente sigue fotografiando papeles torcidos con sombra de mano y sigue guardando todo en una carpeta llamada «documentos». Ninguna de las diez piezas de hoy arregla eso.

*🧷 Cuatro carpetas que conviene tener*

*Identidad:* documento de identidad, pasaporte, licencia, acta de nacimiento. Se tocan una vez al año y se necesitan en las peores horas.

*Casa:* contrato de alquiler o título, recibos de servicios de los últimos dos años, seguro. Es la carpeta que se pide cuando hay una mudanza o una avería.

*Salud:* recetas, resultados de laboratorio, historial de vacunas. La que más veces se comparte y la que más cuidado exige al compartirla.

*Trabajo y estudio:* contratos, certificados, títulos, constancias. La que más se pide en trámites y la que menos se ordena.

Cuatro carpetas, cuatro tipos, una copia fuera de casa. Con eso, el papeleo deja de dar miedo y pasa a ser lo que debería haber sido siempre: una carpeta que responde.

⏬ sigue abajo · parte 10 de 16

═══ MENSAJE 12 de 17 · 2969 caracteres ═══

*🧾 Lo que costó medir estos diez*

La mañana se fue en tres cosas que no se ven en la tabla. Primero, confirmar las dos licencias que la ficha automática no supo leer: hubo que abrir el archivo de licencia de Stirling PDF y de OpenNoteScanner y leer las primeras líneas para encontrar el texto real, MIT y GPL-3.0, y anotar la discrepancia en la ficha en lugar de elegir la versión que más gusta.

Segundo, comprobar las fechas de publicación una por una en la lista de cada proyecto, porque la ficha automática las devuelve vacías en varios casos. De ahí salieron las dos ausencias que ordenan toda la guía: Parchment, con ★3.590 y ninguna publicación, y OpenNoteScanner, con paquete de julio de 2020.

Tercero, decidir qué cinco de los once candidatos se quedaban fuera. Se midieron también OpenPDF y un par de lectores más pequeños; OpenPDF se quedó por ser el único de la familia que sirve para programar, y los otros dos se cayeron por no aportar nada distinto a lo ya medido. Cuando se cae un candidato, se dice: hoy fueron dos, sin nombre y sin pena.

*📎 Lo que deja el escritorio*

Una idea que sirve más allá del papeleo: separar el trabajo en piezas pequeñas y elegir cada pieza por separado. Escáner, motor de texto, archivador y lector son cuatro cosas distintas; cuando se compran juntas, se compran atadas. Cuando se eligen por separado, cada una se puede cambiar sin tocar las otras.

Es la misma lección de la música y de los lectores de libros, aplicada al papel. Y con eso, el papeleo deja de ser ese montón que da flojera y pasa a ser un archivo que, cuando alguien pide un papel, contesta en dos segundos.

*🎚️ Los formatos del papeleo*

*PDF normal.* El de todos los días. Puede tener imágenes y texto, o solo imágenes. Es el que se manda y el que se imprime, y el único que hay que dominar de verdad.

*PDF con capa de texto.* El mismo PDF, con el texto reconocido encima. Se busca, se copia y se lee en voz alta. Ocupa apenas unos kilobytes más que el original y es lo que convierte un montón de fotos en archivo.

*PDF/A.* Variante pensada para conservación a largo plazo: prohíbe ciertas cosas que dependen de fuentes o de programas externos. Útil para documentos que hay que guardar décadas; exagerado para el recibo de la luz.

*Imagen suelta.* JPG o PNG de una página. Sirve para mandar por mensajería y no sirve para archivar: pesa más, no tiene páginas y no se busca dentro. El escáner del teléfono debe devolver PDF, no una galería de fotos.

*Comprimido.* Un PDF comprimido pierde calidad de imagen y conserva el texto. Es la solución cuando el portal de un trámite rechaza un archivo por tamaño, y hay que comprobar después que sigue siendo legible antes de darlo por bueno.

La regla práctica de la casa: se guarda en PDF con capa de texto; se comprime solo la copia que se manda; y el original sin comprimir se conserva, porque comprimir dos veces seguidas convierte un documento legible en una mancha.

⏬ sigue abajo · parte 11 de 16

═══ MENSAJE 13 de 17 · 3405 caracteres ═══

*🧪 Tres pruebas antes de confiar en tu archivo*

*Prueba uno: busca una palabra que solo esté en la página cinco.* Si aparece, hay texto. Si no aparece, tienes imágenes con nombre de PDF. La prueba toma veinte segundos y dice más que cualquier configuración.

*Prueba dos: abre el archivo en otro programa.* El visor del sistema, un lector distinto, la computadora. Un PDF que solo abre en la aplicación donde se creó no es un PDF: es un archivo privado con extensión engañosa.

*Prueba tres: recupera algo de la copia.* Elige un documento al azar, bórralo del original y recupéralo del disco de respaldo. Si no lo recuperas, la copia no existe, aunque el disco esté conectado y la carpeta se vea llena.

Con esas tres pruebas, el archivo se puede llamar archivo. Sin ellas, es una carpeta con fe.

*🧷 El nombre que ordena solo*

Un esquema que funciona en cualquier teléfono y en cualquier computadora, sin programa nuevo: año, mes, día, tipo, emisor. `2026-11-02-factura-luz.pdf`, `2019-03-14-certificado-escuela.pdf`. Con ese orden alfabético, la carpeta se ordena por fecha sin tocar nada y la vista del sistema se vuelve el índice.

Dos excepciones que conviene respetar. Los documentos que se renuevan llevan al final el año de vencimiento: `2026-01-10-licencia-2030.pdf`. Y los que llegan de terceros con nombre incomprensible se renombran el mismo día en que llegan, porque el nombre original no significa nada para nadie y borra la única pista de qué son.

*🏠 El archivador en una cajita*

paperless-ngx no pide un servidor grande. Pide un equipo encendido, un disco y poco más. Las tres formas domésticas que funcionan, en orden de dificultad.

*Una computadora vieja.* La que ya nadie usa, con un sistema ligero y el archivador corriendo dentro. Ventaja: el disco es grande y barato. Desventaja: consume como una computadora y hace ruido. Se enciende por la noche y se apaga de día, y el archivador acepta ese ritmo sin queja.

*Una cajita de placa única.* Un aparato del tamaño de una caja de fósforos, con una tarjeta de memoria o un disco por USB. Consume como una bombilla, no hace ruido y se queda encendida todo el año. Es la opción que más gente termina eligiendo, y la que exige aprender un poco de terminal.

*El teléfono viejo.* Menos común y perfectamente posible con el entorno adecuado: un teléfono de repuesto enchufado, con el archivador dentro y el disco por USB. Lento para reconocer texto, suficiente para archivar y buscar.

Lo que hay que decidir antes de montar nada es una sola cosa: cuánto papel entra al mes. Con cincuenta documentos al mes, cualquier cajita sirve; con mil, el reconocimiento de texto empieza a pedir procesador y la elección cambia. Y en los dos casos, la copia del archivo sigue siendo la obligación que ningún aparato resuelve solo.

*🧾 Lo que cuesta mantener el papeleo al día*

Diez minutos al mes, tres veces, y no hay más. Primero: pasar lo que llegó en papel por el escáner y nombrarlo. Segundo: revisar que la carpeta vigilada no haya dejado documentos sin etiqueta. Tercero: actualizar la copia del mes.

Lo que rompe esa rutina no es la falta de tiempo: es dejar acumular. Un mes sin pasar papeles se resuelve en media hora; seis meses se resuelven en una tarde perdida y con documentos que ya no se sabe de qué son. El papeleo castiga la constancia con la misma dureza que la música castiga la falta de copia.

⏬ sigue abajo · parte 12 de 16

═══ MENSAJE 14 de 17 · 2238 caracteres ═══

*📌 Una nota sobre el orden de esta serie*

El papeleo cierra el primer tramo doméstico de las piezas: después de los lectores, la música y el archivo de libros, viene lo que llega sin que nadie lo pida. Y comparte con todas ellas la misma regla de lectura: un programa se juzga por la fecha de su paquete y por dónde guarda lo que toca, no por el número de estrellas que luce en la portada.

*🎚️ Y una última cosa*

Si de toda esta guía se queda una sola costumbre, que sea la de nombrar el archivo el mismo día en que llega. Es gratis, no necesita programa y es lo único que sigue funcionando cuando el lector, el escáner y el archivador ya no estén instalados.

*📎 Antes de cerrar el escritorio*

Queda dicho lo que hay y lo que falta: diez programas medidos, dos licencias con dos versiones cada una, una ausencia de paquete de seis años y una carpeta que en dos segundos contesta lo que antes costaba dos horas.

*🔗 Enlaces*

- Stirling PDF: https://github.com/Stirling-Tools/Stirling-PDF
- Tesseract: https://github.com/tesseract-ocr/tesseract
- paperless-ngx: https://github.com/paperless-ngx/paperless-ngx
- Pandoc: https://github.com/jgm/pandoc
- OCRmyPDF: https://github.com/ocrmypdf/OCRmyPDF
- OpenPDF: https://github.com/LibrePDF/OpenPDF
- Parchment: https://github.com/AhmadHassan-BTed/Parchment
- OpenNoteScanner: https://github.com/allgood/OpenNoteScanner
- book-story: https://github.com/Acclorite/book-story
- episteme: https://github.com/Aryan-Raj3112/episteme
- Lector de PDF de GrapheneOS: https://github.com/GrapheneOS/PdfViewer
- La capa de inmersión del archivo: https://github.com/gotson/komga

*Cómo se midió:* diez repositorios, tres lecturas cada uno en orden rotado —API de búsqueda, página del repositorio y contenido crudo del README y del archivo de licencia—, y una cuarta comprobación a mano para las dos licencias que la ficha automática no concluyó. Las fechas de versión se tomaron de la lista de publicaciones de cada proyecto y se contrastaron con la fecha del último empujón. Ningún campo se rellenó por memoria: los que no se pudieron leer se escriben como «sin paquete» o «sin conclusión», que es distinto de cero. Corte entre las 09:20 y las 10:35 de Santo Domingo.

⏬ sigue abajo · parte 13 de 16

═══ MENSAJE 15 de 17 · 2522 caracteres ═══

*🌅 Cierre — el papel que se convierte en archivo*

El papeleo del teléfono no lo resuelve una aplicación: lo resuelve separar tres trabajos que siempre se vendieron juntos. Capturar, reconocer y ordenar son cosas distintas, y esta mañana quedaron medidas con nombre y fecha: un escáner de ★1.544 con paquete de 2020, dos motores de texto con ★112.507 entre ambos, un archivador de ★47.563 con versión del sábado y una caja de herramientas de ★95.558 que se corre en la casa.

El reparto de estrellas vuelve a contar la misma historia que en la música: el 97 % del interés está en las herramientas que casi nadie instala en el teléfono, y el papeleo diario se hace con las pequeñas. Saber eso evita dos errores caros: creer que lo popular es lo que hace falta, y creer que lo pequeño es lo que no sirve.

*Medición del corte:* lunes 2 de noviembre de 2026, entre las 09:20 y las 10:35 de Santo Domingo · diez repositorios con las tres lecturas completas y el orden rotado · diez publicaciones consultadas una por una · dos licencias comprobadas a mano contra el archivo del repositorio.

*Licencia de esta entrega:* prosa en CC BY-SA 4.0, cifras en CC BY 4.0 y ejemplos de código en MIT; el nombre «Alexis (La Bandita)» y el sello de la casa no viajan con esas licencias ni se ceden por usarlas.

> —¿Y si nunca ordeno nada?
> —Entonces tendrás papeles, no archivo: la diferencia se nota el día que alguien te pide uno.

💓 *La Bandita informa a partir de fuentes fechadas.* Escanear no es archivar: el archivo empieza cuando el documento se puede encontrar sin abrir carpetas.

## 🗒️ Notas al pie

(2-nov) Dos discrepancias de licencia publicadas con las dos versiones: Stirling PDF (ficha NOASSERTION, archivo MIT con excepciones por partes) y OpenNoteScanner (ficha NOASSERTION, archivo GPL-3.0). No se elige la que conviene: se dicen las dos.

(2-nov) Parchment aparece con «sin paquete» porque la lista de publicaciones del proyecto está vacía al momento del corte; las ★3.590 son de la API y coincidieron con la página y con el README en las tres lecturas.

(2-nov) OpenNoteScanner tiene paquete del 22 de julio de 2020 y último empujón del 23 de abril de 2025; las dos fechas se publican juntas porque la distancia entre ellas —casi cinco años— es el dato, no el adorno.

(2-nov) Las cifras de estrellas de esta pieza son del corte de la mañana y no se redondean; la suma por grupos (★302.412 los cinco grandes, ★8.943 los cinco pequeños) se hizo sobre los valores exactos de la tabla.

⏬ sigue abajo · parte 14 de 16

═══ MENSAJE 16 de 17 · 1840 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 22*

Medí otra vez, hoy 2 de noviembre de 2026, los 13 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• PDF/A — *muerto*: el repositorio responde 404 hoy. Se nombra para esquivarlo, no se recomienda.
• Stirling-Tools/Stirling-PDF — ★95.558 · empujó en las últimas horas · NOASSERTION · última release v3.2.2 (24-oct-2026)
• tesseract-ocr/tesseract — ★77.298 · empujó en las últimas horas · Apache-2.0 · última release 5.5.4 (28-oct-2026)
• paperless-ngx/paperless-ngx — ★47.565 · empujó en las últimas horas · GPL-3.0 · última release v3.4.1 (31-oct-2026)
• jgm/pandoc — ★46.784 · empujó en las últimas horas · GPL-2.0 · última release 3.13 (26-oct-2026)
• ocrmypdf/OCRmyPDF — ★35.209 · empujó el 25-oct-2026 (hace 8 días) · MPL-2.0 · última release v17.13.0 (28-sep-2026)
• LibrePDF/OpenPDF — ★4.385 · empujó el 12-oct-2026 (hace 21 días) · NOASSERTION · última release 3.0.5 (22-may-2026)
• AhmadHassan-BTed/Parchment — ★3.595 · *dormido*: sin empujar desde el 30-jun-2026 (125 días) · Apache-2.0
• allgood/OpenNoteScanner — ★1.544 · *dormido*: sin empujar desde el 23-abr-2025 (558 días) · NOASSERTION · última release 1.0.35-fdroid (22-jul-2020)
• Acclorite/book-story — ★1.418 (+2) · empujó en las últimas horas · GPL-3.0 · última release v1.8.0 (13-oct-2025)
• Aryan-Raj3112/episteme — ★1.329 · empujó el 10-oct-2026 (hace 23 días) · AGPL-3.0 · última release v1.0.58-oss (9-oct-2026)
• GrapheneOS/PdfViewer — ★1.062 · empujó el 28-oct-2026 (hace 5 días) · MIT · última release 33 (30-jul-2026)
• gotson/komga — ★6.812 (+15) · empujó en las últimas horas · MIT · última release 1.29.2 (28-oct-2026)

💓 *LOS ENLACES · medidos hoy uno por uno*

De los 12 enlaces de esta pieza, *12 responden*.
Ninguno roto.

⏬ sigue abajo · parte 15 de 16

═══ MENSAJE 17 de 17 · 152 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.
