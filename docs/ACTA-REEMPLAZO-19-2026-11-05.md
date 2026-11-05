# Acta · reemplazo de raíz de la pieza 19 (5-nov-2026)

**Qué se reemplaza.** `19-Las-tiendas-de-extensiones-con-el-liston-arriba-…` (42.687 caracteres, publicada esta
mañana a las 09:49) pasa a `_reemplazadas/` y su lugar lo ocupa `19-La-tienda-que-le-sirve-a-tu-app-…`
(43.656 caracteres). No es una corrección de erratas: es la reescritura que pide el dueño en su segunda
crítica del día.

**Por qué.** La primera versión contaba 5.481 extensiones en seis índices. Contar no es comprobar. El
dueño pidió subir el listón otra vez: usar la app primero, clonar el repositorio y probarlo, no indexar
repositorios aleatorios, y agrupar las apps por tienda compatible.

**Qué se hizo distinto.**

1. **Herramienta nueva:** `tools/auditar_tienda.py` clona el repositorio, abre `repo.json`, lee el catálogo
   como lo lee la aplicación, cuenta entradas, comprueba la firma, pide un byte de una descarga real
   (`Range: bytes=0-0`) y devuelve veredicto con motivos.
2. **Quince repositorios clonados** entre las 10:03 y las 10:15 UTC, con ficha en
   `docs/AUDITORIA-TIENDAS-2026-11-05.json`.
3. **Ocho tiendas indexadas y siete fuera con nombre y motivo**, frente a las veinte de la versión anterior.
4. **Tabla apps ↔ tienda** con entradas, firma, descarga y veredicto: la sección que el dueño pedía.

**Hallazgos que la versión anterior no tenía.**

- **Cuatro lápidas dentro de cuatro catálogos.** El `index.min.json` de Keiyoushi tiene **2 entradas** y una se
  llama «Outdated App»; el de Yūzōnō para Mihon tiene 2 y su `index.json` declara «Please migrate to
  Keiyoushi»; el de Secozzi pide «Animiru 0.20+». Quien cuenta ese archivo cuenta tiendas cerradas.
- **`mochi-plugins/repository` (49★) está vacío:** solo `LICENSE` y `README.md`, cero complementos. Es el
  repositorio que más se repite cuando alguien pregunta por Usagi.
- **`dragonx943/manga-repo` es código, no tienda:** ocho ramas de trabajo, ni un `index.json`.
- **El MegaRepo de Cloudstream no es una lista:** es un plugin (`MegaProvider`) que añade los demás
  repositorios desde dentro de la app.
- **`quickdesh/Animiru` responde 301** → `animiruorg/Animiru` (907★, v0.20.1.1 del 3-nov).
- **Secozzi son tres extensiones** y su propio índice se llama «Jellyfin, Stremio, and Torbox».

**Compuertas.** `manual_gate` **VERDE** (43.656 car., banda 40.000–45.000) · `novedad_gate` VERDE ·
solape contra la 18 medido · `envio.py` 0 fallos · `make compuertas` y `autoprueba` en verde antes del push.

**Registros.** **E44** (contar `index.min.json` como si fuera el catálogo) → **H25** («una tienda se abre, no
se cita»). La **E43/H24** de la versión anterior se conserva: la lección de que una wiki no es una medición
sigue siendo cierta, y esta pieza es el paso siguiente.
