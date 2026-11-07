# NLnet · borrador para que lo presentes tú

> **Cómo usar este archivo.** El formulario de NLnet exige **inglés**, respuestas breves y tu propia
> voz. Aquí está todo redactado en inglés, con los límites de caracteres respetados, y marcado con
> `[[…]]` lo que solo tú puedes rellenar. Copia, pega, cambia lo que suene a otro, envía.
> **Plazo: 3 de noviembre de 2026, 12:00 CET. No lo envío yo.**
> Política de IA de NLnet: si usaste IA para escribir la propuesta, hay que entregar los prompts.
> El registro está en `docs/NLNET-REGISTRO-PROMPTS.md`, listo para adjuntar.

---

## Fund
`Other / open call` — el proyecto es documentación verificable + herramientas de verificación, no
encaja limpio en Restack ni en CodeSupply. *([[Confirmar al abrir el formulario]])*

## Proposal title
**La Bandita: a dated, auditable registry of the free Android ecosystem, in Dominican Spanish**

## Project website(s) / repositories
`https://github.com/Alex17273747576777/la-bandita-archivo`

## Summary (max 1.000 characters)

La Bandita is a personal, non-commercial project that publishes guides, in Dominican Spanish, about
free and open-source software for Android: 112 WhatsApp pieces and 147 Facebook pieces, each with a
verification date and evidence. Underneath the writing there is a registry of 6,826 repositories,
measured against the GitHub API, with the raw API payload stored and hashed per record. 78.8% of
those repositories declare no licence at all, which is the gap this work addresses.

We ask funding to finish three things: make the registry re-measurable end to end, publish it as a
read-only MCP server so any assistant can query dated facts instead of guessing, and make every
record attestable (Software Heritage identifiers and signed batches). Duration 6 months, one person.

*(~1.000 caracteres exactos; recortar si el formulario es estricto)*

## Proposed effort (max 4.000 characters)

**Requested: €14,000** (first grant). One person, 6 months, part-time, ~360 hours.

Rate used: **€35/hour** — self-employed rate for the Dominican Republic, below the European
equivalent for the same skill.

| Task | Hours | Detail |
|---|---|---|
| Registry re-measurement, end to end | 120 | Finish the resumable measurement pipeline (6,826 records), handle API quotas and rate limits, re-verify activity and licence for every record, publish a dated snapshot |
| MCP server to production quality | 100 | Contract tests, freshness semantics (a stale answer must say "stale" with its age), packaging, CI, installation guide |
| Licence verification by text | 80 | 1,300+ repositories where the API returns NOASSERTION or nothing: read the actual licence file, record SPDX or a signed absence |
| Provenance: Software Heritage + signed attestations | 40 | Archive each cited revision, store its SWHID, sign batch attestations in CI |
| Methodology documentation, citable | 20 | A short technical paper describing the verification method, its failure modes and its limits |

**Expenses: €0.** Infrastructure runs on free tiers (GitHub Actions, static files, public APIs). No
servers, no hardware, no travel.

**What the money buys that does not exist today:** the difference between a blog with good
intentions and a registry that can be checked by a stranger. Today the checks are run by hand; with
this work they run in CI, and the evidence is stored next to the claim.

## What is new compared to other efforts (max 4.000 characters)

There are excellent curated lists of Android software (Awesome-Android, FMHY, the Shizuku
communities) and excellent package metadata services (libraries.io / Ecosyste.ms, deps.dev, OpenSSF
Scorecard). La Bandita is neither, and it does not try to replace them.

**What the lists do:** they recommend. They are useful and mostly unmaintained at the edges: in the
list used for our last discovery run, 42 of 1,273 cited repositories were already dead (HTTP 404).

**What the metadata services do:** they describe packages and their dependency chains, in English,
for developers. They do not answer the question a neighbourhood user asks: *"is this app safe to
install, who maintains it, and when was that true?"*

**What La Bandita does differently:**

1. **Every claim carries a date.** A record without `measured_at` is invalid by schema, not by
   convention.
2. **The raw evidence is stored.** Each record keeps the hashed API payload it was built from, so a
   third party can recompute the hash.
3. **Licence absence is recorded as absence.** 5,381 records say "no licence declared" instead of
   leaving the field empty or guessing from the project name.
4. **HTTP semantics are respected.** 403 and 429 are quota, never death; 404 is death; 451 is
   blocking. Most crawlers get this wrong and quietly mark live projects as dead.
5. **It is in Dominican Spanish**, for a public that the English-language tooling does not reach.
6. **It is queryable by machines** through MCP, with the same dates attached.

**Contributing instead of competing:** the pipeline consumes the official GitHub API, F-Droid's
signed index, Software Heritage, and Ecosyste.ms as secondary sources. Where a project already
answers a question well, we link to it. The gaps we fill are dating, evidence and language.

*(Also considered: publishing inside an existing awesome-list. Rejected because those lists have no
schema, no dates and no verification gate: contributing there would not have produced the registry.)*

## Technical challenges (max 4.000 characters)

1. **Quota arithmetic against a shared public API.** 5,000 authenticated calls per hour, and a
   record needs between one and four calls. Resumability is not optional: the pipeline must survive
   an interrupted run and never re-measure what it already measured today.
2. **Distinguishing "dead" from "rate-limited".** A naive crawler marks thousands of live projects
   dead by treating 429 as 404. Our gate refuses to accept a record that declares `dead` on 403/429.
3. **Licence truth.** GitHub's `license` field is often NOASSERTION even when a licence file exists,
   and sometimes the licence is only declared in the README. The method is ordered: SPDX → licence
   endpoint → licence file text → signed absence. Each step needs its own evidence.
4. **Immutable provenance.** A commit hash is only stable while the host keeps it. We archive cited
   revisions in Software Heritage and store the SWHID; Software Heritage's anonymous quota (HTTP
   429) is the practical bottleneck, so the pipeline must record the failure as a state, not as a
   silent gap.
5. **Machine-readable honesty.** Any MCP server can answer fast. The hard requirement is that it
   answers *"this fact is 180 days old"* instead of answering as if it were current. That is a
   design constraint that has to be tested, not documented.
6. **Verification that fails loudly.** Gates that pass because they exited with code 0 are worse than
   no gates. Our CI requires the literal string `fallos: NINGUNO` in the report, and a self-test
   breaks a fixture on purpose for every gate to prove it detects the violation (8/8 today).

## Ecosystem and users (max 2.000 characters)

**Users:** (a) Spanish-speaking Android users in the Dominican Republic and the Caribbean, where
92.7% of households have a mobile phone and only 56.2% have fixed broadband, so the phone is the
only computer; (b) moderators and contributors of Spanish-language tech communities who need a citable
source; (c) any AI assistant connected through MCP that needs dated facts about Android projects
instead of generated ones.

**Dependencies:** the project depends on the GitHub API (primary), F-Droid's index, Software
Heritage and OpenSSF Scorecard. It does not fork or duplicate any of them.

**Relationships to build:** the Shizuku/Dhizuku community (the subject matter of many pieces), the
Spanish-language FOSS community, and the maintainers of the projects we measure — every measured
project has a right of reply and a published errata path.

## Background (max 2.000 characters)

[[PERSONALIZAR: aquí va tu voz. Lo que sigue es un borrador en primera persona: cámbialo hasta que
sea tuyo.]]

I am a self-taught writer from the Dominican Republic. I have been publishing this archive for over a
year, in Spanish, for people who cannot read English documentation and cannot afford to install the
wrong thing. I wrote 112 WhatsApp pieces and 147 Facebook pieces, and I built the tooling that dates,
measures and seals them, because after a while I stopped trusting my own notes.

I have no institutional backing and no funding history. What I have is a method that already caught
its own author: in October 2026 the registry had been reporting 573 repositories for weeks when the
real count was 5,684 — a CSV quoting bug — and the published correction says so, with the failing
line numbers and the fix. I think that is the most useful thing in the repository: not that it is
right, but that it shows how it fails.

I am also chronically ill ([[decidir si lo mencionas: es verdad y explica por qué el proyecto avanza
a su ritmo]]), which is why the project is designed to run on small, resumable, verifiable steps
instead of sprints.

## Other funding sources (max 1.000 characters)

None. The project has never received money, grants or sponsorship, and it does not accept them: no
advertising, no paid services, no donations that could buy influence. All infrastructure runs on free
tiers. If funded, the grant would be the only income of the project.

## AI disclosure

- **Did you use generative AI in writing this proposal?** Yes.
- **Model:** an assistant on Arena.ai (Agent Mode, which routes across several models including
  Claude, GPT, Gemini and others), used for drafting, for organising measurements and for reviewing
  code.
- **What it was used for, and what it was not:** the assistant wrote code, ran measurements and
  drafted text. It did not decide what gets recommended, and it did not sign anything. Every number
  in this proposal comes from a file in the repository that can be re-measured.
- **Prompts:** attached in full as `NLNET-REGISTRO-PROMPTS.md`.
- **Does the codebase contain AI-generated code?** Yes, substantially — the Python tools and the
  schema were written with the assistant. The method, the rules and the editorial voice are the
  author's.
- **High-level description (max 1.000 chars):** the AI is used as a fast typist and a patient
  reviewer: it writes candidate code and candidate prose, measures APIs, and flags inconsistencies.
  Human judgement decides what is published, what is recommended and what is retracted. Every
  published claim carries a date and a stored payload precisely because the author does not trust
  the tool that produced it.

## Contact information

- **Name:** [[tu nombre o seudónimo]]
- **Email:** [[tu correo]]
- **Phone:** [[con código de país, +1 809 …]]
- **Type of applicant:** `Individual`
- **Name of organisation:** — (ninguna)
- **Country:** `Dominican Republic`

---

## Antes de enviar: lista de verificación

- [ ] Leer el borrador en voz alta y cambiar toda frase que no suene a ti.
- [ ] Completar los `[[…]]`.
- [ ] Decidir si mencionas la enfermedad en Background (es verdad; ayuda a explicar el ritmo).
- [ ] Adjuntar `docs/NLNET-REGISTRO-PROMPTS.md`.
- [ ] Revisar el tope de caracteres de cada campo en el formulario real.
- [ ] Enviar antes del **3 de noviembre de 2026, 12:00 CET**.
