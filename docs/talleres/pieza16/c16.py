# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab16/docs/talleres/pieza16')
from d16 import *
A=AGG; T=[]; w=T.append
def f(r,nombre,texto): T.append(f"{ficha(r,nombre)}. {texto}\n")

w(f"""*🧰 Lo que no es un cliente y también hace falta · tres programas con enlace*

Las tres piezas de este bloque sí llevan dirección, porque ninguna es un cliente de torrentes. Y son, en mi opinión, las más útiles de la pieza: **comprobar un archivo**, **calcular su huella** y **saber si el disco que lo guarda se está muriendo**.

""")
f('rhash/RHash','RHash',
  f"**{num(E['rhash/RHash']['con_huella'])} sumas de {num(E['rhash/RHash']['adjuntos'])} adjuntos** —la mejor proporción del tema con diferencia— y licencia **0BSD**: calcula y verifica sumas de cualquier tipo, incluidas las de los archivos que acabas de bajar. {num(E['rhash/RHash']['commits_30d'])} cambio en treinta días y {num(E['rhash/RHash']['incidencias']['cerradas'])} incidencias cerradas")
f('uutils/coreutils','uutils/coreutils',
  f"**{num(R['uutils/coreutils']['stars'])} estrellas**: la reescritura en Rust de las herramientas de siempre, con `sha256sum`, `df`, `ls` y compañía. **Empujón de hoy** y {num(E['uutils/coreutils']['commits_30d'])} cambios en treinta días; {num(E['uutils/coreutils']['adjuntos'])} adjuntos sin suma, que se instala desde el gestor de paquetes")
f('smartmontools/smartmontools','smartmontools',
  f"**{num(R['smartmontools/smartmontools']['descargas'])} descargas** y {num(E['smartmontools/smartmontools']['con_huella'])} sumas de {num(E['smartmontools/smartmontools']['adjuntos'])} adjuntos: lee la salud del disco antes de que se llene o se muera. {num(E['smartmontools/smartmontools']['commits_30d'])} cambios en treinta días y {num(E['smartmontools/smartmontools']['incidencias']['cerradas'])} incidencias cerradas")

w(f"""
Las tres juntas contestan la pregunta que el tema del torrent casi nunca contesta: **¿el archivo llegó bien y el disco está sano?** RHash compara contra una suma publicada; coreutils calcula la tuya; smartmontools avisa si el disco que lleva diez años sembrando está a punto de fallar. Es la parte aburrida y es la que evita perder una biblioteca.

───────────────────

*⚖️ La responsabilidad · lo que el protocolo no decide y la ley sí*

Esta sección no la trae ninguna lista de clientes, y es la que más falta hace. Va sin adornos.

**El protocolo es neutral; el uso no.** BitTorrent mueve trozos entre pares: no sabe qué contienen. Un cliente bien configurado es igual de útil para distribuir una imagen de Linux que para compartir una película con derechos vigentes. Por eso esta pieza mide **software** y no recomienda **contenido**: no hay un solo enlace a un índice ni a un archivo en todo el texto.

**Lo que la ley mira no es el programa.** Mira tres cosas: **qué obra** es, **qué derecho tienes** sobre ella y **qué haces** con ella. Compartir —sembrar— es el verbo que más problemas ha dado, porque en el protocolo es la conducta por defecto: mientras el cliente está abierto, estás repartiendo. En la República Dominicana rige la Ley 65-00 sobre derecho de autor, con excepciones parecidas a las de la región; en otros países el régimen cambia. **Esta pieza no da consejo legal**; dice dónde está la pregunta.

**Lo práctico, y esto sí es técnico.** Tres ajustes cambian por completo qué haces en la red, y todos los clientes los tienen:

- **La carpeta y el límite de subida.** Saber cuánto subes y a qué es el primer paso; un límite de subida no te hace invisible, solo te hace lento.
- **La siembra después de terminar.** Muchos clientes siembran hasta una proporción determinada. Ese número —el *ratio*— es la decisión más consecuente que se toma en una pantalla de configuración.
- **El cifrado y el registro.** El cifrado del protocolo no oculta lo que haces; cambia cómo se ve en la red. Y el archivo de registro de tu cliente dice exactamente qué hiciste, con fecha y hora: es el primer sitio donde mira quien pregunta.

**Y lo que esta serie no hace.** No enlaza clientes ni índices (norma del canal, H20), no explica cómo saltarse un aviso legal y no dice que algo sea legal porque sea posible. Cuando un programa de la lista tiene una función que sirve sobre todo para compartir obra ajena, se dice y se mide igual —como con SpotiFlyer en la pieza 14—, sin mandar a nadie por ahí.

───────────────────

*🔏 La huella del tema · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}*

**{num(A['adjuntos'])} archivos publicados por las {palabras(A['vivos'])} piezas. {num(A['con_huella'])} con suma de comprobación. El 8,7 %.**

Es la proporción más baja desde la pieza 11, y en este tema duele más que en ningún otro. En su escala: tiendas de extensiones de la pieza 10, **0,08 %**; aplicaciones de la 11, **5,5 %**; descarga de la 15, **10,6 %**; audio de la 13, **11,4 %**; kit de la 12, **17,0 %**; música de la 14, **20,0 %**; y **torrentes, 8,7 %**.

**{palabras(A['vivos']-A['con_huella_repos'])} de los {palabras(A['vivos'])} no publican ni una suma.** Los {palabras(A['con_huella_repos'])} que sí:

""")
w("| Recurso | Adjuntos | Con suma | Nota |\n|---|---|---|---|\n")
for c_,a_,r in sorted([(E[r]['con_huella'],E[r]['adjuntos'],r) for r in VIVOS if E[r]['con_huella']],reverse=True):
    w(f"| {r.split('/')[1]} | {num(a_)} | **{num(c_)}** | {E[r]['puntos']} |\n")
w(f"""
Dos cosas de esa tabla. La primera: **qBittorrent pone {num(E['qbittorrent/qBittorrent']['con_huella'])} de las {num(A['con_huella'])} sumas** —más de un tercio del total— y lo hace con **solo {num(R['qbittorrent/qBittorrent']['entregas'])} entregas etiquetadas**: firma mucho por entrega, publica pocas. La segunda: **RHash, con {num(R['rhash/RHash']['stars'])} estrellas, tiene la mejor proporción del tema** —{num(E['rhash/RHash']['con_huella'])} de {num(E['rhash/RHash']['adjuntos'])}—, y es justamente el programa que sirve para comprobar los demás.

**Lo que se puede hacer hoy:** en los clientes que no publican sumas —casi todos—, la comprobación es la del propio protocolo: el cliente verifica cada trozo contra su hash al bajarlo. Esa es la parte buena del torrent y la razón de que siga vivo: **el archivo se comprueba solo**. Lo que no se comprueba es el instalador del cliente.

───────────────────

*🛠️ Seis órdenes para revisar este ecosistema sin enlazarlo*

1. **Ver si el cliente sigue vivo.** `curl -s api.github.com/repos/<dueño>/<repo> | grep -E '"pushed_at"|"archived"'` — se sustituye el nombre y se mira el campo. Es lo que separa a piko de Deluge, y lo que ninguna lista de «mejores clientes 2026» hace.
2. **Contar sus versiones.** `curl -s api.github.com/repos/<dueño>/<repo>/releases?per_page=100 | grep -c '"tag_name"'` — Deluge responde cero; BATorrent responde cuarenta y ocho.
3. **Buscar una suma.** `curl -s api.github.com/repos/<dueño>/<repo>/releases?per_page=100 | grep -Ei 'sha256|sha512|\\.sig|\\.asc' | head -5` — si imprime líneas, ese proyecto firma.
4. **Comprobar un archivo bajado.** `sha256sum archivo.iso` o `rhash --sha256 archivo.iso` — y comparar con la cifra publicada por quien lo hizo. El protocolo verifica los trozos; esta orden verifica el archivo entero.
5. **Mirar el disco antes de llenarlo.** `smartctl -a /dev/sdX` — temperatura, horas encendidas, sectores reasignados y el veredicto del propio disco. Un cliente de torrentes trabajando sobre un disco moribundo multiplica el daño.
6. **Ver qué hiciste tú.** El archivo de registro del cliente, o el historial de proporción: `cat ~/.local/share/qBittorrent/logs/*.log | tail -40` — es la prueba de lo que salió y lo que entró, y el primer sitio donde mira quien pregunta.

Las órdenes **1 a 3 van sin dirección completa a propósito**: se pega el nombre en la dirección y se ejecuta. La norma del canal es esa, y este tema la lleva al extremo.

───────────────────

*🚪 Lo que esta pieza no tiene*

**Ni un solo enlace de la familia torrentes**: ni clientes, ni índices, ni buscadores, ni automatizadores. Se dan nombre, función y comprobación, y las direcciones van en la versión de WhatsApp. Tampoco hay enlaces a contenido: no se recomienda qué bajar, solo con qué.

**No es una lista de lo más nuevo.** Es un censo con fechas donde lo nuevo gana en nota —piko y emule-qt están arriba— pero donde también hay dos recién nacidos que no llegan al mínimo, **torrent-tui** y **Magnetar**, y dos veteranos que siguen funcionando hoy y ya no se actualizan, **LibreTorrent** y **Deluge**.

*📅 La semana de prueba · cinco días para tener un cliente que se pueda comprobar*

- **Día uno.** Instala **qBittorrent** o **Transmission** desde el paquete de tu distribución y comprueba con la orden 1 que el proyecto publicó algo este mes.
- **Día dos.** Baja un archivo **tuyo** —una imagen de Linux, tu propio material— y verifica con `sha256sum` la cifra que publica quien lo hizo. Acabas de hacer la comprobación que el 91 % de este tema no facilita.
- **Día tres.** Mira la salud de tu disco con la orden 5. Un cliente de torrentes escribe mucho: si el disco tiene diez años, mejor saberlo antes.
- **Día cuatro.** En el teléfono, si usas LibreTorrent, pruébale **Atrium** encima o cambia a **BATorrent** o **hop**: los tres publicaron este mes.
- **Día cinco.** Revisa tu configuración de subida y de siembra con la sección de responsabilidad delante. Es la decisión que más consecuencias tiene y casi nadie la mira.

───────────────────

*❓ Las preguntas del grupo*

**¿Es legal usar BitTorrent?**
El protocolo sí, y por eso está en todas las distribuciones de Linux. Lo que puede no serlo es compartir obras sobre las que no tienes derechos. La ley mira la obra, no el programa; esta pieza no da consejo legal.

**¿Cuál instalo, en una frase?**
**qBittorrent** si quieres ventana y **Transmission** si quieres un demonio. En Android, **BATorrent**, **hop** o **Atrium**; LibreTorrent lleva {R['proninyaroslav/libretorrent']['dias_push']} días sin publicar.

**¿Por qué no pones los enlaces?**
Porque Facebook retiró la pieza 12 por un enlace de esta familia, y el criterio es suyo. Se dan nombre, función y la orden de comprobación; las direcciones van en la versión de WhatsApp.

**¿Qué es la proporción y por qué importa?**
Es lo que has subido dividido entre lo que has bajado. El protocolo funciona porque la gente sube; un cliente con la proporción a cero está usando la red sin devolver nada, y muchos clientes te limitan por eso.

**¿Sirve algo de lo de 2026 con tres meses?**
**piko** saca {E['NihilDigit/piko']['puntos']} y firma {num(E['NihilDigit/piko']['con_huella'])} de {num(E['NihilDigit/piko']['adjuntos'])}; **emule-qt**, {E['ModderMule/emule-qt']['puntos']} con {num(E['ModderMule/emule-qt']['commits_30d'])} cambios al mes. Para probar sí; para mover tu biblioteca, espera un año y vuelve a medir.

**¿Y Deluge y LibreTorrent, que todo el mundo recomienda?**
Que están parados: {R['deluge-torrent/deluge']['dias_push']} y {R['proninyaroslav/libretorrent']['dias_push']} días sin publicar. Funcionan hoy y no se van a arreglar. Es lo mismo que le pasó a Seal en la pieza 15.

**¿Por qué esta pieza firma tan poco?**
Porque el ecosistema del torrent vive de la confianza en el enlace, no en el instalador: el cliente verifica los trozos y nadie verifica el cliente. **8,7 %** es la cifra más baja del año y no es una casualidad: es una cultura.

───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **el protocolo sigue en pie porque no tiene dueño**. {num(R['webtorrent/webtorrent']['dias_nace'])} días, {palabras(A['vivos'])} piezas medidas esta noche y ni una sola que dependa de un servidor central. Eso es una virtud técnica y un problema de mantenimiento: nadie garantiza que las piezas sigan vivas.

Lo segundo: **lo viejo no está muerto, pero dos de sus nombres están parados**. qBittorrent y Transmission publican; LibreTorrent y Deluge no. La diferencia no es la edad —qBittorrent es más viejo que los dos— es que alguien siga empujando.

Lo tercero: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 8,7 %**. La cifra más baja del año, y la explicación está en el propio protocolo: el cliente verifica los trozos, así que nadie siente la necesidad de firmar el instalador. **Ese es justo el hueco que se puede atacar**: si vas a ejecutar un programa que mueve tu disco y tu red, al menos que alguien te diga que es el suyo.

Y lo cuarto: **nueve piezas de 2026 en un tema que parecía cerrado**. Escribir un cliente de torrentes hoy no es un capricho: es que el protocolo es simple, está documentado y hay librerías en todos los idiomas. Lo nuevo no desplaza a qBittorrent, pero ya compite con él en la parte que importa —publicar, atender y no romperse—.

───────────────────
""")
w(f"""— {num(A['adjuntos'])} archivos publicados por {palabras(A['vivos'])} piezas del ecosistema y {num(A['con_huella'])} firmados: el 8,7 %, la proporción más baja del año y con nombre y explicación.
— Siete clientes veteranos, {palabras(A['nuevas2026'])} piezas de 2026 y dos de ellos —LibreTorrent y Deluge— señalados con su fecha.
— Ni un enlace de la familia, como manda el canal: nombre, función y seis órdenes para comprobarlo todo sin abrir una sola dirección.

💓 *La Bandita informa a partir de fuentes fechadas.* {palabras(A['vivos'])} piezas del ecosistema abiertas hoy una por una —del cliente de siempre al de tres meses, del automatizador al comprobador de discos—, la tabla de qué cubre qué, las {num(A['con_huella'])} sumas contadas archivo por archivo y seis órdenes para no instalar a ciegas.

───────────────────

*Medición del corte:* miércoles 4 de noviembre de 2026, {HORA} de la noche en Santo Domingo, con la fecha comprobada en vivo antes de empezar y al terminar · decimoséptima medición del día · {palabras(A['vivos'])} piezas vivas, ninguna archivada, {palabras(A['sin_lic'])} sin licencia legible · {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas · {num(A['descargas'])} descargas · {palabras(A['con_huella_repos'])} repositorios firmando.

*🔗 Enlaces*

*Las tres piezas de este bloque no son clientes de torrentes y por eso llevan dirección:*

""")
GRUPOS=[("Verificación, sistema y disco",['rhash/RHash','uutils/coreutils','smartmontools/smartmontools'])]
usados=set()
for titulo,rs in GRUPOS:
    w(f"*{titulo}:*\n\n")
    for r in rs:
        usados.add(r); w(f"- https://github.com/{r}\n")
    w("\n")
falta=set(VIVOS)-usados
assert falta, "no debería"
w("*La familia de los torrentes · sin dirección, por la norma del canal (H20):*\n\n")
w("- **Clientes:** qBittorrent, Transmission, LibreTorrent, Deluge, WebTorrent, anacrolix/torrent (librería) y libtorrent (librería).\n")
w("- **De 2026:** piko, Atrium, emule-qt, BATorrent, torrra, hop, TorrentShopNX, Magnetar, torrent-tui y nemorosa.\n")
w("- **Automatización:** autobrr y upbrr.\n")
w("- Se buscan por su nombre en GitHub: un `curl` a `api.github.com/repos/<dueño>/<repo>` da su fecha y su estado en un segundo.\n\n")

w(f"""*Las dos direcciones de las órdenes con nombre propio:*

- api rhash: https://api.github.com/repos/rhash/RHash
- api smartmontools: https://api.github.com/repos/smartmontools/smartmontools

───────────────────

*🗒️ Notas al pie*

(4-nov) La fecha se comprobó **en vivo antes de empezar y al terminar**: `tools/fecha_viva.py --inicio` y `--fin` al cerrar. **Antes de sondear** se hizo la revisión obligatoria —fecha, historial y ecosistema— con `tools/preflight.py --tema torrent`; su acta está en `docs/PREFLIGHT-torrent-2026-11-04.json`. La medición es de las {HORA} y vive en `docs/MEDICION-16-noche-2026-11-04.json`.

(4-nov) **Decimoséptima medición del día.** Las {palabras(A['vivos'])} direcciones se pidieron una por una y el escrutinio de las {palabras(A['vivos'])} fichas se rehízo a la misma hora.

(4-nov) La cuenta de **huella** es la de toda la serie: `sha256`, `sha512`, `sha1`, `checksum`, `.sig`, `.asc` o `sums` en el nombre de cada adjunto de las últimas cien entregas. Escala completa: 0,08 % · 5,5 % · 8,7 % · 10,6 % · 11,4 % · 17,0 % · 20,0 %.

(4-nov) **La norma del canal se aplica al pie de la letra (H20):** los {palabras(A['vivos']-3)} programas de la familia torrentes van sin dirección en el cuerpo y sin dirección en la lista de enlaces; solo las tres piezas que no son clientes llevan su dirección. Es la pieza donde esa norma pesa más y por eso se dice tres veces.

(4-nov) Las **notas** se calculan con los nueve pesos de la casa y las cuatro penalizaciones. **emule-qt saca {E['ModderMule/emule-qt']['puntos']} con {num(R['ModderMule/emule-qt']['stars'])} estrellas** y **qBittorrent {E['qbittorrent/qBittorrent']['puntos']} con {num(R['qbittorrent/qBittorrent']['stars'])}**: la vara no premia la fama, premia que se pueda comprobar.

(4-nov) **El taller queda en `docs/talleres/pieza16/`**, con los generadores del texto, para que las cifras se puedan repetir desde el repositorio (H22).

*#task*

#task 075 · volver a medir las {palabras(A['vivos'])} el 4 de diciembre y decir si LibreTorrent y Deluge publicaron: si no, salen de la recomendación del todo.

#task 076 · comprobar con `sha256sum` el instalador de qBittorrent contra su cifra publicada, y dejar el resultado en un acta.

#task 077 · medir en enero si la camada de 2026 aguanta: piko y emule-qt tienen ritmo, torrent-tui y Magnetar no.

#task 078 · escribir la pieza 17 —la radio y el directo— con la misma norma: listas y enlaces de emisión sin URL en el cuerpo.

───────────────────

🏷️ Etiquetas estratégicas

#QBittorrent #Transmission #Piko #BATorrent #Torrra #EmuleQt #WebTorrent #Autobrr #RHash #Smartmontools #BitTorrent #OpenSourceDominicano
""")
open('/tmp/lab16/docs/talleres/pieza16/s3.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
