<!-- respuesta enviada a nbats (issue 7162, comentario 6740801821) · 9-nov-2026 -->

Fair question — I should have been clearer. **Not a new section.** Here's what I'd actually suggest, based on how you already do it:

## Option A (my preference): keep them inline, where they already are

Your wiki already lists extension repos **next to the app**, and that's the right place — the user is
already looking at the reader when they need the repo URL:

```
* ⭐ **Mihon** - Manga Reader / [Extensions](...), [2](...), [3](...), [4](...) / ...
```

So this isn't a new section. It's the same pattern, and it's mostly **already done** for Mihon.

## Option B: a notes page, like `movie-web-sources.md`

You already keep a note file for exactly this kind of thing:
`docs/.vitepress/notes/movie-web-sources.md`, linked from `video.md` as "extra sources". Same pattern
would work here: one note page for extension repositories, linked from the reader entries with one
"[Repos]" link. I'd be happy to write that file in your format and open a PR — you decide if it's
worth its own page.

## The actual gap I found (measured, not guessed)

I grepped `single-page.md` for each reader name:

| Reader | Mentions in the wiki today | Extension repos linked |
|---|---|---|
| Mihon | 12 | 4 |
| Aidoku | 5 | 1 |
| Mangayomi | 7 | Discord only |
| Kotatsu | 4 | — |
| Dantotsu | 4 | "Extension Guide" |
| LNReader | 3 | — |
| Kavita | 2 | — |
| **Aniyomi** | **0** | — |
| **Shiru** | **0** | — |

So the honest answer is: **Mihon is covered, Aniyomi is missing entirely**, and the rest is
half-covered. Not "add 28 rows", which would be spam — a handful, at most.

## The handful I'd actually defend

Only ones that were pushed in the last 60 days, are not archived, and sit above 20 stars:

| Repo | Serves | ★ | Last push |
|---|---|---|---|
| `Aidoku-Community/sources` | Aidoku | 623 | 2026-11-08 |
| `Suwayomi/tachiyomi-extension` | Suwayomi | 344 | 2026-11-07 |
| `TheNetsky/netskys-extensions` | Mihon / Aniyomi | 251 | 2026-11-09 |
| `Secozzi/aniyomi-extensions` | Aniyomi | 130 | 2026-09-20 |
| `Swakshan/mangayomi-swak-extensions` | Mangayomi | 53 | 2026-10-24 |
| `NovelSourcery/extensions` | LNReader | 21 | 2026-10-28 |

That's six. If you only want one, make it **`Suwayomi/tachiyomi-extension`** — Suwayomi is already in
`reading.md` under Manga Readers, the repo ships the "Mihon extensions" compatibility layer, and
today that page only links `keiyoushi.github.io`.

## And one thing worth adding regardless of what you decide

**`signingKey` is a verifiable yes/no, and it's a one-line curl.** I opened six indexes:

| Index | Extensions | Declares `signingKey` |
|---|---|---|
| keiyoushi/extensions | 1,554 | **yes** (64 hex) |
| kodjodevf/mangayomi-extensions | 363 | no |
| tachiyomiorg/extensions | 4 | no |
| aniyomiorg/aniyomi-extensions | 3 | no |

Two widely-circulated URLs are **dead** as of today: `inkdex.github.io/extensions/index.min.json` and
`aidoku-community.github.io/sources.json` both return 404. If anything in the wiki pointed at those,
it's now broken.

Also, a warning for anyone counting: **don't count extensions from `index.min.json`**. Keiyoushi's
`index.min.json` has 2 entries; its `index.json` has 1,554. And the `lang` field is unusable —
keiyoushi's index has no language field at all, and Mangayomi uses both `pt-br` and `pt-BR` as if they
were different languages.

Tell me A or B and I'll do the work in whichever shape you want. If it's a PR, I'll keep it to the six
above and nothing else.
