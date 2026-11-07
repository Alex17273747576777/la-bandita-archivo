# Acta de integración de documentos locales · 2 de noviembre de 2026

**Qué se hizo:** ingresar al repositorio los dos únicos documentos que vivían solo en el espacio local
tras la limpieza del 2-nov, con su huella, su procedencia y la razón por la que llegaron tarde.

**Corte:** lunes 2 de noviembre de 2026, noche (America/Santo_Domingo).
**Commit base:** `13357373` · **CI de ese commit:** success.

## 1 · Lo que entra

| Archivo | Bytes | SHA-256 (completo) | Qué es |
|---|---:|---|---|
| `docs/INFORME-DE-CIERRE-2026-10-31.md` | 17.878 | `8334e0fd2645d2c83313492c5b3ba721aa04784adcf881553a1f0a953de049b9` | Acta de cierre del 31-oct: compuertas G0–G5 con su resultado literal, cifras del corte y las tres subidas de la jornada (`7e8f737` → `5934d54` → `f36890c`) |
| `docs/PLAN-120.md` | 5.611 | `a295dcfc2cbb4b229c53d3545077e78cc98a86d27d35d170b30af3cebd0c2209` | Plan de reescritura de las 120 piezas: qué estaba hecho a las 31-oct, la regla para no volverse genérico y la cuenta de lo que faltaba |

El contenido **no se editó**: entran byte por byte como se escribieron. Las huellas de arriba permiten
comprobar que el archivo del repositorio es el mismo que se escribió aquella noche.

## 2 · Por qué no estaban

Los dos se escribieron **después** de la última subida de su jornada, y quedaron en el espacio local
mientras el resto del árbol ya estaba en GitHub. La limpieza local del 2-nov los detectó al cotejar
archivo por archivo contra el árbol remoto: de 22 archivos que existían solo en local, 20 eran material
superado y estos 2 eran documentos reales. Se conservaron aparte en lugar de borrarlos, y aquí se
integran.

Sin esta acta no se podían integrar: `docs/` está cubierto por `tools/sello_reglas.py`, así que un
archivo que entra sin re-sellar rompe **G5 integridad**, y la casa no empuja un árbol que la vara marca
en rojo.

## 3 · Orden en que se hizo

1. Clon fresco del remoto en `/tmp` (fuera del espacio persistente, que tiene techo de 128 MB).
2. Copia de los dos documentos a `docs/` y cálculo de su SHA-256.
3. Esta acta.
4. `tools/acta_conformidad.py` → conformidad del manual v3.0 al día.
5. `tools/atestar.py` → sello nuevo encadenado al anterior.
6. `tools/vara.py` → G0–G12 en verde.
7. `git commit` + `git push` a `main`; se espera la corrida y se confirma **success**.

## 4 · Lo que no cambia

- **Ninguna pieza se toca.** Este acta solo añade documentación.
- **Los envíos no se regeneran:** no hay pieza nueva ni modificada (`envio.py --verificar` sigue en cero
  fallos).
- **La numeración de piezas no se altera:** el corte sigue en 275 piezas y 6.830 fichas.

## 5 · Estado del espacio local después

El núcleo local (`NUCLEO/`) deja de guardar `_locales-pendientes/`: su contenido ya vive en GitHub y la
copia local pasaría a ser el tipo de duplicado que el manifiesto declara sobrante. Quedan 89 archivos
en local —ley, manual, habilidades, herramientas, esquema, licencias, MCP, token— y nada más.
