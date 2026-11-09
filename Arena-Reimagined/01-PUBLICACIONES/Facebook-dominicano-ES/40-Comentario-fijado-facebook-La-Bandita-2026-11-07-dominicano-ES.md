━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 40 — La lección del hash SHA-256 · premio de La Bandita*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 40 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: los recursos citados en la publicación · API pública de GitHub
• Hora declarada de la medición: noche del sábado en Santo Domingo

Lo que dicen los números medidos:
• Un hash SHA-256 son **sesenta y cuatro caracteres** que resumen un archivo entero.
• Si cambia **un solo bit** del archivo, el hash cambia por completo: no hay manera de disimularlo.
• Se calcula en el teléfono con Termux (`sha256sum`) o en la computadora, sin instalar nada raro.
• Comprobar una suma cuesta **menos de un minuto**; no comprobarla cuesta el archivo entero.
• Una suma publicada en la misma descarga que el archivo no vale gran cosa: sirve la que se publica **aparte** —en la pieza, en las notas de la entrega o en un archivo `.sha256` suelto—.
• El premio de esta casa es para el que publica la huella **antes** de que se la pidan.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
Descarga el archivo, calcula su SHA-256, compáralo con el que publicó el autor y guarda el resultado. Si los sesenta y cuatro caracteres coinciden, tienes lo que el autor publicó; si no, no lo tienes, diga lo que diga el nombre del archivo.

#SHA256 #Hash #Verificacion #Seguridad #Android #GitHub #LaBandita #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
