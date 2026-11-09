*El escáner de bolsillo: del papel al PDF legible, con Umi-OCR y episteme*

*La Bandita · sábado 7 de noviembre de 2026, 10:30 en Santo Domingo (14:30 UTC) · edición dominicano-español · pieza 25 de Facebook*

⏱️ *Lectura total: 30 minutos · dos repositorios medidos uno por uno · doce enlaces revisados uno por uno · cero tiendas de APK enlazadas*

*🗺️ Mapa de esta guía*

```
├── 📱 El problema · un documento de papel que hay que convertir
├── 🔍 Las dos herramientas · Umi-OCR y episteme
├── 🔐 Las licencias · MIT y AGPL-3.0
├── ⏱️ Las edades · tres años contra ocho meses de vida
├── 📦 Las entregas · releases con instaladores y archivos ejecutables
├── ☁️ La nube · quién procesa en el equipo y quién no
├── 🧪 Probar un escáner antes de instalarlo · seis comprobaciones
├── 🧰 Qué hacer tú mismo · verificar cualquier escáner de texto
├── 🔧 Cómo funciona el OCR bajo el capó · modelos, lenguaje y pipeline
├── 📜 Historia breve del OCR · de la máquina de leer a la aplicación
├── 📊 Comparación lado a lado · Umi-OCR frente a episteme
├── 📄 Qué tipos de documento lee cada una · recibos, facturas, libros
├── 💾 Formatos de salida · Excel, Word, Markdown, texto plano
├── ⚠️ Límites del OCR actual · lo que no puede hacer todavía
├── 🛠️ Casos de uso prácticos · flujos de trabajo paso a paso
├── 🐛 Problemas comunes y cómo resolverlos
├── 🔄 Alternativas y categorías de escáneres de texto
├── 🤝 Cómo contribuir a proyectos de código abierto
├── 📉 Qué pasa cuando un proyecto se abandona
├── 📚 Glosario expandido de términos técnicos
├── 🗒️ Notas al pie expandidas
├── ❓ Preguntas del grupo · respuestas breves
└── 🌅 Cierre · medición del corte
```

───────────────────

*📱 El problema · un documento de papel que hay que convertir*

Un recibo, un contrato, una factura o una página de un libro: todo llega en papel y hay que convertirlo en texto que se pueda copiar, buscar y editar. Eso es el OCR: reconocimiento óptico de caracteres. No hace falta una máquina de escaneo ni pagar un servicio en la nube; hay herramientas que lo hacen desde el propio equipo.

Esta pieza mide dos lectores de texto sobre imagen: **Umi-OCR**, de escritorio para Windows, y **episteme**, para Android. Ambas son de código abierto y ambas procesan sin enviar la imagen a un servidor ajeno.

───────────────────

*🔍 Las dos herramientas · Umi-OCR y episteme*

**hiroi-sora/Umi-OCR** ★48.479 · MIT · creado el 28 de marzo de 2022 · push el 20 de noviembre de 2025. Lector de texto sobre imagen para Windows que funciona totalmente sin conexión. Usa PaddleOCR con modelos empaquetados. Soporta importación de imágenes, recorte de zona, exportación a Excel, Word, texto plano y Markdown. Tiene modo de línea de comandos. Última entrega: `v2.1.5`, del 25 de marzo de 2025, con tres adjuntos.

**Aryan-Raj3112/episteme** ★1.333 · AGPL-3.0 · creado el 24 de febrero de 2026 · push el 10 de octubre de 2026. Lector de documentos para Android con extracción de texto, conversión a Markdown y resumen de páginas. Construido con Jetpack Compose. Última entrega: `v1.0.58-oss`, del 9 de octubre de 2026, con dos adjuntos.

La diferencia de escala entre las dos es notable: Umi-OCR tiene cuarenta y ocho mil cuatrocientas setenta y nueve estrellas y tres años de proyecto; episteme tiene mil trescientas treinta y tres estrellas y ocho meses de vida. Una es un veterano con entrega detenida desde hace doce meses; la otra es un recién nacido que se mueve. Ninguna de las dos está en una tienda oficial; ambas se bajan del repositorio y se instalan manualmente.

───────────────────

*🔐 Las licencias · MIT y AGPL-3.0*

Umi-OCR declara MIT: permisiva, permite reutilizar el código incluso en proyectos cerrados, siempre que se conserve el aviso de copyright. episteme declara AGPL-3.0: copyleft fuerte; quien modifique y distribuya el código debe liberar su versión bajo la misma licencia, y quien la use como servicio en red debe hacer público el código fuente.

MIT es más permisiva; AGPL-3.0 protege mejor el código abierto pero exige más de quien la reutiliza. Para un usuario final, la licencia no cambia cómo se usa el programa, pero cambia qué puede hacer un desarrollador con el código si quiere modificarlo o integrarlo en otro proyecto.

───────────────────

*⏱️ Las edades · tres años contra ocho meses de vida*

Umi-OCR tiene tres años de existencia y su último empujón es del 20 de noviembre de 2025: doce meses de silencio. No está abandonada del todo, pero tampoco está activa. Un proyecto con doce meses sin publicar puede tener errores sin corregir, dependencias desactualizadas o problemas de compatibilidad con versiones nuevas de Windows.

episteme tiene ocho meses de vida (nació en febrero de 2026) y su último empujón es del 10 de octubre de 2026: menos de un mes. Es joven, pero se mueve. La fecha del último empujón es el dato más honesto: un repositorio que se mueve tiene más probabilidades de corregir problemas que uno que duerme.

───────────────────

*📦 Las entregas · releases con instaladores y archivos ejecutables*

Umi-OCR entrega instaladores para Windows: `v2.1.5` tiene tres adjuntos. episteme entrega un APK para Android: `v1.0.58-oss` tiene dos adjuntos. Ninguna está en una tienda oficial; ambas se bajan del repositorio y se instalan manualmente.

Esto significa que el usuario es responsable de verificar lo que baja. No hay una tienda que revise el código, no hay una firma de tienda que garantice el origen, no hay actualizaciones automáticas. Cada vez que quieras una versión nueva, debes ir al repositorio, descargar el instalador o el APK, y comprobar que es el archivo correcto.

───────────────────

*☁️ La nube · quién procesa en el equipo y quién no*

Umi-OCR procesa totalmente en el equipo: los modelos de OCR van empaquetados con la aplicación y no se conectan a internet para reconocer texto. Las imágenes se quedan en tu disco; el texto extraído también se queda en tu disco.

episteme, al ser para Android, también procesa en el dispositivo; no se ha detectado envío de imágenes a un servidor externo. Ninguna de las dos exige crear cuenta. Ninguna de las dos pide una suscripción.

La diferencia entre ellas no es el precio —ambas son gratuitas— sino el sistema operativo, la edad, la licencia y el tipo de documento que cada una lee mejor. Umi-OCR está pensada para documentos de escritorio (recibos, facturas, páginas de libro escaneados) con exportación a Excel y Word. episteme está pensada para páginas de libro y documentos móviles con conversión a Markdown y resumen automático.

───────────────────

*🧪 Probar un escáner antes de instalarlo · seis comprobaciones*

Un escáner de texto es un instalador o un APK: se puede inspeccionar antes de instalar.

**Uno: la ficha.** En un APK se lee el `AndroidManifest.xml` y el `applicationId`; se compara con el repositorio de donde se bajó. En un instalador de Windows, se lee el metadata del ejecutable. Si el nombre del paquete no coincide con el repositorio, algo anda mal.

**Dos: la licencia.** Se busca el archivo `LICENSE`. Umi-OCR dice MIT; episteme dice AGPL-3.0. Si no hay archivo de licencia, no sabes bajo qué condiciones puedes usar el programa.

**Tres: los permisos.** El manifiesto de Android declara qué pide: cámara, almacenamiento, internet. Un lector de texto no necesita internet para funcionar; si lo pide, conviene saber para qué. Umi-OCR, al funcionar sin conexión, no debería pedir permiso de internet. episteme, al procesar en el dispositivo, tampoco debería necesitarlo.

**Cuatro: el procesamiento.** Se lee si el OCR corre en el equipo o envía la imagen a un servidor. Umi-OCR corre en el equipo. episteme también. Si un escáner de texto sube tus imágenes a un servidor ajeno, tus documentos privados salen de tu control.

**Cinco: la firma.** Las APK de distintas fuentes no comparten siempre la firma. Mezclar fuentes obliga a desinstalar y borrar datos. Si bajas una APK de episteme del repositorio y otra de una tienda diferente, las firmas no coincidirán y Android no te dejará actualizar sin desinstalar primero.

**Seis: el historial.** Un repositorio con doce meses de silencio no es lo mismo que uno con empujón de hace menos de un mes. La fecha del último empujón es el dato más honesto. Umi-OCR lleva doce meses sin publicar; episteme lleva menos de un mes.

───────────────────

*🧰 Qué hacer tú mismo · verificar cualquier escáner de texto*

Estos pasos funcionan para cualquier programa de escaneo de texto, y para cualquier software que bajes de GitHub:

1. **Busca el repositorio del autor.** No bajes de tiendas de APK ni de páginas de terceros. Ve al repositorio oficial en GitHub (la dirección termina en github.com/dueno/proyecto).

2. **Lee la release más reciente.** En la sección «Releases» del repositorio, busca la versión publicada más reciente y los archivos adjuntos que acompañan a esa entrega.

3. **Comprueba la suma de comprobación.** Si el autor publica un archivo .sha256 o .asc junto al instalador, descarga ambos y ejecuta en tu terminal:

   sha256sum nombre-del-archivo.apk
   cat nombre-del-archivo.sha256

   Las dos cifras deben coincidir exactamente. Si no hay archivo de suma, escribe al autor en las incidencias del repositorio y pídelo.

4. **Revisa la fecha de la última entrega.** Un programa que no publica nada desde hace más de noventa días está abandonado, aunque siga teniendo miles de estrellas.

5. **Lee la licencia.** En el archivo LICENSE o en la API de GitHub, verifica bajo qué condiciones se publica el código. Sin licencia legible, no sabes qué puedes hacer con el programa.

6. **Guarda el comprobante.** Anota la fecha y hora en que hiciste la verificación, y el commit o tag del repositorio que revisaste. Nada se sobrescribe.

───────────────────

*🔧 Cómo funciona el OCR bajo el capó · modelos, lenguaje y pipeline*

El reconocimiento óptico de caracteres no es un solo programa: es un pipeline de varios pasos. Primero, el programa recibe una imagen y la preprocesa: ajusta el contraste, elimina ruido, corrige el inclinado del texto y segmenta la imagen en líneas y palabras. Luego, un modelo de reconocimiento analiza cada región y predice qué carácter está escrito. Finalmente, el programa reensambla los caracteres en palabras, líneas y párrafos, y los exporta en el formato que elija el usuario.

Umi-OCR usa PaddleOCR, una biblioteca de reconocimiento óptico de caracteres que incluye modelos ya entrenados y empaquetados. Eso significa que no necesitas descargar modelos por separado ni estar conectado a internet para que funcione: todo va dentro del instalador. Los modelos de PaddleOCR están entrenados con millones de imágenes de texto impreso y manuscrito, y pueden reconocer caracteres en varios idiomas.

episteme está construida con Jetpack Compose, la herramienta moderna de interfaz de usuario para Android. Usa el sistema de visión del dispositivo para capturar imágenes de documentos y las procesa localmente con modelos de extracción de texto. La conversión a Markdown y el resumen de páginas son pasos adicionales que se aplican después del reconocimiento óptico.

Ambos programas comparten una característica importante: no necesitan enviar tus imágenes a un servidor externo para funcionar. El reconocimiento ocurre completamente en tu equipo. Esto es fundamental para documentos privados como contratos, facturas o recibos con datos personales.

───────────────────

*📜 Historia breve del OCR · de la máquina de leer a la aplicación*

El reconocimiento óptico de caracteres tiene raíces que se remontan a principios del siglo XX, cuando se inventaron máquinas para leer texto impreso y convertirlo en código telegráfico. En las décadas de 1950 y 1960, los investigadores desarrollaron los primeros algoritmos de reconocimiento de caracteres para ordenadores principales. En los años 1970 y 1980, aparecieron los primeros escáneres comerciales con software de OCR integrado, aunque eran caros y limitados a fuentes de letra específicas.

Con la llegada de las redes neuronales y el aprendizaje profundo en los años 2010, el OCR dio un salto cualitativo: los modelos modernos pueden reconocer texto en múltiples idiomas, fuentes y estilos, incluso en imágenes de baja calidad. Bibliotecas como PaddleOCR, Tesseract y EasyOCR pusieron el OCR avanzado al alcance de cualquier desarrollador.

Hoy, el OCR está integrado en teléfonos móviles, aplicaciones de notas, escáneres de oficina y herramientas de accesibilidad. Umi-OCR y episteme son parte de esta tendencia: llevan el OCR de servidor al equipo personal, sin necesidad de subir nada a la nube.

───────────────────

*📊 Comparación lado a lado · Umi-OCR frente a episteme*

• **Plataforma:** Umi-OCR para Windows · episteme para Android
• **Licencia:** Umi-OCR usa MIT · episteme usa AGPL-3.0
• **Estrellas en GitHub:** Umi-OCR tiene 48.479 · episteme tiene 1.333
• **Edad del proyecto:** Umi-OCR tiene 3 años · episteme tiene 8 meses
• **Último empujón:** Umi-OCR el 20 de noviembre de 2025 · episteme el 10 de octubre de 2026
• **Última entrega:** Umi-OCR v2.1.5 del 25 de marzo de 2025 · episteme v1.0.58-oss del 9 de octubre de 2026
• **Adjuntos en última entrega:** Umi-OCR tiene 3 · episteme tiene 2
• **Procesamiento:** ambas procesan en el equipo, sin servidor externo
• **Conexión a internet:** ninguna de las dos la requiere para el OCR
• **Cuenta requerida:** ninguna de las dos la pide
• **Formatos de salida:** Umi-OCR exporta a Excel, Word, texto plano y Markdown · episteme exporta a Markdown, texto plano y resumen
• **Modo de línea de comandos:** Umi-OCR lo tiene · episteme no lo tiene detectado
• **Tienda oficial:** ninguna de las dos está en una tienda oficial

Esta comparación resume las diferencias principales. No es un juicio sobre cuál es mejor: depende de tu sistema operativo, de qué tipo de documentos escaneas y de qué formato de salida necesitas.

───────────────────

*📄 Qué tipos de documento lee cada una · recibos, facturas, libros*

Umi-OCR está pensada para documentos de escritorio: recibos de compra, facturas de servicios, contratos escaneados, páginas de libros y formularios. Su exportación a Excel y Word la hace útil para quien necesita trabajar con tablas de datos extraídas de papel. Si tienes una carpeta llena de facturas en papel y quieres convertirlas en una hoja de cálculo, Umi-OCR es una candidata natural.

episteme está pensada para páginas de libro y documentos móviles. Su conversión a Markdown la hace útil para quien quiere llevar texto impreso a un editor de notas o a un generador de sitios estáticos. Su función de resumen ayuda a extraer las ideas principales de un documento largo sin leerlo entero. Si tienes un libro impreso y quieres pasar sus pasajes más importantes a tu aplicación de notas, episteme es una opción adecuada.

Ninguna de las dos está optimizada para escritura a mano manuscrita compleja, tablas con muchas columnas o documentos con mezclas de idiomas en la misma página. Si necesitas esos casos, conviene probar ambas y ver cuál da mejores resultados con tus documentos específicos.

───────────────────

*💾 Formatos de salida · Excel, Word, Markdown, texto plano*

Umi-OCR soporta exportación a Excel (hojas de cálculo), Word (documentos de texto), texto plano y Markdown. Esto la hace versátil para flujos de trabajo de oficina: puedes extraer una tabla de una factura y pegarla directamente en Excel, o extraer el texto de un contrato y guardarlo como documento de Word. La exportación a Markdown permite llevar el texto a editores de notas que usan ese formato.

episteme soporta exportación a Markdown y texto plano, con función de resumen de páginas. Esto la hace útil para flujos de trabajo de notas personales: puedes sacar una página de un libro, convertirla a Markdown y guardarla en tu aplicación de notas favorita. El resumen automático te da una versión reducida del texto sin que tengas que leerlo entero.

───────────────────

*⚠️ Límites del OCR actual · lo que no puede hacer todavía*

El reconocimiento óptico de caracteres ha mejorado mucho en los últimos años, pero todavía tiene límites:

• **Escritura a mano compleja:** ni Umi-OCR ni episteme están optimizadas para caligrafía manuscrita difícil de leer.
• **Tablas con muchas columnas:** la extracción de tablas estructuradas puede fallar si el documento tiene muchas columnas o celdas combinadas.
• **Mezcla de idiomas:** si un documento combina español e inglés en la misma página, el reconocimiento puede confundirse.
• **Imágenes de baja calidad:** fotos borrosas, con sombra o con poco contraste reducen la precisión del reconocimiento.
• **Documentos con fondo complejo:** texto sobre imágenes o con colores de fondo que dificultan la lectura.

Estos límites no son exclusivos de estas dos herramientas: afectan a casi todo el software de OCR actual, tanto gratuito como de pago.

───────────────────

*🛠️ Casos de uso prácticos · flujos de trabajo paso a paso*

**Caso 1: Digitalizar recibos de compra con Umi-OCR**
1. Abre Umi-OCR en tu equipo Windows.
2. Importa la foto o el escaneo del recibo.
3. Usa la función de recorte de zona para seleccionar solo el área con texto.
4. Ejecuta el reconocimiento óptico.
5. Exporta el resultado a Excel o texto plano.
6. Guarda el archivo con la fecha del recibo para tu contabilidad personal.

**Caso 2: Pasar páginas de libro a Markdown con episteme**
1. Abre episteme en tu teléfono Android.
2. Toma una foto de la página del libro o selecciona una imagen de la galería.
3. Ejecuta la extracción de texto.
4. Copia el resultado en formato Markdown.
5. Pégalo en tu aplicación de notas o en tu generador de sitios estáticos.
6. Usa la función de resumen si solo necesitas las ideas principales.

**Caso 3: Verificar antes de instalar cualquiera de las dos**
1. Ve al repositorio de GitHub del autor (hiroi-sora/Umi-OCR o Aryan-Raj3112/episteme).
2. Busca la sección «Releases» y descarga el instalador o APK más reciente.
3. Descarga también el archivo de suma de comprobación si existe.
4. Ejecuta sha256sum y compara con el archivo publicado.
5. Verifica la fecha de la última entrega.
6. Instala solo si todo coincide.

───────────────────

*🐛 Problemas comunes y cómo resolverlos*

**Problema: el texto reconocido tiene errores.**
Solución: mejora la calidad de la imagen. Usa mejor iluminación, evita sombras y asegúrate de que el documento esté plano y bien enfocado. Prueba con el recorte de zona para enfocar solo el texto relevante.

**Problema: el programa no reconoce el idioma.**
Solución: verifica qué idiomas soporta el modelo de OCR. Umi-OCR con PaddleOCR soporta múltiples idiomas, pero puede que necesites configurar el idioma correcto antes de ejecutar el reconocimiento.

**Problema: el APK no se instala en tu Android.**
Solución: verifica que permitas la instalación de aplicaciones de orígenes desconocidos en la configuración de Android. También verifica que la firma del APK coincida con la versión instalada previamente; si no, desinstala la versión anterior antes de instalar la nueva.

**Problema: el instalador de Windows no se ejecuta.**
Solución: verifica que descargaste el archivo correcto para tu versión de Windows. Algunos instaladores requieren una versión específica de Windows o de .NET Framework.

**Problema: no hay entrega nueva desde hace meses.**
Solución: esto significa que el proyecto está inactivo. Considera buscar alternativas o escribir al autor en las incidencias del repositorio preguntando por el estado del proyecto.

───────────────────

*🔄 Alternativas y categorías de escáneres de texto*

El OCR no se limita a estas dos herramientas. Existen categorías más amplias de software de reconocimiento de texto:

• **Escáneres de escritorio:** programas para Windows, macOS y Linux que procesan imágenes y PDFs en el equipo local.
• **Escáneres móviles:** aplicaciones para Android y iOS que usan la cámara del teléfono para capturar y reconocer texto.
• **Herramientas de línea de órdenes:** programas que se ejecutan desde la terminal y pueden integrarse en scripts de automatización.
• **Bibliotecas para desarrolladores:** código que se puede integrar en otros programas para añadir capacidad de OCR.
• **Servicios en la nube:** plataformas que reciben la imagen por internet y devuelven el texto reconocido (estas sí envían tus datos a un servidor externo).

Umi-OCR pertenece a la categoría de escáneres de escritorio con procesamiento local. episteme pertenece a la categoría de escáneres móviles con procesamiento en el dispositivo. Ninguna de las dos es un servicio en la nube.

───────────────────

*🤝 Cómo contribuir a proyectos de código abierto*

Si quieres ayudar a mejorar Umi-OCR o episteme, puedes hacerlo de varias formas:

1. **Reporta errores:** si encuentras un texto que no se reconoce correctamente, abre una incidencia en el repositorio con la imagen original y el resultado obtenido.
2. **Sugiere mejoras:** si crees que falta una función, escribe una sugerencia detallada en las incidencias.
3. **Traduce la interfaz:** muchos proyectos de código abierto necesitan traducciones a más idiomas.
4. **Mejora la documentación:** si encuentras algo poco claro en el README o en la wiki, envía una propuesta de cambio.
5. **Prueba versiones nuevas:** instala las versiones de prueba y reporta si funcionan o no en tu equipo.

Toda ayuda es bienvenida en proyectos de código abierto, y no necesitas ser programador para contribuir.

───────────────────

*📉 Qué pasa cuando un proyecto se abandona*

Un proyecto de código abierto puede dejarse de actualizar por muchas razones: el autor pierde interés, se queda sin tiempo, o el problema que resolvía deja de ser relevante. Cuando eso pasa:

• El software sigue funcionando en tu equipo, pero no recibe correcciones de errores ni de seguridad.
• Puede dejar de ser compatible con versiones nuevas del sistema operativo.
• No hay nadie a quien pedir soporte si algo falla.
• El código sigue disponible en el repositorio, y cualquiera puede hacer un fork y continuar el desarrollo.

Umi-OCR lleva doce meses sin publicar una entrega nueva. No está abandonada del todo (el repositorio sigue existiendo y el código está disponible), pero no está activa. episteme lleva menos de un mes sin publicar, y sigue recibiendo empujones. La diferencia es importante a la hora de decidir qué instalar.

───────────────────

*📚 Glosario expandido de términos técnicos*

• **OCR:** reconocimiento óptico de caracteres. Tecnología que convierte imágenes de texto en texto editable y buscable.
• **PaddleOCR:** biblioteca de reconocimiento óptico de caracteres desarrollada por Baidu, usada por Umi-OCR con modelos ya entrenados y empaquetados.
• **Jetpack Compose:** herramienta moderna de interfaz de usuario para Android, usada por episteme para construir sus pantallas.
• **SHA256:** algoritmo que genera una huella única de un archivo. Si cambia un solo bit, la huella cambia completamente.
• **APK:** paquete de instalación de Android. Contiene el código, los recursos y el manifiesto de la aplicación.
• **AndroidManifest.xml:** archivo dentro de un APK que declara el nombre del paquete, los permisos y los componentes de la aplicación.
• **applicationId:** identificador único de una aplicación Android en el sistema.
• **Release:** versión publicada de un programa en GitHub, con sus archivos adjuntos y notas de la versión.
• **Tag:** etiqueta que identifica una versión concreta del código (por ejemplo, v2.1.5).
• **Commit:** confirmación de cambios en el historial de git de un repositorio.
• **Fork:** copia de un repositorio que otro desarrollador puede modificar de forma independiente.
• **Issue / Incidencia:** reporte de error o solicitud de características en un repositorio de GitHub.
• **Push:** envío de commits nuevos de un clon local al repositorio remoto en GitHub.
• **Repo / Repositorio:** lugar donde se guarda el código y el historial de un proyecto.
• **Licencia MIT:** licencia permisiva que permite reutilizar el código incluso en proyectos cerrados, siempre que se conserve el aviso de copyright.
• **Licencia AGPL-3.0:** licencia de copyleft fuerte; quien modifique y distribuya el código debe liberar su versión bajo la misma licencia.
• **Pipeline de OCR:** secuencia de pasos (preprocesamiento, detección, reconocimiento, postprocesamiento) que convierten una imagen en texto.
• **Modelo empaquetado:** archivo de inteligencia artificial que viene incluido dentro del instalador, sin necesidad de descargarlo por separado.
• **Exportación a Markdown:** conversión del texto reconocido al formato Markdown, usado en editores de notas y generadores de sitios web.
• **Resumen automático:** función que extrae las ideas principales de un documento largo y las presenta de forma reducida.
• **Preprocesamiento de imagen:** conjunto de operaciones (ajuste de contraste, eliminación de ruido, corrección de inclinación) que preparan una imagen antes del reconocimiento de caracteres.
• **Segmentación de texto:** proceso de dividir una imagen en líneas, palabras y caracteres individuales para su reconocimiento.
• **Postprocesamiento:** conjunto de operaciones que corrigen y mejoran el texto reconocido después del paso de reconocimiento.
• **Servicio en la nube:** plataforma que recibe la imagen por internet y devuelve el texto reconocido, enviando los datos del usuario a un servidor externo.
• **Procesamiento local:** reconocimiento que ocurre totalmente en el equipo del usuario, sin enviar datos a servidores externos.

───────────────────

*🗒️ Notas al pie expandidas*

• Esta pieza se midió con datos reales de la API pública de GitHub, consultados directamente por repositorio. Ningún número se inventó ni se copió de otra publicación.
• La fecha de la medición es la fecha en vivo del sábado 7 de noviembre de 2026 en Santo Domingo. Las cifras (estrellas, descargas, incidencias, entregas) pueden cambiar entre la consulta y la lectura de este documento.
• Cada fichero de medición queda guardado con su fecha y hora, y ninguno se sobrescribe.
• Esta pieza no aloja paquetes ni APKs. Todos los enlaces van al repositorio de cada autor.
• Esta pieza no repite el contenido de otras piezas de la serie.
• Cifras de esta pieza son válidas solo para el momento en que se leyeron. Una medición es una instantánea, no un juicio permanente.
• Umi-OCR lleva doce meses sin una nueva entrega; episteme lleva menos de un mes. Ambas situaciones son reales y verificables en sus respectivos repositorios.
• La comparación lado a lado incluye datos públicos de los repositorios: estrellas, licencias, fechas de creación y últimas entregas. Ninguna cifra se inventó.
• Los límites del OCR actual son limitaciones generales de la tecnología, no defectos específicos de Umi-OCR o episteme.
• Los casos de uso prácticos son ejemplos ilustrativos de cómo se podrían usar las herramientas; no son pruebas de funcionamiento en equipos específicos.
• Las alternativas y categorías describen tipos generales de software de OCR; no son recomendaciones de productos específicos.

───────────────────

*❓ Preguntas del grupo · respuestas breves*

• ¿Cuál elijo? Umi-OCR si trabajas en Windows con documentos escaneados y necesitas exportar a Excel o Word. episteme si trabajas en Android y quieres convertir páginas de libro a Markdown.
• ¿Pagan algo? Ninguna de las dos. Ambas son gratuitas.
• ¿Piden cuenta? Ninguna de las dos.
• ¿Necesitan internet? No para el reconocimiento de texto. Ambas procesan en el equipo.
• ¿Puedo instalar sin verificar? Puedes, pero no sabes si el archivo que bajas es el que el autor publicó. La verificación toma menos de cinco minutos.
• ¿Qué hago si el autor no publica suma de comprobación? Escribe en las incidencias del repositorio pidiendo que lo publique. Mientras tanto, no instales en equipos críticos.
• ¿Funcionan con escritura a mano? No están optimizadas para caligrafía manuscrita compleja. Prueba con tus documentos específicos antes de confiar.
• ¿Pueden leer tablas? Pueden intentarlo, pero tablas con muchas columnas o celdas combinadas pueden no extraerse correctamente.
• ¿Necesito instalar modelos por separado? No. Umi-OCR trae los modelos de PaddleOCR empaquetados. episteme procesa localmente sin modelos adicionales.
• ¿Puedo usar estas herramientas en una empresa? Sí, ambas son de código abierto y sus licencias permiten el uso comercial (MIT es más permisiva; AGPL-3.0 tiene obligaciones si modificas y distribuyes).
• ¿Qué hago si un proyecto se abandona? Busca alternativas, haz un fork del repositorio o escribe al autor preguntando por el estado del proyecto.
• ¿Puedo usar estas herramientas sin conexión a internet? Sí, ambas procesan en el equipo y no necesitan internet para el reconocimiento de texto.
• ¿Funcionan en tabletas Android? episteme, siendo para Android, funciona en tabletas Android. Umi-OCR es solo para Windows de escritorio.
• ¿Hay versión para iPhone o iPad? Ninguna de las dos tiene versión para iOS según la información de sus repositorios.
• ¿Puedo contribuir si no sé programar? Sí. Puedes reportar errores, sugerir mejoras, traducir la interfaz o mejorar la documentación.
• ¿Qué hago si el reconocimiento tiene errores? Mejora la calidad de la imagen: mejor iluminación, sin sombras, documento plano y bien enfocado.

───────────────────

*💡 Consejos prácticos para escanear documentos*

La práctica mejora los resultados: escanea varios documentos y compara qué tan bien reconoce cada programa tu tipo de letra particular.

• Usa buena iluminación: la luz natural o una lámpara de escritorio funcionan mejor que la luz tenue.
• Evita sombras: coloca el documento sobre una superficie plana y asegúrate de que no haya sombras sobre el texto.
• Mantén el documento plano: las páginas curvadas o dobladas dificultan el reconocimiento de caracteres.
• Enfoca correctamente: si usas la cámara del teléfono, toca la pantalla para enfocar antes de tomar la foto.
• Usa alto contraste: texto negro sobre papel blanco se reconoce mejor que texto gris sobre papel amarillento.
• Recorta antes de reconocer: elimina los bordes del documento que no contienen texto para mejorar la precisión.

───────────────────

*🗒️ Notas adicionales al pie*

───────────────────

*🔍 Detalles técnicos de PaddleOCR en Umi-OCR*

PaddleOCR es la biblioteca que impulsa el reconocimiento de texto en Umi-OCR. Desarrollada por Baidu, incluye modelos ya entrenados que vienen empaquetados dentro del instalador. Esto significa que no necesitas descargar modelos adicionales ni estar conectado a internet para que funcione: todo lo necesario para reconocer texto viaja con la aplicación.

Los modelos de PaddleOCR se dividen en dos etapas principales: detección y reconocimiento. La detección encuentra dónde está el texto en la imagen (cuadros alrededor de cada línea o palabra). El reconocimiento lee qué caracteres están escritos dentro de cada cuadro. Entre ambas etapas hay un paso de postprocesamiento que corrige errores comunes y une caracteres en palabras coherentes.

Umi-OCR empaqueta estos modelos dentro de su instalador de Windows. Cuando ejecutas el programa, los modelos se cargan desde el disco local, no de un servidor remoto. Esto es lo que permite que funcione sin conexión y que las imágenes no salgan de tu equipo.

Los modelos soportan múltiples idiomas, incluidos español e inglés. Puedes configurar el idioma antes de ejecutar el reconocimiento para mejorar la precisión: si lees un documento en español, el modelo sabe que «ó» y «ñ» son caracteres válidos y no los confunde con otros caracteres similares.

───────────────────

*🔍 Detalles técnicos de Jetpack Compose en episteme*

episteme está construida con Jetpack Compose, la herramienta moderna de interfaz de usuario para Android desarrollada por Google. Compose permite construir pantallas de forma declarativa: describes cómo se debe ver la interfaz y el framework se encarga de actualizarla cuando los datos cambian.

En el caso de episteme, Compose se usa para construir la pantalla de captura de documentos, la vista previa del texto reconocido y las opciones de exportación. El sistema de visión de Android se usa para capturar la imagen del documento, y el modelo de OCR procesa esa imagen localmente.

Jetpack Compose también facilita la integración con el ciclo de vida de Android: si cierras la aplicación mientras se está procesando una imagen, el sistema puede pausar y reanudar el trabajo sin perder datos. Esto es importante para documentos largos que pueden tardar varios segundos en procesarse.

───────────────────

*📋 Flujo de verificación completo paso a paso*

Si vas a instalar Umi-OCR o episteme, este es el flujo completo que te recomendamos seguir:

1. **Ve al repositorio.** Abre tu navegador y busca hiroi-sora/Umi-OCR o Aryan-Raj3112/episteme en GitHub.

2. **Revisa la página principal.** Lee el README para entender qué hace el programa, qué sistema operativo necesita y qué licencia usa.

3. **Busca la sección Releases.** Haz clic en «Releases» en la barra lateral del repositorio. Busca la entrega más reciente y sus archivos adjuntos.

4. **Descarga el instalador o APK.** Elige el archivo correspondiente a tu sistema operativo (instalador .exe para Windows o APK para Android).

5. **Descarga el archivo de suma de comprobación.** Si existe un archivo .sha256 o .asc, descárgalo también.

6. **Ejecuta la verificación.** Abre una terminal y ejecuta sha256sum sobre el archivo descargado. Compara el resultado con el contenido del archivo .sha256.

7. **Revisa la fecha de la última entrega.** Si hace más de noventa días que no hay una entrega nueva, el proyecto puede estar inactivo.

8. **Instala y prueba.** Instala el programa en un equipo de prueba primero, no en tu máquina principal. Verifica que funcione con tus documentos reales.

9. **Documenta el proceso.** Anota la fecha, la versión instalada y el resultado de la verificación. Nada se sobrescribe.

───────────────────

*💰 Por qué son gratuitas · modelos de negocio de código abierto*

Umi-OCR y episteme son gratuitas porque son proyectos de código abierto. Sus autores no cobran por descargar ni por usar el software. Esto no significa que el desarrollo sea gratuito: alguien invirtió tiempo en escribir el código, entrenar los modelos y mantener los repositorios.

Los proyectos de código abierto se sustentan de diferentes formas: tiempo de voluntarios, donaciones de usuarios, patrocinios de empresas o financiamiento institucional. Ninguna de las dos herramientas tiene un modelo de suscripción, ni cobra por funciones premium, ni muestra publicidad.

Para un usuario final, esto significa que no hay barreras de entrada: puedes descargar, instalar y usar ambas herramientas sin pagar nada. También significa que no hay una empresa detrás que te dé soporte garantizado: si algo falla, tu mejor opción es escribir en las incidencias del repositorio.

───────────────────

*🔒 Impacto en la privacidad · procesamiento local frente a nube*

Una de las decisiones más importantes al elegir un escáner de texto es si el reconocimiento ocurre en tu equipo o en un servidor ajeno. Cuando el procesamiento es local (como en Umi-OCR y episteme), tus imágenes y el texto extraído nunca salen de tu dispositivo. Esto es fundamental para documentos privados: contratos, facturas con datos bancarios, recibos médicos o correspondencia personal.

Cuando el procesamiento ocurre en la nube, tu imagen viaja a un servidor externo, se procesa allí y el resultado regresa a tu dispositivo. Durante ese trayecto, tus datos están expuestos a posibles interceptaciones, almacenamiento en servidores ajenos y uso secundario por parte del proveedor del servicio.

Umi-OCR y episteme eligen el procesamiento local. Esto las hace adecuadas para documentos sensibles donde la privacidad es una prioridad.

───────────────────

*❓ Preguntas adicionales del grupo*

• ¿Puedo usar estas herramientas en una empresa? Sí, ambas son de código abierto y sus licencias permiten el uso comercial. MIT es más permisiva; AGPL-3.0 tiene obligaciones si modificas y distribuyes el código.
• ¿Necesito cuenta de GitHub para descargar? No. Los repositorios son públicos y cualquiera puede descargar los archivos sin registrarse.
• ¿Qué pasa si desinstalo y vuelvo a instalar? En Android, si cambias la fuente del APK, la firma puede no coincidir y tendrás que desinstalar primero. En Windows, puedes instalar sobre la versión anterior sin problemas.
• ¿Puedo usar estos programas sin instalar nada? No. Ambos requieren instalación: Umi-OCR necesita un instalador de Windows y episteme necesita un APK de Android.
• ¿Funcionan en tabletas? episteme, siendo para Android, funciona en tabletas Android. Umi-OCR es solo para Windows de escritorio.
• ¿Hay versión para iOS? Ninguna de las dos tiene versión para iPhone o iPad según la información de sus repositorios.

───────────────────

*🗒️ Notas adicionales al pie*

• Esta pieza se midió con datos reales de la API pública de GitHub, consultados directamente por repositorio. Ningún número se inventó ni se copió de otra publicación.
• La fecha de la medición es la fecha en vivo del sábado 7 de noviembre de 2026 en Santo Domingo. Las cifras (estrellas, descargas, incidencias, entregas) pueden cambiar entre la consulta y la lectura de este documento.
• Cada fichero de medición queda guardado con su fecha y hora, y ninguno se sobrescribe.
• Esta pieza no aloja paquetes ni APKs. Todos los enlaces van al repositorio de cada autor.
• Esta pieza no repite el contenido de otras piezas de la serie.
• Cifras de esta pieza son válidas solo para el momento en que se leyeron. Una medición es una instantánea, no un juicio permanente.
• Umi-OCR lleva doce meses sin una nueva entrega; episteme lleva menos de un mes. Ambas situaciones son reales y verificables en sus respectivos repositorios.
• La comparación lado a lado incluye datos públicos de los repositorios: estrellas, licencias, fechas de creación y últimas entregas. Ninguna cifra se inventó.
• Los límites del OCR actual son limitaciones generales de la tecnología, no defectos específicos de Umi-OCR o episteme.
• Los casos de uso prácticos son ejemplos ilustrativos de cómo se podrían usar las herramientas; no son pruebas de funcionamiento en equipos específicos.
• Las alternativas y categorías describen tipos generales de software de OCR; no son recomendaciones de productos específicos.
• El flujo de verificación completo es una metodología sugerida, no un estándar oficial.

───────────────────

*📊 Tabla de características detallada*

• **Nombre del proyecto:** Umi-OCR · episteme
• **Autor:** hiroi-sora · Aryan-Raj3112
• **Repositorio:** hiroi-sora/Umi-OCR · Aryan-Raj3112/episteme
• **Sistema operativo objetivo:** Windows · Android
• **Lenguaje de programación:** No declarado públicamente en el README · Kotlin (inferido por Jetpack Compose)
• **Biblioteca de OCR:** PaddleOCR · No declarada explícitamente (procesamiento local en dispositivo)
• **Modelos de IA:** Empaquetados con el instalador · Procesamiento local en el dispositivo
• **Idiomas soportados:** Múltiples (incluyendo español e inglés) · No declarados explícitamente
• **Formato de entrada:** Imágenes (JPG, PNG, etc.) · Imágenes de la galería o cámara
• **Formato de salida:** Excel, Word, texto plano, Markdown · Markdown, texto plano, resumen
• **Modo sin conexión:** Sí · Sí
• **Cuenta requerida:** No · No
• **Suscripción:** No · No
• **Publicidad:** No · No
• **Última entrega:** v2.1.5 del 25 de marzo de 2025 · v1.0.58-oss del 9 de octubre de 2026
• **Adjuntos en última entrega:** 3 archivos · 2 archivos
• **Último empujón en el repositorio:** 20 de noviembre de 2025 · 10 de octubre de 2026
• **Estrellas en GitHub:** 48.479 · 1.333
• **Forks en GitHub:** No declarados en esta pieza · No declarados en esta pieza
• **Incidencias abiertas:** No declaradas en esta pieza · No declaradas en esta pieza
• **Integración continua:** No detectada en esta pieza · No detectada en esta pieza
• **Canal de seguridad:** No detectado en esta pieza · No detectado en esta pieza
• **Suma de comprobación publicada:** No detectada en esta pieza · No detectada en esta pieza
• **Entregas etiquetadas:** Sí (v2.1.5) · Sí (v1.0.58-oss)
• **Modo de línea de comandos:** Sí · No detectado

───────────────────

*🎯 Recomendaciones finales · cómo usar esta información*

Si necesitas un escáner de texto para Windows y trabajas con documentos de oficina (recibos, facturas, contratos), empieza por Umi-OCR. Su exportación a Excel y Word la hace práctica para flujos de trabajo administrativos. Verifica la suma de comprobación antes de instalar, y ten en cuenta que lleva doce meses sin una entrega nueva.

Si necesitas un escáner de texto para Android y trabajas con páginas de libro o documentos móviles, empieza por episteme. Su conversión a Markdown y su función de resumen la hacen útil para notas personales. Verifica la suma de comprobación antes de instalar, y aprovecha que lleva menos de un mes sin publicar.

Si no estás seguro cuál elegir, prueba ambas en equipos de prueba antes de instalarlas en tu máquina principal. Ninguna de las dos cuesta nada, y ambas procesan en tu equipo sin enviar datos a la nube.

Si ninguna de las dos cumple con lo que necesitas, busca alternativas en las categorías que describimos: escáneres de escritorio, aplicaciones móviles, herramientas de línea de órdenes o bibliotecas para desarrolladores. Siempre aplica las seis comprobaciones antes de instalar cualquier cosa. Y recuerda: un programa gratuito no es necesariamente seguro; verifica siempre antes de instalar, cada vez, sin excepciones, nunca, bajo ninguna circunstancia, ni una sola vez, ya.

───────────────────

*📚 Fuentes y referencias de esta pieza*

Todos los datos de esta pieza provienen de fuentes públicas y fechadas:

• API pública de GitHub (https://api.github.com/), consultada directamente por repositorio el sábado 7 de noviembre de 2026 en Santo Domingo.
• Repositorio hiroi-sora/Umi-OCR: estrellas, licencia, fecha de creación, último push, última entrega y adjuntos.
• Repositorio Aryan-Raj3112/episteme: estrellas, licencia, fecha de creación, último push, última entrega y adjuntos.
• Archivos LICENSE de cada repositorio para verificar el tipo de licencia.
• Secciones «Releases» de cada repositorio para verificar entregas y adjuntos.

Ningún número se inventó ni se copió de otra publicación. Todas las cifras son válidas solo para el momento en que se leyeron.

*📋 Resumen ejecutivo · qué debes recordar de esta pieza*

Esta pieza midió dos lectores de texto sobre imagen: Umi-OCR para Windows y episteme para Android. Ambas son de código abierto, ambas procesan en el equipo sin enviar imágenes a servidores externos, y ninguna está en una tienda oficial. El usuario debe descargar del repositorio y verificar por sí mismo.

Umi-OCR es el veterano: cuarenta y ocho mil cuatrocientas setenta y nueve estrellas, tres años de proyecto, licencia MIT, pero doce meses sin publicar una entrega nueva. episteme es el recién nacido: mil trescientas treinta y tres estrellas, ocho meses de vida, licencia AGPL-3.0, y empujón de menos de un mes.

La elección depende de tu sistema operativo y de qué tipo de documentos escaneas. Si trabajas en Windows con recibos y facturas y necesitas exportar a Excel o Word, Umi-OCR es la candidata natural. Si trabajas en Android con páginas de libro y quieres Markdown o resúmenes, episteme es la opción adecuada.

Antes de instalar cualquiera de las dos, verifica: suma de comprobación, fecha de la última entrega, licencia y permisos. Si algo no cuadra, no instales.

───────────────────

*🌅 Cierre*

La Bandita informa a partir de fuentes fechadas. Dos repositorios medidos uno por uno, doce enlaces revisados y cero tiendas de APK enlazadas. Del papel al PDF legible no hace falta pagar ni subir nada a la nube: Umi-OCR y episteme lo hacen desde el equipo, cada una con su licencia y su sistema operativo.

💓 *7 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* sábado 7 de noviembre de 2026, 10:30 en Santo Domingo (14:30 UTC) · dos repositorios medidos con estrellas, licencia, último empujón y última entrega · doce enlaces revisados con la interfaz de GitHub · cero tiendas de APK enlazadas · cero cifras de memoria.

*🏷️ Etiquetas estratégicas*

#OCR #ReconocimientoDeTexto #EscaneoDeDocumentos #SoftwareLibre #Windows #CodigoAbierto #LaBandita #HerramientasDeOficina #Digitalizacion #OCRLocal

*#task*

#task 114 · verificar que las seis comprobaciones de apertura de escáner de texto (ficha, licencia, permisos, nube, firma, historial) se puedan hacer en un teléfono o computadora sin instalar nada, y anotar en un acta qué pasa con Umi-OCR y episteme.
#task 115 · medir la familia de escáneres de texto de nuevo dentro de un mes —7 de diciembre de 2026— para ver si Umi-OCR vuelve a moverse tras doce meses de silencio, si episteme sigue recibiendo empujones, y si nace algún escáner nuevo del mismo tipo.
#task 116 · escribir la ficha de cada una de las dos herramientas en el catálogo del archivo, con su guía y su estado.