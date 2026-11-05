# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab16/docs/talleres/pieza16')
from d16 import *
A=AGG; T=[]; w=T.append
def f(r,nombre,texto): T.append(f"{ficha_sin(r,nombre)}. {texto}\n")

w(f"""*🧱 Los clientes de siempre · siete piezas, ninguna con enlace*

Aquí están los nombres que todo el mundo conoce y que, por la norma del canal, van **sin dirección**. Se dan el nombre, lo que hacen y la orden con la que cualquiera comprueba su estado en GitHub. Nada más, y nada menos.

Empiezo por el que casi todo el mundo tiene instalado, porque su ficha es la más interesante de la noche: **qBittorrent** es el único cliente de esta lista que publica sumas de comprobación en cantidad, y a la vez el que menos entregas etiquetadas tiene.

""")
f('qbittorrent/qBittorrent','qBittorrent',
  f"**{num(E['qbittorrent/qBittorrent']['con_huella'])} sumas de {num(E['qbittorrent/qBittorrent']['adjuntos'])} adjuntos** —el único cliente del tema que firma en serio—, canal de seguridad y **empujón de hoy**. {num(E['qbittorrent/qBittorrent']['commits_30d'])} cambios en treinta días y {num(E['qbittorrent/qBittorrent']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['qbittorrent/qBittorrent']['incidencias']['abiertas'])} abiertas. **Sin licencia legible en la API** y **solo {num(R['qbittorrent/qBittorrent']['entregas'])} entregas** etiquetadas: el programa que más gente usa del tema y el que menos versiones anuncia")
f('transmission/transmission','Transmission',
  f"**{num(R['transmission/transmission']['stars'])} estrellas** y {num(R['transmission/transmission']['entregas'])} entregas: el cliente discreto, el que corre sin ventana en un servidor pequeño y el que llevan dentro muchos aparatos de red. **Empujón de ayer**, {num(E['transmission/transmission']['commits_30d'])} cambios en treinta días y **cero sumas** en {num(E['transmission/transmission']['adjuntos'])} adjuntos")
f('anacrolix/torrent','anacrolix/torrent',
  f"**{num(R['anacrolix/torrent']['stars'])} estrellas** y {num(E['anacrolix/torrent']['commits_30d'])} cambios en treinta días: la implementación en Go que usan por dentro otros programas, con **canal de seguridad**. **Sin entregas etiquetadas y sin adjuntos**: es una librería, se importa, no se instala")
f('arvidn/libtorrent','libtorrent (la librería)',
  f"**{num(E['arvidn/libtorrent']['adjuntos'])} adjuntos y {num(R['arvidn/libtorrent']['entregas'])} entregas** —el más prolijo del tema en versiones—, con **empujón de hoy** y {num(E['arvidn/libtorrent']['commits_30d'])} cambios en treinta días. Es el motor que hay debajo de media docena de clientes: **sin licencia legible** y **sin una sola suma**")
f('webtorrent/webtorrent','WebTorrent',
  f"**{num(R['webtorrent/webtorrent']['stars'])} estrellas** y cien entregas: el que lleva el protocolo al navegador y hace que un enlace se pueda abrir como una página. **Empujón de ayer**, {num(E['webtorrent/webtorrent']['incidencias']['cerradas'])} incidencias cerradas y **sin adjuntos publicados**")
f('proninyaroslav/libretorrent','LibreTorrent',
  f"**{R['proninyaroslav/libretorrent']['dias_push']} días sin un empujón y cero cambios en treinta días**: el cliente de Android que recomiendan todas las listas, con {num(R['proninyaroslav/libretorrent']['stars'])} estrellas, {num(R['proninyaroslav/libretorrent']['descargas'])} descargas y **{E['proninyaroslav/libretorrent']['puntos']} puntos**. {num(E['proninyaroslav/libretorrent']['adjuntos'])} adjuntos sin suma")
f('deluge-torrent/deluge','Deluge',
  f"**{R['deluge-torrent/deluge']['dias_push']} días sin publicar, cero entregas y cero adjuntos**: el cliente con demonio y consola web que fue la alternativa «seria» a todo lo demás. **{E['deluge-torrent/deluge']['puntos']} puntos** en la vara y sin licencia legible. Se lista para que nadie lo instale creyendo que está vivo")

w(f"""
El bloque de los veteranos deja tres nombres utilizables —**qBittorrent**, **Transmission**, **WebTorrent**— y dos que ya no deberían estar en ninguna lista de 2026: **LibreTorrent** ({R['proninyaroslav/libretorrent']['dias_push']} días) y **Deluge** ({R['deluge-torrent/deluge']['dias_push']}). Los dos siguen funcionando hoy, y ninguno de los dos va a arreglar el fallo que aparezca mañana.

Y un detalle que se repite en toda la pieza: **de los siete, solo uno firma** —qBittorrent—. En un protocolo cuyo sentido entero es la integridad de los trozos, el archivo que instala el cliente casi nunca se puede comprobar.

───────────────────

*🌱 Las {palabras(A['nuevas2026'])} de 2026 · la camada que sí se mueve*

Otra vez lo nuevo manda, y aquí con más mérito que en ningún otro tema: escribir un cliente de torrentes no es envolver una web, es implementar un protocolo con trozos, pares, anuncios y cola. Estas {palabras(A['nuevas2026'])} piezas lo hacen, y varias con más de doscientos cambios al mes.

**La advertencia de siempre, y aquí importa más:** un cliente de torrentes nuevo todavía no ha visto un enjambre grande, ni un disco lleno, ni un corte de luz con veinte descargas a medias. Se prueban con material propio y se miden igual que los demás.

""")
f('NihilDigit/piko','piko',
  f"**{R['NihilDigit/piko']['dias_nace']} días de vida y {E['NihilDigit/piko']['puntos']} puntos**: la segunda nota del tema, con **{num(E['NihilDigit/piko']['con_huella'])} sumas de {num(E['NihilDigit/piko']['adjuntos'])} adjuntos** y {num(E['NihilDigit/piko']['commits_30d'])} cambios en treinta días. {num(R['NihilDigit/piko']['descargas'])} descargas y {num(E['NihilDigit/piko']['incidencias']['cerradas'])} incidencias cerradas")
f('retransmit/Atrium','Atrium',
  f"**Canal de seguridad** y {num(E['retransmit/Atrium']['commits_30d'])} cambios en treinta días: la consola que gobierna el cliente que ya tienes desde el teléfono, con {num(R['retransmit/Atrium']['descargas'])} descargas y {num(E['retransmit/Atrium']['incidencias']['cerradas'])} incidencias cerradas. {num(E['retransmit/Atrium']['adjuntos'])} adjuntos sin suma")
f('ModderMule/emule-qt','emule-qt',
  f"**{num(E['ModderMule/emule-qt']['commits_30d'])} cambios en treinta días** —el ritmo más alto de la camada—, con {num(E['ModderMule/emule-qt']['con_huella'])} sumas de {num(E['ModderMule/emule-qt']['adjuntos'])} adjuntos y {num(R['ModderMule/emule-qt']['entregas'])} entregas. Otra red entre pares, con la misma lógica de trozos y la misma responsabilidad")
f('BATorrent-app/BATorrent','BATorrent',
  f"**{num(R['BATorrent-app/BATorrent']['entregas'])} entregas en {num(R['BATorrent-app/BATorrent']['dias_nace'])} días**, con **canal de seguridad** y {num(E['BATorrent-app/BATorrent']['commits_30d'])} cambios en treinta días: el más constante de la camada en versiones, con {num(E['BATorrent-app/BATorrent']['adjuntos'])} adjuntos sin firma")
f('stabldev/torrra','torrra',
  f"**{num(R['stabldev/torrra']['stars'])} estrellas** y {num(R['stabldev/torrra']['entregas'])} entregas: el que más ha crecido de los nuevos, con {num(E['stabldev/torrra']['commits_30d'])} cambios en treinta días y **solo {num(E['stabldev/torrra']['incidencias']['abiertas'])} incidencia abierta** contra {num(E['stabldev/torrra']['incidencias']['cerradas'])} cerradas")
f('antonyshakirov/hop','hop',
  f"**{num(E['antonyshakirov/hop']['con_huella'])} sumas de {num(E['antonyshakirov/hop']['adjuntos'])} adjuntos** y {num(E['antonyshakirov/hop']['commits_30d'])} cambios en treinta días: el más pequeño que firma algo, con {num(R['antonyshakirov/hop']['entregas'])} entregas en {num(R['antonyshakirov/hop']['dias_nace'])} días")
f('Langegen/TorrentShopNX','TorrentShopNX',
  f"**{num(E['Langegen/TorrentShopNX']['commits_30d'])} cambios en treinta días** y {num(R['Langegen/TorrentShopNX']['entregas'])} entregas: cliente para consola portátil, con **empujón de hoy** y {num(E['Langegen/TorrentShopNX']['adjuntos'])} adjuntos sin suma")
f('ArrCee76/magnetar','Magnetar',
  f"**{num(E['ArrCee76/magnetar']['puntos'])} puntos y {R['ArrCee76/magnetar']['dias_push']} días sin un empujón**: un cliente pequeño que nació en marzo y ya se ha enfriado, con **sin licencia legible** y {num(E['ArrCee76/magnetar']['adjuntos'])} adjuntos. Se lista como lo que es")
f('ryadios/torrent-tui','torrent-tui',
  f"**{E['ryadios/torrent-tui']['puntos']} puntos** —la nota más baja del tema—, **sin licencia legible, sin entregas y sin adjuntos**: una idea buena —cliente de terminal— con tres meses y seis cambios. Se lista para que se vea que lo nuevo también puede no arrancar")
f('KyokoMiki/nemorosa','nemorosa',
  f"**{R['KyokoMiki/nemorosa']['dias_nace']} días de vida y {num(E['KyokoMiki/nemorosa']['puntos'])} puntos**: sin entregas ni adjuntos y **cero cambios en treinta días**, aunque con empujón de ayer. Un proyecto que se mueve a rachas y todavía no ha publicado una versión")

w(f"""
El reparto de la camada es el más desigual de la serie: **piko ({E['NihilDigit/piko']['puntos']}) y emule-qt ({E['ModderMule/emule-qt']['puntos']}) están a la altura de los veteranos**, y **torrent-tui ({E['ryadios/torrent-tui']['puntos']}) y Magnetar ({E['ArrCee76/magnetar']['puntos']}) no llegan al mínimo**. La diferencia entre unos y otros no es la edad —todos tienen entre uno y ocho meses— sino si publican versiones y si alguien atiende la cola.

───────────────────

*🤖 Automatizar y vigilar · dos piezas de fontanería*

Este par es la mejor nota del tema y la peor noticia para quien busca un cliente: **no son clientes**. Son programas que miran lo que se publica y avisan, y que en esta casa sacan más nota que cualquier interfaz.

""")
f('autobrr/autobrr','autobrr',
  f"**{E['autobrr/autobrr']['puntos']} puntos, la nota más alta de la pieza**: {num(E['autobrr/autobrr']['con_huella'])} sumas de {num(E['autobrr/autobrr']['adjuntos'])} adjuntos, **empujón de hoy**, {num(E['autobrr/autobrr']['commits_30d'])} cambios en treinta días y **solo {num(E['autobrr/autobrr']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['autobrr/autobrr']['incidencias']['cerradas'])} cerradas. Vigila lo que publican los índices y manda lo que te interesa al cliente, sin que tengas que mirar")
f('autobrr/upbrr','upbrr',
  f"**{num(E['autobrr/upbrr']['commits_30d'])} cambios en treinta días** y {num(R['autobrr/upbrr']['entregas'])} entregas: el hermano pequeño de la misma casa, con **empujón de hoy**, {num(E['autobrr/upbrr']['adjuntos'])} adjuntos y {num(E['autobrr/upbrr']['incidencias']['cerradas'])} incidencias cerradas")

w(f"""
Las dos van sin enlace por la misma norma que los clientes: son parte de la familia que Facebook vetó. Y las dos, por cierto, **no firman ni un archivo** —{num(E['autobrr/autobrr']['adjuntos']+E['autobrr/upbrr']['adjuntos'])} adjuntos entre las dos y ninguna suma—, así que su nota alta viene de otra parte: publican a diario, atienden la cola y no se rompen.

───────────────────
""")
open('/tmp/lab16/docs/talleres/pieza16/s2.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
