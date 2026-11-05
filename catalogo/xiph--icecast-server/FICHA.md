# Icecast-Server · xiph

*Icecast streaming media server (Mirror) - Please report bugs at https://gitlab.xiph.org/xiph/icecast-server/issues*

**Racimo:** audio · **Repositorio:** `xiph/Icecast-Server` · **Estado:** lento · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> Icecast 2 - README ---------------------------------------------------------------------

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 19 de agosto de 2026 (hace 78 días)
- **Estrellas:** 557 · 137 bifurcaciones · 31 incidencias abiertas
- **Licencia:** GPL-2.0
- **Lenguaje:** C · creado el 3 de diciembre de 2014
- **Última entrega:** sin entregas etiquetadas
- **Plataformas que menciona su README:** Web
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- Prerequisites
- A note about prerequisite packages
- pre-built packages (eg rpm, deb etc). These setups often have a runtime
- package, which is usually installed for you by default, and enables you

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/xiph/Icecast-Server
- su web: https://icecast.org

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Servidor de **radiodifusión por internet**: recibe un flujo de audio de un programa emisor y lo reparte a
tantos oyentes como aguante el equipo, en varios formatos. Es la pieza clásica para montar una radio propia o
para retransmitir una señal interna.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución. Este repositorio es **un espejo**: los fallos se
   reportan en GitLab y aquí no hay entregas.
2. Se configura el punto de montaje, la contraseña de emisión y los límites de oyentes.
3. Se conecta un programa emisor con esas credenciales y se comprueba desde la página de estado del servidor.

### Lo que conviene saber antes

557 estrellas, GPL-2.0, con cambios en agosto de 2026. Es infraestructura con veinte años encima: fiable y
sin sorpresas si se configura bien, y expuesta a abuso si se deja abierta, porque cualquiera con la
contraseña emite. Ojo con el ancho de banda: cada oyente consume lo suyo.

### Cuándo no vale la pena

Para escuchar tu música en casa no hace falta: esto es para emitir a otros. Y si sólo quieres oír una radio,
eres oyente, no servidor.

<!-- GUIA:FIN -->
