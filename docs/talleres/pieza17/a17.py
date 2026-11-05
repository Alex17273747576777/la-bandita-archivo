# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'/tmp/lab17/docs/talleres/pieza17')
from d17 import *
A=AGG; T=[]; w=T.append

w(f"""*El teclado que escribe por ti: {palabras(A['vivos'])} teclados y dictados medidos hoy —{palabras(A['nuevas2026'])} de 2026, un APK que compiló un desconocido y la proporción de firma más alta del año—*

*La Bandita · miércoles 4 de noviembre de 2026, {HORA} de la noche en Santo Domingo · edición dominicano-español · pieza 17 de Facebook*

⏱️ *Lectura total: 30 minutos · {palabras(A['vivos'])} piezas medidas hoy a las {HORA} · {num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])} —el 19,0 %, la proporción más alta de la serie después de la 14— · {num(A['estrellas'])} estrellas · {num(A['descargas'])} descargas · {palabras(A['sin_lic'])} sin licencia legible · cero archivados · {palabras(A['nuevas2026'])} de 2026*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · la tecla que dejó de ser una tecla
├── ⚡ En una página
├── 🕰️ La medición de las {HORA} · la decimoctava del día
├── 🧠 Cómo funciona · del micrófono al cursor · y 🔁 qué reemplaza a qué
├── ⌨️ Los teclados de siempre · siete piezas sin una línea de IA
├── 🎙️ El teclado que dicta · ocho piezas de bolsillo
├── 🌱 La camada de 2026 en el bolsillo · cuatro nombres nuevos
├── 💻 El dictado en la computadora · nueve piezas de escritorio
├── 🔧 El motor y la corrección · seis piezas que van debajo
├── 📊 La tabla completa · 🎓 glosario · ⚖️ la responsabilidad
├── 🔏 La huella del tema · {num(A['con_huella'])} de {num(A['adjuntos'])} · y 🛠️ seis órdenes
└── 🚪 lo que no tiene · 📅 la semana · ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

> *Semilla de esta pieza:* un teclado era un dibujo de letras que avisaba al sistema de qué tecla habías pulsado. Hoy hay teclados que **oyen, transcriben, corrigen y reescriben** antes de que levantes el dedo —y para eso necesitan un permiso que, técnicamente, les deja ver **todo lo que escribes**—. Ese es el tema: la comodidad más grande del año y el permiso más invasivo del sistema.

Mide {palabras(A['vivos'])} piezas, todas vivas y ninguna archivada: siete teclados clásicos sin IA, ocho que dictan en el bolsillo, cuatro nombres de 2026, nueve programas de escritorio y seis piezas de motor y corrección por debajo. **Aquí no hay una sola receta de «prompts»**: se mide **el programa que hace el trabajo** —el que transcribe, el que corrige, el que escribe en el cursor—, con su fecha, su licencia y su nota.

Y la cifra que rompe la racha: **{num(A['con_huella'])} archivos firmados de {num(A['adjuntos'])}: el 19,0 %**, la segunda más alta del año. En un tema donde el programa **escucha y escribe**, que la descarga se pueda comprobar deja de ser una formalidad.

───────────────────

*⚡ En una página*

{palabras(A['vivos']).capitalize()} piezas, medidas hoy a las {HORA}: **{num(A['estrellas'])} estrellas**, **{num(A['descargas'])} descargas**, {palabras(A['push_hoy'])} con empujón de hoy, {palabras(A['push7'])} en la última semana y **cero archivados**. La nota mediana es **{num(int(A['mediana_puntos']))} sobre 80** —la más alta de la serie— y **solo {palabras(A['sin_lic'])} no declara licencia legible**: la mejor proporción de licencias del año.

Los mejores: **vocalinux** con **{E['VocaHQ/vocalinux']['puntos']}** —dictado para Linux que publica a diario y firma {num(E['VocaHQ/vocalinux']['con_huella'])} de {num(E['VocaHQ/vocalinux']['adjuntos'])} adjuntos—, **wmkeyboard** con **{E['wasi-master/wmkeyboard']['puntos']}** ({R['wasi-master/wmkeyboard']['dias_nace']} días y {num(E['wasi-master/wmkeyboard']['commits_30d'])} cambios al mes) y **Handy** y **openless** con **{E['cjpais/Handy']['puntos']}**. Ninguno es el nombre que más suena.

De actividad: **{palabras(A['push7'])} con código de la última semana**, {palabras(A['push_hoy'])} hoy y {palabras(A['ci'])} flujos de integración en total. De lo nuevo: **{palabras(A['nuevas'])} nacidos en noventa días** y {palabras(A['nuevas2026'])} en todo 2026. De lo que falta: **{palabras(A['sin_entrega'])} sin entrega** y **{palabras(A['sin_ci'])} sin integración continua**.

Y el caso que da el tono, con nombre y fecha: **`Batmancpu/Dictator-`**, un repositorio de **{num(R['Batmancpu/Dictator-']['stars'])} estrellas** cuya descripción dice, palabra por palabra, que el autor **no programa** y que solo compiló el APK de otra persona. Es el teclado que abrió este tema y está medido aquí como lo que es: un binario ajeno, con licencia Apache-2.0 declarada y sin una sola suma publicada.

───────────────────

*🕰️ La medición de las {HORA} · la decimoctava del día*

Antes de elegir nada se hizo la revisión que ya es regla: **fecha en vivo** ({HORA}), **historial** —dieciséis publicadas, la 17 en el mapa de 125 según lo previsto— y **ecosistema**: seis consultas a la API por fecha de creación y por tema, con acta en `docs/PREFLIGHT-teclado-2026-11-05.json` y {palabras(34)} candidatos. Después se midieron las {palabras(A['vivos'])} piezas a las {HORA}, en `docs/MEDICION-17-noche-2026-11-04.json`, y se rehízo el escrutinio entero: `docs/ESCRUTINIO-2026-11-05.json`.

**Una nota sobre el orden de los temas.** El mapa de 125 pone en la 17 «la radio y el directo». Este corte **no** la sigue: el dueño pidió el teclado con IA antes de seguir. Se dice y no se disimula; la radio sigue pendiente.

Las cinco notas más altas, con lo que las sostiene:

| Recurso | Nota | Lo que la sostiene | Lo que le falta |
|---|---|---|---|
| vocalinux | {E['VocaHQ/vocalinux']['puntos']} | {num(E['VocaHQ/vocalinux']['con_huella'])} sumas · {num(E['VocaHQ/vocalinux']['commits_30d'])} cambios al mes | {E['VocaHQ/vocalinux']['incidencias']['abiertas']} incidencias abiertas |
| wmkeyboard | {E['wasi-master/wmkeyboard']['puntos']} | {num(E['wasi-master/wmkeyboard']['adjuntos'])} adjuntos · {num(E['wasi-master/wmkeyboard']['commits_30d'])} cambios al mes | {R['wasi-master/wmkeyboard']['dias_nace']} días de vida |
| Handy | {E['cjpais/Handy']['puntos']} | {num(E['cjpais/Handy']['con_huella'])} sumas de {num(E['cjpais/Handy']['adjuntos'])} | sin canal de seguridad |
| openless | {E['Open-Less/openless']['puntos']} | {num(E['Open-Less/openless']['con_huella'])} sumas · {num(R['Open-Less/openless']['entregas'])} entregas | {E['Open-Less/openless']['incidencias']['abiertas']} abiertas |
| harper | {E['Automattic/harper']['puntos']} | corrector en Rust · empujón de hoy | {num(E['Automattic/harper']['incidencias']['abiertas'])} incidencias abiertas |

**La nota premia que se pueda comprobar, no que sea famoso.** `openai/whisper` tiene **{num(R['openai/whisper']['stars'])} estrellas** —el triple que todo el resto de la tabla junta— y saca **{E['openai/whisper']['puntos']}**: {R['openai/whisper']['dias_push']} días sin un empujón, sin adjuntos y sin una sola incidencia en su cola. En el otro extremo, **vocalinux**, con {num(R['VocaHQ/vocalinux']['stars'])} estrellas, saca **{E['VocaHQ/vocalinux']['puntos']}** porque publica, firma y atiende.

───────────────────

*🧠 Cómo funciona · del micrófono al cursor, en cinco pasos*

Esta sección sustituye a la receta de «prompts» que se suele publicar con este tema, porque una receta caduca y un mecanismo no. Lo que ocurre entre que hablas y el texto aparece en la casilla tiene cinco pasos, y **cada uno puede fallar por su cuenta**.

**Primer paso: alguien captura el audio.** El programa abre el micrófono mientras mantienes pulsada una tecla. Ahí ya hay dos decisiones: **cuándo empieza y cuándo corta** y **si ese audio se queda en el aparato o sale**. La mayoría de los programas de esta lista dicen que se queda; los que no lo dicen, no lo dicen.

**Segundo paso: un motor convierte el audio en texto.** Es la parte cara. Aquí hay tres familias: **Whisper** de OpenAI en sus dos implementaciones rápidas —**whisper.cpp**, que corre en cualquier cosa, y **faster-whisper**, la misma matemática con otra biblioteca—; los motores **propietarios en la nube**, que no se miden porque no son código abierto; y los **del sistema** de Android, que en algunos teléfonos ya son locales. La diferencia práctica: un modelo *large* transcribe mejor y pide varios gigabytes; uno *small* cabe en un teléfono de gama media y se equivoca con los nombres propios.

**Tercer paso: el idioma.** El motor no solo transcribe: **elige un idioma**, o lo detecta. Ahí empieza el problema del español del Caribe: un modelo entrenado con inglés y español neutro **no conoce** «motoconcho» ni «tíguere», ni come sílabas cuando hablas rápido. No falla al azar: rellena con lo más probable de su entrenamiento. Por eso casi todos estos programas aceptan **un diccionario propio** con los nombres que usas, y ese detalle —que no sale en ninguna captura— es el que decide si sirve o estorba.

**Cuarto paso: la corrección, que es otra pieza distinta.** Hay dos maneras de arreglar el texto y conviene no confundirlas. La **determinista** —un diccionario, un conjunto de reglas, **LanguageTool**, **Harper**— no inventa: cambia lo que está mal y deja lo demás. La **generativa** —un modelo que «pule» el texto— reescribe con criterio propio y puede cambiar lo que dijiste. Los programas de esta pieza se reparten entre las dos, y varios permiten apagar la generativa. **Mi consejo, y es el de esta casa: apágala hasta que confíes en el motor.** Un dictado que reescribe lo que dijiste no es un dictado, es un resumen de lo que dijiste.

**Quinto paso: meter el texto en el cursor.** Es el paso que casi nadie explica. Un teclado **es** el cursor: está dentro del sistema y escribe donde sea. Un programa de escritorio **no**: tiene que simular pulsaciones del teclado del sistema, y por eso depende del entorno —en Linux con Wayland eso fue un problema durante años y explica que exista **voxtype**, escrito solo para Wayland—. Si un dictado «no escribe en ninguna parte», casi siempre es este paso y no el motor.

**Y el sexto, que no es técnico: el permiso.** Un teclado es la aplicación con más acceso del teléfono: ve el texto de los campos donde escribes, sabe cuándo estás en una aplicación de banco y puede guardar un historial de todo. Por eso la sección de responsabilidad no va al final: es el corazón del tema.

───────────────────

*🔁 Qué reemplaza a qué · la tabla del teclado*

| Lo que usas hoy | Qué tiene de viejo | Qué lo cubre hoy |
|---|---|---|
| El teclado que vino con el teléfono | Manda lo que escribes según su política, que no eliges | **HeliBoard**, **florisboard** y **Unexpected-Keyboard**: código abierto, sin salida a la red |
| Dictar con el micrófono del sistema | Sube el audio a un servidor y depende de la cobertura del momento | **DictateKeyboard**, **Transcribro**, **wmkeyboard**: transcriben en el aparato |
| Un teclado «con IA» de la tienda | No sabes qué modelo, ni dónde, ni qué guarda | **CyIME**, **BiBi-Keyboard**, **PixelBoard**: el modelo y el repositorio a la vista |
| Dictar en la computadora | Pagar suscripción por minuto | **Handy**, **hex**, **openless**, **vocalinux**, **voxtype**: gratis y local |
| Corregir a mano cada frase dictada | Se pierde más tiempo del que ahorra el dictado | **Harper** y **LanguageTool** para las reglas; **espanso** para lo que repites |
| El motor que hay debajo | Un servicio cerrado que puede cambiar de precio | **whisper.cpp** y **faster-whisper**: se ejecutan en tu equipo |

**Una advertencia sobre esa tabla.** Ninguna de estas piezas «escribe mejor que tú»: quitan el tecleo de en medio. Un dictado sin revisar tiene el ritmo de quien habla, no de quien escribe —frases largas, muletillas y puntuación de quien no te oyó—. La revisión sigue siendo tuya, y la corrección por reglas es la que menos te cambia el texto mientras revisas.

───────────────────
""")
open('/tmp/lab17/docs/talleres/pieza17/s1.md','w',encoding='utf-8').write("".join(T))
print(len("".join(T)))
