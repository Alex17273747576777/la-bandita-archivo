# Shizuku-API · RikkaApps

*The API and the developer guide for Shizuku and Sui.*

**Racimo:** shizuku-y-herederos · **Repositorio:** `RikkaApps/Shizuku-API` · **Estado:** parado · **Medido:** 2026-11-05 11:40 UTC

## Qué es, según quien lo hace

> Shizuku API is the API provided by Shizuku and Sui. With Shizuku API, you can call your Java/JNI code with root/shell (ADB) identity.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** parado · último empujón el 29 de mayo de 2025 (hace 525 días)
- **Estrellas:** 2.745 · 1309 bifurcaciones · 371 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Java · creado el 12 de enero de 2021
- **Última entrega:** `v12.1.0` del 7 de octubre de 2022 · 0 adjuntos
- **Plataformas que menciona su README:** Android, Linux, Web
- **Lo que dice su propio texto:** pide root, pide shizuku, pide magisk, soporte negado
- **Medido:** 2026-11-05 11:40 UTC

## Cómo se consigue

- To use Shizuku APIs, you need to guide the user to install Shizuku or Sui first. Both of them require Android 6.0+.
- I really want to drop pre-v11 support since a possible system issue that may cause system soft reboot (system server crash) on uninstalling Shizuku.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/RikkaApps/Shizuku-API
- la última entrega: https://github.com/RikkaApps/Shizuku-API/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

No es una aplicación: es la documentación y la librería para quien escribe apps que quieren usar los
permisos que da Shizuku o Sui. Si lo que quieres es usar el teléfono, esto no te sirve; si lo que
quieres es programar contra él, es el punto de partida y el único sitio donde están las reglas.

### Qué hay dentro

La guía para desarrolladores —cómo se pide el permiso, cómo se llama al código con identidad de shell
o de root, qué se puede y qué no— y las dependencias que se añaden al proyecto. La licencia es MIT, la
más permisiva de la familia, y eso importa si vas a publicar algo cerrado encima.

### Lo que conviene saber antes

Las entregas etiquetadas del repositorio son viejas —la última, de 2022— porque la librería se
publica por el repositorio de artefactos y no por entregas de GitHub: la fecha de la entrega engaña y
la del empujón, mayo de 2025, es la que vale. Es el caso típico de ficha que una lista de enlaces no
puede contar.

### Cuándo no vale la pena

Si solo quieres instalar una app que use Shizuku, esto te sobra por completo: instala Shizuku y la app.

<!-- GUIA:FIN -->
