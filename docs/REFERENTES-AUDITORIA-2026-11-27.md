# Auditoría de los 6 referentes candidatos · 2026-11-27

*Corte de medición: 2026-11-27 23:3x–23:5x UTC. Todo lo de aquí sale de la API de GitHub en ese
momento o de los archivos descargados, no de memoria ni de lo que decía la ficha anterior.*

Origen: **ALE-67**. Se abre porque los 6 referentes tenían telemetría y release medidos, **pero no
se había ejecutado su suite ni revisado su código**, y eso estaba declarado como límite.

---

## 1 · Lo que se pudo hacer y lo que no, dicho primero

**No se ejecutaron las suites nativas.** Este entorno tiene Java 11, Node 20 y Python 3.13; **no
tiene** Android SDK, Gradle, .NET, Go, Flutter ni Dart. Los seis proyectos son Kotlin/Android, C# o
Dart. Declararlo es el requisito; disimularlo sería mentir en el criterio de cierre.

**Lo que sí se midió**, y es más útil de lo que parece: la **cadena de integridad de cada entrega**
(¿se puede comprobar que el binario que bajas es el que publicaron?) y el **estado real de su CI**
en la rama por defecto, separando `push` de `pull_request`, porque mezclarlos es la forma más común
de leer un CI al revés.

## 2 · Tabla medida

| Referente | ★ | Última release | Assets | Checksum aparte | Tabla SHA-256 en notas | `digest` en la API | CI en `push` |
| :--- | ---: | :--- | ---: | :--- | :--- | :--- | :--- |
| `mihonapp/mihon` | 25.708 | v0.21.3 · 2026-10-25 | 6 | no | no | sí | 21 verde · 11 canceladas |
| `predidit/Kazumi` | 44.310 | 2.4.7 · 2026-11-26 | 9 | no | no | sí | **0 corridas de `push`** (todo por PR: 4 verde, 2 fallo) |
| `Kareadita/Kavita` | 12.192 | v0.9.1.4 · 2026-09-02 | 8 | no | no | sí | 32 verde · 2 fallo |
| `Suwayomi/Suwayomi-Server` | 8.117 | v2.4.2373 · 2026-11-21 | 10 | **`Checksums.sha256`** | no | sí | 6 verde · **34 canceladas** |
| `null2264/yokai` | 1.923 | v1.10.2 · 2026-09-23 | 5 | no | **sí, tabla por variante** | sí | 31 verde · 7 canceladas · 1 fallo |
| `keiyoushi/extensions-source` | 4.939 | *sin release propia* | — | — | — | — | 4 verde · 9 canceladas |

## 3 · Los tres hallazgos que cambian algo

### 3.1 · El «5 de 5 con SHA-256» era verdad, pero por otra razón

El tablero dice **«Referentes maduros (5 de 5) · 100 %»** y **«Total con entregas (9 de 35) · 25,7 %»**.
Medido hoy, de los 5 referentes con release:

- **solo 2 entregan el checksum de forma explícita y comprobable por un humano**:
  `Suwayomi` (archivo `Checksums.sha256` adjunto) y `yokai` (tabla `| Variant | SHA-256 |` dentro de
  las notas de la release, verificada descargando las notas);
- los otros 3 (`mihon`, `Kazumi`, `Kavita`) **no tienen ni archivo ni tabla**: lo que hay es el campo
  `digest` que la API de GitHub calcula hoy al servir el asset.

Eso no es inútil — sirve para comprobar la descarga contra la API — pero **no es lo que la ficha
prometía**: no es un checksum publicado por el proyecto, y **no resiste** que la release se edite o
los assets se reemplacen. La cifra «5 de 5» se sostiene solo si se redefine la palabra «checksum».
Como está escrita, es una promesa más ancha que la prueba.

**Los dos que sí publican, comprobados cruzando las dos fuentes:**

- `yokai`: la tabla de las notas da las 5 variantes y **las 5 coinciden con el `digest` de la API**,
  una por una (Universal, arm64-v8a, armeabi-v7a, x86, x86_64). Dos fuentes independientes que
  concuerdan: eso sí es verificable por quien descarga.
- `Suwayomi`: `Checksums.sha256` descargado, 970 bytes, 9 líneas para los 9 binarios descargables
  (el décimo asset es el propio archivo de sumas). Su línea de `linux-assets.tar.gz` coincide con el
  `digest` de la API.

**Y una comprobación que sí se pudo hacer sin ejecutar nada**: descargué los primeros 2 MB del
`.jar` de Suwayomi y su SHA-256 **no** coincide con el del archivo del release — que es lo correcto,
porque una descarga parcial nunca debe coincidir. Sirve de recordatorio: un checksum solo vale si se
calcula sobre el archivo completo.

### 3.2 · `Kazumi` no tiene CI en `push`: su verde es todo de PR

44.310 estrellas, release de ayer, y en la rama `main` **no hay una sola corrida de CI disparada por
`push`** en las últimas 40: sus 4 verdes y 2 fallos son todos de `pull_request`. Quien mire «CI verde»
y asuma que `main` está construido y probado en cada empuje, se equivoca. No es un defecto — es una
decisión de proceso — pero cambia lo que se puede afirmar sobre el repo más grande del corte.

### 3.3 · El CI de los forks de Mihon no es un CI de `push` en la mayoría de los casos

`mihon`: en `main`, 8 de las últimas corridas de PR quedaron en `action_required` (aprobación
pendiente, no verde), y su último `push` en verde es del **2026-11-22**. `Suwayomi`: **34 de 40
canceladas**. Ninguno de los dos es «rojo»; tampoco son «todo verde», que es lo que sugiere un
porcentaje agregado.

## 4 · Correcciones que hay que hacer en lo ya publicado

| Dónde | Qué dice | Qué debe decir |
| :--- | :--- | :--- |
| `web/observatorio/` (en línea) | «Referentes maduros (5 de 5) · 100 %» | «Checksum publicado por el proyecto: 2 de 5 (40 %)» y, aparte, «digest verificable por la API: 5 de 5» |
| `docs/` y publicaciones ES/EN | «5 de 5 (100 %)» como *checksums* | la misma separación: publicado vs. calculado por el servidor |
| Hoja «Repos_Medidos_37» | `has_sha256_asset` = sí para `mihon`, `Kazumi`, `Kavita` | `checksum_publicado` = no · `digest_api` = sí |
| ALE-67 | criterio de cierre: «6 de 6 con salida de pruebas registrada» | **no se puede cumplir en este entorno**: se cambia a «6 de 6 con cadena de integridad y CI medidos», y la salida de pruebas queda como tarea aparte con su propio entorno |

**Estado de esta corrección (actualizado el 2026-11-27).** La corrección **ya se aplicó** en el
commit `8c0ea1b6`, que lleva por título *«observatorio: separar 'checksum publicado' (2 de 5) del
digest de la API (5 de 5)»*. La versión anterior de este párrafo decía que se estaba reteniendo a la
espera de un visto bueno, y eso dejó de ser cierto en cuanto el commit salió: se deja escrito aquí
porque un documento que se contradice con su propio repositorio es peor que un número equivocado.

Lo que **sigue sin aplicarse** es lo que aquel commit no tocó:

| Dónde | Qué falta |
| :--- | :--- |
| ~~Hoja `Repos_Medidos_37`~~ | **hecho el 2026-11-27**: columnas J `checksum_publicado` (7 de 37) y L `digest_api` (35 de 37) |
| ALE-67 en Linear | el criterio de cierre sigue diciendo «6 de 6 con salida de pruebas registrada» |

La propagación del 2/5 · 40 % a las publicaciones ES/EN y a `datos.json` sí quedó hecha con el
commit; lo que queda pendiente es la hoja y el criterio.

**Sobre el criterio de cierre de ALE-67.** Los seis referentes son Kotlin/Android, C# y Dart. Este
entorno tiene ahora JDK 21, Go 1.24 y el SDK de Android sin plataformas, y **sigue sin** .NET, sin
Flutter/Dart y sin plataformas Android: dos de los seis no se pueden compilar aquí de ninguna
manera, y los otros cuatro necesitan bajar el SDK de su wrapper. Cambiar el criterio a «6 de 6 con
cadena de integridad y CI medidos» es lo honesto; **no se cambia sin tu visto bueno**, porque un
criterio de cierre no lo mueve quien mide.

## 5 · Qué queda pendiente de verdad

- **Ejecutar las suites** de los 6: hace falta un entorno con Android SDK + JDK 17 (mihon, yokai,
  extensions-source), Flutter 3.x (Kazumi), .NET 8 (Kavita) y JDK 21 + Gradle (Suwayomi). Es una
  tarea de CI, no de sandbox: el propio repositorio puede correrla en GitHub Actions con
  `workflow_dispatch` y dejar el registro.
- **`keiyoushi/extensions-source` no publica binarios**: sus APK salen de `keiyoushi/extensions`
  (última tag `e8c7f53`, 2 assets). La ficha debe apuntar allí o decir que no aplica.

## 6 · Cómo se comprobó

- `scripts` del corte: medición por API con y sin token; el rate limit anónimo se agotó a mitad
  (403) y se repitió con token para los tres repos que faltaban. Los dos caminos dieron lo mismo en
  los tres repos medidos dos veces.
- La tabla SHA-256 de `yokai` se leyó **descargando el cuerpo de la release**, no fiándose de un
  resumen: `| Variant | SHA-256 |` con las 5 variantes.
- El `Checksums.sha256` de `Suwayomi` se descargó como archivo (970 bytes, 9 líneas) y se cruzó con
  el `digest` que la API da para los mismos assets.
