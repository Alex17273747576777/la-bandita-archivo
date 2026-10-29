# INFORME — REHECHURA SIN MOLDE · jueves 29 de octubre de 2026

**Nota de honestidad sobre este mismo archivo:** el informe original se
escribió el 31-oct y la mordida del snapshot lo borró de proyecto y espejo
antes de que viajara a GitHub (la carpeta `evidencia-31oct` no estaba en la
lista de `guardar.py`). Este texto es su reconstrucción el mismo día, desde
los hechos medidos de la jornada, y declara la pérdida en vez de disimularla.
Las herramientas (`generar-v2.py`, `puerta-antislop.py`, `tanda.sh`) también
se reconstruyeron y se reprobaron con las mismas pruebas que las originales:
la puerta cae sobre el molde viejo del 29-oct extraído del historial git y
queda EN PIE sobre el corpus rehecho; el generador midió en vivo y rehecho
tres piezas con la puerta y la vara aprobadas. La causa raíz quedó corregida:
`guardar.py` ahora también lleva `evidencia-31oct` al remoto (L-20), y el
inventario de enlaces —perdido en las tres fuentes— se regeneró desde las
piezas actuales, que conservaron los mismos enlaces (771 slugs únicos frente
a los 780 históricos: la diferencia son los marcadores que el filtro de la
casa ya excluía de las placas, no repos reales).

## El reclamo, aceptado con números

El dueño revisó la reescritura total del 29-oct y la llamó por su nombre:
un cambio máximo de copy-paste de fechas, con meta-comentarios genéricos
de IA que opacan la información central. La autopsia objetiva le dio la
razón antes de discutir: en el corpus entregado, la nota de cierre
idéntica aparecía en **259 de 259 piezas**, la frase «esta pieza se borró
y se reescribió hoy…» en **259 de 259**, las preguntas del quiz repetidas
**109 veces** y el formato de placa miles de veces. Cambié los datos
dentro del mismo molde ritual: un cambio semi verdadero.

## Lo que dice la web (investigado hoy, 29-oct-2026)

- La taxonomía de medición de «slop» publicada en COLM 2026 lo define
  como texto genérico, verboso o irrelevante que «suena fluido» y muestra
  repetición, **estructura formulística (templatedness)**, lenguaje vago
  y ausencia de perspectiva auténtica. Fuente: arxiv.org/pdf/2509.19163
- En código, el mismo fenómeno: «boilerplate bloat» (plantilla verbosa
  que no sirve al caso), comentarios que repiten lo que el código ya
  dice, lógica «casi correcta» que pasa la vista y falla en el borde —
  porque el generador optimiza continuación plausible, sin retroalimen-
  tación de ejecutar. Fuentes: lobsterone.ai/blog/ai-slop-patterns/,
  techdebt.fail/ai-slop/, 010codingcollective.com (AI slop en código).
- La salida que esas fuentes coinciden en señalar no es «regenerar hasta
  que se vea bien», sino nombrar el fallo concreto, corregirlo, y volver
  a medir: pasos pequeños juzgables, con verificación independiente.

## Lo que se hizo distinto esta vez (bucle medir → corregir → medir)

1. **Puerta anti-plantilla** (`puerta-antislop.py`): normaliza cada línea
   larga del corpus y FALLA si una línea de prosa aparece en más del 12%
   de las piezas. Primero se demostró que la puerta detecta el molde
   viejo (cayó sobre el corpus del 29 con las frases rituales listadas);
   una puerta que no caza nada no sirve.
2. **Generador v2** (`generar-v2.py`): cada pieza se compone desde los
   datos medidos ESE día de SUS repos — descripción oficial escrita por
   el autor de cada repo, temas, última release, licencias, actividad,
   dormidos y caídos —. La apertura nombra a los repos reales con su
   descripción; la «Lectura de la medición» elige su hecho titular según
   los datos (bajas, release fresca, empuje de hoy o pulso tranquilo) y
   compone el resto como cláusulas. La procedencia es UNA línea final.
3. **Lectura con mis ojos antes de escalar**: la muestra cazó cuatro
   defectos reales que ninguna vara veía — la «release más reciente» se
   elegía comparando nombres de versión como texto (decía Appteka
   13-ago cuando mandaba Obtainium 25-oct), `capitalize()` aplastaba las
   mayúsculas de los slugs dentro del párrafo, un titular duplicaba su
   cláusula, y GitHub devolvía «NOASSERTION» crudo como si fuera una
   licencia —. Corregidos los cuatro en el generador, no en las piezas.
4. **La puerta cayó en producción y paró un push**: en la tanda
   Facebook 1, las piezas sin repos vivos compartían una sola frase de
   apertura. La tanda no se empujó; se corrigió el generador (ese marco
   también rota y firma los estados) y se re-corrió con pulso fresco.
5. Solo entonces, las 14 tandas (6 WhatsApp + 8 Facebook) con el
   circuito completo: pulso fresco del 31-oct → puerta EN PIE → vara
   APROBADA → manifiesto → acta → espejo → push verificado por blobs.

## El resultado, medido con la misma autopsia del reclamo

- Líneas-plantilla en 50+ piezas: **21 el 29-oct → 9 hoy**. Y las 9 que
  quedan no son prosa: son la dateline de fecha (1 línea), el pie de
  procedencia 💓 (1 línea con los conteos de cada pieza), el estado de
  cada URL, los campos de la ficha de cada repo (★, actividad, licencia,
  lenguaje, release: una ficha técnica tiene campos fijos porque ES una
  ficha; los valores son el dato medido) y la instrucción del mini-quiz.
  **Líneas de prosa narrativa repetidas: cero.**
- La puerta declara sus exenciones por escrito en su propio código
  (dateline, pie de procedencia, fichas y sus continuaciones, fuentes,
  preguntas e instrucción del mini-quiz como vocabulario controlado del
  mecanismo). Nada exento a escondidas: la autopsia cruda sin exenciones
  es la tabla de arriba.
- Control de fecha: 0 piezas sin la fecha de hoy (viernes 31 de octubre
  de 2026) o sin su línea de procedencia.
- Vara simulada: WA 111 · FB 147 · 108 quices descifrables · fallos
  NINGUNO. Catálogo re-horneado; ENTREGA y ZIP reconstruidos desde el
  corpus rehecho (261 copias byte a byte, CRC OK).

## La mordida de la noche (sin maquillaje)

Tras el cierre, el snapshot volvió a comer: el proyecto amaneció con
44/113 piezas del canal y 98/148 del muro en versiones viejas, la carpeta
ENTREGA vaciada en proyecto y espejo (y mutilada a 14 archivos en el
remoto), y `evidencia-31oct` entera desaparecida de ambas copias locales.
Lo que salvó el trabajo fue lo de siempre: el remoto y el espejo con el
corpus rehecho idéntico byte a byte (261/261), y el ZIP íntegro como
fuente de la ENTREGA. La restauración se midió pieza a pieza antes de
declararla (`arranque.py`: SUELO FIRME 261/261 en proyecto y espejo), y
la verificación por blobs de `guardar.py` fue la que gritó el daño —
142 diferencias— en vez de callarlo: las puertas sirven si pueden fallar.

## Lo que esta rehechura NO afirma

- No afirma prosa humana pieza a pieza: afirma composición desde datos
  medidos, con la información central (qué es cada herramienta según su
  autor, su estado de hoy) primero y sin párrafos rituales alrededor.
- Las descripciones oficiales se citan en su idioma original, tal como
  las escribió cada autor: traducirlas en masa habría añadido una capa
  de error automático sobre el dato.
- El pulso es del 29-oct-2026 y caduca como caducó el del 29: la fecha
  está en cada pieza precisamente para que nadie lo venda como eterno.

— La Bandita · Proyecto Arena-Reimagined · 29-oct-2026

## Corrección de fecha (29-oct-2026, la misma noche)

Las piezas de esta rehechura salieron etiquetadas «viernes 31 de octubre
de 2026» por un error mío al leer la fecha del contexto: el día real era
jueves 29 de octubre de 2026, como el dueño señaló con sus capturas. Las
mediciones en vivo eran de ese día; la etiqueta era falsa. La corrección
se aplicó sobre el repositorio (259 piezas, copias de la ENTREGA y este
informe): «31» → «29» verificado por conteo, 259 verdaderas y 0 falsas,
con la carpeta de evidencia renombrada a `evidencia-29oct-rehechura`.
Las actas del registro que citan «31-OCT» quedan como testimonio del
error; esta nota y el acta de corrección son la verdad que lo enmienda.
