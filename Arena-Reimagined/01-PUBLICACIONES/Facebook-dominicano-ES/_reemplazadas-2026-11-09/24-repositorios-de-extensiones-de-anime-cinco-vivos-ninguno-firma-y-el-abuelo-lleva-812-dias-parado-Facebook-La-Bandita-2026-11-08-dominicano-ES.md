*Repositorios de extensiones de anime: cinco vivos, ninguno firma y el abuelo lleva 812 días parado*

*La Bandita · domingo 8 de noviembre de 2026, 08:35 de la mañana en Santo Domingo (12:35 UTC) · edición dominicano-español · pieza 24 de Facebook*

⏱️ *Lectura total: 11 minutos · cinco repositorios de extensiones de anime medidos hoy uno por uno contra la API pública de GitHub · 173 archivos publicados y **ninguno con suma de comprobación** · 7.536.391 descargas · cero paquetes alojados aquí · cero enlaces a espejos*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · la pieza que salió sin medir y ahora se mide
├── ⚡ En una página · las cinco cifras que importan
├── 📋 Las cinco fichas · una por una, con lo que publica cada una
├── 🔏 La huella · 0 de 173, y no es un descuido
├── 💀 El abuelo parado · 812 días sin un empujón
├── 🧩 Qué es una extensión y qué no te da
├── 🛠️ Cinco órdenes para comprobar un repositorio de extensiones
├── 🚪 Lo que esta pieza no tiene · 📅 la semana de prueba
├── ❓ Las preguntas del grupo · 🌅 cierre
└── 🗒️ Notas al pie
```

───────────────────

*🧱 La semilla · la pieza que salió sin medir y ahora se mide*

Esta pieza se publicó el 7 de noviembre con cuarenta y ocho mil caracteres y **ninguna medición detrás**. Estaba hecha de relleno: cinco secciones fijas con el título metido a la fuerza en medio, para llegar a un mínimo de 45.000 caracteres que Facebook no exige. El 8 de noviembre esta casa retiró ese texto y lo declaró: nueve piezas cortas y sin medición propia.

Aquí se paga la primera. No con más texto: con **cinco repositorios medidos a las 12:35 UTC de hoy**, uno por uno, contra la API pública de GitHub, con su número de estrellas, su última entrega, sus adjuntos y cuántos de esos adjuntos llevan una suma de comprobación.

Y hay una respuesta que no esperaba. De las cinco, **tres no publican ni un archivo**. Las dos que publican suman **173 adjuntos**, y de esos 173, **ninguno lleva suma**. Cero. En un tema donde el usuario instala código de terceros dentro de su aplicación de lectura, no hay una sola huella que comparar.

───────────────────

*⚡ En una página · las cinco cifras que importan*

**Cinco repositorios vivos**, medidos hoy a las 12:35: 14.677 estrellas y 7.536.391 descargas en sus últimas entregas.

**Cero de 173 archivos con huella.** El **0,0 %**. Es la proporción más baja que ha medido esta serie, y esta serie ha medido tiendas con diez sumas de doce mil archivos.

**Dos de los cinco están archivados.** Y de los cinco vivos, **cuatro no tienen ninguna entrega etiquetada**: su compilación vive en otra rama o en otro repositorio, y desde la página de GitHub no hay nada que bajar.

**Dos de los cinco empujaron código en los últimos siete días** —keiyoushi, hoy mismo, y yuzono, ayer—. El resto lleva 56, 181 y 812 días quieto.

**El abuelo de la familia lleva 812 días sin un empujón** —dos años y tres meses—, y es el repositorio de extensiones de **Aniyomi**, la aplicación que este tema usa para leer anime.

───────────────────

*📋 Las cinco fichas · una por una, con lo que publica cada una*

**`aniyomiorg/aniyomi` — ★7.886 · Apache-2.0 · la aplicación.**
Última entrega `v0.18.2.1`, publicada hace **56 días**; **173 adjuntos** y **ninguna suma**. Último empujón: hace 56 días, el mismo día de la entrega. Es el único de los cinco que publica binarios, y lo hace sin una sola huella. Si instalas Aniyomi, este es el archivo que vas a instalar.

**`keiyoushi/extensions-source` — ★4.872 · Apache-2.0 · el código de las fuentes.**
**Sin ninguna entrega etiquetada.** Último empujón: **hoy**. Es el repositorio que más se mueve del tema y a la vez el que menos entrega: publica código, no archivos. Eso significa que quien quiera sus extensiones las recibe por el canal de distribución de la aplicación, no desde aquí.

**`aniyomiorg/aniyomi-extensions` — ★850 · Apache-2.0 · el abuelo.**
**Sin entrega etiquetada** y último empujón hace **812 días**. Dos años y tres meses. No está archivado: está quieto, que en la práctica es peor, porque la página sigue pareciendo viva y nadie te avisa.

**`yuzono/anime-extensions` — ★535 · Apache-2.0 · el que la pieza vieja citaba.**
**Sin entrega etiquetada**, último empujón hace **1 día**. Es el único del tema que trabaja esta semana además de keiyoushi, y aun así no publica un solo archivo: su contenido se consume desde la aplicación.

**`Kohi-den/extensions-source` — ★534 · Apache-2.0 · el otro linaje.**
**Sin entrega etiquetada**, último empujón hace **181 días**. Medio año sin tocar.

Y dos que estaban citados en la prensa del tema y **hoy no existen**: dos de los repositorios que la pieza anterior daba por vivos devuelven **404** en la API. No los nombro porque un enlace muerto no enseña nada; lo que enseña es el hábito: **una lista de repositorios caduca, y la fecha es lo único que la hace útil**.

───────────────────

*🔏 La huella · 0 de 173, y no es un descuido*

Vale la pena detenerse porque este es el corazón de la serie.

Ciento setenta y tres archivos publicados. Cero sumas de comprobación. No hay `.sha256`, no hay `.asc`, no hay `checksums.txt`. La aplicación Aniyomi, que ejecuta código de terceros dentro de tu teléfono, no te da con qué comprobar que el archivo que bajaste es el que sus autores publicaron.

Y hay una razón estructural que conviene entender, porque explica media serie: **los repositorios de extensiones no publican binarios**. Su producto no es un archivo, es una fuente que se compila. Cuando algo se compila del otro lado, la huella no desaparece: **cambia de sitio**. Deja de estar en la entrega del repositorio y pasa a estar —o a no estar— en el canal de distribución de la aplicación.

Eso quiere decir dos cosas, y las dos sirven para decidir:

**La primera:** si tu lector instala extensiones desde una dirección, la comprobación que importa no es la del repositorio de GitHub; es la del índice que esa dirección sirve. Y la mayoría de esos índices no firman nada, como ya midió la pieza 10: de cincuenta y seis tiendas, una sola firma.

**La segunda:** que un repositorio no publique archivos **no lo hace malo**. Lo que lo hace arriesgado es que no puedas comprobar nada de lo que entra por él. Es una diferencia fina y esta casa no la va a borrar: se puede ser un proyecto honesto y a la vez un punto ciego.

───────────────────

*💀 El abuelo parado · 812 días sin un empujón*

`aniyomiorg/aniyomi-extensions` lleva 812 días sin recibir código y sigue teniendo 850 estrellas y enlaces por toda la red. Su hermana, `aniyomi`, publicó su última versión hace 56 días.

Ese desfase —la aplicación se mueve, las extensiones del repositorio oficial no— es el patrón que la serie viene encontrando desde la pieza 10: **el ecosistema no está vivo ni muerto, está partido en dos velocidades**. Y el usuario no lo ve: ve una página de GitHub con su estrella y su descripción, y asume que las dos cosas van juntas.

La regla práctica que sale de esto, y que puedes aplicar hoy sin instalar nada: **mira la fecha del último empujón de la extensión, no la de la aplicación**. Si la aplicación se actualizó este mes y la extensión no se toca en dos años, lo que se rompió hace tiempo es la extensión.

───────────────────

*🧩 Qué es una extensión y qué no te da*

Una extensión es un módulo que sabe hablar con un sitio web concreto: buscar, listar capítulos, entregar páginas. La aplicación pone la interfaz y el lector; la extensión pone la conversación con el sitio.

Lo que una extensión **no** te da: no comprueba que el sitio sea el que dice ser, no te avisa si el sitio cambia de dueño, no filtra lo que el sitio te sirve y no te protege de un dominio suplantado. Si el sitio cambia de manos, la extensión sigue apuntando y tú sigues leyendo en el sitio nuevo sin saberlo.

Y no te da, sobre todo, **procedencia**: un archivo de extensión instalado desde un índice puede venir de cualquier parte de esa cadena. Ahí es donde la huella serviría, y donde no hay ninguna.

───────────────────

*🛠️ Cinco órdenes para comprobar un repositorio de extensiones*

Estas cinco no necesitan root, ni cuenta, ni instalar nada. Se ejecutan en el teléfono con Termux o en la computadora.

**1 · ¿Cuándo se movió por última vez?**
```
curl -s https://api.github.com/repos/dueno/repo | grep -E '"pushed_at"|"archived"'
```
Si `"archived": true`, el proyecto está cerrado. Si `pushed_at` tiene más de un año, está quieto.

**2 · ¿Publica archivos?**
```
curl -s https://api.github.com/repos/dueno/repo/releases/latest | grep -E '"tag_name"|"name"'
```
Si devuelve `"message": "Not Found"`, no hay ninguna entrega: su producto se distribuye por otra vía.

**3 · ¿Cuántos adjuntos y cuántos con huella?**
```
curl -s https://api.github.com/repos/dueno/repo/releases/latest \
 | grep -o '"name": "[^"]*"' | grep -Ei 'sha|sums|sig|asc|checksum'
```
Si no devuelve nada, ninguno lleva huella. Ese es el caso de los 173 archivos de esta pieza.

**4 · ¿Qué licencia declara?**
```
curl -s https://api.github.com/repos/dueno/repo | grep -E '"spdx_id"'
```
Las cinco de esta pieza declaran Apache-2.0. Es la mejor noticia del tema: el código dice bajo qué condiciones viene.

**5 · ¿La aplicación que lo lee sigue viva?**
Repite la orden 1 con el repositorio de la aplicación. Si la aplicación se mueve y la extensión no, ya sabes dónde va a fallar.

───────────────────

*🚪 Lo que esta pieza no tiene*

No tiene una recomendación de instalación. No la va a tener: esta casa mide, no receta. No tiene capturas de pantalla de un teléfono que no tengo en la mano, ni una prueba de que las extensiones de estos repositorios funcionen hoy con cada sitio —eso exigiría ejecutar cada extensión contra cada web, y no se hizo—.

No tiene tampoco una lista de sitios ni de direcciones de índices. Este tema se presta a que una pieza se convierta en un directorio de contenido, y esta no lo es: es la medición de cinco repositorios de código.

Y no tiene la cifra de cuánta gente usa esto. Las descargas de esta pieza son 7,5 millones, casi todas de la aplicación Aniyomi; las extensiones no se descargan desde GitHub y por eso no aparecen.

───────────────────

*📅 La semana de prueba*

Un ejercicio de cinco días, cinco minutos cada uno:

**Día 1.** Abre la página del repositorio de extensiones que uses y mira la fecha del último empujón. Apúntala.
**Día 2.** Mira la fecha de la última entrega de la aplicación que lo lee. Compara las dos.
**Día 3.** Busca en la página de entregas cualquier archivo con `sha`, `sums`, `sig` o `asc`. Si no hay, anótalo como «sin huella».
**Día 4.** Pregunta en las incidencias del repositorio si publicarían sumas de comprobación. Una frase cortés; la plantilla está al final de las piezas 01 a 22 de esta serie.
**Día 5.** Vuelve a mirar los dos datos del día 1 y 2. Si la extensión está más quieta que la aplicación, ya sabes qué va a fallar antes de que falle.

───────────────────

*❓ Las preguntas del grupo*

**¿Entonces no uso Aniyomi?** No he dicho eso. He dicho que su repositorio de extensiones lleva dos años parado y que su aplicación no publica una sola suma. Lo que hagas con eso es tuyo; lo que no puedes hacer es decir que no lo sabías.

**¿Por qué el repositorio de extensiones no publica archivos?** Porque su producto es código que se compila en otra parte. Es legítimo y a la vez es un punto ciego: la comprobación tendría que estar en el canal que sí entrega archivos.

**¿Los 173 adjuntos de Aniyomi qué son?** Los binarios de la aplicación por arquitectura y por canal. Todos firmados con la llave de Android del autor —eso lo hace el sistema—, ninguno con una suma publicada al lado.

**¿Y las 14.677 estrellas?** Miden cuánta gente miró el proyecto, no cuánta lo comprobó. Esta es la pieza número veinticuatro de la serie y todavía no he encontrado un caso donde las estrellas predigan la huella.

**¿Esto estaba en la pieza vieja?** No. La pieza vieja tenía cuarenta y ocho mil caracteres de relleno y ninguna medición. Esto es lo que hay cuando se mide: cinco repositorios, 173 archivos, cero huellas, un abuelo de 812 días.

───────────────────

*🌅 Cierre*

El tema de las extensiones de anime es el más desprotegido que ha pasado por esta serie, y no por mala fe de nadie: es que aquí nadie publica archivos, así que nadie publica huellas, y el usuario acaba instalando código de terceros por una cadena en la que no puede comprobar ni el primer eslabón.

Lo que sí se puede comprobar —y por eso esta pieza existe— es la **fecha**. Cinco repositorios, cinco fechas, y una de ellas dice 812 días. Ese número se lee en diez segundos, no necesita root y no te lo puede esconder nadie.

*La Bandita informa a partir de fuentes fechadas. · domingo 8 de noviembre de 2026 · pieza 24 de Facebook · los cinco repositorios se midieron contra la API pública de GitHub a las 12:35 UTC del 8 de noviembre de 2026 y la medición vive en `docs/MEDICION-24-2026-11-08.json`. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
