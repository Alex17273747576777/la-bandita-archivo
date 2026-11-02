# PROCESOS · flujos de trabajo

Los procesos son **el ciclo visto desde arriba**: qué se hace, en qué orden, quién lo desbloquea y
qué compuerta lo cierra. Las habilidades (`SKILLS/`) son el detalle de cada paso; los cimientos
(`CIMIENTOS/`) son lo que no se negocia.

| Proceso | Documento | Frecuencia |
|---|---|---|
| Fabricar una pieza | [`01-PIEZA.md`](01-PIEZA.md) | por pieza |
| Cerrar un lote | [`02-LOTE.md`](02-LOTE.md) | cada 5 piezas |
| Publicar un canal | [`03-PUBLICACION.md`](03-PUBLICACION.md) | al cerrar lote |
| Cadencia y turnos | [`04-CADENCIA.md`](04-CADENCIA.md) | continuo |
| Publicar el frontend | [`05-FRONTEND.md`](05-FRONTEND.md) | cuando cambia el sitio |

## El ciclo completo en una línea

> medir → censar → escribir → compuerta → envíos → acta → sello → commit → CI verde → publicar en el canal → registrar la hora.

## Estados por los que pasa una pieza

`BORRADOR` → `MEDIDA` → `ESCRITA` → `VERDE` → `ENVIADA` → `SELLADA` → `PUBLICADA`

Una pieza solo avanza; si retrocede, se anota el motivo en el acta (nunca en silencio).
