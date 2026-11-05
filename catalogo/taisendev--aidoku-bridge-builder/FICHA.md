# aidoku-bridge-builder · TaisenDev

*Turns a Suwayomi-Server catalog into a self-updating Aidoku source repo: one .aix per site, hourly.*

**Racimo:** reemplazo-del-stack · **Repositorio:** `TaisenDev/aidoku-bridge-builder` · **Estado:** vivo · **Medido:** 2026-11-05 11:42 UTC

## Qué es, según quien lo hace

> aidoku-bridge-builder turns Suwayomi's full extension catalog into an Aidoku repository without installing every extension on the server. It installs a catalog-listed extension only when Aidoku requests its package.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 27 de octubre de 2026 (hace 9 días)
- **Estrellas:** 0 · 0 bifurcaciones · 0 incidencias abiertas
- **Licencia:** MPL-2.0
- **Lenguaje:** Python · creado el 26 de septiembre de 2026
- **Última entrega:** `v0.2.24` del 26 de octubre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** iOS, Web
- **Medido:** 2026-11-05 11:42 UTC

## Cómo se consigue

- E[(Suwayomi extension catalog)] -->|discover / update installed| B[aidoku-bridge-builder]
- B -->|install selected extension + build .aix| S
- The scheduled catalog cycle and an on-demand installation follow separate paths:
- | **2. Publish available extensions** | Writes index entries and icons for uninstalled catalog packages; it does not install their APKs. |

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/TaisenDev/aidoku-bridge-builder
- su web: https://github.com/TaisenDev/aidoku-bridge-template
- la última entrega: https://github.com/TaisenDev/aidoku-bridge-builder/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

No hay guía escrita todavía. Lo de arriba está medido; lo de abajo, no.

Esta ficha se genera sola y la guía se escribe a mano, recurso por recurso: para qué sirve de
verdad, qué pasos hay que dar en un teléfono y en qué caso no vale la pena. Mientras eso no esté,
la ficha sirve para saber qué es y en qué estado está, no para instalarlo.

<!-- GUIA:FIN -->
