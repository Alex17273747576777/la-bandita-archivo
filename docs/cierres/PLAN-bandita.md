# Plan de cierre · publicaciones de La Bandita (Facebook-dominicano-ES)

Medido sobre `main` = `ba126654` del repo `la-bandita-archivo`, 8-nov-2026.
Cerrado en `599db05e`, con la vara en `fallos: NINGUNO`.

## Lo que el censo decía, y cómo se resolvió

| Hallazgo | Piezas | Estado |
|---|---|---|
| Falta el comentario fijado | 06, 07, 08, 09, 10, 11, 12, 13, 14, 40 | **10 escritos** (bloque A) |
| Dos versiones de la misma pieza | 32, 33, 34, 35, 36, 37, 38, 39 | **1 por número**, el relleno a `_reemplazadas-2026-11-08/` (bloque B) |
| Cuerpo escrito por plantilla (`generar_piezas.py`) | 32–40 | **Retirado**; la 40 **reescrita entera**; las 8 cortas quedan declaradas sin medición propia (bloques C y D) |
| Voz interna rota dentro del texto publicado | 06 | **Retirada** (bloque D) |
| Afirmación falsa sobre los gigantes | 07 | **Medida otra vez el 8-nov y corregida** (bloque D) |
| Mínimo de longitud inventado | todas las de 31 en adelante | **Doctrina corregida** en `docs/bandas.json`, cabeceras y notas al pie |
| Pieza corta con número de pieza equivocado | 32–39 | **40 piezas renumeradas**, 0 descuadres |

## Doctrina de longitud (corrección de la casa)

El «mínimo obligatorio de 45.000 caracteres» **no existe en Facebook**. Fue una vara interna que
se convirtió en relleno: el generador repetía cinco secciones («Resumen ejecutivo», «Contexto
general», «Análisis técnico profundo», «Comparativa con alternativas»…) con el título de la pieza
metido en medio, y así llegaba a la cifra. Eso viola la regla de la casa: **no se declara lo que
no se midió**.

Doctrina nueva, declarada en `docs/bandas.json`:

* La pieza dura lo que dura su tema. Banda de Facebook: **6.000–45.000 caracteres**; fijado: **900–4.000**.
* Ninguna sección se repite para engordar. Si no hay dato, se escribe «aquí no hay».
* La cabecera deja de afirmar un mínimo que no existe.

## Los seis bloques, todos cerrados

* **A · Comentario fijado 06–14 y 40** — `36638360`
* **B · Una sola versión por número** — `79f6941c`
* **C · Cuerpo real** (la 40) — `a44035fa`
* **D · Mentiras puntuales** — `a44035fa`
* **E · Registro y mapas** (LEEME, bandas, README, CHANGELOG, `tools/leeme_carpeta.py`) — `71f7b280`
* **F · Vara en verde** — `599db05e`

## Lo que sigue abierto, dicho sin adorno

Las piezas **24–29, 32, 33, 34 y 36** son cortas y **no tienen medición propia**: no hay un JSON
de medición detrás de su tema. Se quedan declaradas así en el LEEME en vez de rellenarlas, que es
lo que produjo el problema que este plan vino a arreglar.
