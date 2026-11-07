# Capítulo 4 · Instalar fuera de la tienda

## Qué vas a poder hacer al terminar

Bajar una aplicación desde la página de su autor, comprobar en un minuto que el archivo es el que dice ser y dejarla instalada y actualizable sin depender de ninguna tienda. Sabrás leer una huella, distinguir un paquete de un montón de paquetes partidos, y entender por qué el teléfono a veces se niega a actualizar algo que debería actualizarse.

Y algo que casi nadie tiene claro aunque lleve años haciéndolo: por qué la misma aplicación, con el mismo nombre y el mismo icono, viene firmada con dos llaves distintas según de dónde salga. Eso explica los errores que la gente sufre sin saber por qué, y al final del capítulo lo vas a poder demostrar en tu propio teléfono.

## La regla que ordena el capítulo: la firma manda

Un paquete de Android lleva dentro una firma criptográfica, puesta por quien lo compiló. Android no te pregunta si confías en esa persona: compara la firma del paquete nuevo con la del que ya está instalado. Si coinciden, la actualización entra y conserva tus datos. Si no coinciden, la rechaza —aunque el nombre sea el mismo, aunque la versión sea más nueva, aunque el icono sea idéntico.

Todo lo demás de este capítulo es alrededor de esa regla. Una huella te dice de quién es la firma. Los paquetes partidos son una forma de empaquetar. Las tiendas son formas de repartir. Y los errores que la gente ve en la pantalla son, casi siempre, la misma frase dicha de cinco maneras: *esta firma no es la que yo tengo*.

## La ruta de decisión, en tres preguntas

**Si querés actualizar aplicaciones que ya tenés, sin tiendas** → **Obtainium**. Es la pieza central del capítulo: apuntás a la página del proyecto y él vigila las entregas nuevas. Una vez configurado, el trabajo es ninguno.

**Si querés una tienda entera, con catálogo y curaduría** → **F-Droid** si querés el catálogo grande y libre; **Accrescent** si querés un catálogo pequeño, revisado y con reglas modernas de firma. Los dos son tiendas, no repositorios sueltos, y esa diferencia importa: una tienda firma su índice, y eso te permite comprobar que el catálogo que ves es el que ellos publicaron.

**Si te bajaste un archivo y el teléfono no lo instala, o querés verificar un APK que te pasaron** → **Universal Installer** para los paquetes partidos y **AppVerifier** para la huella. Y si querés la versión de una aplicación que la tienda no tiene, **Aurora Store**, con las advertencias que trae su ficha.

## Qué es un paquete, de verdad

Un APK es un archivo comprimido con reglas: manifiesto, código, recursos, firma. Nada más. Si le cambiás un byte, la firma deja de cuadrar y el teléfono lo rechaza. Por eso «modificar el APK para quitarle los anuncios» es un trabajo de recompilar y volver a firmar, no de editar.

La complicación moderna es que una aplicación ya no es un archivo. Desde Android 5, un paquete puede venir **partido**: un APK base y varios pedazos que sólo sirven para tu teléfono —el del procesador, el de la densidad de pantalla, el del idioma—. El teléfono instala el base más los pedazos que le corresponden. Esos conjuntos circulan con extensiones distintas según quién los empaquete: `.apks`, `.apkm`, `.xapk`. Son lo mismo por dentro: un comprimido con varios APK y un archivo de metadatos que dice cuál es el base.

Si te bajás un `.apks` y lo abrís como si fuera un APK, no vas a poder. Y si te bajás el APK base suelto de una aplicación que sólo publica paquetes partidos, puede instalarse y luego caerse al abrir, porque le faltan los pedazos.

La forma de saber qué estás mirando, ya instalado, es preguntarle al sistema:

```
adb shell pm path com.ejemplo.app
```

Un teléfono con paquetes partidos devuelve varias líneas: `base.apk` y dos o tres `split_config.*`. Uno con paquete sencillo devuelve una sola. Esa lista es la diferencia entre «la aplicación está instalada» y «la aplicación está completa».

## La huella, en un minuto

Hay dos huellas que se confunden todo el tiempo y no son lo mismo.

**La huella del archivo** es un resumen del contenido: si cambia un byte, cambia la huella. Sirve para saber que la descarga llegó completa y que nadie la tocó en el camino. Los proyectos serios la publican al lado del archivo. Obtainium, en su entrega del 1 de noviembre de 2026, publica treinta y dos adjuntos: por cada sabor y cada arquitectura, la APK, su `.idsig`, la suma `.sha256` y la firma de esa suma, `.sha256.sig`. Cuatro piezas por archivo, sin excepción.

**La huella de la llave** es distinta: no describe el archivo, describe al firmante. Dos versiones distintas de la misma aplicación tienen huellas de archivo distintas y huella de llave idéntica. Esa es la que Android compara para decidir si una actualización entra.

Con `apksigner` —viene con las herramientas de Android y también corre en el teléfono con Termux— se ven las dos cosas en una orden:

```
apksigner verify --print-certs aplicacion.apk
```

Ahí aparece el `SHA-256 digest` del certificado. Compare ese número con el que el proyecto publica en su repositorio: si coincide, el archivo lo firmó quien dice. Y si el proyecto publica el archivo de huella, compruebe primero el archivo:

```
sha256sum aplicacion.apk
```

Dos comprobaciones distintas para dos preguntas distintas: `sha256sum` te dice que el archivo es el que se publicó; `apksigner` te dice quién lo firmó. Y hay una tercera pieza que casi nadie usa: el archivo `.asc`, una firma separada hecha con GPG, que se verifica con `gpg --verify aplicacion.apk.asc aplicacion.apk`. F-Droid publica el APK con su firma separada `.asc`, que es lo que permite verificar el archivo sin instalarlo; el `.idsig` aparece en su entrega vieja del espejo, la de enero de 2024, no en las actuales.

Ese `.idsig` merece una línea, porque es el dato que separa al curioso del experto. Es la firma de cuarta generación de Android y sirve para instalar por partes, sin reescribir el paquete completo; el teléfono la usa cuando actualiza en segundo plano. Que un proyecto la publique significa que compila con herramientas actuales y que piensa en actualizaciones incrementales, no en descargas manuales.

## La casa y el espejo

Acá va la lección de método más caras de este capítulo, y la medí para poder contarla con números.

Casi todo proyecto libre tiene dos direcciones: la casa, donde de verdad se trabaja, y uno o varios espejos, donde el código se copia para que otros lo vean. Confundirlas produce un error de medición que se repite en los catálogos de aplicaciones que circulan por ahí: **recomiendan una versión que tiene dos años**.

El cliente de F-Droid lo muestra desnudo. En su espejo de GitHub, la última entrega publicada es la 1.18.0, del 24 de enero de 2024, y tiene 3.255 estrellas. En su casa de GitLab, la etiqueta más reciente es la 2.0.3, del 29 de octubre de 2026, y hay 2.688 estrellas y actividad de hoy mismo. Quien se guíe por el espejo se queda dos versiones mayores atrás y, peor, cree que el proyecto está parado.

Aurora Store es el caso al revés y todavía más claro. Su espejo de GitHub nació el 11 de enero de 2026 y lleva 74 estrellas y ninguna entrega publicada. Su casa, en GitLab, tiene 2.284 estrellas y va por la 4.8.4, del 27 de julio de 2026. Un catálogo que mida el espejo va a decir que Aurora Store es un proyecto de 74 estrellas sin entregas. El número no está mintiendo: está midiendo otra cosa.

De ahí sale una regla que sirve para todo lo que venga después en esta guía, y también para cuando la guía no esté: **antes de creer una cifra, mirá dónde se midió**. Las fichas de este capítulo declaran en cada caso cuál es la casa y cuál el espejo, y qué número salió de cada uno.

## Actualizar sin perder datos: la regla de la misma llave

Como Android exige la misma llave para actualizar, hay consecuencias prácticas que la gente descubre cuando ya perdió los datos.

**Cambiar de canal puede costar todo.** Si instalaste una aplicación desde una tienda que recompila y refirma —F-Droid lo hace— y después querés la versión del autor desde GitHub, el teléfono te va a decir que la actualización es incompatible. La salida es desinstalar, y desinstalar borra los datos. Antes de cambiar de canal: exportá lo que valga la pena.

**La tienda de Google refirma.** En las aplicaciones acogidas a la firma de Google, el paquete que baja de Play lleva la llave de Google, no la del autor. Por eso una aplicación instalada desde Play no se puede actualizar con el APK del repositorio, aunque sea el mismo código, la misma versión y el mismo nombre. Es la comprobación que podés hacer con dos archivos y `apksigner`: huellas de llave distintas, huella de archivo distinta, nombre de paquete idéntico.

**Y cuando un proyecto cambia de llave, avisa o rompe.** Si el autor perdió su llave y firmó de nuevo, todas las actualizaciones se van a negar hasta que desinstales. No es un ataque: es la protección funcionando.

## Los cinco errores de instalación, traducidos

El teléfono no explica lo que pasa, pero los mensajes son pocos y siempre los mismos.

- **«No se pudo instalar»** o `INSTALL_FAILED_UPDATE_INCOMPATIBLE` — la firma no coincide con la que ya está instalada. Salida: desinstalar (perdés datos) o conseguir el paquete firmado con la misma llave.
- `INSTALL_FAILED_VERSION_DOWNGRADE` — estás intentando poner una versión anterior sobre una más nueva. Salida: desinstalar primero, o `adb install -r -d` si tenés consola y sabés lo que hacés.
- `INSTALL_FAILED_INVALID_APK` con mención de splits — bajaste un pedazo suelto de un paquete partido. Salida: el conjunto completo, base incluido.
- `INSTALL_FAILED_DEPRECATED_SDK_VERSION` — desde Android 14, el sistema no instala aplicaciones dirigidas a versiones muy antiguas de Android. No hay truco: ese paquete no está mantenido.
- **«Play Protect no reconoce esta aplicación»** — no es un error de instalación, es un aviso. Un APK que no pasó por Play no tiene historial de instalaciones; vos sos el primero. Se puede continuar, y conviene hacerlo sólo si comprobaste la firma.

## Cuatro cosas que se dicen y no son verdad

**«Instalar fuera de la tienda es ilegal».** No lo es en casi ningún país; lo que puede violar un contrato es la licencia de una aplicación concreta o los términos de un servicio. Esta guía sólo enlaza proyectos cuyo código y licencia permiten redistribuir. Lo que sí es un delito en muchos sitios es usar software para acceder a contenido de pago sin pagarlo, y eso no tiene nada que ver con instalar un APK libre.

**«F-Droid es la opción más segura porque es F-Droid».** F-Droid firma su catálogo y publica firmas separadas en sus entregas —es de los pocos que publica el `.asc`—, y eso es serio. Pero sus paquetes los compila y firma F-Droid, no el autor, así que estás confiando en dos partes a la vez. Eso no es malo: es distinto, y hay que saberlo antes de elegir el canal.

**«Más estrellas, más seguro».** Aurora Store tiene 2.284 estrellas en su casa y 74 en el espejo. Canta, que está en el capítulo 2, tiene 6.446 y saca 71 puntos de 100; Obtainium tiene 21.181 y saca 73. La nota mide cómo se publica —con huellas, con compilación automática, con entregas fechadas, con cola de incidencias atendida—, no cuánta gente lo bajó.

**«Si la tienda lo tiene, ya está verificado».** La verificación de la que hablan las tiendas suele ser del índice: que el catálogo no fue alterado en el camino. Que el paquete que te llega sea el que el autor compiló es otra pregunta, y casi nadie la responde. La única manera de responderla con tus manos es comparar firmas.

## Antes de irte: la prueba de las dos personas

Dale este capítulo a alguien que nunca instaló nada fuera de la tienda: si consigue instalar Obtainium desde su repositorio y comprobar la huella del archivo en menos de veinte minutos sin ayuda, el capítulo sirve.

Y dalo a alguien que lleva años haciéndolo: si no encuentra al menos un dato que no supiera —que la misma aplicación viene firmada por llaves distintas según la tienda, que el espejo de F-Droid está dos años atrás, que un paquete partido se comprueba con `pm path`, que el `.idsig` es la firma de cuarta generación—, el capítulo no sirve y hay que reescribirlo.

## Las seis fichas

Las que siguen están ordenadas por dificultad, no por fama. Cada una declara para quién es y para quién no, y cada una trae el dato de oficio con su comando para comprobarlo. Todas se midieron abriendo sus entregas una por una el 3 de noviembre de 2026, y en las dos que viven en GitLab se midió la casa, no el espejo.
