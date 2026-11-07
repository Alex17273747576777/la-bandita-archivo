# extensions-source · keiyoushi

*Source code of extensions in https://github.com/keiyoushi/extensions*

**Racimo:** tiendas-de-extensiones · **Repositorio:** `keiyoushi/extensions-source` · **Estado:** vivo · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> You can add our repo by visiting the Keiyoushi Website Otherwise, copy & paste the following URL: https://github.com/keiyoushi/extensions/raw/repo/index.pb

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 5 de noviembre de 2026 (hace 0 días)
- **Estrellas:** 4.865 · 1819 bifurcaciones · 473 incidencias abiertas
- **Licencia:** Apache-2.0
- **Lenguaje:** Kotlin · creado el 8 de enero de 2024
- **Última entrega:** sin entregas etiquetadas
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega. Su web: https://keiyoushi.github.io/.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/keiyoushi/extensions-source
- su web: https://keiyoushi.github.io/

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

El código de las extensiones del índice anterior: una extensión por carpeta, cada una con su analizador de la
web correspondiente. Sirve para tres cosas muy concretas: entender cómo está hecha una extensión, arreglar una
que se rompió y escribir una nueva.

### Cómo se usa

1. Se clona el repositorio; es un proyecto de Gradle con muchos módulos, uno por fuente.
2. Se copia la carpeta de una extensión parecida a la que se quiere escribir y se cambian el nombre, el dominio
   y las reglas de extracción.
3. Se compila solo ese módulo, se prueba contra la web real y se instala el paquete resultante.
4. Para aportarlo, se abre una petición con el módulo nuevo y se acepta la guía de estilo del proyecto.

### Lo que conviene saber antes

4.865 estrellas, Apache-2.0, Kotlin, creado en enero de 2024, con 473 incidencias abiertas y movimiento de hoy.
No tiene entregas etiquetadas: aquí no se viene a descargar nada, se viene a compilar.

El trabajo real no es programar, es **leer la web del otro lado**: cada fuente es un analizador que se rompe
cuando esa web cambia. Por eso hay tantas incidencias abiertas y por eso una extensión que hoy funciona puede
no funcionar en tres semanas.

### Cuándo no vale la pena

Si solo quieres leer, este repositorio no te da nada que puedas usar directamente. Y si esperas una extensión
para un sitio muy pequeño, lo más probable es que nadie la haya escrito ni la vaya a escribir.

<!-- GUIA:FIN -->
