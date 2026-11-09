# Reescritura de los issues propios · 9 de noviembre de 2026

*Todo lo que había se guardó antes de tocar nada. Nada se perdió.*

## Lo que se hizo

| | antes | después |
|---|---|---|
| issues abiertos | 35 | **30** |
| cuerpo medio de un issue abierto | 10.364 caracteres | **454** |
| con emoji en el título | 21 | **0** |
| con cuerpo de más de 8.000 caracteres | 7 | **0** |
| comentarios propios en issues abiertos | 17 | 1 (el del FMHY, que era el bueno) |
| comentarios propios en issues cerrados | 30 | 10 (los de `cero-X-app`, que son el arreglo real) |

## Los archivos de este respaldo

- **`RESPALDO-COMPLETO.json`** — los 35 cuerpos originales y sus 32 comentarios, tal cual estaban.
- **`COMENTARIOS-CERRADOS.json`** — los 30 comentarios propios en issues ya cerrados.
- **`CAMBIOS-APLICADOS.json`** — issue por issue: cuerpo anterior, cuerpo nuevo, acción y hora.
- **`CAMBIOS-COMENTARIOS.json`** y **`CAMBIOS-COMENTARIOS-ABIERTOS.json`** — comentario por comentario, con el texto íntegro de lo que había.
- **`PLAN-APLICADO.json`** — el plan completo que se ejecutó.

## Lo que se cerró, y por qué

Ocho issues cerrados con una nota que apunta al hilo que se queda:

- **komikku #1535, #1536, #1537** y **#1476** — duplicados de #1543, #1541, #1544. La serie `📋 Suggestion #1–11` repetía la serie `🎯 Suggestion #1–7`.
- **komikku #354** (tonkatsu_box) — la traducción se entregó y salió en 0.39.
- **los cinco de `cero-X-app`** — ya estaban cerrados y corregidos; GitHub no permite editar un issue cerrado, así que cada uno lleva una nota con el arreglo concreto para cuando se retome.

## Lo que no se pudo hacer, y se dice

**El comentario del issue `keiyoushi/extensions-source#17590`** — el hilo donde un mantenedor contestó «Thanks for shitting AI slop in our requests». No se puede editar ni borrar: el mantenedor **bloqueó la conversación**, y GitHub devuelve `403` («issue is locked») para las dos operaciones. Queda ahí, y la respuesta a eso no es borrarlo: es que los otros 98 no se parezcan a él.

## El criterio que se aplicó

Los mantenedores fueron explícitos en tres hilos distintos: «To do list yerine çevirmişsin lan», «Another ai bs post», «Too long content is hard to read». El problema no era la redacción: era el tamaño, el emoji y la ausencia de una petición concreta.

Cada cuerpo nuevo dice ahora **un problema, una petición y cómo se comprueba**. Donde el mantenedor ya había rechazado una parte, el cuerpo lo dice y no la vuelve a pedir. Ese es el caso de #1545, #1543, #1541, #1540, #1533 y #1529.

El único que acabó con algo publicado fue el de `tonkatsu_box`: pidió traducir `app_es.arb`, se entregó y salió en la 0.39. Ese es el modelo.
