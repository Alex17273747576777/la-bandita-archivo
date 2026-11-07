# PACK DISCORD — RFC v2 para admins (AniZen · Houri) — 10-oct-2026

> **Guía de publicación (esto NO se pega al chat).** Idioma del paquete: inglés (el de ambas comunidades). Seis piezas medidas: cinco mensajes (1/5 → 5/5) para canal de sugerencias o hilo, y un mensaje único compacto para DM. Cada bloque está dentro de una valla de código: copiar el texto EXACTO de dentro, sin las vallas.
>
> **Cómo publicar:**
> 1. Copia el Mensaje 1/5 y pégalo; adjunta en ESE mismo mensaje la tarjeta PNG (se ve en línea, es el gancho visual) — o la imagen sola si prefieres un post corto.
> 2. Pega en orden los mensajes 2/5 → 5/5, uno por uno (Discord no acepta pega de 2.000+ caracteres juntos; cada bloque ya está bajo el límite).
> 3. Al final, adjunta el HTML completo (`RFC-v2-...-2026-10-10.html`, 74 KB) como archivo: es el spec navegable, 0 peticiones de red, seguro de abrir.
> 4. Para DM directo a un admin: usa el «Mensaje único». Para canal #suggestions: los 5.
> 5. Discord convierte los enlaces de GitHub en tarjetas ricas; si no quieres el unfurl en el mensaje 1, envuélvelos entre `<>` (`<https://…>`).
>
| Pieza | caracteres (len) | unidades UTF-16 (cuenta Discord) |
|---|---|---|
| Mensaje 1/5 — gancho + contexto + las 2 observaciones | 1090 | 1090 |
| Mensaje 2/5 — tesis + objeto Feed + metas | 840 | 840 |
| Mensaje 3/5 — NFI: el gap reportado, resuelto | 844 | 844 |
| Mensaje 4/5 — segmentación manual + IA | 1038 | 1038 |
| Mensaje 5/5 — roadmap + cierre | 811 | 811 |
| Mensaje único (DM / versión compacta) | 1238 | 1238 |

Sello del paquete (sha16 de los 6 mensajes concatenados): `9686bafb73168220`

---

## Mensaje 1/5 — gancho + contexto + las 2 observaciones

```text
-# RFC v2 · part 1/5
# RFC v2 — Unified Feed Architecture for AniZen & Houri
**MultiFeed Manager · per-source filters · on-device segmentation**
*Follow-up to "RFC: In-App Private Extension Sandbox & Self-Contained Backups" (v1.0, Sep 2026) — extends its Source Manager (§2), Backups (§4) and integrations (§5).*

Hello! After the new multiFeed shipped, two field observations came up — this proposal turns them into an architecture that fits the sandbox RFC:

**1 · The multiFeed currently shows one source, with no filters.** Selecting a source inside the feed should expose *that source's own* filters (latest / updated) plus the conventional ones (new works / popular / trending).

**2 · The original ask was a *true* multifeed: multiple feeds.** Global by default, segmentable by hand — or by on-device AI classifying existing entries (e.g., movie sources + anime sources, like Zangetsu / AniDash / Mangayomi already do). Each feed: up to **20 sources/extensions**, same as global.

:page_facing_up: Full spec attached as a single HTML file — works 100% offline, zero network requests.
```

## Mensaje 2/5 — tesis + objeto Feed + metas

```text
-# RFC v2 · part 2/5
## The thesis: the Feed is a portable object
Not a screen — a versioned **`feeds.json`** (`schema: feed.v2`) living on top of the Universal Source Manager and **traveling inside `.anizenbk` / `.hourbk` backups** (RFC v1 §4): feeds survive device moves and repo shutdowns, together with the extensions they depend on.

**Design goals**
- :dart: Feed = first-class object — created, named, edited, backed up, restored
- :compass: Respect native capabilities — never fake a filter; degrade honestly
- :writing_hand: Manual first, AI second — rules are data, portable & testable
- :lock: Zero telemetry — classification on-device; taste never leaves the phone
- :jigsaw: <=20 sources per feed, any adapter mix (Mihon / Aniyomi / Kotatsu DEX)
- :earth_africa: Global feed stays the default — segmentation adds, never removes
```

## Mensaje 3/5 — NFI: el gap reportado, resuelto

```text
-# RFC v2 · part 3/5
## §4 — Normalized Filter Interface (the reported gap, fixed)
Each adapter declares a **FilterProfile**; the feed UI renders *exactly* what the selected source can do:

- **Latest** -> `fetchLatestUpdates()` (Mihon / Aniyomi) · `latest` listing (Kotatsu)
- **Popular** -> `fetchPopularManga()` / `fetchPopularAnime()` · `popular`
- **Updated / new works / trending** -> mapped where native; declared facets for movie sources
- **Full native filters** -> `getFilterList()` (genre, status, year…)

**Fallback rule — no fake filters:** if the source lacks a native endpoint, the engine hides the chip or offers client-side post-filtering visibly labeled *“filtro local — no nativo de la fuente”*. Never silent.

*The attached document includes a live demo of these chips re-binding to the selected source — no network needed.*
```

## Mensaje 4/5 — segmentación manual + IA

```text
-# RFC v2 · part 4/5
## §6 — Segmentation: manual first, AI second, always correctable
**Manual rules** (plain data inside `feeds.json`): `source_in` · `content_type` (manga / anime / novel / movie) · `genre in` · `title contains` · `status in` — combinable with AND / OR.

**AI-assisted (opt-in, on-device):** proposes suggested feeds (“Anime”, “Movies”, “Donghua”…) with per-entry confidence — the user **accepts, edits or discards** each suggestion. AI never moves an entry silently. AniZen can ship it on its existing AI stack; Houri gets the light tier (rules + heuristics) first.

**The field case:** movie + anime sources linked -> AI proposes two feeds; manual mode builds the same with one `content_type` rule. Both paths land in the same `feeds.json`.

*Ecosystem check (verified 2026-10-10):* Miyomi's updated-sort is dominated by multi-content apps (Mangayomi, Zangetsu, Kototoro…), and EverythingMoe indexes the culture in 24 category sections. **Segmentation is the market's rule — the single global feed is the exception.**
```

## Mensaje 5/5 — roadmap + cierre

```text
-# RFC v2 · part 5/5
## §8 — Roadmap & acceptance criteria
**Phase 1 · MultiFeed with per-source filters** — source chips <=20; filter chips re-bind to the selected source; honest fallback labels; merge interleave + recency; dedup on.
**Phase 2 · Multiple feeds, manual** — create / rename / delete / reorder; rules engine; `feeds.json` round-trips inside backups with zero loss.
**Phase 3 · AI segmentation (AniZen first, Houri lite)** — on-device only (airplane-mode test in CI); suggestions reviewable per entry; global untouched by default.

Full spec — 10 sections: data model, UX, integration map, risk matrix, landscape appendix — in the attached HTML: one file, renders offline, no external resources. Happy to iterate on any part. Thank you for the amazing work on v0.5.215 and v1.23.16! :raised_hands:
```

## Mensaje único (DM / versión compacta)

```text
**RFC v2 — Unified Feed Architecture for AniZen & Houri** *(follow-up to the sandbox RFC, Sep 2026)*

The new multiFeed sparked two observations: **(1)** it shows one source with no filters — selecting a source should expose *its* filters (latest / updated) plus the conventional ones (new / popular / trending); **(2)** the original ask was a *true* multifeed — global by default, segmentable by hand or by on-device AI (movie + anime sources side by side, <=20 sources each).

**Thesis:** the Feed is a portable object — `feeds.json` (`feed.v2`) on the Universal Source Manager, traveling inside `.anizenbk` / `.hourbk` backups. Filters are a **declared capability**: a FilterProfile per adapter — native chips, honest *“filtro local”* fallbacks, never fake. Segmentation: **manual rules first** (data, testable), **AI second** (opt-in, on-device, per-entry correctable, zero telemetry).

Roadmap: **P1** per-source filters -> **P2** multiple feeds + rules -> **P3** AI (airplane-mode test in CI). Ecosystem check: multi-content apps already dominate (Mangayomi, Zangetsu, Kototoro) — segmentation is the rule; the single global feed is the exception.

Full spec: 10-section HTML, one file, 100% offline. Feedback welcome :raised_hands:
```
