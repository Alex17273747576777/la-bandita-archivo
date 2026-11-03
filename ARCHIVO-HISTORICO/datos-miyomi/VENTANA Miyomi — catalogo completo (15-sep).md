# VENTANA Miyomi — catálogo completo (15-sep-2026)

## Método

La ventana (la web JS que falló dos veces) se cerró por la puerta que el propio proyecto deja abierta: su API pública de Supabase — URL base y anon key **publicadas en el repositorio oficial de Miyomi** (el front las usa en cada visita; acceso público de lectura, nada forzado). Por regla de la casa (13-sep): **la anon key no se pega** en publicaciones ni documentos — se cita el método, no la clave. Los JSON crudos viven en esta carpeta: `apps.json` (133) y `extensions.json` (45).

- Consulta: `GET /rest/v1/apps?select=*&limit=1000` (y `extensions`), con cabeceras apikey/Authorization.
- Resultado: **133 apps · 45 extensiones** · 0 duplicados por `repo_url`.
- Coincide con lo que el dueño traía como estimación (~132/~44) — hoy el catálogo tiene uno más de cada.

## Campos que el scrape de la web no daba

`fork_of` (genealogía declarada) · `upstream_url` · `version` · `last_release_date` · `download_count` · `compatible_with` (fuentes de extensiones por app) · `content_types` · `status` (approved) · `platforms` · `tags`.

## Cruce con el corpus (piezas 00–36)

- **27/133 apps ya fichadas** por la casa (Mihon, Aniyomi, Kotatsu, Kototoro, AniZen, N-Zik de catálogo Multi, etc.).
- **106 apps nuevas** = la cola de candidatas de las puertas **Anime/vídeo** (la mayor), **Lectura III (libros/escritorio)** y **Sótano** (Suwayomi v2.1.1867, stump).
- Las 45 extensiones (40 repos fuente): la geografía de los catálogos de extensiones — para la pieza de extensiones de la puerta Anime.

## Genealogías que el catálogo declara (fork_of)

- Estirpe Mihon: TachiyomiAZ · TachiyomiAT · Taison · tsundoku · taihon · tankobon
- Estirpe Kotatsu: DropSauce · MIYO · Kotatsu-Next · Kaisoku · Nyora · Kototoro (skepsun/Kototoro — cotejar con Kototoro-app/Kototoro del corpus: posible mudanza de organización u homónimos)
- Estirpe Aniyomi: Nekoyomi · Tadami (andreykolesnikov/Tadami-Aniyomi-fork — homónimo del Tadami de libros de la pieza 36, que era tadamiorg/tadami)
- Estirpe Dantotsu: Dartotsu · (ReDantotsu se declara remake sin campo) · la ficha Dantotsu apunta al updater (itsmechinmoy/dantotsu-updater) — la app vive por su updater
- Otras: Shiru←Miru · chimahon←Komikku · NeoQN←QuickNovel

## Joyas nuevas por descargas (top del gap)

Cloudstream 6.58M (¡pero pieza 26 la citaba!) · Seanime 5.82M · Shiru 2.67M · YACReader 1.73M · **Readest 1.73M (libros — estaba en el inventario)** · JHenTai 1.5M · Thorium Reader 1.03M · LNReader 930k · Nuvio 913k · Suwayomi 602k · Github Store 698k (¡un cliente de tiendas — para el Tronco!) · koharu 348k · AnymeX 338k · Mangayomi 391k.

## Huecos y honestidad del catálogo

- Entradas sin repo ni release (Stremio, Panels, Perfect Viewer, CDisplayEx, MangaPin, Suwatte con repo incompleto): el catálogo también tiene sus huecos — no se ficha sin casa.
- Tachiyomi consta en el catálogo (10M descargas, última release 2024-01-13 — la víspera de la DMCA): el catálogo la conserva como historia, igual que la pieza 35.

## Uso previsto

1. **Puerta Anime/vídeo:** lote principal con las ~50 primeras por descargas + genealogías fork_of.
2. **Lectura III:** libros de escritorio (Readest, YACReader, Thorium, koharu, Yomikiru, anx-reader, Openlib…).
3. **Sótano:** Suwayomi, stump.
4. **Tronco (aporte):** Github Store.
5. Extensiones: pieza de la geografía de fuentes (Keiyoushi, yuzono, Aidoku sources, lnreader-plugins, FelipeGFA/extensoes…).

*Ventana cerrada a las 2026-09-15 (UTC del catálogo: entradas con updated_at del día).*
