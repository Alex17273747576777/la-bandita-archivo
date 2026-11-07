# android-keyboard · futo-org

*Official FUTO Keyboard Issue Tracker and Source Mirror of https://gitlab.futo.org/keyboard/latinime*

**Racimo:** teclados-con-ia · **Repositorio:** `futo-org/android-keyboard` · **Estado:** vivo · **Medido:** 2026-11-05 11:45 UTC

## Qué es, según quien lo hace

> The goal is to make a good modern keyboard that stays offline and doesn't spy on you. This keyboard is a fork of LatinIME, The Android Open-Source Keyboard, with significant changes made to it.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 2 de noviembre de 2026 (hace 3 días)
- **Estrellas:** 3.440 · 298 bifurcaciones · 809 incidencias abiertas
- **Licencia:** NOASSERTION
- **Lenguaje:** C++ · creado el 7 de mayo de 2024
- **Última entrega:** `0.1.30` del 4 de agosto de 2026 · 1 adjuntos
- **Plataformas que menciona su README:** Android
- **Lo que dice su propio texto:** espejo declarado
- **Medido:** 2026-11-05 11:45 UTC

## Cómo se consigue

- Check out the FUTO Keyboard website for downloads and more information.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/futo-org/android-keyboard
- su web: https://keyboard.futo.org/
- la última entrega: https://github.com/futo-org/android-keyboard/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Teclado de Android con el objetivo declarado de **quedarse sin conexión**: corrección, predicción y dictado de
voz en el propio teléfono, sin enviar lo que escribes ni lo que dices a ningún servidor. Es un derivado del
teclado de código abierto de Android, LatinIME, con cambios profundos.

El dictado es la parte que lo distingue: reconocimiento de voz local, que es justo lo que casi todos los
teclados resuelven mandando el audio fuera.

### Cómo se usa

1. Se descarga desde la web del proyecto; en este repositorio está el seguimiento de incidencias y un espejo
   del código.
2. Se instala y se activa como método de entrada.
3. Se descarga el paquete de idioma del dictado, que ocupa bastante y se ejecuta en local.
4. Se desactivan los permisos de red si se quiere comprobar que, en efecto, no los usa.

### Lo que conviene saber antes

3.440 estrellas, creado en mayo de 2024, con 298 bifurcaciones y **809 incidencias abiertas**: es la ficha del
racimo con más cola de trabajo. La licencia no la reconoce GitHub como estándar —aparece como `NOASSERTION`—,
así que conviene leer los términos en su propio repositorio antes de reutilizar nada.

El medidor marcó la bandera de espejo, y es correcta: el código se desarrolla en otro sitio y aquí solo se
publica una copia. Eso significa que la actividad de este repositorio no mide la del proyecto.

### Cuándo no vale la pena

Si dictas poco, el peso del paquete de voz no se justifica. Y si necesitas teclados en muchos idiomas con
corrección fina, la cobertura por idioma de un proyecto joven se queda corta.

<!-- GUIA:FIN -->
