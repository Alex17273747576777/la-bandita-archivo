# AppManager · MuntashirAkon

*A full-featured package manager and viewer for Android*

**Racimo:** shizuku-y-herederos · **Repositorio:** `MuntashirAkon/AppManager` · **Estado:** vivo · **Medido:** 2026-11-05 11:40 UTC

## Qué es, según quien lo hace

> - Revoke runtime (AKA dangerous) and development permissions - Change the mode of an app op - Display/kill/force-stop running apps or processes - Clear app data or app cache - View/change net policy - Control battery optimization - Freeze/unfreeze apps

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 3 de noviembre de 2026 (hace 2 días)
- **Estrellas:** 9.457 · 529 bifurcaciones · 194 incidencias abiertas
- **Licencia:** NOASSERTION
- **Lenguaje:** Java · creado el 30 de mayo de 2020
- **Última entrega:** `v4.1.1` del 4 de septiembre de 2026 · 2 adjuntos
- **Plataformas que menciona su README:** Android
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:40 UTC

## Cómo se consigue

- Install/uninstall APK files (including APKS, APKM and XAPK with OBB files)
- Sign APK files with custom signatures before installing
- Systemless disabling/uninstalling of the system apps

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/MuntashirAkon/AppManager
- su web: http://muntashir.dev/AppManager/
- la última entrega: https://github.com/MuntashirAkon/AppManager/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Es el navaja suiza de las aplicaciones de Android: ver permisos, revocarlos, ver qué hace una app por
dentro, congelarla, hacer copias de seguridad, leer sus registros y ejecutar operaciones que el sistema
esconde. Funciona con root, con Shizuku o con ADB, y esa variedad es su mejor argumento y su mayor
complicación.

### Cómo se usa sin root

1. Enciende Shizuku (o conecta por ADB desde un ordenador).
2. Abre AppManager y elige el modo de funcionamiento; pedirá el permiso correspondiente.
3. Desde la lista de apps, cada una abre una ficha con pestañas: permisos, actividades, servicios,
   receptores, registros y operaciones.
4. Todo lo que cambia algo pide confirmación y avisa si es irreversible.

### Lo que conviene saber antes

Entrega `v4.1.1` y repositorio con empujón del 3 de noviembre de 2026: vivo. Su licencia aparece en
GitHub como NOASSERTION porque es la GPL-3.0 con una excepción propia; quien vaya a reutilizar código,
lee el archivo de licencia y no se fía de la etiqueta.

### Cuándo no vale la pena

Es mucha herramienta para quien solo quiere congelar una app: para eso, Hail o Canta son tres pantallas
menos. AppManager se justifica cuando de verdad quieres mirar dentro.

<!-- GUIA:FIN -->
