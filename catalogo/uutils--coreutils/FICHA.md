# coreutils · uutils

*Cross-platform Rust rewrite of the GNU coreutils*

**Racimo:** torrentes · **Repositorio:** `uutils/coreutils` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust. While all programs have been implemented, some options might be missing or different behavior might be experienced.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 24.331 · 2153 bifurcaciones · 1410 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Rust · creado el 2 de agosto de 2013
- **Última entrega:** `0.12.0` del 17 de septiembre de 2026 · 15 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- installing anything.
- and `libclang` are installed on your system. Then, run the following command:
- Installation
- Install with Cargo

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/uutils/coreutils
- su web: https://uutils.org
- la última entrega: https://github.com/uutils/coreutils/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Reescritura en Rust de las utilidades básicas de Unix: `ls`, `cp`, `mv`, `cat`, `sort`, `sha256sum`, `date` y
unas ochenta más. Nació para tener un conjunto de herramientas portátil y rápido, y hoy es una pieza que se usa
en Windows para darle un entorno parecido al de Unix.

En este racimo aparece por una razón concreta: **`sha256sum` y `cksum`**. Cuando hay que comprobar muchos
archivos a la vez, estas son las que se usan.

### Cómo se usa

1. Se instala con Cargo: `cargo install coreutils`; o desde los paquetes del sistema, que en varias
   distribuciones ya lo ofrecen como alternativa.
2. Se invocan igual que sus equivalentes de siempre: los nombres son los mismos.
3. Para comprobar una lista de huellas: `sha256sum -c lista.sha256`.
4. En Windows se añade su carpeta al `PATH` para tener los comandos a mano.

### Lo que conviene saber antes

24.331 estrellas, MIT, Rust, creado en 2013, con 2.153 bifurcaciones y 1.410 incidencias abiertas. Su entrega
`0.12.0` es del 17 de septiembre de 2026, trece años después de empezar: el proyecto avanza despacio a
propósito, porque aquí un error de `rm` cuesta caro.

Y eso es justo lo que hay que decir con claridad: **el propio proyecto avisa de que algunos programas y opciones
no se comportan exactamente igual que los originales**. Para un script de producción que depende de un detalle
raro de GNU, la diferencia puede importar.

### Cuándo no vale la pena

En Linux, macOS o cualquier Unix ya tienes estas herramientas funcionando desde el primer arranque. Sustituirlas
por estas solo tiene sentido si buscas la versión en Rust por velocidad, o si estás en Windows y quieres los
comandos de siempre.

<!-- GUIA:FIN -->
