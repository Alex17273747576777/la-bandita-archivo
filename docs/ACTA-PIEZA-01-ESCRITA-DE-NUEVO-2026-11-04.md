# Acta de la pieza 01 escrita de nuevo · Facebook · 4 de noviembre de 2026

**Pieza:** `01-El-turno-de-los-que-nacieron-este-trimestre-doce-apps-de-octubre-medidas-tres-veces-en-un-dia-y-los-dos-que-no-pasan-Facebook-La-Bandita-2026-11-04-dominicano-ES.md`
**Caracteres:** 44.090 (banda Facebook 40.000–45.000)
**Qué es esto:** no una remedición de la anterior, sino **una pieza escrita de nuevo**, con un ángulo que ayer
no existía y no podía existir: la misma lista medida tres veces en doce horas.

## 1 · El ángulo, y por qué no se puede copiar

La versión de ayer se hizo con una sola pasada de datos. Hoy hubo tres: el corte de anoche, la pasada de las 8:45 y
la de las 9:15. Al comparar la segunda con la tercera apareció algo que nadie escribe en una lista de programas:
**las estrellas no se movieron y las descargas sí, y una bajó**.

- SandFly pasó de 2.817 a 2.798 descargas en media hora: **diecinueve menos**.
- Los catorce repositorios con dos pasadas suman 42.330 → 42.335: **+24 y −19, neto +5**.
- Las doce estrellas quedaron idénticas entre las dos pasadas de hoy, y contra el corte de ayer suman **+16**.

Ese contraste es el argumento de la pieza: **un dato sin hora es un rumor con buena letra**.

## 2 · Las habilidades, aplicadas a esta pieza

| Habilidad | Cómo se aplicó | Resultado |
|---|---|---|
| H01 medir antes de tocar | `remedir.py --escribir` → `docs/MEDICION-01-2026-11-04.json` | 17 repositorios con fecha y hora (13:17) |
| H02 la cifra se cuenta | `remedir.py --pieza --medicion` | **AL DÍA**, con un aviso declarado (catálogo de apoyo) |
| H03 la suma cuadra | `remedir.py --suma 138 122 …` | 614 · seiscientas catorce |
| H04 nada de copiar y pegar | `remedir.py --solape` contra la versión anterior | **3,1 %** (tope 25 %) |
| H06 etiquetas | M29 | 12 etiquetas, todas ganadas en el texto |
| H05 sellar al final | `make ritual` | verificar → sellar → comprobar |

## 3 · Errores nuevos, encontrados mientras se hacía

- **E20** · el detector de etiquetas de la casa buscaba el primer 🏷️ del documento y lo encontraba en el **mapa**:
  una pieza con el mapa bien hecho fallaba sin culpa. Corregido para buscar el bloque rotulado.
- **E21** · la comprobación de estrellas exigía la cifra a todo repositorio citado, incluido un catálogo de apoyo.
  Separado en fallo (programa presentado) y aviso (enlace de apoyo).
- **E22** · los totales de descargas se escribieron de cabeza («28.986», «29.008», «cuarenta y una nuevas») y los
  reales son **42.330 → 42.335, +24 y −19**. Cazado al comprobar la aritmética antes de seguir.

Los tres quedan en `docs/ERRORES.md` con su fila y su habilidad.

## 4 · Qué cambió respecto de la versión de ayer

- Título y cuerpo nuevos: el eje es la tercera medición, no la fecha de nacimiento.
- La columna de **descargas** entra en la tabla, con su letra pequeña: cuenta archivos, no personas, y retrocede.
- Los doce fichas llevan **descargas y tamaño**, no solo estrellas.
- WPAForge queda escrito con **diez entregas** —el dato falso de ayer— y se dice en la propia ficha que el número
  se escribió sin contar.
- La mención de ghost-files lleva su versión y su fecha de entrega.

## 5 · Compuertas

| Compuerta | Resultado |
|---|---|
| `manual_gate --pieza` | **VERDE** (M11 44.090 en banda · M29 doce etiquetas) |
| `novedad_gate --corte 2026-11-04` | **VERDE** |
| `remedir.py --pieza --medicion` | **AL DÍA** |
| `remedir.py --solape` | **3,1 %** · escrita de nuevo |
| `envio.py --verificar` | **0 fallos** |

## 6 · Lo que sigue pendiente, dicho sin adornos

La 02, la 05 y la 06 siguen con cifras del 3 de noviembre (error **E19**). Hasta que pasen por `remedir.py` no se
pueden presentar como del día. La 03 y la 04 se midieron el 3 y el 4, y también les toca repaso con la herramienta.
