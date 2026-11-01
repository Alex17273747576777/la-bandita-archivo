# BARRIDO AL MÍNIMO ERROR · domingo 1 de noviembre de 2026, 06:40–07:20 (Santo Domingo)

**Qué es.** La tercera pasada del día sobre las cinco entregas, esta vez con auditoría **por línea y por
bloque** en vez de por patrón suelto. La pasada de las 06:15 arregló 42 cifras; esta encontró **61 errores
más** que aquella no podía ver, y cuatro recursos nuevos medidos hoy.

---

## 1 · Por qué la pasada anterior no los vio

La comprobación de las 06:15 buscaba el patrón «dueño/repo … ★número» con una ventana de 120 caracteres.
El texto real escribe las fichas de cinco maneras distintas (`• **owner/repo** — ★N`, `*Nombre* — ★N`,
`Medido hoy: *★N`, `• Nombre — *★N`, tablas con `|`). Todo lo que no encajaba en el primer molde **pasaba
sin revisar**: eran 28 cifras en la prosa y en los bloques numerados, invisibles para esa compuerta.

Esta vez se hizo al revés: se parte de **cada aparición de ★** y se le busca el dueño por cercanía, y
además se audita cada bloque (bullets de ficha y fichas numeradas) comparando estrellas, licencia, fecha de
creación, último empuje y última release contra la API. Lo que sigue es lo que salió.

---

## 2 · Los 61 errores, por clase

### 2.1 · Estrellas (28 valores, 46 apariciones)

| Decía | Es | Dónde |
|---|---|---|
| ★7.678 | **7.677** | 01 WA y 01 FB (Droid-ify) |
| ★5.589 / ★5.591 | **5.595** | 01 WA / 01 FB (Neo-Store) |
| ★21.097 | **21.105** | 01 WA y 01 FB (Obtainium) |
| ★1.369 | **1.371** | 01 WA y 01 FB (RepoStore) |
| ★9.393 | **9.399** | 01 WA, 01 FB y la respuesta del quiz de la 01 WA |
| ★1.653 | **1.661** | 01 WA (dos sitios) y 01 FB (dos sitios) |
| ★7.257 / ★7.258 | **7.259** | 01 WA (dos) y 01 FB |
| ★1.397 | **1.398** | 01 WA (Universal-Patch-Manager) |
| ★3.197 | **3.198** | 01 WA (AAAD) |
| ★624 | **625** | 01 WA (GrapheneOS AppStore) |
| ★2.306 | **2.305** | 01 FB (Accrescent) |
| ★8.943 | **8.946** | 02 WA (tres sitios) y 02 FB (Kotatsu) |
| ★24.913 | **24.922** | 02 WA (dos) y 02 FB (Mihon) |
| ★656 | **659** | 02 WA (dos, Kototoro) |

### 2.2 · Fechas y versiones (12)

- **Obtainium** publicó **v1.7.4 el 1 de noviembre** y la pieza citaba v1.7.3 del 25 de octubre → corregido
  en las dos piezas 01, con la frase «publicó hoy».
- **universal-installer** publicó **v1.21.0 el 1 de noviembre** y la pieza citaba v1.20.0 del 25 de octubre
  → corregido en las dos piezas 01.
- **komikku** empujó **hoy** (decía 21-oct) · **mangayomi** empujó **hoy** (decía 31-oct) ·
  **Suwayomi-Server** empujó **hoy** (decía 24-oct) · **Suwayomi-Tsumiru** empujó **hoy** (decía 30-oct).
  Corregidos en las fichas y en el cuerpo de las dos piezas 02.
- **Droid-ify** lleva **50 días** quieto (decía 49) · **Shizuku** lleva **501 días** sin empujar (decía 500,
  en tres sitios y en la respuesta del quiz) · **Suwayomi-JUI** se movió hace **17 días** (decía 16).

### 2.3 · Contadores internos que no cuadraban consigo mismos (8)

- 02 FB: la ficha decía **48** y el cuerpo **49** → 49 en los cuatro sitios.
- 02 WA: decía «**dieciséis** proyectos de 2026»; el censo tiene **14** nacidos en 2026 → corregido.
- 01 FB: cantaba «18 repositorios y 21 enlaces» con **19 y 22** medidos → corregido.
- 01 WA: la ficha decía 30 repos y la firma 28 enlaces; ahora **31 y 29**, con los números verificados.

### 2.4 · Dos preguntas de quiz que no resistían una comprobación (2)

- **01 FB, pregunta 3:** pedía una app con ★13.832 y «última release de 2018». Ni la cifra ni la fecha
  existen hoy en el censo (Lawnchair tiene 13.833 y su release visible es de hoy). Se sustituyó por una
  pregunta que sí se puede comprobar: qué dos apps empujaron y publicaron el 1 de noviembre.
- **01 WA, respuesta 5:** repetía 9.393 con la cifra medida en 9.399.

---

## 3 · Lo que entró de la investigación de recursos nuevos

Detalle completo en `docs/INVESTIGACION-RECURSOS-2026-11-01.md`. Resumen:

| Recurso | ★ | Licencia | Creado | Última release | Dónde entra |
|---|---|---|---|---|---|
| `vinstall/VInstall` | 105 | GPL-3.0 | 03-abr-2026 | v0.4.5 (30-oct) | piezas 01: único que abre el APKV cifrado |
| `ruzhe85/Komiho` | 79 | Apache-2.0 | 19-ago-2026 | v1.6.0 (28-oct) | piezas 02: cliente de Komga nuevo |
| `Boomckman/usagi-nightly` | 114 | sin licencia | 28-jun-2026 | ninguna | piezas 02: **quinto cebo**, se nombra y no se enlaza |

Fuera, con el motivo escrito: `bl3xand/APK-Toolbox` (tres semanas de vida: no se recomienda lo que no ha
demostrado nada), `FedeFluork/multistore` (beta y cinco semanas dormido), `Saber-Alter-Lily/pica-library`
(contenido adulto; esta guía es familiar).

---

## 4 · Estado final medido a las 07:20

| Pieza | Caracteres | Banda | Repos | Enlaces |
|---|---|---|---|---|
| 01 WhatsApp | **63.021** | 63.000–63.099 ✔ | 31 | 29 |
| 01 Facebook | **43.226** | 40.000–45.000 ✔ | 19 | 22 |
| 02 WhatsApp | **63.084** | 63.000–63.099 ✔ | 53 (46 vivos · 4 archivados · 3 muertos) | 56 |
| 02 Facebook | **43.056** | 40.000–45.000 ✔ | 49 | 33 |
| Post de comunidad | **4.152** | exacta ✔ | — | 4 |

Comprobaciones corridas a esa hora: `vara.py` → **fallos: NINGUNO**, G10 con **5 piezas en banda** ·
`envio.py --verificar` → **114 y 148 envíos, 0 fallos** · `autoprueba.py` → **11/11** ·
párrafos compartidos entre las cinco entregas → **0** · `atestar.py` → **10.024 archivos** ·
CI **41298113156 success** · `cosign verify-blob` → **Verified OK**.

---

## 5 · Lo que sigue sin hacer, dicho sin adornos

- **230 piezas de la serie siguen sin reescribir:** 112 de WhatsApp (03-112) y 118 de Facebook (03-120).
  Perfectas las cinco de hoy; el resto es el archivo con su fecha original.
- **Las cifras volverán a moverse.** Las piezas dicen la hora de la medición (06:15) para que el envejecimiento
  sea visible y no una sorpresa.
- **No avanzo a la 03** hasta que el dueño apruebe estas cinco.

💓 *La Bandita · domingo 1 de noviembre de 2026, 07:20 · Santo Domingo.*
