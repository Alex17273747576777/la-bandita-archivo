---
name: informe-al-dueno
version: 1.1.0
dominio: control de calidad
nivel: medidor
cuando: al cerrar cualquier turno de trabajo
entradas: [lo hecho, lo medido, lo que falta]
salidas: [informe corto con cifras, correcciones propias y pendiente exacto]
herramientas: [git log, los informes de los medidores]
verificacion: [cada cifra del informe sale de un medidor, el pendiente se puede empezar]
depende_de: [sellar-y-publicar]
---

# Habilidad · informe al dueño

## Propósito
Decir en una pantalla qué se hizo, **qué se midió**, qué se corrigió de uno mismo y qué falta. Sin
adornos y sin esconder los fallos propios: los fallos del que informa son la información más útil.

## Cuándo se usa
- Al final de cada turno.

## Pasos
1. Las cifras, de los medidores: piezas, caracteres, cifras cotejadas, compuertas.
2. Los **errores propios** del bloque, uno por uno, con lo que se hizo para arreglarlos.
3. Lo que **no** se pudo hacer y por qué (hardware, credenciales, límites reales).
4. El pendiente exacto, en una línea, que se pueda empezar sin preguntar nada.

## Reglas duras
- **Ninguna cifra del informe se escribe de memoria**: se copia del medidor.
- **Nada de «todo listo»** si queda un pendiente.
- **Los fallos propios se cuentan igual que los logros.** Un informe sin correcciones propias es
  un informe incompleto.
- **No se declara verificado en dispositivo** lo que se midió en otro sitio.

## Verificación
- Cada número del informe se puede rastrear a un archivo o a un comando.
- El pendiente nombra archivo, herramienta o comando.
