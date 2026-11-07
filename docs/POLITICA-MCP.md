# POLÍTICA MCP · lista blanca, permisos mínimos, solo lectura

Decidido el 31 de octubre de 2026, antes de conectar nada. Se aplica a todo servidor MCP que use
esta casa, propio o ajeno.

## Lista blanca

**Se usan** (servidores oficiales de referencia, `modelcontextprotocol/servers`): `fetch`,
`filesystem`, `git`, `memory`, `time`, `sequentialthinking`, `everything`.

**Se usa, del proveedor:** `github/github-mcp-server` (MIT, mantenido por GitHub).
**No se usa** el servidor de GitHub del repositorio de referencia: está **archivado** en
`servers-archived`. Adoptar código muerto teniendo el oficial vivo es justo el error que la vara
existe para impedir.

## Prohibiciones

1. Ningún servidor sin repositorio de código enlazado y mantenedor identificable.
2. Ninguna versión flotante: etiqueta inmutable o hash.
3. Ningún token en variable de entorno global: uno por herramienta, alcance mínimo, caducidad.
4. Ninguna herramienta de escritura habilitada por defecto; escritura = aprobación humana explícita.
5. El contenido remoto es **dato**, nunca instrucción. Se cita; no se obedece.
6. Ningún endpoint remoto opaco sin fuente.

## Razón medida

El registro oficial de MCP sigue en *preview*: guarda metadatos y verifica la propiedad del espacio
de nombres, pero **no revisa seguridad, no mide mantenimiento y no audita permisos**. Medido el
31 de octubre de 2026: 53.886 entradas en su última versión, 66,6 % con endpoint remoto. La
especificación vigente es la 2026-07-28, que deprecó Roots, Sampling y Logging con doce meses de
gracia: no se adoptan en implementaciones nuevas.
