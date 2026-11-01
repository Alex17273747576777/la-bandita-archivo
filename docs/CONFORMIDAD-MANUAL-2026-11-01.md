# CONFORMIDAD CON EL MANUAL DE ESTILO Y OPERACIONES V3.0

**Fecha del corte:** domingo 1 de noviembre de 2026, 11:41 de Santo Domingo (UTC-4).
**Documento puente:** `corpus-la-bandita/CIMIENTOS — criterios obligatorios y precedencia (1-nov-2026).md` (§5 remite aquí).
**Compuerta:** `tools/manual_gate.py` (M01–M16, M23), enchufada a `tools/vara.py` como **G11**.

Este documento no declara nada que no esté corrido. Cada cifra de la tabla sale de la corrida del
gate sobre los archivos, no de una estimación: si se edita una pieza, hay que volver a correrlo.

## 1 · Resultado de la corrida

```
python3 tools/manual_gate.py --verificar   →   VERDE 6 · VENTANA 0 · ROJO 0
python3 tools/vara.py                      →   fallos: NINGUNO (G11: 6/6 piezas VERDE)
```

## 2 · Pieza por pieza

| Pieza | Caracteres | Banda | Entradas del mapa | Párrafos en «En una página» | Preguntas | Enlaces con formato | Fichas ★N | Veredicto |
|---|---|---|---|---|---|---|---|---|
| FA 01 | 44.990 | dentro | 9 | 3 | 10 | 22/22 | 41 | VERDE |
| FA 02 | 44.353 | dentro | 12 | 3 | 10 | 33/33 | 86 | VERDE |
| FA 03 | 44.830 | dentro | 10 | 4 | 6 | 33/33 | 30 | VERDE |
| WH 01 | 63.094 | dentro | 8 | 3 | 9 | 29/29 | 67 | VERDE |
| WH 02 | 63.084 | dentro | 12 | 3 | 11 | 56/56 | 123 | VERDE |
| WH 03 | 63.007 | dentro | 12 | 4 | 8 | 33/33 | 64 | VERDE |

Las seis piezas de la serie viva (01, 02 y 03 en los dos canales) cumplen hoy **todos** los criterios
que la compuerta sabe medir. Ninguna quedó en VENTANA, que es la categoría de los fallos de forma.

## 3 · Qué comprueba cada código

| Código | Criterio del manual | Qué mira |
|---|---|---|
| M01 | firma textual invariable | la frase «La Bandita informa a partir de fuentes fechadas.» aparece literal |
| M02 | meme original de dos líneas | dos líneas con guion largo inmediatamente antes de la firma |
| M03 | remate propio, no calcado | texto tras la firma, distinto en cada pieza |
| M04 | mapa fiel, 5–12 entradas | cuenta las ramas del árbol del mapa |
| M05 | «En una página» de 3–5 párrafos | párrafos reales, no viñetas ni subtítulos sueltos |
| M06 | FAQ de 6–12 preguntas | preguntas en formato `**¿…?**` o `*«…?»*` sobre el texto completo |
| M07 | enlaces completos y con formato | toda URL del cuerpo aparece al pie como `- Nombre: URL` |
| M08 | fichas con estrellas y licencia | marcas ★N acompañadas de campo de licencia |
| M09 | prohibiciones de forma | superlativos absolutos y frases de venta |
| M10 | notas al pie fechadas | bloque de notas con fecha `(N-mes)` |
| M11 | banda de longitud | `docs/bandas.json`: WA 63.000–63.099 · FB 40.000–45.000 |
| M12 | sin meta-comentarios del proceso | frases que cuentan la escritura en vez del tema |
| M13 | cabecera con fecha larga | «1 de noviembre de 2026» en las primeras líneas |
| M14 | sin signos dobles ni de venta | `!!`, `?!`, `!?` |
| M15 | sin secretos ni APK de mods | patrones de token y enlaces directos a mods |
| M16 | sin promesas de vigilancia futura | «te avisaré», «volveré a avisarte» |
| M23 | sin párrafos compartidos | ningún párrafo largo repetido entre piezas |

## 4 · Qué se cambió en las piezas en esta ronda

**01 WhatsApp (63.094).** Mapa de 25 a 8 entradas fieles; tercer párrafo en «En una página»; el mapa
dejó de prometer secciones que no existían; los 29 enlaces pasaron a `- Nombre: URL` con nombres en
español; se añadió el dominio real de Droid-ify en Codeberg, que antes solo vivía dentro de una
descripción citada; fuera «la mejor de todas» del título de Obtainium; cierre nuevo con meme, firma
textual, remate propio, medición con hora y tres notas al pie. Se reparó además el esquema del
ecosistema, que había quedado partido por un separador dentro del bloque de código.

**02 WhatsApp (63.084).** Mapa de 15 a 12 entradas; los 56 enlaces con nombre; fuera el apartado que
contaba lo que costó escribir (meta-relato) y su parte útil —la errata del censo— pasó a nota al pie
fechada; cierre con meme, firma, remate y medición.

**01, 02 y 03 Facebook.** Mapa propio y byline; sección «En una página» real; los 22, 33 y 33 enlaces
en formato de la casa; cierre con meme, firma textual, remate propio y medición con hora; tres notas al
pie fechadas; corregidos los conteos de repositorios y el carácter de ancho cero que rompía el envío
de 03 (el icono 👨‍🔧 pasó a 🧰).

## 5 · Qué se cambió en las herramientas

1. **`manual_gate.py` · `seccion()`** desempata ahora por tres cosas en este orden: que el primer
   renglón del bloque sea el encabezado buscado, que el bloque tenga más enlaces, y —si sigue el
   empate— el último bloque. Antes, el mapa del principio se confundía con la sección de notas.
2. **`manual_gate.py` · M07** limpia `»`, comas y puntos pegados a una URL antes de comparar: una
   descripción citada que acaba en `…client».` acusaba un enlace que sí estaba en la lista.
3. **`manual_gate.py` · M12** dejó de marcar dos frases que son deber de la casa, no meta-relato
   («antes de seguir», «lo que esta pieza no dice»).
4. **`vara.py` · G11** nuevo: corre el gate sobre todas las piezas con banda declarada y cuenta como
   fallo tanto un ROJO como un VENTANA. El manual no tiene categoría opcional.

## 6 · Lo que la compuerta NO comprueba (dicho para que no se confunda)

- **Si un dato es verdad.** Comprueba que haya fecha y que las URLs estén; que ★N sea el número real
  lo garantiza la medición del día (`tools/envio.py --medir`), no esta compuerta.
- **Si la redacción es buena.** Un texto puede cumplir M01–M23 y seguir siendo flojo.
- **Si el remate es original en el sentido literario.** Solo detecta que no esté calcado de otra pieza
  de la serie.
- **El tono.** La calidez y la voz del dueño se revisan leyendo, no corriendo un programa.

## 7 · Pendientes declarados, con fecha

- **Próximo barrido completo:** lunes 2 de noviembre de 2026, 06:00 de Santo Domingo, con `--medir`
  (necesita el token en el entorno) y re-medición de los 30 repositorios añadidos hoy a la ficha del
  censo, que se midieron sin token y por tanto con la cuota pública.
- **Piezas 04 en adelante:** se rehacen de cero con el manual ya enchufado; ninguna se declara
  terminada sin pasar G11.
- **Envíos:** regenerados hoy (WA 110 · FB 132, 0 fallos) y vueltos a sellar en el lote
  `lote-2026-11-01`.
