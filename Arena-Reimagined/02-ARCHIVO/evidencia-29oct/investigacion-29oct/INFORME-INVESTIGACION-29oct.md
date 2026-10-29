# INVESTIGACIÓN DE NUEVOS TEMAS Y APPS — 29-oct-2026

Disparador: el dueño encontró `mankidev/orvid` y pidió crear Facebook 83–108 hasta terminar e investigar nuevos temas y apps. Estado al abrir: **Facebook 83–108 ya estaban creadas y empujadas** (26/26 con pulso de nacimiento, commits `2c20988`/`ff3058b`); se re-verificaron 26/26 y se procede con la investigación, que es lo nuevo.

## 1. La pieza del dueño: Orvid

| Campo | Dato verificado 29-oct-2026 |
|---|---|
| Repo | `mankidev/orvid` (GitHub) |
| Qué es | Cliente Android de video privado: busca YouTube, PeerTube, TikTok, Instagram y 250+ sitios a la vez, con **Tor integrado** (circuito por fuente y por video), alternativa a NewPipe |
| Estrellas | ★9 (verificado 29-oct-2026) · 1 fork · 2 contribuidores |
| Licencia | **GPL-3.0-or-later** |
| Nacimiento | 2026-10-16 (v0.1.0) — **13 días de vida** |
| Actividad | Hoy (2026-10-29): release **Orvid 0.4.22** hace horas; **18 releases** en su corta vida |
| Fuentes | No trae fuentes: se añaden desde repositorios firmados; el oficial es `mankidev/orvid-sources` (★1, GPL-3.0, creado 2026-10-17, actividad hoy). Las fuentes adultas viven en repo separado, oculto tras gesto + comprobación de edad |
| Requiere | Android 8.0+ · APK en Releases · Obtainium |
| Oficios firmados | Tor con puentes obfs4/Snowflake/meek, bloqueo por huella/PIN, salida de pánico que borra memoria, sin historial (memoria solamente) |

**Juicio de la casa (enfoque de La Bandita: novedad con futuro, no popularidad):**
- ✅ **Futuro sobresaliente en concepto**: fusiona tres corrientes verificadas (cliente multisource por repos de fuentes — el patrón Mihon/Kazumi —, Tor por defecto con circuito por fuente, y arranque rápido medido contra NewPipe: 1,9 s a resultados contra 7,1 s según `docs/PERFORMANCE.md` del propio repo, dato de parte, no auditado por terceros).
- ✅ Licencia clara desde el día uno, ritmo de releases diario, código abierto javero simple (Java 96%), build reproducible documentado con Termux.
- ⚠️ **Riesgos firmados sin maquillar**: 13 días de vida, 1 desarrollador principal + 1 contribuidor, ★9: es semilla, no roble. Las fuentes son externas y firmadas: la confianza se traslada al firmante del repo de fuentes que el usuario añada (el oficial es del mismo autor). Tor por defecto mejora privacidad y castiga velocidad (el propio README confiesa el banner cuando Tor se apaga). Afirmaciones de catálogo (“250+ sitios”, comparativas) son del autor hasta auditoría independiente.
- **Veredicto**: *joya joven para vigilar y probar en teléfono de laboratorio; candidata a pieza cuando cumpla 30–60 días empujando o sume contribuidores; hoy entra al radar con su vara medida, no al pedestal.*

## 2. Universo de candidatos verificados hoy (29-oct-2026)

| Repo | ★ | Licencia | Nació | Última actividad | Release reciente | Lectura |
|---|---:|---|---|---|---|---|
| `mankidev/orvid` | 9 | GPL-3.0 | 2026-10-16 | 2026-10-29 | v0.4.22 hoy | Semilla Tor+multisource |
| `mankidev/orvid-sources` | 1 | GPL-3.0 | 2026-10-17 | 2026-10-29 | — | Fuentes firmadas del anterior |
| `Predidit/Kazumi` | 40.074 | GPL-3.0 | 2024-05-09 | 2026-10-29 | 2.4.2 (23-oct) | Agregador de anime por fuentes: gigante vivo |
| `libre-tube/libretube` | 12.908 | GPL-3.0 | 2021-12-09 | 2026-10-29 | Nightly hoy | Cliente YouTube vía Piped, en faena diaria |
| `yairm210/Unciv` | 11.498 | MPL-2.0 | 2017-11-21 | 2026-10-29 | 4.22.15 (ayer) | Civilización de bolsillo, decano activo |
| `localsend/localsend` | 96.423 | sin resolver* | 2022-12-16 | 2026-10-29 | 1.18.2 (ago) | Intercambio local soberano (*la web no resolvió SPDX hoy) |
| `rustdesk/rustdesk` | 127.465 | AGPL-3.0 | 2020-09-28 | 2026-10-29 | 1.5.0 (sep) | Escritorio remoto autoalojable |
| `hrydgard/ppsspp` | 14.780 | NOASSERTION | 2012-11-01 | 2026-10-29 | 1.20.4 (may) | Emulador PSP, el decano del bolsillo |
| `deniscerri/ytdlnis` | 10.839 | GPL-3.0 | 2022-05-27 | 2026-10-28 | 1.9.1.1 (19-oct) | Descargador yt-dlp con cara amable |
| `2dust/v2rayNG` | 64.925 | GPL-3.0 | 2019-05-15 | 2026-10-28 | 2.3.14 (ayer) | Cliente proxy del barrio valiente |
| `MM2-0/Kvaesitso` | 5.322 | GPL-3.0 | 2021-09-18 | 2026-10-28 | 1.41.0 (sep) | Lanzador-buscador: la casa ordenada |
| `maxrave-dev/simpmusic` | 12.508 | GPL-3.0 | 2023-04-15 | 2026-10-27 | 2.4.0 (22-oct) | YouTube Music sin cuenta y con letra |
| `TeamNewPipe/NewPipe` | 40.348 | GPL-3.0 | 2015-09-03 | 2026-10-27 | 0.29.1 (ago) | El abuelo cliente: sigue empujando |
| `guardianproject/orbot` | 3.659 | NOASSERTION | 2014-05-21 | 2026-10-26 | v17.9.7 RC1 (9-oct) | Tor para todo el teléfono |
| `ImranR98/Obtainium` | 21.004 | GPL-3.0 | 2022-08-11 | 2026-10-25 | v1.7.3 (25-oct) | La tienda sin tienda: updates desde la forja |
| `FossifyOrg/gallery` | 3.860 | GPL-3.0 | 2022-06-12 | 2026-10-24 | 1.14.1 (24-oct) | Galería básica soberana |
| `MetaCubeX/ClashMetaForAndroid` | 48.590 | GPL-3.0 | 2022-06-07 | 2026-10-21 | 2.11.36 (21-oct) | Proxy con reglas, vivo |
| `solkin/appteka-android` | 1.358 | GPL-3.0 | 2015-01-11 | 2026-10-21 | v24.0 (21-oct) | Tienda comunitaria de APK |
| `brunodev85/winlator` | 19.680 | LGPL-2.1 | 2023-07-26 | 2026-10-17 | 11.2 (jun) | Windows en el bolsillo: empuje sí, release lenta |
| `termux/termux-app` | 63.656 | NOASSERTION | 2015-10-23 | 2026-09-26 | 0.119-beta (2025) | Terminal decano, ritmo pausado |
| `junkfood02/seal` | 30.148 | GPL-3.0 | 2022-04-15 | 2026-09-26 | beta de 2024-11 | Empuja código pero no publica release: **vigilar** |
| `z-huang/innertune` | 6.128 | GPL-3.0 | 2020-02-11 | 2025-11-13 | 0.5.10 (2024) | **Dormido**: historia, no camino nuevo |
| `wintun-dev/nekoray` | — | — | — | 404 | — | Slug citado que no existe: descartado |

## 3. Temas nuevos con futuro (mapa para próximas piezas, cuando el dueño ordene)

1. **Video privado multisource con Tor** (Orvid + orvid-sources, con Orbot y NewPipe/LibreTube como contraste): la corriente que viene — buscar en todas partes sin entregar la IP. Tema #1 del radar.
2. **La app vacía y las fuentes firmadas** (patrón Orvid/Kazumi/Mihon): el cliente como motor y los repos como contenido. Doctrina transversal de la obra; pide pieza-manifiesto cuando la casa la ordene.
3. **La tienda sin tienda** (Obtainium + Appteka + Droid-ify): actualizar desde la forja sin intermediarios. Terreno conocido de la casa, con Pulso fresco hoy.
4. **Soberanía local entre aparatos** (LocalSend + RustDesk autoalojado): archivos y escritorio sin nube ajena; continuación natural del sótano de copias (108).
5. **El bolsillo que juega y emula** (Unciv + PPSSPP + Winlator): tres generaciones de “el teléfono como máquina del tiempo”, todas vivas hoy.
6. **Red con vara** (v2rayNG + ClashMeta + Orbot): privacidad de tránsito en tres niveles (app, sistema, red entera).
7. **Descargar con fecha** (YTDLnis vivo contra Seal dormido en releases): la comparación enseña sola — empuje de código no es release, y release vieja no es muerte si el código respira; se firman las dos fechas.

## 4. Cierre

- Facebook 83–108: **cerradas y verificadas** (26/26), sin duplicar trabajo.
- Orvid: **aprobada como radar de futuro**, con sus riesgos firmados (13 días, 1 dev, ★9) — se re-pulsa en la próxima gira antes de cualquier pedestal.
- Ninguna pieza nueva se creó con esta investigación: es el mapa, listo para cuando el dueño mande convertir tema en publicación (la serie WhatsApp permanece cerrada en 108; Facebook quedó completa en 108 y crecerá solo por orden expresa).

Fuentes: GitHub web oficial + Atom por repo (29-oct-2026), README y docs de Orvid. Datos brutos: `candidatos-nuevos-29oct.json`.
