# Reparto de las 40 piezas · recursos nuevos (P07)

*8–9 de noviembre de 2026 · de dónde sale cada tema y con qué se mide*

## De dónde salen los recursos

Tres fuentes, las tres auditables:

1. **fmhy.net** — 16 páginas leídas, **2.073 enlaces externos** en `/mobile` sola, y **3.284 repositorios de GitHub distintos** entre todas. De ellos, **3.125 que este archivo nunca había medido**. Censo en `CENSO-FMHY-2026-11-09.json`.
2. **miyomi.app** — su API pública devuelve **47 índices** de extensiones (39 con repositorio). 8 ya estaban en el registro y apenas 2 coincidían con el censo de fmhy: son fuentes que no se solapan. Censo en `CENSO-MIYOMI-2026-11-09.json`.
3. **Los seis índices de extensiones** abiertos y contados en `INDICES-2026-11-09.md`.

Los temas **no se inventan**: salen de las secciones reales de fmhy.net (74 secciones en `/mobile`, y las de `/system-tools`, `/file-tools`, `/internet-tools`, `/text-tools`, `/image-tools`, `/developer-tools`, `/linux-macos`) agrupadas por lo que la serie ya venía midiendo.

## El reparto

| Pieza | Tema | Secciones de fmhy.net de donde salen los recursos | Repos nuevos disponibles |
|---|---|---|---|
| 01 | La huella o el silencio | cifras de toda la serie; el censo nuevo da la muestra | 3.125 |
| 02 | La música que no se cae | Linux Audio · Android Audio · Audio Streaming · Audio Editing | 227 |
| 03 | La caja fuerte del bolsillo | Password Privacy / 2FA · Encryption / Certificates | 105 |
| 04 | La lista del permiso | Android Privacy · Android Adblocking · Privacy Tools | 219 |
| 05 | La guía maestra | todas (es la suma de la serie) | 3.125 |
| 06 | El taller de los parches | App Patchers & Modifiers · Android Utilities | 131 |
| 07 | La pantalla grande | Android TV / Firestick · Media Center · Casting | 79 |
| 08 | La red: seis caminos | VPN · Proxy Clients · DNS Adblocking · Firewall | 219 |
| 09 | Archivos, copias y nubes | File Managers · File Transfer · Backups · Selfhosting | 247 |
| 10 | Las tiendas de extensiones | los seis índices medidos + extensiones / lectores | 253 |
| 11 | Las aplicaciones que leen | Android Reading · iOS Reading · Manga / Anime apps | 253 |
| 12 | El kit de reemplazo | Downloading · File Tools · Video Tools | 218 |
| 13 | El audio que faltaba | Audio Streaming · Podcasts · Music Libraries | 227 |
| 14 | Spotify sin Spotify | Android Audio · Linux Audio · Audio Streaming | 227 |
| 15 | Descargar es un acto técnico | Download Managers · Video Download · Debrid | 218 |
| 16 | El torrent que no se rinde | Torrent Apps · Remote Torrenting · Trackers | 93 |
| 17 | El teclado que escribe por ti | Keyboard Tools · Input Methods | 81 |
| 18 | La radio y el directo | IPTV Players · Radio · Live Streaming | 89 |
| 19 | La tienda que le sirve a tu app | los 47 índices de miyomi.app + los 6 índices abiertos | 47 |
| 20 | El teclado que obedece | Keyboard Tools · Customization | 81 |
| 21 | La variante que cambió | Android Apps · Forks · Nightly builds | 131 |
| 22 | El módulo que no necesita root | Shizuku · Root Managers · Modules | 131 |
| 23 | Keiyoushi, catálogo de extensiones | índice de keiyoushi: 1.554 extensiones, `signingKey` | 1.554 ext |
| 24 | Repositorios de extensiones de anime | Aniyomi · índices de anime (miyomi + fmhy) | 253 |
| 25 | OCR de bolsillo | Image Tools · OCR · PDF Tools · Text Tools | 187 |
| 26 | Lectores de manga | Android Reading · Manga Readers | 253 |
| 27 | Lectores de cómic y novela | iOS Reading · Manga / Novel Readers | 253 |
| 28 | Mangayomi y sus extensiones | índice de mangayomi: 363 extensiones, 9 idiomas | 363 ext |
| 29 | LNReader y sus plugins | LNReader · Novel Plugins · Light Novels | 253 |
| 30 | Cloudstream y sus repositorios | Video Streaming Apps · Cloudstream | 89 |
| 31 | El peso no es el problema | APK Tools · Untouched APKs · FOSS APKs | 253 |
| 32 | Un sitio que se cae | dominios + lectores (ya medido: RDAP + DNS) | — |
| 33 | Apoyo a desarrolladores | proyectos de menos de 500 ★ del censo nuevo | 3.125 |
| 34 | Tu biblioteca se recupera | Backups · Export / Import · Android File Tools | 247 |
| 35 | (personal: la Ballenita) | no lleva recursos | — |
| 36 | Cómo se mide un sitio caído | registro, DNS y cabecera (ya medido) | — |
| 37 | (personal: carta a la manada) | no lleva recursos | — |
| 38 | (personal: cine y filosofía) | no lleva recursos | — |
| 39 | (personal: Canserbero) | no lleva recursos | — |
| 40 | La lección del hash | el método + la muestra del censo | 3.125 |

## La regla que no se rompe

Cada pieza que reemplace un recurso tiene que **medirlo**: estrellas, última entrega, adjuntos y
cuántos con suma, contra la API pública, y con su JSON en `docs/`. Ninguna ficha entra por aparecer
en una lista: FMHY y miyomi son **de dónde salen los candidatos**, no la prueba de que sirvan.

Y las cuatro piezas personales (35, 37, 38, 39) siguen sin recursos a propósito: no son piezas de
medición y el LEEME no les exige lo que no son.
