# 05 · Método de medición

El valor de esta casa no está en lo que publica: está en que lo publicado se puede volver a medir.

## Las tres lecturas

Cada recurso se lee **tres veces por caminos distintos**, con el orden rotado entre recursos para que
ningún orden favorezca un resultado:

| Lectura | Fuente | Qué se toma |
|---|---|---|
| 1 | API de búsqueda de GitHub | estrellas, licencia, lenguaje, último empujón |
| 2 | Página del repositorio (HTML renderizado) | lo que ve una persona: descripción, avisos, archivo |
| 3 | Contenido crudo (`raw.githubusercontent`) | README y archivo de licencia, leídos literalmente |

Cuando las tres **no coinciden** en un campo, no se elige el número que más gusta: **se descarta el
campo** y la pieza lo dice. Cuando coinciden, se guarda en `docs/envios/_medicion-{canal}.json` con
`tres_lecturas.py --guardar`.

## Ventana y evidencia

- Toda pieza declara el **día y la hora** del corte en hora de Santo Domingo, con el rango completo
  («entre las 07:58 y las 09:12»).
- Las versiones se toman de la lista de publicaciones de cada proyecto, **una por una**; la ficha
  automática las devuelve vacías con frecuencia y eso no se rellena.
- Empujón y paquete son dos datos distintos: la **brecha** se mide desde el paquete, no desde el
  empujón, y se publica en días.
- Si un campo no se pudo leer, se escribe **«sin paquete»**, **«sin conclusión»** o **«no consta»**.

## Cuándo un dato está rancio

180 días para el registro general (G2). Una pieza de hace un año sigue siendo válida como pieza y su
dato ya no lo es: se dice. Las piezas no se «actualizan» en silencio; se reescriben con censo nuevo y
se cierra la anterior con acta.

## Los números que se publican

Estrellas exactas (sin redondear), suma por grupos cuando aporta, mediana cuando el promedio engaña,
reparto porcentual explicado en palabras y ningún total que no se pueda reconstruir desde la tabla.
