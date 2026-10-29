# Mapa de la Biblioteca — proyecto 50–80 publicaciones (2026-09-15)

**Orden del dueño (martes 15-sep):** «sustraer y organizar, además de actualizar, dividir y corregir información según el tratado» sobre la PUBLICACION_COMPLETA_BANDITA_V25 — «esta vaina que hice antes y salió muy mal» — hacia una biblioteca de «unas 50 o máximo 80 publicaciones. Cada una en formato Facebook y WhatsApp», contando las 20 que ya tenemos (00–19, corte 14-sep).

---

## 1. Diagnóstico de la V25 (números contados, no pegados)

- **Qué es:** «Open Sauce de La Bandita · V25 · actualización 016» — enciclopedia acumulada de **1.029 fichas** de recursos, 2,4 MB, 44.234 líneas, corte de datos **2026-09-02** (13 días caducados), con las secciones repetidas capa sobre capa (16 actualizaciones acumuladas sin corte). Por eso no se pudo publicar: ni el límite de texto (FB 40k / WA 63k) ni el lector aguantan un muro así.
- **Integridad:** los 12 hashes del SHA256SUMS.txt del paquete verifican OK (V25 ×4 idiomas + RESUMEN ×4 + README ×4). El tratado madre V.0.03 incluido es byte-idéntico al del corpus.
- **Estados de las 1.029 fichas:**
  - **~82 verificadas** de algún grado (38 «confirmadas por repositorio» + 25 «observadas/activas» + 19 comprobadas 29–30 ago) → material de primera calidad para guías.
  - **940 «Identidad registrada»** = solo nombre + fuente, sin verificación → **candidatas: no fichan** hasta que su fuente se abra y verifique el día que se usen (regla de las URLs; lección III).
  - 1 archivada · 6 sin estado.
- **12 categorías-puerta** (buenas divisiones, se conservan): Música 231 · Android/sistema 197 · Lectura/cómics 181 · Anime/vídeo 162 · Bibliotecas/metadatos 104 · Servidores/self-hosting 74 · Productividad 22 · Desarrollo/red 14 · Privacidad 12 · Extensiones/parsers 11 · Descarga 0 · Referencias/legado 0. (Las dos vacías no generan piezas: se anota.)

## 2. Arquitectura de la biblioteca (75 piezas objetivo, dentro del rango 50–80)

**00–19 — LAS EXISTENTES (20, corte 14-sep):** LA LISTA, tiendas, Kototoro, ADV, extensiones, TMO, forks, Usagi, música FOSS, herramientas, GLTools, AniZen, FMHY, ramas ×4, capa de inmersión, libros, panorama multi. No se reescriben salvo incoherencia (regla del inventario 13-sep).

**20–74 — LAS NUEVAS (55, corte 15-sep en adelante), por puerta:**

| Piezas | Puerta (fichas V25) | Contenido previsto |
|---|---|---|
| **20** | — | «La Biblioteca» — índice maestro del proyecto (esta noche) |
| 21–29 (9) | Música (231) | reproductores locales · streaming YT · podcasts · letras/sincro · audio avanzado · radio · descarga de audio · herramientas · fichas verificadas del V25 |
| 30–37 (8) | Android/sistema (197) | Shizuku · root/Magisk · backup · gestión de archivos · diagnóstico · lanzadores · firewall/red · fichas verificadas |
| 38–45 (8) | Lectura (181) | lectores EPUB/PDF · clientes de cómics · clientes Lemmy/Reddit · lectores RSS · gestión de ebooks · fichas verificadas |
| 46–52 (7) | Anime/vídeo (162) | reproductores de vídeo · clientes anime no-Aniyomi · media center/TV · todo-en-uno (harbor/PlayTorrio) · descubrimiento · fichas verificadas |
| 53–57 (5) | Bibliotecas/metadatos (104) | etiquetado · colecciones · catálogos personales · sincronización de biblioteca |
| 58–61 (4) | Servidores/self-hosting (74) | media servers (Komga/Kavita/Jellyfin…) · nube propia · monitoreo |
| 62–63 (2) | Productividad (22) | notas/concentración · accesibilidad |
| **64** (1) | Privacidad (12) | firewall/DNS/respaldo |
| **65** (1) | Extensiones/parsers (11) | almacenes y repos de fuentes |
| **66** (1) | Desarrollo/red (14) | terminales/SSH/diagnóstico |
| 67–74 (8) | reserva | LA LISTA V2 del corte nuevo · imprevistos · verificados del V25 que merezcan pieza propia |

**Total: 20 existentes + 55 nuevas = 75.** El rango del dueño (50–80) queda servido con margen.

## 3. La vara de filtrado (lo que entra y lo que no)

1. **Ficha V25 pasa a guía solo si su fuente primaria se abre y verifica HOY** (el corte V25 es del 2-sep: caducado por Art. 63 hasta re-verificar).
2. **«Identidad registrada» (940) = radar, no ficha:** puede citarse como nombre contado con la fuente del V25 citada; sin enlace hasta abrir su casa; no entra a guías como [T].
3. **Prohibidos siempre:** recetas de índice (`index.min.json`/`index.pb`), JWT/anon keys, URL de JAR, APK de tiendas de mods, Discord de envío, URL de clon TMO (NO-REPUBLICAR 13-sep + tratado).
4. **Muertos y archivados al Registro, no al mapa** (§5.4.13). La lista es solo de activos.
5. **Voz:** La Bandita / Alexis. Sin narradora ficticia (hecho 13-sep). Piezas limpias, sin meta-comentarios de IA.
6. **Límites:** FB ≤ 40k (estilo de la casa: 8–12k) · WA ≤ 63k, un mensaje. Gemelas byte a byte, verificadas por hash cruzado.
7. **Exploración por puerta (orden del dueño, 15-sep):** LA LISTA no se apega solo al archivo del muro — cada puerta también se explora hacia afuera: nuevos proyectos del nicho, redes de forks, familias que el muro no guardaba. El muro es el punto de partida, no el perímetro. Ejemplo fundador: la familia AxManager (pieza 24).
8. **Cada puerta, su propia vara (aclaración del dueño, 15-sep):** «Sigue así» = adaptarse a cada contexto — NO repetir el mismo método. No se mide a un pez por su capacidad de trepar árboles: cada puerta, y cada nombre dentro de la puerta, recibe la herramienta que su naturaleza pide (búsqueda de repos, catálogo F-Droid, web, la casa raspada). El método sirve al terreno; el terreno no se dobla al método.
9. **Fruto maduro vs. germinantes (orden del dueño, 15-sep):** las puertas se cosechan por el fruto maduro; los proyectos jóvenes (germinantes) se OBSERVAN, nunca se recomiendan para uso diario. Si un germinante tiene lanzamientos reales actualizados y pasa los criterios del tratado, entra al vivero con ficha — «pa' dentro, tal vez» — como observación para futuro. Sin lanzamientos reales: hoja, al radar. El uso diario se recomienda desde los estantes; el futuro se vigila desde el vivero.

## 4. Ritmo de trabajo (regla del inventario del dueño)

«No se reescriben quince piezas de 40k en un turno. Un lote por vez.» → **un lote = una puerta** (1–9 piezas según la categoría), con re-verificación de fuente primaria de cada ficha el día del corte. Lote 1 (hoy, 15-sep): el plan + el inventario extraído + la pieza 20. Siguientes lotes: Música → Android/sistema → Lectura → Anime/vídeo → Bibliotecas → Servidores → las pequeñas.

## 5. Fuente de verdad

- `01-REGISTRO-Y-PROTOCOLO/Inventario V25 — 1.029 fichas (fuente del proyecto).md` — las 1.029 fichas extraídas del master es-DO, por categoría, con su estado V25.
- El master V25 (es-DO) y sus traducciones viven en `uploads/` (fuera del ZIP, por regla del 14-sep); el RESUMEN de enlaces queda como referencia del dueño.
- Cada lote se asienta en el Registro de verificación con su noche y sus hashes.
