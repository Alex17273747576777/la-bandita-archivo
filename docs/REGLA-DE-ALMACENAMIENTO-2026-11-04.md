# Regla del dueño · el almacén es GitHub y la revisión va antes

*4 de noviembre de 2026, noche · vale desde la pieza 15 y no caduca*

> «Que los resultados siempre se subirán a GitHub; está prohibido almacenar con pérdidas de
> variables o trabajar desde el almacenamiento local limitado, y siempre antes de proceder con
> las publicaciones pendientes debemos estar revisando primero el historial antiguo y la fecha,
> además de todo el ecosistema de recursos de código abierto, cada vez, antes de empezar a sondear.»

## Las cuatro obligaciones, dichas en corto

1. **GitHub es el único almacén.** Lo que no está empujado a `main`, no existe. El commit se hace
   en el mismo turno en que se produce el resultado, no «al final».
2. **Prohibido el almacenamiento con pérdida.** Nada que dependa de una carpeta que el entorno
   puede vaciar o revertir: los clones de trabajo viven en `/tmp` (siempre recién clonados) y los
   talleres —los generadores de cada pieza— se guardan en `docs/talleres/pieza-NN/` dentro del
   repositorio, para que se puedan repetir las cifras desde cualquier máquina.
3. **Antes de publicar, se revisa el historial.** Qué piezas están ya publicadas, cuál toca según
   el mapa de 125, con qué título y con qué gancho: para no repetir tema, ni cifras, ni párrafos.
4. **Antes de sondear, se revisa el ecosistema.** La fecha en vivo, y después GitHub por fecha de
   creación y por tema. Primero el censo del tema; después las fichas. Nunca al revés.

## La herramienta que lo hace cumplir

```
LBT=… python3 tools/preflight.py --tema descarga      # fecha + historial + ecosistema, en ese orden
```

Escribe su acta en `docs/PREFLIGHT-<tema>-<fecha>.json` y **no deja sondear sin historial**: si el
mapa y las publicaciones no cuadran, sale con código 1.

## Por qué esta regla existe (el registro de lo que pasó)

- La pieza 12 se perdió una vez porque el clon vivía en `.cache/`, una carpeta que el entorno no
  conserva entre turnos: hubo que remedir 59 repositorios a mano.
- Al turno siguiente, el directorio de trabajo del repositorio amaneció **revertido a un estado
  viejo y sin `.git`**. Lo publicado en GitHub estaba intacto —01 a 14—; lo local, no.
- Moraleja medida dos veces: **el disco de trabajo no es un archivo**. El archivo es el repositorio.

## Lo que cambia a partir de aquí

- Cada pieza deja su taller en `docs/talleres/pieza-NN/` (los `.py` que generan el texto) y su
  acta; el `.md` final ya se guardaba.
- Cada sesión empieza con `preflight` y no con una búsqueda a ciegas.
- Si el disco local se revierte, no se pierde nada: se vuelve a clonar y se sigue desde el último
  commit. Eso es todo el protocolo.
