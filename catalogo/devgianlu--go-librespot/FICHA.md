# go-librespot · devgianlu

*Yet another open source Spotify client, written in Go.*

**Racimo:** clientes-de-musica · **Repositorio:** `devgianlu/go-librespot` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> - 🎵 Spotify Connect — show up as a speaker in the Spotify app and stream to it from any device on your network (Spotify Premium required). - 🔊 Multiple audio backends — ALSA, PulseAudio, AudioToolbox on macOS, WASAPI on Windows, or a raw named pipe for custom routing. - 📊 Loudness normalization — Spotify-standard −14 LUFS (ITU-R BS.1770) with configurable pregain. - 🔀 Crossfade — configurable over

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 386 · 87 bifurcaciones · 24 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Go · creado el 5 de septiembre de 2023
- **Última entrega:** `v0.10.5` del 16 de octubre de 2026 · 5 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux, Web
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- 💾 **On-disk audio cache** — skip re-downloading tracks, bounded by an LRU size limit.
- To get started you can download prebuilt binaries for
- You can also install go-librespot using Brew
- brew install go-librespot

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/devgianlu/go-librespot
- la última entrega: https://github.com/devgianlu/go-librespot/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Programa que hace que un equipo aparezca como **altavoz** dentro de un servicio de música: se monta en una
Raspberry Pi o en un ordenador sin pantalla, y desde la aplicación oficial del teléfono se le manda la música.
Está escrito en Go, que en este caso significa un solo binario sin dependencias.

### Cómo se usa

1. Se descarga el binario de la entrega `v0.10.5`, del 16 de octubre de 2026, o se compila.
2. Se escribe un archivo de configuración con el nombre del aparato y la salida de audio.
3. Se arranca como servicio; en la aplicación oficial aparece como un dispositivo más de la red.

### Lo que conviene saber antes

386 estrellas, GPL-3.0 y entregas de este mes. Admite varias salidas de audio y, a diferencia de otras piezas
parecidas, su autor lo documenta con ejemplos. Necesita cuenta de pago del servicio. Y hay que tener claro qué
es: no reproduce tu propia biblioteca, reproduce lo que le manden desde la aplicación oficial.

### Cuándo no vale la pena

Si no tienes un equipo dedicado sin pantalla, no aporta nada frente a usar el teléfono. Y en una red inestable,
el aparato aparece y desaparece de la lista.

<!-- GUIA:FIN -->
