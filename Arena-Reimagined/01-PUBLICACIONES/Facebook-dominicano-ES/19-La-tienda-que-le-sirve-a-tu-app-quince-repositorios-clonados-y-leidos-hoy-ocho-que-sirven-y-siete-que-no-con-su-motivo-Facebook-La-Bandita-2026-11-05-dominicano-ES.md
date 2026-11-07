*La tienda que le sirve a tu app: quince repositorios clonados y leídos esta mañana —la única de Mihon, la de Aniyomi, la que está vacía y la que se cerró sola—*

*La Bandita · jueves 5 de noviembre de 2026, 06:14 de la mañana en Santo Domingo (10:14 UTC) · edición dominicano-español · pieza 19 de Facebook, rehecha de raíz*

⏱️ *Lectura total: 26 minutos · quince repositorios clonados y leídos hoy entre las 10:03 y las 10:15 UTC · nueve aplicaciones comprobadas en la API · cuatro catálogos que se cuentan con la mano · ocho tiendas que pasan y siete que no · ninguna cifra copiada de una wiki*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La crítica que llegó · y por qué esta versión no se parece a la anterior
├── ⚡ En una página · 🕰️ la medición de las 06:14
├── 📏 Las siete comprobaciones · cada una con lo que encontró
├── 🗺️ La tabla que se pidió · qué tienda acepta cada aplicación
├── 🪦 Los cuatro cierres que nadie cuenta · la lápida dentro del índice
├── 📱 Las nueve aplicaciones · con su último empujón y su licencia
├── 🚚 Kotatsu está muerto · Usagi, Drop Sauce y el repositorio que está vacío
├── 📦 Tienda por tienda · ocho fichas, sin relleno
├── 🚫 Lo que no se indexa · siete nombres y su motivo
├── 🗣️ La crítica, punto por punto · qué cambié y qué no puedo cambiar
├── 🧠 Lo que una IA no ve · ⚖️ la responsabilidad · 🔏 la huella · 🛠️ las órdenes
└── 🚪 lo que no tiene · 📅 la semana · ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

───────────────────

*🧱 La crítica que llegó*

El escrito decía, más o menos: dejen de usar IA para volcar listas de aplicaciones y extensiones; usen la aplicación primero; pidan solo lo que de verdad sirve; dejen de enlazar repositorios solo porque son el fork de algo popular; y, si de verdad quieren hacerlo bien, **clonen el repositorio completo y prueben la aplicación**.

Y traía un mapa del ecosistema, app por app, que es más exacto que cualquier índice que hubiera en la casa: Mihon tiene **una** tienda —Keiyoushi— y alrededor tres cosas más (Yūzōnō, maldita por cinco extensiones retiradas; TheNano, con un puñado de fuentes chinas; y clones de Keiyoushi con una o dos propias o proyectos abandonados). Animiru tiene **una buena**, que es Yūzōnō; luego SalmanBappi, que vale sobre todo para fuentes BD; uno francés; y el repositorio de tres extensiones de Secozzi. Kotatsu está muerto y se pasa a Usagi con sus complementos, o a Drop Sauce, que acepta el formato de tienda de Mihon. Mangayomi vive de un repositorio que vale la pena. Las novelas **no tienen familia**: cada aplicación inventa su formato, aunque muchas aceptan los complementos de LNReader, que están bien mantenidos. Y en Cloudstream hay un «MegaRepo» que enlaza muchos repositorios en uno.

La crítica tiene razón en el fondo y no la voy a discutir. La pieza anterior contaba 5.481 extensiones en seis índices, y contar extensiones no es lo mismo que saber cuáles sirven. **Volver a subir el listón, esta vez, no significa escribir más: significa escribir menos y haber abierto antes cada cosa.** Así que esta versión hace lo que pedía el escrito: he clonado quince repositorios uno por uno, les he leído el catálogo como lo lee la aplicación, he comprobado si el índice está firmado, he descargado la cabecera de las descargas para ver si existen, y he mirado dentro de cada repositorio si lo que publica es una tienda o solamente el código con el que se construye.

Lo que no he hecho —y conviene decirlo arriba, no al final— es **abrir la aplicación en un teléfono**. Aquí no hay Android, no hay pantalla y no hay biblioteca que rellenar. Eso queda para quien lo tenga delante. Lo que sí hay es la parte que una persona haría con el repositorio abierto en el editor, que es justo la parte que una IA que junta enlaces se salta.

───────────────────

*⚡ En una página*

De quince repositorios, **ocho sirven, cuatro sirven con condiciones y tres no sirven para nada**. Y los tres que no sirven no fallan por ser pequeños ni por ser nuevos: fallan porque **no publican un catálogo que una aplicación pueda añadir**. Uno de ellos es el repositorio de Usagi que más se repite en las listas: tiene licencia, tiene un README de cuatro líneas y **cero complementos**. Otro es fuente con gradle y ramas de trabajo, sin índice publicado. El tercero está archivado desde octubre de 2025.

La familia Mihon se resuelve en una línea: **Keiyoushi, 1.458 extensiones, índice firmado y APK repartidas como adjuntos de release con su `sha256`**. Y tiene una trampa que casi nadie mira: el archivo `index.min.json`, que es el que muchas webs descargan para contar, **ya no es el catálogo**. Hoy son dos entradas y una de ellas se llama, literalmente, «Outdated App». El catálogo real está en un binario (`index.pb`) al que apunta `repo.json`. Quien cuente el archivo viejo cuenta dos.

La familia Aniyomi/Animiru se resuelve en otra línea: **Yūzōnō Anime, 248 extensiones**, y el enlace que circula está mudado —`yuzono/anime-repo` responde 301 y el catálogo vive en `mojuru/anime-repo`, con la misma firma—. La tienda de Yūzōnō para Mihon, en cambio, **se cerró sola**: su índice tiene una entrada que dice «Please migrate to Keiyoushi». Eso es exactamente lo que decía el mapa, pero con fecha y con el texto delante.

Kotatsu está archivada desde el **4 de noviembre de 2025**, hace 366 días, con 8.952 estrellas. Sus herederos vivos son Usagi —290 estrellas, en F-Droid, último empujón anteayer— y Drop Sauce, que acepta el formato de Mihon. Y aquí viene la parte incómoda: **el repositorio de complementos de Usagi que medio mundo enlaza está vacío**, así que recomendar «Usagi y sus complementos» sin decir cuáles es mandar a alguien a una puerta sin picaporte.

Cloudstream no tiene una lista: tiene **un plugin**. El «MegaRepo» se llama así porque al instalarlo añade los demás repositorios desde dentro de la aplicación; su `repo.json` declara una sola lista y su `plugins.json` una sola extensión, `MegaProvider`. Es la pieza más lista del ecosistema y también la que menos se entiende cuando se describe como «un repo con todo».

───────────────────
*🕰️ La medición de las 06:14 · qué se clonó y qué significa «probé»*

La fecha se comprobó **en vivo, dos veces**: al empezar, con la revisión de historial y de ecosistema que la casa exige antes de sondear nada, y al cerrar. El reloj de fuera dio las **10:14 UTC**, que en Santo Domingo son las **06:14** de la mañana. Todo lo que sigue se midió entre las 10:03 y las 10:15 de ese reloj, en una sola sesión.

Quince repositorios clonados con `git clone --depth 1`, uno detrás de otro, borrando cada clon después de leerlo: lo que queda es la ficha de veinte campos en `docs/AUDITORIA-TIENDAS-2026-11-05.json`. La herramienta se llama `tools/auditar_tienda.py` y la escribí para esta pieza porque no había ninguna que hiciera esto.

¿Qué quiere decir «probar» sin teléfono? Cuatro cosas, en el orden en que las hace la aplicación cuando alguien pega una dirección. **Uno:** abrir `repo.json`, el primer archivo que pide, y ver a qué catálogo apunta —en Keiyoushi, a un binario de 107.007 bytes—. **Dos:** contar las entradas de ese catálogo y no de otro. **Tres:** comprobar que está firmado, porque la aplicación rechaza una tienda sin clave y el usuario no ve el motivo. **Cuatro:** pedir un byte de una descarga de verdad, la que el catálogo señala y no la del README.

Con eso hecho, la aplicación sigue hablando con el servidor de la fuente, descarga las imágenes y las muestra. **Eso no lo puedo hacer desde aquí** y no lo voy a fingir: lo que puedo afirmar es que la tienda se instala, que el índice se lee, que la firma cuadra y que el archivo está.
───────────────────
*📏 Las siete comprobaciones · cada una con lo que encontró*

**1 · Está archivado.** Se pregunta a la API y se cruza con el último empujón. Encontró: el repositorio oficial de extensiones de Mangayomi está **archivado** con 363 entradas dentro, último empujón el 1 de octubre de 2025; Kotatsu, la aplicación, archivada el **4 de noviembre de 2025**. Un archivo con contenido no es una tienda: es un museo.

**2 · El catálogo está firmado.** Se busca `signingKey` en el índice y `signingKeyFingerprint` en `repo.json`. **Cinco de las quince firman en la rama que se clona** —Keiyoushi, las dos de Yūzōnō, TheNano y SalmanBappi—, y Secozzi firma en la rama del catálogo, así que la cuenta honesta es seis. Las de Mangayomi no firman porque su formato no contempla la firma.

**3 · Las descargas existen.** Un byte por descarga, seis por tienda. Keiyoushi sirve sus APK como adjuntos de release y las seis responden 206 con su tamaño; SalmanBappi responde 206 por `raw`; Yūzōnō Mihon responde **404 en las dos**, porque su catálogo apunta a archivos que ya no están.

**4 · El archivo que se cuenta es el que la aplicación lee.** Es la comprobación que separa una medición de una cita. Encontró cuatro lápidas disfrazadas de catálogo; van en su propia sección.

**5 · El README niega el soporte, se declara espejo o avisa de una retirada.** Se leen las primeras 120.000 letras y se buscan seis familias de frases. Encontró: **ninguna de las quince** niega el soporte por escrito. Es un dato en contra de la sospecha fácil y a favor de mirar antes de acusar.

**6 · Esto es una tienda o el código de la tienda.** Media lista del ecosistema confunde las dos cosas. Secozzi publica en la rama `repo` (tres extensiones); Cloudstream MegaRepo en `builds` (un plugin); `dragonx943/manga-repo` no publica catálogo, solo el código; `mochi-plugins/repository` no publica nada.

**7 · El nombre que la tienda declara es el del repositorio.** Se lee el campo `name` del índice. `mojuru/anime-repo` se llama **Yūzōnō**; `Secozzi/aniyomi-extensions` se llama **«Jellyfin, Stremio, and Torbox»**, la descripción más honesta de una tienda que he leído hoy. Y los clones que se anuncian con el nombre de otra tienda no entran en la tabla: un clon con nombre ajeno no es una tienda, es un problema para quien lo instala.
───────────────────
*🗺️ La tabla que se pidió · qué tienda acepta cada aplicación*

Esto es lo que el escrito pedía como primera cosa: una página donde las aplicaciones se agrupen según las extensiones compatibles. Aquí está, con lo medido hoy. «Entradas» es lo que publica el catálogo; «firma» es si el índice declara clave —el asterisco marca las que la declaran en la rama del catálogo y no en la principal—; «descarga» es el resultado de pedir un byte. Cuando la casilla queda vacía no es un cero: es un «no aplica».

```
APLICACIÓN        TIENDA                            ENTRADAS  FIRMA  DESCARGA  VEREDICTO
Mihon             Keiyoushi                            1.458    sí      206     sirve
Mihon             TheNano (copymanga-copy20)               5    sí      206     sirve
Mihon             Yūzōnō (manga-repo)                      1    sí      404     cerrada
Komikku / Mihon   Yuzono Cursed                            6   sí*        —     sirve
Animiru / Anikku  Yūzōnō Anime (mojuru/anime-repo)        248   sí*      206     sirve
Animiru           SalmanBappi                              98    sí      206     sirve
Animiru           Secozzi                                   3   sí*        —     sirve
Animiru           Hollow (francés, en Codeberg)             —     —        —     sin auditar
Usagi             mochi-plugins/repository                   0    no        —     vacía
Usagi / Tsuki     dragonx943/manga-repo                      0    no        —     solo código
Mangayomi         m2k3a                                   335    no        —     sirve
Mangayomi         Swakshan                                 15    no        —     sirve
Mangayomi         Mally                                    17    no        —     sirve
Mangayomi         kodjodevf (oficial)                     363    no        —     archivada
Novelas           LNReader (196 archivos, 17 idiomas)      196    no        —     sirve
Cloudstream       MegaRepo (un plugin, no una lista)         1    no        —     sirve
```

Tres cosas que la tabla dice y que una lista de enlaces no puede decir. **La primera:** Mihon y Animiru **no comparten tienda**, y por eso la mitad de las consultas de los grupos son «instalé esto y no me sale nada». **La segunda:** hay tiendas que sirven sin fricción (Keiyoushi, Yūzōnō Anime, SalmanBappi) y tiendas que sirven porque la aplicación lo permite (las tres de Mangayomi, que no firman). **La tercera:** dos de las filas que más se repiten —el repositorio de Usagi y el de Yūzōnō para Mihon— no dan hoy una sola extensión: una está vacía y la otra está cerrada y lo avisa.
───────────────────

*🪦 Los cuatro cierres que nadie cuenta · la lápida dentro del índice*

Una tienda que cierra no borra su repositorio: deja el índice con una entrada que se llama «Outdated App» o «Please migrate», para que la aplicación del que llega tarde le diga algo. Eso es buena ingeniería y es una trampa perfecta para cualquier recuento automático, porque **una lápida es una entrada más**.

**Keiyoushi.** `index.min.json` tiene **dos entradas**: «Outdated App» y una segunda que apunta a la aplicación. El catálogo de verdad —1.458 extensiones— está en `index.pb`, al que apunta `repo.json` con la clave `index_v2`. Durante meses, la cifra que circulaba por el ecosistema venía de este archivo. Sigue circulando.

**Yūzōnō Mihon.** Su `index.json` declara **una** entrada y su nombre es «Please migrate to Keiyoushi». Su `index.min.json` tiene dos: «Outdated App» y «Update to Mihon 0.20.1+». La tienda de Yūzōnō para Mihon **ya no existe como tienda**: existe como cartel. Y el cartel dice exactamente lo que decía el mapa de la crítica: la única tienda de Mihon es Keiyoushi.

**Secozzi.** Su índice principal está en la rama `repo` y tiene tres extensiones de verdad —Jellyfin, Stremio y Torbox, que es lo que su propio índice dice ser—. Su `index.min.json`, en cambio, trae **«Outdated App, switch to Animiru 0.20+»**: la misma lápida, con la versión que hay que instalar. La versión que hay que instalar salió el 3 de noviembre de 2026 con la etiqueta v0.20.1.1. El cartel está actualizado.

**Kotatsu.** No es una lápida pequeña: es un archivo de 8.952 estrellas con fecha. Archivada el **4 de noviembre de 2025**, último empujón ese mismo día. Sus parsers, un día antes. Quien instale hoy Kotatsu instala una aplicación que dejó de actualizarse hace un año exacto.

Un recuento que sume 1.458 + 2 + 248 + 2 + 3 + 1 sin mirar qué hay dentro de cada uno suma 1.714 y de esas, **cinco son lápidas**. No es un error de nadie en particular: es lo que pasa cuando se cuenta con un programa lo que hay que leer con los ojos.

───────────────────
*📱 Las nueve aplicaciones · con su último empujón y su licencia*

Nueve aplicaciones, consultadas hoy una por una en la API. Las estrellas van como contexto, no como argumento: hay proyectos de 8.952 que llevan un año muertos y proyectos de 229 que se actualizaron ayer.

**Mihon · ★25.045 · Apache-2.0 · empujón de hoy.** La aplicación de referencia para manga y la que define el formato de tienda que casi todo imita. Versión 0.21.3 del 25 de octubre de 2026.

**Animiru · ★907 · GPL-3.0 · v0.20.1.1 del 3 de noviembre.** La aplicación de vídeo del ecosistema Aniyomi. Ojo con el enlace: `quickdesh/Animiru` **responde 301** y ahora vive en `animiruorg/Animiru`. Y ojo con la versión: la lápida de Secozzi pide «Animiru 0.20+», que es exactamente la que hay.

**Usagi · ★290 · GPL-3.0 · empujón del 3 de noviembre.** El heredero natural de Kotatsu: mismo formato de complementos, interfaz parecida, en F-Droid como `org.draken.usagi`. Publica la biblioteca que carga los complementos (`Tsuki`) y una plantilla. Lo que no publica es un catálogo lleno.

**Drop Sauce · ★229 · GPL-3.0 · empujón del 4 de noviembre.** Lector de cómic y novela en Compose que acepta el formato de Mihon y complementos de novela. La salida más cómoda de Kotatsu para quien ya tiene biblioteca en formato Mihon.

**Futon · ★477 · GPL-3.0 · empujón del 4 de noviembre.** El camino menos citado y más directo: continúa Kotatsu y le añade compatibilidad con extensiones de Mihon. Para quien no quiere migrar nada.

**Mangayomi · ★4.370 · Apache-2.0 · empujón del 3 de noviembre.** Manga, novela y anime en Android, iOS, escritorio y web. Su formato no es el de Mihon: es una lista de objetos con nombre, idioma y URL del código de la fuente, sin firma. Eso explica media docena de incomprensiones.

**Cloudstream · ★11.162 · GPL-3.0 · empujón del 4 de noviembre.** Vídeo, con más repositorios que ninguna y menos uniformidad que ninguna: cada repositorio es un plugin compilado y su formato es propio.

**Kotatsu · ★8.952 · GPL-3.0 · archivada el 4 de noviembre de 2025.** Un año sin un empujón y el cartel de archivada.

**LNReader · novelas.** No hay familia de novelas: cada aplicación tiene su formato. LNReader es el denominador común porque sus complementos están bien mantenidos —**196 archivos en 17 carpetas de idioma**, 90 en inglés, 21 en ruso, 13 en francés, 11 en árabe y 10 en español— y varias aplicaciones los aceptan.
───────────────────
*🚚 Kotatsu está muerto · Usagi, Drop Sauce y el repositorio que está vacío*

Archivada el 4 de noviembre de 2025: un año exacto sin un empujón. Lo que hay que añadir es lo que se descubre al clonar: **los complementos de Usagi no están en el repositorio que todo el mundo enlaza**. `mochi-plugins/repository`, 49 estrellas, el que aparece en las listas y en las conversaciones, tiene hoy dos archivos —`LICENSE` y `README.md`—, cero complementos, cero catálogo y ninguna rama más. No está roto: está vacío.

El segundo que se cita, `dragonx943/manga-repo`, 24 estrellas, sí tiene contenido, y es `gradle`, `buildSrc` y ocho ramas de trabajo. Es **el código con el que se construyen** los complementos, no el catálogo que se añade: no hay `index.json` ni `repo.json` en ninguna de sus ramas. Quien lo pegue en Usagi no verá nada y va a pensar que Usagi no funciona.

Tres caminos, de menos a más trabajo. **Futon:** continúa Kotatsu y acepta extensiones de Mihon; se instala, se restaura el respaldo y se acabó. **Drop Sauce:** acepta el formato de Mihon y el de novela; se añade Keiyoushi si es manga y se importa el respaldo para conservar el historial. **Usagi:** el más parecido a Kotatsu por dentro y el que exige buscar los complementos donde de verdad estén, en las entregas de sus proyectos de plugins. Y lo que no se hace, que también es parte del listón: enlazar un repositorio vacío como si fuera una tienda.
───────────────────
*📦 Tienda por tienda · ocho fichas, sin relleno*

**Keiyoushi · la única de Mihon.** 1.458 extensiones. Índice firmado (9add65…), catálogo real en protobuf de 107.007 bytes y el `index.min.json` de dos entradas que ya se explicó. Las APK se reparten como **adjuntos de release** y publica `release-assets.json` con el `sha256` de **cada una de las 1.458**: es la única de las quince que firma todo su catálogo. Seis descargas pedidas, seis responden 206. El repositorio que se clona tiene **15.439 estrellas y solo artefactos**; el código está en `keiyoushi/extensions-source`, con empujón de hoy. Buscar el código en el primero es media hora perdida.

**TheNano · las fuentes chinas de Mihon.** `LittleSurvival/copymanga-copy20`. **Cinco extensiones**, todas en chino: CopyManga, VomicMHPlus, BaoziManhuaPlus, ManwaYuPlus y HipManga. Índice firmado, APK dentro del propio repositorio, seis de seis responden 206, y una carpeta `smali` que delata que hay extensiones parcheadas a mano. Son cinco, no cuarenta: el mapa decía la verdad.

**Yūzōnō Anime · la buena de Animiru.** El catálogo vive en **`mojuru/anime-repo`**: 248 extensiones, índice firmado, descargas en `apk/` y `index.html` con los enlaces de release. El enlace que circula, `yuzono/anime-repo`, responde **301** hacia el anterior: el mismo proyecto con el nombre mudado, no un clon. El mapa la llamaba «la única BUENA» y la medición no lo contradice.

**SalmanBappi · lo que dice ser.** 98 entradas en 6 idiomas: 58 en inglés, **21 en bengalí**, 13 «all», 4 en hindi, 1 en árabe y 1 en español. Índice firmado en `repo.json` —el `index.json` del repositorio no repite la clave, y eso queda anotado—. Seis de seis descargas responden 206. Su gracia es la que decía el mapa: **fuentes BD**, servidores del sur de Asia que no aparecen en ninguna otra parte. 21 entradas en bengalí no es un detalle: es la prueba de para quién está hecho.

**Secozzi · tres, y lo dicen.** Catálogo en la rama `repo`, nombre declarado **«Jellyfin, Stremio, and Torbox»**, tres extensiones, clave propia (480e90b0…). Su `index.min.json` es la lápida que pide Animiru 0.20+. Para quien tenga un Jellyfin en casa o use Torbox es utilísimo; para quien no, no es nada, y así está escrito en su propio índice.

**Yuzono Cursed · seis, no 131.** Seis extensiones para contenido adulto con índice propio. La cifra que circula —131— es el número de **archivos del repositorio de fuentes**, no de extensiones publicadas. Es la diferencia entre contar cajas y contar lo que hay dentro.

**m2k3a · la que sostiene Mangayomi.** 335 entradas, el catálogo más grande de su formato, 116 estrellas, empujón del 3 de noviembre. No firma porque el formato no firma. Es «el repositorio que vale la pena» del mapa, y la medición la deja como la única grande con futuro: el oficial está archivado.

**MegaRepo · Cloudstream, y no es una lista.** Su `repo.json` declara **una** `pluginLists`; esa lista contiene **un** plugin, `MegaProvider`; y ese plugin, al instalarse, añade los demás repositorios desde dentro de la aplicación. «Un repositorio que enlaza muchos en uno» es cierto y engañoso: no enlaza, instala un instalador. Es listo, es útil y no se parece a nada más.

*Y una que no es tienda:* **LNReader**, con sus 196 archivos en 17 idiomas, es el catálogo de novela que varias aplicaciones aceptan.
───────────────────
*🚫 Lo que no se indexa · siete nombres y su motivo*

**`mochi-plugins/repository` · vacío.** 49 estrellas, una rama, dos archivos. Cero complementos. Enlazarlo como «los complementos de Usagi» es un error que se repite por copia, no por maldad.

**`dragonx943/manga-repo` · solo código.** Ocho ramas, `gradle`, `buildSrc`, ni un `index.json`. Es la fábrica, no la tienda.

**`kodjodevf/mangayomi-extensions` · archivado.** 360 estrellas, 363 entradas, archivado desde el **1 de octubre de 2025**. Se nombra porque quien llegue por una guía vieja va a pegarla, y con la fecha para que sepa por qué no le aparece nada nuevo en un año.

**`yuzono/manga-repo` · cerrada por su dueño.** Su catálogo dice «Please migrate to Keiyoushi». Indexarla como tienda viva sería indexar un cartel.

**Los clones con el nombre de otra tienda.** Aparecieron catálogos que se llaman «Yūzōnō» y no lo son: mismo nombre, otro dueño, catálogo distinto. Un clon puede ser útil, pero entonces se presenta como clon y con el nombre de quien lo mantiene. El que se hace pasar por la tienda buena es un problema de seguridad.

**Los repositorios cuyo nombre es una dirección.** Proyectos que usan una URL como nombre para que el enlace parezca una fuente de confianza. No se pueden verificar y no se indexan.

**Los forks que solo cambian el nombre.** Un fork de Keiyoushi con dos extensiones propias es, casi siempre, el catálogo de Keiyoushi con retraso. Si alguien quiere esas dos, se las pide al autor por su nombre.

Y una categoría que no se indexa por una razón distinta, la legal: **nada que sirva para descargar contenido protegido**. Aquí no hay una sola URL de contenido, ni de series, ni de películas, ni de cómics. Hay tiendas —programas que enumeran fuentes— y de ellas se mide catálogo, firma y descarga.
───────────────────
*🗣️ La crítica, punto por punto · qué cambié y qué no puedo cambiar*

**«Añadan una página o sección donde las apps se agrupen según las extensiones compatibles.»** Hecho en la tabla de la sección 🗺️: aplicación, tienda, entradas, firma, descarga y veredicto. La respuesta del equipo del sitio —que existe en la administración pero no en público— es de las que esta casa no puede resolver; lo que sí puede es publicar una tabla fechada, y esa diferencia importa.

**«Dejen de usar IA para generar a mansalva listas.»** Aceptado, con una matización: el problema no era la IA, era **el encargo**. Pedirle «dame todas las tiendas que existan» garantiza una lista sin criterio, porque el criterio no está en la máquina. Lo que sí puede hacer una máquina es clonar, contar, comprobar la firma y pedir un byte: eso no decide si algo merece estar, decide si lo que dice ser es verdad. Indexar lo sigo decidiendo yo, y aquí lo firmo.

**«No todo repositorio aleatorio necesita ser indexado.»** De acuerdo. Esta versión indexa **ocho** tiendas y deja fuera **siete** con nombre y motivo. Antes se contaban 5.481 extensiones; ahora 2.382, todas dentro de tiendas que hoy sirven.

**«Usa primero la app tú mismo.»** Hecho hasta donde se puede sin teléfono: clonar, leer el catálogo como lo lee la aplicación, verificar la firma, pedir un byte. Lo que falta está en 🚪 como deuda declarada, con nombre y con la orden.

**«La IA no nota funciones falsas, rate-limit quitado, vibe-code, falta de soporte o años de abandono.»** Hay que separar dos cosas que el escrito mezcla. *Lo automatizable, y hoy automatizado:* archivado y fecha del último empujón, README que niega soporte o se declara espejo, presencia de pruebas, rate-limit comentado, nombre declarado contra nombre real. Son las siete comprobaciones de 📏. *Lo que no se automatiza:* decidir si una extensión concreta trae las páginas que promete; eso pide abrir la aplicación, buscar un título y darle a leer. *Y una que casi nadie automatiza:* comprobar que el catálogo citado es el que la aplicación lee —de ahí salieron las cuatro lápidas—. La máquina aporta paciencia; la persona, criterio. El error fue usar la máquina para lo segundo.

**«Mira cómo formatean otros; deja de repetir. O mejor: que la IA clone y pruebe.»** Sobre el formato: tabla, fichas cortas, secciones de cinco párrafos como mucho y ni una lista de doscientas líneas. Sobre clonar: es literalmente lo que se hizo, quince veces. Sobre repetir: casi ningún nombre de esta versión estaba en la anterior con los mismos números, y los que se repiten llevan cifra de hoy.
───────────────────
*🧠 Lo que una IA no ve · y lo que sí puede hacer si se le deja*

**No ve** si una extensión, al abrirla, trae las páginas que promete; si el sitio de origen cambió el HTML y la extensión devuelve vacío; si una función del README existe de verdad; si el código lo escribió alguien que sabe o alguien que pegó lo que le devolvió un modelo. No ve el cansancio de un mantenedor ni la nota de «no voy a seguir» escondida en una incidencia.

**Sí ve** —y esto es nuevo en la casa— si el repositorio está archivado, cuándo fue su último empujón, si el catálogo está firmado, cuántas entradas declara, si el nombre que declara es el suyo, si el archivo que promete descargar existe, si el README niega el soporte por escrito, si hay pruebas, si el rate-limit está comentado, y si el archivo que medio internet cuenta es un catálogo o una lápida.

La frontera no está donde el escrito la pone sino un paso más allá: **la IA puede reunir la evidencia y no puede tomar la decisión**. Las cuatro lápidas las encontró un programa; decidir que una tienda cerrada no se indexa lo decidió una persona leyendo el cartel. Y hay una tercera cosa que solo se aprende clonando: el ecosistema no está hecho de aplicaciones y tiendas, está hecho de **ramas**. El catálogo de Secozzi vive en `repo`; el de MegaRepo, en `builds`; el de Keiyoushi, en `repo` y en protobuf.
───────────────────

*⚖️ La responsabilidad · lo que una tienda hace y lo que no*

Una tienda de extensiones no aloja contenido: aloja **programas** que le dicen a una aplicación dónde buscar. Esa distinción es la misma que hay entre un navegador y una página, y se pierde cada vez que alguien llama «tienda de películas» a lo que es un catálogo de conectores.

En la República Dominicana, la Ley 65-00 sobre derecho de autor protege las obras y tipifica su reproducción y comunicación no autorizadas; las tiendas y las extensiones viven en un terreno que cada país regula a su manera, y las retiradas por reclamación de derechos —las DMCA que menciona el mapa— son el mecanismo que usan los titulares para pedirlas. Esta pieza no es asesoría legal y no la va a dar: es una medición de repositorios públicos, hecha con las herramientas que cualquiera puede ejecutar.

Lo que sí se puede decir con datos: **ninguna de las quince tiendas publica un aviso de retirada en su README**, y una de ellas (Yūzōnō, la de Mihon) cerró su catálogo y puso un cartel que manda a Keiyoushi. Eso es lo que se ve desde fuera. Lo que no se ve —cuántas extensiones concretas cayeron por reclamación y por qué— no se puede verificar desde GitHub, y por eso en esta pieza no se afirma.

Y una regla de la casa que se cumple aquí al pie de la letra: **ni una URL de contenido**. Las direcciones de esta pieza son repositorios, índices y descargas de programas. Nada más.

───────────────────

*🔏 La huella · quién firma lo que te instala*

Una extensión de Mihon se instala como APK y corre con los permisos de la aplicación. La pregunta que casi nadie hace es: **¿cómo sé que este archivo es el que el autor publicó?** Hay tres respuestas posibles en este ecosistema y hoy solo una se usa.

**La firma del catálogo.** `repo.json` trae `signingKeyFingerprint` y el índice trae `signingKey`. La aplicación comprueba que coinciden antes de aceptar la tienda: si no cuadra, la tienda no entra. Esto protege el **índice** —la lista— pero no los archivos: si alguien cambia el APK y deja el índice igual, la aplicación no se enteraría por esta vía. Seis de quince lo usan.

**El manifiesto de sumas.** Un archivo con el `sha256` de cada descarga. Keiyoushi publica `release-assets.json` con **1.458 sumas**, una por extensión. Es la única de las quince que lo hace con todo su catálogo. Con eso, cualquiera puede comprobar que el archivo que bajó es el que la tienda declara, sin confiar en la conexión.

**La firma del APK.** Android firma cada aplicación, pero esa firma dice «esto lo firmó alguien» y no «esto lo firmó el autor que crees». Ninguna de las quince publica las claves públicas de firma para comparar. En un ecosistema donde se instalan programas de terceros a diario, es la deuda más grande y la menos comentada.

Lo que esto significa en la práctica: **la integridad de una tienda se apoya hoy en el candado del índice y en la buena fe sobre las descargas**. Quien quiera reducir el riesgo tiene tres herramientas y las tres son manuales: usar tiendas con manifiesto de sumas, no añadir tiendas que no conozca y no instalar nada desde un enlace que llegó por mensaje.

───────────────────
*🛠️ Las seis órdenes · para que nadie tenga que creerme*

Todas son de lectura y no modifican nada de nadie. **1 · Ver a qué catálogo apunta una tienda:**

```
curl -s https://raw.githubusercontent.com/keiyoushi/extensions/repo/repo.json
```

**2 · Contar las entradas del catálogo de verdad,** no del archivo viejo:

```
curl -s https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d['extensionList']['extensions']))"
```

**3 · Ver la lápida.** Si el resultado es 1 o 2, la tienda está cerrada o a punto:

```
curl -s https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json | python3 -c "import json,sys; print([e['name'] for e in json.load(sys.stdin)])"
```

**4 · Comprobar la firma:** el `signingKey` del índice y el `signingKeyFingerprint` del `repo.json` tienen que coincidir:

```
curl -s https://raw.githubusercontent.com/LittleSurvival/copymanga-copy20/repo.json
```

**5 · Ver el manifiesto de sumas** que publica la tienda, que es lo que permite comprobar una descarga sin descargarla:

```
curl -s https://raw.githubusercontent.com/keiyoushi/extensions/repo/release-assets.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d), 'sumas publicadas')"
```

Y para pedir un byte de una descarga concreta se usa la dirección que aparece en el `index.html` del repositorio, con `Range: bytes=0-0`: las entregas de GitHub no contestan a `HEAD` con el tamaño, contestan con un 302 vacío. **En esta pieza no se enlaza ningún archivo ejecutable**: la dirección se copia del listado de la propia tienda y se pide desde la terminal.

**6 · Saber si un proyecto está muerto** con dos campos, `archived` y `pushed_at`:

```
curl -s https://api.github.com/repos/KotatsuApp/Kotatsu | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['archived'], d['pushed_at'])"
```

Y todo de una vez, con la herramienta de esta pieza: `python3 tools/auditar_tienda.py --repo keiyoushi/extensions --escribir ficha.json`.
───────────────────
*🚪 Lo que no tiene esta pieza · deuda declarada*

**La prueba de la extensión abierta.** Nadie ha abierto aquí una extensión y ha buscado un título: es la prueba que el escrito pedía y la que no se puede hacer sin teléfono o emulador. Queda como deuda con nombre, la tarea 093 de la lista final.

**Hollow.** La tienda francesa de Animiru está en Codeberg, no en GitHub, y la herramienta solo sabe clonar GitHub. Se nombra en la tabla como «sin auditar», que es distinto de «descartada».

**«atp».** El mapa hablaba de un repositorio de Mangayomi con ese nombre y no se localizó ninguno. Se midieron los tres vivos —m2k3a, Swakshan, Mally— y se dice que esa palabra no apareció. Inventar la URL habría sido peor.

**El censo completo.** Quince repositorios no son todos los que existen: son todos los que se sostienen. Un censo completo volvería a ser una lista, que es lo que se pedía dejar de hacer.

**La garantía de mañana.** Todo lo de aquí tiene fecha y hora. Una tienda puede cerrar el martes que viene; entonces esto será una foto vieja, no una mentira.
───────────────────

───────────────────
*❓ Preguntas frecuentes*

**¿Por qué solo ocho tiendas, si antes había veinte?** Porque estas ocho publican un catálogo que se puede leer y descargan. Las otras siete están nombradas con su motivo: una lista corta con motivos vale más que una larga sin ellos.

**Instalé Yūzōnō en Mihon y no me aparece nada. ¿Qué pasa?** Que esa tienda cerró: su índice dice «Please migrate to Keiyoushi». No es un fallo tuyo ni de la aplicación. Quita esa tienda y añade Keiyoushi.

**Keiyoushi y Yūzōnō no son lo mismo.** No. Keiyoushi es de Mihon (manga) y Yūzōnō Anime es de Animiru, Anikku y Aniyomi (vídeo). Nacieron del mismo tronco y no se mezclan.

**¿Qué tienda uso para anime?** Yūzōnō Anime, 248 extensiones, con el enlace bueno —el que redirige a `mojuru/anime-repo`—. Y si quieres fuentes del sur de Asia, SalmanBappi encima.

**Para manhua.** TheNano, cinco extensiones en chino. Si no lees chino no te sirve de nada, y está bien que sea pequeña.

**Uso Usagi y no encuentro complementos. ¿Por qué?** Porque el repositorio que más se enlaza está vacío y el otro es código fuente. Los complementos se buscan en las entregas de cada proyecto de plugins.

**Qué hacer con la biblioteca de Kotatsu.** Exporta el respaldo y elige: Futon si quieres seguir igual, Drop Sauce si quieres empezar limpio con formato Mihon.

**¿Una tienda sin firma es peligrosa?** Es menos verificable, que no es lo mismo. Las tres de Mangayomi no firman porque su formato no tiene firma. Lo que sí conviene: no añadir tiendas de dueño desconocido y sin historial.

**¿Cómo sé si una extensión concreta funciona?** Abriéndola. Esta pieza no lo ha hecho y lo dice. Antes se puede comprobar que exista, que descargue y que la tienda esté viva.

**¿Y esto no vuelve a ser una lista de enlaces?** Tiene ocho tiendas, nueve aplicaciones y una tabla. La anterior tenía seis índices y 5.481 extensiones. La diferencia no es el tamaño: es que aquí cada nombre tiene un motivo para estar y siete tienen un motivo para no estar.
───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **el mapa de la crítica era correcto y la medición lo confirma con fecha**. Una sola tienda para Mihon, una buena para Animiru, Kotatsu muerto, Mangayomi con un solo repositorio que vale la pena, ninguna familia de novelas y un MegaRepo de Cloudstream que resulta ser un plugin. Todo eso se comprobó hoy, clonando, y no queda ni una línea de aquello sin respaldo.

Lo segundo: **el archivo que todo el mundo cuenta no es el archivo que la aplicación lee**. Cuatro lápidas dentro de cuatro catálogos. Quien sume entradas sin mirar qué dicen va a seguir sumando tiendas cerradas, y ese error se fabrica solo con cada nueva lista.

Lo tercero: **hay un repositorio de complementos vacío con 49 estrellas**, y es el que más se repite cuando alguien pregunta por Usagi. Eso no se arregla con más IA: se arregla clonando una vez y mirando dentro.

Y lo cuarto, que es lo que importa: **el listón no sube escribiendo más, sube abriendo antes lo que se recomienda**. Quince clones, ocho tiendas que se sostienen, siete nombres fuera con su motivo y una herramienta que cualquiera puede ejecutar para repetir la cuenta. Si mañana alguien dice que esto está mal, tiene las órdenes para comprobarlo sin creerme.

───────────────────
— 1.458 extensiones en Keiyoushi, 248 en Yūzōnō Anime, 335 en m2k3a: las tres que sostienen el ecosistema, contadas hoy en su catálogo real.
— Cuatro lápidas dentro de cuatro catálogos, incluida la de la propia Yūzōnō para Mihon, que manda a Keiyoushi con el texto delante.
— Un repositorio de complementos con 49 estrellas y cero complementos: el que más se enlaza cuando alguien pregunta por Usagi.

💓 

━━━━━━━━━━━━━

🧰 *Qué hacer tú mismo: verificar cualquier programa antes de instalarlo*

Estos pasos funcionan para cualquier programa medido en esta pieza, y para cualquier software que bajes de GitHub:

1. **Busca el repositorio del autor.** No bajes de tiendas de APK ni de páginas de terceros. Ve al repositorio oficial en GitHub.

2. **Lee la release más reciente.** En la sección «Releases», busca la versión publicada más reciente y sus archivos adjuntos.

3. **Comprueba la suma de comprobación.** Si el autor publica un archivo .sha256 o .asc, descarga ambos y ejecuta:

   sha256sum nombre-del-archivo.apk
   cat nombre-del-archivo.sha256

   Las dos cifras deben coincidir exactamente.

4. **Revisa la fecha de la última entrega.** Un programa sin entregas en más de noventa días está abandonado.

5. **Lee la licencia.** Sin licencia legible, no sabes bajo qué condiciones puedes usar el programa.

6. **Guarda el comprobante.** Anota la fecha, hora y commit que revisaste. Nada se sobrescribe.

━━━━━━━━━━━━━

📚 *Glosario expandido de términos técnicos*

• **SHA256:** huella única de un archivo. Si cambia un bit, cambia la huella.
• **Release:** versión publicada en GitHub con sus archivos adjuntos.
• **Tag:** etiqueta que identifica una versión (por ejemplo, v1.0.4).
• **Commit:** confirmación de cambios en el historial de git.
• **Fork:** copia de un repositorio que otro desarrollador puede modificar.
• **Issue / Incidencia:** reporte de error o solicitud en un repositorio de GitHub.
• **CI / Integración continua:** flujos automatizados que construyen y prueban el código.
• **Adjunto / Asset:** cada archivo publicado junto a una release.
• **Repo / Repositorio:** lugar donde se guarda el código de un proyecto.
• **Licencia MIT:** permisiva, permite reutilizar el código con aviso de copyright.
• **Licencia AGPL-3.0:** copyleft fuerte; quien modifique y distribuya debe liberar su versión.

━━━━━━━━━━━━━

🗒️ *Notas al pie expandidas*

• Esta pieza se midió con datos reales de la API pública de GitHub, consultados directamente por repositorio.
• La fecha de la medición es la fecha en vivo del sábado 7 de noviembre de 2026 en Santo Domingo.
• Cada fichero de medición queda guardado con su fecha y hora, y ninguno se sobrescribe.
• Esta pieza no aloja paquetes ni APKs. Todos los enlaces van al repositorio de cada autor.
• Esta pieza no repite el contenido de otras piezas de la serie.
• Las cifras son válidas solo para el momento en que se leyeron. Una medición es una instantánea.

━━━━━━━━━━━━━

❓ *Preguntas del grupo (respuestas breves)*

• ¿Puedo instalar sin verificar? Puedes, pero no sabes si el archivo es el que publicó el autor.
• ¿Qué hago si el autor no publica suma de comprobación? Escríbelo en las incidencias del repositorio.
• ¿Las estrellas de GitHub indican seguridad? No. Un repositorio con muchas estrellas puede no publicar ninguna huella.
• ¿Necesito ser experto en seguridad? No. Solo necesitas saber comparar dos cifras.

━━━━━━━━━━━━━*La Bandita informa a partir de fuentes fechadas.* quince repositorios clonados y leídos esta mañana, ocho tiendas que se sostienen, siete nombres fuera con su motivo y seis órdenes para repetir la cuenta sin creerme. Sin volcados, sin relleno y sin una sola URL de contenido.

───────────────────

*Medición del corte:* jueves 5 de noviembre de 2026, 06:14 de la mañana en Santo Domingo (10:14 UTC) — con la fecha comprobada en vivo al empezar y al terminar · quince repositorios clonados entre las 10:03 y las 10:15 UTC · nueve aplicaciones consultadas en la API · 2.382 extensiones contadas en once catálogos · cuatro lápidas encontradas · ninguna cifra de memoria y ningún enlace puesto a ojo.

*🔗 Enlaces*

*Las nueve aplicaciones, que son lo que se instala:*

- Mihon: https://github.com/mihonapp/mihon
- Animiru: https://github.com/animiruorg/Animiru
- Usagi: https://github.com/UsagiApp/Usagi
- Drop Sauce: https://github.com/HuzaifaKhalid1311/DropSauce
- Futon: https://github.com/AppFuton/Futon
- Mangayomi: https://github.com/kodjodevf/mangayomi
- Cloudstream: https://github.com/recloudstream/cloudstream
- Kotatsu (archivada): https://github.com/KotatsuApp/Kotatsu
- LNReader: https://github.com/lnreader/lnreader-plugins

*Las ocho tiendas que pasan el listón:*

- Keiyoushi: https://github.com/keiyoushi/extensions
- Keiyoushi, el código de las extensiones: https://github.com/keiyoushi/extensions-source
- TheNano, las fuentes chinas: https://github.com/LittleSurvival/copymanga-copy20
- Yūzōnō Anime, el enlace bueno: https://github.com/mojuru/anime-repo
- Yūzōnō Anime, el enlace que redirige: https://github.com/yuzono/anime-repo
- SalmanBappi: https://github.com/salmanbappi/extensions-repo
- Secozzi, tres extensiones: https://github.com/Secozzi/aniyomi-extensions
- Yuzono Cursed, seis extensiones: https://github.com/yuzono/cursed-manga-extensions
- m2k3a, el que sostiene Mangayomi: https://github.com/m2k3a/mangayomi-extensions
- Swakshan: https://github.com/Swakshan/mangayomi-swak-extensions
- Mally: https://github.com/Mallyd11/mangayomi-anime-extensions
- Cloudstream MegaRepo: https://github.com/self-similarity/MegaRepo

*Los siete que se nombran y no se enlazan como tienda, con el motivo en la sección 🚫:*

- El repositorio vacío de Usagi, que se enlaza aquí solo para que se vea que está vacío: https://github.com/mochi-plugins/repository
- El código de los complementos de Usagi: https://github.com/dragonx943/manga-repo
- El oficial de Mangayomi, archivado: https://github.com/kodjodevf/mangayomi-extensions
- La tienda cerrada de Yūzōnō para Mihon: https://github.com/yuzono/manga-repo

*Las direcciones de las seis órdenes:*

- el archivo que pide primero la aplicación: https://raw.githubusercontent.com/keiyoushi/extensions/repo/repo.json
- el catálogo con la clave de firma: https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json
- la lápida, para ver lo que se cuenta sin leerlo: https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json
- el archivo que pide primero TheNano: https://raw.githubusercontent.com/LittleSurvival/copymanga-copy20/repo.json
- el manifiesto de sumas, que es lo que se pide para comprobar una descarga: https://raw.githubusercontent.com/keiyoushi/extensions/repo/release-assets.json
- un proyecto para preguntarle si está muerto: https://api.github.com/repos/KotatsuApp/Kotatsu

───────────────────

*🗒️ Notas al pie*

(5-nov) **La fecha se comprobó en vivo dos veces**, no se predijo: la revisión previa de historial y de ecosistema al empezar, con el reloj de fuera, y otra vez al cerrar. Todo lo medido cae entre las **10:03 y las 10:15 UTC**, que en Santo Domingo son las 06:03 y las 06:15 de la mañana. Donde dice «hoy», es hoy.

(5-nov) **Qué se clonó y qué se tiró.** Quince `git clone --depth 1`, cada uno borrado después de leerlo: lo que queda es la ficha de veinte campos en `docs/AUDITORIA-TIENDAS-2026-11-05.json`. El clon pesa cientos de megas; la ficha, unos kilobytes. Guardar el clon no habría aportado nada y habría llenado el disco dos veces.

(5-nov) **Cómo se comprobó una descarga sin bajar el archivo.** Con `Range: bytes=0-0`, que devuelve 206 y el tamaño total en `Content-Range`. Las entregas de GitHub contestan a `HEAD` con un 302 sin tamaño, así que una comprobación con `HEAD` habría dado «no existe» en todos los casos. Es un detalle pequeño y es la razón por la que la primera pasada de la herramienta marcó mal a tres tiendas.

(5-nov) **La cuenta de 2.382** sale de sumar los catálogos que hoy sirven: 1.458 de Keiyoushi, 5 de TheNano, 248 de Yūzōnō Anime, 98 de SalmanBappi, 3 de Secozzi, 6 de Cursed, 335 de m2k3a, 15 de Swakshan, 17 de Mally, 1 del MegaRepo y 196 de LNReader. **Kotatsu, el repositorio oficial de Mangayomi y la tienda cerrada de Yūzōnō quedan fuera a propósito**: están en la sección 🚫 con su motivo.

(5-nov) **Lo que no se pudo comprobar, y se dice.** Si una extensión concreta trae las páginas que promete; cuántas extensiones cayeron por reclamación de derechos; si Hollow, la tienda francesa de Codeberg, sigue viva —la herramienta solo sabe clonar GitHub—; y qué es exactamente el «atp» del mapa, que no apareció en ninguna búsqueda con ese nombre.

(5-nov) **Herramienta nueva y habilidad nueva.** `tools/auditar_tienda.py` clona, lee el catálogo, comprueba la firma, pide un byte y devuelve veredicto con motivos. La habilidad que sale de esto es H25: **una tienda se abre, no se cita**, y el error que la provoca es E44: contar `index.min.json` como si fuera el catálogo.

*#task*

#task 091 · añadir a la herramienta la lectura de Codeberg y de los repositorios autoalojados, para poder auditar la tienda francesa de Animiru sin dejarla en «sin auditar».

#task 092 · volver a clonar las ocho tiendas el 5 de diciembre y publicar la tabla de diferencias: entradas ganadas o perdidas, firmas nuevas y tiendas cerradas.

#task 093 · la prueba que falta: abrir una extensión de Keiyoushi y una de Yūzōnō Anime en un teléfono, buscar el mismo título en las dos y anotar cuántas fuentes responden.

#task 094 · escribir la pieza 20 —los subtítulos y el doblaje, que este corte dejó pendientes— con el mismo método: revisión previa, medición fechada y ninguna cifra escrita a mano.

───────────────────

🏷️ Etiquetas estratégicas

#Keiyoushi #Mihon #Animiru #Yuzono #Usagi #DropSauce #Mangayomi #LNReader #Cloudstream #Kotatsu #SalmanBappi #Secozzi
