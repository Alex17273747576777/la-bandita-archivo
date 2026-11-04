# Acta de la pieza 04 rehecha · Facebook · 4 de noviembre de 2026

**Pieza:** `04-La-lista-del-permiso-veintiseis-medidos-hoy-trece-nacidos-en-el-trimestre-y-el-tronco-que-lleva-quinientos-cuatro-dias-sin-empujar-Facebook-La-Bandita-2026-11-04-dominicano-ES.md`
**Caracteres:** 44.932 (banda Facebook 40.000–45.000)
**Reemplaza a:** `04-La-lista-del-permiso-cuarenta-y-cuatro-medidos-catorce-con-ficha-y-los-nueve-de-la-lista-del-dia-uno-por-uno-Facebook-La-Bandita-2026-11-03-dominicano-ES.md`, movida con `git mv` a `_ARCHIVO-HISTORICO/_reemplazadas-2026-11-03/`.
**Regla aplicada:** lo más nuevo, recién publicado y desconocido primero, medido el día del corte (4-nov-2026).

## 1 · El hallazgo que cambió la pieza

La vieja 04 ordenaba por estrellas y por una lista de enlaces que había llegado por mensajería. La medición de
hoy, con escrutinio de nueve señales sobre 26 programas, invierte el orden: **el tronco del tema saca 40/100 y un
fork de 58 días saca 75/100**. El más famoso lleva 504 días sin empujar y su biblioteca de desarrollo acumula
1.489 días sin entrega.

El segundo hallazgo es de dirección: lo nacido este trimestre **ya no pide el permiso para mandar, lo pide para
medir**. `droynis` (34 días) hace 75 comprobaciones de solo lectura, sin permiso de internet, con flujo
`reproducible.yml` y 74/100.

## 2 · Qué se midió y con qué

| Cosa | Cómo | Resultado |
|---|---|---|
| 26 programas | `GET /repos` + `/releases?per_page=100` | estrellas, nacimiento, empujón, licencia, última entrega, descargas de las 10 últimas |
| Nota de escrutinio | `tools/escrutinio.py --repos` (9 señales, 4 castigos) | acta `docs/ESCRUTINIO-2026-11-04.json`: porter 75 · droynis 74 · Canta 71 · Shizuku 40 · Shizuku-API 15 |
| Censo del dominio | `registry/` con filtro ancho | 6.842 fichas · 564 en el filtro · 86 sin licencia declarada |
| Huellas | adjuntos `.sha256`/`.sums` en las últimas entregas | 5 de 26: porter, droynis, GhostMode, flowpilot, GameCore |

## 3 · Compuertas

| Compuerta | Resultado |
|---|---|
| `manual_gate --pieza` | **VERDE** (M11 44.932 en banda) |
| `novedad_gate --corte 2026-11-04` | **VERDE** (M24 banda de descubrimiento · M25 madurez · M26 «sin movimiento desde» en Shizuku y Shizuku-API · M28 #task 001–003) |

## 4 · Fallos propios cazados, y qué se hizo

1. **Tres cifras escritas de memoria que no cuadraban con la tabla medida**, detectadas al cruzar el JSON antes de
   publicar: (a) decía «ocho nacidos en el trimestre» y son **trece**; (b) decía «nueve con entrega de ayer» y son
   **once entre hoy y ayer** (8 de hoy, 3 de ayer); (c) decía «diez sin publicar desde hace más de un mes» y son
   **tres** (Shizuku 528 d, Shizuku-API 1.489 d, Hail 70 d). Se corrigió el texto y el nombre del archivo.
2. **Reparto de licencias mal contado**: escribí Apache 11 / GPL-3.0 7 / MIT 4 y el real es **Apache 11 · GPL-3.0 8
   · MIT 5 · LGPL-3.0 1 · GPL-2.0 1**, con los 26 declarando licencia. Corregido con la lista de nombres al lado.
3. **«Nueve declaran ser bifurcaciones»**: solo tres lo dicen en su presentación (porter, Shizuku-Next, Nightzuku).
   Reescrito sin el número.
4. **M11 en rojo dos veces** al añadir el párrafo de los seis que quedan fuera (45.737 y 45.411 caracteres): se
   recortó prosa sin quitar datos hasta 44.932.
5. **M25 en rojo** con Shizako ★97 y con el párrafo de los seis (bliss ★0): se añadió «madurez» con los días en
   ambos sitios.
6. **El JSON de medición se sobrescribió** al medir los nueve proyectos nuevos sobre el mismo archivo: se volvió a
   medir los 26 completos para que el acta y la pieza salgan del mismo corte. Nada se publicó con la tabla parcial.

## 5 · Qué se corrigió de la pieza vieja

- Se sustituye el orden por estrellas por el orden por **salud del repositorio**, con los pesos declarados.
- Se añade el censo del dominio y el reparto real de licencias (564 fichas del filtro).
- Se añaden **tres órdenes** verificables (`pm list`, `dumpsys appops`, `dumpsys device_policy`, `diff` de
  inventarios, `sha256sum`) con la salida esperada de cada una.
- Se fechan el tronco y su biblioteca con el día exacto, y se declara la diferencia entre empujar y entregar.

## 6 · Lo que esta pieza no afirma

- No mide el consumo de batería ni audita el código de ningún programa.
- La nota de escrutinio mide salud del repositorio, no calidad del programa; así se dice en la pieza.
- El censo es conservador: cuenta por palabras de la descripción.
