# HABILIDADES DE LA BANDITA · SISTEMA REUTILIZABLE Y AUTOEVOLUTIVO

Todo el proceso de la casa convertido en habilidades que se pueden reusar infinitamente y que **aprenden de cada experiencia**: cada una trae su vara (procedimiento), su herramienta ejecutable y su memoria en la bitácora.

## Las seis habilidades fundacionales
1. **Arranque de suelo firme** — `herramientas/arranque.py` · Detecta la mordida, mide proyecto y espejo contra el manifiesto y restaura antes de afirmar nada. *Vara de arranque: inventario → hash → restaurar → recién trabajar.*
2. **Verificación multinivel** — `herramientas/chequeo-niveles.py` (+ `../_herramientas/verificar-suelo.py`) · L0 hash · L1 lupa · L2 catálogo==disco · L4 paquete íntegro. *Vara de verificación: ningún nivel se salta; el que falla detiene la línea.*
3. **Pulso de repos** — `herramientas/pulso.py` · Mide GitHub por la vía gobernante (API con token en entorno; si no, web oficial) con la semántica de la casa: 404 muerto · 451 existe bloqueado · 403/429 cuota jamás muerte.
4. **Licencias sin inventar** — orden SPDX → endpoint → texto del LICENSE → ausencia firmada (lección L-03).
5. **Pieza editorial** — pipeline de la casa: verificar en fuente primaria → pre-lint → escribir familia adaptativa (jamás gemela) → dedupe/mojibake → lupa → acta → hornear catálogo. Placas con fecha siempre: la fecha es lo que hace cierto al dato mañana.
6. **Guardado en GitHub** — `herramientas/guardar.py` · Procedimiento único contenido: espejo sincronizado → commit → push → ls-remote → clonación fresca byte por byte. *Vara de cierre: no hay push bueno sin su clonación que lo pruebe.*

## Autoevolución
- **`bitacora-lecciones.md`** guarda cada fallo con su regla (L-01…).
- **`herramientas/aprender.py "contexto" "fallo" "regla"`** registra la lección nueva y sube la versión en `EVOLUCION.md`.
- Al arrancar cualquier sesión: leer la bitácora (2 minutos) vale más que re-descubrir una lección cara.
- Una habilidad se corrige editando su herramienta y registrando la lección que la motivó: el sistema no se queda quieto.

## Orden de una jornada cualquiera (el circuito completo)
`arranque.py` → trabajar (pulso/piezas) → `chequeo-niveles.py --con-lupa` → hornear catálogo si hubo piezas → espejo → `guardar.py "mensaje"` → `aprender.py` si algo enseñó algo. Cada vuelta deja el sistema un poco más sabio que la anterior.
