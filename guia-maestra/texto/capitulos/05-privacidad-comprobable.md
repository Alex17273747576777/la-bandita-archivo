# Capítulo 5 · Privacidad que se puede comprobar

## Qué vas a poder hacer al terminar

Ver con tus ojos qué conexiones hace cada aplicación de tu teléfono, decidir cuáles se cortan y demostrar que se cortaron. Sin root, sin confiar en la palabra de nadie y sin instalar nada que pida una cuenta.

Y algo más útil que cualquier lista de consejos: vas a saber distinguir las afirmaciones de privacidad que se pueden comprobar de las que no. La mayoría de lo que se repite en los grupos —«esta aplicación no recopila datos», «este bloqueador te hace invisible», «con esto nadie te rastrea»— no es falso ni verdadero: es incomprobable. Al final del capítulo vas a poder separar las tres categorías, y a usar las herramientas que convierten una promesa en una medición.

## La regla que ordena el capítulo: lo que no se ve, no se puede afirmar

Una afirmación de privacidad sirve cuando dice **qué** se observó, **con qué** se observó y **cuándo**. «Bloqueé tres mil conexiones» es una afirmación. «Soy invisible» no lo es.

Esa regla tiene una consecuencia incómoda y liberadora a la vez: no hace falta creerle a nadie. Un bloqueador no te pide fe, te muestra un registro. Un cortafuegos no promete, cuenta. Y cuando una herramienta no puede mostrar lo que hace, no es que sea mala: es que está fuera de la categoría de lo comprobable, y entonces hay que decidir con otra información.

## La ruta de decisión, en tres preguntas

**Si querés empezar por ver, sin cortar nada** → **TrackerControl**. Instalás, dejás pasar un día normal y mirás el informe: qué aplicación habló con quién y con qué propósito declarado. Ver antes de cortar es el orden que evita romper cosas.

**Si querés cortar sin complicarte y lo que te molesta son los anuncios** → **AdAway**, que hace una sola cosa y la hace bien: mantener una lista de nombres bloqueados. Si querés además bloquear consultas y ver el registro, **personalDNSfilter**, que hace lo mismo pero te deja leer cada consulta y hasta puede servir de filtro para toda la casa.

**Si querés control fino por aplicación, con reglas que se activen según la pantalla o la red** → **Rethink** o **NetGuard**. Los dos son cortafuegos por aplicación y los dos funcionan sin root. Y si lo que querés no es bloquear sino **probar** —demostrar que una aplicación mandó datos a un servidor—, **PCAPdroid**, que captura el tráfico y lo deja en un archivo que se puede abrir en una computadora.

## El túnel único: la limitación que decide todo

Acá está el dato que explica el noventa por ciento de las consultas de este tema, y que casi nadie dice al principio.

Android permite **un solo túnel de red privada activo por usuario**. Los bloqueadores sin root funcionan creando ese túnel en el propio teléfono: el sistema les entrega el tráfico, ellos deciden qué pasa y qué se descarta. Como el sistema sólo admite uno, **dos de estas aplicaciones no pueden trabajar a la vez**. Instalás TrackerControl y AdAway, activás los dos, y el segundo apaga al primero.

De ahí salen tres consecuencias prácticas:

- **Un blocador, no cinco.** Tener instalados cuatro y activar uno es normal; tener cuatro activos es imposible.
- **La VPN de pago y el bloqueador se pelean.** Si usás un servicio de red privada para otra cosa, no puede convivir con el bloqueador salvo que el bloqueador sea también el cliente del túnel —es el caso de Rethink, que además es cliente de túneles— o que el teléfono esté rooteado y la captura se haga por fuera.
- **El aviso persistente no es un adorno.** Mientras el túnel está activo, el teléfono muestra una notificación fija y un icono de llave. Si desaparece, el bloqueo dejó de funcionar aunque la aplicación diga que está encendida. Es la comprobación más rápida que existe y la que casi nadie hace.

## Primero el nombre, después el contenido

Casi todas estas herramientas bloquean en el mismo punto: antes de que la aplicación averigüe a qué dirección tiene que conectarse. Bloquear el nombre resuelve dos problemas de un golpe —no hace falta descifrar nada, porque el tráfico está cifrado, y no hace falta una lista de direcciones, que cambian todos los días—.

Cuando una aplicación pide `telemetria.ejemplo.com`, el filtro contesta «esa dirección no existe» o le devuelve la dirección local del propio teléfono. La aplicación no distingue eso de un servidor caído, y la mayoría de las veces sigue funcionando: los anuncios no cargan y la aplicación anda igual.

Por eso el registro de consultas es también la mejor herramienta de diagnóstico que existe en esta categoría. Si querés saber qué hace una aplicación cuando la abrís, mirá su registro de nombres: ahí está la lista de empresas con las que habla, en orden y con hora.

## Dónde falla el bloqueo por nombre

Este es el punto donde la guía se separa de los folletos. El bloqueo por nombre tiene cuatro agujeros conocidos, y conviene conocerlos antes de confiar el teléfono a un solo método.

**Uno. Direcciones fijas.** Una aplicación puede traer escrita la dirección numérica de su servidor y no preguntar nunca un nombre. Contra eso no hay lista que valga, y por eso los cortafuegos por aplicación existen: cortan por aplicación aunque el destino sea una dirección cruda.

**Dos. Resolución propia.** Muchas aplicaciones ya no usan el resolutor del sistema: hablan con su propio servidor de nombres cifrado, dentro del mismo túnel, de modo que el nombre nunca aparece en claro. TrackerControl llama a esto **encubrimiento de DNS** y lo trata como una señal: una aplicación que esconde a quién le pregunta tiene algo que decir. Los cortafuegos por aplicación lo resuelven por la vía de siempre: si no dejo salir a esa aplicación, no hay nombre que esconder.

**Tres. El túnel apagado.** Si el sistema mata la aplicación o el teléfono reinicia, el túnel se cae y el bloqueo con él. La notificación persistente es el indicador; la comprobación de verdad es preguntarle al registro si sigue habiendo consultas bloqueadas hoy.

**Cuatro. La lista equivocada.** Una lista de nombres desactualizada bloquea lo que ya no molesta y deja pasar lo que sí. Las listas comunitarias se actualizan a diario; conviene revisar de dónde viene la que usás y cuándo se actualizó por última vez.

## Cifrar el DNS: contra quién protege y contra quién no

Android 9 y posteriores traen **DNS privado** en los ajustes del sistema: el teléfono cifra sus consultas de nombres hacia el resolutor que elijas. Eso significa que tu proveedor de internet deja de ver qué sitios y servicios consultás, aunque sigue viendo a qué direcciones te conectás.

La distinción importa y se repite al revés todo el tiempo. Cifrar el DNS **no** te esconde del destino: la aplicación con la que hablás sigue sabiendo que hablaste con ella. Y **no** bloquea nada: un resolutor cifrado que no filtra te devuelve todos los nombres, incluidos los de anuncios.

Hay un ajuste del sistema que permite comprobarlo en un segundo, y es de los pocos que se puede leer sin herramientas externas:

```
adb shell settings get global private_dns_mode
```

Devuelve `off`, `opportunistic` o `hostname`. En el primer caso, tus consultas van en claro. En el tercero, van cifradas —y el nombre del resolutor que uses está en la clave `private_dns_specifier`—. Ese par de claves es la diferencia entre «tengo la privacidad configurada» y «creo que la tengo configurada».

## La rutina de las cinco pruebas

Después de configurar cualquiera de estas herramientas, cinco comprobaciones separan la sensación de la certeza.

1. **La llave está.** El icono de red privada aparece en la barra de estado. Sin eso, no hay túnel.
2. **El registro crece.** Abrí la aplicación que configuraste y mirá si hay consultas nuevas con la hora de ahora.
3. **La prueba del sitio de anuncios.** Abrí una página con anuncios conocidos: si carga igual que antes, el bloqueo no está pasando por ahí.
4. **La prueba de la aplicación propia.** Abrí una aplicación que sepas que se conecta a un servicio legítimo y comprobá que sigue funcionando: si se rompió, bloqueaste de más.
5. **La prueba del reinicio.** Reiniciá el teléfono y repetí las cuatro anteriores. Media docena de configuraciones de privacidad fallan justo acá, porque la aplicación no vuelve a levantar el túnel sola.

## Tres errores que se pagan

**Bloquear todo de entrada.** El teléfono deja de recibir notificaciones, las compras dentro de aplicaciones fallan, los mapas no cargan. La regla es la inversa: primero dejar pasar todo y observar una semana; después bloquear por categoría; al final, por aplicación.

**Bloquear el sistema.** Los servicios del sistema —actualizaciones, respaldo, mensajería del fabricante— también hacen conexiones. Algunos son prescindibles; otros sostienen el aparato. La lista de lo que se puede cortar sin consecuencias cambia por fabricante y por versión, así que ninguna guía seria, incluida esta, puede darte una lista fija.

**Confundir el bloqueo con el anonimato.** Cortar la telemetría de una aplicación no cambia lo que esa aplicación ya sabe de ti por dentro: tu cuenta, tu número, tu lista de contactos. Eso se resuelve con permisos y con decisiones, no con un túnel.

## Cuatro cosas que se dicen y no son verdad

**«Un bloqueador de anuncios te hace anónimo».** Bloquea nombres conocidos. No cambia tu dirección de red, no te esconde del servidor con el que hablás y no borra lo que las aplicaciones ya guardaron en el teléfono.

**«Más listas, mejor bloqueo».** Las listas se pisan entre sí y una lista agresiva rompe funciones. Cinco listas bien elegidas superan a treinta acumuladas.

**«Con root es mejor».** Root permite cortar por debajo, sin túnel y sin que las aplicaciones lo noten, y eso es una ventaja real. Pero también rompe la garantía, expone el aparato y hace que un error sea mucho más caro. Para el uso normal, el túnel alcanza.

**«Si es de código abierto, no envía datos».** Lo que garantiza el código abierto es que **se puede comprobar**, no que no ocurra. Esta guía tiene una ficha entera —TrackerControl— dedicada justamente a comprobarlo, y una —PCAPdroid— dedicada a demostrarlo.

## Las dos cifras que muestran cómo se mide esta categoría

Un ejemplo de lo que se aprende midiendo en vez de repitiendo.

Rethink, en su propio archivo de presentación, publica **tres huellas de certificado distintas**: una para el sabor que distribuye en la tienda de Google y en su sitio, otra para el sabor que distribuye IzzyOnDroid y otra para el sabor alfa que compila GitHub. Es la misma aplicación, con tres firmantes legítimos, según el canal. Es exactamente el dato del capítulo 4 visto desde dentro de un proyecto que lo hace bien: no hay una firma «verdadera», hay canales, y saber cuál tenés instalado es parte de usar el aparato con criterio.

El otro ejemplo es AdAway. Tiene nueve mil quinientas noventa y dos estrellas, la cifra más alta de las seis fichas de este capítulo, y su última entrega publicada es de octubre de 2024, mientras el código se sigue moviendo en septiembre de 2026. La aplicación funciona y el modo de bloqueo por lista no caduca; lo que caduca es la lista. Un proyecto puede estar vivo en el código y quieto en las entregas, y las dos cosas dicen algo distinto.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca instaló un bloqueador: si consigue que TrackerControl le muestre, en un día, al menos una empresa de seguimiento en una aplicación que usa todos los días, y sabe explicar qué significa lo que vio, el capítulo sirve.

Y dalo a alguien que lleva años con esto: si no encuentra al menos un dato que no supiera —que sólo puede haber un túnel activo y por eso los bloqueadores se pelean con la VPN, que el encubrimiento de DNS es una técnica y una señal a la vez, que `private_dns_mode` dice en una línea si el cifrado está puesto, que la misma aplicación tiene tres certificados según el canal—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Las que siguen están ordenadas como el capítulo: primero ver, después cortar, después cifrar, después registrar, después demostrar. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando. Todas se midieron el 3 de noviembre de 2026 abriendo sus entregas y su código, no repitiendo lo que dice un catálogo.
