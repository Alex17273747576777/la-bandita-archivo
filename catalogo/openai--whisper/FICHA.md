# whisper · openai

*Robust Speech Recognition via Large-Scale Weak Supervision*

**Racimo:** teclados-y-dictado · **Repositorio:** `openai/whisper` · **Estado:** lento · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> [[Blog]](https://openai.com/blog/whisper) [[Paper]](https://arxiv.org/abs/2212.04356) [[Model card]](https://github.com/openai/whisper/blob/main/model-card.md) [[Colab example]](https://colab.research.google.com/github/openai/whisper/blob/master/notebooks/LibriSpeech.ipynb)

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 31 de agosto de 2026 (hace 66 días)
- **Estrellas:** 112.000 · 13569 bifurcaciones · 181 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Python · creado el 16 de septiembre de 2022
- **Última entrega:** `v20250625` del 26 de junio de 2025 · 0 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- pip install -U openai-whisper
- Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:
- pip install git+https://github.com/openai/whisper.git
- pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/openai/whisper
- la última entrega: https://github.com/openai/whisper/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

El modelo de reconocimiento de voz que cambió el terreno: transcribe audio en decenas de idiomas, traduce al
inglés lo que oye en otro idioma y funciona razonablemente con ruido y acentos. Este repositorio trae el modelo
y una orden de terminal para usarlo.

### Cómo se usa

1. Se instala con `pip install -U openai-whisper`; la entrega medida es `v20250625`, del 26 de junio de 2025.
2. Se transcribe un archivo: `whisper audio.mp3 --model medium --language es`.
3. Con `--task translate` traduce al inglés; con `--output_format srt` saca subtítulos.
4. Para dictado en vivo hace falta otra pieza: esto trabaja sobre archivos o sobre una entrada de audio
   continua que hay que preparar.

### Lo que conviene saber antes

112.000 estrellas y licencia MIT: es la referencia de todo el racimo, y casi todos los demás programas lo usan
por debajo, en alguna de sus versiones optimizadas. Su último cambio es de **agosto de 2026** y su entrega de
junio de 2025: el proyecto va despacio porque el modelo ya está publicado y lo que evoluciona son las
reimplementaciones.

### Cuándo no vale la pena

Si tienes tarjeta gráfica, hay reimplementaciones de este mismo racimo que van mucho más rápido. Y si no
quieres tocar una terminal, usa una aplicación que lo lleve dentro.
<!-- GUIA:FIN -->
