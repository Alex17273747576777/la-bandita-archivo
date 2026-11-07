#!/usr/bin/env python3
import json
from pathlib import Path
R=Path('/home/user/Arena-Reimagined')
FB=R/'01-PUBLICACIONES/Facebook-dominicano-ES'
VER={}
for p in [R/'02-ARCHIVO/_rearm-29oct/investigacion-29oct/candidatos-nuevos-29oct.json',
          R/'02-ARCHIVO/_rearm-29oct/creacion-fb-83-108/verificacion-fuentes-83-108.json']:
    if p.exists():
        for r in json.load(open(p,encoding='utf-8')):
            if isinstance(r,dict) and r.get('slug') and r.get('stars') is not None: VER[r['slug'].lower()]=r
def fmt(n): return f"{n:,}".replace(',','.') if isinstance(n,int) else '—'
def lic(r):
    l=r.get('license')
    if not l: return 'licencia sin resolver'
    if l=='NOASSERTION': return 'licencia sin clasificar (NOASSERTION)'
    return l
def placa(s):
    r=VER[s.lower()]
    rel=f" · release {r.get('release')} ({r.get('release_at')})" if r.get('release') and (r.get('release_at') or '')>='2026-08-29' else ''
    arch=' · ARCHIVADO' if r.get('archived') else ''
    return f"• `{s.lower()}` — ★{fmt(r.get('stars'))} (verificado 29-oct-2026) · última actividad {r.get('commit') or '—'} · {lic(r)}{rel}{arch}."

P={
'109': dict(slug='El-cine-sin-taquilla-Orvid-y-el-video-privado-con-Tor', titulo='El cine sin taquilla: Orvid y el video privado con Tor',
 esencia='Orvid busca el video en más de 250 sitios a la vez y manda cada petición por Tor, con circuito propio por fuente y por video. Es una semilla de 13 días (nació el 16-oct-2026) con release de hoy, y esta página la firma con su vara completa: concepto sobresaliente, comunidad mínima, confianza delegada al repo de fuentes que el dueño añada. Se prueba en el teléfono de laboratorio; el pedestal se gana con meses, no con titulares.',
 placas=['mankidev/orvid','mankidev/orvid-sources','TeamNewPipe/NewPipe','libre-tube/libretube'],
 reglas=['El teléfono del laboratorio primero: la semilla se prueba donde un fallo no duele.','El repo de fuentes se añade con nombre y apellido: lo que buscas pasa por las fuentes que TU firmaste.','Tor por defecto es doctrina, no adorno: si lo apagas, la app misma te avisa que tu IP queda a la vista.'],
 vara='La privacidad que depende de un solo desarrollador joven se respeta, se verifica y se vuelve a pulsar en la próxima gira: nada de fe ciega, nada de desprecio ciego.',
 meme='—Nueve estrellas y ya quieres pieza. —Nueve estrellas y release de hoy a los 13 días de nacida: la pieza es el radar, no el altar.'),
'110': dict(slug='La-app-vacia-y-las-fuentes-firmadas-el-motor-y-el-contenido', titulo='La app vacía y las fuentes firmadas: el motor y el contenido',
 esencia='La corriente que viene trae las apps vacías: el cliente nace como motor y el contenido vive en repositorios de fuentes que se añaden, se firman y se podan. Mihon lo probó con las extensiones, Kazumi lo llevó al anime y Orvid lo acaba de traer al video con Tor. La doctrina cambia el oficio: ya no se audita solo la app; se audita la fuente, su firmante y su fecha, porque el motor sin fuentes es un cine sin películas y la fuente sin firma es una puerta sin nombre.',
 placas=['Predidit/Kazumi','mihonapp/mihon','mankidev/orvid','mankidev/orvid-sources'],
 reglas=['Fuente con firmante conocido o no entra: el contenido también tiene procedencia.','El motor se actualiza en su gira y las fuentes en la suya: dos calendarios, una libreta.','Fuente muerta se poda sin nostalgia; la lista limpia es parte de la higiene.'],
 vara='La confianza ya no vive en la tienda: vive en la cadena motor → fuente → firmante, y cada eslabón lleva su fecha.',
 meme='—La app no trae nada. —Trae el motor: el contenido lo firmas tú, que es exactamente el punto.'),
'111': dict(slug='La-tienda-sin-tienda-Obtainium-y-las-actualizaciones-desde-la-forja', titulo='La tienda sin tienda: Obtainium y las actualizaciones desde la forja',
 esencia='La tienda sin tienda no vende nada: vigila las forjas de tus apps y te avisa cuando sueltan release. Obtainium manda en ese oficio con pulso de esta semana, Appteka abre la tienda comunitaria y Droid-ify ordena el catálogo libre. La doctrina es la soberanía del update: la app se actualiza desde SU casa, con SU fecha y SU checksum, sin intermediario que decida por ti qué versión mereces.',
 placas=['ImranR98/Obtainium','solkin/appteka-android','Droid-ify/client'],
 reglas=['Cada app vigilada nace de SU repo oficial: el enlace se copia de la forja, no de un blog.','La notificación de release se lee antes de actualizar: fecha, notas y licencia, en ese orden.','Lo que no está en ninguna forja seria no se persigue por canales: la ausencia también es información.'],
 vara='Quien controla tus actualizaciones controla tu teléfono a plazos: la tienda sin tienda te devuelve ese control con recibo.',
 meme='—Mi tienda no me ofreció la actualización. —La forja la soltó hace tres días: la tienda sin tienda ya te había avisado.'),
'112': dict(slug='La-soberania-local-LocalSend-y-RustDesk-sin-nube-ajena', titulo='La soberanía local: LocalSend y RustDesk sin nube ajena',
 esencia='Pasar un archivo al aparato de al lado o mirar tu escritorio desde el sofá no debería pedirle permiso a una nube en otro continente. LocalSend mueve archivos por tu red local con la placa mayor de esta página, y RustDesk abre el escritorio remoto con servidor que puedes alojar tú. Es el sótano de las copias (108) saliendo a pasear por la casa: lo tuyo viaja por tu aire, con tu ley.',
 placas=['localsend/localsend','rustdesk/rustdesk'],
 reglas=['La red local primero: si el archivo no sale de la casa, que tampoco salga el dato.','El servidor propio se monta pequeño y con su respaldo: soberanía sin bodega es discurso.','Contraseña y permiso por aparato: la confianza local también se firma.'],
 vara='La nube ajena es sala prestada: útil para visitar, jamás la única casa de tus cosas.',
 meme='—Subí el archivo a la nube para pasarlo al PC de al lado. —Viajó a otro continente para caminar dos metros.'),
'113': dict(slug='El-bolsillo-que-juega-Unciv-PPSSPP-y-Windows-en-el-telefono', titulo='El bolsillo que juega: Unciv, PPSSPP y Windows en el teléfono',
 esencia='Tres generaciones de la misma idea — el teléfono como máquina del tiempo — empujaron esta misma semana: el Civilization de bolsillo que se reescribe desde 2017, el emulador de PSP decano de 2012 y el Windows que se cuela en Android desde 2023. El juego libre y vivo no necesita tienda ni cuenta: necesita su forja, su release con fecha y un dueño que sepa de dónde bajó cada cosa.',
 placas=['yairm210/Unciv','hrydgard/ppsspp','brunodev85/winlator'],
 reglas=['La ROM y el juego, de tu propia copia: el emulador es libre, el contenido tiene dueño.','Release con fecha antes que “última versión” de un canal: la forja manda.','El bolsillo se calienta jugando a Windows: pausa, aire y batería cuidada con el termostato de la 94.'],
 vara='Jugar sin pedir permiso a una tienda es un derecho que se ejerce con procedencia: emulador de su forja, juego de tu estante.',
 meme='—En mi teléfono corre Windows, PSP y una civilización entera. —Y ninguna te pidió la tarjeta: así se juega en esta casa.'),
'114': dict(slug='La-red-con-vara-v2rayNG-ClashMeta-y-Orbot-en-tres-niveles', titulo='La red con vara: v2rayNG, ClashMeta y Orbot en tres niveles',
 esencia='La privacidad del tránsito viene en tres niveles y hoy los tres empujaron: la app que sale por su túnel (v2rayNG, con release de ayer), el proxy con reglas para todo el sistema (ClashMeta) y Tor para el teléfono entero (Orbot, con su RC de octubre). Elegir nivel es elegir cuánta casa cubre la sombrilla: una app, el sistema o cada petición que sale de tu bolsillo.',
 placas=['2dust/v2rayNG','MetaCubeX/ClashMetaForAndroid','guardianproject/orbot'],
 reglas=['Nivel declarado antes de navegar: qué sale por el túnel y qué no, escrito en la libreta.','El servidor del túnel tiene dueño conocido: gratis y anónimo es otra forma de entregar el dato.','La vara de siempre: tu red, tu cuenta, tu ley; la herramienta no se presta para casas ajenas.'],
 vara='El túnel no te hace invisible: te hace responsable de saber por dónde sale tu tráfico.',
 meme='—Con esto ya nadie me ve. —Te ve el dueño de tu túnel si no lo elegiste tú: la invisibilidad también tiene firmante.'),
'115': dict(slug='Descargar-con-fecha-YTDLnis-vivo-y-la-leccion-de-Seal', titulo='Descargar con fecha: YTDLnis vivo y la lección de Seal',
 esencia='Dos descargadores hermanas enseñan la lección entera de esta casa: YTDLnis soltó release el 19 de octubre y empujó ayer; Seal empuja código desde septiembre pero no publica release desde noviembre de 2024. Ni el empuje solo es salud ni la release vieja es muerte: son dos fechas distintas que se firman por separado, y el dueño que las confunde recomienda fantasmas y entierra vivos.',
 placas=['deniscerri/ytdlnis','JunkFood02/Seal'],
 reglas=['Se firman dos fechas siempre: último empuje y última release, en su línea cada una.','La APK sale de la release de SU forja: el código fresco sin release es cocina, no plato.','Descargar lo tuyo o lo libre: la herramienta baja, la procedencia la firma el dueño.'],
 vara='La fecha que no se distingue es la mentira que se repite: empuje y release son dos relojes, no uno.',
 meme='—Está vivo, mira el código. —Y la última release es de 2024: vivo en la cocina, ausente en la mesa; se firma así.'),
}
for pid in ['109','110','111','112','113','114','115']:
    d=P[pid]
    L=[f"# Publicación {pid} — {d['titulo']}\n","**La Bandita · 29 de octubre de 2026**\n",
       f"## ⚡ En una página\n\n{d['esencia']}\n","## 🗼 Las placas al pulso (29-oct-2026)\n"]
    for s in d['placas']: L.append(placa(s)+"\n")
    L.append("## 📦 Las reglas de la casa\n")
    for i,r in enumerate(d['reglas'],1): L.append(f"**{i}.** {r}\n")
    L.append(f"## ⚖ La vara\n\n{d['vara']}\n")
    L.append(f"## El meme de la pieza\n\n> {d['meme']}\n")
    L.append(f"> La Bandita verifica antes de recomendar: pieza {pid} del muro, nacida el 29 de octubre de 2026 de la investigación del mismo día, con placas re-medidas en su fuente primaria. Las estrellas adornan; las fechas mandan.\n")
    L.append("💓 *Pulso de nacimiento 29-oct-2026:* las placas de esta página se verificaron hoy. El futuro se firma con actividad y licencia, no con aplauso.")
    txt='\n'.join(L)+'\n'
    fn=f"{pid}-{d['slug']}-Facebook-La-Bandita-2026-10-29.md"
    (FB/fn).write_text(txt,encoding='utf-8'); print('escrita',fn,len(txt))
