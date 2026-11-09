---
name: medir-recurso
version: 2.1.0
dominio: medición
nivel: medidor
cuando: antes de citar cualquier repositorio, extensión o proyecto en una pieza
entradas: [lista de repos "owner/repo", canal]
salidas: [fichas medidas y fechadas, con estrellas, licencia, edad, actividad, entrega y sumas]
herramientas: [tools/tres_lecturas.py, tools/pulso.py, tools/licencias_resolver.py, GitHub API]
verificacion: [0 sin leer, campos dudosos descartados y anotados, ventana horaria registrada]
depende_de: [arranque-de-suelo]
---

# Habilidad · medir un recurso

## Propósito
Convertir un nombre de repositorio en un dato publicable: **medido, fechado y con su hueco declarado**
cuando algo no se puede leer. Lo que no se midió se escribe «aquí no hay»; nunca se estima.

## Cuándo se usa
- Al abrir una pieza nueva o reescribir una vieja con censo nuevo.
- Al revisar un dato que huele a viejo.
- Al comprobar si un repositorio sigue vivo antes de volver a citarlo.

**No se usa** para completar una tabla «más o menos»: si no hay medición, no hay fila.

## Pasos
1. Rotar el orden de la lista respecto de la medición anterior (que ningún orden favorezca un resultado).
2. `curl -s -H "Authorization: bearer $T" https://api.github.com/repos/{owner}/{repo}` por cada uno.
   Leer `stargazers_count`, `license.spdx_id`, `created_at`, `pushed_at`, `open_issues_count`, `archived`.
3. `.../releases/latest`: contar `assets` y, dentro de los nombres, los que llevan `.sha256`, `.sha512`,
   `.asc`, `.sig`, `sums` o `checksum`. Esa es la columna de **sumas** de la casa.
4. Licencia: si `spdx_id` es `null` o `NOASSERTION`, resolver con `tools/licencias_resolver.py`
   (orden SPDX → endpoint → texto del LICENSE → ausencia firmada). No convertir «sin licencia» en «MIT».
5. **Seguir los desvíos.** Si la API responde 301, leer `redirect_url`, extraer el número de
   repositorio y pedir `/repositories/{id}`. Así se llega al nombre de hoy **sin adivinar**. Anotar el
   nombre viejo y el nuevo.
6. Anotar la ventana horaria exacta (America/Santo_Domingo) para el bloque «Medición del corte».

## Reglas duras
- **404 es muerte; 451 es bloqueo; 403 y 429 son cuota, jamás muerte.** No se confunden.
- **No se inventan identificadores**: ni QID, ni nombres de paquete, ni rutas de repositorio.
- **Empujón ≠ entrega.** Se publican los dos y la brecha se calcula desde la entrega.
- **La fecha va con hora.** «Hoy» no es una fecha; «entre las 07:58 y las 09:12» sí.
- **Un repositorio mudado no es un repositorio muerto.** Se resuelve por número, se dice en la pieza
  y se anota en `docs/MUDANZAS-<fecha>.json`.

## Verificación
- El informe termina en `N medidos · 0 sin leer`.
- Cada fila tiene sus campos o su hueco declarado.
- Los nombres que hoy redirigen están resueltos y con su nombre viejo escrito.

## Errores conocidos
- Contar el empujón como entrega y escribir «actualizado hoy» sin mirar el paquete.
- Medir en dos tandas separadas por horas y declarar una sola ventana: se declaran las dos.
- Leer `index.min.json` de un repositorio de extensiones: devuelve 2 entradas donde hay 1.554.
