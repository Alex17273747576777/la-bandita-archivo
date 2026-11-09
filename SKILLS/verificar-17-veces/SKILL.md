---
name: verificar-17-veces
version: 1.0.0
dominio: control de calidad
nivel: puerta
cuando: cuando el dueño pide rechequear «por completo» lo que se acaba de hacer
entradas: [el bloque recién terminado]
salidas: [diecisiete comprobaciones, cada una por una vía distinta]
herramientas: [las diecisiete vías de abajo]
verificacion: [17 de 17 ejecutadas, ninguna repetida con otro nombre]
depende_de: [cotejar-cifras, compuerta-manual]
---

# Habilidad · verificar diecisiete veces

## Propósito
Rechequear de verdad, **no tres veces con el mismo comando**. La regla del dueño es explícita: diecisiete
comprobaciones, versátiles, adaptadas a cada tema, sin plantilla única.

## Cuándo se usa
- Cuando el dueño pide rechequear «por completo» o «diecisiete veces».
- Antes de declarar un bloque cerrado tras una corrección grande.
- Cuando algo salió demasiado limpio a la primera.

**No se usa** para cada commit pequeño: para eso están las compuertas de cada bloque.

## Las diecisiete vías
| # | Vía | Qué se aprende que las otras no dicen |
|---|---|---|
| 1 | Recuento de cifras | cuántas hay, no si están bien |
| 2 | Cotejo contra el JSON | si cada una existe en su fuente |
| 3 | Atribución | si la cifra pegada a un nombre es de ese nombre |
| 4 | Fuente en vivo | si el dato sigue siendo cierto ahora |
| 5 | Estructura | cuerpo y fijado, uno de cada |
| 6 | Longitudes | dentro de banda, sin relleno |
| 7 | Firma y fecha | que la casa firme y feche |
| 8 | Rutas citadas | que lo citado exista |
| 9 | Coherencia entre piezas | que la guía sume lo que las piezas dicen |
| 10 | Nombres mudados | que lo citado se llame hoy como se llama |
| 11 | Detector contra sí mismo | ¿el fallo es de la pieza o del medidor? |
| 12 | Reproducir desde cero | rehacer el cálculo en otro comando |
| 13 | Lectura humana de una muestra | lo que ninguna regla ve |
| 14 | El cero | ¿el cero es real o es un lector roto? |
| 15 | Lo que no está | qué debería estar y no está |
| 16 | Coste y tiempo | si el método escala o se cae |
| 17 | Rehacer el bloque | si mañana se repite, ¿sale igual? |

## Pasos
1. Escribir la lista de las diecisiete **antes** de empezar, adaptada al tema.
2. Ejecutarlas en orden, anotando el resultado de cada una.
3. Las que fallen, se arreglan y se vuelven a correr **todas** las que dependan de ellas.

## Reglas duras
- **Repetir el mismo comando diecisiete veces no es verificar diecisiete veces.** Si dos vías usan
  el mismo instrumento, no cuentan como dos.
- **La vía 11 es obligatoria**: en esta casa el detector se equivocó siete veces antes que la pieza.
- **La vía 14 va antes de publicar un cero.** Un cero puede ser un lector mal escrito.

## Verificación
- Están las diecisiete, con su resultado, en el informe del bloque.
