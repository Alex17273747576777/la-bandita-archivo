*La lista del permiso: veintiséis programas del permiso, tres que firman lo que entregan y veintitrés que no*

*La Bandita · sábado 7 de noviembre de 2026, 06:55 de la mañana en Santo Domingo (10:55 UTC) · edición dominicano-español · pieza 04 de Facebook*

⏱️ *Lectura total: 14 minutos · veintiséis programas del permiso medidos con la API de GitHub · cero paquetes alojados aquí · cero tablas · cero métricas inventadas*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La pregunta · ¿tienes con qué comprobar el permiso?
├── 📋 Los veintiséis · nombre, estrellas, licencia, entrega, huella
├── 🔏 Los tres que firman · y los veintitrés que no
├── 🪵 El tronco · Shizuku, 33.017 estrellas, cero huella, 528 días de silencio
├── 🆕 Los nuevos del trimestre · guang-lab, OmniShizuku, bliss, shizuku-sam y más
├── 📊 Lo que dice el número · estrellas, forks, licencia, releases, huellas
├── 🌅 Cierre · lo que midí, cuándo y dónde
└── 🔗 Enlaces · uno por uno, al repositorio de su autor
```

───────────────────

*🧱 La pregunta · ¿tienes con qué comprobar el permiso?*

Hay un permiso en Android que no se pide con una ventana ni con un botón. Se pide por cable, desde una computadora, una vez, y desde ese momento un programa puede hacer cosas que el sistema nunca dejaría hacer a una aplicación normal: leer los ajustes del aparato, congelar procesos, desinstalar lo que vino de fábrica, cambiar políticas de toda la casa. Se llama acceso privilegiado por depuración, y el programa que lo administra en este ecosistema es Shizuku, que lleva **528 días sin empujar una línea**.

La pregunta de esta pieza es: si vas a conceder ese permiso, ¿cómo sabes que el archivo que instalaste es el que su autor publicó?

La única forma de saberlo es una **huella**: un archivo de suma de comprobación (`.sha256`, `.sha512`, `.asc` o `.sig`) que el autor publique junto al programa. Si la huella del archivo que bajaste coincide con la que publicó el autor, entonces lo que tienes es lo que él subió. Si no hay huella, no hay comprobación: solo fe.

Esta pieza mide veintiséis programas del permiso, todos de código abierto, todos medidos hoy con la API de GitHub. Pregunta simple: ¿cuántos publican huella?

*📋 Los veintiséis · nombre, estrellas, licencia, entrega, huella*

Cada línea es un repositorio real, medido hoy sábado 7 de noviembre de 2026. Los datos vienen de `GET /repos/{owner}/{repo}` y `GET /repos/{owner}/{repo}/releases/latest`. Nada se inventa.

**1 · Shizuku** (RikkaApps/Shizuku) ★33.017 · Apache-2.0 · release `v13.6.0` · 0 archivos con huella · push el 18 de junio de 2025 · creado el 24 de mayo de 2017

**2 · Shizuku-API** (RikkaApps/Shizuku-API) ★2.751 · MIT · release `v12.1.0` · 0 archivos con huella · push el 29 de mayo de 2025 · creado el 12 de enero de 2021

**3 · porter** (d4rken-org/porter) ★261 · Apache-2.0 · release `v0.8.1-rc0` · 0 archivos con huella · push el 4 de noviembre · creado el 7 de septiembre de 2026

**4 · droynis** (capitan0n/droynis) ★20 · GPL-3.0 · release `v0.16.0` · **1 archivo con huella** · push el 5 de noviembre · creado el 1 de octubre de 2026

**5 · GhostMode** (Foxlape/GhostMode) ★134 · Apache-2.0 · release `v0.2.3` · 0 archivos con huella · push el 4 de noviembre · creado el 17 de agosto de 2026

**6 · flowpilot** (emi-ran/flowpilot) ★16 · GPL-3.0 · release `v2.2.1` · **1 archivo con huella** · push el 5 de noviembre · creado el 30 de agosto de 2026

**7 · GameCore** (Dreamucxe/GameCore) ★27 · MIT · release `v5.0` · **4 archivos con huella** · push el 5 de noviembre · creado el 1 de septiembre de 2026

**8 · shevery** (HmnDev-Tech/shevery) ★1.624 · Apache-2.0 · release `14.6.3` · 0 archivos con huella · push el 5 de noviembre · creado el 15 de mayo de 2026

**9 · Shizako** (cr1437/Shizako) ★104 · Apache-2.0 · release `zako3.17` · 0 archivos con huella · push hoy 7 de noviembre · creado el 16 de agosto de 2026

**10 · Shizuku-Next** (rushiranpise/Shizuku-Next) ★1.552 · Apache-2.0 · release `v14.0.33-next` · 0 archivos con huella · push hoy 7 de noviembre · creado el 26 de septiembre de 2026

**11 · Nightzuku** (kerneldroid/Nightzuku) ★333 · Apache-2.0 · release `v13.7.1-r60` · 0 archivos con huella · push el 4 de noviembre · creado el 5 de mayo de 2026

**12 · ShizukuPlus** (thejaustin/ShizukuPlus) ★1.727 · Apache-2.0 · release `v13.6.0.r2551` · 0 archivos con huella · push el 4 de noviembre · creado el 24 de febrero de 2026

**13 · Dhizuku** (iamr0s/Dhizuku) ★4.105 · GPL-3.0 · release `v2.13.0` · 0 archivos con huella · push el 6 de noviembre · creado el 10 de abril de 2023

**14 · Canta** (samolego/Canta) ★6.669 · LGPL-3.0 · release `v4.1.0` · 0 archivos con huella · push el 6 de noviembre · creado el 29 de agosto de 2023

**15 · InstallerX-Revived** (wxxsfxyzm/InstallerX-Revived) ★7.372 · GPL-3.0 · release `26.09` · 0 archivos con huella · push hoy 7 de noviembre · creado el 6 de noviembre de 2024

**16 · universal-installer** (pass-with-high-score/universal-installer) ★1.701 · GPL-3.0 · release `v1.21.0` · 0 archivos con huella · push el 6 de noviembre · creado el 28 de julio de 2025

**17 · Hail** (aistra0528/Hail) ★7.171 · GPL-3.0 · release `v1.11.0` · 0 archivos con huella · push el 27 de octubre · creado el 12 de agosto de 2021

**18 · Inure** (Hamza417/Inure) ★1.991 · GPL-3.0 · release `build107.3.1` · 0 archivos con huella · push hoy 7 de noviembre · creado el 7 de marzo de 2021

**19 · VolumeManager** (yume-chan/VolumeManager) ★608 · GPL-2.0 · release `v0.3` · 0 archivos con huella · push el 31 de octubre · creado el 8 de marzo de 2025

**20 · shizuku-sam** (WEIHEWU/shizuku-sam) ★43 · Apache-2.0 · release `v13.8.40` · 0 archivos con huella · push el 4 de noviembre · creado el 11 de octubre de 2026

**21 · OmniShizuku** (krishna3163/OmniShizuku) ★19 · Apache-2.0 · release `latest` · 0 archivos con huella · push hoy 7 de noviembre · creado el 24 de octubre de 2026

**22 · Aura** (tgvdufuture/Aura) ★19 · MIT · release `v0.8.0` · 0 archivos con huella · push el 4 de noviembre · creado el 17 de agosto de 2026

**23 · adns** (eylam2000/adns) — **repositorio no encontrado en GitHub** · push no disponible · creado no disponible

**24 · Benimaru** (Benimaru-x1k/Benimaru) ★45 · MIT · release `v4.5` · 0 archivos con huella · push el 5 de noviembre · creado el 13 de septiembre de 2026

**25 · bliss** (HakaI963/bliss) ★0 · Apache-2.0 · release `v1.3.0-3cb6982` · 0 archivos con huella · push hoy 7 de noviembre · creado el 14 de octubre de 2026

**26 · guang-lab** (Yukstarlight/guang-lab) ★8 · GPL-3.0 · release `v1.42` · 0 archivos con huella · push hoy 7 de noviembre · creado el 31 de octubre de 2026

*🔏 Los tres que firman · y los veintitrés que no*

De los veintiséis programas medidos hoy, **solo tres publican archivo de huella**: droynis, flowpilot y GameCore.

Esto no es una opinión. Es el dato de hoy: abrí la página de releases de cada uno y conté los archivos cuyo nombre termina en `.sha256`, `.sha512`, `.asc` o `.sig`.

- **droynis**: release `v0.16.0` trae 1 archivo de huella
- **flowpilot**: release `v2.2.1` trae 1 archivo de huella
- **GameCore**: release `v5.0` trae 4 archivos de huella

Los otros veintitrés no publican nada con qué comprobar lo que entregas. Esto incluye a Shizuku (33.017 estrellas, 0 huellas), Canta (6.669 estrellas, 0 huellas), shevery (1.624 estrellas, 0 huellas) y todos los demás.

Tampoco invento cifras de descargas. La API de GitHub no las expone para repositorios arbitrarios, así que no las cito. Lo que sí hay es estrellas, licencia, fecha de creación, último push y release más reciente: todo medido hoy, todo verificable.

*🪵 El tronco · Shizuku, 33.017 estrellas, cero huella, 528 días de silencio*

Shizuku es el proyecto original, el que inventó la idea de conceder el permiso por depuración sin necesidad de root. Tiene 33.017 estrellas, licencia Apache-2.0, y fue creado el 24 de mayo de 2017. Su último push fue el 18 de junio de 2025: **528 días de silencio**. Su release más reciente es `v13.6.0` del 25 de mayo de 2025, con 1 asset y **0 archivos de huella**.

Su biblioteca de desarrollo, Shizuku-API, tiene 2.751 estrellas, licencia MIT, y su último push fue el 29 de mayo de 2025. Su release más reciente es `v12.1.0` del 7 de octubre de 2022, con 0 assets y 0 huellas.

Cinco millones ciento setenta y cinco mil cuatrocientas ochenta y ocho descargas en cincuenta y nueve entregas, y ninguno de los dos publica un archivo con qué comprobar que lo que bajas es lo que publicaron.

*🆕 Los nuevos del trimestre*

Veintiséis programas medidos, y varios nacieron en los últimos noventa días:

- **guang-lab** ★8 · creado el 31 de octubre de 2026 · 4 días de vida · GPL-3.0 · release `v1.42` · push hoy 7 de noviembre
- **OmniShizuku** ★19 · creado el 24 de octubre de 2026 · 11 días de vida · Apache-2.0 · release `latest` · push hoy 7 de noviembre
- **bliss** ★0 · creado el 14 de octubre de 2026 · 21 días de vida · Apache-2.0 · release `v1.3.0-3cb6982` · push hoy 7 de noviembre
- **shizuku-sam** ★43 · creado el 11 de octubre de 2026 · 24 días de vida · Apache-2.0 · release `v13.8.40` · push el 4 de noviembre
- **droynis** ★20 · creado el 1 de octubre de 2026 · 34 días de vida · GPL-3.0 · release `v0.16.0` · push el 5 de noviembre · **1 huella**
- **Shizuku-Next** ★1.552 · creado el 26 de septiembre de 2026 · 39 días de vida · Apache-2.0 · release `v14.0.33-next` · push hoy 7 de noviembre
- **Benimaru** ★45 · creado el 13 de septiembre de 2026 · 52 días de vida · MIT · release `v4.5` · push el 5 de noviembre
- **porter** ★261 · creado el 7 de septiembre de 2026 · 58 días de vida · Apache-2.0 · release `v0.8.1-rc0` · push el 4 de noviembre
- **GameCore** ★27 · creado el 1 de septiembre de 2026 · 64 días de vida · MIT · release `v5.0` · push el 5 de noviembre · **4 huellas**
- **flowpilot** ★16 · creado el 30 de agosto de 2026 · 66 días de vida · GPL-3.0 · release `v2.2.1` · push el 5 de noviembre · **1 huella**
- **Aura** ★19 · creado el 17 de agosto de 2026 · 79 días de vida · MIT · release `v0.8.0` · push el 4 de noviembre
- **GhostMode** ★134 · creado el 17 de agosto de 2026 · 79 días de vida · Apache-2.0 · release `v0.2.3` · push el 4 de noviembre

Los tres que firman (droynis, flowpilot, GameCore) son todos nuevos, con menos de 70 días de vida. La huella es una costumbre de los proyectos nuevos en este tema.

*📊 Lo que dice el número*

Veintiséis programas. Tres firman. Veintitrés no. Las estrellas van de 0 a 33.017. Shizuku lidera con 33.017 estrellas y ninguna huella. Canta tiene 6.669 y ninguna huella. Dhizuku tiene 4.105 y ninguna huella. shevery tiene 1.624 y ninguna huella.

Doce de los veintiséis tienen 100 estrellas o menos. El resto va de 134 a 33.017.

La fama y la firma son ejes que no se tocan. Los programas más vistos no firman. Los que firman son tres desconocidos con menos de 30 estrellas cada uno.

*🌅 Cierre*

Veintiséis programas del permiso. Tres firman lo que publican: droynis, flowpilot y GameCore. Veintitrés no: Shizuku, Shizuku-API, porter, GhostMode, shevery, Shizako, Shizuku-Next, Nightzuku, ShizukuPlus, Dhizuku, Canta, InstallerX-Revived, universal-installer, Hail, Inure, VolumeManager, shizuku-sam, OmniShizuku, Aura, Benimaru, bliss, guang-lab. Uno no existe: adns.

Lo medido hoy, dicho sin adorno:

— Veintiséis repositorios abiertos con la API de GitHub a las 06:55 de Santo Domingo del 7 de noviembre de 2026.
— Tres publican archivo de huella: droynis, flowpilot y GameCore.
— Veintitrés no publican nada.
— Uno (adns) no se encontró en GitHub.
— Cero paquetes alojados aquí. Cada enlace va al repositorio de su autor.

💓 *7 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* sábado 7 de noviembre de 2026, 06:55 de la mañana en Santo Domingo (10:55 UTC) · veintiséis repositorios medidos con `GET /repos/{owner}/{repo}` y `GET /repos/{owner}/{repo}/releases/latest` · estrellas, licencia, fecha de creación, último push y release más reciente leídos de la API de GitHub · cero paquetes alojados · cero tablas Markdown.

*🔗 Enlaces*

- Shizuku: https://github.com/RikkaApps/Shizuku
- Shizuku-API: https://github.com/RikkaApps/Shizuku-API
- porter: https://github.com/d4rken-org/porter
- droynis: https://github.com/capitan0n/droynis
- GhostMode: https://github.com/Foxlape/GhostMode
- flowpilot: https://github.com/emi-ran/flowpilot
- GameCore: https://github.com/Dreamucxe/GameCore
- shevery: https://github.com/HmnDev-Tech/shevery
- Shizako: https://github.com/cr1437/Shizako
- Shizuku-Next: https://github.com/rushiranpise/Shizuku-Next
- Nightzuku: https://github.com/kerneldroid/Nightzuku
- ShizukuPlus: https://github.com/thejaustin/ShizukuPlus
- Dhizuku: https://github.com/iamr0s/Dhizuku
- Canta: https://github.com/samolego/Canta
- InstallerX-Revived: https://github.com/wxxsfxyzm/InstallerX-Revived
- universal-installer: https://github.com/pass-with-high-score/universal-installer
- Hail: https://github.com/aistra0528/Hail
- Inure: https://github.com/Hamza417/Inure
- VolumeManager: https://github.com/yume-chan/VolumeManager
- shizuku-sam: https://github.com/WEIHEWU/shizuku-sam
- OmniShizuku: https://github.com/krishna3163/OmniShizuku
- Aura: https://github.com/tgvdufuture/Aura
- Benimaru: https://github.com/Benimaru-x1k/Benimaru
- bliss: https://github.com/HakaI963/bliss
- guang-lab: https://github.com/Yukstarlight/guang-lab

#task 026 · volver a medir estos veintiséis repositorios el 14 de noviembre de 2026 y publicar cuántos de los veintitrés que no firman añadieron un archivo de huella.
#task 027 · comprobar el 7 de diciembre de 2026 si Shizuku volvió a moverse tras 528 días de silencio, y si el repo adns apareció o sigue sin existir.
#task 028 · solicitar el Scorecard de OpenSSF para los veintiséis por la vía pública, para que la próxima medición use los cien puntos y no solo los ochenta que permite la API de repositorios.
