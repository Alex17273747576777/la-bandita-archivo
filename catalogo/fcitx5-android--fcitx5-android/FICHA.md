# fcitx5-android · fcitx5-android

*Fcitx5 input method framework and engines ported to Android*

**Racimo:** teclados-con-ia · **Repositorio:** `fcitx5-android/fcitx5-android` · **Estado:** vivo · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> <img src="https://github.com/rubenpgrady/get-it-on-github/raw/refs/heads/main/get-it-on-github.png" alt="Git it on GitHub" width="207" height="80" <img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png" alt="Get it on F-Droid" width="207" height="80" <img alt="Get it on Google Play" src="https://play.google.com/intl/enus/badges/static/images/badges/enbadgewebgeneric.png" width="207" height

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 13 de octubre de 2026 (hace 23 días)
- **Estrellas:** 5.843 · 501 bifurcaciones · 115 incidencias abiertas
- **Licencia:** LGPL-2.1
- **Lenguaje:** Kotlin · creado el 10 de junio de 2021
- **Última entrega:** `0.1.3` del 26 de julio de 2026 · 47 adjuntos
- **Plataformas que menciona su README:** Android, iOS, Windows, macOS, Linux, Web
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- APKs downloaded from GitHub Release/F-Droid/Jenkins have the same signature, which means they're compatible when upgrading, but Google Play's do not.
- Plugin System for loading addons from other installed apk
- Android NDK (Side by side) 25 & CMake 3.22.1, they can be installed using SDK Manager in Android Studio or `sdkmanager` command line.
- GNU Gettext >= 0.20 (for `msgfmt` binary; or install `appstream` if you really have to use gettext <= 0.19.)

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/fcitx5-android/fcitx5-android
- su web: https://fcitx5-android.github.io/
- la última entrega: https://github.com/fcitx5-android/fcitx5-android/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Trae a Android el marco de métodos de entrada de Fcitx5, el que se usa en Linux: motores de chino, japonés,
coreano y vietnamita, además de los teclados latinos, con la misma arquitectura de complementos que en el
escritorio.

Para quien escribe en esas lenguas, la diferencia es grande: aquí hay motores de conversión de verdad, no un
teclado que traduce palabras sueltas.

### Cómo se usa

1. Se instala la APK de la entrega `0.1.3`, del 26 de julio de 2026; hay 47 adjuntos con variantes por
   arquitectura.
2. Se activa el teclado en los ajustes del sistema.
3. Se añaden motores desde el propio teclado: cada uno es un complemento que se instala aparte.
4. Se configura la disposición y el método de conversión por idioma.

### Lo que conviene saber antes

5.843 estrellas, LGPL-2.1, Kotlin, creado en junio de 2021, con 501 bifurcaciones, 115 incidencias abiertas y
movimiento del 13 de octubre de 2026. Sigue en 0.1: después de cinco años, el número no ha llegado a 1.

Hay un detalle sobre las firmas que el proyecto explica y que conviene leer entero: las APK de GitHub, F-Droid
y su servidor de integración comparten firma, así que se puede actualizar de una a otra sin desinstalar; **las
de Google Play, no**. Mezclarlas obliga a borrar datos.

### Cuándo no vale la pena

Si escribes solo en español, el aparato de complementos es más de lo que necesitas. Y si vienes de Fcitx en el
escritorio esperando la misma configuración exacta, la versión móvil tiene menos piezas.

<!-- GUIA:FIN -->
