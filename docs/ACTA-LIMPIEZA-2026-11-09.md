# ACTA DE LIMPIEZA · 9 de noviembre de 2026

*Qué se limpió, qué se guardó y qué pesa todavía. Donde no se puede limpiar sin dañar el
repositorio, se dice aquí en vez de hacerlo a escondidas.*

## Lo que se limpió

| Qué | Dónde | Destino |
|---|---|---|
| 2 duplicados exactos del issue y la respuesta | raíz de `/home/user` | borrados: el repo ya tenía la versión mejor (con enlace y HTTP 201) |
| 3 documentos de cierre (`PLAN`, `CIERRE-publicaciones`, `CIERRE-nueve-piezas`) | raíz de `/home/user` | **versionados** en `docs/cierres/` antes de borrarlos |
| `fijados_24_34.py` | raíz de `/home/user` | `docs/cierres/…-SUPERADO-por-tools-fijados.py`: hizo las piezas 24–34, hoy las hace `tools/fijados.py` |
| `.wget-hsts`, `.sudo_as_admin_successful` | raíz de `/home/user` | borrados |
| `__pycache__` y `*.pyc` | todo el árbol | borrados |
| `.android/cache` (6,2 MB), `.gradle/*` | caché de build | borrados: se regeneran al compilar |
| `docs/.estado-lote.json`, `docs/.metricas-lote.json` | repo | **sacados del versionado** y añadidos a `.gitignore`: son estado de ejecución con horas y hashes que cambian en cada corrida |

## Lo que se guardó a propósito

- **Los tokens** (`.gh-tokens`, `.gh-token`, `.gh-credential`, `.gh-token-idx`): son lo único que
  la casa permite en el almacenamiento interno.
- **`/home/user/bd/f`** (17 MB): el clon de `fmhy/edit`. No es basura; es la fuente primaria de la
  pieza 41 y de la comprobación de los 385 repositorios. Se queda.
- **`/home/user/.android`** (512 B tras la limpieza) y **`.gradle`** (vacío): solo queda el ajuste de
  analítica; se borra solo si se deja de compilar para Android en esta máquina.

## Lo que pesa y no se puede limpiar aquí

`.git` mide hoy **177 MB**, medido con `du -sm .git` después de `git gc --prune=now` (antes: 188 MB). El `gc` recogió unos once megas de objetos sueltos; el resto es historia y no se va con `gc`. Su peso son objetos históricos, y el mayor es:

```
22,4 MB  paquetes/push-etapa5.bundle
```

Ese archivo está **ignorado hoy** (`.gitignore` ya excluye `paquetes/` y `*.bundle`) pero vive en la
historia. Sacarlo de verdad exige **reescribir la historia** con `git filter-repo`, y eso cambia todos
los hashes de commit: los `sha` que citan las piezas y las atestaciones dejarían de coincidir con lo
que hay en el remoto.

**No se hace.** La regla de la casa es que lo publicado no se reescribe en silencio, y una reescritura
de historia es exactamente eso. Si algún día hay que adelgazar el clon, se hace en una rama aparte,
con el dueño avisado y con las atestaciones regeneradas — no como parte de una limpieza.

Lo demás del peso son cuatro versiones del `catalogo-la-bandita.html` (8,5 MB cada una) en
`Arena-Reimagined/02-ARCHIVO/`. Son evidencia fechada del archivo, no basura: se quedan.

## Cómo se comprueba que quedó limpio

```
git status --porcelain            # nada sin dueño
git status --ignored --porcelain  # nada ignorado por accidente
git rev-list --count origin/main..HEAD   # 0 commits sin subir
find /home/user -maxdepth 1 -type f      # solo los tokens
```
