# wget2 · rockdaboot

*The successor of GNU Wget. Contributions preferred at https://gitlab.com/gnuwget/wget2. But accepted here as well 😍*

**Racimo:** descargas · **Repositorio:** `rockdaboot/wget2` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> GNU Wget2 is the successor of GNU Wget, a file and recursive website downloader.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 21 de octubre de 2026 (hace 15 días)
- **Estrellas:** 800 · 88 bifurcaciones · 30 incidencias abiertas
- **Licencia:** LGPL-3.0
- **Lenguaje:** C · creado el 8 de octubre de 2015
- **Última entrega:** `v2.3.0` del 21 de septiembre de 2026 · 4 adjuntos
- **Plataformas que menciona su README:** Windows, Linux, Web
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Downloading and building from tarball
- Download project and prepare sources with
- Install Wget2 and libwget
- GNU Wget2 is the successor of GNU Wget, a file and recursive website downloader.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/rockdaboot/wget2
- la última entrega: https://github.com/rockdaboot/wget2/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

El sucesor de `wget`: descarga archivos y **sitios completos**, con soporte de conexiones en paralelo,
compresión y reanudación. Es la herramienta de terminal para espejar una web entera o para automatizar
descargas dentro de un guion.

### Cómo se usa

1. Está en el gestor de paquetes de casi todas las distribuciones; si no, se compila. La entrega es la
   `v2.3.0`, del 21 de septiembre de 2026.
2. Un archivo: `wget2` y la dirección. Un sitio: `--recursive` con los límites que quieras —profundidad,
   tipo de archivo, dominio.
3. Con `--continue` se retoma lo cortado y con `--max-threads` se fija el paralelismo.

### Lo que conviene saber antes

El desarrollo principal vive en **GitLab**, no aquí: este repositorio es un espejo que acepta
contribuciones, y así lo dice su propio texto. 800 estrellas, licencia LGPL-3.0. Para espejar un sitio hay
que ser cuidadoso: sin límites, `wget2` se trae la web entera y también lo que no querías.

### Cuándo no vale la pena

Para bajar un archivo suelto, `curl` es más corto de recordar. Y contra sitios que generan el contenido al
vuelo, un espejo no sirve: se trae el cascarón.

<!-- GUIA:FIN -->
