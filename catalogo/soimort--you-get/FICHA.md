# you-get · soimort

*:arrow_double_down: Dumb downloader that scrapes the web*

**Racimo:** descargas · **Repositorio:** `soimort/you-get` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> NOTICE (30 May 2022): Support for Python 3.5, 3.6 and 3.7 will eventually be dropped. (see details here))

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 6 de octubre de 2026 (hace 30 días)
- **Estrellas:** 56.862 · 9661 bifurcaciones · 384 incidencias abiertas
- **Licencia:** NOASSERTION
- **Lenguaje:** Python · creado el 20 de agosto de 2012
- **Última entrega:** `v0.4.1743` del 4 de enero de 2025 · 4 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Lo que dice su propio texto:** abandono declarado, espejo declarado
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- You-Get is a tiny command-line utility to download media contents (videos, audios, images) from the Web, in case there is no other handy way to do it.
- Here's how you use `you-get` to download a video from YouTube:
- download-with: you-get --itag=43 [URL]
- Downloading Me at the zoo.webm ...

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/soimort/you-get
- su web: https://you-get.org/
- la última entrega: https://github.com/soimort/you-get/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Descargador de terminal escrito en Python, veterano y de una sola orden: le das una dirección de vídeo o de
audio y lo baja, con las calidades que encuentre. Su fuerte histórico son los sitios chinos, aunque cubre
muchos más.

### Cómo se usa

1. Se instala con `pip install you-get`, o desde el gestor de paquetes del sistema.
2. `you-get -i` y la dirección muestra lo que hay disponible, sin descargar.
3. `you-get` y la dirección descarga; con `-o` se fija la carpeta y con `--format` la calidad.

### Lo que conviene saber antes

56.862 estrellas y una entrega `v0.4.1743` de **enero de 2025**, con cambios en el repositorio hasta
octubre de 2026. **GitHub no le reconoce la licencia** —aparece como «NOASSERTION»—, así que si vas a
reutilizar su código, mira el archivo antes. Su propio texto avisa de que dejará de admitir versiones viejas
de Python; conviene tener una versión reciente.

### Cuándo no vale la pena

Para YouTube y los sitios grandes, `yt-dlp` está más al día. `you-get` sigue teniendo sentido en su terreno
—los sitios chinos— y por la sencillez: una orden, sin configuración.

<!-- GUIA:FIN -->
