# Política de duplicados, cachés y datos versionados

*Cierra la incidencia #1 (auditoría del 2026-11-10). Todo lo que se afirma aquí está medido sobre el
HEAD `6a963057` el 2026-11-17; el método se dice al principio para que se pueda repetir.*

---

## 0 · Cómo se midió (y por qué las cifras no son las de la incidencia)

La incidencia hablaba de **742 copias adicionales y 12.691.251 bytes** sobre el snapshot
`8bef36307d6c19661a6b4cbf0db8cf3b50702b08`. Ese commit **no está en este clon**: el clon es
superficial (`.git/shallow`, 2 commits), así que su estado no se puede volver a leer y sus cifras no
se pueden reproducir aquí. Se mide el estado actual, y se dice que es otro.

Método, que no recorre el disco ni depende de `sha256sum` sobre 18.464 ficheros:

```bash
git ls-files -s | awk '{print $2, $4}'      # hash de blob + ruta
git cat-file --batch-check                  # tamaño de cada blob
```

Dos rutas con el mismo hash de blob **son el mismo contenido**, byte a byte: lo dice git, no una
heurística. Sobre `6a963057`:

| | valor |
|---|---:|
| ficheros versionados | 18.464 |
| blobs distintos | 17.919 |
| grupos con duplicados | 360 |
| **copias adicionales idénticas** | **545** |
| **bytes que ocupan** | **13.598.396** |

## 1 · Clasificación por procedencia: nada de esto se borra

| zona | copias extra | bytes | qué es | decisión |
|---|---:|---:|---|---|
| `ARCHIVO-HISTORICO/04-VERSIONES-MULTIIDIOMA` | 357 | 2.607.616 | la misma publicación en varios idiomas y canales | **CONSERVAR** |
| `ARCHIVO-HISTORICO/03-PUBLICACIONES-2026-09-15` | 80 | 569.400 | hornada publicada tal cual salió | **CONSERVAR** |
| `Arena-Reimagined/02-ARCHIVO` | 72 | 8.433.952 | archivo de la entrega (lo que más pesa) | **CONSERVAR** |
| `ARCHIVO-HISTORICO/archivo` | 20 | 230.162 | archivo histórico | **CONSERVAR** |
| `Arena-Reimagined/ENTREGA-29OCT-2026` | 7 | 19.189 | entrega fechada | **CONSERVAR** |
| `registry/_manifiesto-sha256.tsv` ↔ `attestations/lote-2026-11-15.tsv` | 1 | 1.570.811 | el manifiesto vivo y su copia sellada | **CONSERVAR las dos** |
| `corpus-la-bandita/*` | 5 | 165.159 | textos del corpus citados en dos sitios; el mayor es el registro de verificación del 14-09 (149.340 B) | **CONSERVAR** |
| `docs/CENSO-*-2026-11-04{,-tarde}.json` | 2 | 880 | dos censos fechados del mismo día | **CONSERVAR** |

**358 de los 360 grupos están enteros dentro de zonas de archivo o de sello.** Los dos que no son las
parejas de censos del 04-11: `CENSO-audio-2026-11-04.json` y `CENSO-audio-2026-11-04-tarde.json` son
idénticos (486 B), y lo mismo las dos de `CENSO-sistema`. No es basura: son **dos mediciones fechadas
que dieron igual**, y eso es información —dice que entre la mañana y la tarde no cambió nada—. Borrar
una dejaría un hueco en la serie sin ahorrar nada que importe (880 bytes).

El caso grande merece línea aparte. `registry/_manifiesto-sha256.tsv` y
`attestations/lote-2026-11-15.tsv` son el mismo blob (`sha256 e192b6c3…526e`, 1.570.811 B): es lo
esperado, porque el sello es una **copia congelada** del manifiesto en el momento de sellar, y hoy el
manifiesto no ha cambiado desde entonces. Son dos funciones distintas —uno se regenera, el otro no se
toca—, así que deduplicarlos rompería el sentido del sello. `tools/atestar.py`,
`tools/atestacion_verificar.py` y `tests/test_atestar_integridad.py` trabajan sobre esas rutas.

Este documento se sella en el lote de hoy, y eso tiene una consecuencia comprobable: al cambiar el
manifiesto vivo, `registry/_manifiesto-sha256.tsv` deja de ser el mismo blob que
`attestations/lote-2026-11-15.tsv` y esa duplicación de 1.570.811 B desaparece sola. Es la prueba de
que son dos funciones distintas —uno se regenera, el otro queda congelado— y de que el «duplicado» no
era más que un manifiesto que aún no se había movido desde el último sello.

**Conclusión de la casilla 1: de las 545 copias, 0 son candidatas a borrado.** La cifra de la
incidencia no era un pasivo de almacenamiento: era archivo histórico, que es justamente lo que la
propia incidencia anticipaba («parte pertenece a archivo histórico y evidencia»).

## 2 · `docs/_medicion-cache`: evidencia sellada, no caché desechable

100 entradas, ~15 MB, **las 100 versionadas** y **las 100 dentro del manifiesto sellado**
(`grep -c "_medicion-cache" registry/_manifiesto-sha256.tsv` → 100). Son el cuerpo crudo de las
respuestas de la API de GitHub que alimentaron las mediciones de las piezas 24-34:

```json
{"url": "https://api.github.com/repos/aniyomiorg/aniyomi/releases/latest", "codigo": 200, "cuerpo": {…}}
```

`tools/medir_piezas_24_34.py:44` fija el directorio, `:171` deriva la clave
(`sha256(url)[:24]`), `:173` reutiliza lo cacheado y `:202` escribe el payload.

**¿Regenerables? En el sentido trivial sí, en el sentido que importa no.** Volver a ejecutar el script
consultaría la API **hoy**: estrellas, descargas y entregas cambian, así que los payloads serían
otros bytes, el manifiesto sellado dejaría de corresponder y `atestacion_verificar.py` fallaría. La
caché es lo que hace que una medición publicada de noviembre siga siendo comprobable en noviembre:
**es evidencia, se conserva, y si algún día se regenera se sella de nuevo.**

### Defecto encontrado al comprobar esto

El docstring del script (línea 18) dice: *«Cachea cada payload y deja el SHA-256 en el JSON de
medición (evidencia)»*. **La segunda mitad no está implementada.** `docs/MEDICION-34-2026-11-08.json`
no lleva ninguna clave con el sha256 de sus payloads: sus únicas huellas son recuentos
(`huellas_ultima`, `huellas_total`, `nombres_huella`) sobre los adjuntos de las entregas. El único
`sha256` que el script calcula sobre ficheros es el de la **salida** (`:313-314`) y sólo se imprime por
pantalla, no se guarda. La cadena de evidencia existe, pero pasa por el sello del manifiesto, no por
el JSON de medición como promete el comentario. Se documenta aquí en vez de arreglarlo de paso:
cambiar el formato de los JSON de medición publicados tocaría evidencia ya sellada.

## 3 · `registry/registro.db` y `.tmp`

**`registry/registro.db`**: SQLite 3, **7.348.224 B**, versionado, y **fuera del sello** —
`grep -c "registro.db" registry/_manifiesto-sha256.tsv` → **0**, mientras las 100 entradas de caché sí
están. Es la inconsistencia real que deja esta auditoría: el binario mutable más grande de la casa es
el único dato importante que nadie attesta.

Política que queda escrita:

1. **Se versiona.** Es el registro canónico de las fichas y su historia importa más que los bytes que
   ocupa; git ya comprime y este clon es superficial, así que el coste de histórico no se puede medir
   aquí (se dice en vez de suponerlo).
2. **No se sella entero, y se dice por qué:** cada escritura cambia los 7,3 MB, así que un sello por
   lote quedaría obsoleto en la siguiente ficha. Lo que sí conviene —y queda pendiente, no hecho— es
   sellar una **huella del contenido** (recuento de fichas + sha256 del volcado SQL), que es estable y
   comparable entre lotes.
3. **Nunca se edita a mano** ni se «optimiza» con VACUUM dentro de un commit de contenido: un cambio
   de bytes sin cambio de fichas es ruido imposible de auditar.

**`.tmp/`**: existe en disco, está vacío y **no estaba en `.gitignore`**. Un directorio vacío no se
versiona (git no los sigue), pero en cuanto algo lo llene, un `git add -A` se lo lleva. Añadido a
`.gitignore` en este mismo commit, junto a `.boveda/`, `paquetes/` y `*.bundle` que ya estaban.
Comprobado antes de tocar nada: ninguna referencia a `.tmp/` en los scripts ni en el Makefile.

## 4 · Lo que NO se hizo

- **No se borró ni se deduplicó nada.** La incidencia pedía clasificar *antes* de eliminar, y la
  clasificación dice que no hay nada que eliminar.
- **No se arregló el docstring de `medir_piezas_24_34.py`** ni se añadió el sha256 a los JSON de
  medición: ambos cambios tocarían formato de evidencia ya publicada y sellada. Se documentan.
- **No se reprodujeron las cifras de la incidencia** (742 copias / 12.691.251 B sobre `8bef363`): ese
  commit no está en un clon superficial de 2 commits. Las de aquí son de `6a963057`.
