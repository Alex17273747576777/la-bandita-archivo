# Acta — duplicados retirados y recursos nuevos

**Fecha:** domingo 1 de noviembre de 2026, hora de la casa (America/Santo_Domingo).
**Motivo:** el dueño pidió corregir hasta el mínimo error y abrir investigaciones a recursos nuevos. Dos frentes: la numeración del archivo estaba repetida en varios números, y las piezas 01 y 02 se cerraron antes de la segunda ronda de investigación.

## 1. Duplicados de numeración

Regla aplicada: **la serie nueva (2026-10-31 en adelante) es la canónica** para cada número. Para los números sin pieza nueva todavía, se conserva el fichero de fecha más reciente y, en caso de empate, el más largo. Los perdedores **no se borran**: se mueven a `_PRE-2026-10-31/` dentro de su carpeta, con `git mv`, para que el historial quede intacto y cualquiera pueda volver a leerlos.

| canal | movidos a `_PRE-2026-10-31/` |
|---|---|
| WhatsApp | 4 (números 02, 03, 04, 05) + 1 fichero de Facebook que estaba extraviado en la carpeta de WhatsApp (nº 10), devuelto a su carpeta |
| Facebook | 17 (números 02, 03 ×2, 04 ×2, 05, 06, 07, 08, 09, 10, 12, 13, 14, 15, 80, 81) |

Resultado medido: **WhatsApp pasa a 110 ficheros con los números 1–109 completos y sin repeticiones**; **Facebook pasa a 132 ficheros con los números 1–131 completos y sin repeticiones**. Antes: 115 y 148 ficheros, con 5 y 17 números repetidos respectivamente. Total del archivo: **242 piezas** (110 de WhatsApp + 132 de Facebook) y **21 ficheros retirados** conservados aparte.

Consecuencia declarada: el conteo de 263 piezas del HTML de archivo baja a 242, porque 21 ficheros dejan de ser piezas de la serie. El número nuevo se publica en el informe del próximo cierre; no se declara aquí para no adelantar una cifra sin medirla.

## 2. Segunda ronda de investigación

Registrada en `docs/INVESTIGACION-RECURSOS-2026-11-01.md`, sección «Segunda ronda». Cuatro recursos nuevos entraron a la 03 (WhatsApp y Facebook) y diez quedaron en la tabla de candidatos para las piezas siguientes. Dos correcciones obligadas por esa ronda: `Pelski/ytzero` pasa de «sin licencia declarada» a **Unlicense**, y `GrapheneOS/Vanadium` pasa a **NOASSERTION** (hay licencia en el repositorio, la API no la reconoce).

## 3. Estado de las dos piezas 03

| pieza | caracteres | banda | repos medidos | enlaces | respuesta |
|---|---|---|---|---|---|
| 03 WhatsApp | 63.032 | 63.000–63.099 | 33 | 33 | 200 todas |
| 03 Facebook | 43.692 | 40.000–45.000 | 33 | 33 | 200 todas |

Comprobaciones de esta ronda: cero párrafos compartidos entre la 03 de WhatsApp, la 03 de Facebook, la 01 y la 02 de ambos canales; acertijos y mini-quiz descifrados uno por uno (se corrigieron cuatro cadenas invertidas que estaban mal); mapa de lectura regenerado con las 32 secciones en su orden real; emoji duplicado del mini-quiz corregido; las cifras de organizaciones (71) y países (23) unificadas en todo el texto.

## 4. Consecuencias que hubo que arreglar en la tubería

Retirar ficheros rompió dos cosas que estaban bien, y las dos quedan arregladas en esta misma corrida.

**Los envíos quedaron huérfanos.** Los mensajes de `docs/envios/` citaban piezas que ya no existen: 6 en WhatsApp y 18 en Facebook. Se borraron esos envíos huérfanos y se regeneró todo: **110 envíos de WhatsApp con 1.048 mensajes** y **132 de Facebook con 622 mensajes**. La compuerta G9 vuelve a cero fallos.

**El HTML de archivo se llamaba por un número escrito a mano.** Decía 263 y ya no eran 263. `tools/html_archivo.py` ahora cuenta las publicaciones y nombra el archivo con el número real, borrando el anterior si cambia. Resultado de esta corrida: `LAS-243-PUBLICACIONES-2026-11-01.html`, **3.004.646 caracteres · 243 publicaciones (110 WhatsApp + 132 Facebook + el post de comunidad)**. También se añadieron las dos piezas 03 a la lista de «publicaciones de hoy» que el HTML marca como nuevas.

## 5. Estado de la corrida de compuertas (esta misma fecha)

`autoprueba.py` **11/11** · `vara.py` **fallos: NINGUNO** (G0 265 piezas · G1 6.830 fichas · G2 edad máxima 17 d · G3 4.552 ausencia-firmada / 2.069 spdx-api · G4 4.474 vivos / 2.342 dormidos / 14 muertos · G5 10.007 archivos sellados · G6 máxima repetición 2× · G7 2.975 enlaces, 0 binarios recetados · G8 WA n=110 máx 70.009 / FB n=133 máx 43.692 · G9 0 fallos · G10 7 piezas en banda) · sello **10.007 · `e3c2a078eef5ffe2…`**.

**Pendiente declarado, no oculto:** `envio.py --medir` (la medición de los ~700 repositorios que alimenta los envíos) no se pudo correr en esta sesión porque necesita el token de GitHub y la cuota sin token es de 60 consultas por hora. Sin esa medición, los envíos nuevos de la 03 llevan el aviso de que sus repositorios no están medidos «hoy». Se corre en cuanto el dueño pase el token, antes de publicar.
