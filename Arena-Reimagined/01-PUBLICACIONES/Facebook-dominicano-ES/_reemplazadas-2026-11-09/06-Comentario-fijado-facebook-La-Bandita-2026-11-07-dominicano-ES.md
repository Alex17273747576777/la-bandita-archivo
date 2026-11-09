━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 06 — El taller*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 06 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: 17 repositorios de gestores y conjuntos de parches · API pública de GitHub
• Hora declarada de la medición: 10:30 de la mañana en Santo Domingo

Lo que dicen los números medidos:
• **17** repositorios medidos: **5 publican al menos una huella** (29,4 %).
• **190** archivos adjuntos en las últimas entregas: **55 con huella** (28,9 %).
• Los conjuntos de parches —lo que se aplica sobre tu aplicación— **no firman ninguno**.
• Los cinco que firman: `MorpheApp/morphe-manager`, `ReVanced/revanced-api`, `ReVanced/revanced-integrations`, `ReVanced/revanced-manager` y `brosssh/revanced-manager-downloaders`.
• `Jman-Github/Patch-Bundle-Registry` pesa más de un gigabyte y **no publica ni una entrega**.
• `ReVanced/revanced-integrations` sigue archivado desde octubre de 2024 y acumula 1.939.884 descargas.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
Un gestor de parches modifica otras aplicaciones. Instálalo solo desde el repositorio del autor, y comprueba el archivo del gestor **antes** de aplicarle nada a tu aplicación: si el gestor viene intervenido, el resultado también.

#ReVanced #Morphe #Parches #Android #GitHub #LaBandita #Verificacion #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
