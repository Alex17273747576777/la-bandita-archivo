# chromaprint · acoustid

*C library for generating audio fingerprints used by AcoustID*

**Racimo:** audio · **Repositorio:** `acoustid/chromaprint` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Chromaprint is an audio fingerprint library developed for the [AcoustID][acoustid] project. It's designed to identify near-identical audio and the fingerprints it generates are as compact as possible to achieve that. It's not a general purpose audio fingerprinting solution. It trades precision and robustness for search performance. The target use cases are full audio file identifcation, duplicate

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 15 de octubre de 2026 (hace 21 días)
- **Estrellas:** 1.415 · 178 bifurcaciones · 31 incidencias abiertas
- **Licencia:** NOASSERTION
- **Lenguaje:** C++ · creado el 17 de abril de 2011
- **Última entrega:** `v1.6.2` del 15 de octubre de 2026 · 7 adjuntos
- **Plataformas que menciona su README:** macOS
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- $ sudo make install
- you will need to have the FFmpeg libraries installed.
- If you have FFmpeg installed in a non-standard location, you can use the `FFMPEG_ROOT` option to specify where:
- $ cmake -DFFMPEG_ROOT=/path/to/local/ffmpeg/install .

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/acoustid/chromaprint
- la última entrega: https://github.com/acoustid/chromaprint/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Biblioteca en C que calcula la **huella acústica** de un archivo de audio: un resumen matemático del sonido
que permite reconocer la misma canción aunque esté recomprimida, cortada o con otro nombre. Es la pieza que
usan los programas de reconocimiento para decir «esto es tal tema».

### Cómo se usa

1. Normalmente no se usa sola: se instala como dependencia del programa que la necesita, o se compila con
   `cmake` y se enlaza desde tu propio código.
2. Trae una orden de ejemplo en sus herramientas que calcula la huella de un archivo.
3. Para identificar de verdad hace falta además consultar la base de datos pública del proyecto AcoustID, con
   la huella y la duración.

### Lo que conviene saber antes

1.415 estrellas y entrega `v1.6.2` publicada el 15 de octubre de 2026, la misma semana en que se midió. Su
texto aclara que **no es una huella de propósito general**: sirve para audio casi idéntico, no para
parecidos. GitHub **no le reconoce la licencia** en la ficha, aunque el proyecto declare la suya.

### Cuándo no vale la pena

Si lo que quieres es etiquetar música, no empieces aquí: usa un programa que ya lo haga, como `Picard`. Esta
biblioteca es para quien escribe el programa.
<!-- GUIA:FIN -->
