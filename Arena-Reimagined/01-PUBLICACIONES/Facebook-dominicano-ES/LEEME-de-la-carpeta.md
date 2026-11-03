# LEEME de la carpeta · Facebook dominicano-ES

*El estado de la carpeta, dicho en una pantalla. Actualizado el 3 de noviembre de 2026.*

## Qué hay aquí y qué no

Aquí, en la raíz de la carpeta, vive **solo el ciclo vivo**: las piezas de la serie que se está publicando ahora, de la 01 a la 14. Nada más. Todo lo anterior —trescientos y pico de archivos de septiembre y octubre— está en `_ARCHIVO-HISTORICO/`, ordenado por mes, y no se borra porque es la memoria firmada de la casa.

Antes de este ordenamiento la carpeta tenía ciento diecinueve archivos al mismo nivel y **números repetidos**: dos piezas 05, una de septiembre y una de noviembre. Eso no era un problema de nombres, era un problema de lectura: quien abría la carpeta no sabía qué era el presente y qué era el pasado. Ahora lo sabe en un segundo.

## La regla del nombre

Toda pieza del ciclo vivo se llama igual, y el nombre contiene todo lo que hace falta para no confundirse:

```
NN-Titulo-en-espanol-sin-acentos-Facebook-La-Bandita-AAAA-MM-DD-dominicano-ES.md
```

El número es el del ciclo (01–14), la fecha es la del corte de medición de la pieza, y el sufijo `dominicano-ES` dice el idioma y el canal. Una pieza publicada no se renombra ni se retoca: si hay que rehacerla, se rehace entera y la anterior pasa a `_ARCHIVO-HISTORICO/_reemplazadas/` con su fecha.

## El ciclo vivo, pieza por pieza

| # | Pieza | Corte | Caracteres | Estado |
|---|---|---|---|---|
| 01 | El turno de los que nacieron este trimestre | 2026-11-03 | 44.994 | Publicada y en banda |
| 02 | La música que no se cae | 2026-11-02 | 44.934 | Publicada y en banda |
| 03 | La caja fuerte del bolsillo | 2026-11-02 | 44.831 | Publicada y en banda |
| 04 | La lista del permiso | 2026-11-03 | 44.151 | Publicada y en banda |
| 05 | La guía maestra | 2026-11-03 | 40.253 | Publicada y en banda |
| 06 | El taller: lo que se puede leer, se puede arreglar | — | — | Siguiente |
| 07 | La pantalla grande y la casa que no hace ruido | — | — | En cola |
| 08 | La red: seis caminos, seis precios | — | — | En cola |
| 09 | Archivos, copias y nubes propias | — | — | En cola |
| 10 | La privacidad que se puede comprobar | — | — | En cola |
| 11 | Cuando algo se rompe: los cinco sitios y el parte | — | — | En cola |
| 12 | El oficio: cómo comprobarme sin creerme | — | — | En cola |
| 13 | Los setenta, otra vez: la remisión de diciembre | — | — | Programa­da |
| 14 | La lista final: qué instalar primero según tu caso | — | — | Programada |

Banda de longitud del canal: **40.000 a 45.000 caracteres** por pieza, declarada en `docs/bandas.json`. Una pieza fuera de banda no se publica, y la cifra del registro tiene que coincidir con la del archivo: si alguien toca el texto sin actualizar el registro, la compuerta lo dice.

## De dónde sale cada pieza

Las doce primeras siguen los doce capítulos de la guía maestra, que vive en `guia-maestra/` en la raíz del repositorio. Cada pieza del canal toma un capítulo, lo cuenta para el muro y abre las fichas que ese capítulo mide. Las dos últimas no son capítulos: la 13 es la remisión obligatoria de diciembre —lo que se midió el 3 de noviembre se vuelve a medir el 3 de diciembre, y se publica qué se movió— y la 14 es la puerta de entrada para quien llega nuevo y no sabe por dónde empezar.

## Dónde está lo demás

```
_ARCHIVO-HISTORICO/
├── 2026-09/   el arranque de la casa, septiembre
├── 2026-10/   la oleada larga de octubre, del muro 00 al 131
├── _PRE-2026-10-31/   lo que quedó antes del reinicio del ciclo
├── _reemplazadas/     las piezas retiradas, con la fecha en que se retiraron
└── sin-fecha/         lo que no declara dateline y no se puede fechar
```

El archivo histórico conserva todo tal como se publicó, incluidos sus fallos. No se corrige hacia atrás: se corrige hacia adelante, y la corrección se anota en la pieza nueva.

## Cómo se comprueba lo que dice este archivo

Tres métodos distintos, y los tres tienen que coincidir. Están corridos y anotados en `docs/ACTA-ORDEN-Y-VERIFICACION-2026-11-03.md`.

1. **Árbol y contenido.** Se cuenta lo que hay y se saca la huella de cada pieza con suma de verificación. El árbol tiene que decir lo que dice esta tabla.
2. **La fuente remota.** Se le pregunta a la plataforma, sin usar el clon, qué archivos hay en esta carpeta y de qué tamaño. Si el clon y la plataforma no coinciden, hay algo sin subir.
3. **Coherencia interna del texto.** Para cada pieza: la fecha del nombre, la fecha del dateline, el tamaño declarado en el registro y la huella anotada en su envío tienen que ser el mismo archivo. Una sola discrepancia y la pieza no se cuenta como publicada.

## Lo que no se hace en esta carpeta

No se aloja ni un paquete ajeno. No se escribe aquí nada que no sea una pieza, un LEEME o el archivo histórico. No se publica una pieza sin pasar las dos compuertas —la de forma y la de novedad— y sin que la vara diga «fallos: NINGUNO».

*La Bandita informa a partir de fuentes fechadas.*
