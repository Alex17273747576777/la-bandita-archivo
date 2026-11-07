# CrossWatch · cenodude

*Synchronize your data across media servers, media agents and trackers. Keep your movies and shows in sync, no matter where you watch.*

**Racimo:** reemplazo-del-stack · **Repositorio:** `cenodude/CrossWatch` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> CrossWatch (CW) tracks what you watch through Watcher and syncs your watchlists, ratings, history, playback progress and collections across supported media servers and trackers. Watcher doesn't need Plex Pass or Emby Premiere.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 993 · 28 bifurcaciones · 6 incidencias abiertas
- **Licencia:** AGPL-3.0
- **Lenguaje:** Python · creado el 27 de agosto de 2025
- **Última entrega:** `v0.14.1` del 3 de noviembre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Linux, Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- <a href="https://wiki.crosswatch.app/getting-started/first-time-setup">
- Not every integration supports every feature. Some sync lists and history; others report playback activity. Setup details are in the wiki.
- Installation
- The examples below use Docker. See the installation guide for more details.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/cenodude/CrossWatch
- su web: https://wiki.crosswatch.app
- la última entrega: https://github.com/cenodude/CrossWatch/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Sincroniza el historial de lo que ves entre servidores de medios y servicios de seguimiento: lo que
marcas visto en Jellyfin aparece en Plex, y lo que puntúas en un rastreador llega al otro. Su terreno es
la casa con varias fuentes de reproducción.

### Cómo se usa

1. Se despliega en un servidor con Docker.
2. Se conectan los servicios por su API —cada uno con su token— y se eligen qué datos se sincronizan.
3. La primera sincronización tarda: está emparejando bibliotecas enteras.

### Lo que conviene saber antes

Su propia documentación avisa de que **no todas las integraciones soportan todo**: unas sincronizan
listas, otras historial, otras solo actividad. Antes de fiarse, se prueba con una serie y se mira qué
llegó al otro lado.

<!-- GUIA:FIN -->
