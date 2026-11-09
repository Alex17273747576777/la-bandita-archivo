# DEPRECADOS · a dónde fue cada cosa

*Nada se borra sin reemplazo declarado. Este archivo existe para que un enlace viejo no lleve a un
hueco.*

---

## `Arena-Reimagined/HABILIDADES/` (7 habilidades y 6 herramientas)

Sustituido por `SKILLS/` el 9 de noviembre de 2026. **No se borra**: se queda como archivo histórico
con este aviso.

### Las habilidades

| Archivo viejo | Ahora vive en | Qué se conservó |
|---|---|---|
| `CORAZON.md` — principios del dueño | `SKILLS/README.md` § *Las reglas que mandan sobre todas* | las 10 reglas, en una lista que se puede citar |
| *Arranque de suelo firme* | `arranque-de-suelo` | inventario → hash → restaurar, y las tres cifras del inicio |
| *Verificación multinivel* (L0–L4) | `arranque-de-suelo` + `cotejar-cifras` + `compuerta-manual` | la separación **puerta / medidor** |
| *Pulso de repos* | `medir-recurso` | la semántica 404/451/403/429 |
| *Licencias sin inventar* | `medir-recurso` | el orden SPDX → endpoint → texto → ausencia |
| *Pieza editorial* | `escribir-pieza` | verificar en fuente primaria → escribir → dedupe → lupa |
| *Guardado en GitHub* | `sellar-y-publicar` | espejo → commit → push → verificación por blobs |
| *Formato respirable* | `escribir-pieza` | la secuencia de palabras idéntica antes y después |
| `bitacora-lecciones.md` (L-01…L-07) | `SKILLS/LECCIONES.md` bloque 1 | las siete, con su número |
| `EVOLUCION.md` | `SKILLS/LECCIONES.md` + el `version:` de cada frontmatter | la versión ahora vive en la habilidad |

### Las herramientas

| Archivo viejo | Estado | Nota |
|---|---|---|
| `herramientas/arranque.py` | **vivo** | se sigue usando; lo llama `arranque-de-suelo` |
| `herramientas/pulso.py` | **vivo** | lo llama `medir-recurso` |
| `herramientas/guardar.py` | **vivo** | lo llama `sellar-y-publicar` |
| `herramientas/chequeo-niveles.py` | **vivo** | lo llama `compuerta-manual` |
| `herramientas/aprender.py` | **vivo** | es el ejecutor de `corregir-a-la-vista` |
| `herramientas/vara-simulada.py` | **vivo** | banco de pruebas de las compuertas |

Las seis herramientas siguen donde estaban: la fusión movió **la documentación**, no los ejecutables.
Mover código que funciona solo para dejarlo más ordenado es la clase de orden que rompe cosas.

---

## `SKILLS/` (las 7 anteriores)

Ninguna se perdió. Las siete entraron en la fusión con lo que les faltaba:

| Antes | Ahora | Qué se le añadió |
|---|---|---|
| `medir-recurso` v1.0.1 | v2.1.0 | seguir desvíos 301 por número de repositorio; nombres mudados |
| `censo-de-pieza` v1.0.0 | v2.0.0 | límites de palabra; el ruido se narra; la 05 se coteja contra la unión |
| `escribir-pieza` v1.0.2 | v2.0.0 | el encabezado como contrato; corregir hacia adelante; el párrafo que no se repite |
| `compuerta-manual` v1.0.0 | v1.1.0 | puerta contra medidor, explícito |
| `envio-canal` v1.0.1 | v1.2.0 | el registro no es una lista cerrada; bandas como herramienta |
| `sellar-y-publicar` v1.0.1 | v2.0.0 | el `-F` y el `$`; el testigo del push |
| `informe-al-dueño` v1.0.0 | v1.1.0 | los fallos propios son la información más útil |

---

## Lo que **no** se deprecó

- `tools/` — las 70 y pico herramientas siguen igual. Las habilidades las llaman.
- `docs/almas/` y `docs/MEDICION-*` — el sistema de medición no cambió.
- El manual de estilo v3.0, las bandas y el LEEME — siguen siendo la fuente de verdad de formato.

---

*Si encuentras un enlace a algo de esta página y no sabes a dónde va, la respuesta está en la tabla de
arriba. Si no está, es un fallo de esta fusión y se anota como lección.*
