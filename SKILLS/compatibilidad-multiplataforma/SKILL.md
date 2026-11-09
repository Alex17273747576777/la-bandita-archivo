---
name: compatibilidad-multiplataforma
version: 1.0.0
dominio: app
nivel: puerta
cuando: cuando un programa tiene que construirse y funcionar en más de una plataforma
entradas: [código, plataformas objetivo]
salidas: [compilación por plataforma, o la razón técnica exacta de por qué no]
herramientas: [Gradle, KMP, modelos ONNX Runtime, tests por plataforma]
verificacion: [compila en cada plataforma declarada, lo no probado se dice]
depende_de: [arranque-de-suelo]
---

# Habilidad · compatibilidad multiplataforma

## Propósito
Que «multiplataforma» signifique algo comprobable: **compila y arranca** en cada plataforma que se
declara, y donde no, se dice por qué. La multi-compatibilidad es requisito, no extra.

## Cuándo se usa
- Cuando se añade una plataforma nueva a la matriz.
- Cuando alguien dice «esto es multiplataforma» y hay que comprobarlo.
- Al preparar una entrega que se anuncia para varios sistemas.

**No se usa** para decidir si vale la pena portar algo: eso es una decisión, no una medición.

## Pasos
1. Definir la matriz: plataformas × arquitecturas (p. ej. arm64-v8a, armeabi-v7a, x86_64).
2. Compilar cada celda por separado y guardar el resultado.
3. Para código compartido (KMP), comprobar que el módulo común compila **sin** depender de una
   plataforma concreta; si depende, el código no era común.
4. Para modelos en dispositivo (ONNX Runtime), verificar que el modelo carga y da la misma respuesta
   en cada plataforma que se declara compatible.
5. Lo que no se pudo probar —emulador sin aceleración, dispositivo ausente— se **declara**, no se
   aprueba por omisión.

## Reglas duras
- **No se declara verificado en dispositivo** lo que se compiló en otro sitio. Sin `/dev/kvm` no hay
  emulador acelerado, y eso se dice tal cual.
- **Un APK que compila no es un APK que funciona.** Compilar es la puerta mínima, no la prueba.
- **Nada de nombres de paquete inventados**: si no está en el manifiesto o en la dependencia, no existe.
- **Las funciones de rendimiento y permisos se limitan al entorno de la propia app.** No se tocan
  gobernadores de CPU ni la frecuencia del panel.

## Verificación
- Tabla de plataformas con su resultado: compila sí/no, y la razón cuando no.
- La fila «no probado en dispositivo» está escrita, no vacía.

## Errores conocidos
- Dar por compatible una plataforma porque el módulo común compiló.
- Copiar un nombre de dependencia de memoria: 519 errores de compilación en esta casa salieron de ahí.
