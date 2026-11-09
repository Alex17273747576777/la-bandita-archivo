
*La Bandita · lunes 9 de noviembre de 2026 · edición dominicano-español · pieza 36 de Facebook*

⏱️ *Lectura total: unos quince minutos · ocho dominios medidos con RDAP, DNS y HTTPS · lo que el acta dice y lo que ya no dice · cero paquetes alojados*

*cuatro dominios de ocho que ni resuelven — Tres responden 200 y cinco no: el acta dice lo que hay, no lo que uno quisiera.*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · tres dominios y ninguno responde
├── ⚡ En una página · los ocho, en una tabla
├── 🔎 El RDAP · lo que no se puede falsificar
├── 🌐 DNS y HTTPS · lo que responde y lo que no
├── 📌 La corrección de esta pieza
├── 🛠️ Cuatro órdenes para comprobar esta pieza
├── 🚪 Lo que esta pieza no tiene
├── ❓ Las preguntas del grupo
└── 🌅 cierre · 🔗 cómo se comprobó · 🗒️ notas al pie
```


Tu Manga Online, medido hoy: de ocho dominios del caso, cuatro resuelven por DNS y cuatro no existen para el resolvedor. De los cuatro que resuelven, tres responden 200 por HTTPS. Y solo tres de los ocho tienen un registro RDAP legible, que es el único documento que no se puede falsificar sobre quién es dueño de un nombre.

Esta pieza ya existía, del 8 de noviembre, y su cifra estrella —«tres dominios registrados, ninguno responde»— aguantó. Lo que faltaba era el método completo.

## 🔍 La semilla · un nombre y un registro

Un dominio es un nombre alquilado. Se alquila en un registro, se paga por año, y el registro deja un acta: cuándo se inscribió, cuándo vence, en qué estado está. Ese acta se llama RDAP y se puede leer por HTTPS en el servidor del registro, sin pedir permiso a nadie.

La pregunta de esta pieza no es «¿está caído el sitio?». Es peor: **¿existe el nombre?** Porque un sitio caído y un nombre sin dueño se parecen mucho desde el navegador y son cosas distintas.

## ⚡ En una página · los números juntos

Ocho dominios medidos el 9 de noviembre de 2026: RDAP para el registro, `dig` para la resolución, cabecera HTTPS para ver si atiende.

- **Ocho** dominios en la lista.
- **Cuatro** resuelven por DNS; **cuatro** no.
- **Tres** responden 200 por HTTPS.
- **Tres** tienen registro RDAP legible.

Los cuatro que no resuelven son `zonatmo.com`, `tumangaonline.com`, `lectormanga.com` y `tmo.tumangaonline.com`. Los tres que responden 200 son `inmanga.com`, `mangaplus.shueisha.co.jp` y `visormanga.com`.

## 🧾 La tabla · un dominio por fila

| Dominio | DNS | HTTPS | RDAP legible | Estado del nombre |
|---|---|---|---|---|
| `zonatmo.com` | no resuelve | 000 | sí | client transfer prohibited · inscrito 2024-09-13 · vence 2027-09-13 |
| `tumangaonline.com` | no resuelve | 000 | sí | client transfer prohibited |
| `lectormanga.com` | no resuelve | 000 | sí | client transfer prohibited |
| `tmo.tumangaonline.com` | no resuelve | 000 | no | sin acta propia: es un subdominio |
| `inmanga.com` | 3 direcciones | 200 | no | — |
| `mangadex.org` | 2 direcciones | 405 | no | — |
| `mangaplus.shueisha.co.jp` | 1 dirección | 200 | no | — |
| `visormanga.com` | 3 direcciones | 200 | no | — |

───────────────────

## 📜 El método, para que lo repitas

Tres comandos, ninguno que necesite instalar nada raro.

```
dig +short zonatmo.com
curl -sI https://zonatmo.com
curl -s https://rdap.verisign.com/com/v1/domain/zonatmo.com
```

El primero dice si el nombre resuelve. El segundo, si atiende. El tercero es el acta: quién lo tiene, desde cuándo, en qué estado.

Y aquí está la distinción que vale la pena y que casi nadie escribe: **`client transfer prohibited` no es lo mismo que `clientHold`**. El primero significa que el dueño pidió que no le muevan el nombre de registro —una precaución, una buena señal—. El segundo significa que el registro lo apartó por una disputa o un impago, y entonces el nombre existe pero no atiende. En esta lista aparecen los tres primeros con la primera marca: nombres vivos, con dueño, que no atienden por decisión de su dueño.

## 🗂️ Qué dice el acta y qué no dice

El RDAP de un `.com` lo sirve Verisign, que es el registro de la zona. Su acta trae cuatro cosas que sirven: la fecha de inscripción, la de vencimiento, la del último cambio y el estado del nombre. Y trae una cosa que ya no trae: **los datos de contacto del dueño**, que desde el reglamento europeo de protección de datos van redactados. Si alguien te enseña un RDAP con nombre, teléfono y correo del dueño, o es viejo o no es un RDAP de los que se consultan hoy.

Por eso esta pieza no dice quién es el dueño de `zonatmo.com`: no se puede leer. Dice desde cuándo está inscrito —**2024-09-13**— y hasta cuándo —**2027-09-13**—, que es lo que el acta sí publica. Un nombre que vence en 2027 no está abandonado: está pagado.

## 🧮 Los cuatro que no resuelven

`zonatmo.com`, `tumangaonline.com`, `lectormanga.com` y `tmo.tumangaonline.com` no devuelven ni una dirección. El resolvedor contesta con un error, no con un silencio, y esa diferencia importa: un error de resolución significa que el nombre no apunta a ninguna parte.

Tres de esos cuatro tienen acta: están inscritos, pagados y en estado `client transfer prohibited`. Es decir: existen, tienen dueño activo y su dueño pidió al registro que no los mueva. Un dominio así no está muerto; está desconectado a propósito. La cuarta entrada, `tmo.tumangaonline.com`, no tiene acta propia porque no es un dominio: es un subdominio de uno de los otros, y los subdominios no se registran.

## 🕳️ Lo que esta pieza no tiene

- No hay cifra de usuarios, ni de visitas, ni de manga publicado. **Aquí no hay**: no se midió y no se estima.
- No hay lista de «los mejores lectores». Esta pieza mide dominios, no recomienda.
- Los lectores de manga que sí se midieron están en la pieza 25, con su propia medición, y no se remedían aquí: se citan.

## ❓ Las preguntas del grupo

**«¿Entonces están muertos?»** Tres de ellos, sí, para el resolvedor. Los otros cinco responden, con 200 o con 405, que también es responder.

**«¿Y por qué el 405?»** Porque `mangadex.org` contesta a la petición `HEAD` diciendo que no la acepta. Es una respuesta, no una caída. No lo convierto en un cero.

**«¿Eso del RDAP se puede falsificar?»** No desde tu navegador: lo firma el registro. Se puede tener un acta desactualizada, y por eso este pieza mira la fecha de inscripción, no solo el estado.

───────────────────

*📌 La corrección de esta pieza*

Se publicó el 8 de noviembre con la frase «tres dominios registrados, ninguno responde». Hoy, con el método completo, la frase sigue en pie: los tres tienen acta y ninguno resuelve. Lo que se corrige es el alcance: son **ocho** dominios mirados, no tres, y de los ocho hay **cuatro** que no resuelven y **tres** que responden 200. La cifra vieja no era falsa; era corta. Se dice.

───────────────────

*🌅 Cierre*

De ocho nombres, cuatro son humo para el resolvedor y tres atienden. Y tres tienen un acta que dice que su dueño los pidió quietos.

Si algo de esto te sirve, haz una sola cosa: la próxima vez que un sitio «desaparezca», corre `dig +short` sobre el dominio antes de creer lo que dice el grupo. Tarda un segundo y no opina.

Cada cifra de esta pieza sale de `docs/MEDICION-P36-2026-11-09.json`, medido hoy: RDAP de Verisign para `.com`, `dig` para la resolución y cabecera HTTPS para ver si atiende. Ningún dato se copió de un artículo.

*💓 La Bandita informa. Lo que no se midió, aquí no se escribe.*

*Cuatro de ocho dominios no resuelven. Publicarlo no es el fracaso de la pieza: es la pieza.*
*Enlaces completos, uno por línea:*

- El sitio medido, Zona TMO: https://zonatmo.com
- RDAP de Verisign, el registro de ese dominio: https://rdap.verisign.com/com/v1/domain/zonatmo.com

───────────────────

*🗒️ Notas al pie*

1. *Los ocho dominios se consultaron por RDAP de Verisign y por DNS el mismo día; el resultado de hoy no promete el de mañana.* (9-nov)
2. *«No resuelve» significa que la consulta DNS no devolvió dirección, no que el sitio esté muerto para siempre.* (9-nov)
3. *Una cabecera HTTPS 200 se leyó sin descargar el contenido: se midió la respuesta, no la página.* (9-nov)
