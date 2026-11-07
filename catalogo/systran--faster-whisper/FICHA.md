# faster-whisper · SYSTRAN

*Faster Whisper transcription with CTranslate2*

**Racimo:** teclados-y-dictado · **Repositorio:** `SYSTRAN/faster-whisper` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 2 de noviembre de 2026 (hace 3 días)
- **Estrellas:** 26.496 · 2210 bifurcaciones · 21 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Python · creado el 11 de febrero de 2023
- **Última entrega:** `v1.2.1` del 31 de octubre de 2025 · 0 adjuntos
- **Plataformas que menciona su README:** Android, Windows, macOS, Linux, Web
- **Lo que dice su propio texto:** abandono declarado
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- GPU execution requires the following NVIDIA libraries to be installed:
- <summary>Other installation methods (click to expand)</summary>
- The libraries (cuBLAS, cuDNN) are installed in this official NVIDIA CUDA Docker images: `nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04`.
- Install with `pip` (Linux only)

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/SYSTRAN/faster-whisper
- la última entrega: https://github.com/SYSTRAN/faster-whisper/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Biblioteca en Python que ejecuta los modelos de reconocimiento de voz de Whisper **mucho más rápido** que la
implementación original, usando un motor de inferencia optimizado. Es la pieza que usan muchos programas de
dictado de este racimo por debajo.

### Cómo se usa

1. Se instala con `pip install faster-whisper`; la entrega medida es la `v1.2.1`, del 31 de octubre de 2025.
2. Desde código se carga un modelo —hay varios tamaños— y se le pasa el audio, o se usa su orden de ejemplo
   para transcribir un archivo.
3. En una tarjeta gráfica compatible va muy rápido; en procesador, más lento pero funciona.

### Lo que conviene saber antes

26.496 estrellas, licencia MIT, y su última entrega es de **octubre de 2025**, aunque el repositorio recibe
cambios en noviembre de 2026. No es un programa: no tiene ventana ni teclado. Se usa desde otro programa o
desde un guion. Su límite es la memoria de tu equipo: los modelos grandes piden varios gigas.

### Cuándo no vale la pena

Si lo que quieres es dictar, no empieces aquí: instala una de las aplicaciones de este racimo que ya lo
llevan dentro. Esta ficha existe porque es la pieza que hace posibles a las demás.

<!-- GUIA:FIN -->
