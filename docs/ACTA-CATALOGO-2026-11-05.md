# Acta · el catálogo por recurso (5-nov-2026, 11:30–11:55 UTC)

**Qué se crea.** `catalogo/`, con una ficha por recurso en lugar de una lista. **279 fichas medidas** en
**9 racimos**, de las cuales **23 ya tienen guía escrita a mano** —el racimo completo de Shizuku y sus
herederos— y 256 están medidas esperando su guía.

**Decisión del dueño.** Las dos opciones a la vez: (1) todo dentro de `la-bandita-archivo`, sin crear
cientos de repositorios, para que el catálogo se clone una vez y se valide con un linter; (2) empezar por
los dos racimos pedidos: el banco de prueba de Shizuku y los recursos de las piezas 12–20.

**Máquina nueva, en `tools/`.** `catalogo_medir.py` (mide y guarda evidencia con fecha), `catalogo_ficha.py`
(escribe fichas y índice, preservando la guía escrita entre marcadores), `catalogo_sync.py` (compara con
GitHub, escribe `SINCRONIA.json` y `CREDITOS.md`, y con `--actualizar` refresca medición y fichas sin tocar
las guías) y `catalogo_lint.py` (12 comprobaciones, código de salida 1 si falla).

**Racimos.** `shizuku-y-herederos` (23) · `reemplazo-del-stack` (52) · `audio` (52) · `clientes-de-musica`
(37) · `descargas` (31) · `torrentes` (3) · `teclados-y-dictado` (34) · `radio-y-directo` (32) ·
`tiendas-de-extensiones` (25) · `teclados-con-ia` (11).

**Hallazgos del racimo de Shizuku.** (1) **Shizuku**, el original, tiene ★32.840 pero su último empujón
es del 18-jun-2025 y su última entrega v13.6.0 del 25-may-2025: el catálogo lo marca «lento», no «vivo».
(2) Tres herederos publican más recientemente: **Stellar** (v1.1, ago-2026), **ShizukuPlus**
(v13.6.0.r2551, sep-2026) y **Shizuku-Next** (v14.0.33-next, **hoy mismo**). (3) **Riru** está archivado
desde 2022 y **InstallerX** desde 2023, y los dos tienen heredero vivo: Zygisk y `InstallerX-Revived`
(★7.327, más estrellas que el padre). (4) **UAD** (★20.338) lleva parado desde ago-2024 sin estar
archivado —el peor estado posible— y su heredero `universal-android-debloater-next-generation` (★9.751)
entregó el 2-nov-2026. (5) `timschneeb/awesome-shizuku` (★10.708) es la lista de referencia del tema: se
le reconoce el trabajo y se le señala lo único que no hace, que es fechar cada entrada.

**Lo que el linter encontró en mi propio trabajo.** 54 fallos en la primera pasada: **49 por una frase
plantilla repetida** en las fichas sin guía, 3 por fichas de repositorios que no existen —tres nombres que
yo había supuesto y que no están en GitHub: se borraron en vez de disimularlos— y 2 por superlativos que
venían de citas del autor, no de mi prosa (se eximen las citas). Segunda pasada: **0 fallos**.

**Compuertas.** `catalogo_lint` 0 fallos · `manual_gate` y `novedad_gate` sin cambios en las piezas ·
`make ritual` sella los ficheros nuevos · `make compuertas` y `autoprueba` antes del push.

**Registros.** **E46** → **H27** («un catálogo se mide por recurso, no se copia por lista»).

## Segunda tanda · racimo 12 completo (12:05–12:40 UTC)

**52 guías más escritas a mano**, todas las del racimo `reemplazo-del-stack` (los recursos de la pieza 12):
lectores y gestores de libros (KOReader, Calibre, Koodo, Readest, Foliate, Thorium, Booklore, Grimmory),
tiendas y actualizadores (Obtainium, F-Droid, Accrescent, RepoStore), reproductores y clientes de vídeo
(Iptvnator, OwnTV, Nuvio en sus cuatro variantes, Cove, Opal), agregadores y complementos (AIOStreams,
easy-aiostreams, AniSync, StreamGram, M3U Mux, MegaNexus, SkipDB), herramientas de escritorio (Sioyek,
Castor, MediaLyze, CrossWatch, Pictorium) y lectores/fuentes de manga y novela de la cola del racimo.

**Total del catálogo:** **75 fichas con guía escrita** de 278 medidas · **203 esperando guía** ·
`catalogo_lint` **0 fallos**.

**Reglas que se aplicaron en este racimo.** (1) Los recursos que dependen de listas de canales o de
fuentes de contenido se describen **sin enlazar ninguna lista** y se dice por qué (`iptv-org`, `OwnTV`,
`Iptvnator`, `stremhu-source`). (2) Ningún recurso se recomienda por estrellas: se dan con la fecha al
lado, y cuando un proyecto está parado o en `alpha` se escribe en la guía, no en una nota al pie.
(3) Los que no declaran licencia (`lipex-reader`, `pulsar-trmangahub`) se señalan como lo que son.

**Lo que no se ha hecho y no se va a fingir.** No se ha instalado ninguna de las 75. La guía dice cómo se
usa según el propio proyecto, no según una prueba propia; el apartado «Qué no está verificado» de cada
ficha lo repite en cada una.

## Tercera tanda · racimo `descargas` completo (30 recursos)

Las **30 guías** del racimo `descargas`, escritas a mano una por una: motores de terminal (`aria2`, `axel`,
`wget2`, `lux`, `you-get`, `gallery-dl`, `N_m3u8DL-RE`, `curl-impersonate`, `youtubedl-android`), ventanas
para el motor (`AriaNg`, `AriaNg-Native`, `yaaw`, `aria-ng-gui`, `aria-ng-gui-android`), gestores de
escritorio (`Motrix`, `rayburst`, `gopeed`, `prism-download-manager`, `persepolis`, `xdm`, `uget`), los de
vídeo por web (`yt-dlp` como dependencia de casi todos, `Seal`, `YTDLnis`, `YoutubeDownloader`, `Downvid`,
`MovieBox-Tui`, `media-downloader`, `xiadown`), y los dos que entran por la puerta de al lado
(`bare-browser`, el navegador que descarga, y `Stash`, la biblioteca musical que se trae las listas).

**Total del catálogo:** **105 fichas con guía escrita** de 278 medidas · **173 esperando guía** ·
`catalogo_lint` **0 fallos**.

**Lo que este racimo obligó a decir en voz alta.** Tres recursos de esta lista están **parados** y así están
escritos: `aria-ng-gui` desde 2020, `aria-ng-gui-android` desde 2023, `uget` desde 2019. Dos **no declaran
licencia** (`yaaw`, `media-downloader`). Dos tienen la **entrega muy por detrás del código** (`Seal`, entrega
de octubre de 2024 y cambios en 2026; `persepolis`, un año parado) y eso se explica en la guía, no en una
nota al pie. Y cinco son **de 2026**, con meses de vida: `rayburst`, `prism-download-manager`, `bare-browser`,
`downvid`, `xiadown`; en sus guías se dice la fecha de creación al lado de las estrellas, porque un número de
estrellas sin fecha es una cifra disfrazada.

**Vetos respetados.** Se nombran enlaces de una sola vía y no se enlaza ningún cliente de torrentes, ni
ningún índice, ni ninguna lista de fragmentos o de canales. Comprobado con `grep` sobre las 30 fichas: cero
coincidencias.

**Lo que no está verificado.** Ninguno de los 30 se ha instalado. La ficha lo repite, y la guía distingue
siempre entre lo que hace el programa según quien lo hace y lo que se ha comprobado aquí, que es su estado
en GitHub.
