# LEEME de la carpeta · WhatsApp dominicano-ES

*El estado de la carpeta, dicho en una pantalla. Actualizado el 3 de noviembre de 2026.*

## Qué hay aquí y qué no

En la raíz de esta carpeta vive **solo el ciclo vivo**: las piezas de la serie que se está publicando ahora, de la 01 a la 14. Todo lo anterior está en `_ARCHIVO-HISTORICO/`, ordenado por mes, y no se borra: es la memoria firmada de la casa y sirve para comparar.

La carpeta tenía ciento trece archivos al mismo nivel y **dos pares de números repetidos**: dos piezas 04 y dos piezas 05, unas de octubre y otras de noviembre. Quien abría la carpeta no podía saber cuál era la vigente. Ahora la raíz tiene cinco archivos y el resto está fechado donde corresponde.

## La regla del nombre

```
NN-Titulo-en-espanol-sin-acentos-WhatsApp-La-Bandita-AAAA-MM-DD-dominicano-ES.md
```

El número es el del ciclo (01–14), la fecha es la del corte de medición y el sufijo dice canal e idioma. Una pieza publicada no se renombra ni se retoca: si hay que rehacerla, se rehace entera y la anterior pasa a `_ARCHIVO-HISTORICO/_reemplazadas/`.

## El ciclo vivo, pieza por pieza

| # | Pieza | Corte | Caracteres | Estado |
|---|---|---|---|---|
| 01 | La puerta y el recibo | 2026-11-02 | 63.068 | Publicada y en banda |
| 02 | La música que no se cae: el inventario que nadie hace | 2026-11-02 | 63.006 | Publicada y en banda |
| 03 | La caja del bolsillo: la libreta que se moja | 2026-11-02 | 63.098 | Publicada y en banda |
| 04 | Los cinco herederos de Shizuku | 2026-11-03 | 63.096 | Publicada y en banda |
| 05 | La guía maestra, contada despacio | 2026-11-03 | 63.096 | Publicada y en banda |
| 06 | El taller en el bolsillo | — | — | Base escrita: la de Facebook del 4-nov; falta la versión de este canal |
| 07 | El televisor limpio y la casa que obedece | — | — | En cola |
| 08 | La red, contada despacio | — | — | En cola |
| 09 | Las copias y las nubes propias | — | — | En cola |
| 10 | La privacidad comprobable | — | — | En cola |
| 11 | El parte de avería | — | — | En cola |
| 12 | El oficio, o cómo no tenerme que creer | — | — | En cola |
| 13 | La remisión de diciembre | — | — | Programada |
| 14 | La lista del día uno | — | — | Programada |

Banda de longitud del canal: **63.000 a 63.099 caracteres** por pieza, declarada en `docs/bandas.json`. El margen es estrecho a propósito: el dueño pidió 63.000 como mínimo y como máximo, y los 99 de tolerancia existen para no cortar una coma por obligación. Una pieza que no cae ahí no se publica.

## La relación con Facebook

Cada pieza del canal de WhatsApp sale **después** de su gemela de Facebook y no es la misma: son dos textos distintos sobre la misma medición. La regla que lo exige es la compuerta M23, que rechaza los párrafos compartidos entre piezas de la casa. Por eso una pieza de WhatsApp se escribe desde cero y no se recorta de la de Facebook.

## Dónde está lo demás

```
_ARCHIVO-HISTORICO/
├── 2026-10/   la serie larga de octubre, del canon 00 al 34 y las fotos del censo
├── _PRE-2026-10-31/   lo que quedó antes del reinicio del ciclo
└── sin-fecha/         lo que no declara dateline y no se puede fechar
```

## Cómo se comprueba lo que dice este archivo

Los tres métodos del acta `docs/ACTA-ORDEN-Y-VERIFICACION-2026-11-03.md`, y los tres tienen que coincidir:

1. **Árbol y contenido.** Contar lo que hay y sellar cada pieza con su suma de verificación.
2. **La fuente remota.** Preguntarle a la plataforma, sin el clon de por medio, qué archivos hay y de qué tamaño.
3. **Coherencia interna del texto.** Fecha del nombre, fecha del dateline, tamaño declarado en el registro y huella anotada en el envío tienen que ser del mismo archivo.

## Lo que no se hace en esta carpeta

No se aloja ni un paquete ajeno. No se publica una pieza sin las dos compuertas en verde y sin la vara en «fallos: NINGUNO». Y no se manda al canal un envío que no haya pasado `--verificar` sin perder una sola línea del cuerpo.

*La Bandita informa a partir de fuentes fechadas.*
