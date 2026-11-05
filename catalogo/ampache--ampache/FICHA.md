# ampache · ampache

*A web based audio/video streaming application and file manager allowing you to access your music & videos from anywhere, using almost any internet enabled device.*

**Racimo:** audio · **Repositorio:** `ampache/ampache` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Ampache8 is now a work in progress and has become the mainline.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 3.845 · 609 bifurcaciones · 229 incidencias abiertas
- **Licencia:** AGPL-3.0
- **Lenguaje:** PHP · creado el 21 de marzo de 2013
- **Última entrega:** `8.3.0` del 20 de octubre de 2026 · 8 adjuntos
- **Plataformas que menciona su README:** Android, Web
- **Lo que dice su propio texto:** abandono declarado
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- Installation
- Please see the wiki and don't forget to check out the basic config guide after that.
- Required PHP modules (the `ext-` requirements of composer.json, plus the MySQL driver and the modules the installer checks):
- Node.js `^20.19.0 || >=22.12.0`, and the npm that ships with it (Required in Ampache 7.0.0 and higher)

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/ampache/ampache
- su web: http://ampache.org
- la última entrega: https://github.com/ampache/ampache/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Servidor de música y vídeo por web, escrito en PHP: se instala en un alojamiento normal, apunta a la carpeta
de archivos y da acceso a la colección desde el navegador o desde clientes que hablen su interfaz. Lleva
años en el ecosistema y tiene fama de aguantar bibliotecas grandes.

### Cómo se usa

1. Se despliega en un servidor web con PHP y base de datos; la entrega medida es la `8.3.0`, del 20 de octubre
   de 2026.
2. En el instalador se define la carpeta de música, el usuario administrador y el modo de catalogación.
3. Se añade un cliente o se usa la web; la catalogación inicial hay que lanzarla a mano y puede tardar.

### Lo que conviene saber antes

3.845 estrellas, AGPL-3.0. Su texto avisa de que la versión 8 es la línea principal y todavía está en
construcción, así que conviene leer las notas de cada entrega. Al ser PHP, se instala en cualquier
alojamiento barato, y eso es justo lo que otros servidores de este racimo no permiten.

### Cuándo no vale la pena

Si no tienes ya un servidor web con PHP, montar el entorno cuesta más que instalar otro servidor con un solo
comando. Y si tu colección es pequeña, sobra potencia.

<!-- GUIA:FIN -->
