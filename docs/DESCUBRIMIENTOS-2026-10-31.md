# DESCUBRIMIENTOS · 31 de octubre de 2026

Jornada de exploración sobre dos fuentes nuevas y una lista curada ajena. Todo lo que sigue está
medido hoy contra la API oficial de GitHub, con el payload guardado y sellado en
`registry/_evidencia/`. Lo que no se pudo medir está dicho como tal.

## 1. Los dos repositorios que trajo el dueño

| Repositorio | ★ | Creado | Último push | Licencia | Lectura |
|---|---|---|---|---|---|
| `krishna3163/OmniShizuku` | 10 | 2026-10-24 | **2026-10-31** | **Apache-2.0** (LICENSE verificado) | Utilidad Android para flujos de **Shizuku, ADB y Dhizuku**; cubre teléfono, **Android TV** y **Wear OS**; Kotlin; release `latest` del 25-oct con APK de manager y de app; README en siete idiomas incluido **español** (`README.es.md`) |
| `krishna3163/best_shizuku_apps_for_android_no_root` | 158 | 2025-11-07 | **2026-10-31** | **sin LICENSE**, pero el texto del README declara **CC BY-SA 3.0** → método `texto-license` | Lista curada: apps Shizuku, ADB inalámbrico, debloat, privacidad y alternativas a root; 1.273 repositorios citados; sitio en GitHub Pages; README de 386 KB con categorías y catálogos por canal |

**Valor para La Bandita.** `OmniShizuku` es un recurso nuevo y vivo que encaja de lleno en las
piezas 33 (Dhizuku), 90 (Shizuku) y 25 (herramientas con Shizuku); su licencia es verificable y su
actividad es de hoy. La lista curada es otra cosa: **no es un recurso, es un yacimiento**. Se usa
como fuente de descubrimiento, jamás como autoridad — su propio README advierte que es una
recopilación de terceros, y 42 de sus enlaces están muertos (ver §3).

**Nota de método sobre su licencia:** el endpoint `/license` devuelve 404 (no hay archivo de
licencia), pero el README declara CC BY-SA 3.0. La casa registra eso como `texto-license`, no como
ausencia: la declaración del dueño en su propia casa cuenta. Lo que **no** se hace es inventar que
la recopilación es de dominio público.

## 2. Lo que produjo el descubrimiento

| Medida | Valor |
|---|---|
| Repositorios distintos citados en la lista | 1.273 |
| Ya estaban en el registro de la casa | 64 |
| Nuevos, medidos hoy | **1.123** |
| Enlaces muertos (404 al medir) | **42** (3,3 % de lo citado) |
| Fichas totales del registro tras la jornada | **6.826** (5.682 del censo + 1.144 medidas hoy) |
| Vivos entre los nuevos | 1.046 de 1.123 (93,1 %) |
| Sin licencia declarada entre los nuevos | 234 (20,8 %) |

Lo primero que enseña el número: la lista ajena es **más ancha** que el censo de la casa en este
rincón del ecosistema. 64 repositorios que la lista cita ya estaban medidos por La Bandita —señal de
que el censo no iba mal encaminado—, pero 1.142 no lo estaban. Un censo propio de 5.682 fichas
seguía teniendo un hueco de más de mil repositorios en su propio terreno.

## 3. Los 42 enlaces muertos, con nombre

`717998477/bunnylock-private` · `jpruful/REDMAGIC_Mini_Window` · `muhib-karim/s23-optimizer` ·
`parvez-devs/DATACLIAR` · `pwnedbygary/scrcpy-terminal` · `thtuan612/Patch-Font-Where-Winds-Meet` ·
`tim1540/kengen` · `arttvad9r/TypedDroid` … y 34 más (lista completa en
`registry/_pulso-2026-10-31.json`, campo `errores_detalle`).

No es un defecto de la lista: es lo que le pasa a toda recopilación que no mide. **Un enlace citado
no es un recurso vivo** — y esa es exactamente la diferencia que La Bandita vende.

## 4. Hallazgos que valen una pieza editorial

- **Shizuku sigue siendo el eje del ecosistema sin root.** Entre los nuevos medidos aparecen
  `thedjchi/Shizuku` (★6.642, Apache-2.0) y `iamr0s/Dhizuku` (★4.066, GPL-3.0) — ambos ya
  protagonistas de piezas de la serie, ahora con ficha y evidencia sellada.
- **Tiendas de app siguen vivas y creciendo:** `komi-store/komi-store` (★20.171, Apache-2.0),
  `DUpdateSystem/UpgradeAll` (★1.358). Komi Store es la que la pieza 01 cuenta que cambió de casa;
  su repo actual está vivo y con licencia.
- **Privacidad y utilidades concentran la lista:** 455 de los 1.209 nuevos cayeron en
  «Privacy & Utility Picks» y 419 en «Featured Top Builds». Es la misma demanda que la propuesta
  identifica como comprador B2C.
- **Parcheo sin root con tracción real:** `MorpheApp/morphe-patches` (★4.470), `crimera/piko`
  (★5.862), `JingMatrix/LSPatch` (★4.289). Es la familia de la pieza 17.

## 5. Procedencia inmutable: lo que sí se consiguió

De los 60 repositorios más citados medidos hoy, **32 quedaron con SWHID** —revisión archivada en
Software Heritage, citable aunque GitHub desaparezca— y **28 quedaron sin archivo**, por cuota
anónima del propio archivo (HTTP 429) o porque la revisión aún no está indexada; ninguna por falta de
existencia. El estado se guarda en cada ficha (`procedencia.swh_estado`), incluido el fracaso: no se
maquilla. La solicitud de archivo, cuando se aceptó, también queda anotada con su identificador.

**Scorecard:** la API pública respondió **404 en los 60**, y también en repos grandes consultados a
mano (`ollama/ollama`, `SagerNet/sing-box`). Conclusión honesta: la API funciona —un repo de
referencia devolvió 200 con 14 chequeos— pero **su cobertura es parcial**, así que no puede sustituir
a ★ de forma general todavía. Queda como señal secundaria cuando existe.

## 6. Lo que NO se concluye

- Que los 1.142 repos nuevos «sean mejores» que los del censo: están medidos con la misma vara, y
  punto. La lista que los citaba no es evidencia de calidad.
- Que el hueco esté cerrado: la lista es de un solo autor y una sola temática. Habrá más.
- Que la procedencia esté completa: 32 de 60. El resto queda declarado como pendiente y con su
  motivo.

---

*Medido el sábado 31 de octubre de 2026, hora de Santo Domingo. Cada ficha de esta jornada guarda el
payload que la sostiene.*
