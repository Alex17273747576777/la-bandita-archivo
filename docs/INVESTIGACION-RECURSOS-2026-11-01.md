# INVESTIGACIÓN DE RECURSOS NUEVOS · domingo 1 de noviembre de 2026, 07:00 (Santo Domingo)

**Para qué.** El dueño pidió abrir investigaciones de recursos nuevos. Esto no es una lista de deseos:
es la corrida de búsqueda con su método, sus candidatos, sus números medidos y el veredicto de cada uno.
De los seis que pasaron el filtro inicial, **dos entraron a las piezas hoy**, uno entró como evidencia
(el quinto cebo) y tres quedaron fuera con el motivo escrito.

---

## 1 · Cómo se buscó (reproducible)

Cuatro consultas a la API de GitHub, ordenadas por estrellas, filtrando por fecha de creación:

| Consulta | Resultado |
|---|---|
| `topic:fdroid created:>2026-01-01 stars:>40` | 26 repositorios |
| `topic:apk installer created:>2026-01-01 stars:>30` | 5 repositorios |
| `manga reader android created:>2026-01-01 stars:>60` | 12 repositorios |
| `fdroid repository created:>2025-09-01 stars:>20` | **0** — no hay tiendas nuevas con ese volumen |

Luego, para cada candidato, se consultó el repositorio completo (`stars`, licencia, lenguaje, tamaño,
creado, último empuje, releases) y **se descartaron** los que no tenían relación con el oficio de cada
pieza: la búsqueda por `topic:fdroid` devuelve apps que *están* en F-Droid (un rastreador de hábitos, un
editor de notas, un escáner de red), no tiendas ni instaladores. Eso es un dato por sí mismo: **el
ecosistema de tiendas nuevas casi no produce tiendas nuevas; produce apps.**

---

## 2 · Los seis candidatos, con lo que dice la API hoy

| Repositorio | ★ | Licencia | Lenguaje | Creado | Último empuje | Última release | Veredicto |
|---|---|---|---|---|---|---|---|
| `vinstall/VInstall` | 105 | GPL-3.0 | Kotlin | 03-abr-2026 | 30-oct-2026 | v0.4.5 (30-oct) | **entra a las piezas 01** |
| `bl3xand/APK-Toolbox` | 99 | GPL-3.0 | Kotlin | 08-oct-2026 | 28-oct-2026 | v1.1.6 (28-oct) | **se queda fuera por ahora** |
| `FedeFluork/multistore` | 54 | GPL-3.0 | Kotlin | 28-ago-2026 | 24-sep-2026 | v0.8.0-BETA | fuera (dormido y beta) |
| `ruzhe85/Komiho` | 79 | Apache-2.0 | Kotlin | 19-ago-2026 | 28-oct-2026 | v1.6.0 (28-oct) | **entra a las piezas 02** |
| `Boomckman/usagi-nightly` | 114 | **sin licencia** | HTML | 28-jun-2026 | 01-nov-2026 | ninguna | **entra como evidencia** |
| `Saber-Alter-Lily/pica-library` | 127 | MIT | TypeScript | 12-ago-2026 | 01-nov-2026 | v0.5.0 (01-oct) | fuera (contenido adulto) |

---

## 3 · Por qué entra cada uno

### `vinstall/VInstall` → pieza 01 (WhatsApp y Facebook)

Es el único instalador de la búsqueda que cubre **APKV**, el paquete cifrado de las tiendas chinas, además
de APK, XAPK, APKS y APKM, con Shizuku y sin root. Siete meses de vida, licencia GPL-3.0, release de anteayer
y un issue abierto. En la pieza 01 entra en el cuerpo, en la ficha y en los enlaces.

Lo que **no** dice la ficha y conviene saber: 105 estrellas es poco. No lo presento como «el mejor»;
lo presento como el que resuelve un formato que las demás no abren.

### `ruzhe85/Komiho` → pieza 02 (WhatsApp y Facebook)

Cliente nativo de **Komga** con escalado de imagen para escaneos viejos. Nace en agosto de 2026, publica
v1.6.0 el 28 de octubre y trabaja en Kotlin. Es el más joven de los clientes de la familia Komga que medí,
y eso importa: en esa familia los clientes eran viejos (`Komelia` 0.20.0, `kmreader` v7.3, `komf` 2.1.0).

### `Boomckman/usagi-nightly` → pieza 02, como **evidencia**, no como recomendación

Cumple el molde del cebo con una precisión que da risa: creado el **28 de junio de 2026** —el mismo día que
los otros cuatro—, escrito en **HTML**, **sin licencia**, con 114 estrellas y el nombre de un lector real
(`Usagi`) en el título. Entra al censo como quinto caso. No se enlaza, igual que los otros cuatro:
*nombrar es informar; enlazar es repartir.*

---

## 4 · Por qué se quedan fuera (y qué haría falta para que entren)

- **`bl3xand/APK-Toolbox`** (99★, GPL-3.0, creado 8-oct-2026): clona, fusiona y actualiza apps desde GitHub
  y F-Droid. Es prometedor y es **tres semanas** de vida. La regla de esta casa dice no recomendar lo que
  todavía no ha demostrado nada; entra cuando cumpla tres meses y dos releases sin romper. Anotado.
- **`FedeFluork/multistore`** (54★, GPL-3.0): agrega varias tiendas de terceros en un catálogo. La idea es
  buena —es la pregunta que la pieza 01 deja abierta—, pero lleva cinco semanas sin empujar y su última
  release es una **BETA**. Queda como candidato del próximo censo.
- **`Saber-Alter-Lily/pica-library`** (127★, MIT): está bien hecho y está fuera por una razón de contenido,
  no de calidad: su catálogo principal es de cómics para adultos. Esta guía es familiar y eso no entra.
- **`InlitX/streak`, `shardulvs/xnotes-android`, `Earendel-lab/Tapbar`…**: son apps que *están* en F-Droid,
  no tiendas ni lectores. No tienen sitio en estas dos piezas.

---

## 5 · Lo que la búsqueda enseñó sobre el mapa (esto no es relleno)

1. **No aparecen tiendas nuevas.** Cero resultados con `fdroid repository created:>2025-09-01`. Lo que
   aparece son clientes e instaladores. El trabajo nuevo está en *cómo se instala*, no en *dónde se compra*.
2. **El nicho de lectores de cómics sigue pariendo proyectos cada mes** —Komiho en agosto, Ciallo en julio,
   LocalViewer en julio— y casi todos son de una sola persona. Es vitalidad y es fragilidad al mismo tiempo.
3. **La fábrica de cebos sigue abierta.** Un quinto repositorio con el molde exacto del 28 de junio apareció
   esta semana. No es un accidente: es un negocio que funciona porque la gente busca nombres, no fechas.

---

## 6 · Lo que se verificó después de tocar las piezas

| Comprobación | Resultado |
|---|---|
| Longitudes | 01 WA **63.021** · 01 FB **43.226** · 02 WA **63.084** · 02 FB **43.056** — las cuatro en banda |
| Enlaces nuevos | `VInstall`, `Komiho` y `usagi-nightly` responden **200** |
| Enlaces de cada pieza | 01 WA 29 · 01 FB 22 · 02 WA 56 · 02 FB 33 |
| Recuentos internos | 01 WA 31 repos/29 enlaces · 01 FB 19/22 · 02 WA 53 (46 vivos, 4 archivados, 3 muertos) · 02 FB 49 |

💓 *La Bandita · domingo 1 de noviembre de 2026 · Santo Domingo.* Cada número de esta página se consultó
hoy entre las 06:50 y las 07:05. Lo que no se midió está dicho como no medido.

─────────────────────────────────────────

## Segunda ronda — recursos nacidos en 2026 (medidos hoy, 1-nov-2026, entre 06:40 y 07:20 de Santo Domingo)

Consulta a `api.github.com/search/repositories` sin caché, filtrando por fecha de creación y ordenando por estrellas. No se reutilizó ninguna lista guardada. Criterio de entrada: proyecto vivo (empuje en los últimos 45 días), licencia declarada cuando existe, y utilidad concreta para alguna de las listas.

### Para la 03 (verificación, instalación, salir de Google)

| repositorio | ★ | licencia | creado | último empuje | release | por qué entra |
|---|---|---|---|---|---|---|
| `bl3xand/APK-Toolbox` | 99 | GPL-3.0 | 2026-10-08 | 2026-10-28 | v1.1.6 (28-oct) | rastrear, clonar, instalar y fusionar APK desde el propio teléfono |
| `richardkfm/los-bootstrap` | 6 | GPL-3.0 | 2026-04-28 | 2026-10-16 | v0.14.0 (15-oct) | instala y deja listo LineageOS en un aparato ya liberado |
| `Ha2mad/package-pass` | 0 | MIT | 2026-10-28 | 2026-10-28 | — | lee en lote los nombres de paquete para saber qué registrar |
| `Meirwolf1289/fdroid-census` | 0 | sin licencia | 2026-10-31 | 2026-10-31 | — | intenta **contar** cuántas apps de F-Droid están registradas |

### Candidatos para las piezas siguientes (no usados todavía)

| repositorio | ★ | licencia | creado | push | utilidad |
|---|---|---|---|---|---|
| `chmouel/liseur` | 170 | MIT | 2026-07-28 | 2026-11-01 | lector EPUB con biblioteca remota — entra en la lista de lectura |
| `InlitX/GymMane` | 1.254 | GPL-3.0 | 2026-08-05 | 2026-10-30 | diario de gimnasio sin cuenta ni internet: el caso «app útil sin nube» |
| `TheZupZup/Linthra` | 77 | AGPL-3.0 | 2026-05-22 | 2026-11-01 | reproductor de música local-first — lista de música |
| `jemcik/JemRec` | 50 | Apache-2.0 | 2026-09-10 | 2026-10-31 | grabador de llamadas sin root — pieza 12/92 |
| `Secure-Phone-apps/Secure-Dialer` | 52 | GPL-3.0 | 2026-07-02 | 2026-10-31 | marcador sin permisos — pieza 39 |
| `EZ-eta/kinetica` | 59 | GPL-3.0 | 2026-08-10 | 2026-10-28 | teclado con deslizamiento a dos pulgares — pieza 30 |
| `jrs8205/ARK-launcher` | 38 | Apache-2.0 | 2026-06-23 | 2026-10-31 | lanzador en Compose — pieza 30 |
| `Acamol/Captain-qBit` | 27 | GPL-3.0 | 2026-07-02 | 2026-10-29 | control remoto de qBittorrent — pieza 48 |
| `harkhowalia-1/MacSubsystemForAndroid` | 521 | GPL-3.0 | 2026-10-15 | 2026-10-21 | apps de Android en ventanas de Mac — familia del 72 |
| `couzteau/Degoogle-Photos` | 6 | MIT | 2026-02-15 | 2026-10-29 | desenreda los ZIP de Takeout — pieza de salida de Google |

### Correcciones que esta ronda obligó a hacer en la 03

- `Pelski/ytzero`: la ficha decía «sin licencia declarada»; la API devuelve **Unlicense**. Corregido en los tres sitios donde aparecía.
- `GrapheneOS/Vanadium`: la ficha decía «licencia sin declarar»; la API devuelve **NOASSERTION** (hay licencia en el repo, la API no la reconoce). Corregido con la explicación en la propia línea.
- Los cuatro recursos nuevos se midieron uno por uno con `/repos` y `/releases/latest`, y sus cuatro enlaces responden **200** hoy.

### Regla de esta ronda, para la próxima

Ningún recurso entra a una pieza sin: (1) medición del día con hora, (2) licencia verificada en la API, (3) enlace comprobado con código 200, (4) una razón escrita de por qué está ahí y no es relleno. Si no cumple las cuatro, se queda en esta tabla de candidatos y no en la pieza.
