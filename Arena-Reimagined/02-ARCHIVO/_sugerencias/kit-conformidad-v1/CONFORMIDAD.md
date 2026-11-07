# Conformance Kit v1 — RFC v2.9 §8 (shipped proof artifacts)

The §8 verification matrices name their proof artifacts. This kit **ships** the ones that are
spec-side by nature: the property, tamper and fault-injection harnesses, with fixed seeds and
zero dependencies (Node ≥ 18, no packages).

## Run

```bash
node kit-conformidad-v1/run-all.js
```

Exits non-zero on any violation. Each harness re-extracts the demo algorithms from the live
RFC HTML file (single source of truth) before hammering them.

## Manifest — AC ↔ check ↔ last measured result

| Kit ID | Harness | What it proves (§8 AC) | Seed | Last run | Result |
|---|---|---|---|---|---|
| K1 [1] | K1-spec-model.js | Dedup `work_key`: idempotence, ASCII output, canonical form over adversarial strings (Phase 1 — dedup AC) | 20261010 | 2026-10-11 | within totals below |
| K1 [2] | K1-spec-model.js | Merge order invariant under source-order permutations vs independent canonical model (Phase 1 — merge AC) | 20261010 | 2026-10-11 | ✓ |
| K1 [3] | K1-spec-model.js | Hysteresis precise rule at boundaries; pins above classifier; GC never eats pins; cold-start consistency (Phase 3 — classify/pins/GC ACs) | 20261010 | 2026-10-11 | ✓ |
| K1 [4] | K1-spec-model.js | rules_packs tamper matrix: drift, fake seal, cross-major fail loudly; clean restores; same-major preserves unknown fields (Phase 2 — packs AC) | 20261010 | 2026-10-11 | ✓ |
| K2 [A] | K2-kernel.js | feeds.json restore under adversarial mutation, 20k scenarios: drift / fake seals / cross-major / unknown-field preservation / restore idempotence (Phase 2 — zero-loss round-trip AC) | 20281010 | 2026-10-11 | ✓ |
| K2 [B] | K2-kernel.js | Rules engine: `(priority, declaration order)` total order, first match wins, «Sin asignar» pool, declaration-order invariance — 50k evaluations (Phase 2 — precedence AC) | 20281010 | 2026-10-11 | ✓ |
| K2 [C] | K2-kernel.js | Label cache 50k keys with day-boundary GC, 100k ops; pins never purged; GC never touches intent (Phase 3 — eviction AC) | 20281010 | 2026-10-11 | ✓ |
| K2 [D] | K2-kernel.js | Refresh storms with failing sources, 10k cycles: frozen order, stale-with-label, retry-failed-only; relative order of live items preserved (Phase 2 — degradation AC) | 20281010 | 2026-10-11 | ✓ |
| K2 [E] | K2-kernel.js | Live demo code equivalence: the HTML's own `dedupKey`/merge under adversarial corpus + 200×6 permutations | 20281010 | 2026-10-11 | ✓ |

**Last full-kit run: 529.800 checks · 0 violations** (K1 233.570 + K2 296.230), 2026-10-11.

## Scope honesty

UI suites, screenshot CI, golden-file jobs and emulator airplane runs are **implementation-side
artifacts**: they belong to each repo's CI and cannot ship inside a specification. §8 declares
them; this kit ships everything that a spec *can* ship. An implementer reproducing this kit's
numbers has proven the algorithmic layer of the acceptance criteria before writing a line of app
code.
