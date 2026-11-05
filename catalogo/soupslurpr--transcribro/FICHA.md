# Transcribro · soupslurpr

*Private and on-device speech recognition keyboard and service for Android.*

**Racimo:** teclados-y-dictado · **Repositorio:** `soupslurpr/Transcribro` · **Estado:** lento · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> Transcribro is a private and on-device speech recognition keyboard and service for Android.\ It uses whisper.cpp to run the OpenAI Whisper family of models and Silero VAD for voice activity detection.\ It features a voice input keyboard, enabling you to type with speech.\ It can also be used by other apps either explicitly or when set as the user-selected speech to text app which some apps may use

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 29 de septiembre de 2026 (hace 37 días)
- **Estrellas:** 761 · 39 bifurcaciones · 22 incidencias abiertas
- **Licencia:** ISC
- **Lenguaje:** Kotlin · creado el 15 de marzo de 2024
- **Última entrega:** `7` del 7 de agosto de 2025 · 1 adjuntos
- **Plataformas que menciona su README:** Android, iOS
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- The package name and SHA-256 hash of the signing certificate is below, so if you are downloading the APK, you can
- If you are downloading from Accrescent then you should verify

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/soupslurpr/Transcribro
- la última entrega: https://github.com/soupslurpr/Transcribro/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Teclado de Android que reconoce la voz **en el propio aparato**: incluye la detección de cuándo empiezas y
acabas de hablar, de modo que no hay que pulsar nada para empezar ni para cortar. Se puede usar como teclado
completo o sólo como servicio de reconocimiento para el teclado que ya tengas.

### Cómo se usa

1. Se instala la APK de la entrega `7`, del 7 de agosto de 2025.
2. En la primera ejecución se descarga un modelo; hay varios tamaños.
3. Se activa como teclado o como servicio de voz, y se habla: la detección de voz corta sola cuando callas.

### Lo que conviene saber antes

761 estrellas, licencia ISC —permisiva y poco habitual—, con desarrollo en 2026 pero **entrega de agosto de
2025**. Es decir: el código va por delante de lo que puedes descargar. Su mezcla de reconocimiento local y
detección de actividad de voz es lo que lo hace cómodo, y su límite es la precisión de los modelos pequeños.

### Cuándo no vale la pena

Si buscas la última versión de cada arreglo, la entrega tiene más de un año. Y si tu teléfono es modesto, el
modelo local y la detección de voz compiten por la misma memoria.
<!-- GUIA:FIN -->
