---
name: traducir-multilingue
version: 1.0.0
dominio: app
nivel: medidor
cuando: cuando un programa debe hablar varios idiomas y no solo el del dueño
entradas: [textos en el idioma base, idiomas objetivo]
salidas: [recursos de idioma completos, con las claves que faltan declaradas]
herramientas: [tests de traducción, comparación de claves entre idiomas]
verificacion: [0 claves sin traducir en los idiomas declarados, o la lista de las que faltan]
depende_de: [compatibilidad-multiplataforma]
---

# Habilidad · traducir multilingüe

## Propósito
Que un idioma nuevo no deje huecos silenciosos. Una clave sin traducir en una app no es un detalle
cosmético: es una pantalla en blanco.

## Cuándo se usa
- Al añadir un idioma.
- Al añadir textos nuevos a la interfaz.
- Antes de una entrega que se anuncia multilingüe.

**No se usa** para traducir las publicaciones de la bandita: esas van en dominicano y punto.

## Pasos
1. Fijar el idioma base y la lista de claves.
2. Traducir y **comparar las claves**: el conjunto tiene que ser idéntico al del base.
3. Correr el test de traducciones presentes (en esta casa: `TraduccionesPresentesTest`, 6/6).
4. Las claves que no se tradujeron se listan, no se rellenan con el texto en inglés sin decirlo.

## Reglas duras
- **El español dominicano obligatorio es solo para las publicaciones de la bandita.** Las apps son
  multilingües; no se mezcla la regla de un canal con la de un producto.
- **Una traducción no se inventa para tapar un hueco**: se deja el idioma base y se declara.
- **Los textos de la interfaz no llevan marcado ni enlaces**: son texto plano que se lee en pantalla.

## Verificación
- El test de presencia de traducciones en verde, con su recuento.
- La lista de claves faltantes, si hay, escrita.

## Errores conocidos
- Añadir un idioma y no añadir sus claves: la app arranca y muestra huecos.
