# snapcast · snapcast

*Synchronous multiroom audio player*

**Racimo:** audio · **Repositorio:** `snapcast/snapcast` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Snapcast is a multiroom client-server audio player, where all clients are time synchronized with the server to play perfectly synced audio. It's not a standalone player, but an extension that turns your existing audio player into a Sonos-like multiroom solution. Audio is captured by the server and routed to the connected clients. Several players can feed audio to the server in parallel and clients

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 3 de noviembre de 2026 (hace 2 días)
- **Estrellas:** 8.044 · 560 bifurcaciones · 126 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** C++ · creado el 2 de enero de 2015
- **Última entrega:** `v0.35.0` del 10 de marzo de 2026 · 46 adjuntos
- **Plataformas que menciona su README:** Android, iOS, Windows, macOS, Linux, Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- la web que da el proyecto: https://github.com/snapcast/snapcast/releases
- Installation
- You can either install Snapcast from a prebuilt package (recommended for new users), or build and install snapcast from source.
- Install Linux packages (recommended for beginners)

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/snapcast/snapcast
- la última entrega: https://github.com/snapcast/snapcast/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Sistema de audio **multisala sincronizado**: un servidor toma el sonido de un reproductor y lo reparte a
varios clientes —Raspberry Pi, ordenadores, móviles— de modo que todos suenan a la vez y sin eco entre
habitaciones.

### Cómo se usa

1. Se instala el servidor en el equipo que tenga la música y un cliente en cada aparato que vaya a sonar; la
   entrega medida es la `v0.35.0`, del 10 de marzo de 2026.
2. Se configura el servidor para que tome la entrada de audio del reproductor que uses.
3. Los clientes se conectan solos por la red; desde una aplicación de control se ajusta el volumen de cada uno
   y el retardo, que es lo que corrige la diferencia entre aparatos.

### Lo que conviene saber antes

8.044 estrellas, GPL-3.0. **No es un reproductor**: sin una fuente de audio no hace nada, y eso hay que
entenderlo antes de instalarlo. En redes wifi inestables el retardo hay que ajustarlo a mano, y el resultado
nunca es tan fino como con cable.

### Cuándo no vale la pena

Con un solo altavoz o con dos aparatos que ya suenan juntos, esto es complicación sin premio. Se justifica en
una casa con varias habitaciones y cable donde se pueda.
<!-- GUIA:FIN -->
