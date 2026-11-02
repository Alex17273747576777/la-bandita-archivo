# La Bandita — archivo, ley y frontend

Una casa que **verifica antes de recomendar**. Todo dato que aparece aquí tiene fecha, método y
evidencia; lo que no se pudo medir se publica como hueco declarado, nunca rellenado.

Este repositorio es tres cosas a la vez, y cada una vive en su sitio:

| Capa | Dónde | Qué contiene |
|---|---|---|
| **Ley** | `CIMIENTOS/` + `corpus-la-bandita/` | Principios, precedencia, criterios obligatorios (C-01…C-24), Manual de Estilo y Operaciones V3.0, contrato de datos, licencias, raya legal |
| **Conocimiento operativo** | `SKILLS/` + `PROCESOS/` | Habilidades ejecutables (una carpeta por skill, con `SKILL.md`) y flujos de trabajo paso a paso |
| **Producto** | `Arena-Reimagined/01-PUBLICACIONES/` + `site/` | Las piezas publicadas (Markdown, fuente de verdad) y el frontend HTML que las ordena (generado) |

---

## Arranque rápido

```bash
# 1 · estado del archivo: las compuertas en un comando
python3 tools/vara.py                 # 12 compuertas G0–G12; «fallos: NINGUNO» = verde

# 2 · una pieza concreta, contra el manual v3.0 (M01–M23)
python3 tools/manual_gate.py --pieza "Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/25-...md"

# 3 · regenerar el frontend (sitio estático, cero CDN)
python3 tools/sitio.py                # escribe site/ — index, piezas, registro, fichas, RSS

# 4 · medir recursos y generar los envíos de canal
LBT="$PAT_FINO" python3 tools/envio.py --medir
python3 tools/envio.py --generar --canal ambos && python3 tools/envio.py --verificar
```

Las llaves (`GHP_A`, `PAT_FINO`) viven **fuera del repositorio**, en `/home/user/.boveda/tokens.env`.
Nunca se imprimen ni se versionan, y ninguna herramienta las escribe en un archivo del árbol.

---

## Mapa del repositorio

```
CIMIENTOS/                  Norma: índice, precedencia, contrato de datos, licencias, método
SKILLS/                     Habilidades: una carpeta por skill, con frontmatter y verificación
PROCESOS/                   Flujos: pieza, lote, publicación, cadencia, frontend
corpus-la-bandita/          Documentos fundacionales (CIMIENTOS canónico y Manual V3.0 viven aquí)
Arena-Reimagined/
  01-PUBLICACIONES/         Piezas Markdown: Facebook-dominicano-ES · WhatsApp-dominicano-ES · POSTS-COMUNIDAD
  02-ARCHIVO/               Catálogo histórico, packs de fuentes, herramientas del archivo
  00-CANON/ · HABILIDADES/  Canon y habilidades de la etapa anterior (se conservan por trazabilidad)
docs/                       Actas, políticas, bandas, envíos generados, conformidad del manual
registry/                   Fichas de repositorio (contrato v1) + índice y calidad del censo
schemas/ficha.schema.json   Contrato de datos: la forma que toda ficha debe cumplir
tools/                      Medición, compuertas, envíos, sellado, sitio
site/                       Frontend generado por tools/sitio.py (no se edita a mano)
site-demo/resultados.html   Panel de resultados autocontenido (entrega de diseño)
attestations/               Sellos SHA-256 encadenados por lote
LEGAL/ · LICENSE* · NOTICE  Licencias: contenido CC BY-SA 4.0 · datos CC BY 4.0 · código MIT · marca reservada
_archivo-historico/         Legado congelado, con manifiesto: se consulta, no se edita
```

Fuera del árbol, a propósito: las **exportaciones** (ZIP del corpus, bundles) se generan cuando se
piden y no se versionan. `paquetes/` se retiró el 2-nov con acta
(`docs/ACTA-LIMPIEZA-2026-11-02.md`); el historial de git lo conserva si hiciera falta.

Regla de oro del árbol: **el Markdown es la fuente y el HTML es la salida**. Nada se corrige en
`site/`; se corrige en la pieza y se regenera.

---

## Estado del archivo (corte del 2026-11-02)

| Indicador | Valor |
|---|---|
| Piezas en `01-PUBLICACIONES` | 275 (Facebook, WhatsApp y comunidad) |
| Piezas con banda declarada | 32 en `docs/bandas.json` |
| Fichas de repositorio | 6.830 conformes al esquema v1 |
| Compuertas | G0–G12 en verde · manual v3.0 31/31 |
| Sello vigente | `attestations/`, huella encadenada por lote |
| Frontend | `site/` con una URL por pieza y por ficha, RSS y JSON-LD |

El detalle fechado de cada corte está en `docs/CONFORMIDAD-MANUAL-*.md`, no en este README.
Este README es un mapa: si discrepa con un acta, manda el acta.

---

## Cómo se trabaja aquí

1. **Medir** con `SKILLS/medir-recurso`: tres lecturas, orden rotado, ventana horaria de Santo Domingo.
2. **Escribir** con `SKILLS/escribir-pieza`: tandas de contenido real hasta la banda declarada.
3. **Gatear** con `SKILLS/compuerta-manual`: M01–M23; rojo no se publica.
4. **Enviar** con `SKILLS/envio-canal`: los envíos se generan, no se escriben a mano.
5. **Sellar y publicar** con `SKILLS/sellar-y-publicar`: acta, atestación, `vara.py`, CI y push.
6. **Reportar** con `SKILLS/informe-al-dueño`: cifras con hora y sin relleno.

El orden no es opcional: cada paso produce la evidencia que el siguiente comprueba.

---

## Procedencia (dicho sin adornos)

El historial git anterior a esta etapa vivía en el repositorio previo del proyecto y se perdió
truncado por límites del entorno. El contenido se restauró **verificado por SHA-256** contra el
catálogo sellado (0 fallos), no como clon de la historia. La historia detallada sigue citada en
`Arena-Reimagined/02-ARCHIVO/` y en `_archivo-historico/MANIFIESTO.md`.
