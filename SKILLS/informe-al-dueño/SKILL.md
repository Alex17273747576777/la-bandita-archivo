---
name: informe-al-dueño
version: 1.0.0
dominio: publicación
cuando: al cerrar un turno o un lote, cuando el dueño pide «cómo va»
entradas: [actas del lote, vara.py, CI, docs/bandas.json]
salidas: [informe corto: cifras reales, hora de Santo Domingo, pendiente exacto]
herramientas: [tools/vara.py, tools/manual_gate.py, tools/acta_conformidad.py, git log, fecha_casa.py]
verificacion: [cada cifra rastreable a un archivo, hora incluida, cero adjetivos de venta]
---

# Skill · informar al dueño

## Propósito
Dar el estado real del proyecto en el mínimo número de líneas útiles: qué se cerró, con qué cifras, qué
quedó pendiente y qué compuerta lo respalda. Sin relleno, sin promesas, sin «todo listo» sin prueba.

## Formato del informe

1. **Corte**: día y hora en America/Santo_Domingo.
2. **Hecho**: lista de acciones cerradas con su identificador (`commit`, sello, número de piezas).
3. **Cifras**: piezas, caracteres, lotes, VERDE/ROJO, frescura del registro. Todas verificables.
4. **Compuertas**: `vara.py`, `manual_gate.py`, CI — con su resultado literal.
5. **Pendiente**: qué sigue, en una línea cada cosa, con su responsable (dueño o agente).
6. **Riesgos**: lo que puede romperse si se retoma en frío (archivos a re-clonar, tokens, piezas a
   medio escribir).

## Reglas duras

- **Cero charla.** Nada de «¡vamos con todo!», «al 110 %» ni cierres motivacionales en el informe.
- **Cada cifra con su fuente**: si no está en un archivo del repo o en la salida de un comando, no se
  escribe.
- **La hora va siempre**, y en hora de Santo Domingo.
- **No se anuncia lo que no está confirmado**: CI pendiente se informa como pendiente.
- **Los huecos se dicen**: si una pieza no se pudo medir, el informe lo declara.

## Verificación

Leer el informe y preguntarse por cada número: *¿de qué archivo sale?* Si la respuesta no existe, el
número se borra.
