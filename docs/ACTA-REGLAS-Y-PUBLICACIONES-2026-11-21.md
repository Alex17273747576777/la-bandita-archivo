# Acta de reglas vigentes de publicación y archivo — 21 de noviembre de 2026

## Motivo

Consolidar las reglas de publicaciones vigentes vs. retiradas en el archivo (`la-bandita-archivo`),
corregir el falso rojo de `tools/vara_idiomas.py` cuando `Arena-Reimagined/01-PUBLICACIONES/` está
retirada y actualizar el estado operativo del repositorio al corte del **21 de noviembre de 2026**.

## Cumplimiento del protocolo de 4 pasos (`REGLAS/INDICE-DE-REGLAS.md`)

1. **Nota fechada en la ley raíz:** añadida en `CORAZON-LA-BANDITA.md` («NOTA DE PUBLICACIONES
   VIGENTES Y RETIRO EN VARA DE IDIOMAS — sábado 21 de noviembre de 2026»).
2. **Sincronización operativa:**
   - Actualizado `tools/vara_idiomas.py` para comprobar los moldes canónicos de
     `ENTORNO-DE-TRABAJO/moldes/` e informar `SIN PUBLICACIONES` con salida `0` cuando
     `Arena-Reimagined/01-PUBLICACIONES/` no existe por el retiro del 15-nov, manteniendo el
     chequeo estricto G20–G23 cuando la carpeta exista o se pase ruta explícita.
   - Añadido `tests/test_vara_idiomas.py`.
   - Creado `docs/REGLAS-DE-PUBLICACION-Y-ARCHIVO.md` (con los 4 pasos de Richard Feynman).
   - Actualizados `README.md` y `CHANGELOG.md` (`[3.1.0] — 2026-11-21`).
3. **Índice y resello encadenado:** regenerado `docs/INDICE.md` (`make libro`) y resellado el lote
   mediante `tools/atestar.py`, verificando `atestar.py --verificar`, `vara.py`, `vara_idiomas.py`,
   `feynman_verificar.py` y las pruebas unitarias.
4. **Entrada en el índice de reglas:** registrada la entrada `(21-nov-2026 — reglas de publicación y retiro en vara_idiomas)` en `REGLAS/INDICE-DE-REGLAS.md`.
