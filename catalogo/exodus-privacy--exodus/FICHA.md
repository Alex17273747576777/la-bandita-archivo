# exodus · Exodus-Privacy

*Platform to audit trackers used by Android application*

**Racimo:** reemplazo-del-stack · **Repositorio:** `Exodus-Privacy/exodus` · **Estado:** lento · **Medido:** 2026-11-05 11:42 UTC

## Qué es, según quien lo hace

> εxodus is a privacy auditing platform for Android applications. It detects behaviors which can be dangerous for user privacy like ads, tracking, analytics, …

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 13 de septiembre de 2026 (hace 53 días)
- **Estrellas:** 814 · 74 bifurcaciones · 51 incidencias abiertas
- **Licencia:** AGPL-3.0
- **Lenguaje:** Python · creado el 19 de noviembre de 2017
- **Última entrega:** `v1.33.0` del 13 de septiembre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Android, Web
- **Medido:** 2026-11-05 11:42 UTC

## Cómo se consigue

- Installing your local instance
- You have different ways of setting up your development environment (via Docker or manually), everything is explained here.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/Exodus-Privacy/exodus
- su web: https://reports.exodus-privacy.eu.org/
- la última entrega: https://github.com/Exodus-Privacy/exodus/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Es el motor del análisis de rastreadores de Exodus Privacy: una plataforma para auditar qué bibliotecas de
seguimiento lleva dentro una aplicación de Android, con un catálogo público de informes por app. No es
una app para el usuario final: es el servicio que produce los informes que consultan otras.

### Cómo se usa

1. Se despliega con Docker o a mano, siguiendo su documentación de entorno de desarrollo.
2. Se le dan APK y devuelve el análisis: rastreadores detectados, firmas y permisos.
3. Para consultar resultados ya hechos, se usa su sitio público; para generarlos tú, esto.

### Cuándo no vale la pena

Si solo quieres saber qué lleva una app, el informe público existe y no hay que montar nada. Esto se
instala cuando quieres análisis propios, en lote, o en una red cerrada.

<!-- GUIA:FIN -->
