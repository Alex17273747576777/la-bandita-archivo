# RFC v2 — Unified Feed Architecture for AniZen & Houri
## MultiFeed Manager, Per-Source Filters & On-Device Segmentation
*extends "RFC: In-App Private Extension Sandbox & Self-Contained Backups" (v1.0, September 2026)*

**Prepared:** October 10, 2026 · verified same day
**Target projects:** [salmanbappi/AniZen](https://github.com/salmanbappi/AniZen) (v0.5.215, 30-sep-2026) · [PineappleTwilight/houri](https://github.com/PineappleTwilight/houri) (v1.23.16, released today)
**Status:** Proposal — Production Candidate, building on RFC v1 §2 (Sandbox Extension Engine) and §3 (Universal Unified Source Manager)

---

## Resumen ejecutivo (ES)

Este documento eleva a nivel de arquitectura dos observaciones enviadas por el dueño de esta
propuesta al equipo de AniZen y Houri tras la reciente implementación del nuevo tipo de Feed:

1. **El MultiFeed actual muestra una sola fuente y no expone filtros.** Al seleccionar una fuente
   concreta dentro del multifeed debería poder alternarse entre *sus* filtros específicos
   («recientes», «actualizados») y los convencionales («nuevas obras», «populares», «en tendencia»).
2. **La petición original era un multifeed de verdad: múltiples feeds.** El feed global por defecto,
   más la capacidad de segmentarlo en categorías — a mano o mediante IA que clasifique
   automáticamente las entradas existentes. Ejemplo real del ecosistema: fuentes de películas y
   fuentes de anime conviven hoy en las mismas apps (Zangetsu, AniDash, Mangayomi); cada feed,
   igual que el global, debería admitir hasta **20 fuentes o extensiones**.

La tesis de esta v2: el Feed no es una pantalla — es un **objeto portátil** de primera clase, que
vive sobre el Universal Source Manager del RFC v1, viaja dentro de los backups autocontenidos
(.anizenbk / .hourbk), y expone los filtros nativos de cada fuente mediante una interfaz normalizada.
La evidencia del ecosistema (§1) muestra que la segmentación por categorías es la regla del mercado;
el feed único global es la excepción.

---

## 1. Context & Motivation — the landscape speaks (verified 2026-10-10)

**The catalog layer already segments; the app layer does not.**

| Evidence | What it shows |
|---|---|
| [Miyomi](https://miyomi.app/software?sort=updated-desc&view=grid) (consulted 10-oct) | Sort-by-updated is dominated by **multi-content apps**: Mangayomi (manga+novel+anime, 6 platforms), Zangetsu ("anime & movie streaming"), AniDash, Foxlations, Kototoro (manga+novel+video, 125.6k) — content types already coexist inside single apps. |
| [EverythingMoe](https://everythingmoe.com/) (consulted 10-oct; updated same day) | The reference index of the culture is organized in **24 category sections** (Anime Streaming 94 sites · Manga Reading 96 · Novel · Drama · Donghua…) — segmentation is how the ecosystem itself thinks. |
| houri v1.23.16 released **today**; 14 releases in 9 days | Shipping cadence supports iterative feed features without long freezes. |
| AniZen v0.5.215 (30-sep) + in-app AI diagnostics (RFC v1 §5) | AniZen already carries the on-device intelligence needed for assisted segmentation. |

**The current gap (owner's field report):** activating the new multiFeed surfaces a single source,
with no source-specific filter toggling (recent / updated) and no conventional filters
(new works / popular / trending) applied to it. And there is no way to keep *several* feeds side by
side — the global feed cannot be forked into categories, manual or AI-assisted.

## 2. Design Goals

1. **Feed as a first-class, portable object** — created, named, edited, backed up, restored.
2. **Respect native source capabilities** — never fake a filter the upstream API lacks; degrade honestly.
3. **Manual first, AI second** — deterministic rules cover 90% of needs; AI is opt-in, on-device, correctable.
4. **Zero telemetry** — classification runs on-device; nothing about a user's taste leaves the phone.
5. **≤20 sources per feed** (as originally requested), any adapter mix (APK manga, APK anime, Kotatsu DEX).
6. **Global feed remains the default** — segmentation adds; it never removes.

## 3. Data Model — the Feed object

```jsonc
// feeds.json — travels inside .anizenbk / .hourbk (RFC v1 §4)
{
  "schema": "feed.v2",
  "feeds": [
    {
      "id": "feed_global",            // reserved, non-deletable
      "name": "Global",
      "sources": [ /* up to 20 */ { "pkg": "eu.kanade.tachiyomi.ext.en.mangadex", "enabled": true } ],
      "mode": "global",               // global | manual | ai
      "rules": [],                    // manual segmentation rules (see §6.1)
      "ai": null,                     // AI segmentation profile (see §6.2)
      "refresh": { "policy": "on_open", "ttl_min": 180 },
      "created": "2026-10-10T16:00:00Z"
    },
    {
      "id": "feed_anime_movies",
      "name": "Anime + Movies",
      "sources": [ { "pkg": "anime.source.a", "enabled": true },
                   { "pkg": "movie.source.b", "enabled": true } ],
      "mode": "manual",
      "rules": [ { "match": "source_in", "sources": ["anime.source.a", "movie.source.b"] } ],
      "refresh": { "policy": "scheduled", "ttl_min": 720 }
    }
  ]
}
```

## 4. Normalized Filter Interface (NFI) — per-source filters, honestly mapped

Each adapter exposes a **FilterProfile**; the MultiFeed UI renders exactly what the selected source
can do, and nothing else.

| Owner-visible filter | Mihon / TachiyomiSY (ParsedHttpSource) | Aniyomi (AnimeHttpSource) | Kotatsu DEX parser | Movie/series sources |
|---|---|---|---|---|
| Recientes / Latest | `fetchLatestUpdates()` | `fetchLatestUpdates()` | `latest` listing | `latest` (if declared) |
| Actualizados | `fetchLatestUpdates` (ordered) | idem + `fetchSeasons` where present | `updated` where present | `updated` (if declared) |
| Nuevas obras | popular ascending by created/popular-set | idem | genre+sort where supported | catalog newest |
| Populares | `fetchPopularManga()` | `fetchPopularAnime()` | `popular` listing | `popular` (if declared) |
| En tendencia | source filter list (trending where native) | idem | trending where native | trending (if declared) |
| Filtros nativos (género, status, año…) | full `getFilterList()` | full `getFilterList()` | parser genres | source-declared facets |

**Fallback rule (no fake filters):** if a source lacks a native endpoint for a requested filter, the
engine (a) hides the chip, or (b) offers *client-side post-filtering* over already-fetched pages,
visibly labeled «filtro local — no nativo de la fuente». Never silent.

## 5. MultiFeed UX Specification

- **Source chips** (one per enabled source of the feed, max 20) + **filter chips row** that
  re-binds to the *selected* source's FilterProfile (§4) — this is the exact gap reported.
- **Feed switcher**: horizontal tabs — Global · user feeds · «+ New feed». Long-press → rename,
  reorder, export single feed.
- **Merge policies** (per feed): `interleave` (round-robin, default), `weighted` (per-source weight),
  `recency` (strict time order across sources). Deduplication by normalized entry key
  (title-cased ASCII-fold + source id) with «show duplicates» toggle.
- **Per-source state inside the feed** (solo mute, weight, filter override) — so «this source, its
  filters» is one tap, not a detour to the Sources screen.

## 6. Segmentation — manual first, AI assisted, always correctable

### 6.1 Manual rules (deterministic, portable, testable)
`source_in` · `content_type` (manga/anime/novel/movie) · `genre/tag in` · `title contains` ·
`status in` · combined with AND/OR. Rules are data (inside `feeds.json`) — no code, no lock-in.

### 6.2 AI-assisted segmentation (opt-in, on-device, correctable)
- **Input:** the existing entries of the Global feed (titles, genres, tags, content type metadata).
- **Engine:** small on-device classifier; AniZen can ship it on its existing AI diagnostics stack
  (RFC v1 §5); Houri ships the lighter tier (rules + heuristics) first.
- **Behavior:** proposes *suggested feeds* (e.g., «Anime», «Movies», «Donghua», «Long-runners»)
  with per-entry confidence; the user accepts, edits, or discards each suggestion. AI never moves
  an entry silently — every assignment is reviewable, reversible, and locally computed.
- **Privacy:** no network calls, no model telemetry, no taste fingerprint leaves the device.
- **Example (owner's case):** movie sources + anime sources linked → AI proposes two feeds; manual
  mode can build the same with one `content_type` rule — both paths land in the same `feeds.json`.

## 7. Integration with RFC v1 (Sandbox)

| RFC v1 piece | What v2 adds on top |
|---|---|
| Universal Unified Source Manager (§2) | Feeds are queries over it — one engine, any adapter mix. |
| Self-contained backups .anizenbk/.hourbk (§4) | `feeds.json` joins the archive: feeds survive device moves and repo shutdowns — with the extensions they depend on. |
| Extension Health Monitoring (§5, AniZen) | Per-source feed health: a source failing inside a feed is flagged *in the feed*, with last-success timestamp — silent dead sources in a merged feed are how trust dies. |
| FileObserver hot-reload (§5, Houri) | Feed definitions hot-reload the same way — no restart. |

## 8. Roadmap & Acceptance Criteria

**Phase 1 — MultiFeed with per-source filters (both apps).**
AC: source chips ≤20; filter chips bound to selected source's native FilterProfile; fallback
labeling honest; merge policy interleave+recency; dedup on.

**Phase 2 — Multiple feeds, manual (both apps).**
AC: create/rename/delete/reorder feeds; rules engine (§6.1); feeds.json schema v2 written and
restored round-trip inside .anizenbk/.hourbk with zero loss.

**Phase 3 — AI-assisted segmentation (AniZen first, Houri lite tier).**
AC: on-device only (verifiable: airplane-mode test); suggestions reviewable per entry; discard/edit
persists; global feed untouched by default.

## 9. Risk Matrix (additive to RFC v1 §6)

| Risk | Level | Mitigation |
|---|---|---|
| Filter-mapping drift (sources change endpoints) | Medium | FilterProfile declared per source version; chips degrade to hidden, never crash; QA fixture per adapter. |
| Merge performance at 20 sources | Medium | Per-source page budgets + lazy interleave; no full-catalog fan-out on open. |
| AI misclassification | Medium | Confidence display, per-entry override, «rules-only» mode for users who refuse ML. |
| Privacy regression | Low | Airplane-mode acceptance test in CI for Phase 3. |
| Feature sprawl on Houri (one maintainer) | Low | Phase 2 ships before Phase 3; lite tier (rules) is the Houri default. |

## 10. Appendix — landscape table (verified 2026-10-10)

| Prior art | What it validates |
|---|---|
| Kototoro — entities & Spaces (in production) | Content typing and scoped views inside one app work at scale. |
| Mangayomi (6 platforms, multi-content) | Mixed manga/anime/novel libraries are mainstream, not niche. |
| Zangetsu ("anime & movie streaming") | The movie+anime coexistence the owner describes already exists. |
| EverythingMoe (24 sections, updated daily) | The culture indexes itself by segmented categories. |
| Miyomi (content-type filters on the catalog) | Even the catalog sorts and filters by type — the apps' feeds should too. |

*Prepared for the developer communities of AniZen, Houri, Kototoro and Miyorare —
with the courtesy already owed to RFC v1's authors. October 2026, Version 2.0 (Draft for review).*
