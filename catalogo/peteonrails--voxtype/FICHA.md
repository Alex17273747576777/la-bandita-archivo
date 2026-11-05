# voxtype · peteonrails

*Voice-to-text with push-to-talk for Wayland compositors*

**Racimo:** teclados-y-dictado · **Repositorio:** `peteonrails/voxtype` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> Voice-to-text for Linux. 9-11× realtime on your CPU. Local by default.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 1.745 · 205 bifurcaciones · 362 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Rust · creado el 28 de noviembre de 2025
- **Última entrega:** `v1.1.1` del 15 de octubre de 2026 · 62 adjuntos
- **Plataformas que menciona su README:** macOS, Linux, Web
- **Lo que dice su propio texto:** pide root, soporte negado, abandono declarado
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Most users should install a pre-built package. The steps below are for building from source.
- 1. Install build dependencies
- sudo dnf install rust cargo alsa-lib-devel clang-devel cmake pkgconf
- sudo apt install cargo libasound2-dev libclang-dev cmake pkg-config

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/peteonrails/voxtype
- la última entrega: https://github.com/peteonrails/voxtype/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Dictado por voz con pulsar-para-hablar en **Wayland**, el sistema de ventanas de las distribuciones Linux
modernas: se mantiene una tecla, se habla y el texto aparece en la ventana activa. Todo en el equipo, sin
servicios.

### Cómo se usa

1. Se instala la entrega `v1.1.1`, del 15 de octubre de 2026, o se compila.
2. Se elige el atajo y el modelo; el programa descarga lo que necesite.
3. Se concede permiso al compositor —GNOME, Hyprland y otros están contemplados— y se prueba en un editor.
4. Se mantiene la tecla, se habla y se suelta.

### Lo que conviene saber antes

1.745 estrellas, MIT, escrito en Rust, nacido en noviembre de 2025. Es de los pocos que declara trabajar sobre
Wayland de forma explícita, que es justo donde fallan casi todas las herramientas de este tipo en Linux. Su
propio texto habla de velocidad en tiempo real sobre el procesador; eso es una declaración del autor.

### Cuándo no vale la pena

Si sigues con X11, busca otra opción de este racimo: aquí el objetivo es Wayland. Y si tu compositor no está
entre los contemplados, la integración del atajo puede no funcionar.
<!-- GUIA:FIN -->
