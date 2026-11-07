# DEMOLICIÓN RED-TEAM — RFC v2.3 (auto-auditoría antes de la quinta ronda)
**Orden del dueño:** revisión exhaustiva de toda la infraestructura y su concepción — código,
diseño e ideología — bajo pruebas de resistencia, sin soluciones superficiales. 10-oct-2026.
**Objeto:** `RFC-v2.3-UNIFIED-FEED-AniZen-Houri-2026-10-10.md` (10f89ddc93a20ce1) + envase HTML
(097eaefbcf701c12). Método: batería mecánica de consistencia + estrés adversarial de los
algoritmos de las demos + lectura hostil de arquitectura e ideología.

## VEREDICTO GENERAL
La arquitectura resiste (los 5 mecanismos tienen portador, las 3 principios cubren los casos
propios), pero la demolición destapó **2 contradicciones internas reales, 1 laguna de colisión,
3 ambigüedades que un revisor experto cobraría, 1 residual de versión y 2 hallazgos ideológicos**.
Todo es reparable sin tocar los cimientos → se aplica como **v2.4** en el mismo turno.

## HALLAZGOS

### CRÍTICOS (contradicciones internas — un revisor experto las cobra)
- **C1 · Cold-start vs classify-on-miss (§6.3).** La prueba de arranque en frío («instalación
  nueva con caché vacía segmenta idéntico») es **falsa para la capa IA**: con caché vacía no hay
  etiquetas hasta que el job en background las compute — el arranque 1 y el 10 difieren por
  diseño. Tal como está, nuestra propia prueba de aceptación fallaría en mode:"ai".
  **Fix v2.4:** la igualdad de arranque en frío se limita a la CAPA DE REGLAS (P2, determinista,
  independiente de caché); la capa IA es explícitamente asíncrona: el primer arranque muestra el
  pozo «Sin asignar» hasta que el batch termina, y las etiquetas nuevas se aplican con aviso
  visible «segmentación actualizada» — jamás reordenación silenciosa. Golden files fijan la
  igualdad de REGLAS; la capa IA recibe otra prueba (llegada asíncrona, sin reorden silencioso).
- **C2 · Colisiones de work_key (§5.1).** Mismo título ≠ misma obra (Fruits Basket 2001/2019,
  HxH 1999/2011). El colapso canónico con claves sin año puede fundir obras distintas — peor que
  mostrar ambos, exactamente la objeción del revisor a su nivel siguiente.
  **Fix v2.4:** el colapso exige igualdad EXACTA de clave completa; entradas sin año solo colapsan
  con claves sin año o de año igual; ambigüedad residual → badge visible «posible duplicado», y
  política conservadora: ante la duda, NO se colapsa (P1: jamás fingir una fusión).
- **C3 · Dos pozos con nombre distinto (§6.1/§6.3).** «Sin asignar» (reglas) y «unclassified»
  (IA) son el mismo estado con dos vocabularios — deriva de UI garantizada.
  **Fix v2.4:** UN solo pozo visible «Sin asignar» con dos productores (sin regla que pegue,
  sin etiqueta en caché).

### ALTOS
- **A1 · rules_packs direccionables por {id,versión} (§3/§6.1):** en merge/restore la referencia
  puede no corresponder al contenido esperado (secuestro de id). **Fix:** packs con dirección por
  contenido — la referencia lleva prefijo sha256 del array de reglas; restore verifica hash y el
  desajuste falla con informe.
- **A2 · Ideología/legal (§1/§10/§2):** la propuesta celebra fuentes grises de cine/streaming y
  cita catálogos con sitios concretos — para un mantenedor eso es superficie de riesgo.
  **Fix:** invariante de neutralidad como Meta 09: la app no incluye NINGUNA fuente; los feeds
  solo presentan entradas de fuentes que el usuario ya instaló; content_type usa «video» neutro;
  los catálogos se citan como evidencia de mercado, no como contenido.
- **A3 · «Zero telemetry» ambiguo (§6.2/§6.3):** las actualizaciones del modelo SON red entrante;
  tal cual, el test modo-avión parece contradecir el ciclo de vida del modelo.
  **Fix:** invariante exacto: «nada derivado del usuario sale jamás del dispositivo; la única red
  es el canal de actualización de la app para los binarios del modelo; las pruebas de aceptación
  (avión/frío) cubren el pipeline de segmentación, no el canal de updates».

### MEDIOS
- **M1 · Promesa de pared sin medida (§2.2):** «bound the worst-case refresh to a few seconds» es
  hand-waving — el spec no vende segundos. **Fix:** el tope es el presupuesto por páginas
  (P páginas × ≤20 fuentes), config por tier de dispositivo y medida en fixtures de QA — sin
  promesas de reloj en el spec.
- **M2 · mode:"ai" nunca ejemplificado en feeds.json.** **Fix:** tercer feed de ejemplo con
  perfil ai (y las constantes de histéresis viven ahí — M3).
- **M3 · Constantes de histéresis sin dueño:** «named config» pero sin lugar. **Fix:** viven en el
  perfil ai del feed (`"ai": {"hysteresis": {"threshold": 0.90, "margin": 0.15}}`).
- **M4 · Inventario de badges disperso:** «también en…», «leyendo desde…·canónica en…»,
  «posible duplicado», «stale», «fuente faltante» — listarlos en una tabla única para evitar
  deriva de UI. **Fix:** tabla de badges en §5.1.

### BAJOS / PROCESO
- **B1 · Residual de versión:** el AC de Fase 2 del md decía «schema v2.1» (gemelo del bug HTML
  ya cazado). **Fix:** → v2.3 (la subida a v2.4 cubre el documento entero).
- **B2 · Deriva terminológica descartada:** work_key/«Sin asignar» usados con constancia salvo C3
  («unclassified» → unificado). Etiquetas de versión en títulos de sección = marcadores
  históricos, se congelan tal cual.
- **B3 · El verificador verificado:** batería B — 2 bugs MÍOS de autoría de test (desestructurar
  sin WEIGHTS; expectativa 7 copiada del caso anime cuando movie∪Action=5), 0 fallos del código
  de las demos. Lección: la expectativa del test se deriva, no se copia.

## BATERÍAS EJECUTADAS (evidencia)
- **A (consistencia md):** 20 secciones mapeadas · 0 refs § rotas · JSON parsea (2 feeds) ·
  schema feed.v2.3 ×2 en cuerpo · 1 residual `schema v2.1` (B1) · constantes 0.90/0.15/90/20
  presentes · sin «a few seconds» en el md (el hand-waving vive solo en el HTML → M1 aplica al
  envase y al re wording).
- **B (estrés de demos, node/vm sobre el JS extraído del HTML vivo):** vacíos totales sin colgar
  ×3 políticas · 1 fuente/1 ítem sobrevive · NFKD fullwidth/café-precompuesto/emoji/«A — B» ==
  sus normalizaciones · weighted 9:1:1 → AABC sin inanición de B/C · 3 variantes de título → 2
  duplicados · 0 entradas → 0 · nada pega → pozo · OR con géneros vacíos no explota. **13/13
  efectivos** (el 1 fallo era del test, B3).

## ESTADO
Fixes CRÍTICOS + ALTOS + M1–M4 + B1 aplicados como **v2.4** (md + HTML) en este mismo turno;
re-sellados y re-validados. Los hallazgos quedan aquí como acta de demolición — la vara roja
se queda montada: cada ronda nueva del administrador se compara contra esta lista.
