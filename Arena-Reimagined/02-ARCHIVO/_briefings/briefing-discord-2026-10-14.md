# BRIEFING — CAMPAÑA CANON PUBLICADA (paste-first, 14-oct-2026)
(Pegar como TEXTO en Discord al administrador — sin adjuntos; los adjuntos de GitHub no llegan al revisor)

---

**CAMPAÑA CANON — PUBLICADA ✓** · repo: github.com/alexaindruews170206-dev/Arena-Reimagined · rama `main` · commit `f738b4a` (sobre `001ef66`)

Proceso completo en 5 etapas con cifras medidas (actas fechadas en `02-ARCHIVO/`, append-only):

**E0 · Mapa asegurado** — inventario total de las 5 piezas generado por script determinístico, verificado por regeneración byte-a-byte (la causa raíz del daño: dos sluggeres distintos — el de los índices escritos a mano conservaba acentos y no truncaba; el del convertidor pliega acentos y trunca a 48).

**E1 · Demolición** — el CONTENIDO está sano: 0 contradicciones · 0 cifras huérfanas · 0 fechas imposibles · 0 promesas incumplidas · 0 artículos fantasma · **0 derogaciones en silencio** (regla de oro, Art. D-007). El daño real era solo de navegación.

**E2 · Reconstrucción única** — anclas muertas: fuentes **364 → 0** · envases **377 → 0** (verificación triple: mapa + regex sobre ids reales + XML ET/lxml). Única mutación de fuentes: targets de anclas bajo orden expresa; **palabras del autor intactas byte-a-byte**. Fuentes HTML legacy (Cimiento, Compendio) sin tocar. Ids nativos `pillars/ops/puerta/erratas` preservados; h3–h6 y título con ancla (curas estructurales del convertidor).

**E3 · Baterías** — vara estática **65/65** (13/13 × 5 piezas) · batería formal **55/55** · batería en navegador real **5/5**: consola 0 errores, deep-links reales verificados, búsqueda, tema, y **0 px de overflow horizontal en móvil** (hasta un SHA-256 de 64 caracteres en prosa verbatim ahora envuelve sin romper nada). 10 capturas de evidencia.

**E4 · Kit sellado** — `canon-labandita-kit-etapa4.zip` (3.970.620 B) · sha256 completo:
`fa52c6dd2525963fbc1b60e55d123e7e0ac5ab6893b8368fb21bd905854da2ef`
Contenido: fuentes + envases XHTML autocontenidos (0 recursos externos, offline, imprimibles) + mapa + taller completo + actas + capturas + SHA256SUMS.txt (`sha256sum -c` verifica todo).

**Cadena de sellos (sha256-16)** — fuentes .md antes → después (solo anclas):
TRATADO `3c58d9f9` → `580fcd21` · MANUAL `c4c33f44` → `e958ef0e` · LECCIONES `1539dfcf` → `89b700fd` · CIMIENTO `f517f6b7` INTACTO · COMPENDIO `07830c49` INTACTO.
Verificación pública post-push: el `TRATADO.md` y el ZIP publicados hash-ean **idénticos** a los sellados.

«Ninguna derogación se ejecuta en silencio. Cada una lleva su fila, su fecha y su firma. Así se corrige sin mentir sobre el pasado.» — Art. D-007. Esta campaña es esa fila. Mejor que lo que precedió, nunca perfecto.
