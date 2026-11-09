# Cierre de las publicaciones · La Bandita

*8 de noviembre de 2026 · `la-bandita-archivo` · `main` = `599db05e` · sincronizado con el remoto*

## Lo que pediste, y cómo quedó

| Lo que pediste | Estado |
|---|---|
| Localizar las piezas 31 a 40 incompletas | Hecho: el censo encontró **10 comentarios fijados que faltaban** (06–14 y 40) y **8 piezas con dos versiones** (32–39) |
| Completar el comentario fijado y el cuerpo | **Los 10 fijados escritos** con las cifras ya medidas de cada cuerpo. **La 40 reescrita entera** (su cuerpo era relleno de plantilla) |
| Organizar todo el repositorio | Una sola versión por número · LEEME reescrito con 40 filas medidas · bandas, README y CHANGELOG al día |
| Limpiar local, commit y push | 5 commits pusheados a `main`, árbol limpio, nada solo en local |

## Lo que encontré debajo (y no estaba en el encargo)

Tres cosas que estaban publicadas y no eran verdad:

1. **El «mínimo obligatorio de 45.000 caracteres para Facebook» no existe.** Era una vara interna que se volvió relleno: `generar_piezas.py` fabricó nueve cuerpos repitiendo cinco secciones con el título de cada pieza metido a la fuerza en medio. Se retiraron a `_reemplazadas-2026-11-08/` y quedó viva la versión original de cada número.
2. **Voz rota publicada a la vista** en la pieza 06: «…son cinco de diecisiete, no cuatro: me corrijo, son cinco. Espera, contemos: …». Retirada.
3. **Una afirmación falsa en la 07**: decía que los cinco gigantes «no publican huella». Lo medí otra vez hoy contra la API de GitHub: tres no publican adjuntos, SmartTube publica cuatro y ninguno de los cinco adjunta suma. La frase ahora dice eso, con fecha.

Y ocho piezas cortas (32–39) declaraban un número de pieza que no era el suyo: la 37 decía «pieza 12», la 39 «pieza 14», la 35 «pieza 10». Renumeradas las cuarenta, 0 descuadres.

## Medido, no declarado

```
python3 tools/leeme_carpeta.py   → piezas comprobadas: 40 · fallos: 0
python3 tools/vara.py            → fallos: NINGUNO  (17 compuertas, G0 a G17)
python3 tools/atestar.py         → 14.481 archivos sellados, huella 807973f8e354ccff…
sha256sum -c (las órdenes de la pieza 40) → prueba.txt: OK
```

La vara de la casa daba **8 fallos** antes de empezar. Lo que había debajo: un LEEME contado como pieza, la pieza 31 sin firma, el sello del día sin generar y siete piezas sin banda declarada. Nada de eso se tapó: se arregló y se anotó en el CHANGELOG (entrada 2.1.0).

## Lo que no se hizo, y por qué

**Nueve piezas cortas siguen sin medición propia** —24 a 29, 32, 33, 34 y 36—. Su tema no se ha medido contra la API: no hay un JSON de medición detrás. Podía haber rellenado 45.000 caracteres con texto plausible, y es exactamente lo que se acaba de retirar del repositorio. Quedan declaradas una por una en el `LEEME-de-la-carpeta.md` con la etiqueta *sin medición propia*, que es lo que un archivo honesto hace.

**La 35, 37, 38 y 39 son textos personales** (la Ballenita, la carta a la manada, Kung Fu Panda, Canserbero). No son piezas de medición: no se les inventó banda de contenido, solo se les corrigió el número de pieza.

## Si quieres seguir por ahí

Lo siguiente con más valor sería **medir de verdad los temas de las nueve cortas** (con la API pública, igual que las otras 31) y reescribirlas con sus cifras. Cada una es una medición y un texto. Dime si tiro por ahí.
