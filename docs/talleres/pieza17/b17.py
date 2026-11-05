# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab17/docs/talleres/pieza17')
from d17 import *
A=AGG; T=[]; w=T.append
def f(r,nombre,texto): T.append(f"{ficha(r,nombre)}. {texto}\n")

w(f"""*⌨️ Los teclados de siempre · siete piezas sin una línea de IA*

Empiezo por los que **no** tienen IA: son la base de todo lo demás, y en este tema la palabra «IA» se usa para vender lo que a veces es un diccionario. Estos siete dibujan las teclas, aprenden tu vocabulario y **no llaman a ningún servidor**.

""")
f('HeliBorg/HeliBoard','HeliBoard',
  f"**{num(R['HeliBorg/HeliBoard']['stars'])} estrellas** y {num(R['HeliBorg/HeliBoard']['entregas'])} entregas: la bifurcación de OpenBoard, con diccionarios a mano y sin permiso de red. **{num(E['HeliBorg/HeliBoard']['adjuntos'])} adjuntos sin una suma** y {num(E['HeliBorg/HeliBoard']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['HeliBorg/HeliBoard']['incidencias']['cerradas'])} cerradas")
f('florisboard/florisboard','FlorisBoard',
  f"**{num(R['florisboard/florisboard']['stars'])} estrellas** y {num(R['florisboard/florisboard']['entregas'])} entregas: el motor de sugerencias más ambicioso del ecosistema abierto, y el que más tarda en llegar. **{num(E['florisboard/florisboard']['con_huella'])} sumas de {num(E['florisboard/florisboard']['adjuntos'])} adjuntos** —de los pocos de su grupo que firma— y {num(E['florisboard/florisboard']['incidencias']['abiertas'])} incidencias abiertas")
f('Julow/Unexpected-Keyboard','Unexpected Keyboard',
  f"**{num(R['Julow/Unexpected-Keyboard']['stars'])} estrellas** y **{num(R['Julow/Unexpected-Keyboard']['dias_nace'])} días de historia**: teclado para símbolos —deslizar saca flechas, tabulador y llaves—, sin permisos raros y con {num(R['Julow/Unexpected-Keyboard']['entregas'])} entregas")
f('AnySoftKeyboard/AnySoftKeyboard','AnySoftKeyboard',
  f"**{num(R['AnySoftKeyboard/AnySoftKeyboard']['dias_nace'])} días de vida**: el abuelo del tema, con {num(R['AnySoftKeyboard/AnySoftKeyboard']['entregas'])} entregas y diccionarios en más idiomas que ninguno. **{num(E['AnySoftKeyboard/AnySoftKeyboard']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['AnySoftKeyboard/AnySoftKeyboard']['incidencias']['cerradas'])} cerradas y {num(E['AnySoftKeyboard/AnySoftKeyboard']['adjuntos'])} adjuntos sin suma")
f('rkkr/simple-keyboard','Simple Keyboard',
  f"**{num(R['rkkr/simple-keyboard']['stars'])} estrellas** y {num(R['rkkr/simple-keyboard']['entregas'])} entregas: hace solo lo que promete, sin diccionario ni internet. **Sin integración continua** y {num(E['rkkr/simple-keyboard']['commits_30d'])} cambios en treinta días")
f('osfans/trime','Trime (Rime para Android)',
  f"**{num(R['osfans/trime']['stars'])} estrellas** y {num(R['osfans/trime']['entregas'])} entregas: la plataforma Rime en Android, con esquemas configurables y {num(E['osfans/trime']['adjuntos'])} adjuntos. Empujón de hoy, {num(R['osfans/trime']['dias_nace'])} días de vida")
f('scholay-xsime/xsime','XSIME',
  f"**{num(R['scholay-xsime/xsime']['dias_nace'])} días y {num(R['scholay-xsime/xsime']['stars'])} estrellas**: banco de trabajo de escritura sobre Rime, con **{num(E['scholay-xsime/xsime']['con_huella'])} sumas de {num(E['scholay-xsime/xsime']['adjuntos'])} adjuntos**. Su cola va al revés: {num(E['scholay-xsime/xsime']['incidencias']['abiertas'])} abiertas contra {num(E['scholay-xsime/xsime']['incidencias']['cerradas'])} cerradas")

w(f"""
**Lo que estos siete enseñan:** un teclado sin red es la única garantía de que lo que escribes no sale. Los siete declaran que no piden permiso de internet —y el que lo pide, lo dice—. Nada de la camada de IA que viene puede ofrecer eso con la misma limpieza: en cuanto hay un modelo, hay un archivo que descargar y una decisión sobre de dónde viene.

**Y el dato incómodo: de los siete, solo dos publican alguna suma** —FlorisBoard y XSIME—, {num(E['florisboard/florisboard']['con_huella']+E['scholay-xsime/xsime']['con_huella'])} archivos firmados entre todos.

───────────────────

*🎙️ El teclado que dicta · ocho piezas de bolsillo*

Aquí está el tema del día y el repositorio que lo abrió: ocho teclados de Android que **oyen**. La diferencia entre uno y otro está en los cinco pasos anteriores —dónde se transcribe, qué modelo, si corrige y qué hace con la voz—.

""")
f('DevEmperor/DictateKeyboard','Dictate Keyboard',
  f"**{num(R['DevEmperor/DictateKeyboard']['stars'])} estrellas y {num(R['DevEmperor/DictateKeyboard']['dias_nace'])} días** —el original, no la copia—: Whisper en el propio teléfono, {num(R['DevEmperor/DictateKeyboard']['entregas'])} entregas y **canal de seguridad**. {num(E['DevEmperor/DictateKeyboard']['adjuntos'])} adjuntos **sin una sola suma**: el que más confianza merece del grupo y el que peor lo pone para comprobarlo")
f('Batmancpu/Dictator-','Dictator- (el APK recompilado)',
  f"**{num(R['Batmancpu/Dictator-']['stars'])} estrellas y {num(R['Batmancpu/Dictator-']['dias_push'])} días desde el último empujón**: el repositorio que abrió este tema, y su descripción lo dice —*«el APK, yo no programo; el mérito es de la persona original, solo lo compilé»*—. Declara **Apache-2.0**, tiene canal de seguridad, {num(R['Batmancpu/Dictator-']['entregas'])} entregas y **{num(E['Batmancpu/Dictator-']['adjuntos'])} adjuntos sin suma**: es un binario ajeno")
f('soupslurpr/Transcribro','Transcribro',
  f"**{num(R['soupslurpr/Transcribro']['stars'])} estrellas** y licencia **ISC**: reconocimiento en el aparato como teclado **y** como servicio del sistema, para que cualquier app dicte sin nube. **{R['soupslurpr/Transcribro']['dias_push']} días sin publicar** y **sin integración continua**")
f('ElishaAz/Sayboard','Sayboard',
  f"**{num(R['ElishaAz/Sayboard']['stars'])} estrellas** y {num(R['ElishaAz/Sayboard']['entregas'])} entregas: dictado libre por Vosk, con modelos que caben en un teléfono modesto. **{R['ElishaAz/Sayboard']['dias_push']} días sin un empujón y cero cambios en treinta días**, con **{E['ElishaAz/Sayboard']['puntos']} puntos**")
f('notune/android_transcribe_app','Android Transcribe',
  f"**{num(R['notune/android_transcribe_app']['dias_nace'])} días de vida**: dictado **y** subtítulos en vivo, con Whisper local y {num(R['notune/android_transcribe_app']['entregas'])} entregas. {num(E['notune/android_transcribe_app']['adjuntos'])} adjuntos sin suma y {R['notune/android_transcribe_app']['dias_push']} días de quietud: el subtitulado es lo que casi nadie más tiene")
f('futo-org/voice-input','FUTO Voice Input',
  f"**El caso raro del tema**: {num(R['futo-org/voice-input']['stars'])} estrellas, **sin entregas, sin adjuntos y sin licencia legible** —es un espejo de un repositorio que vive fuera de GitHub—. {num(E['futo-org/voice-input']['incidencias']['abiertas'])} incidencias abiertas contra {num(E['futo-org/voice-input']['incidencias']['cerradas'])} cerradas: **aquí no se puede comprobar lo que se descarga**")
f('BryceWG/BiBi-Keyboard','BiBi Keyboard',
  f"**{num(R['BryceWG/BiBi-Keyboard']['stars'])} estrellas** y {num(R['BryceWG/BiBi-Keyboard']['entregas'])} entregas: combina reconocimiento y modelo de lenguaje **en la misma aplicación**. {num(E['BryceWG/BiBi-Keyboard']['commits_30d'])} cambios en treinta días y {num(E['BryceWG/BiBi-Keyboard']['adjuntos'])} adjuntos sin suma")
f('Akshayykadam/PixelBoard','PixelBoard',
  f"**{num(R['Akshayykadam/PixelBoard']['dias_nace'])} días y {num(R['Akshayykadam/PixelBoard']['stars'])} estrellas**: activa el dictado natural de un teléfono que no es el tuyo, sin root. {num(E['Akshayykadam/PixelBoard']['commits_30d'])} cambios en treinta días. **Depende de un servicio propietario**: aquí lo abierto es el envoltorio")

w(f"""
**El reparto retrata el tema.** Los tres de mejor nota —**Dictate Keyboard ({E['DevEmperor/DictateKeyboard']['puntos']})**, **BiBi** ({E['BryceWG/BiBi-Keyboard']['puntos']}), **PixelBoard** ({E['Akshayykadam/PixelBoard']['puntos']})**— tienen algo en común: alguien empuja cada mes. Los dos peores —**Sayboard ({E['ElishaAz/Sayboard']['puntos']})** y **FUTO ({E['futo-org/voice-input']['puntos']})**— llevan {R['ElishaAz/Sayboard']['dias_push']} y {R['futo-org/voice-input']['dias_push']} días sin publicar.

Y el detalle que da la pieza: **ninguno de los ocho firma un solo archivo.** {num(sum(E[r]['adjuntos'] for r in ['DevEmperor/DictateKeyboard','Batmancpu/Dictator-','soupslurpr/Transcribro','ElishaAz/Sayboard','notune/android_transcribe_app','futo-org/voice-input','BryceWG/BiBi-Keyboard','Akshayykadam/PixelBoard']))} adjuntos entre los ocho, **cero sumas**. Son programas que **escuchan** y cuyo instalador no se puede comprobar.

───────────────────

*🌱 La camada de 2026 en el bolsillo · cuatro nombres nuevos*

Lo nuevo de este año en Android no es «un teclado con IA»: es un teclado que **funciona sin red y sin cuenta**, con el modelo a la vista. Los cuatro de este bloque nacieron entre enero y septiembre de 2026 y tres de ellos empujaron hoy mismo.

""")
f('wasi-master/wmkeyboard','wmkeyboard',
  f"**{R['wasi-master/wmkeyboard']['dias_nace']} días y la segunda nota del tema ({E['wasi-master/wmkeyboard']['puntos']})**: inteligencia **en el aparato**, seiscientos idiomas y complementos. **{num(E['wasi-master/wmkeyboard']['adjuntos'])} adjuntos y {num(E['wasi-master/wmkeyboard']['con_huella'])} con suma**, {num(E['wasi-master/wmkeyboard']['commits_30d'])} cambios en treinta días y {num(E['wasi-master/wmkeyboard']['incidencias']['cerradas'])} incidencias cerradas contra {num(E['wasi-master/wmkeyboard']['incidencias']['abiertas'])} abiertas")
f('LeanBitLab/LeanType','LeanType',
  f"**{num(R['LeanBitLab/LeanType']['stars'])} estrellas en {num(R['LeanBitLab/LeanType']['dias_nace'])} días**: bifurcación de HeliBoard con lo que al original le falta y {num(R['LeanBitLab/LeanType']['entregas'])} entregas. {num(E['LeanBitLab/LeanType']['commits_30d'])} cambios en treinta días y **{num(E['LeanBitLab/LeanType']['adjuntos'])} adjuntos sin suma**")
f('Cyletix/CyIME','CyIME',
  f"**{num(E['Cyletix/CyIME']['commits_30d'])} cambios en treinta días** con {R['Cyletix/CyIME']['dias_nace']} días de vida: teclado sobre Rime con dictado local, subtítulos y varios esquemas. **Canal de seguridad**, {num(R['Cyletix/CyIME']['entregas'])} entregas y {num(E['Cyletix/CyIME']['con_huella'])} sumas de {num(E['Cyletix/CyIME']['adjuntos'])}")
f('zoolapp/aime','aime',
  f"**{num(R['zoolapp/aime']['dias_nace'])} días**: entrada sobre Rime para escritorio, local primero y la IA como opción. **{num(E['zoolapp/aime']['con_huella'])} sumas de {num(E['zoolapp/aime']['adjuntos'])} adjuntos**, {num(R['zoolapp/aime']['entregas'])} entregas y **{R['zoolapp/aime']['dias_push']} días de quietud**, con {num(R['zoolapp/aime']['stars'])} estrellas")

w(f"""
**Lo que tiene de nuevo esta camada**, leída en conjunto: **{num(A['nuevas2026'])} piezas de 2026, {num(A['nuevas'])} de los últimos noventa días y ninguna archivada**. Y un patrón claro: **tres de los cuatro son bifurcaciones o capas sobre Rime o HeliBoard**, no teclados escritos desde cero. Eso dice algo bueno del ecosistema —hay base para construir— y algo malo de la lista de siempre: los nombres que todo el mundo recomienda llevan años sin incorporar lo que estos cuatro ya tienen.

───────────────────

*💻 El dictado en la computadora · nueve piezas de escritorio*

En el ordenador no hay que sustituir un teclado: hay que **meter texto en el cursor de otra aplicación**, y eso en Wayland fue un problema de sistema durante años. Nueve piezas, todas locales, varias con mejor nota que cualquier teclado del teléfono.

""")
f('cjpais/Handy','Handy',
  f"**{num(R['cjpais/Handy']['stars'])} estrellas y {E['cjpais/Handy']['puntos']} puntos**: pulsas una tecla, hablas y el texto aparece en el cursor, en Mac, Windows y Linux. **{num(E['cjpais/Handy']['con_huella'])} sumas de {num(E['cjpais/Handy']['adjuntos'])} adjuntos** —la cifra más alta del tema— y {num(R['cjpais/Handy']['entregas'])} entregas")
f('anomalyco/hex','hex',
  f"**{R['anomalyco/hex']['dias_nace']} días y {num(E['anomalyco/hex']['commits_30d'])} cambios en treinta días** —el que más ha crecido del bloque—: dictado local para las tres plataformas, con **canal de seguridad** y {num(R['anomalyco/hex']['entregas'])} entregas. **{num(E['anomalyco/hex']['adjuntos'])} adjuntos sin una suma**")
f('Open-Less/openless','openless',
  f"**{num(R['Open-Less/openless']['entregas'])} entregas en {num(R['Open-Less/openless']['dias_nace'])} días**: mantienes, hablas, sueltas y el texto aparece pulido en cualquier aplicación. **{num(E['Open-Less/openless']['con_huella'])} sumas de {num(E['Open-Less/openless']['adjuntos'])} adjuntos** y {num(R['Open-Less/openless']['descargas'])} descargas")
f('altic-dev/FluidVoice','FluidVoice',
  f"**{num(R['altic-dev/FluidVoice']['stars'])} estrellas** y {num(R['altic-dev/FluidVoice']['entregas'])} entregas: dictado en el aparato con un modelo propio de mejora, para Mac. **Sin una sola suma** en {num(E['altic-dev/FluidVoice']['adjuntos'])} adjuntos: el más popular del bloque y el que peor se deja comprobar")
f('amicalhq/amical','Amical',
  f"**{num(R['amicalhq/amical']['descargas'])} descargas** —la más alta del tema en escritorio— y {num(R['amicalhq/amical']['entregas'])} entregas: dictado local con modelos abiertos. **{R['amicalhq/amical']['dias_push']} días de quietud** y **sin integración continua**")
f('peteonrails/voxtype','voxtype',
  f"**{num(E['peteonrails/voxtype']['adjuntos'])} adjuntos y {num(E['peteonrails/voxtype']['con_huella'])} con suma** —la mejor proporción de firma del tema—: pulsar-para-hablar en Wayland, donde el resto falla. {num(R['peteonrails/voxtype']['entregas'])} entregas, **canal de seguridad** y empujón de hoy")
f('VocaHQ/vocalinux','vocalinux',
  f"**La nota más alta de la pieza ({E['VocaHQ/vocalinux']['puntos']})**: dictado **100 % local para Linux** por whisper.cpp, Whisper y Vosk, con GPU opcional y **{num(E['VocaHQ/vocalinux']['con_huella'])} sumas de {num(E['VocaHQ/vocalinux']['adjuntos'])} adjuntos**. {num(R['VocaHQ/vocalinux']['entregas'])} entregas, **canal de seguridad** y **solo {num(E['VocaHQ/vocalinux']['incidencias']['abiertas'])} incidencias abiertas** contra {num(E['VocaHQ/vocalinux']['incidencias']['cerradas'])} cerradas")
f('karansinghgit/speaktype','speaktype',
  f"**{num(R['karansinghgit/speaktype']['dias_nace'])} días de vida**: dictado sin conexión para cualquier sistema, {num(R['karansinghgit/speaktype']['entregas'])} entregas y {num(E['karansinghgit/speaktype']['adjuntos'])} adjuntos. **Cero cambios en treinta días** y {num(E['karansinghgit/speaktype']['incidencias']['abiertas'])} abiertas contra {num(E['karansinghgit/speaktype']['incidencias']['cerradas'])} cerradas")
f('opennookorg/betterwispr','betterwispr',
  f"**El recién nacido del bloque: {R['opennookorg/betterwispr']['dias_nace']} días**, {num(E['opennookorg/betterwispr']['commits_30d'])} cambios en treinta días y {num(R['opennookorg/betterwispr']['entregas'])} entregas: mantienes un atajo, hablas y el texto se escribe en cualquier app de Mac. **Sin integración continua** y {num(E['opennookorg/betterwispr']['adjuntos'])} adjuntos sin suma")

w(f"""
**El hallazgo del bloque:** el dictado **de escritorio** está mejor mantenido que el del teléfono. **{palabras(A['push7'])} de las {palabras(A['vivos'])} piezas tienen código de la última semana** y la mitad de los nombres nuevos están aquí: en el ordenador sobra CPU para un modelo grande, y quien compite con una suscripción pone el listón más alto.

**Y el detalle que nadie cuenta:** cuatro de los nueve —**FluidVoice**, **openless**, **betterwispr** y **Amical**— son **solo para Mac**. Si usas Linux, tienes tres nombres buenos: **vocalinux**, **voxtype** y **Handy**.

───────────────────

*🔧 El motor y la corrección · seis piezas que van debajo*

Ninguna es un teclado y sin ellas no existiría ninguna de las anteriores. Van al final porque son la parte que se olvida, y deciden si el dictado acierta.

""")
f('ggml-org/whisper.cpp','whisper.cpp',
  f"**{num(R['ggml-org/whisper.cpp']['stars'])} estrellas y {num(R['ggml-org/whisper.cpp']['descargas'])} descargas**: Whisper en C/C++, corriendo en un teléfono, en una Raspberry y en un portátil sin tarjeta gráfica. {num(R['ggml-org/whisper.cpp']['entregas'])} entregas y {num(E['ggml-org/whisper.cpp']['commits_30d'])} cambios en treinta días: **el motor de la mitad de las piezas de esta lista**")
f('SYSTRAN/faster-whisper','faster-whisper',
  f"**{num(R['SYSTRAN/faster-whisper']['stars'])} estrellas**: la misma matemática con otra biblioteca y menos memoria, para servidores y equipos modestos. {num(R['SYSTRAN/faster-whisper']['entregas'])} entregas y **{num(E['SYSTRAN/faster-whisper']['incidencias']['abiertas'])} incidencias abiertas** frente a {num(E['SYSTRAN/faster-whisper']['incidencias']['cerradas'])} cerradas. **Sin adjuntos ni descargas publicadas**")
f('openai/whisper','Whisper (OpenAI)',
  f"**{num(R['openai/whisper']['stars'])} estrellas —el más famoso— y la nota más baja de los seis ({E['openai/whisper']['puntos']})**: {R['openai/whisper']['dias_push']} días sin un empujón, **cero incidencias** en su cola y cero cambios en treinta días. Sigue siendo la referencia del modelo; ya no es un proyecto con mantenimiento")
f('Automattic/harper','Harper',
  f"**{num(R['Automattic/harper']['stars'])} estrellas** y **empujón de hoy**: corrector gramatical en Rust, **sin conexión** y en microsegundos, pensado para revisar mientras escribes. {num(R['Automattic/harper']['entregas'])} entregas y {num(E['Automattic/harper']['incidencias']['abiertas'])} incidencias abiertas —mucha cola, es lo que tiene crecer—")
f('languagetool-org/languagetool','LanguageTool',
  f"**{num(R['languagetool-org/languagetool']['stars'])} estrellas y {num(R['languagetool-org/languagetool']['dias_nace'])} días**: el corrector con más idiomas y reglas del ecosistema abierto, instalable en tu propio servidor. **Cero entregas y cero adjuntos**, y {num(E['languagetool-org/languagetool']['incidencias']['abiertas'])} incidencias abiertas")
f('espanso/espanso','Espanso',
  f"**{num(R['espanso/espanso']['stars'])} estrellas** y {num(R['espanso/espanso']['entregas'])} entregas: expansor de texto multiplataforma —escribes `;mail` y sale tu correo entero—, con **{num(E['espanso/espanso']['con_huella'])} sumas de {num(E['espanso/espanso']['adjuntos'])} adjuntos** y **canal de seguridad**")

w(f"""
**Por qué esto va al final y es lo más importante.** Un teclado con IA es un envoltorio: el trabajo lo hace el motor. Si el motor está vivo —**whisper.cpp**, {num(E['ggml-org/whisper.cpp']['commits_30d'])} cambios al mes— el envoltorio puede permitirse ser flojo; si está parado —**Whisper de OpenAI**, {R['openai/whisper']['dias_push']} días— el envoltorio más bonito hereda el problema. **Elegir teclado sin mirar el motor es elegir la funda y no el teléfono.**

───────────────────
""")
open('/tmp/lab17/docs/talleres/pieza17/s2.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
