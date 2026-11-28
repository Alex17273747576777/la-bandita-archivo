# Checksum del corte de 37 · corrección medida el 2026-11-28

*Qué estaba mal, cómo se comprobó y qué dicen los números nuevos.*

---

## 1 · El error

El dato del 2026-11-27 traía un campo llamado `has_sha256_asset`. Ese nombre prometía una cosa
—«el proyecto publica un SHA-256»— y medía otra: **la API de GitHub calcula un `digest` para cada
archivo que sirve**, así que cualquier repo con un binario adjunto salía marcado como «sí».

Resultado: **9 repos marcados con checksum**. Comprobado uno por uno contra el endpoint de la
release, **solo 7 publican algo**, y de esos 7 hay dos casos que el nombre tapaba:

| Repo | `has_sha256_asset` | Qué hay de verdad |
| :--- | :--- | :--- |
| `Kareadita/Kavita` | sí | **No** publica checksum: los 8 adjuntos solo tienen `digest` de la API |
| `mihonapp/mihon` | sí | **No** publica: 6 adjuntos, todos con `digest` de la API |
| `predidit/Kazumi` | sí | **No** publica: 9 adjuntos, todos con `digest` de la API |
| `Suwayomi/Suwayomi-Server` | sí | **Sí**: `Checksums.sha256` con 9/9 archivos |
| `null2264/yokai` | sí | **Sí**: tabla de hashes en las notas, 5/5 coinciden con el `digest` |
| `Kototoro-app/Kototoro` | sí | **Sí** (16 adjuntos) |
| `ReitanSora/koeyomi` | sí | **Sí** |
| `ProjectNox-org/nox-extension-developer` | sí | **Sí** |
| `loeuf237/animelab` | sí | **Sí** |

Y el error va en las dos direcciones: **`akitaonrails/FrankYomik` publica checksum y el flag decía
que no**. Balance del campo viejo: 9 marcados, de los cuales 3 eran falsos (Kavita, mihon, Kazumi)
y a la vez se le escapó 1 verdadero (FrankYomik). 9 marcados → **7 reales**, por caminos distintos.
Eso es exactamente lo que pasa cuando un campo mide «hay un hash en la respuesta» en vez de «el
proyecto publicó un hash».

## 2 · Los números nuevos, sobre los 37

| | |
| :--- | ---: |
| Repositorios remedidos | **37 de 37** |
| Publican checksum de verdad | **7** · **18,9 %** |
| Solo tienen `digest` de la API | **28** |
| Ni una cosa ni la otra | **2** — `keiyoushi/extensions-source` y `ProjectNox-org/project-nox-importer` |

**El 18,9 % es el número que hay que publicar.** El «5 de 5 · 100 %» de los referentes y el
«9 de 37» del tablero eran ambos la misma confusión: contar el `digest` del servidor como si fuera
una firma del proyecto.

## 3 · Qué cambió dónde

| Dónde | Antes | Ahora |
| :--- | :--- | :--- |
| `medidos-37-repos-2026-11-27.json` | `has_sha256_asset` | **intacto**: es el registro de lo que se midió aquel día, con su error |
| `medidos-37-repos-2026-11-28-remedido.json` | — | campos nuevos: `checksum_publicado`, `digest_api`, `checksum_detalle`, `checksum_remedido_en` |
| Hoja `Repos_Medidos_37` | columna J «SHA-256/checksum» = Sí/No | J «Checksum publicado por el proyecto» · L «Digest de la API (no es checksum publicado)», 37 filas |
| `web/observatorio/` y `datos.json` | «5 de 5 · 100 %» | «2 de 5 · 40 %» publicado, «5 de 5» digest (commit `8c0ea1b6`) |

El dato viejo **no se borra**. Un registro que se corrige borrando lo anterior no permite auditar
cómo se llegó al error; uno que conserva las dos versiones sí.

## 4 · Lo que esto NO dice

- **No dice que los binarios sean seguros.** Un checksum publicado prueba que la descarga coincide
  con lo que el proyecto dijo; no prueba que el proyecto sea de fiar.
- **No se descargó ni un binario** para comprobar los 7 checksums publicados. Se comprobó que el
  archivo o la tabla **existen y cubren los adjuntos**; la verificación byte a byte queda declarada
  como pendiente.
- **Los 28 con `digest` no están desprotegidos**: GitHub calcula el hash al servir el archivo, y eso
  detecta una descarga corrupta. Lo que no sobrevive es una release reemplazada.
