*LNReader y sus plugins: cinco sumas de sesenta y nueve archivos, y un repositorio de plugins sin una sola entrega*

*La Bandita · domingo 8 de noviembre de 2026, 08:35 de la mañana en Santo Domingo (12:35 UTC) · edición dominicano-español · pieza 29 de Facebook*

⏱️ *Lectura total: 10 minutos · dos repositorios medidos hoy uno por uno contra la API pública de GitHub · 69 archivos publicados y **cinco con suma** · 1.018.260 descargas · el repositorio de plugins lleva 963 días sin entrega etiquetada · cero paquetes alojados aquí*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · la aplicación firma, los plugins no publican
├── ⚡ En una página · las cuatro cifras que importan
├── 📋 Las dos fichas · una por una
├── 🔏 La huella · 5 de 69, y en el sitio correcto
├── 💀 Los 963 días del repositorio de plugins
├── 🧩 Aplicación y plugins: quién ejecuta qué
├── 🛠️ Tres órdenes y una comprobación que sí funciona
├── 🚪 Lo que esta pieza no tiene · 📅 la semana de prueba
├── ❓ Las preguntas del grupo · 🌅 cierre
└── 🗒️ Notas al pie
```

───────────────────

*🧱 La semilla · la aplicación firma, los plugins no publican*

LNReader es un lector de novelas ligeras para Android, escrito en React Native, con **2.967 estrellas**. Sus plugins —los módulos que saben hablar con cada sitio de novelas— viven en otro repositorio, `LNReader/lnreader-plugins`, con **370**.

De los nueve temas que esta casa midió hoy, este es el único con una noticia buena de verdad: **la aplicación publica cinco sumas de comprobación**. Cinco, en una entrega de 69 archivos. No es el 100 %, pero es cinco veces más de lo que publican los otros ocho temas juntos.

Y la otra cara es la de siempre: el repositorio de plugins **no tiene ninguna entrega etiquetada desde hace 963 días** —dos años y siete meses— aunque su código se empuja a diario.

Esta pieza salió el 7 de noviembre con cuarenta y ocho mil caracteres de relleno y sin medición. Hoy se mide: **dos repositorios a las 12:35 UTC**, con sus 69 archivos, sus 1.018.260 descargas y la cuenta de huellas.

───────────────────

*⚡ En una página · las cuatro cifras que importan*

**Dos repositorios vivos**, ninguno archivado: 3.337 estrellas y 1.018.260 descargas.

**Cinco de 69 archivos con suma de comprobación.** El **7,2 %** — y las cinco están en la **aplicación**, no en los plugins.

**El repositorio de plugins no publica ni un archivo**: cero entregas etiquetadas, cero adjuntos, 963 días desde la última etiqueta.

**La aplicación se movió hace 8 días y los plugins hace 1**: los dos están vivos, solo que los plugins no empaquetan. Es la misma estructura que la pieza 28 y, por primera vez en la serie, con huella en una de las dos mitades.

───────────────────

*📋 Las dos fichas · una por una*

**`LNReader/lnreader` — ★2.967 · MIT · la aplicación.**
Entrega `v2.1.4` hace **44 días**; **69 adjuntos** y **cinco sumas de comprobación**. Último empujón: hace **8 días**. Es el único de los nueve temas medidos hoy que firma parte de lo que publica.

**`LNReader/lnreader-plugins` — ★370 · MIT · los plugins.**
**Sin ninguna entrega etiquetada**; la última etiqueta (`v2.0.0`) es de hace **963 días** y no trae adjuntos. Último empujón: hace **1 día**. Código vivo, empaquetado inexistente.

───────────────────

*🔏 La huella · 5 de 69, y en el sitio correcto*

Cinco sumas para sesenta y nueve archivos. Parece poco y, comparado con la serie, es mucho: en la pieza 24 eran cero de 173; en la 26, cero de 727; en la 28, cero de 3.788. Aquí hay cinco.

Y hay un detalle que las hace valiosas: **están en la aplicación**, es decir, en los archivos que el usuario instala y ejecuta con todos los permisos. La huella importa más donde el archivo tiene más poder, y LNReader ha puesto las suyas justo ahí.

Lo que no hay es huella en los plugins, y eso deja la mitad del problema sin resolver: la aplicación te dice que el archivo es el que publicaron, pero los módulos que ejecuta dentro —los que hablan con los sitios— no llevan ninguna. Es una mejora real y a la vez una mejora a medias, y conviene decirlo con las dos partes.

───────────────────

*💀 Los 963 días del repositorio de plugins*

La última etiqueta del repositorio de plugins es `v2.0.0`, de hace **963 días**, y no trae ni un adjunto. Desde entonces, el repositorio ha seguido recibiendo código —el último empujón es de **ayer**— sin publicar una sola versión.

Eso significa una cosa concreta: **los plugins no se instalan desde GitHub**. La aplicación los recibe por su propio mecanismo, y la versión que ejecuta no se corresponde con ninguna etiqueta del repositorio. En la práctica, el usuario está usando código del día sin que exista una versión con número que pueda citar.

Y eso tiene una consecuencia incómoda: si mañana un plugin se porta mal, no hay una versión publicada contra la que compararlo. Hay un flujo de código y una fecha. Para auditar, es más difícil que un paquete con nombre y número; para mantener, es más rápido. Es el intercambio que hace medio ecosistema, y esta pieza solo lo describe.

───────────────────

*🧩 Aplicación y plugins: quién ejecuta qué*

En LNReader, como en Mangayomi y en los lectores del ecosistema Mihon, la separación es esta:

**La aplicación** pone la interfaz, el lector, la biblioteca, el historial y los permisos. Es lo que instalas desde GitHub, con nombre, versión y —aquí— cinco sumas.

**Los plugins** son módulos que saben hablar con un sitio concreto: buscar, listar capítulos, entregar el texto. Los ejecuta la aplicación, pero el código viene de fuera.

**Lo que ve el usuario** es una sola aplicación. **Lo que hay en el teléfono** son dos capas: la que se instaló una vez y la que se actualiza por detrás.

Ahí está la razón por la que la huella en la aplicación, sola, no basta: comprueba la capa estable y deja sin comprobar la capa que cambia. Es como revisar la cerradura y dejar la ventana abierta, con el agravante de que la ventana se abre sola cada vez que el índice se actualiza.

───────────────────

*🛠️ Tres órdenes y una comprobación que sí funciona*

**1 · ¿La aplicación publica huella?**
```
curl -s https://api.github.com/repos/LNReader/lnreader/releases/latest \
 | grep -o '"name": "[^"]*"' | grep -Ei 'sha|sums|sig|asc|checksum'
```
Aquí devuelve cinco líneas. Y son cinco de sesenta y nueve, así que sirven para cinco archivos: comprueba con la orden siguiente.

**2 · Baja la suma y compruébala:**
```
curl -LO <dirección del archivo .sha256 que aparece en la lista>
sha256sum -c archivo.sha256
```
Si dice `OK`, el archivo es el que publicaron. Si dice `FAILED`, bórralo.

**3 · ¿Los plugins publican algo?**
```
curl -s https://api.github.com/repos/LNReader/lnreader-plugins/releases/latest | grep '"tag_name"'
```
Si la fecha es vieja y los adjuntos son cero —como aquí—, los plugins no tienen versión publicada.

**Y la comprobación que sí funciona siempre, con o sin huella** —la firma del paquete:
```
apksigner verify --print-certs lnreader.apk | grep SHA-256
```
Apunta ese SHA-256. Entre dos versiones de la misma aplicación debe ser **el mismo**; si cambia, cambió la llave y eso siempre hay que explicarlo.

───────────────────

*🚪 Lo que esta pieza no tiene*

No he leído ninguna novela en LNReader ni he probado ninguno de sus plugins contra ningún sitio. No hay aquí una medición de qué fuentes funcionan hoy: eso exige abrir la aplicación y probar, y no se hizo.

No hay capturas de pantalla de un teléfono que no tengo en la mano ni una recomendación de instalación. Tampoco hay un recuento de cuántos plugins existen: el repositorio no publica un índice con número de archivos, y contar carpetas en la API habría sido una medición a medias que prefiero no dar.

Y no hay cifra de usuarios reales: las 1.018.260 descargas son de los adjuntos de GitHub, y quien instala por otra vía no aparece.

───────────────────

*📅 La semana de prueba*

**Día 1.** Mira la entrega de LNReader en GitHub y localiza sus cinco archivos de suma. Baja uno y compruébalo con `sha256sum -c`. Es un minuto.
**Día 2.** Mira la fecha de la última etiqueta de sus plugins. Son 963 días, y no trae archivos.
**Día 3.** Entra en el menú de plugins de la aplicación y cuenta cuántos tienes activos.
**Día 4.** Quita los que no uses. Menos plugins, menos código de terceros ejecutándose.
**Día 5.** Comprueba la firma del paquete de la aplicación y apunta el SHA-256 de su certificado. Es tu huella mínima, la publishes quien la publishes.

───────────────────

*❓ Las preguntas del grupo*

**¿Cinco sumas son suficientes?** No: son cinco de sesenta y nueve archivos. Pero es la primera pieza de este bloque con alguna, y la serie no va a dejar de anotar la mejora solo porque sea parcial.

**¿Por qué los plugins no tienen versión?** Porque se distribuyen por el mecanismo interno de la aplicación, no por entregas de GitHub. La etiqueta `v2.0.0` es de hace 963 días y no trae archivos.

**¿Entonces no puedo comprobar los plugins?** No con una suma publicada. Lo que sí puedes es mirar cuándo se movió el repositorio y cuántos plugins tienes activos. Es menos de lo que quisiéramos y es todo lo que hay.

**¿MIT es buena licencia aquí?** Es permisiva: permite usar, copiar y modificar citando el aviso. Los dos repositorios la declaran, y eso es más de lo que hacen otros cinco repositorios medidos esta mañana.

**¿Esto estaba en la pieza vieja?** No. La vieja eran cuarenta y ocho mil caracteres de relleno. Esto es la medición: dos repositorios, 69 archivos, cinco sumas, 963 días sin etiqueta en los plugins.

───────────────────

*🌅 Cierre*

Cinco sumas no cambian un ecosistema, pero cambian la conversación: por primera vez en nueve temas medidos hoy hay algo que comprobar, y está donde debe estar —en la aplicación que se instala con permisos—. Que falte en los plugins es la mitad del cuadro, y esta casa no la va a tapar con la otra mitad.

Los 963 días sin etiqueta en el repositorio de plugins son el otro dato que vale llevarse: **código que se mueve todos los días y no se empaqueta nunca**. Para el usuario eso significa que su lector de novelas ejecuta código del día, sin número de versión, y que la única fecha que puede consultar es la del último empujón.

*La Bandita informa a partir de fuentes fechadas. · domingo 8 de noviembre de 2026 · pieza 29 de Facebook · los dos repositorios se midieron contra la API pública de GitHub a las 12:35 UTC del 8 de noviembre de 2026 y la medición vive en `docs/MEDICION-29-2026-11-08.json`. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
