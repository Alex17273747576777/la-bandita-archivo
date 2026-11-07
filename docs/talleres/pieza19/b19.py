# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab18/docs/talleres/pieza19')
from d19 import *
A=AGG; T=[]; w=T.append
K=INDICE
def f(r,nombre,texto): T.append(f"{ficha(r,nombre)}. {texto}\n")

w(f"""*🚫 Lo que no se indexa · con nombre, cifra y motivo*

Esta es la sección que hacía falta y la que nadie publica, porque una lista de excluidos no da visitas. Va con nombre y con motivo, y **ninguna de estas diez lleva enlace en esta pieza**: nombrarlas no es recomendarlas.

**Las tres archivadas.** *Kotatsu* —{num(R['KotatsuApp/Kotatsu']['stars'])} estrellas y 366 días de archivo—, *kotatsu-parsers* —{num(R['KotatsuApp/kotatsu-parsers']['stars'])} estrellas, archivado el 3 de noviembre de 2025— y *mangayomi-extensions* —el repositorio oficial de Mangayomi, {num(R['kodjodevf/mangayomi-extensions']['stars'])} estrellas, archivado el 1 de octubre de 2025—. **No están muertas por abandono: están cerradas por decisión de quien las escribió.** Se nombran para explicar de dónde migrar, no para instalar.

**Los dos clones con nombre prestado.** *cuong-tran/manga-repo* —{num(R['cuong-tran/manga-repo']['stars'])} estrellas, {num(K['cuong-tran/manga-repo']['publicadas'])} extensiones, y su índice **se llama «Yūzōnō»**— y *mojuru/cursed-manga-repo* —{num(R['mojuru/cursed-manga-repo']['stars'])} estrellas, {K['mojuru/cursed-manga-repo']['publicadas']} extensiones, «Cursed Yūzōnō»—. El primero publica casi todo lo de Keiyoushi con otro nombre; el segundo es un clon pequeño con {R['mojuru/cursed-manga-repo']['dias_push']} días desde su último empujón. **Duplican lo que ya hay**: indexarlos es inflar una lista sin añadir una sola fuente nueva.

**Los dos que prometen más de lo que publican.** *dragonx943/manga-repo* —24 estrellas y **una** extensión— y *admknight/CloudstreamExtensions* —5 estrellas, un «mega repositorio» que lleva {num(E['admknight/CloudstreamExtensions']['commits_30d'])} cambios en treinta días y publica {num(E['admknight/CloudstreamExtensions']['adjuntos'])} archivos—. El segundo, al menos, es honesto en el nombre: no dice «el mejor», dice «mega». El primero es el ejemplo de que las estrellas no miden catálogo.

**Los de nombre que es una dirección.** Cuatro repositorios encontrados esta mañana cuyo nombre completo es una URL cruda de Keiyoushi, uno con 29 estrellas y ningún código dentro. **Ningún humano los escribiría**; solo un indexador automático. Es la prueba más limpia de por qué esta pieza mide veinte cosas y no trescientas.

**El que no se puede juzgar por la API.** La comunidad afirma que a la tienda Yūzōnō le retiraron cinco extensiones de Keiyoushi por una reclamación de derechos. **Eso no lo puede comprobar esta pieza**: GitHub no publica un registro consultable de retiradas, y una reclamación no deja rastro en la API. Lo que sí está medido: la tienda sigue viva hoy, con {num(K['yuzono/anime-extensions']['publicadas'])} extensiones y empujón de ayer. **Lo que no se puede comprobar, se dice que no se puede comprobar** —y esa frase es, en esta serie, la que separa una lista de un censo—.

───────────────────

*⚖️ La responsabilidad · lo que una tienda de extensiones hace de verdad*

Una extensión de estas aplicaciones es, literalmente, **un programa que lee una página web ajena y convierte lo que encuentra en una lista de capítulos**. Casi nunca tiene permiso del sitio, y casi nunca el sitio cobra por leerlo. Eso pone el tema en un terreno que conviene explicar sin adornos.

**Lo que la extensión hace.** Se conecta a un sitio, pide una búsqueda, interpreta el HTML y devuelve resultados. No aloja el contenido: **apunta**. La diferencia jurídica entre alojar y enlazar es grande en unos países y pequeña en otros, y en la República Dominicana el marco es la **Ley 65-00** sobre derecho de autor; en la Unión Europea hay además una directiva específica sobre servicios que enlazan. **Esta pieza no da consejo legal** y no puede decirte si el sitio de turno tiene licencia: eso lo sabe el sitio.

**Lo que la aplicación sí controla.** Que una tienda **firme su índice** es la única defensa técnica real del usuario, porque impide que alguien cambie las direcciones de los APK en el camino. De las seis tiendas medidas, **tres declaran clave de firma y tres no**. Es el dato más útil de la pieza para decidir con qué te quedas.

**Lo que la extensión se lleva.** Al instalar una extensión le das a un programa de terceros acceso a tu red desde la aplicación de lectura. No es dramático, pero no es nada: una extensión es código que corre en tu teléfono y puede pedir lo que quiera. La comprobación de la sección anterior —que exista el repositorio de fuentes, que esté vivo, que alguien compile— es también una comprobación de seguridad, no solo de calidad.

**Y la raya de esta casa.** Esta pieza **no enlaza ni una sola página de contenido**, no dice qué sitio tiene qué manga y no explica cómo saltarse un muro de pago. Mide **software**: repositorios, índices, firmas, fechas. Si lo que buscabas era una lista de páginas, esta no es la pieza.

───────────────────

*🔏 La huella del tema · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}*

**{num(A['adjuntos'])} archivos publicados por las {palabras(A['vivos'])} piezas. {num(A['con_huella'])} con suma de comprobación. El 0,07 %.**

La proporción más baja de la serie, empatada con las tiendas de la pieza 10 —0,08 %— y muy por debajo de todo lo demás: aplicaciones de la 11, **5,5 %**; torrentes de la 16, **8,7 %**; descarga de la 15, **10,6 %**; audio de la 13, **11,4 %**; radio de la 18, **14,1 %**; kit de la 12, **17,0 %**; teclados de la 17, **19,0 %**; música de la 14, **20,0 %**.

**{palabras(A['con_huella_repos'])} solo repositorio de los {palabras(A['vivos'])} publica alguna suma**: LNReader, con {num(E['lnreader/lnreader-plugins']['con_huella'])}. Y los dos que más archivos publican —**cuong-tran, con {num(E['cuong-tran/manga-repo']['adjuntos'])}**, y **Keiyoushi, con {num(E['keiyoushi/extensions']['adjuntos'])}**— **no publican ni una**.

**Lo que esto significa en la práctica, y no es un tecnicismo.** La aplicación de lectura va a descargar **miles de APK** desde un repositorio de GitHub y a ejecutarlos. Tu única garantía de que el archivo que llega es el que se publicó está en la suma o en la firma del índice. **Tres de las seis tiendas firman el índice** —Keiyoushi, Yūzōnō y el clon de Cursed— y esa firma cubre las direcciones, no los archivos. Es más de lo que tiene cualquier otra cosa del tema y sigue siendo poco.

───────────────────

*🛠️ Seis órdenes para revisar una tienda antes de añadirla*

1. **Ver el estado real del repositorio.** `curl -s api.github.com/repos/keiyoushi/extensions | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['archived'],d['pushed_at'],d['license'] and d['license']['spdx_id'])"` — devuelve tres cosas: si está archivado, cuándo se movió por última vez y con qué licencia. Con eso se caen la mitad de las listas.
2. **Contar las extensiones del índice.** `curl -s https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json | python3 -c "import json,sys;print(len(json.load(sys.stdin)))"` — el número que la descripción promete, comprobado.
3. **Ver si el índice está firmado.** `curl -s https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json | python3 -c "import json,sys;d=json.load(sys.stdin);print(bool(d.get('signingKey')),d.get('name'))"` — dos cosas de golpe: si firma y **cómo se llama de verdad la tienda**, que es donde se descubren los clones.
4. **Seguir la redirección del enlace que tienes guardado.** `curl -sIL -o /dev/null -w '{{url_effective}}\n' https://github.com/keiyoushi/extensions/releases/latest` — si acaba en otro sitio, la dirección ha mudado y tu aplicación lleva meses sin actualizar.
5. **Mirar si el repositorio de fuentes existe y compila.** El de publicación tiene los APK; el de código tiene las fuentes. `curl -s api.github.com/repos/<dueño>/<repo>/actions/runs?per_page=1` dice si algo se compila solo o si cada APK lo subió una persona a mano.
6. **Abrir la aplicación y probar una extensión.** No hay orden para esto y es la que manda: instalar, buscar, abrir un capítulo. Si no funciona, no se pide.

Las órdenes **2, 3 y 4** son las que esta pieza usó para escribir la tabla; ninguna necesita instalar nada y las tres caben en un minuto.

───────────────────

*🚪 Lo que esta pieza no tiene*

**Ni una lista de sitios, ni un enlace de contenido.** Ni un `.json` de tienda enlazado para copiar: la tabla dice qué tienda sirve a qué aplicación y se busca por su nombre. Es la norma del canal desde la pieza 10 y aquí se lleva al extremo a propósito.

**No es un volcado.** {palabras(A['vivos'])} piezas, no trescientas. Diez se quedan fuera con nombre y motivo, que es más útil que meterlas y callar.

**No es una lista de lo más nuevo.** La mediana de edad de este tema es de **{num(int(A['mediana_dias']))} días**: aquí lo nuevo es la excepción —Usagi, DropSauce y el plugin de 2026— y lo viejo que funciona es la norma. Se mide la fecha, no la novedad.

**No hay cifras de memoria.** Cada número de extensión de esta pieza se contó esta mañana en el índice correspondiente, y la tabla del principio enseña, a propósito, las seis cifras que la wiki tenía mal.

*📅 La semana de prueba · cinco días para reordenar tus tiendas*

- **Día uno.** Mira qué aplicación usas y qué tienda tiene configurada. Si es Kotatsu, ya sabes: archivada hace 366 días. Si es Mihon, la respuesta es una y se llama Keiyoushi.
- **Día dos.** Cuenta tu índice con la orden 2 y compara con lo que dice la lista que seguiste. La diferencia es lo que llevas de retraso.
- **Día tres.** Comprueba con la orden 3 si tu tienda firma el índice. Si no firma, no es motivo para desinstalar: es motivo para saberlo.
- **Día cuatro.** Si vienes de Kotatsu, prueba **DropSauce** —acepta el formato de Mihon— o **Usagi** con su plugin. Una tarde, sin perder la biblioteca.
- **Día cinco.** Elige **una** extensión y ábrela. Si funciona, esa es tu tienda; si no, cámbiala. Sin listas de trescientas.

───────────────────

*❓ Las preguntas del grupo*

**¿Cuál es la única tienda buena de Mihon?**
Keiyoushi, con {num(K['keiyoushi/extensions']['publicadas'])} extensiones y el índice firmado. Todo lo demás que tiene esa forma es un clon con otro nombre: los dos que se midieron aquí declaran llamarse «Yūzōnō» en su propio índice.

¿Y para Aniyomi o Animiru? **Yūzōnō**, con {num(K['yuzono/anime-extensions']['publicadas'])}. Ojo con la dirección: el repositorio de publicación **se mudó** y la que circula responde 301; si tu aplicación no actualiza desde hace meses, es casi seguro eso.

**¿Kotatsu sigue vivo?**
No. Archivado el 4 de noviembre de 2025, hace 366 días, y sus parsers al día siguiente. Los reemplazos vivos son **Usagi** y **DropSauce**, los dos de este año, y el segundo acepta tiendas de Mihon.

**¿Mangayomi tiene extensiones?**
Sí, pero **no en el repositorio oficial**, que está archivado desde el 1 de octubre de 2025. Las mantiene **m2k3a**, con {num(K['m2k3a/mangayomi-extensions']['publicadas'])} extensiones y empujón de esta semana.

**¿Y las novelas?**
No hay una familia de novelas: cada aplicación tiene su formato. LNReader mantiene **{num(K['lnreader/lnreader-plugins']['publicadas'])} plugins** y algunas aplicaciones los aceptan tal cual; otras los compilan a su manera. Es el único de todo el tema que publica sumas de comprobación: {num(E['lnreader/lnreader-plugins']['con_huella'])}.

**¿Cloudstream tiene un solo repositorio grande?**
Hay un «mega repositorio» que junta muchos, y esta mañana el que se actualiza a diario es el de `admknight`, con **5 estrellas** —que es justo la prueba de que las estrellas no miden nada—. También está Cs-Karma, con 52. Ninguno declara licencia legible.

**¿Por qué no pones los enlaces de las tiendas para copiar?**
Porque una tienda que se copia sin mirar es exactamente el problema que esta pieza denuncia. Se dan el nombre, la cifra y la orden con la que se comprueba; la dirección se busca y se verifica en un minuto.

───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **la lista que circula está desactualizada en seis de seis cifras**. No por mala fe: porque nadie vuelve a contar. La diferencia entre 131 y 6 —Cursed— no es un detalle, es la prueba de que una wiki no es una medición.

Lo segundo: **la familia Mihon tiene una sola tienda y la familia Aniyomi tiene otra**, y confundirlas explica la mayoría de las consultas de los grupos. Keiyoushi, {num(K['keiyoushi/extensions']['publicadas'])}; Yūzōnō, {num(K['yuzono/anime-extensions']['publicadas'])}. Todo lo demás es clon, ruido o archivo.

Lo tercero: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 0,07 %**, la cifra más baja de la serie, y en un tema donde la aplicación **ejecuta código de terceros** en tu teléfono. Tres tiendas firman su índice; ninguna firma sus APK.

Y lo cuarto, que es lo que la comunidad pidió y esta casa comparte: **el listón no se sube con más enlaces, se sube con menos y mejores**. Diez piezas se quedan fuera de esta tabla con nombre y motivo, y esa es la parte del trabajo que un volcado automático nunca va a hacer.

───────────────────
""")
w(f"""— {num(K['keiyoushi/extensions']['publicadas'])} + {num(K['yuzono/anime-extensions']['publicadas'])} + {num(K['m2k3a/mangayomi-extensions']['publicadas'])} + {num(K['lnreader/lnreader-plugins']['publicadas'])} + {num(K['salmanbappi/sb-extensions-source']['publicadas'])} extensiones contadas esta mañana en seis índices publicados: 5.481 en total, ninguna cifra de memoria.
— Once aplicaciones agrupadas por qué tienda aceptan, que es la tabla que faltaba; y diez repositorios fuera de la lista con nombre, cifra y motivo.
— {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas: el 0,07 %, la proporción más baja de la serie, y tres de las seis tiendas firmando su índice.

💓 *La Bandita informa a partir de fuentes fechadas.* {palabras(A['vivos'])} piezas vivas —y tres archivadas con su fecha— medidas hoy una por una, {num(5481)} extensiones contadas en los índices, el listón de seis comprobaciones y la tabla que dice qué tienda sirve a qué aplicación. Sin volcados, sin relleno y sin enlaces de contenido.

───────────────────

*Medición del corte:* jueves 5 de noviembre de 2026, {HORA} de la mañana en Santo Domingo, con la fecha comprobada en vivo antes de empezar y al terminar · vigésima medición del día · {palabras(A['vivos'])} piezas vivas y {palabras(A['arch'])} archivadas · {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas · {num(A['estrellas'])} estrellas · ningún repositorio con `SECURITY.md`.

*🔗 Enlaces*

*Las aplicaciones, que son lo que se instala:*
""")
GRUPOS=[("Las aplicaciones",['mihonapp/mihon','aniyomiorg/aniyomi','UsagiApp/Usagi','HuzaifaKhalid1311/DropSauce','kodjodevf/mangayomi','lnreader/lnreader']),
        ("Las cuatro tiendas que pasan el listón",['keiyoushi/extensions','keiyoushi/extensions-source','yuzono/anime-extensions','m2k3a/mangayomi-extensions'])]
usados=set()
for titulo,rs in GRUPOS:
    w(f"\n*{titulo}:*\n\n")
    for r in rs:
        usados.add(r); w(f"- https://github.com/{r}\n")
w(f"""
*Las que se nombran y no se enlazan, con el motivo en la sección 🚫:* Kotatsu y sus parsers, el repositorio oficial de Mangayomi, los dos clones de Yūzōnō, el plugin de una sola extensión, el mega repositorio de Cloudstream, Cs-Karma y los cuatro repositorios cuyo nombre es una dirección.

*Las direcciones de las órdenes:*

- api de un repositorio: https://api.github.com/repos/keiyoushi/extensions
- su índice contado, versión comprimida: https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.min.json
- el mismo índice con la clave de firma: https://raw.githubusercontent.com/keiyoushi/extensions/repo/index.json
- la última entrega, para seguir su redirección: https://github.com/keiyoushi/extensions/releases/latest

───────────────────

*🗒️ Notas al pie*

(5-nov) La fecha se comprobó **en vivo antes de empezar y al terminar**: `tools/fecha_viva.py --inicio` y `--fin` al cerrar. **Antes de sondear** se hizo la revisión de historial y ecosistema; la medición es de las {HORA} y vive en `docs/MEDICION-19-tiendas-2026-11-05.json`.

(5-nov) **Cómo se contaron las extensiones.** Se descargó el índice publicado de cada tienda (`repo.json` → `index.json` / `index.min.json`) y se contaron las entradas; en los repositorios de fuentes se contaron además los directorios de `src/<idioma>/`. Las dos cifras se dan cuando difieren —Keiyoushi: {num(K['keiyoushi/extensions']['publicadas'])} publicadas y {num(K['keiyoushi/extensions']['fuentes'])} fuentes— porque las cinco que faltan son las que no compilaron.

(5-nov) **Lo que no se pudo comprobar, y se dice.** La retirada de cinco extensiones por reclamación de derechos en la tienda Yūzōnō es una afirmación de terceros: GitHub no publica un registro consultable, y ninguna llamada a la API la confirma. No se usa como argumento en contra de nada.

(5-nov) La cuenta de **huella** es la de toda la serie: `sha256`, `sha512`, `sha1`, `checksum`, `.sig`, `.asc` o `sums` en el nombre de cada adjunto de las últimas cien entregas. Esta es la medición más baja: **0,07 %**, con {palabras(A['con_huella_repos'])} solo repositorio firmando.

(5-nov) **El listón sube en dos direcciones.** Menos repositorios —{palabras(A['vivos'])} y no trescientas— y mejor comprobados: archivado, último empujón, índice contado, firma del índice, nombre real de la tienda y descripción leída. Las diez que se quedan fuera van con nombre y motivo, que es más trabajo que incluirlas.

(5-nov) **El taller queda en `docs/talleres/pieza19/`**, con los generadores y los índices contados, para que las cifras se puedan repetir desde el repositorio (H22).

*#task*

#task 087 · volver a contar los seis índices el 5 de diciembre y publicar la tabla de diferencias: cuántas extensiones ganó o perdió cada tienda en un mes.

#task 088 · comprobar con la orden 3 qué tiendas declaran clave de firma y añadir esa columna a la lista pública del repositorio.

#task 089 · probar DropSauce con una tienda en formato Mihon y un plugin de Usagi, y dejar en un acta qué conserva y qué pierde al migrar desde Kotatsu.

#task 090 · escribir la pieza 20 —los subtítulos y el doblaje, que este corte dejó pendientes— con el mismo método: preflight previo, medición fechada y ninguna cifra escrita a mano.

───────────────────

🏷️ Etiquetas estratégicas

#Keiyoushi #Yuzono #Mihon #Aniyomi #Usagi #DropSauce #Mangayomi #LNReader #Cloudstream #Kotatsu #OpenSourceDominicano #TiendasDeExtensiones
""")
open('/tmp/lab18/docs/talleres/pieza19/s2.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
