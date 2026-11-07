# Taller de la pieza 15 · cómo se generó el texto

Los tres programas de esta carpeta generan el cuerpo de la pieza **desde la medición**, no desde
la memoria. Se ejecutan en este orden y escriben `s1.md`, `s2.md`, `s3.md` (el `.md` publicado es
la suma de los tres).

```
python3 docs/talleres/pieza15/a15.py   # cabecera, mapa, en una página, tabla de reemplazos
python3 docs/talleres/pieza15/b15.py   # el motor, las caras del motor, el escritorio
python3 docs/talleres/pieza15/c15.py   # bolsillo, terminal, camada de 2026, la ley, huella, enlaces
```

Dependen de `d15.py`, que lee `docs/MEDICION-15b-noche-2026-11-04.json` y
`docs/ESCRUTINIO-2026-11-04.json`. **Si se vuelve a medir, el texto cambia solo**: por eso una cifra
no puede escribirse a mano.

Regla del taller (H22): el generador vive en el repositorio; el clon de trabajo, no.
