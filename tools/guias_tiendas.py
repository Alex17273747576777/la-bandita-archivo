#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_tiendas.py · las guías escritas a mano del racimo «tiendas-de-extensiones» (24 recursos)."""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "tiendas-de-extensiones"

GUIA = {}

GUIA["mihonapp/mihon"] = """
### Para qué sirve

El lector de manga para Android sobre el que gira casi todo este racimo. Lee, organiza la biblioteca por
categorías, descarga capítulos para leer sin conexión, avisa cuando sale uno nuevo y se conecta a siete
rastreadores —MyAnimeList, AniList, Kitsu, MangaBaka, MangaUpdates, Shikimori, Bangumi— más Hikka.

Lo que **no** trae es contenido. Ni una fuente. Es el estante vacío: los libros los pone quien lo usa, a través
de extensiones.

### Cómo se usa

1. Se instala la APK de la entrega `v0.21.3`, del 25 de octubre de 2026, o se baja de la web del proyecto.
2. Se abre *Más → Ajustes → Examinar → Repositorios de extensiones* y se pega la dirección de un índice.
3. Se instalan las extensiones que interesen y aparecen como fuentes en *Examinar*.
4. Si vienes de otro lector de la misma familia, se restaura la copia de seguridad del anterior al arrancar.

### Lo que conviene saber antes

25.042 estrellas, Apache-2.0, Kotlin, creado en enero de 2024 y con un empujón hoy mismo. 746 incidencias
abiertas: es un proyecto grande con mucha gente dentro y mucho ruido fuera.

Hay dos cosas que se aprenden con el uso. La primera, que **las fuentes se rompen**: cuando el sitio de turno
cambia su web, la extensión deja de funcionar hasta que alguien la arregla, y eso no depende del lector. La
segunda, que el lector no opina sobre los derechos de lo que lee; la responsabilidad de qué se descarga es de
quien lo descarga.

### Cuándo no vale la pena

Si quieres abrir un cómic que ya tienes en el teléfono, un visor de archivos hace lo mismo sin pedirte una
biblioteca. Y si lo que buscas es una app que «venga con manga dentro», esta no es: aquí dentro no hay nada
hasta que tú lo pongas.
"""

GUIA["keiyoushi/extensions"] = """
### Para qué sirve

El índice de extensiones de Mihon y sus variantes. No es un programa: es un **repositorio de paquetes** con un
archivo índice que el lector consulta para saber qué fuentes existen, en qué versión y de dónde se descargan.

Es el canon de este racimo: cuando se habla de «el repositorio de extensiones», en la práctica se habla de este.

### Cómo se usa

1. En el lector, se abre *Ajustes → Examinar → Repositorios de extensiones* y se añade la dirección del índice.
2. El lector lee el índice y lista las fuentes disponibles.
3. Se instalan las que se quieran, una a una; el lector se encarga de avisar de las actualizaciones.
4. Si el lector no permite añadir repositorios, queda la vía manual: descargar el paquete desde la página de
   entregas e instalarlo como cualquier APK.

### Lo que conviene saber antes

15.438 estrellas y 1.364 bifurcaciones, pero **sin licencia reconocible**: es el repositorio de los artefactos
compilados, no el del código —ese es otro, y ese sí declara licencia—. Tiene 20 adjuntos en su última entrega y
se mueve a diario.

Y el detalle que explica el resto: sus 0 incidencias abiertas no significan que no haya problemas, significa que
las incidencias se atienden en el repositorio del código. Buscar un fallo aquí es buscar en el sitio equivocado.

### Cuándo no vale la pena

Si ya usas otro índice que te funciona, añadir este duplica fuentes y confunde las actualizaciones. Y si tu
lector no entiende este formato de índice, no sirve de nada descargarlo.
"""

GUIA["keiyoushi/extensions-source"] = """
### Para qué sirve

El código de las extensiones del índice anterior: una extensión por carpeta, cada una con su analizador de la
web correspondiente. Sirve para tres cosas muy concretas: entender cómo está hecha una extensión, arreglar una
que se rompió y escribir una nueva.

### Cómo se usa

1. Se clona el repositorio; es un proyecto de Gradle con muchos módulos, uno por fuente.
2. Se copia la carpeta de una extensión parecida a la que se quiere escribir y se cambian el nombre, el dominio
   y las reglas de extracción.
3. Se compila solo ese módulo, se prueba contra la web real y se instala el paquete resultante.
4. Para aportarlo, se abre una petición con el módulo nuevo y se acepta la guía de estilo del proyecto.

### Lo que conviene saber antes

4.865 estrellas, Apache-2.0, Kotlin, creado en enero de 2024, con 473 incidencias abiertas y movimiento de hoy.
No tiene entregas etiquetadas: aquí no se viene a descargar nada, se viene a compilar.

El trabajo real no es programar, es **leer la web del otro lado**: cada fuente es un analizador que se rompe
cuando esa web cambia. Por eso hay tantas incidencias abiertas y por eso una extensión que hoy funciona puede
no funcionar en tres semanas.

### Cuándo no vale la pena

Si solo quieres leer, este repositorio no te da nada que puedas usar directamente. Y si esperas una extensión
para un sitio muy pequeño, lo más probable es que nadie la haya escrito ni la vaya a escribir.
"""

GUIA["yuzono/manga-repo"] = """
### Para qué sirve

Un índice de extensiones pequeño, compatible con Mihon y sus variantes, para fuentes que no están en el índice
grande. Es el tipo de repositorio que existe porque alguien quería una fuente concreta y la publicó.

### Cómo se usa

1. Se añade la dirección de su índice en *Ajustes → Examinar → Repositorios de extensiones*.
2. Se instalan las fuentes que aparezcan.
3. Si el lector no admite repositorios, desde la página de listado se pueden bajar los paquetes a mano.

### Lo que conviene saber antes

13 estrellas y **sin licencia declarada**. Creado el 14 de agosto de 2026 y sin un empujón desde el 18 de ese
mismo mes: tres meses y medio de silencio. La descripción que trae es, literalmente, la del índice grande,
señal de que nació como copia y no se ha terminado de presentar.

Con ese tamaño y esa inactividad, lo honesto es tratarlo como lo que es: un índice de autor único, con pocas
fuentes y sin nadie detrás comprometido a mantenerlo. Si mañana una fuente deja de funcionar, puede que nunca
se arregle.

### Cuándo no vale la pena

Casi siempre. Si el índice grande ya cubre lo que lees, este añade ruido. Solo tiene sentido si buscas una
fuente muy específica que no está en ningún otro sitio y aparece aquí.
"""

GUIA["yuzono/cursed-manga-extensions"] = """
### Para qué sirve

Índice de extensiones compatible a la vez con Komikku y con Mihon y sus variantes. Ese «a la vez» es lo que lo
hace distinto: la mayoría de índices sirven a una familia y este se declara compatible con dos.

### Cómo se usa

1. Se añade la dirección de su índice en el lector que uses —Komikku o Mihon—.
2. Se instalan las fuentes que aparezcan en el listado.
3. No hay página de descargas separada: el propio índice es el que reparte los paquetes.

### Lo que conviene saber antes

221 estrellas, Apache-2.0, Kotlin, creado el 24 de marzo de 2026, con 48 bifurcaciones, 28 incidencias abiertas
y movimientos de ayer. Es un proyecto joven pero con actividad real y código a la vista.

La palabra que da nombre al repositorio no es un adjetivo: es la etiqueta de una colección concreta de fuentes.
Antes de añadirlo conviene mirar el listado y decidir si eso es lo que se quiere en el estante, porque una vez
dentro aparece junto al resto.

### Cuándo no vale la pena

Si no usas Komikku ni Mihon, no aplica. Y si te basta con el índice principal de tu lector, este solo añade
fuentes que probablemente ya tengas cubiertas.
"""

GUIA["yuzono/anime-repo"] = """
### Para qué sirve

Índice de extensiones de **vídeo** para Aniyomi y sus derivados, entre ellos Anikku y Animiru. Donde los
índices de manga reparten analizadores de páginas de lectura, este reparte analizadores de páginas de emisión.

### Cómo se usa

1. Se añade la dirección del índice en el apartado de repositorios del reproductor.
2. Se instalan las extensiones de anime que aparezcan.
3. Las fuentes se ordenan por idioma y por subtitulado o doblaje, según lo que declare cada una.

### Lo que conviene saber antes

72 estrellas y **sin licencia declarada**, con 29 incidencias abiertas y empujón de hoy. Lo peculiar está en su
propio aviso: pide que se siga usando la dirección `yuzono/anime-repo` **aunque el repositorio real esté en otro
sitio**. Eso es un traslado con la puerta vieja abierta, y conviene respetarlo: si copias la dirección nueva,
las actualizaciones dejarán de llegar a quien ya lo tenía instalado.

El medidor marcó además la bandera de espejo, y con razón: existe un segundo repositorio con el mismo contenido.

### Cuándo no vale la pena

Si no usas un reproductor de la familia Aniyomi, este índice no te sirve de nada. Y si ya tienes uno que
funciona, cambiarlo solo para tener más fuentes suele costar más de lo que aporta.
"""

GUIA["mojuru/anime-repo"] = """
### Para qué sirve

El mismo índice de extensiones de vídeo del recurso anterior, publicado bajo otra cuenta. La descripción del
repositorio lo dice sin rodeos: hay que seguir usando la dirección `yuzono/anime-repo` para instalarlo, esté el
repositorio donde esté.

Está en el catálogo porque **medirlo por separado era necesario**: dos repositorios con nombre distinto y el
mismo contenido cuentan como dos entradas, y quien lea el catálogo tiene derecho a saber que son la misma cosa.

### Cómo se usa

1. No se instala desde aquí. Se usa la dirección del índice que el propio proyecto señala.
2. Si aun así se pega esta, el lector leerá el mismo listado de fuentes.
3. Las actualizaciones dependen de que el índice se regenere, y eso ocurre en un solo sitio.

### Lo que conviene saber antes

72 estrellas, sin licencia declarada, creado el 6 de febrero de 2026, con 23 bifurcaciones, 29 incidencias y
movimiento de hoy — exactamente los mismos números que su gemelo, porque es el mismo repositorio con otra
dirección.

Ese es el dato útil de esta ficha: **cuando dos entradas del catálogo tienen las mismas estrellas, las mismas
bifurcaciones y las mismas incidencias, no son dos proyectos**. Son uno. Contarlas como dos opciones distintas
sería inflar el catálogo.

### Cuándo no vale la pena

Siempre que exista el original, esta entrada no aporta nada nuevo. Su utilidad es de archivo: si algún día la
dirección vieja desaparece, aquí queda constancia de por dónde pasó.
"""

GUIA["AppFuton/Futon"] = """
### Para qué sirve

Lector de manga para Android con fuentes en línea incorporadas, heredero directo de Kotatsu: mismo enfoque,
misma biblioteca local, mismos archivos CBZ de terceros que se pueden abrir sin fuente ninguna.

Nació, como casi todo lo de este racimo, de una retirada: cuando Kotatsu anunció su cierre, alguien continuó el
trabajo con otro nombre.

### Cómo se usa

1. Se instala la APK de la entrega `v9.9`, del 21 de octubre de 2026.
2. Se añaden fuentes desde el catálogo de extensiones del propio lector.
3. Se descarga para leer sin conexión; los CBZ que ya tengas se abren directamente.
4. La biblioteca se puede exportar e importar para no perderla al cambiar de teléfono.

### Lo que conviene saber antes

477 estrellas, GPL-3.0, Kotlin, creado el 7 de diciembre de 2025, con 45 bifurcaciones, 30 incidencias abiertas
y movimiento de ayer. La numeración `v9.9` llama la atención en un proyecto de menos de un año: viene heredada
del proyecto del que sale, no de su propia cuenta.

El medidor le puso dos banderas —abandono declarado y aviso de retirada— que proceden del texto que arrastra la
herencia de Kotatsu. **No significa que Futon esté abandonado**: se mueve a diario. Significa que su
documentación habla del cierre del otro, y eso conviene leerlo sabiendo de quién habla.

### Cuándo no vale la pena

Si vienes de Kotatsu y solo quieres seguir leyendo lo mismo, aquí está. Si empiezas de cero y no tienes motivo
para preferir este lector a otro, el ecosistema pequeño de este se nota cuando una fuente falla.
"""

GUIA["KotatsuApp/Kotatsu"] = """
### Para qué sirve

Fue el lector de manga con fuentes incorporadas más usado de Android: biblioteca local, favoritos, historial,
descarga de capítulos y un catálogo propio de extensiones.

Está en el catálogo **porque hay que decirlo**: su propio texto anuncia el cierre. Amenazas legales de Kakao
Entertainment y la nueva política de instalación de Google son los dos motivos que da el proyecto para dejarlo.

### Cómo se usa

No se usa. Si ya lo tienes instalado, lo que queda por hacer es exportar la biblioteca y el historial desde
*Ajustes → Copia de seguridad* antes de que el teléfono lo actualice o lo deje huérfano.

1. Se abre el lector.
2. Se exporta la copia en un archivo y se guarda fuera del teléfono.
3. Se elige un lector sucesor y se importa esa copia.

### Lo que conviene saber antes

8.952 estrellas, GPL-3.0, Kotlin, creado en enero de 2020: seis años de trabajo. Su último empujón es del 4 de
noviembre de 2025, hace un año, y **no tiene ninguna entrega etiquetada**. 579 incidencias abiertas que ya no
se van a cerrar.

Ese es el dato que ordena todo lo demás: un proyecto con 8.952 estrellas y un año de silencio no está «en
pausa», está terminado. Las bifurcaciones que salieron de aquí —Futon, Usagi, Drop Sauce— son la continuación
real.

### Cuándo no vale la pena

Siempre, para instalar de nuevo. Su valor hoy es el de una copia de seguridad: si tienes datos dentro, sácalos.
Si no tienes nada que rescatar, no hay motivo para empezar por aquí.
"""

GUIA["HuzaifaKhalid1311/DropSauce"] = """
### Para qué sirve

Lector de cómics y novelas para Android, ligero, con su propio catálogo de extensiones. Es una de las
continuaciones que aparecieron tras el cierre de Kotatsu, y se distingue por dos cosas que el original no tenía:
sincronización con Google Drive y actualizaciones dentro de la propia aplicación.

### Cómo se usa

1. Se instala la APK de la entrega `v1.1.2`, del 4 de noviembre de 2026.
2. El asistente de bienvenida ofrece dos caminos: empezar limpio o restaurar una copia anterior.
3. Se añade el repositorio de extensiones que use el lector y se instalan las fuentes.
4. La copia se puede dejar en local o sincronizar con Drive para no perderla.

### Lo que conviene saber antes

229 estrellas, GPL-3.0, Kotlin, creado el 25 de marzo de 2026, con 23 bifurcaciones, **una sola incidencia
abierta** y entrega de ayer mismo. Ese «una incidencia» en un lector con fuentes dice bastante: o el proyecto
está muy cuidado, o todavía tiene pocos usuarios. Probablemente las dos cosas.

El detalle a mirar con lupa es la sincronización con Google Drive: cómoda, y a la vez la parte que más datos
mueve fuera del teléfono. Se puede usar solo la copia local.

### Cuándo no vale la pena

Si vienes de Kotatsu con una biblioteca grande, importa primero y decide después: no todas las bifurcaciones
leen la misma copia. Y si no quieres ninguna cuenta de por medio, la sincronización sobra.
"""

GUIA["UsagiApp/Usagi"] = """
### Para qué sirve

Lector de manga para Android que corre desde la versión 5.0 del sistema —lo que ya es raro y dice mucho de
cuántos teléfonos viejos siguen vivos—. Trae lector propio, descargas para leer sin conexión, soporte de CBZ
ajenos y un sistema de plugins compatible con Tsuki.

### Cómo se usa

1. Se instala la APK de la entrega `v1.2`, del 3 de octubre de 2026.
2. Se añade el repositorio de plugins que corresponda y se instalan las fuentes.
3. Se organiza la biblioteca por categorías y se descargan los capítulos que se quieran tener a mano.
4. La copia de seguridad local permite mover la biblioteca entre teléfonos.

### Lo que conviene saber antes

289 estrellas, GPL-3.0, Kotlin, creado el 20 de marzo de 2026, con 65 bifurcaciones, 18 incidencias abiertas y
movimiento de hoy. Su texto menciona túneles dentro de la aplicación para saltar bloqueos de red: útil en redes
cerradas, y también la clase de función que conviene entender antes de activarla.

El medidor le puso la bandera de abandono declarado por una mención en su propio texto. **El repositorio está
vivo**; la mención viene de la historia del proyecto, no de su estado de hoy.

### Cuándo no vale la pena

Si tu teléfono es reciente y ya tienes un lector que funciona, cambiar solo por el soporte de Android antiguo
no tiene sentido. Su motivo de existir es otro: seguir leyendo en aparatos que otros ya no admiten.
"""

GUIA["dragonx943/manga-repo"] = """
### Para qué sirve

Repositorio de plugins para Usagi, compatible también con Tsuki. Es el tipo de pieza que hace falta para que un
lector joven tenga algo que leer: alguien que mantenga el catálogo de fuentes por su cuenta.

### Cómo se usa

1. Se añade la dirección del índice en el apartado de plugins del lector.
2. Se instalan las fuentes del listado.
3. Cuando una fuente falla, se desinstala y se espera a que el índice se actualice.

### Lo que conviene saber antes

24 estrellas, GPL-3.0, Kotlin, creado el 15 de mayo de 2026, con 15 bifurcaciones, **0 incidencias abiertas** y
entrega del 23 de octubre de 2026. Declara plataformas de escritorio además de Android, aunque lo que reparte
son extensiones para el lector.

La ficha arrastra la bandera «pide root»: el medidor la puso porque el texto del repositorio menciona root en
algún punto. **No es un requisito para instalar las extensiones**, y conviene decirlo para que nadie se asuste
sin motivo. Las etiquetas del repositorio hablan de contenido para adultos, y eso es decisión de cada cual.

### Cuándo no vale la pena

Si no usas Usagi ni Tsuki, no hay nada que hacer aquí. Y si lo que buscas es un catálogo amplio, este tiene
pocas fuentes y un solo mantenedor: se agota rápido.
"""

GUIA["animiruorg/Animiru"] = """
### Para qué sirve

Gestor de biblioteca y reproductor de vídeo para Android, pensado para series: organiza lo que ves, lleva la
cuenta de los capítulos y reproduce con un reproductor montado sobre mpv, con todos sus ajustes de imagen,
subtítulos y decodificación. Se conecta a MyAnimeList, AniList, Kitsu, Shikimori, Simkl, Bangumi y Hikka.

Es el equivalente en vídeo de lo que Mihon es en lectura: el estante, no el contenido.

### Cómo se usa

1. Se instala la APK de la entrega `v0.20.1.1`, del 3 de noviembre de 2026.
2. Se añade un índice de extensiones de vídeo en los ajustes del reproductor.
3. Se instalan las fuentes y se busca la serie.
4. El progreso se sincroniza con el rastreador que se haya conectado.

### Lo que conviene saber antes

907 estrellas, GPL-3.0, Kotlin, creado en marzo de 2022, con 38 bifurcaciones, 39 incidencias abiertas y
movimiento de ayer. Seis adjuntos en su última entrega y versiones frecuentes.

El medidor marcó la bandera de espejo: el proyecto se publica también desde otra dirección. Y hay un detalle
práctico que vale la pena: **mpv no perdona**. En teléfonos modestos, un archivo de vídeo grande va a tirones
por mucho que la app esté bien hecha; eso se arregla con el archivo, no con la aplicación.

### Cuándo no vale la pena

Si no ves series en el teléfono, no hay nada que hacer. Y si lo que quieres es solo descargar un capítulo
suelto, el reproductor del sistema hace el trabajo sin pedirte una biblioteca.
"""

GUIA["Secozzi/aniyomi-extensions"] = """
### Para qué sirve

Índice de extensiones de vídeo para Aniyomi y los reproductores derivados, entre ellos Animiru. Reparte los
analizadores que convierten una página de emisión en algo que el reproductor puede reproducir.

### Cómo se usa

1. Se añade la dirección del índice en el reproductor.
2. Se instalan las extensiones que aparezcan, filtrando por idioma.
3. Si se prefiere, desde la rama `repo` del repositorio se pueden bajar los paquetes uno a uno e instalarlos a
   mano.

### Lo que conviene saber antes

130 estrellas, Apache-2.0, Kotlin, creado en junio de 2024, con 18 bifurcaciones y solo 2 incidencias abiertas.
Su última entrega es del 20 de septiembre de 2026, con tres adjuntos, y el último empujón es de ese mismo día:
**seis semanas sin movimiento**.

Eso no lo invalida, pero sí lo sitúa: un índice de extensiones sin empujones recientes suele significar fuentes
que se van rompiendo poco a poco sin que nadie las arregle. Tiene menos fuentes que los índices grandes, y a
cambio es más fácil saber qué hay dentro.

### Cuándo no vale la pena

Si tu reproductor tiene un índice propio que se actualiza, añadir este mezcla fuentes de dos orígenes y complica
las actualizaciones. Y si usas Mihon, esto no es para ti: aquí se reparte vídeo, no lectura.
"""

GUIA["kodjodevf/mangayomi"] = """
### Para qué sirve

Aplicación de lectura y visionado hecha en Flutter que va más allá de Android: lee manga, lee novelas y ve
anime, y corre en móvil, escritorio y navegador. Las extensiones son **scripts en JavaScript**, no paquetes
compilados, y eso cambia la forma de instalarlas y de arreglarlas.

### Cómo se usa

1. Se instala desde las entregas: la última es la `v0.9.95`, del 1 de noviembre de 2026, con 14 adjuntos para
   distintas plataformas.
2. En *Ajustes → Extensiones* se añade la dirección de un índice.
3. Se instalan las fuentes; cada una se ejecuta como script dentro de la app.
4. La biblioteca queda en local, con copia de seguridad manual.

### Lo que conviene saber antes

4.375 estrellas, Apache-2.0, Dart, creado en abril de 2023, con 191 bifurcaciones, 66 incidencias abiertas y
movimiento de ayer. Sigue en versión 0.9: después de tres años, el proyecto no se ha declarado estable.

La decisión de usar JavaScript tiene una consecuencia que se nota: las extensiones se pueden escribir y probar
sin compilar un APK, y por eso hay varias personas manteniendo índices a la vez. La otra cara es que un script
con un fallo deja la fuente muerta sin más aviso que el error.

### Cuándo no vale la pena

Si solo usas Android y te basta un lector de manga, Mihon tiene un ecosistema mucho más grande. Mangayomi se
elige cuando importa leer en escritorio o en el navegador con la misma biblioteca.
"""

GUIA["kodjodevf/mangayomi-extensions"] = """
### Para qué sirve

El índice de extensiones oficial de Mangayomi: los scripts de manga y novela que la aplicación ofrece por
defecto. Es el que aparece en todas las guías del programa y el que se añade primero.

### Cómo se usa

1. Se copia la dirección de su índice y se pega en *Ajustes → Extensiones → Añadir repositorio*.
2. Se instalan las fuentes y se ordenan por idioma.
3. Las actualizaciones llegan cuando el índice se regenera; si no llegan, es que no se ha regenerado.

### Lo que conviene saber antes

360 estrellas, Apache-2.0, JavaScript, creado en julio de 2023, con 79 bifurcaciones y **103 incidencias
abiertas**. El último empujón es del **1 de octubre de 2025**: más de un año parado, y sin ninguna entrega
etiquetada.

Ese es el dato que hay que leer con cuidado, porque el repositorio sigue siendo el «oficial». Un índice parado
durante un año no es un índice roto —los paquetes que hay siguen sirviendo— pero sí es un índice que ya no
recibe fuentes nuevas ni arreglos. Por eso en este racimo hay tres índices comunitarios de la misma aplicación.

### Cuándo no vale la pena

Para empezar, no: es la puerta de entrada normal. Pero si te encuentras fuentes muertas que nadie arregla, el
problema no se resuelve aquí, se resuelve añadiendo otro índice.
"""

GUIA["m2k3a/mangayomi-extensions"] = """
### Para qué sirve

Índice de extensiones de Mangayomi mantenido por la comunidad, con fuentes que no están en el oficial y con
arreglos que el oficial ya no recibe. Es la respuesta práctica al año de silencio del índice de referencia.

### Cómo se usa

1. Se añade la dirección de su índice junto al oficial: no lo sustituye, se suma.
2. Se instalan las fuentes nuevas; las que ya existían pueden aparecer duplicadas.
3. Cuando dos entradas hacen lo mismo, se queda la que se actualice y se quita la otra.

### Lo que conviene saber antes

116 estrellas, Apache-2.0, JavaScript, creado el 24 de julio de 2025, con 59 bifurcaciones, 8 incidencias
abiertas y movimiento de ayer mismo. Sin entregas etiquetadas: aquí se trabaja sobre el índice, no sobre
versiones.

Lo que se gana es mantenimiento; lo que se paga es orden. Tener dos índices añadidos significa dos listas de
fuentes que se solapan, y el lector no avisa de duplicados: hay que revisarlo a mano de vez en cuando.

### Cuándo no vale la pena

Si el índice oficial te cubre y no has visto fuentes caídas, añadir este solo complica el estante. Su momento
llega cuando aparece el primer «esto antes funcionaba».
"""

GUIA["Swakshan/mangayomi-swak-extensions"] = """
### Para qué sirve

Otro índice comunitario de extensiones de Mangayomi, con selección propia: menos fuentes que los grandes y más
centrado en las que su autor usa. Sirve para cubrir huecos concretos.

### Cómo se usa

1. Se añade la dirección del índice en *Ajustes → Extensiones*.
2. Se revisa el listado antes de instalar: es corto y se lee de un vistazo.
3. Se instalan solo las fuentes que falten.

### Lo que conviene saber antes

54 estrellas, Apache-2.0, JavaScript, creado el 1 de mayo de 2025, con 7 bifurcaciones, 6 incidencias abiertas
y movimiento del 24 de octubre de 2026. Sin entregas: se sirve desde el índice.

El medidor marcó la bandera de aviso de retirada por una mención en el texto. Aquí la explicación es sencilla:
ese aviso se refiere a la forma de instalar la aplicación en algunos entornos, no al repositorio de extensiones.

### Cuándo no vale la pena

Si ya tienes dos índices añadidos, un tercero empieza a ser un problema de orden sin ganancia clara. Tiene
sentido cuando buscas una fuente concreta y sabes que está aquí.
"""

GUIA["Mallyd11/mangayomi-anime-extensions"] = """
### Para qué sirve

Índice de extensiones de **anime** para Mangayomi y también para AnymeX. Cubre la parte de vídeo, que en los
índices de esta aplicación suele ir aparte de la de manga y novela.

### Cómo se usa

1. Se añade la dirección del índice en la aplicación.
2. Se instalan las fuentes de vídeo que aparezcan, filtrando por subtitulado o doblaje.
3. En AnymeX se añade igual: el formato de los scripts es el mismo.

### Lo que conviene saber antes

28 estrellas, Apache-2.0, JavaScript, creado el 22 de abril de 2026, con 7 bifurcaciones y **0 incidencias
abiertas**, aunque sin empujón desde el 1 de noviembre de 2026. Es el más pequeño de los índices de este
programa que están vivos.

Su texto incluye una tabla de nombres, versiones y fechas que el medidor no puede leer sin descargarla; lo que
sí queda claro es cómo se instala. Con este tamaño, la pregunta correcta no es «¿cuántas fuentes tiene?» sino
«¿cuánto va a durar?».

### Cuándo no vale la pena

Si ves anime en otro reproductor, no aplica. Y si necesitas un catálogo amplio de fuentes, este no lo es:
es un complemento para huecos.
"""

GUIA["lnreader/lnreader-plugins"] = """
### Para qué sirve

Repositorio de plugins de LNReader, la aplicación de novelas ligeras y webnovelas. Es donde viven los
analizadores de los sitios de lectura por capítulos, y también donde se piden las fuentes nuevas: el propio
proyecto lo plantea como el sitio para incidencias y peticiones.

### Cómo se usa

1. Desde LNReader se añade la dirección del índice de plugins.
2. Se instalan los que interesen; aparecen como fuentes en el buscador.
3. Para pedir una fuente nueva, se abre una petición en este repositorio, no en el de la aplicación.
4. Para escribir un plugin, se clona, se instala con Node y se prueba contra el sitio.

### Lo que conviene saber antes

368 estrellas, MIT, TypeScript, creado en diciembre de 2020, con **434 bifurcaciones** y **563 incidencias
abiertas**: más peticiones que capacidad, y eso se nota en los tiempos de espera.

Hay un detalle que confunde a mucha gente: **la última entrega etiquetada es de marzo de 2024**, y sin embargo
el repositorio tiene movimiento de ayer. No hay contradicción: los plugins se sirven desde el índice del
repositorio, no desde las entregas. Mirar solo las entregas daría la impresión falsa de un proyecto parado.

### Cuándo no vale la pena

Si lees novela en un lector que no es LNReader, esto no te sirve. Y si esperas que tu petición se resuelva en
semanas, conviene saber que aquí hay 563 abiertas por delante de la tuya.
"""

GUIA["recloudstream/cloudstream"] = """
### Para qué sirve

Aplicación de Android para ver y descargar vídeo, con una arquitectura de extensiones muy abierta: el programa
no trae ninguna fuente y su propio texto lo avisa en la primera línea. Todo lo que se ve, se ve porque alguien
instaló una extensión.

### Cómo se usa

1. Se instala la APK de la entrega `v4.8.0`, del 10 de julio de 2026.
2. En *Ajustes → Extensiones* se añade la dirección de un índice de extensiones de Cloudstream.
3. Se instalan las fuentes y se busca el contenido.
4. Los capítulos se pueden descargar para verlos sin conexión.

### Lo que conviene saber antes

11.161 estrellas, GPL-3.0, Kotlin, creado en agosto de 2022, con 1.186 bifurcaciones, 566 incidencias abiertas
y movimiento de ayer. Se distribuye además como aplicación de escritorio en Windows y Linux.

Dos cosas que conviene tener claras. La primera, que **sin extensiones la app está vacía**: no es un fallo, es
el diseño. La segunda, que el medidor marca abandono declarado y aviso de retirada, y aquí sí hay que hacerle
caso al matiz: el texto del repositorio habla de la situación del proyecto, no de que se haya dejado de
mantener; los empujones son de hoy.

### Cuándo no vale la pena

Si buscas una app que funcione al instalarla, esta no: hay que montar el índice primero. Y en un televisor o un
móvil modesto, la reproducción depende del archivo, no del programa.
"""

GUIA["self-similarity/MegaRepo"] = """
### Para qué sirve

Índice de extensiones para Cloudstream. Es el que la mayoría de las guías del programa mencionan primero,
porque reúne una colección amplia de fuentes en un solo listado.

### Cómo se usa

1. Se abre Cloudstream y se entra en *Ajustes → Extensiones → Añadir repositorio*.
2. Se pega la dirección del índice.
3. Se instalan las fuentes que aparezcan; el listado se puede filtrar por idioma.
4. Si una fuente deja de funcionar, se desinstala y se espera una actualización del índice.

### Lo que conviene saber antes

142 estrellas y **sin licencia declarada**, con 23 bifurcaciones, una sola incidencia abierta y **último empujón
el 3 de octubre de 2025**: más de un año sin movimiento. Kotlin como lenguaje, y ninguna entrega etiquetada.

Ese año de silencio es el dato que manda. Un índice de extensiones no se rompe de golpe: se va apagando fuente
a fuente, sin avisos, y el usuario lo descubre cuando abre un capítulo y no carga. Si se usa hoy, hay que
contar con eso.

### Cuándo no vale la pena

Para alguien que empieza, tiene sentido como primera parada. Pero si vas a montar esto para usarlo de verdad,
conviene tener a mano otros índices de Cloudstream, porque este no se está actualizando.
"""

GUIA["salmanbappi/extensions-repo"] = """
### Para qué sirve

Índice de extensiones de anime dedicado a Anikku, un reproductor derivado de la familia Aniyomi. Reúne las
fuentes que ese programa necesita y que no están en los índices generales.

### Cómo se usa

1. En Anikku se abre *Ajustes → Explorar → Repositorios de extensiones*.
2. Se añade la dirección del índice y se pega.
3. Se vuelve a la pestaña de extensiones para buscar, instalar y actualizar las fuentes.
4. El propio repositorio incluye una guía de montaje en forma de diagrama para ese camino.

### Lo que conviene saber antes

52 estrellas y **sin licencia declarada**, creado el 24 de diciembre de 2025, con 3 bifurcaciones, **14
incidencias abiertas** y movimiento de ayer. HTML como lenguaje: es un índice, no un programa.

Tiene una proporción poco habitual —14 incidencias para 52 estrellas— y eso suele querer decir que la gente lo
usa y reporta. También quiere decir que hay cosas pendientes. Con un solo mantenedor visible, el ritmo de
arreglo es el que es.

### Cuándo no vale la pena

Si tu reproductor no es Anikku ni de su familia, no sirve. Y si ya tienes un índice que cubre el mismo
contenido, dos listas solapadas solo dan trabajo de limpieza.
"""

GUIA["LittleSurvival/copymanga-copy20"] = """
### Para qué sirve

Repositorio de fuentes en chino para Mihon, Tachiyomi y Suwayomi: cubre varios sitios de lectura en chino —
entre ellos los que da el nombre— y está escrito directamente en Smali, sin código fuente en Kotlin detrás.

### Cómo se usa

1. Se añade la dirección del índice en el lector, o se descarga el paquete de la entrega `hipmh-v1.4.1`, del
   11 de octubre de 2026.
2. Se instala como cualquier extensión.
3. En Suwayomi, que corre en un servidor, se añade igual y sirve a todos los dispositivos conectados.

### Lo que conviene saber antes

2.994 estrellas y **sin licencia declarada**. 19 bifurcaciones, 14 incidencias abiertas y movimiento del 11 de
octubre de 2026. El desequilibrio entre estrellas y bifurcaciones es la pista: mucha gente lo usa, casi nadie
lo toca.

Que esté escrito en Smali significa que **no hay código legible que revisar ni arreglar**: si una fuente se
rompe, se espera a que el autor publique otra versión. Y sin licencia declarada, nadie puede continuarlo
legalmente si el autor desaparece.

### Cuándo no vale la pena

Si no lees en chino, no hay nada aquí para ti. Y si te importa poder arreglar lo que uses, un paquete sin
código fuente es la peor base posible.
"""

GUIA["Hotaro26/miko"] = """
### Para qué sirve

Lector de manga para Android construido enteramente con Kotlin y Jetpack Compose, con interfaz Material 3 Expressive y un catálogo en línea de manga. Está pensado para navegar y leer manga desde fuentes externas; el programa no trae contenido propio.

### Cómo se usa

1. Se instala la APK de la entrega `v3.3`, del 3 de agosto de 2026.
2. Se abre el lector y se añade el catálogo de manga que se quiera consultar.
3. Se busca el título y se lee en línea o se descarga para leer sin conexión, según lo que permita la fuente.

### Lo que conviene saber antes

34 estrellas y **sin licencia declarada**. Creado el 26 de abril de 2026, con un empujón del 11 de septiembre de 2026: cinco meses sin movimiento en el repositorio. GitHub no reconoce ninguna licencia, así que no está claro qué se puede reutilizar del código.

Sin entrega reciente desde agosto, el proyecto está quieto. Un lector sin empujones recientes puede seguir funcionando, pero si una fuente deja de funcionar, puede que nadie la arregle.

### Cuándo no vale la pena

Si buscas un lector que reciba actualizaciones frecuentes, este no da esa garantía. Y si no quieres agregar catálogos tú mismo, al instalarlo no encontrarás nada que leer.
"""

GUIA["Hynf5/Hitori"] = """
### Para qué sirve

Fork de Kotatsu-Redo: lector de manga para Android. Hereda la estructura del lector que se archivó en 2025 y la continúa con otro nombre, manteniendo el enfoque de biblioteca local y lecturas descargadas.

### Cómo se usa

1. Se instala la APK de la entrega `v9.2.5`, del 26 de octubre de 2026.
2. Se configuran las fuentes de manga que se quieran leer.
3. Se descargan los capítulos para leer sin conexión y se organiza la biblioteca local.

### Lo que conviene saber antes

16 estrellas, GPL-3.0, creado el 16 de diciembre de 2025, con un empujón del 26 de octubre de 2026. Es un proyecto pequeño: una bifurcación y cero incidencias abiertas.

Al ser un fork de Kotatsu-Redo, comparte su lógica de extensiones y su forma de organizar la biblioteca. El medidor no detectó abandono declarado: tiene movimiento reciente.

### Cuándo no vale la pena

Si ya usas otro lector de la familia Kotatsu con tu biblioteca montada, cambiar solo por el nombre no aporta nada. Y si necesitas muchas fuentes ya integradas, este es pequeño y las tendrás que añadir tú.
"""

GUIA["Noirero/Miyorare"] = """
### Para qué sirve

Fork de DropSauce basado en Kotatsu: lector de cómics y novelas para Android. Se presenta como una versión ajustada al gusto de su autor, con descargas rápidas y una interfaz que no es plana. Trabaja con extensiones y fuentes que el usuario añade.

### Cómo se usa

1. Se instala la APK de la entrega `v1.4.19`, del 5 de noviembre de 2026.
2. Se añaden las fuentes de manga y novela que se quieran leer.
3. Se descarga para leer sin conexión y se organiza la biblioteca.

### Lo que conviene saber antes

21 estrellas, GPL-3.0, creado el 4 de septiembre de 2026, con un empujón de hoy mismo (5 de noviembre de 2026). Es un proyecto joven, dos meses de vida, con entrega publicada esta semana.

Viene de DropSauce y de Kotatsu, así que hereda su ecosistema de extensiones y su forma de manejar la biblioteca. Con solo dos meses, no hay historial largo que avale que siga recibiendo actualizaciones dentro de seis meses.

### Cuándo no vale la pena

Si ya usas DropSauce y te funciona, cambiar a este fork solo tiene sentido si te interesa su interfaz específica. Y si buscas un lector con años de trayectoria, este todavía no la tiene.
"""

GUIA["Torro101/MIYO"] = """
### Para qué sirve

Lector de manga para Android. Su repositorio no trae descripción, así que lo que se sabe de él viene de su código y de sus entregas: es un lector con APKs publicados.

### Cómo se usa

1. Se instala la APK de la entrega `v0.0.5-1`, del 15 de junio de 2026, con tres adjuntos.
2. Se abre el lector y se configuran las fuentes de manga que se quieran leer.
3. Se lee y se descarga para usar sin conexión.

### Lo que conviene saber antes

10 estrellas, GPL-3.0, creado el 27 de abril de 2026, con un empujón del 26 de octubre de 2026. Sin descripción en el repositorio y sin incidencias abiertas. El medidor no pudo extraer una descripción clara de qué hace ni de qué fuentes usa.

Con cero bifurcaciones y ninguna incidencia, es un proyecto de una sola persona que no ha llamado la atención. Eso no significa que no funcione, pero tampoco hay evidencia de que lo haga bien.

### Cuándo no vale la pena

Si buscas un lector con comunidad detrás, respuestas a incidencias y documentación clara, este no la tiene todavía. Y sin descripción, instalarlo es comprar a ciegas.
"""

GUIA["TsukiAndroid/Tsuki"] = """
### Para qué sirve

Lector de manga y novelas ligeras para Android con más de mil doscientas fuentes integradas, detección automática de analizadores y soporte desde Android 6. Se presenta como un lector que «lee de todo»: manga, novelas ligeras y cómics, con un motor de extensiones que reconoce las fuentes por sí solo.

### Cómo se usa

1. Se instala la APK de la entrega `alpha-latest`, del 2 de noviembre de 2026, con cuatro adjuntos.
2. Al abrirlo, el lector detecta las fuentes disponibles y las propone para añadir.
3. Se eligen las fuentes que se quieren leer y se navega por el catálogo de cada una.
4. Se descargan capítulos para leer sin conexión.

### Lo que conviene saber antes

40 estrellas, GPL-3.0, creado el 29 de abril de 2026, con un empujón del 2 de noviembre de 2026. Tiene una bifurcación y una incidencia abierta. Publica tres canales de entrega: estable, beta y alpha, todos con fecha de hace días.

Es un lector joven (menos de un año de vida) pero con movimiento reciente y muchas fuentes declaradas. Como todo lector joven, el riesgo es que una fuente deje de funcionar y nadie la arregle a tiempo.

### Cuándo no vale la pena

Si buscas un lector con años de historial y miles de usuarios detrás, este todavía no los tiene. Y si ya usas otro lector de la familia con tu biblioteca montada, cambiar solo por el número de fuentes no aporta nada.
"""

GUIA["salmanbappi/Tsukimi"] = """
### Para qué sirve

Lector de manga de alto rendimiento para Android, con muchas funciones y enfoque en lecturas rápidas. Es una aplicación de una sola persona que lleva meses sin actualizar, pero que sigue publicada con entregas desde marzo de 2026.

### Cómo se usa

1. Se instala la APK de la entrega `v3.0.109`, del 31 de marzo de 2026, con cinco adjuntos.
2. Se abre el lector y se configuran las fuentes de manga que se quieran leer.
3. Se lee y se descarga para usar sin conexión.

### Lo que conviene saber antes

49 estrellas, GPL-3.0, creado el 29 de enero de 2026, con un empujón del 5 de septiembre de 2026. **Más de medio año sin movimiento en el repositorio**: desde septiembre de 2026 no hay un solo empujón. Tiene una bifurcación y dos incidencias abiertas.

La última entrega es de marzo de 2026, y el código no se toca desde septiembre. Eso significa que el lector puede seguir funcionando, pero si una fuente deja de funcionar o Android cambia algo que rompe la app, puede que nadie lo arregle.

### Cuándo no vale la pena

Si buscas un lector que reciba actualizaciones frecuentes, este no las da: lleva más de seis meses sin moverse. Y si te importa que haya alguien detrás que responda incidencias, este tiene solo dos abiertas y un solo mantenedor visible.
"""

def main() -> int:
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    escritas = 0
    for repo, texto in GUIA.items():
        f = medido.get(repo)
        if not f or f.get("racimo") != RACIMO:
            print("  ! sin medir en el racimo:", repo)
            continue
        p = CATALOGO / repo.replace("/", "--").lower() / "FICHA.md"
        if not p.exists():
            print("  ! sin ficha:", repo)
            continue
        t = p.read_text(encoding="utf-8")
        if INICIO not in t or FIN not in t:
            print("  ! sin marcadores:", repo)
            continue
        nuevo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN),
                       INICIO + "\n" + texto.strip() + "\n" + FIN, t, flags=re.S)
        if nuevo != t:
            p.write_text(nuevo, encoding="utf-8")
            escritas += 1
    print(f"guías escritas: {escritas} de {len(GUIA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
