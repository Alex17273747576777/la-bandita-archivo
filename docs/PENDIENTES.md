# MATRIZ DE PENDIENTES · estado al 31 de octubre de 2026

Cada pendiente con su estado real: **hecho** (existe, corre y está probado), **medido** (hay cifra
publicada, no decisión), **bloqueado por el dueño** (no lo puedo decidir yo) o **pendiente** (falta
trabajo técnico que sí puedo hacer).

## Deudas estructurales del §1.3 de la propuesta

| # | Deuda | Estado | Dónde |
|---|---|---|---|
| 1 | Sin licencia | **bloqueado por el dueño** — paquete listo para un comando | `LEGAL/PROPUESTA-LICENCIA.md`, `LEGAL/aplicar-licencia.sh` |
| 2 | Cero integración continua | **hecho** — 11 pasos, ocho compuertas, autoprueba y MCP en cada push | `.github/workflows/vara.yml` |
| 3 | Sin contrato de datos | **hecho** — esquema v1 y 5.684 fichas validadas | `schemas/ficha.schema.json`, `registry/` |
| 4 | Duplicación sin gobierno | **medido y reglado** — 277 grupos, 441 copias, 3,2 MB; política escrita; borrar es del dueño | `docs/POLITICA-DUPLICADOS.md`, `tools/duplicados.py` |
| 5 | Superficie de producto inexistente | **en curso** — el registro ya es consultable (API MCP); falta el sitio estático con URL por pieza | `mcp-labandita-registro/` |
| 6 | Canal prestado | **bloqueado por el dueño** — requiere dominio, correo y decisiones de marca | — |
| 7 | Frescura afirmada, no demostrada | **hecho** — cada ficha declara `medido_en`; la compuerta G2 y el servidor MCP dicen «rancio» con la edad exacta | `tools/vara.py`, `registry/` |

## Integración MCP (fases del §6.5)

| Fase | Alcance | Estado |
|---|---|---|
| F1 | Cliente MCP con los oficiales de referencia, solo lectura | **hecho en política** — lista blanca, versiones fijadas, solo lectura (`docs/POLITICA-MCP.md`) |
| F2 | GitHub oficial (`github/github-mcp-server`) con lista blanca | **documentado** — requiere que el dueño instale el servidor en su cliente |
| F3 | Servidor propio `labandita-registro` sobre el registro | **hecho y probado** por el cliente oficial del SDK |
| F4 | Atestaciones verificables por terceros | **hecho en lo posible sin llaves** — sello SHA-256 encadenado por lote; la firma sin llave (Sigstore) exige identidad OIDC del dueño |
| F5 | Endpoint remoto con OAuth y cuotas | **no se hace** — exige operación pagada y demanda demostrada |

## Trabajo técnico restante (puedo hacerlo yo)

| Tarea | Estado | Nota |
|---|---|---|
| Sitio estático con URL por pieza y por ficha, RSS y JSON-LD | pendiente | siguiente hito técnico natural |
| Medición fresca del registro (hoy el corte es del 15-oct: 17 días) | pendiente | requiere token y una corrida de la API; la compuerta G2 avisará a los 180 días |
| SWHID por revisión medida (Software Heritage) | pendiente | la API responde; falta archivar cada revisión citada |
| Verificación de licencias por texto cuando el endpoint no concluye (57 `NOASSERTION`) | pendiente | inspección manual de 57 árboles |
| Firma sin llave de las atestaciones (Sigstore) | bloqueado por identidad | requiere la cuenta del dueño |
| Re-medición de Scorecard para sustituir ★ como señal de mérito | pendiente | API pública, sin llave |

## Decisiones que solo el dueño puede tomar (§11)

1. **Licencia** — opciones A/B/C/D en `LEGAL/PROPUESTA-LICENCIA.md`. Es la más urgente.
2. **Marca y dominio.**
3. **Canal primario.**
4. **Línea de arranque:** L1 (B2B) o L2 (suscripción).
5. **Política de patrocinio.**
6. **Publicar `labandita-registro` en abierto** (el servidor ya existe y funciona).
7. **NLnet:** la convocatoria **cierra el 3 de noviembre de 2026 a las 12:00 CET** — quedan tres días.
   Su política exige propuesta escrita por humanos y, si se usó IA, los registros de los prompts.
   La decisión de presentarla es del dueño; este material sirve de base, no de sustituto de su voz.

## Cerrado en la jornada del 31 de octubre

| Pendiente | Resultado |
|---|---|
| Registro ampliado por descubrimiento | **+1.142 fichas nuevas** medidas hoy (total 6.826) desde una lista curada ajena |
| Procedencia inmutable (SWHID) | **32 fichas** con revisión archivada en Software Heritage y citable |
| Licencias por texto | **84 fichas** resueltas por texto (README o archivo) donde el endpoint no concluía |
| Frescura del registro | el corte ya no es del 15-oct: 1.144 fichas medidas hoy |
| Fecha de la casa | corregida a `America/Santo_Domingo` en las seis herramientas; el 1 de noviembre de UTC no es el 31 de octubre del barrio |
| Plazo de NLnet | corregido: **no cerró**, vence el 3 de noviembre de 2026 a las 12:00 CET |

## Deuda declarada y congelada

`tools/baseline.json` contiene **un** fallo conocido que la vara no bloquea pero sí publica en cada
informe: la pieza `01-Tiendas-APK ... Facebook ... 2026-09-15` no lleva la firma 💓 de la casa.
No la edité: es una pieza publicada y su corrección es una decisión editorial, no técnica.
