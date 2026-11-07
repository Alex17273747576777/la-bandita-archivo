# INFORME DE CIERRE · sábado 31 de octubre de 2026

Fecha de la casa: **sábado 31 de octubre de 2026** (America/Santo_Domingo, UTC-4). Todas las corridas
de GitHub Actions con marca 1-nov en UTC pertenecen a esta misma jornada.

**Repo:** `Alex17273747576777/la-bandita-archivo` · `main` en **`f36890c`** (tres subidas hoy:
`7e8f737` → `5934d54` → `f36890c`), verificado en clon fresco.

---

## 1 · Lo que quedó cerrado y medido

| Compuerta | Resultado literal de la última corrida |
|---|---|
| G0 piezas | **261 piezas · 260 con 💓 · 261 con dateline** (1 deuda congelada, declarada en `tools/baseline.json`) |
| G1 esquema | **6.830 fichas** conformes al contrato |
| G2 frescura | edad máxima **16 d** · mediana 16 d · umbral 180 d |
| G3 licencia | `ausencia-firmada` 4.552 · `spdx-api` 2.069 · `texto-license` 207 · `endpoint-license` 2 |
| G4 actividad | **vivo 4.474 · dormido 2.342 · muerto 14** (los 404 ahora se registran como muertos) |
| G5 integridad | **9.746 archivos sellados** · huella `7b798de41e3b755a…` |
| G6 anti-plantilla | máxima repetición interna 2× (en `09-Herramientas-FOSS…`) |
| G7 enlaces | 2.914 enlaces revisados · 0 binarios recetados |
| G8 presupuesto | WhatsApp n=113 (mediana 2.719 car.) · Facebook n=148 (mediana 2.402) |
| **fallos** | **NINGUNO** · `autoprueba.py` **8/8** violaciones detectadas |

Datos remedidos: **2.644 fichas** con fecha 2026-10-31. De ellas, **14 muertas** registradas con su
404 en vez de descartarlas en silencio — la ausencia también es un dato.

## 2 · Firma (Sigstore, sin llave)

- Corrida CI **41263142528** sobre `f36890c` → 14/14 pasos en verde.
- Artefacto `atestacion-firmada` (10.767 B) descargado de esa corrida y verificado:
  `cosign verify-blob` → **`Verified OK`**, identidad
  `https://github.com/Alex17273747576777/la-bandita-archivo/`, emisor
  `https://token.actions.githubusercontent.com`.
- El digest firmado (b64 decodificado) es **`7b798de41e3b755a…`**, idéntico al sha256 del
  `registry/_manifiesto-sha256.tsv` local: **9.746 archivos**. La firma corresponde a este estado, no
  al anterior (`0e09d098…`), que quedó registrado como `huella_lote_anterior`.

## 3 · Servidor MCP · listo para que lo dispares tú

- `server.json` **valida** contra el esquema oficial `2025-12-11` (`jsonschema`, Draft-07).
- `repository.id` ahora es el real: **`1438391702`** (antes había un relleno `1230000000` — error mío,
  corregido).
- **No declara paquete PyPI** porque `labandita-registro` **no existe en PyPI** (comprobado: HTTP 404).
  Declararlo habría sido una promesa falsa y el registro la rechaza. La instalación honesta hoy es
  desde el repositorio; el registro admite servidores solo con `repository` (en una muestra de 600
  servidores publicados, 17 no tienen ni paquete ni remoto).
- `probar.py` → **PRUEBA MCP: OK** con las seis herramientas: `buscar_recurso`, `ficha_recurso`,
  `censo_familia`, `estado_frescura`, `verificar_licencia`, `atestacion_lote`.

Publicar es un comando y una verificación de espacio de nombres por GitHub:
`mcp-publisher login github` → `mcp-publisher publish mcp-labandita-registro/server.json`.
No lo disparo yo: el espacio de nombres es tuyo.

## 4 · Lo único que queda en tus manos

| # | Qué | Cuándo |
|---|---|---|
| 1 | **NLnet**: repasar `docs/NLNET-BORRADOR.md`, rellenar los marcadores `[[…]]` y enviar | **antes del 3-nov-2026, 12:00 CET** |
| 2 | **Registro MCP**: `mcp-publisher login github` + `publish` | cuando quieras, sin fecha |
| 3 | Corregir el titular de la licencia si «Alexis (La Bandita)» no es como quieres firmar | una línea, cuando digas |

## 5 · Correcciones de hoy que valen más que las cifras

1. **Licencia leída mal.** El heurístico anterior marcaba «MIT» a `best_shizuku_apps` porque el README
   tenía un «MIT» dentro de una tabla. Su sección `License` dice **CC BY-SA 3.0**. Ahora se lee primero
   la sección de licencia y, si hay varias candidatas, se declara la ambigüedad (`licencia.nota`).
2. **README perdido.** `GET /readme` sin `Accept: application/vnd.github.raw` devuelve JSON: el texto
   de licencia se perdía y se firmaba una ausencia falsa.
3. **Muertos invisibles.** Los 404 del barrido se descartaban; ahora se registran como `muerto`. Los
   403/429 nunca se convierten en muerte.
4. **Firma obsoleta.** Un sello firmado deja de valer en cuanto se re-sella. Tras cada cambio hay que
   relanzar CI; el bundle anterior (`ddab3526…`, luego `0e09d098…`) no se reutiliza.

## 6 · Pieza 109

`109-La-utilidad-que-habla-con-Shizuku-OmniShizuku-y-el-taller-sin-root-…-2026-10-31-dominicano-ES.md`
(2.454 palabras): semilla, mapa de la familia, ficha medida de OmniShizuku (★10, Apache-2.0, push de
hoy, release del 25-oct, móvil + Android TV + Wear OS), tutorial de 8 pasos, análisis de la lista del
vecino, meme, Q&A con quiz verificado descifrándolo, lectura por edad, consejos por perfil, vara,
glosario, enlaces y firma 💓.

## 7 · El envío de la pieza 01, y el agujero que destapó

Antes de mandar la 01 por WhatsApp se midió todo lo que afirma, otra vez, hoy:

- **15 repositorios: 14 vivos, 1 muerto** (`droidify/client`, 404 también hoy).
- **18 enlaces: los 18 responden 200.**
- **Ninguna licencia cambió, ningún proyecto se archivó.**
- Cinco se movieron en dos días: Shizuku +157★, komi +82★, Obtainium +67★, ShizuStore +23★,
  Omnify +3★.

La pieza tiene 65.157 caracteres: 16 veces el tope de 4.000 del canal. Partida en **20 mensajes**
(ninguno pasa de 3.983), más la portada. El cuerpo va **intacto**; lo que se rehízo es el cierre, que
era del 29 de octubre y decía «hoy es 29». Material completo en
`docs/envios/01-2026-10-31/` dentro del repositorio, para que se pueda copiar desde el teléfono.

**El agujero (errata E-08):** al montar el envío se descubrió que el sello **no veía los archivos
nuevos**. `atestar.py` sellaba lo que existía y `vara.py` comprobaba solo lo que estaba en el
manifiesto: un archivo colado después de firmar entraba sin sello y las dos herramientas decían «todo
bien». Había **30 archivos publicados que nunca estuvieron firmados**, entre ellos todos los `.txt` de
envío. Corregido con reglas únicas (`tools/sello_reglas.py`), altas y bajas cantadas, y un caso nuevo
en la autoprueba: **9 de 9**.

Sello final: **9.776 archivos · huella `ec154f73cca6f329…`**, y `cosign verify-blob` → **`Verified
OK`** contra la corrida 41264522239 de `ffc1c31`.

## 8 · Los 259 envíos, hechas todas las piezas

Después de la 01 se hizo lo mismo con **todas**: 112 envíos de WhatsApp y 147 de Facebook, uno por
pieza. No se escribió ninguno a mano: se escribió la herramienta (`tools/envio.py`) y ella parte,
mide y comprueba; el archivo original queda intacto y su sha256 va en cada envío.

| | WhatsApp | Facebook |
|---|---|---|
| Piezas | 113 | 147 |
| Envíos | **112** (la 01 tiene su paquete propio) | **147** |
| Mensajes listos para pegar | **1.056** | **647** |
| Repos medidos hoy | 255 · **253 vivos, 2 muertos** | 663 · **650 vivos, 9 muertos** |
| Enlaces revisados | 456 · **445 responden** | 1.046 · **1.002 responden** |
| Mensaje más largo | 3.835 caracteres | 3.922 caracteres |

**Lo que se arregló por el camino, y se dice:**

- El texto de las piezas viejas dice «hoy» y está fechado el 29-oct o antes. Cada envío lo avisa en la
  portada y en el primer mensaje: *«Texto del 29-oct-2026: cuando dice «hoy», es ese día»*. El cierre
  medido hoy va al final, aparte y firmado.
- **Nueve piezas** (12 a 20 de WhatsApp) dejan un bloque de código sin cerrar. El envío lo cierra para
  que se lea y lo avisa en la cabecera; **la pieza original no se toca**. Corregirlas es una decisión
  del dueño.
- Los enlaces que no dan 200 se cuentan con su código: un `403` **no** es un enlace muerto (es un
  servidor que no deja entrar a un robot) y un `000` no es un sitio caído (es uno que no contestó).

**Compuerta nueva, G9.** `tools/vara.py` revisa ahora los 259 envíos en cada push: que ninguno pase de
4.000 caracteres, que **toda línea del cuerpo** haya llegado, que el último mensaje lleve firma y que
el archivo sea exactamente lo que el programa genera (si alguien edita uno a mano, canta). La
autoprueba tiene su caso: **10 de 10**.

Sello: **10.042 archivos · `892ff9d5cdf1769f…`** · CI 41266360378 en verde (17 pasos) ·
`cosign verify-blob` → **`Verified OK`**.

## 9 · La 01 reescrita, en los dos canales

Las dos piezas 01 se reescribieron enteras el 31 de octubre, no se retocaron. Motivo: cerraban con un
pulso del 29 que decía «hoy», citaban repos sin volver a medir y la de Facebook era una versión
reducida de la de WhatsApp.

| | WhatsApp 01 | Facebook 01 |
|---|---|---|
| Caracteres | **63.075** (banda pedida: 63.000) | **42.383** (banda: 40.000–45.000) |
| Repos medidos hoy | **30** · 29 vivos, 1 muerto | **33** · 33 vivos |
| Enlaces | **36** · los 36 responden | **39** · los 39 responden |
| Párrafos compartidos con la otra | **0** | **0** |

Material nuevo medido para estas dos piezas: **Orion Store** (★3.883, su web va un mes por detrás de su
repo), **GrapheneOS Apps**, **Appteka** (334.000 apps declaradas, mercado abierto), **AAA**,
**awesome-fdroid**, **awesome-shizuku**, los tres repositorios de **krishna3163** —incluido
`best-root-apps-for-android`, ★50, MIT, release de hoy—, **AntiSplit-M**, **InstallerX-Revived**,
**InstallWithOptions**, **APKeep**, y el paquete **Fossify** con el caso de las fechas que engañan
(Lawnchair con ★13.832 y una «última release» de 2018 sin estar muerto).

**Compuertas nuevas que salieron de esta reescritura:**

- **G10 · bandas.** `docs/bandas.json` declara mínimo y máximo de cada pieza reescrita; la vara no deja
  pasar una pieza fuera de banda ni un registro que maquille la cifra. Autoprueba **11/11**.
- **Guarda de huecos en `tools/envio.py`.** Si una pieza cita repositorios que no se midieron hoy,
  `--generar` falla y lo dice, en vez de escribir un cierre que afirme «medí N» con la mitad sin dato.
  Saltó con esta reescritura y evitó publicar un cierre falso.

Sello: **10.015 archivos · `ea4e9d639d39fc4c…`** · CI 41269140132 en verde ·
`cosign verify-blob` → **`Verified OK`** · `main` en **`eb5c63d`**.

## 10 · La pieza 02 de WhatsApp, cerrada y sellada

**63.081 caracteres** (banda 63.000–63.099), **40 repositorios medidos hoy**, **29 enlaces y los 29
responden 200**. Tema propio: *el mueble de los tres cajones* — motor, catálogo de extensiones y
archivo del usuario — sobre la familia Tachiyomi/Mihon y sus forks.

- **Tres muertos con su 404 a la vista:** `tachiyomiorg/tachiyomi`, `Mangayomi-app/Mangayomi` y
  `Paperback-Community/Paperback`. Se nombran para que nadie copie un enlace de tutorial viejo.
- **Tres archivados marcados como archivados**, no como muertos: Kotatsu (★8.943, último empuje
  4-nov-2025), OpenManga, `aniyomi-extensions`, `timschneeb/tachiyomi-extensions-archive` y
  `kotatsu-parsers`.
- **Los dos casos que enseñan a mirar dos veces:** Suwayomi-JUI con release de marzo de 2024 y código
  empujado hace 16 días; Komikku con release de julio y empuje de octubre.
- **Cero párrafos compartidos** con la 01 de WhatsApp, la 01 de Facebook y la 02 anterior (comprobado
  por script, no a ojo).
- El mini-quiz lleva sus cinco respuestas invertidas y **descifradas por código** para comprobar que se
  leen bien de atrás para adelante.

Sello: **10.017 archivos · `e2a4f87ba4ff7c24…`** · CI **41270520239** en verde ·
`cosign verify-blob` → **`Verified OK`** · `main` en **`0f827a7`**. Envíos regenerados con la medición
de hoy: **114 de WhatsApp y 147 de Facebook, 0 fallos** en `--verificar`; la vara pasa entera, con
**G10 en 3 piezas dentro de banda**.

## 11 · Las cuatro primeras, rehechas con lo que nació este año

La orden fue clara: la lista de hace cuatro meses estaba llena de cadáveres porque se quedó con los
recursos viejos. Se empieza otra vez desde la 01, con descubrimiento propio y medición del día, y no se
entrega nada que no sea el archivo entero.

**Lo que se buscó, y cómo.** Cuatro barridos de la API de GitHub con filtro de empuje posterior al 1 de
agosto de 2026 —tiendas y clientes de APK, instaladores, gestores de paquetes, lectores de cómics,
servidores, descargadores— más `fmhy.net`, `appteka.store` y los repositorios de los mismos autores.
De ahí salieron **32 proyectos que no están en ninguna lista de hace cuatro meses** y **cuatro cebos**
que sí están en los primeros resultados de las búsquedas.

**Los cebos, medidos como lo que son:** `sri-sivaram/Neko-Manga-Pearl` ★116, `ubedshah/manga-vault-nexus`
★115, `meyamane37923-hash/komikku-scans` ★114 y `khaledmahmud5286-cmd/manga-zen-reader` ★113. Los cuatro
creados el **28 de junio de 2026**, los cuatro en HTML, los cuatro **sin licencia**, los cuatro empujando
en las últimas 48 horas y los cuatro anunciándose como «la mejor alternativa 2026» de una app real.

**Las cuatro piezas, medidas y en banda:**

| Pieza | Caracteres | Repos medidos | Lo nuevo |
|---|---|---|---|
| 01 WhatsApp | 63.093 | 31 | RepoStore (release del mismo día), ShizuStore (creada el 17-sep-2026), AppManagerNG, termux-app-store, universal-installer, InstallerX-Revived, Universal-Patch-Manager, Ackpine, WebViewUpgrade, developer-verifier-placeholder, AAAD, AppManager, APK-Installer; cementerio de cebos y «cómo se lee una lista vieja» |
| 01 Facebook | 42.740 | 22 | Escena del que copió una lista de hace cuatro meses; doce casas, seis nacidas este año; dieciséis apps donde la fecha de la release no es la del proyecto |
| 02 WhatsApp | 63.094 | 56 | Yokai ★1.914, OtakuWorld ★637, Usagi ★288, Chimahon ★239, Ciallo ★261, Yomihon ★142, kmreader, manga-tui (release de hoy), manga-downloader, comic-looms, KamiYomu, BookHeaven, liseur, LocalViewer, kotlin-toolkit, koodo-reader ★28.679, Suwayomi-VUI |
| 02 Facebook | 42.249 | 56 | Pieza nueva entera: seis escenas de mudanza, seis casas nuevas, cuatro servidores que no son Suwayomi, el archivo, tutorial de doce pasos, ocho errores, cementerio de cebos, ley, sincronización y ficha de 49 repos con fecha de nacimiento |

**Verificado, no declarado:** 114 envíos de WhatsApp y 148 de Facebook con **0 fallos**; `vara.py` →
**fallos: NINGUNO** con **G10 en 4 piezas dentro de banda**; sello de **10.020 archivos ·
`601f0c9c780b6597…`**; CI en verde y `cosign verify-blob` → **Verified OK**; `main` en **`c1f4962`**.

## 12 · El archivo entero en un solo HTML

`ENTREGA-2026-10-31/LAS-262-PUBLICACIONES-2026-11-01.html` — **3.164.132 caracteres**, **262
publicaciones** (114 de WhatsApp y 148 de Facebook), todas íntegras y sin un solo recurso externo: se abre
sin red y sin depender de ninguna hoja de estilo ajena. Trae buscador por número y título, filtro por
canal, filtro «reescritas hoy» y un panel de lectura que muestra cada pieza tal como se escribió.

Las 258 piezas que no se han reescrito van **tal cual, con su fecha interna a la vista**: no se retocan
para que parezcan frescas. Mezclar datos de días anteriores con los de hoy sería exactamente el problema
que este archivo denuncia. El generador queda en `tools/html_archivo.py`, así que el HTML se puede
reconstruir con un comando desde las piezas y no es un archivo huérfano.

**Lo que falta y cómo sigue:** 112 piezas de WhatsApp (03-112) y 118 de Facebook (03-120), de dos en
dos por número, cada una con su medición y su banda. La cuenta completa está en
`PIEZAS-2026-10-31/PLAN-120.md`.

---

**Lo que no prometo:** que esto esté «terminado» para siempre. Prometo que cada número de este informe
salió de una corrida ejecutada hoy, y que lo que no medí está dicho como no medido.

---

## 13 · Revisión profunda del 1 de noviembre (antes de avanzar)

Se revisaron las cuatro piezas terminadas, una por una, y se encontraron **cinco fallos** que ninguna
compuerta automática veía:

1. **37 estrellas desfasadas** entre la medición de la mañana y la del cierre (Shizuku 32.552→32.554,
   Obtainium →21.097, InstallerX →7.258, Dhizuku →4.069, Mihon →24.916, aniyomi →7.865, Kototoro →657,
   mangayomi →4.286, LocalViewer →198).
2. **13 fechas relativas falsas** al cambiar el día: «empujó hoy» por empujes del 31 de octubre y
   «empujó ayer» por empujes del 1 de noviembre; y tres releases que decían «de hoy» siendo del 25 y 27
   de octubre.
3. **Una afirmación propia falsa**: RepoStore «publicó una versión el mismo día en que la medí». Su
   v1.0.22 es del 29 de octubre. Corregida en cuerpo, tabla, pregunta y respuesta del quiz.
4. **Tres párrafos compartidos** entre piezas (la lista de los cuatro cebos y dos frases de cierre).
   `G6` mide repetición *dentro* de una pieza, no *entre* piezas: se detectó con un script aparte y se
   reescribieron. Ahora: 0 en las diez parejas posibles.
5. **Enlaces en 429** de Facebook, que no son muertos: se quedan declarados como «no deja entrar a un
   robot» y conviene re-medir antes de mandarlos.

Acta completa, con la matriz de comprobaciones y los comandos para desmentirla:
`REVISION-2026-11-01/REVISION-PROFUNDA-2026-11-01.md`.

**Quinta entrega:** el post de comunidad del «mama hueso», **4.135 caracteres**, con su banda exacta en
`docs/bandas.json` y fuera del circuito de envíos a propósito. Nombra las ocho páginas de mods, parches y
ROMs **sin enlazarlas** —la regla de la casa que ya estaba escrita en la 01— y enlaza solo las cuatro
fuentes que respondieron 200 hoy: `fmhy.net`, `virgil.samidy.com`, `komistore.app` y `appteka.store`.

Sello: **10.022 archivos · `856247d8afe9e993…`** · CI **41274763425** en verde · `cosign verify-blob` →
**`Verified OK`** · `main` en **`b89ffa3`**.
