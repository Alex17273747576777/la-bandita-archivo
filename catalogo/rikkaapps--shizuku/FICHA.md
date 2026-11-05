# Shizuku · RikkaApps

*Using system APIs directly with adb/root privileges from normal apps through a Java process started with app_process.*

**Racimo:** shizuku-y-herederos · **Repositorio:** `RikkaApps/Shizuku` · **Estado:** parado · **Medido:** 2026-11-05 11:40 UTC

## Qué es, según quien lo hace

> When developing apps that requires root, the most common method is to run some commands in the su shell. For example, there is an app that uses the pm enable/disable command to enable/disable components.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** parado · último empujón el 18 de junio de 2025 (hace 505 días)
- **Estrellas:** 32.840 · 3551 bifurcaciones · 702 incidencias abiertas
- **Licencia:** Apache-2.0
- **Lenguaje:** Kotlin · creado el 24 de mayo de 2017
- **Última entrega:** `v13.6.0` del 25 de mayo de 2025 · 1 adjuntos
- **Plataformas que menciona su README:** Android, Web
- **Lo que dice su propio texto:** pide root, pide shizuku, pide magisk, espejo declarado
- **Medido:** 2026-11-05 11:40 UTC

## Cómo se consigue

- User guide & Download

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/RikkaApps/Shizuku
- la última entrega: https://github.com/RikkaApps/Shizuku/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Es el programa que le da a otras aplicaciones los permisos del sistema sin que el teléfono esté
rooteado. No hace nada visible por sí solo: enciende un servicio y las apps que lo piden (Hail, Canta,
ShizukuTools, Inure…) pueden desinstalar, congelar o cambiar ajustes que normalmente exigirían root.

### Cómo se enciende

Con **root**, el servicio arranca solo al reiniciar. Sin root, hay que encenderlo cada vez que el
teléfono se apaga, y el camino es el de la depuración inalámbrica:

1. Ajustes → Información del teléfono → toca siete veces «Número de compilación» para activar las
   opciones de desarrollador.
2. Ajustes → Sistema → Opciones de desarrollador → activa **Depuración inalámbrica** (Android 11 o
   superior) y conecta el teléfono a la misma red que el equipo desde el que vas a emparejar.
3. Abre Shizuku, pulsa «Empezar», elige «Depuración inalámbrica» y sigue el emparejamiento con el
   código de seis dígitos que muestra el sistema.
4. En Android 10 o anterior hace falta un cable y `adb` en un ordenador: no hay depuración
   inalámbrica que empareje sola.

### Lo que conviene saber antes

El último empujón del repositorio es del 18 de junio de 2025 —**505 días** antes de esta ficha— y la
última entrega, la v13.6.0, del 25 de mayo de 2025: el proyecto no está archivado, y precisamente por
eso el catálogo lo marca «parado» y no «vivo». No está roto; está quieto, que en un catálogo es un dato
distinto. Los forks que salieron de aquí —Stellar, ShizukuPlus,
Shizuku-Next— publican versiones más recientes y son la razón de que el ecosistema siga vivo aunque
el original esté quieto.

### Cuándo no vale la pena

Si el teléfono es de trabajo, si tiene una cuenta de empresa o si no puedes activar la depuración,
Shizuku no arranca y su función estrella —desinstalar sin root— se queda en nada. En ese caso la
alternativa es el camino de ADB desde un ordenador, que hace lo mismo de una vez y no hay que
mantenerlo encendido.

<!-- GUIA:FIN -->
