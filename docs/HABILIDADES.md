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
