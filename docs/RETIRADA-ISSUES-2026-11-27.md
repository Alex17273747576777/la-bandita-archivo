# Retirada de issues propios sin respuesta · 2026-11-27

*Corte: 2026-11-27. Medido con `search/issues` + la API de comentarios, no de memoria.*

---

## 1 · El problema, con la cifra

La cuenta tiene **89 issues abiertos** en repositorios de terceros. **76 no han recibido una sola
respuesta de nadie.** Algunos llevan más de año y medio abiertos.

Un issue abierto sin respuesta no es una petición pendiente: es una petición que el mantenedor nunca
va a leer. Ocupa la primera página de «issues» de un proyecto ajeno, y eso tiene un coste real que
los propios mantenedores ya dijeron en voz alta:

- `komikku#1539`, 2026-02-27: **«Don't create dupe issues. Do you have a memory problem or something?»**
- `komikku#892`, 2026-11-12, `kana-shii`: **«Stop spamming shit in old ass not planned issues.»**
- `keiyoushi/extensions-source#17590`: «Thanks for shitting AI slop in our requests.»

Ese último hilo está **bloqueado** por el mantenedor y no se puede editar ni borrar (registrado en
`docs/ISSUES-RESPALDO-2026-11-09/LEEME.md`). La respuesta a eso no es disculparse otra vez: es
**dejar de ocupar sitio**.

## 2 · El criterio (tres condiciones, las tres obligatorias)

| # | Condición | Por qué |
|---|---|---|
| 1 | Abierto **hoy** | cerrados no se tocan: ya no ocupan sitio |
| 2 | **Cero** respuestas de alguien que no sea el autor | si un mantenedor contestó, el hilo tiene información que se perdería al cerrarlo |
| 3 | **180 días o más** desde su apertura | por debajo, la retirada mata peticiones que aún pueden ser útiles |

De los 89 abiertos: **11** cumplen las tres y se retiran; **12** tienen respuesta y se quedan; **66**
son recientes y se quedan.

## 3 · El método: cerrar **sin comentario**

Aquí es donde esta retirada se separa de la del 9 de noviembre. Entonces se cerró *con una nota*
apuntando al hilo que se quedaba, y estuvo bien. Hoy ya no:

> `kana-shii`, en `komikku#892` el **2026-11-12**: «Stop spamming shit in old ass not planned issues.»

Un comentario más en un issue viejo no planeado es exactamente lo que esa frase pide no recibir. Así
que se cierra con `state_reason = not_planned` y **sin escribir nada**. El cierre quita el issue de la
lista del mantenedor; el comentario, además de no quitar nada, le manda una notificación. No es
timidez: es que el método tiene que servir al que recibe, no al que escribe.

**La constancia no se pierde:** está en este documento, con el texto íntegro de los 11 títulos, la
fecha de apertura y el enlace. Donde se busca una decisión propia es en el archivo propio.

## 4 · Los 11 que se retiran

| Días | Issue | Abierto | Título |
|---:|---|---|---|
| 660 | [`Animetail#220`](https://github.com/Animetailapp/Animetail/issues/220) | 2025-02-05 | Copias en la nube que se interrumpen; petición de que no se pierdan los respaldos |
| 360 | [`komikku#1311`](https://github.com/komikku-app/komikku/issues/1311) | 2025-12-02 | Separar «sincronizar con la nube» de «actualizar biblioteca» |
| 356 | [`komikku#1314`](https://github.com/komikku-app/komikku/issues/1314) | 2025-12-06 | Perfiles de feed múltiple: un título, varias fuentes |
| 295 | [`komikku#1475`](https://github.com/komikku-app/komikku/issues/1475) | 2026-02-05 | WebDAV: reducir el formulario a tres campos |
| 295 | [`komikku#1477`](https://github.com/komikku-app/komikku/issues/1477) | 2026-02-05 | Vista de dos páginas recordada por título |
| 273 | [`komikku#1531`](https://github.com/komikku-app/komikku/issues/1531) | 2026-02-27 | Salud de fuentes compartida: es una decisión de política, no un botón |
| 273 | [`komikku#1532`](https://github.com/komikku-app/komikku/issues/1532) | 2026-02-27 | Perfiles de hardware: retirar la idea, dejar un ajuste medible |
| 273 | [`komikku#1534`](https://github.com/komikku-app/komikku/issues/1534) | 2026-02-27 | Sincronización bidireccional con rastreadores: la regla antes que el código |
| 273 | [`komikku#1540`](https://github.com/komikku-app/komikku/issues/1540) | 2026-02-27 | Categorizar por regla de fuente, visible para el usuario |
| 273 | [`komikku#1544`](https://github.com/komikku-app/komikku/issues/1544) | 2026-02-27 | Estadísticas de lectura por título, con exportación |
| 256 | [`AniZen#12`](https://github.com/salmanbappi/AniZen/issues/12) | 2026-03-16 | Actualización de rastreadores manual primero, con diferencia visible |

**Ninguno de los 11 era una petición mala.** Cinco de los de `komikku` son propuestas de diseño
razonables que el mantenedor simplemente no ha leído. La retirada no dice que estuvieran mal: dice
que, sin respuesta en medio año, ocupar sitio es el único efecto que les queda.

## 5 · Los 12 que se quedan (y por qué)

| Días | Issue | Última respuesta | Quién |
|---:|---|---|---|
| 273 | `komikku#1533` (fuentes muertas) | 2026-11-24 | `cuong-tran` |
| 264 | `Animetail#262` (rendimiento) | 2026-11-11 | *(mía)* + `karkimishan00-ai` |
| 246 | `KomaStream#2` | 2026-11-27 | `Paduu29` |
| — | `ShinKu#43..#50`, `#61`, `#62` | 2026-11-26/27 | `Harrys-HQ` |
| — | `Miyorare#1057`, `#1058` | 2026-11-27 | `Noirero` |
| — | `hyoukan#104` | 2026-11-27 | `PineappleTwilight` |
| — | `ifritraen/kisara#…` | 2026-11-27 | mantenedor |

Cerrar un hilo donde alguien contestó sería tirar su trabajo. Esos se quedan y se responden.

## 6 · Los 66 recientes

Sin respuesta, pero por debajo de 180 días. Son la mayoría de la oleada del 26 y 27 de noviembre.
**Se quedan**: son peticiones vivas y el plazo para juzgarlas no ha llegado. En la revisión del
**2027-05-26** entrarán en el criterio solas, sin que haya que acordarse de nada.

## 7 · Cómo se ejecuta, y con qué token

`tools/retirar_issues.py` lee el JSON de este corte y cierra **solo** los que están en su lista
blanca, comprobando antes el estado real de cada uno. Es idempotente: si ya está cerrado, lo dice y
no hace nada.

```bash
python3 tools/retirar_issues.py --simular   # dice qué haría, no escribe
python3 tools/retirar_issues.py             # cierra los 11
```

**Requisito medido:** el token *fine-grained* de la cuenta **no puede** cerrar issues en repositorios
de terceros — lo comprobé hoy sobre `komikku#1311` y devuelve `HTTP 403 · Resource not accessible by
personal access token`. Para ejecutar la retirada hace falta un token **clásico con `public_repo`**.
Sin él, la lista queda preparada y el pendiente sigue abierto, dicho como lo que es.
