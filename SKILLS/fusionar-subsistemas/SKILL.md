---
name: fusionar-subsistemas
version: 1.0.0
dominio: cimiento
nivel: puerta
cuando: cuando hay dos sistemas que hacen lo mismo y ninguno es completo
entradas: [dos o más sistemas, con su documentación y sus herramientas]
salidas: [un sistema único, con las piezas mejores de cada uno y deprecaciones declaradas]
herramientas: lectura de los dos, diff conceptual, tabla de decisión]
verificacion: [ninguna capacidad se perdió, cada deprecación apunta a su reemplazo]
depende_de: [arranque-de-suelo]
---

# Habilidad · fusionar subsistemas

## Propósito
Unificar sin perder nada. Cuando en un repositorio conviven dos sistemas de habilidades, el riesgo no
es elegir mal: es **perder en silencio la capacidad que solo tenía el otro**.

## Cuándo se usa
- Cuando hay dos carpetas que documentan lo mismo y no coinciden.
- Cuando una herramienta lista cosas que el disco dice de otra manera.
- Al heredar un repositorio con historia a medias.

**No se usa** para ordenar por gusto: solo cuando hay capacidades que se pisan o se pierden.

## Pasos
1. Inventariar **capacidades**, no archivos. Una capacidad puede estar en dos sitios con nombres distintos.
2. Tabla de tres columnas: capacidad · quién la tiene · quién la tiene mejor.
3. Escribir la versión fusionada tomando lo mejor y **mejorando donde los dos fallaban**.
4. Deprecar el sistema viejo con un archivo que diga a dónde fue cada cosa y por qué.
5. Comprobar que no se perdió ninguna capacidad de la tabla del paso 2.

## Reglas duras
- **Nada se borra sin reemplazo declarado.** El sistema viejo se marca deprecado, no se hace
  desaparecer: alguien puede tener un enlace.
- **Se conserva lo que el sistema viejo hacía mejor**, aunque el nuevo sea más moderno. En esta casa
  el viejo tenía las lecciones aprendidas de fallos reales; eso no se tira.
- **La fusión se verifica con la tabla de capacidades**, no con la sensación de orden.

## Verificación
- Cada capacidad del inventario aparece en el sistema nuevo.
- Cada deprecación tiene su «esto ahora vive en…».
