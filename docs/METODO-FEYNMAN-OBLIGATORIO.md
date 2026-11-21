# Método de Richard Feynman obligatorio en La Bandita

*Vigente desde el sábado 21 de noviembre de 2026. Norma integrada en `CORAZON-LA-BANDITA.md`,
`REGLAS/INDICE-DE-REGLAS.md`, `CIMIENTOS/04-VOZ-Y-CIERRE.md`, `PROCESOS/01-PIEZA.md`,
`SKILLS/escribir-pieza/SKILL.md` y los doce capítulos de `guia-maestra/texto/capitulos/`.*

---

## 0 · Qué exige esta norma (sin excepciones parciales)

Para cada tarea, lista de textos, análisis de datos o recurso recomendado, se aplica el **ciclo
completo de cuatro pasos** desarrollado por **Richard Feynman**:

1. **Seleccionar y estudiar el concepto:** elegir el tema o recurso concreto y estudiarlo en fuentes primarias confiables (código fuente, entregas firmadas, metadatos medidos, normas de `CIMIENTOS/`).
2. **Enseñarlo por escrito con palabras simples:** explicar qué hace, por qué importa y cómo se usa sin jerga técnica sin traducir, como si quien lee empezara de cero.
3. **Identificar lagunas y volver a la fuente original:** detectar dónde la explicación flaquea, falta un dato o aparece un «funciona porque sí», regresar al payload/fuente original para completarlo y declarar explícitamente cualquier hueco no medible.
4. **Simplificar y revisar con analogías:** reescribir el texto final integrando lo corregido mediante analogías cotidianas claras (indicando dónde termina la analogía para no engañar) hasta lograr una lectura fluida y comprobable.

---

## 1 · Aplicación completa a las **listas de textos** (`docs/INDICE.md`, `corpus-la-bandita/`, `guia-maestra/texto/capitulos/`)

1. **Seleccionar y estudiar el concepto:** tomar cada lista de textos (`docs/INDICE.md` con 165+ documentos y 78+ herramientas, el corpus normativo y los 12 capítulos temáticos de `guia-maestra/texto/capitulos/`) directamente desde su fuente en disco y el generador `tools/indice_docs.py`.
2. **Enseñarlo con palabras simples:** una lista de textos no es un cajón de enlaces sueltos: es el mapa del edificio. Cada entrada dice en una línea qué problema resuelve ese texto para alguien que entra por primera vez, y qué herramienta ejecuta cada paso.
3. **Identificar lagunas y volver a la fuente original:** cuando un índice tiene documentos huérfanos, líneas desactualizadas o capítulos que nombran herramientas sin explicar el porqué de su orden, la laguna delata un salto lógico. Se vuelve a la primera línea del script o al archivo real (`python3 tools/indice_docs.py` y `guia-maestra/datos/apps/*.json`) para corregirlo y declarar lo que está congelado como historia (como `site/` o `ARCHIVO-HISTORICO/`).
4. **Simplificar y revisar con analogías:** *analogía de la estantería etiquetada:* si un taller tiene 165 manuales apilados sin lomo ni orden, hasta el dueño pierde la tarde buscando cómo cambiar un tornillo; un índice generado directo de los libros en el estante es una etiqueta pegada en el canto que se actualiza sola en cuanto mueves una carpeta. (*Límite:* el índice indica dónde está cada documento y cuántas líneas tiene, no sustituye leerlo entero).

---

## 2 · Aplicación completa a los **análisis y mediciones** (`registry/`, `docs/MEDICION-*.json`, `docs/CENSO-*.json`)

1. **Seleccionar y estudiar el concepto:** cada análisis parte de los JSON medidos del registro (`6.838` fichas en `registry/` y `registry/registro.db`), los payloads crudos en `registry/_evidencia/` y `docs/_medicion-cache/`, y las compuertas `G0–G17` de `tools/vara.py`.
2. **Enseñarlo con palabras simples:** medir un proyecto de código abierto no es contar aplausos ni estrellas: es abrir la caja y mirar si la licencia te deja usarlo, si el autor arregló algo este año y si publicó un archivo con huella para que puedas comprobar que nadie lo cambió en el camino.
3. **Identificar lagunas y volver a la fuente original:** si al escribir un análisis no sabemos explicar por qué una app popular tiene nota baja (por ejemplo, por no publicar sumas SHA-256 o tener incidencias acumuladas), regresamos al JSON crudo de esa ficha (`registry/<id>.json`) y al payload cacheado (`payloads_sha256` en `tools/medir_piezas_24_34.py`), en vez de inventar excusas o rellenar huecos.
4. **Simplificar y revisar con analogías:** *analogía de la inspección técnica del coche:* las estrellas de GitHub son la pintura brillante del coche; la medición de licencia, actividad y huellas SHA-256 es revisar frenos, papeles y número de chasis antes de salir a carretera. (*Límite:* las 18 compuertas prueban forma, frescura e integridad del archivo, no garantizan que una aplicación funcione sin fallos en un teléfono concreto).

---

## 3 · Aplicación completa a los **recursos** (`guia-maestra/` y `tools/`)

1. **Seleccionar y estudiar el concepto:** cada uno de los `70` recursos de `guia-maestra/datos/apps/*.json` y sus `12` capítulos de `guia-maestra/texto/capitulos/*.md`, junto con el código ejecutable de `tools/`.
2. **Enseñarlo con palabras simples:** un recurso entra solo cuando responde tres preguntas llanas: qué haces con tus **Manos** (pasos claros), qué entiendes en tu **Cabeza** (cómo funciona y dónde falla) y cómo lo compruebas en el **Oficio** (un comando o enlace reproducible).
3. **Identificar lagunas y volver a la fuente original:** si un capítulo menciona un permiso (como Shizuku/ADB), un túnel VPN o un cifrado sin explicar qué ocurre cuando falla o cómo se deshace, se regresa a las fichas del capítulo y al dato de oficio medido para cerrar ese vacío en la sección Feynman de cada capítulo.
4. **Simplificar y revisar con analogías:** cada uno de los 12 capítulos en `guia-maestra/texto/capitulos/` cierra con una analogía concreta del capítulo (copia de seguridad, congelación de apps, permiso prestado, instalación verificada, cortafuegos, biblioteca local, nube propia, túnel de red, hogar inteligente, taller de diagnóstico, parte de avería y sello de oficio).

---

## 4 · Comprobación automática

El verificador [`tools/feynman_verificar.py`](../tools/feynman_verificar.py) y las pruebas de
[`tests/test_feynman.py`](../tests/test_feynman.py) comprueban que la norma y los doce capítulos
de `guia-maestra/texto/capitulos/` mantienen íntegros los cuatro pasos del método Richard Feynman.
