# LEEME de la carpeta · Facebook dominicano-ES

*El estado de la carpeta, dicho en una pantalla. Actualizado el 8 de noviembre de 2026.*

## Qué hay aquí y qué no

En la raíz de esta carpeta vive **solo el ciclo vivo**: las cuarenta piezas de la serie que se está publicando ahora, de la 01 a la 40, cada una con su cuerpo y su comentario fijado. Nada más. Todo lo anterior —trescientos y pico de archivos de septiembre y octubre— está en `_ARCHIVO-HISTORICO/`, ordenado por mes, y no se borra porque es la memoria firmada de la casa.

## La regla del nombre

Toda pieza del ciclo vivo se llama igual, y el nombre contiene lo que hace falta para no confundirse:

```
NN-Titulo-en-espanol-sin-acentos-...-Facebook-La-Bandita-AAAA-MM-DD-dominicano-ES.md
NN-Comentario-fijado-facebook-La-Bandita-AAAA-MM-DD-dominicano-ES.md
```

El número es el del ciclo (01–40), la fecha es la del corte de medición de la pieza, y el sufijo `dominicano-ES` dice el idioma y el canal. Una pieza publicada no se renombra ni se retoca: si hay que rehacerla, se rehace entera y la anterior pasa a `_reemplazadas-AAAA-MM-DD/` con su fecha.

**Cada número tiene exactamente dos archivos**: el cuerpo y el comentario fijado. Hay una comprobación que lo verifica y que puede ejecutarse en cualquier momento —ver «Cómo se comprueba lo que dice este archivo», al final—.

## El ciclo vivo, pieza por pieza

**Las cuarenta piezas están medidas o declaradas.** Las 01 a 22 y la 31 se midieron contra la API pública de GitHub, cada una con su hora y su corte. Las **24 a 29, 32, 33, 34 y 40** se reescribieron enteras el 8 de noviembre con medición propia nueva —cada una tiene su `docs/MEDICION-NN-2026-11-08.json`, y su comentario fijado se genera desde ese JSON—. Las **35, 37, 38 y 39** son textos personales (la Ballenita, la carta a la manada, Kung Fu Panda, Canserbero): no son piezas de medición y el LEEME no les exige lo que no son. La **36** también se midió el 8 de noviembre: el cierre de un sitio no se mide con la API de GitHub, pero sí con el registro del dominio (RDAP), el DNS y una cabecera HTTPS — y eso es lo que hace, ocho dominios sondeados.

| # | Pieza | Cuerpo | Fijado | Estado |
|---|---|---|---|---|
| 01 | La huella o el silencio | 16.606 | 1.712 | Medida · 12 programas, 6 con huella |
| 02 | La música que no se cae | 18.114 | 1.711 | Medida · 21 repos, 6 con huella |
| 03 | La caja fuerte del bolsillo | 11.411 | 1.714 | Medida · 16 repos, 1 con huella |
| 04 | La lista del permiso | 13.405 | 1.728 | Medida · 26 repos, 6 con huella |
| 05 | La guía maestra | 46.761 | 3.331 | Medida · 70 fichas, 22 con huella |
| 06 | El taller de los parches | 12.170 | 1.682 | Medida · 17 repos, 5 con huella (55 de 190 archivos) |
| 07 | La pantalla grande | 11.140 | 1.699 | Medida · 17 repos, 4 con huella · gigantes re-verificados el 8-nov |
| 08 | La red: seis caminos | 13.583 | 1.695 | Medida · 20 repos, 5 con huella |
| 09 | Archivos, copias y nubes | 13.726 | 1.730 | Medida · 17 repos, 4 con huella |
| 10 | Las tiendas | 12.792 | 1.684 | Medida · 56 repos, 1 firma |
| 11 | Las aplicaciones que leen | 11.078 | 1.681 | Medida · 51 apps, 116 archivos firmados |
| 12 | El kit de reemplazo | 11.364 | 1.710 | Medida · 59 recursos, 501 de 3.022 |
| 13 | El audio que faltaba | 12.281 | 1.695 | Medida · 54 proyectos, 409 de 3.599 |
| 14 | Spotify sin Spotify | 12.075 | 1.702 | Medida · 38 clientes, 495 de 2.473 |
| 15 | Descargar es un acto técnico | 12.346 | 1.723 | Medida · 31 programas |
| 16 | El torrent que no se rinde | 9.072 | 1.662 | Medida · 22 piezas |
| 17 | El teclado que escribe por ti | 9.467 | 1.673 | Medida · 34 teclados |
| 18 | La radio y el directo | 11.337 | 1.664 | Medida · 32 piezas |
| 19 | La tienda que le sirve a tu app | 12.244 | 1.713 | Medida · 15 repos |
| 20 | El teclado que obedece | 11.403 | 1.682 | Medida · 11 teclados |
| 21 | La variante que cambió | 9.844 | 1.676 | Medida · OmniShizuku |
| 22 | El módulo que no necesita root | 10.405 | 1.661 | Medida · AxManager |
| 23 | Keiyoushi, catálogo de extensiones | 11.018 | 1.666 | Una ficha medida |
| 24 | Repositorios de extensiones de anime | 9.881 | 1.669 | **Medida el 8-nov** · 5 vivos, 173 archivos, 0 huellas, un abuelo de 812 días |
| 25 | OCR de bolsillo | 11.137 | 1.689 | **Medida el 8-nov** · 7 programas, 334 archivos, 1 suma (episteme) |
| 26 | Usagi y su familia | 10.915 | 1.706 | **Medida el 8-nov** · 6 vivos, 727 archivos, 0 huellas, el original 370 días parado |
| 27 | DropSauce y su tema | 8.165 | 1.663 | **Medida el 8-nov** · 4 vivos, 262 archivos, 3 sumas (las pone el más pequeño) |
| 28 | Mangayomi y sus extensiones | 10.096 | 1.665 | **Medida el 8-nov** · 5 vivos, 3.788 archivos, 0 huellas: el peor del día |
| 29 | LNReader y sus plugins | 10.281 | 1.662 | **Medida el 8-nov** · 2 vivos, 69 archivos, 5 sumas, 963 días sin etiqueta |
| 30 | Cloudstream MegaRepo | 45.011 | 1.415 | Una ficha medida |
| 31 | El peso no es el problema | 50.628 | 3.351 | Medida de nuevo el 8-nov |
| 32 | Tu Manga Online, sin lista de dominios | 11.129 | 2.090 | **Medida el 8-nov** · 9 lectores, 4.182 archivos, 0 huellas, uno que devuelve 404 |
| 33 | Apoyo a desarrolladores | 11.244 | 2.042 | **Medida el 8-nov** · 9 proyectos, 977 archivos, 0 huellas, uno de 0 estrellas |
| 34 | Biblioteca de Kototoro y v2.4 | 12.781 | 2.026 | **Medida el 8-nov** · 4 repos, 1.385 archivos, **102 sumas**: récord del día |
| 35 | La Ballenita vuelve al mar | 6.206 | 1.337 | Corta · personal |
| 36 | Tu Manga Online, medido | 12.936 | 2.572 | **Medida el 8-nov** · 8 dominios sondeados: 3 registrados, 0 resolviendo |
| 37 | Carta a la manada azul | 10.254 | 1.503 | Corta · personal |
| 38 | Kung Fu Panda | 6.231 | 1.249 | Corta · personal |
| 39 | Canserbero | 22.155 | 1.512 | Corta · personal |
| 40 | La lección del hash SHA-256 | 12.678 | 2.363 | **Reescrita entera el 8-nov** · el método probado en esta máquina |

## La medición del 8 de noviembre

Las nueve piezas que estaban declaradas «sin medición propia» se midieron de verdad, y las cifras quedaron guardadas:

```
docs/MEDICION-24-2026-11-08.json   …   docs/MEDICION-34-2026-11-08.json
python3 tools/medir_piezas_24_34.py --todas     # vuelve a medir las nueve
```

Cada JSON guarda, por repositorio: estrellas, forks, licencia, archivado, fecha de nacimiento, último empujón, última entrega con etiqueta y su fecha, número de entregas, adjuntos totales, **cuántos adjuntos llevan suma de comprobación** y descargas acumuladas. Los totales de cada pieza se cuentan en el propio archivo, y el comentario fijado se genera desde ahí: **no hay una cifra escrita a mano en los nueve fijados**.

Lo que salió al medir, en una línea por tema: 0 huellas de 173 en las extensiones de anime; 1 de 334 en OCR; 0 de 727 en lectores de manga; **3 de 262** en DropSauce, del más pequeño; 0 de 3.788 en Mangayomi, el peor del día; 5 de 69 en LNReader; 0 de 4.182 en Tu Manga Online; 0 de 977 en apoyo a desarrolladores; y **102 de 1.385** en Kototoro, el récord.

Y tres cosas que la pieza vieja no podía decir porque no había medido: que `tachiyomiorg/tachiyomi` devuelve **404**, que el **fork de 294 estrellas se mueve y su original de 8.958 lleva 370 días parado**, y que **Kototoro publicó la v2.4.1 el mismo día de la medición**.

---

## La banda de longitud, corregida

Hasta el 8 de noviembre esta casa declaraba un «mínimo obligatorio de 45.000 caracteres para publicaciones de Facebook». **Ese mínimo no existe**: era una vara interna que se convirtió en relleno, y produjo nueve cuerpos hechos con un generador que repetía cinco secciones con el título de cada pieza metido a la fuerza en medio. Se detectó el 8 de noviembre, se retiró el relleno y se corrigió la doctrina:

* La banda de la casa es **6.000 a 45.000 caracteres** para el cuerpo y **900 a 4.000** para el comentario fijado, declarada en `docs/bandas.json`.
* **Ninguna pieza tiene que acercarse al máximo.** La 40 se publica con 13.532 caracteres y es la más corta de la serie a propósito.
* Si no hay dato, se escribe «aquí no hay». No se rellena.

## De dónde sale cada pieza

Las doce primeras siguen los doce capítulos de la guía maestra, que vive en `guia-maestra/` en la raíz del repositorio. De la 13 en adelante la serie mide temas por demanda del público —audio, reemplazos, tiendas de extensiones, lectores— y cada pieza parte de una «semilla»: la deuda que dejó la anterior.

## Dónde está lo demás

```
_ARCHIVO-HISTORICO/
├── 2026-09/   el arranque de la casa, septiembre
├── 2026-10/   la oleada larga de octubre, del muro 00 al 131
├── _PRE-2026-10-31/   lo que quedó antes del reinicio del ciclo
├── _reemplazadas/     las piezas retiradas, con la fecha en que se retiraron
└── sin-fecha/         lo que no declara dateline y no se puede fechar

_reemplazadas-2026-11-04/   piezas rehechas esa fecha
_reemplazadas-2026-11-08/   las ocho versiones de relleno de las piezas 32 a 39,
                            y las piezas cortas que sustituyó la versión nueva
```

El archivo histórico conserva todo tal como se publicó, incluidos sus fallos. No se corrige hacia atrás: se corrige hacia adelante, y la corrección se anota en la pieza nueva.

## Cómo se comprueba lo que dice este archivo

```
python3 tools/leeme_carpeta.py            # cuadra el LEEME contra los archivos
python3 tools/leeme_carpeta.py --arreglar # reescribe la tabla con los conteos reales
```

Comprueba tres cosas: que cada número 01–40 tenga **un cuerpo y un comentario fijado**, que los caracteres de la tabla coincidan con los del archivo, y que no quede en la raíz ninguna pieza sin número. Si algo no cuadra, lo dice y devuelve código de salida distinto de cero.
