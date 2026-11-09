---
name: censo-de-pieza
version: 2.0.0
dominio: medición
nivel: medidor
cuando: cuando hay medición guardada y hay que convertirla en las cifras madre de una pieza
entradas: [medición en docs/MEDICION-*, tema, banda de longitud]
salidas: [docs/MEDICION-PNN-<fecha>.json con fichas y agregados]
herramientas: [tools/medir_censo.py, tools/elige.py, tools/cuadre.py]
verificacion: [cada ficha tiene repo o hecho, agregados recalculables, cero cifras huérfanas]
depende_de: [medir-recurso, medir-hecho]
---

# Habilidad · censo de una pieza

## Propósito
Recortar el universo medido al tema de la pieza y dejar sus **cifras madre** en un archivo que el
cotejo pueda usar después. Es el paso donde una pieza se vuelve comprobable o se vuelve humo.

## Cuándo se usa
- Después de medir y antes de escribir.
- Al reescribir una pieza vieja con datos nuevos.

## Pasos
1. Elegir el tema y **el filtro exacto**, escrito en palabras que cualquiera pueda repetir.
2. Buscar candidatos por palabra clave con **límites de palabra**. `"ime"` casa con `time` y
   `uptime-kuma`; `"live"` casa con `powerlevel10k`. Sin límites, el filtro miente.
3. Mirar la lista a ojo y contar. Quitar el ruido **por lista explícita** y **narrarlo dentro de la
   pieza** («cae en la tabla por su nombre, se queda y se dice»).
4. Escribir el JSON con la forma de la casa: `fichas` (con `repo` o con `hecho`+`valor`), `fuente`,
   `medido_en`, `medido_a_las`, `tema`.
5. Calcular agregados solo con lo que hay: suma, mediana, mínimos, máximos, conteos de subconjuntos.
   **Ningún agregado se escribe a mano en la pieza**: salen del JSON.

## Reglas duras
- **El filtro se publica con sus números** para que se pueda repetir y llegar al mismo conjunto.
- **Un cero es un resultado, no un fracaso.** Doce de treinta y tres piezas dieron cero sumas y se
  publicaron igual.
- **Nada de relleno para llegar a la banda.** Si el tema da para diez, la pieza tiene diez.
- **La pieza 05 (guía) suma las demás**: su universo de cotejo es la **unión** de todos los JSON,
  no solo el agregado, o el detector marca en falso.

## Verificación
- Contar fichas y compararlo con el número que la pieza dice en su primera línea.
- Cada agregado de la pieza se puede recalcular desde el JSON en un comando.

## Errores conocidos
- Elegir por subcadena y no notar que el más grande de la lista es de otro tema.
- Sumar fichas de repositorios con fichas de hechos: son dos cosas y no se suman.
