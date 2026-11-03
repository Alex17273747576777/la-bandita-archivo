# La Bandita — archivo, ley y frontend

*Una casa que verifica antes de recomendar. Todo dato que aparece aquí tiene fecha, método y evidencia; lo que no se pudo medir se publica como hueco declarado, nunca rellenado.*

**TL;DR —** este repositorio es un **archivo de divulgación técnica en español** sobre aplicaciones y recursos de código abierto para Android, con **una guía maestra de 70 fichas en 12 capítulos** y **dos series de canal** (Facebook y WhatsApp) que van por la pieza 5 de 14. Todo lo que declara se puede comprobar con un comando: `make verificar`. Si venís con prisa, empezá por `make doctor` y por la tabla de estado de abajo. Si venís a leer, la puerta es `guia-maestra/`. Si venís a auditar, la puerta es `ARQUITECTURA.md`.

---

## Antes de nada: una disculpa

Este archivo llegó a tener la raíz con veintinueve entradas, las dos carpetas de canal con **números repetidos** —dos piezas 04 y dos piezas 05 en la misma carpeta— y actas que citaban rutas que ya no existían. Quien abría el repositorio no podía saber qué era presente y qué era memoria, y eso es un fallo de quien lo ordenó, no de quien lo lee.

Se corrigió: el presente quedó en la puerta, el pasado en `ARCHIVO-HISTORICO/` con su fecha y un mapa que traduce las rutas viejas. **Lo ya publicado no se reescribió**: se conserva con sus fallos y se corrige hacia adelante, porque un archivo que se retoca solo es un archivo que no se puede citar. Lo que sigue abierto se declara en [`docs/TAREAS.md`](docs/TAREAS.md), no se esconde.

---

## Estado del archivo, hoy (3 de noviembre de 2026)

| Qué | Dónde | Estado |
|---|---|---|
| **Guía maestra** | `guia-maestra/` | 12 capítulos · **70 fichas** medidas · compuertas en cero fallos |
| **Serie de Facebook** | `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/` | piezas **01 a 05** publicadas, en banda · siguiente: **06 · El taller** |
| **Serie de WhatsApp** | `Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES/` | piezas **01 a 05** publicadas, en banda · siguiente: **06 · El taller en el bolsillo** |
| **Todo lo anterior** | `_ARCHIVO-HISTORICO/` de cada canal · `ARCHIVO-HISTORICO/` en la raíz | archivado por mes, con su fecha; no se borra, no se retoca |
| **Registro medido** | `registry/` | **6.838 fichas** conformes al contrato de datos v1 |
| **Sello** | `registry/_manifiesto-sha256.tsv` · `attestations/` | SHA-256 encadenado + firma sin llave de Sigstore |

El mapa completo, con la traducción de rutas antiguas, está en **[`MAPA-DEL-ARCHIVO.md`](MAPA-DEL-ARCHIVO.md)**. El estado pieza por pieza está en el `LEEME-de-la-carpeta.md` de cada canal; la comprobación de todo eso, en `docs/ACTA-ORDEN-Y-VERIFICACION-2026-11-03.md`; el porqué de cada decisión de estructura, en **[`ARQUITECTURA.md`](ARQUITECTURA.md)**.

---

## Arranque en tres comandos

```bash
make doctor      # ¿está todo en su sitio? cinco bloques y un veredicto
make verificar   # registro + sello + 16 compuertas + autoprueba → «fallos: NINGUNO»
make ayuda       # los catorce destinos del Makefile, con una línea cada uno
```

No hace falta instalar nada más que Python 3.11 o superior. El sitio que se genera no usa CDN, ni fuentes externas, ni una sola dependencia de terceros: sale HTML y CSS propios.

**Si querés ver lo que hay antes de leer código:**

```bash
python3 tools/sitio.py            # escribe site/ — índice, piezas, fichas, RSS
python3 tools/tareas.py           # escribe docs/TAREAS.md — el tablero de tareas abiertas
python3 tools/indice_docs.py      # escribe docs/INDICE.md — 49 documentos con su resumen
```

**Si vas a publicar una pieza:**

```bash
python3 tools/manual_gate.py --pieza "…/06-…md"     # manual v3.0, M01–M23
python3 tools/novedad_gate.py --corte               # M24–M28, lo que ya se dijo
make sellar && make verificar                       # sello nuevo y vara completa
```

Las llaves (`GHP_A`, `PAT_FINO`) viven **fuera del repositorio**, en `~/.boveda/tokens.env` con permisos `600`. Ninguna herramienta las imprime ni las escribe en el árbol, y `make push` rechaza cualquier llave que no empiece por `github_pat_`.

---

## Cómo está organizado

Tres capas, y cada una se cambia a distinto ritmo a propósito. El detalle y el coste de cada decisión están en `ARQUITECTURA.md`.

| Capa | Dónde | Qué contiene |
|---|---|---|
| **Ley** | `CIMIENTOS/` · `corpus-la-bandita/` · `PROCESOS/` | Principios, precedencia, criterios obligatorios C-01 a C-24, Manual de Estilo y Operaciones V3.0, contrato de datos, raya legal |
| **Oficio** | `tools/` · `SKILLS/` · `registry/` · `schemas/` | Las **31 herramientas** que miden, comprueban y sellan, las habilidades ejecutables y las fichas medidas con su esquema |
| **Producto** | `guia-maestra/` · `Arena-Reimagined/01-PUBLICACIONES/` · `site/` | La guía de doce capítulos, las piezas de los dos canales y el sitio generado |

```
CIMIENTOS/  corpus-la-bandita/  PROCESOS/  SKILLS/  LEGAL/     la ley y el oficio
tools/                     las 31 herramientas (explicadas en docs/CODIGO.md)
registry/  schemas/        6.838 fichas medidas y el contrato que las valida
guia-maestra/              datos · textos · sitio · CREDITOS.md
Arena-Reimagined/
  01-PUBLICACIONES/
    Facebook-dominicano-ES/   5 piezas vivas + LEEME + hash de 135 archivos
    WhatsApp-dominicano-ES/   5 piezas vivas + LEEME + hash de 112 archivos
    POSTS-COMUNIDAD/          las historias del muro, que no son piezas de la serie
docs/                      actas, políticas, bandas, envíos, tableros y este índice
site/                      el frontend generado, sin CDN ni dependencias
attestations/              sellos SHA-256 encadenados y firmas de Sigstore
ARCHIVO-HISTORICO/         la memoria: ocho carpetas de etapas anteriores, con su manifiesto
```

**Regla de oro del árbol:** el Markdown es la fuente y el HTML es la salida. Nada se corrige en `site/`; se corrige en la pieza y se regenera. Y la regla que decide qué es código y qué es texto: **lo que es dato se genera, lo que es enseñanza se escribe.**

*Deuda declarada, no oculta:* `Arena-Reimagined/` conserva carpetas de etapas anteriores (`_versiones/`, `packs/`, `_herramientas/`) que hoy tienen 43, 81 y 26 referencias vivas. Se moverán en una pasada dedicada, con sus referencias corregidas en el mismo cambio; hasta entonces este mapa las nombra en vez de fingir que no están.

---

## Documentación, para quien llega

| Quiero… | Voy a |
|---|---|
| Entender cómo está hecho y por qué | [`ARQUITECTURA.md`](ARQUITECTURA.md) |
| Saber qué hace cada herramienta | [`docs/CODIGO.md`](docs/CODIGO.md) — 31 programas, con «qué no hace» cada uno |
| Ver qué falta y qué está declarado | [`docs/TAREAS.md`](docs/TAREAS.md) — tablero generado, 12 tareas |
| Encontrar un documento entre 47 | [`docs/INDICE.md`](docs/INDICE.md) |
| Aportar algo | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Reportar un fallo de seguridad | [`SECURITY.md`](SECURITY.md) — en privado, 48 h |
| Saber qué cambió y cuándo | [`CHANGELOG.md`](CHANGELOG.md) |
| Convivir sin fricción | [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) |
| Pedir ayuda sin perder tiempo | [`SUPPORT.md`](SUPPORT.md) |

Los archivos de salud comunitaria siguen la práctica estándar de GitHub, las confirmaciones siguen [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), el registro de cambios sigue [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) y la licencia por archivo sigue las prácticas de [REUSE](https://reuse.software/) de la FSFE: `reuse lint` sale conforme sobre **13.811 archivos**. Adoptar la convención no es moda: es que otro pueda auditar sin preguntarnos nada.

---

## Cómo se trabaja aquí

1. **Medir** con `SKILLS/medir-recurso`: tres lecturas, orden rotado, ventana horaria de Santo Domingo.
2. **Escribir** con `SKILLS/escribir-pieza`: tandas de contenido real hasta la banda declarada.
3. **Compuerta** con `SKILLS/compuerta-manual`: M01–M23; rojo no se publica, y una pieza no se «arregla» bajando el umbral.
4. **Enviar** con `SKILLS/envio-canal`: los envíos se generan y se verifican, no se escriben a mano.
5. **Sellar y publicar** con `SKILLS/sellar-y-publicar`: acta, atestación, `vara.py`, integración continua y push.
6. **Reportar** con `SKILLS/informe-al-dueño`: cifras con hora, sin relleno.

El orden no es opcional: cada paso produce la evidencia que el siguiente comprueba. Y ninguna compuerta se aprueba por salir en cero: se aprueba cuando el informe **dice** `fallos: NINGUNO` y ese texto queda en el registro.

---

## Los números, y lo que no dicen

| Indicador | Valor del corte | Cómo se comprueba |
|---|---|---|
| Archivos sellados | **10.196** | `tools/atestar.py --verificar` |
| Fichas del registro | 6.838 | `tools/vara.py`, compuerta G1 |
| Compuertas | **G0 a G15**, ninguna en rojo | `tools/vara.py` |
| Piezas del archivo | 258 (5 + 5 vivas, el resto en histórico) | G0 |
| Envíos verificados | 5 + 5, cero fallos | `tools/envio.py --verificar` |
| Tareas abiertas | 12 | `tools/tareas.py` |
| Dependencias externas del sitio | 0 | `tools/sitio.py` |
| Paquetes de terceros alojados | 0 | política de la raya legal |

Lo que estos números **no** dicen: que el archivo esté terminado (el ciclo va por la pieza 5 de 14), que la guía no pueda mejorar (sí puede), ni que el método sea el único (es el que se puede repetir, que es lo único exigible). Hay dos deudas congeladas y declaradas en `tools/baseline.json`: una pieza del histórico sin latido y cinco sin novedad medida. Están a la vista porque esconderlas habría sido más caro que decirlas.

---

## Procedencia, sin adornos

El historial git de una etapa anterior se perdió truncado por límites del entorno. El contenido se restauró **verificado por SHA-256** contra el catálogo sellado —cero fallos— y no como clon de la historia. Esa etapa está citada en `Arena-Reimagined/02-ARCHIVO/` y su manifiesto en `ARCHIVO-HISTORICO/MANIFIESTO-2026-10.md`. El historial posterior sí está completo en este repositorio, confirmación por confirmación.

---

## Licencias

| Qué | Licencia | Archivo |
|---|---|---|
| Código (`tools/`, servidor MCP, flujos) | MIT | [`LICENSE`](LICENSE) |
| Contenido editorial (piezas, guía, docs) | CC BY-SA 4.0 | [`LICENSE-CONTENIDO`](LICENSE-CONTENIDO) |
| Datos y registro (fichas, censos) | CC BY 4.0 | [`LICENSE-DATOS`](LICENSE-DATOS) |
| Marca, nombre y sello de verificación | Reservados | [`NOTICE`](NOTICE) |

Los metadatos de proyectos de terceros se citan con fines de verificación y conservan la licencia de su origen. **Este archivo no relicencia código ajeno ni aloja paquetes de nadie.**

*La Bandita informa a partir de fuentes fechadas.*
