*La cerradura que cambió de dueño: firmas, atestación y el aviso del sistema*

*La Bandita · domingo 1 de noviembre de 2026 · edición dominicano-español · pieza 03 de Facebook*

*🗺️ Mapa de esta guía*

```
├── ⚡ En una página
├── 🎬 Cuatro escenas de la misma cerradura
├── 🧾 El censo de hoy: diez piezas de verificación
├── 🧩 Qué firma un paquete y qué no
├── 🔐 La atestación del aparato
├── 🧯 El aviso que asusta y no siempre informa
├── 🏗️ El aparato endurecido
├── 🛠️ Comprobar una firma en seis pasos
├── ⚖️ La ley, sin sermón
├── ❓ Preguntas que me hacen
├── 📊 Tabla, mitos y glosario
└── 🔗 Enlaces y notas del corte
```

───────────────────

*⚡ En una página*

El teléfono toma decisiones sobre lo que instala y casi nadie sabe con qué criterio. Cuando dice «aplicación no instalada» está comparando firmas. Cuando muestra un aviso de que una app puede ser peligrosa está comparando listas. Y cuando una app de banca se niega a abrir, está mirando el estado del aparato, no la cara del dueño. Tres cerraduras distintas que la gente confunde en una sola: «el teléfono no me deja».

Esta mañana medí diez piezas de verificación, cada una leída tres veces por tres caminos, y el mapa de hoy tiene una novedad y un hueco. La novedad es que el aparato endurecido se volvió cotidiano: hardened_malloc, con ★2.048, empujó hoy mismo; Vanadium, el navegador del mismo proyecto, ★2.270, publicó versión el 30 de octubre; la cámara, ★1.423, también. El hueco es que la herramienta que todo el mundo citaba para pasar la verificación de integridad ya no existe en su dirección conocida: devuelve un 404 y no hay ficha que sacar.

Debajo de eso hay una familia de herramientas que sí se pueden leer y que sirven para lo que esta guía propone: Auditor, ★729, que lee el certificado de atestación del aparato; AppManager, ★9.398, que muestra con qué firma está instalado cada paquete; Shizuku, ★32.590, que presta el permiso de depuración sin root; degoog, ★2.505, que audita qué servicios de Google quedan en el teléfono; FreeDroidWarn, ★3.731, que convierte los avisos del sistema en algo legible.

Y hay un dato que vale para la vida diaria: dos de las diez fichas no coinciden consigo mismas en el campo de licencia. Ytzero declara Unlicense en su ficha y AGPL-3.0 en su README; el navegador Vanadium aparece sin licencia identificable. Se publican las dos versiones de cada discrepancia, como se hace siempre, sin elegir la que queda mejor.

La idea que hay que llevarse: una firma dice quién hizo el paquete, no si es bueno. La atestación dice si el aparato es el que dice ser, no si su dueño es de fiar. Y el aviso del sistema dice lo que la lista de turno sabe, que puede ser mucho o puede ser nada.

───────────────────

*🎬 Cuatro escenas de la misma cerradura*

**La app del banco que no abre.** Un señor instala una herramienta de administración, todo funciona, y a la semana la app del banco se niega a abrir con un mensaje seco. No lo bloqueó el banco por capricho: el teléfono dejó de responder como un teléfono sin modificaciones. La salida no es discutir con el banco; es decidir qué se quiere tener y aceptar el costo.

**El paquete que se instaló dos veces.** Una muchacha se baja la misma app de dos sitios y el segundo intento falla. Las dos descargas dicen la misma versión. Lo que cambió fue la firma: para Android son dos aplicaciones distintas. Ese detalle es la primera cosa que hay que mirar cuando algo «no instala».

**El aviso que llegó tarde.** Un cliente instala un paquete y el sistema avisa, tres días después, que la app puede ser dañina. El aviso no es magia: es una lista que el sistema consulta y que a veces llega tarde. Sirve como señal, no como veredicto.

**El teléfono heredado.** Alguien compra un aparato usado y quiere saber si está como salió de fábrica. Con el certificado de atestación y una herramienta que lo lea se puede comprobar parte de eso: si el cargador de arranque está abierto, si el sistema fue modificado, si las claves del aparato son las originales. Es una revisión, no un certificado de buena salud.

───────────────────

*🧾 El censo de hoy: diez piezas de verificación*

Medidas entre las 13:25 y las 13:35 de Santo Domingo, tres lecturas por proyecto y con el orden rotado: buscador de la forja, página del repositorio, archivo crudo. Estrellas, licencia, lenguaje y último empujón son de esa hora; la versión es la del último release publicado.

*La atestación y la auditoría*

- **Auditor** — lee el certificado con el que el aparato demuestra qué sistema lleva y si sus claves son las originales ★729 · licencia MIT · Java · empujó el 30-oct (hace 2 días) · release 92 (30-may) · https://github.com/GrapheneOS/Auditor
- **AppManager** — muestra la firma de cada paquete instalado, además de permisos, servicios y rastreadores ★9.398 · licencia NOASSERTION en la ficha y GPL-3.0 en su README · Java · empujó el 30-oct (hace 2 días) · release v4.1.1 (04-sep) · https://github.com/MuntashirAkon/AppManager
- **Shizuku** — presta el permiso de depuración a las apps que lo piden, sin tocar el arranque ★32.590 · licencia Apache-2.0 · Kotlin · empujó el 18-jun-2025 (hace 501 días) · release v13.6.0 (25-may-2025) · https://github.com/RikkaApps/Shizuku

*El aparato endurecido*

- **Vanadium** — el navegador del proyecto que endurece Android, con sus propios parches ★2.270 · sin licencia identificada en la ficha · Python · empujó el 30-oct (hace 2 días) · release 156.0.8078.79.0 (30-oct) · https://github.com/GrapheneOS/Vanadium
- **Camera** — la cámara del mismo proyecto, con el procesamiento dentro del teléfono ★1.423 · licencia MIT · Kotlin · empujó el 30-oct (hace 2 días) · release 93 (01-ago) · https://github.com/GrapheneOS/Camera
- **hardened_malloc** — el asignador de memoria endurecido, la pieza que casi nadie ve y más cambia ★2.048 · licencia MIT · C · empujó hoy · release 14 (22-feb) · https://github.com/GrapheneOS/hardened_malloc

*Los avisos y el ruido*

- **FreeDroidWarn** — traduce los avisos del sistema sobre apps «poco fiables» y los pone en contexto ★3.731 · licencia Apache-2.0 · Java · empujó el 28-oct (hace 4 días) · release V1.14 (09-sep) · https://github.com/woheller69/FreeDroidWarn
- **degoog** — audita qué servicios de Google quedan activos en el teléfono y ayuda a quitarlos ★2.505 · licencia AGPL-3.0 · TypeScript · empujó el 29-oct (hace 3 días) · release 1.1.1 (25-oct) · https://github.com/degoog-org/degoog
- **ytzero** — cliente de video que evita el rastreo de la plataforma grande ★671 · licencia Unlicense en la ficha y AGPL-3.0 en su README · TypeScript · empujó el 28-sep (hace 34 días) · release 2026.09.9 (28-sep) · https://github.com/Pelski/ytzero
- **Gearslip** — pieza joven para actualizar el sistema sin la tienda del fabricante ★232 · licencia AGPL-3.0 · Kotlin · empujó el 27-oct (hace 5 días) · release v0.3.12-alpha (25-oct) · https://github.com/twinksoftware/Gearslip

*Lo que el censo dice en tres líneas.* Seis de las diez empujaron en los últimos cinco días, y eso en un grupo de herramientas de verificación es la señal que importa: son las que se rompen cuando el sistema cambia. Dos fichas no coinciden consigo mismas en licencia —ytzero y Vanadium— y se publican las dos versiones cuando existen. Y una herramienta que se citaba en todas las listas para pasar la verificación de integridad ya no está en su dirección: devuelve 404, no tiene ficha y no se rellena el hueco.

───────────────────

*🧩 Qué firma un paquete y qué no*

Un APK lleva dentro un certificado. Ese certificado no dice «esta app es buena»: dice «esto lo firmó alguien que tiene esta llave». Android lo usa para tres cosas y solo tres: actualizar encima sin pedir permiso de más, compartir datos entre apps del mismo firmante, y decidir si dos paquetes con el mismo nombre son el mismo programa.

De ahí salen casi todos los mensajes que la gente ve y no entiende. «Aplicación no instalada» casi siempre significa que la firma no coincide con la que ya está instalada. «Conflicto de paquete» es lo mismo con otras palabras. Y «versión no compatible» a veces no tiene nada que ver con la firma: es que el paquete es de otra arquitectura o pide un Android más nuevo.

Lo que una firma no dice es quién está detrás. Cualquiera puede generar una llave hoy y firmar un paquete mañana. Por eso hay un segundo nivel, el que casi nadie mira: el certificado de la tienda. Cuando una app viene de una tienda que compila el código, la firma es de la tienda aunque el autor sea otro, y eso explica por qué no se puede actualizar con el APK del autor.

Y hay un tercer nivel que se confunde con los otros dos: el estado del aparato. Que un teléfono esté modificado no cambia la firma de nada; cambia lo que algunas apps están dispuestas a hacer. La app del banco no mira quién firmó la aplicación que se instaló: mira el aparato.

La consecuencia práctica es sencilla. Antes de instalar, la pregunta útil es de dónde viene el paquete. Después de instalar, la pregunta es con qué firma quedó. Y cuando algo se niega a funcionar, la pregunta es cuál de las tres cerraduras se cerró.

───────────────────

*🔐 La atestación del aparato*

La atestación es la forma que tiene un teléfono de demostrar, sin que uno se lo pida, qué sistema lleva y si sus claves son las que trajo de fábrica. No es una app: es una capacidad del hardware que se activa cuando alguien pregunta.

Auditor, con ★729 y licencia MIT, es la herramienta más directa para leerla en los aparatos que la soportan: pide el certificado, lo muestra y explica cada campo. Su último release es el 92 del 30 de mayo, aunque el repositorio empujó el 30 de octubre; se publican las dos fechas.

Para qué sirve en la práctica: para saber si un aparato usado está como salió de fábrica, para entender por qué una app de banca se niega a abrir, y para comprobar si una actualización de sistema se aplicó de verdad. Para lo que no sirve: para demostrar que el aparato está libre de programas maliciosos. Un teléfono con el sistema original puede tener tres apps espía y su atestación saldrá perfecta.

Ese malentendido es el que más daño hace. La atestación responde a una pregunta concreta —¿este aparato ejecuta el sistema que dice ejecutar?— y la gente la lee como un certificado de salud general. No lo es, y saberlo evita dos errores: confiarse por un resultado limpio y alarmarse por uno sucio.

───────────────────

*🧯 El aviso que asusta y no siempre informa*

Cuando el sistema muestra el aviso de que una aplicación «puede ser dañina», no está haciendo un análisis. Está consultando una lista. Esa lista la mantiene quien opera la tienda o el fabricante, se actualiza cuando se actualiza, y contiene lo que alguien decidió poner ahí.

De ahí salen dos verdades incómodas. La primera: hay avisos que llegan tarde, porque la lista se actualiza después de que el paquete circule. La segunda: hay avisos que sobran, porque castigan a una app legítima por su origen y no por lo que hace. Las dos cosas pasan todos los meses y las dos se resuelven igual: mirando el paquete, no el aviso.

FreeDroidWarn, con ★3.731 y licencia Apache-2.0, existe justamente para eso: pone en contexto los avisos que aparecen al instalar software libre desde fuera de la tienda, explica por qué salen y deja al usuario decidir con información en vez de con susto. Su versión V1.14 es del 9 de septiembre y empujó el 28 de octubre.

La costumbre que vale es esta: cuando aparezca un aviso, no cerrar por reflejo ni ignorarlo por reflejo. Anotar de dónde vino el paquete, con qué firma está, y si el aviso habla de comportamiento o solo de procedencia. Las tres cosas se comprueban con AppManager en dos minutos.

Y una regla que no falla: el aviso más peligroso no es el que aparece, es el que no aparece. Un paquete firmado por una llave desconocida, instalado desde una carpeta de descargas, sin ningún aviso, es más probable que sea un problema que el que el sistema marca en amarillo.

───────────────────

*🏗️ El aparato endurecido*

Hay un proyecto que lleva años construyendo un Android distinto, con el foco en la seguridad del aparato y no en las funciones: el de GrapheneOS. De ese proyecto salen cuatro piezas que aparecen en este censo y que conviene entender por separado.

hardened_malloc, con ★2.048, es la más invisible y la más importante: un asignador de memoria que hace más difícil aprovechar un fallo de un programa. Empujó hoy mismo y su última versión publicada es la 14, de febrero. Que una pieza así exista y se mantenga dice más de un proyecto que cualquier campaña de imagen.

Vanadium, con ★2.270, es el navegador basado en Chromium con los parches del proyecto. Su release 156.0.8078.79.0 es del 30 de octubre, lo que muestra el ritmo: sigue a las versiones del motor casi al día. Su ficha aparece sin licencia identificable, y eso se publica tal cual, sin adivinar.

Camera, con ★1.423, es la cámara con el procesamiento dentro del teléfono y sin servicios externos. Release 93 del 1 de agosto, empujón del 30 de octubre.

Auditor, ★729, cierra el grupo con la atestación, como ya se dijo. Y fuera de ese proyecto hay dos piezas que completan el cuadro de la verificación sin pertenecer a él: degoog, ★2.505, que audita qué queda de los servicios de Google y ayuda a retirarlos paso a paso; y Gearslip, ★232, un proyecto joven y en alfa —v0.3.12-alpha del 25 de octubre— que apunta a actualizar el sistema sin la tienda del fabricante.

Lo que este grupo enseña, más allá de sus números, es una forma de trabajar: piezas pequeñas, cada una con una responsabilidad, publicadas con fecha y con su código a la vista. No es un paquete único que promete seguridad: es un conjunto de cerraduras que se pueden revisar una por una.

───────────────────

*🛠️ Comprobar una firma en seis pasos*

**Paso uno: saber qué versión está instalada.** Antes de tocar nada, anotar el nombre del paquete, la versión y la fecha de instalación. Sin ese punto de partida, cualquier cambio es a ciegas.

**Paso dos: mirar la firma con una herramienta que la muestre.** AppManager la enseña en la ficha de cada app instalada. Si no se tiene, cualquier visor de paquetes sirve, siempre que muestre la huella del certificado y no solo el nombre bonito del desarrollador.

**Paso tres: comparar con la firma del paquete nuevo.** El APK que se va a instalar trae la suya. Si las huellas coinciden, es una actualización; si no, es otra aplicación con el mismo nombre.

**Paso cuatro: decidir antes de instalar.** Con firmas iguales, se actualiza y se conservan los datos. Con firmas distintas hay dos caminos: desinstalar la vieja aceptando perder lo guardado, o no instalar la nueva. Elegir a sabiendas es la mitad del trabajo.

**Paso cinco: dejar constancia.** Una nota con la huella de la versión que funciona sirve dentro de seis meses, cuando el paquete ya no esté y haya que decidir si el que aparece es el mismo.

**Paso seis: repetir cuando cambie algo.** Cada actualización de sistema puede cambiar el comportamiento de estas herramientas. Lo que hoy muestra una firma, mañana puede pedir otro permiso. La comprobación no es un trámite de una vez: es una costumbre.

───────────────────

*⚖️ La ley, sin sermón*

Las licencias de este grupo son cortas de contar y largas de entender. MIT en Auditor, Camera y hardened_malloc: se puede usar, copiar y modificar, con una cláusula de garantía que dice que nadie responde por nada. Apache-2.0 en Shizuku, FreeDroidWarn: lo mismo con una cláusula de patentes. AGPL-3.0 en degoog y Gearslip: si se modifica y se ofrece como servicio en red, hay que publicar el código. Y dos fichas sin licencia identificable —Vanadium— o con dos versiones que se contradicen —ytzero, Unlicense en la ficha y AGPL-3.0 en el README—, que se publican tal cual.

Nada de eso protege de un mal uso. Una firma se puede generar para cualquier cosa, y una herramienta de auditoría sirve igual para revisar un aparato propio que para husmear en uno ajeno sin permiso. La línea no está en el programa: está en de quién es el aparato y quién dio el visto bueno.

Hay además un asunto de convivencia que conviene decir sin dramatismo: modificar un teléfono puede dejarlo fuera de garantía y fuera de algunas apps. Eso no es una prohibición moral; es una consecuencia que se acepta o no. Lo que no se puede es exigirle al banco que ignore el estado del aparato y, a la vez, tener el aparato abierto.

───────────────────

*🗣️ Los mensajes del sistema, traducidos*

La mitad de las consultas que llegan son el mismo mensaje mal entendido. Esta es la traducción de los que más salen, dicha como se diría en la puerta de una casa.

**«Aplicación no instalada».** Casi siempre es la firma: el paquete nuevo no coincide con el que ya está. Puede ser también que la app esté instalada para otro usuario del teléfono, o que el paquete esté incompleto porque la descarga se cortó. El orden de comprobación es ese: firma, usuario, tamaño.

**«Paquete con el mismo nombre ya existe».** El sistema encontró otra app con el mismo identificador. Si se quiere instalar de todos modos, hay que quitar la anterior y aceptar que se van sus datos.

**«La aplicación no es compatible con tu teléfono».** Aquí no hay firma que valga: el paquete pide un Android más nuevo, otra arquitectura o una pantalla que el aparato no declara. Las tres cosas se ven en la ficha del archivo antes de instalar.

**«Bloqueado por Play Protect».** Es un aviso de lista, no un análisis. Se puede mirar por qué y decidir. Un paquete libre descargado del repositorio del autor suele salir en esa lista por su origen, no por lo que hace.

**«Este paquete parece dañino».** Igual que el anterior, con más palabras. Y con la misma recomendación: mirar la firma y los permisos antes de decidir.

**«Instalación bloqueada por el administrador».** Hay un perfil de trabajo, una app de control parental o una política del aparato que prohíbe instalar. No es un fallo: es un permiso que alguien retiró, y quien lo retiró tiene que devolverlo.

**«No hay espacio suficiente».** Suena a poco espacio y a veces es un paquete que pide el doble de su tamaño para instalarse. Con un paquete dividido, además, hay que contar las partes.

**«Error de análisis».** El archivo está corrupto o no es un APK. Pasa mucho con descargas interrumpidas y con archivos que en realidad son páginas de error guardadas con extensión cambiada.

**«Firma no válida».** El paquete fue modificado después de firmarse, o se firmó con un método que este Android no acepta. Un paquete tocado a mano sin volver a firmarlo da exactamente este mensaje.

**«Origen desconocido bloqueado».** El sistema no permite instalar desde la app que está intentando hacerlo. Se concede el permiso a esa app concreta y solo a esa, que es el consejo que vale para todo lo demás.

Traducir el mensaje no resuelve el problema, y ahorra la media hora de buscar en foros una respuesta que habla de otra cosa. Casi todos estos textos describen una comprobación concreta, y todas las comprobaciones de esta lista se pueden hacer con las herramientas del censo.

───────────────────

*🕰️ Cronología de las cerraduras*

La historia de estas tres cerraduras explica por qué hoy hay tantas piezas pequeñas en vez de una grande.

**2017 y 2018: la firma se vuelve esquema.** Android pasa a exigir firmas con esquema moderno para las apps nuevas, y eso rompe la compatibilidad con paquetes viejos firmados a la antigua. Muchos «no instala» de esa época vienen de ahí.

**2019 y 2020: llega la atestación al uso masivo.** Los aparatos empiezan a traer claves de hardware capaces de demostrar qué sistema ejecutan. Al principio lo usa el mundo del pago; después lo adoptan las apps que quieren negarse a correr en aparatos modificados.

**2021 y 2022: los avisos se generalizan.** Los sistemas empiezan a mostrar avisos propios al instalar paquetes de fuera de la tienda, con listas que se consultan en línea. La consecuencia social es que instalar software libre pasa a parecer una actividad sospechosa.

**2023 y 2024: el endurecimiento se hace cotidiano.** Asignadores de memoria más estrictos, navegadores con parches propios, cámaras sin servicios externos. Lo que era de laboratorio pasa a estar en el teléfono de quien lo quiera instalar.

**2025: se archivan proyectos que parecían eternos.** Syncthing oficial en diciembre de 2024, LSPatch en diciembre de 2023, Kotatsu en noviembre de 2025. La lección se repite: lo que no se empuja, se acaba.

**Hoy, 1 de noviembre de 2026: seis empujones en cinco días.** hardened_malloc empujó esta mañana; Vanadium, Camera y Auditor el 30 de octubre; degoog el 29; FreeDroidWarn el 28. Las cerraduras se siguen afinando, y ese es el dato que deja tranquilo a quien las usa.

Lo que la cronología no dice es hacia dónde va: no hay manera de saber si mañana una verificación nueva dejará fuera a la mitad de las herramientas de esta lista. Lo que sí se puede hacer es mirar las fechas cada mes, que es exactamente lo que esta guía hace.

───────────────────

*🏠 El teléfono de la casa: una auditoría de treinta minutos*

No hace falta ser técnico para saber qué tiene un teléfono. Hace falta media hora y un orden.

**Primer cuarto de hora: la lista.** Abrir los ajustes de aplicaciones y ordenar por fecha de instalación. Casi todo lo que aparece en los últimos lugares se instaló en una emergencia y nadie recuerda por qué. Anotar las que no se usan hace más de tres meses: son candidatas a salir, y ninguna de ellas explica el funcionamiento del aparato.

**Segundo cuarto de hora: el origen.** De las que quedan, separar las que vinieron de la tienda del sistema de las que vinieron de otro sitio. Las primeras se actualizan solas y no dan problemas. Las segundas son las que hay que mirar: ¿de qué repositorio salieron? ¿con qué firma están? ¿tienen versión nueva?

Ese es todo el ejercicio. Al terminarlo, la persona sabe tres cosas que antes no sabía: cuántas apps tiene, de dónde vinieron y cuáles están sin actualizar desde hace meses. Con eso puede decidir, sin ayuda de nadie, si el aparato está ordenado o si es un cajón desastre.

Lo que este ejercicio no hace es detectar un programa malicioso bien hecho. Para eso hace falta análisis forense, y el análisis forense no se hace en media hora ni con una app. Lo que sí hace es quitar de en medio el 90% de los problemas reales, que casi siempre son apps viejas, permisos de más y orígenes olvidados.

Y hay un resultado secundario que vale mucho: después de hacerlo una vez, la persona empieza a instalar de otra manera. Ya no acepta el primer enlace que llega, porque sabe que dentro de tres meses tendrá que acordarse de dónde salió.

───────────────────

*🧨 El permiso que se presta sin querer*

Hay un grupo de permisos que no se parece a los demás y que casi nunca se lee: los de accesibilidad. Sirven para que una app lea la pantalla, mueva el cursor y actúe por el usuario. Los usan los lectores de pantalla, los teclados alternativos y los automatizadores; también los usan las apps que roban contraseñas, porque con ese permiso pueden ver todo lo que aparece en pantalla.

El sistema avisa cuando se activa uno, y ese aviso se ignora más que ningún otro. Es comprensible: llega en medio de la configuración, con letra pequeña y una advertencia genérica que se parece a todas las demás.

La costumbre que sirve es simple: cada vez que se activa un permiso de accesibilidad, anotar qué app lo pidió y para qué. Si a los tres meses no se recuerda, se desactiva. El aparato no se rompe por desactivarlo; la app que lo necesitaba dejará de hacer esa función, y eso es todo.

Lo mismo vale para el permiso de administrador del dispositivo, que permite bloquear, borrar y cambiar ajustes sin pasar por el dueño. Son contadas las apps que lo necesitan de verdad —algunas de correo corporativo, algunas de control parental— y muchas lo piden por comodidad. Es el permiso más potente del teléfono después de root, y se concede con la misma facilidad.

Los dos permisos tienen algo en común: no se pueden revisar mirando la ficha de la app. Hay que ir a un apartado específico de los ajustes, que cambia de nombre según el fabricante. Encontrarlo una vez y revisarlo dos veces al año es toda la defensa disponible, y es más de la que tiene la mayoría.

───────────────────

*🛡️ Qué se puede y qué no se puede comprobar sin root*

Cuando la conversación llega a la verificación, aparece siempre la misma pregunta: ¿hace falta root? La respuesta corta es no, y la larga se divide en tres columnas.

**Sin nada instalado** se puede comprobar el origen de un paquete, la fecha de la descarga y el tamaño del archivo. También se puede mirar qué permisos declara una app antes de instalarla, porque el instalador los muestra. Con eso se descartan los casos evidentes y no se detecta nada sutil.

**Con el permiso de depuración** —que es lo que presta Shizuku— se puede ver la lista completa de paquetes con sus firmas, congelar apps del sistema y revisar componentes. Es el mejor punto de equilibrio que existe hoy: mucho acceso, ningún riesgo de arranque y la posibilidad de revocarlo apagando un interruptor.

**Con root** se puede ver todo: el sistema de archivos completo, los registros del núcleo, la memoria de otros procesos. También se puede romper todo con una línea mal escrita, y algunas apps dejan de abrir.

La columna del medio es la que casi nadie aprovecha y la que resuelve más. Shizuku lleva más de un año sin empujón y sigue funcionando porque el permiso que usa es del sistema; AppManager empujó el 30 de octubre y muestra con eso lo que antes pedía root. Entre las dos cubren la auditoría de una casa sin tocar el arranque.

La regla que se desprende: primero mira qué se puede saber sin modificar nada, después qué se puede saber prestando un permiso temporal, y solo al final considera root, con una razón concreta que valga el riesgo.

───────────────────

*🧭 Cómo se elige entre tanta herramienta*

Diez nombres en una guía y la tentación de instalarlo todo. No hace falta: cada una resuelve una pregunta distinta y la mayoría de la gente necesita dos.

Si la pregunta es «qué tengo instalado y con qué firma está», la respuesta es AppManager, y el permiso de depuración lo completa. Dos piezas, una tarde, y la casa queda auditada.

Si la pregunta es «este teléfono es el que dice ser», la respuesta es Auditor, y solo tiene sentido en aparatos que soportan atestación. Si el aparato no la soporta, la herramienta no tiene nada que leer y la pregunta se queda sin respuesta.

Si la pregunta es «por qué el sistema me avisa de todo lo que bajo», la respuesta es FreeDroidWarn, que no quita avisos ni los justifica: los pone en contexto.

Si la pregunta es «qué hace Google en mi teléfono», degoog lo enseña sin prometer que se pueda quitar todo.

Si la pregunta es «quiero usar el teléfono sin que me sigan», el navegador y la cámara endurecidos hacen más que cualquier lista de bloqueo. Y si la pregunta es «quiero actualizar sin la tienda», Gearslip está en alfa y se prueba con respaldo.

Lo que ninguna de las diez hace es decidir por uno. Cada una entrega un dato y el juicio queda del lado de la persona, que es exactamente donde tiene que estar.

───────────────────

*❓ Preguntas que me hacen*

**¿Por qué la app del banco no abre si mi teléfono funciona perfecto?** Porque el banco no evalúa el funcionamiento, evalúa el estado: si el arranque está abierto, si el sistema está modificado, si el aparato responde como uno sin cambios. Se puede discutir si es justo; no se puede evitar mirando la app.

**¿Qué es exactamente la atestación?** Una prueba que el aparato genera con claves de hardware sobre el sistema que ejecuta. Sirve para saber si el teléfono es el que dice ser. No dice nada sobre las apps que tiene instaladas.

**Vi un aviso de app dañina en algo que bajé del repositorio del autor, ¿me asusto?** No por reflejo. Los avisos salen de listas y las listas castigan a veces el origen, no el comportamiento. Mira la firma, mira los permisos, y decide con eso.

**¿Cambiar la firma de un APK sirve para algo?** Sirve para instalarlo cuando la firma original estorba, y rompe la actualización: el paquete queda huérfano y no recibe nada del autor. Es un recurso de taller, no una costumbre.

**¿Puedo saber si mi teléfono usado está como salió de fábrica?** En parte, sí: la atestación lo dice en los aparatos que la soportan, y Auditor lo lee. Lo que no dice es si alguien instaló algo después. Para eso hace falta mirar la lista de paquetes con AppManager.

**¿Shizuku sirve para verificar firmas?** No directamente: sirve para dar a otras apps el permiso de depuración, y con eso algunas herramientas de auditoría acceden a más información sin root. Es una llave que se presta, no una herramienta de análisis.

**¿Qué pasa si desinstalo la app de la que dudo?** Se van los datos que tuviera. Si la duda es de firma y no de comportamiento, a veces basta con congelarla —AppManager puede, con permisos— y ver si algo se rompe. Es más reversible que borrar.

**¿degoog quita los servicios de Google?** Ayuda a auditarlos y a retirarlos paso a paso. Quitarlos del todo puede dejar sin funcionar apps que dependen de ellos, así que el orden importa: primero mirar qué depende de qué, después retirar.

**¿Gearslip reemplaza a la tienda del fabricante?** Es un proyecto joven y en alfa, con versión v0.3.12-alpha del 25 de octubre. Sirve para actualizar el sistema sin la tienda, y como todo lo que está en alfa, se prueba con respaldo y sin prisa.

**¿Por qué hay herramientas que llevan un año sin empujón y siguen recomendándose?** Porque el permiso que usan no cambia. Shizuku empujó por última vez en junio de 2025 y sigue funcionando; lo que hace depende del sistema, no de sus novedades. Distinto es un navegador, que envejece cada semana.

**¿Una firma fuerte garantiza que la app es buena?** No. Garantiza que es la misma app que firmó esa llave. Lo que hace la app se juzga leyendo lo que pide y lo que trae, no la huella del certificado.

**¿Vale la pena todo esto para un teléfono de uso normal?** Vale la pena saber lo mínimo: de dónde vienen los paquetes y con qué firma están. Lo demás —atestación, endurecimiento, auditoría profunda— es para quien administra, investiga o compró usado y quiere saber qué tiene en la mano.

───────────────────

*💬 Lo que dice la gente que ya pasó por aquí*

Las frases se repiten tanto que ya son parte del paisaje, y cada una tiene su traducción.

«Me salió que la app es peligrosa y la borré por miedo». Casi siempre era un aviso de lista por origen. La app se podía usar; lo que no se podía era saberlo sin mirar.

«Instalé la nueva y perdí las conversaciones». Firmas distintas, datos perdidos. El respaldo se hace antes, no después.

«No sé qué tengo instalado». La respuesta es la auditoría de media hora, y no hay atajo que valga.

«Mi teléfono es viejo, no aguanta estas cosas». Las herramientas de esta lista pesan poco; lo que pesa es tener doscientas apps. Lo viejo aguanta más de lo que se cree cuando está ordenado.

«¿Y si me equivoco?» Se equivoca uno, se desinstala y se vuelve. Lo único que no se recupera es lo que no se respaldó.

───────────────────

*🔍 El caso del paquete que llega sin nombre*

Hay una situación que se repite cada semana y que resume todo lo anterior: llega un archivo «app.apk», sin nombre, sin captura, con un mensaje de tres palabras y un emoji de fuego. El archivo existe, pesa cuarenta megas y la persona que lo recibió quiere saber si puede instalarlo.

La primera comprobación no necesita el archivo: necesita la conversación. Quién lo mandó, si la persona lo probó, si puede decir de dónde lo sacó. Si la respuesta es «me lo pasaron», la cadena se acaba ahí y la respuesta honesta es no.

La segunda comprobación tampoco necesita instalar nada: se mira el contenido del paquete sin ejecutarlo. Un visor de paquetes muestra el nombre real, la versión, el identificador y los permisos declarados. Con eso ya se sabe si es lo que dice ser y si pide lo que debería.

La tercera es la firma. Si el paquete declara ser la versión nueva de una app conocida, su firma tiene que coincidir con la de la app instalada. Cuando no coincide, hay dos posibilidades y las dos son malas: alguien reparte una copia modificada, o el autor cambió de llave. La segunda existe y es rara; la primera es lo habitual.

La cuarta es la que casi nadie hace y la que más información da: buscar el mismo paquete en su origen. Si la app es libre, su repositorio publica la versión con un número y una fecha; si esa versión no coincide con el archivo, el archivo no es esa versión. Dos minutos de búsqueda y se acabó la duda.

Con esas cuatro comprobaciones —la conversación, el contenido, la firma y el origen— se resuelve el caso entero sin instalar el archivo. Y si aun así se decide probarlo, se hace en un aparato que no tenga las cuentas de la casa, sabiendo que eso es una precaución, no una garantía.

Lo que no sirve, y conviene decirlo porque se hace mucho: pasarlo por un servicio de análisis en línea y quedarse tranquilo con el resultado. Esos servicios comparan con lo que ya conocen; un paquete nuevo, hecho para una sola persona, no aparece en ninguna lista el primer día.

───────────────────

*📌 Lo que hay que apuntar y dónde*

Una libreta, un archivo de texto o una nota en el teléfono: el formato da igual. Lo que importa es que exista, porque la memoria de estas cosas dura tres meses.

Cuatro datos por app que se instala fuera de la tienda: de dónde salió, con qué fecha, con qué firma y qué se esperaba de ella. Con esos cuatro, dentro de un año se puede reconstruir la decisión y, si algo falla, se sabe qué cambiar.

Un quinto dato, para las que se van a usar todos los días: dónde está guardado el APK que funciona. Una carpeta con cinco archivos y el número de versión en el nombre resuelve el día que el enlace desaparece, y ese día llega siempre.

La nota sirve además para lo que nadie espera: contar la historia a otra persona. Cuando alguien hereda el teléfono, o cuando hay que pedir ayuda, tener el registro ahorra media hora de explicaciones y evita que el que ayuda tome decisiones a ciegas.

───────────────────

*📊 Tabla, mitos y glosario*

*Las diez piezas, en una línea*

| Pieza | Qué verifica | Licencia | Empujón | Estrellas |
|---|---|---|---|---|
| Shizuku | presta el permiso de depuración | Apache-2.0 | 18-jun-2025 | ★32.590 |
| AppManager | firma, permisos y componentes | NOASSERTION (README GPL-3.0) | 30-oct | ★9.398 |
| FreeDroidWarn | pone en contexto los avisos | Apache-2.0 | 28-oct | ★3.731 |
| degoog | audita los servicios de Google | AGPL-3.0 | 29-oct | ★2.505 |
| Vanadium | navegador endurecido | sin licencia identificada | 30-oct | ★2.270 |
| hardened_malloc | asignador de memoria endurecido | MIT | hoy | ★2.048 |
| Camera | cámara sin servicios externos | MIT | 30-oct | ★1.423 |
| Auditor | atestación del aparato | MIT | 30-oct | ★729 |
| ytzero | cliente de video sin rastreo | Unlicense (ficha) y AGPL-3.0 (README) | 28-sep | ★671 |
| Gearslip | actualizar sin la tienda | AGPL-3.0 | 27-oct | ★232 |

*Cinco mitos de la cerradura*

**Mito uno: «candado verde, app segura».** El candado habla de la conexión. La firma habla del paquete. La atestación habla del aparato. Ninguna de las tres habla de la intención de nadie.

**Mito dos: «si es del autor, no hace falta comprobar nada».** Ayuda, y no sustituye la comprobación. Las cuentas se roban y las llaves se filtran; la huella del certificado es lo único que se puede comparar sin confiar.

**Mito tres: «el aviso del sistema es una condena».** Es una lista consultada en un momento. Puede llegar tarde y puede equivocarse de motivo.

**Mito cuatro: «la atestación demuestra que el teléfono está limpio».** Demuestra que el sistema es el que dice ser. Un aparato impecable puede tener tres apps que no debería.

**Mito cinco: «rootear es la única forma de auditar».** Shizuku y el permiso de depuración dan buena parte de lo que hace falta, y se revocan apagando un interruptor.

*Glosario de bolsillo*

**Firma** — certificado que acompaña al paquete y lo identifica ante el sistema.

**Huella** — resumen único del certificado. Es lo que se compara, no el nombre del autor.

**Atestación** — prueba criptográfica del estado del aparato, emitida con claves de hardware.

**Arranque abierto** — estado en el que el sistema permite cargar software no firmado por el fabricante.

**Permiso de depuración** — canal de administración que Android ofrece a los desarrolladores.

**Endurecimiento** — conjunto de defensas del sistema, como un asignador de memoria más estricto.

**Alfa** — versión temprana, con cambios frecuentes y fallos esperables.

───────────────────

*🔗 Enlaces y notas del corte*

Cada dirección se abrió hoy. Ninguna sale de una lista guardada.

*Atestación y auditoría*

- Auditor: https://github.com/GrapheneOS/Auditor
- AppManager: https://github.com/MuntashirAkon/AppManager
- Shizuku: https://github.com/RikkaApps/Shizuku

*El aparato endurecido*

- Vanadium: https://github.com/GrapheneOS/Vanadium
- Camera: https://github.com/GrapheneOS/Camera
- hardened_malloc: https://github.com/GrapheneOS/hardened_malloc

*Avisos, servicios y actualizaciones*

- FreeDroidWarn: https://github.com/woheller69/FreeDroidWarn
- degoog: https://github.com/degoog-org/degoog
- ytzero: https://github.com/Pelski/ytzero
- Gearslip: https://github.com/twinksoftware/Gearslip

*Lo que no se pudo medir.* La herramienta que muchas listas citan para pasar la comprobación de integridad del sistema devuelve hoy 404 en la dirección que se conocía: no hay repositorio que leer, así que no hay ficha, ni número, ni enlace. Se anota el hueco y se sigue, que es la única forma de no publicar de memoria.

*Cómo se midió.* Diez proyectos, tres lecturas cada uno y por tres caminos distintos: el buscador de la forja, la página del repositorio y el archivo crudo del README con su licencia. El orden de las lecturas se rotó de un proyecto al siguiente. Donde las tres no coincidieron —dos casos de licencia— se publicaron las dos versiones en vez de elegir.

───────────────────

*🌅 Cierre — tres cerraduras y ninguna es la puerta*

Lo que deja esta guía, en plata: el teléfono decide con tres criterios distintos y la gente los vive como uno. La firma dice quién hizo el paquete, la atestación dice qué sistema corre y el aviso del sistema habla de una lista que consulta en ese momento. Separarlas resuelve la mayoría de los sustos.

El hallazgo de hoy es que el aparato endurecido ya no es un experimento de laboratorio: hardened_malloc empujó esta mañana, el navegador sigue al motor casi al día y la cámara se actualiza. Y el hueco del día también cuenta: una herramienta que todas las listas citaban ya no está en su dirección, y la guía lo dice en vez de repetirla.

> —¿Y si el banco me cierra la puerta?
> —Entonces decides qué quieres tener, y lo decides sabiendo por qué.

💓 *La Bandita informa a partir de fuentes fechadas.* Una firma dice quién firmó; no dice quién responde.

*Medición del corte:* domingo 1 de noviembre de 2026, entre las 13:25 y las 13:40 de Santo Domingo · diez proyectos leídos tres veces con el orden rotado · dos fichas con licencia contradictoria o ausente se publican con lo que dicen sus fuentes · una herramienta sin repositorio legible queda fuera con su motivo.

*Licencia de esta entrega:* el texto va en CC BY-SA 4.0, los datos medidos en CC BY 4.0 y el código en MIT; la marca y el nombre de la casa quedan reservados para «Alexis (La Bandita)».

## 🗒️ Notas del corte

**Nota de corte (1-nov, 13:30):** las diez fichas son de esta tarde y llevan hora. Donde el release público no acompaña al trabajo reciente —Auditor, Camera, hardened_malloc— se escriben las dos fechas para que se vea la diferencia.

**Nota de hueco (1-nov):** la herramienta de integridad que citaban las listas viejas ya no existe en su dirección: 404. Se nombra como hueco y no como ficha. Es la misma regla aplicada a Phocid, a los parches de ReVanced y a InstallerX-Revived.

**Nota de alcance (1-nov):** esta guía no enseña a saltarse verificaciones ni a falsificar firmas. Explica qué comprueba el sistema y cómo leerlo, y deja dicho que modificar un aparato tiene consecuencias con algunas apps.

**Nota de corrección (1-nov):** la versión anterior de esta pieza se apoyaba en las herramientas de verificación de hace cuatro meses, incluida una que hoy no tiene repositorio. Se reescribió con el censo de esta tarde y se quitó lo que no se pudo leer.
