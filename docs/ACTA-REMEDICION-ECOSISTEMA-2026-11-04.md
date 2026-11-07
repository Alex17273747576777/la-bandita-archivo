# Acta de la remedición del ecosistema · 4 de noviembre de 2026

**Qué se hizo.** No se retocó la fecha de nada. Se volvió a medir cada cifra de las seis piezas de Facebook,
de las setenta fichas de la guía maestra y del censo que alimenta a las dos, y se corrigió lo que salió distinto.
Donde un dato no se podía repetir, se retiró y se sustituyó por una orden que cualquiera puede correr.

## 1 · Las seis piezas, medidas y en verde

| Pieza | Caracteres | Banda | `manual_gate` | `novedad_gate` | `remedir` |
|---|---|---|---|---|---|
| 01 · El turno de los que nacieron este trimestre | 44.090 | sí | VERDE | VERDE | AL DÍA |
| 02 · La música que no se cae | 44.236 | sí | VERDE | VERDE | AL DÍA |
| 03 · La caja fuerte del bolsillo | 41.925 | sí | VERDE | VERDE | AL DÍA |
| 04 · La lista del permiso | 44.988 | sí | VERDE | VERDE | AL DÍA |
| 05 · La guía maestra | 40.901 | sí | VERDE | VERDE | AL DÍA |
| 06 · El taller | 44.916 | sí | VERDE | VERDE | AL DÍA |

Cada pieza tiene su archivo de medición con fecha **y hora**: `docs/MEDICION-0X-2026-11-04.json`.

## 2 · Lo que cambió de verdad, pieza por pieza

- **01** — doce programas, 614★, rango de madurez 9–35 días. Descargas 42.330 → 42.335 (+24 y −19). Escrita de nuevo
  con el ángulo de las tres pasadas del día. Solape con la versión anterior: 3,1 %.
- **02** — los ocho de octubre con su entrega, su tamaño y sus descargas de hoy: SplitAudio pasó de **1** a **1.109**
  descargas en un día y sacó la v0.5.6 esta mañana. Los cinco grandes movieron estrellas; el censo de audio se rehizo
  con orden repetible. **Dos enlaces se habían mudado**: `RootlessJamesDSP` cambió de dueño y el catálogo de Shizuku
  cambió de nombre. Las dos direcciones viejas ya no llevan a ninguna parte.
- **03** — Monica, Keyguard, Aegis, Stratum, KeePass2Android, Bitwarden y AuthPass con sus cifras de hoy; «publicada
  hoy» pasó a «ayer» donde la entrega era del 3; los días de silencio de los cuatro parados, uno más. El título decía
  **mil seiscientos tres días** y hoy son mil seiscientos cuatro: el archivo se renombró con `git mv`.
- **04** — cuatro estrellas movidas y tres programas que se nombraban sin cifra; ahora la llevan.
- **05** — las setenta fichas de la guía se midieron otra vez con `tools/medir_guia.py`: 58 estrellas, 58 recuentos de
  descargas, 63 recuentos de incidencias, 17 tamaños, 6 contribuyentes y 6 notas cambiaron. La suma de la tabla pasó a
  **1.396.395★**, las descargas de las diez últimas a **138.081.520** y los repositorios a **15.182,1 MB**. La mediana
  de nota sigue en 53,5. Y apareció un error viejo: la pieza decía «cuatro por debajo de treinta» cuando su tabla
  publicaba **cinco** (E25).
- **06** — 1.410★ y no 1.407: el título y el nombre del archivo se corrigieron. Cuarenta y dos hilos abiertos, no
  cuarenta; 123.058 descargas, no 122.769. Las sesenta y cinco entregas, las 2.355 confirmaciones y los 78
  contribuidores siguen igual, medidos hoy.

## 3 · La guía maestra, remedida entera

`guia-maestra/datos/medicion-2026-11-04.json` guarda la medición de las setenta. La señal anterior de cada ficha quedó
en `guia-maestra/datos/_senal-anterior/2026-11-04/` — nada se borra. Después se regeneraron créditos, índice, sitio y
las doce páginas de capítulo, y las compuertas M30–M34 dieron **cero fallos**.

## 4 · Herramientas nuevas, con su habilidad

| Herramienta | Qué hace | Habilidad | Error que la obligó |
|---|---|---|---|
| `tools/medir_guia.py` | mide las 70 fichas de la guía y guarda la señal anterior | H11 | una guía que envejece sin que nadie lo note |
| `tools/censo_tema.py` | cuenta un tema con palabras y ventana declaradas | H10 | E30: un censo que no se podía repetir |
| `tools/alinear.py` | pone la ★ de la medición en su línea, y dice cuáles cambió | H09 | E26 y E27: una compuerta que se ablanda sola |
| `make medir-guia` · `make censo` · `make alinear` | los tres atajos, en el `Makefile` | — | — |

Además, `tools/remedir.py` aprendió a contar hasta los millones en palabras, a apocopar («veintiún mil», nunca
«veintiuno mil») y a aceptar la cifra cuando vive en una columna de tabla. Y `make ritual` pasó a regenerar el libro
antes de sellar, porque el CI lo comparaba y tumbaba la línea.

## 5 · Errores anotados en esta pasada

E25 (cuatro por cinco) · E26 (la cifra en la celda) · E27 (el corte de enlaces se comía el cuerpo) · E28 (dos
repositorios mudados) · E29 (cifras que se mueven dentro del título) · E30 (un censo que no se repite). Cada uno con
su fila en `docs/ERRORES.md` y su habilidad en `docs/HABILIDADES.md`.

## 6 · Lo que queda abierto, dicho sin adornos

1. **Las etiquetas estratégicas de WhatsApp.** La banda 63.000–63.099 no deja sitio: hay que recortar texto para que
   entren. Es trabajo de redacción pieza por pieza, no de compuerta.
2. **La pieza 06 de WhatsApp.** No existe: hay que escribirla en banda 63.000–63.099 desde cero.
3. **Los SWHID por revisión medida.** La API responde; falta archivar por lotes cada revisión citada.
4. **Las decisiones del dueño** (licencia, marca, dominio, canal, patrocinio, publicar el MCP). No son técnicas.
