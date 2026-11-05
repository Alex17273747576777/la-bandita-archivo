# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab16/docs/talleres/pieza16')
from d16 import *
A=AGG; T=[]; w=T.append

w(f"""*🧠 Cómo funciona, en cinco pasos y sin tecnicismos*

Esta sección no la pide la lista, la pide el tema. Si no se entiende el mecanismo, todo lo demás —las sumas, los clientes, la proporción— suena a jerga. Y el mecanismo es sencillo: **es una cadena de favores entre desconocidos, con una lista de la compra**.

**Primer paso: alguien hace la lista.** El archivo original se parte en trozos de tamaño fijo —de 16 kB a 16 MB, según cómo se hizo— y a cada trozo se le calcula una huella. Con todas las huellas y los nombres sale un archivo pequeño, el `.torrent`, que **no contiene el archivo**: contiene la lista y las huellas. Ese archivo se puede enviar por correo; pesa kilobytes.

**Segundo paso: alguien reparte la lista.** Para que los interesados la encuentren hay dos caminos. El clásico es un **anunciador** —el *tracker*— al que cada cliente le dice «estoy aquí y tengo estos trozos»; el moderno es la **DHT**, una tabla distribuida donde los propios clientes se buscan entre sí sin servidor. Ese cambio —del anunciador a la DHT— es lo que hizo que el protocolo sobreviviera a la desaparición de los grandes índices, y es lo que explica que {palabras(A['vivos'])} piezas sigan funcionando hoy aunque el servicio que las anunciaba cerró en 2013.

**Tercer paso: alguien pide trozos.** Cuando abres la lista, tu cliente pregunta a los demás quién tiene qué trozo y empieza a pedirlos. Los trozos llegan de veinte personas distintas a la vez, cada una desde su casa. Tú no bajas un archivo de un servidor: bajas **pedazos de archivo de gente que también lo está bajando**.

**Cuarto paso: cada trozo se comprueba solo.** Esta es la parte buena. Al llegar un trozo, el cliente calcula su huella y la compara con la de la lista. Si no coincide, pide ese trozo a otro. **Nadie tiene que firmar nada para que el protocolo funcione**: la verificación está dentro del diseño. Por eso, cuando en esta pieza se dice que 15 de 22 no publican sumas, no significa que sus descargas lleguen corruptas —el protocolo ya lo evita—, sino que **no puedes comprobar el instalador del programa** antes de ejecutarlo.

**Quinto paso: los trozos que ya tienes se reparten.** En cuanto tienes un trozo, lo ofreces. El cliente no distingue entre bajarte a ti o subirte a ti: mientras está abierto, reparte. Eso es la **siembra**, y la cifra que la mide es la **proporción** —lo subido entre lo bajado—. Todo el sistema se sostiene en que la mayoría deje la ventana abierta un rato después de terminar.

**Y aquí está el nudo de todo lo demás.** Los cinco pasos son neutrales: describen un mecanismo de reparto de datos, igual de válido para una imagen de Linux que para una obra con derechos. **Lo que no es neutral es el paso quinto**, porque repartir es la conducta por defecto. La sección de responsabilidad, más abajo, va justo de eso.

**Qué cambió en veinte años, y qué no.** Cambió el anuncio —del servidor a la DHT—, cambió el enlace —del `.torrent` al *magnet*, que es la lista resumida en una línea de texto— y cambió el cliente: de una ventana pesada a una consola en el teléfono. **No cambió el fondo**: trozos, huellas, pares. Un cliente de 2005 y **piko**, con {R['NihilDigit/piko']['dias_nace']} días, hablan el mismo idioma y se entienden entre sí. Encontrar un protocolo de veinte años que un proyecto nuevo pueda implementar en un mes es exactamente lo que se está viendo en la camada de 2026.

───────────────────

*📊 La tabla completa de las {palabras(A['vivos'])} · lo medido, fila por fila*

Las secciones anteriores cuentan lo que importa; esta deja el registro entero. Se ordena por nota, y la columna de sumas es la que más se repite en toda la pieza.

| # | Recurso | Nota | ★ | Último empujón | Entregas | Sumas / adjuntos |
|---|---|---|---|---|---|---|
""")
for i,r in enumerate(sorted(VIVOS,key=lambda x:(-E[x]['puntos'],x)),1):
    e=E[r]; ea=R[r]
    w(f"| {i} | {r} | **{e['puntos']}** | {num(ea['stars'])} | {cuando(r).replace('**','')} | {num(ea['entregas'])} | {num(e['con_huella'])} / {num(e['adjuntos'])} |\n")
w(f"""
Leída en vertical, la columna de sumas dice lo que ninguna lista de recomendaciones dice: **{palabras(A['con_huella_repos'])} de {palabras(A['vivos'])} publican alguna**, y la mitad de las sumas del tema las pone un solo programa. Leída en horizontal, la tabla deja ver los extremos: **autobrr** arriba con **{E['autobrr/autobrr']['puntos']}** y **torrent-tui** abajo con **{E['ryadios/torrent-tui']['puntos']}**, y entre ellos todo lo demás.

**Lo que la tabla no mide**, y conviene decirlo: si el programa es agradable de usar, si traga bien un enjambre de cien mil pares o si se rompe al llenar el disco. Ninguna de esas cosas se ve desde la API de GitHub. Por eso la pieza da la vara y la fecha, y la semana de prueba da el resto.

───────────────────

*🎓 Glosario mínimo · doce palabras para no perderse*

- **Semilla** (*seed*): quien tiene el archivo entero y lo reparte. Un enjambre sin semillas es un enjambre muerto, y por eso importa tanto la proporción.
- **Par** (*peer*): cualquiera que está en la descarga, con el archivo completo o a medias. Cada par es a la vez cliente y servidor.
- **Enjambre** (*swarm*): el conjunto de pares y semillas de un mismo archivo. No hay centro: si se cae uno, no pasa nada.
- **Trozo** (*piece*): una rebanada del archivo, con su huella. Es la unidad que se pide, se verifica y se reparte.
- **`.torrent`**: la lista de trozos y huellas. **No contiene el archivo.**
- **Magnet**: la misma lista resumida en una línea de texto, sin archivo que enviar. Se impuso cuando los índices empezaron a caer.
- **DHT**: la tabla distribuida que permite encontrar pares sin anunciador. Es lo que hace el protocolo difícil de apagar.
- **Anunciador** (*tracker*): el servidor clásico que ponía en contacto a los pares. Hoy es opcional.
- **Proporción** (*ratio*): lo subido dividido entre lo bajado. Es la moneda del sistema.
- **Siembra** (*seeding*): seguir repartiendo después de terminar. El paso que sostiene todo y el que tiene consecuencias legales.
- **Cliente**: el programa que habla el protocolo. Lo que mide esta pieza.
- **Indexador**: el sitio o programa que busca listas. **No aparece en esta pieza**, ni con enlace ni como recomendación: es la familia que el canal veta (H20).

**Una advertencia sobre las palabras.** «Torrent» se usa para tres cosas distintas: el **protocolo**, el **archivo de la lista** y el **programa**. Cuando alguien dice «prohibieron los torrents» normalmente habla de un índice, no del protocolo — y el protocolo sigue en pie {num(R['webtorrent/webtorrent']['dias_nace'])} días después, con {palabras(A['vivos'])} implementaciones medidas esta noche. Distinguir esas tres cosas es la mitad de entender este tema.

───────────────────
""")

w(f"""*🔌 Tres configuraciones típicas · qué instalar según dónde estés*

No hace falta elegir un cliente para siempre. Hay tres escenarios que cubren casi todo lo que la gente pregunta, y en los tres la respuesta se puede comprobar con las seis órdenes de la sección anterior.

**En la computadora de casa.** **qBittorrent** si quieres ventana y ver la cola; **transmission** si quieres que corra solo, sin interfaz, y lo manejes desde el navegador. Los dos publican este mes. El segundo pesa menos y no te pide nada; el primero tiene más ajustes y más superficie donde equivocarse.

**En el teléfono.** Aquí el terreno se movió: **LibreTorrent**, el favorito de las listas, lleva {R['proninyaroslav/libretorrent']['dias_push']} días sin un empujón. **BATorrent** publica versiones desde hace meses, **hop** firma {num(E['antonyshakirov/hop']['con_huella'])} de {num(E['antonyshakirov/hop']['adjuntos'])} adjuntos y **Atrium** te deja gobernar el de la computadora desde el móvil, que muchas veces es lo que de verdad se necesita. Los tres son de 2026 y los tres tienen repositorio abierto: se prueban con material propio.

**En un servidor pequeño o un aparato de casa.** **transmission** en modo demonio y **smartmontools** vigilando el disco. Y una cosa que se olvida siempre: un cliente de torrentes trabajando sobre un disco que se está muriendo convierte un fallo de hardware en una biblioteca perdida. La orden 5 de esta pieza cuesta un minuto y ahorra eso.

**Y el cuarto escenario, que casi nadie cuenta: compartir lo tuyo.** Los {palabras(A['vivos'])} programas de esta pieza sirven igual para repartir tu propio material —un disco de fotos, el taller de tu barrio, una grabación que quieras que circule— sin pagar servidor ni pedir permiso a nadie. Ese uso existe, es técnico y es legítimo, y es el que casi nunca aparece cuando se habla de torrentes. Si lo que quieres es eso, el camino es el mismo: qBittorrent o transmission, la lista creada por ti, y una suma publicada donde pongas el enlace. La diferencia con el resto de los usos no está en el programa, está en el derecho que tengas sobre lo que repartes.

**Lo que no recomiendo, y por qué.** No recomiendo instalar ninguna pieza de esta lista por lo que diga una lista de «mejores clientes de 2026»: esa lista, casi siempre, no ha mirado una fecha. Y no recomiendo automatizar —**autobrr**, **upbrr**— antes de tener claro qué se está automatizando, porque un automatizador hace más deprisa exactamente lo que ya hacías.

───────────────────
""")

open('/tmp/lab16/docs/talleres/pieza16/s1b.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
