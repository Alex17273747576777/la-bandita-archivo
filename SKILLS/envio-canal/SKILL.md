---
name: envio-canal
version: 1.2.0
dominio: publicación
nivel: medidor
cuando: cuando hay piezas verdes y hay que dejarlas listas para su canal
entradas: [piezas verdes, canal (facebook | whatsapp)]
salidas: [cuerpo + comentario fijado por pieza, numerados y con nombre de la casa]
herramientas: [tools/fijados.py, tools/leeme_carpeta.py, tools/bandas.py]
verificacion: [40 de 40 con cuerpo y fijado, longitudes dentro de banda, LEEME al día]
depende_de: [compuerta-manual]
---

# Habilidad · envío al canal

## Propósito
Dejar cada pieza en su forma de publicación: **un cuerpo y un comentario fijado**, con el mismo
número que el cuerpo, y el registro (bandas y LEEME) cuadrando con el disco.

## Cuándo se usa
- Al cerrar un tramo de piezas.
- Cuando se añaden piezas nuevas a la carpeta.

## Pasos
1. `python3 tools/fijados.py NN` — el fijado se genera **desde la medición**, no se escribe aparte.
2. `python3 tools/bandas.py --cuadrar` — el registro se rehace leyendo los archivos, no al revés.
   Añade las piezas nuevas que aún no tienen entrada.
3. `python3 tools/leeme_carpeta.py --arreglar` — recuenta las columnas y añade filas que falten.
4. `python3 tools/leeme_carpeta.py` — comprobar: 0 fallos.

## Reglas duras
- **El fijado y el cuerpo no pueden decir cosas distintas**: los dos salen del mismo JSON.
- **El registro no es una lista cerrada.** Si hay 41 piezas, el LEEME dice 41.
- **Una pieza vieja no se borra**: se mueve a `_reemplazadas-<fecha>/`.
- **El ciclo cerrado no se reescribe.** Las piezas nuevas entran numeradas aparte (segunda vuelta).

## Verificación
- `piezas comprobadas: N · fallos: 0`.
- Cada fijado entre 900 y 4.000 caracteres; cada cuerpo dentro de la banda de su canal.

## Errores conocidos
- Reescribir `bandas.json` a mano: nadie lo cuadraba y 18 piezas quedaron fuera de banda sin que se
  supiera por qué. Ahora es herramienta.
