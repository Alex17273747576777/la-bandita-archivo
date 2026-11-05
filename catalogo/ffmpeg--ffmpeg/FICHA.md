# FFmpeg · FFmpeg

*Mirror of https://git.ffmpeg.org/ffmpeg.git*

**Racimo:** audio · **Repositorio:** `FFmpeg/FFmpeg` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 66.537 · 14519 bifurcaciones · 3 incidencias abiertas
- **Licencia:** NOASSERTION
- **Lenguaje:** C · creado el 14 de abril de 2011
- **Última entrega:** sin entregas etiquetadas
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega. Su web: https://ffmpeg.org/.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/FFmpeg/FFmpeg
- su web: https://ffmpeg.org/

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

El juego de programas que convierte, corta, une, recodifica y mide audio y vídeo. No es una aplicación con
ventana: es la pieza que hay dentro de casi todas las demás de este racimo. Cuando un programa te pregunta
«¿con qué convierto esto?», la respuesta suele ser `ffmpeg`.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución, o se descarga una compilación ya hecha. Este
   repositorio es **un espejo**: el original vive en `git.ffmpeg.org` y así lo dice su descripción.
2. Convertir un archivo: `ffmpeg -i entrada.wav -codec:a libopus -b:a 96k salida.opus`.
3. Sacar sólo el sonido de un vídeo: `ffmpeg -i video.mp4 -vn -codec:a copy audio.m4a`.
4. Mirar qué trae un archivo, sin tocar nada: `ffprobe archivo.mp3`.

### Lo que conviene saber antes

66.537 estrellas y **ninguna entrega publicada en GitHub**: las versiones se cogen de la web del proyecto o
del paquete de tu sistema. GitHub **no le reconoce la licencia** («NOASSERTION») porque convive con
bibliotecas de varias condiciones; si vas a distribuirlo dentro de algo tuyo, revisa qué compilación coges,
porque no todas tienen las mismas.

### Cuándo no vale la pena

Para convertir una canción una vez, cualquier web lo hace sin instalar 300 MB de herramientas. `FFmpeg` se
justifica cuando repites la operación, cuando automatizas, o cuando quieres saber exactamente qué se le hace
al archivo.

<!-- GUIA:FIN -->
