#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_teclado_ia.py · las guías escritas a mano del racimo «teclados-con-ia» (4 recursos)."""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"
RACIMO = "teclados-con-ia"

GUIA = {}

GUIA["SvReenen/Deskdrop"] = """
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
"""

GUIA["dessalines/thumb-key"] = """
### Para qué sirve

Teclado para Android diseñado para escribir **con los dos pulgares y sin mirar**, con las letras colocadas por
frecuencia alrededor del centro y gestos de deslizamiento para todo lo demás: símbolos, mayúsculas, acentos,
teclas muertas y combinaciones.

Viene de la tradición de MessagEase, el teclado de los primeros teléfonos táctiles, y conserva su lógica:
gestos cortos, teclas grandes, nada de teclas diminutas en las esquinas.

### Cómo se usa

1. Se instala la APK de la entrega `5.1.20`, del 2 de noviembre de 2026.
2. Se activa en *Ajustes → Sistema → Idiomas → Teclados* y se elige como método de entrada.
3. Se elige distribución —hay varias— y se ajusta el tamaño de las teclas.
4. Hay que **aprenderla**: el propio proyecto incluye una guía de usuario y trucos para los primeros días.

### Lo que conviene saber antes

1.572 estrellas, AGPL-3.0, Kotlin, creado en marzo de 2023, con 341 bifurcaciones, 51 incidencias abiertas y
movimiento de ayer. Publica en F-Droid y permite verificar el certificado de firma antes de instalar, algo que
muy pocos hacen y que aquí está explicado.

El coste real es el aprendizaje: entre una y dos semanas escribiendo despacio antes de recuperar la velocidad
anterior. Quien no esté dispuesto a eso, lo abandonará al segundo día. El medidor marcó abandono declarado por
una mención en su texto; el repositorio tiene movimiento de hoy.

### Cuándo no vale la pena

Si escribes sobre todo en un idioma con muchas tildes y no quieres memorizar gestos, o si usas el teléfono
poco, el cambio no compensa. Este teclado premia a quien escribe mucho con los pulgares.
"""

GUIA["fcitx5-android/fcitx5-android"] = """
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
"""

GUIA["futo-org/android-keyboard"] = """
### Para qué sirve

Teclado de Android con el objetivo declarado de **quedarse sin conexión**: corrección, predicción y dictado de
voz en el propio teléfono, sin enviar lo que escribes ni lo que dices a ningún servidor. Es un derivado del
teclado de código abierto de Android, LatinIME, con cambios profundos.

El dictado es la parte que lo distingue: reconocimiento de voz local, que es justo lo que casi todos los
teclados resuelven mandando el audio fuera.

### Cómo se usa

1. Se descarga desde la web del proyecto; en este repositorio está el seguimiento de incidencias y un espejo
   del código.
2. Se instala y se activa como método de entrada.
3. Se descarga el paquete de idioma del dictado, que ocupa bastante y se ejecuta en local.
4. Se desactivan los permisos de red si se quiere comprobar que, en efecto, no los usa.

### Lo que conviene saber antes

3.440 estrellas, creado en mayo de 2024, con 298 bifurcaciones y **809 incidencias abiertas**: es la ficha del
racimo con más cola de trabajo. La licencia no la reconoce GitHub como estándar —aparece como `NOASSERTION`—,
así que conviene leer los términos en su propio repositorio antes de reutilizar nada.

El medidor marcó la bandera de espejo, y es correcta: el código se desarrolla en otro sitio y aquí solo se
publica una copia. Eso significa que la actividad de este repositorio no mide la del proyecto.

### Cuándo no vale la pena

Si dictas poco, el peso del paquete de voz no se justifica. Y si necesitas teclados en muchos idiomas con
corrección fina, la cobertura por idioma de un proyecto joven se queda corta.
"""


def main() -> int:
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    escritas = 0
    for repo, texto in GUIA.items():
        f = medido.get(repo)
        if not f or f.get("racimo") != RACIMO:
            print("  ! sin medir en el racimo:", repo)
            continue
        p = CATALOGO / repo.replace("/", "--").lower() / "FICHA.md"
        if not p.exists():
            print("  ! sin ficha:", repo)
            continue
        t = p.read_text(encoding="utf-8")
        if INICIO not in t or FIN not in t:
            print("  ! sin marcadores:", repo)
            continue
        nuevo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN),
                       INICIO + "\n" + texto.strip() + "\n" + FIN, t, flags=re.S)
        if nuevo != t:
            p.write_text(nuevo, encoding="utf-8")
            escritas += 1
    print(f"guías escritas: {escritas} de {len(GUIA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
