# INFORME DE ASEGURAMIENTO PREVIO A PUBLICAR — 29-oct-2026

Orden del dueño: maratón de aseguramiento antes de empezar a publicar en Facebook y WhatsApp, sin olvidar el guardado en GitHub. Se auditó todo lo publicado y todo lo que lo sostiene; lo que sigue es el resultado medido, no prometido.

## 1. Suelo y rescate
- La mordida de turno había dejado el proyecto sin las publicaciones y sin la carpeta de datos: **todo se restauró desde el espejo y desde GitHub** (`main` verificado en cada paso) y se re-midió tras restaurar.
- Estado verificado: **WhatsApp 111/111 con nota · Facebook 147 archivos (132 ids únicos) con 💓** — elegibles completos para el muro del catálogo.

## 2. Estructura, pieza por pieza
- WhatsApp: ids **00–108 completos, sin huecos**; cada pieza canónica con su nota `PULSO 29-OCT-2026` **exactamente una vez**; ningún duplicado. La única “sin nota” de la carpeta es un archivo FB extraviado histórico, fuera del canon (constatado desde el día uno). Seis piezas canónicas superan levemente la banda original de 62–64k **por la nota añadida** (la banda era del generador sin nota); la 00 cierra con su nota global deliberada, comprobada a mano.
- Facebook: ids **00–131 completos, sin huecos**; 147 archivos con variantes históricas; todas con 💓 (condición del muro). Quince piezas viejas conservan el formato de apertura de su época (`*Título*`), legibles y copiables; todas las nuevas abren con `#`.
- Placas citadas en las piezas nuevas (02, 83–131): **100% cruzadas contra datasets verificados** — ni una placa sin su medición detrás.
- **Lupa v6 sobre todo el corpus (WA + FB): EXIT=0 en ambas series.**

## 3. Re-pulso del universo entero (API autenticada de GitHub)
- Los **753 repos** del universo se re-midieron tras el dataset: **ningún repo pasó a no responder**, **ninguno pasó a archivado** entre la pasada y el re-pulso.
- Deriva de estrellas en horas: máxima **+15** (`project-nomad`); las placas citan “verificado 29-oct-2026”, así que la deriva es crecimiento del mismo día, no error.
- GitHub ya resuelve SPDX de tres que teníamos por texto: `aidoku-community/sources`, `koharu-rs/koharu`, `ponces/treble_aosp` → **Apache-2.0**; las tres celdas quedaron actualizadas en `repos-al-dia-29oct.tsv`.
- Nota de método firmada: la API (`pushed_at`, cualquier rama) marca actividad algo más fresca que Atom (rama por defecto); las piezas citan la actividad por la vía gobernante declarada. No es discrepancia, son dos relojes descritos.

## 4. Catálogo e integridad
- El JSON embebido del catálogo (build 16:13) contiene **WA 111 y FB 147**, y su texto es **byte por byte idéntico** a los archivos en disco (0 diferencias en las dos series).
- **MANIFIESTO SHA-256 de las 261 piezas** (WA+FB) guardado en `MANIFIESTO-SHA256-PIEZAS.tsv`: cualquier corrupción futura se detecta comparando, no recordando.
- Espejo local: **byte por byte idéntico al proyecto en los 261 archivos**, y catálogo/registro también idénticos.

## 5. URL
- Las 30 URL dudosas (403/404) se re-midieron: estados **idénticos** a los firmados (los 403 son bloqueo de bot ya comprobados en navegador; los 404 son los muertos confesados por pieza). Google Support responde ya 200 directo.

## 6. Lo que este aseguramiento NO promete
1. Los datos de estrellas son del 29-oct-2026 y seguirán moviéndose: al publicar, la fecha de la placa es la que manda.
2. Licencias firmadas sin resolver (79 del universo) siguen así: no se inventó ningún SPDX en ninguna auditoría.
3. La identidad GitHub de algunos repos jóvenes citados (crecimiento muy rápido de estrellas, p. ej. `aerial-tv`) sigue marcada con la ceja en sus piezas; es radar, no ranking.

## 7. Veredicto
**Listo para publicar.** Serie WhatsApp cerrada y sellada (00–108), muro Facebook completo y creciendo (00–121→00–131 con las de hoy), datos de cada recurso al día, catálogo íntegro, espejo idéntico y GitHub guardado parte por parte. Artefactos de esta maratón: carpeta `02-ARCHIVO/_rearm-29oct/aseguramiento-29oct/`.
