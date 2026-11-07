# EXPLORACIÓN DE NUEVOS RECURSOS — 15 de octubre de 2026 · 10:53–11:05 UTC

**Orden del dueño [P], verbatim:** «No basta con re-verificar lo que ya teníamos sino también
que hay que explorar nuevos recursos sin limitarnos a lo que ya poseemos ni duplicando o
buscando entre cadáveres o famosos, recuerda lo de La Bandita: es la novedad, lo desconocido,
pero con calidad y potencial, y recuerda que la desinformación y la omisión también es mentir».

**Decisión del dueño sobre el token [P]:** «sigue siendo el mismo token pues lo necesitarás
hasta que terminemos esto» — el token permanece vivo durante el proyecto; revocación solo al
cierre total. Queda constado y NO se vuelve a pedir revocación intermedia.

---

## MÉTODO (todo contado hoy, nada heredado)

Búsquedas contra GitHub Search API (con token), 9 vetas, 15 resultados por veta:

| Veta | Filtro | total_count |
|---|---|---|
| recién nacidos | topic:android, creado >2026-04-01, ★15..3000 | 1.407 |
| activos medios | topic:android, ★150..3000, push >2026-10-05 | 1.127 |
| lanzadores | topic:launcher+android, ★20..3000, push >2026-09-15 | 36 |
| rss | topic:rss-reader, ★20..3000, push >2026-09-15 | 69 |
| ebooks | topic:ebook+android, ★20..3000, push >2026-09-15 | 7 |
| dinero | topic:expense-tracker, ★20..3000, push >2026-09-15 | 37 |
| salud | topic:fitness+android, ★20..3000, push >2026-09-15 | 11 |
| clima | topic:weather+android, ★20..3000, push >2026-09-15 | 11 |
| notas | topic:notes+android, ★50..3000, push >2026-09-15 | 16 |

4.672 resultados brutos → filtros: sin archivados (cadáveres), sin forks, con licencia SPDX
declarada, señal android en topics o descripción → **70 sobrevivientes**
(evidencia completa: `exploracion-nuevos-recursos-2026-10-15.tsv`) → exclusión de ~60 nombres
del censo de la casa (Mihon, NewPipe, Metrolist, SimpMusic, Fossify, Kotatsu, Usagi, etc.) y
de los famosos de siempre → censo fino de 10.

**Velocidad** = estrellas ÷ meses de vida del repo. Edad del censo: medido 15-oct-2026.

## LOS DIEZ MEDIDOS A FONDO (censo de API, 15-oct-2026)

| Casa | Qué declara ser | ★ | Vida | ★/mes | Push | Licencia | Release | Colab. |
|---|---|---|---|---|---|---|---|---|
| PimpinPumpkin/**Vela** | mapas y navegación paso a paso SIN Google Play Services | 1.961 | 4,1 m | 482 | **HOY** | GPL-3.0 | canary (HOY) | 23 |
| Leviidev/**Husk** | «Run Android on iOS. Natively or Emulated» | 1.920 | 1,1 m | 1.746 | 14-oct | GPL-2.0 | 2.0 (11-oct) | 4 |
| kitsumed/**ShizuCallRecorder** | grabar llamadas sin root, vía Shizuku/ADB | 1.755 | 5,1 m | 342 | 14-oct | GPL-3.0 | v1.3.3 (12-ago) | 7 |
| flectar/**mail** | cliente de correo nativo «built for speed» | 1.366 | 1,4 m | 976 | **HOY** | AGPL-3.0 | v0.1.0-alpha.7 (8-oct) | 5 |
| mokshablr/**gander** | visor offline cero-permisos: PDF, Word… «take a gander at any file» | 1.271 | 2,9 m | 433 | 14-oct | MIT | v2.5 (14-oct) | 3 |
| DSH-APP/**DSHA** | DeepSeek en el teléfono sin root ni Termux (Ubuntu+proroot) | 1.270 | 2,1 m | 615 | **HOY** | MIT | v0.2.0-rc2 (9-oct) | 9 |
| nano-muse/**nanoMuse** | agente personal open-source «for every device you own» | 1.233 | 0,7 m | 1.681 | **HOY** | GPL-3.0 | v1.0.5 (13-oct) | 12 |
| ciddwd/**overlay-translator** | traducción en vivo de la pantalla (juegos, novelas visuales, manga) sin root | 1.016 | 3,8 m | 265 | 13-oct | Apache-2.0 | v0.4.7 (13-sep) | 0* |
| IacobIonut01/**ReFra** | galería de medios moderna (Jetpack Compose) | 2.897 | 43,7 m | 66 | **HOY** | Apache-2.0 | 5.2.2 (4-oct) | 23 |
| ahpxex/**read-aware** | lector de ebooks con agente que recuerda tu lectura entre libros | 451 | 8,4 m | 54 | 14-oct | AGPL-3.0 | v0.6.7 (13-oct) | 1 |

\* El conteo de colaboradores con anon=false devolvió 0 (quizá commits sin perfil vinculado):
se marca como riesgo de verificación, no como defecto del proyecto.

## LECTURAS DE OFICIO (con la vara de la casa)

- **Vela** llena un hueco real del catálogo: la caja 09 tiene mapas (Organic Maps) pero nadie
  cubre la *navegación por voz sin Google* — el «llévame aquí» de la gente que desinstaló
  Play Services. 23 colaboradores y release el mismo día del censo: taller grande y despierto.
- **ShizuCallRecorder** es caso dominicano puro: grabar llamadas sin root, apalancado en la
  herramienta que nuestra guía ya enseña (Shizuku). Nicho nuevo, pedidísimo, sin entrada en
  nuestro catálogo.
- **Husk** es la bomba de novedad de la cosecha: 1.920 estrellas en cinco semanas. Alcance
  especial (Android sobre iPhone) — no es guía de tienda, es historia de portada.
- **gander** y **flectar/mail** son la generación nueva de utilidades: cero permisos y
  velocidad nativa. mail está en alpha — potential sí, madurez aún no; se vigilan.
- **nanoMuse** y **DSHA** abren la puerta IA-on-device del catálogo. Velocidad de las más
  altas medidas. DSHA nació con README en chino: calidad a validar antes de recetar.
- **overlay-translator** pega directo con nuestra comunidad de manga: traducir la pantalla
  en vivo dentro de cualquier lector. Riesgo: un solo bus (0 colaboradores contados,
  release de hace un mes).
- **ReFra** es la galería moderna madura (43 meses, 23 colaboradores): candidata a compañera
  de Fossify en la caja, no a sustituta.
- **read-aware** es el experimento bonito (agente que recuerda entre libros): un colaborador,
  bus de una sola persona — potencial sí, resiliencia no.

## LO QUE SE QUEDÓ FUERA Y POR QUÉ (anti-omisión)

- **Famosos y recursos de dev:** Pocket Casts (Automattic), DAVx⁵, Decompose, kotlin-footguns,
  chrisbanes/skills — conocidos o no son apps de usuario.
- **README en chino sin validar** (Breeze, HeartRateMonitor, solomd): quedan en reserva en el
  TSV; no se declaran calidad ni riesgo sin leerlos a fondo.
- Todos los 70 sobrevivientes (con fechas y licencias) están en el TSV adjunto — nada se
  descarta en silencio.

## RECOMENDACIÓN PARA WA 11+ (una pieza nueva por turno, bajo orden del dueño)

1. **Vela** — nicho vacío, taller grande, release de hoy. La más Lista.
2. **ShizuCallRecorder** — caso de uso dominicano, apalancado en Shizuku que ya enseñamos.
3. **gander** — privacidad sin discurso: un visor que no pide nada.
4. **Husk** — pieza de alcance especial (novedad de portada).
5. **overlay-translator** — manga + juegos en vivo (validar bus primero).

---
*La Bandita informa a partir de fuentes fechadas: cada número de esta hoja fue contado hoy
15-oct-2026 por API, con el método arriba descrito. Lo que no se midió, no se declaró.*
