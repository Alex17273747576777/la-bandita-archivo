# MATRIZ DE PENDIENTES · estado al 3 de noviembre de 2026

Cada pendiente con su estado real: **hecho** (existe, corre y está probado), **medido** (hay cifra
publicada, no decisión), **bloqueado por el dueño** (no lo puedo decidir yo) o **pendiente** (falta
trabajo técnico que sí puedo hacer).

## Cierre del 3 de noviembre de 2026 · lo que se terminó hoy

| Pendiente | Estado hoy | Evidencia |
|---|---|---|
| Eliminar los residuos sin utilidad | **hecho** — 11 archivos retirados (16,6 MB), 53 documentos reubicados, con hash y motivo | `ARCHIVO-HISTORICO/_podado-2026-11-03/README.md`, `docs/ACTA-PODA-2026-11-03.md` |
| `uploads/` en la raíz del archivo | **hecho** — pasó a `ARCHIVO-HISTORICO/subidas-2026-09/`; la mudanza entró en la tabla de `tools/referencias.py` | G17 en verde, 0 rutas vivas rotas |
| Publicación específica de `Jman-Github/Universal-Patch-Manager` | **hecho** — pieza 06 de Facebook, VERDE en `manual_gate` y en `novedad_gate` | `docs/ACTA-PIEZA-06-2026-11-03.md` |
| Duplicación sin gobierno (§1.3 deuda 4) | **podado y reglado** — los 20 grupos de archivos idénticos ≥50 KB quedaron resueltos; siguen las 163 piezas históricas con varias fechas, que son decisión del dueño | `docs/POLITICA-DUPLICADOS.md` |
| Reescritura de las piezas 01–06 de Facebook | **04 rehecha el 4-nov** — 44.932 car., VERDE en las dos compuertas, la vieja archivada con `git mv` | `docs/ACTA-PIEZA-04-REHECHA-2026-11-04.md` |
| Etiquetas estratégicas (#pings) | **Facebook hecho el 4-nov** — política, compuerta M29 y las seis piezas etiquetadas · **WhatsApp pendiente**: la banda 63.000–63.099 no admite 250 caracteres sin recortar otros tantos | `docs/POLITICA-ETIQUETAS.md`, `docs/ACTA-ETIQUETAS-2026-11-04.md` |
| README desactualizado | **hecho** — estado al 4-nov, piezas 01–06, poda declarada | `README.md` |

### Lo que sigue abierto, con nombre y con motivo

| Pendiente | Por qué no se cerró hoy | Quién lo cierra |
|---|---|---|
| Archivo de sumas SHA-256 en las entregas del programa 06 | lo tiene que emitir el autor del programa; pedido en la tarea 001 de la pieza | el autor, y esta casa lo anota |
| Versión de WhatsApp de la pieza 06 | requiere reescribir en banda 63.000–63.099, que es otro registro | esta casa, siguiente sesión (tarea 003 de la pieza) |
| SWHID por revisión medida (Software Heritage) | la API responde; falta archivar cada revisión citada, por lotes | esta casa, por tandas |
| Medición fresca del registro completo | cuándo, lo decide el dueño; G2 avisa a los 180 días y hoy la mediana es de 19 días | el dueño |
| Sitio estático con URL por ficha | **descartado por el dueño** como producto; `tools/sitio.py` queda como herramienta interna | cerrado por decisión |
| Las cuatro decisiones de duplicados históricos | no son técnicas | el dueño |
| Las siete decisiones del §11 (licencia de marca, dominio, canal primario, línea de arranque, patrocinio, publicar el MCP, NLnet) | la convocatoria de NLnet cerró el 3-nov; las demás son de marca | el dueño |

## Deudas estructurales del §1.3 de la propuesta

| # | Deuda | Estado | Dónde |
|---|---|---|---|
| 1 | Sin licencia | **bloqueado por el dueño** — paquete listo para un comando | `LEGAL/PROPUESTA-LICENCIA.md`, `LEGAL/aplicar-licencia.sh` |
| 2 | Cero integración continua | **hecho** — 11 pasos, ocho compuertas, autoprueba y MCP en cada push | `.github/workflows/vara.yml` |
| 3 | Sin contrato de datos | **hecho** — esquema v1 y 5.684 fichas validadas | `schemas/ficha.schema.json`, `registry/` |
| 4 | Duplicación sin gobierno | **podado el 4-nov** — los 20 grupos de idénticos ≥50 KB resueltos (7,9 MB) y los envases redundantes retirados con acta; queda la decisión del dueño sobre 163 piezas históricas | `docs/POLITICA-DUPLICADOS.md`, `docs/ACTA-PODA-2026-11-03.md` |
| 5 | Superficie de producto inexistente | **en curso** — el registro ya es consultable (API MCP); falta el sitio estático con URL por pieza | `mcp-labandita-registro/` |
| 6 | Canal prestado | **bloqueado por el dueño** — requiere dominio, correo y decisiones de marca | — |
| 7 | Frescura afirmada, no demostrada | **hecho** — cada ficha declara `medido_en`; la compuerta G2 y el servidor MCP dicen «rancio» con la edad exacta | `tools/vara.py`, `registry/` |

## Integración MCP (fases del §6.5)

| Fase | Alcance | Estado |
|---|---|---|
| F1 | Cliente MCP con los oficiales de referencia, solo lectura | **hecho en política** — lista blanca, versiones fijadas, solo lectura (`docs/POLITICA-MCP.md`) |
| F2 | GitHub oficial (`github/github-mcp-server`) con lista blanca | **documentado** — requiere que el dueño instale el servidor en su cliente |
| F3 | Servidor propio `labandita-registro` sobre el registro | **hecho y probado** por el cliente oficial del SDK |
| F4 | Atestaciones verificables por terceros | **hecho** — sello SHA-256 encadenado por lote + firma Sigstore keyless con identidad OIDC del flujo de CI, verificable en frío por cualquiera (`tools/atestacion_verificar.py`) |
| F5 | Endpoint remoto con OAuth y cuotas | **no se hace** — exige operación pagada y demanda demostrada |

## Trabajo técnico restante · estado al 3 de noviembre de 2026 (12:45 AST)

| Tarea | Estado | Evidencia |
|---|---|---|
| Integrar M24–M28 en la vara y en CI | **hecho** | `tools/novedad_gate.py` + compuerta **G13** en `tools/vara.py` + 3 casos nuevos en `tools/autoprueba.py` (**14/14**) |
| Registro de novedades | **hecho** | `docs/CALENDARIO-DE-NOVEDADES.json` con **7 novedades medidas el 3-nov** (NOV-2026-001…007); G13 lo valida y marca rancio a los 90 días |
| Firma sin llave (Sigstore) | **hecho** | identidad OIDC del flujo; paquete `attestations/lote-2026-11-03.sigstore.json` verificado con `tools/atestacion_verificar.py` (Rekor nº 3.669.131.378); compuerta **G14** |
| Licencias que no concluían | **hecho en lo resoluble** | `tools/licencias_resolver.py`: 179 → 44; 134 con SPDX, 39 declaradas propietarias con su frase y su fecha (`docs/ACTA-LICENCIAS-2026-11-03.json`) |
| Scorecard como señal de mérito | **hecho el método, abierta la cobertura** | `tools/merito.py`: 9 de 48 repositorios citados indexados; ★32.705 → 2,7/10 frente a ★1.681 → 5,2/10 (`docs/SCORECARD-2026-11-03.json`) |
| HdP: carpeta, banda, siglas | **decidido** | publica en `POSTS-COMUNIDAD/` con 4.152 exactos; las siglas no se inventan (CORAZON, §29 y §30.5) |
| Medición fresca del registro completo (corte 15-oct) | pendiente, del dueño el cuándo | G2 avisa a los 180 días; hoy la mediana es de 19 días |
| SWHID por revisión medida (Software Heritage) | pendiente | la API responde; falta archivar cada revisión citada, trabajo por lotes |
| Sitio estático con URL por pieza y por ficha | pendiente | el dueño descartó la página web como producto; `tools/sitio.py` queda como herramienta interna |

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

## Cerrado tras las decisiones del titular (31 de octubre, segunda tanda)

| Decisión | Estado |
|---|---|
| 1 · Licencia | **aplicada por encargo**: contenido CC BY-SA 4.0, datos CC BY 4.0, código MIT, marca reservada. Titular: «Alexis (La Bandita)» — suposición declarada |
| 2 · Página web | **descartada**: proyecto personal, sin dominio ni marca; `tools/sitio.py` queda como herramienta interna |
| 3 · Canal | **WhatsApp como principal**; plan en `docs/CANAL-WHATSAPP.md` |
| 4 · Inteligencia | **decidida**: agente con MCP al registro + Ollama local + código para medir (`docs/INTELIGENCIA.md`) |
| 5 · Dinero | **no se acepta**, en ninguna forma; escrito en `NOTICE` |
| 6 · MCP | **listo para publicar**: `server.json` validado contra el esquema oficial `2025-12-11` con el `repository.id` real; sin paquete PyPI porque no existe (404 verificado); lo dispara el dueño |
| 7 · NLnet | **borrador listo** para que lo presente el dueño, con registro de prompts; plazo 3-nov-2026 12:00 CET |
| 8 · Sigstore | **firmado y verificado**: corrida de CI en verde y `cosign verify-blob` → `Verified OK` |
| Pieza nueva | **109 publicada**: OmniShizuku y el taller sin root, con tutorial, meme, Q&A, lectura por edad y consejos por usuario |
| Registro | **6.830 fichas**, **2.644** medidas hoy; 14 marcadas como muertas (404), que antes se descartaban en silencio |

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

## Reinicio ordenado el 1-nov-2026 (orden del dueño)

- **Hecho hoy:** piezas **09** (41.328 car.) y **10** (40.045 car.) VERDE; 16/16 VERDE en el
  manual v3.0; `vara.py` sin fallos; sello 10.030 archivos `5164e0a1…`; CI **success** en
  `a4aaa37`; `cosign verify-blob` → **Verified OK** contra `registry/_manifiesto-sha256.tsv`.
- **Cambio de método:** tres lecturas por recurso **en orden rotado** y con llave local
  (`tools/tres_lecturas.py`, 5.000 peticiones/hora, sin esperas). Sección 451/422 sin README
  se declara hueco, nunca se rellena.
- **TMO re-medido en vivo** (`docs/TMO-2026-11-01.md`): cinco dominios, tres lecturas cada
  uno; solo dos entregan catálogo hoy. La pieza **05 FB** parte de material viejo y es la
  primera que hay que reescribir con este censo.
- **Siguiente lote del reinicio:** 01 → 05 de Facebook, con fecha y hora vivas, censo TMO
  nuevo y revisión pieza contra pieza para que no quede párrafo compartido (M23).
