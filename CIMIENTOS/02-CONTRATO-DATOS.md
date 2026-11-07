# 02 · Contrato de datos

Toda ficha que entre al registro cumple `schemas/ficha.schema.json`. El contrato existe para que una
máquina pueda decir «este dato es viejo» sin interpretar prosa.

## Campos obligatorios

| Campo | Tipo | Regla |
|---|---|---|
| `id` | texto | `owner--repo` en minúsculas, sin barras |
| `repo` | texto | `owner/repo` tal como lo devuelve la API |
| `licencia.spdx` | texto o `null` | Identificador SPDX; `null` solo si la ausencia está **firmada** |
| `licencia.metodo` | enumerado | `spdx-api`, `texto-license`, `endpoint-license`, `ausencia-firmada` |
| `actividad.estado` | enumerado | `vivo`, `dormido`, `muerto` |
| `actividad.ultimo_push` | fecha | `AAAA-MM-DD` |
| `medido_en` | fecha | Día de la medición, en hora de Santo Domingo |
| `fuente.primaria` | texto | URL o endpoint exacto del que salió el dato |
| `evidencia.sha256` | texto | Huella del payload medido, para poder re-verificar |

## Reglas de integridad

1. **Ausencia firmada.** Si no hay licencia, `spdx` es `null` y `metodo` es `ausencia-firmada`.
   Inventar «probablemente MIT» rompe G3.
2. **Frescura declarada.** `medido_en` no es decorativo: G2 calcula la edad y avisa a los 180 días.
3. **Un cambio, una huella.** Si se re-mide, se actualiza `medido_en` y `evidencia`; no se edita a
   mano el resto sin volver a medir.
4. **Coherencia con las piezas.** Lo que una pieza afirma de un repo debe poder rastrearse a su
   ficha; si la ficha no existe, el repo entra al registro o la pieza lo declara como no medido.
5. **Nada de campos inventados.** El esquema `additionalProperties: false` existe precisamente para
   que nadie añada «notas» que después nadie sabe de dónde salieron.

## Dónde vive cada dato

- `registry/*.json` — fichas individuales (contrato v1).
- `registry/_indice.json` y `registry/_calidad.json` — índice y salud del censo (generados).
- `docs/envios/_medicion-{canal}.json` — censo de trabajo de los envíos (estrellas, licencia,
  empujón, versión por repo medido para las piezas del canal).
- `site/datos/registro.json` — proyección compacta para el frontend (generada, no fuente).
