---
name: construir-y-entregar-apk
version: 1.0.0
dominio: app
nivel: puerta
cuando: cuando hay que producir un instalable y dejarlo publicado
entradas: [código compilable, versión, canal de entrega]
salidas: [APK con nombre y versión, sha256, tamaño, publicación con la huella]
herramientas: [Gradle, apksigner, sha256sum, gh release]
verificacion: [el APK sube, su sha256 coincide con el local, el enlace responde]
depende_de: [compatibilidad-multiplataforma]
---

# Habilidad · construir y entregar un APK

## Propósito
Que el archivo que baja el usuario sea **el que se compiló aquí**, y que se pueda comprobar sin
confiar en nadie.

## Cuándo se usa
- Al cerrar una versión del programa.
- Cuando se cambia el código de firma o el número de versión.
- Siempre que vaya a haber un enlace de descarga público.

**No se usa** para probar la app: un APK publicado no es una app probada.

## Pasos
1. Compilar en modo release con la firma declarada.
2. Anotar tres cosas del archivo: **nombre con versión**, **tamaño en bytes** y **sha256**.
3. Publicar y **verificar el remoto**: bajar el asset o comparar su `digest` contra el local.
4. Dejar la huella escrita junto al enlace, para que el usuario pueda correr `sha256sum`.
5. Si el APK es grande (esta casa entregó uno de 488 MB), decirlo con el número: el usuario tiene
   derecho a saber qué está bajando.

## Reglas duras
- **Prohibido almacenar recursos en el almacenamiento interno; única excepción: los tokens.**
- **Nada sale del dispositivo sin consentimiento o llave del usuario**, y eso se dice en la app.
- **La versión va en el nombre del archivo**, no solo en el manifiesto.
- **Un release sin huella publicada no está entregado**, solo subido.

## Verificación
- `sha256sum` local == el publicado.
- El enlace de descarga responde 200 y el tamaño coincide.

## Errores conocidos
- Publicar y dar por bueno el asset sin bajar el remoto.
- Subir el APK y olvidar el `sha256` en el texto: el usuario no tiene con qué comprobar.
