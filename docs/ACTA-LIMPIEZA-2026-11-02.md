# Acta de limpieza · 2 de noviembre de 2026

**Qué se hizo:** retirar del árbol `paquetes/`, once exportaciones comprimidas del propio
repositorio que no aportaban un solo dato nuevo. Un paquete es **salida, nunca fuente**: se
regenera desde el árbol, y lo que contenía sigue aquí y en el historial.

**Corte:** lunes 2 de noviembre de 2026, noche (America/Santo_Domingo) · **commit base:** `fb2129e4`  
**Retirado:** 11 archivos · 62.20 MB  
**Sellos afectados:** ninguno. `paquetes/` no entra en `tools/sello_reglas.py`, así que
`registro/_manifiesto-sha256.tsv` y la cadena de `attestations/` quedan intactos y `vara.py` sigue
en verde sin re-sellar.

## Inventario de lo retirado

| Archivo | Bytes | Blob (recuperación) |
|---|---:|---|
| `paquetes/La Bandita â Corpus 2026-09-10.zip` | 2.385.168 | `52fcb21794de` |
| `paquetes/La Bandita â Versiones 2026-09-15 â ingles-US.zip` | 1.073.467 | `a7520b200b8f` |
| `paquetes/La Bandita â Versiones 2026-09-17 â coleccion-continuacion.zip` | 4.556.741 | `78bd28ab87ca` |
| `paquetes/La Bandita â Versiones 2026-09-18 â cierre-frances-FR.zip` | 3.637.577 | `c5624e58f534` |
| `paquetes/La Bandita â Versiones 2026-09-19 â apertura-pt-br.zip` | 3.704.724 | `c0e280609451` |
| `paquetes/La Bandita â Versiones 2026-09-19 â pt-br-10-13.zip` | 3.815.398 | `54f0e1dd1438` |
| `paquetes/La Bandita â Versiones 2026-09-19 â pt-br-fundacion.zip` | 3.773.004 | `7f1ac83cd7a9` |
| `paquetes/La Bandita â Versiones 2026-09-20 â continuidad.zip` | 5.910.996 | `d865bdc8ac93` |
| `paquetes/La Bandita â Versiones 2026-09-20 â corte-multilengua-80.zip` | 3.930.141 | `22ca1c77e023` |
| `paquetes/bandita-continuidad-2026-09-20.zip` | 5.910.996 | `d865bdc8ac93` |
| `paquetes/push-etapa5.bundle` | 23.500.089 | `5cafd65225e2` |

## Por qué

1. **Son exportaciones, no originales.** Cada ZIP contiene piezas que ya están en
   `Arena-Reimagined/01-PUBLICACIONES/` y `04-VERSIONES-MULTIIDIOMA/`; el `.bundle` es un respaldo
   del propio repositorio, que ya vive en GitHub.
2. **Hay un duplicado exacto.** `… Versiones 2026-09-20 — continuidad.zip` y
   `bandita-continuidad-2026-09-20.zip` son el mismo contenido con otro nombre (5.910.996 bytes,
   blob `d865bdc8`).
3. **Coste desproporcionado.** 62,20 MB de archivos binarios versionados que crecen en cada clon y
   en cada descarga del archivo, a cambio de cero información adicional.
4. **Riesgo evitado.** Un ZIP fechado en septiembre se puede confundir con el estado actual;
   regenerarlo obliga a mirar el árbol de hoy, que es lo correcto.

## Lo que se miró y **no** se retiró

| Ruta | Peso | Decisión | Motivo |
|---|---:|---|---|
| `Arena-Reimagined/01-PUBLICACIONES/` | — | se queda | corpus vivo: 275 piezas |
| `Arena-Reimagined/02-ARCHIVO/` | — | se queda | madres de la tanda del 15-sep: evidencia de redacción |
| `03-PUBLICACIONES-2026-09-15/` | 1,4 MB | se queda | su texto coincide con el canónico, pero prueba **qué se publicó y cuándo** |
| `04-VERSIONES-MULTIIDIOMA/` | 11 MB | se queda | traducciones reales (EN 560, FR 150, PT-BR 54); se comprobó que no son copias del español |
| `uploads/` | 14 MB | se queda | originales recibidos, con fecha de entrega |
| `backup-previo-correccion-14-09/` | 0,11 MB | **se queda** | se comprobó que **no** son copias de `uploads/`: son las versiones **previas a la corrección**, y esa diferencia es la evidencia de la cirugía |
| `archivo/` | 720 KB | se queda | respaldo de piezas antiguas con índice |
| `site/` | 19 MB | se queda, marcado **generado** | lo produce `tools/sitio.py`; se regenera entero, no se edita a mano |
| `site-demo/resultados.html` | 68 KB | se queda | entregable del panel de resultados |
| `registry/` | 60 MB | se queda | 6.830 fichas medidas: son datos, no copias |
| `docs/` | 11 MB | se queda | actas, mediciones y envíos: la prueba del método |

## Duplicados que siguen vivos, y por qué

`tools/duplicados.py` censó 2.351 archivos y encontró 277 grupos idénticos (441 copias sobrantes,
3,2 MB). Casi todos son coincidencias **entre carpetas con funciones distintas**: la misma pieza en
su carpeta de canal y en el conjunto fechado de publicación, o la versión dominicana repetida en
`facebook/` y `whatsapp/` de `04-VERSIONES-MULTIIDIOMA/`. Borrar una de las dos destruiría la prueba
de que existió publicación en ese canal y esa fecha. **Se conservan y se declaran**: esa duplicación
es documental, no basura.

## Verificación posterior

- `python3 tools/vara.py` → G0–G12 sin cambios (ninguna ruta retirada estaba sellada).
- `python3 tools/duplicados.py` → sin grupos nuevos.
- Árbol de trabajo: **209 MB** (antes 269 MB). `.git` conserva 158 MB con todo el historial.

## Reversión

```bash
git show fb2129e4:"paquetes/<nombre del archivo>" > <destino>
```

Si hace falta otra vez el paquete de septiembre, se **regenera** desde el árbol en lugar de
recuperar el ZIP: es más honesto y no arrastra el riesgo de publicar una instantánea vieja.
