# El catálogo · una ficha por recurso, con lo medido y una guía de verdad

Esto no es una lista de enlaces. Es un archivo de fichas: cada recurso tiene la suya, con lo que se
midió el día que se midió, y —cuando está escrita— una guía que dice para qué sirve, cómo se usa y
cuándo no vale la pena.

## Cómo está hecho

```
catalogo/
├── recursos.json      qué recursos hay y a qué racimo pertenecen (se edita a mano)
├── medido.json        la medición de cada uno, con su fecha y su URL (lo escriben los programas)
├── SINCRONIA.json     última consulta a GitHub: qué cambió desde la medición
├── CREDITOS.md        quién hizo cada cosa y con qué licencia (generado)
├── INDICE.md          el mapa por racimo con el estado de cada recurso (generado)
├── LEEME.md           esto
└── <dueño>--<repo>/
    └── FICHA.md       la ficha del recurso
```

## Las dos mitades de una ficha

Una ficha tiene dos partes y solo una se genera:

- **Lo medido** —estado, estrellas, licencia, última entrega, qué dice su README, cómo se instala— se
  reescribe cada vez que se vuelve a medir. Lleva siempre la fecha y la hora de la consulta.
- **La guía** —entre los marcadores `<!-- GUIA:INICIO -->` y `<!-- GUIA:FIN -->`— se escribe a mano y
  **no se toca** al regenerar. Es la parte que responde a «¿me sirve?», que es la que no se puede
  automatizar.

Si una ficha dice «No hay guía escrita todavía», está medida pero no explicada: sirve para saber qué es
y en qué estado está, no para instalarla.

## Los cuatro programas

```
python3 tools/catalogo_medir.py                 # mide los recursos declarados en recursos.json
python3 tools/catalogo_ficha.py --indice        # escribe o actualiza las fichas y el índice
python3 tools/catalogo_sync.py [--actualizar]   # compara con GitHub y pone al día
python3 tools/catalogo_lint.py                  # las doce comprobaciones de las fichas
```

`catalogo_medir.py` guarda: estrellas, licencia, archivado, empujón, última entrega con fecha y número
de adjuntos, plataformas que menciona el README, las líneas donde habla de instalar, el primer párrafo
en prosa —citado como lo que el autor declara, no como una verificación— y seis banderas de texto
(¿pide root?, ¿pide Shizuku?, ¿pide Magisk?, ¿niega el soporte?, ¿se declara espejo?, ¿avisa de una
retirada?).

`catalogo_lint.py` revisa doce cosas. Dos son las que importan cuando el catálogo crece: **C11** marca
una frase larga que se repita en más del 15 % de las fichas —la señal de que el catálogo se ha vuelto
una plantilla— y **C12** exige que una guía escrita tenga al menos tres apartados propios.

## Los estados

```
● vivo      último empujón hace 30 días o menos
◐ lento     hasta un año
○ parado    más de un año, sin archivar (el peor caso: parece vivo)
✕ archivado o no contesta
```

Un recurso parado o archivado **no se borra**: se queda con su fecha y, si tiene heredero, con una
flecha al heredero. Media historia del software libre es eso.

## Cómo se añade un recurso

1. Se añade su `dueño/repo` al racimo que le toque en `recursos.json`.
2. `python3 tools/catalogo_medir.py --racimo <racimo>`
3. `python3 tools/catalogo_ficha.py --indice`
4. Se escribe la guía dentro de los marcadores, a mano.
5. `python3 tools/catalogo_lint.py` tiene que salir en cero.

## Lo que este catálogo no hace

No prueba las apps. Se mide el repositorio; no se ha instalado ni usado. Quien lo haga, que lo cuente
con fecha y versión: eso es lo que convierte una ficha en una fuente.
