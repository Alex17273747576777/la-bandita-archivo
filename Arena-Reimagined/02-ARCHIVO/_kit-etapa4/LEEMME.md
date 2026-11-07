# KIT DE ENTREGA — CAMPAÑA CANON (E0–E4), LA BANDITA
Estado: pre-publicación. E5 (publicación) solo bajo orden expresa del dueño y con su
satisfacción total. Este kit fue armado por el taller al servicio del dueño; el proceso
completo, con cifras medidas, vive en `actas/registro-2026-10-14.md`.

## Contenido
- `fuentes/` — 5 piezas del canon: TRATADO, MANUAL, LECCIONES (.md, navegación reconstruida
  bajo orden expresa del dueño: SOLO targets de anclas; palabras del autor intactas byte-a-byte)
  y CANON-CIMIENTO + COMPENDIO (HTML legacy, intactos: sello original sin cambios).
- `envases/` — 5 ediciones XHTML autocontenidas (0 recursos externos, 0 peticiones, offline,
  imprimible; búsqueda, tema auto/claro/oscuro, navegación con scrollspy).
- `mapa/` — MAPA-CANON.json (inventario total, regenerable byte-a-byte con
  `python3 herramientas/mapa-canon.py --verify`), DEMOLICION-CONTENIDO.json (demolición E1) y sello.
- `capturas/` — 10 evidencias visuales (5 escritorio-claro + 5 móvil-oscuro), Etapa 3.
- `herramientas/` — el taller completo (mapa, reparador de TOC, demolición, vara E1,
  batería estática, batería viva, convertidor).
- `actas/` — registros fechados 10/11/14-oct-2026. Append-only.

## Cadena de sellos (sha256, primeros 16 hex)
Fuentes .md — antes → después (mutación autorizada: solo targets de anclas):
- TRATADO:   3c58d9f907205f3a → 580fcd21c339617c446073a6e5ea11cb0230ca0720d7f6cf3adf816074d10078
- MANUAL:    c4c33f44c02cdeef → e958ef0e35f59fb3786ab90f01c4560bfac1896497d60c7bc36e3c48b759e5ee
- LECCIONES: 1539dfcf753bb4d3 → 89b700fdce25ce2261abbea49043ab383d47911e6dba4d1cc5e114d892c88c3a
Fuentes HTML legacy — INTACTOS (sello del 11-oct sin cambios):
- CIMIENTO:  f517f6b7b301d6bf
- COMPENDIO: 07830c49e685aa16
Envases XHTML finales (esta cocción):
- TRATADO: 1523239 B · `301b32b8ae31cdbd36d5bd89fc03477a8537457311e09511230ec07cbc5cd5c8`
- MANUAL-COMPLETO: 627674 B · `9b2b15fb938d4288f915033b63165bdc67abbcbeee3d4860c2b38c2e404724fe`
- LECCIONES-ALEXIS: 68323 B · `10c27b7ff8593742adf9df574753247777e64366eee8e903cdda8cfe265add0d`
- CANON-CIMIENTO: 39678 B · `9bdff926c95497fe0b590a9670d3ee165aedadb548c28b3bbd69b39aa8565c4f`
- COMPENDIO-INTEGRAL: 37332 B · `7800d0b2d4af83d068d62b8aae4f52da03c15c7623c6101c5ecaa6bf1530738d`
Navegación medida en los envases de ESTE kit — anclas muertas: TRATADO=0, MANUAL-COMPLETO=0, LECCIONES-ALEXIS=0, CANON-CIMIENTO=0, COMPENDIO-INTEGRAL=0 (0 en las 5).

## Verificación (todo corre desde la raíz del kit extraído)
1. `sha256sum -c SHA256SUMS.txt`
2. `python3 herramientas/mapa-canon.py --verify` (requiere la estructura del repo; en el kit
   el mapa viene sellado en `mapa/sello.txt`)
3. `python3 herramientas/bateria-funcionamiento.py` (batería estática 5×11)
4. Abrir cualquier `envases/*.xhtml` en un navegador: consola limpia, deep-links, `/` busca,
   tema, móvil sin desborde horizontal (batería viva: 5/5, acta 14-oct).

## Doctrina
Regla de oro (Art. D-007): «Ninguna derogación se ejecuta en silencio. Cada una lleva su
fila, su fecha y su firma. Así se corrige sin mentir sobre el pasado.» — Esta entrega es
esa fila. Mejor que lo que precedió, nunca perfecto.
