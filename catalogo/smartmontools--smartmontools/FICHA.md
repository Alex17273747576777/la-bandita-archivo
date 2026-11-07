# smartmontools · smartmontools

*2025-06-01: This is now the official upstream repository of smartmontools*

**Racimo:** torrentes · **Repositorio:** `smartmontools/smartmontools` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> Smartmontools was originally derived from the Linux smartsuite package and supports ATA/SATA, SCSI/SAS, and NVMe disks and also SCSI/SAS tape devices. It should run on any modern Linux, FreeBSD, NetBSD, OpenBSD, Darwin (macOS), Solaris, Windows, Cygwin, OS/2, eComStation, or QNX system. Smartmontools can also be run from one of many different Live CDs/DVDs.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 3 de noviembre de 2026 (hace 2 días)
- **Estrellas:** 1.460 · 304 bifurcaciones · 99 incidencias abiertas
- **Licencia:** GPL-2.0
- **Lenguaje:** C++ · creado el 29 de septiembre de 2017
- **Última entrega:** `RELEASE_7_5` del 12 de mayo de 2025 · 9 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega. Su web: https://www.smartmontools.org/browser.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/smartmontools/smartmontools
- su web: https://www.smartmontools.org/browser
- la última entrega: https://github.com/smartmontools/smartmontools/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Los dos programas clásicos para preguntarle a un disco cómo está: `smartctl` lee los datos internos que el
propio disco lleva contando desde el primer día —horas encendido, sectores reasignados, errores, temperatura— y
`smartd` vigila en segundo plano y avisa cuando algo se tuerce.

Para quien guarda archivos grandes de verdad, esto es lo que separa una pérdida de datos de un susto.

### Cómo se usa

1. Se instala desde los paquetes del sistema o desde el código fuente.
2. `smartctl -a /dev/sdX` muestra todo lo que el disco declara sobre sí mismo.
3. La prueba corta —`smartctl -t short /dev/sdX`— dura dos minutos y conviene hacerla de vez en cuando.
4. `smartd` se deja como servicio y manda correo cuando un valor cruza el umbral.

### Lo que conviene saber antes

1.460 estrellas, GPL-2.0, C++, con 304 bifurcaciones y 99 incidencias abiertas. Este repositorio es el sitio
oficial del proyecto desde 2017; su última entrega es `RELEASE_7_5`, del 12 de mayo de 2025, y el trabajo sigue
a diario.

Funciona con discos ATA/SATA, SCSI/SAS, NVMe y cintas, y en casi cualquier sistema operativo que exista. Dos
límites que conviene saber: **detrás de un adaptador USB barato no siempre se puede leer**, y un «disco sano»
hoy puede morir mañana; los valores sirven para ver tendencias, no para predecir.

### Cuándo no vale la pena

En un portátil con un único disco del sistema, leer sus datos una vez al año basta. Y si usas un servidor en la
nube, el disco no está a tu alcance: eso lo vigila quien te lo alquila.

<!-- GUIA:FIN -->
