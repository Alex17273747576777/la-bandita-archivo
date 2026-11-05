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
| E24 | 4-nov | `Makefile` · CI | El ritual sellaba sin regenerar antes el índice y el tablero: el CI los regenera y compara, así que una fila de más en `ERRORES.md` tumbaba la línea. Ahora `libro` es el primer paso del ritual. | CI rojo en `e3781f10` | H05 |
| E25 | 4-nov | Pieza 05 | La pieza decía «hay cuatro que sacan menos de treinta puntos» cuando su propia tabla publicaba cinco (Aurora 25, NetGuard 25, Seedvault 26, PermissionManagerX 28, Kodi 29). El número se escribió a ojo leyendo la tabla, no contando. | contar la tabla con un programa antes de publicar | H03 |
| E26 | 4-nov | `tools/remedir.py` | La comprobación de estrellas exigía la forma ★N y la guía escribe sus cifras en una columna ★ sin símbolo: daba por desactualizadas quince fichas correctas. Se acepta la cifra como celda de tabla. | primera pasada sobre la 05 | H02 |
| E27 | 4-nov | `tools/remedir.py` | El corte entre cuerpo y enlaces casaba el 🔗 del mapa del principio, así que el cuerpo quedaba reducido a veinte líneas y todo lo demás pasaba por «enlace de apoyo»: una compuerta que se ablanda sola. Ahora el corte exige el encabezado de la sección. | revisión de la 04 | H06 |
| E28 | 4-nov | Piezas 02 y 05 | Dos enlaces del 3-nov ya no existen como se citaban: `krishna3163/best_shizuku_apps_for_android` cambió a `…_no_root` y `thepbone/RootlessJamesDSP` pasó a `timschneeb/RootlessJamesDSP`. Se publicó una dirección que hoy da página no encontrada. | medir los enlaces, no solo las estrellas | H01 |
| E29 | 4-nov | Piezas 03 y 06 | Los títulos llevaban cifras que se mueven solas: «mil seiscientos tres días de silencio» y «mil cuatrocientas siete estrellas». Al remedir cambiaron, y con ellas el nombre del archivo. El título no puede llevar la cifra que cambia cada noche sin que el archivo se renombre. | remedir antes de publicar el título | H01 |
| E30 | 4-nov | Pieza 02 | El censo de audio («ciento doce proyectos, veintitrés de octubre, noventa y tres por debajo de quinientas estrellas») no se podía repetir: la consulta no estaba escrita en ninguna parte. Se retiró y se sustituyó por `tools/censo_tema.py --tema audio`, que imprime sus palabras y su ventana. | intento de repetir la cuenta | H10 |
| E31 | 4-nov | Toda la casa | Un apagón de dos horas dejó la jornada sin fecha comprobada: la medición se firma con la fecha del reloj local, y ese reloj es justo el que se queda atrás cuando se va la luz. Desde hoy la fecha se lee **en vivo, de una fuente de fuera, al empezar y al terminar**. | un apagón | H12 |
| E32 | 4-nov | `Makefile` | El ritual sellaba el árbol y **después** escribía la fecha viva de cierre, así que el sello quedaba con un archivo ya alterado y la compuerta G5 protestaba con razón. La fecha de fin se anota antes de sellar. | primera corrida del ritual con fecha viva | H05 |
| E33 | 4-nov | `tools/escrutinio.py` | El detector de huellas buscaba las formas `.sha256` y `sha256sum` como sufijo del nombre de archivo, y no veía `com.x8bit.bitwarden.apk-sha256.txt`: Bitwarden salía con **cero** huellas cuando tiene **quince**. Se corrigió para buscar la **palabra** (`sha256`, `sha512`, `sha1`, `checksum`, `.sig`, `.asc`, `sums`) en cualquier posición. Repasadas las quince fichas de la pieza 01 y las veintiuna de la 02: los recuentos publicados no cambian. | la pieza 03, al ver que la única que firma salía sin firma | H13 |

| E34 | 4-nov | `tools/remedir.py` · `tools/manual_gate.py` | Dos compuertas trataban lo excepcional como avería. Una: el repositorio bloqueado por la plataforma (código 451, aviso legal) salía como «cifra desactualizada», así que una pieza que **cuenta** el bloqueo no podía pasar la comprobación. Otra: una dirección pegada a un acento grave de código en línea (`…patches\``) no casaba con la lista de enlaces y M07 daba la URL por perdida. Se separó lo declarado de lo fallado: un repositorio sin objeto **medido hoy** se avisa y se cita en la pieza, y el detector de enlaces recorta también el acento grave. | la pieza 06, que gira alrededor del 451 | H14 |

| E35 | 4-nov | `tools/censo_tema.py` | El censo de la pieza 06 se contó **a mano** porque la herramienta de temas solo tenía cuatro palabras declaradas y «parches» no estaba entre ellas: un número que no se puede repetir con una orden no es un censo. Se añadieron los temas **parches**, **televisor** y **casa**, con sus palabras a la vista. Al repetir la cuenta, la herramienta da **58** donde la mano dio **57**: la diferencia es la palabra «patcher», que la mano no buscó. | el censo de la pieza 07 | H15 |

| E36 | 4-nov | Pieza 10 · medición de longitud | La banda se comprobó con `wc -c`, que cuenta **bytes**, y la vara cuenta **caracteres**: en un texto con acentos, estrellas y rayas cada carácter pesa dos o tres bytes. Se recortaron más de dos mil caracteres de prosa buena creyendo que sobraban, y al pasar la compuerta la pieza salió con 43.370 caracteres cuando el cálculo a ojo decía 45.167. | la compuerta M11, después de tres rondas de recorte | H16 |
| E37 | 4-nov | Pieza 10 · fichas en bloque | `novedad_gate` comprueba M25 **por párrafo**: si en un párrafo hay una ficha con menos de cien estrellas, ese párrafo entero tiene que declarar «madurez». Las fichas de la pieza van en un solo bloque por familia, así que ocho familias salieron en rojo con la madurez escrita en otra parte del texto. Se declaró ficha a ficha, solo en las jóvenes, y el rojo se fue. | novedad_gate, primera corrida | H17 |

| E38 | 4-nov | Pieza 11 · nombre del archivo | El título de la pieza llevaba «ciento diecisiete mil descargas» cuando la medición decía **58.427.007**. La cifra se escribió de memoria al nombrar el archivo y no se volvió a contar; el texto de dentro sí la llevaba bien, así que el error solo vivía en el nombre, que es lo que se ve en el índice y en el envío. Se renombró con la cifra calculada. | revisión del nombre antes de sellar | H18 |
| E39 | 4-nov | `tools/remedir.py` · medición de las 20:38 | Tres repositorios salieron con **−1 días** de empujón. La casa fecha en Santo Domingo (UTC−4) y GitHub fecha en UTC: a las 20:38 locales ya es el 5 de noviembre en UTC, así que un empujón de ese mismo instante se restaba contra el día 4 y daba negativo. El recuento de «empujones de hoy» salió en **11** cuando eran **14**. Se corrigió la herramienta para que el día se cuente en la zona de la casa y para que un empujón con fecha de mañana valga cero. | la tabla de la pieza 11, al ver un «hace −1 días» | H19 |

| E40 | 4-nov | Pieza 12 · enlace vetado por la plataforma | La pieza 12 se publicó a las 21:02 y Facebook la retiró veinte minutos después: **no puedes compartir este enlace — `github.com/jackett/jackett` — infringe nuestras Normas comunitarias**. El programa era fontanería de torrentes y el enlace iba en el cuerpo y en la lista de direcciones. No se discutió el criterio: se cumplió. Se remedió entero a las `21:37`, se quitó el repositorio y con él su nombre del cuerpo, de la tabla de reemplazos y del bloque de enlaces (**cero menciones en el texto final**), y en su lugar entraro **ocho** proyectos nacidos en 2026, uno por sección. La compuerta M07 pasó a exigir que **toda** URL del cuerpo aparezca en la lista de enlaces, que es lo que hacía falta para poder revisarlas de un vistazo. | el envío de Facebook, captura del aviso | H20 |

| E41 | 4-nov | Taller · almacenamiento local | Dos veces en la misma noche se perdió trabajo por fiarse del disco de trabajo: el clon vivía en `.cache/` —carpeta que el entorno no conserva— y, al turno siguiente, el directorio del repositorio apareció **revertido a un estado viejo y sin `.git`**. Lo publicado en GitHub estaba intacto (piezas 01–14); lo local, no. Se perdió una medición de 59 repositorios y hubo que repetirla entera. | la segunda pérdida, al abrir el turno | H22 |

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
