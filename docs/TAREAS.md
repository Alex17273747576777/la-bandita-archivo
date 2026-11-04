# TABLERO DE TAREAS

*Generado por `tools/tareas.py` el día que se corre. No se edita a mano: se vuelve a correr.*

**TL;DR —** 15 tareas abiertas en 11 piezas vivas, numeradas dentro de cada pieza, de 001 a 009. Numeración sin huecos ni repetidos dentro de cada pieza. El tablero se regenera con `make tareas` y la integración continua comprueba que no haya huecos.

## De dónde salen

Cada tarea vive en la pieza que la engendra, como una línea `#task NNN · texto`. Esa es la regla de la casa: **una tarea no se guarda en una lista aparte, se escribe dentro del documento que la justifica**, para que quien lea la pieza vea qué quedó pendiente y por qué. Este tablero no es la fuente: es la vista.

## Las tareas abiertas

| # | Tarea | Origen | Corte |
|---|---|---|---|
| 001 | volver a medir los doce proyectos de esta pieza el 3 de diciembre de 2026 y publicar qué cambió, incluida la suerte de cleanyourtv y de la cola de cleanyourtv-app. | Facebook · 01 | 2026-11-03 |
| 001 | volver a medir los cuarenta y cuatro el 3 de diciembre de 2026 y publicar cuáles siguen publicando, con atención especial a OmniShizuku, que hoy tiene diez días y sesenta y siete. | Facebook · 04 | 2026-11-03 |
| 001 | pedir al autor del programa, en su repositorio, que el flujo de publicación escriba un archivo de sumas SHA-256 al lado de cada entrega, y anotar la respuesta en el acta del 4 de diciembre de 2026. | Facebook · 06 | 2026-11-03 |
| 002 | abrir las tres discrepancias de licencia en sus repositorios respectivos, proponiendo la corrección del archivo de detección y no del texto de la licencia. | Facebook · 01 | 2026-11-03 |
| 002 | pedir al archivo público la conservación de las catorce revisiones de las fichas y anotar el número de solicitud en cada una. | Facebook · 04 | 2026-11-03 |
| 002 | remedir el 3 de diciembre de 2026 las tres entregas del linaje —el gestor original, el de Morphe y este— y publicar cuál de los tres publicó más seguido en el mes, con la fecha del empujón de cada uno. | Facebook · 06 | 2026-11-03 |
| 003 | completar la conservación en el archivo público de las seis revisiones que quedaron en cola hoy, y anotar el número de solicitud en cada ficha. | Facebook · 01 | 2026-11-03 |
| 003 | abrir en sus repositorios los cuatro casos de licencia sin resolver que aparecen en la tabla, proponiendo la corrección del archivo de detección y no del texto de la licencia. | Facebook · 04 | 2026-11-03 |
| 003 | escribir la versión de WhatsApp de esta pieza, más corta, con los cinco pasos reducidos a tres y el episodio del 451 contado en dos párrafos, y comprobar que su banda de longitud se cumple antes de enviarla. | Facebook · 06 | 2026-11-03 |
| 004 | remedir el 3 de diciembre de 2026 las nueve fichas de menos de quinientas estrellas, empezando por OmniShizuku y TVSlim, y publicar cuáles siguieron publicando. | Facebook · 05 | 2026-11-03 |
| 005 | pedir al archivo público la conservación de las doce revisiones de los capítulos y anotar el número de solicitud en cada acta. | Facebook · 05 | 2026-11-03 |
| 006 | abrir en sus repositorios los cuatro casos de nota por debajo de treinta, proponiendo la corrección del archivo de licencia o del canal de seguridad, que es lo que la nota señala. | Facebook · 05 | 2026-11-03 |
| 007 | remedir el 3 de diciembre de 2026 las nueve fichas de menos de quinientas estrellas, empezando por OmniShizuku y TVSlim, y publicar cuáles siguieron publicando. | WhatsApp · 05 | 2026-11-03 |
| 008 | pedir al archivo público la conservación de las doce revisiones de los capítulos y anotar el número de solicitud en cada acta. | WhatsApp · 05 | 2026-11-03 |
| 009 | abrir en sus repositorios los cuatro casos de nota por debajo de treinta, proponiendo la corrección del archivo de licencia o del canal de seguridad, que es lo que la nota señala. | WhatsApp · 05 | 2026-11-03 |

## Numeración: la regla y lo declarado

> **Declarado:** 05-La-guia-maestra-contada-despacio-doce: numera desde 007 y no desde 001 (pieza publicada antes de la regla; se declara, no se retoca)
> **Declarado:** 05-La-guia-maestra-doce-capitulos-setent: numera desde 004 y no desde 001 (pieza publicada antes de la regla; se declara, no se retoca)

La numeración es **por pieza**, no global: cada pieza numera sus tareas desde 001 porque la compuerta de novedad (M28) las cuenta dentro de la pieza. Por eso la misma cifra puede aparecer en dos piezas distintas y no es un error: la tarea se identifica por su número **y** su pieza.

## Cómo se cierra una tarea

No se borra de aquí. Se cumple, y la pieza siguiente lo cuenta con su medición al lado. Cuando una tarea se cumple, su número deja de aparecer en las piezas nuevas y el tablero se encoge solo en la próxima corrida. Una tarea que llevas tres meses sin hacer no es una tarea: es una decisión que hay que tomar y decir en voz alta.

## Las comprobaciones que hace este programa

1. **Sin huecos**: la numeración sube de uno en uno; un salto se declara aquí y no se disimula.
2. **Sin textos contradictorios**: el mismo número no puede decir dos cosas distintas en dos canales.

*La Bandita informa a partir de fuentes fechadas.*
