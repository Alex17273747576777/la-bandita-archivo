# 03 · Publicar en el canal

**Entrada:** lote sellado y CI en verde. **Salida:** publicación en el canal con su hora registrada.

## Antes de publicar

- [ ] El envío que se copia es el **generado** (comparar con `envio.py --verificar`).
- [ ] El texto no se edita a mano en el canal: si hay que cambiar algo, se cambia la pieza y se
      regenera.
- [ ] El canal es el correcto (Facebook / WhatsApp) y la pieza es de ese canal.
- [ ] La hora de publicación se anota en la bitácora del lote.

## Durante

1. Copiar el envío completo, sin recortar el cierre ni la firma.
2. Publicar y **verificar a ojo** que llegó entero (trozos en WhatsApp: comprobar el último).
3. Anotar hora y enlace o identificador en `docs/` del lote.

## Después

- Si el canal recorta o rompe formato, se anota en `docs/ERRATA-<fecha>.md` y se ajusta el generador,
  no el texto publicado.
- Si hubo error de contenido, se aplica `CIMIENTOS/06-PROTOCOLO-DE-ERRORES.md`: se corrige, se deja
  rastro y —si el fallo es de raíz— se reinicia la lista de forma declarada.

## Reglas

- **Un lote, una publicación por canal.** No se publica a medias y se completa después.
- **Nada de promesas de seguimiento** en el canal («mañana traigo más»): el manual lo prohíbe.
- El canal **no** es fuente de datos: lo que se publica viene del repositorio.
