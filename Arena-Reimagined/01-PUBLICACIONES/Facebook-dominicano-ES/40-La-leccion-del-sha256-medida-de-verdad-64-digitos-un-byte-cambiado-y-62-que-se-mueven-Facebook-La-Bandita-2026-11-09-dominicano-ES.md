
*La Bandita · lunes 9 de noviembre de 2026 · edición dominicano-español · pieza 40 de Facebook*

⏱️ *Lectura total: unos quince minutos · el sha256 medido con hashlib sobre un archivo real · seis órdenes sin root · cero paquetes alojados*

Para esta pieza no cito a nadie: medí el hash yo mismo, aquí, con `hashlib`. Tomé un archivo de **3.461 bytes**, calculé su sha256 y me dio una huella de **64** dígitos hexadecimales. Después cambié **un solo byte** en el medio y volví a calcularlo: cambiaron **62 de los 64 dígitos**. Esa es toda la lección de esta pieza, y por eso vale la pena.

## 🔐 La semilla · comprobar sin confiar

Cuando bajas un programa, tu teléfono no te dice si es el que su autor publicó. Te dice que se bajó. Son dos cosas muy distintas y la diferencia es la puerta por la que entra todo lo demás.

Una suma de comprobación —un hash— es la única respuesta práctica: un número que se calcula sobre el archivo completo y que cambia por completo si el archivo cambia en algo. No necesitas root, no necesitas confiar en nadie: solo multiplicar y comparar.

## ⚡ En una página · los números juntos

Medido hoy sobre un archivo real de este mismo archivo:

- **3.461 bytes** pesa el archivo medido.
- **64** dígitos hexadecimales tiene el sha256.
- **40** tiene el sha1.
- **32** tiene el md5.
- **62 de 64** dígitos cambiaron al alterar **un solo byte**.
- **256 bits** son las posibilidades distintas del sha256.

## 🧮 Por qué 64 dígitos son tantos

Cada dígito hexadecimal vale 16 posibilidades. 64 dígitos son 16 elevado a 64, que es lo mismo que 2 elevado a 256. Escribirlo así, con el exponente, es lo único honesto: el número completo tiene 78 cifras decimales y nadie las lee.

Lo que importa no es el tamaño: es que **un byte cambiado mueva 62 de los 64 dígitos**. No hay manera de tocar un archivo y que la huella se parezca. No es que sea difícil: es que no pasa.

## 🧾 La tabla · la misma huella, dos veces

| | Archivo original | El mismo con un byte cambiado |
|---|---|---|
| Bytes | 3.461 | 3.461 |
| Bytes alterados a mano | 0 | 1 |
| sha256 | `efb29f2a85601554b45f1e75f403897f345938384636cab474…` | `05ddbdbee8d459a5c5900f9977f184e6cc1a15a52e8ed33500…` |
| Dígitos distintos | — | 62 de 64 |

Las dos huellas están cortadas en la tabla por el ancho de la pantalla; las completas están en `docs/MEDICION-P40-2026-11-09.json`, que cualquiera puede abrir y contar.

───────────────────

## 🛠️ Seis órdenes para comprobar un archivo, sin root

1. `sha256sum archivo.apk` —o el archivo que sea—. Te da 64 dígitos.
2. Busca en la página de entregas del proyecto un archivo que termine en `.sha256`, `.sha512`, `.asc`, `sums` o `checksums.txt`.
3. Si hay un archivo de sumas: `sha256sum -c archivo.sha256` y te dice OK o FAILED. Nada de comparar a ojo.
4. Si la suma está escrita en el texto de la entrega: compara los 64 dígitos completos. Sesenta y tres iguales y uno distinto es un NO.
5. Si el proyecto publica `.asc` o `.sig`, es mejor: eso firma la suma, no solo la calcula. `gpg --verify archivo.asc archivo`.
6. Si no publica nada de eso, ya tienes la respuesta, y es la misma de casi todas las piezas de esta serie: el proyecto no te da con qué comprobar.

───────────────────

*🚪 Lo que esta pieza no tiene*

- **No hay lista de programas.** Esta pieza enseña el método; los programas medidos están en las otras 39.
- **No hay consejo de seguridad.** Un hash te dice que el archivo es el que su autor publicó. **No te dice que el programa sea bueno.** Eso va en la nota al pie y no es un detalle.
- No se afirma nada sobre ningún teléfono concreto: aquí no se verificó en dispositivo.

───────────────────

*❓ Las preguntas del grupo*

**«¿Y si el autor publica un hash falso?»** Entonces el hash no sirve para nada, y por eso las piezas de esta serie cuentan cuántos publican **firma** y no solo suma. Una firma dice quién lo publicó; una suma solo dice que el archivo no cambió.

**«¿md5 ya no sirve?»** Para comprobar una descarga rota, sirve. Para seguridad, no: se pueden fabricar dos archivos distintos con el mismo md5. Por eso esta pieza usa sha256 y lo mide.

**«¿Cuánto tarda?»** En un teléfono, un archivo de 3.461 bytes es instantáneo. Un APK de 488 MB tarda unos segundos. Es lo más barato que puedes hacer por tu seguridad.

───────────────────

*📌 La corrección de esta pieza*

Se publicó el 8 de noviembre explicando la lección sin haberla medido: decía que un byte cambiado cambia la huella, y era cierto, pero era una afirmación de memoria. Hoy se midió de verdad con `hashlib` sobre un archivo real, se cambiaron **un byte** y se contó cuántos dígitos se movieron: **62 de 64**. La pieza ahora tiene el número en vez de la promesa.

───────────────────

*🧩 Las tres cosas que un hash no te dice*

1. **No te dice si el programa es bueno.** Un archivo puede coincidir con lo que publicó su autor y llevar dentro cualquier cosa. La suma comprueba la integridad del archivo, no las intenciones de quien lo hizo.
2. **No te dice quién lo publicó.** Para eso hace falta una firma, que es otra cosa: una llave privada que solo el autor tiene. Por eso las piezas de esta serie cuentan cuántos publican **firma** y no solo suma, y por eso casi todas dan cero.
3. **No te protege del sitio.** Si el que te entrega el archivo es el mismo que te entrega la suma, un atacante que controle ese sitio cambia las dos. La suma sirve cuando la comparas contra una fuente distinta, o cuando está firmada.

*⚖️ Los tres tamaños, en una línea cada uno*

- **md5**: **32** dígitos. Sirve para saber si una descarga se cortó. No sirve para seguridad: dos archivos distintos pueden compartirlo.
- **sha1**: **40** dígitos. Mejor, y aun así retirado para firmas. Git lo usa para nombrar objetos y eso no es seguridad de descarga.
- **sha256**: **64** dígitos. El que esta pieza mide y el que recomienda. Los tres se calcularon sobre el mismo archivo, aquí, hoy.

*🌅 Cierre*

64 dígitos, 3.461 bytes, un byte cambiado y 62 dígitos distintos. Eso es todo lo que necesitas saber sobre confiar en un archivo que bajaste.

Si algo de esto te sirve, haz una sola cosa: la próxima descarga, antes de abrirla, corre `sha256sum`. Tarda menos que leer este párrafo.

*💓 La Bandita informa. Lo que no se midió, aquí no se escribe.*
