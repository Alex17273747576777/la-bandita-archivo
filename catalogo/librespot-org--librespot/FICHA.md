# librespot · librespot-org

*Open Source Spotify client library*

**Racimo:** audio · **Repositorio:** `librespot-org/librespot` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Note: librespot only works with Spotify Premium. This will remain the case. We will not support any features to make librespot compatible with free accounts, such as limited skips and adverts.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 21 de octubre de 2026 (hace 15 días)
- **Estrellas:** 7.369 · 969 bifurcaciones · 203 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Rust · creado el 15 de noviembre de 2017
- **Última entrega:** `v0.8.0` del 10 de noviembre de 2025 · 0 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Lo que dice su propio texto:** abandono declarado
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- On Debian/Ubuntu, the following command will install these dependencies:
- sudo apt-get install build-essential libasound2-dev
- On Fedora systems, the following command will install these dependencies:
- sudo dnf install alsa-lib-devel make gcc

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/librespot-org/librespot
- la última entrega: https://github.com/librespot-org/librespot/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Biblioteca en Rust que implementa el protocolo del reproductor de Spotify: sirve para construir un cliente
propio, para montar un aparato que aparezca como dispositivo en la aplicación oficial, o para entender cómo
funciona ese protocolo por dentro.

### Cómo se usa

1. Se compila con las herramientas de Rust, o se instala el paquete de tu distribución; la entrega medida es
   la `v0.8.0`, del 10 de noviembre de 2025.
2. Trae una orden de ejemplo que arranca como dispositivo: se le dan credenciales y una salida de audio.
3. Para integrarlo en un programa propio se usa como biblioteca y se controlan sus eventos desde el código.

### Lo que conviene saber antes

7.369 estrellas, MIT. Su propio texto lo dice sin ambigüedad: **sólo funciona con cuentas de pago**, y no
habrá soporte para las gratuitas. Eso no es un detalle, es la premisa del proyecto. Como biblioteca es muy
buena; como programa para el usuario final, no está pensada.

### Cuándo no vale la pena

Si no programas y no tienes cuenta de pago, no hay nada que hacer con esto. Para el caso de «aparato que
aparece en la aplicación oficial» hay un programa ya hecho en este racimo, y es más corto de instalar.
<!-- GUIA:FIN -->
