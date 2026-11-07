# ACTA · orden del repositorio y verificación triple

*3 de noviembre de 2026 · La Bandita · commit `9606203`*

## 1 · El problema, tal como lo vio el dueño

«Solo hay una subida reciente y las otras no, no has actualizado el README y tampoco has ordenado el repositorio, que es un caos total.»

La primera parte de la frase era una lectura de la pantalla de GitHub y resultó ser un síntoma, no un error: las piezas 01 a 04 estaban publicadas desde horas antes y su fecha de último cambio era la de su publicación. La segunda parte era verdad y este acta la corrige.

Lo que había de verdad, medido antes de tocar nada:

| Carpeta | Archivos en la raíz | Series mezcladas | Números repetidos |
|---|---|---|---|
| `Facebook-dominicano-ES/` | 119 | tres (sep, oct, nov) | **dos piezas 05** |
| `WhatsApp-dominicano-ES/` | 113 | cuatro (oct, oct-31, nov-02, nov-03) | **dos piezas 04 y dos piezas 05** |

Los repetidos no eran cosméticos: la pieza 05 de septiembre era un texto de 496 caracteres y la de noviembre uno de 40.253. Dos archivos con el mismo número y el mismo nombre de canal, en la misma carpeta, a un clic de distancia.

## 2 · Lo que se hizo

- **225 archivos movidos** con `git mv` a `_ARCHIVO-HISTORICO/<mes>/` dentro de cada canal: 135 en Facebook (septiembre, octubre, reemplazadas y las que no declaran fecha) y 112 en WhatsApp (octubre, pre-reinicio y sin fecha). La historia de cada archivo se conserva porque se movió, no se copió.
- **Las dos raíces quedan con cinco piezas vivas y su LEEME**, nada más.
- **Los envíos de las piezas archivadas** pasan a `docs/envios/_historico/<canal>/` (114 y 108) y se regeneran los diez vivos: `5 · fallos: 0` en cada canal.
- **Mapa único en la raíz**: `MAPA-DEL-ARCHIVO.md`, con la traducción de las rutas anteriores.
- **README** con el estado del día arriba y **`LEEME-ESTRUCTURA.md` marcado como historia**, para que nadie lea el mapa de octubre como si fuera el de hoy.
- **LEEME en cada canal** con la tabla pieza por pieza, la banda, la fecha de corte y el plan 01–14 con sus títulos.

## 3 · La verificación triple, con métodos distintos

El dueño pidió comprobar al principio y al final, al menos tres veces y con métodos que no sean el mismo repetido. Estos tres no comparten fuente: el primero lee el árbol de git, el segundo pregunta a la plataforma sin usar el clon, el tercero no mira archivos sino la coherencia del contenido consigo mismo.

### Método A · árbol y huella (git, local)

`git ls-tree -r --long HEAD` sobre las dos carpetas, separando lo vivo del archivo, y `sha256` de cada archivo vivo.

- Facebook: **5 piezas + 1 LEEME** en la raíz, **135 archivos** en el archivo histórico.
- WhatsApp: **5 piezas + 1 LEEME** en la raíz, **112 archivos** en el archivo histórico.

### Método B · la fuente remota (API, sin clon)

Consulta a `contents` de la plataforma sobre el commit `9606203`, que devuelve nombre, tamaño y huella de cada archivo **tal como está publicado**.

Resultado: **los doce archivos de las dos raíces coinciden byte a byte con el árbol local**, y la única entrada que no es un `.md` en cada raíz es la carpeta del archivo histórico. Cero archivos sin subir, cero archivos fantasma.

| Canal | Archivo | Bytes | sha256 (16) | Remoto |
|---|---|---|---|---|
| Facebook | 01 | 46.824 | `2fb1cbce34804c3d` | ✓ |
| Facebook | 02 | 46.723 | `9b135a5873090451` | ✓ |
| Facebook | 03 | 46.612 | `81d776b17ad01c35` | ✓ |
| Facebook | 04 | 45.765 | `ad7f586ea6b0b585` | ✓ |
| Facebook | 05 | 41.701 | `baeecceb35cca3b4` | ✓ |
| WhatsApp | 01 | 65.562 | `49bb71194d12c6c1` | ✓ |
| WhatsApp | 02 | 65.598 | `6f10c22d91adaa74` | ✓ |
| WhatsApp | 03 | 65.363 | `64a9c2083cccdfde` | ✓ |
| WhatsApp | 04 | 65.323 | `09f6ae34fe1e2b24` | ✓ |
| WhatsApp | 05 | 65.265 | `8845438bd6683205` | ✓ |

### Método C · coherencia interna del texto

Para cada una de las diez piezas vivas, cuatro comprobaciones que no dependen de ninguna de las dos anteriores:

1. **Caracteres** del archivo contra los declarados en `docs/bandas.json`.
2. **Dentro de la banda** del canal (40.000–45.000 en Facebook; 63.000–63.099 en WhatsApp).
3. **Fecha del nombre** igual a la **fecha del dateline** del propio texto.
4. **sha256 de la pieza** igual al que su envío generado anota en la cabecera.

Resultado: **10 de 10 piezas pasan las cuatro**, sin una sola discrepancia. Las dos entradas `LEEME` quedan fuera del cómputo a propósito: no son publicaciones y no llevan firma, igual que las excluye la vara.

## 4 · La vara, al final

```
python3 tools/vara.py   →   fallos: NINGUNO
```

Con **10.170 archivos sellados**, huella `4552ba1f439a3dc2…` encadenada con la anterior, G0 con 258 piezas y G9 con `5 · fallos: 0` y `5 · fallos: 0`.

## 5 · Lo que este acta no dice

No dice que la serie esté terminada. Dice que lo publicado está ordenado y comprobado. El ciclo vivo va de la **01 a la 14** por canal: hay cinco piezas publicadas en cada uno y faltan nueve, con sus títulos y su orden declarados en el LEEME de cada carpeta. Eso es trabajo de los próximos turnos, y no se anuncia como hecho.

*La Bandita informa a partir de fuentes fechadas.*
