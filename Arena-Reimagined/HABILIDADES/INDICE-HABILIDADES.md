# HABILIDADES DE LA BANDITA · SISTEMA REUTILIZABLE Y AUTOEVOLUTIVO

Todo el proceso de la casa convertido en habilidades que se pueden reusar infinitamente y que **aprenden de cada experiencia**: cada una trae su vara (procedimiento), su herramienta ejecutable y su memoria en la bitácora.

> **Antes que todo: `CORAZON.md`** — los principios dictados por el dueño («no eres un chatbot: eres un asistente personal que crece con tu usuario»). Se lee al arrancar; manda sobre cualquier habilidad de esta lista.

## Las seis habilidades fundacionales
1. **Arranque de suelo firme** — `herramientas/arranque.py` · Detecta la mordida, mide proyecto y espejo contra el manifiesto y restaura antes de afirmar nada. *Vara de arranque: inventario → hash → restaurar → recién trabajar.*
2. **Verificación multinivel** — `herramientas/chequeo-niveles.py` (+ `../_herramientas/verificar-suelo.py`) · L0 hash · L1 lupa (**medición** de aire: cifras, no puerta) · L2 catálogo==disco · L4 paquete íntegro. *Vara de verificación: ningún nivel se salta; el que es puerta y falla detiene la línea; el que mide, publica su cifra.*
3. **Pulso de repos** — `herramientas/pulso.py` · Mide GitHub por la vía gobernante (API con token en entorno; si no, web oficial) con la semántica de la casa: 404 muerto · 451 existe bloqueado · 403/429 cuota jamás muerte.
4. **Licencias sin inventar** — orden SPDX → endpoint → texto del LICENSE → ausencia firmada (lección L-03).
5. **Pieza editorial** — pipeline de la casa: verificar en fuente primaria → pre-lint → escribir familia adaptativa (jamás gemela) → dedupe/mojibake → lupa → acta → hornear catálogo. Placas con fecha siempre: la fecha es lo que hace cierto al dato mañana.
6. **Guardado en GitHub** — `herramientas/guardar.py` · Procedimiento único contenido: espejo sincronizado → commit → push → ls-remote → verificación por blobs del árbol remoto contra los archivos locales. *Vara de cierre: no hay push bueno sin su verificación por blobs que lo pruebe (alcance exacto: piezas, catálogo, ZIP y mapa — lo que el script enumera, ni más ni menos).*

## Autoevolución
- **`bitacora-lecciones.md`** guarda cada fallo con su regla (L-01…).
- **`herramientas/aprender.py "contexto" "fallo" "regla"`** registra la lección nueva y sube la versión en `EVOLUCION.md`.
- Al arrancar cualquier sesión: leer la bitácora (2 minutos) vale más que re-descubrir una lección cara.
- Una habilidad se corrige editando su herramienta y registrando la lección que la motivó: el sistema no se queda quieto.

## Orden de una jornada cualquiera (el circuito completo)
`arranque.py` → trabajar (pulso/piezas) → `chequeo-niveles.py --con-lupa` → hornear catálogo si hubo piezas → espejo → `guardar.py "mensaje"` → `aprender.py` si algo enseñó algo. Cada vuelta deja el sistema un poco más sabio que la anterior.

## Habilidad 7 · Formato respirable (Facebook) — `02-ARCHIVO/evidencia-29oct/respirable-29oct/`
En Facebook el texto respira o muere: mapa mental en dos líneas por familia (quién → qué hace), placas una por bloque con cada dato en su línea, nada de tablas disfrazadas de viñetas. Regla de oro aprendida del dueño: la reorganización se prueba — **la secuencia de palabras debe ser idéntica antes y después**; cualquier edición de palabras va declarada y contada, jamás disfrazada de formato.

---

## ENMIENDA 2026-11-01 · fusión con el Manual de Estilo y Operaciones V3.0

**Registrada por:** orden del dueño del 1 de noviembre de 2026 («guarda esto y fusiónalo con los archivos principales de los cimientos… criterios obligatorios de éxito»).

**Qué entra:** el `Manual de Estilo y Operaciones La Bandita — V3.0 (1-nov-2026)` y la lista de criterios obligatorios `CIMIENTOS — criterios obligatorios y precedencia (1-nov-2026)`, ambos en `corpus-la-bandita/`.

**Qué cambia aquí:** el índice gana una entrada nueva, la habilidad «cumplir el manual»: saber de memoria el cierre de cuatro piezas (meme, firma textual, remate propio, medición con hora), el molde de la ficha de ocho campos y la lista de frases prohibidas. Es habilidad de oficio, no adorno: se evalúa con `tools/manual_gate.py`.

**Precedencia:** este documento conserva su rango; el Manual V3.0 queda **subordinado** y manda sobre la **forma** de cada pieza (molde, fichas, FAQ, enlaces, firma, meme, notas, prohibiciones). Donde el dueño dio una orden posterior, manda el dueño; las tensiones están registradas, con su resolución, en `CIMIENTOS` §3.

**Comprobación:** `tools/manual_gate.py` ejecuta los criterios C-01 a C-24 y `tools/vara.py` los vuelve compuerta (G11). Un criterio que solo vive en prosa no se cumple: este se mide.
