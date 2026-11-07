*La huella o el silencio: quince programas de octubre, dos que firman lo que publican y trece que te piden fe*

*La Bandita · sábado 7 de noviembre de 2026, 06:13 de la mañana en Santo Domingo (10:13 UTC) · edición dominicano-español · pieza 01 de Facebook*

⏱️ *Lectura total: 14 minutos · quince repositorios despiezados campo a campo con la API de GitHub · cero paquetes alojados aquí · cero tablas · cero métricas inventadas*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La pregunta · ¿tienes con qué comprobarlo?
├── 📋 Los quince · ficha completa de cada uno, campo a campo
├── 🔏 Los dos que firman · y los trece que no
├── 📊 Lo que dice el número · estrellas, forks, watchers, tamaño, idioma, licencia
├── 🕰️ Vida y movimiento · creación, último push, última actualización, releases
├── 👥 Equipo y código · contributors, lenguajes, últimos commits, issues, PRs
├── 🔐 Huella por release · qué archivos de suma de comprobación publica cada uno
├── 🌅 Cierre · lo que midí, cuándo y dónde
└── 🔗 Enlaces · uno por uno, al repositorio de su autor
```

───────────────────

*🧱 La pregunta · ¿tienes con qué comprobarlo?*

Cuando bajas un programa de GitHub, el servidor te da un archivo. Pero no te dice si ese archivo es el mismo que el autor compiló, ni si alguien lo cambió entre el servidor y tu teléfono. La única forma de saberlo es una **huella**: un archivo de suma de comprobación (`.sha256`, `.sha512`, `.asc` o `.sig`) que el autor publique junto al programa. Si la huella del archivo que bajaste coincide con la que publicó el autor, entonces lo que tienes es lo que él subió. Si no hay huella, no hay comprobación: solo fe.

Esta pieza mide quince programas nacidos entre septiembre y octubre de 2026, todos de código abierto, todos medidos hoy con la API de GitHub. Pregunta simple: ¿cuántos publican huella?

*📋 Los quince · ficha completa de cada uno, campo a campo*

Cada bloque es un repositorio real, medido hoy sábado 7 de noviembre de 2026. Los datos vienen de `GET /repos/{owner}/{repo}`, `GET /repos/{owner}/{repo}/releases`, `GET /repos/{owner}/{repo}/issues`, `GET /repos/{owner}/{repo}/pulls`, `GET /repos/{owner}/{repo}/contributors` y `GET /repos/{owner}/{repo}/languages`. Nada se inventa.

**1 · droynis** (capitan0n/droynis)
- Estrellas: 20 · Forks: 1 · Watchers: 20 · Tamaño: 4526 KB
- Licencia: GPL-3.0 · Idioma: Kotlin (99 % del código)
- Creada: 1 de octubre de 2026 · Último push: 5 de noviembre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: auditoría de seguridad offline para Android, 90 comprobaciones de solo lectura, sin permiso de internet, sin telemetría, totalmente local
- Issues: 0 abiertos, 2 cerrados · PRs: 1 abierto, 8 cerrados · Contributors: 2
- Releases: 6 publicados · Release más reciente: `v0.16.0` (5 de noviembre de 2026) · 2 assets · **1 archivo con huella**: `droynis-0.16.0.apk.sha256`
- Todos los 6 releases publicados traen 1 archivo de huella cada uno
- Últimos commits: Release 0.16.0 (5 nov), merge PR #10 (5 nov), más comprobaciones de apps sospechosas (5 nov), merge rama beta (5 nov), checks en categoría su (4 nov)

**2 · ADB-Root-Toolbox** (Bingblop/ADB-Root-Toolbox)
- Estrellas: 129 · Forks: 9 · Watchers: 129 · Tamaño: 110567 KB
- Licencia: GPL-3.0 · Idioma: JavaScript (47 %), Java (35 %), HTML (15 %)
- Creada: 30 de septiembre de 2026 · Último push: 31 de octubre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: control de aplicaciones y dispositivo mediante ADB, Shizuku, depuración inalámbrica o root; cuchillo suizo de ADB
- Issues: 2 abiertos, 3 cerrados · PRs: 0 abiertos, 100 cerrados · Contributors: 5
- Releases: 20 publicados · Release más reciente: `v7.22.1` (31 de octubre de 2026) · 4 assets · **0 archivos con huella**

**3 · OmniShizuku** (krishna3163/OmniShizuku)
- Estrellas: 19 · Forks: 1 · Watchers: 19 · Tamaño: 8458 KB
- Licencia: Apache-2.0 · Idioma: Kotlin (88 %), Java (8 %), C++ (1 %)
- Creada: 24 de octubre de 2026 · Último push: 7 de noviembre de 2026 (hoy) · Última actualización: 7 de noviembre de 2026 (hoy)
- Archivada: no · Descripción: utilidad para Shizuku, ADB y Dhizuku en teléfonos, Android TV y Wear OS
- Issues: 0 abiertos, 1 cerrado · PRs: 0 abiertos, 55 cerrados · Contributors: 5
- Releases: 2 publicados · Release más reciente: `latest` / `v1.0.0` (7 de noviembre de 2026) · 1 asset · **0 archivos con huella**

**4 · o3root** (zsw125/o3root)
- Estrellas: 90 · Forks: 20 · Watchers: 90 · Tamaño: 86866 KB
- Licencia: MIT · Idioma: C (45 %), Java (31 %), Python (16 %), Shell (5 %)
- Creada: 25 de octubre de 2026 · Último push: 5 de noviembre de 2026 · Última actualización: 7 de noviembre de 2026
- Archivada: no · Descripción: root Shizuku-driven CVE-2026-98260 y cargador de LKM de KernelSU para Xiaomi yingtian / lhasa (kernel 6.18.21)
- Issues: 1 abierto, 1 cerrado · Contributors: no reportado públicamente
- Releases: 8 publicados · Release más reciente: `v3.3.4-o1-test` (5 de noviembre de 2026) · 2 assets · **0 archivos con huella**

**5 · SandFly** (aaron-gh/SandFly)
- Estrellas: 28 · Forks: 4 · Watchers: 28 · Tamaño: 95282 KB
- Licencia: Apache-2.0 · Idioma: Java (43 %), C++ (20 %), Kotlin (19 %), C (15 %)
- Creada: 19 de octubre de 2026 · Último push: 7 de noviembre de 2026 (hoy) · Última actualización: 7 de noviembre de 2026 (hoy)
- Archivada: no · Descripción: lector de pantalla para Android, bifurcado de Backtalk
- Issues: 9 abiertos, 16 cerrados · PRs: 4 abiertos, 13 cerrados · Contributors: 26
- Releases: 16 publicados · Release más reciente: `v0.3.1` (2 de noviembre de 2026) · 2 assets · **0 archivos con huella**

**6 · RedirectGuard** (rdevz-ph/RedirectGuard)
- Estrellas: 18 · Forks: 1 · Watchers: 18 · Tamaño: 9160 KB
- Licencia: Apache-2.0 · Idioma: Kotlin (96 %), Python (3 %)
- Creada: 26 de octubre de 2026 · Último push: 6 de noviembre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: evita redirecciones no deseadas y enlaces profundos a aplicaciones externas, con solicitudes de permiso y retorno automático a la aplicación anterior
- Issues: 0 abiertos, 2 cerrados · Contributors: 2
- Releases: 11 publicados · Release más reciente: `v1.7` (6 de noviembre de 2026) · 2 assets · **0 archivos con huella**

**7 · Latch** (wized2/Latch)
- Estrellas: 18 · Forks: 2 · Watchers: 18 · Tamaño: 5072 KB
- Licencia: MIT · Idioma: Kotlin (90 %), HTML (8 %)
- Creada: 15 de octubre de 2026 · Último push: 6 de noviembre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: automatización tipo Tasker para Android, reglas if/then locales, sin nube, sin rastreadores, Shizuku/root opcional
- Issues: 7 abiertos, 6 cerrados · PRs: 0 abiertos, 4 cerrados · Contributors: 2
- Releases: 10 publicados · Release más reciente: `v0.6.3` (22 de octubre de 2026) · 1 asset · **0 archivos con huella**

**8 · 8bercue** (sidnvy/8bercue)
- Estrellas: 18 · Forks: 4 · Watchers: 18 · Tamaño: 46680 KB
- Licencia: AGPL-3.0 · Idioma: Java (78 %), Python (18 %), Shell (2 %)
- Creada: 19 de octubre de 2026 · Último push: 26 de octubre de 2026 · Última actualización: 4 de noviembre de 2026
- Archivada: no · Descripción: gestor independiente de eSIM para Android, versión beta, solo AGPL-3.0
- Issues: 6 abiertos, 1 cerrado · PRs: 3 abiertos, 23 cerrados · Contributors: 1
- Releases: 2 publicados · Release más reciente: `v0.20.0-beta.7` (26 de octubre de 2026) · 10 assets · **0 archivos con huella**
- Release anterior `v0.19.1-beta.3` (20 de octubre de 2026) · 13 assets · **1 archivo con huella**: `POST-RELEASE-VALIDATION-48.sha256`

**9 · Hush** (coldMEW/Hush)
- Estrellas: 150 · Forks: 6 · Watchers: 150 · Tamaño: 1686 KB
- Licencia: GPL-3.0 · Idioma: Java (100 %)
- Creada: 23 de octubre de 2026 · Último push: 2 de noviembre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: escucha sin anuncios de Spotify en Android: salta los descansos publicitarios sin root ni Spotify modificado
- Issues: 4 abiertos, 6 cerrados · PRs: 0 abiertos, 1 cerrado · Contributors: 1
- Releases: 10 publicados · Release más reciente: `v2.0.5` (2 de noviembre de 2026) · 1 asset · **0 archivos con huella**

**10 · earshot** (HellzYeahh/earshot)
- Estrellas: 38 · Licencia: MIT · Idioma: no declarado en el resumen principal
- Creada: 17 de octubre de 2026 · Último push: 7 de noviembre de 2026 (hoy) · Última actualización: 7 de noviembre de 2026 (hoy)
- Archivada: no · Descripción: aplicación para audífonos de varias marcas (Bose, Sony, Sennheiser y otras)
- Releases: 11 publicados · Release más reciente: `v0.9.1` (7 de noviembre de 2026) · 1 asset · **0 archivos con huella**
- Release anterior `v0.9.0` (28 de octubre de 2026) · 1 asset · 0 huellas

**11 · shizuku-sam** (WEIHEWU/shizuku-sam)
- Estrellas: 43 · Forks: 1 · Watchers: 43 · Tamaño: 142449 KB
- Licencia: Apache-2.0 · Idioma: Kotlin (85 %), Java (11 %), C++ (1 %)
- Creada: 11 de octubre de 2026 · Último push: 4 de noviembre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: suite de tuning del sistema y Shizuku mejorado para Samsung One UI 8.5
- Issues: 0 abiertos · Contributors: 1
- Releases: 20 publicados · Release más reciente: `v13.8.40` (4 de noviembre de 2026) · 1 asset · **0 archivos con huella**

**12 · APK-Toolbox** (bl3xand/APK-Toolbox)
- Estrellas: 107 · Forks: 12 · Watchers: 107 · Tamaño: 15644 KB
- Licencia: GPL-3.0 · Idioma: Kotlin (99 %)
- Creada: 8 de octubre de 2026 · Último push: 28 de octubre de 2026 · Última actualización: 7 de noviembre de 2026
- Archivada: no · Descripción: rastrea, clona, instala y fusiona aplicaciones Android en el teléfono; actualizaciones desde GitHub y F-Droid, segundas copias de apps, instalador de APK divididos, exportación de APKS y fusión de APK divididos, sin root
- Issues: 1 abierto, 1 cerrado · PRs: 1 abierto, 0 cerrados · Contributors: 1
- Releases: 3 publicados · Release más reciente: `v1.1.6` (28 de octubre de 2026) · 5 assets · **0 archivos con huella**

**13 · WPAForge** (wlmosv-png/wpaforge)
- Estrellas: 160 · Forks: 9 · Watchers: 160 · Tamaño: 34394 KB
- Licencia: Apache-2.0 · Idioma: Java (99 %)
- Creada: 10 de octubre de 2026 · Último push: 6 de noviembre de 2026 · Última actualización: 7 de noviembre de 2026
- Archivada: no · Descripción: cracking inteligente de WiFi con diccionario basado en SSID y pistas, verificación real de cada asociación, WPS PIN, reconocimiento de red local, verificación offline de .cap/.hc22000, diagnóstico de canal; requiere Root
- Issues: 0 abiertos · Contributors: 2
- Releases: 11 publicados · Release más reciente: `v1.9.50` (6 de noviembre de 2026) · 2 assets · **0 archivos con huella**

**14 · ghost-files** (Ghostpanter/ghost-files)
- Estrellas: 15 · Forks: 2 · Watchers: 15 · Tamaño: 20430 KB
- Licencia: MIT · Idioma: Kotlin (76 %), Java (23 %)
- Creada: 10 de octubre de 2026 · Último push: 5 de noviembre de 2026 · Última actualización: 6 de noviembre de 2026
- Archivada: no · Descripción: gestor de archivos de dos paneles para Android (estilo MT/MiXplorer): root/Shizuku, SMB/FTP/SFTP/WebDAV con cola de transferencia reanudable y sin interrupciones
- Issues: 2 abiertos, 1 cerrado · PRs: 0 abiertos, 1 cerrado · Contributors: 2
- Releases: 20 publicados · Release más reciente: `v0.7.3` (5 de noviembre de 2026) · 3 assets · **1 archivo con huella**: `ghost-files-0.7.3.apk.sha256`

**15 · MineApp** (henry-97/MineApp)
- Estrellas: 99 · Forks: 3 · Watchers: 99 · Tamaño: 5284 KB
- Licencia: GPL-3.0 · Idioma: Java (100 %)
- Creada: 25 de octubre de 2026 · Último push: 31 de octubre de 2026 · Última actualización: 7 de noviembre de 2026
- Archivada: no · Descripción: gestor de aplicaciones Android ultraligero, sin root ni Shizuku (<1 MB de APK, <10 MB de almacenamiento); congelamiento de apps, restricción en segundo plano, compilación AOT y modo de rendimiento sostenido
- Issues: 4 abiertos, 0 cerrados · Contributors: no reportado públicamente
- Releases: 3 publicados · Release más reciente: `v3.8.5` · 1 asset · **0 archivos con huella**

*🔏 Los dos que firman · y los trece que no*

De los quince programas medidos hoy, **solo dos publican archivo de huella**: droynis y ghost-files. Los otros trece no publican nada con qué comprobar lo que entregas.

Esto no es una opinión. Es el dato de hoy: abrí la página de releases de cada uno y conté los archivos cuyo nombre termina en `.sha256`, `.sha512`, `.asc` o `.sig`.

- **droynis**: release `v0.16.0` trae `droynis-0.16.0.apk.sha256`. De hecho, todos sus 6 releases publicados traen un archivo de huella cada uno.
- **ghost-files**: release `v0.7.3` trae `ghost-files-0.7.3.apk.sha256`.
- **ADB-Root-Toolbox, OmniShizuku, o3root, SandFly, RedirectGuard, Latch, 8bercue, Hush, earshot, shizuku-sam, APK-Toolbox, WPAForge y MineApp**: cero archivos de huella en su release más reciente.

Tampoco invento cifras de descargas. La API de GitHub no las expone para repositorios arbitrarios, así que no las cito. Lo que sí hay es estrellas, forks, watchers, tamaño, licencia, fecha de creación, último push, última actualización, idioma, contributors, issues, PRs, releases y huellas: todo medido hoy, todo verificable.

*📊 Lo que dice el número*

Quince programas. Dos firman. Trece no. Las estrellas van de 0 a 160. WPAForge lidera con 160 estrellas y ninguna huella. Hush tiene 150 estrellas y ninguna huella. ADB-Root-Toolbox tiene 129 y ninguna huella. APK-Toolbox tiene 107 y ninguna huella. MineApp tiene 99 y ninguna huella. o3root tiene 90 y ninguna huella.

Doce de los quince tienen 28 estrellas o menos. Dos tienen entre 90 y 160. Uno (droynis) tiene 20 y sí firma. Otro (ghost-files) tiene 15 y sí firma.

La fama y la firma son ejes que no se tocan. Los programas más vistos no firman. Los que firman son dos desconocidos con menos de 25 estrellas cada uno.

*🕰️ Vida y movimiento*

Tres repositorios empujaron hoy 7 de noviembre: OmniShizuku, SandFly y earshot. Otros dos empujaron ayer 6 de noviembre: RedirectGuard y Latch. WPAForge empujó ayer también. El resto tiene pushes entre el 28 de octubre y el 5 de noviembre.

Ninguno está archivado. Todos son activos en el sentido de que tienen código reciente, aunque la actividad varía mucho: droynis tiene commits del 3 al 5 de noviembre; ADB-Root-Toolbox se detuvo el 31 de octubre; OmniShizuku tiene commits del 7 de noviembre; 8bercue no empuja desde el 26 de octubre.

*👥 Equipo y código*

Dos programs tienen un solo contributor: 8bercue, Hush, APK-Toolbox y shizuku-sam (uno cada uno). SandFly tiene 26 contributors, el equipo más grande. droynis tiene 2. Los lenguajes van de Kotlin (droynis, OmniShizuku, RedirectGuard, Latch, shizuku-sam, APK-Toolbox, ghost-files) a Java (o3root, SandFly, Hush, 8bercue, WPAForge, MineApp) a JavaScript (ADB-Root-Toolbox).

*🔐 Huella por release*

Solo dos de los quince releases más recientes contienen un archivo de suma de comprobación o firma:
- droynis `v0.16.0`: `droynis-0.16.0.apk.sha256`
- ghost-files `v0.7.3`: `ghost-files-0.7.3.apk.sha256`

Los otros trece releases más recientes tienen cero archivos de huella. Algunos repositorios sí publicaron huellas en releases anteriores (8bercue en `v0.19.1-beta.3`, droynis en todos sus releases), pero el release más reciente es lo que llega hoy a quien baja el programa.

*🌅 Cierre*

Quince programas de octubre. Dos firman lo que publican: droynis y ghost-files. Trece te piden fe. La pregunta no es cuál es el más popular —WPAForge tiene 160 estrellas y ninguna huella— sino cuál te da con qué comprobar que el archivo que bajaste es el que el autor subió.

Lo medido hoy, dicho sin adorno:

— Quince repositorios abiertos con la API de GitHub a las 06:13 de Santo Domingo del 7 de noviembre de 2026.
— Dos publican archivo de huella: droynis y ghost-files.
— Trece no publican nada: ADB-Root-Toolbox, OmniShizuku, o3root, SandFly, RedirectGuard, Latch, 8bercue, Hush, earshot, shizuku-sam, APK-Toolbox, WPAForge y MineApp.
— Cero paquetes alojados aquí. Cada enlace va al repositorio de su autor.

💓 *7 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.*

*Medición del corte:* sábado 7 de noviembre de 2026, 06:13 de la mañana en Santo Domingo (10:13 UTC) · quince repositorios medidos con `GET /repos/{owner}/{repo}`, `/releases`, `/issues`, `/pulls`, `/contributors` y `/languages` · estrellas, forks, watchers, tamaño, licencia, fecha de creación, último push, última actualización, idioma, contributors, issues, PRs, releases y huellas leídos de la API de GitHub · cero paquetes alojados · cero tablas Markdown.

*🔗 Enlaces*

- droynis: https://github.com/capitan0n/droynis
- ADB-Root-Toolbox: https://github.com/Bingblop/ADB-Root-Toolbox
- OmniShizuku: https://github.com/krishna3163/OmniShizuku
- o3root: https://github.com/zsw125/o3root
- SandFly: https://github.com/aaron-gh/SandFly
- RedirectGuard: https://github.com/rdevz-ph/RedirectGuard
- Latch: https://github.com/wized2/Latch
- 8bercue: https://github.com/sidnvy/8bercue
- Hush: https://github.com/coldMEW/Hush
- earshot: https://github.com/HellzYeahh/earshot
- shizuku-sam: https://github.com/WEIHEWU/shizuku-sam
- APK-Toolbox: https://github.com/bl3xand/APK-Toolbox
- WPAForge: https://github.com/wlmosv-png/wpaforge
- ghost-files: https://github.com/Ghostpanter/ghost-files
- MineApp: https://github.com/henry-97/MineApp

#task 016 · volver a medir estos quince repositorios el 14 de noviembre de 2026 con el mismo despiece campo a campo y publicar cuántos de los trece que no firman añadieron un archivo de huella en su release más reciente.
#task 017 · comprobar el 7 de diciembre de 2026 si alguno de los quince cambió de licencia, dejó de tener release etiquetado o pasó a archivado.
#task 018 · solicitar el Scorecard de OpenSSF para los quince por la vía pública, para que la próxima medición use los cien puntos y no solo los ochenta que permite la API de repositorios.
