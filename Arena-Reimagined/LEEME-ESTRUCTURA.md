# ESTRUCTURA DE LA CASA · LA BANDITA

> **Aviso del 3 de noviembre de 2026.** Este mapa describía el estado de octubre y quedó viejo en dos puntos: las dos carpetas de canal ya no mezclan el ciclo vivo con la memoria, y el contador de piezas cambió. El mapa vigente es **`MAPA-DEL-ARCHIVO.md`**, en la raíz del repositorio. Lo que sigue se conserva como historia y como traducción de rutas anteriores.

Mapa vivo del proyecto y del repo. Si una acta vieja cita una ruta anterior, aquí está su traducción.

## Carpetas
- **`01-PUBLICACIONES/`** — el contenido publicable: `WhatsApp-dominicano-ES/` (canon 00–108) y `Facebook-dominicano-ES/` (muro 00–131). Esto es lo que se copia y se publica.
- **`02-ARCHIVO/`** — la memoria: `catalogo-la-bandita.html` (el catálogo visual), `registro-2026-10-15.md` (las actas firmadas de cada hito) y **`evidencia-29oct/`** (antes `_rearm-29oct`: la evidencia completa de la jornada del 29-oct-2026 por fases — pulso, creación, datos, aseguramiento, depuración, chequeos, pendientes).
  - **`_etapas-anteriores/`** — desde el 3-nov-2026 vive aquí lo que antes estaba suelto en la raíz de `Arena-Reimagined/`: `_versiones/` (manual, tratado y lecciones congelados), `packs/` (extras de las series viejas), `_herramientas/` (la lupa, las forjas, el montador), `_herramientas-casa/` y `_referencia/`. La traducción de rutas está en `MAPA-DEL-ARCHIVO.md`, y `tools/referencias.py` comprueba que ninguna quede citada por su ruta vieja desde un archivo vivo.
- **`HABILIDADES/`** — el sistema reutilizable y autoevolutivo: índice, herramientas ejecutables, `EVOLUCION.md` y `bitacora-lecciones.md`.
- **`ENTREGA-29OCT-2026/`** — el paquete de entrega (guía, series, datos, informes, anexo BitXBit). Su envase comprimido se retiró el 4-nov-2026 porque sus 284 entradas están todas abiertas aquí; el acta con el hash está en `ARCHIVO-HISTORICO/_podado-2026-11-03/`.
- **`MANIFIESTO-DE-ENTREGA-FINAL.md`** — la firma de la entrega con sus SHA-256.

## Traducción de rutas (reorden 29-oct-2026)
- `02-ARCHIVO/_rearm-29oct/…` → **`02-ARCHIVO/evidencia-29oct/…`** (mismo contenido, nombre que se entiende sin contexto).
- Las actas históricas conservan las rutas de su día: son historia firmada y no se reescriben; este mapa es su traductor.

## El circuito de trabajo
`HABILIDADES/herramientas/arranque.py` → trabajar → `HABILIDADES/herramientas/chequeo-niveles.py --con-lupa` → espejo → `HABILIDADES/herramientas/guardar.py "mensaje"` → `HABILIDADES/herramientas/aprender.py` si hubo lección.
