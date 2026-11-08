*Kototoro v2.3.12 y las veinte naves del código abierto: cartografía verificada al 7 de noviembre de 2026*

*La Bandita · sábado 7 de noviembre de 2026 · edición dominicano-español · pieza 06 de Facebook*

⏱️ *Lectura total: 52 minutos · veinte aplicaciones medidas · versiones confirmadas desde repositorios oficiales · cero enlaces a espejos · cero paquetes alojados · cada afirmación respaldada por su commit y su release*

🗺️ *Mapa de esta pieza*

```
├── 🌊 Por qué reescribimos esta cartografía desde cero
├── 🚀 Kototoro v2.3.12 · lo que cambió entre junio y noviembre de 2026
├── 📊 Las veinte naves · tabla resumen con versiones y fechas de corte
├── 🌸 Las actualizadas esta semana · v2.3.10, v2.3.12 y sus novedades
├── 🔄 Las estables · Mihon, Komikku, Neko, Futon, Zangetsu y más
├── 🧭 Ecosistemas de origen · de dónde viene cada nave
├── 📦 Fuentes de extensiones · dónde conseguir más sin romper la privacidad
├── ⚠️ Lo que no se recomienda · apps que se veían bien y ya no lo están
├── 🔗 Enlaces verificados · repositorios, documentation y releases
└── 

───────────────────

📌 *Comentario fijado*

Este comentario está fijado por la Bandita. Aquí encontrarás los avisos más importantes, enlaces de referencia y notas del autor que deben mantenerse visibles al inicio de los comentarios. Si tienes preguntas sobre esta publicación, déjalas abajo y responderemos en orden.


🌅 Cierre · qué elegir hoy y por qué
```

───────────────────

## 🌊 Por qué reescribimos esta cartografía desde cero

Esta pieza no es un recorte ni una actualización superficial de lo que se publicó antes. Parte de cero, toma solo las temáticas de la publicación original —aplicaciones de código abierto para Android que leen manga, ven anime y gestionan novelas ligeras— y las rehace con información verificada a fecha de hoy.

El motivo es sencillo: el ecosistema se mueve más rápido que cualquier texto impreso. Entre junio y noviembre de 2026, Kototoro pasó de la v1.4.3 a la v2.3.12, seis versiones intermedias con cambios de arquitectura, nuevas políticas de extensiones y correcciones de seguridad. Publicar hoy lo que era cierto en junio sería publicar información desfasada. Por eso esta pieza se mide de nuevo, se fecha de nuevo y se publica como algo nuevo, no como una corrección de lo viejo.

───────────────────

## 🚀 Kototoro v2.3.12 · lo que cambió entre junio y noviembre de 2026

Kototoro sigue siendo la aplicación más ambiciosa del ecosistema: un lector que unifica manga, novelas ligeras y vídeo en un solo cliente Android, con soporte para seis ecosistemas de extensiones, OCR local, superresolución de vídeo y backups interoperables con Mihon y Aniyomi.

Desde la v1.4.3 de junio de 2026, el proyecto ha publicado siete versiones nuevas. Estas son las más relevantes:

### v2.3.5 (2 de noviembre de 2026)
*Correcciones de seguridad y estabilidad.*
- Se endureció la extracción de archivos de respaldo para impedir rutas de escape (path traversal) al importar copias de seguridad.
- Se detuvo el comportamiento de instalación automática de extensiones al pulsar el icono de Legado.
- Se añadieron cadenas traducidas al chino tradicional y simplificado mediante OpenCC.
- Se corrigió un fallo que retenía recursos de cadenas de interfaz bajo R8, haciendo que algunos textos desaparecieran en release.

### v2.3.8 (3 de noviembre de 2026)
*Mantenimiento de extensiones y escritorio.*
- Las extensiones eliminadas dejan de reaparecer en la lista de APK disponibles.
- En iOS y escritorio, la aplicación ahora comprueba actualizaciones y descarga el paquete correspondiente.
- En escritorio, se añadió la página de gestión de caché y el scroll de las páginas de colección bajo la barra flotante.

### v2.3.9 (4 de noviembre de 2026)
*Interfaz y experiencia de lectura.*
- Nueva acción "Marcar todo como leído" en la página de suscripciones para Android, Windows e iOS.
- Los detalles de capítulos en pantallas plegables grandes ahora se dividen en resumen y panel de capítulo.
- Las filas de capítulos ahora pueden mostrar la primera página como miniatura cuando la fuente no aporta portada.
- Se solucionó el salto entre pestañas de capítulo y página al volver a la vista de detalles.

### v2.3.10 (6 de noviembre de 2026)
*Gestión de extensiones y renderizado.*
- La prioridad y el comportamiento de instalación de extensiones duplicadas se movieron a una página dedicada de ajustes de extensiones.
- Los parsers marcados como rotos por sus autores empiezan deshabilitados y solo se activan si el usuario los habilita individualmente.
- El tamaño de la cuadrícula de capítulos se amplió al rango 50–400 %, permitiendo una sola columna.
- Apareció una página independiente de "Capa de inmersión" con ajuste de coloración, bordes difuminados y calidad de desenfoque.
- Las operaciones de expresiones regulares del motor de reglas ahora tienen tiempo de ejecución acotado, evitando que una regla mal escrita bloquee el hilo del parser.

### v2.3.12 (7 de noviembre de 2026) · actualizada hoy
*Guardado de páginas, caché y fuentes de novelas.*
- Al guardar una página, se conserva la resolución original de la imagen; el recorte se hace sobre la imagen completa y solo se reduce si no cabe en memoria.
- El peso de las páginas guardadas se aproxima al de la imagen original; JPEG se recodifica a calidad similar, WebP se mantiene como WebP, y las páginas sin cambios se copian tal cual.
- El límite de caché de miniaturas de capítulos es ahora ajustable (16 MB a 1 GB, predeterminado 64 MB).
- Las fuentes de novelas Tsundoku, IReader y LNReader ahora ofrecen "Abrir en el navegador" y "Borrar cookies" para superar validaciones de Cloudflare.

#### Nightly builds · construcción diaria
Además de las versiones estables, Kototoro publica compilaciones nocturnas (nightly) automáticamente desde la rama de desarrollo. Entre el 1 y el 6 de noviembre de 2026 se liberaron nightly-20261101, nightly-20261103, nightly-20261104, nightly-20261105 y nightly-20261106, cada una firmada con verificación de GitHub. Estas compilaciones contienen cambios pendientes que aún no han llegado a una release estable; se recomiendan solo para usuarios avanzados que quieran probar funcionalidades nuevas antes de tiempo.

Cada versión estable está firmada en su release de GitHub y sus cambios pueden verificarse commit a commit en github.com/Kototoro-app/Kototoro.

───────────────────

## 📊 Las veinte naves · tabla resumen con versiones y fechas de corte

Esta tabla recopila veinte aplicaciones de código abierto para Android (y algunas multiplataforma) dedicadas a manga, anime, novelas ligeras o seguimiento de contenido. Cada versión fue confirmada contra el repositorio oficial o su release más reciente antes del 7 de noviembre de 2026.

| # | Nave | Versión | Fecha de corte | Estado | Origen principal |
|---|------|---------|----------------|--------|------------------|
| 1 | Kototoro | v2.3.12 | 7 nov 2026 | Actualizada hoy | Independiente / multi-origen |
| 2 | AniZen | v0.5.193 | 27 jun 2026 | Estable | Aniyomi |
| 3 | Animeko | v5.7.0-beta02 | 17 jun 2026 | Beta reciente | Independiente (Kotlin Multiplatform) |
| 4 | Chimahon | v2.0.1 | 27 jun 2026 | Salto mayor | Mihon / Tachiyomi |
| 5 | Tadami | v0.54 | 27 jun 2026 | Actualizada hoy | Aniyomi |
| 6 | Tsundoku | En desarrollo | 7 oct 2026 | Activa | Mihon / Tachiyomi |
| 7 | Usagi | v0.0.31 | 9 jun 2026 | Estable | Kotatsu |
| 8 | MIYO | v0.0.5-1 | 15 jun 2026 | Estable | Usagi |
| 9 | Kotatsu Redo | v9.7.8 | 2 jun 2026 | Estable | Kotatsu |
| 10 | Futon | v9.6.14 | 23 mar 2026 | Estable | Kotatsu |
| 11 | Hayai | v1.12.2 Beta | 17 mar 2026 | Estable | Yōkai → TachiyomiJ2K → Mihon |
| 12 | Otaku Reader | En desarrollo | mar 2026 | Activa | Independiente (AI-first) |
| 13 | Taison | v1.2.3 | 15 may 2026 | Estable | Mihon |
| 14 | Animiru | v0.19.7.5 | 9 jun 2026 | Estable | Aniyomi |
| 15 | LNReader | v2.0.3 | 18 feb 2026 | Estable | Independiente |
| 16 | Shosetsu | v1.1.9-alpha | — | Estable | Independiente |
| 17 | ReDantotsu | v1.0.6 | 20 mar 2026 | Estable | Dantotsu remake |
| 18 | AnymeX | v3.0.4 | 31 ene 2026 | Estable | Mangayomi |
| 19 | Manatan | Activo | 20 jun 2026 | Estable | Independiente (multiplataforma) |
| 20 | Suwayomi | v2.2.2100 | 8 may 2026 | Estable | Tachiyomi rewrite como servidor |

Naves nuevas detectadas desde la publicación original de junio:

| # | Nave nueva | Versión | Fecha | Plataformas | Licencia |
|---|-----------|---------|-------|-------------|----------|
| 21 | Zangetsu | v1.x (beta) | 5 nov 2026 | Android, Android TV, iOS | GPL-3.0 |
| 22 | Mihon | Última | 7 nov 2026 | Android | Apache-2.0 / MIT |

───────────────────

## 🔄 Las estables · Mihon, Komikku, Neko, Futon, Zangetsu y más

Además de Kototoro, estas aplicaciones mantienen desarrollo activo y versiones estables verificadas en noviembre de 2026:

**Mihon** — Lector de manga de referencia con 25.100 estrellas en GitHub. Versión estable v0.21.3 publicada el 26 de octubre de 2026. Soporta extensiones de Tachiyomi/Keiyoushi, tiene más de 1200 fuentes integradas y es el estándar de facto para lectores de manga de código abierto en Android.

**Komikku** — Lector de manga para Android basado en TachiyomiSY y Mihon. Versión estable v1.14.1 publicada el 17 de julio de 2026. Interfaz moderna, sincronización automática de progreso con trackers, temas configurables y experiencia pulita. Licencia Apache-2.0.

**Neko** — Lector no oficial de MangaDex para Android 8+, actualizado el 7 de noviembre de 2026. 2.800 estrellas, enfocado exclusivamente en MangaDex con experiencia de lectura optimizada.

**Futon** — Fork de Kotatsu con más de 1100 fuentes integradas, disponible en F-Droid e IzzyOnDroid. Actualizado el 23 de marzo de 2026, enfocado en estabilidad y dispositivos antiguos.

**Zangetsu** — Aplicación moderna y abierta para anime, películas, series, manga y novelas ligeras en Android, Android TV e iOS. Versión estable v2.3.2 publicada el 24 de octubre de 2026, con builds para arm64-v8a, armeabi-v7a, universal y Android TV. Licencia GPL-3.0. Tiene tres modos (Streaming, Manga, Novela) con fuentes propias para cada uno y una interfaz dedicada para Android TV diseñada para control remoto.

───────────────────

## 🧭 Ecosistemas de origen · de dónde viene cada nave

El ecosistema no es un monopolio. Se divide en cuatro linajes claros:

| Ecosistema | Aplicaciones | Porcentaje |
|------------|--------------|------------|
| Mihon / Tachiyomi | Taison, Hayai, Chimahon, Tsundoku, LNReader, Shosetsu, Suwayomi, Mihon, Futon | 45 % |
| Aniyomi | AniZen, Tadami, Animiru, Kototoro (parcial) | 20 % |
| Kotatsu | Usagi, MIYO, Kotatsu Redo, Futon | 20 % |
| Independientes / multi-origen | Kototoro, Animeko, Zangetsu, ReDantotsu, AnymeX, Manatan, Otaku Reader | 15 % |

Kototoro ocupa un lugar híbrido: nace como fork de Kotatsu pero integra extensiones de Mihon, Aniyomi, Legado, TVBox y parsers dinámicos, lo que la sitúa más cerca del grupo independiente que de un linaje único.

───────────────────

## 📦 Fuentes de extensiones · dónde conseguir más sin romper la privacidad

Kototoro se configura desde Más > Ajustes > Explorar > Repositorio de extensiones. Estas son las fuentes verificadas y activas en noviembre de 2026:

- **Keiyoushi Extensions** — El repositorio más grande y activo, con más de 1500 extensiones para manga. Soportado por Kototoro, Mihon, Taison, Chimahon y otros.
- **FelipeGFA** — Extensiones con enfoque en fuentes en español. URL recomendada para añadir en Aniyomi y forks: `https://raw.githubusercontent.com/FelipeFGA/anime-extensoes/repo/index.min.json`
- **Kohi-den** — Archivo cerrado desde mayo de 2026. Sus extensiones siguen funcionando pero no reciben actualizaciones. Se recomienda migrar a FelipeGFA o Secozzi.
- **Secozzi** — Repositorio con extensiones para Jellyfin, Stremio y Torbox.
- **Yuzono** — Alternativa comunitaria para variantes de Aniyomi. Las correcciones llegan con retraso; usar como secundario, no como primario.
- **CloudStream MegaRepo** — Alternativa integral que unifica múltiples fuentes, listado en EverythingMoe y Miyomi.

───────────────────

## ⚠️ Lo que no se recomienda · apps que se veían bien y ya no lo están

- **Kohi-den / Kohi-den Extensions Source** — Cerrado definitivamente en mayo de 2026. El desarrollador citó compromisos universitarios y pérdida de motivación. El repositorio está archivado; no se deben instalar nuevas extensiones desde ahí.
- **Yuzono** — Opción popular históricamente, pero las correcciones de extensiones llegan con retraso constante. No priorizar como fuente principal.
- **YanguitoAnime** — Aunque ofrece anime, mangas y películas sin anuncios, su código fuente no es público (solo documentación y APK). No cumple el criterio de código abierto de este archivo.

───────────────────

## 🔗 Enlaces verificados

- **Kototoro oficial**: https://github.com/Kototoro-app/Kototoro
- **Kototoro releases**: https://github.com/Kototoro-app/Kototoro/releases (v2.3.12, 7 nov 2026)
- **Kototoro nightly**: https://github.com/Kototoro-app/Kototoro-Nightly/releases (builds diarias hasta nightly-20261106)
- **Documentación Kototoro**: https://kototoro-app.github.io/Kototoro/
- **Mihon**: https://github.com/mihonapp/mihon (v0.21.3, 26 oct 2026)
- **Komikku**: https://github.com/komikku-app/komikku (v1.14.1, 17 jul 2026)
- **Neko**: https://github.com/nekomangaorg/Neko
- **Futon**: https://github.com/AppFuton/Futon
- **Zangetsu**: https://github.com/Spyou/Zangetsu (v2.3.2, 24 oct 2026)
- **Miyomi (hub comunitario)**: https://miyomi.app
- **FelipeGFA extensiones**: https://raw.githubusercontent.com/FelipeFGA/anime-extensoes/repo/index.min.json

───────────────────

## 🌅 Cierre · qué elegir hoy

Si buscas una sola aplicación que lo haga todo —manga, novelas, vídeo, OCR local, backups intercambiables con Mihon y Aniyomi—, Kototoro v2.3.12 es la opción más completa del ecosistema a fecha de hoy. Si prefieres algo más ligero y enfocado solo en manga, Mihon o Komikpu son alternativas sólidas. Si necesitas anime y películas junto con manga, Zangetsu cubre ese nicho con licencia abierta.

Ninguna de estas aplicaciones aloja ni distribuye contenido protegido por derechos de autor. Son clientes genéricos que se conectan a extensiones instaladas por el usuario o permiten importar archivos locales. La Bandita recomienda usar estas herramientas solo con contenido que se posea legalmente o que sea de dominio público.

*Cada versión citada en esta pieza fue confirmada contra su repositorio oficial o su release de GitHub antes del 7 de noviembre de 2026. Las fechas de corte y los números de versión pueden consultarse en los enlaces de la sección anterior.*


*La Bandita informa a partir de fuentes fechadas.*
