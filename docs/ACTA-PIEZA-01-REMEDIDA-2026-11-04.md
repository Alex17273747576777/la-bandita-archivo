# Acta de la pieza 01 remedida · Facebook · 4 de noviembre de 2026

**Pieza:** `01-El-turno-de-los-que-nacieron-este-trimestre-doce-apps-de-octubre-que-casi-nadie-conoce-y-dos-que-no-aguantan-Facebook-La-Bandita-2026-11-04-dominicano-ES.md`
**Caracteres:** 44.913 (banda Facebook 40.000–45.000)
**Qué se hizo:** no se cambió la fecha y se dejó el texto: se volvió a medir **todo** y se reescribió cada cifra.
**Regla del dueño aplicada:** «prohibido copiar y pegar; hay que re-verificar la información actualizada y actualizar cada dato, no solo la fecha».

## 1 · Lo que cambió al remedir (catorce repos abiertos hoy)

| Programa | Antes (3-nov) | Hoy (4-nov) | Qué cambió |
|---|---|---|---|
| Hush | ★132 · 11 d | ★138 · 12 d | estrellas y madurez |
| ADB/Root Toolbox | ★121 · 110 MiB | ★122 · 108 MiB | estrellas y tamaño |
| APK Toolbox | ★101 · 15 MiB | ★101 · 15,3 MiB | tamaño |
| MineApp | ★70 · 5 MiB | ★72 · 5,2 MiB | estrellas y tamaño |
| Shizuku Sam | ★37 · v13.8.39 | ★40 · **v13.8.40 publicada hoy** | estrellas y entrega nueva |
| Earshot | ★36 · 12 MiB | ★37 · 12,5 MiB | estrellas y tamaño |
| SandFly | ★20 · empujón 3-nov | ★21 · empujón hoy | estrellas y empujón |
| OmniShizuku | ★17 · 10 d | ★18 · 11 d | estrellas y madurez |
| Latch | ★17 · 19 d | ★17 · 20 d | madurez |
| 8bercue | ★17 · 15 d | ★17 · 16 d | madurez |
| Redirect Guard | ★15 · 8 d | ★16 · 9 d | estrellas y madurez |
| Droynis | ★15 · 33 d | ★15 · 34 d | madurez y empujón de hoy |
| WPAForge (rechazado) | ★150 · 40 entregas | ★153 · **10 entregas** | estrellas y un dato falso |
| O3 Root (rechazado) | ★31 · 9 d | ★33 · 10 d | estrellas y madurez |
| ghost-files (mención) | 24 d | 25 d · 20 entregas | madurez |

Suma de estrellas de los doce: **598 → 614**. Rango de madurez: **8–34 → 9–35 días**.

## 2 · Errores propios que la remedición destapó

1. **«Cuarenta entregas publicadas» de WPAForge era falso**: tiene **diez**. Se escribió el 3-nov sin contar la lista y hoy, al contarla, se corrigió.
2. **«Tres Apache» en el reparto de licencias**: son **cuatro** (Shizuku Sam, SandFly, OmniShizuku, Redirect Guard). El total sumaba once licencias y no doce.
3. **«Nueve de las doce no necesitan root»**: la frase no resistía el recuento. Reescrita con precisión: **ninguna exige root**; diez no lo necesitan y dos lo ofrecen como vía.
4. **Censo de la nota al pie**: decía «seis mil quinientas sesenta y cuatro fichas vivas» y el registro tiene **6.838**.

## 3 · Censo remedido hoy (sobre las fichas selladas el 3-nov)

| Dato | Antes (3-nov) | Hoy (4-nov) |
|---|---|---|
| Fichas en el registro | 6.838 | **6.838** |
| Nacidas ≤90 días | 852 | **865** (12,6 %) |
| Con menos de 100★ | 743 (87 %) | **756** (87,4 %) |
| Con menos de 500★ | 805 (93 %) | **805** (93,1 %) |
| Con más de 1.000★ | 41 (5 %) | **41** (4,7 %) |
| Sin licencia declarada | 250 (29 %) | **247** (28,6 %) |
| Sin ninguna entrega | 123 (14 %) | **148** (17,1 %) |
| Con entrega ≤30 días | 411 (48 %) | **390** (45,1 %) |
| Licencias: MIT · GPL-3.0 · Apache · AGPL | 241 · 163 · 135 · 28 | **247 · 165 · 138 · 31** |

Y un dato nuevo que la medición de hoy permite dar: de las **652 joyas nacidas en el trimestre**, **407 no pasan el segundo filtro** (sin descripción, sin licencia o sin entrega). Menos de la mitad de lo recién nacido es un proyecto.

## 4 · Compuertas

| Compuerta | Resultado |
|---|---|
| `manual_gate --pieza` | **VERDE** (M11 44.913 en banda · M29 doce etiquetas) |
| `novedad_gate --corte 2026-11-04` | **VERDE** |
| `envio.py --verificar` | **0 fallos** en los seis envíos de Facebook |

## 5 · Nota de método

El censo se calcula sobre el registro sellado el 3 de noviembre —su evidencia está fechada ese día—; las quince fichas de la pieza se remidieron en vivo hoy. Las dos fechas se declaran en la pieza para que nadie compare peras con manzanas. El archivo pasa con `git mv` de 11-03 a 11-04 porque la fecha del corte es hoy.
