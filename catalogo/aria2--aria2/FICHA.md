# aria2 · aria2

*aria2 is a lightweight multi-protocol & multi-source, cross platform download utility operated in command-line. It supports HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink.*

**Racimo:** descargas · **Repositorio:** `aria2/aria2` · **Estado:** lento · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

Su README no tiene un párrafo en prosa que se pueda citar: o es una lista de escudos, o son capturas, o no hay README. Se deja dicho en vez de rellenarlo.

## Lo que se midió

- **Estado:** lento · último empujón el 25 de junio de 2026 (hace 133 días)
- **Estrellas:** 43.414 · 3958 bifurcaciones · 1186 incidencias abiertas
- **Licencia:** GPL-2.0
- **Lenguaje:** C++ · creado el 27 de noviembre de 2010
- **Última entrega:** `release-1.37.0` del 15 de noviembre de 2023 · 6 adjuntos
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega. Su web: https://aria2.github.io/.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/aria2/aria2
- su web: https://aria2.github.io/
- la última entrega: https://github.com/aria2/aria2/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

El motor. Una orden que descarga por HTTP, HTTPS, FTP, SFTP y por enlaces de una sola vía, partiendo cada
archivo en varios trozos y usando varias fuentes a la vez. No tiene ventana: se maneja por comandos o
dejándolo como servicio y hablándole por su interfaz de control, que es lo que usan casi todas las ventanas
de este racimo.

### Cómo se usa

1. Se instala desde el gestor de paquetes de tu sistema —está en todas las distribuciones— o se compila; la
   última entrega etiquetada es `release-1.37.0`, del 15 de noviembre de 2023.
2. Una descarga normal: `aria2c` seguido de la dirección y el número de conexiones (`-x 8 -s 8`).
3. Para dejarlo de servicio se arranca con el control remoto activo y un secreto; desde ahí, `AriaNg` o
   cualquier otra ventana se conecta a él.

### Lo que conviene saber antes

Que las entregas estén paradas desde 2023 **no significa abandono**: el repositorio recibe cambios en 2026
y el programa está terminado, no a medias. Tiene 43.414 estrellas, licencia GPL-2.0 y 1.186 incidencias
abiertas, la mayoría dudas de uso. No es un programa para principiantes: es la pieza que hay debajo de los
programas para principiantes.

### Cuándo no vale la pena

Si no quieres abrir una terminal, no empieces por aquí: instala una de las ventanas del racimo, que ya lo
llevan dentro. `aria2` se justifica en un servidor, en un equipo sin escritorio o para automatizar.

<!-- GUIA:FIN -->
