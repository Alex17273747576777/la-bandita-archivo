# foliate · johnfactotum

*Read e-books in style*

**Racimo:** reemplazo-del-stack · **Repositorio:** `johnfactotum/foliate` · **Estado:** lento · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> - gjs (= 1.82) - gtk4 (= 4.12) - libadwaita (= 1.8; gir1.2-adw-1 in Debian-based distros) - webkitgtk-6.0 (webkitgtk6.0 in Fedora; gir1.2-webkit-6.0 in Debian-based distros)

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 8 de abril de 2026 (hace 211 días)
- **Estrellas:** 8.869 · 435 bifurcaciones · 340 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** JavaScript · creado el 26 de mayo de 2019
- **Última entrega:** `3.3.0` del 1 de abril de 2025 · 3 adjuntos
- **Plataformas que menciona su README:** Linux
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- Installation
- For text-to-speech support, install `speech-dispatcher` and output modules such as `espeak-ng`.
- If installed, `tracker` (>= 3; `gir1.2-tracker-3.0` in Debian-based distros) and `tracker-miners` can be used to track the locations of files.
- The repo uses git submodules. Before running or installing, make sure you clone the whole thing with `--recurse-submodules`:

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/johnfactotum/foliate
- su web: https://johnfactotum.github.io/foliate/
- la última entrega: https://github.com/johnfactotum/foliate/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Lector de libros para el escritorio de Linux, con interfaz de GNOME: limpio, con tipografía cuidada,
anotaciones, diccionario y lectura en voz alta si el sistema tiene las voces instaladas. Fue el punto de
partida de Readest.

### Cómo se usa

1. En Debian y Ubuntu se instala el paquete `foliate`; si no está, hay Flatpak oficial.
2. Necesita las bibliotecas de GNOME que su README lista —`gjs`, `gtk4`, `libadwaita` y `webkitgtk-6.0`—;
   sin ellas no arranca, y ese es el fallo más común.
3. Para la voz hay que instalar `speech-dispatcher` y una voz como `espeak-ng`.

### Lo que conviene saber antes

El repositorio se movió por última vez en abril de 2026 y su última entrega es del 1 de abril de 2025:
va despacio, porque su autor está trabajando en Readest. No está muerto; está en segundo plano, y eso en
una ficha se escribe.

<!-- GUIA:FIN -->
