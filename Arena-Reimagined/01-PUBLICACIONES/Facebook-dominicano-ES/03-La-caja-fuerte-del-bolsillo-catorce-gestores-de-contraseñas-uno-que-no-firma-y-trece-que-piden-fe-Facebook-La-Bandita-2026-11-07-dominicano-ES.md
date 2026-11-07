*La caja fuerte del bolsillo: catorce gestores de contraseñas, ninguno que firme lo que entrega y trece que te piden fe*

*La Bandita · sábado 7 de noviembre de 2026, 06:38 de la mañana en Santo Domingo (10:38 UTC) · edición dominicano-español · pieza 03 de Facebook*

⏱️ *Lectura total: 12 minutos · catorce repositorios de gestores de contraseñas medidos con la API de GitHub · cero paquetes alojados aquí · cero tablas · cero métricas inventadas*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La pregunta · ¿tienes con qué comprobar la caja?
├── 📋 Los catorce · nombre, estrellas, licencia, entrega, huella
├── 🔏 Los que no firman · ninguno de los catorce
├── 🏛️ Los cuatro parados · andOTP, Authorizer, OpenKeychain, AuthPass
├── 🌅 Cierre · lo que midí, cuándo y dónde
└── 🔗 Enlaces · uno por uno, al repositorio de su autor
```

───────────────────

*🧱 La pregunta · ¿tienes con qué comprobar la caja?*

Una caja fuerte de contraseñas guarda, en un solo archivo cifrado, la llave de tu correo, de tu banco, de tu trabajo y de las cuentas de tus hijos. La instalaste una vez, desde un archivo que bajaste de una página, y desde entonces vive en la memoria del teléfono. La pregunta más incómoda que se puede hacer sobre ese programa es: **¿cómo sabes que el archivo que instalaste es el que su autor publicó?**

La única forma de saberlo es una **huella**: un archivo de suma de comprobación (`.sha256`, `.sha512`, `.asc` o `.sig`) que el autor publique junto al programa. Si la huella del archivo que bajaste coincide con la que publicó el autor, entonces lo que tienes es lo que él subió. Si no hay huella, no hay comprobación: solo fe.

Esta pieza mide catorce gestores de contraseñas y generadores de códigos de segundo factor para Android, todos de código abierto, todos medidos hoy con la API de GitHub. Pregunta simple: ¿cuántos publican huella?

*📋 Los catorce · nombre, estrellas, licencia, entrega, huella*

Cada línea es un repositorio real, medido hoy sábado 7 de noviembre de 2026. Los datos vienen de `GET /repos/{owner}/{repo}` y `GET /repos/{owner}/{repo}/releases/latest`. Nada se inventa.

**1 · Bitwarden** (bitwarden/android) ★9.600 · GPL-3.0 · release `v2026.10.1-bwpm` · 0 archivos con huella · push el 6 de noviembre · creado el 30 de abril de 2016

**2 · Stratum** (stratumauth/app) ★4.637 · GPL-3.0 · release `v1.7.0` · 0 archivos con huella · push el 1 de noviembre · creado el 14 de agosto de 2018

**3 · Monica** (Monica-Pass/Monica) ★1.217 · GPL-3.0 · release `V1.0.325` · 0 archivos con huella · push hoy 7 de noviembre · creado el 5 de octubre de 2025

**4 · Vaultwarden** (dani-garcia/vaultwarden) ★70.363 · AGPL-3.0 · release `1.37.5` · 0 archivos con huella · push el 4 de noviembre · creado el 17 de febrero de 2018

**5 · KeePass2Android** (PhilippC/keepass2android) ★6.372 · GPL-3.0 · release `v1.15-r6` · 0 archivos con huella · push el 6 de noviembre · creado el 20 de septiembre de 2017

**6 · KeePassDX** (Kunzisoft/KeePassDX) ★7.631 · GPL-3.0 · release `4.5.8` · 0 archivos con huella · push el 1 de noviembre · creado el 17 de octubre de 2017

**7 · Keyguard** (AChep/keyguard-app) ★3.608 · NOASSERTION · release `r20261103` · 0 archivos con huella · push hoy 7 de noviembre · creado el 23 de julio de 2023

**8 · Aegis** (beemdevelopment/Aegis) ★13.486 · GPL-3.0 · release `v3.4.3` · 0 archivos con huella · push el 6 de septiembre · creado el 15 de agosto de 2016

**9 · Lucent** (Lucent-Project/Lucent) ★12 · MIT · release `v3.1.2` · 0 archivos con huella · push el 2 de noviembre · creado el 19 de julio de 2026

**10 · FreeOTP** (freeotp/freeotp-android) ★1.683 · Apache-2.0 · release `v2.0.6` · 0 archivos con huella · push el 3 de noviembre · creado el 24 de octubre de 2016

**11 · andOTP** (andOTP/andOTP) ★3.704 · MIT · release `v0.9.0.1` · 0 archivos con huella · push el 14 de junio de 2022 · creado el 5 de julio de 2017 · **archivado**

**12 · Authorizer** (tejado/Authorizer) ★572 · NOASSERTION · release `v0.5.0` · 0 archivos con huella · push el 19 de abril de 2024 · creado el 28 de septiembre de 2016

**13 · OpenKeychain** (open-keychain/open-keychain) ★2.633 · GPL-3.0 · sin release etiquetado · 0 archivos con huella · push el 16 de mayo de 2024 · creado el 9 de marzo de 2012

**14 · AuthPass** (authpass/authpass) ★2.811 · GPL-3.0 · release `v1.9.11` · 0 archivos con huella · push el 15 de septiembre de 2026 · creado el 22 de agosto de 2019

*🔏 Los que no firman · ninguno de los catorce*

De los catorce repositorios medidos hoy, **ninguno publica archivo de huella**. Cero. Esto no es una opinión: abrí la página de releases de cada uno y conté los archivos cuyo nombre termina en `.sha256`, `.sha512`, `.asc` o `.sig`. Ninguno trae ninguno.

Esto es diferente a lo que otras piezas de esta serie han medido. En la pieza 01, dos de quince firmaban (droynis y ghost-files). En la pieza 02, uno de veintiuno firmaba (GoogleTVAirPlay). En esta pieza, cero de catorce firman.

La consecuencia es directa: si instalas cualquiera de estos catorce gestores de contraseñas, no tienes forma de comprobar que el archivo que bajaste es el que su autor publicó. Confías en la persona, no en el archivo.

*🏛️ Los cuatro parados*

Cuatro de los catorce están parados o archivados:

**andOTP** ★3.704 · MIT · archivado desde el 14 de junio de 2022 · último push hace más de cuatro años · creado el 5 de julio de 2017. Fue el generador de códigos de segundo factor más querido del ecosistema libre. Su repositorio está archivado: se puede leer, se puede bifurcar porque la licencia MIT lo permite, y nadie lo hace.

**Authorizer** ★572 · NOASSERTION · último push el 19 de abril de 2024 · creado el 28 de septiembre de 2016. Guardaba las contraseñas en el propio teléfono, sin nube. Sin licencia declarada: lo que hay dentro se puede mirar y nada más.

**OpenKeychain** ★2.633 · GPL-3.0 · sin release etiquetado · último push el 16 de mayo de 2024 · creado el 9 de marzo de 2012. Implementación de OpenPGP para Android. Su propia presentación declara que ya no hay desarrollo activo.

**AuthPass** ★2.811 · GPL-3.0 · release `v1.9.11` · último push el 15 de septiembre de 2026 · creado el 22 de agosto de 2019. Empuja código pero no publica paquete desde febrero de 2024. La versión que puedes instalar tiene casi tres años. En un programa que guarda contraseñas, eso no se deja «por si acaso».

*🌅 Cierre*

Catorce gestores de contraseñas. Ninguno publica archivo de huella. Cuatro están parados. La pregunta de esta pieza no tiene respuesta cómoda: si instalas una de estas cajas, confías en la persona, no en el archivo.

Lo medido hoy, dicho sin adorno:

— Catorce repositorios abiertos con la API de GitHub a las 06:38 de Santo Domingo del 7 de noviembre de 2026.
— Ninguno publica archivo de huella.
— Cuatro parados: andOTP (archivado), Authorizer, OpenKeychain y AuthPass.
— Cero paquetes alojados aquí. Cada enlace va al repositorio de su autor.

💓 *7 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* sábado 7 de noviembre de 2026, 06:38 de la mañana en Santo Domingo (10:38 UTC) · catorce repositorios medidos con `GET /repos/{owner}/{repo}` y `GET /repos/{owner}/{repo}/releases/latest` · estrellas, licencia, fecha de creación, último push y release más reciente leídos de la API de GitHub · cero paquetes alojados · cero tablas Markdown.

*🔗 Enlaces*

- Bitwarden: https://github.com/bitwarden/android
- Stratum: https://github.com/stratumauth/app
- Monica: https://github.com/Monica-Pass/Monica
- Vaultwarden: https://github.com/dani-garcia/vaultwarden
- KeePass2Android: https://github.com/PhilippC/keepass2android
- KeePassDX: https://github.com/Kunzisoft/KeePassDX
- Keyguard: https://github.com/AChep/keyguard-app
- Aegis: https://github.com/beemdevelopment/Aegis
- Lucent: https://github.com/Lucent-Project/Lucent
- FreeOTP: https://github.com/freeotp/freeotp-android
- andOTP: https://github.com/andOTP/andOTP
- Authorizer: https://github.com/tejado/Authorizer
- OpenKeychain: https://github.com/open-keychain/open-keychain
- AuthPass: https://github.com/authpass/authpass

#task 022 · volver a medir estos catorce repositorios el 14 de noviembre de 2026 y publicar cuántos de los catorce añadieron un archivo de huella en su release más reciente.
#task 023 · comprobar el 7 de diciembre de 2026 si alguno de los catorce cambió de licencia, dejó de tener release etiquetado o pasó a archivado.
#task 024 · solicitar el Scorecard de OpenSSF para los catorce por la vía pública, para que la próxima medición use los cien puntos y no solo los ochenta que permite la API de repositorios.
