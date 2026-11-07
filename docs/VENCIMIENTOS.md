# VENCIMIENTOS DEL REGISTRO

*Generado por `tools/vencimiento.py` con las ventanas de [`POLITICA-FRESCURA.json`](POLITICA-FRESCURA.json). No se edita a mano: se vuelve a correr.*

**TL;DR —** al corte del **2026-11-03**, de **6.838 fichas**: **6.560 vigentes**, **0 por vencer**, **0 vencidas** y **0 sin respaldo de fecha**. Además, **278 sin objeto**: el repositorio ya no existe, así que no hay nada que volver a medir. Veredicto: **TODO VIGENTE**.

## Qué significa cada estado

| Estado | Qué dice | Qué se hace |
|---|---|---|
| **vigente** | todos sus campos dentro de ventana y la fecha respaldada por su evidencia | nada |
| **por vencer** | algún campo entra en sus últimos 15 días | se avisa: entra en la próxima tanda |
| **vencida** | algún campo supera su ventana | se vuelve a medir, y si no se puede, se declara |
| **sin respaldo** | la fecha declarada no es la de su evidencia | se vuelve a medir para que la fecha sea verdad |
| **sin objeto** | el repositorio ya no existe (404) | no se puede remedir: se conserva la ficha con su motivo |

## Las ventanas, y por qué cada una

| Campo | Ventana | Por qué |
|---|---|---|
| `actividad.ultimo_push` | 30 días | El estado vivo/dormido se calcula con el último empujón. Un mes es el plazo en que una etiqueta «vivo» sigue siendo defendible: pasado ese tiempo, el repositorio puede haber publicado diez veces o haberse archivado. |
| `actividad.release_en` | 30 días | Una versión citada sin fecha de comprobación caduca en cuarenta y ocho horas (pieza 04 de WhatsApp). Treinta días es el techo del calendario mensual de remediciones; más allá, el número que se cita ya no es el que se instala. |
| `merito.stars` | 30 días | Las estrellas son la señal más volátil del registro y la que más se usa para ordenar: ordenar por un número de hace dos meses es ordenar por una foto vieja. |
| `merito.scorecard` | 90 días | El Scorecard de OpenSSF es una foto de prácticas (revisión, ramas protegidas, dependencias) que cambia despacio y cuesta de recalcular: noventa días, la misma ventana que la licencia y que las novedades de la casa. |
| `licencia` | 90 días | Misma ventana que la regla de novedades de la casa (CALENDARIO-DE-NOVEDADES). Una licencia puede cambiar de un día para otro, pero cambiarla es un acto raro y deliberado; noventa días detecta el cambio sin gastar mediciones. |
| `ficha` | 180 días | El umbral de la compuerta G2 de la vara. Pasado medio año, la ficha entera se declara vencida aunque ninguno de sus campos sueltos haya fallado. |

## Las primeras veinticinco, por gravedad

| Ficha | Estado | Declarada | Evidencia | Edad | Vencida por |
|---|---|---|---|---|---|
| `0xbadcod3--obtainx-root` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `123456789zws--morphe-manager` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `123456789zws--vectras-vm-android` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `2007shahadat--codeassist` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `869386072406856--linux-42000` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `abdellox--mangayomi` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `aki-dev-code--airi` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `alexkoj--aniyomi` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `alyxme--fmhy` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `amarjitmondal836-commits--zangetsu` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `android-zeros--vectras-vm-android` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `anosu--lemonmanager` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `arkaneelroy--codeassist` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `ate-art--installerx-revived` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `avesta259--mangayomi` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `bilakau--kaizen-app` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `binarysit--jhentai` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `birhantprkc--kai` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `birhantprkc--tinyai` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `bitchcreateshitware--jhentai` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `blulee9--anikku` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `bomuggle-ks--installerx-revived` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `cagecellag--fmhy` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `celestiallauncherreleases--anythingllm-mobile` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |
| `celestiallauncherreleases--kilo-ide` | **sin_objeto** | 2026-11-03 | 2026-10-15 | 19 d | — |

## La deuda, dicha sin adorno

Las **0** fichas sin respaldo no están desactualizadas: están mal fechadas. Declaran el día de la última corrida como si fuera el día de la medición, y su única evidencia es una fila del censo del 15 de octubre. Eso no es un dato viejo: es un dato con la fecha cambiada, y la compuerta G2 las contaba como recién medidas. Se remedian, y la que no se pueda remedir se queda marcada como vencida con su motivo escrito.

*La Bandita informa a partir de fuentes fechadas.*
