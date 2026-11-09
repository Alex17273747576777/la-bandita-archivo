*DropSauce: el único del tema que firma —tres sumas de cincuenta y cinco archivos— y la casa que dejó*

*La Bandita · domingo 8 de noviembre de 2026, 08:35 de la mañana en Santo Domingo (12:35 UTC) · edición dominicano-español · pieza 27 de Facebook*

⏱️ *Lectura total: 10 minutos · cuatro lectores de cómic y novela medidos hoy uno por uno contra la API pública de GitHub, más uno que ya no existe · 262 archivos publicados y **tres con suma**, los tres del más pequeño · 25.096.104 descargas · cero paquetes alojados aquí*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · un lector nuevo que hace lo que los grandes no
├── ⚡ En una página · las cinco cifras que importan
├── 📋 Las cuatro fichas · una por una
├── 🔏 La huella · 3 de 262, y del pequeño
├── 🧩 Qué es Jetpack Compose y por qué importa aquí
├── 🛠️ Cuatro órdenes y una comprobación de firma
├── 🚪 Lo que esta pieza no tiene · 📅 la semana de prueba
├── ❓ Las preguntas del grupo · 🌅 cierre
└── 🗒️ Notas al pie
```

───────────────────

*🧱 La semilla · un lector nuevo que hace lo que los grandes no*

DropSauce es un lector de cómic y novela escrito en Jetpack Compose, la herramienta moderna de interfaces de Android. Tiene **235 estrellas**, que en este ecosistema es poco más que nada: Mihon tiene veinticinco mil.

Y sin embargo es **el único de los cuatro que publica una suma de comprobación**. Tres sumas, para ser exactos, en una entrega de cincuenta y cinco archivos publicada hace cinco días.

Esta pieza se publicó el 7 de noviembre con cuarenta y ocho mil caracteres de relleno y ninguna medición. Hoy se mide de verdad: **cuatro lectores vivos y uno que devuelve 404**, medidos a las 08:35 contra la API pública de GitHub, con sus 262 archivos y la cuenta de huellas. Y el resultado repite el patrón que ya llevamos visto tres veces esta mañana: la huella no la pone el grande.

───────────────────

*⚡ En una página · las cinco cifras que importan*

**Cuatro repositorios vivos**, más uno que devuelve 404. Juntos: 39.350 estrellas y 25.096.104 descargas.

**Tres de 262 archivos con suma de comprobación.** El **1,1 %**. Y las tres están en el mismo repositorio, el más pequeño del grupo.

**El que más publica no firma nada**: Mihon, con **152 adjuntos** y cero huellas. El que menos publica es el que sí firma: DropSauce, 55 adjuntos y 3 sumas.

**Kotatsu lleva 370 días sin empujón y sin ninguna entrega etiquetada**, igual que en la pieza 26: es el mismo repositorio visto desde otro tema.

**Y el padre no está**: `tachiyomiorg/tachiyomi` devuelve **404**. Ya lo vimos esta mañana midiendo lectores de manga; aquí vuelve a aparecer porque este tema es la misma familia contada desde el cómic.

───────────────────

*📋 Las cuatro fichas · una por una*

**`mihonapp/mihon` — ★25.154 · Apache-2.0 · el grande.**
Entrega `v0.21.3` hace **15 días**; **152 adjuntos** y **ninguna suma**. Último empujón: hace 1 día. Es el lector de referencia y el que más archivos publica.

**`KotatsuApp/Kotatsu` — ★8.958 · GPL-3.0 · el parado.**
**Sin ninguna entrega etiquetada**. Último empujón hace **370 días**. GPL-3.0, código abierto, sin señales de vida.

**`komikku-app/komikku` — ★5.003 · Apache-2.0 · el que publica poco y sigue.**
Entrega `v1.14.1` hace **115 días**; **55 adjuntos**; ninguna suma. Último empujón: hace 2 días.

**`HuzaifaKhalid1311/DropSauce` — ★235 · GPL-3.0 · el pequeño que firma.**
Entrega `v1.1.2` hace **5 días**; **55 adjuntos** y **tres sumas de comprobación**. Último empujón: hace **5 días**. Es el único del tema que te da con qué comprobar.

───────────────────

*🔏 La huella · 3 de 262, y del pequeño*

Doscientos sesenta y dos archivos entre los cuatro. Tres con suma. Los tres de DropSauce.

Vale la pena detenerse en el contraste porque es el mismo de la pieza 25 y el mismo de la pieza 09: **Mihon publica 152 archivos y no da una sola huella; DropSauce publica 55 y da tres**. No es una diferencia de recursos: es una diferencia de costumbre. Publicar una suma cuesta escribir un archivo de texto de dos líneas en la entrega.

Y el usuario lo nota en un momento muy concreto: el día que baja un APK y quiere saber si es el que el autor publicó. Con Mihon, no puede. Con DropSauce, sí: baja el archivo, mira la suma, la compara y sigue.

Lo que la huella **no** dice, y conviene repetirlo como en cada pieza de la serie: no dice si el programa es bueno, ni si respeta tu privacidad, ni si las fuentes que lee son legales en tu país. Dice una sola cosa: **este archivo es el que esa persona publicó**. Y con eso se evita un ataque muy concreto, que es el archivo cambiado en el camino.

───────────────────

*🧩 Qué es Jetpack Compose y por qué importa aquí*

Jetpack Compose es el marco con el que Google escribe hoy las interfaces de Android: describes la pantalla y el sistema la dibuja, en vez de mover elementos a mano. Para un lector de cómics importa por tres razones prácticas:

**Pesa menos y arranca más rápido** que una interfaz vieja, porque no arrastra el sistema de vistas clásico. En un teléfono de gama baja —que es el que usa la mayoría— eso se nota.

**Se adapta mejor a pantallas raras**: tablet, plegable, horizontal. Un lector de cómic en horizontal es casi otra aplicación, y Compose lo lleva mejor.

**Y obliga a mantenerse al día**: cada versión del marco trae cambios, así que un proyecto en Compose tiende a actualizarse por necesidad. Eso explica, en parte, que DropSauce tenga cinco días de vida en su última entrega y Kotatsu trescientos setenta.

Lo que no dice nada de Compose es la calidad del lector: es una herramienta, no un aval. Un lector mal hecho sigue siendo malo con el marco nuevo.

───────────────────

*🛠️ Cuatro órdenes y una comprobación de firma*

**1 · ¿Está vivo y publica?**
```
curl -s https://api.github.com/repos/HuzaifaKhalid1311/DropSauce | grep -E '"pushed_at"|"archived"'
curl -s https://api.github.com/repos/HuzaifaKhalid1311/DropSauce/releases/latest | grep '"tag_name"'
```

**2 · ¿Qué archivos trae la entrega y cuáles con huella?**
```
curl -s https://api.github.com/repos/HuzaifaKhalid1311/DropSauce/releases/latest \
 | grep -o '"name": "[^"]*"' | grep -Ei 'sha|sums|sig|asc|checksum'
```
En DropSauce devuelve tres líneas. En Mihon, ninguna.

**3 · Compara la lista completa de adjuntos:**
```
curl -s https://api.github.com/repos/dueno/repo/releases/latest | grep -c '"browser_download_url"'
```
Ese es el número de archivos que hay que comprobar. Si es 152 y las huellas son 0, ya sabes cuánto trabajo te ahorra no tenerlas.

**4 · Y la comprobación que sí puedes hacer siempre, con o sin huella:**
```
apksigner verify --print-certs app.apk | grep SHA-256
```
Apunta ese SHA-256. Te sirve para dos cosas: saber que el paquete no cambió de llave entre versiones, y tener una huella propia cuando el autor no publique ninguna.

───────────────────

*🚪 Lo que esta pieza no tiene*

No he leído ningún cómic en ninguno de los cuatro. No hay aquí prueba de que las fuentes de DropSauce funcionen hoy, ni de que su interfaz sea mejor o peor que la de los grandes: eso exige usarlo, y esta casa mide repositorios.

No hay capturas de pantalla de un teléfono que no tengo en la mano, ni una recomendación de instalación, ni la cifra de usuarios reales —las descargas son de adjuntos de GitHub—.

Y no hay una comparación de rendimiento entre Compose y las interfaces clásicas. Se dice lo que es y por qué importa; medirlo con números exigiría correr los cuatro en el mismo aparato, y eso no se hizo.

───────────────────

*📅 La semana de prueba*

**Día 1.** Entra en la página de DropSauce y mira sus dos fechas: último empujón y última entrega. Son cinco y cinco días.
**Día 2.** Baja su archivo `.sha256` y el APK de la misma entrega. Calcula el hash con `sha256sum` y compara. Es la primera vez que vas a poder hacerlo en este tema.
**Día 3.** Repite el intento con tu lector actual. Busca una suma y no la vas a encontrar. Ahí tienes la diferencia en la mano.
**Día 4.** Comprueba la firma del paquete de tu lector actual y apunta su SHA-256 en una nota.
**Día 5.** Decide con las dos cosas a la vista: la fecha de la última entrega y si puedes comprobar el archivo. No con las estrellas.

───────────────────

*❓ Las preguntas del grupo*

**¿Entonces DropSauce es el mejor?** No he dicho eso. He dicho que es el único de los cuatro que firma tres archivos y que lleva cinco días de actividad. Lo que no sé —porque no lo probé— es si lee bien.

**¿Por qué Mihon no publica huella con 25.000 estrellas?** Porque nunca le ha hecho falta: nadie se la ha pedido en masa. La huella no aparece por tamaño, aparece por costumbre o por susto.

**¿Qué pasó con Tachiyomi?** La API devuelve 404: el repositorio no existe hoy. El motivo no lo medí.

**¿Kotatsu está muerto?** No está archivado. Lleva 370 días sin empujón. Quieto y muerto no son lo mismo, pero para el usuario se parecen mucho.

**¿Esto estaba en la pieza vieja?** No. La vieja eran cuarenta y ocho mil caracteres de relleno. Esto es la medición: cuatro vivos, uno desaparecido, 262 archivos, tres huellas.

───────────────────

*🌅 Cierre*

Un lector de 235 estrellas, publicado hace cinco días y con tres sumas de comprobación, hace lo que los tres grandes del tema no hacen con veinticinco mil estrellas y 152 archivos. Eso no lo convierte en mejor lector: lo convierte en el único del grupo con el que puedes comprobar lo que bajas.

Y hay una lección de método que vale más que la pieza: cuando se mide, lo pequeño deja de ser invisible. Con las estrellas en la mano, DropSauce no existe. Con la fecha y la huella en la mano, es el único que tiene algo que enseñar.

*La Bandita informa a partir de fuentes fechadas. · domingo 8 de noviembre de 2026 · pieza 27 de Facebook · los cuatro repositorios vivos y el que devuelve 404 se midieron contra la API pública de GitHub a las 12:35 UTC del 8 de noviembre de 2026 y la medición vive en `docs/MEDICION-27-2026-11-08.json`. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
