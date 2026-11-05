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
| H16 | **La banda se mide en caracteres** | E36 | `python3 tools/manual_gate.py --pieza` | M11 |
| H18 | **El título se calcula, no se recuerda** | E38 | `python3 tools/manual_gate.py --pieza` | el nombre del archivo |
| H19 | **El día se cuenta en la hora de la casa** | E39 | `tools/remedir.py --escribir` | la columna del empujón |
| H20 | **Ningún enlace vetado en una pieza del canal que lo veta** | E40 | `tools/envio.py --verificar` · `grep` de la familia | el cuerpo y el bloque de enlaces |
| H21 | **El historial y el ecosistema se revisan antes de sondear** | E41 + regla del dueño | `tools/preflight.py --tema` | el punto de partida de cada pieza |
| H22 | **El almacén es GitHub; el disco de trabajo es efímero** | E41 | `git push` en el mismo turno · talleres en `docs/talleres/` | todos los resultados |
| H23 | **La cifra se busca en el diccionario que la tiene** | E42 | `E` = escrutinio (sumas, adjuntos, commits, incidencias) · `R` = medición (estrellas, entregas, licencia, días) · `python3 b16.py` antes de ensamblar | cada taller nuevo |
| H24 | **Una tienda se cuenta, no se cita** | E43 | `repo.json` → `index.json` → contar entradas · `archived` y `pushed_at` de la API · `signingKey` · seguir la redirección · leer la descripción del autor | cada lista de repositorios o tiendas |
| H17 | **La madurez se declara ficha a ficha** | E37 | `python3 tools/novedad_gate.py` | M25 |

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

## H14 · Separar lo declarado de lo fallado

**Nace de E34.** Una compuerta que solo sabe decir «bien» o «mal» obliga a esconder el caso raro, y
el caso raro suele ser el que da interés a la pieza: un repositorio bloqueado por un aviso legal, un
paquete que no existe porque el proyecto nunca publicó, una dirección que redirige a otro nombre.

**La regla.** Si una fuente responde algo distinto de lo esperado **hoy y de forma comprobable**
(451, 404, archivado, sin entregas), eso no es un dato viejo: es un dato. La herramienta lo avisa, la
pieza lo declara con su código y su fecha, y la compuerta no lo cuenta como fallo. Lo que sí sigue
siendo fallo es una cifra que no coincide con lo medido.

**Cómo se pierde.** Metiendo el caso raro en el mismo saco que el error: la pieza acaba ocultando lo
que más enseña para poder pasar en verde. Y al revés: marcando como «declarado» cualquier cosa, hasta
que la compuerta no sirve para nada. La frontera es la fecha: se declara lo que se midió hoy.

## H15 · Un censo es una orden, no una tarde

**Nace de E35.** Contar a mano se siente como rigor y es lo contrario: el número existe, pero no se
puede repetir, y lo que no se repite no se puede discutir ni corregir. La pieza 06 publicó un censo
de 57 fichas que solo vivía en la memoria de quien lo contó.

**La regla.** Ninguna pieza publica un total de fichas que no salga de una orden escrita en el
repositorio. Si el tema no está en la herramienta, se añade **antes** de escribir la pieza, con sus
palabras a la vista, y se corre delante de quien quiera comprobarlo. La herramienta imprime sus
palabras y su ventana, así que el número lleva su método pegado.

**Cómo se pierde.** Añadiendo palabras hasta que el tema lo abarque todo: entonces el censo dice
«cuatrocientas fichas» y no dice nada. La disciplina es la contraria: pocas palabras, declaradas, y
la diferencia entre la cuenta a mano y la de la máquina se publica en vez de esconderse.

## H16 · La banda se mide en caracteres, no en bytes

**Nace de E36.** `wc -c` devuelve bytes y la compuerta M11 compara caracteres. En esta casa el texto
va lleno de acentos, estrellas y rayas largas, así que la diferencia entre las dos cuentas pasa de dos
mil unidades en una pieza de cuarenta mil: suficiente para recortar media sección de más o para
publicarse fuera de banda creyendo que se va dentro.

**La regla.** La longitud se consulta **con la compuerta**, nunca con `wc -c` ni a ojo:
`python3 tools/manual_gate.py --pieza <archivo>` imprime el número exacto que se compara con la banda.
Se recorta y se vuelve a preguntar, en ese orden y no al revés.

**Cómo se pierde.** Recortando a ciegas hasta que «parezca» que cabe: el resultado es una pieza más
pobre y la misma duda. La compuerta existe para que esa duda no se resuelva adivinando.

## H17 · La madurez se declara ficha a ficha

**Nace de E37.** El testigo de novedad no lee la pieza entera: lee párrafos. Un bloque con una ficha
joven —menos de cien estrellas— tiene que llevar la palabra «madurez» dentro, y no vale que esté en
la sección de método tres pantallas más arriba.

**La regla.** Cada ficha que baja de cien estrellas declara sus días de vida en su propia línea, y el
generador lo hace solo (`ficha_c` en el taller de la pieza): la cifra no se escribe a mano, se toma de
la medición del día. Así la pieza no puede declarar una madurez que no midió.

**Cómo se pierde.** Escribiendo «madurez» una vez en la cabecera del bloque para callar la compuerta.
El lector de la ficha se queda sin el dato y la compuerta pasa: forma sin oficio, que es el error que
esta casa lleva todo el día cazando.

## H18 · El título se calcula, no se recuerda

**Nace de E38.** El nombre de la pieza es lo primero que se lee —índice, envío, tablero— y es también lo
último que se revisa. En la pieza 11 llevaba una cifra que no era la de la medición: ciento diecisiete
mil descargas donde el archivo decía cincuenta y ocho millones. El texto estaba bien; el título, no.

**La regla.** La cifra del nombre se copia de la variable que ya salió de la medición, nunca se teclea.
Y antes de sellar, el nombre se lee en voz alta contra la tabla: si la cifra del título no está en el
cuerpo, el título está inventando.

**Cómo se pierde.** Escribiendo el nombre al final, con prisa, cuando ya está todo lo demás hecho. El
título es parte del dato, no la etiqueta del dato.

## H19 · El día se cuenta en la hora de la casa

**Nace de E39.** GitHub fecha en UTC y la casa fecha en Santo Domingo. A las 20:38 locales ya es el día
siguiente en UTC, así que tres repositorios con empujón reciente salieron con «−1 días» y el recuento
de empujones del día se quedó tres corto. Un número negativo no es un detalle: es una compuerta que
miente hacia abajo.

**La regla.** Toda resta de fechas se hace contra el día de la casa (`America/Santo_Domingo`), y un
empujón con fecha posterior al corte se cuenta como hoy, no como mañana. La herramienta ya lo hace:
`tools/remedir.py` toma la zona de la casa y recorta el negativo a cero.

**Cómo se pierde.** Usando `date.today()` a secas, que en el servidor devuelve UTC y en la computadora
del dueño no. La fecha de la casa es la única que vale, y por eso hay un programa que la lee en vivo.

## H20 · Ningún enlace vetado en una pieza del canal que lo veta

**Nace de E40.** Facebook retiró la pieza 12 por un solo enlace: un buscador de índices de torrentes.
El programa no era ilegal ni el dato era falso; el criterio de la plataforma no distingue matices. Una
pieza que se cae a los veinte minutos no informa a nadie, por muy bien medida que esté.

**La regla.** En una pieza de Facebook no se enlaza **ningún indexador ni cliente de torrentes**
(buscadores de índices, clientes, sembradores, herramientas de cruce). De esa familia se dan el
**nombre**, lo que hace y **cómo se comprueba** —la orden de `curl` con la que cualquiera ve su estado
en GitHub—, y las direcciones viajan solo en la versión de WhatsApp. Se revisa con
`grep -i` sobre el envío generado antes de publicar, y la compuerta M07 obliga a que toda URL del
cuerpo esté en la lista de enlaces para poder revisarlas de un vistazo.

**Cómo se pierde.** Escribiendo la pieza desde el catálogo del tema en vez de desde el canal: lo que
está bien documentado no siempre está permitido. Y confiando en que «un enlace de GitHub es inocente».

## H21 · El historial y el ecosistema se revisan antes de sondear

**Nace de la regla del dueño (4-nov-2026, noche).** Antes de elegir candidatos de una pieza se mira,
en este orden: **la fecha en vivo**, **qué está ya publicado y qué toca** según el mapa de 125, y
**el ecosistema** —GitHub por fecha de creación y por tema—. Sondear primero y mirar el historial
después produce piezas que repiten tema y párrafos que ya estaban escritos.

**La regla.** `tools/preflight.py --tema <tema>` hace las tres cosas y deja acta. No se escribe una
ficha que no venga de ese censo previo.

**Cómo se pierde.** Abriendo el editor antes que el historial: es cómo se escriben dos piezas del
mismo tema con tres semanas de diferencia y no se nota hasta que la compuerta de solape lo dice.

## H22 · El almacén es GitHub; el disco de trabajo es efímero

**Nace de E41.** En una sola noche se perdió dos veces el trabajo local: una carpeta que el entorno
no conserva y un directorio que amaneció revertido. Lo empujado, intacto.

**La regla.** Se empuja **en el mismo turno** en que se produce el resultado. Los clones viven en
`/tmp` y se rehacen; los talleres (los generadores del texto) se guardan en `docs/talleres/pieza-NN/`
dentro del repositorio, porque un número que no se puede repetir desde el repositorio no es un dato,
es un recuerdo.

**Cómo se pierde.** Diciendo «lo subo al final». El final, en un taller que se corta, no llega.

## H23 · La cifra se busca en el diccionario que la tiene

**Nace de E42.** Los dos primeros guiones de la pieza 16 murieron por pedirle al diccionario
equivocado una cifra que existía en el otro. La medición (`R`) trae estrellas, entregas, licencia y
días; el escrutinio (`E`) trae adjuntos, sumas, cambios en treinta días e incidencias. Confundirlos
no da un número falso: da un `KeyError`, que es el fallo bueno.

**La regla.** Antes de ensamblar la pieza se ejecuta cada generador y se mira la salida. Un guion que
no corre a la primera se arregla en el taller y no se toca el texto publicado.

**Cómo se pierde.** Sustituyendo el `KeyError` por un `R.get(campo, 0)`: el texto sale, y con un cero
donde había una cifra. Ese sí llega a la calle.

## H24 · Una tienda se cuenta, no se cita

**Nace de E43.** La lista de tiendas de extensiones que circulaba tenía seis cifras de seis mal,
porque venía de una wiki que nadie volvía a medir. No hubo error de cálculo: hubo **cita sin
comprobación**.

**La regla.** Antes de nombrar una tienda se abren su `repo.json` y su índice, se cuentan las
entradas, se mira si el repositorio está archivado, si el índice declara clave de firma y si la
dirección que circula redirige a otra. Y antes de incluir un repositorio se lee su descripción: si
el autor dice que no programa, que no hay soporte o que es un espejo, se cree al autor.

**Lo que no se hace.** No se indexa por estrellas —hay un plugin de 24 estrellas con **una** sola
extensión—, no se duplican clones renombrados y no se meten repositorios cuyo nombre es una
dirección. **El listón sube con menos y mejores**, no con más enlaces.

**Cómo se pierde.** Volcando: cuando una lista crece más rápido de lo que se comprueba, deja de ser
una lista y pasa a ser ruido, y el trabajo de comprobarlo se le cae encima a quien la lee.

## El ritual completo, con las habilidades dentro



```
LBT=… python3 tools/preflight.py --tema <tema>  # fecha + historial + ecosistema (H21)
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
