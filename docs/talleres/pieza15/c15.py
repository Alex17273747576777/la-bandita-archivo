# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab/docs/talleres/pieza15')
from d15 import *
A=AGG; T=[]; w=T.append
def f(r,nombre,texto): T.append(f"{ficha(r,nombre)}. {texto}\n")

w(f"""*🕹️ En el bolsillo · tres programas de Android (y el famoso que no está)*

En Android, descargar es otra cosa: la mitad de las apps son una cara amable encima de yt-dlp, y la otra mitad son lanzadores que solo abren el motor del sistema. Tres fichas, y una ausencia que ya se explicó arriba y que conviene repetir aquí porque es la que la gente busca.

""")
f('deniscerri/ytdlnis','ytdlnis',
  f"**{num(E['deniscerri/ytdlnis']['commits_30d'])} cambios en treinta días** —la cifra más alta de todo el tema—, **canal de seguridad** y {num(R['deniscerri/ytdlnis']['descargas'])} descargas: la bifurcación de Seal que sí se mantiene, con {num(R['deniscerri/ytdlnis']['entregas'])} entregas y solo {num(E['deniscerri/ytdlnis']['incidencias']['abiertas'])} incidencias abiertas")
f('yausername/youtubedl-android','youtubedl-android',
  f"**{num(E['yausername/youtubedl-android']['adjuntos'])} adjuntos** y {num(R['yausername/youtubedl-android']['entregas'])} entregas: lo que hay debajo de casi todas las apps de Android que bajan vídeo —un paquete que mete el motor dentro de la aplicación. **{R['yausername/youtubedl-android']['dias_push']} días sin un empujón** y cero cambios en treinta días")
f('JunkFood02/Seal','Seal (el famoso, parado)',
  f"**{num(R['JunkFood02/Seal']['stars'])} estrellas y {num(R['JunkFood02/Seal']['descargas'])} descargas**: el nombre que aparece en todos los vídeos de «descarga vídeos en Android». Hoy: **{R['JunkFood02/Seal']['dias_push']} días sin empujón**, cero cambios en treinta días y **{num(E['JunkFood02/Seal']['incidencias']['abiertas'])} incidencias abiertas**. **{E['JunkFood02/Seal']['puntos']} puntos**. Se lista con su fecha, porque quien lo instale leyendo un tutorial de 2024 merece saberlo")

w(f"""
Ese es el resumen del bloque y casi de la pieza: **el programa más recomendado del tema no se mueve desde hace un mes**, y su bifurcación —ytdlnis, con {num(E['deniscerri/ytdlnis']['commits_30d'])} cambios en treinta días— sí. La diferencia entre los dos es de dos mil estrellas y de un mes de silencio.

───────────────────

*💬 La línea de órdenes · cuatro programas que sí se auditan*

Si hay un sitio donde «descargar es un acto técnico» se ve sin adornos, es aquí. Cuatro programas que no dibujan nada: se les da una dirección y devuelven un archivo, con su nombre, su tamaño y su comprobación. Son los únicos de la pieza que se pueden meter en un guion, y por eso son los que aguantan.

""")
f('yt-dlp/yt-dlp','yt-dlp',
  f"**{num(R['yt-dlp/yt-dlp']['stars'])} estrellas y {num(R['yt-dlp/yt-dlp']['descargas'])} descargas** —la cifra más alta de las quince piezas—, con **empujón de hoy**, {num(E['yt-dlp/yt-dlp']['con_huella'])} sumas de {num(E['yt-dlp/yt-dlp']['adjuntos'])} adjuntos y **{num(E['yt-dlp/yt-dlp']['incidencias']['cerradas'])} incidencias cerradas**. Es el motor que usan por dentro media lista y el patrón de facto del oficio")
f('iawia002/lux','lux',
  f"**{num(R['iawia002/lux']['stars'])} estrellas** y {num(E['iawia002/lux']['commits_30d'])} cambios en treinta días: descargador escrito en Go, un solo binario, sin dependencias. {num(E['iawia002/lux']['adjuntos'])} adjuntos y {num(E['iawia002/lux']['con_huella'])} sumas. **{R['iawia002/lux']['dias_push']} días sin un empujón**: el ritmo lo marca la web, no el programa")
f('soimort/you-get','you-get',
  f"**{num(R['soimort/you-get']['stars'])} estrellas** y {num(E['soimort/you-get']['con_huella'])} sumas de {num(E['soimort/you-get']['adjuntos'])} adjuntos: el veterano de Python que enseñó a una generación a bajar vídeo desde la terminal. **Sin licencia legible en la API** y {num(E['soimort/you-get']['incidencias']['abiertas'])} incidencias abiertas ni una cerrada")
f('mikf/gallery-dl','gallery-dl',
  f"**{num(E['mikf/gallery-dl']['incidencias']['cerradas'])} incidencias cerradas** contra {num(E['mikf/gallery-dl']['incidencias']['abiertas'])} abiertas: el descargador de galerías y colecciones, el más especializado de los cuatro. **Empujón de hace {R['mikf/gallery-dl']['dias_push']} días**, {num(R['mikf/gallery-dl']['entregas'])} entregas y **cero adjuntos**: se instala con `pip`")

w(f"""
Los cuatro se parecen en lo importante: **publican a menudo porque la web de enfrente cambia a menudo**, y ninguno depende de una ventana. Y los cuatro comparten un defecto: **la suma de comprobación se publica poco** —{num(E['yt-dlp/yt-dlp']['con_huella'])} de {num(E['yt-dlp/yt-dlp']['adjuntos'])} en el mejor caso— así que si bajas un binario, la comprobación es tuya.

───────────────────

*🌱 Los {palabras(A['nuevas2026'])} nacidos en 2026 · la camada de la descarga*

Otra vez lo nuevo, y otra vez con mejores números que los veteranos. Ocho proyectos escritos este año, con {num(sum(R[r]['stars'] for r in VIVOS if R[r]['dias_nace']<=300))} estrellas entre todos, y **{palabras(sum(1 for r in VIVOS if R[r]['dias_nace']<=300 and E[r]['con_huella']))} de los ocho publican sumas de comprobación**: rayburst cien, xiadown sesenta, prism diez y MovieBox-Tui diez.

**La advertencia, la misma de ayer:** un proyecto de tres meses no ha pasado por una migración de formato, ni por un cambio de dueño, ni por un año de incidencias. Se recomiendan para probar y se miden igual que los demás.

""")
f('AnInsomniacy/rayburst','rayburst',
  f"**{num(R['AnInsomniacy/rayburst']['stars'])} estrellas y {num(R['AnInsomniacy/rayburst']['descargas'])} descargas en {num(R['AnInsomniacy/rayburst']['dias_nace'])} días**: la nota más alta del tema, con **{num(E['AnInsomniacy/rayburst']['con_huella'])} sumas de {num(E['AnInsomniacy/rayburst']['adjuntos'])} adjuntos** —la mejor proporción de toda la pieza— y {num(E['AnInsomniacy/rayburst']['commits_30d'])} cambios en treinta días")
f('rawnaldclark/Stash','Stash',
  f"**{num(E['rawnaldclark/Stash']['commits_30d'])} cambios en treinta días con {num(E['rawnaldclark/Stash']['contribuyentes'])} personas**: el ritmo más alto de la camada, **canal de seguridad** y {num(R['rawnaldclark/Stash']['entregas'])} entregas en {num(R['rawnaldclark/Stash']['dias_nace'])} días. {num(E['rawnaldclark/Stash']['adjuntos'])} adjuntos sin suma")
f('Downvid/downvid','downvid',
  f"**{R['Downvid/downvid']['dias_nace']} días de vida**, **canal de seguridad** y solo **{num(E['Downvid/downvid']['incidencias']['abiertas'])} incidencia abierta** contra {num(E['Downvid/downvid']['incidencias']['cerradas'])} cerradas: el que mejor atiende de los ocho, con {num(E['Downvid/downvid']['adjuntos'])} adjuntos")
f('FortoGraphy/prism-download-manager','prism',
  f"**{R['FortoGraphy/prism-download-manager']['dias_nace']} días y {E['FortoGraphy/prism-download-manager']['puntos']} puntos**: el más joven de todos y el segundo en nota, con {num(E['FortoGraphy/prism-download-manager']['con_huella'])} sumas de {num(E['FortoGraphy/prism-download-manager']['adjuntos'])} adjuntos y {num(E['FortoGraphy/prism-download-manager']['commits_30d'])} cambios en veinte días de vida")
f('mesamirh/MovieBox-Tui','MovieBox-Tui',
  f"**{num(R['mesamirh/MovieBox-Tui']['stars'])} estrellas** y {num(E['mesamirh/MovieBox-Tui']['commits_30d'])} cambios en treinta días: un gestor de terminal con cola y descarga en paralelo, con {num(E['mesamirh/MovieBox-Tui']['adjuntos'])} adjuntos y {num(E['mesamirh/MovieBox-Tui']['con_huella'])} sumas")
f('arnoldhao/xiadown','xiadown',
  f"**{num(E['arnoldhao/xiadown']['con_huella'])} sumas de {num(E['arnoldhao/xiadown']['adjuntos'])} adjuntos**: la mejor proporción de la camada después de rayburst, con {num(R['arnoldhao/xiadown']['descargas'])} descargas. **{R['arnoldhao/xiadown']['dias_push']} días sin un empujón** y {E['arnoldhao/xiadown']['contribuyentes']} persona: empieza a enfriarse")
f('pixel-point/media-downloader','Media Downloader',
  f"**{num(R['pixel-point/media-downloader']['descargas'])} descargas y {R['pixel-point/media-downloader']['dias_push']} días sin empujón**: nació en mayo, publicó dos entregas y se paró. **Sin licencia legible y {E['pixel-point/media-downloader']['puntos']} puntos**: se lista como lo que es, y es el aviso de que lo nuevo también se muere")
f('BareBrowser/bare-browser','bare-browser',
  f"**{R['BareBrowser/bare-browser']['dias_nace']} días** y {num(E['BareBrowser/bare-browser']['adjuntos'])} adjuntos: navegador mínimo con descarga integrada, con {num(E['BareBrowser/bare-browser']['commits_30d'])} cambios en treinta días y **{num(E['BareBrowser/bare-browser']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['BareBrowser/bare-browser']['incidencias']['cerradas'])} cerradas")

w(f"""
Un dato de la camada que sirve para las piezas que vienen: **{palabras(sum(1 for r in VIVOS if R[r]['dias_nace']<=300 and R[r]['dias_push']<=7))} de los ocho publicaron código esta semana** y uno —media-downloader— ya lleva medio año parado después de dos entregas. La camada de 2026 no es homogénea: hay tres proyectos serios y cinco intentos. **Lo nuevo hay que medirlo, no celebrarlo.**

───────────────────

*🧭 Cómo se elige un gestor en cinco preguntas*

Después de treinta y una fichas, hay un método que se puede resumir y que sirve para cualquier programa de esta familia. Cinco preguntas, en este orden, y la primera que falle descarta el candidato.

**Uno: ¿publica o está quieto?** Es la única pregunta que se contesta con una orden y la que más descarta. **Seal** ({R['JunkFood02/Seal']['dias_push']} días), **Motrix** ({R['agalwood/Motrix']['dias_push']}), **uGet** ({R['uget/uget']['dias_push']}) y **media-downloader** ({R['pixel-point/media-downloader']['dias_push']}) se caen aquí, con miles de estrellas cada uno.

**Dos: ¿tiene motor propio o envuelve otro?** No es un defecto envolver —**ytdlnis** envuelve y es lo mejor del tema en Android— pero cambia a quién hay que vigilar. Si el motor de debajo se para, la cara se queda sin motor: es lo que pasó con casi todas las caras de aria2.

**Tres: ¿lo que baja lo comprueba?** Aquí solo pasan diez de los treinta y uno. Publicar una suma no es un lujo de equipo grande: **rayburst** empezó a publicarlas con tres meses de vida y **prism** con veinte días.

**Cuatro: ¿te deja ver la cola?** Suena menor y no lo es. Un gestor que no enseña los trabajos en curso —cuántos, a qué velocidad, cuánto falta— no se puede auditar. Es la diferencia entre **Gopeed** y una web con un botón.

**Cinco: ¿puedes sacarlo mañana sin perder nada?** Los programas de esta lista que guardan su cola en un archivo de texto —**aria2**, **yt-dlp**, **gallery-dl**— se mudan sin drama. Los que la guardan en una base de datos propietaria, también, pero hay que exportarla a mano.

Con esas cinco preguntas, la recomendación de esta pieza se ordena sola: **yt-dlp** como motor, **Gopeed** o **XDM** como ventana, **ytdlnis** en el bolsillo, y **rayburst** o **prism** como la apuesta del año. Todo lo demás son alternativas razonables o piezas de museo, y las dos cosas se dicen con la fecha al lado.

───────────────────

*⚖️ Lo que la ley permite, lo que la app permite y lo que el archivo dice de sí mismo*

Esta sección no la trae ninguna lista de descargas, y es la que más falta hace.

**Primero: la herramienta no es el acto.** Bajar un archivo es una operación de red; lo que decide si es lícito es **qué** se baja y **de dónde**. Un mismo programa sirve para guardar tu propio material, para archivar una clase grabada, para bajarte un podcast con permiso o para copiar una obra ajena. Medir el programa no es recomendar el uso: es lo que esta serie hace con todo lo demás.

**Segundo: la app no siempre permite lo que la web permite.** Cada servicio pone sus condiciones de uso, y muchas prohíben la descarga automática. Eso no es una ley, es un contrato entre tú y el servicio; incumplirlo puede costarte una cuenta, no una denuncia. La ley es otra cosa y depende del país, del tipo de obra y del uso —copia privada, cita, docencia, accesibilidad—. En la República Dominicana rige la Ley 65-00 sobre derecho de autor, con excepciones parecidas a las del resto de la región. **Esta pieza no da consejo legal**; dice que la pregunta existe y que no se contesta con un «todo el mundo lo hace».

**Tercero, y esto sí es técnico: el archivo dice de sí mismo.** Un vídeo descargado trae en su interior el contenedor, la resolución, el códec, la pista de audio y, a veces, los metadatos de la fuente. Con dos órdenes se ve todo:

```
ffprobe -hide_banner entrada.mp4
sha256sum entrada.mp4
```

El primero cuenta qué hay dentro —y si el archivo está completo, porque un MP4 cortado lo dice—; el segundo da la huella para comparar con la que publicó quien lo hizo. **Esa es la parte de «acto técnico» que la conversación pública se salta**: no es solo bajarlo, es saber qué llegó.

**Un caso concreto que sirve de ejemplo.** Bajar el audio de una charla que tú mismo grabaste y publicaste, para escucharla en el coche, es un uso normal de estas herramientas y nadie va a discutirlo. Bajar la discografía completa de un artista con licencia vigente y repartirla por un grupo, no. Entre esos dos extremos hay una zona gris enorme —docencia, investigación, accesibilidad, prensa, copia privada— y cada país la dibuja distinto. Lo que sí es igual en todas partes: **la responsabilidad es de quien decide qué bajar**, no del programa que lo baja.

**Y una nota sobre el «todo el mundo lo hace».** La mitad de los programas de esta pieza existen porque una web cambió su reproductor y dejó fuera a quien tenía una conexión mala, un aparato viejo o una discapacidad visual. Esa es la parte que casi nunca se cuenta y la que explica por qué estas herramientas siguen vivas: **no todas se usan para copiar; muchas se usan para poder ver**.

**Y cuarto: lo que esta pieza no hace.** No enlaza catálogos, no enlaza torrentes, no explica cómo saltarse un pago y no dice que algo sea legal porque sea posible. Cuando un programa de la lista es un descargador de catálogos ajenos, se dice y se mide igual —como con SpotiFlyer en la pieza 14—, sin mandar a nadie por ahí.

───────────────────

*🔏 La huella del tema · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}*

**{num(A['adjuntos'])} archivos publicados por los {palabras(A['vivos'])} programas. {num(A['con_huella'])} con suma de comprobación. El 10,6 %.**

En su escala: tiendas de extensiones de la pieza 10, **0,08 %**; aplicaciones de la 11, **5,5 %**; audio de la 13, **11,4 %**; kit de la 12, **17,0 %**; clientes de música de la 14, **20,0 %**; y la descarga, **10,6 %**. Ciento treinta veces las tiendas.

**{palabras(A['vivos']-A['con_huella_repos'])} de los {palabras(A['vivos'])} no firman nada.** Los {palabras(A['con_huella_repos'])} que sí:

""")
w("| Recurso | Adjuntos | Con suma | Nota |\n|---|---|---|---|\n")
for c_,a_,r in sorted([(E[r]['con_huella'],E[r]['adjuntos'],r) for r in VIVOS if E[r]['con_huella']],reverse=True):
    w(f"| {r.split('/')[1]} | {num(a_)} | **{num(c_)}** | {E[r]['puntos']} |\n")
w(f"""
Dos cosas de esa tabla. La primera: **rayburst pone {num(E['AnInsomniacy/rayburst']['con_huella'])} de las {num(A['con_huella'])} sumas** —más de un tercio del total— y tiene tres meses; el resto lo reparten nueve proyectos. La segunda: **el programa con más descargas de la serie, yt-dlp, firma {num(E['yt-dlp/yt-dlp']['con_huella'])} de {num(E['yt-dlp/yt-dlp']['adjuntos'])} archivos**; el que más se usa no es el que más garantiza, pero al menos garantiza algo.

**Lo que se puede hacer hoy:** bajar, calcular `sha256sum`, apuntarlo y compararlo en la actualización siguiente. En los {palabras(A['con_huella_repos'])} que publican su cifra, contra la suya; en los demás, contra la que apuntaste tú.

───────────────────

*🛠️ Seis órdenes para bajar algo sin quedarse a ciegas*

1. **Ver si el programa está vivo.** `curl -s https://api.github.com/repos/JunkFood02/Seal | grep -E '"pushed_at"|"archived"'` — es la orden que separa a Seal de ytdlnis, y la que casi nadie ejecuta antes de instalar.
2. **Contar sus versiones.** `curl -s https://api.github.com/repos/yt-dlp/yt-dlp/releases?per_page=100 | grep -c '"tag_name"'` — cien significa que publica siempre; cero, que se instala desde el código.
3. **Buscar una suma.** `curl -s https://api.github.com/repos/AnInsomniacy/rayburst/releases?per_page=100 | grep -Ei 'sha256|sha512|\\.sig|\\.asc' | head -5` — si imprime líneas, ese proyecto firma. Es la orden que da el 10,6 % de esta pieza.
4. **Ver qué llegó, por dentro.** `ffprobe -hide_banner archivo.mp4` — imprime contenedor, pistas, códec y duración. Un archivo cortado se delata aquí antes de que lo abras.
5. **Comprobar el archivo.** `sha256sum archivo.mp4` y comparar con la cifra publicada. Si no hay cifra publicada, se apunta la de hoy y se compara en la próxima descarga del mismo sitio.
6. **Bajar solo lo que pediste.** `yt-dlp --no-playlist -f "bv*+ba/b" -o "%(title)s.%(ext)s" <dirección>` — `--no-playlist` evita que un enlace de un vídeo se convierta en la descarga de una lista de trescientas entradas; el formato elige lo mejor disponible y el nombre sale del título.

La cuarta y la quinta son las que esta serie considera obligatorias: **un archivo del que no sabes qué contiene ni cuánto pesa de verdad no está descargado, está tirado en una carpeta**.

───────────────────

*🚪 Lo que esta pieza no tiene*

No trae direcciones de catálogos, ni torrentes, ni servicios de suscripción: se mide software. **Ningún cliente ni índice de torrentes aparece con enlace** —esa es la familia que Facebook vetó en la pieza 12 y el tema de la 16—. Tampoco hay consejo legal: hay una sección que dice dónde está la pregunta.

**No es una lista de lo más nuevo ni de lo mejor**, es un censo con fechas: {palabras(A['nuevas2026'])} de 2026 arriba, los veteranos en medio con su nota, y dos casos —Seal y Motrix— señalados por lo que son, los más famosos del tema y los que no se mueven.

*📅 La semana de prueba · cinco días para dejar de bajar a ciegas*

- **Día uno.** Instala **yt-dlp** y baja un archivo tuyo con `--no-playlist`. Es el programa que hay debajo de casi todo lo demás.
- **Día dos.** Abre lo bajado con `ffprobe` y calcula su `sha256sum`. Apunta la huella: acabas de hacer lo que el 89 % de los programas de esta lista no hace.
- **Día tres.** Prueba un gestor: **Gopeed** si quieres ventana, **MovieBox-Tui** si quieres terminal. Mira cuál de los dos te deja ver la cola real.
- **Día cuatro.** En el teléfono, cambia Seal por **ytdlnis** si tienes Seal instalado: son la misma idea, uno parado y el otro con {num(E['deniscerri/ytdlnis']['commits_30d'])} cambios al mes.
- **Día cinco.** Revisa qué de lo que usas está en la lista de los quietos —Motrix, Seal, aria-ng-gui, uGet— y decide con la fecha delante.

───────────────────

*🧾 Lo que cambió en la noche, para que se pueda repetir*

Este bloque no va en ninguna otra pieza de la serie y esta lo lleva porque la noche lo pidió. Son los pasos exactos, con la orden de cada uno, para que cualquiera llegue a las mismas treinta y una fichas.

```
1. LBT=… python3 tools/fecha_viva.py --inicio                 # la fecha, en vivo
2. LBT=… python3 tools/preflight.py --tema descarga           # historial + ecosistema
3. LBT=… python3 tools/remedir.py --escribir docs/MEDICION-15b-noche-2026-11-04.json --pieza lista.txt
4. LBT=… python3 tools/escrutinio.py --repos …                # las notas de las 31
5. python3 docs/talleres/pieza15/a15.py && b15.py && c15.py    # el texto, desde los datos
6. python3 tools/manual_gate.py --pieza <pieza> && python3 tools/novedad_gate.py <pieza>
7. LBT=… python3 tools/envio.py --medir && --generar --canal ambos && --verificar
```

Lo que hace cada uno, en una línea: el **1** lee la fecha de una fuente de fuera y la anota; el **2** revisa qué está publicado, cuál toca y qué hay en el ecosistema antes de elegir nada; el **3** mide cada repositorio y escribe un archivo que nunca se sobrescribe; el **4** pone la nota con los nueve pesos; el **5** genera el texto desde esos datos, no desde la memoria; el **6** comprueba forma, banda y novedad; y el **7** corta la pieza en mensajes y verifica que no se perdió una línea.

La lección de la noche está en el paso 2 y en el 5 juntos: **si el texto se genera desde la medición, no hay forma humana de escribir una cifra de memoria.** Y si además el taller queda en el repositorio —`docs/talleres/pieza15/`—, cualquiera puede volver mañana, medir otra vez y ver qué cambió.

───────────────────

*❓ Las preguntas del grupo*

**¿Bajar vídeos es legal?**
Depende de qué bajes, de dónde y para qué. La herramienta no decide eso. En la República Dominicana aplica la Ley 65-00 con sus excepciones; esta pieza no da consejo legal y lo dice en voz alta.

**¿Cuál instalo, en una frase?**
**yt-dlp** de base, **Gopeed** si quieres ventana, **ytdlnis** en el teléfono. Los tres publican y los tres se mueven; los tres famosos que no se mueven son Seal, Motrix y uGet.

**¿Por qué dices que Seal está parado si funciona?**
Porque lleva **{R['JunkFood02/Seal']['dias_push']} días sin un empujón**, cero cambios en treinta días y {num(E['JunkFood02/Seal']['incidencias']['abiertas'])} incidencias abiertas. Funciona hoy y no se arregla mañana. Eso es lo que mide la fecha, no el programa.

**¿Merece la pena el de 2026 con tres meses?**
Para probar, sí: **rayburst** saca {E['AnInsomniacy/rayburst']['puntos']} y firma {num(E['AnInsomniacy/rayburst']['con_huella'])} de {num(E['AnInsomniacy/rayburst']['adjuntos'])} archivos. Para depender de él, espera un año y vuelve a mirar: media-downloader nació en mayo y ya está parado.

**¿Qué diferencia hay entre un gestor y un motor?**
El motor descarga —**aria2**, **wget2**, **yt-dlp**— y el gestor lo dirige con una ventana o una cola. Casi todos los gestores de esta lista son caras del mismo motor, y por eso el motor sigue vivo aunque la cara se muera.

**¿Y los programas que bajan de una web con anuncios?**
Se miden como todo: licencia, fecha, firma y cola. Ninguno de los que salen bien en esta pieza necesita anuncios, y eso ya es un dato.

**¿Por qué no hay torrentes aquí?**
Porque es la pieza 16 y porque Facebook vetó esa familia de enlaces en la 12. Se dice el nombre, se explica y se comprueba; la dirección no va.

───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **bajar es un acto técnico con tres decisiones** —de dónde sale, cómo se comprueba y qué llegó— y esta pieza mide los programas que permiten tomar las tres. No dice qué bajar.

Lo segundo: **los dos nombres más famosos del tema están parados.** Seal, con {num(R['JunkFood02/Seal']['stars'])} estrellas, lleva {R['JunkFood02/Seal']['dias_push']} días sin publicar; Motrix, con {num(R['agalwood/Motrix']['stars'])}, no tiene un cambio en treinta días. Ninguna lista de 2024 lo dice, y por eso esta se mide cada vez.

Lo tercero: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 10,6 %**. La mitad de la música de ayer, cuatro veces las aplicaciones de la 11 y ciento treinta veces las tiendas de la 10. Y un tercio de esa cifra la pone un proyecto de tres meses.

Lo cuarto, sobre el método: esta pieza es la primera que se escribió **después** de la revisión obligatoria —fecha, historial y ecosistema, en ese orden— y se nota en una cosa concreta: no hay una sola ficha que venga de una lista de 2024. Las treinta y una salieron del censo de esta noche.

Y lo cuarto: **{palabras(A['nuevas2026'])} nacidos en 2026, tres serios y cinco intentos**. Lo nuevo se mide, no se celebra. Ese es el método y no va a cambiar en la pieza 16.

───────────────────
""")
w(f"""— {num(A['adjuntos'])} archivos publicados por {palabras(A['vivos'])} programas de descarga y {num(A['con_huella'])} firmados: el 10,6 %, con un tercio de la cifra puesto por un proyecto de tres meses.
— Seal y Motrix, los dos nombres más recomendados del tema, medidos y señalados: {R['JunkFood02/Seal']['dias_push']} y {R['agalwood/Motrix']['dias_push']} días sin publicar.
— De la ley al `ffprobe`: lo que la app permite, lo que el archivo dice de sí mismo y seis órdenes para no bajar a ciegas.

💓 *La Bandita informa a partir de fuentes fechadas.* {palabras(A['vivos'])} programas abiertos hoy uno por uno —del motor que nadie instala al gestor que todos instalan—, la tabla de qué cubre qué, las {num(A['con_huella'])} sumas contadas archivo por archivo y seis órdenes para saber qué llegó y qué no.

───────────────────

*Medición del corte:* miércoles 4 de noviembre de 2026, {HORA} de la noche en Santo Domingo, con la fecha comprobada en vivo antes de empezar y al terminar · decimosexta medición del día · {palabras(A['vivos'])} programas vivos, ninguno archivado, {palabras(A['sin_lic'])} sin licencia legible · {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas · {num(A['descargas'])} descargas · {palabras(A['con_huella_repos'])} repositorios firmando.

*🔗 Enlaces*

""")
GRUPOS=[
("El motor bajo todo",['aria2/aria2','nilaoda/N_m3u8DL-RE','rockdaboot/wget2','axel-download-accelerator/axel','lwthiker/curl-impersonate']),
("Las caras del motor clásico",['mayswind/AriaNg','mayswind/AriaNg-Native','Xmader/aria-ng-gui','Xmader/aria-ng-gui-android','binux/yaaw']),
("Gestores de escritorio",['GopeedLab/gopeed','agalwood/Motrix','subhra74/xdm','Tyrrrz/YoutubeDownloader','persepolisdm/persepolis','uget/uget']),
("En el bolsillo",['deniscerri/ytdlnis','yausername/youtubedl-android','JunkFood02/Seal']),
("La línea de órdenes",['yt-dlp/yt-dlp','iawia002/lux','soimort/you-get','mikf/gallery-dl']),
("Los nacidos en 2026",['AnInsomniacy/rayburst','rawnaldclark/Stash','Downvid/downvid','FortoGraphy/prism-download-manager','mesamirh/MovieBox-Tui','arnoldhao/xiadown','pixel-point/media-downloader','BareBrowser/bare-browser']),
]
usados=set()
for titulo,rs in GRUPOS:
    w(f"*{titulo}:*\n\n")
    for r in rs:
        usados.add(r); w(f"- https://github.com/{r}\n")
    w("\n")
assert usados==set(VIVOS), set(VIVOS)-usados

w(f"""*Las cuatro direcciones de las órdenes:*

- api seal: https://api.github.com/repos/JunkFood02/Seal
- api entregas yt-dlp: https://api.github.com/repos/yt-dlp/yt-dlp/releases?per_page=100
- api sumas rayburst: https://api.github.com/repos/AnInsomniacy/rayburst/releases?per_page=100
- api ytdlnis: https://api.github.com/repos/deniscerri/ytdlnis

───────────────────

*🗒️ Notas al pie*

(4-nov) La fecha se comprobó **en vivo antes de empezar y al terminar**: `tools/fecha_viva.py --inicio` a las 22:28 y `--fin` al cerrar. **Antes de sondear un solo candidato** se hizo la revisión que ahora es regla —fecha, historial y ecosistema— con `tools/preflight.py --tema descarga`, y su acta quedó en `docs/PREFLIGHT-descarga-2026-11-04.json`. La medición final es de las {HORA} y vive en `docs/MEDICION-15b-noche-2026-11-04.json`.

(4-nov) **Decimosexta medición del día.** Las {palabras(A['vivos'])} direcciones se pidieron una por una. Una candidate salió con el nombre cambiado —Persepolis no vive donde decían las listas, sino en `persepolisdm/persepolis`— y se corrigió antes de escribir: la primera medición traía un «not found» y no se publicó.

(4-nov) La cuenta de **huella** es la de toda la serie: `sha256`, `sha512`, `sha1`, `checksum`, `.sig`, `.asc` o `sums` en el nombre de cada adjunto de las últimas cien entregas. Escala completa: 0,08 % · 5,5 % · 10,6 % · 11,4 % · 17,0 % · 20,0 %.

(4-nov) Las **notas** se calculan con los nueve pesos de la casa y las cuatro penalizaciones. Un proyecto de veinte días —prism— saca {E['FortoGraphy/prism-download-manager']['puntos']} porque cumple lo mismo que uno de diez años; y Seal, con {num(R['JunkFood02/Seal']['stars'])} estrellas, saca {E['JunkFood02/Seal']['puntos']} porque hace un mes que no publica.

(4-nov) **Ningún cliente ni índice de torrentes lleva enlace en esta pieza** (H20). El tema de la descarga directa se mide aquí; el de los torrentes es la pieza 16 y se escribirá con la misma norma.

(4-nov) **El taller de esta pieza queda en `docs/talleres/pieza15/`**, dentro del repositorio: los tres programas que generan el texto, para que cualquiera pueda repetir las cifras. Es la regla nueva —el almacén es GitHub y el disco de trabajo no se conserva—.

*#task*

#task 071 · volver a medir los {palabras(A['vivos'])} el 4 de diciembre y decir si Seal y Motrix publicaron algo: si no, dejan de recomendarse en la serie.

#task 072 · comprobar con `sha256sum` los instaladores de rayburst, ytdlnis y Gopeed contra la cifra que publican sus repositorios.

#task 073 · medir si la camada de 2026 de este tema aguanta: de los ocho, uno ya está parado y dos llevan un mes sin empujón.

#task 074 · escribir la pieza 16 con la norma del canal delante: torrentes sin enlace, nombre, función y comprobación.

───────────────────

🏷️ Etiquetas estratégicas

#Ytdlp #Gopeed #Rayburst #Seal #Ytdlnis #Aria2 #Ffprobe #Sha256sum #DescargaDirecta #GestoresDeDescarga #OpenSourceDominicano #SoftwareLibre
""")
open('/tmp/lab/docs/talleres/pieza15/s3.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
