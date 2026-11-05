# vocalinux · VocaHQ

*Free, open-source, 100% offline voice dictation for Linux. Speak and type anywhere via whisper.cpp, Whisper & VOSK engines, GPU-accelerated, works on X11 + Wayland!*

**Racimo:** teclados-y-dictado · **Repositorio:** `VocaHQ/vocalinux` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> Vocalinux turns speech into typed text in whatever app has focus. It is a free, AGPL-3.0-licensed desktop app for X11 and Wayland. After you download a model, local engines (whisper.cpp by default, plus OpenAI Whisper, Faster Whisper, VOSK, and Parakeet) run speech-to-text on your machine. An optional remote HTTP API is off unless you configure it.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 994 · 110 bifurcaciones · 15 incidencias abiertas
- **Licencia:** AGPL-3.0
- **Lenguaje:** Python · creado el 12 de abril de 2025
- **Última entrega:** `v0.18.5` del 27 de octubre de 2026 · 12 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux, Web
- **Lo que dice su propio texto:** espejo declarado
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- la web que da el proyecto: https://www.python.org/downloads/
- Website · Install · Docs · Releases
- No Voca account is required. Models download once. After that, speech-to-text stays on your machine.
- On-device after model download**: Local engines; speech-to-text stays on your machine

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/VocaHQ/vocalinux
- su web: https://vocalinux.com/
- la última entrega: https://github.com/VocaHQ/vocalinux/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Dictado por voz para **Linux**, sin conexión: se habla y el texto se escribe en la ventana que tenga el foco,
funcione con X11 o con Wayland. Admite varios motores locales —el de referencia es `whisper.cpp`, pero
también Whisper y VOSK— y aprovecha la tarjeta gráfica cuando la hay.

### Cómo se usa

1. Se instala desde la entrega `v0.18.5`, del 27 de octubre de 2026, o desde el paquete de tu distribución.
2. La primera vez se descarga un modelo; el tamaño decide la precisión y la memoria que ocupa.
3. Se elige el atajo de teclado y el motor; al pulsarlo se empieza a dictar y al soltarlo se escribe.
4. En Wayland conviene revisar los permisos de la sesión: es la parte que más falla en ese entorno.

### Lo que conviene saber antes

994 estrellas, AGPL-3.0, escrito en Python, y versión `0.18`: está en construcción activa desde abril de 2025.
Es de los pocos proyectos de dictado que trata Wayland como ciudadano de primera, y eso ya justifica su
existencia. Su dependencia del modelo hace que en un equipo modesto la primera frase tarde.

### Cuándo no vale la pena

Si usas Windows o macOS, aquí no hay nada. Y si tu equipo es muy antiguo, mover el modelo en el procesador va
a ser más lento que escribir.

<!-- GUIA:FIN -->
