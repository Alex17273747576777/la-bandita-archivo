# Capítulo 10 · El taller

## Qué vas a poder hacer al terminar

Tener a mano las herramientas con las que se hace todo lo que esta guía estuvo haciendo de refilón desde el capítulo 1: una terminal en el bolsillo, el teléfono manejado desde la computadora con teclado y mouse, un programa que abre una aplicación y te deja leer su código, y dos que te conectan a tus servidores para administrarlos desde donde estés.

Y algo que no es una herramienta sino una costumbre: vas a saber **dónde mirar cuando algo no funciona**, sin reinstalar, sin reiniciar y sin preguntar en un grupo a ver si a alguien le pasó.

## La regla que ordena el capítulo: lo que se puede leer, se puede arreglar

Todo lo que se hizo en los nueve capítulos anteriores —comprobar una firma, ver qué empresa habla con una aplicación, revisar si un servidor responde, saber qué paquete se desactivó— se hizo con una orden escrita. El taller es tener esas órdenes a mano y saber leer lo que contestan.

De ahí sale la regla: **frente a una pantalla que dice «no se pudo», siempre hay una orden que dice por qué.** El taller es la diferencia entre adivinar y mirar.

Y una segunda regla, que ahorra años: **el taller se monta una vez**. Instalás una terminal, un programa de control remoto y un cliente de servidores; con eso resolvés el noventa por ciento de lo que va a pasar de aquí en adelante. No se instala una herramienta por problema.

## La ruta de decisión, en cuatro preguntas

**Si querés una terminal de verdad en el teléfono** → **Termux**. Es un entorno Linux completo con su propio gestor de paquetes, y sirve para lo que sirve cualquier terminal: mirar, mover, automatizar y conectarse.

**Si querés manejar el teléfono desde la computadora** —escribir rápido, copiar y pegar entre aparatos, grabar la pantalla, ver lo que pasa en el aparato de un familiar sin estar al lado— → **scrcpy**. No instala nada en el teléfono y no necesita root.

**Si querés saber qué hace una aplicación por dentro** → **jadx** para leer su código y **Apktool** para abrirla, tocar recursos y volver a cerrarla. Son las dos caras del mismo oficio: entender y desarmar.

**Si querés administrar tus servidores desde el teléfono** → **ConnectBot** para las órdenes, **Material Files** para mover archivos entre el teléfono y tus servidores propios por los protocolos de siempre.

## La terminal en el bolsillo

Termux no es un emulador ni una cárcel: es un entorno Linux con su propio prefijo de sistema, su gestor de paquetes y miles de programas compilados para teléfonos. Con él se puede hacer desde una copia cifrada hasta un servidor pequeño, pasando por scripts que ordenan fotos.

Tres cosas hay que saber antes de instalarlo, y las tres están en su propio repositorio:

- **Viene de su repositorio o de F-Droid, no de la tienda de Google.** La versión de la tienda quedó abandonada hace años y su política es incompatible con cómo funciona esta terminal.
- **Android 12 y posteriores matan procesos.** El sistema limita los procesos fantasma a treinta y dos en total entre todas las aplicaciones y además mata los que consumen mucha batería. Un script largo puede morir a mitad de camino, y no es un fallo de la terminal: es el sistema administrando el aparato.
- **Su sistema de archivos no es el de Linux de escritorio.** Los binarios y las librerías viven bajo su propio prefijo, y una orden escrita para una computadora puede no encontrarlos. Por eso los tutoriales de servidores no se copian tal cual.

Con eso claro, la terminal hace algo que ninguna aplicación hace: **te devuelve el control de lo repetitivo**. Un script de diez líneas que ordena las fotos por fecha vale más que diez aplicaciones.

## El teléfono en la pantalla grande

**scrcpy** muestra la pantalla del teléfono en la computadora y deja manejarla con teclado y mouse. No instala nada en el aparato, no pide root y no necesita internet: es la misma conexión de depuración que se explicó en el capítulo 3, aprovechada al máximo.

Sus números son los más altos de toda la guía: **ciento cincuenta y tres mil novecientas treinta y seis estrellas** y casi diez millones de descargas en sus diez últimas entregas. No es casual: resuelve un problema que todos tienen —escribir en un teléfono con el teclado de una computadora— y lo resuelve sin dejar rastro.

Y su repositorio abre con una advertencia que vale para todo lo demás: **es la única fuente oficial**; no se bajan sus archivos de sitios que llevan su nombre. Un programa popular y libre tiene copias falsas en la primera página de cualquier buscador, y eso incluye a cualquiera de las fichas de esta guía.

## Leer un binario: la diferencia entre ver y desarmar

Acá el capítulo se pone serio, y conviene entender dos herramientas que se confunden todo el tiempo.

**jadx lee.** Toma un paquete, traduce el código compilado a algo parecido a Java y lo muestra en pantalla con búsqueda y navegación. Es la herramienta con la que se responde: «¿esta aplicación manda datos a algún sitio?», «¿a qué dominio llama cuando arranco?», «¿qué permiso pide y para qué?». Su propio repositorio avisa que **no siempre puede con todo**: hay código que no se puede reconstruir con exactitud, y en esos casos muestra errores. Eso no es un defecto: es la naturaleza del oficio, y saberlo evita conclusiones falsas.

**Apktool abre y vuelve a cerrar.** Decodifica los recursos —textos, imágenes, diseños, el manifiesto— a una forma casi original, deja modificarlos y reconstruye el paquete. Es la herramienta del que traduce una aplicación o le añade algo, y su presentación dice con claridad que **no es para piratear**.

Las dos juntas dan lo que ningún análisis de tienda puede dar: la capacidad de mirar por dentro y decidir con evidencia. Y las dos tienen la misma consecuencia al final, que ya se explicó en el capítulo 4: un paquete reconstruido lleva otra firma, y Android lo tratará como un programa distinto.

## Las cinco órdenes que valen un curso

Si te llevás algo de este capítulo, que sea esto. Con estas cinco se diagnostica casi todo.

**Ver qué está pasando ahora mismo en el aparato:**

```
adb logcat -d | tail -200
```

**Saber quién instaló una aplicación y cuándo:**

```
adb shell dumpsys package com.ejemplo.app | grep -iE "installerPackageName|lastUpdateTime"
```

**Saber dónde viven los archivos de una aplicación y si está partida:**

```
adb shell pm path com.ejemplo.app
```

**Listar lo que está desactivado, para saber qué se puede devolver:**

```
adb shell pm list packages -d
```

**Ver la batería por aplicación, que es donde miente el sentido común:**

```
adb shell dumpsys batterystats --charged | grep -A5 "Estimated power"
```

Cinco órdenes, ninguna necesita root, todas contestan una pregunta concreta. Un taller es eso.

## Los cuatro errores que se pagan

**Instalar la terminal desde una tienda cualquiera.** Además de la versión abandonada de Google, hay copias empaquetadas por terceros. La regla del capítulo 4 se aplica igual: se baja del repositorio de quien lo hizo y se comprueba.

**Copiar un tutorial de servidor sin mirar la ruta.** Las rutas de una terminal de teléfono no son las de una computadora; un script que escribe en `/etc` va a fallar siempre, y no por el script.

**Modificar una aplicación y esperar que se actualice.** Al reconstruir, la firma cambia: la aplicación modificada vive aparte y nunca se actualiza encima de la original. Es el precio del taller, y hay que saberlo antes, no después.

**Usar el taller para lo que no es.** Desarmar una aplicación propia para traducirla o para entender un fallo es oficio. Desarmar la de otro para saltarse un pago es lo que el propio Apktool pide no hacer, y esta guía tampoco.

## Tres cosas que se dicen y no son verdad

**«La depuración es solo para desarrolladores».** Es la puerta por la que pasa todo lo de esta guía, desde quitar publicidad hasta hacer una copia. Lo que hay que hacer es cerrarla al terminar.

**«Con root el taller es mejor».** Root añade herramientas y quita garantías. La mayor parte del taller de este capítulo funciona sin él, y lo que no funciona sin root se puede resolver con la depuración del capítulo 3 en la mayoría de los casos.

**«Si el teléfono va lento, hay que reinstalar».** Casi siempre hay una aplicación despertando el aparato cada minuto, y se ve en el registro. Reinstalar es lo que se hace cuando ya se miró y no se encontró; no antes.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca abrió una terminal: si consigue ver la pantalla de su teléfono en la computadora y copiar un texto de una a otra con el teclado, el capítulo sirve.

Y dalo a alguien que administra servidores: si no encuentra al menos un dato que no supiera —que Termux vive en un prefijo propio y no en las rutas de Linux, que Android 12 mata los procesos fantasma por encima de treinta y dos, que jadx no reconstruye todo el código y lo dice en su presentación, que al reconstruir con Apktool la firma cambia y la aplicación deja de actualizarse, que scrcpy no instala nada en el aparato—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Van de la más simple a la más honda: el teléfono en la pantalla grande, la terminal, el cliente de servidores, el gestor de archivos remoto, y al final las dos que abren binarios. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas y sus licencias.
