# Las nueve piezas medidas · cierre del 8 de noviembre de 2026

`la-bandita-archivo` · `main` = `7c9ca77e` · sincronizado con el remoto

## Lo que se hizo

Las nueve piezas que estaban declaradas «sin medición propia» —24, 25, 26, 27, 28, 29, 32, 33 y 34— se midieron **de verdad** contra la API pública de GitHub y se reescribieron con sus cifras. No se rellenó nada.

- **Herramienta nueva:** `tools/medir_piezas_24_34.py`. Escribe un JSON por pieza en `docs/MEDICION-NN-2026-11-08.json` y se puede volver a correr con `--todas`.
- **Nueve cuerpos** de 9.984 a 13.856 caracteres, todos dentro de banda.
- **Nueve comentarios fijados generados desde el JSON:** ninguna cifra escrita a mano.
- **Las nueve piezas viejas** se retiraron con `git mv` a `_reemplazadas-2026-11-08/`.

**Salida medida:** 9 JSON · 34 repositorios distintos · **11.897 archivos** contados · **111 con suma**, y 102 de esos 111 son de un solo proyecto.

## Lo que salió al medir

| # | Tema | Archivos | Sumas | El dato que importa |
|---|---|---|---|---|
| 24 | Extensiones de anime | 173 | **0** | El repositorio de extensiones de Aniyomi lleva **812 días** sin un empujón |
| 25 | OCR | 334 | **1** | La única suma la pone episteme (1.340 ★), no PaddleOCR ni Tesseract |
| 26 | Usagi / lectores de manga | 727 | **0** | El fork de **294 ★** se mueve; su original, de **8.958 ★**, lleva **370 días** parado |
| 27 | DropSauce | 262 | **3** | Las tres sumas las pone el proyecto de **235 ★**; Mihon publica 152 archivos sin ninguna |
| 28 | Mangayomi | 3.788 | **0** | El peor número de la serie: 3.160 archivos de keiyoushi, cero huellas, sin licencia declarada |
| 29 | LNReader | 69 | **5** | Cinco sumas en la aplicación; los plugins no publican etiqueta desde hace **963 días** |
| 32 | Tu Manga Online | 4.182 | **0** | Reescribida **sin lista de dominios**, con el motivo explicado |
| 33 | Apoyo a desarrolladores | 977 | **0** | 9 proyectos auditados: 8 se mueven este mes, uno lleva 99 días parado, uno tiene **0 ★** |
| 34 | Biblioteca de Kototoro | 1.385 | **102** | Récord del día — y la **v2.4.1 salió hoy**, así que la pieza vieja (v2.3) nació desactualizada |

Y un hallazgo transversal: **`tachiyomiorg/tachiyomi` devuelve 404**. El lector del que desciende casi todo el ecosistema ya no existe en GitHub.

## Medido, no declarado

```
tools/leeme_carpeta.py   → 40 piezas comprobadas · fallos: 0
tools/vara.py            → fallos: NINGUNO  (G10: 89 piezas dentro de su banda)
tools/atestar.py         → 14.599 archivos sellados
carpeta                  → 40 cuerpos + 40 comentarios fijados
```

De paso corregí un fallo mío en el medidor: `dias_push = 0` se interpretaba como «desconocido», así que quien había empujado código **hoy** no contaba como actividad de la semana. Lo detecté comparando la prosa con los totales y regeneré las nueve mediciones.

## Lo que sigue sin hacerse, y se declara

- **La pieza 36** sigue corta y sin medición propia: cuenta el cierre de un sitio y eso no se mide con la API de repositorios.
- **Ninguna de las nueve se probó ejecutando la aplicación.** Lo que se midió son repositorios —fechas, archivos, licencias, huellas—, no el comportamiento de los programas en un teléfono. No hay dispositivo ni `/dev/kvm` en este entorno, así que ninguna pieza puede decir «probado en dispositivo».
- **Los temas con 0 sumas no mejoran porque se midan.** La pieza los describe; sigue en pie el trabajo de pedir la huella a los autores con la plantilla de las piezas 01 a 22.
