# ESTRUCTURA DE LA CASA · LA BANDITA

Mapa vivo del proyecto y del repo. Si una acta vieja cita una ruta anterior, aquí está su traducción.

## Carpetas
- **`01-PUBLICACIONES/`** — el contenido publicable: `WhatsApp-dominicano-ES/` (canon 00–108) y `Facebook-dominicano-ES/` (muro 00–131). Esto es lo que se copia y se publica.
- **`02-ARCHIVO/`** — la memoria: `catalogo-la-bandita.html` (el catálogo visual), `registro-2026-10-15.md` (las actas firmadas de cada hito) y **`evidencia-29oct/`** (antes `_rearm-29oct`: la evidencia completa de la jornada del 29-oct-2026 por fases — pulso, creación, datos, aseguramiento, depuración, chequeos, pendientes).
- **`HABILIDADES/`** — el sistema reutilizable y autoevolutivo: índice, herramientas ejecutables, `EVOLUCION.md` y `bitacora-lecciones.md`.
- **`ENTREGA-29OCT-2026/`** — el paquete de entrega (guía, series, datos, informes, anexo BitXBit) y su gemelo `ENTREGA-La-Bandita-29oct2026.zip`.
- **`MANIFIESTO-DE-ENTREGA-FINAL.md`** — la firma de la entrega con sus SHA-256.

## Traducción de rutas (reorden 29-oct-2026)
- `02-ARCHIVO/_rearm-29oct/…` → **`02-ARCHIVO/evidencia-29oct/…`** (mismo contenido, nombre que se entiende sin contexto).
- Las actas históricas conservan las rutas de su día: son historia firmada y no se reescriben; este mapa es su traductor.

## El circuito de trabajo
`HABILIDADES/herramientas/arranque.py` → trabajar → `HABILIDADES/herramientas/chequeo-niveles.py --con-lupa` → espejo → `HABILIDADES/herramientas/guardar.py "mensaje"` → `HABILIDADES/herramientas/aprender.py` si hubo lección.
