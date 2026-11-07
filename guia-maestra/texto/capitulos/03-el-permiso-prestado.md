# Capítulo 3 · El permiso prestado

## Qué vas a poder hacer al terminar

Conceder a tus aplicaciones el permiso que les permite ordenar el sistema sin rootear el teléfono, comprobar que de verdad lo tienen, saber cuándo se pierde y recuperarlo sin desinstalar nada. Y algo más importante: distinguir un programa que usa ese permiso para una tarea concreta de una copia que se disfraza de programa.

Al final del capítulo hay seis fichas, cada una con sus pasos, con lo que hay que saber por dentro y con un dato de oficio que puedes comprobar tú mismo en un minuto.

## Antes de empezar: tres cosas que conviene tener claras

**No hace falta root.** Casi todo lo que la gente quiere hacer con root —apagar publicidad del sistema, quitar aplicaciones de fábrica, ordenar permisos— se puede hacer con un permiso que el propio Android ofrece y que se concede desde los ajustes. No rompe la garantía del aparato y se revoca reiniciando el teléfono.

**El permiso es una sesión, no una propiedad.** Vivirá mientras la sesión de depuración esté abierta. Si el teléfono se reinicia, la sesión se cierra y el permiso se pierde hasta que se vuelve a conceder. Eso no es un fallo: es exactamente lo que el sistema está protegiendo, y es la razón de que esta vía sea más segura que root.

**El permiso se concede por aplicación, una por una.** No es una llave maestra del teléfono. Cada programa que lo pide aparece con su nombre en una ventana de autorización, y esa ventana es la última frontera entre tu teléfono y una aplicación que llegó por un enlace.

## La ruta de decisión, en tres preguntas

**Si es la primera vez y solo quieres quitar las aplicaciones que te metieron** → ve directo a la ficha de **Shizuku** para conceder el permiso y sigue con **Shevery** para usarlo. Con eso cubres el noventa por ciento de los casos.

**Si quieres poder escribir órdenes y ver lo que hacés** → **aShellYou**, después de haber concedido el permiso. Es la ficha marcada como experto, y con razón.

**Si administras un teléfono dedicado —un quiosco, un aparato de la casa, el de un familiar** → **Dhizuku**. Es otro permiso, más fuerte y más difícil de deshacer; se explica más abajo para que no se confunda con el de depuración.

## Qué es exactamente el permiso

Android dejó una puerta abierta para quien configura el aparato desde una computadora: la depuración por USB o por red. Por esa puerta, una computadora puede dar órdenes al teléfono con un usuario especial que tiene más poder que una aplicación normal y menos que root.

La idea de estos programas es ocupar el lugar de la computadora. En lugar de conectar el teléfono al ordenador cada vez, se le pide a una aplicación que haga de puente: el teléfono autoriza a esa aplicación una vez, y desde entonces ella reparte el acceso a las demás que se lo pidan, con tu visto bueno en cada una.

Con ese permiso se puede congelar una aplicación, desinstalarla para tu usuario, leer qué permisos tiene concedidos, cambiar ajustes del sistema y ejecutar las mismas órdenes que escribirías en una consola. Lo que no se puede es tocar los archivos de otra aplicación ni alcanzar el sistema de raíz.

## Los cuatro límites que hay que aceptar

**Uno. Se pierde al reiniciar.** En Android 11 o superior, si la depuración inalámbrica queda activada, la sesión puede reabrirse sola; en versiones anteriores hay que emparejar otra vez. Ninguna aplicación arregla eso, porque no está roto: es el diseño.

**Dos. Cambia con la red.** El emparejamiento inalámbrico abre un puerto en tu red local. Si cambias de red —de la casa a la oficina, o a datos móviles— ese puerto ya no sirve y la sesión cae aunque la depuración siga activada.

**Tres. No es un permiso global.** Que una aplicación lo tenga no implica que las demás lo tengan. Cada una se autoriza aparte, y retirárselo a una no afecta a las otras.

**Cuatro. El aparato tiene que dejarte.** Algunos fabricantes esconden las opciones de desarrollador o bloquean la depuración inalámbrica. Si es tu caso, no hay truco: este camino no está disponible en ese teléfono

## Cómo se comprueba que funciona

No confíes en la pantalla de la aplicación: comprueba el sistema. Abre una consola con el permiso activo y ejecuta:

```
pm list packages -3
```

Esa orden lista las aplicaciones instaladas por ti, no las del sistema. Si responde con una lista, el permiso está funcionando. Si responde «Permission denied», no lo está, por mucho que la aplicación diga lo contrario.

Para ver qué permisos tiene una aplicación concreta:

```
dumpsys package com.ejemplo.app | grep -i -A2 granted
```

Y para saber qué has congelado, que es lo que casi nadie sabe:

```
pm list packages -d
```

## Los dos perjuicios que se cometen con este permiso

**Dar el permiso a cualquier cosa.** Un paquete que llegó por un enlace de un grupo puede hacer con ese permiso lo mismo que harías tú: desinstalar, congelar, leer ajustes. La regla no es de esta guía, es de sentido común: el permiso se le da al programa cuyo código se puede leer, no al que llegó con prisa.

**Congelar sin anotar el nombre del paquete.** Si congelas el lanzador o el teclado, el teléfono se queda sin interfaz. Y sin el nombre exacto, que es un texto como `com.ejemplo.app`, no hay manera de revertirlo desde fuera. Anótalo antes de tocar, siempre.

## Lo que no hay que creer

**«Con esto se puede hacer todo lo que hace root».** No. Hay cosas que solo root permite, y las aplicaciones serias de este ecosistema no las prometen. Cuando una lo promete, es una señal para mirar el código, no para instalarlo.

**«El proyecto más famoso es el más seguro».** El que abrió esta puerta —y que va primero en las fichas porque todo lo demás depende de él— tiene treinta y dos mil setecientas veintiuna estrellas, casi cinco millones de descargas y quinientos tres días sin que nadie empuje su código. Su contrato, el documento que los demás usan para hablarle al sistema, no se toca desde octubre de 2022. Está medido y fechado.

**«Si tiene muchas estrellas, está mantenido». Y al revés.** En esta guía hay un derivado de diecisiete estrellas que saca mejor nota que otro de mil seiscientas ochenta. La nota mide cómo se publica —con huellas, con compilación automática, con la cola de incidencias atendida, con entregas fechadas— y no cuánta gente lo bajó.

## El error que se paga caro: confundir los dos permisos

El permiso de depuración se concede y se revoca con facilidad. El permiso de **dueño del aparato** —el que se usa para configurar teléfonos de empresa o de quiosco— no: impone políticas, sobrevive a los reinicios y, mal aplicado, deja un aparato bloqueado. Dhizuku reparte ese segundo permiso, y su ficha lo dice con todas las letras: es para aparatos dedicados, no para el teléfono personal.

## Antes de irte: la prueba de las dos personas

Este capítulo está escrito para que lo entiendan dos personas distintas, y se comprueba así. Dale el capítulo a alguien que nunca ha hecho esto: si consigue el permiso activo en menos de veinte minutos sin ayuda, el capítulo sirve. Y dáselo a alguien que lleva años trasteando: si no encuentra al menos un dato que no supiera —el del puerto que cambia con la red, el de la desinstalación que se deshace con una orden, el de la proporción entre cambios y personas—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Las que siguen están ordenadas por dificultad, no por fama. Cada una declara para quién es y para quién no es, y cada una trae el dato de oficio con su comando para comprobarlo. Ninguna se ha copiado de un catálogo: todas salieron de abrir sus entregas una por una, el 3 de noviembre de 2026.
