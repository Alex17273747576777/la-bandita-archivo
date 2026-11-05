# Acta · el catálogo por recurso (5-nov-2026, 11:30–11:55 UTC)

**Qué se crea.** `catalogo/`, con una ficha por recurso en lugar de una lista. **279 fichas medidas** en
**9 racimos**, de las cuales **23 ya tienen guía escrita a mano** —el racimo completo de Shizuku y sus
herederos— y 256 están medidas esperando su guía.

**Decisión del dueño.** Las dos opciones a la vez: (1) todo dentro de `la-bandita-archivo`, sin crear
cientos de repositorios, para que el catálogo se clone una vez y se valide con un linter; (2) empezar por
los dos racimos pedidos: el banco de prueba de Shizuku y los recursos de las piezas 12–20.

**Máquina nueva, en `tools/`.** `catalogo_medir.py` (mide y guarda evidencia con fecha), `catalogo_ficha.py`
(escribe fichas y índice, preservando la guía escrita entre marcadores), `catalogo_sync.py` (compara con
GitHub, escribe `SINCRONIA.json` y `CREDITOS.md`, y con `--actualizar` refresca medición y fichas sin tocar
las guías) y `catalogo_lint.py` (12 comprobaciones, código de salida 1 si falla).

**Racimos.** `shizuku-y-herederos` (23) · `reemplazo-del-stack` (52) · `audio` (52) · `clientes-de-musica`
(37) · `descargas` (31) · `torrentes` (3) · `teclados-y-dictado` (34) · `radio-y-directo` (32) ·
`tiendas-de-extensiones` (25) · `teclados-con-ia` (11).

**Hallazgos del racimo de Shizuku.** (1) **Shizuku**, el original, tiene ★32.840 pero su último empujón
es del 18-jun-2025 y su última entrega v13.6.0 del 25-may-2025: el catálogo lo marca «lento», no «vivo».
(2) Tres herederos publican más recientemente: **Stellar** (v1.1, ago-2026), **ShizukuPlus**
(v13.6.0.r2551, sep-2026) y **Shizuku-Next** (v14.0.33-next, **hoy mismo**). (3) **Riru** está archivado
desde 2022 y **InstallerX** desde 2023, y los dos tienen heredero vivo: Zygisk y `InstallerX-Revived`
(★7.327, más estrellas que el padre). (4) **UAD** (★20.338) lleva parado desde ago-2024 sin estar
archivado —el peor estado posible— y su heredero `universal-android-debloater-next-generation` (★9.751)
entregó el 2-nov-2026. (5) `timschneeb/awesome-shizuku` (★10.708) es la lista de referencia del tema: se
le reconoce el trabajo y se le señala lo único que no hace, que es fechar cada entrada.

**Lo que el linter encontró en mi propio trabajo.** 54 fallos en la primera pasada: **49 por una frase
plantilla repetida** en las fichas sin guía, 3 por fichas de repositorios que no existen —tres nombres que
yo había supuesto y que no están en GitHub: se borraron en vez de disimularlos— y 2 por superlativos que
venían de citas del autor, no de mi prosa (se eximen las citas). Segunda pasada: **0 fallos**.

**Compuertas.** `catalogo_lint` 0 fallos · `manual_gate` y `novedad_gate` sin cambios en las piezas ·
`make ritual` sella los ficheros nuevos · `make compuertas` y `autoprueba` antes del push.

**Registros.** **E46** → **H27** («un catálogo se mide por recurso, no se copia por lista»).
