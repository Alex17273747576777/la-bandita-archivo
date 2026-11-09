---
name: cotejar-cifras
version: 2.0.0
dominio: control de calidad
nivel: puerta
cuando: después de escribir, antes de declarar nada verificado
entradas: [pieza publicada, su JSON de medición]
salidas: [informe de cifras sin respaldo y mal atribuidas]
herramientas: [tools/coteja.py, tools/vara.py]
verificacion: [0 cifras sin respaldo, 0 mal atribuidas, 0 rutas rotas]
depende_de: [escribir-pieza]
---

# Habilidad · cotejar las cifras

## Propósito
Que **cada número de la pieza exista de verdad en el archivo del que dice salir**, y que la cifra
pegada a un nombre sea un campo de ese nombre. Un verde que no se midió contra nada no es un verde.

## Cuándo se usa
- Después de cada escritura, sin excepción.
- Antes de cualquier `commit` que diga «verificado».

## Pasos
1. `python3 tools/coteja.py --todo` — recorre las piezas y sus JSON.
2. Leer dos cifras: **sin respaldo** (no está en el JSON) y **mal atribuidas** (está, pero es de otro).
3. Donde falle, decidir quién se equivoca: la pieza, el JSON **o el detector**.
4. `python3 tools/vara.py` para las compuertas del repositorio (17 en total, con bandas, firmas y rutas).

## Reglas duras
- **Se arregla el detector, nunca se baja el listón.** Siete rondas de esta casa fueron el detector
  equivocado antes que la pieza: años contados como cifras, números en palabras, ventanas de
  atribución que cruzaban al repo vecino, coincidencias por subcadena (`1.665` dentro de `11.665`).
- **Un identificador no es una cifra.** Un UUID contiene `4843` y un sha256 contiene grupos que
  parecen números: se limpian antes de contar, no se cuentan.
- **Un nombre mudado no es un cero.** Comparar contra la lista de FMHY sin mirar los nombres viejos
  dio 16 falsos positivos en una sola pasada.
- **Nada se declara verificado en dispositivo** si no se midió en dispositivo.

## Verificación
- El informe termina en `N cifras revisadas · 0 sin respaldo · 0 mal atribuidas`.
- La lista de nombres mudados se aplicó también al propio detector.

## Errores conocidos
- Dar por bueno un número porque existe en el JSON: puede existir y estar pegado a otro repositorio.
- Cotejar la guía 05 contra su solo agregado y marcar 35 cifras en falso: su universo es la unión.
