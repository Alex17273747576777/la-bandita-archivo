# 06 · Protocolo de errores

Un fallo no se tapa: se convierte en pieza, en acta o en errata. Este es el orden.

## 1 · Detectar

Las compuertas lo hacen por ti: `vara.py` (G0–G12), `manual_gate.py` (M01–M23), `envio.py
--verificar`, `duplicados.py`, `idioma_mojibake.py`. Si una compuerta no canta, no significa que esté
bien: significa que no estaba mirando.

## 2 · Diagnosticar antes de tocar

- ¿Es un problema de **contenido** (dato falso o viejo), de **forma** (banda, mapa, firma) o de
  **integridad** (envío huérfano, sello roto)?
- ¿Cuántas piezas comparten el fallo? Si son varias, el fallo está en la plantilla o en la
  herramienta, no en el texto.

## 3 · Cirugía real

Se aplica la cura **en la causa**, no en el síntoma: si M23 canta por una línea de licencia repetida,
se redacta propia en cada pieza y se deja constancia de la nueva redacción; si G9 canta por un envío
huérfano, se borra el envío junto con la pieza, en el mismo commit.

## 4 · Orden de retirada de una pieza

`acta` → `pieza` → `envío` → `sello`. Saltarse un paso deja huérfanos que rompen G5 o G9 y obliga a
re-sellar el lote entero.

## 5 · Dejar rastro

Todo arreglo se anota en `docs/ERRATA-AAAA-MM-DD.md` o en el acta del lote, con: qué estaba mal, cómo
se detectó, qué se cambió y qué compuerta lo confirma. Una corrección sin acta es una corrección que
volverá.

## 6 · Reinicio declarado

Si el fallo es de raíz —una lista de piezas construida sobre un supuesto equivocado— la casa reinicia
la lista desde la 01 y lo dice en voz alta. Reiniciar no es fracasar: es no arrastrar el error.

## 7 · Errores conocidos que no se reintentan

Los que ya costaron tiempo: repositorios que devuelven 404, proyectos sin README, servicios que
bloquean la medición. Se documentan en la pieza como **huecos** y no se vuelven a intentar sin motivo
nuevo.
