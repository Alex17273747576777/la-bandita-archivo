# EL CÓDIGO, EXPLICADO

*Cada componente de esta casa, dicho como se lo explicaría a alguien inteligente que nunca programó. Actualizado el 3 de noviembre de 2026.*

**TL;DR —** hay **31 herramientas** en `tools/` y un generador dentro de `guia-maestra/`. Ninguna hace dos cosas: cada una recibe algo, hace una sola cosa con eso y escribe un resultado que otra puede comprobar. Este documento explica las 31 con la misma estructura —qué recibe, qué hace, qué produce y **qué no hace**— porque en un archivo que presume de verificar, saber el límite de cada programa vale más que saber su función.

---

## Cómo leer esto si no programás

Un programa es una receta: entra un ingrediente, se hace un paso, sale un plato. Lo único que hay que entender de un código para juzgarlo es **qué entra y qué sale**, y si el paso intermedio se puede revisar. Todo lo demás son detalles de cocina.

Así se lee cualquier herramienta de esta casa:

1. **Qué recibe** — un archivo, una carpeta, una dirección de internet o nada.
2. **Qué hace** — siempre una cosa, y siempre la misma con la misma entrada.
3. **Qué produce** — otro archivo, una línea por pantalla, o un número que se guarda.
4. **Qué no hace** — el límite. Aquí está la diferencia entre una herramienta honesta y una que promete de más: la honesta dice qué no toca.

Y una regla que se repite en las 31: **ninguna aprueba nada diciendo «cero errores»**. Se aprueba cuando el informe dice una frase concreta, y esa frase se busca letra por letra en la integración continua. Un programa que se calla no es un programa que está de acuerdo.

---

## 1 · El reloj y la medida

Todo lo que esta casa afirma tiene una fecha. Este primer grupo es el que pone el reloj, mide la fuente primaria y convierte lo medido en una ficha.

**`fecha_casa.py`** · *45 líneas*
Recibe nada. Devuelve el día de la casa —Santo Domingo, no el del servidor— en formato ISO y en formato largo. Existe porque en un archivo con diez mil archivos sellados la fecha aparece en cientos de sitios y basta con que dos usen husos distintos para que la verificación se caiga sola a medianoche. **No hace:** no adivina la zona horaria, la declara.

**`pulso.py`** · *430 líneas*
Recibe una lista de repositorios. Pregunta a la fuente primaria **doce cosas por repositorio** —estrellas, fecha de creación, último empujón, licencia, tamaño, incidencias, entregas, descargas, equipo— y las guarda con la respuesta cruda al lado. **No hace:** no opina ni puntúa; solo mide y archiva. La puntuación es de otro.

**`censo_medir.py`** · *el que mide de verdad* — explicado entero en la §7
Recibe el registro anterior y vuelve a medir contra la fuente primaria, cincuenta repositorios por consulta. **No hace:** no borra una ficha porque el proyecto se murió; la marca.

**`extraer_fresco.py`** · *218 líneas*
Recibe una fuente —una búsqueda, una lista, un archivo— y se queda solo con lo que existe **hoy**, medido hoy. **No hace:** no recicla números de una corrida anterior, y por eso se llama fresco: si un dato es de ayer, no entra.

**`ficha_profunda.py`** · *195 líneas*
Recibe un repositorio ya elegido y abre lo que hay que abrir antes de recomendar: licencia leída del archivo, últimas diez entregas, equipo, cola de incidencias, README. **No hace:** no decide si el proyecto es bueno; reúne la evidencia para que la decisión se pueda discutir.

**`escrutinio.py`** · *269 líneas*
Recibe la evidencia profunda y devuelve **la nota de 0 a 100**, con nueve señales de peso declarado y cuatro castigos —licencia 15, integración 10, huella 10, entrega 10, actividad 10, equipo 10, cola 10, seguridad 5, mérito 20; menos 30 si está archivado, 10 sin adjuntos, 15 por atención anómala, 5 por una sola persona—. **No hace:** no mide la calidad del programa, mide si el proyecto está en condiciones de que le pongas tus datos encima. La diferencia está escrita en su cabecera porque se confunde todo el tiempo.

**`merito.py`** · *150 líneas*
Recibe un repositorio y consulta el Scorecard de OpenSSF, la puntuación independiente de la fundación. **No hace:** no lo inventa cuando no existe. Si no hay dato, lo dice, y ese hueco es el que deja la nota máxima en 80 de 100 en las setenta fichas de la guía.

**`licencias_resolver.py`** · *222 líneas*
Recibe las fichas cuya licencia la plataforma no supo identificar y **abre el archivo de licencia** para resolverlo a mano. Así se descubrió que Kodi es GPL-2.0-o-posterior y no «desconocida», que ESPHome mezcla MIT y GPL-3.0 y que Termux es GPL-3.0 con excepciones. **No hace:** no adivina por el nombre del archivo ni por la fama del proyecto.

**`swhid.py`** · *155 líneas*
Recibe una revisión medida y le pide al archivo público de Software Heritage que la conserve, devolviendo un identificador citable. **No hace:** no garantiza que el pedido se complete; anota el número de solicitud para poder reclamarlo.

**`tres_lecturas.py`** · *207 líneas*
Recibe una medición y la hace **tres veces por tres caminos distintos** —interfaz de programación, HTML público y archivo— para ver si los tres coinciden. **No hace:** no elige la respuesta que más le gusta cuando discrepan; publica la discrepancia.

**`descubrir.py`** · *105 líneas*
Recibe una fuente de texto y extrae los repositorios que menciona, cruzados contra el registro para no repetir. **No hace:** no recomienda lo que encuentra; lo pone a la cola de medición.

---

## 2 · Las compuertas

Una compuerta no es un consejo: **detiene la línea**. Este grupo es el que decide si algo puede salir.

**`vara.py`** · *513 líneas*
Ejecuta las **quince compuertas G0 a G15** en un solo comando y escribe un informe. Cada una mide una cosa: piezas con firma y fecha, esquema de las fichas, frescura de los datos, licencias, actividad, integridad del sello, anti-plantilla, enlaces, presupuesto de longitud, envíos, bandas, manual de estilo, firma literal, novedad, atestación firmada y la guía maestra. **No hace:** no arregla lo que encuentra, y no se aprueba por salida en cero: se aprueba cuando el informe dice `fallos: NINGUNO`.

**`manual_gate.py`** · *361 líneas*
Aplica los criterios del Manual de Estilo y Operaciones V3.0 a una pieza: firma textual, meme del corte, remate propio y único, mapa de cinco a doce entradas, sección «en una página», preguntas frecuentes, enlaces completos, fichas con licencia, frases prohibidas, notas fechadas, banda de longitud, meta-comentarios, signos dobles, secretos y párrafos compartidos. Devuelve **VERDE, VENTANA o ROJO**. **No hace:** no reescribe el texto; dice qué criterio no cumple y dónde.

**`novedad_gate.py`** · *248 líneas*
Mide lo que el manual no puede: si la pieza **recomienda algo nuevo** (al menos un recurso por debajo de 500 estrellas o con paquete reciente), si declara la madurez de lo nuevo, si no vende un proyecto dormido como vivo, si no usa fórmulas de plataforma y si la serie corta lleva sus `#task` numeradas sin huecos. **No hace:** no juzga el gusto del texto; cuenta hechos del texto.

**`firma_literal.py`** · *114 líneas*
Comprueba lo que una expresión regular no puede: que la frase de la casa esté **al final del cuerpo** y no en medio, y que el bloque de medición diga la hora. **No hace:** no valida el contenido de la medición, solo su forma y su sitio.

**`idioma_mojibake.py`** · *71 líneas*
Recorre el corpus buscando texto roto por codificación —las `Ã¡`, las `Â«`— y señala dónde. **No hace:** no corrige. Su cabecera lo dice: mide la salud, no opera.

**`duplicados.py`** · *86 líneas*
Agrupa archivos por contenido para saber qué está repetido antes de borrar nada. **No hace:** no borra. Un archivo repetido puede ser una copia legítima y una decisión humana.

**`autoprueba.py`** · *196 líneas*
La compuerta de las compuertas: construye un árbol de mentira, le mete **fallos sintéticos** y comprueba que cada compuerta los detecta. Una compuerta que no falla ante un fallo inventado no es una compuerta, es un adorno. **No hace:** no prueba el contenido real; prueba el detector.

**`acta_conformidad.py`** · *125 líneas*
Recibe una corrida real y escribe el acta de conformidad contra el manual, con fecha y resultado por pieza. **No hace:** no puede correrse sin que la corrida exista; nunca inventa un resultado.

---

## 3 · El sello

Si alguien puede cambiar una coma sin que se note, todo lo anterior es teatro. Este grupo lo impide.

**`atestar.py`** · *113 líneas*
Recorre el árbol, calcula la huella SHA-256 de cada archivo y escribe un manifiesto **encadenado con el lote anterior**: cada sello lleva dentro la huella del sello de ayer. **No hace:** no decide qué archivos importan; sella lo que hay, y si falta uno lo dice en vez de callarlo.

**`sello_reglas.py`** · *42 líneas*
Las reglas de qué se sella y qué no, en un solo sitio, para que la vara y la atestación no puedan contradecirse. **No hace:** nada por sí mismo; es la ley que los otros dos leen.

**`atestacion_verificar.py`** · *174 líneas*
Recibe la atestación firmada y la comprueba **en frío, sin llave**: verifica la firma de Sigstore, la identidad de quien firmó y que el contenido coincida. **No hace:** no confía en que la firma exista; comprueba que la firma cubra ese archivo y no otro.

---

## 4 · La publicación

**`envio.py`** · *788 líneas*
Recibe una pieza y la convierte en mensajes que un canal no corta: parte por párrafos, nunca dentro de un bloque de código o una tabla, mide otra vez los repositorios que la pieza cita y escribe una portada con la fecha y las licencias. **No hace:** no reescribe la pieza —el original queda intacto y su sha256 va en la cabecera— y no manda nada: prepara.

**`sitio.py`** · *617 líneas*
Recibe las piezas y el registro, y genera el sitio estático: índice, piezas, fichas, registro y RSS, sin una sola dependencia externa. **No hace:** no toca las fuentes; escribe en `site/`, que se puede borrar y volver a generar.

**`diseno.py`** · *477 líneas*
El sistema visual de la casa en un solo archivo: tipografía serif pesada, rejilla de doce, paleta pastel. **No hace:** no genera páginas; las viste.

**`html_archivo.py`** · *247 líneas*
Junta todas las piezas vivas en un único HTML para leer de corrido o imprimir. **No hace:** no cuenta los números a mano; los cuenta del nombre de cada archivo.

**`registro_construir.py`** · *201 líneas*
Construye las fichas JSON del registro desde el censo medido y comprueba que estén al día. **No hace:** no inventa campos; si el censo no trae un dato, la ficha lo declara vacío.

---

## 5 · El oficio y la casa

**`doctor.py`** · *168 líneas*
El primer comando en una máquina nueva. Mira cinco bloques —entorno, árbol, estado, integridad y veredicto— y dice **LISTO, LISTO CON AVISOS o DETENIDO**, con la salida para cada caso. **No hace:** no arregla. Diagnosticar y arreglar en el mismo gesto es lo que rompe los archivos.

**`tareas.py`** · *163 líneas*
Cosecha las líneas `#task NNN ·` de las piezas vivas y escribe el tablero en `docs/TAREAS.md`, comprobando que no haya huecos ni repetidos dentro de cada pieza. **No hace:** no cierra tareas por su cuenta ni las inventa; cerrar una tarea es un acto humano que se escribe en la pieza siguiente.

**`indice_docs.py`** · *183 líneas*
Lee `docs/` y `tools/`, agrupa los documentos por familia y **se presenta a sí mismo y a sus vecinos con la primera frase de su propio código**. Escribe `docs/INDICE.md`. **No hace:** no borra ni decide qué documento es importante; ordena lo que hay.

**`mcp_conectar.py`** · *195 líneas*
Hace un saludo real a un servidor MCP, lista sus herramientas y ejecuta una llamada de prueba. **No hace:** no simula la conexión; si el servidor no contesta, lo dice.

**`guia-maestra/herramientas/guia_maestra.py`** · *el generador de la guía*
Recibe setenta fichas en JSON y doce capítulos escritos a mano, valida cada ficha contra su esquema, aplica las compuertas y genera el índice, las doce páginas, la lista de créditos y el archivo de texto. **No hace:** no escribe la enseñanza; la enseñanza es el único texto que se escribe a mano en toda la guía.

---

## 6 · La puerta de entrada, que no es un programa

**`Makefile`** · *diecisiete destinos*
No es una herramienta más: es lo primero que ejecuta quien llega, y por eso está escrito en el idioma que ya existe en vez de en uno propio. Cada destino es **idempotente** —correrlo dos veces no rompe nada— y ninguno adivina: si falta un token o una dependencia, se detiene y lo dice antes de tocar el árbol.

| Destino | Qué hace | Qué no hace |
|---|---|---|
| `make doctor` | Diagnóstico en cinco bloques con veredicto | no arregla nada |
| `make verificar` | Registro, sello, vara y autoprueba | no sella ni publica |
| `make sellar` | Re-sella el árbol y encadena el lote | no verifica después |
| `make compuertas` | Solo la vara, informe corto | no mira registro ni autoprueba |
| `make licencias` | `reuse lint`: una licencia por archivo | no corrige cabeceras |
| `make generar` | Regenera la guía maestra | no escribe la enseñanza |
| `make sitio` | Regenera `site/` | no toca las piezas |
| `make tareas` | Reescribe `docs/TAREAS.md` | no cierra tareas |
| `make indice` | Reescribe `docs/INDICE.md` | no ordena por importancia |
| `make libro` | `tareas` + `indice` | no sella |
| `make vencer` | Recalcula el estado de frescura de cada ficha | no mide: decide |
| `make remedir` | Vuelve a medir lo vencido (exige `LBT`) | no decide el estado |
| `make referencias` | Audita las rutas movidas | no corrige |
| `make medir` | Mide y regenera envíos (exige `LBT`) | no publica |
| `make publicar` | `sellar` + `libro` + `verificar` | no empuja: eso se decide aparte |
| `make push` | Empuja con `GHP_A`, sin imprimirlo | no confirma: eso se mira en la CI |
| `make ayuda` | La lista de todo lo anterior | — |

**`tools/sello_reglas.py`** · *una sola lista*
Decide **qué se sella**, y existe separado para que la vara y la atestación no puedan discrepar: si cada una tuviera su lista, la compuerta podría dar por bueno un árbol que la atestación nunca firmó. Se corrigió en esta pasada porque dejaba fuera `Makefile`, `ARQUITECTURA.md`, los archivos de salud comunitaria, `.github/` y las licencias —es decir, justo las reglas del juego. **No hace:** no sella; solo dice qué entra.

---

## 7 · La fecha y la evidencia

Aquí vive lo que separa un archivo que presume de fechas de uno que las puede probar.

**`vencimiento.py`** · *el que decide qué hay que volver a medir*
Lee las 6.838 fichas, mide la edad de cada campo **contra su evidencia** y no contra lo que la ficha declara, aplica las ventanas de `docs/POLITICA-FRESCURA.json` y escribe tres cosas: el tablero `docs/VENCIMIENTOS.md`, el índice `registry/_vencimientos.json` y el bloque `frescura` de cada ficha. **No hace:** no mide repositorios. Decide qué hay que medir y lo deja escrito; medir es el oficio de `censo_medir.py`. Un programa que decide y mide en el mismo gesto no se puede auditar: cuando dice «vigente» nadie sabe si lo comprobó o se lo creyó.

**`referencias.py`** · *el que impide que una mudanza rompa algo en silencio*
Guarda la tabla de carpetas movidas y audita el árbol contra ella, distinguiendo lo que hay que arreglar de lo que hay que respetar: una ruta vieja citada por un archivo vivo es un fallo (detiene la línea), y citada por un acta o un registro histórico es una cita (se conserva y el mapa la traduce). **No hace:** no corrige rutas por su cuenta. Corregir una ruta exige saber qué quería decir la frase que la cita, y eso no lo sabe un programa.

**`censo_medir.py`** · *el que mide de verdad, cincuenta repositorios por consulta*
Pregunta a la API GraphQL —que cobra por nodos y no por petición, así que 6.838 fichas caben en ~137 consultas— y actualiza estrellas, último empujón, estado, licencia y revisión. Desde esta pasada guarda además el payload crudo en `registry/_evidencia/<id>.json` con la fecha **dentro del archivo**, y su SHA-256 en la ficha; acepta `--vencidas` y `--solo` para remedir únicamente lo que hace falta; y fecha con la hora de Santo Domingo, no con la del servidor. **No hace:** no inventa. Cuando la API devuelve 404 lo escribe como veredicto —`sin_objeto`— y no como dato ausente.

---

## Las tres invariantes que sostienen todo esto

Si algún día alguien tiene que auditar esta casa sin leer los 33 archivos, con estas tres frases alcanza:

1. **Nada se aprueba por silencio.** Un programa que sale con cero no dice nada; la aprobación es una frase concreta que la integración continua busca letra por letra.
2. **Nada se corrige sin dejar rastro.** Lo que se sella encadena con lo anterior; lo que se archiva conserva su fecha; lo que se rehace deja la versión anterior en `_reemplazadas/`.
3. **Nada se mide una sola vez.** Toda cifra que se publica tiene un método que otro puede repetir con un comando, y ese comando está escrito al lado de la cifra.

*La Bandita informa a partir de fuentes fechadas.*

### `tools/novedad.py` · el selector de novedad

Responde a la regla editorial que el dueño fijó el 3-nov-2026: **primero lo recién nacido, lo recién
publicado y lo desconocido**. No mide: lee la evidencia sellada de cada ficha (`registry/_evidencia/`),
de donde saca la fecha de nacimiento del repositorio, el último empujón, la última entrega y el tamaño, y
clasifica cada proyecto en `nacido` (≤90 días), `joven` (≤365), `desconocido` (≤300★ y vivo), `recien`
(entrega ≤30 días), `dormido` (>365 sin empujón) y `muerto` (404).

Ordena por **juventud × actividad**, nunca por estrellas, y exige una **señal de calidad** mínima —entrega
publicada, tamaño, descripción, licencia legible, tema Android— para que un repositorio vacío de tres días
no encabece la lista. Es el programa que produjo las doce fichas de la pieza 01 de Facebook.
