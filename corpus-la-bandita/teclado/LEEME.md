# La biblioteca de instrucciones del teclado

Esta carpeta no es una lista de prompts: es el archivo del que salen las teclas de IA y los
atajos largos de un teclado Android. Se puede leer, se puede revisar y se puede volver a
exportar al formato de cada aplicación.

```
corpus-la-bandita/teclado/
├── prompts.json          la biblioteca: 10 teclas, 12 atajos y 5 macros, cada uno con su razón
├── FUENTES.json          los 11 teclados medidos, con la evidencia de cada función en su código
├── VERSIONES.json        última entrega, empujón y licencia de cada fuente (lo escribe sync_fuentes)
├── CREDITOS.md           quién hizo cada cosa y bajo qué licencia (lo escribe sync_fuentes)
└── exportado/            los tres formatos que genera lint_teclado --exportar
```

## Tres órdenes y ya

```
python3 tools/lint_teclado.py --exportar   # comprueba las 11 reglas y escribe exportado/
python3 tools/sync_fuentes.py              # pregunta a GitHub y reescribe VERSIONES y CREDITOS
python3 tools/lint_teclado.py --json       # el informe para el acta
```

`lint_teclado.py` devuelve 1 si algo falla, así que sirve dentro de cualquier cadena de
comprobación. No tiene dependencias: solo la biblioteca estándar de Python.

## Por qué diez teclas y no setenta y cinco

LeanType, el teclado que ejecuta instrucciones desde la barra superior, admite diez:
`KeyCode.CUSTOM_AI_1` … `CUSTOM_AI_10` en su `InputLogic.kt`. Ese tope está en `TOPE_TECLAS`,
en una sola línea. Lo que no cabe en una tecla va a los atajos, que son texto y no gastan
espacio en pantalla.

## Qué NO hace esto

No escribe dentro de la aplicación: los ajustes del teclado se configuran a mano la primera vez.
No sincroniza entre teléfonos por sí solo: eso lo hace Git. Y no mide si un modelo obedece —
eso pide ejecutar las teclas contra un modelo y leer la respuesta, y sigue pendiente.
