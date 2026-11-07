# 02 · Cerrar un lote

**Un lote son cinco piezas.** Se abre con la primera medición y se cierra con acta, sello, commit y
CI en verde.

## Secuencia

1. Las cinco piezas están en `VERDE` (paso 8 de `01-PIEZA.md`).
2. `envio.py --medir` con la llave en el entorno (una sola vez por lote).
3. `envio.py --generar --canal ambos` y `--verificar` → `fallos: 0`.
4. Comprobar que no hay **envíos huérfanos** ni piezas sin envío.
5. `acta_conformidad.py` → `docs/CONFORMIDAD-MANUAL-<fecha>.md`.
6. `atestar.py` → sello nuevo; anotar huella anterior y nueva.
7. `vara.py` → `fallos: NINGUNO` (G0–G12).
8. `git add -A && git commit && git push` con `GHP_A`; un push, una espera.
9. Confirmar CI `success` y escribir la línea del lote en `docs/` (cifras reales, no estimadas).

## Definición de «lote cerrado»

- [ ] 5 piezas VERDE, longitudes en banda.
- [ ] Envíos regenerados y verificados, sin huérfanos.
- [ ] Acta escrita y sello nuevo.
- [ ] `vara.py` sin fallos.
- [ ] Commit empujado y CI en verde.
- [ ] Cifras del lote registradas (piezas totales y caracteres acumulados).

Si falta un solo punto, el lote está **abierto** y no se anuncia.

## Prohibiciones

- Sellar sin acta, o acta sin sello: el orden es parte del procedimiento.
- Push doble para «ver si pasa»: cancela el CI y desordena el historial.
- Cerrar un lote con piezas fuera de banda «que se arreglan luego»: luego es nunca.
