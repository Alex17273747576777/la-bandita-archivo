# Observatorio OSS · el tablero medido del 27 de noviembre de 2026

**Esta carpeta se sirve tal cual en `https://alex17273747576777.github.io/la-bandita-archivo/observatorio/`.**
No se genera: se copia. Lo que hay aquí es el corte del **2026-11-27 08:38 AST**, congelado.

## Los tres archivos, y para qué sirve cada uno

| Archivo | Qué es |
|---|---|
| `index.html` | El tablero entero, **64.375 B**, con los datos embebidos dentro. Se abre sin red y funciona: sin CDN, sin fuentes externas, sin una sola petición al cargar. |
| `datos.json` | Los mismos datos en JSON (**32.567 B**): 37 repositorios, 32 hallazgos verificados, 6 nichos con recomendación y el estado de los conectores. Para que otra herramienta los lea sin abrir el HTML. |
| `medidos-37-repos-2026-11-27.json` | La evidencia cruda de la medición (**17.940 B**): fecha AST y UTC, modo de autenticación y los 37 repositorios campo a campo. |

## Qué mide, y qué no

- **37 repositorios** del ecosistema manga, anime y novela ligera: **132.582 estrellas** en total.
- **9 de 35** con release publican un archivo de suma SHA-256 (**25,7 %**). De los 30 auditados, 4; de los 6 candidatos, 5.
- **2 repositorios sin licencia** (`diogorainhalopes/atahon`, `reyyuuki/Azyx`).
- **32 hallazgos** verificados en código, con su commit y su severidad.
- **6 nichos** con patrón a adoptar, antipatrón a evitar y siguiente acción concreta.

Lo que **no** está medido se dice en el propio tablero, no se rellena: no hubo prueba en dispositivo
físico Android en este corte; WordPress respondió `404`; el proyecto de Supabase está `INACTIVE`; y
Vercel rechazó el despliegue por validación de esquema, así que **el tablero no se publica en Vercel**.

## Por qué está publicado aquí y no en Vercel

La API de despliegue de Vercel rechazó los envíos (`files[].data` debe ser cadena y `projectSettings`
debe llevar un preset válido). En vez de seguir intentándolo, se usa la vía que este repositorio ya
tenía funcionando: `.github/workflows/pagina.yml` sirve `web/` con `actions/deploy-pages`. El tablero
entra como subcarpeta, así que **la página histórica de `web/index.html` sigue intacta** en la raíz.

## Licencia

Los **datos** de este corte van como **CC BY 4.0** y el HTML como **MIT**, igual que el resto del
archivo. Los proyectos de terceros citados conservan la licencia que declara su repositorio; aquí no
se licencia nada ajeno.
