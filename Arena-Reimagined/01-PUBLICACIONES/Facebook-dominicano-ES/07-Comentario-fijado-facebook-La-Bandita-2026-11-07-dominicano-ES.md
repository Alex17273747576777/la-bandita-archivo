━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 07 — La pantalla grande y la casa que no hace ruido*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 07 de Facebook
• Fecha en vivo: sábado 7 de noviembre de 2026
• Medido con: 17 programas de pantalla grande y casa inteligente · API pública de GitHub
• Hora declarada de la medición: 11:15 de la mañana en Santo Domingo

Lo que dicen los números medidos:
• **17** repositorios medidos: **4 publican al menos una huella** (23,5 %).
• **16** archivos adjuntos en total: **6 con huella** (37,5 %).
• Los cinco gigantes —`esphome/esphome`, `home-assistant/core`, `jellyfin/jellyfin`, `xbmc/xbmc` y `yuliskov/SmartTube`— suman más de 220.000 estrellas y **no publican ni una suma**.
• Los cuatro que sí firman son pequeños y nuevos: `Gingerbreadfork/lounge` (20 días), `jolabs40/TVSlim` (55 días), `meta-tabchen/MoonCast` (31 días) y `mkatadev/GoogleTVAirPlay` (36 días).
• **Siete de los diecisiete** no declaran una licencia que se pueda nombrar.
• `xbmc/xbmc` pesa más de un gigabyte y medio y no publica huella.

**Seis órdenes para comprobarlo tú mismo:**
1. Abre la página de entregas del repositorio y busca archivos `.sha256`, `.sha512`, `.asc`, `.sig` o `sums`.
2. En Termux: `pkg install coreutils && sha256sum *.apk` —o el archivo que hayas bajado—.
3. Compara con lo que publicó el autor: `sha256sum -c archivo.sha256`.
4. Mira la firma del paquete: `apksigner verify --print-certs archivo.apk` y compara la línea SHA-256 con la de la versión anterior.
5. Si no hay suma, pídela en las incidencias del repositorio. La plantilla está al final de la pieza.
6. Si hay atestación: `gh attestation verify archivo.apk --repo dueno/nombre`.

Qué hace cada cosa y para qué te sirve:
Esto se instala en el aparato que está encendido todo el día y que menos revisas: el televisor, el servidor de casa, el reproductor del cuarto. Compruébalo antes de actualizar, no después de que algo raro salga en pantalla.

#AndroidTV #Kodi #Jellyfin #HomeAssistant #SmartTube #GitHub #LaBandita #Verificacion #SoftwareLibre

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
