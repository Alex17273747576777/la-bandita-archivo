# LA BANDITA — de archivo verificado a empresa de verificación

**Propuesta ejecutiva · corte medido el 31 de octubre de 2026**

**Autor del análisis:** asistente de La Bandita, por orden del dueño
**Fuente de verdad:** `github.com/Alex17273747576777/la-bandita-archivo`, commit `3f04b89`, clonado y medido hoy
**Naturaleza del documento:** propuesta de negocio, arquitectura e integración — no un adorno. Cada cifra dice de dónde sale y cuándo se midió; lo que no se pudo medir está firmado como ausencia.

---

## 0. Resumen ejecutivo

La Bandita no es un blog. Es un **registro verificado del ecosistema Android libre, escrito en español dominicano, con fecha y evidencia en cada dato**. Hoy tiene 261 publicaciones, 573 repositorios censados con licencia y actividad medidas, 701 recursos mapeados y un método de verificación propio que ya demostró que sabe detectar sus propios errores.

Lo que no tiene —y esto es el diagnóstico central— es **estructura de empresa**: no tiene licencia, no tiene integración continua, no tiene contrato de datos, no tiene canal propio, no tiene precio, no tiene un solo ingreso. Todo el valor está concentrado en la cabeza y la disciplina de una persona.

La propuesta es convertir ese método en tres cosas vendibles y una infraestructura:

1. **Un servicio de debida diligencia de software** para quien tiene que decidir con papeles: bancos, telcos, fintech, sector público y fondos que invierten en tecnología en República Dominicana y el Caribe. Alto precio por informe, venta consultiva, cero dependencia de algoritmos.
2. **Una suscripción de barrio** —el producto de siempre, pero con canal propio, pago y continuidad— que además alimenta el registro.
3. **La Vara como servicio** (*open core*): el motor de verificación publicado como herramienta abierta y como **servidor MCP**, para que cualquier agente o medio pueda consultar "qué es esto, quién lo mide, cuándo y con qué evidencia".

La infraestructura que lo sostiene es un repositorio convertido en sistema: contrato de datos con esquema, ocho compuertas automáticas en integración continua, procedencia criptográfica por pieza y un sitio estático autocontenido que no depende de ninguna plataforma.

**Lo que se pide al dueño:** cinco decisiones (licencia, marca, canal primario, política de patrocinio y publicación del servidor MCP) y autorización para el primer trimestre de ejecución. **Inversión de infraestructura estimada:** menos de US$10/mes en la fase 1. **Riesgo principal:** seguir igual, que es el único escenario donde el activo se deprecia solo.

---

## 1. Diagnóstico: lo que el repositorio es, medido hoy

### 1.1 Inventario crudo

| Medida | Valor | Cómo se midió |
|---|---|---|
| Archivos en el árbol | 3.411 | `find` sobre el clon de `main` |
| Peso del contenido (sin `.git`) | 174 MB | `du --exclude=.git` |
| Archivos Markdown | 3.005 | conteo por extensión |
| Palabras en Markdown | 6.067.493 | conteo de `split()` sobre los 3.005 archivos |
| Publicaciones WhatsApp | 113 · 367.737 palabras | carpeta `01-PUBLICACIONES/WhatsApp-dominicano-ES` |
| Publicaciones Facebook | 148 · 82.177 palabras | carpeta `01-PUBLICACIONES/Facebook-dominicano-ES` |
| Repositorios censados | 573, todos con campo de licencia | `censo-ecosistema-2026-10-15.tsv` leído con parser CSV |
| Vivos (push ≤180 días al corte) | 467 (81,5 %) | cálculo de fechas contra 2026-10-15 |
| Dormidos | 106 (18,5 %) | ídem |
| Estrellas totales censadas | 4.203.143 · mediana 1.760 | suma y mediana del campo `stars` |
| Velocidad mediana | 65,1 ★/mes | campo `stars_por_mes` |
| Recursos mapeados | 701 en 108 piezas | `mapa-recursos-29oct.json` |
| Herramientas propias | 20 scripts Python, ≈2.600 líneas | `HABILIDADES/herramientas` + `_herramientas` |

### 1.2 Los cuatro activos reales

**A. Corpus editorial.** 449.914 palabras publicadas en dos plataformas con voz propia, anatomía fija (semilla, mapa mental, fichas, meme, método, glosario, nota de verificación fechada) y un registro lingüístico que ningún generador reproduce por accidente: el barrio, el mueble, el portero, la casa. Eso es marca, no texto.

**B. Registro verificado.** 573 fichas con licencia, actividad, estrellas y velocidad; 701 recursos mapeados a piezas. Es la materia prima de todo lo que sigue: sin registro no hay informe, no hay API, no hay MCP.

**C. Método.** Siete habilidades ejecutables (arranque, verificación multinivel, pulso, licencias sin inventar, pieza editorial, guardado con verificación por blobs, formato respirable) más la puerta anti-plantilla y la doctrina de la casa. Este es el activo más difícil de copiar y el único que se puede vender tal cual.

**D. Herramientas.** `arranque.py`, `chequeo-niveles.py`, `pulso.py`, `vara-simulada.py`, `guardar.py`, `aprender.py`, las cinco lupas, la forja del catálogo. Funcionan, están probadas en producción y son pequeñas (22 a 489 líneas): se pueden endurecer y publicar en semanas, no en años.

### 1.3 Las siete deudas estructurales (con nombre y consecuencia)

1. **Sin licencia.** El repositorio no tiene `LICENSE` en la raíz. Sin licencia, nadie puede reutilizarlo legalmente, ningún fondo puede financiarlo y ninguna empresa puede comprarle un informe sin abogado de por medio. Es la deuda más caras de todas y cuesta un día resolverla.
2. **Cero integración continua.** No existe `.github/`. La vara —las compuertas que impiden publicar basura— se ejecuta a mano, por disciplina humana. El propio historial demuestra el costo: se empujó una pieza rota (`ebd74b0`) porque la vara reportó fallos con salida en cero. La disciplina sin automatización falla; la automatización sin disciplina también. Necesita las dos.
3. **Sin contrato de datos.** El censo es un TSV de 573 filas; el mapa es un JSON con tres claves distintas; las placas son prosa con formato. Nada de eso se puede validar, versionar ni consumir por máquina. Un esquema convierte 573 filas en un producto.
4. **Duplicación sin gobierno.** 3.005 archivos Markdown incluyen versiones en portugués, francés e inglés, cortes de septiembre, respaldos previos y entregas empaquetadas. Cada duplicado es un sitio donde una corrección puede quedarse sin aplicar, y el proyecto ya vivió esa mordida.
5. **Superficie de producto inexistente.** El catálogo es un HTML único de 997 KB, sin rutas por pieza, sin búsqueda indexable, sin sindicación, sin descarga de datos. Funciona como archivo; no funciona como producto.
6. **Canal prestado.** Todo el alcance vive en Facebook y WhatsApp. Una decisión de moderación o un cambio de política y el proyecto desaparece sin perder un byte de contenido. No hay lista de correo, no hay RSS, no hay dominio propio en uso.
7. **Frescura desigual.** Conviven piezas fechadas 15-sep, 22-sep, 15-oct y 29-oct. La casa tiene razón al no maquillar fechas, pero hoy no hay ningún indicador que diga al lector —ni al comprador— la edad real de cada dato. La frescura se afirma, no se demuestra.

### 1.4 Lectura estratégica: dónde está el foso

Un modelo de lenguaje escribe hoy un artículo aceptable sobre F-Droid. Lo que no puede hacer es **afirmar con fecha, evidencia y firma que un repositorio concreto tenía 185.239 estrellas, licencia MIT y su último empuje el 29 de octubre de 2026, y demostrar que ese número salió de la API oficial ese día y no se ha modificado después**. Esa asimetría es el negocio: el texto se commoditiza, la procedencia no.

Esta propuesta se organiza alrededor de una sola idea: **vender procedencia verificable**, con el texto como empaque.

---

## 2. Mercado: quién paga, por qué y cuánto

### 2.1 Contexto dominicano medido

La Encuesta Nacional de Hogares (EnHogar-MICS 2025, publicada por la ONE y difundida en julio de 2026) mide: **92,7 % de hogares con al menos un teléfono móvil**, **89,4 % con smartphone**, y solo **56,2 % con banda fija** (60,2 % urbano, 45,5 % rural); computadora en el hogar, 32,8 %.

Consecuencia directa para el negocio: el país es **móvil-primero y WhatsApp-primero**, y cualquier producto digital que exija descargar una aplicación desde una tienda o registrarse en un portal web de escritorio va a perder a la mayoría antes del primer clic. Esto no es una preferencia estética: es una restricción de arquitectura.

### 2.2 Los cuatro compradores

| Comprador | Dolor concreto | Qué compra | Sensibilidad al precio |
|---|---|---|---|
| **B2B cumplimiento** (banca, telco, fintech, seguros, aseguradoras de software) | Tienen que decidir si aceptan un componente de código abierto y no saben quién lo mantiene, con qué licencia ni qué tan vivo está | Informe de debida diligencia con evidencia fechada y metodología auditable | Baja si el informe les ahorra un riesgo legal o un incidente |
| **B2G educación y digitalización** | Programas de alfabetización digital y de "uso seguro" que necesitan contenido y método, no folletos | Licencia de contenido + capacitación + informe de medición | Media; ciclos lentos; requiere facturación formal |
| **Barrio y diáspora (B2C)** | Le instalan cosas, le piden permisos raros, le roban datos y no sabe a quién creer | Suscripción con verificación continua y consultas | Alta sensibilidad, pero volumen agregable |
| **Ecosistema FOSS** (proyectos, directorios, medios técnicos) | Necesitan medir frescura y procedencia de su propio catálogo sin montar un equipo | La Vara como servicio y como servidor MCP | Media; paga en visibilidad y en dinero pequeño, con alta credibilidad |

### 2.3 Por qué ahora

Tres cosas están pasando al mismo tiempo y empujan en la misma dirección:

- **El ecosistema se está cerrando.** La verificación de desarrolladores de Google, el registro del 30 de septiembre de 2026 y la fecha de 2027 que la serie cronometra hacen que "saber qué se puede instalar de verdad" pase de curiosidad a necesidad. Cuando todo está abierto, verificar no vale nada; cuando se cierra, verificar es el producto.
- **La IA multiplicó el contenido y bajó su confianza.** El valor marginal de otro artículo generado es cero; el valor de un dato fechado y firmado sube. La puerta anti-plantilla que la casa ya construyó es, literalmente, el diferencial del mercado.
- **MCP convirtió los catálogos en infraestructura.** Un registro que un agente puede consultar con contrato y fecha se vuelve proveedor; uno que solo existe en prosa se vuelve forraje. Medición propia de hoy: el registro oficial de MCP tiene **53.886 entradas en su última versión**, y el **66,6 %** declara endpoint remoto. Hay un mercado naciendo de consumidores automáticos de datos verificados.

### 2.4 Lo que no vamos a hacer

No se compite por tráfico con medios de tecnología. No se vende publicidad programática. No se cobra por reseñar aplicaciones. No se monetiza la lista de correo con afiliados de tiendas de mods. Cada una de esas vías destruye exactamente el activo que hace valiosa la marca: la independencia verificable.

---

## 3. Portafolio de ofertas

Cinco líneas. Dos de arranque, una apuesta, una subvención, una diferida. El orden importa: la línea de arranque financia la apuesta, no al revés.

### L1 · Debida diligencia de software (arranque, recomendada)

**Qué es:** informe de 12 a 20 páginas sobre un componente, proveedor o conjunto de aplicaciones, con: identidad y propiedad del proyecto, licencia verificada por orden (SPDX → endpoint → texto del archivo → ausencia firmada), actividad medida con semántica explícita (404 muerto, 451 bloqueado, 403/429 jamás es muerte), cadena de mantenimiento, señales de riesgo (dependencias fantasma, binarios sin fuente, permisos excesivos), y anexo de evidencia con fechas y hashes.

**Por qué lo compran:** porque el comité de riesgos no acepta "lo dice un blog". Acepta un documento con metodología, fecha de corte y evidencia reproducible.

**Precio:** US$1.200 (componente único) · US$2.400 (conjunto de 10) · US$4.800 (proveedor completo + seguimiento de 90 días).
**Costo marginal estimado:** 6–14 horas de trabajo, casi todo lectura de evidencia ya automatizada.
**Margen objetivo:** 65–80 % una vez que la Vara esté en CI.

### L2 · Suscripción de barrio (arranque, recomendada)

**Qué es:** el producto de siempre con tres añadidos que lo vuelven cobrable: (a) *alerta de cambios* — cuando una app que usas cambia de dueño, de licencia o se queda dormida, te enteras con la evidencia; (b) *consulta directa* — una pregunta al mes, respondida con placa medida, no con opinión; (c) *archivo completo* descargable, porque el archivo es la promesa.

**Canal:** WhatsApp propio con enlace de pago, y página de suscripción en el dominio propio. WhatsApp es el canal de entrada; la base de datos es nuestra, no de Meta.
**Precio:** RD$200/mes o RD$2.000/año (equivalente aproximado US$3–4/mes; la conversión se fija el día que se publique el precio, no antes).
**Objetivo realista año 1:** 120–300 suscriptores. No es la línea que paga la casa; es la que construye la lista propia, que es el activo de distribución que hoy no existe.

### L3 · La Vara como servicio (apuesta)

**Qué es:** el motor de verificación, publicado en abierto (núcleo) y ofrecido como servicio alojado (capas de operación): monitoreo continuo de un catálogo ajeno, atestaciones firmadas descargables, y un **servidor MCP** que expone el registro como herramientas para agentes.

**Cliente:** directorios de apps, medios técnicos, proyectos FOSS con catálogo, equipos de cumplimiento que ya pagan por inventario de software.
**Precio:** US$49/mes (hasta 100 repositorios) · US$199/mes (hasta 1.000 + atestaciones) · acuerdos anuales para directorios.
**Por qué es apuesta:** requiere obra técnica real y credibilidad pública antes de la primera venta. Pero es la única línea con techo alto y la única que un fondo de infraestructura abierta financiaría sin pedirnos que dejemos de escribir.

### L4 · Subvención de infraestructura abierta (financiamiento, no negocio)

**Hecho verificado hoy:** NLnet tiene fecha límite **3 de noviembre de 2026, 12:00 CET**, primer grant de **€5.000 a €50.000**, exige licencias abiertas y estándares abiertos, y su política declara que **las propuestas deben ser escritas por humanos, no por IA**; si se usa asistencia de IA, hay que entregar los registros de prompts.

Esto tiene dos consecuencias que el dueño debe saber antes de decidir:
1. Una propuesta redactada por un asistente y enviada como propia **viola la política del fondo**. La vía legítima es que el dueño la escriba, o que se declare el uso de IA con los registros. Este documento sirve como material de base, no como sustituto de su voz.
2. La fecha es en tres días. Si no hay decisión hoy, la siguiente ventana es la siguiente convocatoria.

**Evaluación honesta del encaje:** NLnet financia *desarrollo técnico*: la Vara (motor, esquema, atestaciones, servidor MCP) encaja; la serie editorial no. **Sovereign Tech Fund** exige mínimo €50.000, foco en infraestructura base y **no financia aplicaciones de usuario**; con la información pública de hoy, el encaje de La Bandita es débil salvo que se presente exclusivamente el componente de verificación. Decirlo ahora evita un mes perdido en un formulario.

### L5 · Programa B2G de alfabetización verificada (diferida a año 2)

**Qué es:** licencia del corpus adaptado, talleres para docentes y periodistas, e informe de medición de adopción. Requiere personería jurídica, facturación y un socio local con experiencia en compras públicas. No se arranca antes de tener L1 y L2 funcionando: el sector público compra a quien ya existe.

---

## 4. Economía: supuestos explícitos, no pronósticos

Todo lo que sigue son **supuestos de trabajo** declarados como tales, no datos de mercado medidos. Se presentan para que el dueño pueda discutir la aritmética, no para prometer resultados.

**Supuestos base:** 12 horas semanales de producción; 6 informes L1 en el año; 2 retainers de seguimiento a 6 meses; 180 suscriptores promedio en L2; 2 talleres; 0 ingresos de L3 en el año (se construye, no se vende).

| Línea | Cálculo | Año 1 (US$) |
|---|---|---|
| L1 informes | 6 × US$1.800 (mezcla de alcances) | 10.800 |
| L1 retainers | 2 × US$900 × 6 meses | 10.800 |
| L2 suscripción | 180 × US$3,5 × 12 | 7.560 |
| Talleres | 2 × US$1.200 | 2.400 |
| **Total ingresos** | | **31.560** |
| Infraestructura | dominio + CI + hosting estático | −120 |
| Herramientas y fuentes | APIs gratuitas; reserva para cuentas y respaldo | −600 |
| **Margen bruto estimado** | | **30.840** |

**Punto de equilibrio operativo:** 1 informe L1 al mes cubre infraestructura y tiempo parcial; el resto es construcción de la L3.
**Escenario conservador (mitad):** US$15.800. **Escenario optimista (×2,2):** US$69.000, que solo ocurre si L1 consigue dos clientes ancla en el primer semestre.
**Sensibilidad:** el negocio es frágil al primer trimestre (sin informes no hay caja) y robusto a partir del segundo (los retainers y la suscripción son recurrentes). Por eso el orden de ejecución es L1 antes que L3, aunque L3 sea más interesante.

---

## 5. Arquitectura técnica objetivo

El estándar superior que se pide no es más contenido: es **estructura que impida el error**. Esta es la forma concreta.

### 5.1 El repositorio como sistema

```
la-bandita-archivo/
├── content/            # piezas por plataforma, una fuente por pieza, sin duplicados
├── registry/           # fichas .json (una por recurso) — el activo vendible
├── schemas/            # contrato de datos versionado (ficha, placa, atestación)
├── tools/              # vara, pulso, guardar, lupa — empaquetados y con pruebas
├── site/               # generador estático: catálogo, rutas por pieza, RSS, JSON-LD
├── acts/               # actas y erratas: la memoria pública del proyecto
├── dist/               # salida publicada (nunca editada a mano)
└── .github/workflows/  # las ocho compuertas
```

Regla de oro: **una pieza, una fuente**. Facebook y WhatsApp dejan de ser dos archivos que hay que mantener sincronizados a mano y pasan a ser dos *renderizados* de una misma fuente con restricciones propias. La duplicación actual (3.005 Markdown) es el mayor pasivo técnico del proyecto y el más fácil de detener: basta con no crear el décimo duplicado.

### 5.2 Contrato de datos

Una ficha mínima, en JSON, con estos campos obligatorios: `repo`, `medido_en` (fecha ISO), `fuente` (API oficial, web oficial, terciaria), `licencia` con `spdx`, `metodo` (orden SPDX → endpoint → texto → ausencia firmada) y `verificado_en`; `actividad` con `ultimo_push` y `estado` calculado con semántica explícita; `evidencia` con hash del payload crudo; y `atestacion` opcional.

El esquema completo va como anexo (`anexos/ficha.schema.json`) y como ejemplo ejecutable (`datos/ejemplo-ficha.json`). Una ficha sin `medido_en` no es una ficha: es una opinión con corchetes.

### 5.3 Las ocho compuertas (la Vara en integración continua)

| # | Compuerta | Qué detiene | Cómo se prueba |
|---|---|---|---|
| 1 | Esquema | ficha sin fecha, sin fuente o sin método de licencia | validador JSON Schema |
| 2 | Frescura | dato de más de N días presentado como actual | comparación `medido_en` vs `hoy` |
| 3 | Licencia | licencia inventada o inferida por el nombre | orden SPDX → endpoint → texto → ausencia firmada |
| 4 | Actividad | 403/429 tratados como muerte | tabla de semántica de códigos |
| 5 | Integridad | pieza alterada tras el sello | SHA-256 por archivo y por lote |
| 6 | Anti-plantilla | prosa genérica, estructura formulística | densidad, repetición de n-gramas, frases de transición |
| 7 | Enlaces | recurso canónico ausente o espejo presentado como oficial | resolución de URL + dominio canónico declarado |
| 8 | Presupuesto | pieza fuera de la banda de tamaño de su plataforma | `len()` por plataforma |

Ninguna compuerta se aprueba por salida en cero: se aprueba cuando el reporte dice **"fallos: NINGUNO"** y ese texto está en el registro del job. La lección costó una pieza rota en producción; queda codificada.

### 5.4 Procedencia criptográfica (la innovación real)

El sello SHA-256 actual prueba que un archivo no cambió. No prueba **quién midió, cuándo y con qué**. El salto de estándar es este:

1. **SWHID por revisión.** Al medir un repositorio, se archiva su revisión en Software Heritage y se cita el identificador inmutable (`swh:1:rev:…`). Verificado hoy: la API de Software Heritage responde. Con eso, la placa deja de depender de que GitHub conserve el commit.
2. **Atestación firmada por lote.** Cada hornada produce una atestación (formato in-toto) firmada sin llave (Sigstore/cosign keyless) que enumera las fichas, sus hashes y la fecha. Cualquiera puede verificar que el informe de julio fue medido en julio.
3. **Publicación de la atestación junto al informe.** El cliente B2B no compra confianza: compra algo que puede verificar sin llamarnos.

Esto es lo que separa "un blog serio" de "infraestructura de verificación", y es exactamente el tipo de trabajo que un fondo de infraestructura abierta financia.

### 5.5 Fuentes verificadas y su papel

Cada fuente tiene un rol y un límite. Probadas hoy contra su endpoint:

| Fuente | Rol | Estado verificado hoy | Límite que hay que respetar |
|---|---|---|---|
| API y web de GitHub | gobernante para ★, actividad, releases, licencia | operativa con token | cuota; 403/429 jamás es muerte |
| F-Droid `index-v2.json` | catálogo firmado de apps libres | HTTP 200 | solo ecosistema F-Droid |
| Repology | versionado cruzado entre distribuciones | HTTP 200 | no mide actividad del repo |
| Ecosyste.ms | metadatos secundarios y descubrimiento | HTTP 200 | nunca sustituye la fuente primaria |
| OpenSSF Scorecard | mérito de prácticas (sustituye a ★ como señal) | operativa (probada con un repo de referencia: score 5, 14 chequeos, fecha 2026-10-19) | no todos los repos están puntuados |
| deps.dev | cadena de suministro a nivel de paquete | HTTP 200 | mide paquetes, no aplicaciones |
| Software Heritage | inmutabilidad y cita canónica | HTTP 200 | archiva, no verifica licencias |
| Registro oficial MCP | descubrimiento de servidores MCP | HTTP 200; 53.886 entradas latest medidas hoy | está en *preview* y no revisa seguridad |

**Decisión de diseño:** ★ se conserva como dato, pero **el mérito se mide con Scorecard + actividad + licencia**. Es la traducción técnica de la regla del dueño: la popularidad no sustituye el mérito.

### 5.6 El sitio: producto, no folleto

- Generación estática desde `content/` y `registry/`: cada pieza con URL propia, cada recurso con ficha enlazable.
- **Autocontenido por principio:** cero CDN, cero fuentes externas, iconos SVG dibujados a mano, tipografía del sistema. El módulo de referencia (MOS Premium v15) tomaba sus fuentes de Google y sus iconos de unpkg: sin red, se degradaba. La versión de La Bandita no pide un byte.
- Búsqueda local con índice precargado, descarga del registro en JSON/CSV, RSS y `JSON-LD` por ficha para que los buscadores entiendan qué se está afirmando y cuándo.
- PWA instalable sin tienda, porque el país es móvil y la tienda es un peaje.
- **Costo estimado:** US$0–5/mes (hosting estático gratuito + dominio anual). El sitio no es el gasto; el gasto es el tiempo de medición.

### 5.7 Capacidad y automatización

Orden de automatización por retorno: (1) medición de repos y licencias — ya casi resuelta; (2) validación de fichas y frescura; (3) renderizado por plataforma desde fuente única; (4) atestaciones; (5) generación del sitio. Lo que **no** se automatiza: la decisión editorial, el juicio de riesgo y la firma. Un sistema que se firma solo no es un sistema verificable, es una máquina de ruido.

---

## 6. Integración de servicios MCP: evaluación, selección y jugada propia

### 6.1 Qué es hoy MCP (hechos verificados, con fecha)

- Protocolo abierto que conecta aplicaciones de IA con servidores que exponen herramientas, recursos y prompts. Creado por Anthropic (noviembre de 2024) y **gobernado desde el 9 de diciembre de 2025 por la Agentic AI Foundation, bajo la Linux Foundation**. Código y especificación con **licencia Apache 2.0**.
- **Revisión vigente de la especificación: 2026-07-28.** En esa revisión quedaron **deprecados Roots, Sampling y Logging**, con doce meses de gracia; una implementación nueva no debe adoptarlos.
- Transportes: **stdio** para servidores locales y **Streamable HTTP** para remotos. Autorización opcional para HTTP, con perfil OAuth 2.1, metadatos de recurso protegido (RFC 9728) y tokens con audiencia (RFC 8707).
- **El registro oficial sigue en *preview*.** Medición propia de hoy, 31 de octubre de 2026, paginando su API: **53.886 entradas en su última versión**, de las cuales **35.884 (66,6 %) declaran endpoint remoto**.

### 6.2 Riesgo medido: el registro no es un catálogo de confianza

El registro guarda metadatos y verifica la propiedad de un espacio de nombres; **no revisa seguridad, no mide mantenimiento y no audita permisos**. Censos independientes de 2026 reportan que una parte grande de los servidores publicados no vuelve a actualizarse y que una fracción relevante no enlaza su código fuente. Y el vector de ataque propio de este protocolo ya está documentado: descripciones de herramientas envenenadas (*tool poisoning*), inyección de instrucciones desde contenido remoto, y exfiltración por herramientas que leen lo que no deberían.

**Consecuencia operativa, sin matices:** integrar MCP por moda es un pasivo. Se integra por lista blanca, con versión fijada, permisos mínimos y registro de auditoría.

### 6.3 Selección de servidores: lo que sí y lo que no

**Sí — servidores oficiales de referencia** (mantenidos en `modelcontextprotocol/servers`, el repositorio del propio proyecto; verificados hoy en su rama `main`):

| Servidor | Para qué lo usa La Bandita | Riesgo residual |
|---|---|---|
| **Fetch** | traer una página oficial y convertirla a texto para medir | contenido remoto es dato, nunca instrucción |
| **Filesystem** | lectura del árbol local de piezas y fichas, con raíz acotada | debe apuntar solo a la carpeta del proyecto |
| **Git** | historial y diffs: auditar qué cambió y cuándo | solo lectura por defecto |
| **Memory** | grafo de conocimiento persistente entre sesiones | no guardar secretos ni datos personales |
| **Time** | fechas y zonas: la casa vive de fechas correctas | ninguna relevante |
| **Sequential Thinking** | descomposición de auditorías complejas | no sustituye evidencia |
| **Everything** | banco de pruebas del cliente MCP | solo en entorno de pruebas |

**Sí — servidor oficial del proveedor:** **`github/github-mcp-server`**, el servidor MCP de GitHub (licencia **MIT**, ★34.126, último empuje **2026-10-30**, verificado hoy). Es la vía para operar el repositorio desde un agente sin reimplementar la API.

**No — los archivados.** El repositorio de referencia movió a `servers-archived` los servidores de **GitHub, GitLab, PostgreSQL, SQLite, Puppeteer, Slack, Sentry, Google Drive, Google Maps, Redis, Brave Search, AWS KB y EverArt**. En particular: el servidor de GitHub del repo de referencia **está archivado**; usar ese sería adoptar código muerto teniendo el oficial vivo. Esta es exactamente la clase de error que la puerta de La Bandita existe para impedir, aplicada a la propia casa.

**Prohibiciones duras (lista negra operativa):**

1. Ningún servidor sin repositorio de código enlazado y mantenedor identificable.
2. Ningún servidor sin versión fijada por hash o etiqueta inmutable.
3. Ningún servidor que reciba credenciales por variable de entorno global: token por herramienta, con alcance mínimo y caducidad.
4. Ningún servidor con escritura habilitada por defecto: escritura siempre con aprobación humana explícita.
5. Ningún contenido remoto se interpreta como instrucción; se trata como dato y se cita.
6. Ningún servidor cuya única distribución sea un endpoint remoto opaco y sin fuente.

### 6.4 La jugada propia: el servidor MCP de La Bandita

Aquí está el movimiento estratégico que esta propuesta recomienda: **no solo consumir MCP — publicar La Bandita como servidor MCP**.

**Nombre propuesto:** `labandita-registro`
**Qué expone (herramientas de solo lectura, contrato JSON con fecha obligatoria):**

| Herramienta | Entrada | Salida (siempre con `medido_en`, `fuente`, `evidencia`) |
|---|---|---|
| `buscar_recurso` | texto, familia, plataforma | fichas coincidentes del registro |
| `ficha_recurso` | `repo` o identificador | ficha completa con licencia, actividad, estado y SWHID |
| `censo_familia` | familia (lectores, música, respaldo…) | agregados: vivos, dormidos, licencias, mediana de actividad |
| `estado_frescura` | `repo` o pieza | edad del dato en días y si supera el umbral |
| `verificar_licencia` | `repo` | resultado del orden SPDX → endpoint → texto → ausencia firmada |
| `atestacion_lote` | fecha o identificador de hornada | atestación firmada y hashes verificables |

**Por qué esto vale dinero y no es un juguete:**

- Convierte 573 fichas y 701 recursos en **infraestructura consultable por agentes**, que es el formato en el que se va a consumir información técnica en los próximos años.
- Obliga a tener el contrato de datos limpio: no se puede servir lo que no está esquematizado. La jugada MCP **fuerza** la deuda técnica buena.
- Es defendible: nadie más tiene este corpus en español con fecha y evidencia.
- Es el entregable natural para L3 y para una subvención de infraestructura abierta.
- Y encaja con la casa: la pieza 63 de la serie ya trata el protocolo; el catálogo ya es una webroot autocontenida; la vara ya es una política de "rechazar antes de aplicar".

**Regla de honestidad del servidor:** ninguna herramienta devuelve una afirmación sin fecha. Si un recurso no se ha medido en el umbral configurado, la herramienta responde `estado: "rancio"` con la edad exacta, en vez de devolver el dato viejo como si fuera fresco. Un servidor que miente con seguridad es peor que uno que no existe.

### 6.5 Costo y calendario de la integración

| Fase | Alcance | Esfuerzo | Riesgo |
|---|---|---|---|
| F1 | Cliente MCP con los 7 oficiales de referencia, solo lectura, en local | 1 semana | bajo |
| F2 | GitHub oficial + política de lista blanca versionada | 1 semana | medio (permisos) |
| F3 | Servidor propio `labandita-registro` en modo lectura sobre el registro | 3–4 semanas | medio (calidad del registro) |
| F4 | Atestaciones y verificación pública de fichas | 3 semanas | bajo |
| F5 | Endpoint remoto con OAuth y cuotas (solo si hay demanda pagada) | 4 semanas | alto (operación) |

---

## 7. Gobernanza, legal y ética

**7.1 Licencia (decisión pendiente del dueño).** Propuesta: contenido **CC BY-SA 4.0**, código **MIT**, registro de datos **CC BY 4.0** con atribución obligatoria y cita de la fecha de medición. Sin licencia no hay negocio posible ni subvención posible; con licencia, el uso comercial sigue siendo del dueño si se reserva la marca y los servicios.

**7.2 Marca.** "La Bandita" se protege como marca y como dominio. La licencia abre el contenido; no abre el nombre ni la certificación. Esa separación es lo que permite vender confianza sin cerrar el archivo.

**7.3 Contenido sensible.** La serie nombra tiendas de mods para advertir, no para recomendar. Esa política existe en la práctica; la propuesta la convierte en **regla dura del sistema**: ninguna pieza puede contener enlace de descarga a binario modificado, y la compuerta 7 detiene la publicación si aparece. Un letrero no es una receta.

**7.4 Dependencia de plataforma.** Facebook y WhatsApp son canales prestados. El plan crea canal propio (dominio, correo, RSS, PWA) y trata las redes como escaparate. Objetivo medible: que a los 12 meses el 50 % de la relación con la audiencia viva en una lista que el proyecto controla.

**7.5 Privacidad.** Cero analítica de terceros por defecto; métricas agregadas y propias; sin cookies de seguimiento; sin perfilado de lectores. Además de ser correcto, es coherente con el producto: no se puede vender privacidad midiendo a la gente.

**7.6 Transparencia sobre IA.** Este proyecto usa asistentes de IA en investigación, medición y redacción. Se declara en cada acta, se conservan los registros cuando un financiador los exija (NLnet lo exige si se usa IA en la propuesta) y nunca se presenta como humano lo que no lo es. La marca no se construye sobre el engaño de origen: se construye sobre la evidencia de método.

**7.7 Derecho de réplica y errata.** Todo proyecto medido puede pedir corrección; toda corrección se publica con fecha y con el error original visible. Una errata pública vale más que cien aciertos silenciosos, y es el mejor argumento de venta de un servicio de verificación.

---

## 8. Plan de 12 meses

**T1 (nov 2026 – ene 2027) · Cimientos que no se ven pero sostienen**
Licencia y aviso legal · esquema de ficha v1 + migración del censo · CI con compuertas 1, 3, 4 y 5 · repositorio ordenado (una pieza, una fuente; congelar duplicados) · precio y página de suscripción · cartera de 20 prospectos B2B. *Criterio de salida:* una pieza nueva publicada sin intervención manual de verificación, y primer informe L1 vendido o en negociación formal.

**T2 (feb – abr 2027) · Producto**
Generador de sitio con rutas por pieza y ficha enlazable · RSS y PWA · compuertas 6, 7 y 8 · SWHID por revisión medida · primer lote de atestaciones firmadas · 3 informes L1 entregados. *Criterio de salida:* 2 retainers firmados y 100 suscriptores.

**T3 (may – jul 2027) · La Vara como servicio**
Paquete instalable de la Vara con pruebas · servidor `labandita-registro` en lectura · piloto con un directorio o medio aliado · publicación técnica de la metodología (paper corto o documentación citable) · si aplica, propuesta de subvención con la voz del dueño. *Criterio de salida:* un tercero usa la Vara sobre su propio catálogo.

**T4 (ago – oct 2027) · Escala y defensa**
Atestaciones públicas verificables por terceros · endpoint remoto solo si hay demanda pagada · programa de talleres · revisión de precios con datos reales · auditoría anual del propio método publicada. *Criterio de salida:* ingresos recurrentes ≥ 60 % del total.

---

## 9. Riesgos y mitigaciones

| Riesgo | Prob. | Impacto | Señal temprana | Mitigación |
|---|---|---|---|---|
| Dependencia de una sola persona | Alta | Crítico | dos semanas sin publicar | método documentado y ejecutable; el sistema no vive en la cabeza |
| Cambio de política de Meta | Media | Alto | reducción de alcance sin cambio de contenido | canal propio y lista de correo desde el T1 |
| Erosión de frescura del registro | Alta | Alto | placas de más de 90 días en portada | compuerta de frescura y caducidad visible |
| Rechazo del mercado al precio B2B | Media | Alto | 10 prospectos sin respuesta | oferta de entrada más pequeña y piloto pagado |
| Incidente de seguridad por un servidor MCP | Media | Alto | herramienta con permisos crecientes | lista blanca, versión fijada, solo lectura, auditoría |
| Reclamación legal por contenido | Baja | Alto | requerimiento de un proyecto medido | derecho de réplica, errata pública, lenguaje de evidencia |
| Conflicto de interés por patrocinio | Media | Medio | patrocinador del ecosistema medido | política de divulgación obligatoria y separación editorial |
| Subvención que nunca llega | Alta | Medio | plazos perdidos | el plan no depende de ella; es acelerador, no pilar |

---

## 10. Indicadores: la vara de la empresa

No se declara sano lo que no se mide. Estos son los números que el dueño debe poder ver cada mes:

| Indicador | Meta T4 | Por qué importa |
|---|---|---|
| Piezas publicadas con verificación automática | 100 % | la vara dejó de ser manual |
| Fichas con `medido_en` dentro del umbral | ≥ 90 % | frescura demostrada, no afirmada |
| Fichas con atestación firmada | ≥ 80 % | procedencia verificable por terceros |
| Tiempo medio de verificación por pieza | ≤ 20 min | viabilidad económica del corpus |
| Erratas publicadas con corrección | 100 % | credibilidad |
| Informes L1 entregados | ≥ 8 | caja |
| Retención de suscripción a 6 meses | ≥ 70 % | producto, no curiosidad |
| Ingreso recurrente sobre total | ≥ 60 % | empresa, no proyecto |
| Dependencia de plataformas prestadas | ≤ 50 % del alcance | soberanía de canal |

---

## 11. Decisiones que solo el dueño puede tomar

1. **Licencia.** ¿CC BY-SA 4.0 para contenido + MIT para código + CC BY 4.0 para datos? Sin esto, nada de lo demás se puede firmar. Es la decisión más urgente y la más barata.
2. **Marca y dominio.** ¿Se registra "La Bandita" y se compra dominio propio este trimestre?
3. **Canal primario.** ¿WhatsApp sigue siendo la puerta de entrada con lista propia detrás, o se apuesta primero a la web? Recomendación: WhatsApp como puerta, web como casa.
4. **Línea de arranque.** ¿L1 (debida diligencia B2B) o L2 (suscripción) primero? Recomendación: L1 por caja y credibilidad; L2 en paralelo por lista.
5. **Política de patrocinio.** ¿Se acepta dinero de proyectos que la serie mide? Recomendación: sí, con divulgación obligatoria en la misma pieza y sin capacidad de veto editorial.
6. **Servidor MCP.** ¿Se publica `labandita-registro` en abierto? Recomendación: sí, en lectura y con atestaciones; es el diferenciador y el gancho de la línea L3.
7. **NLnet.** Fecha límite 3 de noviembre de 2026. ¿Se presenta propuesta escrita por el dueño (con este documento como base) declarando el uso de IA y sus registros? Si no se decide hoy, se pierde la ventana.

---

## 12. Anexos de esta entrega

| Archivo | Qué contiene |
|---|---|
| `datos/medicion-2026-10-31.json` | la medición cruda del repositorio que sostiene el diagnóstico |
| `anexos/ficha.schema.json` | contrato de datos v1 para las fichas del registro |
| `datos/ejemplo-ficha.json` | una ficha real escrita contra ese contrato |
| `anexos/vara-ci.yml` | plantilla de integración continua con las ocho compuertas |
| `propuesta-la-bandita.html` | esta propuesta como presentación web autocontenida |

**Lo que este documento no es.** No es una promesa de ingresos: los números de la sección 4 son supuestos declarados. No es un plan aprobado: es una propuesta con decisiones abiertas. No es una medición de mercado dominicano: la única cifra nacional citada viene de la ONE a través de su difusión pública de julio de 2026, y el resto del contexto competitivo queda pendiente de medición primaria. Y no sustituye al dueño en la decisión editorial, que es la única cosa de este proyecto que no se delega ni se automatiza.

---

*La Bandita verifica antes de recomendar — y ahora también antes de vender. 31 de octubre de 2026.*
