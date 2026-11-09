━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 11 — Las aplicaciones que leen lo que la pieza 10 midió*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 11 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: 51 aplicaciones lectoras de extensiones · API pública de GitHub
• Hora declarada de la medición: 20:45 · undécima medición del día

Lo que dicen los números medidos:
• **51** aplicaciones vivas: **103.457 estrellas** y **58.427.498 descargas**. Nota mediana **49 de 80**.
• **116 archivos firmados de 2.104**, casi el doble que las tiendas de la pieza 10.
• Las tres mejores: **Kototoro** (75, 27 archivos firmados de 118), **Mangatan** (75, 20 de 70) e **Ito** (69, 20 de 40).
• **Solo 5 de 51** no declaran licencia.
• **10 nacieron en los últimos 90 días**; cuatro de ellas ya pasan de 45 puntos.
• **2 archivadas** (Kotatsu, ★8.951; Sorayomi, ★1.571), **5 sin entrega etiquetada** y **4 sin integración continua**.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
La extensión no se ejecuta sola: alguien tiene que leerla, descomprimirla y darle permisos, y ese alguien es la aplicación. Elige primero la aplicación que firma, después la extensión.

#Mihon #Kototoro #Mangatan #Ito #Lectores #GitHub #LaBandita #Verificacion #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
