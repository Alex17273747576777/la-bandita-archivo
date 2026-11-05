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

## Cuarta tanda · racimo `audio` completo (52 recursos)

Las **52 guías** del racimo `audio`, escritas a mano una por una. Es el racimo más mezclado del catálogo y
se ordenó por lo que el recurso hace, no por su fama:

- **Pódcast** (5): `AntennaPod`, `gpodder`, `Podcini`, `escapepod`, más el servidor `audiobookshelf`.
- **Audiolibros** (4): `Voice`, `BookPlayer`, `Libation`, `audiobookshelf`.
- **Servidores autoalojados** (11): `Navidrome`, `Jellyfin`, `Koel`, `Ampache`, `BlackCandy`,
  `airsonic-advanced`, `Mopidy`, `slimserver`, `MPD`, `owntone`, `snapcast`, más `Icecast` para emitir.
- **Clientes de esos servidores** (4): `feishin`, `supersonic`, `sonixd`, `cider`-familia vía `spotifyd` y
  `librespot` como piezas de protocolo.
- **Reproductores de Android** (10): `Auxio`, `RetroMusicPlayer`, `namida`, `Metrolist`, `OuterTune`,
  `InnerTune`, `ViMusic`, `SimpMusic`, `namida`, `Harmony-Music`.
- **Reproductores de escritorio** (5): `Elisa`, `Tauon`, `Strawberry`, `quodlibet`, `harmonoid`.
- **Etiquetado y datos** (7): `beets`, `Picard`, `easytag`, `taglib`, `chromaprint`, `musicbrainz-server`,
  `listenbrainz-server`, más `pano-scrobbler` para las estadísticas.
- **Herramientas** (3): `FFmpeg`, `yt-dlp`, `cobalt`.

**Total del catálogo:** **157 fichas con guía escrita** de 278 medidas · **121 esperando guía** ·
`catalogo_lint` **0 fallos**.

**Lo que este racimo obligó a decir sin adornos.** Siete recursos llevan guía que **empieza avisando de que
están parados o archivados**: `airsonic-advanced` (entrega de 2020, cambios de 2024), `sonixd` (archivado, y
su sucesor está en el mismo racimo), `ViMusic` (archivado en 2024), `escapepod` (archivado en 2022),
`Podcini` (sin cambios desde enero de 2025), `OuterTune` (su propio texto dice que no está en desarrollo
activo) y `InnerTune` (entrega de septiembre de 2024). Cuatro tienen la **entrega por detrás del código** y
se explica: `gpodder`, `quodlibet`, `librespot`, `spotifyd`. Tres **no declaran licencia reconocible**:
`FFmpeg`, `chromaprint`, `harmonoid`, `namida`, `musicbrainz-server`. Dos son **beta o por debajo de la 1.0**
pese a su fama: `spotube` (`6.0.0-beta.0`) y `harmonoid` (`0.3.37`).

**Frontera que se respetó en todo el racimo.** Los recursos que dependen de servicios ajenos —`Metrolist`,
`SimpMusic`, `InnerTune`, `OuterTune`, `ViMusic`, `Harmony-Music`, `nuclear`, `spotube`, `cobalt`— llevan
escrito en su guía que **no tienen catálogo propio** y que su continuidad no la deciden sus autores. No se
enlaza ninguna fuente de contenido, ni ningún servicio de música, ni ninguna lista. `grep` sobre las 52
fichas: cero coincidencias con los vetos.

**Lo que no está verificado.** Ninguno de los 52 se ha instalado. Cada guía separa lo que el programa hace
según su propio proyecto de lo que se ha medido aquí, que es su estado en GitHub el 5 de noviembre de 2026.

## Quinta tanda · racimo `teclados-y-dictado` completo (34 recursos)

Las **34 guías** del racimo, escritas a mano una por una. El racimo se ordenó por lo que el recurso es, porque
bajo un mismo título conviven cosas muy distintas:

- **Teclados de Android, con código propio** (8): `HeliBoard`, `AnySoftKeyboard`, `florisboard`,
  `Unexpected-Keyboard`, `simple-keyboard`, `LeanType`, `wmkeyboard`, `trime`.
- **Teclados con dictado** (5): `DictateKeyboard`, `BiBi-Keyboard`, `Sayboard`, `Transcribro`, `CyIME`.
- **Dictado que no cambia tu teclado** (2): `futo-org/voice-input`, `android_transcribe_app`.
- **Dictado de escritorio** (8): `Handy`, `hex`, `openless`, `betterwispr`, `speaktype`, `FluidVoice`,
  `amical`, `vocalinux`, `voxtype`.
- **Motores y modelos** (4): `whisper.cpp`, `openai/whisper`, `faster-whisper`, `whisper` como familia.
- **Corrección y expansión de texto** (3): `harper`, `languagetool`, `espanso`.
- **Entradas chinas sobre Rime** (3): `CyIME`, `trime`, `xsime`, `aime`.
- **Dos que no son lo que parecen** (2): `PixelBoard` y `Batmancpu/Dictator-`.

**Total del catálogo:** **191 fichas con guía escrita** de 278 medidas · **87 esperando guía** ·
`catalogo_lint` **0 fallos**.

**Lo que este racimo obligó a decir en voz alta.**

- `Akshayykadam/PixelBoard` **no es software libre**: es el teclado de Google reempaquetado por un tercero. Su
  guía lo dice en la primera línea útil, porque un teclado ve todo lo que escribes y aquí lo que se instala es
  una compilación ajena.
- `Batmancpu/Dictator-` **es una copia recompilada** de `DevEmperor/DictateKeyboard`, hecha por alguien que
  declara no ser programador. Tiene 3 estrellas. Las dos fichas se escribieron para que no se confundan.
- `LeanType` arrastra la corrección de **E45**: no tiene «75 teclas de IA», tiene **diez** huecos
  `CUSTOM_AI_1`…`CUSTOM_AI_10`. La guía lo corrige con el dato, no con una negación.
- `FluidVoice` **anuncia cuatro plataformas y entrega dos**: medido hoy sólo hay macOS y una prueba de iOS.
- `betterwispr` se creó el **7 de octubre de 2026**: un mes de vida, y la guía lo pone delante de las estrellas.
- `speaktype` dice «cualquier sistema» y está escrito en **Swift**: el alcance real es el de Apple.
- Cuatro tienen **entrega por detrás del código** y se explica: `florisboard` (nov-2025), `Sayboard`
  (ago-2024), `Transcribro` (ago-2025), `faster-whisper` (oct-2025).

**Números del autor que no se repiten como propios.** `wmkeyboard` dice «seiscientos idiomas» y «89
herramientas»; `BiBi-Keyboard`, «18 motores»; `voxtype`, velocidad en tiempo real. En las cuatro guías la cifra
aparece atribuida a quien la publica, con la frase que lo dice, y no como medición de este catálogo.

**Lo que no está verificado.** Ninguno de los 34 se ha instalado. Y hay un motivo de peso en este racimo: un
teclado o un dictado recibe **todo lo que escribes o dices**. Por eso cada guía separa lo que el programa hace
según su proyecto, lo que se midió en GitHub el 5 de noviembre de 2026, y lo que el usuario debe decidir por su
cuenta —motor en la nube o en el aparato, código propio o paquete ajeno—.

## Sexta tanda · racimos `clientes-de-musica` (27) y `radio-y-directo` (29)

Las **56 guías** que faltaban de los dos racimos que comparten suelo: el de los clientes de música y el de la
radio y la televisión por internet. Se escribieron en la misma sesión porque comparten piezas —los catálogos de
donde salen las listas, los motores de reproducción, los servicios ajenos— y arrastran el mismo criterio.

**Total del catálogo:** **247 fichas con guía escrita** de 278 medidas · **31 esperando guía** ·
`catalogo_lint` **0 fallos**.

**`clientes-de-musica` (27).** Aquí conviven tres familias que no se parecen: los **clientes de servicios
ajenos** (`LastWave-Native`, `Echo-Music`, `BitChord`, `YumaPlayer`, `Square`, `Leap`, `myspoti`, `MeloX`,
`kumone`, `riff`, `sonora`, `Leviathan`… en sus nombres reales), los **clientes de terminal** (`spotify-tui`,
`spotify-player`, `ncspot`, `lazyspotify`), y las **bibliotecas** de las que todo eso vive (`ytmusicapi`,
`spotipy`, `NewPipeExtractor`). Y en medio, las piezas de infraestructura: `go-librespot` y el demonio clásico
para hacer de altavoz en la red.

Lo que se dijo sin adornos: **`spotify-tui` lleva parado desde abril de 2024**, `psst` declara en su propio
texto que le faltan funciones y estabilidad, `MeloX-Android` pide estrellas para publicar sus versiones de
escritorio, y `myspoti` se presenta como la forma de saltarse los anuncios de una cuenta gratuita — lo que va
contra las condiciones del servicio, y así está escrito. Tres no declaran licencia reconocible y varias están
por debajo de la versión 1.

**`radio-y-directo` (29).** Dos mitades muy distintas: **radio** (`InternetRadio`, `deutsia-radio`, `aerial`,
`receiver`, `omnibeat`, `freqcast`, `tune-roam`, `AetherTune`, `Traydio`, `British-Radio-Player`, `RadioDroid`)
y **televisión por internet** (`StreamVault`, `OwnTV`, `Lume`, `clubTivi`, `prysm`, `better-iptv`, `mytv`,
`opentv`, `OKVideoMac`, `webos-iptv-player`, `Extreme-InfiniTV`, `another-iptv-player`, `WoodicIPTV`), más las
**herramientas de mantenimiento** (`epg-tools`, `xmltv-splitter`, `iptv-doctor`) y las **plataformas de
emisión** (`AzuraCast`, `LibreTime`, `Icecast`).

Tres guías **empiezan avisando del estado del proyecto**: `WoodicIPTV` (★5, sin licencia, sin un cambio desde el
día que se publicó), `RadioDroid` (dos años parado) y `tune-roam` (★10, dos semanas de vida). Otras dos tienen
**una sola estrella** y se dice por qué están igualmente en el catálogo: `epg-tools` y `xmltv-splitter` resuelven
un problema concreto —una guía de programación de decenas de megas— que ningún otro recurso del racimo toca.

**Vetos respetados, y esta vez con más motivo.** En este racimo casi todo lo que se describe funciona con listas
de canales, portales o cuentas. En las 29 guías **no se enlaza ninguna lista, ningún portal, ninguna cuenta y
ninguna fuente de contenido**: se describe el reproductor, se dice qué necesita y se deja claro que el catálogo
lo pone quien lo use. `grep` de vetos sobre las 56 fichas: cero coincidencias.

**Lo que no está verificado.** Ninguno de los 56 se ha instalado. En los que dependen de fuentes ajenas —casi
todos los de televisión— eso significa que la guía describe el programa, no el contenido: ni una sola lista se
ha abierto, ni se abrirá.
