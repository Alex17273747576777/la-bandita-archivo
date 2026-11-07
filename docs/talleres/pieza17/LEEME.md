# Taller de la pieza 17 · cómo se generó el texto

Los cuatro programas de esta carpeta generan el cuerpo de la pieza **desde la medición**, no desde
la memoria. Se ejecutan en este orden y escriben `s1.md`, `s2.md` y `s3.md`; el `.md` publicado es
la suma de los tres.

```
python3 docs/talleres/pieza17/a17.py   # cabecera, mapa, en una página, medición, cómo funciona, reemplazos
python3 docs/talleres/pieza17/b17.py   # teclados, dictado, camada de 2026, escritorio, motor
python3 docs/talleres/pieza17/c17.py   # tabla completa, glosario, responsabilidad, huella, cierre, enlaces
```

Dependen de `d17.py`, que lee `docs/MEDICION-17-noche-2026-11-04.json`,
`docs/ESCRUTINIO-2026-11-05.json` y la lista `docs/LOTE-17-recursos-2026-11-04.md`. **Si se vuelve a
medir, el texto cambia solo**: por eso una cifra no puede escribirse a mano (H22).

Regla del taller: el generador vive en el repositorio; el clon de trabajo, no.
