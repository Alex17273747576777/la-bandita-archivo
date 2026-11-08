# kototoro · Kototoro-app

*Lector multimedia de código abierto para Android: manga, novelas ligeras y vídeo en una sola app*

**Racimo:** lectores-de-manga · **Repositorio:** `Kototoro-app/Kototoro` · **Estado:** vivo · **Medido:** 2026-11-07 12:00 UTC

## Qué es, según quien lo hace

> *Kototoro is built for users who want one Android app for manga, novels, and video instead of maintaining separate apps for each content type.*

*Es lo que declara su documentación oficial. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · última entrega el 7 de noviembre de 2026 (hace 0 días)
- **Estrellas:** consultar en repositorio · bifurcaciones y incidencias: consultar en GitHub
- **Licencia:** consultar en repositorio
- **Lenguaje:** Kotlin · creado antes de julio de 2026
- **Última entrega:** `v2.3.12` del 7 de noviembre de 2026 · compilaciones nightly hasta `nightly-20261106`
- **Plataformas que menciona su documentación:** Android
- **Medido:** 2026-11-07 12:00 UTC

## Cómo se consigue

- la web que da el proyecto: https://kototoro-app.github.io/Kototoro/
- releases: https://github.com/Kototoro-app/Kototoro/releases/tag/v2.3.12
- nightly builds: https://github.com/Kototoro-app/Kototoro-Nightly/releases

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/Kototoro-app/Kototoro
- la última entrega estable: https://github.com/Kototoro-app/Kototoro/releases/latest
- compilaciones nightly: https://github.com/Kototoro-app/Kototoro-Nightly/releases
- documentación oficial: https://kototoro-app.github.io/Kototoro/

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Kototoro es el lector multimedia más ambicioso del ecosistema de código abierto para Android. No es solo manga: también lee novelas ligeras y reproduce vídeo, todo bajo una misma interfaz. Su rasgo más distintivo es el sistema de entidades, que relaciona cómics, novelas y vídeos entre sí —si lees un manga y existe su adaptación en anime o una novela ligera relacionada, Kototoro te lo muestra como contenido vinculado.

Lo que **no** trae es contenido. Es el estante vacío: las fuentes las pones tú mediante extensiones.

### Cómo se usa

1. Se instala la APK de la entrega `v2.3.12` (7 de noviembre de 2026) o una compilación nightly más reciente si se quiere probar lo último en desarrollo.
2. Se abre *Más → Ajustes → Explorar → Repositorio de extensiones* y se pega el índice de una fuente, por ejemplo Keiyoushi (más de 1500 extensiones) o FelipeGFA (enfoque en español: `https://raw.githubusercontent.com/FelipeFGA/anime-extensoes/repo/index.min.json`).
3. Se instalan las extensiones que interesen y aparecen como fuentes en *Examinar*.
4. Para configurar OCR local, superresolución de vídeo (Anime4K / NCNN) y sincronización WebDAV o Google Drive, se va a *Ajustes* y se activan los módulos correspondientes.

### Lo que conviene saber antes

- Entre junio y noviembre de 2026, Kototoro pasó de la v1.4.x a la v2.3.12 con siete versiones intermedias. Los cambios incluyen mejoras de seguridad en copias de seguridad, gestión de extensiones duplicadas, caché de miniaturas ajustable y soporte para abrir fuentes de novelas en el navegador para superar Cloudflare.
- Las compilaciones nightly se publican casi a diario (nightly-20261101 a nightly-20261106 confirmadas). Están firmadas por GitHub pero son para usuarios avanzados: contienen cambios no aún estables.
- El sistema de backups interoperables permite importar y exportar copias de seguridad con Mihon y Aniyomi, incluyendo mapeo inteligente de IDs de entidad y protección contra colisiones de contenido.

### Cuándo no vale la pena

Si solo quieres leer manga y nada más, Mihon o Komikku son más ligeros y simples. Si no quieres configurar extensiones ni gestionar fuentes, esta app te quedará grande. Y si buscas algo que «venga con contenido dentro», no es para ti: todo lo que lees depende de las extensiones que instales.

<!-- GUIA:FIN -->
