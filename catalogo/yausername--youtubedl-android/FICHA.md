# youtubedl-android · yausername

*youtube-dl for android*

**Racimo:** descargas · **Repositorio:** `yausername/youtubedl-android` · **Estado:** lento · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> If you wish to use config file in the download option by using this command --config-location you must create a file named config.txt inside youtubedl-android directory and add the commands for example.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 16 de noviembre de 2025 (hace 354 días)
- **Estrellas:** 1.381 · 253 bifurcaciones · 115 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Kotlin · creado el 4 de febrero de 2019
- **Última entrega:** sin entregas etiquetadas
- **Plataformas que menciona su README:** Android
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Debug apk for testing can be downloaded from the releases page
- o /sdcard/Download/youtubedl-android/%(title)s.%(ext)s
- Checkout dvd, a video downloader app based on this library.
- Also take a look at Seal, another video/audio downloader app which demonstrates a more advanced and customized use of this library.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/yausername/youtubedl-android

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

No es una aplicación: es una **biblioteca para programadores** que quieran meter `yt-dlp` dentro de su app
de Android sin pelearse con Python. Trae los binarios y un envoltorio para llamarlos desde Java o Kotlin.

### Cómo se usa

1. Se añade como dependencia en el proyecto de Android, siguiendo lo que indica su documentación.
2. Se inicializa la biblioteca en la aplicación, que descarga las piezas la primera vez.
3. Desde el código se lanza una orden de `yt-dlp` y se recoge la salida para mostrarla en tu interfaz.
4. El archivo de configuración se coloca como `config.txt` dentro de la carpeta de la biblioteca.

### Lo que conviene saber antes

1.381 estrellas, GPL-3.0, último cambio en **noviembre de 2025**. **No tiene entregas** porque no es un
programa: se integra en el tuyo. Y si lo integras, heredas su licencia y su mantenimiento: cuando una web
cambie, tendrás que actualizar tú.

### Cuándo no vale la pena

Si no programas para Android, no hay nada que hacer con esto. Y si programas, valora antes si te conviene
llevar Python dentro de tu aplicación: pesa y complica la publicación en la tienda.

<!-- GUIA:FIN -->
