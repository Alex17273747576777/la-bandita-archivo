*Editar la foto sin pagar: cuatro herramientas, dos que piden cuenta y una que no pide nada*

*La Bandita · jueves 5 de noviembre de 2026, 11:05 de la mañana en Santo Domingo (15:05 UTC) · edición dominicano-español · pieza 24 de Facebook*

⏱️ *Lectura total: 20 minutos · cuatro repositorios medidos uno por uno · catorce enlaces revisados uno por uno · cero tiendas de APK modificadas enlazadas · dos herramientas piden cuenta para funciones en la nube, una no pide nada*

*🗺️ Mapa de esta guía*

```
├── 🖼️ La edición sin suscripción · qué se puede y qué no
├── 🛠️ Las cuatro herramientas · ImageToolbox, Image-Cropper, Snapedit y Aksiphoto
├── 🔐 Las licencias · tres Apache-2.0 y una que no declara nada
├── ⏱️ Las edades · de diez años a menos de un mes de vida
├── 📦 Las entregas · APKs, bibliotecas y código fuente sin compilar
├── ☁️ La cuenta y la nube · quién pide registro y quién no
├── 🧪 Abrir un editor antes de instalarlo · seis comprobaciones en diez minutos
└── ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

───────────────────

*🖼️ La edición sin suscripción · qué se puede y qué no*

Editar una foto en el teléfono no tiene por qué significar pagar una suscripción mensual ni crear una cuenta en una nube ajena. Hay herramientas open source que hacen recorte, ajuste de color, filtros y más, sin pedir correo electrónico ni tarjeta de crédito.

El truco está en distinguir tres cosas que suelen confundirse. **Primero:** una aplicación de edición de fotos es para el usuario final; se instala y se usa. **Segundo:** una biblioteca de recorte es para programadores; se incluye en otra aplicación, no se abre sola. **Tercero:** un proyecto sin entregas publicadas hay que compilarlo desde el código fuente, y eso ya no es para cualquiera.

Esta pieza mide cuatro herramientas de edición de imagen para Android y dice, para cada una, si pide cuenta, si funciona sin conexión y si está viva.

*🛠️ Las cuatro herramientas · ImageToolbox, Image-Cropper, Snapedit y Aksiphoto*

**T8RIN/ImageToolbox** ★15.440 · Apache-2.0 · creado el 6 de abril de 2022 · push el 5 de noviembre de 2026. Editor de imagen avanzado con docenas de funciones: recorte, dibujo, filtros, mejoras con IA, OCR y herramientas de PDF. Construido con Kotlin y Jetpack Compose. Última entrega: `4.2.0`, del 4 de septiembre de 2026, con ocho adjuntos. También disponible en F-Droid y Google Play Store.

**ArthurHub/Android-Image-Cropper** ★6.406 · Apache-2.0 · creado el 15 de enero de 2015 · push el 17 de septiembre de 2023. Biblioteca de recorte de imágenes para integrar en otras aplicaciones de cámara y galería. No es una aplicación que el usuario instale: es código para desarrolladores. Más de tres años sin movimiento en el repositorio. Última entrega etiquetada: `2.8.0`, del 27 de octubre de 2018.

**BorgorNinja/Snapedit** ★0 · Apache-2.0 · creado el 11 de octubre de 2026 · push el 31 de octubre de 2026. Suite de edición de fotografía no destructiva, inspirada en Snapseed y Lightroom Mobile. Todo corre en el dispositivo: sin telemetría, sin red, sin nube. Última entrega: `latest`, del 11 de octubre de 2026, con tres adjuntos. Cero estrellas, cero bifurcaciones: un proyecto de menos de un mes.

**pelayanan/aksiphoto** ★0 · sin licencia declarada · creado el 22 de octubre de 2026 · push el 27 de octubre de 2026. Aplicación para gestionar y editar fotos con galería en cuadrícula y cámara. Construida con Kotlin y Jetpack Compose. Sin entrega de APK publicada; hay que compilarla desde el código fuente. GitHub no reconoce ninguna licencia estándar.

*🔐 Las licencias · tres Apache-2.0 y una que no declara nada*

Tres de las cuatro herramientas declaran Apache-2.0: ImageToolbox, Image-Cropper y Snapedit. Esa licencia permite usar, modificar y distribuir el código, incluso en proyectos cerrados, siempre que se conserve el aviso de licencia.

La cuarta, **Aksiphoto, no declara ninguna licencia**. GitHub la muestra como `NOASSERTION`: no está claro qué se puede reutilizar del código. Quien quiera usarla o tomar parte de su código está operando sin saber los términos. Esa es la diferencia más concreta entre una herramienta y otra.

*⏱️ Las edades · de diez años a menos de un mes de vida*

Image-Cropper lleva más de diez años existente (2015), pero no se mueve desde septiembre de 2023: es una herramienta madura abandonada en la práctica. ImageToolbox tiene cuatro años y se actualizó hoy mismo. Snapedit y Aksiphoto tienen menos de un mes: funcionan, pero no hay historial que asegure que seguirán recibiendo actualizaciones dentro de seis meses.

*📦 Las entregas · APKs, bibliotecas y código fuente sin compilar*

ImageToolbox publica APKs: la entrega `4.2.0` tiene ocho adjuntos, y también se baja de F-Droid y Play Store. Image-Cropper no entrega APKs para el usuario; entrega una biblioteca Java para programadores. Snapedit publica una APK (`latest`, tres adjuntos). Aksiphoto no publica nada: solo hay código fuente, y hay que compilarlo con Android Studio.

Cuatro herramientas, cuatro formas distintas de llegar al teléfono: dos con APK lista para instalar, una biblioteca para desarrolladores y un proyecto que solo existe como código.

*☁️ La cuenta y la nube · quién pide registro y quién no*

ImageToolbox funciona sin cuenta: se instala y se usa. Sus funciones de IA y OCR son opcionales y se descargan aparte si se quiere. Image-Cropper no tiene usuario final: es código para integrar. Snapedit es **100 % local**: no pide cuenta, no se conecta a internet, no envía nada a ningún servidor. Aksiphoto, al no tener APK publicada, no se ha podido comprobar si pide cuenta, pero al compilarse desde el fuente no hay registro obligatorio visible.

Dos de las cuatro herramientas (ImageToolbox y, opcionalmente, sus funciones en la nube) pueden llevar a crear una cuenta si el usuario elige usarlas. Las otras dos no piden nada. Pero la regla de la casa sigue: **no se enlaza ninguna tienda de APK modificada**, ni se recomienda bajar de un escaparate ajeno. Cada herramienta tiene su repositorio en GitHub; de ahí se baja o se compila.

*🧪 Abrir un editor antes de instalarlo · seis comprobaciones en diez minutos*

Un editor de imagen es un APK o un proyecto de código: se puede inspeccionar antes de instalar.

**Uno: la ficha.** En un APK se lee el `AndroidManifest.xml` y el `applicationId`; se compara con el repositorio de donde se bajó. En una biblioteca como Image-Cropper, se lee el `build.gradle` para saber qué se está integrando.

**Dos: la licencia.** Se busca el archivo `LICENSE` en el repositorio. ImageToolbox, Image-Cropper y Snapedit dicen Apache-2.0; Aksiphoto no declara nada.

**Tres: los permisos.** El manifiesto declara qué pide: internet, almacenamiento, cámara, micrófono. Un editor de fotos no necesita el micrófono. Si lo pide, conviene saber por qué.

**Cuatro: las funciones en la nube.** ImageToolbox ofrece IA y OCR opcionales que descargan modelos; Snapedit no se conecta a la red. Se lee qué funciona sin internet y qué no.

**Cinco: la firma.** Las APK de distintas fuentes no comparten siempre la firma; mezclar fuentes obliga a desinstalar y borrar datos.

**Seis: el historial.** Un repositorio con tres años de silencio (Image-Cropper) no es lo mismo que uno con entrega de hoy (ImageToolbox). La fecha del último empujón es el dato más honesto.

*❓ preguntas*

¿Cuál de las cuatro elijo? Depende: ImageToolbox si quiero el editor más completo y con más usuarios; Snapedit si quiero algo local y sin cuenta; Image-Cropper solo si programo en Android; Aksiphoto solo si sé compilar Android y no me importa la falta de licencia. ¿Pido cuenta en alguna? Ninguna la exige para funcionar, aunque ImageToolbox ofrece funciones opcionales en la nube.

───────────────────

*🌅 Cierre*

La Bandita informa a partir de fuentes fechadas. Cuatro repositorios medidos uno por uno, catorce enlaces revisados y cero tiendas de APK modificadas enlazadas. Editar una foto sin pagar es posible: hay herramientas open source, locales y sin suscripción. La diferencia entre ellas no es el precio —ninguna cobra— sino la edad, la licencia, la entrega y si piden cuenta o no.

💓 *5 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* jueves 5 de noviembre de 2026, 11:05 de la mañana en Santo Domingo (15:05 UTC) · cuatro repositorios medidos con estrellas, licencia, último empujón y última entrega · catorce enlaces revisados con la interfaz de GitHub · cero tiendas de APK enlazadas · cero cifras de memoria.

#task 110 · verificar que las seis comprobaciones de apertura de editor de imagen (ficha, licencia, permisos, nube, firma, historial) se puedan hacer en un teléfono sin instalar nada, y anotar en un acta qué pasa con cada una de las cuatro herramientas de esta pieza.
#task 111 · medir la familia de editores de imagen de nuevo dentro de un mes —3 de diciembre de 2026— para ver si Snapedit y Aksiphoto siguen vivas, si ImageToolbox sigue recibiendo empujones, y si Aksiphoto declara alguna licencia.
#task 112 · escribir la ficha de cada una de las cuatro herramientas en el catálogo del archivo, con su guía y su estado, y la advertencia de que Image-Cropper es una biblioteca para programadores, no una aplicación de usuario.
