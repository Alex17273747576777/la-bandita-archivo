# xmltv-splitter · suuhm

*tool to filter an XMLTV EPG file by specific channels. Ideal for use with TVHeadend, Plex, or any XMLTV-compatible app*

**Racimo:** radio-y-directo · **Repositorio:** `suuhm/xmltv-splitter` · **Estado:** lento · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> XMLTV Splitter is a lightweight Python script that filters large XMLTV EPG files down to only the channels you care about — by name or from a remote source.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 7 de julio de 2026 (hace 121 días)
- **Estrellas:** 1 · 1 bifurcaciones · 0 incidencias abiertas
- **Licencia:** Apache-2.0
- **Lenguaje:** Python · creado el 15 de mayo de 2025
- **Última entrega:** sin entregas etiquetadas
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- Install via pip:
- pip install lxml
- | `--url-extern` | URL to download XMLTV file *(optional if `--input` used)* |

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/suuhm/xmltv-splitter

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Guion de Python que **filtra un archivo enorme de guía de programación** y deja sólo los canales que te
interesan, por nombre o desde una fuente remota. Sirve para que el reproductor no cargue una guía de decenas de
megas cuando sólo ves quince canales.

### Cómo se usa

1. Se ejecuta con Python; **no tiene entregas publicadas**, así que se toma el código del repositorio.
2. Se le pasa el archivo de guía y la lista de canales que quieres conservar.
3. El resultado es un archivo más pequeño que se le da al reproductor.

### Lo que conviene saber antes

**Una estrella** y licencia Apache-2.0, creado en mayo de 2025 y sin cambios desde julio de 2026. Es una
herramienta de una sola tarea, escrita para resolver el problema de alguien concreto, y su propio texto lo dice
sin adornos: ideal para servidores de televisión y programas compatibles con ese formato de guía.

### Cuándo no vale la pena

Si tu guía ya es pequeña, no hay nada que recortar. Y si no quieres tocar un archivo por línea de órdenes, esto
no es para ti.

<!-- GUIA:FIN -->
