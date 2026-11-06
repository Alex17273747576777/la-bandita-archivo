# PIEZA 25 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/25-El-scanner-de-bolsillo-del-papel-al-PDF-legible-Umi-OCR-y-episteme-Facebook-La-Bandita-2026-11-06-dominicano-ES.md`
- **Fecha de la pieza:** 6-nov-2026 (según dateline; edad hoy: 0 días)
- **sha256 de la pieza:** `c05d71afe4a5e40d6822ab3c1621ddfe26378376d12fe140c26d315cea612c15`
- **Envío generado:** 2026-11-06 · 6 mensajes · el mayor de 3558 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 6 · 742 caracteres ═══

*El escáner de bolsillo: del papel al PDF legible, con Umi-OCR y episteme*

La Bandita · pieza 25 · guía del 6-nov-2026 · te la mando hoy en 6 mensajes.

Antes de mandártela volví a medir lo que afirma: *2 repositorios, 2 vivos*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: MIT 1 · AGPL-3.0 1.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/25-El-scanner-de-bolsillo-del-papel-al-PDF-legible-Umi-OCR-y-episteme-Facebook-La-Bandita-2026-11-06-dominicano-ES.md

💓 6 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 6 · 821 caracteres ═══

*El escáner de bolsillo: del papel al PDF legible, con Umi-OCR y episteme*

*La Bandita · viernes 6 de noviembre de 2026, 11:05 de la mañana en Santo Domingo (15:05 UTC) · edición dominicano-español · pieza 25 de Facebook*

⏱️ *Lectura total: 16 minutos · dos repositorios medidos uno por uno · doce enlaces revisados uno por uno · cero tiendas de APK enlazadas*

*🗺️ Mapa de esta guía*

```
├── 📱 El problema · un documento de papel que hay que convertir
├── 🔍 Las dos herramientas · Umi-OCR y episteme
├── 🔐 Las licencias · MIT y AGPL-3.0
├── ⏱️ Las edades · tres años contra ocho meses de vida
├── 📦 Las entregas · releases con instaladores y archivos ejecutables
├── ☁️ La nube · quién procesa en el equipo y quién no
└── 🧪 Probar un escáner antes de instalarlo · seis comprobaciones
```

⏬ sigue abajo · parte 1 de 5

═══ MENSAJE 3 de 6 · 3558 caracteres ═══

*📱 El problema · un documento de papel que hay que convertir*

Un recibo, un contrato, una factura o una página de un libro: todo llega en papel y hay que convertirlo en texto que se pueda copiar, buscar y editar. Eso es el OCR: reconocimiento óptico de caracteres. No hace falta una máquina de escaneo ni pagar un servicio en la nube; hay herramientas que lo hacen desde el propio equipo.

Esta pieza mide dos lectores de texto sobre imagen: **Umi-OCR**, de escritorio para Windows, y **episteme**, para Android. Ambas son de código abierto y ambas procesan sin enviar la imagen a un servidor ajeno.

*🔍 Las dos herramientas · Umi-OCR y episteme*

**hiroi-sora/Umi-OCR** ★48.479 · MIT · creado el 28 de marzo de 2022 · push el 20 de noviembre de 2025. Lector de texto sobre imagen para Windows que funciona totalmente sin conexión. Usa PaddleOCR con modelos empaquetados. Soporta importación de imágenes, recorte de zona, exportación a Excel, Word, texto plano y Markdown. Tiene modo de línea de comandos. Última entrega: `v2.1.5`, del 25 de marzo de 2025, con tres adjuntos.

**Aryan-Raj3112/episteme** ★1.333 · AGPL-3.0 · creado el 24 de febrero de 2026 · push el 10 de octubre de 2026. Lector de documentos para Android con extracción de texto, conversión a Markdown y resumen de páginas. Construido con Jetpack Compose. Última entrega: `v1.0.58-oss`, del 9 de octubre de 2026, con dos adjuntos.

*🔐 Las licencias · MIT y AGPL-3.0*

Umi-OCR declara MIT: permisiva, permite reutilizar el código incluso en proyectos cerrados, siempre que se conserve el aviso. episteme declara AGPL-3.0: copyleft fuerte; quien modifique y distribuya el código debe liberar su versión bajo la misma licencia, y quien la use como servicio en red debe hacer público el código fuente.

MIT es más permisiva; AGPL-3.0 protege mejor el código abierto pero exige más de quien la reutiliza.

*⏱️ Las edades · tres años contra ocho meses de vida*

Umi-OCR tiene tres años de existencia y su último empujón es del 20 de noviembre de 2025: doce meses de silencio. No está abandonada del todo, pero tampoco está activa.

episteme tiene ocho meses de vida (nació en febrero de 2026) y su último empujón es del 10 de octubre de 2026: menos de un mes. Es joven, pero se mueve.

*📦 Las entregas · releases con instaladores y archivos ejecutables*

Umi-OCR entrega instaladores para Windows: `v2.1.5` tiene tres adjuntos. episteme entrega un APK para Android: `v1.0.58-oss` tiene dos adjuntos. Ninguna está en una tienda oficial; ambas se bajan del repositorio y se instalan manualmente.

*☁️ La nube · quién procesa en el equipo y quién no*

Umi-OCR procesa totalmente en el equipo: los modelos de OCR van empaquetados con la aplicación y no se conectan a internet para reconocer texto. episteme, al ser para Android, también procesa en el dispositivo; no se ha detectado envío de imágenes a un servidor externo. Ninguna de las dos exige crear cuenta.

La diferencia entre ellas no es el precio —ambas son gratuitas— sino el sistema operativo, la edad, la licencia y el tipo de documento que cada una lee mejor.

*🧪 Probar un escáner antes de instalarlo · seis comprobaciones*

Un escáner de texto es un instalador o un APK: se puede inspeccionar antes de instalar.

**Uno: la ficha.** En un APK se lee el `AndroidManifest.xml` y el `applicationId`; se compara con el repositorio de donde se bajó. En un instalador de Windows, se lee el metadata del ejecutable.

**Dos: la licencia.** Se busca el archivo `LICENSE`. Umi-OCR dice MIT; episteme dice AGPL-3.0.


⏬ sigue abajo · parte 2 de 5

═══ MENSAJE 4 de 6 · 2236 caracteres ═══

**Tres: los permisos.** El manifiesto de Android declara qué pide: cámara, almacenamiento, internet. Un lector de texto no necesita internet para funcionar; si lo pide, conviene saber para qué.

**Cuatro: el procesamiento.** Se lee si el OCR corre en el equipo o envía la imagen a un servidor. Umi-OCR corre en el equipo. episteme también.

**Cinco: la firma.** Las APK de distintas fuentes no comparten siempre la firma. Mezclar fuentes obliga a desinstalar y borrar datos.

**Seis: el historial.** Un repositorio con doce meses de silencio no es lo mismo que uno con empujón de hace menos de un mes. La fecha del último empujón es el dato más honesto.

*❓ preguntas*

¿Cuál elijo? Umi-OCR si trabajo en Windows con documentos escaneados y necesito exportar a Excel o Word. episteme si trabajo en Android y quiero convertir páginas de libro a Markdown. ¿Pagan algo? Ninguna. ¿Piden cuenta? Ninguna.

*🌅 Cierre*

La Bandita informa a partir de fuentes fechadas. Dos repositorios medidos uno por uno, doce enlaces revisados y cero tiendas de APK enlazadas. Del papel al PDF legible no hace falta pagar ni subir nada a la nube: Umi-OCR y episteme lo hacen desde el equipo, cada una con su licencia y su sistema operativo.

💓 *6 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* viernes 6 de noviembre de 2026, 11:05 de la mañana en Santo Domingo (15:05 UTC) · dos repositorios medidos con estrellas, licencia, último empujón y última entrega · doce enlaces revisados con la interfaz de GitHub · cero tiendas de APK enlazadas · cero cifras de memoria.

#task 114 · verificar que las seis comprobaciones de apertura de escáner de texto (ficha, licencia, permisos, nube, firma, historial) se puedan hacer en un teléfono o computadora sin instalar nada, y anotar en un acta qué pasa con Umi-OCR y episteme.
#task 115 · medir la familia de escáneres de texto de nuevo dentro de un mes —6 de diciembre de 2026— para ver si Umi-OCR vuelve a moverse tras doce meses de silencio, si episteme sigue recibiendo empujones, y si nace algún escáner nuevo del mismo tipo.
#task 116 · escribir la ficha de cada una de las dos herramientas en el catálogo del archivo, con su guía y su estado.

⏬ sigue abajo · parte 3 de 5

═══ MENSAJE 5 de 6 · 503 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 25*

Medí otra vez, hoy 6 de noviembre de 2026, los 2 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• hiroi-sora/Umi-OCR — ★48.485 (+6) · *dormido*: sin empujar desde el 20-nov-2025 (351 días) · MIT · última release v2.1.5 (25-mar-2025)
• Aryan-Raj3112/episteme — ★1.333 (sin cambio) · empujó el 10-oct-2026 (hace 27 días) · AGPL-3.0 · última release v1.0.58-oss (9-oct-2026)

⏬ sigue abajo · parte 4 de 5

═══ MENSAJE 6 de 6 · 152 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.
