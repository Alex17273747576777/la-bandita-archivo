# Auditoría del volcado 2026-09-13 (publicaciones FB/WA + anexos)
### Verificación hecha en el workspace canónico el 2026-09-13 · Método: conteo real de caracteres + grep de patrones + diff contra corpus

**Origen:** sesión externa del 13-sep que preparó 12 publicaciones en doble versión (Facebook-40k y WhatsApp) siguiendo el Handoff y los perfiles §5.2. Este volcado llegó completo con su propio control de calidad (00-INVENTARIO, NO-REPUBLICAR, LEEME-publicaciones).

## 1. Cumplimiento de límites de perfil (§5.2)

| Pub | Facebook (máx 40k) | WhatsApp (máx 63k) |
|---|---|---|
| 01 Tiendas APK | 37.684 ✓ | 61.931 ✓ |
| 02 Kototoro | 36.566 ✓ | 62.949 ✓ |
| 03 ADV | 37.709 ✓ | **64.059 — EXCEDE (63k) ⚠️** |
| 04 Extensiones | **41.233 — EXCEDE (40k) ⚠️** | 62.892 ✓ |
| 05–12 | 4.4k–32.6k ✓ | 4.7k–31.5k ✓ |

**Veredicto:** 22 de 24 cumplen. **Pendiente de decisión de Alexis (no se edita sin él):** 04-Facebook necesita recorte o división en partes numeradas; 03-WhatsApp está 1.059 caracteres por encima — recorte mínimo o remisión a Facebook. Regla aplicable: §5.2 («si no cabe: partes numeradas o remisión»), sin inflar (C05) y sin perder enlaces (regla transversal).

## 2. Patrones prohibidos (NO-REPUBLICAR): CUMPLE

El grep halló menciones de `index.min.json` / `index.pb` / `anon key` en 7 publicaciones (02, 04, 05, 06, 07, 12). **Contexto verificado: son menciones de cumplimiento, no recetas pegadas.** La 04 dice: «son precisamente el gancho de instalación. **No se pegan.**»; documenta GETs verificados con fecha («respondió 200», 13-sep 17:38 UTC); la 06 lista los patrones prohibidos como checklist. Veredicto: **limpias.**

## 3. Fusión con el corpus canónico (hecha)

- **Manual:** se fusionaron sus §8 (Carta como ejemplo) y §8.1 (textos personales, sin PII) — rutas adaptadas al workspace. El nuestro conservaba el bloque «ancestro 1789» que el suyo no tenía; el suyo traía §8/§8.1 que el nuestro no tenía. Unión sin pérdida. Manual: 646 líneas.
- **Lecciones de Alexis:** se fusionó la entrada **2026-09-13 (III)** — «No se puede guiar a otros por un camino que uno mismo no ha recorrido» (de la Carta v9). Registro: 4 entradas fechadas.
- **Nuevos archivos del corpus:** `Carta a La Bandita — Regreso a la Confianza (ejemplo).md` · `Lecciones extraidas de textos personales (archivo, no norma).md` · carpeta `Publicaciones 2026-09-13/` (24 posts + INVENTARIO + NO-REPUBLICAR + LEEME-publicaciones).
- **Dossier AniZen:** idéntico byte a byte en ambas versiones — sin conflicto.
- Codificación de todo lo fusionado: LIMPIA (sin glifos corruptos).

## 4. Lo que el volcado aporta de doctrina (ya integrado, no nuevo en tratado)

- NO-REPUBLICAR: el Art. 63 operando como lista de corte («historia fechada, no vigente»).
- Las publicaciones aplican §5.2, Art. 205 (GETs fechados), Art. 246 (parentaje declarado), C05/G-002 («no se rellenaron con agua»).
- La Carta v9: P02 en voz humana; «el verbatim, cuando llegue, desplaza al [P]» — honestidad de archivo ejemplar.

*Auditoría V1.0 — 2026-09-13. Las dos excedencias quedan como pendientes fechados con responsable: Alexis decide recorte o división.*

---

## Corrección del 2026-09-14 — las dos excedencias, resueltas por división (§5.2)

**Decisión de Alexis:** «complétalo según el tratado mismo». Método aplicado: §5.2 — «si el contenido no cabe... se divide en partes numeradas»; se descartó el recorte porque las piezas son densas en datos y enlaces (C05 prohíbe inflar; la regla transversal prohíbe perder enlaces; recortar a ciegas está prohibido por la propia §5.2).

| Pieza | Antes | Después |
|---|---|---|
| 04-Extensiones-Facebook (41.233 > 40.000) | 1 archivo excedente | **2 partes**: P1 = 20.688 ✓ · P2 = 20.745 ✓ |
| 03-ADV-WhatsApp (64.059 > 63.000) | 1 archivo excedente | **2 partes**: P1 = 32.315 ✓ · P2 = 31.944 ✓ |

**Verificación:** contenido íntegro en ambas divisiones (byte-idéntico salvo el espacio en blanco de la costura — normalizado y verificado); enlaces preserved 32/32 y 9/9; codificación limpia. Los originales quedan respaldados fuera del paquete: `backup-previo-correccion-14-09/`. Cada parte abre con una nota editorial (»Parte X de 2«) que Alexis puede ajustar al firmar (§5.1 paso 7). Estado: **BORRADORES listos — siguen pendientes de lectura y firma humana.**
