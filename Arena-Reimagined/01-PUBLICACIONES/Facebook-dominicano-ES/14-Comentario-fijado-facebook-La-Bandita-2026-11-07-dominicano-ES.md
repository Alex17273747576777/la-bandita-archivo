━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 14 — Spotify sin Spotify: treinta y ocho clientes medidos hoy*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 14 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: 38 clientes de música · API pública de GitHub
• Hora declarada de la medición: 22:10 · decimoquinta medición del día

Lo que dicen los números medidos:
• **38** programas: **252.059 estrellas** y **41.213.007 descargas**.
• **495 archivos firmados de 2.473**: el **20,0 %**, la proporción más alta de la serie.
• Nota mediana **57 de 80**, la más alta de las quince piezas.
• Los mejores: **OmnIGet 77**, **LastWave Native 76**, **Spotube 73**, **limusic 73** y **Levyra 71**.
• **Cuatro de esos cinco no firman ni un archivo**: el que más trabaja no es el que más garantiza.
• **Quince nacieron en 2026**; **tres están muertos** —ViMusic (archivado, ★9.468), SpotiFlyer y spotify-tui—.
• **Uno solo** de los 38 no declara licencia legible. Ninguno sin entrega etiquetada y ninguno sin integración continua.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
El catálogo no es tuyo y no lo va a ser. El programa que lo lee sí: su código, su versión, su fecha y su firma. Instala desde el repositorio del autor y comprueba el archivo.

#Spotify #OmnIGet #Spotube #LastWave #Clientes #GitHub #LaBandita #Verificacion #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
