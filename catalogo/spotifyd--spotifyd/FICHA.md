# spotifyd · Spotifyd

*A spotify daemon*

**Racimo:** audio · **Repositorio:** `Spotifyd/spotifyd` · **Estado:** lento · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Spotifyd streams music just like the official client, but is more lightweight and supports more platforms. Spotifyd also supports the Spotify Connect protocol, which makes it show up as a device that can be controlled from the official clients.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 28 de mayo de 2026 (hace 161 días)
- **Estrellas:** 10.822 · 521 bifurcaciones · 76 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Rust · creado el 10 de diciembre de 2014
- **Última entrega:** `v0.4.2` del 19 de noviembre de 2025 · 26 adjuntos
- **Plataformas que menciona su README:** Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- __To read about how to install and configure Spotifyd, take a look at our [wiki][wiki]!__

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/Spotifyd/spotifyd
- su web: https://spotifyd.rs
- la última entrega: https://github.com/Spotifyd/spotifyd/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Demonio que hace que un equipo —una Raspberry Pi, un ordenador sin pantalla— aparezca como **dispositivo de
Spotify** en la aplicación oficial. Se controla desde el teléfono, suena por el equipo, y no necesita
interfaz en él.

### Cómo se usa

1. Se instala desde el gestor de paquetes o se compila; la entrega es la `v0.4.2`, del 19 de noviembre de
   2025.
2. Se crea un archivo de configuración con el usuario, el nombre del aparato y la salida de audio.
3. Se arranca como servicio y, en la aplicación oficial, el equipo aparece en la lista de dispositivos.

### Lo que conviene saber antes

10.822 estrellas, GPL-3.0, escrito en Rust. Su último cambio es de **mayo de 2026** y su entrega de noviembre
de 2025: va despacio. Y hay algo que su propio proyecto deja claro en el ecosistema: este tipo de cliente
necesita cuenta de pago; la versión gratuita no se soporta.

### Cuándo no vale la pena

Si no tienes un equipo dedicado sin pantalla, no aporta nada frente a la aplicación oficial. Y si no pagas
la cuenta, directamente no funciona.

<!-- GUIA:FIN -->
