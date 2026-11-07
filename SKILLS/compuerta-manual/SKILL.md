---
name: compuerta-manual
version: 1.0.0
dominio: control de calidad
cuando: antes de dar una pieza por buena y antes de cada commit
entradas: [pieza o carpeta de piezas]
salidas: [informe VERDE/ROJO por pieza, con el criterio que falla]
herramientas: [tools/manual_gate.py, tools/firma_literal.py, tools/vara.py]
verificacion: [0 ROJO en toda la carpeta, G11 en verde]
---

# Skill · pasar la compuerta

## Propósito
Comprobar, criterio por criterio, que una pieza cumple el manual v3.0 sin que nadie tenga que
recordarlo a ojo.

## Uso
```bash
python3 tools/manual_gate.py --pieza "<ruta exacta>.md"   # una pieza, con detalle
python3 tools/manual_gate.py --verificar                  # toda la carpeta: resumen
python3 tools/firma_literal.py --verificar                # posición de la firma y fecha del día
```

## Lo que mira (M01–M23)
Firma textual (M01), meme del corte (M02), remate propio no calcado (M03), mapa 5–12 (M04), «En una
página» 3–5 párrafos (M05), FAQ 6–12 (M06), enlaces `- Nombre: URL` y cobertura del cuerpo (M07),
fichas con licencia (M08), frases prohibidas (M09), notas fechadas (M10), banda de longitud (M11),
meta-comentarios (M12), cabecera con fecha larga (M13), signos dobles (M14), secretos y APK de mods
(M15), promesas de vigilancia (M16), párrafos compartidos entre piezas (M23).

## Pasos
1. Limpiar **caracteres de ancho cero** antes de gatear (tumban G9 y aparecen al pegar).
2. Gatear la pieza; si sale ROJO, leer el criterio y corregir la **causa**.
3. Volver a gatear; luego `--verificar` sobre la carpeta entera (detecta M23 contra las vecinas).
4. Si se tocó una pieza ya publicada: regenerar envíos (`envio.py --generar`) y re-sellar.
5. Anotar el resultado en el acta del lote.

## Reglas duras
- **Rojo no se publica**, ni «solo por esta vez».
- Un fallo de forma se arregla en el texto, nunca relajando la compuerta.
- Si la compuerta está mal, se corrige la compuerta **y se deja acta**: una compuerta que se ablanda
  deja de significar algo.

## Verificación
`MANUAL GATE · N piezas · VERDE N · ROJO 0` y `vara.py` con `fallos: NINGUNO`.
