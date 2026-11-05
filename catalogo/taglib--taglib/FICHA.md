# taglib · taglib

*TagLib Audio Meta-Data Library*

**Racimo:** audio · **Repositorio:** `taglib/taglib` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> TagLib is a library for reading and editing the metadata of several popular audio formats. Currently, it supports various metadata containers such as [ID3v1][], [ID3v2][] and [Vorbis][] comments for MP3, MP4, AAC, [Ogg][], [Opus][], [FLAC][], [Speex][], [APE][], [MPC][], [WavPack][], [WAV][], [AIFF][], [TrueAudio][], [Matroska][], [WebM][], ASF, WMA, DSF, DFF and tracker (MOD, XM, S3M, IT) files.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 1.467 · 405 bifurcaciones · 30 incidencias abiertas
- **Licencia:** LGPL-2.1
- **Lenguaje:** C++ · creado el 10 de marzo de 2011
- **Última entrega:** `v2.3.2` del 5 de septiembre de 2026 · 1 adjuntos
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega. Su web: http://taglib.org/.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/taglib/taglib
- su web: http://taglib.org/
- la última entrega: https://github.com/taglib/taglib/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Biblioteca en C++ para **leer y escribir metadatos** de audio: etiquetas, carátulas, propiedades técnicas del
archivo. Es la pieza que hay debajo de muchos reproductores y etiquetadores, incluidos varios de este racimo.

### Cómo se usa

1. Normalmente se instala como dependencia del programa que la usa, o se compila con `cmake`; la entrega
   medida es la `v2.3.2`, del 5 de septiembre de 2026.
2. Desde código se abre el archivo, se leen o escriben las etiquetas y se guarda.
3. Las herramientas de ejemplo que trae permiten ver y cambiar etiquetas desde la terminal.

### Lo que conviene saber antes

1.467 estrellas, LGPL-2.1, quince años de historia. Su límite es el que declara su propio texto: cubre
contenedores y etiquetas conocidos, no cualquier formato exótico. Si escribes un programa que toca etiquetas,
usar esto te ahorra implementar cinco formatos a mano.

### Cuándo no vale la pena

Si no programas, no hay nada que hacer aquí: usa `Picard` o `easytag`. Esta ficha existe porque es la pieza
que sostiene a los demás.

<!-- GUIA:FIN -->
