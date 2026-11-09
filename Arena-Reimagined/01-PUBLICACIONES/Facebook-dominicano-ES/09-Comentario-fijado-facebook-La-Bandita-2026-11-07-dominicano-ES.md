━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 09 — Archivos, copias y nubes propias: cuatro de diecisiete dan la huella*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 09 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: 17 repositorios de archivos, copias de seguridad y nubes propias · API pública de GitHub
• Hora declarada de la medición: 18:27 · novena medición del día

Lo que dicen los números medidos:
• **17** repositorios vivos: **375.559 estrellas** y **70.615.524 descargas**. Nota mediana **48 de 80**.
• **4 publican huella**: AF-File-Manager (40 de 80), restic (30 de 284), rclone (30 de 510) y Hexora (8 de 28).
• **108 sumas de 1.449 casillas**: el **7,5 %** del tema.
• Los tres más instalados no firman ninguna: **LocalSend** (15.777.324 descargas, 133 archivos), **Immich** (4.882.000, 100 archivos) y **Nextcloud**.
• **AF-File-Manager** es el que más firma del tema: 82 días de vida, ★18, **50 entregas** y 40 sumas de 80.
• Las dos herramientas de copia del teléfono llevan **410 y 185 días** sin publicar.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
Una copia de seguridad que no has probado no es una copia: es un archivo más. Prueba a restaurar algo pequeño hoy, y comprueba el programa que va a guardar tus archivos antes de meterle la vida dentro.

#Rclone #Restic #Immich #LocalSend #CopiasDeSeguridad #GitHub #LaBandita #Verificacion #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
