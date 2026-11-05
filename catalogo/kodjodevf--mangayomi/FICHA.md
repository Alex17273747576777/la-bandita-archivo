# mangayomi · kodjodevf

*Free and open source application for reading manga, novels, and watching animes available on Android, iOS, macOS, Linux and Windows*

**Racimo:** tiendas-de-extensiones · **Repositorio:** `kodjodevf/mangayomi` · **Estado:** vivo · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> Mangayomi is an open-source Flutter app for reading manga, novels, and watching animes across multiple platforms. </div

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 3 de noviembre de 2026 (hace 2 días)
- **Estrellas:** 4.375 · 191 bifurcaciones · 66 incidencias abiertas
- **Licencia:** Apache-2.0
- **Lenguaje:** Dart · creado el 3 de abril de 2023
- **Última entrega:** `v0.9.95` del 1 de noviembre de 2026 · 14 adjuntos
- **Plataformas que menciona su README:** iOS, Web
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- Flutter SDK
- and Rust toolchain
- installed on your system.
- Note that all the Flutter subcomponents should be installed.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/kodjodevf/mangayomi
- la última entrega: https://github.com/kodjodevf/mangayomi/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
### Para qué sirve

Aplicación de lectura y visionado hecha en Flutter que va más allá de Android: lee manga, lee novelas y ve
anime, y corre en móvil, escritorio y navegador. Las extensiones son **scripts en JavaScript**, no paquetes
compilados, y eso cambia la forma de instalarlas y de arreglarlas.

### Cómo se usa

1. Se instala desde las entregas: la última es la `v0.9.95`, del 1 de noviembre de 2026, con 14 adjuntos para
   distintas plataformas.
2. En *Ajustes → Extensiones* se añade la dirección de un índice.
3. Se instalan las fuentes; cada una se ejecuta como script dentro de la app.
4. La biblioteca queda en local, con copia de seguridad manual.

### Lo que conviene saber antes

4.375 estrellas, Apache-2.0, Dart, creado en abril de 2023, con 191 bifurcaciones, 66 incidencias abiertas y
movimiento de ayer. Sigue en versión 0.9: después de tres años, el proyecto no se ha declarado estable.

La decisión de usar JavaScript tiene una consecuencia que se nota: las extensiones se pueden escribir y probar
sin compilar un APK, y por eso hay varias personas manteniendo índices a la vez. La otra cara es que un script
con un fallo deja la fuente muerta sin más aviso que el error.

### Cuándo no vale la pena

Si solo usas Android y te basta un lector de manga, Mihon tiene un ecosistema mucho más grande. Mangayomi se
elige cuando importa leer en escritorio o en el navegador con la misma biblioteca.
<!-- GUIA:FIN -->
