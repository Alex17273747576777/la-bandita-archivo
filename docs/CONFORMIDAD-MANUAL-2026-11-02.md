# CONFORMIDAD CON EL MANUAL DE ESTILO Y OPERACIONES V3.0

**Fecha del corte:** Monday 2026-11-02, 21:24 de Santo Domingo (UTC-4).
**Documento puente:** `corpus-la-bandita/CIMIENTOS — criterios obligatorios y precedencia (1-nov-2026).md` (§5 remite aquí).
**Compuerta:** `tools/manual_gate.py` (M01–M16, M23), enchufada a `tools/vara.py` como **G11**.

Este acta no declara nada que no esté corrido: la tabla sale de `manual_gate.py --verificar --json`.
Si se edita una pieza, se vuelve a correr `python3 tools/acta_conformidad.py` y se rehace sola.

## 1 · Resultado de la corrida

```
python3 tools/manual_gate.py --verificar   →   VERDE 31 · VENTANA 0 · ROJO 0
python3 tools/vara.py                      →   fallos: NINGUNO (G11: 31/31 piezas VERDE)
```

## 2 · Pieza por pieza

| Pieza | Caracteres | Banda | Entradas del mapa | Párrafos en «En una página» | Preguntas | Enlaces con formato | Fichas ★N | Veredicto |
|---|---|---|---|---|---|---|---|---|
| FA 01 | 40.326 | dentro | 12 | 5 | 11 | 18/18 | 62 | VERDE |
| FA 02 | 40.123 | dentro | 12 | 5 | 12 | 27/27 | 93 | VERDE |
| FA 03 | 40.442 | dentro | 12 | 5 | 12 | 10/10 | 36 | VERDE |
| FA 04 | 40.033 | dentro | 12 | 5 | 10 | 33/33 | 58 | VERDE |
| FA 05 | 40.139 | dentro | 12 | 5 | 12 | 17/17 | 42 | VERDE |
| FA 06 | 44.158 | dentro | 12 | 5 | 12 | 26/26 | 43 | VERDE |
| FA 07 | 41.905 | dentro | 12 | 5 | 11 | 21/21 | 43 | VERDE |
| FA 08 | 41.258 | dentro | 11 | 5 | 12 | 16/16 | 40 | VERDE |
| FA 09 | 41.590 | dentro | 12 | 5 | 12 | 18/18 | 60 | VERDE |
| FA 10 | 40.326 | dentro | 12 | 5 | 12 | 15/15 | 47 | VERDE |
| FA 11 | 40.006 | dentro | 12 | 5 | 10 | 9/9 | 38 | VERDE |
| FA 12 | 40.038 | dentro | 12 | 5 | 10 | 8/8 | 27 | VERDE |
| FA 13 | 40.069 | dentro | 12 | 5 | 10 | 9/9 | 35 | VERDE |
| FA 14 | 40.051 | dentro | 12 | 5 | 12 | 10/10 | 65 | VERDE |
| FA 15 | 40.374 | dentro | 12 | 5 | 10 | 9/9 | 59 | VERDE |
| FA 16 | 40.081 | dentro | 12 | 5 | 12 | 9/9 | 56 | VERDE |
| FA 17 | 40.308 | dentro | 12 | 5 | 10 | 9/9 | 37 | VERDE |
| FA 18 | 40.346 | dentro | 12 | 5 | 10 | 8/8 | 45 | VERDE |
| FA 19 | 40.399 | dentro | 12 | 5 | 10 | 9/9 | 70 | VERDE |
| FA 20 | 40.121 | dentro | 11 | 5 | 10 | 12/12 | 26 | VERDE |
| FA 21 | 40.098 | dentro | 11 | 5 | 10 | 12/12 | 39 | VERDE |
| FA 22 | 40.214 | dentro | 11 | 5 | 10 | 12/12 | 47 | VERDE |
| FA 23 | 40.013 | dentro | 11 | 5 | 10 | 12/12 | 47 | VERDE |
| FA 24 | 40.302 | dentro | 11 | 5 | 10 | 12/12 | 49 | VERDE |
| FA 25 | 40.795 | dentro | 12 | 5 | 10 | 12/12 | 52 | VERDE |
| WH 01 | 63.094 | dentro | 8 | 3 | 9 | 29/29 | 67 | VERDE |
| WH 02 | 63.084 | dentro | 12 | 3 | 11 | 56/56 | 123 | VERDE |
| WH 03 | 63.007 | dentro | 12 | 4 | 8 | 33/33 | 64 | VERDE |
| WH 04 | 63.086 | dentro | 12 | 5 | 11 | 33/33 | 92 | VERDE |
| WH 05 | 63.020 | dentro | 12 | 5 | 12 | 17/17 | 38 | VERDE |
| WH 06 | 63.002 | dentro | 12 | 5 | 11 | 26/26 | 55 | VERDE |

Las 31 piezas de la serie viva cumplen hoy todos los criterios que la compuerta sabe medir.
Ninguna quedó en VENTANA, que es la categoría de los fallos de forma.

## 3 · Qué comprueba cada código

| Código | Criterio del manual | Qué mira |
|---|---|---|
| M01 | firma textual invariable | la frase «La Bandita informa a partir de fuentes fechadas.» aparece literal |
| M02 | meme original de dos líneas | dos líneas con guion largo antes de la firma |
| M03 | remate propio, no calcado | texto tras la firma, distinto en cada pieza |
| M04 | mapa fiel, 5–12 entradas | cuenta las ramas del árbol del mapa |
| M05 | «En una página» de 3–5 párrafos | párrafos reales, no viñetas ni subtítulos |
| M06 | FAQ de 6–12 preguntas | formato `**¿…?**` o `*«…?»*` sobre el texto completo |
| M07 | enlaces completos y con formato | toda URL del cuerpo aparece al pie como `- Nombre: URL` |
| M08 | fichas con estrellas y licencia | marcas ★N con campo de licencia |
| M09 | prohibiciones de forma | superlativos absolutos y frases de venta |
| M10 | notas al pie fechadas | bloque de notas con fecha `(N-mes)` |
| M11 | banda de longitud | `docs/bandas.json`: WA 63.000–63.099 · FB 40.000–45.000 |
| M12 | sin meta-comentarios del proceso | frases que cuentan la escritura y no el tema |
| M13 | cabecera con fecha larga | «1 de noviembre de 2026» en las primeras líneas |
| M14 | sin signos dobles ni de venta | `!!`, `?!`, `!?` |
| M15 | sin secretos ni APK de mods | patrones de token y enlaces directos a mods |
| M16 | sin promesas de vigilancia futura | «te avisaré», «volveré a avisarte» |
| M23 | sin párrafos compartidos | ningún párrafo largo repetido entre piezas |

## 4 · Qué se cambió en las herramientas

1. **`seccion()`** busca primero una línea que sea el encabezado y devuelve desde ahí hasta el
   siguiente separador; si no la hay, desempata por (primer renglón, nº de enlaces, el más temprano).
   Antes el mapa del principio se confundía con la sección de notas y con la página de resumen.
2. **M07** limpia `»`, comas y puntos pegados a una URL antes de comparar.
3. **M12** no marca dos frases que son deber de la casa, no meta-relato.
4. **`vara.py` · G11**: nuevo. Cuenta como fallo un ROJO y también un VENTANA.
5. **`tools/acta_conformidad.py`**: este acta se genera sola desde la corrida; ninguna cifra a mano.

## 5 · Lo que la compuerta NO comprueba (dicho para que no se confunda)

- **Si un dato es verdad.** Comprueba que haya fecha y que las URLs estén; que ★N sea real lo
  garantiza la medición del día (`tools/envio.py --medir`), no esta compuerta.
- **Si la redacción es buena.** Un texto puede cumplir M01–M23 y seguir siendo flojo.
- **Si el remate es original en sentido literario.** Solo detecta que no esté calcado de otra pieza.
- **El tono.** La voz del dueño se revisa leyendo, no corriendo un programa.

## 6 · Pendientes declarados, con fecha

- **Próximo barrido completo:** lunes 2 de noviembre de 2026, 06:00 de Santo Domingo, con `--medir`
  (necesita el token en el entorno) para re-medir con autenticación los repositorios que hoy se
  midieron con el buscador y con la cuota pública.
- **Piezas 05 en adelante:** se hacen de cero con la compuerta ya enchufada; ninguna se declara
  terminada sin pasar G11.
- **Envíos:** regenerados y verificados (WA 111 · FB 133, 0 fallos) y sellados en `lote-2026-11-01`.
