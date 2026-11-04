# ACTA · la memoria a su sitio y el registro remedido

*3 de noviembre de 2026. Dos encargos, dos resultados, y una mentira que apareció de camino y que hay que contar primero porque es la más grave.*

**TL;DR —** (1) `Arena-Reimagined/` quedó ordenado: cinco carpetas de memoria se movieron a `02-ARCHIVO/_etapas-anteriores/` con **cero referencias vivas rotas**, comprobado por una compuerta nueva (G17) que impide que vuelva a pasar. (2) El registro se volvió a medir: **4.098 fichas** contra la API real, de las cuales **4.093 quedaron al día** y **278 resultaron no existir** (404) y se marcan como tales. (3) Y de paso apareció lo importante: **4.186 fichas declaraban haberse medido el 3 de noviembre teniendo como única evidencia una fila del censo del 15 de octubre**. No estaban viejas: estaban mal fechadas, y la compuerta G2 las contaba como recién medidas. Eso ya no puede pasar: hay compuerta nueva (G16) y fecha dentro de cada payload.

---

## 1 · Lo que se movió, y por qué se movió ahí

| Antes | Ahora | Qué es |
|---|---|---|
| `Arena-Reimagined/_versiones/` | `Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/_versiones/` | manual, tratado y lecciones congelados de septiembre |
| `Arena-Reimagined/packs/` | `…/_etapas-anteriores/packs/` | 47 archivos de extras de las series viejas |
| `Arena-Reimagined/_herramientas/` | `…/_etapas-anteriores/_herramientas/` | la lupa, las forjas y el montador de la etapa anterior |
| `Arena-Reimagined/_herramientas-casa/` | `…/_etapas-anteriores/_herramientas-casa/` | una copia suelta de `verificar-suelo.py` |
| `Arena-Reimagined/_referencia/` | `…/_etapas-anteriores/_referencia/` | material de consulta local, excluido del versionado |

La regla que decide el destino es la misma que ya ordenaba la raíz: **el presente en la puerta, la memoria con su fecha.** `02-ARCHIVO/` ya era la carpeta de la memoria del proyecto, y dentro de ella `_etapas-anteriores/` dice lo que es sin necesidad de leer un LEEME.

## 2 · Las referencias, que era el trabajo de verdad

Mover con `git mv` es la parte fácil: git mueve los archivos y **no toca una sola línea de los documentos que los citan**. El árbol queda con rutas muertas y nadie se entera hasta que alguien las sigue. Así se produjo el desorden que se corrigió ayer, y así se habría producido otra vez.

Se contaron antes de mover: **106 menciones de `_versiones/`, 117 de `packs/`, 100 de `_herramientas/`, 4 de `_herramientas-casa` y 21 de `_referencia`**. Después de mover, la pregunta correcta no es «¿cuántas había?» sino «¿cuáles de ellas están en algo que hoy se lee o se ejecuta?». `tools/referencias.py` separa las dos cosas:

- **Vivo** (la raíz, `docs/`, `tools/`, `.github/`, la guía, el registro y lo publicado): una ruta vieja ahí es un **fallo** y detiene la línea.
- **Histórico** (`ARCHIVO-HISTORICO/`, `02-ARCHIVO/`, las entregas, las actas fechadas, `uploads/`): una ruta vieja ahí es una **cita**. Un acta que se reescribe deja de servir como prueba, así que se conserva y el mapa la traduce.

Resultado: **0 rutas vivas rotas** y **307 citas en 47 documentos históricos** que se quedan como están, a la vista.

Se corrigieron, además, tres consumidores reales que habrían fallado en silencio:
`.gitignore` de `Arena-Reimagined/` (apuntaba a `_referencia/mos-v15/`), `HABILIDADES/herramientas/chequeo-niveles.py` (cargaba la lupa desde la ruta vieja) y `HABILIDADES/herramientas/guardar.py` (copiaba los dos talleres desde la ruta vieja). Los tres verificados después del cambio: la lupa carga y expone `medir()`.

## 3 · La fecha que nadie había respaldado

Al empezar a decidir qué fichas había que remedir apareció esto:

```
medido_en: "2026-11-03"          ← lo que la ficha declara
evidencia.payload_ref: "censo-ecosistema-2026-10-15.tsv#…"   ← lo que la respalda
```

**4.186 fichas.** La fecha de la última corrida se había escrito como fecha de medición. El esquema lo prohíbe desde el primer día —«Fecha ISO de la medición. Nunca heredada ni inferida»— pero nada lo comprobaba: G2 lee `medido_en` y lo da por bueno, así que el registro entero figuraba como medido «hoy» con datos de hace tres semanas. Una compuerta que confía en el campo que vigila no vigila nada.

Se corrigió en tres piezas:

1. **`docs/POLITICA-FRESCURA.json`** — las ventanas, cada una con su razón y en un solo sitio: actividad y estrellas 30 días, licencia y scorecard 90, ficha entera 180. Antes estaban repartidas entre un número en la vara y una frase en el calendario de novedades.
2. **`tools/vencimiento.py`** — calcula la edad contra la **evidencia**, no contra la confianza, y escribe `docs/VENCIMIENTOS.md` + `registry/_vencimientos.json` + el bloque `frescura` de cada ficha. Cinco estados: `vigente`, `por_vencer`, `vencida`, `sin_respaldo` y `sin_objeto`.
3. **`tools/censo_medir.py`** — ahora guarda el payload crudo de cada medición en `registry/_evidencia/<id>.json` con la fecha **dentro del archivo** (`_medido_en`) y su SHA-256 en la ficha. Una fecha sin archivo que la sostenga ya no se puede escribir.

Y una cuarta: **G16 en la vara**. Ninguna ficha puede declarar una fecha que su evidencia no respalde, y ninguna puede decir «vencida» sin el motivo escrito.

## 4 · La re-medición, con sus números

| Paso | Resultado |
|---|---|
| Fichas seleccionadas para remedir | **4.098** (4.186 sin respaldo + 7 con scorecard de 71 días, menos las ya remedidas en la prueba) |
| Fichas leídas de la fuente primaria | **4.098** |
| Fichas actualizadas | **4.093** |
| Repositorios que ya no existen | **194** con 404 en esta tanda |
| Sin respuesta | **0** |
| Tiempo | ~10 minutos, 50 repositorios por consulta GraphQL |

Después de la re-medición, y ésta es la foto que queda:

| Estado | Fichas |
|---|---|
| **vigente** | **6.560** |
| **sin objeto** (el repositorio ya no existe) | **278** |
| vencida | **0** |
| sin respaldo | **0** |
| **Total** | **6.838** |

**Por qué 278 y no 194**: la tanda arreó 194, y el resto ya venía marcado de mediciones anteriores con la misma respuesta. Se cuentan todos juntos porque son el mismo veredicto.

## 5 · Un error propio, corregido y anotado

La primera tanda de re-medición fechó las fichas con `date.today()`, que en este entorno es **UTC**: a las 20:30 del 3 de noviembre en Santo Domingo, UTC ya dice 4. Resultado: 4.193 fichas quedaron con fecha del día siguiente. Es exactamente el error que `tools/fecha_casa.py` existe para evitar —y que ya había pasado una vez—, y volvió a pasar porque el programa nuevo no lo usaba.

Se corrigió en el programa (ahora lee `fecha_casa.hoy()`), se refecharon las 4.193 fichas, se reescribieron 3.999 payloads con su `_medido_en` correcto **y se recalculó el SHA-256 de cada uno**: un payload tocado sin re-sellar es peor que un payload mal fechado. Se corrigieron también 3.711 campos `licencia.verificado_en`.

## 6 · Verificación triple

**A · En disco.** Compuertas G0 a G17 en verde (`fallos: NINGUNO`), sello íntegro, autoprueba 14/14, `reuse lint` conforme.

**B · Contra la fuente remota, sin creerle a la ficha.** Diez fichas tomadas al azar de las 6.838 y consultadas de nuevo por REST contra la API, comparando estrellas, último empujón y licencia:

| Resultado | Cuenta |
|---|---|
| Coinciden exactamente | **7 de 8** consultables |
| Difieren solo en estrellas (+14 y +2, medidas media hora antes) | **2** |
| El repositorio ya no existe y la ficha lo declara | **1** |

Las dos diferencias son el reloj, no el método: 14 estrellas sobre 9.727 en media hora es el mundo moviéndose. Se anotan en vez de esconderse, porque una verificación que solo acepta coincidencias perfectas no verifica: decora.

**C · Coherencia interna.** `docs/VENCIMIENTOS.md`, `registry/_vencimientos.json` y los bloques `frescura` de las 6.838 fichas dicen lo mismo (6.560 / 278 / 0 / 0); `tools/referencias.py` da 0 rutas vivas rotas sobre 14.224 archivos revisados; y el índice del registro declara `medido_en 2026-11-03` con rango de un solo día, que es lo que hay.

## 7 · Lo que esto cambia hacia adelante

- **Una ficha ya no puede nacer sin archivo que la respalde.** El payload va con su fecha dentro y su hash en la ficha.
- **La ventana deja de ser un número suelto**: vive en `docs/POLITICA-FRESCURA.json`, con su razón, y la usan el programa, la compuerta y el informe.
- **Mover una carpeta ya no puede romper nada en silencio**: se añade la fila a `tools/referencias.py` y G17 dice si algún archivo vivo se quedó atrás.
- **`make vencer` y `make remedir`** son los dos destinos nuevos; `make referencias` el tercero.

## 8 · Lo que sigue

1. **Los 278 sin objeto** no se pueden remedir: o el proyecto volvió con otro nombre, o no volverá. Se conservan con su motivo y, cuando alguno aparezca con nombre nuevo, se enlaza en la ficha nueva y se anota.
2. **La remisión de diciembre** ya tiene fecha calculada: el bloque `frescura` de cada ficha trae su `proxima_remedicion`, así que la próxima tanda se genera sola con `make vencer`.
3. **Pieza 06 de Facebook · «El taller»** y después **06 de WhatsApp · «El taller en el bolsillo»**: el ciclo sigue en la 5 de 14.

*La Bandita informa a partir de fuentes fechadas.*
