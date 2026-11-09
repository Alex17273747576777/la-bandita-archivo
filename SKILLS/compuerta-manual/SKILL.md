---
name: compuerta-manual
version: 1.1.0
dominio: control de calidad
nivel: puerta
cuando: cuando una pieza está escrita y hay que decidir si pasa o no, criterio por criterio
entradas: [pieza, manual de estilo del canal]
salidas: [VERDE/ROJO por criterio, con la cita que lo prueba]
herramientas: [tools/manual_gate.py, tools/firma_literal.py, tools/doctor.py]
verificacion: [cada criterio tiene su cita, ningún ROJO sin explicación]
depende_de: [cotejar-cifras]
---

# Habilidad · compuerta del manual

## Propósito
Aplicar el manual de estilo como una lista de criterios comprobables, no como un gusto. Cada
criterio devuelve **VERDE o ROJO con la cita del texto** que lo demuestra.

## Cuándo se usa
- Antes de publicar cualquier pieza.
- Al revisar un lote entero.

## Pasos
1. `python3 tools/manual_gate.py` — recorre los criterios del manual v3.0.
2. `python3 tools/firma_literal.py --verificar` — la firma va letra por letra y en el cierre.
3. Para cada ROJO: citar el fragmento, no la impresión.
4. Si un criterio no se puede comprobar con una regla, se marca como **medidor** y no como puerta:
   un medidor publica su cifra, no bloquea.

## Reglas duras
- **Una puerta que falla detiene la línea.** Un medidor que sube se informa y se sigue.
- **No se inventa un criterio para suspender una pieza que no gusta**, ni se quita para aprobarla.
- **La frase de la casa se comprueba con `in`, no con una expresión regular laxa.**

## Verificación
- Todas las puertas verdes o su ROJO explicado con cita.
- Los medidores dan su número.

## Errores conocidos
- Contar como fallo un cero esperado: cero sumas es el resultado habitual de esta serie.
