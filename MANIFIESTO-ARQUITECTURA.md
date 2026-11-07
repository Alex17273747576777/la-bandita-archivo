# Manifiesto de arquitectura

Reglas de la casa para que este repositorio siga siendo mantenible dentro de dos años. No son
sugerencias: son el criterio con el que se acepta o se rechaza un cambio.

## 1 · Principios

1. **Una fuente de verdad por cosa.** La ley está en `CIMIENTOS/` y en `corpus-la-bandita/`; las
   piezas, en `01-PUBLICACIONES`; los datos medidos, en `registry/` y `docs/envios/`. Todo lo demás
   enlaza, no copia. Cuando dos documentos dicen lo mismo con palabras distintas, uno de los dos se
   convierte en enlace y se borra su cuerpo.
2. **El Markdown es fuente; el HTML es salida.** `site/` es un artefacto: se regenera con
   `python3 tools/sitio.py` y no se edita nunca a mano. Si el HTML está mal, la pieza está mal.
3. **Lo generado se marca como generado.** Todo archivo que una herramienta pueda reproducir lleva
   cabecera o convención de nombre que lo diga (`site/`, `docs/envios/`, `datos/registro.json`).
4. **Lo que no se midió, no se escribe.** Un hueco declarado (`NO CONSTA`, «sin paquete») vale más
   que una estimación: el hueco se puede cerrar mañana, la estimación se queda para siempre.
5. **Autocontención.** Cero CDN, cero fuentes remotas, cero rastreadores en el frontend. El sitio
   abre igual desde un pendrive, desde un teléfono y desde GitHub Pages.
6. **Las llaves no entran.** Tokens fuera del árbol; ninguna herramienta los escribe en un archivo
   versionado. Si aparece uno en un `git status`, se rota y se limpia el historial del commit.

## 2 · Dónde va cada cosa

| Si es… | va a | y su nombre empieza por |
|---|---|---|
| Una norma que obliga | `CIMIENTOS/` | número de orden (`01-`, `02-`) |
| Una habilidad ejecutable | `SKILLS/<slug>/SKILL.md` | el slug, en minúsculas y guiones |
| Un procedimiento con pasos | `PROCESOS/` | número de flujo |
| Una pieza publicable | `Arena-Reimagined/01-PUBLICACIONES/<canal>/` | número de pieza, `NN-` |
| Un acta o política fechada | `docs/` | MAYÚSCULAS y `-AAAA-MM-DD` |
| Un dato medido | `registry/` o `docs/envios/` | según lo genere la herramienta |
| Un script | `tools/` | verbo en minúsculas (`medir_`, `atestar`, `sitio`) |
| Legado que no se edita | `_archivo-historico/` | tal como llegó, con manifiesto |

## 3 · Convenciones de nombre

- Fechas en `AAAA-MM-DD`, siempre, sin excepción, y con hora cuando el dato la necesita.
- Sin espacios en rutas de código; con espacios solo en documentos heredados que ya se citan así.
- Un archivo, un asunto: `POLITICA-DUPLICADOS.md` no contiene también la política de licencias.
- Los números de versión de skills usan semver: `1.0.0`, y suben cuando cambia el procedimiento.

## 4 · Qué se considera «sobrante»

Sobra, y se retira:

- una copia de un documento que ya existe en su sitio, sin diferencia de contenido;
- un artefacto regenerable que se puede reconstruir en un comando (`site/` viejo, `__pycache__`);
- un ZIP de una etapa ya publicada, cuando su contenido está en el árbol y en el historial;
- un borrador superado por una versión posterior, si el acta de la corrección ya lo cita.

**No sobra** y no se toca sin acta: piezas publicadas, actas, mediciones, sellos y todo lo que
sostiene una afirmación pública. Borrar una pieza sin borrar su envío rompe la compuerta G9; borrar
una ficha sin actualizar el registro rompe G1. El orden de retirada es: acta → pieza → envío → sello.

## 5 · Ritmo de mantenimiento

- **Cada pieza:** gate M01–M23 y anotación en `docs/bandas.json`.
- **Cada lote:** `envio.py`, `vara.py`, `acta_conformidad.py`, `atestar.py`, commit y CI.
- **Cada semana:** `tools/duplicados.py` y `tools/idioma_mojibake.py`; lo que cante, se arregla.
- **Cada mes:** regenerar `site/`, revisar `docs/PENDIENTES.md` y podar el legado con acta.

---

## Exportaciones: fuera del repositorio

`paquetes/` (11 archivos, 62,20 MB de ZIP y un `git bundle`) se retiró el **2-nov-2026** con acta en
`docs/ACTA-LIMPIEZA-2026-11-02.md`. Regla desde entonces:

| Si es… | Va a… |
|---|---|
| Un ZIP, bundle o tar del propio repositorio | **fuera del árbol** (carpeta de entregas del día), nunca versionado |
| Un export que el dueño pide | se genera desde el árbol en ese momento, con fecha del día |
| Un paquete de terceros (APK, release ajeno) | **no entra nunca** al repositorio |

Motivo: un paquete versionado crece en cada clon, se confunde con el estado actual y no aporta datos.
El `.gitignore` bloquea `paquetes/` para que no vuelva por descuido.

## Sobre los duplicados «documentales»

`tools/duplicados.py` informa de ~441 copias idénticas. **No todas son sobrante.** Distinguir es parte
del oficio:

- **Sobrante real:** dos copias del mismo archivo en la misma función (respaldo redundante, export
  viejo). Se retira con acta.
- **Duplicado documental:** la misma pieza en la carpeta del canal y en el conjunto fechado de
  publicación. Prueba **qué se publicó y cuándo**: se conserva y se declara.
- **Traducción:** texto distinto por idioma, aunque comparta estructura. Se conserva siempre; si es
  copia del español con otro sufijo, es un error que se corrige traduciendo o retirando, no fingiendo.

Antes de borrar por duplicado: ¿qué prueba este archivo que el otro no pruebe? Si no hay respuesta, se
queda.
