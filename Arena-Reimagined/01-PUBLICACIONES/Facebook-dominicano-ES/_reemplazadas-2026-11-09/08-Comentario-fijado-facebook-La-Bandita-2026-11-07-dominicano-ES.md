━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 08 — La red: seis caminos, seis precios*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 08 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: 20 repositorios de red · API pública de GitHub
• Hora declarada de la medición: 18:14 · octava medición del día

Lo que dicen los números medidos:
• **20** repositorios vivos: **205.629 estrellas** y **51.193.255 descargas**.
• **5 de 20 publican huella**. Nota mediana: **39 sobre 80**.
• Los dos más instalados no firman nada: **hiddify** (24 millones de descargas, 140 adjuntos) y **sing-box** (14,7 millones, 1.675 adjuntos), **ni una suma entre los dos**.
• La nota más alta de la serie: **tachyon**, 114 días, ★560, **80 de 80**, diez sumas de setenta adjuntos.
• Seis caminos: VPN comercial (Mullvad, 69), VPN propia por WireGuard (wg-easy, 55), malla (Headscale 74, NetBird 63), túnel y proxy (sing-box 49, hiddify 50), DNS privado y cortafuegos por aplicación.
• La nota más baja: **NetControl**, 34 días, ★7, **10 de 80**, tres adjuntos y ninguna suma.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
Un cliente de red privada ve todo lo que sale y entra de tu teléfono. No le entregues ese mapa a un archivo que no puedes comprobar: elige el camino primero —VPN, malla, túnel, DNS, cortafuegos— y después elige el programa que firma.

#VPN #WireGuard #SingBox #Hiddify #RedPrivada #GitHub #LaBandita #Verificacion #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
