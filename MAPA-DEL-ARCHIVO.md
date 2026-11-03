# MAPA DEL ARCHIVO

*La puerta única. Si un acta vieja cita una ruta que ya no existe, aquí está su traducción. Actualizado el 3 de noviembre de 2026.*

**TL;DR —** el presente está en la puerta y el pasado en `ARCHIVO-HISTORICO/`, con su fecha y su manifiesto. Las dos series de canal van por la pieza **5 de 14**; la siguiente es la **06 · El taller** en Facebook y **06 · El taller en el bolsillo** en WhatsApp. La guía maestra está completa: **12 capítulos y 70 fichas**. Todo lo que este mapa declara se comprueba con `make verificar`.

---

## La regla que ordena todo

**El presente en la puerta; el pasado en su carpeta y con su fecha.** Nada se borra y nada se reescribe hacia atrás: lo que cambió se corrige hacia adelante y la corrección queda anotada. Quien abre una carpeta tiene que saber en un segundo qué se está publicando hoy y qué es memoria.

---

## Tres capas

| Capa | Dónde | Qué contiene |
|---|---|---|
| **Ley** | `CIMIENTOS/` · `corpus-la-bandita/` · `PROCESOS/` | Principios, precedencia, criterios C-01 a C-24, Manual de Estilo y Operaciones V3.0, contrato de datos, licencias y raya legal |
| **Oficio** | `tools/` · `SKILLS/` · `registry/` · `schemas/` | Las 31 herramientas que miden, sellan y comprueban, las habilidades ejecutables y las fichas medidas |
| **Producto** | `guia-maestra/` · `Arena-Reimagined/01-PUBLICACIONES/` · `site/` | La guía de doce capítulos, las piezas de los dos canales y el sitio generado |

---

## Los dos ciclos vivos

**La guía maestra.** Doce capítulos, setenta fichas, cada una con autor, licencia, versión y fecha de medición. Vive en `guia-maestra/`: los datos en `datos/apps/`, los textos en `texto/capitulos/`, las páginas en `sitio/` y los créditos en `CREDITOS.md`. Se genera y se valida con un solo comando:

```bash
python3 guia-maestra/herramientas/guia_maestra.py --compuertas --generar --estricto
```

**La serie de canal.** Dos carpetas, un ciclo de catorce piezas cada una, y **cada canal se lee 01 → 14 sin saltos**:

| Canal | Dónde | Banda de longitud | Va |
|---|---|---|---|
| Facebook | `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/` | 40.000–45.000 caracteres | primero |
| WhatsApp | `Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES/` | 63.000–63.099 caracteres | después |

La segunda no es la primera recortada: es otro texto, porque la compuerta M23 prohíbe párrafos idénticos entre canales. En las dos carpetas la raíz contiene **solo las piezas del ciclo** más un `LEEME-de-la-carpeta.md` con la tabla de estado; todo lo anterior vive en `_ARCHIVO-HISTORICO/` de cada carpeta, ordenado por mes.

---

## Estado del ciclo, hoy

| Canal | Piezas vivas | Longitudes medidas | Siguiente |
|---|---|---|---|
| Facebook | **01 a 05** | 40.253 – 44.994 | **06 · El taller** |
| WhatsApp | **01 a 05** | 63.006 – 63.098 | **06 · El taller en el bolsillo** |

El plan completo, que no cambia de esta pasada: 01 la puerta y el recibo · 02 la música · 03 la caja del bolsillo · 04 la lista del permiso · 05 la guía maestra · **06 el taller** · 07 la pantalla grande · 08 la red · 09 archivos y nubes propias · 10 privacidad comprobable · 11 cuando algo se rompe · 12 el oficio · 13 la remisión de diciembre · 14 la lista del día uno.

Las tablas pieza por pieza, con fecha de corte, están en el LEEME de cada carpeta y en `docs/TAREAS.md`.

---

## Qué es cada pieza, para no confundirlas

| Pieza | Qué enseña | Quién la usa |
|---|---|---|
| **Guía maestra** | Las 70 fichas con autor, licencia y fecha, en 12 capítulos | quien llega por primera vez y quiere el mapa entero |
| **Piezas de Facebook** | Un tema por entrega, con el método a la vista y el largo que permite leer en el muro | quien lee con calma y comparte |
| **Piezas de WhatsApp** | Otro texto, más largo y más conversacional, para reenviar por mensaje | la familia que recibe un reenvío |
| **Posts de comunidad** | Historias del muro, sin numeración de serie | el que ya sigue el archivo |
| **Envíos** (`docs/envios/`) | La pieza ya medida y troceada en mensajes, verificada | quien publica |

---

## Dónde está cada cosa

```
guia-maestra/                 la guía: datos, textos, páginas y créditos
Arena-Reimagined/
  01-PUBLICACIONES/
    Facebook-dominicano-ES/   ciclo vivo + LEEME-de-la-carpeta + _ARCHIVO-HISTORICO
    WhatsApp-dominicano-ES/   ciclo vivo + LEEME-de-la-carpeta + _ARCHIVO-HISTORICO
    POSTS-COMUNIDAD/          las historias del muro, que no son piezas de la serie
  00-CANON/                   los cuatro archivos de la casa
  02-ARCHIVO/                 registro de hitos y evidencia de las jornadas
registry/                     las 6.838 fichas medidas, la materia prima de todo
schemas/                      el contrato de datos: la forma que toda ficha debe cumplir
docs/                         compuertas, bandas, envíos, actas, tableros
  bandas.json                 la banda de longitud de cada pieza viva
  TAREAS.md                   el tablero de tareas, generado por tools/tareas.py
  INDICE.md                   los 49 documentos con su resumen, generado
  CODIGO.md                   qué hace y qué no hace cada una de las 31 herramientas
  envios/<canal>/             los envíos listos para mandar
  envios/_historico/          los envíos de las piezas que pasaron al archivo
tools/                        las herramientas: vara, compuertas, medición, sellado, sitio
site/                         el frontend generado, sin CDN ni dependencias
attestations/                 los sellos encadenados y sus firmas sin llave
CIMIENTOS/ · PROCESOS/ · SKILLS/ · corpus-la-bandita/    la ley y el oficio
ARCHIVO-HISTORICO/            la memoria del repositorio, en un solo sitio
```

---

## `ARCHIVO-HISTORICO/`, la memoria

Ocho carpetas de etapas anteriores y dos índices. Se leen; no se ordenan ni se retocan, porque un archivo histórico que se reescribe deja de servir como prueba.

| Carpeta | Qué fue |
|---|---|
| `03-PUBLICACIONES-2026-09-15/` | la tanda de publicaciones del 15 de septiembre |
| `04-VERSIONES-MULTIIDIOMA/` | las versiones en otros idiomas, antes del giro a español de origen |
| `backup-previo-correccion-14-09/` | copia anterior a la corrección del 14 de septiembre |
| `archivo/` | el archivo de la primera etapa |
| `site-demo/` | el panel de resultados autocontenido de la entrega de diseño |
| `datos-censo/` · `datos-miyomi/` · `datos-v25/` | los censos crudos de los que salieron las fichas |
| `INDICE-2026-10.md` · `MANIFIESTO-2026-10.md` | el índice y el manifiesto de esa memoria |

**Traducción de rutas.** Si un acta vieja cita una ruta de esta tabla, la ruta viva es `ARCHIVO-HISTORICO/<lo mismo>`:

| Antes (raíz) | Ahora |
|---|---|
| `03-PUBLICACIONES-2026-09-15/` | `ARCHIVO-HISTORICO/03-PUBLICACIONES-2026-09-15/` |
| `04-VERSIONES-MULTIIDIOMA/` | `ARCHIVO-HISTORICO/04-VERSIONES-MULTIIDIOMA/` |
| `backup-previo-correccion-14-09/` | `ARCHIVO-HISTORICO/backup-previo-correccion-14-09/` |
| `archivo/` | `ARCHIVO-HISTORICO/archivo/` |
| `site-demo/` | `ARCHIVO-HISTORICO/site-demo/` |
| `datos-censo/` · `datos-miyomi/` · `datos-v25/` | `ARCHIVO-HISTORICO/<lo mismo>` |
| `_archivo-historico/INDICE.md` | `ARCHIVO-HISTORICO/INDICE-2026-10.md` |
| `_archivo-historico/MANIFIESTO.md` | `ARCHIVO-HISTORICO/MANIFIESTO-2026-10.md` |
| `00-LEEME-de-la-carpeta.md` (canal) | `LEEME-de-la-carpeta.md` |

Las tres herramientas que apuntaban a las rutas viejas —`tools/duplicados.py`, `tools/idioma_mojibake.py` y `tools/sitio.py`— se corrigieron en el mismo cambio que movió las carpetas. Mover sin corregir referencias es exactamente el error que produjo el desorden anterior.

---

## Deuda declarada

No todo se movió, y decirlo es parte del arreglo:

- **`Arena-Reimagined/`** conserva carpetas de etapas anteriores (`_versiones/` 43 referencias, `packs/` 81, `_herramientas/` 26, más las entregas en zip). Se moverán en una pasada dedicada, con las referencias corregidas en el mismo cambio. Hoy este mapa las nombra en vez de fingir que no existen.
- **`uploads/`** se mantiene en la raíz porque es la carpeta de entrada de material nuevo; su contenido está declarado, no disperso.
- **Dos deudas congeladas** en `tools/baseline.json`: una pieza del histórico sin latido (G0) y cinco sin novedad medida (G13). Están a la vista y no crecen.

---

## Cómo se comprueba lo que declara este mapa

Tres métodos, y los tres tienen que coincidir. El acta con las corridas y sus números es `docs/ACTA-ORDEN-Y-VERIFICACION-2026-11-03.md`.

1. **El árbol y su contenido** — contar lo que hay y sellar cada archivo con su suma de verificación (`tools/atestar.py`).
2. **La fuente remota** — preguntarle a la plataforma, sin el clon de por medio, qué archivos hay y de qué tamaño, y comparar contra lo sellado.
3. **La coherencia interna** — que la fecha del nombre, el dateline y el tamaño declarado en `docs/bandas.json` coincidan con la huella anotada en el envío, del mismo archivo.

Y al final, la vara: `make verificar` tiene que terminar diciendo **`fallos: NINGUNO`**. Ninguna compuerta se aprueba por salir en cero; se aprueba cuando el informe lo dice y ese texto queda en el registro.

*La Bandita informa a partir de fuentes fechadas.*
