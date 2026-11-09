---
name: descubrir-recursos
version: 1.0.0
dominio: medición
nivel: medidor
cuando: cuando hay que encontrar recursos nuevos en vez de repetir los ya conocidos
entradas: [catálogos: fmhy.net, miyomi.app, keiyoushi, mangayomi, otros]
salidas: [candidatos con su origen, y la separación entre «nuevo» y «ya medido»]
herramientas: [tools/censo_fmhy.py, tools/descubrir.py, tools/censo_medir.py]
verificacion: [cada candidato dice de qué página salió, cada descartado dice por qué]
depende_de: [medir-recurso]
---

# Habilidad · descubrir recursos

## Propósito
Buscar lo que **no está medido** sin confundir «no lo tengo» con «no existe». Una lista curada ajena
sirve para descubrir, no para creer: los datos se miden en fuente primaria.

## Cuándo se usa
- Al abrir temas nuevos.
- Cuando el dueño pide «recursos nuevos, revisando cada catálogo».

## Pasos
1. Leer el catálogo por su API o su repositorio, no a ojo: `fmhy.net` (clon de `fmhy/edit`),
   `miyomi.app/api/extensions`, el `index.json` de keiyoushi, el de mangayomi.
2. Extraer repositorios **con la página y la sección de donde salieron**.
3. Cruzar contra el registro y contra el censo ya medido. Separar en tres listas: nuevos, ya medidos,
   y **mudados** (los que hoy redirigen).
4. Medir los nuevos con `medir-recurso`, no darlos por buenos por estar en la lista.

## Reglas duras
- **Un catálogo no es una fuente de datos**: es una fuente de candidatos.
- **Antes de decir que a un catálogo le falta algo, comprobar con los nombres viejos.** Comparar sin
  eso dio 16 falsos positivos en una pasada.
- **El censo hereda el sesgo de su fuente.** Si el censo nació de FMHY, no puede contener lo que a
  FMHY le falta; para encontrar huecos hay que mirar fuera de ella.
- **Un archivo trampa existe**: `index.min.json` devuelve 2 donde hay 1.554. Se mide el bueno y se
  nombra el malo.

## Verificación
- Cada candidato tiene página y sección de origen.
- Los reportados como hueco se comprobaron también por su nombre anterior.

## Errores conocidos
- Pedir a un catálogo que añada lo que ya tiene.
- Contar como nuevo un repositorio que solo cambió de dueño.
