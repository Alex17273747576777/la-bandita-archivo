# epg-tools · Ruby184

*Memory-efficient EPG toolkit for Node: grab from XMLTV, M3U and Xtream Codes sources with day-level caching, then merge, validate and serve XMLTV guides*

**Racimo:** radio-y-directo · **Repositorio:** `Ruby184/epg-tools` · **Estado:** vivo · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> - Grabber — define multiple site configs, fetched in parallel with p-queue and ky - Day cache — every site + channel + day is cached; building a 14-day guide only fetches the days that are missing or stale. Files of ndjson or XMLTV, one SQLite file, memory, or a driver of your own - Streaming XMLTV — a dependency-free, XMLTV-specialized streaming parser (tokenizer technique inspired by txml, fused

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 30 de octubre de 2026 (hace 6 días)
- **Estrellas:** 1 · 0 bifurcaciones · 1 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** TypeScript · creado el 16 de agosto de 2026
- **Última entrega:** `v0.9.0` del 16 de octubre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Web
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- npm install epg-tools
- downloading again, and what comes out merges with any hand-written site below.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/Ruby184/epg-tools
- su web: https://www.npmjs.com/package/epg-tools
- la última entrega: https://github.com/Ruby184/epg-tools/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Juego de herramientas para la **guía de programación**: recoge los datos de una o varias fuentes, los guarda por
días con caché, y los une y valida en un archivo único que cualquier reproductor pueda leer. Es fontanería para
quien mantiene una lista grande y no quiere volver a descargarla entera cada vez.

### Cómo se usa

1. Se instala con las herramientas de Node; la entrega medida es la `v0.9.0`, del 16 de octubre de 2026.
2. Se escriben las fuentes en su configuración, una por una.
3. Se ejecuta el recogedor; los días ya descargados se reutilizan y sólo se piden los que faltan.
4. El resultado se sirve al reproductor como una guía más.

### Lo que conviene saber antes

**Una estrella** y licencia MIT: es una herramienta recién nacida, de agosto de 2026, hecha por una persona para
su propio problema. Lo interesante no es su tamaño sino su idea: la caché por día y por canal, que es lo que
hace viable una guía de dos semanas sin descargar un archivo enorme cada mañana.

### Cuándo no vale la pena

Si tienes cuatro canales, el reproductor se apaña con su propia descarga. Esto se justifica con listas grandes o
con fuentes que tardan en responder.

<!-- GUIA:FIN -->
