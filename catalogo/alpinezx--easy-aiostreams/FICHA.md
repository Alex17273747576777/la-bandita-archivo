# easy-aiostreams · alpinezx

*One-command installer for a self-hosted AIOStreams instance, on a VPS or a computer at home*

**Racimo:** reemplazo-del-stack · **Repositorio:** `alpinezx/easy-aiostreams` · **Estado:** vivo · **Medido:** 2026-11-05 11:42 UTC

## Qué es, según quien lo hace

> A one-command installer for a self-hosted AIOStreams instance. It sets up Docker, Caddy (automatic HTTPS via Let's Encrypt), and secure login access to the config page and dashboard, all in one script. Restricted to your own credentials.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 57 · 6 bifurcaciones · 1 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Shell · creado el 14 de agosto de 2026
- **Última entrega:** `v1.5.2` del 3 de noviembre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Web
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:42 UTC

## Cómo se consigue

- Installing for the first time?** You can skip this.
- Prerequisites
- A management menu for status, restart, updates, backups, and clean uninstall
- <sub>The control panel's demo mode, with every add-on running. Your own panel shows only what you've installed.</sub>

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/alpinezx/easy-aiostreams
- la última entrega: https://github.com/alpinezx/easy-aiostreams/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Instalador de un comando para levantar AIOStreams en un servidor propio o en un ordenador de casa, sin
tener que escribir el archivo de composición ni recordar los pasos.

### Cómo se usa

1. En un VPS o en un equipo con Docker, se ejecuta el instalador de su última entrega (`v1.5.2`, del 4 de
   noviembre de 2026).
2. El asistente pide dominio o IP, puerto y poco más, y deja el servicio levantado.
3. Después se entra en el configurador de AIOStreams y se sigue por ahí.

### Cuándo no vale la pena

Si no vas a usar AIOStreams, esto no sirve para nada: es su instalador. Y si ya sabes usar Docker
Compose, sus veinte líneas hacen lo mismo con menos capas de confianza.

<!-- GUIA:FIN -->
