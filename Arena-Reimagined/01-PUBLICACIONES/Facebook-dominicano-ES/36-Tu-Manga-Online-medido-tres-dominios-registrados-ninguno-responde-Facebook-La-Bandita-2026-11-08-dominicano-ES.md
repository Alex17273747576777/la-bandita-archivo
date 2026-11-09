*Tu Manga Online, medido: tres dominios registrados, ninguno que responde, y ocho direcciones que sí contestan*

*La Bandita · domingo 8 de noviembre de 2026, 08:52 de la mañana en Santo Domingo (12:52 UTC) · edición dominicano-español · pieza 36 de Facebook*

⏱️ *Lectura total: 10 minutos · ocho dominios sondeados hoy desde esta máquina con RDAP, DNS y cabecera HTTPS · **tres registrados, cero resolviendo** · la pieza que antes decía «clientHold» se corrige con lo medido · cero enlaces a espejos · cero paquetes alojados*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · un cierre se puede medir, solo hay que saber dónde
├── ⚡ En una página · la tabla de los ocho dominios
├── 🔎 Cómo se mide un dominio muerto, en tres capas
├── 🧾 Lo que el registro dice y lo que el sitio hacía
├── 🩹 La corrección · lo que esta pieza afirmaba y no era cierto
├── 🧩 Lo que sí se puede medir de este tema
├── 🛠️ Cuatro órdenes para sondear un dominio por tu cuenta
├── 🚪 Lo que esta pieza no tiene · 📅 la semana de prueba
├── ❓ Las preguntas del grupo · 🌅 cierre
└── 🗒️ Notas al pie
```

───────────────────

*🧱 La semilla · un cierre se puede medir, solo hay que saber dónde*

Esta es la última de las cuarenta piezas que quedaba declarada «sin medición propia». La excusa que escribí ayer era: «el cierre de un sitio no se mide con una API de repositorios». Era verdad a medias. **El cierre de un sitio no se mide con la API de GitHub, pero sí se mide**, y con tres herramientas que no piden cuenta ni llave: el registro del dominio, el DNS y una petición de cabecera.

Así que hoy se mide. **Ocho direcciones sondeadas a las 08:52 de la mañana** desde esta máquina, y una respuesta que ordena toda la pieza: de los tres dominios del caso, **los tres siguen registrados y ninguno resuelve**. El registro dice que existen; el DNS dice que no están en ninguna parte.

Y hay una segunda cosa que esta pieza tiene que hacer, más incómoda: **corregirse**. La versión anterior afirmaba que `zonatmo.com` había pasado a estado `clientHold` el 18 de marzo de 2026. Hoy el registro dice otra cosa, y lo medido va primero.

───────────────────

*⚡ En una página · la tabla de los ocho dominios*

Medido a las 12:52 UTC del 8 de noviembre de 2026. «Registrado» es lo que dice el registro del `.com` (RDAP de Verisign); «resuelve» es si el nombre se convierte en una dirección IP; «responde» es el código que devuelve una petición HTTPS.

| Dominio | Registrado | Resuelve | Responde | Lectura |
|---|---|---|---|---|
| `zonatmo.com` | **sí** · alta 13-sep-2024 · vence 13-sep-2027 | **no** | nada | Registrado y apagado |
| `tumangaonline.com` | **sí** · alta 29-may-2014 · vence 29-may-2027 | **no** | nada | El dominio histórico, apagado |
| `lectormanga.com` | **sí** · alta 22-nov-2017 · vence 22-nov-2027 | **no** | nada | Registrado y apagado |
| `tmo.tumangaonline.com` | — | **no** | nada | El subdominio tampoco existe |
| `inmanga.com` | — | sí | **200** | Vivo y respondiendo |
| `mangadex.org` | — | sí | **405** | Vivo y respondiendo |
| `mangaplus.shueisha.co.jp` | — | sí | **200** | Vivo y respondiendo |
| `visormanga.com` | — | sí | **200** | Vivo y respondiendo |

**Tres registrados y apagados; cuatro vivos y respondiendo; uno que no existe ni como subdominio.** Esa es toda la medición de esta pieza, y no hay manera de adornarla.

───────────────────

*🔎 Cómo se mide un dominio muerto, en tres capas*

Un dominio no «se cae» de una vez. Se apaga por capas, y cada capa deja una prueba distinta. Estas son las tres, en orden, y lo que significa cada resultado:

**Capa 1 · el registro (RDAP).** Es el libro donde consta quién es el dueño de un nombre y hasta cuándo. Se consulta sin llave en el RDAP del registro del `.com`. Si el dominio aparece **registrado** con fecha de vencimiento futura, el nombre sigue en manos de alguien: nadie lo ha soltado. Si aparece **`clientHold`**, el registrador lo ha puesto en pausa a petición de alguien —normalmente por una orden—. Y si no aparece, está libre.

**Capa 2 · la resolución (DNS).** Es la guía telefónica: convierte el nombre en una dirección. Si no devuelve nada, el nombre no lleva a ninguna parte, aunque esté pagado hasta 2027.

**Capa 3 · la respuesta (HTTPS).** Es lo que ve el navegador. Un `200` significa que hay algo detrás; un `405` que hay un servidor que no acepta ese método pero existe; un `000` que no hubo conversación.

Las tres capas juntas son la diferencia entre «dicen que lo cerraron» y «está cerrado». La primera es una noticia; las otras dos son una medición.

───────────────────

*🧾 Lo que el registro dice y lo que el sitio hacía*

Los tres dominios del caso siguen pagados y con fecha de vencimiento en 2027. Ninguno resuelve. Esa combinación —**registro activo, resolución muerta**— es exactamente lo que se ve cuando alguien apaga un servicio **sin soltar el nombre**.

Y ahí hay un detalle que conviene entender: soltar el nombre sería peor para quien lo tiene. Un dominio `.com` que vence y no se renueva queda libre, y el primero que lo compre puede poner ahí lo que quiera con el mismo nombre. Mantenerlo registrado y apagado es la manera de que **nadie más lo use**.

Para el lector, la consecuencia práctica es la que importa: **cuando veas esos nombres en un grupo, no son los originales**. Los originales están apagados a propósito y el nombre sigue en manos de quien lo tenía. Cualquier dirección con ese nombre que aparezca funcionando es otra cosa: un clon, un aparcamiento de dominios o una estafa, y de las tres, la tercera es la que cobra.

Los otros cuatro dominios de la tabla están vivos y responden hoy. Eso no dice nada sobre su legalidad, su catálogo ni su seguridad: dice que hay un servidor detrás. Es lo único que se puede afirmar sin auditar el sitio, y esta pieza no lo audita.

───────────────────

*🩹 La corrección · lo que esta pieza afirmaba y no era cierto*

La versión anterior de esta pieza, publicada el 7 de noviembre, decía:

> «El 18 de marzo de 2026, el dominio principal `zonatmo.com` dejó de estar disponible, mostrando inicialmente un mensaje de "mantenimiento". Días después, el dominio pasó a estado `clientHold`…»

Lo medido hoy, **8 de noviembre de 2026**, dice:

* `zonatmo.com` **está registrado**, con alta el **13 de septiembre de 2024**, vencimiento el **13 de septiembre de 2027** y última modificación del registro el **17 de agosto de 2026**.
* Su estado en el RDAP es **`client transfer prohibited`**, que es el candado normal contra transferencias, **no `clientHold`**.
* **No resuelve**: no hay dirección IP para ese nombre.

Es decir: **el dominio no está en pausa; está apagado y pagado**. La fecha del 18 de marzo y el resto del relato de la operación no los puedo verificar con lo que tengo —no cito prensa en esta pieza y no he consultado comunicados para ella—, así que esta versión no los repite. Lo que sí hace es dejar la parte que se puede medir, con su fecha y su fuente.

Esta casa tiene una regla para esto: **lo publicado no se reescribe, se corrige hacia adelante y la corrección se anota**. Aquí está anotada.

───────────────────

*🧩 Lo que sí se puede medir de este tema*

Ya que el cierre no se puede verificar en su relato, hay tres cosas de este tema que sí se miden, y las tres están en esta serie:

**Los lectores siguen vivos.** La pieza 32 midió nueve lectores el mismo día: **seis de los nueve empujaron código en los últimos siete días**, dos llevan más de medio año quietos y uno —el padre de la familia— devuelve **404**. La medición vive en `docs/MEDICION-32-2026-11-08.json`.

**Los archivos no se firman.** Esos nueve lectores publicaron **4.182 archivos y ninguno con suma de comprobación**. Cuando un sitio cambia de dirección, el lector sigue siendo el mismo; lo que no puedes comprobar es lo que ejecuta.

**La biblioteca sí se puede salvar.** Es la única cosa de este tema que depende enteramente de ti: exportar, comprobar que el archivo se reimporta y guardarlo fuera del teléfono. Está en la pieza 34, con los pasos y con lo que se puede comprobar de cada uno.

Con esas tres, un lector puede atravesar la desaparición de un sitio sin perder nada que importe. Lo demás —los nombres, los clones, los mensajes de «mantenimiento»— cambia cada semana y no se puede firmar.

───────────────────

*🛠️ Cuatro órdenes para sondear un dominio por tu cuenta*

**1 · ¿Está registrado y hasta cuándo?**
```
curl -s -H 'Accept: application/rdap+json' https://rdap.verisign.com/com/v1/domain/ejemplo.com \
 | grep -E '"eventAction"|"eventDate"|"status"'
```
Devuelve el alta, el vencimiento y el estado. `client transfer prohibited` es normal; `clientHold` es una pausa; `pendingDelete` es que se está cayendo.

**2 · ¿Resuelve?**
```
getent hosts ejemplo.com || nslookup ejemplo.com
```
Si no devuelve nada, el nombre no lleva a ninguna parte.

**3 · ¿Responde?**
```
curl -sSI --max-time 10 https://ejemplo.com | head -1
```
`200`, `301`, `403` o `405` significan que hay un servidor. `000` o un error de conexión significa que no.

**4 · ¿Y si es un subdominio?**
Repite el paso 2 con el nombre completo. Aquí, `tmo.tumangaonline.com` tampoco resuelve: el subdominio no existe sin el dominio.

Ninguna de las cuatro necesita cuenta, ni root, ni instalar nada que no venga con el sistema.

───────────────────

*🚪 Lo que esta pieza no tiene*

No tiene el relato del cierre. No he consultado comunicados policiales, judiciales ni de prensa para esta pieza, así que no afirmo fechas de detenciones, números de visitas ni nombres de operaciones. Lo que la versión anterior decía de eso se queda fuera hasta que se pueda verificar con una fuente que yo haya abierto.

No tiene lista de dominios alternativos ni de espejos, por la misma razón que la pieza 32: caducan, no se miden y trasladan el riesgo a quien los lee.

No audita los cuatro sitios que responden. Que un dominio conteste no dice nada de su contenido, su legalidad o su seguridad: dice que hay un servidor. Y no hay aquí ninguna captura de pantalla ni prueba de uso: lo que hay son ocho nombres, tres capas y una hora.

───────────────────

*📅 La semana de prueba*

**Día 1.** Coge un dominio que uses y consulta su registro con la orden 1. Mira el estado y el vencimiento. Es lo más parecido a ver la escritura de una casa.
**Día 2.** Comprueba si resuelve y si responde. Anota los dos resultados.
**Día 3.** Repite con un dominio que hayas visto recomendado en un grupo. Muchas veces no resuelve, y entonces ya sabes que la recomendación era vieja.
**Día 4.** Exporta la biblioteca de tu lector de manga, aunque no vayas a cambiar nada. Es el único seguro de este tema.
**Día 5.** Comprueba la firma del paquete de tu lector y apunta el SHA-256 en una nota. Con eso, el día que aparezca otro dominio, tu decisión no dependerá del nombre.

───────────────────

*❓ Las preguntas del grupo*

**¿Entonces Tu Manga Online está cerrado?** Lo que puedo afirmar es lo que medí: sus tres dominios siguen registrados con vencimiento en 2027 y **ninguno resuelve**. El nombre existe; el sitio, no.

**¿Y los clones que circulan?** Que un nombre parecido responda no lo convierte en el original: el original está apagado a propósito y su nombre sigue registrado. Cualquier otro uso de ese nombre no es la misma casa.

**¿Por qué antes decía `clientHold` y ahora no?** Porque el registro dice `client transfer prohibited`, que es otra cosa. La versión anterior lo afirmaba sin haberlo consultado; esta lo consulta y lo corrige, y la corrección queda anotada.

**¿La fecha del 18 de marzo es falsa?** No digo eso. Digo que no la he podido verificar para esta pieza y que por eso no la repito. Una casa que firma con fecha no puede arrastrar datos que no ha abierto.

**¿Esto estaba en la pieza vieja?** No. La vieja contaba el cierre con fuentes que no citaba y no medía ni un dominio. Esta mide ocho, a una hora concreta, y deja fuera todo lo que no puede comprobar.

───────────────────

*🌅 Cierre*

Cuarenta piezas después, esta es la última que estaba sin medir, y el método resultó ser el mismo de siempre: buscar la capa donde el dato se pueda comprobar y medirlo ahí. Para un repositorio es la API de GitHub; para un dominio es el registro, el DNS y una cabecera. Ninguna de las dos cosas pide permiso a nadie.

Lo que queda es un dato pequeño y limpio: **tres nombres registrados, ninguno en pie**. Y una lección para quien lea esto dentro de seis meses: no preguntes si el sitio cerró, pregunta cuándo vence su dominio y si resuelve. Eso lo puedes ver tú, hoy, sin creerme.

*La Bandita informa a partir de fuentes fechadas. · domingo 8 de noviembre de 2026 · pieza 36 de Facebook · los ocho dominios se sondearon a las 12:52 UTC del 8 de noviembre de 2026 (RDAP de Verisign, DNS y cabecera HTTPS) y la medición vive en `docs/MEDICION-36-dominios-2026-11-08.json`; los lectores citados salen de `docs/MEDICION-32-2026-11-08.json`. Ningún paquete se aloja aquí; solo enlaces a repositorios de código abierto.*
