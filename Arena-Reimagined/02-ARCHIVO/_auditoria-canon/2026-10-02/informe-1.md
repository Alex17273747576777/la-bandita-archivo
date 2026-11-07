# INFORME-1 — Auditoría de los CUATRO ARCHIVOS soberanos (Fase 1.1)
Fecha: 2-oct-2026 · Forma de la jornada: HIELO · Vara: len() UTF-8 + slugger GitHub exacto
Método: censo estructural → clasificación de anomalías → aserción de enumeraciones →
shingles (12-gramos) → anclas internas con slugger real → cirugía documentada (PRE/diffs/sha16).

## Veredictos

### Limpio (0 defectos)
- Mojibake (Ã©/â€): 0 en los cuatro. Cero-anchos (ZWSP/ZWNJ/BOM): 0. U+FFFD: 0. Caracteres de control: 0.
- Fences de código: paridad correcta en los cuatro.
- Enumeración R-01…R-24 (A-1): secuencia completa sin huecos.
- Fichas F-076…F-092 (A-3): secuencia completa sin huecos.
- A-4 (Lecciones): 0 headings duplicados, 0 secciones vacías, 0 shingles repetidos.

### Anomalías clasificadas como LEGÍTIMAS (evidencia citada / estructura)
- Hanzi «硬件设施已经老» / «更高的» (A-2 ×2 citas, A-3 ×1 acto, A-4 ×1 lección) y kana «の» (A-1):
  son citas verbatim de los 48 tramos malogrados históricos — la evidencia ES el contenido.
  (15+7+7+1 hits a nivel de carácter, no defectos activos.)
- «TODO el corpus» (A-1, LEY R-09) y «F-XXX» (motor): español e intencional — falsos positivos del escáner.
- Fórmula sellada 180× (A-1, «La combinación exige…») y 75× (A-2/A-3, «se evalúa contra los
  principios de honestidad…»): sello por unidad (75 = exactamente las fichas F-001–F-075) —
  estructura, no duplicación. Contextos verificados: cada sello sigue texto distinto.
- Años 2008/2010 (A-4): «Cámbiate» (2008) y Canserbero, álbum Vida (2010) — citas culturales legítimas.
- Homónimo de series F: «Fichas F-076+» (fallos) vs «Art. F-200…F-903» (capa de fusión A-1) —
  series distintas bajo misma letra. OBSERVACIÓN estructural para el dueño (renombrar = decisión suya).

### Defecto real encontrado y REPARADO (Fase 1.2)
**310 enlaces internos muertos (TOC → sección) en los cuatro soberanos** — causa raíz: los enlaces
perdieron la raya larga de los headings («Familia A — Veracidad» → enlace `a-veracidad` en vez de
`a--veracidad`) y, en A-4, fechas del TOC que no coinciden con las de las lecciones (09-14 vs 09-13).
Cirugía: reescritura de enlaces al slug verdadero (jamás se tocaron headings ni fechas de actas).
- A-1: 100 enlaces · sha16 49f8f2c88ae3bcda → cc92b3c009db418a · diff 387 líneas
- A-2:  91 enlaces · sha16 3df46b380636d3fd → 504c8aa7d41dc5f4 · diff 218 líneas
- A-3:  84 enlaces · sha16 28b6301a270b0023 → 30d0aabefcf15828 · diff 181 líneas
- A-4:  35 enlaces (17 únicos) · sha16 7b096fc7a9d241eb → 6d00d9586425d57d · diff 75 líneas
- Re-verificación: **0 anclas rotas restantes** en los cuatro. PRE + diffs en esta carpeta.

### Pendiente de palabra del dueño (candidatos al mapa de purga — NO se tocó)
1. Art. N-701…N-704 (A-1): shells vacíos donde el título promete «Checklists/Plantillas con
   ejemplo completo/Prompts canónicos/FAQ» — 4 artículos sin contenido.
2. Shells de anexos «propuestos» (M, N, O, P) y registros V32.x vacíos (A-1) — declarados propuesta.
3. Cabezas de Libro consecutivas sin cuerpo directo (índice-de-libros) — probablemente estructura
   de índice; confirmar si cada Libro tendrá desarrollo propio o se fusionan.
4. La heredada FICHAS/A-3: A-2 y A-3 comparten la sección de 75 fichas (por diseño R-08, «en los
   archivos 2 y 3») — confirmar que la duplicidad entre archivos es intención y no carga muerta.

## Conclusión Fase 1.1 (primer paseo completo)
Los cuatro soberanos están estructuralmente sanos tras la cirugía de anclas: 0 anomalías activas,
enumeraciones íntegras, duplicación cero fuera de sellos por unidad. Lo que resta del «concluir»
es palabra del dueño (purga de shells) y los volúmenes de conclusión (Fase 1.3: acta + sha16 al
padrón por archivo). Fuentes heredadas: intactas (PADRÓN §6) hasta firma del mapa de purga.

---
## RECTIFICACIÓN (nano-lote, misma noche)
El «Defecto pendiente» nº 1 (Art. N-701–704 vacíos) se RETIRA: el bloque tiene 94.505 c de
contenido real; mi detector de vacíos marcaba heading+sub-heading como vacío (falso positivo
estructural). Los puntos 2–5 de purga se re-examinarán con el detector corregido antes de
cualquier palabra del dueño. La vara también se audita a sí misma.

## VEREDICTO PUNTO 2 (detector corregido)
De los ~25 sospechosos, A-1 tiene SOLO 2 vacíos reales — y son un mismo bloque hueco:
«# CAPA VI — MEMORIA DE SESIONES VERIFICADAS (V32.4: propuesta canonizable)» + su
«## Registro de actualización V32.4» vacío. Los anexos M/N/O/P, los Libros y los registros
V32.x restantes TIENEN contenido o hijos: no son vacíos. Purga se reduce a UNA decisión.
