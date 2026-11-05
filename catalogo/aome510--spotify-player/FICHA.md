# spotify-player · aome510

*A Spotify player in the terminal with full feature parity*

**Racimo:** clientes-de-musica · **Repositorio:** `aome510/spotify-player` · **Estado:** lento · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> - Introduction - Examples - Installation - Authentication - How authentication works - Why you may be asked to authenticate multiple times - Client ID and rate limits - Using a custom client ID - Features - Spotify Connect - Streaming - Audio Visualization - Media Control - Image - Notify - Mouse support - Daemon - Fuzzy search - CLI commands - Commands - Configurations - Caches - Logging - Acknow

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 19 de septiembre de 2026 (hace 47 días)
- **Estrellas:** 7.302 · 403 bifurcaciones · 168 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Rust · creado el 8 de julio de 2021
- **Última entrega:** `v0.25.1` del 9 de septiembre de 2026 · 10 adjuntos
- **Plataformas que menciona su README:** Android, Windows, macOS, Linux, Web
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Installation
- By default, the application's installed binary is `spotify_player`.
- Rust and cargo as the build dependencies
- install `openssl`, `alsa-lib` (`streaming` feature), `libdbus` (`media-control` feature).

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/aome510/spotify-player
- la última entrega: https://github.com/aome510/spotify-player/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Cliente de un servicio de música para la terminal, con la ambición de tener todo lo que tiene el cliente
oficial: búsqueda, biblioteca, listas, cola, control de aparatos y letras. Es la alternativa viva al cliente de
terminal que quedó parado.

### Cómo se usa

1. Se instala con las herramientas de Rust, desde el gestor de paquetes o con el binario de la entrega
   `v0.25.1`, del 9 de septiembre de 2026.
2. La primera vez pide autorización: abre el navegador, se concede el permiso y se guarda el testigo.
3. Se maneja con el teclado; su documentación trae un mapa de atajos que conviene imprimir o tener al lado.

### Lo que conviene saber antes

7.302 estrellas, MIT, y última entrega de septiembre. La autenticación es la parte que más preguntas genera en
su propio proyecto: el testigo caduca y hay que volver a autorizar cada cierto tiempo, y su documentación lo
explica con detalle. Necesita cuenta de pago del servicio, como casi todo lo de esta familia.

### Cuándo no vale la pena

Si no vives en la terminal, la curva de atajos no compensa. Y si no tienes cuenta de pago, no funciona: no hay
plan para cuentas gratuitas.

<!-- GUIA:FIN -->
