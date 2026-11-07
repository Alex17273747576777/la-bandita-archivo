---
name: censo-de-pieza
version: 1.0.0
dominio: medición
cuando: al cerrar la medición de una pieza, antes de escribir
entradas: [medición guardada, lista de repos de la pieza]
salidas: [cifras madre de la pieza: total, mediana, reparto, conteos por estado]
herramientas: [python3, docs/envios/_medicion-{canal}.json, docs/bandas.json]
verificacion: [cifras reproducibles en un comando, suma que cuadra con la tabla]
---

# Skill · censo de la pieza

## Propósito
Sacar de la medición las **cifras madre** que sostienen la pieza: totales, medianas, reparto por
licencia, quién empujó esta semana, quién no publica paquete. Sin censo no se escribe: se improvisa.

## Pasos
1. Leer la medición guardada y quedarse solo con los repos de esta pieza.
2. Calcular: suma de estrellas, mediana, reparto por licencia, empujones por mes, brechas
   paquete↔empujón en días, cuántos no publican paquete.
3. Elegir **una cifra madre** que ordene la pieza (la que el lector recordaría si solo lee el titular).
4. Comprobar que toda cifra del texto se puede reconstruir desde la tabla publicada.
5. Anotar la cifra madre en el acta del lote (`docs/`), para que la siguiente pieza no la repita.

## Reglas duras
- Un total que no suma desde la tabla es un error, no una licencia poética.
- Si un porcentaje se redondea, se dice («el 72 %, redondeado»).
- No se repite la cifra madre de la pieza anterior: se busca otro ángulo del mismo censo.

## Verificación
Recalcular el total con un comando y compararlo con el texto. Si difieren, manda el comando.
