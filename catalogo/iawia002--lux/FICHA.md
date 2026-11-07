# lux · iawia002

*👾 Fast and simple video download library and CLI tool written in Go*

**Racimo:** descargas · **Repositorio:** `iawia002/lux` · **Estado:** lento · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> - Installation - Prerequisites - Install via go install - Homebrew (macOS only) - Arch Linux - Void Linux - Scoop on Windows - Chocolatey on Windows - Cask on Windows/macOS/Linux - Getting Started - Download a video - Download anything else - Download playlist - Multiple inputs - Resume a download - Auto retry - Cookies - Proxy - Multi-Thread - Short link - bilibili - Use specified Referrer - Spec

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 29 de marzo de 2026 (hace 221 días)
- **Estrellas:** 31.827 · 3330 bifurcaciones · 545 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Go · creado el 24 de febrero de 2018
- **Última entrega:** `v0.24.1` del 6 de mayo de 2024 · 20 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- 👾 Lux is a fast and simple video downloader built with Go.
- Installation
- Prerequisites
- Install via `go install`

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/iawia002/lux
- la última entrega: https://github.com/iawia002/lux/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Programa de terminal escrito en Go para bajar vídeo de bastantes sitios —los chinos, sobre todo— sin
dependencias: un solo archivo ejecutable. Hace listas de reproducción, varias direcciones a la vez, reanudar
y reintentar solo.

### Cómo se usa

1. Se instala desde el gestor de paquetes de tu sistema, con `go install`, o se baja el binario de la
   entrega `v0.24.1`, del 6 de mayo de 2024.
2. `lux` y la dirección muestra las calidades disponibles sin descargar nada.
3. Con `-f` se elige la calidad; con `-p` se baja la lista entera; `-o` fija la carpeta.

### Lo que conviene saber antes

31.827 estrellas, licencia MIT, pero su entrega es de **mayo de 2024** y su último cambio, de marzo de 2026.
Para sitios que cambian a menudo eso es un problema: cuando la web cambia, `lux` falla y no siempre hay
prisa por arreglarlo. Es muy bueno en lo suyo —Go, un binario, sin instalar nada más— y flojo en
actualidad.

### Cuándo no vale la pena

Si tu sitio principal es YouTube, `yt-dlp` lo cubre mejor y con más mantenimiento. `lux` se elige por sus
sitios y por no necesitar intérprete.

<!-- GUIA:FIN -->
