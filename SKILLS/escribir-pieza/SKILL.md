---
name: escribir-pieza
version: 2.0.0
dominio: redacción
nivel: medidor
cuando: cuando existe el censo y hay que escribir el cuerpo de la pieza
entradas: [docs/MEDICION-PNN.json, banda de longitud, formato del canal]
salidas: [cuerpo de la pieza dentro de banda, con firma y bloque de corrección]
herramientas: [docs/almas/NN.md, tools/redacta.py, tools/cuadre.py]
verificacion: [dentro de banda, firma literal, fecha del día, cita su propio JSON]
depende_de: [censo-de-pieza]
---

# Habilidad · escribir una pieza

## Propósito
Que la voz la ponga una persona y las cifras las ponga el JSON. La pieza se escribe en un **alma**
(`docs/almas/NN.md`) con marcas que el motor rellena; así ninguna cifra se copia a mano.

## Cuándo se usa
- Siempre que hay censo y se va a publicar.
- Al rehacer una pieza entera (la anterior se mueve a `_reemplazadas-<fecha>/`).

## Pasos
1. Escribir el alma con el encabezado `TITULO:` y `RESUMEN:`, luego la cabecera de fecha de la casa,
   el mapa, la semilla, y los bloques del formato del canal.
2. Usar las marcas: `{{AGREGADOS}}`, `{{TABLA}}`, `{{TABLA_CIFRAS}}`, `{{FIRMAS}}`, `{{EXTREMOS}}`,
   `{{SIN_ENTREGA}}`, `{{N}}`, `{{TOTAL_ESTRELLAS}}`. Nunca escribir una cifra agregada a mano.
3. Para piezas que no miden repositorios, la tabla se escribe a mano con los valores del JSON, y la
   pieza cita **su propio archivo** de medición.
4. Cerrar con la firma literal y con el bloque de corrección si la pieza corrige algo anterior.
5. `python3 tools/redacta.py NN --reemplazar` y leer el recuento de caracteres.

## Reglas duras
- **Corregir hacia adelante, no reescribir en silencio.** Lo publicado se corrige y la corrección se
  anota **dentro** de la pieza, con el nombre viejo y el nuevo si hubo mudanza.
- **La firma es literal**: `La Bandita informa. Lo que no se midió, aquí no se escribe.` y va en el cierre.
- **Un párrafo no se repite.** Si aparece tres veces, es plantilla, no voz.
- **Español dominicano solo en las publicaciones.** Las apps son multilingües: no se mezcla la regla.
- **La fecha del día va en la cabecera**, no «hoy».

## Verificación
- `len(cuerpo)` dentro de la banda del canal.
- La firma aparece una vez y al final.
- La pieza cita `docs/MEDICION-PNN-<fecha>.json` propio.

## Errores conocidos
- Olvidar el encabezado `TITULO:` y generar el archivo como `NN--Facebook-…`.
- Añadir una cita a la **alma** y no volver a renderizar: el archivo no cambia y parece que la
  herramienta perdió el texto.
- Rellenar para llegar a la banda: se nota, y el dueño lo prohíbe.
