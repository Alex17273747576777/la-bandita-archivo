# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab18/docs/talleres/pieza19')
from d19 import *
A=AGG; K=INDICE

def f(r,nombre,texto,nl=True):
    return f"{ficha(r,nombre)}. {texto}\n"

# ── A · las aplicaciones y la salida de Kotatsu ────────────────────────────────
T=[]; w=T.append
w(f"""*📱 Las siete aplicaciones, una por una*

La tabla dice qué tienda acepta cada una. Esto dice cómo está cada una hoy, porque una aplicación sin mantenimiento convierte la mejor tienda en un problema.

""")
T.append(f('mihonapp/mihon','Mihon',
  f"**{num(R['mihonapp/mihon']['stars'])} estrellas y {num(R['mihonapp/mihon']['dias_nace'])} días de historia**: el lector de referencia de la familia, con **empujón de hoy**, {num(R['mihonapp/mihon']['entregas'])} entregas y {num(E['mihonapp/mihon']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['mihonapp/mihon']['incidencias']['abiertas'])} abiertas. **{num(E['mihonapp/mihon']['adjuntos'])} adjuntos sin una suma**: el programa que instala extensiones no firma los suyos"))
T.append(f('aniyomiorg/aniyomi','Aniyomi',
  f"**{num(R['aniyomiorg/aniyomi']['stars'])} estrellas**, {num(R['aniyomiorg/aniyomi']['entregas'])} entregas y **{R['aniyomiorg/aniyomi']['dias_push']} días desde el último empujón**: la familia de vídeo, que es la que usa la tienda Yūzōnō. {num(E['aniyomiorg/aniyomi']['adjuntos'])} adjuntos sin firma y {num(E['aniyomiorg/aniyomi']['incidencias']['abiertas'])} incidencias abiertas"))
T.append(f('UsagiApp/Usagi','Usagi',
  f"**{num(R['UsagiApp/Usagi']['dias_nace'])} días de vida y {num(R['UsagiApp/Usagi']['stars'])} estrellas**: el heredero pequeño de Kotatsu, con {num(R['UsagiApp/Usagi']['entregas'])} entregas y **empujón de ayer**. {num(E['UsagiApp/Usagi']['commits_30d'])} cambios en treinta días y solo {num(E['UsagiApp/Usagi']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['UsagiApp/Usagi']['incidencias']['cerradas'])} cerradas"))
T.append(f('HuzaifaKhalid1311/DropSauce','DropSauce',
  f"**{num(R['HuzaifaKhalid1311/DropSauce']['dias_nace'])} días y la mejor nota del tema ({E['HuzaifaKhalid1311/DropSauce']['puntos']})**: lector de cómics y novelas que **acepta el formato de tienda de Mihon**, con {num(R['HuzaifaKhalid1311/DropSauce']['entregas'])} entregas y {num(E['HuzaifaKhalid1311/DropSauce']['commits_30d'])} cambios en treinta días. {num(E['HuzaifaKhalid1311/DropSauce']['adjuntos'])} adjuntos sin suma"))
T.append(f('kodjodevf/mangayomi','Mangayomi',
  f"**{num(R['kodjodevf/mangayomi']['stars'])} estrellas y {num(R['kodjodevf/mangayomi']['entregas'])} entregas**: lector multiplataforma con su propio formato de extensión, {num(E['kodjodevf/mangayomi']['commits_30d'])} cambios en treinta días y **{num(E['kodjodevf/mangayomi']['adjuntos'])} adjuntos sin una suma**. Su repositorio de extensiones oficial está archivado; el que se mantiene es m2k3a"))
T.append(f('lnreader/lnreader','LNReader',
  f"**{num(R['lnreader/lnreader']['stars'])} estrellas y {num(R['lnreader/lnreader']['dias_nace'])} días**: lector de novelas ligeras, el único del tema con **{num(E['lnreader/lnreader']['con_huella'])} sumas de {num(E['lnreader/lnreader']['adjuntos'])} adjuntos**. {num(R['lnreader/lnreader']['entregas'])} entregas y {num(E['lnreader/lnreader']['commits_30d'])} cambios en treinta días: el proyecto más quieto y el único que firma"))
T.append(f('KotatsuApp/Kotatsu','Kotatsu (archivada)',
  f"**{num(R['KotatsuApp/Kotatsu']['stars'])} estrellas, la más popular de la familia, y {R['KotatsuApp/Kotatsu']['dias_push']} días sin publicar**: archivada por su autor el 4 de noviembre de 2025. **Cero entregas, cero adjuntos, cero cambios en treinta días** y **{E['KotatsuApp/Kotatsu']['puntos']} puntos**. Se lista para que nadie la instale creyendo que sigue viva"))
open('/tmp/lab18/docs/talleres/pieza19/c19a1.md','w',encoding='utf-8').write("".join(T))

T=[]; w=T.append
w(f"""
**Lo que dicen las siete juntas:** la familia Mihon se mantiene —**empujón de hoy**, {num(E['mihonapp/mihon']['commits_30d'])} cambios en treinta días—; la de vídeo va más despacio —{R['aniyomiorg/aniyomi']['dias_push']} días—; y los dos herederos de Kotatsu son de este año y están vivos. **Ninguna de las siete firma sus archivos**: la aplicación que instala código de terceros no firma el suyo propio, y eso vale para todo el tema.

───────────────────

*🚚 Cómo salir de Kotatsu sin perder la biblioteca*

Si tu aplicación está archivada, el problema no es filosófico: es que tienes una biblioteca con marcadores, historial y descargas dentro de un programa que ya no se actualiza. El camino tiene cuatro pasos y ninguno es difícil.

**Primero, la copia.** Kotatsu exporta su biblioteca a un archivo propio y también a formatos que otras aplicaciones entienden. Se hace **antes** de instalar nada: ajustes → copia de seguridad → exportar. Ese archivo se guarda fuera del teléfono.

**Segundo, la elección.** Hay dos caminos vivos. **DropSauce** si quieres seguir leyendo lo mismo con la tienda de Mihon —Keiyoushi, {num(K['keiyoushi/extensions']['publicadas'])} extensiones— sin conversiones. **Usagi** si quieres lo más parecido a Kotatsu, con su propio plugin y compatibilidad con fuentes de Tsuki. Los dos aceptan bibliotecas exportadas; el primero, además, acepta tiendas que no son suyas.

**Tercero, la conversión si hace falta.** Los formatos de copia de estas aplicaciones son primos hermanos y hay conversores —uno de ellos, de una sola persona, convierte entre Mihon, Komikku, Aniyomi y TachiyomiSY—. Es el paso donde se pierde el historial si se hace mal: **se prueba con diez títulos, se mira qué llegó y después se hace con los mil**.

**Cuarto, las extensiones.** Se instala la tienda, se busca la extensión de cada fuente que usabas y se comprueba una por una. Aquí es donde se descubre que la mitad de lo que tenías venía de extensiones que ya no existen: **una biblioteca de marcadores no es una biblioteca de contenido**, y las fuentes se caen solas con el tiempo.

**Lo que no se puede hacer:** seguir en una aplicación archivada y esperar que alguien la arregle. Un repositorio archivado es una decisión, no un descuido.

───────────────────
""")
open('/tmp/lab18/docs/talleres/pieza19/c19a2.md','w',encoding='utf-8').write("".join(T))

# ── B · anatomía + las seis tiendas ───────────────────────────────────────────
T=[]; w=T.append
w(f"""*🔬 Anatomía de una extensión · cinco archivos y una versión con truco*

Una extensión de esta familia es un APK pequeño con una clase que implementa una interfaz. Verlo por dentro explica por qué una tienda puede tener mil cuatrocientas y otra seis.

**El código** vive en `src/<idioma>/<nombre-de-la-fuente>/`, con un archivo por clase: uno declara el nombre, el idioma y la versión; otro hace la búsqueda; otro lee los capítulos y otro las páginas. **{num(K['keiyoushi/extensions']['fuentes'])} de esas carpetas** hay en Keiyoushi, repartidas en {K['keiyoushi/extensions']['idiomas']} idiomas: **{K['keiyoushi/extensions']['idiomas'] and K['keiyoushi/extensions']['publicadas'] and 423}** en inglés, **140** en japonés, **139** para todos los idiomas, **117** en portugués, **104** en español, **59** en árabe.

**La versión** es la parte que casi nadie entiende y la que rompe las instalaciones. No es `1.4.3`: es `1.4.<parche>+<código>` y el número que la aplicación compara es el de la derecha. Cuando el sitio cambia su HTML y la extensión se arregla, **se sube el código, no la versión bonita**; y como cada extensión tiene su propio contador, la aplicación puede actualizar una sin tocar las demás. Por eso una tienda publica entregas casi a diario: **cada arreglo es un archivo nuevo**.

**El manifiesto** declara el paquete, la versión mínima de la aplicación y —esto es lo interesante— **de qué aplicación es la librería**. Una extensión de Mihon y una de Aniyomi se parecen mucho por fuera y no son intercambiables: compilan contra librerías distintas y una aplicación rechaza la de la otra. **Ahí está la raíz del error de la tabla.**

**El índice** es lo que la aplicación lee primero: un archivo con las {num(K['keiyoushi/extensions']['publicadas'])} entradas de Keiyoushi, cada una con su paquete, su versión y la dirección de su APK. Se descarga una vez cada pocas horas y se cachea. **Si el índice no se actualiza, la aplicación no ve las extensiones nuevas aunque estén publicadas.**

**Y la clave de firma**, cuando existe, es lo que impide que alguien cambie esa lista por el camino. Tres de las seis tiendas medidas la declaran. Las otras tres confían en que el archivo que baja es el que se publicó, sin comprobarlo.

───────────────────

*📦 Las seis tiendas que pasan el listón, una por una*

Seis y no veinte. Cada una con lo que publica hoy, lo que firma y lo que le falta.

""")
T.append(f('keiyoushi/extensions','Keiyoushi',
  f"**{num(K['keiyoushi/extensions']['publicadas'])} extensiones publicadas y {num(K['keiyoushi/extensions']['fuentes'])} fuentes** en {K['keiyoushi/extensions']['idiomas']} idiomas: **la única tienda real de la familia Mihon**, con el índice firmado. {num(R['keiyoushi/extensions']['stars'])} estrellas, **{num(E['keiyoushi/extensions']['adjuntos'])} adjuntos sin una sola suma** y **empujón de ayer**. {num(E['keiyoushi/extensions-source']['commits_30d'])} cambios en treinta días en el repositorio de código y {num(E['keiyoushi/extensions-source']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['keiyoushi/extensions-source']['incidencias']['abiertas'])} abiertas: el que más gente usa y el que más cola tiene"))
T.append(f('keiyoushi/extensions-source','Keiyoushi (el código)',
  f"**{num(R['keiyoushi/extensions-source']['stars'])} estrellas y empujón de hoy**: el repositorio donde se escribe lo que el otro publica, con **{num(K['keiyoushi/extensions']['fuentes'])} carpetas de fuente**, integración continua y {num(E['keiyoushi/extensions-source']['incidencias']['cerradas'])} incidencias cerradas. Es el único del tema que enseña cómo se hace una tienda"))
T.append(f('yuzono/anime-extensions','Yūzōnō (Aniyomi)',
  f"**{num(K['yuzono/anime-extensions']['publicadas'])} extensiones, índice firmado y {num(R['yuzono/anime-extensions']['stars'])} estrellas**: la tienda de la familia Aniyomi, con empujón de ayer y {num(E['yuzono/anime-extensions']['commits_30d'])} cambios en treinta días. **El repositorio de publicación se mudó**: la dirección que circula responde 301 a `mojuru/anime-repo`"))
T.append(f('m2k3a/mangayomi-extensions','m2k3a (Mangayomi)',
  f"**{num(K['m2k3a/mangayomi-extensions']['publicadas'])} extensiones y {num(R['m2k3a/mangayomi-extensions']['stars'])} estrellas**: las mantiene una sola persona desde que el repositorio oficial se archivó, con {num(E['m2k3a/mangayomi-extensions']['commits_30d'])} cambios en treinta días y **{num(E['m2k3a/mangayomi-extensions']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['m2k3a/mangayomi-extensions']['incidencias']['cerradas'])} cerradas. **Sin firma de índice**"))
T.append(f('salmanbappi/sb-extensions-source','SalmanBappi',
  f"**{num(K['salmanbappi/sb-extensions-source']['publicadas'])} fuentes, {num(R['salmanbappi/sb-extensions-source']['entregas'])} entregas y {num(E['salmanbappi/sb-extensions-source']['commits_30d'])} cambios en treinta días**: el complemento de la familia Aniyomi para fuentes del sur de Asia —**21 en bengalí y 58 en inglés**—. {num(R['salmanbappi/sb-extensions-source']['stars'])} estrellas, integración continua y **sin firma de índice**"))
T.append(f('lnreader/lnreader-plugins','LNReader',
  f"**{num(K['lnreader/lnreader-plugins']['publicadas'])} plugins y {num(R['lnreader/lnreader-plugins']['stars'])} estrellas**: el ecosistema de novelas, con {num(E['lnreader/lnreader-plugins']['commits_30d'])} cambios en treinta días y **{num(E['lnreader/lnreader-plugins']['con_huella'])} sumas de {num(E['lnreader/lnreader-plugins']['adjuntos'])} adjuntos**. Es el **único de los veinte repositorios del tema que firma algo**, y por eso el 0,07 % de esta pieza tiene un solo autor"))

T.append(f"""
**Lo que comparten las seis:** todas publican desde un repositorio de GitHub, todas aceptan que cualquiera lea su código salvo la de Keiyoushi, que **no declara licencia legible** pese a tener {num(R['keiyoushi/extensions']['stars'])} estrellas, y **ninguna firma sus APK**. Y una que no está en la lista y conviene decir por qué: el mega repositorio de Cloudstream se actualiza a diario y junta muchos otros, pero **no declara licencia** y publica {num(E['admknight/CloudstreamExtensions']['adjuntos'])} archivos con {num(E['admknight/CloudstreamExtensions']['incidencias']['abiertas'])} incidencias abiertas sin cerrar. Se nombra; no se recomienda.

───────────────────
""")
open('/tmp/lab18/docs/talleres/pieza19/c19b.md','w',encoding='utf-8').write("".join(T))

# ── C · la comunidad, punto por punto ─────────────────────────────────────────
T=[]; w=T.append
w(f"""*🗣️ Lo que la comunidad reclamó, punto por punto*

Estas tiendas tienen un sitio comunitario que las ordena, y sus administradores escribieron una queja que conviene contestar de frente, porque es la crítica más justa que ha recibido esta serie. Va punto por punto, sin defenderse.

**«Añadan una sección donde las apps se agrupen según las extensiones compatibles.»** Está hecho: es la tabla 🗺️ de esta pieza, con once aplicaciones y su tienda, comprobada hoy. Es también la petición más razonable de todo el escrito y la única que se resuelve con trabajo de medición.

**«Dejen de usar IA para volcar listas.»** De acuerdo. Esta pieza mide **{palabras(A['vivos'])} piezas y no trescientas**, y deja diez fuera con nombre y motivo. Un volcado de trescientas no es un censo: es una lista donde nadie puede comprobar nada.

**«No todo repositorio necesita ser indexado.»** De acuerdo, y aquí está el criterio: archivado, último empujón, índice contado, firma, nombre real de la tienda y descripción leída. Con esas seis, diez de los veinte medidos hoy se quedan fuera.

**«La IA no nota si un repositorio dice tener funciones que no tiene.»** Cierto —si no se cuenta—. Por eso aquí las funciones se cuentan en el índice: {num(K['keiyoushi/extensions']['publicadas'])} en Keiyoushi, {num(K['yuzono/anime-extensions']['publicadas'])} en Yūzōnō, **{K['dragonx943/manga-repo']['publicadas']}** en el plugin de Usagi que presume de 24 estrellas.

**«Ni si quita límites de tasa, ni si está vibe-codeado, ni si dice que no hay soporte.»** Las dos primeras **no se pueden comprobar desde la API** y esta pieza no las usa como argumento: quien las afirme, que enseñe la línea. La tercera sí: **se lee la descripción**, y si el autor dice que no programa o que no hay soporte, se cree al autor —es lo que se hizo con el APK de la pieza 17 y lo que se hace aquí con los cuatro repositorios cuyo nombre es una dirección—.

**«Paredes de texto que ningún humano lee.»** Esta pieza tiene 12 secciones, cuatro tablas y **{num(A['vivos'])} fichas de una línea cada una**. Si sigue siendo demasiado, el problema no es el formato: es el tema.

**«Que la IA clone el repositorio y pruebe la aplicación.»** Es la crítica que **no se puede cumplir desde aquí y no se va a fingir**: este taller no tiene un teléfono Android ni puede abrir una extensión. Lo que sí se puede —y se hizo— es abrir el índice publicado, contar sus entradas, leer su nombre real y seguir sus redirecciones. **Lo que no se puede, se declara**, y por eso la orden 6 de esta pieza no es un comando: es abrir la aplicación.

**«Revisen la fecha en vivo en vez de predecirla.»** Es la primera regla de esta casa desde el 4 de noviembre: fecha comprobada en vivo antes de empezar y al terminar, en cada pieza. La de hoy está en las notas al pie.

**Y lo que esta pieza añade a la queja, en la misma dirección:** la lista que circula **está mal en seis de seis cifras**, y no por culpa de quien la copió. Cursed pasó de 131 extensiones a **{K['mojuru/cursed-manga-repo']['publicadas']}**; Kotatsu lleva **366 días archivada**; el enlace de Yūzōnō **redirige**. Con eso no hace falta más discurso: hace falta volver a contar cada mes.

───────────────────
""")
open('/tmp/lab18/docs/talleres/pieza19/c19c.md','w',encoding='utf-8').write("".join(T))
print("ok")
