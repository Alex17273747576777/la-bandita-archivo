# El archivo abierto de La Bandita

Una página, un solo archivo, **3.116 repositorios medidos** uno por uno contra la API pública de GitHub
el 9 de noviembre de 2026. Sin CDN, sin fuentes externas, sin rastreadores, sin cuentas y sin cookies:
los datos van dentro del propio `index.html`, así que funciona igual con red y sin ella.

## Qué se puede hacer

* Buscar por nombre de repositorio.
* Ordenar por estrellas, por sumas publicadas, por más nuevo, por actividad reciente o por adjuntos.
* Filtrar para ver **solo los que publican suma de comprobación** (375 de 3.116).
* Todo lo demás se lee como una tabla: licencia, última entrega, días de vida, días sin empujar.

## Qué significa cada columna

| Columna | Qué mide | Cómo se midió |
|---|---|---|
| Estrellas | cuánta gente lo marcó | campo `stargazers` de la API |
| Sumas | archivos de comprobación en la última entrega | nombres de los adjuntos que terminan en `.sha256`, `.sha512`, `.asc`, `.sig`, `sums`… |
| Adjuntos | archivos que trae la última entrega | campo `assets` de la última entrega |
| Días de vida | desde que se creó el repositorio | `createdAt` contra el 9-nov-2026 |
| Días sin empujar | desde el último envío de código | `pushedAt` contra el 9-nov-2026 |
| Licencia | la que declara el repositorio | campo `license.spdxId`; si no declara, dice «sin declarar» |

Cuando un dato no se pudo medir, la página escribe **«aquí no hay»**. No hay estimaciones.

## Licencias

* **Datos:** CC0 (dominio público). Se pueden copiar, mezclar y republicar sin pedir permiso.
* **Código de la página:** también CC0.
* **Los programas enlazados:** la licencia que declara cada autor, en su propio repositorio. Aquí no se
  afirma la licencia de nadie más allá de lo que devolvió la API.

## De dónde salen los datos

De `docs/CENSO-MEDIDO-2026-11-09.json` en el repositorio del archivo: 16 páginas de fmhy.net leídas,
3.284 repositorios distintos encontrados, 3.125 que esta casa no había medido nunca, cruzados con su
propio registro de 6.842 fichas. Para publicar, copia `index.html` y `datos.json`: no hace falta nada más.
