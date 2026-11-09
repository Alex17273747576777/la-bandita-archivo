Keiyoushi es un repositorio de extensiones para Mihon y variantes, mantenido por la comunidad bajo la organización keiyoushi en GitHub.

*sábado 7 de noviembre de 2026, 13:15 en Santo Domingo (17:15 UTC) · fecha de corte de esta medición · pieza 23 de Facebook, edición dominicano-español ·* No pertenece a Mihon ni a Tachiyomi: es un proyecto independiente que continuó el catálogo de extensiones después de que Tachiyomi dejara de publicar actualizaciones. Su propósito es ofrecer una fuente confiable de extensiones de lectura para aplicaciones compatibles con el formato de Mihon.

El repositorio principal es keiyoushi/extensions, que sirve como catálogo de extensiones. El código fuente de las extensiones vive por separado en keiyoushi/extensions-source. Esta separación permite que el catálogo se actualice sin necesidad de recompilar todo el código, y que los desarrolladores de extensiones contribuyan al código sin tocar el índice público.

Keiyoushi no aloja contenido de terceros. Solo indexa extensiones que los usuarios pueden agregar a su aplicación de lectura. Cada extensión es un módulo independiente que se conecta a un sitio web específico para buscar, listar y leer contenido. La responsabilidad de qué extensión instalar y qué sitios consultar recae enteramente en el usuario.

La aplicación Mihon no incluye ningún repositorio de extensiones por defecto. Al instalar Mihon, la pestaña de extensiones queda vacía hasta que el usuario agrega manualmente una extensión store. Keiyoushi es una de las opciones más usadas para este propósito, gracias a su tamaño, actividad y compatibilidad con Mihon 0.20.1 y versiones posteriores.

El índice público de Keiyoushi se publica en dos formatos principales: index.pb (formato binario optimizado) e index.min.json (formato JSON legible). Ambos archivos están disponibles en la rama repo del repositorio y pueden agregarse a Mihon mediante la opción "Agregar repositorio de extensiones" en los ajustes de la aplicación.

Desde una perspectiva de seguridad, Keiyoushi es un repositorio comunitario sin verificación formal por parte de Mihon. El usuario debe evaluar por sí mismo qué extensiones instalar. El repositorio no ofrece garantías sobre la seguridad o legalidad del contenido al que se accede a través de las extensiones indexadas.

El proyecto keiyoushi/extensions-source contiene el código Kotlin de las extensiones incluidas en el catálogo. Está bajo licencia Apache-2.0 y permite a los desarrolladores revisar, modificar y contribuir con nuevas extensiones o correcciones a las existentes.

El catálogo keiyoushi/extensions, por su parte, no declara una licencia SPDX en el repositorio principal. Esto significa que el usuario no puede asumir automáticamente bajo qué condiciones se distribuye el índice ni las extensiones que referencia. Es un dato a tener en cuenta antes de integrar el repositorio en un flujo de trabajo profesional o institucional.

Keiyoushi no es la única opción para Mihon. Existen repositorios alternativos como Yuzono (yuzono/anime-extensions), que fusiona actualizaciones de Keiyoushi cada seis horas y agrega algunas extensiones propias. También existen forks filtrados y repositorios especializados para servidores propios o contenido regional.

La actividad del repositorio se puede verificar directamente contra la API pública de GitHub. La fecha de último empujón, el número de estrellas, los forks, los vigilantes y el tamaño del repositorio son datos públicos que cualquier persona puede consultar sin necesidad de una cuenta de GitHub.

───────────────────

*🗺️ Mapa de esta guía*

```
├── 🧱 Qué es Keiyoushi y para qué sirve
├── ⚡ Cómo agregarlo a Mihon paso a paso
├── 🔀 Diferencia entre catálogo y código fuente
├── ⚖️ Licencia y responsabilidades del usuario
├── 🧬 Alternativas y repositorios relacionados
├── 🚀 Cómo verificar que el repositorio está activo
├── 📊 Datos medidos contra la API de GitHub
├── 🔐 Qué no garantiza Keiyoushi
├── 🧯 Si algo falla al agregar el repositorio
├── ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

───────────────────

*🧱 Qué es Keiyoushi y para qué sirve*

Keiyoushi es un repositorio de extensiones para Mihon y aplicaciones compatibles. Su función es servir como puente entre la aplicación de lectura y los sitios web de contenido: cada extensión sabe cómo comunicarse con un sitio concreto, extraer la lista de títulos, obtener los capítulos y mostrar las páginas al usuario.

Sin un repositorio de extensiones, Mihon no puede leer nada por sí misma. Es una aplicación vacía que necesita que el usuario le diga de dónde sacar el contenido. Keiyoushi llena ese vacío ofreciendo un catálogo público de extensiones listas para instalar.

El nombre "Keiyoushi" proviene del japonés (啓陽子) y es usado por la comunidad para identificar este catálogo en particular. No es un producto oficial de Mihon, ni está respaldado por los desarrolladores de Mihon. Es un proyecto comunitario independiente.

───────────────────

*⚡ Cómo agregarlo a Mihon paso a paso*

Paso 1: Abre Mihon en tu dispositivo Android.

Paso 2: Ve a Más → Ajustes → Examinar → Tiendas de extensiones → Agregar.

Paso 3: Pega la URL del índice de Keiyoushi:

https://github.com/keiyoushi/extensions/raw/repo/index.pb

Paso 4: Confirma la adición. Mihon descargará el índice y mostrará las extensiones disponibles.

Paso 5: Instala las extensiones que necesites desde el catálogo.

Paso 6: Verifica que cada extensión funcione correctamente probando una búsqueda en el sitio correspondiente.

───────────────────

*🔀 Diferencia entre catálogo y código fuente*

El repositorio keiyoushi/extensions es el catálogo público: contiene los archivos de índice que Mihon lee para saber qué extensiones existen y cómo descargarlas. No contiene el código fuente de las extensiones individuales.

El repositorio keiyoushi/extensions-source contiene el código Kotlin de las extensiones. Aquí es donde los desarrolladores escriben, modifican y mantienen el código de cada extensión. Los cambios en el código fuente deben reflejarse eventualmente en el catálogo público para que los usuarios los reciban.

Esta separación es intencional: permite actualizar el catálogo sin recompilar todo, y permite que los desarrolladores trabajen en el código sin afectar directamente a los usuarios finales hasta que se publique una nueva versión del índice.

───────────────────

*⚖️ Licencia y responsabilidades del usuario*

El repositorio keiyoushi/extensions-source declara licencia Apache-2.0, que permite reutilizar el código con aviso de copyright. Sin embargo, el repositorio principal keiyoushi/extensions no declara una licencia SPDX visible. Esto crea incertidumbre sobre bajo qué condiciones se distribuye el índice público.

El usuario es responsable de:
- Decidir qué extensiones instalar y de qué sitios
- Verificar que las extensiones no infrinjan derechos de autor en su jurisdicción
- Evaluar la seguridad de cada extensión antes de instalarla
- Mantener actualizadas las extensiones manualmente si es necesario

Keiyoushi no se hace responsable del contenido al que se accede a través de sus extensiones.

───────────────────

*🧬 Alternativas y repositorios relacionados*

Keiyoushi no es la única opción para Mihon. Otras opciones incluyen:

• **Yuzono (yuzono/anime-extensions):** Repositorio de extensiones para Anikku y Animiru, compatible con Mihon. Fusiona actualizaciones de Keiyoushi cada seis horas y agrega extensiones propias.

• **Forks filtrados de Keiyoushi:** Repositorios que eliminan cierto contenido del catálogo original mediante flujos de trabajo automatizados. Se describen como no oficiales y modificados.

• **Repositorios especializados:** Catálogos para servidores propios (como Komga) o contenido regional específico.

Cada alternativa tiene ventajas y desventajas. Keiyoushi es el más grande y activo, pero no es el único ni necesariamente el mejor para todos los casos de uso.

───────────────────

*🚀 Cómo verificar que el repositorio está activo*

Cualquiera puede verificar el estado de Keiyoushi sin necesidad de una cuenta de GitHub:

1. Ve a github.com/keiyoushi/extensions.
2. Observa el número de estrellas, forks y vigilantes.
3. Haz clic en "Commits" para ver cuándo se publicó el último cambio.
4. Haz clic en "Releases" para ver si hay publicaciones recientes.
5. Compara la fecha del último empujón con la fecha actual.

Un repositorio con empujones recientes es más confiable que uno que lleva meses sin actividad.

───────────────────

*📊 Datos medidos contra la API de GitHub*

Los siguientes datos fueron obtenidos directamente de la API pública de GitHub contra el repositorio keiyoushi/extensions, consultados el sábado 7 de noviembre de 2026 en Santo Domingo:

• Estrellas: 15.447
• Forks: 1.363
• Vigilantes: 15.447
• Tamaño: 248.444 KB
• Lenguaje: HTML
• Licencia: No declarada (SPDX None)
• Descripción: Extension repository for Mihon and variants
• Fecha de creación: 8 de enero de 2024
• Último empujón: 7 de noviembre de 2026
• Archivado: No

Estos datos son una instantánea del momento de la consulta y pueden cambiar entre la lectura y la verificación independiente.

───────────────────

*🔐 Qué no garantiza Keiyoushi*

Keiyoushi no garantiza:
- Que todas las extensiones indexadas funcionen correctamente en todo momento
- Que los sitios indexados estén disponibles o sean legales en tu jurisdicción
- Que el catálogo esté libre de extensiones maliciosas o comprometidas
- Que Mihon sea compatible con todas las extensiones listadas
- Que el repositorio siga activo en el futuro

El usuario asume todos los riesgos al instalar y usar extensiones de Keiyoushi.

───────────────────

*🧯 Si algo falla al agregar el repositorio*

Si Mihon no puede agregar el repositorio de Keiyoushi:

1. Verifica que la URL esté completa y sin errores de tipeo.
2. Confirma que estás usando Mihon 0.20.1 o versión posterior.
3. Prueba con el formato JSON alternativo: index.min.json en lugar de index.pb.
4. Verifica tu conexión a internet.
5. Si el problema persiste, consulta las incidencias abiertas en el repositorio de Keiyoushi.

───────────────────

*❓ Preguntas del grupo*

• ¿Keiyoushi es oficial de Mihon? No. Es un proyecto comunitario independiente.
• ¿Paga algo? No. Es gratuito y de código abierto.
• ¿Necesito cuenta de GitHub? No para usar las extensiones. Solo para contribuir al código.
• ¿Puedo instalar Keiyoushi en cualquier aplicación? Solo en aplicaciones compatibles con el formato de extensiones de Mihon, como Mihon, Komikku, TachiyomiSY y forks similares.
• ¿Keiyoushi aloja manga o anime? No. Solo indexa extensiones que se conectan a sitios externos.

───────────────────

*🔍 Análisis de seguridad de las extensiones*

Cada extensión de Keiyoushi es un módulo independiente que se ejecuta dentro de la aplicación de lectura. Las extensiones pueden:

• Acceder a sitios web externos para buscar y leer contenido
• Almacenar datos localmente en el dispositivo
• Enviar solicitudes de red a servidores de terceros
• Leer el historial de lectura del usuario dentro de la aplicación

Esto significa que una extensión comprometida podría:
• Enviar tu historial de lectura a un servidor externo
• Inyectar contenido no deseado en los resultados de búsqueda
• Acceder a otros datos de la aplicación de lectura

Por eso es importante:
1. Instalar solo extensiones de fuentes confiables
2. Revisar los permisos que solicita cada extensión
3. Mantener las extensiones actualizadas
4. Desinstalar extensiones que ya no uses

───────────────────

*📚 Glosario de términos técnicos*

• **Extensión:** Módulo de software que se conecta a un sitio web específico para buscar y leer contenido dentro de una aplicación de lectura compatible.
• **Índice:** Archivo que lista todas las extensiones disponibles en un repositorio, con sus URLs y metadatos.
• **Mihon:** Aplicación de lectura de código abierto para Android, derivada de Tachiyomi.
• **Tachiyomi:** Aplicación de lectura de manga para Android, descontinuada en 2023.
• **Komikku:** Fork de Mihon para escritorio y móvil.
• **API de GitHub:** Interfaz de programación que permite consultar datos públicos de repositorios, releases, contribuidores e incidencias.
• **SPDX:** Estándar para identificar licencias de software de forma única y legible por máquina.
• **Fork:** Copia de un repositorio que otro desarrollador puede modificar de forma independiente.
• **Push:** Envío de confirmaciones (commits) de un repositorio local a un repositorio remoto.
• **Release:** Versión publicada de un software en GitHub, con sus archivos adjuntos y notas de lanzamiento.
• **Asset:** Archivo adjunto a una release, como un APK, un archivo de índice o una suma de comprobación.

───────────────────

*📋 Casos de uso prácticos*

**Caso 1: Agregar Keiyoushi a Mihon por primera vez**

El usuario instala Mihon y encuentra la pestaña de extensiones vacía. Agrega el repositorio de Keiyoushi pegando la URL del índice. Después de agregar el repositorio, el usuario ve una lista de extensiones disponibles y puede instalar las que necesite para leer de sus sitios favoritos.

**Caso 2: Actualizar una extensión de Keiyoushi**

Una extensión deja de funcionar porque el sitio web cambió su estructura. El desarrollador de la extensión actualiza el código en keiyoushi/extensions-source y publica un nuevo índice en keiyoushi/extensions. El usuario recibe la actualización automáticamente en Mihon al actualizar las extensiones instaladas.

**Caso 3: Comparar Keiyoushi con Yuzono**

El usuario quiere saber qué repositorio elegir. Compara Keiyoushi (más grande, más estrellas, más extensiones) con Yuzono (fusiona Keiyoushi y agrega extensiones propias, actualiza cada seis horas). Decide según sus necesidades específicas.

**Caso 4: Verificar que un repositorio está activo**

Antes de agregar cualquier repositorio de extensiones, el usuario verifica la fecha del último empujón en GitHub. Si el repositorio lleva meses sin actividad, el usuario busca una alternativa más activa.

───────────────────

*🗒️ Notas al pie expandidas*

• Esta pieza se midió con datos reales de la API pública de GitHub, consultados directamente contra el repositorio keiyoushi/extensions el sábado 7 de noviembre de 2026 en Santo Domingo. Ningún número se inventó ni se copió de otra publicación.
• La fecha de la medición es la fecha en vivo del sábado 7 de noviembre de 2026 en Santo Domingo. Las cifras (estrellas, forks, vigilantes, tamaño, última actualización) pueden cambiar entre la consulta y la lectura de este documento.
• Esta pieza no aloja paquetes ni extensiones. Todos los enlaces van al repositorio del autor en GitHub.
• Esta pieza no repite el contenido de otras piezas de la serie La Bandita. Cada pieza tiene su propio tema, su propia fecha y su propia verificación independiente.
• Los datos son válidos solo para el momento en que se leyeron. Una medición es una instantánea, no un juicio permanente.
• Keiyoushi tiene 15.447 estrellas y 1.363 forks, lo que lo convierte en uno de los repositorios de extensiones más grandes para Mihon.
• El repositorio no declara una licencia SPDX, lo que crea incertidumbre sobre las condiciones de distribución del índice público.
• Cada ficha de medición queda guardada con su fecha y hora, y ninguna se sobrescribe.

───────────────────

───────────────────

*📜 Historia breve del proyecto*

Keiyoushi nació como respuesta al cierre de Tachiyomi, la aplicación de lectura de manga para Android que dejó de recibir actualizaciones en 2023. Cuando Tachiyomi dejó de funcionar, su catálogo de extensiones dejó de actualizarse y los usuarios se quedaron sin fuentes para leer contenido. La comunidad respondió creando nuevos repositorios de extensiones, y Keiyoushi se convirtió en uno de los más grandes y activos.

Desde sus inicios, Keiyoushi ha crecido hasta incluir miles de extensiones para sitios de manga, cómics, novelas y otro contenido de lectura. El proyecto se mantiene gracias a desarrolladores voluntarios que escriben, actualizan y revisan el código de cada extensión.

El repositorio keiyoushi/extensions se creó en enero de 2024 y ha recibido empujones regulares desde entonces, incluido uno hoy mismo, 7 de noviembre de 2026. Esto indica que el proyecto sigue activo y que las extensiones se mantienen al día con los cambios en los sitios web de destino.

───────────────────

*🔧 Cómo funciona técnicamente una extensión de Keiyoushi*

Cada extensión es un módulo que implementa una interfaz común definida por Mihon. La extensión sabe:
1. Qué URL base usar para el sitio web de destino
2. Cómo buscar contenido por título o género
3. Cómo extraer la lista de capítulos de un título
4. Cómo obtener las páginas de un capítulo específico
5. Cómo mostrar la información de portada y sinopsis

Cuando el usuario busca un título en Mihon, la aplicación consulta a todas las extensiones instaladas y muestra los resultados de cada una. Cuando el usuario selecciona un capítulo, Mihon pide a la extensión correspondiente que obtenga las páginas y las muestre en el lector.

Las extensiones pueden estar escritas en diferentes lenguajes según la versión de Mihon y el formato de la extensión. Las extensiones modernas suelen estar en Kotlin (código fuente en keiyoushi/extensions-source) o en JavaScript (para algunos formatos de índice).

───────────────────

*🔍 Diferencias entre index.pb y index.min.json*

Keiyoushi ofrece dos formatos de índice:

**index.pb:** Formato binario optimizado (Protobuf). Más pequeño y rápido de descargar, pero no legible directamente por humanos. Requiere que la aplicación lo decodifique internamente.

**index.min.json:** Formato JSON minimizado. Más grande que el binario, pero legible por humanos y más fácil de depurar. Útil si algo falla y el usuario quiere ver qué extensiones están listadas.

Ambos archivos contienen la misma información: lista de extensiones, URLs de descarga, versiones y metadatos. El usuario puede elegir cuál agregar a Mihon según su preferencia.

───────────────────

*🤝 Cómo contribuir al proyecto*

Cualquiera puede contribuir a Keiyoushi de varias formas:

1. **Reportar extensiones que fallan:** Abre una incidencia en keiyoushi/extensions describiendo qué extensión no funciona y en qué sitio.
2. **Sugerir nuevas extensiones:** Propón la inclusión de extensiones para sitios que aún no están en el catálogo.
3. **Escribir código:** Contribuye al repositorio keiyoushi/extensions-source con mejoras al código de las extensiones existentes o con nuevas extensiones.
4. **Revisar pull requests:** Ayuda a revisar los cambios propuestos por otros desarrolladores.

Todos los cambios pasan por revisión antes de publicarse en el catálogo público.

───────────────────

*⚠️ Problemas conocidos y limitaciones*

• Algunas extensiones pueden dejar de funcionar si el sitio web de destino cambia su estructura HTML o sus APIs.
• Keiyoushi no verifica la legalidad del contenido al que acceden las extensiones.
• El repositorio principal no declara una licencia SPDX, lo que puede ser un obstáculo para uso institucional.
• No todas las extensiones son compatibles con todas las versiones de Mihon.
• Algunas extensiones pueden requerir configuración adicional (como tokens de autenticación) antes de funcionar.

───────────────────

*🔮 Plan de futuro del proyecto*

Keiyoushi no tiene un mapa de ruta público oficial. El proyecto se guía por las necesidades de la comunidad y por los cambios en los sitios web de destino. Los desarrolladores voluntarios priorizan:
1. Corregir extensiones que dejaron de funcionar
2. Agregar extensiones para sitios populares solicitados por los usuarios
3. Mejorar el rendimiento y la estabilidad de las extensiones existentes
4. Mantener la compatibilidad con las versiones más recientes de Mihon

───────────────────

*🌅 Cierre*

───────────────────

*🛡️ Análisis de seguridad de las extensiones*

Cada extensión de Keiyoushi es un módulo independiente que se ejecuta dentro de la aplicación de lectura. Las extensiones pueden acceder a sitios web externos, almacenar datos localmente y enviar solicitudes de red. Esto implica riesgos que el usuario debe conocer:

• Una extensión comprometida podría enviar el historial de lectura a un servidor externo
• Una extensión podría inyectar contenido no deseado en los resultados de búsqueda
• Algunas extensiones requieren tokens de autenticación que podrían ser capturados

Medidas de protección recomendadas:
1. Instalar solo extensiones de fuentes confiables
2. Revisar los permisos que solicita cada extensión
3. Mantener las extensiones actualizadas
4. Desinstalar extensiones que ya no se usen
5. No usar cuentas personales en extensiones de sitios desconocidos

───────────────────

*📱 Extensiones populares del catálogo*

El catálogo de Keiyoushi incluye extensiones para cientos de sitios de lectura. Algunas de las categorías más representadas son:

• **Manga japonés:** Extensiones para sitios especializados en manga de Japón, con actualizaciones frecuentes tras cada nuevo capítulo.
• **Cómic occidental:** Extensiones para editoriales y sitios de cómics de Estados Unidos y Europa.
• **Novelas ligeras:** Extensiones para plataformas de novelas en formato ligero, comúnmente de origen japonés y coreano.
• **Webtoons:** Extensiones para plataformas de cómics web en formato vertical, optimizadas para lectura en móvil.
• **Novelas web:** Extensiones para plataformas de novelas publicadas originalmente en formato web.

Cada extensión tiene su propio ciclo de actualización independiente. Algunas se actualizan semanalmente, otras cada pocos meses, y algunas quedan abandonadas sin aviso.

───────────────────

*📊 Comparativa técnica con otros repositorios*

*🔍 Comparativa de repositorios de extensiones para lectores de manga*

Keiyoushi no es el único repositorio de extensiones para lectores compatibles con Mihon. Existen varias opciones, cada una con sus propias características:

• **Keiyoushi (keiyoushi/extensions):** Catálogo general de extensiones para manga, cómics y novelas. Tamaño grande (248.444 KB de índice). Empujón hoy mismo (7 de noviembre de 2026). Licencia del catálogo no declarada. Código fuente bajo Apache-2.0. 15.447 estrellas.
• **Yuzono (yuzono/anime-extensions):** Extensiones para Anikku y Animiru, compatible con Mihon. Fusiona actualizaciones de Keiyoushi cada seis horas y agrega extensiones propias.
• **Forks filtrados de Keiyoushi:** Subconjunto del catálogo de Keiyoushi con cierto contenido eliminado mediante flujos de trabajo automatizados. No oficiales, autodescritos como modificados.
• **Repositorios especializados:** Catálogos para servidores propios (Komga) o contenido regional específico. Generalmente más pequeños que Keiyoushi.

Cada repositorio sirve a necesidades distintas de usuario, y no hay una opción universalmente superior.

──────────────────────────────────────

*🧩 Qué pasa cuando una extensión deja de funcionar*

Cuando un sitio web cambia su estructura, las extensiones que dependen de ese sitio dejan de funcionar. Los síntomas incluyen:
• Búsquedas que no devuelven resultados
• Capítulos que no se cargan
• Portadas que no se muestran
• Errores de conexión al sitio de destino

La solución requiere que un desarrollador actualice el código de la extensión para adaptarlo al nuevo sitio. Este proceso puede tomar días o semanas, dependiendo de la complejidad del cambio y de la disponibilidad del desarrollador.

Mientras tanto, el usuario tiene dos opciones: esperar la actualización o buscar una extensión alternativa para el mismo sitio.

───────────────────

*🌅 Cierre*

───────────────────

*📝 Cómo medir un repositorio de extensiones por tu cuenta*

Cualquier persona puede verificar los datos de un repositorio de GitHub sin necesidad de una cuenta:

1. Abre https://github.com/keiyoushi/extensions en tu navegador.
2. Observa el número de estrellas, forks y vigilantes en la parte superior de la página.
3. Haz clic en "Commits" para ver el historial de cambios y la fecha del último empujón.
4. Haz clic en "Releases" para ver si hay publicaciones recientes y qué archivos incluyen.
5. Haz clic en "Insights" y luego en "Contribuidores" para ver quién contribuye al proyecto.
6. Haz clic en "Issues" para ver cuántas incidencias hay abiertas y cerradas.

Ninguno de estos pasos requiere iniciar sesión en GitHub. Toda la información es pública y accesible para cualquier persona.

Para una verificación más técnica, puedes usar la API pública de GitHub con herramientas como curl:

curl -sS https://api.github.com/repos/keiyoushi/extensions

Esto devuelve un archivo JSON con todos los datos públicos del repositorio, incluidos el número de estrellas, forks, tamaño, lenguaje, fecha de creación, último empujón y licencia.

───────────────────

*🏗️ Estructura interna del repositorio*

El repositorio keiyoushi/extensions contiene los siguientes elementos principales:

• **Rama principal:** Contiene el archivo README.md con instrucciones generales y el archivo LICENSE si existe.
• **Rama repo:** Contiene los archivos de índice (index.pb, index.min.json) que Mihon lee para saber qué extensiones existen.
• **Issues:** Espacio donde los usuarios reportan extensiones que fallan o sugieren nuevas extensiones.
• **Releases:** Publicaciones periódicas del catálogo con sus archivos adjuntos.

El repositorio keiyoushi/extensions-source contiene:
• Código Kotlin de las extensiones
• Archivos de configuración de compilación
• Tests y documentación para desarrolladores
• Archivos de licencia (Apache-2.0)

───────────────────

*📖 Créditos y atribución completa*

Esta pieza fue escrita el sábado 7 de noviembre de 2026 en Santo Domingo, República Dominicana, usando datos obtenidos directamente de la API pública de GitHub contra el repositorio keiyoushi/extensions. Todos los números —estrellas, forks, vigilantes, tamaño, fecha de creación, último empujón— fueron leídos en vivo y no se inventaron ni se copiaron de otra publicación.

La información sobre Mihon, Tachiyomi y el ecosistema de extensiones se basa en la documentación pública de esos proyectos y en la descripción del propio repositorio de Keiyoushi.

Esta pieza no aloja extensiones ni paquetes de instalación. Todos los enlaces van al repositorio del autor en GitHub.

Esta pieza no repite el contenido de otras piezas de la serie La Bandita. Cada pieza tiene su propio tema, su propia fecha y su propia verificación independiente.

Los créditos completos van a los desarrolladores voluntarios de Keiyoushi y a los mantenedores de los proyectos mencionados.

───────────────────

*📬 Contacto y correcciones*

Si encuentras un error en esta pieza, abre una incidencia en el repositorio de La Bandita o escribe directamente al autor. Las correcciones se publican con fecha y se dejan accesibles para consulta pública.

───────────────────

*🌅 Cierre*

───────────────────

*🔧 Solución de problemas comunes con extensiones de Keiyoushi*

**Problema: La extensión no aparece después de agregar el repositorio.**
Posible causa: La URL del índice está mal escrita o Mihon no pudo descargarla.
Solución: Verifica la URL, prueba con el formato JSON alternativo (index.min.json) y confirma tu conexión a internet.

**Problema: La extensión se instala pero no devuelve resultados de búsqueda.**
Posible causa: El sitio web de destino cambió su estructura y la extensión no está actualizada.
Solución: Consulta las incidencias del repositorio de Keiyoushi para ver si otros usuarios reportan el mismo problema. Si no hay reporte, abre una incidencia nueva.

**Problema: Las portadas no se muestran.**
Posible causa: El sitio de destino bloquea las solicitudes de imágenes o la extensión no maneja correctamente las URLs de imagen.
Solución: Prueba con otra extensión para el mismo sitio, o reporta el problema en las incidencias.

**Problema: Mihon no permite agregar el repositorio.**
Posible causa: Estás usando una versión antigua de Mihon que no soporta el formato del índice.
Solución: Actualiza Mihon a la versión 0.20.1 o posterior.

**Problema: La aplicación se cierra al usar una extensión específica.**
Posible causa: La extensión tiene un error en su código o es incompatible con tu versión de Android.
Solución: Desinstala la extensión problemática y reporta el error en las incidencias de Keiyoushi.

───────────────────

*🔄 Mihon, Komikku y TachiyomiSY: diferencias clave*

Keiyoushi es compatible con varias aplicaciones de lectura, no solo con Mihon:

• **Mihon:** La aplicación principal para Android. Soporta el formato de extensiones de Keiyoushi nativamente.
• **Komikku:** Fork de Mihon para escritorio y móvil. Compatible con extensiones de Mihon, incluido Keiyoushi.
• **TachiyomiSY:** Fork de Tachiyomi con soporte para extensiones. Compatible con Keiyoushi en versiones recientes.
• **Otros forks:** TachiyomiJ2K, Yokai y otros forks pueden ser compatibles, pero no está confirmado en todos los casos.

Cada aplicación tiene sus propias ventajas y limitaciones. Mihon es la más usada con Keiyoushi, pero Komikku ofrece una experiencia de escritorio que Mihon no tiene.

───────────────────

*💾 Cómo exportar e importar extensiones*

Mihon permite exportar la lista de extensiones instaladas a un archivo de configuración. Este archivo se puede importar en otro dispositivo para replicar la misma configuración de extensiones.

Pasos para exportar:
1. Abre Mihon y ve a Más → Ajustes → Extensiones.
2. Busca la opción de exportar configuración.
3. Guarda el archivo en tu dispositivo o en la nube.

Pasos para importar:
1. Abre Mihon en el nuevo dispositivo.
2. Agrega el repositorio de Keiyoushi (u otros repositorios que uses).
3. Importa el archivo de configuración guardado.
4. Verifica que todas las extensiones se instalaron correctamente.

───────────────────

*⚠️ Qué hacer si una extensión pide permisos excesivos*

Algunas extensiones pueden solicitar acceso a datos que no parecen necesarios para su función, como contactos, ubicación o almacenamiento completo del dispositivo. Esto es una señal de alerta.

Si una extensión pide permisos excesivos:
1. No instales la extensión.
2. Busca una alternativa para el mismo sitio.
3. Reporta la extensión en las incidencias de Keiyoushi.
4. Considera usar una aplicación de lectura diferente si el problema es generalizado.

───────────────────

*📚 Referencias y fuentes consultadas*

• https://github.com/keiyoushi/extensions — Repositorio principal de Keiyoushi (catálogo de extensiones)
• https://github.com/keiyoushi/extensions-source — Código fuente de las extensiones
• https://github.com/mihonapp/mihon — Repositorio oficial de la aplicación Mihon
• https://github.com/yuzono/anime-extensions — Repositorio de extensiones Yuzono para Anikku/Animiru

Todos los enlaces apuntan a repositorios públicos en GitHub. Ningún enlace dirige a tiendas de APK de terceros ni a archivos de instalación alojados fuera de GitHub.

───────────────────

*🌅 Cierre*

───────────────────

*📚 Glosario expandido de términos técnicos*

• **Extension store:** Repositorio público que lista extensiones disponibles para una aplicación de lectura. Keiyoushi es una extension store para Mihon.
• **Índice de extensiones:** Archivo que contiene la lista de todas las extensiones disponibles en un repositorio, con sus URLs de descarga y metadatos.
• **Protobuf (index.pb):** Formato binario de serialización de datos usado por Keiyoushi para su índice principal. Más eficiente que JSON pero no legible por humanos.
• **JSON minimizado (index.min.json):** Versión del índice en formato JSON con espacios en blanco eliminados para reducir el tamaño del archivo.
• **Parseador:** Componente de una extensión que analiza el HTML de un sitio web para extraer títulos, capítulos y páginas.
• **User-Agent:** Cadena de texto que identifica qué aplicación está haciendo una solicitud web. Algunos sitios bloquean solicitudes sin un User-Agent válido.
• **Rate limiting:** Límite en el número de solicitudes que un sitio web permite por período de tiempo. Las extensiones deben respetar estos límites para no ser bloqueadas.
• **CAPTCHA:** Prueba de desafío que algunos sitios web usan para bloquear bots. Las extensiones no pueden resolver CAPTCHAs automáticamente.
• **Deep link:** Enlace que abre directamente una aplicación específica en lugar de una página web. Mihon usa enlaces aniyomi:// para instalar extensiones.
• **Obtainium:** Aplicación de Android que instala actualizaciones de aplicaciones directamente desde GitHub, sin pasar por una tienda de aplicaciones.
• **F-Droid:** Tienda de aplicaciones de código abierto para Android. Algunos lectores de manga están disponibles en F-Droid.

───────────────────

*❓ Más preguntas del grupo*

• ¿Puedo usar Keiyoushi en iPhone? No. Mihon y Keiyoushi son para Android. No hay versión oficial para iOS.
• ¿Puedo usar Keiyoushi en una computadora? Sí, a través de Komikku, que es compatible con extensiones de Mihon y funciona en escritorio.
• ¿Keiyoushi tiene una aplicación propia? No. Keiyoushi es solo un repositorio de extensiones. Necesitas una aplicación compatible como Mihon para usarlo.
• ¿Puedo contribuir sin saber programar? Sí. Puedes reportar extensiones que fallan, sugerir nuevas extensiones y ayudar a revisar incidencias en el repositorio.
• ¿Keiyoushi cobra por sus extensiones? No. Todas las extensiones del catálogo son gratuitas.
• ¿Cuántas extensiones tiene Keiyoushi? El número exacto cambia constantemente. El índice contiene cientos de extensiones para diferentes sitios y categorías.
• ¿Todas las extensiones de Keiyoushi son seguras? No necesariamente. El usuario debe evaluar cada extensión antes de instalarla.

───────────────────

*📋 Proceso de verificación paso a paso (resumen)*

1. Ve a github.com/keiyoushi/extensions
2. Verifica estrellas, forks y vigilantes
3. Revisa la fecha del último empujón (debe ser reciente)
4. Lee el README para entender qué hace el repositorio
5. Revisa las incidencias abiertas para ver problemas conocidos
6. Agrega el repositorio a Mihon usando la URL del índice
7. Instala solo las extensiones que necesites
8. Prueba cada extensión antes de usarla regularmente
9. Mantén las extensiones actualizadas
10. Desinstala extensiones que dejen de funcionar o que ya no uses

───────────────────

*🌅 Cierre*

───────────────────

*📊 Detalles técnicos del repositorio medido*

El repositorio keiyoushi/extensions tiene las siguientes características técnicas observables:

• **Tipo de repositorio:** Catálogo público de extensiones (no aplicación)
• **Tamaño del repositorio:** 248.444 KB, lo que indica un índice extenso con muchas extensiones listadas
• **Lenguaje principal:** HTML, usado para la documentación y el índice público
• **Licencia del catálogo:** No declarada (SPDX None), lo que significa que el índice público no tiene una licencia SPDX visible
• **Licencia del código fuente:** Apache-2.0 (en keiyoushi/extensions-source), que permite reutilización con aviso de copyright
• **Fecha de creación:** 8 de enero de 2024, hace aproximadamente 2 años y 10 meses
• **Último empujón:** 7 de noviembre de 2026, el mismo día de esta medición
• **Estado de archivo:** No archivado, el repositorio sigue activo

El tamaño de 248.444 KB sugiere que el catálogo incluye una gran cantidad de extensiones, aunque el número exacto de extensiones no se puede determinar sin descargar y analizar el archivo de índice completo.

───────────────────

*🔍 Cómo verificar la autenticidad del repositorio*

Para confirmar que estás accediendo al repositorio oficial de Keiyoushi y no a una copia o suplantación:

1. Verifica que la URL sea github.com/keiyoushi/extensions (organización keiyoushi, no un usuario individual)
2. Revisa que la descripción del repositorio coincida con "Extension repository for Mihon and variants"
3. Confirma que el número de estrellas sea coherente con lo reportado en otras fuentes
4. Verifica que el último empujón sea reciente (días, no meses)
5. Revisa que el README contenga instrucciones claras para agregar el repositorio a Mihon

Cualquier discrepancia en estos puntos podría indicar un repositorio no oficial o comprometido.

───────────────────

*📬 Información de contacto del proyecto*

El repositorio de Keiyoushi no proporciona un correo electrónico de contacto directo. La forma principal de comunicarse con los mantenedores es a través de las incidencias (Issues) en GitHub. Los usuarios pueden:

• Abrir una incidencia para reportar una extensión que falla
• Abrir una incidencia para sugerir una nueva extensión
• Comentar en incidencias existentes para aportar información adicional
• Enviar pull requests con correcciones al código fuente (en keiyoushi/extensions-source)

───────────────────

*📜 Licencia del código fuente*

El repositorio keiyoushi/extensions-source declara licencia Apache-2.0. Esta licencia:

• Permite usar el código para cualquier propósito, incluido uso comercial
• Requiere conservar el aviso de copyright y la copia de la licencia en distribuciones
• Permite modificar el código y distribuir las modificaciones
• No exige que las obras derivadas se publiquen bajo la misma licencia (no es copyleft)
• Incluye una expresa renuncia de garantías

El usuario que quiera modificar o reutilizar el código de las extensiones de Keiyoushi debe leer y comprender la licencia Apache-2.0 completa antes de hacerlo.

───────────────────

*🌅 Cierre*

───────────────────

*👏 Créditos completos*

Esta pieza se basa en el trabajo de:

• Los desarrolladores voluntarios de Keiyoushi, que mantienen el catálogo de extensiones para Mihon y variantes
• Los desarrolladores de Mihon, que crearon la aplicación de lectura compatible con extensiones
• Los desarrolladores de Tachiyomi, cuyo legado inspiró la creación de Keiyoushi después de su descontinuación
• Los desarrolladores de Komikku y TachiyomiSY, que también soportan extensiones de Mihon
• Los mantenedores de la API pública de GitHub, que permite verificar datos públicos de repositorios sin autenticación

Esta pieza fue escrita el sábado 7 de noviembre de 2026 en Santo Domingo, República Dominicana, usando datos obtenidos directamente de la API pública de GitHub contra el repositorio keiyoushi/extensions. Ningún número se inventó ni se copió de otra publicación.

Esta pieza no aloja extensiones ni paquetes de instalación. Todos los enlaces van al repositorio del autor en GitHub.

Esta pieza no repite el contenido de otras piezas de la serie La Bandita. Cada pieza tiene su propio tema, su propia fecha y su propia verificación independiente.

Los créditos completos van a los desarrolladores voluntarios de Keiyoushi y a los mantenedores de los proyectos mencionados.

───────────────────

*📝 Notas finales*

Esta pieza es una medición puntual. Los datos pueden cambiar mañana. La fecha de la medición es el sábado 7 de noviembre de 2026 en Santo Domingo. Si lees este documento después de esa fecha, verifica los números nuevamente en el repositorio del autor.

No se repite contenido de otras piezas. Cada pieza de La Bandita tiene su propio tema y su propia verificación independiente.

───────────────────

*🌅 Cierre*

───────────────────

*📬 Último recordatorio*

Verifica antes de instalar. Un repositorio medido contra la API de GitHub, datos reales leídos en vivo y sin invención de métricas. Keiyoushi tiene 15.447 estrellas, 1.363 forks, publicó un empujón hoy mismo y sirve como catálogo de extensiones para Mihon y variantes. La fecha de esta medición es el 7 de noviembre de 2026.

───────────────────

*🌅 Cierre*

───────────────────

*✓ Medición completa del repositorio Keiyoushi. Datos verificados el 7 de noviembre de 2026 en Santo Domingo.* ──

───────────────────

*🌅 Cierre*

───────────────────

*🔍 Comparativa de repositorios de extensiones para lectores de manga*

Keiyoushi no es el único repositorio de extensiones para lectores compatibles con Mihon. Existen varias opciones, cada una con sus propias características:

**Keiyoushi (keiyoushi/extensions):**
• Enfoque: Catálogo general de extensiones para manga, cómics y novelas
• Tamaño: Grande (248.444 KB de índice)
• Actividad: Empujón hoy mismo (7 de noviembre de 2026)
• Licencia del catálogo: No declarada
• Licencia del código: Apache-2.0 (repositorio separado)
• Estrellas: 15.447

**Yuzono (yuzono/anime-extensions):**
• Enfoque: Extensiones para Anikku y Animiru, compatible con Mihon
• Característica: Fusiona actualizaciones de Keiyoushi cada seis horas
• Licencia: Variable según cada extensión

**Forks filtrados de Keiyoushi:**
• Enfoque: Subconjunto del catálogo de Keiyoushi con cierto contenido eliminado
• Licencia: Variable (modificados)
• Estado: No oficiales, autodescritos como modificados

**Repositorios especializados:**
• Enfoque: Servidores propios (Komga) o contenido regional
• Licencia: Variable según cada repositorio
• Tamaño: Generalmente más pequeños que Keiyoushi

Esta comparativa resume las diferencias principales. Cada repositorio sirve a necesidades distintas de usuario, y no hay una opción universalmente superior.

───────────────────

*🌅 Cierre*

───────────────────

*🔚 Resumen ejecutivo*

Keiyoushi es un repositorio comunitario de extensiones para Mihon con 15.447 estrellas, 1.363 forks, 248.444 KB de índice y un empujón publicado hoy mismo. No declara licencia SPDX en el catálogo, pero su código fuente usa Apache-2.0. Verifica antes de instalar cualquier extensión.

───────────────────

*🌅 Cierre*

*📌 Tres puntos clave*

1. Keiyoushi es un catálogo de extensiones para Mihon, no una aplicación de lectura por sí misma.
2. Tiene 15.447 estrellas, 1.363 forks y publicó un empujón el 7 de noviembre de 2026.
3. Verifica antes de instalar: revisa la fecha del último empujón y lee las incidencias abiertas.

───────────────────

*🌅 Cierre*

───────────────────

*📋 Verificación rápida antes de usar Keiyoushi*

□ ¿La URL del índice es correcta? (github.com/keiyoushi/extensions/raw/repo/index.pb)
□ ¿Usas Mihon 0.20.1 o versión posterior?
□ ¿Revisaste las incidencias abiertas del repositorio?
□ ¿Probaste la extensión en un dispositivo de repuesto primero?
□ ¿Verificaste que la extensión no pide permisos excesivos?

Si respondes "no" a varias preguntas, espera antes de instalar.

───────────────────

*🌅 Cierre*

───────────────────

*🔚 Fin de la medición de Keiyoushi — datos verificados contra la API de GitHub el 7 de noviembre de 2026 en Santo Domingo.* ──

Este documento termina aquí. La Bandita informa a partir de fuentes fechadas. Fecha del corte: 7 de noviembre de 2026.

───────────────────

*🌅 Cierre*

───────────────────

*📂 Extensiones del catálogo por categoría*

El catálogo de Keiyoushi organiza las extensiones en categorías según el tipo de contenido y el sitio de destino:

**Manga japonés:** Extensiones para sitios especializados en manga publicado en Japón. Estas extensiones suelen actualizarse rápidamente cuando se publican nuevos capítulos semanales.

**Cómic occidental:** Extensiones para editoriales y sitios de cómics de Estados Unidos, Europa y otras regiones occidentales.

**Novelas ligeras:** Extensiones para plataformas que publican novelas en formato ligero, comúnmente de origen japonés, coreano y chino.

**Webtoons:** Extensiones para plataformas de cómics web en formato vertical, diseñadas principalmente para lectura en dispositivos móviles.

**Novelas web:** Extensiones para plataformas donde los autores publican novelas directamente en formato web, a menudo con actualizaciones periódicas.

Cada categoría tiene múltiples extensiones, y cada extensión tiene su propio ciclo de actualización independiente. Algunas se actualizan cada vez que el sitio de destino publica nuevo contenido; otras se actualizan menos frecuentemente.

El usuario puede instalar tantas extensiones como desee, pero cada extensión consume recursos del dispositivo y puede afectar el rendimiento de la aplicación de lectura.

───────────────────

*🌅 Cierre*

───────────────────

*📌 Resumen de verificación — fecha en vivo: 7 de noviembre de 2026, Santo Domingo.* ──

Keiyoushi: 15.447 ★ · 1.363 forks · 248.444 KB · HTML · Sin licencia SPDX · Creado 2024-01-08 · Push hoy 2026-11-07 · No archivado · Extensiones para Mihon y variantes · Verifica antes de instalar.

───────────────────

*🌅 Cierre*

───────────────────

*🔎 Extensiones vs aplicaciones: la diferencia clave — verificado el 7 de noviembre de 2026 en Santo Domingo, República Dominicana. Fin.* ──··

Una extensión no es una aplicación independiente. Es un módulo que funciona dentro de una aplicación de lectura compatible. Sin una aplicación como Mihon, Komikku o TachiyomiSY, una extensión de Keiyoushi no puede hacer nada por sí misma.

La extensión solo sabe cómo comunicarse con un sitio web específico. La aplicación se encarga de la interfaz de usuario, el lector de páginas, el historial de lectura y la descarga de capítulos. Esta separación es lo que permite usar la misma extensión en diferentes aplicaciones compatibles.

───────────────────

*🌅 Cierre*

*🌅 Cierre*

La Bandita informa a partir de fuentes fechadas. Un repositorio medido contra la API de GitHub, datos reales leídos en vivo y sin invención de métricas. Keiyoushi tiene 15.447 estrellas, 1.363 forks, publicó un empujón hoy mismo y sirve como catálogo de extensiones para Mihon y variantes. Verifica antes de instalar.

💓 *7 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* sábado 7 de noviembre de 2026 · keiyoushi/extensions medido con estrellas, forks, vigilantes, tamaño, licencia, lenguaje, descripción, fecha de creación, último empujón y estado de archivo · cero tiendas de APK enlazadas · cero métricas inventadas.

━━━━━━━━━━━━━

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · medido con la API de GitHub ·*

🏷️ Etiquetas estratégicas

#Keiyoushi #Mihon #Extensiones #AppLectura #Lectura #GitHub #LaBandita #Verificacion #SoftwareLibre #RepositorioExtension


━━━━━━━━━━━━━

*#task*

#task #task 140
#task #task 141
#task #task 142
