# ACTA · refinado del repositorio y verificación triple (segunda pasada)

*3 de noviembre de 2026. Se firma lo que se comprobó, con el método al lado. Lo que no se comprobó no se firma.*

**TL;DR —** la segunda pasada cerró el orden de la raíz, abrió una puerta de entrada (`Makefile` + `doctor`), publicó el gobierno del repositorio y añadió el extractor de tareas y el índice de documentos. La verificación se hizo tres veces por caminos distintos: **en disco**, **contra la fuente remota** y **por coherencia interna**. Salieron **10.196 archivos sellados**, **vara con `fallos: NINGUNO`** y la integración continua en **`success`**. Y una cosa que salió mal y se cuenta aquí porque es la prueba de que las compuertas sirven: la primera corrida de la CI **falló**, y falló por algo real.

---

## 1 · Qué se hizo en esta pasada

| Trabajo | Dónde | Resultado |
|---|---|---|
| Consolidar la memoria | `ARCHIVO-HISTORICO/` | 8 carpetas movidas con `git mv`, 2 índices fechados; la raíz pasa de 29 a 24 entradas |
| Corregir las rutas que apuntaban a lo movido | `tools/duplicados.py` · `idioma_mojibake.py` · `sitio.py` | las dos compuertas vuelven a salir con código 0 |
| Abrir una puerta de entrada | `Makefile` · `tools/doctor.py` | 14 destinos idempotentes; veredicto en cinco bloques |
| Extraer el tablero de tareas | `tools/tareas.py` → `docs/TAREAS.md` | 12 tareas · 0 incidencias · 2 declaradas |
| Indexar los documentos | `tools/indice_docs.py` → `docs/INDICE.md` | 49 documentos · 19 familias · 31 herramientas |
| Explicar cada componente | `docs/CODIGO.md` · `ARQUITECTURA.md` | 31 herramientas con su «qué no hace» + 6 decisiones con su coste |
| Publicar el gobierno | `CONTRIBUTING` · `CODE_OF_CONDUCT` · `SECURITY` · `SUPPORT` · `CHANGELOG` · `.github/` · `LICENSES/` · `.reuse/dep5` | REUSE conforme en 13.811 archivos |
| Cerrar el agujero del sello | `tools/sello_reglas.py` | el gobierno y el `Makefile` ahora se sellan: de 10.173 a 10.196 archivos |

---

## 2 · Verificación triple

### A · En disco, con la vara y el sello

```
integridad: 10195 archivos OK · 0 alterados o ausentes · 0 sin sellar · 0 desaparecidos
vara: G0…G15 todas ✓ · fallos: NINGUNO
autoprueba: 14/14 violaciones detectadas · fallos: NINGUNO
reuse lint: conforme (REUSE 3.3) · 13811/13811 archivos con licencia
```

### B · Contra la fuente remota, sin el clon de por medio

Quince archivos de gobierno descargados con la API sobre el commit publicado y comparados por SHA-256 contra el manifiesto local. **13 iguales en la primera pasada, y 2 que no estaban sellados** —`Makefile` y `.reuse/dep5`—, lo que descubrió un hueco real: la lista de rutas selladas no los alcanzaba porque no tienen extensión. Corregido con `EXACTOS` en `sello_reglas.py`, y esa corrección es la que llevó el manifiesto a los 10.196.

Este es el valor de comprobar por fuera: las quince compuertas internas estaban en verde y el sello cubría el contenido, pero **el archivo con el que cualquiera entraba al repositorio no estaba firmado**.

### C · Por coherencia interna, entre documentos distintos

| Qué se cruzó | Contra qué | Resultado |
|---|---|---|
| Numeración de las piezas vivas | `docs/bandas.json` y el LEEME de cada canal | 01→05 sin huecos ni repetidos en los dos canales |
| Longitud de cada pieza | la banda declarada | 12 piezas dentro de banda (WhatsApp 63.006–63.098 · Facebook 40.253–44.994) |
| Envíos publicados | su cabecera, su huella y la pieza de origen | 5 + 5, cero fallos |
| Recuentos de los documentos nuevos | el árbol | 49 documentos · 31 herramientas · 6.838 fichas · 258 piezas |
| Nombres de archivo | el filtro `startswith(("leeme","readme"))` de G0 | `LEEME-de-la-carpeta.md` cumple; el viejo `00-LEEME` no cumplía |

---

## 3 · Lo que falló, y por qué se cuenta

La primera corrida de la integración continua sobre el commit `ec9c9fa` terminó en **`failure`**, en el paso que se había añadido en esta misma pasada: *Índice de documentos generado*. La razón era legítima: `docs/INDICE.md` se había regenerado **antes** de la última edición de `docs/CODIGO.md`, así que el recuento de líneas del índice ya no coincidía con el código. La compuerta nueva hizo exactamente lo que se le pedía —impedir que un derivado viejo viaje como si fuera actual— y la corrección fue regenerar, sellar y volver a empujar (`a190aee`).

Se deja escrito por una razón: un repositorio que solo cuenta sus éxitos no está verificando, está posando. **Una compuerta que nunca ha fallado no ha demostrado nada**; esta falló la primera vez que se la puso a trabajar.

---

## 4 · Estado que queda firmado

| Indicador | Valor | Método |
|---|---|---|
| Commit publicado | `a190aee` (+ el de esta acta) | `git log` |
| CI del commit | `success` | API por `head_sha` |
| Archivos sellados | **10.196** | `registry/_manifiesto-sha256.tsv` |
| Vara | G0–G15 ✓ · `fallos: NINGUNO` | `tools/vara.py` |
| Autoprueba | 14 de 14 violaciones detectadas | `tools/autoprueba.py` |
| Licencias | REUSE 3.3 conforme · 13.811 archivos | `reuse lint` |
| Deudas declaradas | G0: 1 pieza · G13: 5 piezas | `tools/baseline.json` |
| Deudas de estructura | `Arena-Reimagined/` conserva `_versiones/`, `packs/`, `_herramientas/` | declaradas en `MAPA-DEL-ARCHIVO.md` |

---

## 5 · Lo que sigue, sin adornos

1. **Pieza 06 de Facebook · «El taller»** y después **06 de WhatsApp · «El taller en el bolsillo»**: el ciclo va por la 5 de 14 y esa es la deuda que más se nota.
2. **`Arena-Reimagined/`**: mover `_versiones/` (43 referencias), `packs/` (81) y `_herramientas/` (26) en una pasada dedicada, corrigiendo las referencias en el mismo cambio. No se hizo aquí porque mover 150 referencias y cerrar el orden de la raíz en el mismo commit habría hecho imposible saber qué rompió qué.
3. **Remedir** las fichas que cumplan su ventana y marcar como vencidas las que no.

*La Bandita informa a partir de fuentes fechadas.*
