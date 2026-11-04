# REGISTRO DE CAMBIOS

Todo lo notable de este archivo, en orden inverso, con la forma de [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) y numeración [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html). Las fechas van en ISO 8601 (`AAAA-MM-DD`).

Criterio de numeración, para que no sea arbitraria: **menor** cuando cambia una pieza publicada, una herramienta o el registro de fichas; **mediano** cuando cambia la estructura del árbol o el contrato de datos; **mayor** cuando cambia la licencia o se rompe una ruta publicada sin traducción en el mapa.

---

## [1.4.0] — 2026-11-03

La pasada de la memoria y del registro. Se movieron cinco carpetas de etapas anteriores
**sin romper una sola referencia viva**, y el registro se volvió a medir contra la fuente
primaria: 4.098 fichas leídas, 278 declaradas sin objeto. De camino apareció lo que había
debajo: 4.186 fichas declaraban una fecha que ningún archivo respaldaba.

### Añadido

- **`tools/vencimiento.py`**: decide qué ficha está `vigente`, `por_vencer`, `vencida`, `sin_respaldo` o `sin_objeto`, midiendo la edad **contra la evidencia** y no contra la confianza. Escribe `docs/VENCIMIENTOS.md`, `registry/_vencimientos.json` y el bloque `frescura` de cada ficha.
- **`docs/POLITICA-FRESCURA.json`**: las ventanas en un solo sitio, cada una con su razón —actividad y estrellas 30 días, licencia y scorecard 90, ficha entera 180—. Antes eran un número suelto en la vara y una frase en el calendario de novedades.
- **`tools/referencias.py`**: la tabla de mudanzas del repositorio y el auditor que distingue una ruta vieja citada por un archivo vivo (fallo) de una citada por un acta (cita que se conserva y se traduce).
- **Compuerta G16 · fecha respaldada**: ninguna ficha puede declarar una fecha que su evidencia no sostenga, ni decir «vencida» sin motivo escrito.
- **Compuerta G17 · rutas vivas**: ninguna carpeta movida puede seguir citada por su ruta vieja desde un archivo que hoy se lee o se ejecuta.
- **`make vencer`**, **`make remedir`** y **`make referencias`**: los tres destinos nuevos del `Makefile`.
- **`docs/ACTA-REMEDICION-2026-11-03.md`**: el acta de la pasada, con sus números y con el error propio que hubo que corregir.

### Cambiado

- **`Arena-Reimagined/_versiones/`, `packs/`, `_herramientas/`, `_herramientas-casa/` y `_referencia/`** → `Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/`. Cinco carpetas, 70 archivos, y las referencias corregidas en el mismo cambio.
- **`tools/censo_medir.py`**: guarda el payload crudo de cada medición en `registry/_evidencia/<id>.json` con la fecha **dentro del archivo** y su SHA-256 en la ficha; acepta `--vencidas` y `--solo` para remedir solo lo que hace falta en vez del registro entero; y fecha con `fecha_casa.hoy()` en lugar de `date.today()`.
- **`tools/registro_construir.py`**: modo `--indice`, que refresca el índice del registro desde el disco sin reconstruir las fichas —reconstruirlas desde el censo habría borrado la re-medición—.
- **`schemas/ficha.schema.json`**: se declara el bloque `frescura` (estado, días, evidencia, próxima remedición, ventana y motivo).
- **`MAPA-DEL-ARCHIVO.md`** y **`README.md`**: la deuda de estructura deja de ser deuda y pasa a ser una mudanza hecha, con su tabla de traducción de rutas.

### Corregido

- **4.186 fichas declaraban `medido_en: 2026-11-03` con una fila del censo del 15 de octubre como única evidencia.** La compuerta G2 leía `medido_en` y las contaba como recién medidas. Se remediation leyendo la API y hoy ninguna ficha declara una fecha sin respaldo.
- **194 + 84 repositorios de la lista ya no existen**: sus fichas se marcan `sin_objeto` con el motivo escrito, en vez de seguir contando como vigentes.
- **La re-medición fechó con UTC**: 4.193 fichas quedaron con el día siguiente al de la casa. Se refecharon y se recalcularon los SHA-256 de 3.999 payloads y las fechas de 3.711 licencias.
- **`Arena-Reimagined/.gitignore`**, `HABILIDADES/herramientas/chequeo-niveles.py` y `HABILIDADES/herramientas/guardar.py` apuntaban a las carpetas movidas: son consumidores reales y se corrigieron con la mudanza.

### Verificado

- Vara: **G0 a G17 en verde**, `fallos: NINGUNO`.
- Registro: **6.838 fichas · 6.560 vigentes · 278 sin objeto · 0 vencidas · 0 sin respaldo**.
- Referencias: **0 rutas vivas rotas** sobre 14.224 archivos revisados; 307 citas históricas conservadas en 47 documentos.
- Contra la fuente remota: 10 fichas al azar consultadas otra vez por REST; 7 coinciden al dato, 2 difieren solo en estrellas (+14 y +2 en media hora) y 1 declara correctamente que el repositorio no existe.

---

## [1.3.1] — 2026-11-03

La pasada de orden. Se hizo porque el archivo, que presume de verificar, tenía la raíz con 29 entradas, dos carpetas de canal con **números repetidos** y rutas que las actas citaban y ya no existían. Nada de lo aquí listado cambia una pieza ya publicada: se corrige hacia adelante.

### Añadido

- `ARQUITECTURA.md`: las tres capas, el sentido del dato en cinco pasos, seis decisiones con su contexto y su coste, y los números del corte.
- `docs/CODIGO.md`: las 31 herramientas explicadas una por una —qué recibe, qué hace, qué produce y **qué no hace**— más tres invariantes.
- `tools/tareas.py`: extrae el tablero de tareas de las piezas y los documentos, y falla si una pieza repite número o salta uno dentro de su propia serie. Salida: `docs/TAREAS.md`, 12 tareas, 0 incidencias, 2 declaradas.
- `tools/indice_docs.py`: índice de documentos con resumen largo verificado. Salida: `docs/INDICE.md`, 49 documentos en 19 familias y 31 herramientas.
- `tools/doctor.py`: cinco bloques de diagnóstico y un veredicto. Se niega a decir LISTO si falta una pieza esencial.
- `Makefile`: catorce destinos (`ayuda`, `doctor`, `verificar`, `sellar`, `compuertas`, `licencias`, `generar`, `sitio`, `tareas`, `indice`, `libro`, `medir`, `publicar`, `push`) para que el primer comando no haya que adivinarlo.
- Archivos de salud comunitaria: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `CHANGELOG.md`, plantillas de incidencia y de solicitud de cambio, y `CODEOWNERS`.

### Cambiado

- **`ARCHIVO-HISTORICO/`**: ocho carpetas de memoria (`03-PUBLICACIONES-2026-09-15`, `04-VERSIONES-MULTIIDIOMA`, `backup-previo-correccion-14-09`, `archivo`, `site-demo`, `datos-censo`, `datos-miyomi`, `datos-v25`) consolidadas en una sola, con `INDICE-2026-10.md` y `MANIFIESTO-2026-10.md`. La raíz pasa de 29 a 24 entradas.
- **El sello ahora cubre el gobierno del repositorio.** `tools/sello_reglas.py` no sellaba `Makefile`, `ARQUITECTURA.md`, los archivos de salud comunitaria, `.github/`, `LICENSES/` ni las licencias: el README podía cambiar sin que la integridad lo notara. Con la corrección, el sello pasa de 10.173 a **10.196 archivos**.
- Rutas de herramienta corregidas en `tools/duplicados.py`, `tools/idioma_mojibake.py` y `tools/sitio.py`, que seguían apuntando a las carpetas movidas. Las dos compuertas vuelven a salir con código 0.
- `README.md` y `MAPA-DEL-ARCHIVO.md` revisados: tabla de rutas anteriores traducidas, estado del corte y punto de entrada único.

### Corregido

- El resumen del índice tomaba la primera línea no vacía y devolvía fragmentos que empezaban a media frase («tras la limpieza del 2-nov, con su huella…»). Ahora une el párrafo antes de leerlo, exige que empiece en mayúscula o signo de apertura y corta en oración completa; los documentos sin primera oración con cuerpo se marcan en vez de quedar en blanco.
- `_archivo-historico/` (con guion bajo) duplicaba la función de `ARCHIVO-HISTORICO/`; se eliminó tras mover su contenido.
- El `LEEME` de la carpeta de canal llevaba un prefijo numérico `00-` que lo sacaba del filtro `startswith(("leeme","readme"))` y hacía fallar la compuerta G0 por el latido y la fecha. Renombrado a `LEEME-de-la-carpeta.md`.

### Verificado

- `vara.py`: **fallos NINGUNO** en las quince compuertas.
- `atestar.py`: **10.196 archivos**, huella encadenada en `attestations/lote-2026-11-03.json`.
- Integración continua: `success` sobre el árbol sellado.
- `envio.py --verificar`: 5 de 5 en Facebook y 5 de 5 en WhatsApp, cero fallos.

---

## [1.3.0] — 2026-11-03

### Añadido

- Pieza **05** de cada canal: «la guía maestra» en Facebook y el resumen de bolsillo en WhatsApp, con su tabla de bandas y su parte de envío.
- `docs/envios/{facebook,whatsapp}/` con los envíos medidos y verificados de las cinco piezas de cada canal.

### Cambiado

- `MAPA-DEL-ARCHIVO.md` y `README.md` con el bloque de estado del corte.

---

## [1.2.0] — 2026-11-02

### Añadido

- **Guía maestra**: 70 fichas medidas en 12 capítulos, con autor, licencia, versión, fecha de medición y límite declarado de cada aplicación; más el comando único `guia_maestra.py --compuertas --generar --estricto` (70 fichas, 12 páginas, 0 fallos).
- Créditos completos de los creadores y las licencias de cada obra citada, conforme a `LEGAL/`.

### Corregido

- Autor mal atribuido en la familia de clientes de YouTube alternativos: la atribución correcta es la del repositorio vigente, no la del espejo.

---

## [1.1.0] — 2026-10-28

### Añadido

- Ciclo vivo de canal con plan de catorce piezas: 01 la puerta y el recibo · 02 la música · 03 la caja del bolsillo · 04 la lista del permiso · 05 la guía maestra · 06 el taller · 07 la pantalla grande · 08 la red · 09 archivos y nubes propias · 10 privacidad comprobable · 11 cuando algo se rompe · 12 el oficio · 13 remisión de diciembre · 14 la lista del día uno.
- `LEEME-de-la-carpeta.md` en cada canal con el estado, el plan y la regla de convivencia con el archivo histórico.

### Cambiado

- Las piezas anteriores pasan a `_ARCHIVO-HISTORICO/<mes>/` y conservan su fecha y sus fallos.

---

## [1.0.0] — 2026-10-15

### Añadido

- Piezas 01 a 04 de Facebook y 00 a 04 de WhatsApp, con las dos compuertas en verde, el sello encadenado y la integración continua en `success`.
- Las quince compuertas de la vara, el sello `atestar.py` y las herramientas de medición sobre las que se apoya todo lo demás.
- `LICENSE`, `LICENSE-CONTENIDO`, `LICENSE-DATOS` y `NOTICE`: código, texto y datos con condiciones distintas, declaradas por archivo según las prácticas de REUSE.

---

*La Bandita informa a partir de fuentes fechadas.*
