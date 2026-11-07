# Sui · RikkaApps

*Modern super user interface implementation on Android.*

**Racimo:** shizuku-y-herederos · **Repositorio:** `RikkaApps/Sui` · **Estado:** parado · **Medido:** 2026-11-05 11:40 UTC

## Qué es, según quien lo hace

> Modern super user interface (SUI) implementation on Android. <delThe name, Sui, also comes from a character.</del

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** parado · último empujón el 12 de agosto de 2024 (hace 815 días)
- **Estrellas:** 4.352 · 485 bifurcaciones · 133 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Java · creado el 3 de enero de 2021
- **Última entrega:** `v13.5.1` del 19 de septiembre de 2023 · 2 adjuntos
- **Plataformas que menciona su README:** Android, Web
- **Lo que dice su propio texto:** pide root, pide shizuku, pide magisk
- **Medido:** 2026-11-05 11:40 UTC

## Cómo se consigue

- 2. It is much slower because run a command means at least one new process is started. And `PackageManager#getInstalledApplications` is used inside `pm list`.
- You can download and install Sui from Magisk directly. Or, download the zip from release and use "Install from storage" in Magisk.
- Install the zip with `adb shell su -c magisk --install-module`.
- Install the zip and reboot the device.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/RikkaApps/Sui
- la última entrega: https://github.com/RikkaApps/Sui/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Es la otra forma de darle permisos de sistema a las apps de Shizuku, y la más cómoda **si ya tienes
root**: en vez de un servicio que hay que encender, se instala como módulo de Magisk y el sistema lo
levanta al arrancar. Para quien ya rooteó el teléfono, es un módulo y un reinicio.

### Cómo se instala

1. Descarga el zip desde la última entrega o instálalo desde el propio gestor de módulos de Magisk.
2. Instálalo con el gestor, o desde el ordenador con `adb shell su -c magisk --install-module`.
3. Reinicia el teléfono. A partir de ahí, las apps compatibles con la API de Shizuku lo detectan
   solas, sin emparejamientos ni códigos de seis dígitos.

### Lo que conviene saber antes

La última entrega es del 19 de septiembre de 2023 y el repositorio no se mueve desde agosto de 2024.
Funciona en los teléfonos donde ya funcionaba, y en un Android nuevo puede encontrarse con cambios de
permisos que nadie ha actualizado. No está archivado, y eso no significa que esté mantenido.

### Cuándo no vale la pena

Si no tienes root, Sui no es una opción: su camino es Magisk. Y si lo tienes, Shizuku con root hace
casi lo mismo sin convertir el asunto en un módulo del sistema que hay que quitar antes de una
actualización grande.

<!-- GUIA:FIN -->
