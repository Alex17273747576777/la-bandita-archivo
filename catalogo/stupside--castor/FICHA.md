# castor · stupside

*Point it at any web page and it finds the video, transcodes it, and streams it to your TV in real time. It even burns in subtitles.*

**Racimo:** reemplazo-del-stack · **Repositorio:** `stupside/castor` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Cast web video to your TV, even when it has no built-in casting like Chromecast. Point it at any web page and it finds the video, transcodes it, and streams it to your TV in real time. It even burns in subtitles.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 28 de octubre de 2026 (hace 8 días)
- **Estrellas:** 2.528 · 102 bifurcaciones · 3 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Go · creado el 8 de febrero de 2026
- **Última entrega:** `v2.5.0` del 27 de octubre de 2026 · 7 adjuntos
- **Plataformas que menciona su README:** Android, Windows, macOS, Linux, Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- brew install --cask stupside/tap/castor # macOS
- npm install -g @castor-dev/cli # any platform, Node 20+
- Or download the latest release, or build from source.
- | Setup | Run on the NAS | Add to your `config.yaml` |

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/stupside/castor
- la última entrega: https://github.com/stupside/castor/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Manda a la televisión un vídeo que está incrustado en una página web que no ofrece Chromecast. Encuentra
el vídeo en la página que le indiques, lo transcodifica al vuelo y lo emite a un Chromecast o a un
televisor compatible.

### Cómo se usa

1. Se instala con `brew install --cask stupside/tap/castor` en macOS, con `npm install -g @castor-dev/cli`
   en cualquier sistema con Node 20 o superior, o desde su última entrega (`v2.5.0`, del 27 de octubre de
   2026).
2. Se le pasa la dirección de la página y el destino; opcionalmente, subtítulos para incrustar.
3. La transcodificación se hace en el equipo donde corre: con vídeo pesado, el ventilador se entera.

### Lo que conviene saber antes

Solo sirve para contenido que la propia página te deja ver: no salta muros de pago ni protecciones. Y
hace falta estar en la misma red que el televisor.

<!-- GUIA:FIN -->
