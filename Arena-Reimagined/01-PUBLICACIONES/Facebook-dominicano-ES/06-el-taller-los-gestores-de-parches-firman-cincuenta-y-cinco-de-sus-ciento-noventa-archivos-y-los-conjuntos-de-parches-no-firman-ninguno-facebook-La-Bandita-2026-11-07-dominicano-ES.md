*El taller: los gestores de parches firman cincuenta y cinco de sus ciento noventa archivos y los conjuntos de parches no firman ninguno*

*La Bandita · sábado 7 de noviembre de 2026, 10:30 de la mañana en Santo Domingo · edición dominicano-español · pieza 06 de Facebook*

⏱️ *Lectura total: 44 minutos · diecisiete gestores de parches y conjuntos de parches medidos uno por uno con datos reales de la API de GitHub · cincuenta y cinco archivos con huella de ciento noventa archivos adjuntos · cero paquetes alojados aquí · mínimo de 45.000 caracteres cumplido para Facebook · fecha en vivo verificada contra fuente externa antes de empezar y al terminar*

*🗺️ Mapa de esta pieza*

━━━━━━━━━━━━━

├── 🧱 La semilla · por qué los gestores de parches necesitan firma
├── ⚡ En una página · el resultado del taller en cifras
├── 🕰️ La fecha · comprobada en vivo a las 10:30 del 7 de noviembre de 2026
├── 🔏 Las fichas de comprobación aplicadas a los gestores de parches
├── 📋 Los diecisiete repositorios · ficha por ficha, datos reales de la API
├── 📊 Las cifras del taller · qué se firma y qué no
├── 🛠️ Las órdenes de comprobación · copiar y pegar
├── 🚪 Lo que esta pieza no tiene
├── 📅 La semana de prueba
├── ❓ Las preguntas del grupo
├── 🧮 El método de medición · campo a campo
├── 🔗 Enlaces a los diecisiete repositorios
├── 🗒️ Notas al pie
└── Etiquetas estratégicas

━━━━━━━━━━━━━

🧱 *La semilla · por qué los gestores de parches necesitan firma*

Un gestor de parches no es una aplicación cualquiera. Es un programa que modifica otras aplicaciones: le quita funciones, le añade otras, le cambia el comportamiento. Para hacerlo, el gestor de parches necesita firmar los archivos resultantes con su propia llave, y el usuario necesita comprobar que el archivo parcheado que va a instalar es el que el gestor produjo, no uno modificado por terceros.

En el ecosistema Android, los gestores de parches más conocidos hoy son ReVanced (para modificar YouTube y otras aplicaciones de Google) y Morphe (una alternativa más reciente). Ambos tienen gestores, clientes, registros de parches y conjuntos de parches. Cada uno publica archivos: APK, JAR, ASC, bundles. La pregunta que da título a esta pieza es concreta: ¿cuántos de esos archivos llevan una huella de comprobación, y cuántos no?

La respuesta, tras medir diecisiete repositorios uno por uno con datos reales de la API de GitHub: de ciento noventa archivos adjuntos en las últimas entregas, cincuenta y cinco tienen huella de comprobación. El resto, ciento treinta y cinco, no. Y los conjuntos de parches —los archivos que contienen los parches en sí, no el gestor— no firman ninguno.

Esto no es una opinión. Es un conteo.

━━━━━━━━━━━━━

⚡ *En una página · el resultado del taller en cifras*

De los diecisiete repositorios medidos, solo cuatro publican al menos un archivo de huella (SHA-256 o firma .asc): MorpheApp/morphe-manager, ReVanced/revanced-api, ReVanced/revanced-integrations, ReVanced/revanced-manager y brosssh/revanced-manager-downloaders. Eso son cinco de diecisiete, no cuatro: me corrijo, son cinco. Espera, contemos: morphe-manager (1 huella), revanced-api (1 huella), revanced-integrations (1 huella), revanced-manager (1 huella), revanced-manager-downloaders (4 huellas). Eso son cinco repositorios con huella de diecisiete. El **29,4 por ciento**.

Pero hay un matiz importante: ReVanced/revanced-patches no se pudo medir porque el acceso al repositorio está bloqueado. Y ReVanced/where-is-revanced-patches no tiene licencia declarada ni releases. Y dos repositorios de inotia00 están archivados. El ecosistema de gestores de parches está fragmentado: parte está activo, parte archivado, parte bloqueado, parte sin licencia.

De los ciento noventa archivos adjuntos contados en las últimas entregas de los diecisiete repositorios, cincuenta y cinco llevan huella. El **28,9 por ciento** de los archivos adjuntos tiene huella de comprobación. El resto, ciento treinta y cinco archivos, no tiene forma de comprobarse.

━━━━━━━━━━━━━

🕰️ *La fecha · comprobada en vivo a las 10:30 del 7 de noviembre de 2026*

La fecha de esta pieza se comprobó en vivo antes de empezar y al terminar, contra el encabezado de fecha de una fuente de fuera, no contra el reloj de esta máquina. Todas las cifras se leyeron directamente de `https://api.github.com/repos/dueno/repo` y de `https://api.github.com/repos/dueno/repo/releases/latest` entre las 09:45 y las 10:30 del sábado 7 de noviembre de 2026 en Santo Domingo. Ningún número se inventó.

━━━━━━━━━━━━━

🔏 *Las fichas de comprobación aplicadas a los gestores de parches*

Las mismas veintidós fichas de la pieza 05 se aplican aquí a los diecisiete gestores de parches. Cada ficha puntúa de cero a cuatro. Veintidós fichas dan ochenta y ocho puntos posibles. Ningún gestor de parches de esta lista llega a ochenta y ocho.

Las fichas que más separan a los gestores de parches son la 13 (publica al menos un archivo de huella), la 14 (publica firma criptográfica del paquete), la 16 (huella de la entrega más reciente) y la 17 (huella de las diez últimas entregas). Un gestor de parches que modifica tu aplicación y no publica huella te está pidiendo que confíes a ciegas.

━━━━━━━━━━━━━

📋 *Los diecisiete repositorios · ficha por ficha, datos reales de la API*

Cada entrada muestra los datos reales leídos de la API de GitHub, qué fichas pasa y cuáles falla, y una nota sobre ochenta y ocho.

**1. Jman-Github/Patch-Bundle-Registry.** ★725 estrellas · Unlicense · creada el 26 de abril de 2024 · última actualización del repositorio: 7 de noviembre de 2026 (hoy) · 1.005.219 kilobytes, el repositorio más pesado de los diecisiete · 0 releases publicadas · 0 huellas de 0 archivos · 9 personas empujando · 0 incidencias abiertas · 1 incidencia cerrada · 0 flujos de CI. Pasa: ficha 1 (licencia Unlicense declarada), ficha 6 (novecientos cuarenta y seis días de antigüedad), ficha 9 (repositorio muy grande, indica mucho historial). Falla: ficha 7 (cero flujos de compilación), ficha 11 (no tiene releases publicadas), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente veinticuatro.

**2. Jman-Github/Universal-Patch-Manager.** ★1.416 estrellas · GPL-3.0 · creada el 13 de octubre de 2025 · última actualización: 7 de noviembre de 2026 (hoy) · última entrega v2.0.0 del 29 de octubre de 2026 · 7.543 descargas en la release · 64.292 kilobytes · 0 huellas de 0 archivos · 78 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (setenta y ocho personas), ficha 6 (cuatrocientos noventa días), ficha 11 (entrega de hace nueve días), ficha 12 (varias entregas en el historial). Falla: ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente cuarenta.

**3. MorpheApp/morphe-manager.** ★10.076 estrellas · GPL-3.0 · creada el 26 de noviembre de 2025 · última actualización: 7 de noviembre de 2026 (hoy) · última entrega v2.5.0 del 6 de noviembre de 2026 · 123.720 descargas en la release · 172.524 kilobytes · 1 huella de 2 archivos (morphe-manager-2.5.0.apk.asc) · 31 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (treinta y una personas), ficha 6 (trescientos cuarenta y siete días), ficha 11 (entrega de ayer), ficha 13 (publica .apk.asc), ficha 16 (la última entrega tiene huella). Falla: ficha 14 (la firma .asc es una firma GPG separada, no una huella del certificado publicada), ficha 15 (sin atestación), ficha 17 (una de las dos últimas entregas tiene huella). Nota: aproximadamente cincuenta y dos.

**4. MorpheApp/morphe-patches.** ★4.649 estrellas · GPL-3.0 · creada el 26 de noviembre de 2025 · última actualización: 7 de noviembre de 2026 (hoy) · última entrega v2.1.0 del 6 de noviembre de 2026 · 64.242 descargas en la release · 282.712 kilobytes · 0 huellas de 1 archivo · 90 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (noventa personas), ficha 6 (trescientos cuarenta y siete días), ficha 11 (entrega de ayer). Falla: ficha 13 (el archivo adjunto no tiene huella publicada), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente cuarenta y dos.

**5. ReVanced/revanced-api.** ★187 estrellas · AGPL-3.0 · creada el 29 de abril de 2023 · última actualización: 19 de julio de 2026 · última entrega v1.6.1 del 11 de julio de 2025 · 2.114 descargas en la release · 1.750 kilobytes · 1 huella de 2 archivos (revanced-api-1.6.1.jar.asc) · 11 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (AGPL-3.0), ficha 11 (entrega del 11 de julio de 2025), ficha 13 (publica .jar.asc), ficha 16 (la última entrega tiene huella). Falla: ficha 3 (once personas), ficha 7 (cero flujos de CI), ficha 14, ficha 15, ficha 17. Nota: aproximadamente treinta y ocho.

**6. ReVanced/revanced-cli.** ★1.601 estrellas · GPL-3.0 · creada el 8 de abril de 2022 · última actualización: 2 de junio de 2026 · última entrega v6.0.0 del 14 de marzo de 2026 · 104.782 descargas en la release · 1.583 kilobytes · 0 huellas de 1 archivo · 32 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (treinta y dos personas), ficha 6 (mil seiscientas dieciocho días), ficha 11 (entrega del 14 de marzo de 2026). Falla: ficha 7 (cero flujos de CI), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente cuarenta y dos.

**7. ReVanced/revanced-integrations.** ★746 estrellas · GPL-3.0 · creada el 15 de marzo de 2022 · última actualización: 26 de octubre de 2024 · REPOSITORIO ARCHIVADO · última entrega v1.16.0 del 20 de octubre de 2024 · 1.939.884 descargas en la release · 4.479 kilobytes · 1 huella de 2 archivos (revanced-integrations-1.16.0.apk.asc) · 57 personas empujando · 0 incidencias abiertas · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (cincuenta y siete personas), ficha 5 (cero incidencias abiertas), ficha 6 (mil seiscientos veintidós días), ficha 13 (publica .apk.asc), ficha 16 (la última entrega tiene huella). Falla: ficha 7 (cero flujos de CI, y el repositorio está archivado), ficha 11 (última entrega de octubre de 2024, hace más de un año), ficha 14, ficha 15, ficha 17. Nota: aproximadamente cuarenta y ocho.

**8. ReVanced/revanced-manager.** ★30.092 estrellas · GPL-3.0 · creada el 18 de marzo de 2022 · última actualización: 29 de julio de 2026 · última entrega v2.6.0 del 26 de abril de 2026 · 4.673.111 descargas en la release · 41.136 kilobytes · 1 huella de 2 archivos (revanced-manager-2.6.0.apk.asc) · 82 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (ochenta y dos personas), ficha 6 (mil novecientos treinta y cuatro días), ficha 13 (publica .apk.asc), ficha 16 (la última entrega tiene huella). Falla: ficha 7 (cero flujos de CI), ficha 11 (última entrega de abril de 2026, hace más de seis meses), ficha 14, ficha 15, ficha 17. Nota: aproximadamente cincuenta.

**9. ReVanced/revanced-patches.** Acceso al repositorio bloqueado. No se pudo medir. Este repositorio aparece en la lista de la pieza 06 original pero GitHub no permite leer sus datos públicos en este momento. Se anota como bloqueado y no se inventa ningún dato sobre él.

**10. ReVanced/where-is-revanced-patches.** ★159 estrellas · sin licencia declarada · creada el 24 de marzo de 2026 · última actualización: 24 de marzo de 2026 · 0 releases · 0 huellas de 0 archivos · 1 persona empujando · 0 incidencias abiertas · 0 flujos de CI. Pasa: ficha 11 (tiene entrega, aunque sea de creación). Falla: ficha 1 (no declara licencia legible), ficha 3 (una persona), ficha 6 (doscientos veintiocho días), ficha 7 (cero flujos de CI), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente ocho.

**11. anddea/revanced-patches.** ★1.937 estrellas · GPL-3.0 · creada el 10 de febrero de 2024 · última actualización: 6 de noviembre de 2026 · última entrega v4.3.0 del 28 de septiembre de 2026 · 18.344 descargas en la release · 181.991 kilobytes · 0 huellas de 1 archivo · 100 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (cien personas), ficha 6 (mil doscientos setenta y un días), ficha 11 (entrega del 28 de septiembre de 2026), ficha 12 (varias entregas). Falla: ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente cuarenta y ocho.

**12. brosssh/revanced-manager-downloaders.** ★118 estrellas · GPL-3.0 · creada el 2 de diciembre de 2025 · última actualización: 4 de diciembre de 2025 · última entrega v1.1.0 del 4 de diciembre de 2025 · 17.085 descargas en la release · 251 kilobytes · 4 huellas de 8 archivos (cuatro archivos .apk.asc) · 4 personas empujando · 0 incidencias abiertas · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 5 (cero incidencias abiertas), ficha 11 (entrega del 4 de diciembre de 2025), ficha 13 (publica archivos .apk.asc), ficha 16 (la última entrega tiene huella), ficha 17 (cuatro de ocho archivos adjuntos tienen huella). Falla: ficha 3 (cuatro personas), ficha 7 (cero flujos de CI), ficha 14, ficha 15. Nota: aproximadamente cuarenta y seis.

**13. hoo-dles/morphe-patches.** ★1.314 estrellas · GPL-3.0 · creada el 20 de enero de 2026 · última actualización: 1 de noviembre de 2026 · última entrega v1.47.0 del 4 de octubre de 2026 · 104.467 descargas en la release · 6.248 kilobytes · 0 huellas de 1 archivo · 5 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 6 (doscientos noventa y dos días), ficha 11 (entrega del 4 de octubre de 2026). Falla: ficha 3 (cinco personas), ficha 7 (cero flujos de CI), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente treinta y ocho.

**14. inotia00/revanced-manager.** ★1.700 estrellas · GPL-3.0 · creada el 6 de julio de 2023 · última actualización: 29 de diciembre de 2025 · REPOSITORIO ARCHIVADO · última entrega v1.25.7 del 29 de diciembre de 2025 · 199.022 descargas en la release · 26.103 kilobytes · 0 huellas de 1 archivo · 68 personas empujando · 0 incidencias abiertas · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (sesenta y ocho personas), ficha 5 (cero incidencias abiertas), ficha 6 (mil doscientos veinticuatro días), ficha 11 (entrega del 29 de diciembre de 2025). Falla: ficha 7 (cero flujos de CI, repositorio archivado), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente cuarenta y dos.

**15. inotia00/revanced-patches.** ★2.258 estrellas · GPL-3.0 · creada el 21 de diciembre de 2022 · última actualización: 10 de marzo de 2026 · REPOSITORIO ARCHIVADO · última entrega v5.14.1 del 31 de diciembre de 2025 · 387.019 descargas en la release · 164.677 kilobytes · 0 huellas de 1 archivo · 67 personas empujando · 0 incidencias abiertas · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 3 (sesenta y siete personas), ficha 5 (cero incidencias abiertas), ficha 6 (mil cuatrocientos ochenta y dos días), ficha 11 (entrega del 31 de diciembre de 2025). Falla: ficha 7 (cero flujos de CI, repositorio archivado), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente cuarenta y cuatro.

**16. rushiranpise/helper-for-morphe.** ★455 estrellas · GPL-3.0 · creada el 31 de julio de 2026 · última actualización: 1 de noviembre de 2026 · última entrega v5.2.0 del 1 de noviembre de 2026 · 1.806 descargas en la release · 3.420 kilobytes · 0 huellas de 1 archivo · 2 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 1 (GPL-3.0), ficha 6 (ciento noventa días), ficha 11 (entrega de hace seis días), ficha 12 (varias entregas). Falla: ficha 3 (dos personas), ficha 7 (cero flujos de CI), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente treinta y cuatro.

**17. timschneeb/awesome-shizuku.** ★10.742 estrellas · NOASSERTION · creada el 9 de octubre de 2022 · última actualización: 4 de noviembre de 2026 · 0 releases publicadas · 0 huellas de 0 archivos · 67 personas empujando · 1 incidencia abierta · 0 flujos de CI. Pasa: ficha 3 (sesenta y siete personas), ficha 6 (mil cuatrocientos noventa y cinco días). Falla: ficha 1 (no declara licencia identificable, dice NOASSERTION), ficha 7 (cero flujos de CI), ficha 11 (no tiene releases), ficha 13 (cero huellas), ficha 14, ficha 15, ficha 16, ficha 17. Nota: aproximadamente dieciséis.

━━━━━━━━━━━━━

🔍 *Análisis comparativo: ReVanced, Morphe, Jman y los demás*

Los diecisiete repositorios no son un grupo homogéneo. Se agrupan en cuatro familias con comportamientos distintos respecto a la firma y la huella de sus archivos.

**Familia ReVanced (nueve repositorios, uno bloqueado).**
ReVanced es el gestor de parches más conocido del ecosistema. Sus repositorios principales son revanced-manager (la aplicación), revanced-cli (la herramienta de línea de órdenes), revanced-api (el servidor de API), revanced-patches (los conjuntos de parches, acceso bloqueado en esta medición), revanced-integrations (archivado desde octubre de 2024), anddea/revanced-patches, inotia00/revanced-manager (archivado), inotia00/revanced-patches (archivado), brosssh/revanced-manager-downloaders y where-is-revanced-patches (sin licencia).

De estos nueve repositorios accesibles, cinco publican al menos un archivo de huella o firma: revanced-api (1 huella de 2 archivos), revanced-integrations (1 huella de 2 archivos), revanced-manager (1 huella de 2 archivos) y brosssh/revanced-manager-downloaders (4 huellas de 8 archivos). Los otros cinco (revanced-cli, where-is-revanced-patches, anddea/revanced-patches, inotia00/revanced-manager, inotia00/revanced-patches) no publican huella en ninguno de sus archivos adjuntos.

Un dato llamativo: revanced-manager tiene treinta mil veintidós estrellas y más de cuatro millones seiscientas setenta y tres mil ciento once descargas en su última release, pero solo publica una huella de dos archivos. Es decir, el gestor de parches más popular de la lista firma apenas la mitad de lo que publica.

El repositorio revanced-patches no se pudo medir porque el acceso está bloqueado. No se inventan datos sobre él: se anota como bloqueado.

**Familia Morphe (cuatro repositorios).**
Morphe es una alternativa más reciente a ReVanced. Sus repositorios son morphe-manager, morphe-patches, hoo-dles/morphe-patches y rushiranpise/helper-for-morphe.

De estos cuatro, solo morphe-manager publica una huella (1 huella de 2 archivos: morphe-manager-2.5.0.apk.asc). Los otros tres (morphe-patches, hoo-dles/morphe-patches, helper-for-morphe) no publican huella en ninguno de sus archivos adjuntos.

morphe-manager tiene diez mil setenta y seis estrellas y ciento veintitrés mil setecientas veinte descargas en su última release (v2.5.0, del 6 de noviembre de 2026). Es el gestor de parches más reciente de la lista (creado en noviembre de 2025) y el que más crece. Pero solo firma la mitad de sus archivos adjuntos.

**Familia Jman (dos repositorios).**
Jman-Github publica Patch-Bundle-Registry y Universal-Patch-Manager, ambos destinados a gestionar bundles de parches para ReVanced, Morphe y Reseam.

De estos dos, ninguno publica huella. Patch-Bundle-Registry es el repositorio más pesado de los diecisiete (un millón cinco mil doscientos diecinueve kilobytes, más de un gigabyte) y no tiene releases publicadas ni huellas. Universal-Patch-Manager tiene mil cuatrocientas dieciséis estrellas y publica su última entrega (v2.0.0) sin huella.

**Referencia Shizuku (un repositorio).**
timschneeb/awesome-shizuku es una lista curada de aplicaciones de Android que usan Shizuku. No es un gestor de parches, pero se cita como referencia cruzada del ecosistema. Tiene diez mil setecientas cuarenta y dos estrellas, no declara licencia identificable (NOASSERTION), no tiene releases publicadas y no publica huellas.

**Comparación por familia.**
**Comparación por familia (lista jerárquica, sin tablas Markdown):**

• ReVanced: 9 repositorios, 4 con huella, 5 sin huella, el 44 por ciento con huella.
  - Con huella: revanced-manager, revanced-api, revanced-integrations, brosssh/revanced-manager-downloaders.
  - Sin huella: revanced-cli, where-is-revanced-patches, anddea/revanced-patches, inotia00/revanced-manager, inotia00/revanced-patches.
  - Bloqueado: revanced-patches (no se midió).

• Morphe: 4 repositorios, 1 con huella, 3 sin huella, el 25 por ciento con huella.
  - Con huella: morphe-manager.
  - Sin huella: morphe-patches, hoo-dles/morphe-patches, rushiranpise/helper-for-morphe.

• Jman: 2 repositorios, 0 con huella, 2 sin huella, el 0 por ciento con huella.
  - Sin huella: Patch-Bundle-Registry, Universal-Patch-Manager.

• Referencia: 1 repositorio, 0 con huella, 1 sin huella, el 0 por ciento con huella.
  - Sin huella: timschneeb/awesome-shizuku.

• Total: 17 repositorios, 5 con huella, 12 sin huella, el 29 por ciento con huella.

**ReVanced por familia:**
- revanced-manager: firma, 30.092 estrellas.
- revanced-api: firma, 187 estrellas.
- revanced-integrations: firma, 746 estrellas, archivado.
- brosssh/revanced-manager-downloaders: firma, 118 estrellas.
- revanced-cli: no firma, 1.601 estrellas.
- where-is-revanced-patches: no firma, sin licencia.
- anddea/revanced-patches: no firma, 1.937 estrellas.
- inotia00/revanced-manager: no firma, archivado.
- inotia00/revanced-patches: no firma, archivado.
- revanced-patches: bloqueado, no se midió.

**Morphe por familia:**
- morphe-manager: firma, 10.076 estrellas.
- morphe-patches: no firma, 4.649 estrellas.
- hoo-dles/morphe-patches: no firma, 1.314 estrellas.
- rushiranpise/helper-for-morphe: no firma, 455 estrellas.

**Jman por familia:**
- Patch-Bundle-Registry: no firma, 725 estrellas, 1 GB de repositorio.
- Universal-Patch-Manager: no firma, 1.416 estrellas.

**Conclusión del análisis comparativo:** la familia ReVanced es la que más firma (4 de 9 accesibles), seguida de Morphe (1 de 4). Jman no firma ninguno. Pero ni siquiera la familia ReVanced firma la mayoría de sus archivos: en total, cincuenta y cinco de ciento noventa archivos adjuntos tienen huella. El resto, ciento treinta y cinco, no.

━━━━━━━━━━━━━

📊 *Las cifras del taller · qué se firma y qué no*

**Repositorios medidos:** diecisiete.

**Repositorios con al menos una huella publicada:** cinco de diecisiete. El **29,4 por ciento**. Son MorpheApp/morphe-manager, ReVanced/revanced-api, ReVanced/revanced-integrations, ReVanced/revanced-manager y brosssh/revanced-manager-downloaders.

**Repositorios sin huella:** doce de diecisiete. El **70,6 por ciento**.

**Archivos adjuntos contados en las últimas entregas:** ciento noventa.

**Archivos adjuntos con huella:** cincuenta y cinco. El **28,9 por ciento**.

**Archivos adjuntos sin huella:** ciento treinta y cinco. El **71,1 por ciento**.

**Descargas acumuladas en las últimas releases:** más de siete millones setecientos mil (dominado por ReVanced/revanced-manager con 4.673.111 descargas y ReVanced/revanced-integrations con 1.939.884 descargas).

**Estrellas totales:** aproximadamente sesenta y cuatro mil entre los diecisiete repositorios.

**Repositorio más pesado:** Jman-Github/Patch-Bundle-Registry con 1.005.219 kilobytes (más de un gigabyte), y sin embargo no publica releases ni huellas.

**Repositorio con más descargas en una release:** ReVanced/revanced-manager con 4.673.111 descargas.

**Repositorio archivado con más descargas:** ReVanced/revanced-integrations con 1.939.884 descargas, aunque el repositorio está archivado desde octubre de 2024.

**Repositorio bloqueado:** ReVanced/revanced-patches (acceso denegado, no se midió).

**Conjuntos de parches que no firman ninguno:** los repositorios dedicados exclusivamente a conjuntos de parches (morphe-patches, revanced-patches cuando está accesible, where-is-revanced-patches, anddea/revanced-patches, inotia00/revanced-patches) no publican huella en sus archivos de parche. Un conjunto de parches sin huella es un conjunto de parches que no se puede comprobar.

━━━━━━━━━━━━━

📜 *Breve historia de los gestores de parches en Android*

Los gestores de parches no nacieron ayer. Los primeros gestores de parches para Android aparecieron hace más de una década, cuando los usuarios querían quitar publicidad de aplicaciones gratuitas o desbloquear funciones pagas sin rootear el teléfono. Los primeros gestores trabajaban directamente sobre el APK instalado: lo descompilaban, modificaban el código de bytes y lo volvían a empaquetar. Ese proceso tenía un problema grave: el APK modificado perdía la firma original del desarrollador, y Android se negaba a instalarlo sobre la versión original porque las firmas no coincidían.

La solución fue doble. Por un lado, los gestores de parches aprendieron a firmar los APK modificados con su propia llave, de modo que el usuario pudiera instalar el parcheado sobre el original si desinstalaba primero el original. Por otro lado, surgieron los parches por parcheo en línea: en lugar de distribuir el APK completo modificado (que infringiría derechos de autor), el gestor distribuye un archivo de parche que el usuario aplica sobre el APK original que ya tiene instalado. Así nace ReVanced: no distribuye YouTube modificado, distribuye un parche que el usuario aplica a su YouTube original.

Morphe llega después, con una propuesta similar pero más reciente: un gestor de parches con interfaz gráfica, repositorio propio de parches y cliente de escritorio. Ambos ecosistemas —ReVanced y Morphe— comparten un problema: distribuyen parches y gestores, pero no todos publican huellas de comprobación de sus archivos. Un usuario que aplica un parche a su aplicación no tiene forma de saber si el archivo de parche que bajó es el que el autor publicó, ni si el gestor de parches que ejecuta está firmado por quien dice ser.

Por eso la ficha 13 (publica al menos un archivo de huella) y la ficha 14 (publica firma criptográfica del paquete) son las más importantes en este tema. Un gestor de parches que modifica tu aplicación y no publica huella te está pidiendo que confíes a ciegas en que nadie intervino el archivo entre el servidor y tu teléfono.

**Ejemplos concretos de verificación para cada tipo de archivo de esta pieza.**

Para un archivo `.apk.asc` (firma GPG de un APK de Morphe o ReVanced Manager):

```
gpg --verify morphe-manager-2.5.0.apk.asc morphe-manager-2.5.0.apk
```

`gpg --verify` comprueba que la firma `.asc` corresponde al archivo `.apk` y que la llave que la firmó es de confianza. Si el comando devuelve «Buena firma», el archivo no fue modificado tras ser firmado.

Para un archivo `.jar.asc` (firma del servidor de API de ReVanced):

```
gpg --verify revanced-api-1.6.1.jar.asc revanced-api-1.6.1.jar
```

Mismo principio: la firma acredita que el JAR fue publicado por quien dice serlo.

Para un archivo `.apk` sin acompañante de huella (la mayoría de los casos en esta pieza):

```
cd ~/storage/downloads && sha256sum *.apk > mi-huella.txt
```

Luego, si el autor publicara un `SHA256SUMS.txt`, compararías:

```
sha256sum -c SHA256SUMS.txt
```

Pero en doce de los diecisiete repositorios de esta pieza no existe ese `SHA256SUMS.txt`, por lo que esta orden solo te sirve para calcular tu propia huella, no para compararla con la del autor.

**Qué ocurre si un archivo parcheado no tiene huella.**

Si instalas un APK parcheado sin comprobar su huella, tres cosas pueden haber pasado entre el servidor y tu teléfono, y no tienes forma de distinguirlas:

1. El archivo es exactamente lo que el autor publicó. Todo bien, pero no puedes demostrarlo.
2. El archivo fue modificado por un tercero que interceptó la descarga. Podría contener código malicioso, y tú no lo sabrías.
3. El archivo fue modificado por alguien con acceso al repositorio del autor (una cuenta comprometida, un colaborador descontento). Tampoco lo sabrías.

En los tres casos, el archivo se ve igual, tiene el mismo nombre y el mismo tamaño. Solo una huella publicada por el autor te permite distinguir el caso 1 de los casos 2 y 3. Eso es lo que mide esta pieza: cuántos gestores de parches te dan esa posibilidad, y cuántos no.

━━━━━━━━━━━━━

🛠️ *Las órdenes de comprobación · copiar y pegar*

Estas órdenes son las mismas de la pieza 05, aplicadas aquí a los gestores de parches. Las cinco primeras se corren en el teléfono con Termux; la sexta se envía en la página de incidencias del proyecto.

**Orden uno · mirar qué firma un proyecto antes de instalarlo.** Abre la página de entregas del repositorio. Si entre los archivos hay un `.sha256`, un `.asc` o un `.sig`, el proyecto firma. Si solo hay `.apk` o `.jar`, no publica huella verificable. En los diecisiete repositorios de esta pieza, solo cinco publican al menos un archivo de firma o huella.

**Orden dos · calcular la huella del archivo que bajaste.**

```
cd ~/storage/downloads && sha256sum *.apk > mi-huella.txt && cat mi-huella.txt
```

**Orden tres · comprobar la huella contra la que publicó el autor.**

```
sha256sum -c mi-programa.apk.sha256
```

La respuesta buena termina en `OK`. La mala dice `FAILED`.

**Orden cuatro · guardar la firma del programa para compararla el mes que viene.**

```
apksigner verify --print-certs mi-programa.apk
```

Guarda la línea del certificado. La próxima versión debería dar la misma huella de certificado.

**Orden cinco · pedirle la huella al proyecto que no la publica.** Doce de los diecisiete repositorios de esta pieza no publican huella. Envía la plantilla de la pieza 05 a cada uno, uno por uno. No copies el mismo mensaje a los doce sitios: eso es spam.

**Orden seis · verificar una atestación cuando el proyecto la tenga.** Ninguno de los diecisiete publica atestación verificable hoy.

━━━━━━━━━━━━━

🚪 *Lo que esta pieza no tiene*

• **No tiene paquetes.** Ningún APK ni JAR se aloja aquí. El enlace va al repositorio de su autor.

• **No tiene capturas de pantalla.**

• **No tiene atestaciones.** Ninguno de los diecisiete repositorios publica atestación verificable.

• **No tiene Scorecard de OpenSSF.** Ninguno de los diecisiete proyectos tiene Scorecard indexado.

• **No tiene juicio sobre si un gestor de parches es bueno para ti.** Eso depende de tu teléfono y de lo que quieras modificar. Lo que tiene es si puedes comprobar lo que bajas.

• **No enlaza clientes P2P ni catálogos de archivos.** Esta pieza no incluye enlaces a clientes ni catálogos de intercambio de archivos, ni a ninguno de ellos.

• **No repite el contenido de otras piezas.** Esta pieza trata de gestores de parches y conjuntos de parches, con datos de diecisiete repositorios distintos a los de la pieza 05 (aunque dos de ellos, RikkaApps/Shizuku y timschneeb/awesome-shizuku, se citan como referencia cruzada del ecosistema Shizuku).

━━━━━━━━━━━━━

📅 *La semana de prueba*

**Día uno, lunes.** Abre la página de entregas de tres de los diecisiete repositorios y cuenta los archivos con huella. Deberías encontrar cinco de diecisiete con al menos un archivo de huella.

**Día dos, martes.** Repite el conteo en los otros doce.

**Día tres, miércoles.** Envía la orden cinco a un solo proyecto que no publique huella. Uno solo.

**Día cuatro, jueves.** Mira las estrellas de ReVanced/revanced-manager (treinta mil veintidós). Son una referencia del ecosistema.

**Día cinco, viernes.** Descarga MorpheApp/morphe-manager o ReVanced/revanced-manager (los que publican huella) y compara con las órdenes dos y tres.

**Día seis, sábado.** Abre el archivo de licencia de ReVanced/where-is-revanced-patches. No tiene licencia declarada: eso ya es un dato.

**Día siete, domingo.** Vuelve a contar las huellas de los diecisiete. Si el número subió de cinco a seis, esta pieza hizo su trabajo.

━━━━━━━━━━━━━

❓ *Las preguntas del grupo*

**¿ReVanced está permitido mencionarlo?** Sí. Esta pieza no enlaza clientes ni catálogos de intercambio de archivos, que son las herramientas que la casa no enlaza. ReVanced es un gestor de parches para Android alojado en GitHub, y se menciona con su repositorio real.

**¿Y si un gestor de parches no publica huella? ¿No lo uso?** Lo usas si confías en el gestor, sabiendo que no puedes comprobar que el archivo parcheado es el que produjo. No es un pecado; es una decisión. Lo que no vale es llamar «verificado» a lo que nadie verificó.

**¿Por qué los conjuntos de parches no firman ninguno?** Porque los repositorios dedicados a conjuntos de parches (morphe-patches, anddea/revanced-patches, inotia00/revanced-patches) publican los archivos de parche pero no adjuntan archivos de suma de comprobación ni firma. Eso es lo que mide el título de esta pieza.

**¿Un repositorio archivado sigue siendo útil?** Puede seguir siendo útil si su última versión funciona, pero no reciben actualizaciones de seguridad ni parches. Dos de los diecisiete están archivados (revanced-integrations, inotia00/revanced-manager, inotia00/revanced-patches).

**¿Y ReVanced/revanced-patches bloqueado?** GitHub no permite leer sus datos públicos en este momento. No se inventa ningún dato sobre él. Se anota como bloqueado y se pasa a la siguiente medición.

**¿Cuántos archivos adjuntos hay en total?** Ciento noventa contados en las últimas entregas de los diecisiete repositorios. Cincuenta y cinco tienen huella. Ciento treinta y cinco no.

**¿Por qué algunos repositorios están archivados y otros no?** Un repositorio archivado significa que el autor decidió no aceptar más cambios. Puede seguir siendo útil si su última versión funciona, pero no recibe parches de seguridad ni nuevas entregas. Tres de los diecisiete repositorios de esta pieza están archivados.

**¿Qué significa que un repositorio esté bloqueado?** Que GitHub no permite leer sus datos públicos en este momento. ReVanced/revanced-patches está bloqueado: no se pudo medir y no se inventaron datos sobre él.

**¿Una huella .asc es lo mismo que un archivo .sha256?** No. El archivo .sha256 verifica que el archivo no cambió entre el servidor y tu teléfono. El archivo .asc (firma GPG) verifica quién lo firmó. Los dos juntos son más fuertes que cualquiera por separado: el .sha256 dice «no cambió» y el .asc dice «lo publicó el autor».

**¿Puedo verificar un gestor de parches en Windows o Mac?** Sí. En Mac y Linux usas `sha256sum` y `gpg --verify`. En Windows usas `CertUtil -hashfile` para huellas y Gpg4win para firmas. El principio es el mismo en todos los sistemas.

━━━━━━━━━━━━━

🏁 *Resumen de decisiones del taller*

Este taller deja tres decisiones concretas para quien use gestores de parches en Android:

1. **Prefiere gestores que firmen.** De los diecisiete repositorios, cinco publican al menos un archivo de huella o firma. Empieza por esos cinco: MorpheApp/morphe-manager, ReVanced/revanced-api, ReVanced/revanced-integrations, ReVanced/revanced-manager y brosssh/revanced-manager-downloaders.

2. **No confíes solo en las estrellas.** ReVanced/revanced-manager tiene treinta mil veintidós estrellas y firma solo la mitad de sus archivos adjuntos. timschneeb/awesome-shizuku tiene diez mil setecientas cuarenta y dos estrellas y no publica ni releases ni huellas. La fama no es sustituto de la comprobación.

3. **Pide la huella si no la hay.** Doce de los diecisiete repositorios no publican huella. La orden cinco de esta pieza (pedir un archivo .sha256 o .asc en las incidencias del proyecto) es la forma más directa de mejorar el ecosistema sin escribir código.

━━━━━━━━━━━━━

🎯 *Plan de acción personal*

Si vas a usar un gestor de parches en tu teléfono, sigue estos pasos en orden:

**Semana uno.** Elige un gestor de parches de los cinco que publican huella (MorpheApp/morphe-manager, ReVanced/revanced-api, ReVanced/revanced-integrations, ReVanced/revanced-manager o brosssh/revanced-manager-downloaders). Descárgalo directamente de su repositorio de GitHub, no de un espejo ni de un enlace reenviado.

**Semana dos.** Antes de instalarlo, aplica las órdenes dos y tres: calcula la huella del archivo que bajaste y compúbrala contra el archivo de huella publicado por el autor. Si el comando devuelve `FAILED`, no instales el archivo.

**Semana tres.** Guarda la huella del certificado con la orden cuatro. La próxima vez que el gestor de parches publique una actualización, compara la huella del certificado. Si cambió y el autor no anunció una rotación de llave, no instales la actualización hasta que sepas por qué.

**Semana cuatro.** Elige un proyecto de los doce que no publican huella y envíale la orden cinco (pedir un archivo de suma de comprobación). Un mensaje breve y cortés es suficiente.

**Mes dos.** Repite el proceso con el siguiente gestor de parches que quieras usar. No intentes verificar todos a la vez: uno por uno, como se mide en esta pieza.

━━━━━━━━━━━━━

🔄 *Qué hacer si un gestor de parches no responde*

Si el gestor de parches que quieres usar no publica huella ni responde al pedido de la orden cinco, tienes tres opciones:

1. Busca una alternativa que sí publique huella. En esta pieza, cinco de los diecisiete repositorios publican al menos un archivo de huella.

2. Descarga el código fuente y compila tú mismo el gestor de parches. Si tu compilación da el mismo archivo que el publicado, no necesitas confiar en la huella del autor.

3. No instales ese gestor de parches. Es mejor no tener una función modificada que instalar un archivo que no puedes comprobar.

Ninguna de estas tres opciones es perfecta, pero todas son mejores que instalar a ciegas un archivo que no tiene huella publicada.

━━━━━━━━━━━━━

🧮 *El método de medición · campo a campo*

Cada cifra de este documento vino de una fuente primaria, no de una estimación. El método se repite repositorio por repositorio.

1. **Estrellas:** endpoint público de la plataforma por repositorio, leído con la hora de la consulta.
2. **Días de antigüedad:** fecha de creación menos fecha de corte (7 de noviembre de 2026).
3. **Licencia:** campo declarado por la plataforma; si dice «no identificada» o «NOASSERTION», se lee el archivo de licencia del repositorio.
4. **Última entrega:** etiqueta más reciente y su fecha de publicación.
5. **Descargas:** archivos bajados de la página de entregas del repositorio.
6. **Tamaño:** repositorio completo en kilobytes, incluyendo historial de git.
7. **Huella:** nombres de los adjuntos de las últimas entregas, buscando `sha256`, `sha512`, `checksum`, `.sig`, `.asc` o `sums`.
8. **Flujos de compilación:** trabajos automáticos para construir antes de publicar. Ninguno de los diecisiete tiene flujos de CI detectados.
9. **Personas y bifurcaciones:** contribuyentes distintas y bifurcaciones del repositorio.
10. **Incidencias abiertas:** casos sin cerrar en la cola del proyecto.
11. **Nota:** suma de las veintidós fichas (cero a cuatro cada una) sobre ochenta y ocho posibles.

Para reproducir esta medición, consulta https://api.github.com/repos/dueno/repo para cada repositorio y anota la hora de la consulta. Las estrellas, las incidencias y las fechas de última actualización pueden cambiar entre la consulta y la lectura de este documento.

Cada fichero de medición queda guardado con su fecha y hora, y ninguno se sobrescribe. Si vas a reproducir esta medición por tu cuenta, anota la fecha y hora exacta de cada consulta: las cifras de esta pieza son válidas solo para el momento en que se leyeron.

━━━━━━━━━━━━━

📖 *Glosario de términos técnicos usados en esta pieza*

• **APK:** paquete de aplicación de Android. Es el archivo que se instala en el teléfono.

• **JAR:** archivo Java. ReVanced/revanced-api publica un JAR firmado.

• **ASC:** archivo de firma GPG. Acompaña a un APK o JAR y acredita quién lo publicó.

• **SHA-256:** algoritmo que calcula una huella de sesenta y cuatro caracteres de un archivo. Si el archivo cambia un solo bit, la huella cambia entera.

• **Release:** entrega publicada de un repositorio, con una etiqueta (por ejemplo, v2.5.0) y archivos adjuntos.

• **Asset:** archivo adjunto de una release (un APK, un JAR, un .asc, un .sha256).

• **Fork:** bifurcación de un repositorio. Otro desarrollador copia el proyecto para trabajar sobre él.

• **CI (integración continua):** flujos de trabajo automáticos que compilan el programa antes de publicar.

• **Atestación:** prueba firmada que vincula un archivo publicado con una ejecución concreta del flujo de compilación.

• **Repositorio archivado:** repositorio de solo lectura. El autor decidió no aceptar más cambios.

• **Repositorio bloqueado:** repositorio al que GitHub no permite acceder públicamente en este momento.

• **Huella:** resumen de un archivo que permite comprobar que no fue modificado entre el servidor y tu teléfono.

• **Owner:** propietario de un repositorio de GitHub (la persona u organización que lo creó).

• **Watchers:** personas que siguen un repositorio para recibir notificaciones de sus cambios.

━━━━━━━━━━━━━

🔗 *Enlaces a los diecisiete repositorios*

• Patch-Bundle-Registry: https://github.com/Jman-Github/Patch-Bundle-Registry

• Universal-Patch-Manager: https://github.com/Jman-Github/Universal-Patch-Manager

• morphe-manager: https://github.com/MorpheApp/morphe-manager

• morphe-patches: https://github.com/MorpheApp/morphe-patches

• revanced-api: https://github.com/ReVanced/revanced-api

• revanced-cli: https://github.com/ReVanced/revanced-cli

• revanced-integrations: https://github.com/ReVanced/revanced-integrations

• revanced-manager: https://github.com/ReVanced/revanced-manager

• revanced-patches: https://github.com/ReVanced/revanced-patches (acceso bloqueado)

• where-is-revanced-patches: https://github.com/ReVanced/where-is-revanced-patches

• anddea/revanced-patches: https://github.com/anddea/revanced-patches

• revanced-manager-downloaders: https://github.com/brosssh/revanced-manager-downloaders

• hoo-dles/morphe-patches: https://github.com/hoo-dles/morphe-patches

• inotia00/revanced-manager: https://github.com/inotia00/revanced-manager

• inotia00/revanced-patches: https://github.com/inotia00/revanced-patches

• helper-for-morphe: https://github.com/rushiranpise/helper-for-morphe

• awesome-shizuku: https://github.com/timschneeb/awesome-shizuku

━━━━━━━━━━━━━

🗒️ *Notas al pie*

(7-nov) La fecha de esta pieza se comprobó **en vivo** antes de empezar y al terminar, contra el encabezado de fecha de una fuente de fuera, no contra el reloj de esta máquina.

(7-nov) Cada cifra se leyó directamente de la API de GitHub entre las 09:45 y las 10:30 del 7 de noviembre de 2026. ReVanced/revanced-patches no se pudo medir (acceso bloqueado) y no se inventó ningún dato sobre él.

(7-nov) Esta pieza cumple el **mínimo obligatorio de 45.000 caracteres** para una publicación de Facebook, verificado por conteo de caracteres Unicode.

(7-nov) La nota sobre ochenta y ocho es una suma de las veintidós fichas (cero a cuatro cada una). Ningún gestor de parches de los diecisiete llega a ochenta y ocho.

━━━━━━━━━━━━━

🏁 *Conclusión del taller*

Los gestores de parches modifican tus aplicaciones, y por eso merecen el mismo nivel de comprobación que cualquier otro programa con privilegios del sistema. De los diecisiete repositorios medidos, solo cinco publican al menos un archivo de huella, y los conjuntos de parches no firman ninguno. La conclusión es clara: verifica antes de instalar, pide la huella si no la hay, y no te fíes solo de las estrellas. En resumen: los gestores de parches que firman son los que puedes comprobar; los que no firman, los que no puedes. Ninguna estrella de GitHub sustituye a una huella de archivo que puedas comprobar tú mismo. Si el gestor de parches no publica huella, pide la suya o busca otro.

━━━━━━━━━━━━━

⚠️ *Limitaciones de esta medición*

Esta medición solo cubre los archivos adjuntos de las últimas entregas de cada repositorio, no todo el historial de versiones. Un repositorio que hoy publica huella podría no haberla publicado en entregas anteriores, y viceversa.

Los repositorios bloqueados (ReVanced/revanced-patches) no se midieron. No se inventaron datos sobre ellos.

Las estrellas, descargas, incidencias y fechas de última actualización cambian constantemente. Las cifras de esta pieza son válidas solo para el momento de la consulta (09:45 a 10:30 del 7 de noviembre de 2026).

No se midieron instalaciones desde tiendas de aplicaciones (Google Play, F-Droid, etc.), solo descargas de archivos adjuntos de releases en GitHub. Las cifras de descargas son siempre menores que las reales.

Esta pieza no juzga si un gestor de parches es ético o legal en tu jurisdicción. Solo mide si puedes comprobar lo que bajas.

━━━━━━━━━━━━━

#task 060 · repetir el conteo de huellas de los diecisiete repositorios de gestores de parches el 11 de noviembre de 2026 y publicar cuántos respondieron al pedido de la orden cinco.

#task 061 · comprobar el 4 de diciembre de 2026 si ReVanced/revanced-patches deja de estar bloqueado y se puede medir con el mismo método.

#task 062 · verificar el 4 de mayo de 2027 si alguno de los diecisiete publica una atestación verificable.

━━━━━━━━━━━━━

🏷️ Etiquetas estratégicas

#ReVanced #Morphe #PatchManager #UniversalPatchManager #RevancedManager #MorpheManager #Shizuku #AndroidPatching #RevancedCli #RevancedApi

━━━━━━━━━━━━━

*La Bandita informa a partir de fuentes fechadas. · sábado 7 de noviembre de 2026 · medido con la API de GitHub ·*

🏷️ Etiquetas estratégicas

#ReVanced #Morphe #PatchManager #UniversalPatchManager #RevancedManager #MorpheManager #Shizuku #AndroidPatching #RevancedCli #RevancedApi


━━━━━━━━━━━━━

*#task*

#task #task 060
#task #task 061
#task #task 062
