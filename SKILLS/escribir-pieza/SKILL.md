---
name: escribir-pieza
version: 1.0.2
dominio: redacción
cuando: con el censo cerrado y la banda declarada en docs/bandas.json
entradas: [censo, banda min/max, tema, piezas vecinas para no repetir]
salidas: [pieza Markdown completa, dentro de banda, con forma M01–M23]
herramientas: [docs/bandas.json, tools/manual_gate.py, script de párrafos repetidos]
verificacion: [manual_gate VERDE, longitud en banda, remate propio único]
---

# Skill · escribir una pieza

## Propósito
Escribir de una vez una pieza que pase la compuerta, con voz propia y datos del censo de hoy.

## Pasos
1. **Mapa primero.** Escribir el `🗺️` con 5–12 secciones reales; sirve de esqueleto.
2. **Tandas de contenido real**, no de relleno: cada tanda es una sección completa (1.500–4.000
   caracteres) con encabezado en negrita y separador `───────────────────`.
3. Contar caracteres después de cada tanda; apuntar hacia la banda, no pasarla de golpe.
4. Al llegar a ~39.500, escribir las secciones fijas: tabla + cinco mitos + glosario, enlaces y
   cierre con diálogo.
5. Cerrar en el orden exacto: diálogo → **firma con remate propio** → medición del corte → licencia de
   la entrega → notas al pie fechadas.
6. Pasar `manual_gate.py --pieza`. Rojo no se entrega: se corrige la causa.
7. Anotar la longitud real en `docs/bandas.json`.

## Reglas duras
- **Cada pieza se escribe desde su propio censo.** Prohibido reciclar plantilla, listados viejos o
  frases comodín.
- **El remate de la firma es único** entre todas las piezas: si se repite, M03 la caza.
- **La línea de licencia se redacta distinta cada vez**: es el párrafo que más se repite y el que
  rompe M23.
- **Nada de meta-comentarios** («en esta sección voy a…»).
- **La banda es la banda**: 40.000–45.000 en Facebook, 4.000–7.000 en WhatsApp.

## Verificación
`MANUAL GATE · 1 piezas · VERDE 1 · ROJO 0`, longitud dentro de banda, y comparación de párrafos
largos contra las piezas vecinas sin coincidencias.

## Errores conocidos
- Escribir el cierre antes de tener las secciones fijas: obliga a reescribirlo dos veces.
- Dejar la firma antes de las notas al pie: G12 la marca aunque exista.
- Tandas de 300 caracteres: multiplican los turnos sin avanzar (usar 1.500+).
