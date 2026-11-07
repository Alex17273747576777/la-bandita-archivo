# RFC v2.9 — Unified Feed Architecture for AniZen & Houri
## MultiFeed Manager, Per-Source Filters & On-Device Segmentation
*extends "RFC: In-App Private Extension Sandbox & Self-Contained Backups" (v1.0, September 2026) · revisions 2.1–2.5: three review rounds + red-team demolition + property-based fuzzing (October 10, 2026)*

**Prepared:** October 10, 2026 · verified same day · **Revised:** v2.1–v2.9 — rounds + demolition + fuzz + integral audit + decision record + executable §8 + conformance kit
**Target projects:** [salmanbappi/AniZen](https://github.com/salmanbappi/AniZen) (v0.5.215, 30-sep-2026) · [PineappleTwilight/houri](https://github.com/PineappleTwilight/houri) (v1.23.16, released 10-oct)
**Status:** Proposal — **Draft for review** (the status ladder and its criteria are defined in §0) — building on RFC v1 §2 (Sandbox Extension Engine) and §3 (Universal Unified Source Manager)

---

## 0. Status of this document (definitions)

A status label without a criterion is a claim, not a status — and an earlier version of this
document over-claimed: it said «Production Candidate» about a proposal with no merged code.
Corrected here — principle P1 (honest capability) applies to this document too. The ladder:

| State | Criterion — who declares it, on what evidence |
|---|---|
| **Draft for review** ← *this document* | Published and open for review. Declared by the author. |
| **Reviewed** | The maintainers state the spec is implementable as written (or list exactly what blocks it). Declared by each maintainer. |
| **Accepted (per repo)** | A maintainer commits to implement — milestone or issue-state change in that repo. Declared by that repo's maintainer. |
| **Production Candidate (per repo)** | A merged implementation, behind a feature flag, passes **every** §8 acceptance criterion in that repo's CI: golden-file rules parity (warm vs cold), airplane-mode test, feeds.json round-trip with zero loss, ≤20-source budget fixtures. Declared by the repo's maintainer — **never by the proposal author**. |
| **Shipped** | Enabled by default in a stable release of that repo. |

Until a transition happens, this document is simply a **Draft for review**.

---

## Revision history

| Ver | Date | Change |
|---|---|---|
| v2.0 | 2026-10-10 | Initial proposal. |
| v2.1 | 2026-10-10 | Incorporated the five points of the first maintainer review: (1) per-source **fallback ladder** declared by the source — §4.1; (2) **classify once, cache the label** — never in the render path — §6.3; (3) **manual overrides permanent & visible**, AI as suggestion layer over hand-made structure — §6.3; (4) **canonical work identity** vs duplicates policy — §5.1; (5) **stable feed identity under source removal / outage** — §5.2. Roadmap reordered: per-source filters ship first and independently (§8). |
| v2.2 | 2026-10-10 | Second review round absorbed: **chronological floor** + declared versioned aliases in the ladder (§4.1); **hysteresis** on re-classification + **labels GC** (§6.3); pins keyed by **work_key hash** + granularity levels (§6.3); **deterministic canonical tiebreak** + reading-source badge (§5.1); degradation **UI surface** + retry-failed-only refresh (§5.2); **two-store persistence split** (§6.4); Phase 1 vs Phase 3 scope table (§8.1). |
| v2.5 | 2026-10-10 | **Property-based fuzz round** (harness in repo; 3.001 checks pre-fix → 3 real findings; 5.704 checks post-fix → 0 violations): (F1) **recency ties are order-sensitive** — merge now declares its tiebreak (time desc → source id → in-source order), so the result no longer depends on fetch order; (F2) **hysteresis could flip-flop** A→B→A when candidates both clear 0.90 — a label **change** now always requires the margin; the threshold alone only rescues the low-confidence band (< 0.60); (F3) **Turkish İ** survives NFKD with a combining mark — work_key normalization now strips combining marks (\p{M}) after NFKD. Demo code in the HTML updated to match, then re-fuzzed against the live file. Also stated honestly: content addressing guards drift, not malice (§6.1); the «Sin asignar» pool is render-capped with a count summary. |
| v2.6 | 2026-10-10 | **Integral artifact audit** (markup + code + differential oracle): static + mobile battery → 2 real defects (frozen `<title>` still at v2; 2px horizontal overflow at 360px — flex header pushed its tool buttons past the viewport; both fixed); hyperextreme battery **233,570 checks → 0 violations** (35k dedupKey adversarial strings, 400×6 canonical-order permutations, 600×300 boundary-clustered hysteresis ops, 200 pack/restore scenarios); **JS↔Python differential on 4,010 hostile strings → 0 divergences, identical collision profiles**; test-authoring bugs found: 5 — all in the auditor's harness, none in the code. |
| v2.4 | 2026-10-10 | **Internal red-team demolition** (self-audit, acta in repo): (C1) cold-start equality scoped to the **rules layer** — AI layer explicitly async with visible «segmentación actualizada» notice, never silent reshuffle; (C2) **collision-conservative work_key** — collapse requires full-key equality, yearless keys only merge with yearless/equal-year, residual ambiguity → visible «posible duplicado», never auto-merge; (C3) **one visible «Sin asignar» pool, two producers** (no matching rule / no cached label); (A1) **content-addressed rules_packs** (sha256 in the reference, verified on restore); (A2) **source-neutrality invariant** (Goal 09): no sources bundled, feeds present only user-installed sources, catalogs cited as market evidence; (A3) privacy invariant precisely worded — nothing user-derived leaves; model binaries ride the app update channel; (M1) honest latency wording — budgets and QA fixtures, no wall-clock promises; (M2+M3) `mode:"ai"` exemplified with hysteresis constants living in the profile; (M4) badge inventory table; additive optional fields stay within the feed.v2.3 major (dogfooding our own compat policy). |
| v2.3 | 2026-10-10 | Third round absorbed: **three structural principles** with a mechanism→principle traceability table (§2.1); **total precedence** for rules — declared priority, first-match-wins, visible unassigned pool (§6.1); **rules_version** — rules are an independently addressed & migratable object (§6.1); **cold-start acceptance test** beside airplane-mode (§6.3, §8); portable-object hygiene — stable source IDs, credentials never, loud-or-preserving compat (§3); **missing-source visible state** on restore (§5.2); **local-fallback honesty constraint** — window-declared, recomputed every refresh, never cached (§4.1); **≤20 declared as a latency budget** (§2.1). |

---
| v2.7 | 2026-10-10 | **Round 5 (content, not design)**: the published body now carries §§4–6 **unabridged** (the body *is* the canonical document — nothing condensed away); a **Decision Record** documents every alternative that lost and why (so consolidation does not erase the debate); the **status ladder** is defined in §0 and the earlier «Production Candidate» label is demoted — it over-claimed on an unimplemented proposal; a **reviewer checklist** answers the six raised points (all resolved, none deferred). |
| v2.8 | 2026-10-10 | **Round 6 adopted — §8 made executable** (the maintainer's deferred observation): every AC names its **proof artifact**, where it runs, and what failure means; golden-file cold-start parity (warm vs cold) is explicitly flagged as the rung §0 stands on. New **kernel-level battery** (fixed seed, harness in repo): **296.230 checks, 0 violations** on the live code — feeds.json restore under adversarial mutation (20k scenarios: drift, fake seals, cross-major, unknown-field preservation, restore idempotence), precedence engine with declaration-order invariance (50k), 50k-key label cache with day-boundary GC (100k ops, pins never purged), refresh storms with failing sources — frozen order, stale-with-label, retry-failed-only (10k cycles against the live merge). The auditor's own harness: 4 tautological checks removed before counting, and 1 over-strong oracle (permutation invariance beyond the declared `(priority, declaration order)` semantics) produced 39 false violations before being corrected — the artifact's code: **0**. |
| v2.9 | 2026-10-11 | **Conformance Kit v1 shipped** (the maintainer accepted; the level still had headroom): the §8 spec-side proof artifacts are now runnable, in-repo and zero-dependency — `kit-conformidad-v1/` with a manifest mapping each AC to its check (`CONFORMIDAD.md`) and a single runner. Fresh full run against the live file: **529.800 checks, 0 violations** (spec-model 233.570 · kernel 296.230). An implementer reproduces the algorithmic acceptance layer before writing app code. |

## Decision Record — the alternatives that lost, and why

Consolidating the discussion into one document must not erase *why* each decision was made.
Each entry records the alternatives discussed and the reason they were rejected, so a future
contributor gets the debate, not just the winner.

| ID | Decision | Alternatives considered | Why they lost | Lives in |
|---|---|---|---|---|
| DR-1 | Merge identity is **per-entry** (`work_key`); collapse-vs-keep is a declared **per-feed policy** | (a) source-scoped keys — never collapse across sources; (b) feed-scoped silent auto-merge; (c) AI fuzzy matching | (a) hides the very cross-source duplicates the feature exists to surface; (b) the same two entries would merge in one feed and not in another — truth varies per view and loss is silent; (c) non-deterministic, not portable data | §5.1 |
| DR-2 | `work_key` is collision-conservative: ambiguity shows «posible duplicado», never auto-merges | aggressive slug / similarity matching | a false merge is unrecoverable trust damage; a visible badge costs one line | §5.1 |
| DR-3 | Normalization: NFKD → strip `\p{M}` → casefold → ASCII-fold | NFC-only; plain lower+ASCII (the v2.2 rule) | Turkish İ survives both — fuzzing broke the equality (F3); idempotence now verified over 35.000 adversarial strings | §5.1 |
| DR-4 | Recency tiebreak: time desc → source id → in-source order | fetch/arrival order (v2.0 behavior) | 287 permutation violations — merge output depended on which source answered first | §5 |
| DR-5 | Total precedence in `(priority, declaration order)` + one shared visible «Sin asignar» pool | (a) per-feed rule subsets; (b) first-declared-wins; (c) AI resolves conflicts | (a) fragments the model and orphans entries per feed (C3); (b) fragile under reordering; (c) non-deterministic | §6.1 |
| DR-6 | Rules live in their own content-addressed pack (`rules_version` + sha256) | (a) version inside the feed schema; (b) no versioning | (a) a rule tweak would force a feed-schema migration (the B1 residual-string lesson); (b) restore could not detect drift | §6.1 |
| DR-7 | sha256 guards drift/mismatch — **not** malice | claim tamper-resistance | the holder can recompute the hash; the honest scope is device trust + sandbox (RFC v1) | §6.1 |
| DR-8 | Cold-start parity **scoped to the rules layer**; AI layer explicitly async | (a) full parity incl. AI; (b) ship the label cache inside backups | (a) would block first paint on a model run — dishonest; (b) transports derived data: silent reshuffles plus a privacy surface | §6.3 |
| DR-9 | Hysteresis: margin (≥ +0.15) **always** on label change; the 0.90 threshold rescues only the < 0.60 band | threshold-only (the v2.2 rule); freeze labels on model upgrade | threshold-only flip-flopped A→B→A above 0.90 (F2); freezing never learns | §6.3 |
| DR-10 | Pins keyed by `work_key` hash, above the classifier, surviving restore | (a) pin by row id; (b) pin by raw title; (c) pins honored until re-train | (a) dies on refresh; (b) breaks under normalization (İ); (c) silent — violates P3 | §6.3 |
| DR-11 | Labels GC (90d, same batch job that classifies, never on cold start) | (a) GC on cold start; (b) TTL on write; (c) never GC | (a) stalls first open (C1); (b) touches intention invisibly; (c) unbounded growth | §6.3 / §6.4 |
| DR-12 | Degradation: frozen order, stale-with-label, retry-failed-only, visible «fuente faltante» | reshuffle on failure; silent drop; retry-all | a dead source must not reshuffle or erase the feed — silent loss is how trust dies (P1) | §5.2 |

## Reviewer checklist — asked and answered

Raised by the maintainer in round 5; each point's state in this document:

| # | Point | State | Where / what guarantees it |
|---|---|---|---|
| 1 | Total precedence | **Resolved** | §6.1 — rules evaluate in `(priority, declaration order)`; first match wins; no-match lands in the visible «Sin asignar» pool; golden-file tests pin assignment. |
| 2 | Independent rules versioning | **Resolved** | §6.1 — `rules_packs` carry their own `rules_version` + sha256, verified on restore; rule tweaks migrate independently of the feed schema. |
| 3 | Cold-start parity | **Resolved, scoped** | §6.3 — equality guaranteed on the rules layer (golden files, warm vs cold, in CI). The AI layer is async *by declared design*: entries wait in the visible pool with a notice. A scope decision (DR-8), not a deferral. |
| 4 | Hysteresis on re-classification | **Resolved** | §6.3 — precise rule: a label change always requires ≥ +0.15; the 0.90 threshold alone rescues only the < 0.60 band; fuzz-proven (F2). |
| 5 | Eviction | **Resolved** | §6.3 / §6.4 — labels GC at 90d in the same batch job that classifies, never on cold start; GC never touches the rules store. |
| 6 | Pin keying by work_key | **Resolved** | §6.3 — pins are keyed by work_key hash, sit above the classifier, and survive re-classification, model upgrades and restore. |

Nothing on this list is deferred. If a future round cannot find one of these guarantees at the
cited section, that is a defect of this document — report it as such.

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

**En la v2.1**, tras la primera revisión del mantenedor, se añaden compromisos explícitos: la fila
de filtros se **genera de lo que cada fuente realmente admite** con una escalera de retroceso
declarada por fuente (§4.1); la clasificación IA se ejecuta **una vez por trabajo y se cachea la
etiqueta** — jamás en el camino del render (§6.3); la anulación manual es **permanente y visible**;
la identidad del trabajo es **canónica y declarada** por feed (§5.1); y una fuente caída o
eliminada **no detiene ni reordena el feed** (§5.2).

---

## 1. Context & Motivation — the landscape speaks (verified 2026-10-10)

**The catalog layer already segments; the app layer does not.**

| Evidence | What it shows |
|---|---|
| [Miyomi](https://miyomi.app/software?sort=updated-desc&view=grid) (consulted 10-oct) | Sort-by-updated is dominated by **multi-content apps**: Mangayomi (manga+novel+anime, 6 platforms), Zangetsu ("anime & movie streaming"), AniDash, Foxlations, Kototoro (manga+novel+video, 125.6k) — content types already coexist inside single apps. |
| [EverythingMoe](https://everythingmoe.com/) (consulted 10-oct; updated same day) | The reference index of the culture is organized in **24 category sections** (Anime Streaming 94 sites · Manga Reading 96 · Novel · Drama · Donghua…) — segmentation is how the ecosystem itself thinks. |
| houri v1.23.16 released 10-oct; 14 releases in 9 days | Shipping cadence supports iterative feed features without long freezes. |
| AniZen v0.5.215 (30-sep) + in-app AI diagnostics (RFC v1 §5) | AniZen already carries the on-device intelligence needed for assisted segmentation. |

**The current gap (owner's field report):** activating the new multiFeed surfaces a single source,
with no source-specific filter toggling (recent / updated) and no conventional filters
(new works / popular / trending) applied to it. And there is no way to keep *several* feeds side by
side — the global feed cannot be forked into categories, manual or AI-assisted.

**First maintainer review (2026-10-10):** the direction was called solid; per-source filters were
singled out as the low-risk half that should ship first and independently; the five structural
points listed in the revision history were requested and are now addressed inline.

## 2. Design Goals

1. **Feed as a first-class, portable object** — created, named, edited, backed up, restored.
2. **Respect native source capabilities** — the filter row is generated from what each source
   actually supports, with a declared fallback ladder; never an empty chip, never a silent bucket.
3. **Manual first, AI second** — deterministic rules cover 90% of needs; AI is a suggestion layer
   over hand-made structure, opt-in, on-device, correctable, and cheap at runtime.
4. **Zero telemetry** — classification runs on-device; nothing about a user's taste leaves the phone.
5. **≤20 sources bound the worst-case refresh **by construction** (per-source page budget × ≤20);
budgets are device-tier config and are measured in QA fixtures — the spec makes no wall-clock
promises.1).
6. **Global feed remains the default** — segmentation adds; it never removes.

### 2.1 — Three structural principles & the mechanism map (v2.3)

The mechanisms of v2.1/v2.2 are not a bag: they hang from three principles. Every future feature
must state which principle carries it — if none does, it does not ship.

- **P1 · Honest capability** — render what each source can actually do; degrade visibly; a silent
  feed is a defect, not a state.
- **P2 · Deterministic, data-first segmentation** — rules, identities and precedence are declared
  data; same inputs, same segments, on every device, cold or warm.
- **P3 · Derived vs intent** — disposable compute and durable intent live in separate stores with
  separate write paths; the portable object carries intent, references capabilities, never secrets.

| v2.1 mechanism | Carrier section | Principle |
|---|---|---|
| Label cache + hysteresis + eviction (GC) | §6.3 | P3 (derived store), P2 (deterministic recompute) |
| Pins keyed by work_key hash | §6.3 | P2 (canonical identity), P3 (INTENT store) |
| Duplicate policy (canonical / keep) | §5.1 | P2 (declared tiebreak, stable across sessions) |
| Degradation (stale-with-label, frozen order) | §5.2 | P1 (visible, boring failure) |
| Fallback ladder (floor + declared aliases) | §4.1 | P1 (never fake, never silent) |

### 2.2 — Why 20 sources: a latency budget (v2.3)

The ≤20 cap is a budget line, inherited from the owner's request and now declared: per refresh,
merge cost ≈ Σ(one page per source) + interleave — 20 sources bound the worst-case refresh to a
few seconds and bound memory on low-end devices. The UI limit is the consequence, not the cause.
Device tiers may lower the number; nothing raises it silently.
7. **Classify once, render forever** — no AI work in feed render or scroll paths (v2.1).
8. **Degradation must be boring** — a dead or removed source never blocks, re-sorts, or
   re-identifies a feed (v2.1).
9. **Source neutrality (v2.4)** — the app bundles no sources and no content: feeds present entries
   only from sources the user already installed; catalogs are cited as market evidence, never as
   content.

## 3. Data Model — the Feed object

```jsonc
// feeds.json — travels inside .anizenbk / .hourbk (RFC v1 §4)
{
  "schema": "feed.v2.3",
  "feeds": [
    {
      "id": "feed_global",            // reserved, non-deletable, immutable (see §5.2)
      "name": "Global",
      "sources": [ /* up to 20 */ { "pkg": "eu.kanade.tachiyomi.ext.en.mangadex", "enabled": true } ],
      "mode": "global",               // global | manual | ai
      "rules_pack": null,             // global segments by definition, not by rules (§6.1)
      "ai": null,
      "dedup": { "policy": "canonical", "show_duplicates": false },   // §5.1
      "degradation": { "policy": "stale_with_label", "freeze_order": true }, // §5.2
      "refresh": { "policy": "on_open", "ttl_min": 180 },
      "created": "2026-10-10T16:00:00Z"
    },
    {
      "id": "feed_anime_movies",
      "name": "Anime + Movies",
      "sources": [ { "pkg": "anime.source.a", "enabled": true },
                   { "pkg": "movie.source.b", "enabled": true } ],
      "mode": "manual",
      "rules_pack": { "id": "rules_anime_movies", "rules_version": 1, "sha256": "9f31c2…" }, // content-addressed (§6.1)
      "dedup": { "policy": "keep_duplicates" },
      "degradation": { "policy": "stale_with_label", "freeze_order": true },
      "refresh": { "policy": "scheduled", "ttl_min": 720 }
    },
    {
      "id": "feed_ai_donghua",
      "name": "Donghua (AI-assisted)",
      "sources": [ { "pkg": "anime.source.c", "enabled": true } ],
      "mode": "ai",                   // labels arrive async; «Sin asignar» until the batch lands (§6.3)
      "rules_pack": null,
      "ai": { "model_v": "cls-2026.10", "hysteresis": { "threshold": 0.90, "margin": 0.15 } },
      "dedup": { "policy": "canonical" },
      "degradation": { "policy": "stale_with_label", "freeze_order": true },
      "refresh": { "policy": "scheduled", "ttl_min": 1440 }
    }
  ],
  "rules_packs": {
    "rules_anime_movies": {
      "rules_version": 1,
      "sha256": "9f31c2…",            // restored references verify against this (§6.1)
      "rules": [
        { "priority": 10, "match": "content_type", "value": "movie" },
        { "priority": 20, "match": "genre_in", "value": ["Sports"] }
      ]
    }
  }
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

### 4.1 Fallback ladder — declared per source, never improvised (v2.1)

"Popular" and "trending" are not universal concepts. When a source does not expose a bucket, the
engine walks the **ladder declared by that source** in its FilterProfile — it never renders an
empty chip and never silently dumps everything into one bucket:

1. **Native** — the source exposes the bucket's own endpoint → chip rendered as native.
2. **Declared alias** — the profile's **versioned alias map** maps another of the source's endpoints
   to the bucket (`"aliases": { "trending": "popular" }`) → chip rendered as native, tooltip names the
   backing endpoint. Nothing is inferred at runtime: if the map does not declare it, the alias does
   not exist — no guessing game one level down.
3. **Local post-filter** — client-side filtering over already-fetched pages → chip visibly labeled
   «filtro local — no nativo de la fuente».
4. **Chronological floor (v2.2)** — every adapter family exposes latest/updated, so a source that
   matches no bucket above still serves it **chronological and labeled as such** («cronológico — la
   fuente no expone popular»). The rung is never silent, and the feed is never indistinguishable
   from empty.
5. **Hidden — visible, never silent (v2.2)** — only a source with no working listing at all ends
   hidden, and that state is **visible per source** in the feed's health row («esta fuente no expone
   filtros» / «sin respuesta»). A source can no longer contribute nothing without signal.

Because the ladder lives in the source's FilterProfile (part of its manifest, alongside the
extension metadata), **adding a source is self-describing**: the feed UI learns what the source can
do without new feed-side code. The ladder order itself is per-source data, reviewable in QA
fixtures, and versioned with the source.

**Local-fallback honesty constraint (v2.3):** a local filter can only trim the already-fetched
window — its result is a function of **window size and fetch order**, and both are declared by the
adapter in the FilterProfile. Local results are **recomputed on every refresh and never cached**:
the window moves underneath them, and an honest fallback that goes stale is just a slower lie.

## 5. MultiFeed UX Specification

- **Source chips** (one per enabled source of the feed, max 20) + **filter chips row** that
  re-binds to the *selected* source's FilterProfile (§4) — this is the exact gap reported.
- **Feed switcher**: horizontal tabs — Global · user feeds · «+ New feed». Long-press → rename,
  reorder, export single feed.
- **Merge policies** (per feed): `interleave` (round-robin, default), `weighted` (per-source weight),
  `recency` (strict time order across sources; ties break by source id, then in-source order —
  the merge no longer depends on which source answers first, v2.5, fuzz-proven).
- **Per-source state inside the feed** (solo mute, weight, filter override) — so «this source, its
  filters» is one tap, not a detour to the Sources screen.

### 5.1 Canonical work identity & duplicates (v2.1)

The global feed will surface the same work from multiple sources. The behavior is **declared data,
per feed**, not an accident:

- **`work_key`** = normalized title — NFKD, strip combining marks (\p{M}), casefold, fold to
  ASCII, punctuation to spaces (the Turkish İ must equal i, v2.5) — plus content type and declared
  creator/year when the source exposes them. Hashed locally; nothing leaves the device.
- **`policy: "canonical"`** (default for Global): duplicates collapse to the first occurrence; a
  badge lists the other sources («también en B, C»). Metadata of the winning entry wins; no silent
  merging of chapter/episode state across sources.
- **Canonical tiebreak is deterministic (v2.2):** (1) the feed's primary source if the user pinned
  one, (2) richer metadata (count of non-null fields), (3) most recently updated entry, (4) stable
  lexical order by source id. Same winner every session — collapse is never non-deterministic.
- **The badge tells the reading truth (v2.2):** the canonical entry says «canónica en A»; if the
  user's download came from B, it says «leyendo desde B · canónica en A», with a one-tap
  «usar B como canónica» — a primary-source pin that feeds tiebreak rule (1).
- **Collision-conservative by default (v2.4):** same title ≠ same work (Fruits Basket 2001/2019).
  Collapse requires **exact full-key equality**; entries whose key lacks year/creator only collapse
  with yearless or equal-year keys; residual ambiguity never auto-collapses — it shows a visible
  «posible duplicado» badge. When in doubt, keep duplicates: P1 forbids faking a merge.
- **Badge inventory (v2.4, closed set):** «también en B, C» · «leyendo desde B · canónica en A» ·
  «posible duplicado» · stale-with-label («sin actualizar desde…») · «fuente faltante» ·
  «Sin asignar» · pin mark. New badges require a spec row — no UI drift.
- **`policy: "keep_duplicates"`** (available per feed, and the sane default for library-adjacent
  feeds): duplicates stay visible; the filter-by-source chips (§4) are how users separate them.
- The «show duplicates» toggle overrides either policy temporarily, per session.

### 5.2 Stable feed identity under removal or outage (v2.1)

Multi-source feeds degrade badly when a source dies. Rules, in order of importance:

- **A downed source never blocks the feed.** Merge is partial-success: live sources refresh; the
  downed one serves its last cache **stale-with-label** («sin actualizar desde el 8-oct») instead
  of stalling or vanishing.
- **No global re-sorting on failure.** Entry order for surviving sources is untouched; the failed
  source's block keeps its position, flagged. A flaky source must not make the whole feed feel
  haunted.
- **Degradation has a specified surface (v2.2):** a feed-level banner («2 fuentes sin actualizar ·
  última sincronización 8-oct») **and** per-item markers on entries served stale — the banner is
  feed state, the markers are attribution.
- **Degraded refresh is retry-failed-only (v2.2):** live sources serve from cache and are not
  re-fetched; only the failed sources retry, merged incrementally. A full re-fetch exists only as
  an explicit user action. Documented as the rule, not as an optimization.
- **Removal is identity-preserving.** Deleting or disabling a source changes nothing else: the
  feed keeps its `id`, name, order, rules, and pins. Entries from the removed source leave the
  merge; nothing renumbers. `feed_global` is immutable and non-deletable by definition.
- **Health is visible where it matters** (ties into RFC v1 §5 Extension Health Monitoring): the
  per-source row inside the feed shows last-success timestamp and state, not a global error toast.
- **A missing source is a visible state, never a silent loss (v2.3):** if a referenced source id is
  absent on restore or import (renamed, removed, not yet installed), the feed loads with a
  «fuente faltante» placeholder block in the switcher and health row — the feed says so, always.

## 6. Segmentation — manual first, AI assisted, always correctable

### 6.1 Manual rules (deterministic, portable, testable)
`source_in` · `content_type` (manga/anime/novel/movie) · `genre/tag in` · `title contains` ·
`status in` · combined with AND/OR. Rules are data — no code, no lock-in.

**Precedence is total, not emergent (v2.3):** every rule carries an explicit `priority` (integer,
lower wins); evaluation sorts by `(priority, declaration order)` — a total order — and the first
matching rule takes the entry. **An entry matching no rule goes to the visible «Sin asignar»
pool** — never dropped, never auto-spread; the pool is a real segment in the feed UI and its size
is part of the QA fixture output. Same rules + same entries ⇒ same assignment on any device,
warm or cold; golden-file tests pin this.

**Rules are independently versioned (v2.3):** the rule set lives in its own addressed object
(`rules_pack` with `rules_version`), referenced by the feed — rule tweaks bump `rules_version`
and migrate on their own; the feed schema (`feed.v2.3`) moves only when the feed object itself
changes shape. One data change must not burn the schema's migration budget. The pack reference is
**content-addressed (v2.4):** it carries the sha256 prefix of the rules array, and restore verifies
it — an id/version/content mismatch fails loudly with a report. Stated honestly: this guards
  against **drift and mismatch, not malice** — tamper-resistance lives in device trust and the
  sandbox, not in a hash the holder can recompute (v2.5). The **«Sin asignar» pool is the
single visible bucket across producers (v2.4):** an entry lands there either when no rule matches
(rules producer) or when no cached label exists yet (AI producer) — one pool, two feeds into it. Render caps
  the pool view with a count summary («+112 más»); the data stays whole (v2.5).

### 6.2 AI-assisted segmentation (opt-in, on-device, correctable)
- **Input:** the existing entries of the Global feed (titles, genres, tags, content type metadata).
- **Engine:** small on-device classifier; AniZen can ship it on its existing AI diagnostics stack
  (RFC v1 §5); Houri ships the lighter tier (rules + heuristics) first.
- **Behavior:** proposes *suggested feeds* (e.g., «Anime», «Movies», «Donghua», «Long-runners»)
  with per-entry confidence; the user accepts, edits, or discards each suggestion. AI never moves
  an entry silently — every assignment is reviewable, reversible, and locally computed.
- **Privacy (precise invariant, v2.4):** nothing user-derived ever leaves the device; the
  segmentation pipeline makes zero network calls; model binaries arrive only through the app's own
  update channel — the acceptance tests (airplane / cold-start) cover the pipeline, not the update
  channel.
- **Example (owner's case):** movie sources + anime sources linked → AI proposes two feeds; manual
  mode can build the same with one `content_type` rule — both paths land in the same `feeds.json`.

### 6.3 Classify once, cache the label; pins are permanent (v2.1)

The maintainer review named the cost correctly: classification inside the render path is a battery
and latency tax on the exact screen users open most. So:

- **Classification is a job, not a render step.** It runs once per work — on first sight of a new
  `work_key`, or in an explicit, user-triggered batch — and writes to a local **label cache**:
  `work_key → { label, confidence, model_version, timestamp }`. Feed render and scroll read the
  cache; they never invoke the model. Zero classification work happens on the screen being
  scrolled.
- **Cache invalidation is boring too:** a label is recomputed only when the user edits the rule
  set, upgrades the model *and* opts into re-classification, or requests it per entry. Model
  version is stored with the label so stale caches are detectable, not assumed.
- **Hysteresis guards re-classification (precise rule, v2.5):** on a model_v upgrade — or any
  recompute — a **label change** always requires beating the old confidence by the margin
  (≥ +0.15); the high-confidence threshold (≥ 0.90) alone is only enough to rescue the
  low-confidence band (< 0.60). A candidate that fails the margin is kept as a visible alternate.
  Fuzzing showed why: threshold-only allowed A→B→A flip-flops between strong candidates. Both
  constants are named config — segments do not rotate when the model updates.
- **Labels GC (v2.2):** rows unseen for `labels_gc.days` (default 90) are purged by the same batch
  job that classifies — never on cold start; cold start reads per key and never loads the table
  whole.
- **Cold-start determinism is an acceptance test — scoped to the rules layer (v2.4):** a fresh
  install with an empty label cache and the same `feeds.json` + `rules_pack` must produce
  **identical rules-layer segments** to a warm device; golden files in CI run both paths. The AI
  layer is explicitly **async**: a cold start shows those entries in the «Sin asignar» pool until
  the classification batch lands, and arriving labels apply with a visible «segmentación
  actualizada» notice — the feed may enrich between launches, but never reshuffles silently.
- **Manual overrides are permanent and visible.** A user pin (`{ "pin": "Movies" }` on a work)
  sits *above* the classifier forever: pins survive re-classification, model upgrades, and restore
  from backup (they live in `feeds.json`). Pinned entries show a small pin mark, so the structure
  reads honestly. The classifier will mislabel niche and multi-genre titles — the answer is a
  one-tap pin, not a fight with the model. Pins are keyed by **work_key hash, not row id** (v2.2):
  a work that leaves and returns keeps its pin. Granularity is two-level: `pin_segment` (membership,
  default) and `pin_position` (membership + explicit order, opt-in per entry).
- **AI is a suggestion layer over hand-made structure, never a replacement.** Feeds created by
  rules are the skeleton; AI proposals attach to it as suggestions; pins and rules always win.

### 6.4 — Two stores, one write path each (v2.2)

Persistence is split so janitorial work can never touch intent — the cheapest insurance in the
whole document:

- **LABELS** — derived and disposable: `k / label / conf / model_v / ts`. Wiped whole without
  losing anything that matters; GC and model migrations touch only this store.
- **INTENT** — durable user data, lives in `feeds.json`: feed definitions, rules, dedup policy,
  pins.
- One write path each, **never a shared transaction**: a purge or a model migration is physically
  unable to reach intent. Backups always carry INTENT; LABELS ride along only as optional cache
  (recomputable).

## 7. Integration with RFC v1 (Sandbox)

| RFC v1 piece | What v2 adds on top |
|---|---|
| Universal Unified Source Manager (§2) | Feeds are queries over it — one engine, any adapter mix. |
| Self-contained backups .anizenbk/.hourbk (§4) | `feeds.json` (feeds, rules, pins, label cache) joins the archive: feeds survive device moves and repo shutdowns — with the extensions they depend on. |
| Extension Health Monitoring (§5, AniZen) | Per-source feed health in the feed itself (§5.2): state + last-success per source, feeding the stale-with-label policy. |
| FileObserver hot-reload (§5, Houri) | Feed definitions hot-reload the same way — no restart. |

**Portable-object hygiene (v2.3, invariant):** `feeds.json` references adapters by **stable source
id** (display names resolved at runtime) and **never carries credentials, cookies or session
tokens** — extensions needing auth keep it in app-private storage (RFC v1 sandbox); the export
path runs a sanitizer that refuses to embed secrets. Compat policy: same schema major → unknown
fields are **preserved verbatim** through load/save (round-trip, never mangled); different major →
import **fails loudly** with a report. A backup that leaks or silently rewrites is not a backup.

## 8. Roadmap & Acceptance Criteria

**Phase 1 — Per-source filters with the fallback ladder (both apps). Ships first, independently —
it does not wait for anything else in this document.**
Every AC below is a **verifiable criterion with a named proof artifact** — vague prose was the
weak rung this ladder stood on (maintainer's round-6 observation, adopted): if a criterion cannot
demonstrate how it is checked, it is rewritten here until it can.

**Conformance Kit v1 — shipped.** The spec-side checks behind these matrices run as fixed-seed,
zero-dependency harnesses: `kit-conformidad-v1/run-all.js`, with a manifest (`CONFORMIDAD.md`)
mapping every AC to its check. Last full run: **529.800 checks, 0 violations** (2026-10-11).
UI, screenshot, golden-file and emulator artifacts stay implementation-side by nature — §8
declares them; the kit ships everything a specification can ship.

**Phase 1 — Per-source filters with the fallback ladder (both apps). Ships first, independently —
it does not wait for anything else in this document.**

| AC | Proof artifact (must exist in the repo) | Runs in | Failure means |
|---|---|---|---|
| Source chips ≤20 | Unit test: the 21st source is rejected at build time; UI test: chips render exactly `feed.sources` | unit + screenshot CI | >20 chips, or chips ≠ sources |
| Filter row from FilterProfile | Contract test per adapter: chips == declared capabilities, nothing else | adapter-fixture CI matrix | any chip without a declared backend |
| Ladder order per §4.1 | Golden files: rung resolution per fixture source recorded and diffed | CI golden job | rung differs from declaration |
| Honest fallback labeling | UI test: local post-filter renders «filtro local — no nativo»; hidden is a visible health state | screenshot CI | unlabeled local filter, or silent hide |
| Merge interleave + recency with declared tiebreak | Property test: merge output invariant under fetch-order permutations (the 400×6 harness family, in repo) | CI property job | output depends on arrival order |
| Dedup canonical/keep + toggle (§5.1) | Property test over the adversarial title corpus: key idempotence, ASCII output; toggle preserves raw entries | CI property job | non-idempotent key, or toggle loses data |

**Phase 2 — Multiple feeds, manual (both apps).**

| AC | Proof artifact | Runs in | Failure means |
|---|---|---|---|
| Create/rename/delete/reorder | Instrumented UI suite writing feeds.json; schema validator gates every write | UI CI suite | validator error, or UI state ≠ file |
| Immutable identity, stale-with-label (§5.2) | Fault injection: source dies mid-refresh → order frozen, stale label set, id unchanged | CI fault-injection job | reshuffle or silent drop |
| Rules engine, total precedence (§6.1) | Property test: `(priority, declaration order)` is a total order; first match wins; no-match lands in the visible pool; golden files pin assignments | CI property + golden | precedence violated, or orphan entries invisible |
| packs sha256 round-trip | Tamper matrix: rule drift, fake seal, cross-major → all fail loudly; clean pack restores | CI storage job | any tamper restores silently |
| Zero-loss restore in backups | Round-trip with unknown-field injection: same-major preserves unknown fields verbatim (§7) | CI round-trip job | any field lost |

**Phase 3 — AI-assisted segmentation as a non-blocking prototype (AniZen first, Houri lite tier).
Valuable, but never a prerequisite for feed work.**

| AC | Proof artifact | Runs in | Failure means |
|---|---|---|---|
| Classify-once — no model in render/scroll (§6.3) | Trace test: the render path records zero model invocations | CI instrumentation | any model call on screen |
| Pins permanent & visible | Property test: pins survive re-classification, model upgrade and restore (120-day simulated churn) | CI property job | a pin lost, or a pin invisible |
| Suggestions reviewable per entry | UI test: accept/edit/discard persists to feeds.json | UI CI suite | a suggestion applied without review |
| On-device only | Airplane profile: instrumented runtime asserts zero network syscalls during classify + render | CI emulator, airplane | any network syscall |
| Cold-start rules parity — **the rung §0 stands on** | Golden files: rules-layer segment ids equal warm vs cold install given the same feeds.json + pack; the AI layer is async by declared design (DR-8) | CI golden job, both profiles | any rules-layer divergence |
| Global untouched by default | Snapshot: global feed before/after segmentation diffs empty unless the user opts in | CI snapshot | silent mutation of global feed |

### 8.1 — What's actually in Phase 1 vs Phase 3 (v2.2)

| Concern | Phase 1 (ships alone, zero models) | Phase 3 (adds only the model) |
|---|---|---|
| Filter row + ladder | Generated from FilterProfile; chronological floor; declared versioned aliases | — |
| Identity & duplicates | work_key; canonical dedup; deterministic tiebreak; reading-source badge | — |
| Degradation | Banner + per-item markers; retry-failed-only refresh; frozen order | — |
| Labels | Table with k/label/conf/model_v/ts — **rules engine as label producer** | On-device classifier as an additional producer |
| Cache policy | Schema carries model_v + ts from day one | Hysteresis activation (threshold + margin); GC activation by volume |
| Pins | work_key-keyed; pin_segment; fixed precedence | — (unchanged) |
| Persistence | Two stores, one write path each (§6.4) | — (unchanged) |
| Privacy | No model, nothing to test | Airplane-mode acceptance test in CI |

The infrastructure contract is identical across phases — Phase 3 plugs a model into a socket
Phase 1 already built and tested with rules.

## 9. Risk Matrix (additive to RFC v1 §6)

| Risk | Level | Mitigation |
|---|---|---|
| Filter-mapping drift (sources change endpoints) | Medium | Ladder declared per source version (§4.1); chips degrade down the ladder, never crash; QA fixture per adapter. |
| Merge performance at 20 sources | Medium | Per-source page budgets + lazy interleave; no full-catalog fan-out on open. |
| AI misclassification | Medium | One-tap permanent pins (§6.3), confidence display, per-entry override, «rules-only» mode. |
| Battery/latency from classification | Medium→Solved | Classify-once + label cache; render path is cache-read only (§6.3). |
| Dead source degrades feed | High→Solved | Partial-success merge, stale-with-label, frozen order, immutable feed id (§5.2). |
| Privacy regression | Low | Airplane-mode acceptance test in CI for Phase 3. |
| Feature sprawl on Houri (one maintainer) | Low | Phase 1 ships alone first; Phase 2 before Phase 3; lite tier is the Houri default; Phase 3 is a prototype, not a blocker. |

## 10. Appendix — landscape table (verified 2026-10-10)

| Prior art | What it validates |
|---|---|
| Kototoro — entities & Spaces (in production) | Content typing and scoped views inside one app work at scale. |
| Mangayomi (6 platforms, multi-content) | Mixed manga/anime/novel libraries are mainstream, not niche. |
| Zangetsu ("anime & movie streaming") | The movie+anime coexistence the owner describes already exists. |
| EverythingMoe (24 sections, updated daily) | The culture indexes itself by segmented categories. |
| Miyomi (content-type filters on the catalog) | Even the catalog sorts and filters by type — the apps' feeds should too. |

*Prepared for the developer communities of AniZen and Houri — with the courtesy already owed to
RFC v1's authors, with thanks for the three review rounds that sharpened it, and with one internal
demolition that tried to break it before anyone else could. October 2026, Version 2.9 (Draft for
review).*
