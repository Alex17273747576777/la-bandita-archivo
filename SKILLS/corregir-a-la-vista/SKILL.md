---
name: corregir-a-la-vista
version: 1.0.0
dominio: cimiento
nivel: puerta
cuando: cuando aparece un fallo, propio o del sistema, en cualquier punto del trabajo
entradas: [fallo observado, contexto]
salidas: [lección escrita, herramienta corregida si toca, versión subida]
herramientas: [SKILLS/LECCIONES.md, este mismo archivo]
verificacion: [la lección tiene síntoma, causa y regla; la herramienta quedó arreglada]
depende_de: []
---

# Habilidad · corregir a la vista

## Propósito
Que el sistema **aprenda de cada fallo**. Es la habilidad que hace que las otras mejoren: sin ella,
el repositorio repite los mismos errores con nombres nuevos.

## Cuándo se usa
- Cada vez que algo falla: un medidor, una pieza, un comando, una suposición propia.
- Al final de un bloque, repasando qué se corrigió.

## Pasos
1. Escribir la lección en tres líneas: **síntoma** (qué se vio), **causa** (qué había de verdad),
   **regla** (qué se hace distinto desde ahora).
2. Decidir a quién pertenece: si es del detector, se arregla el detector; si es de la pieza, se corrige
   la pieza **hacia adelante** y se anota en la pieza.
3. Subir la versión de la habilidad afectada en su frontmatter.
4. Añadir la lección a `SKILLS/LECCIONES.md` con fecha y número.

## Reglas duras
- **Se arregla el detector, nunca se baja el listón.**
- **No se reescribe el pasado en silencio**: la corrección se publica donde ocurrió.
- **Una lección sin regla no es una lección**, es una anécdota.
- **Un fallo propio se cuenta con el mismo detalle que un hallazgo.** Los siete fallos de detector de
  esta casa valen más que sus tres verdes.

## Verificación
- La lección tiene sus tres partes.
- La herramienta afectada cambió, o se explica por qué no hacía falta.

## Errores conocidos
- Apuntar la lección y no tocar la herramienta: al mes siguiente el mismo fallo, otra vez.
- Corregir el síntoma (la cifra) sin corregir la causa (el lector).
