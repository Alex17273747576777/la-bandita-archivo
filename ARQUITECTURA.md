# ARQUITECTURA

*Cómo está hecho este repositorio, por qué está hecho así y qué se puede comprobar de lo que declara. Actualizado el 3 de noviembre de 2026.*

**TL;DR —** el repositorio tiene **tres capas** (ley, oficio, producto) y **un solo sentido del dato**: se mide, se guarda, se escribe la enseñanza, se genera el producto y se sella todo. La regla que decide qué es código y qué es texto es una sola frase: **lo que es dato se genera, lo que es enseñanza se escribe**. Hoy: 33 herramientas, 17 compuertas, 6.838 fichas medidas, 70 fichas de guía en 12 capítulos y 2 canales con 5 piezas publicadas cada uno. Quien quiera el detalle de cada programa tiene `docs/CODIGO.md`; quien quiera el mapa de carpetas tiene `MAPA-DEL-ARCHIVO.md`.

---

## 1 · Las tres capas, y por qué están separadas

| Capa | Dónde vive | Qué contiene | Quién la cambia |
|---|---|---|---|
| **Ley** | `CIMIENTOS/` · `corpus-la-bandita/` · `PROCESOS/` · `SKILLS/` | Principios, precedencia, criterios obligatorios, manual de estilo, contrato de datos, raya legal | Se cambia poco y se cambia en acta |
| **Oficio** | `tools/` · `registry/` · `schemas/` | Las 31 herramientas, las 9.472 fichas medidas y los esquemas que las validan | Cada vez que se mide o se corrige un método |
| **Producto** | `guia-maestra/` · `Arena-Reimagined/01-PUBLICACIONES/` · `site/` | La guía de doce capítulos, las piezas de los dos canales y el sitio generado | Cada publicación |

La separación no es decorativa. Una ley que se puede tocar mientras se publica deja de ser ley; un producto que depende de una herramienta no documentada deja de ser producto y pasa a ser el recuerdo de quien lo hizo. Con las tres capas separadas, **cualquiera puede auditar el producto contra la ley sin leer una línea de código.**

---

## 2 · El sentido del dato, en cinco pasos

```
   fuente primaria                registro              texto               producto
 ┌────────────────┐   medir   ┌──────────────┐  escribir ┌───────────┐ generar ┌───────────┐
 │ GitHub, forjas │ ────────► │ registry/    │ ────────► │ guia y    │ ──────► │ sitio/    │
 │ y archivos     │           │ 9.472 fichas │           │ piezas.md │         │ y envíos  │
 └────────────────┘           └──────────────┘           └───────────┘         └───────────┘
          ▲                           │                        │                     │
          │        compuertas: vara, manual_gate, novedad_gate, firma_literal        │
          └───────────────────────────┴────────────────────────┴─────────────────────┘
                                    sello: atestar.py (SHA-256 encadenado)
```

1. **Medir.** `pulso`, `censo_medir`, `extraer_fresco` y `ficha_profunda` preguntan a la fuente primaria y guardan la respuesta cruda. Nunca se copia una cifra de una captura ni de una nota de prensa.
2. **Guardar.** `registro_construir` convierte lo medido en fichas JSON validadas contra `schemas/ficha.schema.json`. Un campo que falta no se rellena: se declara.
3. **Escribir.** La enseñanza —los doce capítulos, las piezas de canal— es el único texto escrito a mano. No se genera, porque un texto generado a partir de otro texto generado no enseña.
4. **Generar.** `guia_maestra.py`, `sitio.py` y `envio.py` producen índice, páginas, créditos y mensajes. Nadie escribe a mano una tabla de setenta filas.
5. **Sellar y comprobar.** `atestar` sella; `vara` juzga; `autoprueba` comprueba que el juez sabe fallar.

---

## 3 · Decisión: por qué el árbol se sella y encadena

**Contexto.** Un archivo que presume de verificar tiene que poder demostrar que lo que el lector está leyendo es lo que se publicó. Sin eso, cualquiera puede cambiar una coma y el archivo sigue diciendo «verificado».

**Decisión.** Sellar el árbol completo con SHA-256 y **encadenar cada lote con la huella del anterior**, y firmar el manifiesto con Sigstore en modo sin llave desde la integración continua.

**Consecuencia.** Cualquier cambio, incluso de un byte, rompe la compuerta G5 hasta que alguien vuelva a sellar y lo firme de nuevo. El coste es real: cada edición exige una corrida completa. El beneficio es que la afirmación «esto es lo que se publicó» deja de ser una promesa y pasa a ser una verificación de treinta segundos.

**Alternativa descartada.** Firmar solo los documentos importantes. Se descartó porque decidir qué es importante es justo lo que se hace mal cuando hay prisa, y porque el archivo histórico también se cita.

---

## 4 · Decisión: por qué el presente vive separado del pasado

**Contexto.** Las dos carpetas de canal llegaron a tener 119 y 113 archivos al mismo nivel, con **números repetidos** —dos piezas 04 y dos 05— porque convivían tres series distintas. Quien abría la carpeta no sabía qué era presente.

**Decisión.** La raíz de cada canal contiene **solo el ciclo vivo** (01–14) más un `LEEME-de-la-carpeta.md` con el estado; todo lo anterior vive en `_ARCHIVO-HISTORICO/<mes>/`, y en la raíz del repositorio las carpetas de memoria están bajo `ARCHIVO-HISTORICO/`.

**Consecuencia.** El presente se ve en una pantalla y el pasado conserva su fecha y su sitio. Lo que se gana en claridad se paga en rutas más largas, y ese precio se amortiza con un mapa: `MAPA-DEL-ARCHIVO.md`, que traduce las rutas anteriores para que ninguna acta vieja mienta.

**Regla de convivencia.** Lo archivado **no se reescribe**: se conserva con sus fallos. Lo que se corrige se corrige hacia adelante, en la pieza siguiente, y la corrección se anota.

---

## 5 · Decisión: un punto de entrada, no treinta y uno

**Contexto.** Un repositorio con 31 herramientas y 15 compuertas es hostil para quien llega. La documentación perfecta no arregla eso si el primer comando no está claro.

**Decisión.** Un `Makefile` con diecisiete destinos y un `doctor.py` que dice en cinco bloques si la máquina puede trabajar y en qué estado está el árbol.

```
make doctor      # ¿está todo en su sitio?
make verificar   # registro + sello + vara + autoprueba
make libro       # tablero de tareas e índice de documentos
make vencer      # qué ficha está vigente y cuál hay que volver a medir
make publicar    # sellar + libro + verificar, listo para empujar
```

**Consecuencia.** El arranque pasa de «lee el README y averigua» a dos comandos. Y el `doctor` falla a propósito cuando falta algo: su primera corrida en este repositorio detectó que `ARQUITECTURA.md` no existía —este documento— y se negó a decir LISTO.

---

## 6 · Decisión: la fecha la sostiene un archivo, no una promesa

**Contexto.** El registro declaraba 6.838 fichas medidas «hoy» cuando 4.186 tenían como única evidencia una fila del censo del 15 de octubre. La compuerta de frescura leía el campo `medido_en` —el mismo que estaba mal— y daba todo por bueno. Una compuerta que confía en el campo que vigila no vigila nada.

**Decisión.** Cada medición guarda su payload crudo en `registry/_evidencia/`, con la fecha **dentro del archivo**, y la ficha lleva su SHA-256. Una compuerta nueva (G16) compara la fecha declarada con la de la evidencia y detiene la línea cuando no coinciden.

**Consecuencia.** El repositorio crece con cada medición —unos 4 MB por tanda completa— y el árbol tarda más en sellarse. A cambio, «medido hoy» deja de ser una afirmación y pasa a ser un archivo que se puede abrir, fechar y verificar. La alternativa —confiar en el campo— es gratis y es lo que produjo el problema.

**Alternativa descartada.** Marcar como vencidas las fichas dudosas y seguir adelante. Se descartó porque no eran dudosas: eran medibles. Declarar vencido lo que se puede volver a medir es cambiar un dato malo por una etiqueta.

---

## 7 · Decisión: la memoria de un proyecto va dentro de su archivo

**Contexto.** `Arena-Reimagined/` tenía cinco carpetas de etapas anteriores al mismo nivel que el presente: `_versiones/`, `packs/`, `_herramientas/`, `_herramientas-casa/` y `_referencia/`. Quien abría esa carpeta veía catorce entradas donde tres eran el presente.

**Decisión.** Todo eso pasa a `02-ARCHIVO/_etapas-anteriores/`, que es la carpeta donde el propio proyecto ya guarda su memoria, y cada mudanza se anota en una tabla que una compuerta sostiene (G17). Las referencias se corrigen en el mismo cambio, y el auditor distingue una ruta vieja citada por un archivo vivo —fallo— de una citada por un acta —cita que se conserva—.

**Consecuencia.** Las rutas vivas son más largas, y un documento histórico que cite la ruta antigua necesita el mapa para traducirla. Se paga con un mapa y se gana lo único que importa: que la memoria no compita con el presente.

**Alternativa descartada.** Borrar lo que no se usa. Se descartó por la misma razón por la que no se borran las actas: la lupa de la etapa anterior y los packs viejos son la prueba de cómo se llegó hasta aquí, y una casa que borra su historia no puede explicar sus reglas.

---

## 8 · Divulgación de ingeniería: los números de hoy

Lo que se declara aquí se puede volver a medir con `make verificar`.

| Métrica | Valor del corte | Cómo se obtiene |
|---|---|---|
| Archivos sellados | ver el corte del sello | `atestar.py`, manifiesto SHA-256 |
| Fichas del registro | **6.838**: 6.560 vigentes y 278 sin objeto | `vencimiento.py` |
| Fichas de la guía | **70** en 12 capítulos | `guia-maestra/datos/apps/` |
| Herramientas | **33** en `tools/` + 1 generador | `indice_docs.py` |
| Compuertas de la vara | **17** (G0–G17) | `vara.py` |
| Piezas vivas por canal | **5 de 14** | `LEEME-de-la-carpeta.md` |
| Envíos verificados | **5 + 5**, cero fallos | `envio.py --verificar` |
| Documentos en `docs/` | 47 en 19 familias | `indice_docs.py` |
| Tareas abiertas | **12** | `tareas.py` |
| Dependencias externas del sitio | **0** | `sitio.py` (HTML y CSS propios) |
| Paquetes de terceros alojados | **0** | política de la raya legal |

**Lo que estos números no dicen.** No dicen que el archivo esté terminado: el ciclo de canal va por la pieza 5 de 14. No dicen que la guía sea la mejor posible: dicen que cada ficha tiene autor, licencia, versión y fecha, y que se puede volver a medir. Y no dicen que el método sea el único: dicen que es **repetible**, que es lo único que se puede exigir a un método.

---

## 9 · Mapa de componentes

| Componente | Responsabilidad | Documento |
|---|---|---|
| `tools/` | Medir, compuertas, sellar, publicar, decidir frescura | [`docs/CODIGO.md`](docs/CODIGO.md) |
| `registry/` + `_evidencia/` | La materia prima medida y el payload que la respalda | [`docs/VENCIMIENTOS.md`](docs/VENCIMIENTOS.md) |
| `registry/` + `schemas/` | La materia prima medida y su contrato | [`docs/INDICE.md`](docs/INDICE.md) |
| `guia-maestra/` | Datos, textos y páginas de la guía | `guia-maestra/README.md` |
| `Arena-Reimagined/01-PUBLICACIONES/` | Piezas del ciclo vivo, dos canales | `LEEME-de-la-carpeta.md` de cada canal |
| `docs/` | Actas, políticas, bandas, envíos y tableros | [`docs/INDICE.md`](docs/INDICE.md) |
| `ARCHIVO-HISTORICO/` | La memoria: todo lo anterior, con su fecha | [`MAPA-DEL-ARCHIVO.md`](MAPA-DEL-ARCHIVO.md) |
| `.github/workflows/vara.yml` | La puerta de la integración continua | este documento, §3 |

---

## 10 · Convenciones, con su fuente

No se inventan aquí: se adoptan convenciones que ya existen, para que un recién llegado no tenga que aprender un idioma nuevo.

- **Mensajes de confirmación** con la forma de [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/): tipo, alcance opcional, descripción, cuerpo y pies.
- **Registro de cambios** con el formato de [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) y numeración [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html).
- **Archivos de salud comunitaria** en la raíz y en `.github/`, según la [documentación de GitHub](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file): `README`, `CONTRIBUTING`, `SECURITY`, `CODEOWNERS`, plantillas de incidencia y de solicitud de cambio.
- **Licencia por archivo** siguiendo las prácticas de [REUSE 2.0](https://reuse.software/spec-2.0/) de la FSFE: identificador SPDX y titular, en la cabecera cuando el archivo lo permite, y en los metadatos del repositorio cuando no.
- **Métricas de salud del proyecto** con el [Scorecard de OpenSSF](https://github.com/ossf/scorecard), que es el mérito de terceros que la nota intenta usar cuando existe.

Adoptar una convención no es obedecerla por moda: es que otro pueda auditar sin preguntarnos nada.

---

## 11 · Lo que este repositorio no hace

- **No aloja paquetes de terceros.** Ni copia, ni espejo, ni enlace a un espejo cómodo.
- **No recomienda por fama.** Nueve de las setenta fichas tienen menos de 500 estrellas y cuatro menos de 100, y están porque resolvieron una tarea mejor que sus competidores famosos.
- **No borra su historia.** Lo archivado se conserva con sus fallos; lo sustituido queda en `_reemplazadas/` con su fecha.
- **No promete vigilancia.** Hay un calendario de remediciones, y lo que no se remide se declara vencido en su propia ficha.

*La Bandita informa a partir de fuentes fechadas.*
