---
name: medir-en-dispositivo
version: 1.0.0
dominio: app
nivel: medidor
cuando: cuando hay que saber si algo funciona en un teléfono de verdad
entradas: [APK, dispositivo o emulador disponible]
salidas: [resultado medido, o la declaración de que no se pudo medir]
herramientas: [adb, emulador, logs]
verificacion: [el resultado dice en qué se midió y en qué no]
depende_de: [construir-y-entregar-apk]
---

# Habilidad · medir en dispositivo

## Propósito
Distinguir entre «compila», «arranca en un emulador» y «funciona en un teléfono». Son tres cosas
distintas y confundirlas es la forma más común de mentir sin querer.

## Cuándo se usa
- Cuando hay que afirmar que algo funciona y no solo que compila.
- Antes de decir «probado».
- Cuando el dueño pregunta si se probó en un teléfono.

**No se usa** para aprobar por omisión: si no hay dispositivo, la respuesta es «no medido».

## Pasos
1. Comprobar qué hay disponible: `adb devices`, `/dev/kvm`, RAM.
2. Si hay dispositivo: instalar, abrir, provocar el caso y leer el registro.
3. Si solo hay emulador sin aceleración: se puede compilar y a veces arrancar; **decirlo** y no
   presentarlo como prueba en dispositivo.
4. Si no hay nada: escribir «no medido en dispositivo» y seguir. Es una respuesta válida.

## Reglas duras
- **Nunca declarar verificado en dispositivo** algo que se midió en otro sitio. Sin `/dev/kvm` no hay
  emulador acelerado, y el hardware no se discute: se dice y se continúa.
- **La RAM no es una objeción**: si el hardware lo permite pero la herramienta no, se dice cuál falló.
- **Un test que pasa en el emulador no prueba el teléfono**, prueba el emulador.

## Verificación
- El informe dice dónde se midió cada cosa.
- La fila «no medido» existe cuando toca.

## Errores conocidos
- Presentar un `assembleDebug` exitoso como «la app funciona».
- Reintentar el emulador diez veces cuando el problema es la ausencia de aceleración.
