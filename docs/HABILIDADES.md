# Habilidades · lo que esta casa sabe hacer porque antes se equivocó

Una habilidad no es una intención: es un procedimiento con un comando que se puede correr y un veredicto que se
puede perder. Cada una nace de un error concreto de `docs/ERRORES.md`, y si el error vuelve, la habilidad falló.

| # | Habilidad | Nace de | Se ejecuta con | Vigilante |
|---|---|---|---|---|
| H01 | **Medir antes de tocar** | E06, E10, E19 | `tools/remedir.py --escribir` | la fecha de la medición |
| H02 | **La cifra se cuenta, no se recuerda** | E02, E04, E05, E09, E12, E14 | `tools/remedir.py --pieza --medicion` | M29 + remedir |
| H03 | **La suma cuadra** | E03, E13 | `tools/remedir.py --suma` | lectura del acta |
| H04 | **Nada de copiar y pegar** | E06 | `tools/remedir.py --solape` | el solape con la versión vieja |
| H05 | **Sellar al final, después de verificar** | E16 | `make ritual` | CI |
| H06 | **Etiqueta específica o no hay etiqueta** | E01 | `tools/manual_gate.py` | M29 |
| H07 | **Las etiquetas viajan en el último mensaje** | E15, E18 | `tools/envio.py --verificar` | envio |
| H08 | **Una medición, un archivo, con hora** | E17 | `tools/remedir.py --escribir` | nombre con fecha |
| H09 | **Alinear la cifra en su línea** | E26, E27 | `tools/alinear.py` | remedir |
| H10 | **Un censo se repite o no se publica** | E30 | `tools/censo_tema.py` | lectura del censo |
| H11 | **La guía también se mide** | E25 | `tools/medir_guia.py --aplicar` | `guia-maestra` + remedir |
| H12 | **La fecha se lee en vivo, al empezar y al terminar** | E31 | `tools/fecha_viva.py --inicio` / `--fin` | `docs/FECHA-VIVA.json` |

## H01 · Medir antes de tocar

**Qué es.** Ninguna pieza se publica —ni se reedita— sin una medición del día. Antes de escribir una letra, cada
repositorio citado se abre en la fuente y se guarda lo que devolvió.

**Cómo.** `LBT=… python3 tools/remedir.py --escribir docs/MEDICION-01-2026-11-04.json --pieza <pieza>` Extrae los
`owner/repo` citados, los mide uno por uno y escribe un archivo con fecha **y hora**.

**Cómo se pierde.** Si el archivo de medición no es de hoy, `--pieza … --medicion …` falla y no deja publicar.

**Por qué nació.** Porque se añadieron etiquetas a cuatro piezas y se les cambió la fecha sin volver a medir. El
dueño lo llamó por su nombre y tenía razón.

## H02 · La cifra se cuenta, no se recuerda

**Qué es.** Toda estrella escrita con la forma `★N` tiene que existir en la medición del día. Toda cifra que se
afirme en prosa —«cuarenta entregas», «nueve de los doce»— se cuenta sobre la tabla antes de escribirla.

**Cómo.** `--pieza --medicion` compara el texto con la fuente y nombra cada cifra que no cuadra. Y para los
recuentos de prosa, la regla de la casa: si no se puede señalar la fila de la tabla que lo sostiene, no se escribe.

**Cómo se pierde.** Una sola cifra que no aparezca en la medición y el veredicto es «datos desactualizados».

**Por qué nació.** De siete cifras escritas de memoria en tres piezas distintas, dos de ellas falsas por completo.

## H03 · La suma cuadra

**Qué es.** Cuando una pieza dice «sumadas tienen tantas estrellas», esa suma se calcula con una orden, no de
cabeza, y la orden devuelve también la cifra en palabras para no transcribirla mal.

**Cómo.** `python3 tools/remedir.py --suma 138 122 101 72 40 37 21 17 17 18 16 15`

**Cómo se pierde.** Si los sumandos del texto no dan el total escrito, alguien lo va a notar. Y si el reparto por
licencia no suma el número de fichas, se nota todavía más rápido.

**Por qué nació.** Del «tres Apache» que dejaba once licencias donde había doce.

## H04 · Nada de copiar y pegar

**Qué es.** Reemplazar una pieza no es retocarla. Se escribe de nuevo, y si se reutiliza la estructura, el texto
de cada párrafo es nuevo.

**Cómo.** `python3 tools/remedir.py --solape <pieza-nueva> <pieza-vieja.md>` compara párrafos largos y da el
porcentaje copiado. El tope de la casa es **25 %**.

**Cómo se pierde.** Por encima del tope, el veredicto es literal: «es un retoque, no una pieza nueva».

**Por qué nació.** De la 01 etiquetada y con la fecha cambiada encima de los datos viejos.

## H05 · Sellar al final, después de verificar

**Qué es.** El orden del ritual no es un gusto: `libro` → `verificar` → `sellar` → comprobar el sello. Verificar
**escribe** (`registry/_vencimientos.json` se reescribe con la fecha del día), así que sellar antes deja un
archivo alterado y el CI cae.

**Cómo.** `make ritual` hace los tres pasos en el orden correcto.

**Cómo se pierde.** El flujo de GitHub ejecuta `atestar.py --verificar` y canta «1 alterados o ausentes».

**Por qué nació.** De un CI en rojo por sellar primero.

## H06 · Etiqueta específica o no hay etiqueta

**Qué es.** Entre ocho y doce etiquetas por pieza, sin genéricas, sin tildes, con al menos el setenta por ciento
ganadas con sus palabras en el cuerpo.

**Cómo.** `tools/manual_gate.py` regla **M29**, con la lista negra de `docs/POLITICA-ETIQUETAS.md`.

**Por qué nació.** De cuatro piezas publicadas sin etiquetas.

## H07 · Las etiquetas viajan en el último mensaje

**Qué es.** El bloque de etiquetas se coloca en el cierre del envío, no entre el cuerpo, y el generador de envíos
lo mueve allí sin tocar el resto del texto.

**Cómo.** `tools/envio.py --generar` y luego `--verificar`, que comprueba que no se perdió ni una línea.

**Cómo se pierde.** El verificador dice cuántas líneas del cuerpo no llegaron al envío y nombra el párrafo.

**Por qué nació.** De haber perdido la última nota al pie y los tres `#task` al mover el bloque.

## H08 · Una medición, un archivo, con hora

**Qué es.** Cada medición se escribe en su propio archivo, con fecha y hora en el nombre y en el contenido. Nunca
se sobrescribe la anterior: si dos mediciones del mismo día discrepan, es un dato, no un problema.

**Cómo.** `--escribir docs/MEDICION-01-2026-11-04.json` y, si hace falta otra, `…-2026-11-04-b.json`.

**Por qué nació.** De un archivo de medición sobrescrito con un subconjunto de veintiséis repos.

## H09 · Alinear la cifra en su línea

**Qué impide.** Que la fuente mueva siete estrellas y la pieza siga publicando las de ayer en siete párrafos distintos.

**Cómo se hace.** `python3 tools/alinear.py --pieza <pieza.md> --medicion docs/MEDICION-XX-2026-11-04.json --aplicar`.
Solo toca el número pegado a ★, y solo en líneas que nombran **un** repositorio medido; si la línea nombra dos, no
toca nada e informa. Imprime cada cambio con su número de línea.

**Cómo se pierde.** Cuando alguien «arregla» a mano y olvida una línea. El programa no se olvida, pero tampoco adivina:
si una cifra no está pegada a ★, la cambia una persona, no esta habilidad.

## H10 · Un censo se repite o no se publica

**Qué impide.** Publicar «ciento doce proyectos de audio nacidos en el año» sin que nadie pueda volver a contar ciento doce.

**Cómo se hace.** `python3 tools/censo_tema.py --tema audio --json docs/CENSO-audio-2026-11-04.json`. El programa
declara sus palabras de búsqueda, su ventana y el denominador (las fichas del registro con su evidencia sellada).

**Cómo se pierde.** Cambiando las palabras entre una medición y otra sin decirlo. Por eso las palabras van en el
archivo de salida y en la pieza.

## H11 · La guía también se mide

**Qué impide.** Que las setenta fichas de la guía maestra envejezcan en silencio, porque el texto se lee bien igual.

**Cómo se hace.** `python3 tools/medir_guia.py --aplicar` mide las setenta con la API y con `tools/escrutinio.py`,
escribe `guia-maestra/datos/medicion-<fecha>.json` y guarda la señal anterior en `datos/_senal-anterior/<fecha>/`.
Después, `guia_maestra.py --generar` rehace créditos, índice, sitio y páginas.

**Cómo se pierde.** Aplicando sin generar: los datos cambian y el sitio sigue diciendo lo de ayer.

## H12 · La fecha se lee en vivo, al empezar y al terminar

**Qué impide.** Firmar un censo con la fecha del reloj de la casa cuando ese reloj es justo el que
se queda atrás: un apagón de dos horas basta para que una medición de la tarde se publique con el
día de ayer, o para que dos piezas del mismo día lleven fechas distintas.

**Cómo se hace.** `python3 tools/fecha_viva.py --inicio` antes de tocar nada, y `--fin` al cerrar.
El programa pregunta la hora **a GitHub** —fuente de fuera, no de esta máquina—, compara con el
reloj local y dice el desfase en minutos. Anota las dos lecturas en `docs/FECHA-VIVA.json` y, al
cerrar, exige que el censo haya empezado y terminado **el mismo día**: si no, se vuelve a medir.

**Cómo se pierde.** Escribiendo la fecha de memoria en el encabezado de la pieza mientras el
programa dice otra cosa. La pieza y el acta tienen que decir lo mismo, y las dos salen de la
misma lectura.

## H13 · Buscar la palabra, no la forma del nombre

**Qué impide.** Que una compuerta cuente cero porque el archivo se llama de una manera que el
detector no previó: Bitwarden publica `com.x8bit.bitwarden.apk-sha256.txt` y el detector, que
buscaba `.sha256` con punto o `sha256sum`, no lo veía. Una pieza habría publicado «ninguna de las
catorce firma» con una de ellas firmando quince archivos.

**Cómo se hace.** Antes de creer un cero, mirar **los nombres reales** de lo que se está contando,
a mano, en la página de entregas de un repositorio del lote. Y en el código, buscar la palabra en
cualquier posición (`MARCAS = ("sha256", "sha512", "sha1", "checksum", ".sig", ".asc", "sums")`)
en lugar de componer sufijos.

**Cómo se pierde.** Confiando en el cero: un cero es el resultado más sospechoso que da un
detector, porque es también lo que devuelve cuando está roto. Y cuando se cambia un detector, se
vuelven a pasar las piezas ya publicadas de la serie para ver si sus cifras se mueven.

## El ritual completo, con las habilidades dentro

```
make libro                                     # tablero, índice y tareas
LBT=… python3 tools/remedir.py --escribir docs/MEDICION-<pieza>-<fecha>.json --pieza <pieza>
LBT=… python3 tools/remedir.py --pieza <pieza> --medicion docs/MEDICION-<pieza>-<fecha>.json
python3 tools/manual_gate.py --pieza <pieza>   # forma y M29
python3 tools/novedad_gate.py <pieza> --corte <fecha>
python3 tools/remedir.py --solape <pieza-nueva> <pieza-vieja>     # si reemplaza a otra
LBT=… python3 tools/envio.py --medir --generar --verificar
make ritual                                    # verificar y después sellar
git commit && git push                         # y esperar el CI
```
