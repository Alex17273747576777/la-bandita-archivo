# Registro de errores · lo que se rompió, cómo se cazó y qué habilidad salió de ahí

Cada error de esta casa, con su número, queda aquí **para siempre**. No se borra uno porque ya se arregló: se
marca como cerrado y se le pone al lado la habilidad que impide que vuelva. Un error sin habilidad es un error
que va a repetirse.

La columna **cazado por** distingue dos cosas que no son iguales: *compuerta* (lo detectó una regla automática) y
*el dueño* (lo detectó una persona leyendo). Los dos cuentan, y la segunda columna es la que más veces ha salvado
la publicación.

| # | Fecha | Dónde | Qué pasó | Cazado por | Habilidad |
|---|---|---|---|---|---|
| E01 | 4-nov | Piezas 01–04 de Facebook | Se publicaron **sin una sola etiqueta**. En Facebook la etiqueta es la única puerta de entrada por nombre de programa. | el dueño | H06 |
| E02 | 4-nov | Pieza 01 | Se afirmó que WPAForge tenía «cuarenta entregas publicadas»: tiene **diez**. Nunca se contaron. | remedición | H02 |
| E03 | 4-nov | Pieza 01 | El reparto de licencias decía «tres Apache» y el total sumaba **once de doce**. Eran cuatro. | remedición | H03 |
| E04 | 4-nov | Pieza 01 | «Nueve de las doce no necesitan root»: la frase no resistía el recuento. Ninguna exige root. | remedición | H02 |
| E05 | 4-nov | Pieza 01 | La nota al pie decía «seis mil quinientas sesenta y cuatro fichas vivas»; el registro tiene **6.838**. | remedición | H02 |
| E06 | 4-nov | Pieza 01 | Se añadieron etiquetas y se cambió la fecha **sin remedir**. El dueño lo llamó por su nombre: eso es copiar y pegar. | el dueño | H01, H04 |
| E07 | 4-nov | Pieza 02 | «En una página» salió con seis párrafos y la vara pide tres a cinco. | compuerta M05 | — |
| E08 | 4-nov | Pieza 02 | La tabla de los ocho programas no declaraba madurez en la cabecera. | compuerta M25 | — |
| E09 | 4-nov | Pieza 03 | Se escribió que «nueve» de los doce leen o escriben KeePass: son **cinco**. | lectura propia | H02 |
| E10 | 4-nov | Pieza 03 | Estrella de Bitwarden desfasada entre la medición de la madrugada y la del cierre (★9.582 → ★9.583). | remedición | H01 |
| E11 | 4-nov | Pieza 03 | «En una página» con seis párrafos otra vez. | compuerta M05 | — |
| E12 | 4-nov | Pieza 04 | Tres cifras escritas de memoria: «ocho nacidos» (eran trece), «nueve con entrega de ayer» (eran once), «diez sin publicar» (eran tres). | cruce con la tabla | H02 |
| E13 | 4-nov | Pieza 04 | Reparto de licencias mal contado: decía 11/7/4 y era 11/8/5 más dos sueltas. | cruce con la tabla | H03 |
| E14 | 4-nov | Pieza 04 | «Nueve declaran ser bifurcaciones»: solo tres lo dicen en su presentación. | lectura propia | H02 |
| E15 | 4-nov | `tools/envio.py` | Al mover las etiquetas al último mensaje se perdió el párrafo final de cada pieza: **la última nota y los tres #task no llegaban al envío**. | `envio.py --verificar` | H07 |
| E16 | 4-nov | Infraestructura | CI en rojo porque se selló **antes** de verificar: `make verificar` reescribe `registry/_vencimientos.json` y el sello quedó viejo. | CI | H05 |
| E17 | 4-nov | Medición | El JSON de medición se **sobrescribió** al medir un subconjunto: la tabla quedó incompleta y hubo que remedir los 26. | revisión propia | H08 |
| E18 | 4-nov | Envíos | Las etiquetas quedaron enterradas en el mensaje 18 de 20 y no se leían. | lectura del envío | H07 |
| E19 | 4-nov | `tools/estrellas` | Las cifras de estrellas de la 02, 05 y 06 siguen siendo del 3-nov: **están pendientes de remedición**. | declarado | H01 |
| E20 | 4-nov | `tools/manual_gate.py` | El detector de etiquetas buscaba el primer icono 🏷️ del documento, que está en el **mapa**, y por eso no encontraba el bloque real. Una pieza con el mapa bien hecho fallaba M29 sin tener culpa. | la pieza 01 nueva | H06 |
| E21 | 4-nov | `tools/remedir.py` | La comprobación de estrellas exigía la cifra a **todo** repositorio citado, incluidos los que solo aparecen como enlace de apoyo (un catálogo). Se separó: cifra exigida a los programas que la pieza presenta, aviso para los de apoyo. | primera corrida de la herramienta | H02 |
| E22 | 4-nov | Pieza 01 | Se escribieron de cabeza los totales de descargas («28.986» y «29.008») y la suma de incrementos («cuarenta y una»). Los reales: **42.330 → 42.335**, +24 y −19. Se cazó al comprobar la aritmética antes de seguir. | revisión propia | H03 |
| E23 | 4-nov | `Makefile` | El objetivo `ritual` verificaba **antes** de sellar, así que fallaba siempre por archivos sin sellar: el mismo error E16 metido dentro de la herramienta que venía a arreglarlo. Ahora la primera pasada puede fallar a propósito y la segunda comprueba el sello. | la primera corrida del ritual | H05 |

## Cómo se usa este registro

1. Antes de escribir una pieza nueva se leen los errores de su misma familia.
2. Si aparece un error nuevo, se añade una fila **el mismo día**, con su número siguiente.
3. Si un error nuevo no tiene habilidad, se escribe la habilidad antes de seguir escribiendo piezas.
4. En cada acta de pieza se citan los números de error que se encontraron durante su escritura.

## Las tres familias

- **Familia del dato** (E02–E05, E09, E10, E12–E14): una cifra que se escribió sin contarla o sin volver a medirla.
  Se ataca con H01, H02 y H03, que son medir, contar y cuadrar.
- **Familia del oficio** (E06, E01, E18): se cumplió la forma y se olvidó para qué sirve. Se ataca con H04 y H06.
- **Familia de la máquina** (E15–E17): una herramienta que hace más de lo que se le pidió. Se ataca con H05, H07
  y H08, que son probar antes de creer.
