# android_transcribe_app · notune

*Offline voice input keyboard & live subtitle tool for Android*

**Racimo:** teclados-y-dictado · **Repositorio:** `notune/android_transcribe_app` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> An offline, privacy-focused speech-to-text tool for Android, built with Rust. Tap the microphone on the keyboard you already use — your speech is transcribed entirely on-device and typed into any app. Also includes live subtitles and an optional dedicated voice keyboard.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 17 de octubre de 2026 (hace 19 días)
- **Estrellas:** 338 · 54 bifurcaciones · 66 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Java · creado el 22 de noviembre de 2025
- **Última entrega:** `v0.2.3` del 17 de octubre de 2026 · 3 adjuntos
- **Plataformas que menciona su README:** Android, Linux
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Prerequisites
- | Dependency | Installation |
- | **cargo-ndk** | `cargo install cargo-ndk` |
- │ ├── assets/ # Model files (downloaded at build time)

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/notune/android_transcribe_app
- la última entrega: https://github.com/notune/android_transcribe_app/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Herramienta de Android con dos caras: dictado sin conexión que se ofrece al micrófono del teclado que ya usas,
y **subtítulos en vivo** en pantalla para lo que se oye por el micrófono. El reconocimiento ocurre en el propio
teléfono.

### Cómo se usa

1. Se instala la APK de la entrega `v0.2.3`, del 17 de octubre de 2026.
2. Se activa como servicio de reconocimiento de voz, o se abre el modo de subtítulos.
3. En el modo de subtítulos se elige el tamaño del texto y el idioma; la transcripción va apareciendo mientras
   se habla.

### Lo que conviene saber antes

338 estrellas, MIT, escrito en Rust, con versión `0.2.x` y nacido en noviembre de 2025: es un proyecto joven y
pequeño. Su punto interesante es el modo de subtítulos, útil para ver una charla sin sonido o para quien tiene
dificultades de audición. Su límite es la precisión de un motor pequeño corriendo en un teléfono.

### Cuándo no vale la pena

Si quieres dictar textos largos con precisión alta, aquí no está. Y si tu teléfono tiene poca memoria, el
modelo local va a cortar frases.
<!-- GUIA:FIN -->
