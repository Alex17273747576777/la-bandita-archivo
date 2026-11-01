# CIMIENTOS — criterios obligatorios de éxito y orden de precedencia

**Corte:** 1 de noviembre de 2026 · **Clase:** documento normativo de la casa (no es pieza, no se numera, no entra al ZIP) · **Función:** fusionar los cimientos en una sola lista ejecutable y verificable por máquina.

Este documento no sustituye a nadie: **ata** los documentos de la casa entre sí y convierte sus obligaciones en criterios con número, con dueño y con comprobación automática. Si un criterio de esta lista no se cumple, la pieza **NO** está lista, diga lo que diga cualquier informe anterior.

---

## 1. Los cimientos, con su rango

| # | Documento | Ruta | Rango | Qué manda |
|---|---|---|---|---|
| 1 | Next Tratado Bandita Open Source V.0.03 (Edición Corregida) | `corpus-la-bandita/Next Tratado Bandita Open Source — Fusión Universal V.0.03 (Edición Corregida).md` | **Norma madre.** Manda sobre todo lo demás. | Principios, deberes, prohibiciones de fondo. |
| 2 | Manual de Campo La Bandita — Edición Completa | `corpus-la-bandita/Manual de Campo La Bandita — Edición Completa.md` | **Manual operativo.** Bajo el Tratado. | Cómo se ejecuta el oficio paso a paso. |
| 3 | Manual de Campo — Fichas de Fallos (Uso Diario) | `corpus-la-bandita/Manual de Campo La Bandita — Fichas de Fallos (Uso Diario).md` | **Libro 2.** Bajo el Tratado. | Taxonomía de fallos (A, B, C, D, F) y severidad. |
| 4 | Lecciones de Alexis — para recordar entre sesiones | `corpus-la-bandita/Lecciones de Alexis — para recordar entre sesiones.md` | **Voz del dueño.** Fuente primaria de doctrina. | Valores, frases textuales fechadas, calibración de tono. |
| 5 | Ampliación al Tratado — las canciones de Almendra (15-sep) | `corpus-la-bandita/Ampliación al Tratado — las canciones de Almendra (15-sep).md` | **Anexo doctrinal.** Bajo el Tratado. | El uso de la canción como llave de lección. |
| 6 | Lecciones extraídas de textos personales | `corpus-la-bandita/Lecciones extraidas de textos personales (archivo, no norma).md` | **Archivo.** NO es norma. | Contexto; nunca obliga. |
| 7 | Lecciones de Alexis y el corazón de la casa | `Arena-Reimagined/HABILIDADES/CORAZON.md` y `INDICE-HABILIDADES.md` | **Carácter operativo.** Bajo el Tratado. | Útil sin relleno, con opinión, honestidad radical, concisión por defecto. |
| 8 | **Manual de Estilo y Operaciones La Bandita — V3.0** | `corpus-la-bandita/Manual de Estilo y Operaciones La Bandita — V3.0 (1-nov-2026).md` | **Norma de forma y verificación.** Subordinado a 1–3 por su propia cabecera; manda sobre la forma de cada pieza. | Molde, voz, fichas, FAQ, enlaces, firma, meme, notas, prohibiciones, checklist. |
| 9 | Reglas operativas vivas del dueño (bandas, series, canal, fecha de la casa) | esta misma lista, §3, y `docs/bandas.json` | **Orden directa del dueño.** Manda sobre cualquier manual cuando el dueño la dio después. | Longitudes, numeración, medición con hora, cero párrafos compartidos. |

**Precedencia, en una línea:** Tratado → Manual de Campo → Libro 2 → Lecciones de Alexis → Manual V3.0 → reglas operativas del dueño. Cuando el dueño da una orden posterior que choca con un manual, **manda el dueño** y se registra la tensión en §3 de este documento.

---

## 2. Criterios obligatorios de éxito (C-01 a C-24)

Cada criterio dice **qué** se exige, **de dónde** viene y **cómo se comprueba**. La comprobación no es retórica: `tools/manual_gate.py` la ejecuta y `tools/vara.py` la vuelve puerta (G11). Una pieza que falle un criterio de severidad **crítica** no se publica.

### Bloque A — Verdad y verificación

**C-01 · Cada dato tiene fuente abierta con fecha.** Origen: Tratado · Manual V3.0 §13. Comprobación: fichas con URL + fecha de corte; enlaces con código HTTP registrado.
**C-02 · Nada de verificación fingida.** Origen: Libro 2 (F05). Comprobación: la pieza no afirma haber abierto lo que no está en el registro del día.
**C-03 · Lo no verificado se declara.** Origen: Manual V3.0 §13.2, §14.3. Comprobación: toda ausencia va escrita como «no comprobado al corte» o «sin URL al corte», con motivo.
**C-04 · Datos contados, no estimados.** Origen: Manual V3.0 §7.4. Comprobación: las cifras de la pieza coinciden con la medición del día (estrella por estrella).
**C-05 · Sin URLs por analogía.** Origen: Libro 2 (A02). Comprobación: todo enlace de la pieza responde en la verificación del día.

### Bloque B — Forma obligatoria de la pieza

**C-06 · Cabecera.** Título descriptivo, número a dos dígitos, fecha de corte en formato largo («1 de noviembre de 2026»). Origen: Manual V3.0 §4.
**C-07 · Mapa de la guía.** Encabezado `🗺️ Mapa de esta guía`, entre **5 y 12** entradas, `├──` y `└──`, emojis por afinidad. Origen: Manual V3.0 §5.
**C-08 · «En una página».** Entre 3 y 5 párrafos que respondan qué es, qué se verificó, qué se aprende y a quién sirve, con el corte declarado. Origen: Manual V3.0 §6.
**C-09 · Fichas completas.** Nombre en negrita, URL completa, estrellas, versión con fecha, push, licencia exacta y descripción citada o su ausencia declarada. Origen: Manual V3.0 §7.
**C-10 · FAQ.** Entre 6 y 12 preguntas reales con respuestas honestas y sin promesas. Origen: Manual V3.0 §8.
**C-11 · Enlaces.** Todos los del cuerpo, con formato `- Nombre: URL`, y ninguno de la lista ausente del cuerpo. Origen: Manual V3.0 §9.
**C-12 · Firma textual.** Exactamente: `La Bandita informa a partir de fuentes fechadas.` Origen: Manual V3.0 §2.7 y §10.
**C-13 · Remate propio.** Una a tres líneas, tras la firma, que solo tenga sentido al final de esa pieza; prohibido repetirlo entre piezas. Origen: Manual V3.0 §10.2.
**C-14 · Meme del corte.** Dos líneas con guion largo, original, antes de la firma, sin humillar ni contradecir la pieza. Origen: Manual V3.0 §3.
**C-15 · Notas al pie.** Fechadas, del tipo declarado (mudanza, verificación final, corrección, pendiente, del corte). Origen: Manual V3.0 §11.

### Bloque C — Prohibiciones

**C-16 · Cero frases prohibidas del §2.6.** «La mejor para todos», «imprescindible», «100% segura», «todo el mundo sabe», «según expertos» sin fuente, «descárgalo ya», «el único que necesitas», «revolucionario», «único en su clase», «sin precedentes», «el futuro es ahora», «game changer».
**C-17 · Cero superlativos absolutos y cero fórmulas de autoridad vacía.** Origen: Libro 2 (A13, B08).
**C-18 · Cero promesas de vigilancia futura.** Origen: Libro 2 (F06).
**C-19 · Cero meta-comentarios del proceso de escritura.** Prohibido «aquí va un dato», «esta sección explica», «en esta pieza voy a». Origen: Manual V3.0 §11.2 y §12.1. **Interpretación registrada:** explicar **cómo se midió un dato** es evidencia y sí se permite (C-03 lo exige); hablar del **acto de escribir la pieza** no se permite.
**C-20 · Cero secretos, cero datos personales de terceros, cero índices de instalación, cero enlaces a mods.** Origen: Libro 2 (D03, D06, D07) y manual §12.1.
**C-21 · Cero signos dobles** (`!!`, `?!`, `??`) y cero exclamaciones de venta.

### Bloque D — Reglas vivas del dueño

**C-22 · Bandas de longitud.** WhatsApp **63.000–63.099** · Facebook **40.000–45.000** · post de comunidad: longitud exacta declarada en `docs/bandas.json`. Origen: orden del dueño; ver §3.1 para la tensión con el manual.
**C-23 · Cero párrafos compartidos entre piezas.** Ni entre canales ni entre números. Origen: orden del dueño.
**C-24 · Medición del día con hora.** La firma declara la hora de la casa (America/Santo_Domingo) y qué se midió. Origen: orden del dueño; se suma al cierre del manual, no lo sustituye.

### El cierre obligatorio, en orden exacto

1. **Meme del corte** (dos líneas, original).
2. **Firma textual** + **remate propio** en la misma línea: `La Bandita informa a partir de fuentes fechadas. [remate]`.
3. **Línea de medición** con la marca de la casa 💓, la fecha, la hora de la casa y el conteo de lo medido.
4. **Notas al pie** fechadas.

Ese orden resuelve la tensión entre el manual (firma + remate) y la orden del dueño (hora de medición): no compiten, se apilan.

---

## 3. Tensiones entre cimientos, con su resolución

Ninguna se resuelve en silencio. Todas quedan escritas, y las que necesitan al dueño se marcan como pendientes.

**3.1 · Banda de Facebook.** El Manual V3.0 dice «FB ≤40k» (§17.1, §18.4); la orden del dueño fija **40.000–45.000**. **Resolución:** manda la orden del dueño (posterior y explícita) → la banda operativa es 40.000–45.000 y `docs/bandas.json` es la fuente de verdad. **Pendiente para el dueño:** si quiere que el tope vuelva a 40.000, lo dice y se ajusta la banda en el mismo día.

**3.2 · Numeración.** El Manual V3.0 fija la serie `00`–`80` (§4.2); la orden del dueño lleva la serie hasta **120** (WhatsApp se agota en 113). **Resolución:** manda la orden del dueño. El rango `00`–`80` describe el corpus viejo, no la serie viva.

**3.3 · Firma.** El manual exige firma textual + remate; la orden del dueño exige hora de medición. **Resolución:** el cierre de cuatro piezas del §2 las apila sin contradicción. El emoji 💓 se conserva como **marca de la casa**, no como adorno: el manual prohíbe emojis decorativos (§2.4) y la marca no es decorativa, es identificación.

**3.4 · Mapa largo contra mapa corto.** El manual limita el mapa a 12 entradas (§5.2); las piezas escritas hasta hoy tienen hasta 32 secciones. **Resolución:** el mapa lista como máximo 12 entradas agrupadas y el cuerpo puede desarrollarlas, siempre que cada entrada del mapa corresponda a contenido real (C-07). Las piezas actuales quedan **no conformes** hasta que su mapa se agrupe y su cuerpo se ordene bajo esas entradas.

**3.5 · Idioma de las citas del dueño.** Las lecciones se citan textuales, incluidas las formas peninsulares que el dueño escribió; la prosa de la pieza va en dominicano-ES. **Resolución:** la cita no se «corrige» (sería A11, traducción que altera); la prosa sí se escribe en la casa.

**3.6 · «Gemela byte a byte».** El Manual V3.0 pide gemela idéntica en el cuerpo (§18.4); la orden del dueño prohíbe **párrafos compartidos** entre WhatsApp y Facebook. **Resolución:** manda el dueño (posterior): la gemela comparte **hechos, cifras, fuentes y advertencias**, jamás redacción. Se comprueba con C-23.

**3.7 · Meta-comentarios.** Ver C-19: la interpretación queda registrada para que nadie la aplique a gusto. Método de medición = evidencia (permitido). Relato del acto de escribir = relleno (prohibido).

---

## 4. Cómo se comprueba (y qué pasa si falla)

El gate nuevo **`tools/manual_gate.py`** recorre las piezas y emite, por cada una, un veredicto:

- **VERDE** — cumple todos los criterios obligatorios.
- **VENTANA** — cumple los de severidad crítica y falla alguno de forma, con el fallo declarado en la pieza (nota al pie).
- **ROJO** — falla un criterio crítico (firma, meme, fuente, prohibición, banda): **no se publica**.

`tools/vara.py` lo llama como compuerta **G11 · manual**. La vara no opina: si el gate dice ROJO, la corrida falla y no hay commit que lo tape.

Los criterios y su severidad viven en `tools/manual_gate.py` y en la tabla de §2 de este documento. Si alguien cambia una regla, cambia los dos — o el gate canta.

---

## 5. Lo que este documento NO hace

No mejora ninguna pieza por existir. Declara la vara y la deja enchufada. La conformidad de una pieza se mide pieza por pieza, y hoy —al corte de este documento— las piezas de la serie viva **no están conformes**: les falta el cierre del manual (meme, firma textual, remate, notas al pie), tienen mapas de más de doce entradas y varias conservan secciones de meta-comentario. El inventario de lo que falta está en `docs/CONFORMIDAD-MANUAL-2026-11-01.md`, con su cuenta exacta.

La Bandita informa a partir de fuentes fechadas. Una vara que no se puede medir es una opinión con buena letra; esta ya se puede medir.
