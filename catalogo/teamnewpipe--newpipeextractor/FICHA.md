# NewPipeExtractor · TeamNewPipe

*NewPipe's core library for extracting data from streaming sites*

**Racimo:** clientes-de-musica · **Repositorio:** `TeamNewPipe/NewPipeExtractor` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> NewPipe Extractor is a library for extracting things from streaming sites. It is a core component of NewPipe, but could be used independently.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 2 de noviembre de 2026 (hace 3 días)
- **Estrellas:** 2.039 · 627 bifurcaciones · 181 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Java · creado el 1 de marzo de 2017
- **Última entrega:** `v0.26.5` del 15 de agosto de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Android, Linux
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- 3. Run gradle's `ìnstall` task to deploy this library to your local repository (using the wrapper, present in the root of this project: `./gradlew install`)

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/TeamNewPipe/NewPipeExtractor
- la última entrega: https://github.com/TeamNewPipe/NewPipeExtractor/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

No es una aplicación: es la **biblioteca** que hay debajo de un conocido cliente libre de vídeo, y sirve para
sacar de un sitio de vídeos lo que hace falta para reproducirlo sin su aplicación oficial: direcciones, pistas
de audio, subtítulos y metadatos. En este racimo entra por el audio.

### Cómo se usa

1. Se incluye como dependencia en un proyecto de Java o Android; la entrega medida es la `v0.26.5`, del 15 de
agosto de 2026.
2. Desde código se pide la información de un enlace y se reciben los objetos con las pistas disponibles.
3. Hay una aplicación de prueba en el repositorio para ver qué devuelve la biblioteca sin escribir código.

### Lo que conviene saber antes

2.039 estrellas, GPL-3.0, y desarrollo vivo: su último cambio es de noviembre de 2026. La versión importa
mucho: la biblioteca se publica y los clientes se atan a una versión concreta, porque los cambios internos
rompen. Si programas un cliente, esto te ahorra la parte más frágil y más sujeta a cambios.

### Cuándo no vale la pena

Si no programas, no hay nada que hacer aquí: usa uno de los clientes que ya la llevan dentro. Esta ficha está
para entender de dónde salen y por qué se rompen a la vez varios programas cuando el sitio cambia.

<!-- GUIA:FIN -->
