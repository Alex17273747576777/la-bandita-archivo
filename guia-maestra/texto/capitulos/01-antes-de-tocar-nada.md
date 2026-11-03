# Capítulo 1 · Antes de tocar nada

## Qué vas a poder hacer al terminar

Guardar todo lo que hay en tu teléfono de forma que puedas volver atrás, saber qué se pierde y qué no, y tener por escrito la lista de lo que tenías instalado. Suena a trámite. Es el capítulo que decide si los otros once te cuestan una tarde o te cuestan el teléfono.

## La regla que ordena todo lo demás

**Ninguna operación de esta guía es irreversible si antes se hizo una copia.** Y ninguna copia sirve si vive dentro del aparato que se va a tocar. Esa segunda mitad es la que se olvida: una copia en la memoria interna del teléfono que vas a formatear no es una copia, es una foto pegada en la pared de la casa que se está quemando.

## Qué se pierde y qué no, en orden de importancia

**Lo que no se recupera de ninguna manera.** Las conversaciones de WhatsApp sin copia en su nube, las fotos que solo existen en el carrete, las notas del teléfono, los códigos de verificación en dos pasos que viven en una aplicación de autenticación y no tienen copia de seguridad, las claves de las redes wifi guardadas. Nada de esto se vuelve a generar solo.

**Lo que se recupera con trabajo.** Las aplicaciones que se bajaron de una tienda se vuelven a bajar; lo que se pierde es la sesión y la configuración, y volver a iniciar sesión en treinta aplicaciones es una tarde.

**Lo que se recupera fácil.** La lista de contactos si estaba sincronizada, las fotos si estaban en una nube, los archivos que también están en la computadora.

**Lo que no se pierde nunca y la gente cree que sí.** Las licencias de las aplicaciones de pago compradas con una cuenta, las suscripciones, los historiales de compra. Eso vive en la cuenta, no en el aparato.

## La copia mínima, en cuatro pasos y sin instalar nada

Antes de hablar de aplicaciones, hay una copia que no necesita ninguna y que casi nadie hace.

**Paso uno: la lista de paquetes.** Con la depuración activada y el teléfono conectado, una sola orden guarda el nombre exacto de todo lo que tienes instalado, incluidas las aplicaciones que el menú no muestra:

```
adb shell pm list packages -u > lista-de-paquetes.txt
```

Ese archivo pesa unos kilobytes y sirve para reconstruir la memoria de lo que había. Es la copia más pequeña y la más útil que existe.

**Paso dos: las fotos y los archivos.** Copiarlos a la computadora por cable. Es el método más aburrido y el único que no depende de que un servicio siga existiendo.

**Paso tres: los códigos de verificación en dos pasos.** Si el teléfono es el segundo factor de tus cuentas, una copia mal hecha te deja fuera de tu propio correo. Antes de formatear, exporta las semillas de tu aplicación de autenticación, o comprueba que tienes los códigos de recuperación de cada servicio importante.

**Paso cuatro: la frase de recuperación de cualquier copia cifrada.** Si vas a usar una copia con contraseña, esa frase se escribe en un papel y el papel se guarda fuera del teléfono. Es el único paso que no se puede repetir después.

## La decisión: qué herramienta, según lo que tengas

**Si tu teléfono no tiene root y no quieres ponerlo:** la lista de paquetes más una copia de archivos a la computadora. Para los datos de las aplicaciones, las herramientas de este capítulo funcionan con el permiso prestado del capítulo 3, pero solo para las aplicaciones que permiten copia. Las que no la permiten se quedan fuera y hay que decirlo: el sistema las protege a propósito.

**Si tu teléfono tiene root:** las copias son completas y las tres primeras fichas de este capítulo hacen el trabajo. Con root también puedes copiar lo que el sistema protege.

**Si tu sistema trae copia integrada:** empieza por ahí. Está probada por el fabricante, se cifra sola y no hay que instalar nada. Su límite es que solo funciona en los teléfonos que la traen.

## Cómo se sabe que una copia sirve

No por el tamaño del archivo ni por el mensaje de «completado». Por tres comprobaciones que se hacen en este orden:

**Primera: el destino sobrevive.** Abre la carpeta de la copia desde otro aparato. Si no puedes verla desde fuera del teléfono, no tienes copia.

**Segunda: el recuento coincide.** Cuenta las aplicaciones del teléfono y cuenta las que hay en la copia. Si los números no coinciden, mira cuáles faltan antes de formatear, no después.

**Tercera: la restauración de prueba.** Restaura una sola aplicación en el teléfono nuevo y comprueba que vuelve con sus datos. Una copia que nunca se restauró es una hipótesis, no una copia.

## Los tres errores que se cometen siempre

**Guardar la copia dentro del teléfono.** El más común y el más caro. La copia tiene que estar en una tarjeta que se saca, en la computadora o en un servidor de tu casa.

**Copiar los datos y no el paquete.** Si la aplicación desaparece de la tienda, los datos no valen nada. Y si reinstalas el paquete desde otro sitio, la firma no coincide y la restauración se niega.

**Confundir «he hecho copia» con «he hecho copia comprobada».** El mensaje de terminado no prueba nada; la restauración de prueba sí.

## Lo que este capítulo no resuelve

No enseña a hacer una copia completa del sistema, que es otra cosa y necesita otro tipo de herramientas. No reemplaza a la copia en la nube para las fotos si ya la usas y te funciona. Y no evita que un teléfono se rompa: evita que, cuando se rompa, se lleve tus cosas con él.

## Las cinco fichas

Van de la más simple a la más exigente, y están pensadas para usarse en ese orden si es la primera vez. La primera no necesita root ni permiso y sirve para cualquier teléfono; la última solo funciona en los aparatos que ya la traen de fábrica. Todas declaran para quién son y para quién no, y todas traen un dato de oficio con su comando para comprobarlo sin creerle nada a esta guía.
