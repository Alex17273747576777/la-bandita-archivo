# cli · lnreader

*Search, read and download web novels as EPUBs from your terminal, powered by LNReader plugins. Includes an MCP server for AI agents.*

**Racimo:** reemplazo-del-stack · **Repositorio:** `lnreader/cli` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Run LNReader plugins outside the app: search hundreds of web novel sources and download novels as clean EPUB 3 files for Apple Books, Calibre, KOReader, Kobo or Kindle.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 24 de octubre de 2026 (hace 12 días)
- **Estrellas:** 0 · 0 bifurcaciones · 0 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** TypeScript · creado el 5 de mayo de 2025
- **Última entrega:** sin entregas etiquetadas
- **Plataformas que menciona su README:** macOS, Linux, Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- npx @lnreader/cli --help # run without installing
- npm i -g @lnreader/cli # or install the `lnreader` command
- pnpm install
- lnreader download # asks what to search for, then pick a result and options

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/lnreader/cli

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Lleva los complementos de LNReader a la terminal: busca en cientos de fuentes de novelas web y descarga
el resultado como EPUB 3 limpio para Apple Books, Calibre o KOReader. Incluye además un servidor MCP para
que un asistente pueda usarlo.

### Cómo se usa

1. Sin instalar nada: `npx @lnreader/cli --help`. O con `npm i -g @lnreader/cli`.
2. Se busca por título, se elige la fuente y se descarga; el EPUB lleva portada, índice y capítulos.
3. Para automatizar, el modo MCP se levanta como servidor y se conecta desde el cliente que se use.

### Lo que conviene saber antes

Las fuentes son las de LNReader: funcionan mientras funcionen, y dependen de que alguien mantenga el
complemento del sitio. ★0 y sin entregas etiquetadas: es nuevo, y se puede leer entero porque es corto.

<!-- GUIA:FIN -->
