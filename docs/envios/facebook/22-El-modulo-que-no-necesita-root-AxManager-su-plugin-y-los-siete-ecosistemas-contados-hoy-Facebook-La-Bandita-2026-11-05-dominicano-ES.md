# PIEZA 22 · envío para Facebook

- **Pieza original:** `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/22-El-modulo-que-no-necesita-root-AxManager-su-plugin-y-los-siete-ecosistemas-contados-hoy-Facebook-La-Bandita-2026-11-05-dominicano-ES.md`
- **Fecha de la pieza:** 5-nov-2026 (según dateline; edad hoy: 2 días)
- **sha256 de la pieza:** `aa5251290d04e531b0a21c37cf5309cfdb369e2ceaf0c8c2cb9a18f5284169ac`
- **Envío generado:** 2026-11-07 · 20 mensajes · el mayor de 3319 caracteres
- **La pieza no se reescribe:** el cuerpo va íntegro; lo nuevo es la portada y el cierre.

═══ MENSAJE 1 de 20 · 1049 caracteres ═══

*El modulo que no necesita root AxManager su plugin y los siete ecosistemas contados hoy Facebook La Bandita 2026 11 05 dominicano ES*

La Bandita · pieza 22 · guía del 5-nov-2026 · te la mando hoy en 20 mensajes.

Antes de mandártela volví a medir lo que afirma: *24 repositorios, 22 vivos y 2 muertos*, más los enlaces de la pieza, revisados uno por uno hoy. Lo que salió está en el cierre, con la fecha al lado.

Licencias de lo que recomienda: GPL-3.0 11 · MIT 3 · sin licencia 3 · Apache-2.0 2.

⚠️ *Aviso de fecha:* este texto se escribió el 5-nov-2026. Todo lo que dice «hoy» dentro se refiere a ese día, no a este. La medición de hoy va al final, firmada y con su fecha.

La guía entera, ya guardada en el archivo: https://github.com/Alex17273747576777/la-bandita-archivo/blob/main/Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/22-El-modulo-que-no-necesita-root-AxManager-su-plugin-y-los-siete-ecosistemas-contados-hoy-Facebook-La-Bandita-2026-11-05-dominicano-ES.md

💓 7 de noviembre de 2026. Lo que no medí, lo digo: no lo medí.

═══ MENSAJE 2 de 20 · 3319 caracteres ═══

[Texto del 5-nov-2026: cuando dice «hoy», es ese día. La medición de hoy está al final.]

*El módulo que no necesita root: AxManager, su plugin que no es del todo un módulo y los siete ecosistemas contados hoy — cinco mil repositorios con etiqueta, un catálogo de ciento treinta y cinco del que noventa y seis llevan dos años sin tocarse, y una tienda que aquí no se enlaza*

*La Bandita · jueves 5 de noviembre de 2026, 11:05 de la mañana en Santo Domingo (15:05 UTC) · edición dominicano-español · pieza 22 de Facebook*

⏱️ *Lectura total: 24 minutos · un repositorio clonado y leído (13 MB) · veintiséis repositorios medidos uno por uno · un catálogo de módulos abierto y contado: 135 entradas · doce etiquetas de GitHub contadas · un manual de plugins leído hasta el final · cero tiendas enlazadas*

*🗺️ Mapa de esta guía*

```
├── 🧱 La semilla · el escaparate que no se enlaza
├── ⚡ En una página · 🕰️ la medición de las 11:05
├── 🔧 Qué es AxManager · un servidor que hace de root de mentira
├── 📦 El plugin que no es del todo un módulo · nueve archivos y un número
├── 🔐 La 3.0 y el certificado · por qué las apps viejas dejaron de conectar
├── 🌍 Siete ecosistemas · quién manda en cada uno y con qué licencia
├── 🗂️ Los catálogos · ciento treinta y cinco módulos y noventa y seis parados
├── 📉 El censo de las etiquetas · dónde vive de verdad un módulo
├── 🕳️ El agujero de AxManager · un tema con cinco repositorios
├── 🧨 La tienda que aquí no se enlaza · la regla y su motivo
├── 🧯 Abrir un módulo antes de instalarlo · seis comprobaciones
└── ❓ preguntas · 🌅 cierre · 🔗 enlaces · 🗒️ notas
```

*🧱 La semilla · el escaparate que no se enlaza*

Llega el encargo: una pieza sobre los módulos de AxManager y los otros ecosistemas que se encuentran en el escaparate de módulos más enlazado de la red. Trae además la orden de buscar páginas con contenido parecido. Las dos cosas se hacen aquí, con una excepción que hay que decir antes de la primera cifra: **ese escaparate no se enlaza en esta pieza**. No es un olvido ni una manía.

La casa tiene una regla escrita desde septiembre, y está en las compuertas que se ejecutan en cada publicación: **no se pega nunca un enlace a un reparto de APK modificados**. No es una regla contra la curiosidad. Es que un APK modificado es, por definición, un paquete que alguien recompiló y volvió a firmar, y cuyo contenido nadie audita; pegarlo en una guía que se lee en un teléfono es empujar a alguien a instalar algo que ni quien escribe ha abierto. Cuando la petición viene de arriba, la regla no cambia: cambia el modo de contarlo. Así que esta pieza hace lo contrario de copiar un escaparate: **va a las fuentes que se pueden medir** —los repositorios de los gestores, el código de los plugins, los catálogos oficiales y las etiquetas de GitHub— y cuenta lo que hay ahí. El resultado es más útil que la lista original, porque la lista original no dice cuántos módulos están vivos.

Y hay una segunda razón, que se ve al final del camino: **el ecosistema de módulos de Android no vive en un escaparate, vive en las etiquetas de GitHub y en tres catálogos, de los cuales dos están archivados y el tercero lleva dos años sin tocarse en su mayoría**. Buscar módulos en una tienda es buscar donde hay escaparate; el almacén está en otra parte.

⏬ sigue abajo · parte 1 de 19

═══ MENSAJE 3 de 20 · 2522 caracteres ═══

*⚡ En una página*

**Qué es AxManager.** Un entorno privilegiado para Android que arranca su propio servidor con los permisos de la consola de depuración —o de root si lo hay— y encima construye lo que su autor llama *plugins*: módulos con el mismo formato que los de Magisk y KernelSU, pero ejecutados por ese servidor y no por un demonio de root. Su repositorio tiene **1.553 estrellas**, licencia Apache-2.0, 147 bifurcaciones y una entrega `v3.0.0` fechada el 29 de octubre de 2026, una semana antes de este corte.

**Qué se verificó hoy.** Que los plugins de AxManager **no son módulos de Magisk aunque se llamen igual**: usan `module.prop`, `customize.sh`, `service.sh`, `post-fs-data.sh`, `system.prop` y `action.sh`, y su especificación añade un campo obligatorio —`axeronPlugin=30000`— que los módulos de Magisk no tienen. Que el proyecto **no tiene tienda**: en su repositorio hay un solo plugin de ejemplo, y el manual manda instalarlos con el botón «+» de la pantalla de plugins, a mano. Y que la versión 3.0 cambió el modelo de seguridad: el permiso se ata al **certificado de firma** de cada aplicación, no a su nombre de paquete.

**Lo que el censo dice del resto.** Se contaron doce etiquetas de GitHub: `magisk-module` **883** repositorios, `magisk` **1.535**, `kernelsu` **737**, `kernelsu-module` **196**, `apatch` **192**, `lsposed` **721**, `xposed-module` **570**, `zygisk` **97**, `shevery-modules` **8**, `axmanager` **5**, `axeron` **0** y `module-webui` **1**. El catálogo alterno de módulos —el más citado después de la tienda— publica **135 módulos**, de los cuales **2** se actualizaron en los últimos treinta días y **96** llevan más de dos años sin tocarse. La mediana de estrellas de ese catálogo es **21**.

**A quién sirve.** A quien tenga un teléfono de repuesto y quiera entender por qué «sin root» se ha vuelto una etiqueta que vende: AxManager, OmniShizuku y el propio Shizuku compiten por el mismo hueco, cada uno con una estrategia distinta. Y a quien haya descargado un módulo alguna vez de un escaparate y quiera aprender a abrirlo antes de instalarlo: la sección de las seis comprobaciones se puede hacer en diez minutos y no necesita instalar nada.

**El corte.** Todo lo de arriba está medido el **jueves 5 de noviembre de 2026 entre las 14:40 y las 15:05 UTC** (10:40 a 11:05 en Santo Domingo), contra la interfaz de GitHub, un clon de 13 MB del repositorio de AxManager y un catálogo público de módulos descargado y contado entrada por entrada.

⏬ sigue abajo · parte 2 de 19

═══ MENSAJE 4 de 20 · 2008 caracteres ═══

*🕰️ La medición de las 11:05 · clonar el gestor antes de hablar de sus módulos*

La fecha se comprobó en vivo al empezar y al cerrar. El reloj de fuera dio las **15:05 UTC**, que en Santo Domingo son las **11:05 de la mañana**. Ningún dato de esta pieza viene de otro artículo, de una captura ni de la memoria de quien escribe.

El orden fue este. **Primero** se buscó el nombre: «AxManager» devuelve en GitHub un repositorio principal, **115** repositorios donde la palabra aparece en el nombre, la descripción o el texto de presentación, y un tema con **5**. Ese desfase —115 menciones frente a 5 repositorios etiquetados— es el primer dato del día y ya dice algo: la mayoría de lo que existe alrededor de este gestor no está etiquetado, así que un catálogo por etiquetas nunca lo va a encontrar todo. **Segundo** se preguntó por los repositorios uno por uno: estrellas, bifurcaciones, incidencias abiertas, licencia, último empujón, última entrega, fecha de creación. **Tercero** se clonó el repositorio del gestor —`git clone --depth 1`, 13 MB— y se leyó su texto de presentación completo, el manual de plugins que vive dentro del proyecto y la carpeta de plugins de ejemplo. **Cuarto** se descargó el catálogo público de módulos del repositorio alterno y se contó: 135 entradas, cada una con su fecha de última actualización y sus estrellas. **Quinto** se contaron doce etiquetas de GitHub por su número de repositorios, que es la única forma de censar un ecosistema sin tienda.

Ese último paso merece una advertencia que vale para toda la pieza: **una etiqueta no es un catálogo**. Que 883 repositorios lleven `magisk-module` no significa que haya 883 módulos vivos: significa que 883 repositorios se etiquetaron así alguna vez, con cualquier estado, cualquier calidad y cualquier fecha. La cifra sirve para ordenar de magnitud, no para prometer inventario. Y como se ve más abajo, el catálogo que sí cuenta módulos uno por uno da un número mucho menor y mucho más frío.

⏬ sigue abajo · parte 3 de 19

═══ MENSAJE 5 de 20 · 3277 caracteres ═══

*🔧 Qué es AxManager · un servidor que hace de root de mentira*

El nombre completo es **Axeron Manager** y su proyecto lo describe así, en su propio texto: un entorno privilegiado para Android que corre con permisos de **ADB (shell)**, o con **root** cuando lo hay. La diferencia con un gestor de módulos normal está en la primera palabra: no es una aplicación que instala cosas, es una aplicación que **levanta un servidor** y luego vive de él.

**Cómo arranca.** Su manual lista seis formas de encender ese servidor, y esa lista es la mitad de su propuesta de valor: desde la propia aplicación si hay root; por depuración inalámbrica en Android 11 o superior, emparejando en el mismo teléfono sin ordenador; por depuración TCP con puerto configurable; desde un ordenador con una sola orden de consola; **desde el navegador**, por USB, en Chrome o Edge, sin instalar la consola de depuración; y por **OTG**, usando un teléfono como ordenador de otro. A eso se suma arranque al encender el aparato —con root, o por ADB en Android 11 o superior, marcado como experimental— y un registro de activación que va contando cada paso, para que un fallo diga dónde se paró en vez de quedarse en silencio.

**Qué hace con ese servidor encendido.** Cuatro bloques. **Privilegios por aplicación**: conceder o negar el acceso al servidor a cada aplicación instalada, con filtros para las instaladas, las del sistema y las que hablan la interfaz de Shizuku; y dentro de cada una, detener, limpiar caché, limpiar datos, desinstalar —incluidas las del sistema para el usuario actual—, tocar la optimización de batería, la actividad en segundo plano, los modos de permiso especiales y los permisos normales. **Plugins**, que es lo que interesa aquí. **Una consola** con órdenes guardadas como fragmentos y una pieza llamada `axsh` que lleva los mismos privilegios a cualquier aplicación de terminal. Y un **editor de ajustes** del sistema con búsqueda, edición y una lista de valores frecuentes para cambiar en un toque.

**La compatibilidad con Shizuku, que es la joya de la corona.** Las aplicaciones escritas contra la interfaz de Shizuku **se conectan a AxManager sin que Shizuku esté corriendo**. Algunas antiguas siguen exigiendo que la aplicación de Shizuku esté instalada —aunque no se ejecute—, y el propio gestor avisa cuando no lo está. Léase despacio: un gestor que se presenta como alternativa ofrece a las aplicaciones existentes el mismo enchufe, sin pedirles que cambien una línea. Es la misma jugada que la pieza anterior encontró dentro del paquete de OmniShizuku, por otro camino: allí se ocupaba el **nombre** de la aplicación; aquí se ocupa la **interfaz** que las aplicaciones llaman. El resultado para el usuario es parecido: el teléfono deja de necesitar el original.

**Un detalle de forma que dice mucho.** El proyecto tiene **1.553 estrellas**, **147 bifurcaciones**, **25 incidencias abiertas**, licencia **Apache-2.0**, está escrito en Kotlin y se creó el **17 de agosto de 2025**: quince meses de vida, no dos semanas. No es una promesa: es un proyecto que ya tiene historia, y su última entrega, `v3.0.0`, es del 29 de octubre de 2026. En un barrio donde casi todo lo que sale es de hace un mes, quince meses sin morirse es un dato.

⏬ sigue abajo · parte 4 de 19

═══ MENSAJE 6 de 20 · 3185 caracteres ═══

*📦 El plugin que no es del todo un módulo · nueve archivos y un número*

Aquí está el malentendido que conviene deshacer, porque es la razón por la que esta pieza existe. Un «módulo de AxManager» se llama plugin, se empaqueta como un zip y se instala como un módulo de Magisk. Pero no lo es, y las diferencias están escritas.

**Lo que comparte con un módulo de Magisk o de KernelSU.** Los archivos con los mismos nombres y el mismo papel: `module.prop` con la ficha, `customize.sh` para lo que se hace al instalar, `post-fs-data.sh` para lo que corre muy temprano, `service.sh` para lo que queda de fondo, `system.prop` para inyectar propiedades, `action.sh` para el botón de acción y `uninstall.sh` para lo que se hace al quitar. Si has escrito un módulo de Magisk, sabes escribir un plugin de AxManager: esa es la gracia y también el riesgo, porque invita a copiar y pegar módulos que no fueron escritos para este entorno.

**Lo que no comparte, y es lo que de verdad importa.** El manual de AxManager enumera su propio entorno: un **BusyBox completo** con modo autónomo, la orden `resetprop`, y seis variables de entorno con nombre propio —`AXERON`, `AXERONVER`, `AXERONDIR`, `AXERONBIN`, `AXERONXBIN` y `TMPDIR`—. Y una carpeta `system/bin` que se enlaza dentro de `$AXERONXBIN`, que está en el camino de búsqueda. Traducido: un plugin no trae sus propias herramientas y espera encontrarlas donde Magisk las pondría; trae sus binarios y AxManager los pone en el camino con otro nombre. Un módulo copiado tal cual de Magisk puede funcionar, o puede buscar una ruta que aquí no existe.

**El campo que lo separa todo.** En la carpeta de plugins de ejemplo del repositorio hay un plugin llamado `test_function` cuya ficha declara `axeronPlugin=30000`. Ese campo no existe en Magisk, y el propio proyecto explica para qué sirve: **marca la versión mínima de AxManager que el plugin necesita** —30000 es 3.0—. Un plugin sin ese campo no se instala. Es la forma más limpia de decir «esto no es un módulo de Magisk» que se puede escribir en un archivo de texto.

**La WebUI, compatible por los dos lados.** Los plugins pueden traer interfaz web, y esa interfaz tiene **dos puentes**: el del gestor, con su propia API, y el de KernelSU, que AxManager imita para que los plugins escritos para ese ecosistema funcionen. Además, la WebUI de un plugin **solo ve sus propias páginas**: cualquier otro sitio se abre en el navegador y no alcanza esas APIs. Y la WebUI se puede fijar en la pantalla de inicio con su nombre y su icono, como si fuera una aplicación.

**El ciclo de vida, que es la parte seria.** Cada proceso que arranca un plugin —desde sus guiones, su acción o su WebUI— lleva una marca `AXERON_PLUGIN=<id>`. Al desactivar o quitar el plugin, el gestor **detiene todos esos procesos**, demonios incluidos: primero una señal de terminación, y a los tres segundos, una señal de muerte. Los guiones de arranque y de desinstalación pueden bloquear como mucho **cuarenta segundos**, y lo que imprimen queda en la carpeta de registros del propio gestor. Quien haya intentado apagar un demonio lanzado por un módulo de Magisk sabe cuánto vale esa promesa.

⏬ sigue abajo · parte 5 de 19

═══ MENSAJE 7 de 20 · 2073 caracteres ═══

*🔐 La 3.0 y el certificado · por qué las apps viejas dejaron de conectar*

La entrega `v3.0.0`, del 29 de octubre, no es una versión con más funciones: el propio proyecto la anuncia como **una versión de seguridad**, y merece el párrafo porque cambia lo que significa «dar permiso».

**Antes.** Un permiso se daba a una aplicación, y punto. **Ahora.** Cada aplicación recibe su **propio acceso al servidor**, atado a su **certificado de firma**, y ese acceso desaparece en el momento en que se revoca. El gestor lo dice con una frase que hay que leer dos veces: un permiso pertenece al certificado de la aplicación, así que **la misma aplicación firmada con otra clave —o otra aplicación que más tarde herede su identificador de usuario— tiene que pedirlo de nuevo**.

**Por qué eso importa.** En Android, el identificador de una aplicación puede acabar en manos de otra cuando se desinstala y se reinstala algo con el mismo nombre, o cuando alguien publica una aplicación con el identificador de otra. Atar el permiso al certificado cierra esa puerta: el permiso no viaja con el nombre, viaja con la firma. En una aplicación que puede detener procesos y tocar los ajustes del sistema, esa diferencia es la que separa un permiso de un descuido.

**La consecuencia incómoda, que el proyecto también dice.** Las aplicaciones construidas sobre la interfaz propia de Axeron anteriores a la 3.0 **ya no pueden conectar**; las que usan la interfaz de Shizuku **no se ven afectadas**. Es decir: la versión de seguridad rompió su propia compatibilidad hacia atrás para no romper la ajena. Y hay un detalle que completa el cuadro: la pantalla de inicio muestra una **insignia de firma** —coincide, no coincide, o sin verificar— que dice si el servidor que está corriendo lo arrancó *este* AxManager, identificado por su certificado y no por su nombre de paquete. Es la misma lección de la pieza anterior, contada al revés: allí se midió un paquete que cambia de firma en cada compilación; aquí, un proyecto que hace de la firma el eje de su seguridad.

⏬ sigue abajo · parte 6 de 19

═══ MENSAJE 8 de 20 · 2617 caracteres ═══

*🌍 Siete ecosistemas · quién manda en cada uno y con qué licencia*

Un módulo de Android necesita dos cosas: un gestor que lo ejecute y un sitio del que salga. Los gestores medidos hoy, con sus números delante y la fecha al lado:

```
Magisk               topjohnwu/Magisk          ★63.786  GPL-3.0    v31.1      25-oct-2026
KernelSU             tiann/KernelSU            ★20.128  GPL-3.0    v3.3.1     12-oct-2026
KernelSU-Next        KernelSU-Next             ★ 4.732  GPL-3.0    v3.4.2     13-oct-2026
APatch               bmax121/APatch            ★ 8.129  GPL-3.0    11282      15-oct-2026
SukiSU-Ultra         SukiSU-Ultra              ★ 6.898  GPL-3.0    v4.3.0-r1   3-nov-2026
BakaSU               Baka-SU/BakaSU            ★ 2.111  GPL-3.0    —          4-nov-2026
AxManager            fahrez182/AxManager       ★ 1.553  Apache-2.0 v3.0.0     29-oct-2026
```

**Lo primero que salta a la vista: casi todo es GPL-3.0 y todo está vivo.** Los seis gestores de root se movieron en las últimas tres semanas; AxManager es el único que no necesita root para funcionar —aunque lo aproveche si lo hay— y es también el único con licencia Apache-2.0, que permite reutilizar su código en proyectos cerrados.

**El árbol, en una línea por rama.** **Magisk** es el abuelo: define el formato del módulo y su repositorio tiene sesenta y tres mil estrellas. **KernelSU** es la rama que mete el privilegio en el núcleo, y de ella salieron **KernelSU-Next**, **SukiSU-Ultra** y **BakaSU**, tres bifurcaciones con entregas de este mes. **APatch** es la rama que parchea el núcleo sin recompilarlo del todo. Y **AxManager** es la rama que no toca el núcleo: se queda en el servidor de la consola de depuración.

**Lo que esto significa para quien busca módulos.** Que un módulo escrito para Magisk puede no funcionar en KernelSU, y viceversa, aunque el archivo se llame igual y tenga los mismos guiones. Que las tres bifurcaciones de KernelSU se mueven a distinta velocidad —SukiSU entrega esta semana, BakaSU empuja a diario—. Y que el ecosistema de módulos sin root, el de AxManager, es el más pequeño de todos por una razón de fecha: nació en agosto de 2025, cuando los otros llevaban siete años.

**Y una nota sobre el lenguaje, que no es un detalle.** «Módulo» en este barrio significa una cosa muy concreta —un zip con `module.prop` y guiones— y por eso los cuatro gestores pueden llamar igual a cosas que no son iguales. Cuando alguien te venda «el módulo que lo hace todo sin root», la primera pregunta no es qué hace: es **qué gestor lo va a ejecutar**, porque de eso depende que arranque.

⏬ sigue abajo · parte 7 de 19

═══ MENSAJE 9 de 20 · 2756 caracteres ═══

*🗂️ Los catálogos · ciento treinta y cinco módulos y noventa y seis parados*

Aquí está el dato que cambia la pieza, y sale de contar, no de leer. El catálogo público de módulos del repositorio alterno —el más citado después del escaparate— se descargó y se contó entrada por entrada. Lo que hay:

```
entradas en el catálogo            135
con identificador                    135  (todas)
primera actualización          21-ago-2020
última actualización           28-oct-2026
actualizados en los últimos 30 días    2
actualizados en los últimos 90 días    7
actualizados en los últimos 180 días  13
actualizados en el último año         23
sin tocar en más de dos años          96   (71 %)
estrellas: máximo 509 · mediana 21
```

**Léelo otra vez.** Un catálogo de ciento treinta y cinco módulos en el que **dos** se han tocado este mes y **noventa y seis** llevan más de dos años quietos. La mediana de estrellas es 21, y el más popular tiene 509. No es un almacén: es un museo con la puerta abierta.

**Y eso es lo que hay detrás de los escaparates.** La tienda que originó esta pieza no publica un catálogo auditable en un repositorio; publica páginas. El catálogo que sí se puede auditar tiene esos números. Cuando alguien dice «hay miles de módulos», la respuesta honesta es: hay miles de **repositorios etiquetados** —883 con `magisk-module`, 1.535 con `magisk`— y hay un catálogo curado de **135**, del que la mayoría está parado. Las dos cifras son ciertas y no dicen lo mismo.

**Los otros dos catálogos, y su estado.** El gestor de módulos **MMRL** —2.237 estrellas, GPL-3.0, actualizado el 25 de octubre— sigue vivo y es el único de los tres que se mueve: carga catálogos de varios repositorios y los presenta en una aplicación. **FoxMMM**, el gestor de módulos que nació cuando la aplicación oficial dejó de buscarlos, tiene 2.208 estrellas y está **archivado desde mayo de 2023**. **MRepo**, el que servía a Magisk, KernelSU y APatch a la vez, tiene 1.118 estrellas y está **archivado desde julio de 2024**. Y **Androidacy**, que heredó el primero y hoy sostiene el escaparate, tiene 1.240 estrellas, licencia LGPL-3.0, su última entrega en **marzo de 2025** y su último cambio en **abril de 2026**: medio año sin publicar nada.

**La lectura, sin adornos.** De cuatro gestores de catálogo —FoxMMM, MRepo, Androidacy y MMRL—, **dos están archivados, uno publica cada año y medio y uno está vivo**. El ecosistema no está sano porque tenga muchas estrellas: está sano en los gestores de root, que se actualizan cada semana, y débil justo en la capa que sirve para **descubrir** módulos. Es la consecuencia lógica: si los módulos se han vuelto pocos y viejos, la aplicación para buscarlos no tiene nada que buscar.

⏬ sigue abajo · parte 8 de 19

═══ MENSAJE 10 de 20 · 2106 caracteres ═══

*📉 El censo de las etiquetas · dónde vive de verdad un módulo*

Si los catálogos están así, ¿dónde están los módulos? En repositorios sueltos, cada uno con su nombre, encontrados por búsqueda o por etiqueta. El censo de hoy, contado con doce consultas a la interfaz de GitHub:

```
magisk              1.535      magisk-module        883
kernelsu              737      kernelsu-module      196
apatch                192      lsposed              721
xposed-module         570      zygisk                97
shevery-modules         8      axmanager              5
axeron                  0      module-webui           1
```

**Cómo se lee esto.** Las etiquetas grandes —`magisk`, `kernelsu`, `lsposed`, `xposed-module`— son de proyectos que llevan años existiendo: hay 721 repositorios con `lsposed` y 570 con `xposed-module`, que son el mismo barrio de módulos que enganchan código en otras aplicaciones. Las etiquetas pequeñas son las nuevas: **`shevery-modules` tiene 8** —es el catálogo de módulos del proyecto que se midió en la pieza anterior, el que se instala por zips de tipo Magisk pero corre sobre un gestor sin root—, `axmanager` tiene **5** y `axeron` tiene **0**.

**El dato que hay que subrayar: `axeron` está a cero.** El nombre técnico del gestor, el que aparece en sus variables de entorno y en su interfaz, no lo usa nadie como etiqueta. Y `module-webui`, la etiqueta de los módulos con interfaz web, tiene **1**. Es decir: la función que AxManager presume —WebUI con dos puentes de JavaScript— es tan nueva en este barrio que no hay etiqueta que la agrupe.

**El desfase que hay que contar.** Buscar «axmanager» en el nombre, la descripción o el texto de presentación devuelve **115** repositorios; etiquetados hay **5**. Veintitrés veces más menciones que etiquetas. Cualquier catálogo que se construya sólo con etiquetas va a encontrar una de cada veintitrés. Y de esos repositorios, la mayoría son plugins sueltos de una persona, con una descripción, sin licencia y sin entregas: el tipo de cosa que un escaparate muestra y un catálogo no puede sostener.

⏬ sigue abajo · parte 9 de 19

═══ MENSAJE 11 de 20 · 2994 caracteres ═══

*🕳️ El agujero de AxManager · un tema con cinco repositorios*

Vale la pena mirar de cerca ese cinco, porque es la respuesta a la pregunta con la que empezó todo: ¿dónde están los módulos de AxManager?

**No hay tienda.** El repositorio del gestor trae una carpeta `plugins` con **un solo plugin**, `test_function`, que no sirve para nada útil: es una prueba que recorre todo el entorno y la API de la WebUI y va escribiendo resultados `[PASS]` y `[FAIL]` en una carpeta de informes. Su propio texto lo dice: sirve para comprobar que el entorno está completo. El manual manda instalar los plugins con el botón «+» de la pantalla de plugins y volver a encenderlos.

**Lo que hay fuera, medido uno por uno.** Cinco repositorios que se presentan como colecciones o piezas del ecosistema:

```
magiskap/axmanager-plugin        ★12  sin licencia    último empujón 8-ago-2026 · madurez: colección de una persona
abysssnare/Axmanager-modle       ★28  MIT            v2.1.0 · 12-sep-2026 · madurez: entrega de hace dos meses
ScarletHanami/Network_Enhance    ★25  MIT            v1.1.6 · 29-jul-2026 · madurez: módulo único, tres meses
corvexis/Axora                   ★19  Apache-2.0     26.10.21 · 21-oct-2026 · madurez: bifurcación de 15 días
bufanchen121101/AxManagerD       ★51  NOASSERTION    31-oct-2026 · madurez: creado 18-ago-2026, sin licencia clara
```

**Qué es cada uno.** `axmanager-plugin` se anuncia como «la mayor colección de plugins sin root para AxManager» y **no declara licencia**: doce estrellas y un último cambio de hace tres meses. `Axmanager-modle` dice tener **treinta herramientas de sistema** con interfaz web y licencia MIT. `Network_Enhance` es un módulo de red con dos funciones concretas —degradar de una señal falsa de 5G a 4G y fijar LTE en modo juego— y licencia MIT. `Axora` es una bifurcación declarada del gestor «orientada al minimalismo», con licencia Apache-2.0 y entrega del 21 de octubre. Y `AxManagerD` es un proyecto chino que se presenta como marco modular sin root con inyección de tipo Xposed y seguimiento de guiones por inteligencia artificial: 51 estrellas, licencia que GitHub no reconoce y dos meses y medio de vida.

**La conclusión, que es la noticia de esta pieza.** El ecosistema de módulos de AxManager, hoy, son **cinco repositorios y un plugin de ejemplo**, y de esos cinco, **uno no declara licencia**, **uno no tiene licencia reconocible** y dos son colecciones de una sola persona. No hay un catálogo, no hay un índice, no hay un escaparate propio: hay que buscarlos a mano y confiar en el que los publicó. Frente a los 883 repositorios etiquetados de Magisk o a los 135 módulos del catálogo alterno, esto es un barrio en obras.

**Y por eso el escaparate era tentador.** Porque un sitio que reúne plugins en páginas resuelve justo lo que falta: descubrimiento. Pero lo resuelve sin lo otro, que es lo que aquí no se puede dar por bueno: quién compiló ese zip, con qué firma, y si su código se puede leer.

⏬ sigue abajo · parte 10 de 19

═══ MENSAJE 12 de 20 · 1992 caracteres ═══

*🧨 La tienda que aquí no se enlaza · la regla y su motivo*

Conviene ser explícito, porque la petición venía con un enlace y esta pieza va sin él.

**La regla.** La casa tiene escrito, entre sus compuertas de forma, que **no se pega un enlace a un reparto de APK modificados**. Ni en el cuerpo, ni en los enlaces, ni en una nota al pie «por si acaso». La comprobación se ejecuta en cada publicación y busca enlaces directos a ese tipo de reparto.

**El motivo, en tres razones que no son morales sino prácticas.** **Primera:** un APK modificado es un paquete que alguien descompiló, tocó y volvió a firmar; su contenido no lo ha auditado nadie, y una guía que se lee en un teléfono no puede pedirle a quien la lee que haga esa auditoría. **Segunda:** esos paquetes no se actualizan por la tienda del sistema, así que o se quedan viejos para siempre o se actualizan bajando otra vez de la misma página, con otra firma y sin historial. **Tercera:** el que firma no es el autor del programa original, de modo que cualquier cosa que ese paquete pida —permisos, accesos, cuentas— la concede el usuario a alguien que no escribió el programa.

**Lo que sí se puede hacer, y se hace aquí.** Nombrar los ecosistemas y dar sus repositorios oficiales, que es de donde salen los módulos que luego aparecen en esas páginas. Un módulo de Magisk vive en un repositorio de GitHub con su `module.prop`, su licencia y su historial de cambios; la página que lo muestra es una copia con mejor tipografía. Si te interesa un módulo, busca su nombre en GitHub antes de bajarlo de ninguna parte: si el módulo es serio, existe allí. Si sólo existe en la página, eso ya es la respuesta.

**Y una excepción que no es una excepción.** Hay módulos que no tienen repositorio público porque su autor sólo publica zips. En ese caso la regla no cambia: no se enlaza. Se dice «existe, se llama así, búscalo por su nombre» y se sigue. La casa prefiere perder un enlace a ganar un teléfono ajeno.

⏬ sigue abajo · parte 11 de 19

═══ MENSAJE 13 de 20 · 2653 caracteres ═══

*🧯 Abrir un módulo antes de instalarlo · seis comprobaciones*

Esto es lo que de verdad se lleva uno de esta pieza, y se puede hacer con un teléfono y sin instalar nada. Un módulo es un zip: se abre con cualquier gestor de archivos.

**Uno: la ficha.** Dentro hay un `module.prop`, un archivo de texto con cinco o seis líneas: `id`, `name`, `version`, `versionCode`, `author`, `description`. Se lee entero. Si el `id` no coincide con la carpeta que lo contiene, ese módulo no se instalará bien en la mitad de los gestores. Si el `author` no coincide con el nombre del repositorio del que lo bajaste, algo cambió de manos.

**Dos: los guiones, y qué hacen.** `customize.sh` es lo que corre al instalar. `service.sh` es lo que queda corriendo para siempre. `post-fs-data.sh` es lo que corre antes que casi todo. Tres archivos de texto que se leen en dos minutos, y en los que hay dos cosas que buscar: **llamadas a la red** —`curl`, `wget`, cualquier dirección— y **rutas absolutas** hacia sitios que no son del módulo. Un módulo legítimo de cambio de fuente o de propiedades del sistema no necesita hablar con internet.

**Tres: lo que trae dentro.** `system/bin`, `system/etc`, bibliotecas `.so`, archivos `.apk`. Si el módulo dice ser un ajuste de sonido y lleva un ejecutable de 20 MB, eso hay que explicarlo antes de instalarlo, no después.

**Cuatro: la firma del zip.** Muchos módulos no van firmados, y eso no es un delito; pero si el módulo va firmado y la firma no es la misma entre la versión 1 y la versión 2, es que lo firmó alguien distinto. Se compara con el mismo método que se usó en la pieza anterior con dos paquetes de Android: extraer el certificado y mirar si es igual.

**Cinco: la dirección de actualización.** Los módulos pueden declarar en su ficha un archivo `update.json` desde el que el gestor consulta si hay versión nueva. Si esa dirección no es del repositorio del autor, ese módulo no se actualiza solo: se actualiza desde donde diga otro.

**Seis: el botón de deshacer.** Antes de instalar, se sabe cómo se quita. En Magisk y en KernelSU es desactivar el módulo y reiniciar. En AxManager es desactivar el plugin —y ahí el gestor promete algo que conviene apuntar: al desactivarlo, **mata todos los procesos que ese plugin arrancó**, con terminación y luego muerte a los tres segundos—. Saber esto antes es la diferencia entre probar algo y quedarse con algo.

**Y una advertencia de orden.** Un módulo que toca el sistema se prueba en un aparato de repuesto. No por prudencia de folleto: porque si el arranque falla, el teléfono no enciende y no hay aplicación que lo arregle desde dentro.

⏬ sigue abajo · parte 12 de 19

═══ MENSAJE 14 de 20 · 1598 caracteres ═══

*🚫 Lo que no está verificado · deuda con nombre*

**No se ha instalado AxManager.** Ni en un teléfono ni en un emulador. Todo lo que se cuenta de su comportamiento —el arranque por navegador, la marca de procesos, la insignia de firma— viene de su documentación y de su código, no de haberlo ejecutado.

**No se ha instalado ningún plugin.** Se ha leído la ficha del plugin de ejemplo y las de cinco colecciones ajenas. Ninguna se ha puesto en un teléfono.

**No se ha auditado el código de ningún módulo.** Se describe el método para hacerlo —las seis comprobaciones— y no se ha aplicado a ninguno de los cinco repositorios del ecosistema de AxManager. Eso queda como tarea.

**No se ha visitado el escaparate.** Por la regla del apartado 🧨: no se abre ni se enlaza. Lo que se dice de él es lo que se sabe de su familia —que es una tienda que reparte paquetes modificados—, no una medición de sus páginas.

**Las etiquetas son un censo imperfecto y así se ha contado.** Los números de `magisk-module` (883) y compañía son repositorios etiquetados, no módulos vivos. La pieza lo repite dos veces porque es la diferencia entre una cifra y un inventario.

**No se ha comprobado qué módulos del catálogo alterno siguen funcionando.** Se ha contado su fecha de última actualización y sus estrellas; si un módulo de 2021 sigue funcionando en Android 16 es otra pregunta, y esa pide un teléfono.

**No se ha medido la tienda que el encargo traía.** Su inventario, sus categorías y sus números no están aquí porque no se ha entrado. Es una ausencia declarada, no un olvido.

⏬ sigue abajo · parte 13 de 19

═══ MENSAJE 15 de 20 · 3242 caracteres ═══

*❓ preguntas*

**¿Un plugin de AxManager es un módulo de Magisk?** Se parece y no lo es. Comparte los nombres de los archivos y el formato del zip, pero su especificación exige un campo que Magisk no tiene (`axeronPlugin`), su entorno tiene variables y rutas propias, y lo ejecuta un servidor de usuario shell en vez de un demonio de root. Un módulo copiado puede funcionar; no se puede dar por hecho.

**¿Necesito root para AxManager?** No. Arranca su servidor con permisos de consola de depuración —por depuración inalámbrica en Android 11 o superior, por cable, por navegador o por OTG— y, si hay root, lo aprovecha. Es de los pocos de su barrio que se puede usar sin desbloquear el cargador de arranque.

**¿Por qué no enlazas la tienda que te mandaron?** Porque la casa no pega enlaces a repartos de APK modificados, y esa regla no distingue entre encargos. El motivo está en el apartado 🧨 y es práctico: nadie audita esos paquetes, no se actualizan por el sistema y los firma quien no escribió el programa.

**¿Entonces dónde busco módulos?** En el repositorio del gestor que vayas a usar, en el catálogo alterno —135 módulos, con la advertencia de que 96 están parados— y en las etiquetas de GitHub. Y antes de instalar, las seis comprobaciones.

**¿Qué pasa con las aplicaciones que usan Shizuku?** Que AxManager ofrece la misma interfaz, así que se conectan sin que Shizuku esté corriendo. Algunas antiguas siguen pidiendo que la aplicación de Shizuku esté instalada, aunque no se ejecute.

**¿La versión 3.0 rompe algo?** Sí, y su autor lo dice: las aplicaciones escritas contra la interfaz propia de Axeron anteriores a la 3.0 ya no conectan. Las de Shizuku no se ven afectadas. A cambio, cada permiso queda atado al certificado de firma de la aplicación.

**¿Y los módulos viejos del catálogo alterno, sirven?** Sirven para leer cómo se escribía un módulo y para ver qué se hacía con `resetprop` hace cinco años. Para instalar en un Android de 2026, la fecha de última actualización manda: 96 de 135 llevan más de dos años quietos.

**¿Por qué hay 883 repositorios con `magisk-module` y sólo 135 en el catálogo?** Porque una etiqueta la pone cualquiera, incluido un repositorio vacío, un experimento o una copia. Un catálogo pide una ficha, un autor y un archivo que descargar. La diferencia entre 883 y 135 es la diferencia entre etiquetarse y estar.

**¿Cuál es entonces el ecosistema más vivo?** Los gestores de root: Magisk, KernelSU, KernelSU-Next, SukiSU-Ultra, APatch y BakaSU se movieron todos en las últimas tres semanas. La capa de descubrimiento es la que está débil: dos catálogos archivados, uno que publica cada año y medio y uno vivo.

**¿Vale la pena AxManager hoy?** Para mirar cómo se construye un gestor sin root con quince meses de historia y una versión de seguridad reciente, sí. Para el teléfono de todos los días, con cinco repositorios de plugins y ninguno con licencia clara salvo dos, conviene esperar a que el barrio crezca.

**¿Y el módulo de ejemplo del repositorio?** `test_function` no es un módulo para usar: es una prueba que recorre el entorno y escribe `[PASS]` y `[FAIL]`. Sirve para aprender cómo se escribe un plugin leyendo uno que funciona, y para nada más.

⏬ sigue abajo · parte 14 de 19

═══ MENSAJE 16 de 20 · 2485 caracteres ═══

*🌅 Cierre · lo que hay que llevarse*

Lo primero: **«módulo» es una palabra que ya no significa una sola cosa**. Cuatro gestores comparten el formato y ninguno comparte el entorno. Antes de instalar, la pregunta no es qué hace el módulo: es quién lo va a ejecutar.

Lo segundo: **AxManager existe y no es una promesa de dos semanas**. Quince meses, 1.553 estrellas, una versión 3.0 que cambió el modelo de permisos para atarlos al certificado de firma, y una compatibilidad con la interfaz de Shizuku que le abre la puerta a las aplicaciones que ya existen. Eso es más de lo que tienen casi todos los proyectos de este barrio.

Lo tercero: **su ecosistema de plugins es un barrio en obras**. Cinco repositorios, un plugin de ejemplo, una etiqueta con cinco entradas y otra con cero. Quien busque plugins de AxManager va a tener que buscarlos uno por uno y leerlos, y eso —leerlos— es exactamente lo que hay que hacer de todos modos.

Lo cuarto: **los catálogos están en peor estado que los módulos**. Dos archivados, uno que publica cada año y medio, y un catálogo curado de 135 entradas con 96 sin tocar desde hace más de dos años. Cuando alguien te venda un escaparate con miles de módulos, la pregunta que ordena todo es una: ¿cuántos de esos se actualizaron este año. La respuesta, en el único catálogo que se puede contar, es 23.

Y lo quinto, que es la razón por la que no hay un enlace al final: **un módulo se juzga por lo que trae dentro, no por la página que lo enseña**. Seis comprobaciones, diez minutos y un gestor de archivos. Eso no lo hace ninguna tienda por ti.

— Cuatro gestores, cuatro entornos: el mismo zip no es el mismo módulo según quién lo ejecute.
— Ciento treinta y cinco módulos en el catálogo más citado, y noventa y seis llevan dos años sin que nadie los abra.

💓 *La Bandita informa a partir de fuentes fechadas.* un gestor clonado y leído, veintiséis repositorios medidos uno por uno, un catálogo contado entrada por entrada y doce etiquetas censadas. Sin enlazar una sola tienda de paquetes modificados, y explicando por qué.

*Medición del corte:* jueves 5 de noviembre de 2026, 11:05 de la mañana en Santo Domingo (15:05 UTC) · un repositorio clonado (13 MB) · veintiséis repositorios medidos con estrellas, licencia, último empujón y última entrega · un catálogo de 135 módulos descargado y contado con sus fechas y sus estrellas · doce etiquetas de GitHub censadas · cero tiendas enlazadas · cero cifras de memoria.

⏬ sigue abajo · parte 15 de 19

═══ MENSAJE 17 de 20 · 1778 caracteres ═══

*🔗 Enlaces*

*El gestor y su ecosistema, medidos hoy:*

- AxManager, el repositorio y el texto donde se explica todo: https://github.com/fahrez182/AxManager
- Axeron-API, el puente para las aplicaciones: https://github.com/fahrez182/Axeron-API
- Axora, la bifurcación minimalista: https://github.com/corvexis/Axora
- la colección de treinta plugins: https://github.com/abysssnare/Axmanager-modle
- el módulo de red con dos funciones: https://github.com/ScarletHanami/Network_Enhance
- el marco modular sin root, en chino: https://github.com/bufanchen121101/AxManagerD

*Los gestores, uno por uno:*

- Magisk, el abuelo: https://github.com/topjohnwu/Magisk
- KernelSU: https://github.com/tiann/KernelSU
- KernelSU-Next: https://github.com/KernelSU-Next/KernelSU-Next
- SukiSU-Ultra: https://github.com/SukiSU-Ultra/SukiSU-Ultra
- APatch: https://github.com/bmax121/APatch
- BakaSU: https://github.com/Baka-SU/BakaSU

*Los catálogos y los buscadores:*

- el catálogo alterno, con sus 135 módulos: https://github.com/Magisk-Modules-Alt-Repo/json
- las normas para enviar un módulo a ese catálogo: https://github.com/Magisk-Modules-Alt-Repo/submission
- MMRL, el único buscador vivo: https://github.com/MMRLApp/MMRL
- FoxMMM, archivado en 2023: https://github.com/Fox2Code/FoxMagiskModuleManager
- MRepo, archivado en 2024: https://github.com/MRepoApp/MRepo
- el gestor de la tienda que aquí no se enlaza: https://github.com/Androidacy/MagiskModuleManager

*El barrio de los módulos que enganchan código, para entender el censo:*

- LSPosed: https://github.com/LSPosed/LSPosed
- Vector, su bifurcación viva: https://github.com/JingMatrix/Vector
- ZygiskNext: https://github.com/Dr-TSNG/ZygiskNext
- TrickyStore: https://github.com/5ec1cff/TrickyStore

⏬ sigue abajo · parte 16 de 19

═══ MENSAJE 18 de 20 · 3049 caracteres ═══

*🗒️ Notas al pie*

(5-nov) **La fecha, en vivo.** Comprobada al empezar y al cerrar. Reloj de fuera: 15:05 UTC, 11:05 en Santo Domingo. La medición de los repositorios se hizo entre las 14:40 y las 15:05 UTC del mismo día.

(5-nov) **El catálogo, contado y no citado.** Se descargó el archivo del catálogo alterno y se contaron sus entradas una por una: 135, todas con identificador. Las fechas de actualización van en milisegundos en el archivo y se convirtieron a fecha legible; el reparto por tramos —2 en treinta días, 7 en noventa, 13 en ciento ochenta, 23 en un año, 96 con más de dos años— sale de esa misma lista.

(5-nov) **Las doce etiquetas.** Se consultaron una a una y se anotó el total de repositorios que devuelve cada una. No se filtró nada: lo que devuelve la consulta es lo que aparece. `axeron` devolvió cero y así se escribe.

(5-nov) **Lo del campo `axeronPlugin`.** Está en la ficha del plugin de ejemplo del propio repositorio, con valor 30000, y el texto de la carpeta de plugins explica que el guion de empaquetado comprueba `module.prop` con las reglas del instalador: patrón del identificador, `versionCode` numérico, `axeronPlugin` y que el identificador coincida con el nombre de la carpeta.

(5-nov) **Lo de la versión 3.0.** El texto de presentación del proyecto la anuncia como versión de seguridad y explica tres cosas que se citan aquí: que cada aplicación recibe su propio acceso atado a su certificado de firma, que las aplicaciones anteriores a la 3.0 construidas sobre la interfaz propia dejan de conectar, y que las de la interfaz de Shizuku no se ven afectadas.

(5-nov) **Lo que no se abrió.** La tienda que originó el encargo no se ha visitado, por la regla del apartado 🧨. No hay en esta pieza ninguna cifra suya, ni de inventario ni de categorías, porque no se ha entrado a contarlas. Es una ausencia declarada.

(5-nov) **El plugin de ejemplo.** `test_function` declara la versión mínima 3.0 y escribe sus resultados en una carpeta de informes dentro del directorio del plugin. No modifica el sistema: comprueba que el entorno funciona. Se cita como muestra del formato, no como módulo recomendable.

*#task*

#task 103 · abrir los cinco repositorios de plugins de AxManager con las seis comprobaciones de esta pieza y anotar en un acta qué llama a la red, qué escribe fuera de su carpeta y qué licencia declara cada uno de verdad.

#task 104 · instalar el plugin de ejemplo `test_function` en un aparato de repuesto y recoger sus informes de `[PASS]` y `[FAIL]`: es la única forma de saber qué partes del entorno funcionan en un teléfono real y no sólo en el texto.

#task 105 · repetir el censo de etiquetas dentro de un mes —3 de diciembre de 2026— para ver si `axmanager` crece de cinco, si `axeron` deja de estar a cero y si el catálogo alterno pasa de dos actualizaciones mensuales.

#task 106 · escribir la ficha de AxManager en el catálogo del archivo, con su guía y su estado, y la advertencia de que sus plugins no son módulos de Magisk en la primera línea útil.

⏬ sigue abajo · parte 17 de 19

═══ MENSAJE 19 de 20 · 3173 caracteres ═══

💓 *EL ESTADO DE HOY · pieza 22*

Medí otra vez, hoy 7 de noviembre de 2026, los 24 repositorios que cita esta pieza, con la API de GitHub. Lo que sigue es lo que devolvió, no lo que decía la pieza:

• system/bin — *muerto*: el repositorio responde 404 hoy. Se nombra para esquivarlo, no se recomienda.
• system/etc — *muerto*: el repositorio responde 404 hoy. Se nombra para esquivarlo, no se recomienda.
• fahrez182/AxManager — ★1.555 · empujó el 1-nov-2026 (hace 6 días) · Apache-2.0 · última release v3.0.0 (29-oct-2026)
• fahrez182/Axeron-API — ★22 · empujó el 1-nov-2026 (hace 6 días) · MIT · última release 3.0.0 (29-oct-2026)
• corvexis/Axora — ★19 · empujó el 21-oct-2026 (hace 17 días) · Apache-2.0 · última release 26.10.21 (21-oct-2026)
• abysssnare/Axmanager-modle — ★29 · empujó el 5-oct-2026 (hace 33 días) · MIT · última release v2.1.0 (12-sep-2026)
• ScarletHanami/Network_Enhance — ★25 · *dormido*: sin empujar desde el 29-jul-2026 (101 días) · MIT · última release v1.1.6 (29-jul-2026)
• bufanchen121101/AxManagerD — ★52 · empujó el 31-oct-2026 (hace 7 días) · NOASSERTION · última release v1.4.0 (31-oct-2026)
• topjohnwu/Magisk — ★63.836 · empujó el 27-oct-2026 (hace 11 días) · GPL-3.0 · última release v31.1 (25-oct-2026)
• tiann/KernelSU — ★20.233 · empujó en las últimas horas · GPL-3.0 · última release v3.3.1 (12-oct-2026)
• KernelSU-Next/KernelSU-Next — ★4.748 · empujó en las últimas horas · GPL-3.0 · última release v3.4.2 (13-oct-2026)
• SukiSU-Ultra/SukiSU-Ultra — ★6.942 · empujó en las últimas horas · GPL-3.0 · última release v4.3.0-r2 (5-nov-2026)
• bmax121/APatch — ★8.133 · empujó el 4-nov-2026 (hace 3 días) · GPL-3.0 · última release 11282 (15-oct-2026)
• Baka-SU/BakaSU — ★2.128 · empujó en las últimas horas · GPL-3.0
• Magisk-Modules-Alt-Repo/json — ★131 · empujó en las últimas horas · GPL-3.0
• Magisk-Modules-Alt-Repo/submission — ★292 · empujó el 27-sep-2026 (hace 41 días) · sin licencia detectada por la API
• MMRLApp/MMRL — ★2.242 · empujó en las últimas horas · GPL-3.0 · última release v34296 (8-mar-2026)
• Fox2Code/FoxMagiskModuleManager — ★2.208 · *dormido*: sin empujar desde el 3-may-2023 (1284 días) · LGPL-3.0 · última release v2.0.2 (2-may-2023) · *ARCHIVADO*
• MRepoApp/MRepo — ★1.117 · *dormido*: sin empujar desde el 2-jul-2024 (858 días) · GPL-3.0 · última release v2.5.0 (2-jul-2024) · *ARCHIVADO*
• Androidacy/MagiskModuleManager — ★1.238 · *dormido*: sin empujar desde el 9-abr-2026 (212 días) · LGPL-3.0 · última release v2.3.8-1 (31-mar-2025)
• LSPosed/LSPosed — ★25.357 · empujó el 14-oct-2026 (hace 24 días) · GPL-3.0 · última release v1.9.2 (11-oct-2023)
• JingMatrix/Vector — ★13.057 · empujó en las últimas horas · GPL-3.0 · última release v2.2 (4-ago-2026)
• Dr-TSNG/ZygiskNext — ★10.839 · empujó el 15-oct-2026 (hace 23 días) · sin licencia detectada por la API · última release v1.5.2 (15-oct-2026)
• 5ec1cff/TrickyStore — ★6.459 · *dormido*: sin empujar desde el 30-nov-2025 (342 días) · sin licencia detectada por la API · última release 1.4.1 (2-nov-2025)

💓 *LOS ENLACES · medidos hoy uno por uno*

De los 22 enlaces de esta pieza, *22 responden*.
Ninguno roto.

⏬ sigue abajo · parte 18 de 19

═══ MENSAJE 20 de 20 · 271 caracteres ═══

💓 *La Bandita · medido a mano con la API, no copiado.* Si mañana abres esto y algo cambió, la fecha del dato está escrita al lado para que no te engañe.

*🏷️ Etiquetas estratégicas*

#AxManager #Axeron #Magisk #KernelSU #APatch #SukiSU #Zygisk #LSPosed #ModuleProp #WebUI
