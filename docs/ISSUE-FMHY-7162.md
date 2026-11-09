<!-- enviado como issue real: https://github.com/fmhy/edit/issues/7162 · abierto el 2026-11-09 · HTTP 201 -->

# Proposed addition: extension index repositories (Mihon / Aniyomi / Mangayomi / LNReader / Aidoku / Suwayomi)

Hi, and thanks for the wiki. I read `docs/other/contributing.md` before writing this: I know site
submissions normally go through Discord first and that you check every link yourselves, and that
issues are the easier route than a PR. This is an **issue on purpose** — I am not opening a PR
against `docs/`.

## What this is

A set of **software repositories that publish extension indexes**, not content sites. Each of them is
the address a user pastes into the "extensions / repositories" menu of an open-source reader
(Mihon, Aniyomi, Mangayomi, LNReader, Aidoku, Suwayomi, Kotatsu…). They are the executable half of
those readers: the index decides which code runs inside the app.

I measured all of them against the public GitHub API on **2026-11-08/09** so the numbers below can be
re-checked, not taken on trust. Every row lists: interface it serves, stars, last push, and whether
the index declares a signing key.

## Which ones actually declare a signing key (measured)

Only one of the six indexes I opened has a `signingKey` field:

| Index | File | Extensions in the index | Declares `signingKey` |
|---|---|---|---|
| keiyoushi | `keiyoushi/extensions`, branch `repo`, `index.json` | **1,554** | **yes** (64 hex) |
| Mangayomi | `kodjodevf/mangayomi-extensions`, `index.json` | **363** | no |
| Tachiyomi (legacy) | `tachiyomiorg/extensions`, `repo`, `index.min.json` | 4 | no |
| Aniyomi | `aniyomiorg/aniyomi-extensions`, `repo`, `index.min.json` | 3 | no |

Two routes that circulate widely return **404** today: `inkdex.github.io/extensions/index.min.json`
and `aidoku-community.github.io/sources.json`. If a wiki entry ever pointed at those, it would now be
dead.

## Suggested entries

Most of these are already inside the wiki's reading/manga sections under some form; the ones I could
not find at all in `single-page.md` are marked **not currently listed**.

| Repository | Serves | ★ | Last push | License |
|---|---|---|---|---|
| `Aidoku-Community/sources` | Aidoku (iOS) | 623 | 2026-11-08 | Apache-2.0 |
| `Suwayomi/tachiyomi-extension` | Suwayomi | 344 | 2026-11-07 | Apache-2.0 |
| `TheNetsky/netskys-extensions` | Mihon/Aniyomi | 251 | 2026-11-09 | not declared |
| `yuzono/cursed-manga-extensions` | Mihon | 224 | 2026-11-09 | Apache-2.0 |
| `Secozzi/aniyomi-extensions` | Aniyomi | 130 | 2026-09-20 | Apache-2.0 |
| `Bas1874/Seanime-Marketplace` | Seanime | 115 | 2026-11-09 | NOASSERTION |
| `Spithskia/Shiru-Extensions` | Shiru | 93 | 2026-10-16 | GPL-3.0 |
| `Swakshan/mangayomi-swak-extensions` | Mangayomi | 53 | 2026-10-24 | Apache-2.0 |
| `salmanbappi/extensions-repo` | Aniyomi | 52 | 2026-11-08 | not declared |
| `mochi-plugins/repository` | Mihon | 50 | 2026-09-13 | GPL-3.0 |
| `FelipeGFA/extensoes` | Aniyomi | 44 | 2026-09-28 | not declared |
| `Spyou/zangetsu-providers` | Zangetsu | 36 | 2026-09-19 | not declared |
| `Schnitzel5/ApkBridge` | Mangayomi | 36 | 2026-02-11 | Apache-2.0 |
| `IReaderorg/IReader-extensions` | IReader | 32 | 2026-10-27 | MPL-2.0 |
| `inkdex/extensions` | Mihon | 32 | 2026-11-03 | not declared |
| `Mallyd11/mangayomi-anime-extensions` | Mangayomi | 28 | 2026-11-01 | Apache-2.0 |
| `NovelSourcery/extensions` | LNReader | 21 | 2026-10-28 | not declared | **not currently listed**
| `Moomooo95/moomooo95-extensions` | Mihon | 20 | 2025-05-21 | GPL-3.0 |
| `Shebyyy/kotatsu-multi-parsers` | Kotatsu | 19 | 2026-10-21 | not declared |
| `dannovels/novel-extensions` | Dantotsu | 17 | 2025-01-05 | not declared |
| `gato404/kegareta-sauces` | Mihon | 14 | 2025-07-22 | Apache-2.0 |
| `Gekkoushi/plugin` | (plugin index) | 11 | 2026-09-13 | not declared |
| `marbou92/MHRepo` | Aniyomi | 8 | 2026-11-08 | Apache-2.0 |
| `Schnitzel5/mangayomi-custom-buttons` | Mangayomi | 6 | 2025-10-05 | MIT |
| `bluecxt/anime-extensions-french` | Aniyomi | 5 | 2026-11-06 | Apache-2.0 |
| `rurin1x/animetosho-shiru-extension` | Shiru | 4 | 2026-05-21 | GPL-3.0 |
| `bunoriapp/extensions` | LNReader | 1 | 2026-10-18 | GPL-3.0 |
| `bunoriapp/LNCrawlerSources` | LNReader | 0 | 2026-09-11 | Apache-2.0 |

Source of the list: the public index at `https://miyomi.app/api/extensions` (47 entries, 39 with a
GitHub repo), minus everything already present in `single-page.md`.

## Two things I would flag as useful for readers

1. **"Does the index declare a signing key?" is a verifiable yes/no**, unlike "is the app good". It
   takes one `curl`. Out of six indexes I opened, exactly one declares it.
2. **The `lang` field is not trustworthy.** Keiyoushi's `index.json` has no language field at all
   (1,554 extensions, language only inferable from package names), and Mangayomi uses both `pt-br`
   and `pt-BR` as if they were different languages. Any table counting "languages supported" from
   these indexes will be wrong.

## What I am not asking for

Not asking to list content sites, mirrors, or anything that streams copyrighted material — the
entries above are **index repositories for open-source readers**, and whether any extension's target
site is legal is up to the reader, not to the wiki.

Happy to split this into smaller issues, add entries one at a time, or drop the ones you consider out
of scope. If Discord is the right place, tell me and I will go there instead.

---

*Measured with the public GitHub API on 2026-11-08/09. The JSON with every field —stars, forks,
license, archive status, last push, release count, assets, and whether the last release ships
checksums— is public at `https://github.com/Alex17273747576777/la-bandita-archivo` under
`docs/CENSO-MIYOMI-2026-11-09.json` and `docs/INDICES-2026-11-09.md`.*
