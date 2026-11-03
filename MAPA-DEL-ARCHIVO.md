# MAPA DEL ARCHIVO

*La puerta única. Si una acta vieja cita una ruta que ya no existe, aquí está su traducción. Actualizado el 3 de noviembre de 2026.*

## La regla que ordena todo

**El presente en la puerta; el pasado en su carpeta y con su fecha.** Nada se borra, nada se reescribe hacia atrás: lo que cambió se corrige hacia adelante y la corrección queda anotada. Quien abre una carpeta tiene que saber en un segundo qué se está publicando hoy y qué es memoria.

## Qué es este repositorio, en tres capas

| Capa | Dónde | Qué contiene |
|---|---|---|
| **Ley** | `CIMIENTOS/` · `corpus-la-bandita/` | Principios, precedencia, criterios C-01 a C-24, Manual de Estilo y Operaciones V3.0, contrato de datos, licencias y raya legal |
| **Oficio** | `SKILLS/` · `PROCESOS/` · `tools/` | Las habilidades ejecutables y las treinta y cinco herramientas que miden, sellan y comprueban |
| **Producto** | `guia-maestra/` · `Arena-Reimagined/01-PUBLICACIONES/` · `site/` | La guía de doce capítulos, las piezas de los dos canales y el sitio generado |

## Los dos ciclos vivos

**La guía maestra.** Doce capítulos, setenta fichas, cada una con autor, licencia, versión y fecha de medición. Vive en `guia-maestra/`: los datos en `datos/apps/`, los textos en `texto/capitulos/`, las páginas en `sitio/` y la lista de créditos en `CREDITOS.md`. Se genera y se valida con un solo comando.

**La serie de canal.** Dos carpetas, un ciclo de catorce piezas cada una:

- `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/` — piezas de 40.000 a 45.000 caracteres. Va primero.
- `Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES/` — piezas de 63.000 a 63.099 caracteres. Va después, y no es la misma pieza recortada: es otro texto, porque la compuerta M23 prohíbe párrafos compartidos entre canales.

En las dos carpetas la raíz tiene **solo las piezas del ciclo** y un `LEEME-de-la-carpeta.md` con la tabla de estado. Todo lo anterior está en `_ARCHIVO-HISTORICO/` de cada carpeta, ordenado por mes.

## Estado del ciclo de canal, hoy

| Canal | Piezas vivas | Rango | Banda | Siguiente |
|---|---|---|---|---|
| Facebook | 01 a 05 | 40.253 a 44.994 | 40.000–45.000 | 06 · El taller |
| WhatsApp | 01 a 05 | 63.006 a 63.098 | 63.000–63.099 | 06 · El taller en el bolsillo |

Las dos tablas completas, con fecha de corte y estado pieza por pieza, están en el LEEME de cada carpeta.

## Dónde está cada cosa

```
guia-maestra/                 la guía: datos, textos, páginas y créditos
Arena-Reimagined/
  01-PUBLICACIONES/
    Facebook-dominicano-ES/   ciclo vivo + 00-LEEME + _ARCHIVO-HISTORICO
    WhatsApp-dominicano-ES/   ciclo vivo + 00-LEEME + _ARCHIVO-HISTORICO
    POSTS-COMUNIDAD/          las historias del muro, que no son piezas de la serie
  00-CANON/                   los cuatro archivos de la casa
  02-ARCHIVO/                 registro de hitos y evidencia de las jornadas
registry/                     9.472 fichas medidas, la materia prima de todo
docs/                         compuertas, bandas, envíos, actas y decisiones
  bandas.json                 la banda de longitud de cada pieza viva
  envios/<canal>/             los envíos listos para mandar
  envios/_historico/          los envíos de las piezas que pasaron al archivo
tools/                        las herramientas: vara, compuertas, medición, sellado
site/                         el frontend generado, sin CDN ni dependencias
CIMIENTOS/ · PROCESOS/ · SKILLS/ · corpus-la-bandita/   la ley y el oficio
```

## Carpetas de memoria que no se tocan

`_archivo-historico/`, `archivo/`, `03-PUBLICACIONES-2026-09-15/`, `04-VERSIONES-MULTIIDIOMA/`, `backup-previo-correccion-14-09/`, `uploads/`, `datos-censo/`, `datos-miyomi/`, `datos-v25/` y los `_ARCHIVO-HISTORICO/` de las dos carpetas de canal. Son historia firmada: se leen, no se ordenan.

## Cómo se comprueba el estado que declara este mapa

Tres métodos, y los tres tienen que coincidir. El acta con las corridas y sus números es `docs/ACTA-ORDEN-Y-VERIFICACION-2026-11-03.md`.

1. **Árbol y contenido** — contar lo que hay y sellar cada pieza con su suma de verificación.
2. **La fuente remota** — preguntarle a la plataforma, sin el clon de por medio, qué archivos hay y de qué tamaño.
3. **Coherencia interna** — fecha del nombre, dateline, tamaño declarado en `docs/bandas.json` y huella anotada en el envío, del mismo archivo.

Y al final, la vara: `python3 tools/vara.py` tiene que decir **fallos: NINGUNO**. No es un adorno: es la puerta de salida de todo lo que se publica.

*La Bandita informa a partir de fuentes fechadas.*
