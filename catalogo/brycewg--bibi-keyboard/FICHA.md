# BiBi-Keyboard · BryceWG

*说点啥（BiBi Keyboard）:一个基于 Kotlin 的 Android 平台的 LLM 与 ASR 语音输入法键盘应用 An LLM ASR voice input method keyboard application for the Android platform based on Kotlin*

**Racimo:** teclados-y-dictado · **Repositorio:** `BryceWG/BiBi-Keyboard` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> - 长按录音 - 简单直观的录音操作 - 智能判停 - 静音自动停止录音，无需手动操作 - 极速识别 - 松开即上传，快速返回结果 - 多引擎支持 - 18 个 ASR 供应商（12 个云端 + 6 个本地） - 本地 ASR 模型 - SenseVoice / FunASR Nano / Qwen3-ASR / Parakeet / FireRedASR / X-ASR，离线可用 - 主备与本地兜底 - 支持备用引擎与本地备用驻留，网络不稳时更可靠 - AI 文本润色 - LLM 润色修正识别结果；历史可缓存音频并重跑识别或润色

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 3 de noviembre de 2026 (hace 2 días)
- **Estrellas:** 862 · 62 bifurcaciones · 14 incidencias abiertas
- **Licencia:** Apache-2.0
- **Lenguaje:** Kotlin · creado el 6 de octubre de 2025
- **Última entrega:** `v4.5.3` del 26 de octubre de 2026 · 2 adjuntos
- **Plataformas que menciona su README:** Android
- **Lo que dice su propio texto:** pide magisk
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega. Su web: https://bibi.brycewg.com.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/BryceWG/BiBi-Keyboard
- su web: https://bibi.brycewg.com
- la última entrega: https://github.com/BryceWG/BiBi-Keyboard/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Teclado de dictado por voz para Android construido alrededor de un motor de reconocimiento: se mantiene
pulsada la tecla, se habla y el texto aparece. Admite varios proveedores de reconocimiento, unos en la nube y
otros en el propio teléfono, y modelos locales de varios fabricantes.

### Cómo se usa

1. Se instala la APK de la entrega `v4.5.3`, del 26 de octubre de 2026.
2. En sus ajustes se elige el motor: en la nube hace falta una clave del proveedor; en local hay que
   descargar el modelo, que ocupa bastante.
3. Se activa como teclado y se pulsa la tecla de micrófono; el envío es al soltar, y se puede configurar el
   silencio para que corte solo.

### Lo que conviene saber antes

862 estrellas, Apache-2.0, y su documentación está en chino; la interfaz tiene traducción parcial al inglés.
Su propio texto dice que admite **18 motores** —doce en la nube y seis locales—, y eso es una declaración del
autor: aquí no se ha probado ninguno. Los motores en la nube implican mandar tu voz fuera; los locales,
descargar cientos de megas y depender de la potencia del teléfono.

### Cuándo no vale la pena

Si no escribes chino ni necesitas dictado, es una aplicación grande para usar una sola tecla. Y si lo que
quieres es privacidad, elige un motor local desde el principio y no configures ninguno en la nube.
<!-- GUIA:FIN -->
