# REVISIÓN PROFUNDA · las cinco entregas del domingo 1 de noviembre de 2026

**Qué es este documento.** Lo que se entrega para que el dueño revise pieza por pieza, con la lista de
comprobaciones que se corrieron, los fallos que encontré al revisar y lo que queda abierto. No es un
informe de mercadeo: es un acta. Cada cifra de aquí salió de un comando ejecutado hoy y está dicha con
la hora del día en que se midió.

**La fecha de la casa:** domingo **1 de noviembre de 2026**, Santo Domingo (UTC-4). Toda pieza de hoy
lleva esa fecha en su dateline, y toda afirmación con la palabra «hoy» se comprobó contra la API de
GitHub el mismo día.

---

## 1 · Lo que se entrega para revisión

| # | Pieza | Caracteres | Repos | Enlaces | Estado |
|---|---|---|---|---|---|
| 1 | **01 WhatsApp** — tiendas de APK | **63.075** | 31 | 28 · todos 200 | lista para revisar |
| 2 | **01 Facebook** — tiendas de APK, en escenas | **42.746** | 22 | 21 · 15 en 200 y 6 en 429 | lista para revisar |
| 3 | **02 WhatsApp** — el mueble de los tres cajones | **63.079** | 56 | 55 · 52 en 200 y 3 en 404 documentados | lista para revisar |
| 4 | **02 Facebook** — el barrio cambió de gente | **42.311** | 56 | 32 · 26 en 200 y 6 en 429 | lista para revisar |
| 5 | **Post de comunidad** — «mama hueso» | **4.135** | — | 4 · todos 200 | listo para revisar |

Rutas dentro del repositorio:

- `Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES/01-Tiendas-APK-legales-mods-reloj-2027-WhatsApp-La-Bandita-2026-10-31-dominicano-ES.md`
- `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/01-Tiendas-APK-legales-mods-reloj-2027-Facebook-La-Bandita-2026-10-31-dominicano-ES.md`
- `Arena-Reimagined/01-PUBLICACIONES/WhatsApp-dominicano-ES/02-El-mueble-de-los-tres-cajones-familia-Tachiyomi-servidores-y-archivo-WhatsApp-La-Bandita-2026-10-31-dominicano-ES.md`
- `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/02-El-barrio-cambio-de-gente-mueble-de-comics-Facebook-La-Bandita-2026-10-31-dominicano-ES.md`
- `Arena-Reimagined/01-PUBLICACIONES/POSTS-COMUNIDAD/post-2026-11-01-mama-hueso-WhatsApp-La-Bandita-dominicano-ES.md`

Y el archivo entero en un solo archivo: **`Arena-Reimagined/01-PUBLICACIONES/LAS-263-PUBLICACIONES-2026-11-01.html`**
(114 de WhatsApp + 148 de Facebook + el post de comunidad, sin un solo recurso externo).

---

## 2 · Cómo se revisa (tres comandos, sin creerme)

```
python3 tools/vara.py            # las once compuertas, con sus cifras
python3 tools/envio.py --verificar && python3 tools/envio.py --verificar --canal facebook
python3 tools/autoprueba.py      # 11 casos: cada compuerta tiene que saber cazar su violación
```

Para comprobar una cifra suelta de cualquier ficha, sin instalar nada:

```
curl -s -H "Authorization: Bearer $LBT" https://api.github.com/repos/mihonapp/mihon | grep stargazers_count
```

`LBT` es el token del dueño: **no está escrito en ningún archivo de este repositorio**.

---

## 3 · La matriz de comprobaciones, pieza por pieza

| Comprobación | 01 WA | 01 FB | 02 WA | 02 FB | Post |
|---|---|---|---|---|---|
| Longitud dentro de su banda declarada | 63.075 ✔ | 42.746 ✔ | 63.079 ✔ | 42.311 ✔ | 4.135 ✔ (banda exacta) |
| Dateline con la fecha de hoy | sí | sí | sí | sí | sí |
| Firma 💓 | sí | sí | sí | sí | sí |
| Vallas de código balanceadas | 8 (par) | 2 (par) | 2 (par) | 2 (par) | 0 |
| Caracteres de ancho cero | 0 | 0 | 0 | 0 | 0 |
| Repos citados y medidos hoy | 31 | 22 | 56 | 56 | — |
| Repos muertos, cada uno con su 404 escrito | 1 (`droidify/client`) | 0 | 3 | 3 | — |
| Enlaces que responden 200 | 28/28 | 15/21 | 52/55 | 26/32 | 4/4 |
| Enlaces en 429 (límite de GitHub, no muerte) | 0 | 6 | 0 | 6 | 0 |
| Párrafos compartidos con otra pieza | **0** | **0** | **0** | **0** | **0** |
| Quiz con respuestas invertidas y descifradas | sí | sí | sí | sí | — |

**El dato que más importa del cuadro:** cero párrafos compartidos entre las cinco entregas. Se midió
por script —párrafos de más de 110 caracteres, comparados dos a dos— y no a ojo.

---

## 4 · Lo que encontré al revisar (y corregí antes de entregar)

Esta sección es la razón de ser del documento. Si no hubiera encontrado nada, no habría revisado.

### 4.1 · Cinco desfases de estrellas, de una medición a la siguiente

La pieza se midió por la mañana y se volvió a medir al cerrar. En esas horas, cinco cifras se movieron:

| Repo | Decía | Dice hoy | Dónde estaba |
|---|---|---|---|
| `RikkaApps/Shizuku` | ★32.552 | **★32.554** | 01 WA y 01 FB |
| `ImranR98/Obtainium` | ★21.095 / 21.096 | **★21.097** | 01 WA y 01 FB |
| `wxxsfxyzm/InstallerX-Revived` | ★7.257 | **★7.258** | 01 WA y 01 FB |
| `iamr0s/Dhizuku` | ★4.067 | **★4.069** | 01 FB |
| `mihonapp/mihon` · `aniyomiorg/aniyomi` · `Kototoro-app/Kototoro` · `kodjodevf/mangayomi` · `zmz125000/LocalViewer` | ★24.913 · 7.863 · 656 · 4.285 · 197 | **★24.916 · 7.865 · 657 · 4.286 · 198** | 02 WA y 02 FB |

Corregidas las treinta y siete apariciones. **Ninguna de las piezas se pasó de su banda** al corregirlas,
porque los números conservan longitud (2.1097 → 21.097 es el mismo número de caracteres).

### 4.2 · Trece fechas relativas que se volvieron falsas al cambiar el día

Las piezas se escribieron el 31 de octubre. Al pasar a **1 de noviembre**, frases como «empujó hoy»
dejaron de ser verdad: esos empujes eran del día anterior. Se revisaron una por una contra la API y se
corrigieron trece:

- `accrescent/accrescent`, `fmhy/edit`, `timschneeb/awesome-shizuku`, `iamr0s/Dhizuku`,
  `wxxsfxyzm/InstallerX-Revived`, `Kototoro-app/Kototoro`, `kodjodevf/mangayomi`,
  `jakepurple13/OtakuWorld` → **«empujó ayer»** (empuje del 31 de octubre).
- `GrapheneOS/AppStore`, `ImranR98/Obtainium`, `pass-with-high-score/universal-installer`,
  `timschneeb/ShizuStore`, `nekomangaorg/Neko`, `keiyoushi/extensions-source`, `gotson/komga`,
  `Kareadita/Kavita` → **«empujó hoy»** (empuje del 1 de noviembre).
- Tres releases que decían «de hoy» y no lo eran: `Utolaris/Kujira-Manga` (v1.5.3, 25-oct),
  `Mister-album/Koharia` (v0.7.5, 27-oct) y `Wammy-app/Wammy` (v0.1.4, 25-oct).

### 4.3 · Una afirmación falsa que yo mismo había escrito

En la 01 de WhatsApp decía que **RepoStore** era «la única de esta lista que publicó una versión el
mismo día en que la medí», y el mini-quiz premiaba ese dato. Al re-medir: la release **v1.0.22 es del
29 de octubre**, no del día de la medición. Era una afirmación bonita y falsa.

Corregida en cinco sitios: el bloque de las puertas nuevas, el cuerpo del texto, la tabla de decisión, la
pregunta del quiz y su respuesta invertida. La pregunta ahora es comprobable: *«¿Qué puerta nueva nació
en enero de 2026, es MIT y tiene versión del 29 de octubre?»*.

### 4.4 · Tres párrafos compartidos que la compuerta no ve

`vara.py` mide repetición **dentro** de una pieza (G6), no **entre** piezas. Al comparar las cuatro
entregas dos a dos aparecieron tres coincidencias:

1. La lista de los cuatro repositorios cebo, idéntica en 01 WA y 02 FB.
2. La frase de cierre de 02 WA («La app que uses mañana…»), repetida en 02 FB.
3. La tesis del cierre («lo que se puede respaldar, se puede mudar…»), repetida en 02 FB.

Las tres se reescribieron en la pieza de Facebook, que es la que las tomaba prestadas. Después del
arreglo: **0 párrafos compartidos en las diez parejas posibles**.

### 4.5 · Lo que la compuerta no cubre y ahora está declarado

- **429 no es 404.** Seis enlaces de 01 FB y seis de 02 FB devolvieron 429 (límite de peticiones de
  GitHub) en la última pasada. En la pasada anterior respondieron 200. Se quedan como «no deja entrar a
  un robot», que es lo que son, y no se cuentan como muertos.
- **El post de comunidad está fuera del circuito de envíos.** `tools/envio.py` parte las piezas de las
  dos carpetas de canal; el post vive en `POSTS-COMUNIDAD` y se pega tal cual. Sus cuatro enlaces se
  midieron a mano hoy con `curl -A` (los cuatro, 200) y no pasan por `--verificar`. Dicho queda antes de
  que alguien lo descubra por su cuenta.
- **Las estrellas siguen moviéndose.** La foto es del domingo 1 de noviembre, entre las 04:20 y las
  04:45, hora de Santo Domingo. Mañana será otra. La pieza dice la fecha al lado de cada cifra para que
  nadie la lea como eterna.

---

## 5 · Sobre el post de comunidad (lo que decidí y por qué)

El texto que me pasó el dueño recomienda, entre las fuentes buenas, ocho páginas de APKs modificados,
parches de compras y ROMs (`espacioapk`, `happymod`, `luckypatchers`, `liteapks`, `platinmods`,
`zona-leros`, `axekin`, `romheaven`).

**Se publica el post, con las ocho nombradas y ninguna enlazada.** No es censura: es la regla que la casa
ya tiene escrita desde la 01 —*los letreros de mods se nombran, no se enlazan*— y es la única forma de
que el post siga diciendo la verdad que dice, que es que esas puertas cobran en riesgo lo que prometen
en gratis. Enlazarlas habría convertido una crítica en un reparto.

Las cuatro que sí van con enlace son las que respondieron **200 hoy**: `fmhy.net`, `virgil.samidy.com`,
`komistore.app` y `appteka.store`. Con una advertencia puesta en el propio post: FMHY y Appteka no
firman nada, sirven para descubrir, y la verificación sigue siendo tuya.

---

## 6 · Lo que sigue abierto (y no se disimula)

- **230 piezas de la serie sin reescribir:** 112 de WhatsApp (03 a 112) y 118 de Facebook (03 a 120).
  Están en el archivo con su fecha original a la vista y **no** se presentan como frescas.
- **La revisión del dueño.** Este documento existe para que él pueda aprobar o rechazar cada entrega con
  los ojos en el dato, no en mi palabra. Si algo de lo que digo aquí no le cuadra, el comando para
  desmentirlo está en la sección 2.
- **Los enlaces en 429** volverán a 200 cuando pase la ventana de límite; conviene re-medir antes de
  mandar los envíos de Facebook.

---

💓 *La Bandita · domingo 1 de noviembre de 2026 · Santo Domingo.* Todo lo que este documento afirma se
comprobó ejecutando algo hoy. Lo que no se midió, está dicho como no medido.
