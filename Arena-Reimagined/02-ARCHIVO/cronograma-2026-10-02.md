# CRONOGRAMA — Arena-Reimagined — 2-oct-2026

El suelo que pidió el dueño. «Este solo será tu suelo, la base; no tu cielo.»
Vigencia: hasta que el dueño la revoque. Cada fase cierra con acta y sha16.
Toda modificación queda documentada (orden E). Nada se publica sin aceptación expresa (R-07).

---

## FASE 1 — CONCLUSIÓN DEL CANON (prioridad 1 de la orden)

Objeto: los CUATRO ARCHIVOS soberanos (+ fuentes heredadas intactas hasta firma de purga).
Rumbo: **concluir, no inflar** (R-11). Sin meta de crecimiento; cada archivo termina donde su
contenido real termina.

| Paso | Qué | Puerta de calidad |
|---|---|---|
| 1.1 | Auditoría A-1→A-4: enumeración con aserción mecánica, numeración, duplicados (shingles), escáner de anomalías, gramática | 0 deficiencias por volumen |
| 1.2 | Cirugía correctiva (solo reparación; crecimiento neto = cero) | diffs PRE/post por volumen |
| 1.3 | Volumen de conclusión por archivo: acta fechada + sha16 al padrón | archivo declarado CONCLUIDO |
| 1.4 | Mapa de purga propuesto (fuentes heredadas → qué se archiva) | firma del dueño (PADRON §6) |

Entregable: 4 archivos con «Edición Concluida» + informe de defectos reparados + mapa de purga.
Cadencia: un archivo por jornada como máximo (A-1 es el grande: se parte en tramos).

## FASE 2 — ESQUEMAS DE PUBLICACIÓN (antes de ninguna pluma)

Por cada pieza pendiente (WA 72 + FB re-trabajos) un esquema detallado en `02-ARCHIVO/_esquemas/`:
secciones, tesis, fuentes a verificar con hora (escaneo concurrente + ingeniería inversa donde
haya código), novedades del ecosistema aplicables (Animiru-org → 14/19 · sozo muertas → 44 ·
WinNative 0.7.1 → 80 · Yōkai 1.10.2 → 15 · Kototoro 2.2.6 → 02/07 · Houri 1.23.2 → 16),
innovación real que aporta la pieza (no mero cambio de fecha), y vara de banda prevista.

## FASE 3 — HORNEADO WHATSAPP ES (lista pendiente: 00, 02, 11–80 = 72 fichas)

Banda nueva (R-10): objetivo 62.500–63.150 c · techo duro 63.200 c · len() UTF-8.
Primer tren: recorte documentado de WA 01 (63.947) y WA 10 (63.688).
Tren tipo (par de piezas): esquema → verificación viva de fuentes (hora en acta) → pluma nativa
(sin markdown, R-02; estilo_casa.py como herramienta, vara humana revisa) → cirugía (escáner +
enumeración + banda + greps R-01/R-06) → acta del tren + sha16 → export auditoría PRE/post.
Cadencia: 4–8× según decisión vigente del dueño, sin apurar — un tren bueno antes que cinco apurados.

## FASE 4 — RE-AUDITORÍA FACEBOOK ES (todas las versiones, per orden G)

1. Dedupe: gemelas de slug viejo → `_versiones/` (03, 04, 05, 06, 07, 08, 09, 15).
2. Re-trabajo al formato nuevo de las que nunca lo tuvieron (00, 11–14, 16–17, 18–80).
3. Expansión documentada al piso ≥45.000c (R-10) de TODAS — patrón _auditoría-30sep (PRE/post).
4. 00 y 78: si reclaman exención histórica de banda, se somete a palabra del dueño en acta.

## FASE 5 — RÉPLICAS (idiomas · plataformas) — SOLO POR ORDEN

La base nueva solo contiene ES (FB/WA). El legado multilingüe (7 lenguas × 8 plataformas, era
04-VERSIONES) queda archivado en `02-ARCHIVO/` hasta que el dueño ordene su destino.

## RITUAL DIARIO (transversal)

- Apertura: barrido total del ecosistema + registro fechado ANTES de hornear.
- Forma de la jornada declarada (hielo/agua/vapor/gota) en padrón y acta (PADRON §7).
- Actas del tren con números; nada fuera del registro.
- Operación de entrega: sin PAT no hay push — cada cierre de fase genera ZIP/patch para que el
  dueño sincronice al repo desde su móvil (o PAT en env para empujar directo).

## ORDEN DE EJECUCIÓN

HOY (2-oct): Fase 0 ejecutada (reconocimiento + bandas + choques + este cronograma).
Siguiente jornada: **Fase 1.1** (auditoría del canon), empezando por A-1 en tramos.
Las fases 2–3 arrancan cuando la Fase 1 entregue su primer archivo concluido (o antes, si el
dueño prioriza las publicaciones — palabra suya manda).
