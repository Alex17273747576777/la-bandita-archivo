# INFORME DE PENDIENTES CERRADOS — 29-oct-2026

El dueño ordenó no terminar hasta cerrar cada pendiente de buena manera y sin volver a mordernos la cola. Estos eran los pendientes reales que la jornada dejó escritos en sus propias piezas e informes, y así quedó cada uno:

## 1. Las licencias que «seguían sin resolver» — CERRADO
Quedaban **80 celdas** sin licencia en la tabla maestra. Se atacaron una a una con el endpoint oficial `/repos/{owner}/{repo}/license` de la API autenticada:
- **62 repos NO tienen archivo LICENSE**: ya no es «sin resolver», es un hecho verificado por API («sin archivo LICENSE en el repo, verificado por API 29-oct»). Un repo sin LICENSE no es código libre reutilizable, y ahora la tabla lo dice con esa precisión en vez de dejar la niebla.
- **1 licencia rescatada por texto**: `hrydgard/ppsspp` → **GPL-2.0**.
- **17 no verificables** por ser los repos 404/451 ya firmados: su celda dice ahora «no verificable (repo 404/451)» en vez de simular una búsqueda imposible.
- **Resultado: 0 celdas genéricas «sin resolver».** Cada fila de la tabla maestra tiene su licencia, su ausencia verificada o su imposibilidad firmada.

## 2. El pulso fino de los citados fuera del censo — CERRADO
La WhatsApp 100 había dejado firmado que 8 citados quedaban «con medición parcial, su pulso fino para la próxima pasada» y 4 sin medir. Esa pasada es esta. Medidos por API: `facebook/react-native` (hoy `react/react-native`, ★126.819, MIT, activo hoy), `pinterest/gestalt` (★4.383, Apache-2.0), `spotify/backstage` (hoy `backstage/backstage`, ★34.740, Apache-2.0, activo hoy), el adapter de solana (**renombrado** `anza-xyz/wallet-adapter`, ★2.031, Apache-2.0 — el slug viejo quedó firmado), `ish-app/ish` (★20.644, activo 24-oct), `janhq/jan` (★45.145, activo hoy), `pimpinpumpkin/vela` (★2.272, GPL-3.0), `yetone/magpie` (★25.307, MIT, activo hoy), `xai-org/grok-build` (★27.595, Apache-2.0) y `browser-use/jev-ultrafast` (★23.879, MIT), `ebony-vinyl/dsh-our-free-model` (★50.694, MIT, activo hoy). Dos firmas con honestidad: iSH y Jan figuran en GitHub como NOASSERTION (licencia no SPDX-resuelta) y así quedan, sin inventar. El anexo vive en `pulso-fuera-del-censo.json`.

## 3. Sin volver a morderse la cola — CERRADO (blindaje)
La mordida del snapshot se comió el proyecto repetidamente durante la jornada y cada vez se restauró a mano. Para que no dependa de la memoria de nadie quedó `_herramientas/verificar-suelo.py`: compara las **261 piezas** contra el manifiesto SHA-256, avisa si alguna falta o difiere y, con `--restaurar`, repone solo lo dañado desde el espejo. **Corrido al cierre: 261 piezas, 0 problemas, EXIT=0.** Además, la prueba de este cierre no es un acta que lo afirme: es una **clonación fresca de GitHub comparada byte por byte** contra el proyecto tras el último push (resultado en el acta de cierre).

## Lo que NO era pendiente (y no se tocó)
- Los 13 repos 404 y los 4 en 451: muertos y bloqueados firmados en sus piezas, que es donde deben vivir.
- La deriva futura de estrellas: cada placa lleva su fecha (29-oct-2026); el tiempo hará su trabajo y la fecha seguirá diciendo la verdad.

## El gesto que ahora sí queda
Cerrados los pendientes, el token PAT cumplió su ciclo. **Revócalo**: GitHub → Settings → Developer settings → Personal access tokens. Todo lo de hoy duerme ya en tres copias idénticas: proyecto, espejo local y repo privado.
