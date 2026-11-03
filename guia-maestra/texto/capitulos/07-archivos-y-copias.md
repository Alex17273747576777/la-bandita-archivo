# Capítulo 7 · Archivos, copias y nubes propias

## Qué vas a poder hacer al terminar

Pasar un archivo de un aparato a otro sin intermediarios, mantener dos aparatos sincronizados sin pagar nube, tener tus fotos en un servidor que es tuyo y tener una copia de todo que sobreviva a un disco roto, a un teléfono perdido y a un error tuyo.

Y vas a poder responder, sin dudar, la pregunta que decide todo este capítulo: **¿en qué se diferencia sincronizar de respaldar?** Casi todo el mundo usa las dos palabras como si fueran la misma cosa, y esa confusión es la causa de la mitad de los archivos perdidos que la gente cuenta en los grupos. Al final del capítulo la diferencia va a estar clara, con una prueba de un minuto que la demuestra.

## La regla que ordena el capítulo: tres copias, dos medios, una fuera

La regla vieja de la informática —tres copias, en dos medios distintos, con una fuera de tu casa— sigue siendo la mejor que existe, y sirve igual para un teléfono que para un servidor.

Traducida a la vida real: tus fotos están en el teléfono y en un disco; los documentos están en la computadora y en una copia cifrada en otro sitio; y si el teléfono se cae al agua mientras el disco está conectado a la misma regleta, no perdiste nada. No hace falta un servidor para cumplirlo: hace falta tenerlo pensado una vez.

Y hay una segunda regla, más chica y más olvidada: **un respaldo que no se probó restaurar no es un respaldo, es una intención**. Cada ficha de este capítulo trae su manera de probarlo.

## La distinción que decide todo: sincronizar no es respaldar

**Sincronizar copia los cambios, incluidos los borrados.** Si en el teléfono borrás una carpeta por error, el otro aparato la borra también, porque su trabajo es que los dos estén iguales. Si el aparato que sincroniza tiene papelera, tenés unos días para recuperarla; si no, se fue.

**Respaldar guarda estados anteriores.** Un respaldo conserva versiones: la foto que borraste el martes sigue en el respaldo del lunes. Su trabajo no es que dos aparatos sean iguales, sino que lo que existía siga existiendo.

De ahí sale la combinación honesta, la que usan quienes nunca perdieron nada: **sincronizar para trabajar, respaldar para dormir**. Syncthing para tener los mismos documentos en el teléfono y en la computadora; restic para que dentro de un año siga existiendo lo que hoy borraste sin pensar.

La prueba de un minuto que demuestra la diferencia: creá un archivo en una carpeta sincronizada, esperá a que aparezca en el otro aparato, borralo, y mirá cómo desaparece de los dos. Después buscá ese archivo en tu respaldo. Si está, tenés las dos cosas; si no está en ninguno de los dos, sólo tenías sincronización y la creías respaldo.

## La ruta de decisión, en cuatro preguntas

**Si lo que querés es pasar un archivo ahora, de este teléfono a esta computadora** → **LocalSend**. Sin cuenta, sin servidor, sin internet: los dos aparatos en la misma red y listo. Es la ficha por la que empieza todo el mundo.

**Si querés que dos aparatos tengan siempre lo mismo** → **Syncthing**, envuelto en su versión para Android. No hay nube de por medio: los aparatos hablan entre ellos, cifrado, y los datos no pasan por ningún servidor ajeno.

**Si lo tuyo son las fotos y los vídeos** → **Immich**. Es un servidor propio de fotos, con aplicación de teléfono que sube automáticamente y reconoce caras y lugares sin mandar nada a internet. Y su propia documentación avisa lo que esta guía repite: no es un respaldo, es la biblioteca.

**Si querés una nube entera —archivos, calendario, contactos, notas, tareas— en tu casa** → **Nextcloud**. Es la pieza más grande de este capítulo y la que más mantenimiento pide.

Y para el final, las dos herramientas que hacen el trabajo invisible: **restic** para la copia que se verifica, y **rclone** para conectar todo eso con las nubes que ya usás, sin depender de ellas.

## Qué hay que tener antes de empezar

Tres cosas, ninguna técnica.

**Un lugar donde guardar.** Un disco externo conectado a la computadora, o mejor un equipo pequeño siempre encendido. Un pendrive sirve para empezar y no sirve para vivir: se pierde, se rompe y nadie lo recuerda.

**Un mapa de qué tenés.** Antes de copiar nada, mirá tus carpetas y decí en voz alta qué se pierde si mañana no está: las fotos, los documentos, las notas, las conversaciones que exportaste, las claves. Lo demás es reemplazable.

**Una decisión sobre el cifrado.** Si el disco se pierde o te lo roban, ¿querés que lo que hay adentro sea legible? Si la respuesta es no, hay que cifrar —y eso significa que la contraseña pasa a ser la cosa más importante de todo el sistema—. Las dos fichas del final, restic y rclone, cifran por diseño.

## El árbol que hace que todo funcione

Casi todos los problemas de este capítulo se resuelven con una estructura de carpetas aburrida y estable. Un ejemplo que sirve para teléfono, computadora y servidor a la vez:

- `Fotos` — sólo fotos y vídeos, un archivo por imagen, sin subcarpetas inventadas por una aplicación.
- `Documentos` — lo que abrís y editás: textos, hojas de cálculo, PDF importantes.
- `Libros` — lo del capítulo 6.
- `Música` — lo del capítulo 6.
- `Copias` — lo que generan las herramientas de respaldo, fuera de las carpetas que se sincronizan.

La regla de oro: **una carpeta que se sincroniza nunca contiene a otra que se respalda**. Si el respaldo vive dentro de lo que sincronizás, el respaldo viaja, se duplica y se corrompe, y encima ocupa el doble.

## Las nubes ajenas: cómo usarlas sin depender de ellas

Tener una nube propia no obliga a renunciar a las ajenas. Obliga a cambiar de lugar la confianza: en lugar de subir archivos a ciegas, se suben **cifrados**, y la llave se queda en casa.

**rclone** es el programa que habla con casi todas las nubes comerciales desde una consola, y trae una capa que se llama `crypt`: lo que se sube va cifrado y con los nombres de archivo también cifrados. Para la nube, son archivos incomprensibles; para vos, son tus carpetas de siempre.

Y hay una comprobación que casi nadie hace y que cambia la conversación: **comparar sumas entre el origen y el destino**. Subir no es lo mismo que haber subido bien. rclone lo hace con una orden, y esa orden es la diferencia entre creer que el archivo está arriba y saberlo.

## Los cuatro errores que se pagan

**Respaldar dentro del mismo disco.** El respaldo en la misma máquina protege del error humano y no protege de la avería, del robo ni del incendio. Tiene que salir del aparato.

**Cifrar y no guardar la contraseña en dos sitios.** Una copia cifrada con la contraseña perdida es basura perfectamente segura. La contraseña se guarda escrita, en dos lugares físicos distintos, y se le dice a una persona de confianza que existe.

**Confiar en la sincronización como copia de seguridad.** Es el error más caro y más común: el borrado se propaga en segundos a todos los aparatos. Papelera del sistema, si existe, y respaldo aparte.

**Nunca haber restaurado.** Un respaldo que nunca se abrió puede llevar meses roto: un disco a medio escribir, una carpeta excluida por error, una contraseña que ya no es la que era. Se prueba restaurar algo pequeño, cada tanto, sin urgencia.

## Tres cosas que se dicen y no son verdad

**«La nube es más segura que mi casa».** La nube de una empresa grande tiene mejor disponibilidad que tu disco, y eso es verdad. También tiene tus archivos en un formato que no controlás, sujeto a sus condiciones, y con un candado legal en otro país. Las dos cosas pueden ser ciertas a la vez: por eso se combinan, no se eligen.

**«Si lo tengo en el teléfono, lo tengo».** El teléfono es el aparato que más se rompe, se pierde y se roba de todos los que tenés. Es el peor lugar del mundo para la única copia de algo.

**«Sincronizar ya es respaldar».** No. Ya está explicado arriba y lo vas a poder demostrar en un minuto con un archivo y un borrado.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca hizo una copia: si consigue pasar una foto del teléfono a la computadora con LocalSend y programar una copia semanal que se note cuando falla, el capítulo sirve.

Y dalo a alguien que administra servidores desde hace años: si no encuentra al menos un dato que no supiera —que la aplicación oficial de Syncthing para Android está archivada desde diciembre de 2024 y la comunidad continúa en una bifurcación viva, que Immich deduplica por suma y por eso dos copias de la misma foto ocupan una, que `restic check` sin opciones no lee los datos y por eso no detecta un disco que se corrompe, que Nextcloud necesita escanear la carpeta para ver lo que copiaste a mano—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Las que siguen van en el orden en que se necesita: pasar, sincronizar, tener fotos, tener nube, respaldar de verdad y conectar con lo ajeno. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas y leyendo lo que publican, no repitiendo lo que dice un catálogo.
