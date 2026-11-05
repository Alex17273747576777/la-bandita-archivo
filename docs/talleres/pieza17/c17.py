# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab17/docs/talleres/pieza17')
from d17 import *
A=AGG; T=[]; w=T.append

w(f"""*📊 La tabla completa de las {palabras(A['vivos'])} · lo medido, fila por fila*

El registro entero, ordenado por nota. La columna de firmas se repite en toda la pieza: **{num(A['con_huella'])} de {num(A['adjuntos'])}**.

| # | Recurso | Nota | ★ | Último empujón | Entregas | Sumas / adjuntos |
|---|---|---|---|---|---|---|
""")
for i,r in enumerate(sorted(VIVOS,key=lambda x:(-E[x]['puntos'],x)),1):
    e=E[r]; ea=R[r]
    w(f"| {i} | {r} | **{e['puntos']}** | {num(ea['stars'])} | {cuando(r).replace('**','')} | {num(ea['entregas'])} | {num(e['con_huella'])} / {num(e['adjuntos'])} |\n")
w(f"""
Leída en vertical dice tres cosas que ninguna lista de recomendaciones dice: **{palabras(A['con_huella_repos'])} de {palabras(A['vivos'])} firman algún archivo**, **{palabras(A['sin_ci'])} no tienen integración continua** y **{palabras(A['sin_entrega'])} no han etiquetado una sola versión**. **Lo que no mide**, y hay que decirlo: si el dictado acierta con tu acento o si el modelo cabe en tu teléfono. Eso no se ve desde la API; para eso está la semana de prueba.

───────────────────

*🎓 Glosario mínimo · diez palabras para no perderse*

- **IME**: el nombre técnico del teclado en Android, y una aplicación con permiso para inyectar texto en cualquier campo.
- **ASR**: el motor que convierte audio en texto. Lo que aquí se llama «el motor».
- **Whisper**: el modelo de reconocimiento liberado por OpenAI en 2022; de él salen las dos implementaciones de esta lista.
- **Local** (*on-device*): que el audio **no sale del aparato**. La palabra que cambia las consecuencias legales del asunto.
- **Diccionario propio**: los nombres que le das al motor para que no invente. Decide si entiende tu manera de hablar.
- **Corrección determinista**: aplica reglas y no inventa —LanguageTool, Harper—. La alternativa es que un modelo «pule» y cambie lo que dijiste.

───────────────────

*⚖️ La responsabilidad · tu voz, tus dedos y lo que el teclado ve*

Este tema tiene más letra pequeña que el de los torrentes, y por una razón sencilla: **un teclado no mueve archivos, ve lo que escribes**. No hace falta ser abogado para entender las cinco cosas que siguen; hace falta leerlas antes de instalar.

**Primero: el permiso.** En Android, un teclado es una aplicación con un permiso que el sistema no limita: puede leer el contenido del campo donde escribes y enviarlo a donde quiera. Eso incluye tus mensajes, tus búsquedas y **cualquier contraseña que escribas en una aplicación que no marque el campo como protegido**. Los teclados de esta lista que declaran no tener permiso de red no pueden enviar nada, ni queriendo. Es el único argumento de seguridad que no depende de la buena fe de nadie.

**Segundo: la voz es un dato biométrico.** No es un archivo cualquiera: identifica a una persona concreta, con su acento y su manera de hablar, y no se puede cambiar como una contraseña. En la República Dominicana la **Ley 172-13** sobre protección de datos personales trata los datos biométricos como sensibles; en la Unión Europea, el RGPD les da la misma consideración. **Esta pieza no da consejo legal**: dice que la pregunta existe y que la respuesta cambia según dónde vivas.

**Tercero: lo que dice «local» y lo que no.** «Funciona sin conexión» y «no envía tus datos» no son lo mismo: un programa puede transcribir en el aparato y pedir permiso de red para actualizarse o para mandar estadísticas. La prueba está en el manifiesto, no en la captura de pantalla; y de todo el tema, **vocalinux**, **voxtype** y **Handy** son los que lo dicen de forma más comprobable.

**Cuarto: el historial.** Varios teclados guardan lo que aprenden —las palabras nuevas, los nombres que repites— y ese archivo es, en la práctica, un diario de lo que escribiste. En un teléfono compartido, o en uno que vas a vender, es lo primero que hay que borrar. Ningún programa de esta lista te lo va a recordar.

**Quinto, el más incómodo: el APK que compiló otro.** **`Batmancpu/Dictator-`** es el ejemplo perfecto y por eso está medido: alguien tomó el código de **Dictate Keyboard**, lo compiló y lo publicó con su nombre, diciendo que no programa. Puede ser un favor limpio y **no se puede comprobar**: no hay suma ni compilación reproducible publicada. Cuando el programa escucha, eso deja de ser un detalle.

**Y la raya de esta casa.** No hay aquí ninguna lista de «prompts» que prometa obediencia: se miden programas, con fecha y con firma. **Un modelo no obedece: predice**, y quien promete obediencia al cien por cien está vendiendo otra cosa.

───────────────────

*🔏 La huella del tema · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}*

**{num(A['adjuntos'])} archivos publicados por las {palabras(A['vivos'])} piezas. {num(A['con_huella'])} con suma de comprobación. El 19,0 %.**
La segunda más alta del año. En su escala: tiendas de la 10, **0,08 %**; aplicaciones de la 11, **5,5 %**; torrentes de la 16, **8,7 %**; descarga de la 15, **10,6 %**; audio de la 13, **11,4 %**; kit de la 12, **17,0 %**; **teclados, 19,0 %**; música de la 14, **20,0 %**.

**{palabras(A['vivos']-A['con_huella_repos'])} de los {palabras(A['vivos'])} no publican ni una suma.** Los que sí:

""")
w("| Recurso | Adjuntos | Con suma | Nota |\n|---|---|---|---|\n")
for c_,a_,r in sorted([(E[r]['con_huella'],E[r]['adjuntos'],r) for r in VIVOS if E[r]['con_huella']],reverse=True):
    w(f"| {r.split('/')[1]} | {num(a_)} | **{num(c_)}** | {E[r]['puntos']} |\n")
w(f"""
Dos lecturas. La primera: **Handy firma {num(E['cjpais/Handy']['con_huella'])} archivos y voxtype {num(E['peteonrails/voxtype']['con_huella'])}**, y entre los dos ponen **dos tercios de las {num(A['con_huella'])} sumas** del tema: la cultura de firmar existe donde se publican binarios, no en la tienda. La segunda: **los ocho teclados de dictado de Android no firman ni uno**.

**Lo que se puede hacer hoy, y es poco.** Verificar la suma cuando se publica, instalar desde el gestor de paquetes —que al menos pasa por un mantenedor— y **no instalar APK recompilados por terceros** cuando hay original.

───────────────────

*🛠️ Seis órdenes para revisar este ecosistema tú mismo*

1. **Ver si el teclado sigue vivo.** `curl -s api.github.com/repos/<dueño>/<repo> | grep -E '"pushed_at"|"archived"|"license"'` — la fecha del último empujón y la licencia, sin abrir la página. Es lo que separa a wmkeyboard de Sayboard.
2. **Contar sus versiones.** `curl -s api.github.com/repos/<dueño>/<repo>/releases?per_page=100 | grep -c '"tag_name"'` — LanguageTool responde cero; wmkeyboard responde veintiséis.
3. **Buscar una suma.** `curl -s api.github.com/repos/<dueño>/<repo>/releases?per_page=100 | grep -Ei 'sha256|sha512|\\.sig|\\.asc' | head -5` — si imprime líneas, ese proyecto firma.
4. **Comprobar el permiso de red antes de instalar.** `aapt dump permissions app.apk | grep -i INTERNET` — sin esa línea, el teclado no puede enviar nada aunque quiera. Es la orden más útil de toda la pieza.
5. **Ver el tamaño del modelo.** `ls -lh ~/.local/share/<programa>/models/` — un modelo de 75 MB y uno de 3 GB no caben en el mismo teléfono, y el grande no siempre acierta más con tu acento.
6. **Borrar lo que aprendió.** El historial del teclado y su diccionario personal están en los ajustes de la propia aplicación; en Android, además, en su carpeta de datos. Antes de vender o prestar el teléfono, se vacían ahí y no en el historial visible.

Las órdenes **1 a 3** necesitan solo el nombre del programa en la dirección; las otras tres se ejecutan en tu equipo, sobre el archivo que acabas de bajar.

───────────────────

*🚪 Lo que esta pieza no tiene*

**Ni una sola receta de «prompts».** No hay armadura universal, ni fórmula de cinco pasos, ni etiquetas que prometan que el modelo obedecerá: eso no se mide. Lo que hay es lo que hace el trabajo —el motor, el teclado, el corrector— y el permiso.

**No es una lista de lo más nuevo.** Es un censo con fechas: {palabras(A['nuevas2026'])} piezas de 2026 ganan en nota, hay {palabras(A['nuevas'])} nacidas en los últimos noventa días, y también hay nombres parados con su fecha al lado —**Sayboard ({R['ElishaAz/Sayboard']['dias_push']} días)**, **Transcribro ({R['soupslurpr/Transcribro']['dias_push']})**, **Whisper ({R['openai/whisper']['dias_push']})**—.

**No hay aplicaciones cerradas.** Ni una: los grandes del dictado de pago no aparecen porque no se pueden medir —sin repositorio, sin licencia y sin archivo que comprobar—.

*📅 La semana de prueba · cinco días para tener un teclado que puedas comprobar*

- **Día uno.** Antes de instalar nada, mira qué teclado usas y qué permisos tiene (en Android: ajustes → aplicaciones → teclado → permisos). Casi todo el mundo descubre ahí que su teclado tiene acceso a la red.
- **Día dos.** Instala **HeliBoard** o **florisboard** y comprueba con la orden 4 que no piden internet. Se pierden los diccionarios automáticos y se gana no mandar lo que escribes.
- **Día tres.** Dicta con **Dictate Keyboard** o **Transcribro** y un **diccionario propio** con los nombres que usas: tu calle, tu trabajo, los apodos de tu casa. Sin esa prueba, todos fallan.
- **Día cuatro.** En la computadora, **Handy** si usas Windows o Mac y **vocalinux** si usas Linux. Si el texto dictado te obliga a releer dos veces, no te está ahorrando tiempo.
- **Día cinco.** Corrige con **Harper** o **LanguageTool** **sin generación** —reglas, no reescritura— y borra el historial del teclado con la orden 6.

───────────────────

*❓ Las preguntas del grupo*

**¿Cuál instalo, en una frase?**
**HeliBoard** si quieres un teclado que no hable con nadie; **wmkeyboard** o **Dictate Keyboard** para dictar en el teléfono; **Handy** o **vocalinux** en la computadora.

**¿El dictado manda mi voz a un servidor?**
Depende del programa, no de la palabra «IA» del anuncio. Los de esta lista transcriben en el aparato, pero eso no exime de mirar el permiso de red (orden 4). Si un teclado pide internet y dice ser local, una de las dos cosas es falsa.

**¿Por qué se equivoca con mi manera de hablar?**
Porque el modelo se entrenó con otra. No falla al azar: rellena con lo más probable de su entrenamiento, y en el Caribe eso son palabras que no usas. La solución no es un modelo más grande, es un **diccionario propio**.

**¿Sirve el teclado «con IA» de la tienda?**
Puede servir y no se puede comprobar: sin repositorio, sin licencia y sin suma. No lo recomiendo ni lo prohíbo; digo que en un programa que ve todo lo que escribes la comprobación no es un lujo.

**¿Y el `Batmancpu/Dictator-` que me pasaron?**
Es un APK compilado por un tercero que declara no programar, sobre el código de **Dictate Keyboard**, sin una sola suma publicada. **Usa el original**: {num(R['DevEmperor/DictateKeyboard']['stars'])} estrellas, {num(R['DevEmperor/DictateKeyboard']['entregas'])} entregas y canal de seguridad. No hay nada en el recompilado que no esté en el original, y sí hay algo que no puedes verificar.

**¿El dictado reemplaza al teclado?**
No: lo complementa, y solo en el registro en que se habla. Una nota de voz convertida a texto sale mejor que tecleada; un correo formal dictado suena a transcripción.

───────────────────

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **la tecla dejó de ser una tecla y el permiso sigue siendo el mismo**. Un teclado con IA oye, transcribe, corrige y reescribe, y conserva el acceso más amplio del sistema. **{palabras(A['push7'])} de las {palabras(A['vivos'])} piezas tienen código de esta semana**: la tecnología ya está; falta que la comodidad venga con la comprobación al lado.

Lo segundo: **el dictado de escritorio está mejor mantenido que el del teléfono**, y no es casualidad. Donde hay costumbre de publicar binarios hay firmas —**Handy y voxtype ponen dos tercios de las {num(A['con_huella'])} sumas**—; donde el instalador viaja por la tienda, nadie firma.

Lo tercero: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}, el 19,0 %**, la segunda mejor proporción del año, y concentrada en dos programas.

Y lo cuarto: **el nombre que más suena no es el que mejor está**. `openai/whisper` tiene {num(R['openai/whisper']['stars'])} estrellas y {E['openai/whisper']['puntos']} puntos, con {R['openai/whisper']['dias_push']} días de silencio; **vocalinux**, con {num(R['VocaHQ/vocalinux']['stars'])} estrellas, saca {E['VocaHQ/vocalinux']['puntos']}. En un tema donde el programa te escucha, la vara no premia la fama: premia que alguien esté ahí, publicando y firmando.

───────────────────
""")
w(f"""— {num(A['adjuntos'])} archivos publicados por {palabras(A['vivos'])} piezas y {num(A['con_huella'])} firmados: el 19,0 %, la segunda proporción más alta del año, con dos tercios puestos por dos programas de escritorio.
— Siete teclados sin IA, ocho que dictan en el bolsillo, cuatro de 2026 y nueve de escritorio: nombre, fecha, licencia y nota, sin una sola receta de «prompts».
— Cinco cosas que la letra pequeña decide —el permiso, la voz como dato biométrico, lo que «local» significa, el historial y el APK recompilado— y seis órdenes para comprobarlo antes de instalar.

💓 *La Bandita informa a partir de fuentes fechadas.* {palabras(A['vivos'])} piezas medidas hoy una por una —del teclado que no pide red al motor que transcribe, del dictado de escritorio al APK que compiló un desconocido—, la tabla completa, los {num(A['con_huella'])} archivos firmados contados uno por uno y el permiso que hay que leer antes de darle voz al teléfono.

───────────────────

*Medición del corte:* miércoles 4 de noviembre de 2026, {HORA} de la noche en Santo Domingo, con la fecha comprobada en vivo antes de empezar y al terminar · decimoctava medición del día · {palabras(A['vivos'])} piezas vivas, ninguna archivada, {palabras(A['sin_lic'])} sin licencia legible · {num(A['adjuntos'])} archivos y {num(A['con_huella'])} sumas · {num(A['descargas'])} descargas · {palabras(A['con_huella_repos'])} repositorios firmando.

*🔗 Enlaces*

*Los teclados de siempre:*
""")
GRUPOS=[("Los teclados de siempre, sin IA",['HeliBorg/HeliBoard','florisboard/florisboard','Julow/Unexpected-Keyboard','AnySoftKeyboard/AnySoftKeyboard','rkkr/simple-keyboard','osfans/trime','scholay-xsime/xsime']),
        ("El teclado que dicta · Android",['DevEmperor/DictateKeyboard','Batmancpu/Dictator-','soupslurpr/Transcribro','ElishaAz/Sayboard','notune/android_transcribe_app','futo-org/voice-input','BryceWG/BiBi-Keyboard','Akshayykadam/PixelBoard']),
        ("La camada de 2026 en el bolsillo",['wasi-master/wmkeyboard','LeanBitLab/LeanType','Cyletix/CyIME','zoolapp/aime']),
        ("El dictado en la computadora",['cjpais/Handy','anomalyco/hex','Open-Less/openless','altic-dev/FluidVoice','amicalhq/amical','peteonrails/voxtype','VocaHQ/vocalinux','karansinghgit/speaktype','opennookorg/betterwispr']),
        ("El motor y la corrección",['ggml-org/whisper.cpp','SYSTRAN/faster-whisper','openai/whisper','Automattic/harper','languagetool-org/languagetool','espanso/espanso'])]
usados=set()
for titulo,rs in GRUPOS:
    w(f"\n*{titulo}:*\n\n")
    for r in rs:
        usados.add(r); w(f"- https://github.com/{r}\n")
assert set(VIVOS)==usados, (set(VIVOS)-usados, usados-set(VIVOS))
w(f"""
*Las direcciones de las órdenes:*

- api de un repositorio cualquiera: https://api.github.com/repos/rhash/RHash
- api de las entregas: https://api.github.com/repos/wasi-master/wmkeyboard/releases?per_page=100

───────────────────

*🗒️ Notas al pie*

(4-nov) La fecha se comprobó **en vivo antes de empezar y al terminar**: `tools/fecha_viva.py --inicio` y `--fin` al cerrar. **Antes de sondear** se hizo la revisión obligatoria —fecha, historial y ecosistema— con `tools/preflight.py --tema teclado`; su acta está en `docs/PREFLIGHT-teclado-2026-11-05.json`. La medición es de las 03:17 y vive en `docs/MEDICION-17-noche-2026-11-04.json`; el escrutinio se rehízo entero y está en `docs/ESCRUTINIO-2026-11-05.json`.

(4-nov) **Este corte cambia el tema previsto.** El mapa de 125 pone en la 17 «la radio y el directo»; el dueño pidió el teclado con IA antes, y ese es el tema de esta pieza. La radio conserva su hueco y se hará con el mismo método.

(4-nov) **Lo que no se mide y por qué.** No hay recetas de ingeniería de «prompts»: no se pueden medir, ni fechar, ni comprobar. Se mide el programa que hace el trabajo. Un modelo **predice**; no obedece.

(4-nov) La cuenta de **huella** es la de toda la serie: `sha256`, `sha512`, `sha1`, `checksum`, `.sig`, `.asc` o `sums` en el nombre de cada adjunto de las últimas cien entregas. Escala completa: 0,08 % · 5,5 % · 8,7 % · 10,6 % · 11,4 % · 17,0 % · **19,0 %** · 20,0 %.

(4-nov) Las **notas** se calculan con los nueve pesos de la casa y las cuatro penalizaciones: **vocalinux saca {E['VocaHQ/vocalinux']['puntos']} con {num(R['VocaHQ/vocalinux']['stars'])} estrellas** y **Whisper {E['openai/whisper']['puntos']} con {num(R['openai/whisper']['stars'])}**. La vara no premia la fama.

(4-nov) **El taller queda en `docs/talleres/pieza17/`**, con los generadores del texto, para que las cifras se puedan repetir desde el repositorio (H22).

*#task*

#task 079 · volver a medir las {palabras(A['vivos'])} el 4 de diciembre y decir si Sayboard, Transcribro y Whisper publicaron: si no, salen de la recomendación.

#task 080 · comprobar con `aapt` el permiso de red de los ocho teclados de dictado y dejar el resultado en un acta con la fecha.

#task 081 · probar un diccionario propio en Dictate Keyboard y en wmkeyboard con diez palabras del español dominicano, y contar los aciertos antes y después.

#task 082 · escribir la pieza 18 —la radio y el directo, que este corte dejó pendiente— con el mismo método: preflight previo, medición fechada y ninguna cifra escrita a mano.

───────────────────

🏷️ Etiquetas estratégicas

#TecladoIA #DictadoPorVoz #Whisper #wmkeyboard #Vocalinux #Harper #LanguageTool #Espanso #HeliBoard #florisboard #Wayland #voxtype
""")
open('/tmp/lab17/docs/talleres/pieza17/s3.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
