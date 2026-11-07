# Taller de la pieza 19 · cómo se generó el texto

Los cuatro programas de esta carpeta generan el cuerpo **desde la medición**, no desde la memoria.
El `.md` publicado se ensambla así: `s1.md` + `c19a1` + `c19a2` + `c19b` + la cola de `s1.md` + `c19c` + `s2.md`.

```
python3 docs/talleres/pieza19/a19.py   # cabecera, mapa, en una página, medición, qué es una tienda, la tabla, el listón
python3 docs/talleres/pieza19/b19.py   # lo que no se indexa, responsabilidad, huella, órdenes, cierre, enlaces
python3 docs/talleres/pieza19/c19.py   # las siete aplicaciones, salir de Kotatsu, anatomía, las seis tiendas, la comunidad
```

Dependen de `d19.py`, que lee `docs/MEDICION-19-tiendas-2026-11-05.json`,
`docs/ESCRUTINIO-2026-11-05.json` y la lista `docs/LOTE-19-recursos-2026-11-05.md`, y lleva en
`INDICE` **las extensiones contadas a mano en cada índice publicado** el 5-nov-2026 entre las 09:45 y
las 09:52 AST. Esa tabla es la que hace que la pieza no repita las cifras de la wiki (H24).

Regla del taller: el generador vive en el repositorio; el clon de trabajo, no.
