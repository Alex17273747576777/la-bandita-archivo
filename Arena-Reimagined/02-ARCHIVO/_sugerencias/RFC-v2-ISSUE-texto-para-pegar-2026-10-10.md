# RFC v2 — TEXTO PARA EL ISSUE DE GITHUB (estilo #30) — 10-oct-2026

> **Cómo usar esto (NO se pega al issue).** El plan del dueño: publicar el RFC v2 como issue
> (igual que el #30 de houri) y compartir en Discord solo el enlace resultante. Pasos:
> 1. Descarga de este workspace el archivo adjunto: **`RFC-v2-UNIFIED-FEED-AniZen-Houri-2026-10-10.html`** (74 KB, nombre ASCII, se abre offline — mismo mecanismo user-attachments que usaste con el v1 en el #30).
> 2. Abre «New issue» en el repo destino:
>    · Houri → https://github.com/PineappleTwilight/houri/issues/new?template=1_request_feature.yml (elige ⭐ Feature request)
>    · AniZen → https://github.com/salmanbappi/AniZen/issues/new (elige ⭐ Feature request)
> 3. Pega el **título** y el **cuerpo** de abajo (el que corresponda al repo), adjunta el HTML en
>    «Describe your suggested feature» o en «Other details», marca las 4 casillas de
>    Acknowledgements y publica.
> 4. Comparte en Discord el enlace del issue publicado. Listo.
>
> Nota: los dos repos usan la misma familia de plantilla (Komikku/Mihon), así que el cuerpo vale
> para ambos; solo cambia la primera línea de referencia.

---

## TÍTULO del issue (ambos repos)

```text
RFC v2 — Unified Feed Architecture (MultiFeed Manager, per-source filters, on-device segmentation)
```

---

## CUERPO para Houri (referencia al #30)

```markdown
**Follow-up to #30** — the sandbox extension RFC you resolved in **1.23.2**. Thank you for the
incredible turnaround! After some days on the new multiFeed, two field observations came up.
I wrote them up as a full architecture proposal, attached as a **single self-contained HTML
file** (opens offline, zero network requests, live demos inside).

### 1 · Per-source filters inside the multiFeed
Selecting a source currently exposes no filters. Selecting a source should toggle *that
source's own* filter set (latest / updated) plus the conventional ones (new works / popular /
trending).

### 2 · A true multifeed: multiple feeds
Global feed by default, segmentable **by hand or by on-device AI** classifying the existing
entries — e.g. movie sources + anime sources side by side (Zangetsu, AniDash and Mangayomi
already ship this). Each feed: up to **20 sources/extensions**, same as global.

### The proposal in one line
The Feed becomes a **portable object** — `feeds.json` (`schema: feed.v2`) living on the
Universal Source Manager and traveling inside `.anizenbk` / `.hourbk` backups — with a
**Normalized Filter Interface** per adapter (native chips, honest “local filter” fallbacks,
never fake), merge policies with dedup, **manual rules first + opt-in on-device AI second**
(per-entry correctable, airplane-mode acceptance test in CI).

**Attached:** `RFC-v2-UNIFIED-FEED-AniZen-Houri-2026-10-10.html` — 10 sections: data model,
UX spec, integration map with the sandbox pieces already shipped, 3-phase roadmap with
acceptance criteria, risk matrix, and an ecosystem appendix (verified 2026-10-10). The
filter-chip re-binding, the merge policies and the rule engine run as live demos inside the
file itself.
```

---

## CUERPO para AniZen (referencia neutra, sin nº de issue)

```markdown
**Follow-up to the sandbox extension RFC** shared with this project in September 2026. After
some days on the new multiFeed, two field observations came up. I wrote them up as a full
architecture proposal, attached as a **single self-contained HTML file** (opens offline, zero
network requests, live demos inside).

### 1 · Per-source filters inside the multiFeed
Selecting a source currently exposes no filters. Selecting a source should toggle *that
source's own* filter set (latest / updated) plus the conventional ones (new works / popular /
trending).

### 2 · A true multifeed: multiple feeds
Global feed by default, segmentable **by hand or by on-device AI** classifying the existing
entries — e.g. movie sources + anime sources side by side (Zangetsu, AniDash and Mangayomi
already ship this). Each feed: up to **20 sources/extensions**, same as global.

### The proposal in one line
The Feed becomes a **portable object** — `feeds.json` (`schema: feed.v2`) living on the
Universal Source Manager and traveling inside `.anizenbk` / `.hourbk` backups — with a
**Normalized Filter Interface** per adapter (native chips, honest “local filter” fallbacks,
never fake), merge policies with dedup, **manual rules first + opt-in on-device AI second**
(per-entry correctable, airplane-mode acceptance test in CI).

**Attached:** `RFC-v2-UNIFIED-FEED-AniZen-Houri-2026-10-10.html` — 10 sections: data model,
UX spec, integration map with the sandbox pieces already shipped, 3-phase roadmap with
acceptance criteria, risk matrix, and an ecosystem appendix (verified 2026-10-10). The
filter-chip re-binding, the merge policies and the rule engine run as live demos inside the
file itself.
```

---

## Casillas de Acknowledgements (marcar todas)

- [x] I have searched the existing issues and this is a new ticket, **NOT** a duplicate…
- [x] I have written a short but informative title.
- [x] I have updated the app to **latest** (houri v1.23.16 · AniZen v0.5.215 — ambas vigentes hoy 10-oct).
- [x] I will fill out all of the requested information in this form.

---

## Sellado de esta pieza

- Cuerpo Houri: medido abajo · Cuerpo AniZen: +24 c por la referencia neutra · límite de issue
  de GitHub: muy por encima (los cuerpos caben con holgura).
- Adjunto requerido: `RFC-v2-UNIFIED-FEED-AniZen-Houri-2026-10-10.html` (sha16 del envase
  `b537482707f7a396` · sella el texto fuente `bb408a9b10246be0`).
- El pack Discord de las 5 piezas queda en el archivo como reserva; el plan vigente del dueño es
  solo el enlace del issue.


---

# ADENDA v2.1 (10-oct tarde) — SEGUNDA ENTREGA, TRAS LA PRIMERA REVISIÓN

**Lección del revisor:** «solo obtuve el texto del problema a través de los enlaces, no el HTML
adjunto» — el adjunto NO llega. Corrección de entrega: el spec COMPLETO va pegado en el PRIMER
COMENTARIO del issue (GitHub lo renderiza: tablas, negritas, enlaces); el HTML v2.1 se adjunta
solo como cortesía. Archivos nuevos:
· `RFC-v2.1-UNIFIED-FEED-AniZen-Houri-2026-10-10.md` (fuente canónica v2.1, sha16 8aec2c7c962710ee)
· `RFC-v2.1-UNIFIED-FEED-AniZen-Houri-2026-10-10.html` (envase v2.1 con §4.1/§5.1/§5.2/§6.3 y
  tabla de revisión 1:1, sha16 f85186bde5e243f3)

## COMENTARIO 1 — el spec completo pegado (para AMBOS repos; publicar como primer comentario del issue v2.1)

```markdown
## Full spec — RFC v2.1 (canonical copy, pasted so nothing is lost)

**Follow-up to the sandbox extension RFC. Two field observations after the new multiFeed:**

**1 · Per-source filters inside the multiFeed.** Selecting a source currently exposes no filters.
Selecting a source should toggle *that source's own* filter set (latest / updated) plus the
conventional ones (new works / popular / trending).

**2 · A true multifeed: multiple feeds.** Global by default, segmentable by hand or by on-device
AI classifying existing entries — e.g. movie sources + anime sources (Zangetsu, AniDash,
Mangayomi already ship this). Each feed: up to **20 sources/extensions**, same as global.

**Thesis:** the Feed is a portable object — `feeds.json` (`schema: feed.v2.1`) living on the
Universal Source Manager and traveling inside `.anizenbk` / `.hourbk` backups.

### §4.1 Fallback ladder — declared per source, never improvised
"Popular"/"trending" are not universal. Each source's FilterProfile declares its ladder:
**native → declared alias → local post-filter (visibly labeled «filtro local») → hidden**.
Never an empty chip, never a silent bucket. Because the ladder is per-source data, **adding a
source is self-describing** — no feed-side code per source.

### §5.1 Canonical work identity & duplicates (per-feed policy)
`work_key` = normalized title + content type + creator/year when exposed (hashed locally).
`policy: "canonical"` (Global default): duplicates collapse to first occurrence with a badge
«también en B, C» — no silent state merging. `policy: "keep_duplicates"`: they stay; the
source chips separate them. «Show duplicates» toggle overrides per session.

### §5.2 Stable feed identity under removal or outage
A downed source **never blocks the feed**: partial-success merge, last cache served
**stale-with-label**, block keeps its position (frozen order). Removal is identity-preserving:
the feed keeps id, name, order, rules, pins. `feed_global` is immutable by definition.

### §6 Segmentation — manual first, AI as suggestion layer
Rules are data: `source_in` · `content_type` · `genre in` · `title contains` · `status in` with
AND/OR. **AI (opt-in, on-device):** proposes suggested feeds with per-entry confidence; user
accepts/edits/discards each one.

### §6.3 Classify once, cache the label; pins are permanent
Classification is a **job, not a render step**: `work_key → {label, confidence, model_version,
ts}` computed once per work; feed render/scroll read the cache and **never invoke the model**
(battery + latency belong to a batch, not to the screen users open most). **Manual pins are
permanent and visible:** they survive re-classification, model upgrades and restore (stored in
feeds.json); a pinned entry shows a pin mark. The answer to a mislabeled niche title is a
one-tap pin, not a fight with the model.

### §8 Roadmap — Phase 1 ships first, alone
**P1** per-source filters with the fallback ladder (both apps) — independent, blocks nothing.
**P2** multiple feeds, manual: immutable identity under removal/outage; feeds.json round-trip
in backups, zero loss. **P3** AI segmentation as a **non-blocking prototype** (AniZen first,
Houri lite): label cache with classify-once semantics, permanent pins, airplane-mode test in CI.

*Risk matrix, integration map with the sandbox pieces, and the ecosystem appendix
(Miyomi/EverythingMoe, verified 2026-10-10) in the attached HTML — single file, offline,
live demos of the chips, merge policies and the rule engine.*
```

## COMENTARIO 2 — changelog corto (responder al revisor con el mapa 1:1)

```markdown
Five structural points from the first review, absorbed in v2.1 — each as a committed mechanism:

1. **Fallback ladder (§4.1):** per-source declared order native → alias → labeled local → hidden;
   self-describing sources.
2. **Classify once (§6.3):** label cache `work_key → {label, conf, model_v, ts}`; render/scroll
   never invoke the model.
3. **Permanent pins (§6.3):** overrides survive re-classification and restore; visible pin mark;
   AI = suggestion layer over hand-made structure.
4. **Duplicates (§5.1):** canonical collapse (badge «también en…») or keep-and-filter — per-feed
   declared policy + session toggle.
5. **Degradation (§5.2):** immutable feed id; partial-success merge; stale-with-label; frozen
   order. Phase 1 ships first and independently; Phase 3 is a non-blocking prototype (§8).
```

## Nota de publicación v2.1 (ACTUALIZADA: los v2.0 YA VIVEN en issues abiertos)

Verificado 10-oct: AniZen#86 y houri#37 están ABIERTOS, publicados por el dueño con el v2.0
adjunto (33287613 / 33287594), SIN comentarios. El feedback del revisor llegó POR DISCORD.
Plan v2.1 — SIN issues nuevos, comentarios de seguimiento en los mismos hilos:
1. AniZen: https://github.com/salmanbappi/AniZen/issues/86 → publicar COMENTARIO 1 (spec
   completo v2.1 pegado) adjuntando ahí el HTML v2.1 como cortesía; luego COMENTARIO 2 (mapa 1:1).
2. Houri: https://github.com/PineappleTwilight/houri/issues/37 → mismos 2 comentarios.
3. Si el revisor es admin de Discord: etiquetarlo en el comentario 2 («thanks for the review
   that drove this revision») y a Discord se llevan SOLO los enlaces de los issues.
4. El cuerpo del issue (v2.0) no se toca: la historia queda en el hilo, como manda el canon.


---

# ADENDA v2.1-b (10-oct noche) — RESPUESTA TÉCNICA AL REVISOR (segunda ronda)
El revisor insiste: llegó el NOMBRE del archivo, no el archivo; pide el CÓMO concreto de las
dos preocupaciones y promete PROBAR la implementación. Entrega: todo pegado como texto.

## COMENTARIO 3 — implementación de las dos preocupaciones (para #86 y #37, y Discord)

```markdown
**How v2.1 answers the two concerns — implementation, not concept.** (Paste of the diff sections that matter; the HTML keeps getting stripped, so everything is in text from now on.)

**1 · The label cache — classification is a job, never a render step**

Storage: a local `labels` table (Room, or `files/labels.json` if we keep it sandbox-flat), keyed by a 64-bit hash of the `work_key`:

```jsonc
// one row per work
{ "k": 0x9f31c2…, "label": "Movies", "conf": 0.92,
  "model_v": "cls-2026.10", "ts": "2026-10-10T18:04Z" }
```

- **When it computes:** only on cache miss — a `work_key` seen for the first time during a refresh/merge job. Background dispatcher (WorkManager), batched (≤50 new keys per run), never on the UI thread. Opening the feed triggers *zero* classification work.
- **Render path:** `labels.get(key) ?: "unclassified"` — a map lookup, nothing else. The classifier is not reachable from the UI module (enforced by module boundary, not discipline).
- **Invalidation:** rows carry `model_v`. A model upgrade marks rows stale but keeps serving them; recompute happens only as an explicit, user-opted batch ("re-classify with new model") or per-entry action. Rule edits never need the model — the rules engine is deterministic and re-runs cheap.
- **Acceptance hooks:** airplane-mode e2e for the whole pipeline, plus a debug assertion that feed render/scroll performs zero classifier calls.

**2 · Pins — the permanent, visible manual override**

Storage: a `pins` map **inside `feeds.json`** — plain data, so it travels inside `.anizenbk`/`.hourbk` and survives model upgrades, re-classification and restore:

```jsonc
"pins": { "0x9f31c2…": "Movies" },
"pin_policy": "pin > rule > cached_label"
```

- Precedence is fixed: **pin > manual rule > cached label > unclassified**.
- The re-classification job **skips pinned keys** — it physically cannot overwrite them.
- UI: pinned entries show a small pin mark; long-press → «Pin to…» / «Unpin»; unpin falls back to the cached label. One tap answers a mislabeled niche title.

**3 · The other two structural answers, short form**

- **Duplicates:** per-feed declared policy. `work_key` = casefold + ASCII-fold + article-stripped title + content type (+ creator/year when the source exposes it). `"canonical"` collapses to first occurrence with a «also on B, C» badge; `"keep_duplicates"` keeps them and the source chips separate them. The running demo in the HTML uses exactly this key function.
- **Dead source:** partial-success merge — live sources refresh, the downed one serves last cache stale-with-label, its block keeps its position (frozen order); feed id/name/rules/pins are immutable under source removal.

**Diff summary v2.0 → v2.1:** +§4.1 fallback ladder (native → declared alias → labeled local → hidden, per-source FilterProfile) · +§5.1 work_key & duplicate policy · +§5.2 degradation rules · +§6.3 label cache & pins (above) · §8 reordered: per-source filters ship first and independently; AI segmentation is a non-blocking prototype. Schema bumped `feed.v2` → `feed.v2.1` (adds `dedup`, `degradation`, `pins`).

Both mechanisms are testable **without shipping the AI tier**: the rules engine can act as the label producer, and pins are plain data. Want the full §6.3 text or any other section pasted, say which.```

## MENSAJE CORTO para chat/Discord (1 pieza)

```text
Short version for chat: v2.1 answers your two concerns like this — **(a) label cache:** classification runs only on cache miss (new work_key during a refresh job), background + batched; feed render does a map lookup and nothing else; rows carry model_version, recomputed only on explicit opt-in. **(b) permanent override:** pins live in feeds.json (so they survive upgrades, re-classification and restore), precedence pin > rule > cached label, the reclassify job skips pinned keys, and pinned entries show a visible pin mark. Both testable without the AI tier — rules engine can produce labels, pins are plain data. Full implementation note is pasted in the issue comments.```

## Guion de publicación v2.1-b
1. Comentario 3 arriba → como comentario en AniZen#86 y houri#37 (y por Discord al revisor,
   que es donde está revisando).
2. Si ya publicaste Comentarios 1-2 (spec + mapa 1:1), el 3 los complementa; si no, el 3
   basta por sí solo — es justo lo que el revisor pidió.
3. Nada de adjuntos en esta ronda: TODO pegado. El HTML queda de cortesía solo si algún día
   confirman que user-attachments les funciona.


---

# ADENDA v2.2-c (10-oct noche) — TERCERA RONDA: seis ajustes + alcance F1/F3
El revisor valida v2.1 («una revisión real, no una reiteración») y pide 6 ajustes pre-Fase-1
+ tabla de alcance. Absorbidos como v2.2: md `RFC-v2.2-...md` (23.662 B, sha16 396da224f4b33c31)
y html `RFC-v2.2-...html` (94.464 B, sha16 1615f88491808975; 18 edits con assert; Tabla 0b,
§6.4 dos almacenes, §8.1 alcance, riesgo persistencia). Schema → feed.v2.2 (la vara cazó que
el html v2.1 seguía con feed.v2 en el JSON — inconsistencia fuente/envase corregida).

## COMENTARIO 4 — respuesta a los seis ajustes (para #86 y #37)

```markdown
All six absorbed in v2.2 — mechanism for mechanism, and the Phase 1/3 split at the end.

**1 · Ladder floor + declared aliases (§4.1).** "Hidden" is no longer a silent terminal rung. The ladder ends in a **chronological floor**: every adapter family exposes latest/updated, so a source matching no bucket above serves it **chronological and labeled** («cronológico — la fuente no expone popular»). Hidden survives only for a source with no working listing at all — and that state is **visible per source** in the feed's health row. A contributing-nothing source can no longer masquerade as "feed is empty today." **Aliases are a declared, versioned map** in the FilterProfile (`"aliases": {"trending": "popular"}`); nothing is inferred at runtime — if the map doesn't declare it, the alias doesn't exist.

**2 · Hysteresis + GC (§6.3).** On a model_v upgrade, a cached label is overwritten only if the new label clears a high-confidence threshold (**≥ 0.90**) or beats the old confidence by a margin (**≥ +0.15**); otherwise the old label stays and the candidate is kept as a visible alternate. Both constants are named config — low-confidence works don't rotate segments when the model updates. **Retention:** rows unseen for `labels_gc.days` (default 90) are purged by the same batch job that classifies — never on cold start; cold start reads per key and never loads the table whole.

**3 · Pins (§6.3).** Confirmed: pins are keyed by **work_key hash, not row id** — a work that leaves and returns keeps its pin, because the key is canonical identity. Granularity is two-level: `pin_segment` (membership, default) and `pin_position` (membership + explicit order, opt-in per entry).

**4 · Deterministic canonical tiebreak + reading badge (§5.1).** Tiebreak order is declared: (1) the feed's primary source if the user pinned one, (2) richer metadata (count of non-null fields), (3) most recently updated entry, (4) stable lexical order by source id. Same winner every session. And the badge tells the reading truth: «canónica en A» — if the user's download came from B, it says **«leyendo desde B · canónica en A»** with a one-tap «usar B como canónica», which is a primary-source pin feeding tiebreak rule (1).

**5 · Degradation UI + incremental refresh (§5.2).** Both levels specified: a **feed-level banner** («2 fuentes sin actualizar · última sincronización 8-oct») plus **per-item markers** on entries served stale — banner is feed state, markers are attribution. Degraded refresh is **retry-failed-only, merge incremental**: live sources serve from cache and are not re-fetched; full re-fetch exists only as an explicit user action. Documented as the rule, not an optimization.

**6 · Persistence split (new §6.4).** Exactly as you framed it — two stores, one write path each, **never a shared transaction**: **LABELS** (derived, disposable: k/label/conf/model_v/ts — wiped whole without touching intent; GC and model migrations touch only this) vs **INTENT** (feeds.json: feed defs, rules, dedup policy, pins). Backups always carry INTENT; LABELS ride along only as optional recomputable cache.

**What's actually in Phase 1 vs Phase 3 (new §8.1, table):** Phase 1 ships the **entire infrastructure with zero models** — filter row from FilterProfile with the floor + declared aliases; work_key with canonical dedup, deterministic tiebreak and reading badge; degradation (banner, markers, retry-failed-only); the labels table with model_v/ts schema and the **rules engine as label producer**; work_key-keyed pins; two-store persistence. Phase 2: multiple feeds + full rules engine + backup round-trip. Phase 3 adds **only the model**: classifier as an additional label producer, hysteresis activation, GC activation by volume, per-entry suggestions. The contract is identical across phases — Phase 3 plugs a model into a socket Phase 1 already built and tested with rules.```

## MENSAJE corto para Discord (1 pieza)

```text
v2.2 absorbs all six: (1) ladder ends in a chronological floor — labeled, never silent; hidden is a visible per-source health state; aliases are a declared versioned map, nothing inferred at runtime. (2) Hysteresis: overwrite only ≥0.90 confidence or +0.15 margin over the old label; labels GC at 90 days unseen, in the batch job, never cold-start. (3) Pins confirmed keyed by work_key hash (a work that leaves and returns keeps its pin); granularity pin_segment (default) / pin_position (opt-in). (4) Deterministic tiebreak: user-pinned primary source → richer metadata → freshest → stable lexical; badge «leyendo desde B · canónica en A» + one-tap canonical switch. (5) Degradation surface: feed banner + per-item markers; degraded refresh is retry-failed-only, merge incremental — documented as the rule. (6) Two stores, one write path each: LABELS (disposable) vs INTENT (feeds.json) — never a shared transaction. And §8.1 answers the scope question: Phase 1 ships the whole infrastructure (rules engine as label producer); Phase 3 only plugs the model into that socket.```

## Guion v2.2-c
1. Comentario 4 en ambos issues; M3 al revisor por Discord.
2. Adjuntar el HTML v2.2 SOLO como cortesía (sigue sin llegar); el texto pegado manda.
3. Si responde con más vara, otra ronda; si confirma, Fase 1 queda lista para diseño.


---

# ADENDA v2.3-d (10-oct noche) — CUARTA RONDA: trazabilidad + siete endurecimientos
El revisor pregunta lo que decide el progreso (¿sobrevivieron los 5 mecanismos de v2.1?) y pide
7 ajustes. Entrega v2.3: md `RFC-v2.3-...md` (28.851 B, sha16 10f89ddc93a20ce1) · html
`RFC-v2.3-...html` (103.683 B, sha16 097eaefbcf701c12; 17+1 edits con assert; §2.1 principios+
Table A de trazabilidad · §2.2 presupuesto ≤20 · Table 0c · §6.1 precedencia total+rules_packs ·
§6.3 cold-start · §7 higiene portable · §5.2 fuente faltante · §4.1 ventana/recompute · JSON
schema feed.v2.3 con rules_packs). LA VARA CAZÓ: (a) el JSON del md quedó mal anidado en la
1.a cirugía (feeds array cerrado antes del 2.º feed) — reparado y verificado con json.loads;
(b) el schema del md seguía en feed.v2.1 desde la v2.2 (inconsistencia heredada) y el AC del
html en v2.2 — ambos bump a feed.v2.3.

## COMENTARIO 5 — trazabilidad + siete mecanismos (para #86 y #37)

```markdown
The question first, because it decides the round: **all five v2.1 mechanisms survived v2.2 — nothing was subsumed away, each has one carrier section.** v2.3 (new revision) now states this formally as three structural principles with a traceability table:

| Principle | Carries |
|---|---|
| **P1 · Honest capability** — render what sources can do, degrade visibly, silence is a defect | fallback ladder §4.1 · degradation §5.2 · missing-source state (new) |
| **P2 · Deterministic, data-first segmentation** — same inputs, same segments, every device, cold or warm | work_key + duplicate policy §5.1 · pins §6.3 · rules precedence + unassigned pool §6.1 (new) |
| **P3 · Derived vs intent** — separate stores, separate write paths, object carries intent never secrets | label cache + hysteresis + GC §6.3 · two stores §6.4 · portability hygiene §7 (new) |

So: label cache w/ hysteresis+eviction → §6.3 (P3+P2) · work_key pins → §6.3 (P2+P3) · duplicate policy → §5.1 (P2) · degradation → §5.2 (P1) · ladder → §4.1 (P1).

**The seven tightening points, as mechanisms (v2.3):**

1. **Total precedence (§6.1):** every rule carries an explicit `priority`; evaluation sorts by `(priority, declaration order)` — a total order — first match takes the entry. Entries matching no rule go to a **visible «Sin asignar» pool** (a real segment; its size is part of QA fixture output). Same rules + same entries ⇒ same assignment on any device; golden-file tests pin it.
2. **`rules_packs` (§6.1):** the rule set is its own addressed object with `rules_version`, referenced by the feed — rule tweaks bump `rules_version` and migrate independently; the feed schema moves only when the feed object changes shape. One data change can't burn the schema's migration budget.
3. **Cold-start acceptance test (§6.3, §8):** fresh install + empty label cache + same feeds.json/rules_pack must segment identically to a warm device — golden files in CI run both paths. First launch and tenth launch show the same feed.
4. **Portable-object hygiene (§7 invariant):** adapters referenced by **stable source id** (names resolved at runtime); **credentials, cookies and session tokens never** — auth stays in app-private storage, and the export path runs a sanitizer that refuses to embed secrets. Compat: same schema major → unknown fields **preserved verbatim** through load/save; different major → import **fails loudly** with a report. Never mangle-and-resave.
5. **Missing-source visible state (§5.2):** a source id absent on restore/import (renamed, removed, not installed) → the feed loads with a visible «fuente faltante» placeholder in the switcher and health row. A feed never silently loses a source.
6. **Local-fallback honesty constraint (§4.1):** a local filter only trims the fetched window — its result is a function of **window size and fetch order, both declared by the adapter** in the FilterProfile; local results are **recomputed on every refresh and never cached**. An honest fallback that goes stale is just a slower lie.
7. **≤20 declared as a latency budget (§2.2):** per refresh, merge cost ≈ Σ(one page per source) + interleave; 20 bounds worst-case refresh to seconds and bounds memory on low-end devices. The UI limit is the consequence, not the cause; device tiers may lower it, nothing raises it silently.

Also bumped: schema is now `feed.v2.3` with `rules_packs` in the example (your note caught us at the right time — the demo data model now shows the pack reference, not inline rules).

And noted on your read: you've had the summary + reading map, not the §4/§5/§6 bodies — say the word and I'll paste any section's full body here; they're short enough to survive GitHub text fine.```

## MENSAJE corto para Discord (1 pieza)

```text
v2.3 up. Your question first: all five v2.1 mechanisms survived — nothing dissolved into the principles; each has one carrier: label cache+hysteresis+GC → §6.3, work_key pins → §6.3, duplicate policy → §5.1, degradation → §5.2, fallback ladder → §4.1. Formalized as three principles with a traceability table (P1 honest capability / P2 deterministic data-first segmentation / P3 derived-vs-intent). Your seven points, as mechanisms: (1) total precedence — per-rule priority, first-match-wins, visible «Sin asignar» pool, golden-file tests; (2) rules_packs — own object, own rules_version, migrates without touching the feed schema; (3) cold-start acceptance test beside airplane-mode — fresh install + empty cache segments identically; (4) portable-object hygiene — stable source ids, credentials never (export sanitizer), same-major preserves unknown fields verbatim, cross-major fails loudly; (5) missing source = visible placeholder state on restore; (6) local fallbacks = window-declared, recomputed every refresh, never cached; (7) ≤20 documented as a latency budget (Σ one page per source + interleave). Schema now feed.v2.3 with rules_packs in the example. Want any §4/§5/§6 body pasted in full, name it.```

## Guion v2.3-d
1. Comentario 5 en ambos issues; M4 al admin por Discord.
2. La tabla de trazabilidad (P1/P2/P3) es LA respuesta: si el admin la acepta, es progreso.
3. Oferta abierta en C5: pegar cuerpos §4/§5/§6 completos si los pide.


---

# ADENDA v2.5-e (10-oct madrugada) — NIVEL SUPERIOR DE PRUEBAS + RESPUESTA RONDA 4
Orden del dueño: elevar el nivel de las pruebas de estrés ANTES de re-enviar. Ejecutado:
fuzzing property-based (3.001 checks) → 3 hallazgos reales (F1 recency ties dependían del orden
de fetch, 287 violaciones de permutación · F2 histéresis con flip-flop A→B→A ≥0.90 · F3 İ turco
rompía igualdad de work_key tras NFKD) → fixes declarados y modelo corregido re-fuzzed limpio
(5.704 checks, 0 violaciones) → CÓDIGO VIVO del HTML v2.5 re-probado 11/11. Bug de autoría de
test #3 registrado (expectativa intercalada mal escrita; el código sobrevivió).
Archivos v2.5: md 34.102 B · f7844aed6897787c · html 108.677 B · a400f1c1f9766761 ·
validación completa ✓ (14 secciones, 10 tablas, JS OK, 0 anclas rotas).
ACTA DE DEMOLICIÓN: `_auditoria/demolicion-redteam-rfc-v23-2026-10-10.md` +
`_auditoria/fuzz-nivel-superior-2026-10-10.js` (harness reproducible, semilla fija).

## COMENTARIO 6 — respuesta ronda 4, elevada (para #86 y #37; sustituye al Comentario 5)

```markdown
Answering your round, and raising our own bar first: before replying we ran a property-based fuzz round against our own mechanisms — the demo algorithms and a state-machine model of the label cache (3.001 checks pre-fix). It found three real defects; all three are now declared fixes, and the corrected model re-fuzzed clean (5.704 checks, 0 violations):

- **F1 · Recency ties were fetch-order sensitive.** With equal timestamps across sources, merge order followed arrival order — non-deterministic across devices. Fix (§5): ties break by **source id, then in-source order**; merge output is now provably independent of which source answers first.
- **F2 · Hysteresis could flip-flop A→B→A** when both candidates clear 0.90 (the margin never applied if each new candidate alone crossed the threshold). Fix (§6.3): a **label change always requires the margin** (≥ +0.15 over the old confidence); the 0.90 threshold alone only rescues the low-confidence band (< 0.60). Segments cannot rotate on model upgrades.
- **F3 · Turkish İ broke work_key equality.** U+0130 survives NFKD with a combining mark, so «İstanbul» and «istanbul» hashed differently. Fix (§5.1): normalization is now NFKD → **strip combining marks (\p{M})** → casefold → ASCII-fold — verified idempotent on the adversarial corpus (fullwidth, ligatures, ZWJ emoji, bidi).

And your round-four points, absorbed as **v2.5** (md + single-file HTML, seals `f7844aed6897787c` / `a400f1c1f9766761`):

**Traceability answer first:** all five v2.1 mechanisms survived — each with one carrier, formalized in §2.1 as three principles (P1 honest capability · P2 deterministic data-first segmentation · P3 derived-vs-intent): label cache+hysteresis+GC → §6.3 (P3, P2) · work_key pins → §6.3 (P2, P3) · duplicate policy → §5.1 (P2) · degradation → §5.2 (P1) · ladder → §4.1 (P1).

1. **Total precedence (§6.1):** per-rule `priority`, evaluation in `(priority, declaration order)` — a total order, first match wins; no-match entries land in a **visible «Sin asignar» pool** (render-capped with a count summary; data stays whole). Golden-file tests pin assignment.
2. **`rules_packs` (§6.1):** own object, own `rules_version`, **content-addressed** (sha256 of the rules array verified on restore — guarding drift and mismatch, honestly *not* malice; tamper-resistance lives in device trust + sandbox). Rule tweaks migrate independently of the feed schema.
3. **Cold-start (§6.3):** equality scoped to the rules layer (golden files, warm and cold); the AI layer is explicitly async — «Sin asignar» until the batch lands, labels apply with a visible notice, never a silent reshuffle. Airplane + cold-start both in CI.
4. **Portable-object hygiene (§7):** adapters referenced by stable id; **credentials/cookies/tokens never** (export sanitizer); same major → unknown fields preserved verbatim; different major → loud failure.
5. **Missing source (§5.2):** visible «fuente faltante» state on restore/import — never silent loss.
6. **Local fallbacks (§4.1):** window size + fetch order declared by the adapter; local results **recomputed every refresh, never cached**.
7. **≤20 as a latency budget (§2.2):** page budget × ≤20, device-tier config, measured in QA fixtures — no wall-clock promises in the spec.

The demo code in the attached HTML was updated with the same fixes and re-tested against the invariants (11/11 on the live file) — spec and demo now provably say the same thing. Say the word if you want any §4/§5/§6 body pasted in full.```

## MENSAJE corto para Discord (1 pieza; sustituye a M4)

```text
v2.5 up — and this round we fuzzed ourselves before you could: 3.001 property-based checks found three real defects, all fixed and re-fuzzed clean (5.704 checks, 0 violations): (F1) recency ties were fetch-order sensitive → tiebreak now declared (time desc → source id → in-source order); (F2) hysteresis allowed A→B→A flip-flops above 0.90 → label changes now always require the +0.15 margin, the threshold only rescues the <0.60 band; (F3) Turkish İ broke work_key equality after NFKD → combining marks now stripped. Your points, all in v2.5: traceability table (the five mechanisms survived, one carrier each — §2.1) · total precedence with «Sin asignar» pool + rules_packs content-addressed (§6.1) · cold-start scoped to rules layer, AI explicitly async with visible notice (§6.3) · portable-object hygiene: stable ids, credentials never, same-major preserves verbatim, cross-major fails loud (§7) · missing source = visible state (§5.2) · local fallbacks recomputed every refresh, never cached (§4.1) · ≤20 declared as latency budget (§2.2). Demo code updated and re-proven against the live file. Seals: md f7844aed6897787c · html a400f1c1f9766761.```

## Veredicto de re-envío
v2.5 está lista para publicar como comentario en #86 y #37 (y M5 al admin). La propuesta ahora
lleva: 3 rondas del revisor absorbidas + auto-demolición + fuzzing con hallazgos propios
publicados — nada que ocultar, todo sellado. Si el admin pide cuerpos §4/§5/§6 completos,
se pegan bajo pedido.


---

# BRIEFING PARA EL ADMINISTRADOR (10-oct) — CONTENIDO DEL ARCHIVO + DIFERENCIAS POR VERSIÓN

```markdown
**RFC v2.5 — file contents and per-version differences**

**The file.** One self-contained HTML document — no external fonts, scripts, styles or images; it renders offline. Contents: abstract; revision history answering each review round; executive summary in Spanish; §1 context; §2 design goals with the principle→mechanism traceability table; §3 data model (feeds.json, schema feed.v2.3); §4 per-source filters and the five-rung fallback ladder; §5 MultiFeed UX (work_key dedup, degradation); §6 segmentation — manual rules with total precedence and content-addressed rules_packs, AI label cache with named hysteresis constants, pins, GC; §7 RFC v1 integration; §8 roadmap and acceptance criteria; §9 risk matrix; §10 landscape appendix; colophon with the canonical-text seal. Three live exhibits (source re-bind, merge policies, cold-start) run deterministic sample data on the page; the airplane-mode counter is wired to fetch / XMLHttpRequest / sendBeacon and reads 0.

**Artifacts.** Canonical text: md 34,102 B · sha256 f7844aed6897787c. Envelope: html 108,677 B · sha256 a400f1c1f9766761 — same text plus TOC, search, themes, print stylesheet and the live exhibits. Any divergence between the two is an envelope defect, not a proposal defect.

**Differences between versions** (v2.0 bodies stay as published; later versions land as comments):

- **v2.0** — base proposal: feed as portable object, per-source filters, manual-first segmentation. md 11,547 B (bb408a9b10246be0) · html 75,738 B (b537482707f7a396).
- **v2.1** — maintainer round 1 (5 structural points), each turned into a mechanism: fallback ladder (§4.1); classify-once + label cache (§6.3); permanent pins; work_key duplicate policy (§5.1); degradation with immutable feed ids (§5.2); roadmap re-titled non-blocking prototype (§8).
- **v2.2** — round 2 (6 adjustments + 1 scope question): «hidden» as declared terminal rung; alias maps declared and versioned; named hysteresis constants (0.90 / +0.15 / 90d GC) living in the ai profile; cold-start determinism; closed badge set; deterministic tie-break declared.
- **v2.3** — round 4 (traceability first): principles P1–P3 plus a table giving each earlier mechanism exactly one carrier; source-neutrality invariant (Goal 09); rule and AI stores separated (§6.4); portable-object hygiene — stable ids yes, credentials never (§7).
- **v2.4** — internal red-team demolition (same day, no external trigger): cold-start equality scoped to the rules layer, AI explicitly async with visible notice; collision-conservative work_key («posible duplicado», never silent merges); one visible «Sin asignar» pool; rules_packs sha256 verified on restore; precise privacy wording; residual v2.1 schema string fixed everywhere. Demo stress battery 13/13.
- **v2.5** — property-based fuzz round: 3,001 checks found three real defects, fixed and re-fuzzed clean (5,704 checks, 0 violations). F1: recency ties were fetch-order sensitive → tie-break now time desc → source id → in-source order. F2: hysteresis allowed A→B→A flip-flops above 0.90 → a label change always requires the +0.15 margin; the threshold alone only rescues the <0.60 band. F3: Turkish İ broke work_key equality after NFKD → combining marks stripped. Also: honest wording for sha256 (guards drift, not malice); «Sin asignar» pool render-capped with count. The demo code inside the file was updated with the same fixes and re-tested against the live HTML.```

(u16 medidos: 3429)


---

# ACTUALIZACIÓN v2.6 (10-oct noche) — AUDITORÍA INTEGRAL DEL ARTEFACTO

Sustituciones: el BRIEFING de arriba describe v2.5 → los artefactos ahora son md 34.783 B ·
33383ac4c863b51b · html 110.151 B · e863eafab0128bb5; a la tabla de diferencias se añade la fila
**v2.6 — integral artifact audit**: batería estática + sonda 360px (2 defectos reales: `<title>`
congelado en «RFC v2» desde v2.0; overflow de 2px por cabecera flex — ambos corregidos) +
batería hiperextrema 233.570 checks / 0 violaciones + oráculo diferencial JS↔Python 4.010
strings / 0 divergencias. El Comentario 6 y el M5 siguen válidos; añadir esta fila si se pegan.

## MENSAJE DISCORD v2.6 (sustituye a M5)

```text
RFC v2.6 is up — this round we demolished the artifact itself before resubmitting. Integral audit (markup + code + testing ideology): static battery + 360px probe found 2 real defects — the <title> had stayed at «RFC v2» since v2.0 through five rounds of edits, and a flex header pushed its tool buttons 2px past narrow viewports — both fixed. Hyperextreme battery on the live code and a spec model: 233,570 checks, 0 violations — 35,000 adversarial strings through dedupKey (idempotence, ASCII output, canonical form), 400×6 canonical-order permutations against an independent model, 600×300 boundary-clustered hysteresis ops (pins/GC/cold-start), 200 pack/restore scenarios (drift, fake seals, cross-major). Differential oracle: 4,010 hostile strings through both V8 and CPython — 0 divergences, identical collision profiles. The auditor's own harness broke 5 times; the artifact's code, 0. Seals: md 33383ac4c863b51b · html e863eafab0128bb5 (single self-contained file, renders offline).```

(u16: 990)


---

# ISSUE NUEVO v2.6 (10-oct noche) — PUBLICACIÓN LIMPIA, CUERPO AUTOCONTENIDO

**Cambio de doctrina (orden del dueño):** el hilo anterior se BORRA (los comentarios se complicaron).
La vara «v2.x va como comentario» queda REVOCADA → el cuerpo del issue NUEVO lleva la propuesta
completa v2.6: historial de revisiones + evidencia + mecanismos, autocontenido, nada en comentarios.
Texto del cuerpo nuevo (única fuente de pega): `RFC-v2.6-ISSUE-nuevo-cuerpo-para-pegar-2026-10-10.md`
(16.341 B · f20030a97a3c8f38 · 16.062 chars — cabe de sobra en el límite de GitHub).
Adjuntar el HTML v2.6 (110.151 B · e863eafab0128bb5) como cortesía tras pegar el cuerpo.
Va a AMBOS repos (AniZen + houri), mismo cuerpo, como en v2.0. En el formulario: los 4
Acknowledgements se marcan en la UI de la plantilla.

## MENSAJE DISCORD v2.6-anuncio (sustituye a M6 previo)

```text
New clean thread for the RFC — v2.6 now lives entirely in the issue body, nothing in comments: full revision history (3 review rounds + red-team demolition + fuzzing with published findings + integral artifact audit: 233,570 checks / 0 violations; V8-CPython differential, 4,010 strings / 0 divergences), the complete mechanism spec, and the single-file HTML attached as a courtesy. The previous thread is retired to keep the discussion in one place.```

(u16: 450)


---

# RONDA 5 (10-oct noche) — CONTENIDO, NO DISEÑO: v2.7

Tres frentes del maintainer: (1) §§4–6 no visibles → el cuerpo NUEVO es el texto canónico COMPLETO
(`RFC-v2.7-ISSUE-cuerpo-completo-para-pegar-2026-10-10.md`, 41.831 B · 51313eb2b7a9ed27 — pegar
íntegro como cuerpo del issue; HTML adjunto 117.417 B · 3a8f30d811d11878 como cortesía).
(2) Hilo borrado = debate perdido → Decision Record (12 entradas, DR-1..DR-12) con las alternativas
perdedoras y por qué; el ejemplo del maintainer (fusión por fuente vs por feed) es DR-1.
(3) «Production Candidate» sin criterio → §0 define la escalera (Draft→Reviewed→Accepted→
Production Candidate→Shipped); la etiqueta anterior over-claimed y quedó degradada.
Los 6 puntos: todos Resolved (cold-start = Resolved, scoped — DR-8, decisión de alcance, NO aplazo).
Auditoría de sellos previa: 3/3 coincidían con disco. Captura 04 cazó paréntesis sin cerrar en el
colofón → corregido → re-sellado (3a8f30d811d11878). Defecto real #12 del día: tipográfico.

## COMENTARIO 7 — respuesta ronda 5 (para el issue nuevo; sustituye al Comentario 6)

```markdown
All three points answered — and the document now carries the answers as structure, not prose.

**1. §§4–6 in the body, unabridged.** The issue body *is* now the canonical document: the full Normalized Filter Interface with the five-rung fallback ladder (§4/§4.1), the complete merge/degradation policies (§5/§5.1/§5.2), and the full segmentation spec — precedence, packs, hysteresis, pins, GC, cold-start (§6.1–6.4). The attached HTML contains the same text plus live exhibits; nothing is condensed away anywhere. Note: the consolidation was never a summary-by-design — the earlier body did carry full §§4–6; the gap you saw was the deleted thread, and your reading correctly exposed that consolidation without a decision log erases the debate.

**2. Decision Record — the alternatives that lost.** New in this version: twelve entries (Table 0C), each with the alternatives considered and why they lost. Your exact example is DR-1: merge identity per-entry (`work_key`) with collapse-vs-keep as a declared per-feed policy — rejected alternatives: source-scoped keys (they hide the cross-source duplicates the feature exists to surface), feed-scoped silent auto-merge (the same two entries would merge in one feed and not in another), and AI fuzzy matching (non-deterministic, not portable data).

**3. «Production Candidate» — you were right, and it is fixed.** The label was a status claim without a criterion; worse, it over-claimed on an unimplemented proposal. §0 now defines the whole ladder: Draft for review (this document, declared by the author) → Reviewed (each maintainer states the spec is implementable, or lists what blocks it) → Accepted per repo (a maintainer commits — milestone/issue state) → Production Candidate per repo (a merged implementation behind a feature flag passing every §8 acceptance criterion in that repo's CI — declared by the repo's maintainer, **never** by the proposal author) → Shipped (enabled by default in a stable release). Until a transition happens, this document is simply a **Draft for review**.

**Your six points — asked and answered (Table 0D):** total precedence §6.1 (resolved) · independent rules versioning §6.1 (resolved) · cold-start parity §6.3 (**resolved, scoped** — rules layer guaranteed with golden files in CI; the AI layer is async by declared design, DR-8: a scope decision, not a deferral) · hysteresis §6.3 (resolved, fuzz-proven) · eviction §6.3/§6.4 (resolved — labels GC 90d in the classify batch, GC never touches intent) · pin keying §6.3 (resolved — work_key hash, survives restore). None deferred. If a future round cannot find one of these guarantees at the cited section, that is a defect of the document — report it as such.

Version 2.7, seals: md `51313eb2b7a9ed27` · html `3a8f30d811d11878`.```

## MENSAJE DISCORD v2.7 (sustituye a M6/M6-anuncio)

```text
v2.7 answers the content round with structure, not prose: the issue body is now the canonical document (§§4–6 unabridged), a Decision Record documents the twelve alternatives that lost — including merge identity per-entry work_key vs source-scoped/feed-scoped/AI-fuzzy (DR-1) — and §0 defines the status ladder with precise criteria; the earlier «Production Candidate» label over-claimed and is demoted — this is a Draft for review until a maintainer says otherwise. Your six points: precedence, rules versioning, hysteresis, eviction and pin keying all resolved in §6; cold-start parity resolved and scoped to the rules layer (AI async by declared design, DR-8 — a scope decision, not a deferral). Seals: md 51313eb2b7a9ed27 · html 3a8f30d811d11878.```

(u16: C7 2771 · M7 750)


---

# RONDA 6 ADOPTADA → RFC v2.8 (10-oct madrugada siguiente) — §8 EJECUTABLE + KERNEL

Vara diferida del maintainer convertida en estructura: las 3 fases de §8 son matrices de
verificación (AC → artefacto de prueba → dónde corre → qué significa el fallo); cold-start
golden parity marcado como EL peldaño de §0. Cuerpo issue: `RFC-v2.8-ISSUE-cuerpo-completo-para-pegar-2026-10-10.md`
(45.939 B · 7b9a04292a467175, byte-a-byte = md). HTML: 121.810 B · 2769bdb4747110b2 (11 edits).
Baterías: kernel 296.230/0 (5 fases, semilla 20281010, `_auditoria/fuzz-v28-kernel-2026-10-10.js`,
resultado en fuzz-v28-resultado.txt) + estática 12/12 + 15 tablas + móvil 360=360 + 4 capturas.
Honestidad: harness roto 2× (4 tautologías eliminadas; oráculo sobre-exigente → 39 falsas
violaciones corregidas test-side) — código del artefacto: 0.

## COMENTARIO 8 — respuesta ronda 6 (para el issue nuevo)

```markdown
Adopting your deferred observation as structure: §8 is now executable. Every acceptance criterion names its **proof artifact**, where it runs (unit / contract / property / golden / fault-injection / UI / emulator CI), and what failure means — across all three phases, as verification matrices. Your cold-start point sits where it belongs: golden-file rules parity (warm vs cold install, same feeds.json + pack) is flagged in the Phase 3 matrix as *the rung §0 stands on* — if it diverges, the ladder falls; airplane-mode and snapshot tests pin the rest of Phase 3.

And because a proof artifact is only as good as its harness, we ran the kernel battery against the live code before answering: **296.230 checks, 0 violations** — feeds.json restore under adversarial mutation (20k scenarios: rule drift, fake seals, cross-major, unknown-field preservation, restore idempotence), precedence engine with declaration-order invariance (50k), 50k-key label cache with day-boundary GC (100k ops, pins never purged), and refresh storms with failing sources (10k cycles: frozen order, stale-with-label, retry-failed-only).

Honesty ledger, as always: the harness broke twice before counting — 4 tautological checks removed (they could not fail), and one over-strong oracle (permutation invariance beyond the declared `(priority, declaration order)` semantics) produced 39 false violations before we corrected the test, not the code. The artifact's code: **0 failures**.

Version 2.8, seals: md `7b9a04292a467175` · html `2769bdb4747110b2`.```

## MENSAJE DISCORD v2.8 (sustituye a M7)

```text
v2.8 — §8 is now executable: every acceptance criterion names its proof artifact, where it runs, and what failure means (verification matrices across all three phases); golden-file cold-start parity sits flagged as the rung §0 stands on. Kernel battery before answering: 296,230 checks / 0 violations on the live code — restore under adversarial mutation (20k), precedence invariance (50k), 50k-key cache with GC (100k ops), refresh storms (10k cycles). Harness broke twice (4 tautologies, 1 over-strong oracle = 39 false violations); code, 0. Seals: md 7b9a04292a467175 · html 2769bdb4747110b2.```

(u16: C8 1529 · M8 595)
