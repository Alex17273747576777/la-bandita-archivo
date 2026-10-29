# INFORME — CORRECCIÓN FINAL SIN MAQUILLAJE (29-oct-2026)

Lo que estaba mal, encontrado midiéndolo, y su corrección con la misma medición después.

## 1. Las notas 💓 que faltaban (el fallo grave)
La reparación de quices del pase anterior truncó **41 piezas de WhatsApp (43–80, 82–84)**:
su zona de respuestas no usa el marcador de soluciones y el script se llevó todo lo que
había tras el quiz, incluida la nota `💓 PULSO 29-OCT-2026`. La vara no miraba la nota en
WhatsApp y por eso «pasó». Corrección: nota restaurada en las 41 desde el árbol del commit
`43aa6e5` (solo la nota firmada; el bloque duplicado sin firmar que la precedía no volvió).
La vara del catálogo y su réplica offline ahora exigen 💓 también en WhatsApp.
**Después: WhatsApp 111/111 con su nota.**

## 2. Duplicados pegados a la nota
24 piezas WA traían bloques del pulso repetidos antes de la nota y dentro de ella.
Retirados **190 bloques** previos a la nota que duplicaban a la propia nota; queda una
repetición revisada a mano (término de glosario repetido en dos listas de la WA 84), que
se conserva porque cada lista lo cita como término, no como dato.

## 3. «Licencias sin resolver hoy» — era mentira por arrastre
**89 frases** (31 WA + 57 FB, con duplicados ya retirados) seguían diciendo «sin resolver»
cuando el dataset del día ya las había resuelto. Sustituidas por el estado real, repo por
repo: SPDX donde lo hay, «sin archivo LICENSE en su repo (verificado por API)» donde no lo
hay, y «presente, no clasificada como SPDX» donde GitHub no clasifica. Dos se resolvieron
a mano hoy: `seedvault-app/seedvault` (Apache-2.0 por su LICENSE en master) y
`naman14/timber` (sin archivo LICENSE en su repo). **Después: 0 frases «sin resolver».**
(La WA 103 nombraba 8 de 9; el noveno nunca fue nombrado en ninguna fuente: se listan los 8.)

## 4. El catálogo mentía en la vitrina
- **Orden lexicográfico**: tras la 09 venía la 100. Ahora orden numérico real (00→108, 00→131);
  Anterior/Siguiente y «las últimas seis» ya son las 103–108.
- **Títulos de vitrina**: Facebook mostraba el nombre del archivo cortado a 40 caracteres y
  WhatsApp tenía 25 piezas sin título y varias con la línea de fecha por título. Ahora el
  título se lee del texto de cada pieza: **0 sin título, 0 con nombre de archivo**.
- **Textos caducos de la carcasa**: «corte 15-oct-2026» → 29-oct-2026; «cps=len en las 23
  piezas» → el conteo real y dinámico; fuera la insignia «censo 15-oct» y la línea
  «batería 24/24 · 30/30 · fuzz 60/60» que nadie había medido en esta copia; la frase del
  muro «las de era-vieja no van aquí» → descripción exacta de lo que el muro contiene.
- La vara ahora también comprueba los quices de Facebook y `cps=len` del muro:
  **74 quices descifrables (71 WA + 3 FB), fallos NINGUNO**.

## 5. Las varas que medían mal
- `chequeo-niveles.py` prometía un nivel L3 que no existía y daba «L1 lupa OK» porque la
  lupa siempre sale 0 aunque solo imprime medidas. Corregido: L1 **mide y publica cifras**
  (bloques >380/>700 y máximo por serie) y no es puerta; el veredicto solo mira las puertas.
- `guardar.py` y el índice decían «clonación fresca byte por byte»; el script verifica por
  **blobs del árbol remoto** sobre una lista enumerada. La documentación ahora dice eso.

## 6. Papeles caducos
- Los dos `LEEME-de-la-carpeta.md` describían el estado del 15-sep (80 piezas, rutas que ya
  no existen): reescritos al estado del 29-oct-2026 con conteos exactos por carpeta.
- La guía de publicación ahora cuenta la carpeta tal cual es (113 y 148 archivos, con la
  variante histórica y los LEEME nombrados, no escondidos).

## Verificación tras corregir (medida, no afirmada)
- Auditoría objetiva: 0 caracteres de reemplazo, 0 mojibake, 0 «sin resolver», 0 «★—»;
  los únicos caracteres de ancho cero son los ZWJ de los emojis familiares (legítimos).
- Vara simulada: **WA 111 · FB 147 · quices 74 · fallos NINGUNO — APROBADA**.
- Chequeo multinivel: L0 OK · L1 MEDIDA (cifras publicadas) · L2 OK (0 distintos) · L4 OK.
- Sintaxis JavaScript del catálogo comprobada con `node --check`.
