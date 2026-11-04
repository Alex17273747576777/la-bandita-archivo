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
| 01 | La huella o el silencio (**escrita de nuevo el 4-nov, 11:58**) | 2026-11-04 | 40.530 | Publicada y en banda · doce programas y su huella, tres fuera, censo 6.842 · las versiones anteriores, en `_ARCHIVO-HISTORICO/` |
| 02 | La música que no se cae: seis que firman y seis grandes que no (**escrita de nuevo el 4-nov, 12:35**) | 2026-11-04 | 41.946 | Publicada y en banda · 21 repos medidos, 6 con huella · censo de 121 · la versión anterior, en `_ARCHIVO-HISTORICO/` |
| 03 | La caja fuerte del bolsillo: una de catorce da la huella y dos se reservan los derechos (**escrita de nuevo el 4-nov, 12:44**) | 2026-11-04 | 40.396 | Publicada y en banda · 16 repos medidos, 1 con huella (15 adjuntos) · censo de 11 · la versión anterior, en `_ARCHIVO-HISTORICO/` |
| 04 | La lista del permiso (**rehecha**) | 2026-11-04 | 44.513 | Escrita de nuevo el 4-nov, 13:16 · 26 repos medidos, 6 con huella · censo de 454 · la anterior, en `_ARCHIVO-HISTORICO/_reemplazadas-2026-11-04/` |
| 05 | La guía maestra (**rehecha**) | 2026-11-04 | 44.429 | Escrita de nuevo el 4-nov, 17:56 · 70 fichas remedidas, 22 con huella · capítulo del permiso: 0 de 6 · la anterior, en `_ARCHIVO-HISTORICO/_reemplazadas-2026-11-04/` |
| 06 | El taller: un gestor de parches y un módulo que perdió su casa | 2026-11-03 | 44.703 | Publicada y en banda |
| 07 | La pantalla grande y la casa que no hace ruido | — | — | Siguiente |
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

## Cambio de tema en la pieza 06, declarado

El programa original de la serie daba a la pieza 06 el título «El taller: lo que se puede leer, se puede arreglar», sobre el derecho a reparar. El dueño pidió el 4 de noviembre una publicación específica del gestor de parches Universal Patch Manager, y ese programa **es** el taller: la herramienta con la que se abre un paquete ajeno y se vuelve a cerrar. Se publicó como 06 con ese tema y el título se ajustó para que diga lo que la pieza hace. El tema de reparabilidad no se pierde: pasa a la pieza 11, «Cuando algo se rompe», donde ya estaba previsto el título de los cinco sitios y el parte de avería.

## La regla que manda desde el 3 de noviembre: lo nuevo primero

El dueño fijó una regla editorial que ordena la serie entera: **enfocarse en los recursos más nuevos,
actualizados, recién lanzados y desconocidos**. No es una preferencia de estilo, es un cambio de método, y
por eso la casa construyó `tools/novedad.py`: lee la evidencia sellada de las 6.838 fichas, saca la fecha
de nacimiento de cada repositorio y clasifica en nacido, joven, desconocido, recién, dormido y muerto.
Ordena por juventud × actividad, nunca por estrellas.

La pieza 01 rehecha es la primera que se escribió con esa regla: doce programas nacidos en octubre de 2026,
ninguno por encima de ★132, y dos rechazos razonados. Las piezas 02 a 06 se rehacen en las tandas
siguientes, y de la 07 en adelante el mapa de 125 ya está ordenado por la misma regla.
