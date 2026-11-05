# Deskdrop · SvReenen

*Android keyboard with local AI (Ollama, Whisper, MCP) or cloud (Gemini, Groq, OpenAI)*

**Racimo:** teclados-con-ia · **Repositorio:** `SvReenen/Deskdrop` · **Estado:** vivo · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> Deskdrop is an Android keyboard with AI built in. Use Ollama, any OpenAI-compatible server, or a cloud API key. Built on HeliBoard.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 59 · 13 bifurcaciones · 4 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Kotlin · creado el 11 de abril de 2026
- **Última entrega:** `v1.3.1` del 21 de abril de 2026 · 1 adjuntos
- **Plataformas que menciona su README:** Android, Windows, Linux, Web
- **Lo que dice su propio texto:** espejo declarado
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- la web que da el proyecto: https://github.com/SvReenen/Deskdrop/releases/latest
- Built for self-hosted setups.** MCP support for Home Assistant and custom tool servers. Primary plus LAN/Tailscale fallback URL.
- Primary + fallback URL for LAN/Tailscale setups
- Install the APK, open Deskdrop, and the setup wizard walks you through everything.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/SvReenen/Deskdrop
- su web: https://svreenen.github.io/Deskdrop/
- la última entrega: https://github.com/SvReenen/Deskdrop/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Teclado de Android con modelos de lenguaje dentro. La idea es que la escritura no salga del teléfono salvo que
tú quieras: puede hablar con un servidor local —Ollama, cualquier servidor compatible con OpenAI— o con una
clave de la nube, y así reescribir, resumir o corregir lo que escribes sin cambiar de aplicación.

Es un derivado de HeliBoard, y eso se nota: la base es un teclado normal, sin predicción en la nube ni
telemetría.

### Cómo se usa

1. Se instala la APK de la entrega `v1.3.1`, del 21 de abril de 2026.
2. Al abrirlo, un asistente pregunta qué motor usar: local, servidor propio o clave de la nube.
3. Para un modelo en casa, se indica la dirección del servidor; admite una principal y otra de respaldo para
   redes locales o Tailscale.
4. Se activa el teclado en los ajustes del sistema y se elige como método de entrada.

### Lo que conviene saber antes

59 estrellas, GPL-3.0, Kotlin, creado el 11 de abril de 2026, con 13 bifurcaciones, 4 incidencias abiertas y
movimiento de hoy. La entrega, en cambio, es de abril: **el código va por delante de la APK publicada**, así que
quien quiera lo último tendrá que compilar.

Dos cosas que conviene pensar antes de instalarlo. La primera, que la parte de IA funciona contra un servidor
que hay que tener; sin Ollama o sin clave, el teclado queda en teclado. La segunda, y más importante: **un
teclado lo ve todo lo que escribes**, incluidas contraseñas. Aquí el modelo va donde tú decidas, y esa decisión
es la que vale.

### Cuándo no vale la pena

Si no tienes un servidor donde correr el modelo, la función principal no existe. Y si solo querías un teclado
que corrija bien, hay opciones más maduras y con más años de uso.

<!-- GUIA:FIN -->
