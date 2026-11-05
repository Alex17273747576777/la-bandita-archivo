# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab18/docs/talleres/pieza19')
from d19 import *
A=AGG; T=[]; w=T.append
K=INDICE

w(f"""*Las tiendas de extensiones, con el listón arriba: veinte piezas medidas hoy —la que es la única, las tres que están archivadas y las dos que son un clon con otro nombre—*

*La Bandita · jueves 5 de noviembre de 2026, {HORA} de la mañana en Santo Domingo · edición dominicano-español · pieza 19 de Facebook*

⏱️ *Lectura total: 28 minutos · {palabras(A['vivos'])} piezas medidas hoy a las {HORA} · {num(A['estrellas'])} estrellas · {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas —el 0,07 %, la proporción más baja de toda la serie— · {palabras(A['arch'])} archivadas · 5.481 extensiones contadas una por una en {palabras(6)} índices*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · la lista que circula tiene cifras de una wiki
├── ⚡ En una página · 🕰️ la medición de las {HORA}
├── 🧠 Qué es una tienda por dentro · 🔬 anatomía de una extensión
├── 🗺️ La tabla que hacía falta · 📱 las siete aplicaciones · 🚚 salir de Kotatsu
├── 📦 Las seis tiendas que pasan el listón
├── 📏 El listón nuevo · seis comprobaciones antes de indexar
├── 🗣️ Lo que la comunidad reclamó · 🚫 lo que no se indexa
├── ⚖️ La responsabilidad · 🔏 la huella · 🛠️ seis órdenes
└── 🚪 lo que no tiene · 📅 la semana · ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

> *Semilla de esta pieza:* la lista de tiendas de extensiones que circula por los grupos tiene **cifras de una wiki que nadie vuelve a medir**. Esta mañana se abrieron los índices publicados de seis tiendas y se contaron sus entradas una por una: donde la lista dice cientos, hay seis; donde dice que una tienda está viva, el repositorio está **archivado desde hace un año**; y donde una dirección era la de siempre, el servidor responde **que se mudó**. El listón no se sube con más enlaces: se sube **contando**.

Este corte mide {palabras(A['vivos'])} piezas y **no trescientas**, y eso es deliberado. La comunidad de estas aplicaciones lleva meses pidiendo lo contrario de lo que hace un índice automático: **menos repositorios, mejor comprobados**. Aquí van las seis tiendas que sirven a alguna aplicación, las siete que son clon, ruido o están de más —con el motivo y la cifra— y la tabla que faltaba: **qué tienda le sirve a qué aplicación**.

Y una cifra que cierra el círculo de la serie: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}: el 0,07 %**, empatando con la peor medición del año —las tiendas de la pieza 10 (0,08 %)—. Un ecosistema que vive de instalar código de terceros en el teléfono y que **no firma ni lo que sirve con su propio nombre**.

───────────────────

*⚡ En una página*

{palabras(A['vivos']).capitalize()} piezas medidas a las {HORA}: **{num(A['estrellas'])} estrellas**, **{num(A['descargas'])} descargas**, {palabras(A['push7'])} con empujón de la última semana y **{palabras(A['arch'])} archivadas** —las tres del mismo tema: Kotatsu, sus parsers y el repositorio oficial de Mangayomi—. La nota mediana es **{num(int(A['mediana_puntos']))} sobre 80**, la más baja de las diecinueve piezas, y **ningún repositorio del tema tiene `SECURITY.md`**: cero de veinte.

**5.481 extensiones contadas en los índices publicados esta mañana**, repartidas así: **1.458** en Keiyoushi —la única tienda de la familia Mihon—, **248** en Yūzōnō (la de la familia Aniyomi), **335** en m2k3a (Mangayomi), **327** en LNReader, **97** en SalmanBappi y **6** en el clon que la lista vieja daba por 131.

Y un detalle que no tiene ningún otro tema de la serie, medido sobre los veinte repositorios: **{palabras(A['security'])} de {palabras(A['vivos'])} publican un `SECURITY.md`**. Cero. En un ecosistema donde la aplicación ejecuta código de terceros en tu teléfono, no hay ni un canal declarado para avisar de un fallo.

Las tres frases que resumen el corte, y las tres están medidas:

- **Keiyoushi es la única tienda real de la familia Mihon.** Todo lo demás con esa forma es un clon con su nombre en la portada: `cuong-tran/manga-repo` **declara llamarse «Yūzōnō»** en su propio índice y publica **1.447** extensiones —es Keiyoushi por dentro—, y `mojuru/cursed-manga-repo` declara **«Cursed Yūzōnō»** y publica **{K['mojuru/cursed-manga-repo']['publicadas']}**.
- **Kotatsu está muerto y hay fecha**: el repositorio quedó **archivado el 4 de noviembre de 2025**, hace 366 días, y sus parsers al día siguiente. Sus herederos vivos son **Usagi** y **DropSauce**, los dos de este año.
- **El repositorio de publicación de la tienda Yūzōnō se mudó**: la dirección que circula responde **301** hacia `mojuru/anime-repo`. Media lista de la comunidad apunta a un enlace que redirige.

───────────────────

*🕰️ La medición de las {HORA} · y cómo se cuenta una tienda de verdad*

Antes de medir nada, la revisión que ya es regla: **fecha en vivo**, **historial** —dieciocho publicadas y el mapa de 125 en la 19— y **ecosistema**. Después, las {palabras(A['vivos'])} direcciones medidas en vivo a las {HORA}, con su fecha, su licencia y su estado de archivo, en `docs/MEDICION-19-tiendas-2026-11-05.json`.

**Las extensiones no se citan: se cuentan.** Para cada tienda se abrió su índice publicado —`repo.json`, `index.json` o `index.min.json`—, se descargó y se contaron las entradas. Eso es lo que hay detrás de cada cifra de esta pieza, y por eso las cifras no coinciden con la wiki que todo el mundo copia:

| Tienda | Lo que dice la lista vieja | Lo que dice su índice hoy |
|---|---|---|
| Keiyoushi | «1503» | **{num(K['keiyoushi/extensions']['publicadas'])} publicadas · {num(K['keiyoushi/extensions']['fuentes'])} fuentes** |
| Yūzōnō (Aniyomi) | «250» | **{num(K['yuzono/anime-extensions']['publicadas'])}** |
| Cursed (Yūzōnō maldito) | «131» | **{K['mojuru/cursed-manga-repo']['publicadas']}** |
| SalmanBappi | «48» | **{num(K['salmanbappi/sb-extensions-source']['publicadas'])} fuentes · 21 en bengalí** |
| Mangayomi (m2k3a) | «275» | **{num(K['m2k3a/mangayomi-extensions']['publicadas'])}** |
| LNReader | «327» | **{num(K['lnreader/lnreader-plugins']['publicadas'])}** |

**La diferencia no es un error de nadie: es el paso del tiempo.** Una wiki cuenta lo que vio un día y no vuelve; un índice cuenta lo que hay. Cursed pasó de 131 a 6 —le retiraron casi todo—, y esa sola línea explica por qué esta pieza existe.

**Una nota sobre el mapa.** El mapa de 125 pone en la 19 «subtítulos y doblaje». Este corte no la sigue: el dueño pidió volver sobre las tiendas de extensiones con el listón más alto, después de que la comunidad de estas aplicaciones lo reclamara. Se dice y no se disimula; los subtítulos conservan su número.

───────────────────

*🧠 Qué es una tienda por dentro · el índice, la firma y el APK*

Para juzgar una tienda hay que saber qué es, y no es una página web: es **tres archivos y una carpeta**.

**El primero es `repo.json`.** Un archivo pequeño que le dice a la aplicación dónde está el índice de verdad. Cambia poco y casi nunca se firma. Cuando la dirección de este archivo se muda —como le pasó a Yūzōnō—, la aplicación que la tenía guardada deja de actualizar sin decir por qué.

**El segundo es el índice**: `index.json`, o su versión comprimida `index.min.json`. Trae la lista de extensiones, cada una con su nombre, su paquete, su idioma, su versión y **la dirección del APK**. Es el archivo que se cuenta. Y aquí está el detalle que casi nadie mira: **un índice puede declarar una clave de firma**. Keiyoushi la declara —`{K['keiyoushi/extensions']['clave']}`—, y eso significa que la aplicación puede comprobar que el índice no lo ha tocado nadie por el camino. **Yūzōnō también la declara. Cursed, también. SalmanBappi y m2k3a, no.**

**El tercero es el APK de cada extensión**, alojado en las entregas del propio repositorio. Y ahí llega la cuenta de esta pieza: las seis tiendas juntas publican **{num(A['adjuntos'])} archivos** y **solo uno de los veinte repositorios publica alguna suma** —LNReader, con {num(E['lnreader/lnreader-plugins']['con_huella'])}—. Es decir: **la aplicación comprueba el índice de Keiyoushi con su clave, y después instala un APK que nadie firma en un archivo aparte**.

**Y la carpeta es el código**: casi todas las tiendas separan el repositorio de publicación —los APK, cientos de megas— del repositorio de fuentes, donde está el código que se compila. Keiyoushi tiene **{num(K['keiyoushi/extensions']['fuentes'])} fuentes** en su repositorio de código y publica **{num(K['keiyoushi/extensions']['publicadas'])}** extensiones: las cinco que faltan son las que no compilaron. Yūzōnō tiene {num(K['yuzono/anime-extensions']['fuentes'])} fuentes y publica las mismas {num(K['yuzono/anime-extensions']['publicadas'])}.

**Lo que esto cambia al juzgar:** una tienda con tres estrellas puede tener un catálogo enorme y estar perfectamente mantenida —m2k3a, {num(R['m2k3a/mangayomi-extensions']['stars'])} estrellas y {num(K['m2k3a/mangayomi-extensions']['publicadas'])} extensiones—; y una con veinticuatro estrellas puede tener **una**. Las estrellas miden otra cosa.

───────────────────

*🗺️ La tabla que hacía falta · qué tienda sirve a qué aplicación*

Esto es lo que la comunidad venía pidiendo: las aplicaciones agrupadas por **qué extensiones aceptan**. Se lee al revés que una lista de recomendaciones —primero la aplicación, después la tienda— y cada casilla está comprobada hoy.

| Aplicación | Tienda que le sirve | Extensiones | Estado de la tienda |
|---|---|---|---|
| **Mihon** y sus variantes (Komikku, TachiyomiSY…) | **Keiyoushi** | {num(K['keiyoushi/extensions']['publicadas'])} | viva · índice firmado · empujón de ayer |
| Mihon y variantes — *alternativa* | cuong-tran/manga-repo | {num(K['cuong-tran/manga-repo']['publicadas'])} | **es Keiyoushi renombrado** |
| Mihon y variantes — *alternativa* | mojuru/cursed-manga-repo | {K['mojuru/cursed-manga-repo']['publicadas']} | clon con su nombre |
| **Aniyomi** y **Animiru** | **Yūzōnō** | {num(K['yuzono/anime-extensions']['publicadas'])} | viva · índice firmado · el repo de publicación **mudó** |
| Aniyomi — *fuentes del sur de Asia* | SalmanBappi | {num(K['salmanbappi/sb-extensions-source']['publicadas'])} | viva · 21 en bengalí · sin firma de índice |
| **Usagi** | dragón (plugin propio) + fuentes compatibles Tsuki | {K['dragonx943/manga-repo']['publicadas']} | viva · 24★ y **una** extensión |
| **DropSauce** | acepta el formato de tienda de Mihon | — | viva · {num(R['HuzaifaKhalid1311/DropSauce']['stars'])}★ · {num(R['HuzaifaKhalid1311/DropSauce']['entregas'])} entregas |
| **Kotatsu** | — | — | **archivada el 4-nov-2025** |
| **Mangayomi** | m2k3a | {num(K['m2k3a/mangayomi-extensions']['publicadas'])} | viva · la oficial está **archivada** |
| **LNReader** | lnreader-plugins | {num(K['lnreader/lnreader-plugins']['publicadas'])} | viva · el único que firma archivos |
| **Cloudstream** | MegaRepo (admknight) y Cs-Karma | — | vivas · sin licencia legible |

**Tres cosas que la tabla dice y una lista en columnas no diría:**

La primera: **Mihon y Aniyomi no comparten tienda**, y es el error más repetido de las guías. Keiyoushi sirve a la familia Mihon; Yūzōnō sirve a la familia Aniyomi. Meterse una en la otra es el 90 % de los «no me sale la extensión» de los grupos.

La segunda: **no existe una familia de novelas.** LNReader tiene su formato de plugin, y algunas aplicaciones de lectura aceptan esos plugins, pero cada una los compila a su manera. Por eso LNReader aparece solo en su fila: **{num(K['lnreader/lnreader-plugins']['publicadas'])} plugins** que sirven a la aplicación para la que se escribieron y a las que decidieron ser compatibles, no a todas.

La tercera: **DropSauce es la excepción que conviene saber** si vienes de Kotatsu: acepta el formato de tienda de Mihon, así que hereda la de Keiyoushi sin conversión. Es la vía menos traumática para salir de una aplicación archivada.

───────────────────

*📏 El listón nuevo · seis comprobaciones antes de pedir que se indexe algo*

Esta sección es la que el dueño pidió y la que la comunidad reclamó, palabra por palabra: antes de añadir un repositorio a una lista pública, **seis comprobaciones que hace una persona en dos minutos** —y que un volcado automático no hace nunca—. Cada una va con el caso real que la justifica esta mañana.

**1 · ¿Está archivado?** No es un matiz: es el estado que el propio autor declaró al cerrar. **Kotatsu** está archivado desde el 4 de noviembre de 2025 —366 días—, **sus parsers** desde el 3 de noviembre y **el repositorio oficial de Mangayomi** desde el 1 de octubre de 2025, con 360 estrellas. Los tres siguen en las listas. Una línea de la API lo dice: `"archived": true`.

**2 · ¿Cuándo fue el último empujón, y no cuándo nació?** Un proyecto puede tener diez años y estar vivo —mihon, {num(R['mihonapp/mihon']['dias_nace'])} días y empujón de hoy— o tener dos y estar parado. La fecha que importa es la del último empujón, no la de creación ni la de la última estrella.

**3 · ¿El índice tiene lo que la descripción promete?** Aquí se cae la mitad de las listas. `dragonx943/manga-repo` tiene 24 estrellas, se describe como el plugin de fuentes para Usagi y **publica una sola extensión**. Keiyoushi publica {num(K['keiyoushi/extensions']['publicadas'])}. La cifra está en el índice; se cuenta o no se escribe.

**4 · ¿Es un clon con otro nombre?** Se ve en su propio `repo.json`: dos repositorios distintos —`cuong-tran/manga-repo` y `mojuru/cursed-manga-repo`— **declaran llamarse «Yūzōnō» y «Cursed Yūzōnō»**, y el primero publica {num(K['cuong-tran/manga-repo']['publicadas'])} extensiones. Indexarlo como «otra tienda» es duplicar la de siempre con otro color. Se nombra como lo que es o no se nombra.

**5 · ¿El repositorio se llama de verdad así, o su nombre es una dirección?** Existen repositorios cuyo nombre completo es `https-raw.githubusercontent.com-keiyoushi-extensions-repo-index.min.json`, uno de ellos con **29 estrellas y cero código**: alguien pegó una URL como nombre de repositorio y un indexador automático lo tomó por una tienda. Es el retrato del problema: **lo que un bot cuenta como recurso, una persona lo ve como basura**.

**6 · ¿Dice el propio autor que no hay soporte, o que no programa?** Es la comprobación más humana de las seis y la que ninguna API hace: leer la descripción. Hay repositorios que declaran ser un APK recompilado por alguien que avisa de que no sabe programar —lo vimos en la pieza 17, con `Batmancpu/Dictator-`—, y hay proyectos que dicen «sin soporte» en la primera línea. **Si el autor lo dice, se cree al autor.**

**Y una séptima, que no es de la ficha sino del uso:** **¿la has abierto tú?** Una extensión que instala, busca y abre un capítulo vale más que veinte que solo están en una lista. La comunidad lo pidió así de claro: *úsala primero, pídela después*.

───────────────────
""")
open('/tmp/lab18/docs/talleres/pieza19/s1.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
