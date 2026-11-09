---
name: publicar-fuera
version: 1.0.0
dominio: publicación
nivel: medidor
cuando: cuando el hallazgo sirve a otro proyecto y hay que decírselo (issue, PR, comentario)
entradas: [hallazgo medido, proyecto destino]
salidas: [issue o comentario con la tabla medida y una propuesta concreta]
herramientas: [gh api, curl con token, el clon del proyecto]
verificacion: [cada cifra del issue se midió, la propuesta responde lo que preguntaron]
depende_de: [descubrir-recursos]
---

# Habilidad · publicar fuera de casa

## Propósito
Llevar un hallazgo a quien puede usarlo **con la medición delante**, no con una opinión. Y responder
exactamente lo que se preguntó, en el formato del proyecto que lo recibe.

## Cuándo se usa
- Cuando se encuentra un hueco real en un catálogo que se usa.
- Cuando el mantenedor pregunta algo en un issue abierto.

## Pasos
1. Reunir la tabla de cifras **medidas** con su fecha y su comando.
2. Leer lo que el proyecto ya hace igual (su patrón existente) y proponer **en ese patrón**.
3. Si el mantenedor dio opciones, dar **su** opción A y su opción B, no una tercera inventada.
4. Ofrecerse a hacer el PR si es un archivo nuevo, y decir que se hará en su formato.
5. Publicar y guardar el enlace.

## Reglas duras
- **No pedir una sección nueva cuando basta una línea.** Menos estructura es más probable que se acepte.
- **Nada de cifras sin comando.** Si no se midió, no va.
- **Un «no» del mantenedor es un dato**, no una derrota: se anota y se sigue.
- **No se promete un PR que no se puede hacer** (sin credenciales, sin permiso, sin tiempo).

## Verificación
- El issue responde la pregunta que se hizo, en su primera línea.
- Cada número de la tabla se puede reproducir con el comando que se cita.

## Errores conocidos
- Escribir un issue largo que no contesta la pregunta del mantenedor.
- Proponer una reorganización entera de una wiki ajena.
