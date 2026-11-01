# REVISIÓN EN VIVO · domingo 1 de noviembre de 2026, 06:15 (hora de Santo Domingo)

**Qué es esto.** El mapa completo vuelto a medir, pieza por pieza, a las seis de la mañana del domingo.
No es una copia del acta de las 04:30: es otra medición, con la API otra vez, y por eso encuentra cosas
que la anterior no podía encontrar — entre ellas, que las cifras de la primera revisión ya se habían
movido.

**Hora de referencia.** GitHub marcaba `Sun, 01 Nov 2026 10:04:45 GMT` cuando empecé; en Santo Domingo
(UTC-4) eso son las **06:04**. La fecha de la casa sigue siendo **domingo 1 de noviembre de 2026**.

---

## 1 · El mapa, pieza por pieza, medido ahora

| Pieza | Caracteres | Banda | Repos en la ficha | Vivos | Archivados | Muertos | Enlaces | Responden 200 |
|---|---|---|---|---|---|---|---|---|
| 01 WhatsApp | **63.099** | 63.000–63.099 ✔ | 30 | 29 | 0 | 1 (`droidify/client`, 404) | 28 | **28** |
| 01 Facebook | **42.726** | 40.000–45.000 ✔ | 18 | 18 | 0 | 0 | 21 | **21** |
| 02 WhatsApp | **63.075** | 63.000–63.099 ✔ | 52 | 45 | 4 | 3 (404 escritos) | 55 | 52 (+3 en 404) |
| 02 Facebook | **42.293** | 40.000–45.000 ✔ | 48 | 41 | 4 | 3 (404 escritos) | 32 | **32** |
| Post de comunidad | **4.152** | exacta ✔ | — | — | — | — | 4 | **4** |

Los tres 404 de la 02 son los de siempre y van escritos a propósito: `tachiyomiorg/tachiyomi`,
`Mangayomi-app/Mangayomi` y `Paperback-Community/Paperback`. Los cuatro archivados tampoco son un fallo:
`KotatsuApp/Kotatsu`, `Koitharu/OpenManga`, `timschneeb/tachiyomi-extensions-archive` y
`aniyomiorg/aniyomi-extensions` están marcados como archivados, que es lo que son.

**Los 429 desaparecieron.** En la revisión de las 04:30 había doce enlaces de Facebook que devolvían «no
deja entrar a un robot». A las 06:15 los **32 de la 02 y los 21 de la 01 responden 200**. Era la ventana
de límite de GitHub, como estaba dicho.

---

## 2 · Lo que se movió en dos horas (y por eso hay que volver a medir)

**28 repositorios cambiaron de estrellas entre las 04:30 y las 06:15.** La pieza que se publica con
cifras de la mañana envejece antes del almuerzo; esa es la razón de que el sello lleve hora.

| Repo | 04:30 | 06:15 | Δ | Estado |
|---|---|---|---|---|
| `RikkaApps/Shizuku` | 32.554 | 32.573 | **+19** | vivo |
| `pass-with-high-score/universal-installer` | 1.653 | 1.661 | +8 | vivo |
| `ImranR98/Obtainium` | 21.097 | 21.105 | +8 | vivo |
| `fmhy/edit` | 12.666 | 12.673 | +7 | vivo |
| `MuntashirAkon/AppManager` | 9.393 | 9.399 | +6 | vivo |
| `mihonapp/mihon` | 24.916 | 24.922 | +6 | vivo |
| `offa/android-foss` | 11.607 | 11.611 | +4 | vivo |
| `NeoApplications/Neo-Store` | 5.591 | 5.595 | +4 | vivo |
| `keiyoushi/extensions-source` | 4.839 | 4.843 | +4 | vivo |
| `roxycon-dev/Ciallo-Reader` | 261 | 265 | +4 | vivo |
| `timschneeb/awesome-shizuku` | 10.667 | 10.670 | +3 | vivo |
| `KotatsuApp/Kotatsu` | 8.943 | 8.946 | +3 | **archivado** |
| `samyak2403/RepoStore` · `iamr0s/Dhizuku` · `Kototoro-app/Kototoro` · `Mister-album/Koharia` · `zmz125000/LocalViewer` | — | — | +2 cada uno | vivos |
| `GrapheneOS/AppStore` · `wxxsfxyzm/InstallerX-Revived` · `Jman-Github/Universal-Patch-Manager` · `shmykelsa/AAAD` · `komikku-app/komikku` · `Chimahon/chimahon` · `chmouel/liseur` · `aidoku-community/sources` | — | — | +1 cada uno | vivos |
| `Droid-ify/client` | 7.678 | 7.677 | **−1** | vivo |
| `accrescent/accrescent` | 2.306 | 2.305 | **−1** | vivo |
| `aniyomiorg/aniyomi` | 7.865 | 7.864 | **−1** | vivo |

**Tres cosas que este cuadro demuestra y que ninguna guía suele decir:**

1. **Las estrellas suben y también bajan.** Tres proyectos perdieron una en dos horas. Un número que solo
   sube en tus apuntes no es un número medido: es un número copiado.
2. **Un repositorio archivado sigue ganando estrellas.** Kotatsu lleva casi un año cerrado y aun así ganó
   tres. Las estrellas miden atención acumulada, no salud.
3. **Cuarenta y dos cifras se actualizaron** en las cuatro piezas (80 apariciones contando las repetidas).
   Todas dentro de banda, porque el número cambia pero no de tamaño.

---

## 3 · Los fallos que encontró esta pasada (y se corrigieron)

### 3.1 · Cuatro fechas relativas que la pasada de las 04:30 dejó al revés

Entre las dos revisiones el día siguió avanzando y dos repositorios empujaron de nuevo:

- `fmhy/edit` — pasó a empujar **el 1 de noviembre** (dos apariciones en la 01 WA): de «ayer» a «hoy».
- `kodjodevf/mangayomi` — igual, empujó **el 1 de noviembre** (dos apariciones en la 02 WA): de «ayer» a «hoy».

Es exactamente el problema que este archivo denuncia: una frase relativa sin hora se vuelve falsa sola.

### 3.2 · Cuatro contadores internos que no cuadraban consigo mismos

Esto no lo caza ninguna compuerta, porque cada número es plausible por separado; lo que falla es que
**no coinciden con el propio texto que los rodea**:

| Pieza | Decía | Dice ahora | Qué era |
|---|---|---|---|
| 01 WA (firma) | «los 30 repositorios **y sus 36 enlaces**» | **28 enlaces** | el recuento era de una versión anterior del texto |
| 01 FB (firma) | «**33 repositorios** … y **39 enlaces**: los 33 están vivos y los 39 responden» | **18 repos en ficha · 21 enlaces** | arrastraba el recuento de la lista vieja que se sustituyó |
| 02 WA (mapa, ficha, cuerpo, firma) | «53 repos» · «la ficha de hoy (32 repos)» · «medir 40 repositorios» · «3 archivados … 3 archivados» | **52 · 52 · 52 · 4 archivados** | tres recuentos de tres versiones distintas del mismo texto |
| 02 FB (ficha y firma) | «49 repositorios» y una firma sin cifras | **48 · 41 vivos, 4 archivados, 3 muertos** | el número bueno era el de la ficha, no el del título |

Un texto puede tener todas las cifras bien y aun así mentir por dentro. Esa es la lección de esta pasada,
y por eso ahora **cada pieza dice la hora de la medición** en su firma, no solo la fecha.

### 3.3 · El post de comunidad, revisado otra vez

- Los cuatro enlaces (`fmhy.net`, `virgil.samidy.com`, `komistore.app`, `appteka.store`) siguen **200**.
- Las ocho páginas de mods, parches y ROMs siguen **nombradas y ninguna enlazada**: comprobado por script,
  el post no contiene ni una sola URL con esos dominios.
- Se le añadió la hora a su firma (06:15) y su banda exacta quedó actualizada en `docs/bandas.json`
  (4.152 caracteres, mínimo igual a máximo).

---

## 4 · El resto del mapa: lo que también se volvió a correr

| Comprobación | Resultado a las 06:35 |
|---|---|
| `tools/envio.py --medir` | 315 repos y 490 enlaces (WhatsApp) · 697 repos y 1.052 enlaces (Facebook) |
| `tools/envio.py --verificar` | **114 envíos · 0 fallos** · **148 envíos · 0 fallos** |
| `tools/vara.py` | **fallos: NINGUNO** · G10 con **5 piezas en banda** |
| `tools/autoprueba.py` | **11/11** violaciones detectadas |
| `tools/atestar.py` | **10.022 archivos · `f7f3eda0f5e28c12…`** |
| HTML del archivo | **263 publicaciones** regeneradas (114 WhatsApp + 148 Facebook + el post) |

Párrafos compartidos entre las cinco entregas: **0** en las diez parejas (medido por script, no a ojo).

---

## 5 · Lo que sigue abierto

- **230 piezas de la serie sin reescribir:** 112 de WhatsApp (03-112) y 118 de Facebook (03-120). En el
  archivo, con su fecha original a la vista.
- **Las cifras seguirán moviéndose.** La pieza dice la hora; la próxima revisión las volverá a mover. Eso
  no es un defecto del método: es el método.
- **La firma de las piezas queda en la hora de esta medición.** Si el dueño manda un envío a las tres de
  la tarde, las cifras tendrán nueve horas: están fechadas y así se leen.

---

💓 *La Bandita · domingo 1 de noviembre de 2026, 06:35 · Santo Domingo.* Todo lo que este documento
afirma se ejecutó hoy, entre las 06:04 y las 06:35. Lo que no se midió, está dicho como no medido.
