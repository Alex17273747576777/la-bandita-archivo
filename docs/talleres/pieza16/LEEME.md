# Taller de la pieza 16 · cómo se generó el texto

Los cinco programas de esta carpeta generan el cuerpo de la pieza **desde la medición**, no desde
la memoria. Se ejecutan en este orden y escriben `s1.md`, `s2.md`, `s1b.md` y `s3.md`; el `.md`
publicado es la suma, con `s1b` insertado antes de la tabla de reemplazos.

```
python3 docs/talleres/pieza16/a16.py   # cabecera, mapa, en una página, medición, reemplazos
python3 docs/talleres/pieza16/b16.py   # los siete clientes, la camada de 2026, los automatizadores
python3 docs/talleres/pieza16/c16.py   # los tres con enlace, responsabilidad, huella, órdenes, cierre
python3 docs/talleres/pieza16/e16.py   # cómo funciona, tabla completa, glosario, configuraciones
```

Dependen de `d16.py`, que lee `docs/MEDICION-16-noche-2026-11-04.json`,
`docs/ESCRUTINIO-2026-11-04.json` y la lista `docs/LOTE-16-recursos-2026-11-04.md`. **Si se vuelve a
medir, el texto cambia solo**: por eso una cifra no puede escribirse a mano (H22).

Regla del taller: el generador vive en el repositorio; el clon de trabajo, no.
