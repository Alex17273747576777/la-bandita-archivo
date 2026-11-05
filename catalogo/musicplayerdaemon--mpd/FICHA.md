# MPD · MusicPlayerDaemon

*Music Player Daemon*

**Racimo:** audio · **Repositorio:** `MusicPlayerDaemon/MPD` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> A daemon for playing music of various formats. Music is played through the server's audio device. The daemon stores info about all available music, and this info can be easily searched and retrieved. Player control, info retrieval, and playlist management can all be managed remotely.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 2.812 · 436 bifurcaciones · 133 incidencias abiertas
- **Licencia:** GPL-2.0
- **Lenguaje:** C++ · creado el 16 de febrero de 2012
- **Última entrega:** sin entregas etiquetadas
- **Plataformas que menciona su README:** Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- For basic installation instructions
- read the manual.
- Manual, or see `/usr/share/doc/mpd/html` in your installation

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/MusicPlayerDaemon/MPD
- su web: https://www.musicpd.org/

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Demonio reproductor: se queda corriendo en el equipo, tiene tu música indexada y la reproduce por la salida
de sonido del servidor. No tiene ventana propia; se le controla desde cualquier cliente —hay decenas— por
red, y por eso es la pieza que sostiene a otros programas de este racimo.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución; aquí no hay entregas.
2. Se edita su archivo de configuración con la carpeta de música, la salida de audio y, si hace falta, el
   acceso por red.
3. Se arranca el servicio y se conecta un cliente; desde él se busca, se encola y se reproduce.

### Lo que conviene saber antes

2.812 estrellas, GPL-2.0, y una estabilidad que viene de su edad: nació en 2003 y su interfaz no ha cambiado.
Todo se configura en un archivo de texto, y eso es a la vez su virtud —se puede automatizar entero— y su
pega —si te equivocas en una línea, no hay ventana que te lo diga.

### Cuándo no vale la pena

Para escuchar música en el ordenador de casa, es fontanería innecesaria: un reproductor con ventana hace
eso. MPD tiene sentido en un equipo sin pantalla, en una casa con varios clientes, o cuando quieres que la
música siga sonando al cerrar la sesión.

<!-- GUIA:FIN -->
