# 00 · Índice normativo

Este directorio **no reescribe la ley: la ordena y la enlaza**. Los dos documentos que obligan de
verdad viven en `corpus-la-bandita/` y conservan su redacción original; aquí se explica qué manda
cada uno, en qué orden y cómo se comprueba.

| Rango | Documento (fuente) | Qué obliga |
|---|---|---|
| 1 | `corpus-la-bandita/CIMIENTOS — criterios obligatorios y precedencia (1-nov-2026).md` | Los criterios C-01…C-24 en cuatro bloques (verdad, forma, prohibiciones, reglas vivas) y el **orden de precedencia** cuando dos criterios chocan |
| 2 | `corpus-la-bandita/Manual de Estilo y Operaciones La Bandita — V3.0 (1-nov-2026).md` | Voz, cabecera, mapa, «En una página», fichas, meme del corte, cierre, firma, longitud y prohibiciones de lenguaje |
| 3 | `schemas/ficha.schema.json` + `CIMIENTOS/02-CONTRATO-DATOS.md` | La forma que debe cumplir toda ficha de repositorio |
| 4 | `CIMIENTOS/03-LICENCIAS-Y-RAYA-LEGAL.md` + `LICENSE`, `LICENSE-CONTENIDO`, `LICENSE-DATOS`, `NOTICE` | Qué se cede, qué se reserva y qué no se reparte nunca |
| 5 | `CIMIENTOS/05-METODO-DE-MEDICION.md` | Cómo se mide: tres lecturas, orden rotado, ventana horaria, corte |
| 6 | `CIMIENTOS/06-PROTOCOLO-DE-ERRORES.md` | Qué se hace cuando algo sale mal: cirugía, errata, reinicio de lista |
| 7 | `docs/POLITICA-DUPLICADOS.md`, `docs/POLITICA-MCP.md`, `docs/CANAL-WHATSAPP.md` | Políticas específicas ya aprobadas por el dueño |

## Cómo se usa este índice

1. Antes de escribir: leer el rango 1 y el 2 en su fuente. No se cita de memoria.
2. Antes de publicar: pasar `tools/manual_gate.py` (M01–M23) y `tools/vara.py` (G0–G12).
3. Antes de discutir: buscar si el conflicto ya está resuelto en `CIMIENTOS/01-PRECEDENCIA.md`.
4. Nunca: crear una tercera versión de una norma que ya existe. Si hace falta matiz, se añade un
   párrafo fechado al documento fuente y se anota en `docs/ERRATA-*.md`.

## Archivos de este directorio

- `01-PRECEDENCIA.md` — orden de mando y resolución de conflictos.
- `02-CONTRATO-DATOS.md` — esquema de ficha y reglas de integridad del registro.
- `03-LICENCIAS-Y-RAYA-LEGAL.md` — cesión, marca reservada y límites de contenido.
- `04-VOZ-Y-CIERRE.md` — resumen operativo de la forma obligatoria (para tenerlo a mano).
- `05-METODO-DE-MEDICION.md` — el método, con sus ventanas y su evidencia.
- `06-PROTOCOLO-DE-ERRORES.md` — qué se hace y en qué orden cuando algo falla.
