# 01 · Fabricar una pieza

**Entrada:** un tema con repos candidatos y la banda del canal.
**Salida:** un `.md` en `docs/envios/<canal>/` que pasa `manual_gate.py`.

> **Nota del 2026-11-27.** La serie de canal `Arena-Reimagined/01-PUBLICACIONES/` fue **retirada**
> el 2026-11-15 por orden del dueño (458 ficheros, Addendum de retiro del CORAZON). Este proceso
> apuntaba a esa carpeta y por eso describía una salida que ya no existe. Donde decía
> `Arena-Reimagined/01-PUBLICACIONES/<canal>/` se lee **`docs/envios/<canal>/`**, que es la ruta
> viva que gobierna `docs/REGLAS-DE-PUBLICACION-Y-ARCHIVO.md`.

## Secuencia

| # | Paso | Herramienta | Qué cierra el paso |
|---|---|---|---|
| 1 | Elegir tema y canal | `docs/PENDIENTES.md` | tema sin repetir de las últimas tres piezas |
| 2 | Medir los repos | `tres_lecturas.py` | N medidos, 0 sin leer |
| 3 | Censar | `_medicion-{canal}.json` | cifra madre elegida |
| 4 | Escribir el mapa | — | 5–12 secciones reales |
| 5 | Escribir el cuerpo en tandas | Método Feynman (4 pasos) | cada tanda ≥ 1.500 caracteres, sin jerga y con analogía fiel |
| 6 | Secciones fijas | — | ⚡ En una página · ❓ 6–12 · 📊 tabla+mitos+glosario · 🔗 enlaces |
| 7 | Cierre | — | diálogo → firma+remate → medición con hora → licencia → notas |
| 8 | Compuerta | `manual_gate.py --pieza` | VERDE |
| 9 | Registrar longitud | `docs/bandas.json` | dentro de banda |

## Reglas del proceso

- **No se escribe sin censo.** Si el censo no está, la pieza no empieza.
- **No se entrega sin verde.** Un rojo se corrige en el texto, no en la compuerta.
- **Una pieza, un tema.** Si aparecen dos temas, son dos piezas.
- **La hora del corte es un dato de la pieza**, no del reporte: va en el cuerpo.
- El paso 6 no se adelanta al 5: primero el contenido real, después la estructura fija.

## Salidas que deben quedar en el árbol

`docs/envios/<canal>/<pieza>.md` · `docs/envios/_medicion-<canal>.json`
actualizado · longitud anotada.
