# POLÍTICA DE DUPLICADOS · medida, no borrada

La duplicación es el mayor pasivo técnico del archivo y el más fácil de detener: basta con no crear
el siguiente. Esta política no borra nada — esa decisión es del dueño — pero deja la cifra a la vista
y fija la regla para lo que viene.

## Lo que midió `tools/duplicados.py` (31 de octubre de 2026)

| Medida | Valor |
|---|---|
| Archivos censados | 2.333 |
| Grupos de archivos idénticos | 277 |
| Copias sobrantes | 441 |
| Peso repetido | 3,2 MB |
| Piezas con varias fechas para el mismo número y plataforma | 163 |

Un archivo idéntico no es un daño; un archivo idéntico **que nadie sabe que existe** sí lo es:
cuando llega una corrección, se aplica en uno y el otro queda mintiendo con cara de vigente.
Ese es el riesgo que esta política ataca.

## Reglas

1. **Una pieza, una fuente.** Toda pieza nueva entra una sola vez. Las variantes de plataforma se
   generan desde la fuente; no se escriben a mano dos veces.
2. **Ningún archivo duplicado sin declaración.** Si por historia hay que conservar una copia, vive en
   `_archivo-*/` y su nombre lo dice. Fuera de esas carpetas, idéntico = error.
3. **La fecha manda.** Entre dos piezas del mismo número y plataforma, la de fecha más reciente es la
   vigente; la anterior se archiva, no se deja suelta al lado.
4. **Borrar es del dueño.** Ni la vara ni los medidores borran piezas publicadas. Se proponen y se
   espera la orden, por escrito.
5. **El medidor corre siempre.** `tools/duplicados.py` entra al circuito de la jornada; la cifra
   puede bajar, pero no puede crecer sin que alguien lo haya decidido.

## Lo que falta y no se hace solo

- Decidir qué copias históricas se conservan y cuáles se retiran (163 piezas con varias fechas).
- Decidir si el corte del 15-sep se mantiene como archivo público o se pliega.
- Decidir si las versiones en portugués, francés e inglés siguen vivas como línea editorial.

Ninguna de esas tres es una decisión técnica. Por eso no la tomé.
