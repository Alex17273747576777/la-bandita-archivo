# Taller de la pieza 19 (segunda versión) · cómo se generó

Esta pieza no se escribió desde la memoria: se escribió desde dos ficheros de datos y una herramienta.

```
python3 tools/auditar_tienda.py --repo keiyoushi/extensions --repo ... \
        --escribir docs/AUDITORIA-TIENDAS-2026-11-05.json
```

- `tools/auditar_tienda.py` · clona, lee `repo.json`, cuenta el catálogo real, comprueba la firma, pide un
  byte de una descarga con `Range: bytes=0-0` y devuelve veredicto con motivos.
- `docs/AUDITORIA-TIENDAS-2026-11-05.json` · quince fichas de veinte campos, 10:03–10:15 UTC del 5-nov-2026.
- `docs/MEDICION-19b-apps-2026-11-05.json` · las nueve aplicaciones con estrellas, licencia y último empujón.
- `cifras.py` · imprime todas las cifras que aparecen en la pieza, sacadas de los dos JSON. Sirve para
  comprobar que ninguna se escribió a mano.

`pieza.md` es el texto publicado. Los clones de trabajo **no** se guardan: se borran después de leerlos, y lo
que queda es la ficha.
