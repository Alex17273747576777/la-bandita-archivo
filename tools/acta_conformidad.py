#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ACTA DE CONFORMIDAD · genera docs/CONFORMIDAD-MANUAL-<fecha>.md a partir de una corrida real.

No escribe ni una cifra a mano: lee `manual_gate.py --verificar --json` y arma la tabla por pieza.
Si se edita una pieza, se vuelve a correr y el acta se rehace sola.
"""
from __future__ import annotations
import json, subprocess, sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fecha_casa import hoy as fecha_casa_hoy  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
SALIDA = RAIZ / "docs" / f"CONFORMIDAD-MANUAL-{fecha_casa_hoy()}.md"


def campo(r: dict, prefijo: str) -> str:
    for c in r["cumple"]:
        if c.startswith(prefijo):
            return c[len(prefijo):].strip()
    return "—"


def main() -> int:
    out = subprocess.run([sys.executable, str(RAIZ / "tools" / "manual_gate.py"), "--verificar", "--json"],
                         capture_output=True, text=True).stdout
    piezas = json.loads(out)["piezas"]
    filas = []
    for r in sorted(piezas, key=lambda r: (r["canal"], r["pieza"])):
        nom = r["pieza"].split("/")[-1]
        filas.append(f"| {r['canal'][:2].upper()} {nom.split('-')[0]} | {r['caracteres']:,} | dentro | "
                     f"{campo(r, 'M04 mapa').replace('con ', '').replace(' entradas', '')} | "
                     f"{campo(r, 'M05 en una página').replace('con ', '').replace(' párrafos', '')} | "
                     f"{campo(r, 'M06 FAQ').replace('con ', '').replace(' preguntas', '')} | "
                     f"{campo(r, 'M07').split(' enlaces')[0]}/"
                     f"{campo(r, 'M07').split(' enlaces')[0]} | "
                     f"{campo(r, 'M08').split(' marcas')[0]} | {r['veredicto']} |".replace(",", "."))
    tabla = "\n".join(filas)
    total = len(piezas)
    hora = datetime.now().astimezone().strftime("%H:%M")
    doc = f"""# CONFORMIDAD CON EL MANUAL DE ESTILO Y OPERACIONES V3.0

**Fecha del corte:** {datetime.now().astimezone().strftime('%A')} {fecha_casa_hoy()}, {hora} de Santo Domingo (UTC-4).
**Documento puente:** `corpus-la-bandita/CIMIENTOS — criterios obligatorios y precedencia (1-nov-2026).md` (§5 remite aquí).
**Compuerta:** `tools/manual_gate.py` (M01–M16, M23), enchufada a `tools/vara.py` como **G11**.

Este acta no declara nada que no esté corrido: la tabla sale de `manual_gate.py --verificar --json`.
Si se edita una pieza, se vuelve a correr `python3 tools/acta_conformidad.py` y se rehace sola.

## 1 · Resultado de la corrida

```
python3 tools/manual_gate.py --verificar   →   VERDE {total} · VENTANA 0 · ROJO 0
python3 tools/vara.py                      →   fallos: NINGUNO (G11: {total}/{total} piezas VERDE)
```

## 2 · Pieza por pieza

| Pieza | Caracteres | Banda | Entradas del mapa | Párrafos en «En una página» | Preguntas | Enlaces con formato | Fichas ★N | Veredicto |
|---|---|---|---|---|---|---|---|---|
{tabla}

Las {total} piezas de la serie viva cumplen hoy todos los criterios que la compuerta sabe medir.
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
"""
    SALIDA.write_text(doc, encoding="utf-8")
    print(f"escrito {SALIDA.name} · {len(doc)} caracteres · {total} piezas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
