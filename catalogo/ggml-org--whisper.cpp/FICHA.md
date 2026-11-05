# whisper.cpp · ggml-org

*Port of OpenAI's Whisper model in C/C++*

**Racimo:** teclados-y-dictado · **Repositorio:** `ggml-org/whisper.cpp` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model:

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 54.948 · 6275 bifurcaciones · 362 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** C++ · creado el 25 de septiembre de 2022
- **Última entrega:** `v1.9.5` del 6 de octubre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Android, iOS, Windows, macOS, Linux, Web
- **Lo que dice su propio texto:** soporte negado, abandono declarado, espejo declarado
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Then, download one of the Whisper models converted in `ggml` format. For example:
- sh ./models/download-ggml-model.sh base.en
- The command downloads the `base.en` model converted to custom `ggml` format and runs the inference on all `.wav` samples in the folder `samples`.
- This will download a few more audio files from Wikipedia and convert them to 16-bit WAV format via `ffmpeg`.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/ggml-org/whisper.cpp
- la última entrega: https://github.com/ggml-org/whisper.cpp/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Implementación de los modelos de reconocimiento de voz de Whisper en C y C++, sin dependencias y capaz de
correr en un teléfono, una Raspberry Pi o un portátil modesto. Es la pieza que hace posible el dictado local en
casi todas las aplicaciones de este racimo.

### Cómo se usa

1. Se compila —son dos órdenes con `cmake`— o se toma el binario de la entrega `v1.9.5`, del 6 de octubre de
   2026.
2. Se descarga un modelo en el formato del proyecto; hay varios tamaños, de unos cientos de megas a varios
   gigas.
3. Se transcribe un archivo con la orden de ejemplo, o se levanta su servidor local para que otros programas le
   manden audio.
4. Admite el micrófono del sistema para dictado en vivo.

### Lo que conviene saber antes

54.948 estrellas, licencia MIT, y desarrollo diario. Su virtud es correr donde otros no corren; su precio es
que hay que compilar y elegir el modelo a mano, y que la calidad depende de ese tamaño. En un equipo sin
tarjeta gráfica, los modelos grandes tardan lo suyo.

### Cuándo no vale la pena

Si lo que quieres es dictar y ya, instala una aplicación que lo lleve dentro: esto es el motor, no el
volante.
<!-- GUIA:FIN -->
