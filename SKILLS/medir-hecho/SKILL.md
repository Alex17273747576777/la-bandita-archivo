---
name: medir-hecho
version: 1.0.0
dominio: medición
nivel: medidor
cuando: cuando la pieza no mide repositorios sino hechos: fechas, dominios, obras, cronologías, hashes
entradas: [tema de la pieza]
salidas: [fichas con campo "hecho" y "valor", cada una contra su fuente primaria]
herramientas: [Wikidata, MusicBrainz, RDAP, dig, curl -sI, git log, hashlib, tools/medir_personales.py]
verificacion: [cada valor tiene fuente, los no medidos escriben "aquí no hay"]
depende_de: [arranque-de-suelo]
---

# Habilidad · medir un hecho

## Propósito
Medir lo que **no es un repositorio** sin caer en dos trampas: inventar el dato o rellenarlo con una
estimación. Cada tema pide su instrumento, y la habilidad consiste en elegir el correcto.

## Cuándo se usa
- Piezas personales, culturales o de suceso (no de catálogo de programas).
- Cuando la pieza habla de una película, un disco, un dominio, una vida o un archivo.
- Cuando el dueño pide «rechequea adaptado a cada tema».

**No se usa** para recomendar ni para opinar: mide y deja el dato; la opinión va aparte y marcada.

## El catálogo de instrumentos
| Se mide | Instrumento | Se lee |
|---|---|---|
| Fechas de una obra o de una vida | Wikidata `Special:EntityData/{QID}.json` | `P577` estreno · `P569` nacimiento · `P570` muerte |
| Discografía | MusicBrainz `/ws/2/release-group?artist={mbid}` | clave **`release-groups`** |
| Un dominio | RDAP del registro + `dig +short` + `curl -sI` | `status`, fechas, IP, código HTTP |
| Una cronología de trabajo | `git log --pretty=%ad --date=short` | commits por día y huecos |
| Un archivo | `hashlib.sha256(...).hexdigest()` | 64 dígitos; y otra vez con un byte cambiado |

## Pasos
1. Elegir el instrumento del catálogo. Si el tema no está, **se dice** que no hay instrumento y no se
   escribe cifra.
2. Buscar el identificador **antes** de usarlo: `wbsearchentities`. Nunca suponer un QID.
3. Confirmar que la entidad es lo que se cree leyendo qué dice de sí misma (`P31` y su etiqueta),
   no comparando contra un QID elegido a mano.
4. Consultar y **guardar el crudo** junto a la ficha, para que el cotejo pueda volver a la fuente.
5. Escribir la ficha con dos campos: `hecho` y `valor`. `null` cuando no se midió, con nota de por qué.

## Reglas duras
- **Jamás suponer un identificador.** Dos QID supuestos en esta casa resultaron ser un videojuego y
  una banda sonora. Se buscan, se comprueban y solo entonces se aceptan.
- **La salud de una persona no se mide.** Se dice «aquí no hay» y se sigue.
- **Los nombres de las claves importan.** Leer `release-group` donde la fuente publica
  `release-groups` devuelve cero y hace parecer vacía una fuente que está llena.
- **Una fuente que parece vacía es la mentira más fácil de creerse**: antes de publicar un cero,
  comprobar el lector.

## Verificación
- Cada `valor` no nulo tiene su consulta detrás, guardada en `crudo`.
- Los `null` llevan nota.
- El cotejo de la pieza puede reproducir cada cifra desde el JSON.

## Errores conocidos
- Cortar fechas con un índice fijo: `"+1997-12-05T00:00:00Z"[1:11]` es correcto, `[:10]` deja `+1997-12-0`.
- Filtrar películas por `P31 = Q11424` cuando la animada se declara `Q202866`: se pregunta por la
  etiqueta, no por un número elegido a mano.
