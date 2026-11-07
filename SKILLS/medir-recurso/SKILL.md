---
name: medir-recurso
version: 1.0.1
dominio: medición
cuando: antes de citar cualquier repositorio o proyecto en una pieza
entradas: [lista de repos "owner/repo", canal]
salidas: [fichas con estrellas, licencia, lenguaje, empujón, versión, discrepancia declarada]
herramientas: [tools/tres_lecturas.py, GitHub API (PAT_FINO), raw.githubusercontent]
verificacion: [0 sin leer, campos descartados anotados, ventana horaria registrada]
---

# Skill · medir un recurso

## Propósito
Convertir un nombre de repositorio en un dato publicable: **medido tres veces por tres caminos y
fechado**. Lo que no se pueda medir se declara como hueco, no se estima.

## Cuándo se usa
- Al abrir cualquier pieza nueva.
- Al reescribir una pieza anterior con censo nuevo.
- Al revisar un dato que huele a viejo.

**No se usa** para completar una tabla «más o menos»: si no hay medición, no hay fila.

## Entradas
- Una lista de `owner/repo`, uno por línea.
- El canal (`facebook` o `whatsapp`) para guardar en la medición correcta.

## Pasos
1. Rotar el orden de la lista respecto de la medición anterior (para que ningún orden favorezca un
   resultado).
2. Correr `tres_lecturas.py` sin `--guardar` y leer el informe:
   `printf 'owner/repo\n' | python3 tools/tres_lecturas.py`
3. Donde las tres lecturas **no coincidan** en un campo, descartar ese campo y anotar la discrepancia
   en el texto de la pieza (con las dos versiones).
4. Consultar la **última publicación** de cada proyecto en su lista de publicaciones. Si la ficha
   automática la devuelve vacía, no se rellena: se escribe «sin paquete» o «sin conclusión».
5. Repetir con `--guardar` para dejar el censo en `docs/envios/_medicion-{canal}.json`.
6. Anotar la ventana horaria exacta (America/Santo_Domingo) para el bloque «Medición del corte».

## Reglas duras
- **Tres lecturas o no hay dato.** Una sola fuente no se publica como medición.
- **Prohibido redondear estrellas** o convertir «sin licencia» en «probablemente MIT».
- **Empujón ≠ paquete.** Se publican los dos y se calcula la brecha desde el paquete.
- **La fecha va con hora.** «Hoy» no es una fecha; «entre las 07:58 y las 09:12» sí.
- **Los 404 y los repos sin README** se documentan como huecos y no se reintentan sin motivo nuevo.

## Verificación
- El informe termina en `N medidos · 0 sin leer`.
- Cada fila que llegue al texto tiene sus cuatro campos o su hueco declarado.
- La pieza cita la ventana completa del corte.

## Ejemplo de salida
```
· maxrave-dev/SimpMusic  ★12.657 GPL-3.0 Kotlin push 2026-11-02
· DevEmperor/DictateKeyboard  ★313 Apache-2.0 Kotlin push 2026-11-02   (sin paquete adjunto)
TRES LECTURAS · 10 medidos · 0 sin leer
```

## Errores conocidos
- Dar por buena la fecha de versión de la ficha automática: casi siempre viene vacía.
- Contar el empujón como entrega y escribir «actualizado hoy» sin comprobar el paquete.
- Medir en dos tandas separadas por horas y declarar una sola ventana: se declaran las dos.
