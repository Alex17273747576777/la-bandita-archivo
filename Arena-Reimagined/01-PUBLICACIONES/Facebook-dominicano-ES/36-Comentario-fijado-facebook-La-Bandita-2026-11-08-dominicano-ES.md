━━━━━━━━━━━━━

📎 *Comentario fijado · Pieza 36 — Tu Manga Online, medido: tres dominios registrados, ninguno responde*

Enlaces rápidos:
• Cuerpo de la publicación: pieza 36 de Facebook
• Fecha en vivo: domingo 8 de noviembre de 2026
• Medido con: RDAP de Verisign (.com), resolución DNS y cabecera HTTPS · API pública de GitHub para los lectores
• Medición guardada en: `docs/MEDICION-36-dominios-2026-11-08.json`

Lo que dicen los ocho dominios sondeados a las 12:52 UTC:
• `zonatmo.com` — **registrado** (alta 13-sep-2024, vence 13-sep-2027, estado `client transfer prohibited`), **no resuelve**.
• `tumangaonline.com` — **registrado** (alta 29-may-2014, vence 29-may-2027), **no resuelve**.
• `lectormanga.com` — **registrado** (alta 22-nov-2017, vence 22-nov-2027), **no resuelve**.
• `tmo.tumangaonline.com` — **no existe**: el subdominio tampoco resuelve.
• Responden hoy: `inmanga.com` (200), `mangadex.org` (405), `mangaplus.shueisha.co.jp` (200) y `visormanga.com` (200).

La corrección de esta pieza:
• La versión del 7 de noviembre afirmaba que `zonatmo.com` pasó a estado `clientHold` el 18 de marzo de 2026. El registro dice **`client transfer prohibited`**, que es otra cosa, y el dominio está **apagado y pagado hasta 2027**, no en pausa. Lo corregido queda anotado en el cuerpo.

De los lectores, medido el mismo día (pieza 32):
• **9 lectores vivos**, **4.182 archivos publicados** y **ninguno con suma de comprobación**; **6 de 9** empujaron código en la última semana y `tachiyomiorg/tachiyomi` **devuelve 404**.

**Cuatro órdenes para comprobarlo tú mismo:**
1. El registro: `curl -s -H 'Accept: application/rdap+json' https://rdap.verisign.com/com/v1/domain/zonatmo.com | grep -E '"eventAction"|"status"'`
2. La resolución: `getent hosts zonatmo.com || nslookup zonatmo.com` (no devuelve nada).
3. La respuesta: `curl -sSI --max-time 10 https://zonatmo.com | head -1` (no hay conversación).
4. La que de verdad depende de ti: exporta la biblioteca de tu lector y comprueba que se reimporta. Está en la pieza 34.

Qué significa para ti:
Un dominio registrado y sin resolver es **un nombre que sigue en manos de su dueño y no lleva a ninguna parte**: nadie más puede usarlo. Cualquier dirección con ese nombre que aparezca funcionando no es la casa original. Y lo único que puedes salvar de este tema sin depender de nadie es tu biblioteca exportada.

*La Bandita informa a partir de fuentes fechadas. · domingo 8 de noviembre de 2026 · comentario fijado de la publicación. Ningún paquete se aloja aquí; solo enlaces a repositorios de código abierto.*
