*14 — ANDROID DENTRO DE ANDROID*
*La calle DSU: probar un sistema completo sin perder el tuyo (hallazgo del dueño de la casa ·
WhatsApp · La Bandita · 15-oct-2026 · dominicano-ES)*

*Por La Bandita · edición dominicana · pieza 14 de la biblioteca · censo de esta tarde*

*🗺 MAPA DE ESTA GUÍA*

```
*🌱 LA SEMILLA*

Esta pieza nace de un hallazgo del DUEÑO de esta casa, en vivo, durante la tarde del 15 de
octubre de 2026. Así pasó: la casa estaba escribiendo la pieza 13 (Android corriendo dentro del
iPhone) cuando el dueño dejó el enlace sobre la mesa: R15Hi/Dsu-Multi-sideloader, «mírate esto».

Y la casa lo miró de una vez, como manda la ley: dato de dueño no se cuestiona, se verifica.

Lo que la verificación encontró dio para esta pieza entera. El README dice «fork modernizado del DSU-Sideloader original», pero GitHub no lo registra como fork de su red: es una re-publicación independiente que acredita a su padre con enlace y todo, VegaBobo/DSU-Sideloader.

¿Y el padre? Una veneración de la calle: 2.324 estrellas, 211 derivaciones... y el último empuje
de código en marzo de 2024.

Dormido desde hace dos años y medio.

Entonces la pregunta de esta guía no es «¿qué es esta app?» sino una que toda la cuadra reconoce: ¿qué pasa cuando el dueño original de la calle se va y alguien retoma el negocio con energía nueva? Aquí pasó lo bueno: el heredero no solo mantiene, añade.

Varios sistemas de prueba a la vez (el Android oficial solo aguanta uno), un catálogo de
sistemas integrado con los cocineros vivos de la escena, y una versión 2.20 publicada el MISMO
día de este censo.

Para el lector nuevo, el fondo del asunto, que es más viejo y más bonito que la app: tu teléfono Android puede arrancar UN SISTEMA COMPLETO DIFERENTE sin borrar nada, sin root y sin costo, usando una puerta oficial que Google dejó en Android 10 y que casi nadie usa porque está escondida detrás de comandos de desarrollador. Las apps de esta pieza son la llave amable de esa puerta.

Y la advertencia que va antes que el entusiasmo: la puerta exige el bootloader desbloqueado, que es la llave maestra del taller, y abrir esa llave una sola vez borra el teléfono entero. Esta pieza te acompaña a decidir si vale la pena, a respaldar como Dios manda, y a probar sin miedo después — porque una vez abierta la puerta, el probador DSU no vuelve a borrar nada jamás.

*📰 EL CENSO DE ESTA TARDE*

Censo del turno (15-oct-2026, tarde, API pública de GitHub), las dos placas de la calle:

Placa del hijo — R15Hi/Dsu-Multi-sideloader (hallazgo del dueño):
· Estrellas: ★2 (censo de la tarde del 15-oct). Recién nacido público: la calidad aquí no se mide en estrellas todavía, se mide en código y en descendencia.
· Nacimiento: 1 de octubre de 2026. Quince días de vida al censo.
· Empuje de código: HOY, 15-oct-2026. La cocina encendida el mismo día que escribimos.
· Lanzamiento vigente: v2.20, publicada el 15-oct-2026, con dos archivos: la app (app-release.apk) y un módulo zip heredado del ecosistema del padre (module_DSU_Sideloader.zip).
· Asuntos públicos: 0 abiertos, 0 en total. O nada falla o nadie llegó aún: con quince días y una estrella, es lo segundo. El probador social está por estrenar.
· Licencia: Apache-2.0 (la del padre, respetada).
· Lenguaje: Kotlin.

Placa del padre — VegaBobo/DSU-Sideloader:
· Estrellas: ★2.325 (censo de la tarde del 15-oct). Derivaciones: 211.
· Nacimiento: 31 de enero de 2022. Casi cuatro años de calle.
· Último empuje: 13 de marzo de 2024. Última lanzamiento público: la 2.03, del 29 de abril de 2023. Dormido 31 meses al censo.

Y los cocineros que el catálogo GSI Hub del hijo sirve en vivo (censo de la tarde):
· phhusson/treble_experimentations: ★3.562 (15-oct) — LA FUNDACIÓN: el taller donde Pierre-Hugues Husson inventó la era moderna de las GSIs. Empuje de enero de 2025.
· ponces/treble_aosp: ★315 (15-oct) — guiones y parches para cocinar GSIs de AOSP/TrebleDroid. Empuje de julio de 2025.
· AndyYan, MisterZTR y Nazim: nombres citados por el catálogo del hijo como fuentes vivas; sus cocinas viven repartidas entre GitHub y espejos externos. Re-censo pendiente (dato fechado, no re-medido en esta pieza).

La lectura de la camada, con la misma vara de siempre: la calle DSU no es una moda de esta semana — es una calle de 2022 con su cabeza clásica dormida y su heredero encendido. Esas calles son las mejores para guía: historia probada, presente con movimiento y nadie cobrando boletos.

*🏛 LA HISTORIA DE LA CUADRA*

Para entender la puerta DSU hay que entender la obra maestra de ingeniería que la hizo posible,
y esa obra tiene nombre de proyecto de Google: Project Treble.

La era pre-Treble (2008-2017, fechado de archivo): cada teléfono Android era una isla. El
sistema de Google y la capa del fabricante vivían amarrados, así que actualizar Android exigía
que el fabricante re-cocinara TODO.

Resultado conocido: teléfonos de un año botados del soporte.

El parto de Treble (2017, fechado de archivo): Google separó el sistema en dos pisos con una frontera de contratos: arriba el Android puro, abajo la capa del fabricante. Con la frontera firme, el piso de arriba se puede CAMBIAR sin tocar el de abajo.

De esa separación nace la GSI: un Android genérico que corre sobre la capa de cualquier
fabricante que respete los contratos.

La puerta DSU (2019, fechado de archivo): con Android 10, Google añadió Dynamic System Updates: descargar una GSI al almacenamiento y arrancarla SIN instalar nada, SIN tocar la partición del sistema, sin root. Una sesión dinámica: reinicias y tu Android de siempre regresa intacto.

Diseñada para desarrolladores; escondida detrás de opciones de desarrollador y comandos.

La era del probador amable (2022, fechado de archivo): VegaBobo publica DSU-Sideloader, la app que convierte el comando escondido en botones: eliges tu GSI, la app pide el permiso, instala la sesión y te da el botón de regreso. La calle se llena de gente normal probando Android puro.

El sueño (2024) y la resurrección (2026, ambos fechados de repositorio): el padre deja de
empujar código en marzo de 2024. La calle no muere porque el inventario (las GSIs) sigue
cocinándose en las fundaciones vivas: phhusson, ponces, AndyYan y compañía.

El 1 de octubre de 2026 aparece el heredero con features que el padre no alcanzó a dar: varios
slots a la vez y el catálogo integrado. Tu dueño lo encuentra y lo pone sobre esta mesa quince
días después.

¿Y por qué Google la mantiene tan escondida? Porque está pensada para desarrolladores: quien
prueba una build genérica necesita entender que el sistema de prueba no lleva la certificación
ni la afinación del fabricante.

La puerta exige saber lo que se abre. Las apps de esta pieza no fuerzan la puerta: la señalan y
te acompañan a abrirla con la vara puesta — que es exactamente lo que esta guía hace contigo a
tu lado.

Por eso esta pieza se escribe HOY: estás leyendo el registro de una sucesión de calle mientras
pasa, con los números de la tarde puestos.

*📇 LA PLACA DOBLE DE LA CASA*

Toda pieza de la biblioteca lleva placa; esta lleva dos, porque es la primera pieza de la
historia de la casa dedicada a una SUCESIÓN:

· Nombre del heredero: Dsu-Multi-sideloader (R15Hi). El nombre lo dice: el DSU Sideloader de siempre, con MULTI-slot encima.
· El apellido honrado: el README acredita al padre con su enlace (VegaBobo/DSU-Sideloader) y se presenta como modernización de su obra. La casa verificó el linaje: no es un fork de red de GitHub, es una continuación independiente que reconoce su origen. En la cuadra eso se llama llegar con la vara en alto.
· Qué añade el hijo, auditado en su README de esta tarde:
  · MULTI-SLOT: el Android oficial guarda UN sistema dinámico; el hijo respalda el activo (block maps y metadatos a una carpeta de respaldo), libera el espacio y deja instalar y alternar VARIOS. Con root puede hacerlo solo; sin root, asistido.
  · GSI HUB: catálogo integrado con las cocinas vivas (AndyYan, ponces, phhusson, MisterZTR, Nazim y las que añadas a mano), con reconocimiento de familias de sistemas (AOSP, LineageOS, crDroid, Evolution X, Pixel Experience...), notas de cambio visibles y descarga con instalación de un toque que limpia los archivos a medias si algo se cancela.
  · UI nueva completa: temas (Material You dinámico, oscuro, claro, AMOLED puro y «Glassy»), barra flotante traslúcida, iconos propios para claro y oscuro.
  · Cuatro pestañas: Instalados · Multi-DSU · GSI Hub · Ajustes.
· Requisitos del hijo, textuales del README: Android 10 o más · bootloader desbloqueado · aparato con particiones dinámicas · GSI compatible con tu arquitectura (arm64, arm o x86_64) y tu VNDK (A/B o solo-A).
· Licencia: Apache-2.0, la licencia del padre, la misma de tantas herramientas serias de Android.
· Y el módulo zip que viaja con la v2.20: herencia del ecosistema del padre (el compañero que ayuda en aparatos donde la vía pura de app no basta). Se instala aparte y solo si tu caso lo pide.

*🧭 QUÉ ES Y QUÉ NO ES*

Lo que la calle DSU ES:
· Un probador OFICIAL de Android: la función Dynamic System Updates existe en Android desde la versión 10, puesta por Google. La app es la llave amable, no el invento.
· Un sistema completo arrancando encima del tuyo: la GSI (Android puro o sabores comunitarios) vive en tu almacenamiento y corre en una sesión dinámica.
· Reversible por diseño: reinicias y tu Android de siempre regresa exacto — tus apps, tus fotos, tus contraseñas, todo donde lo dejaste.
· Un taller de aprendizaje sin riesgo de ladrillo (una vez abierto el bootloader, que ese paso SÍ borra y SÍ tiene sus reglas): si la sesión se pone fea, apagas y vuelves.
· Gratis: la app del hijo es Apache-2.0 sin cobros; las GSIs de las fundaciones son código abierto cocinado en público.

Lo que la calle DSU NO ES:
· Root, NO: no se tocan permisos de superusuario, no se instala Magisk, tu sistema real queda intacto y sellado.
· Flashear, menos: nada se escribe sobre tu sistema actual. El probador vive aparte. Reiniciar = regreso.
· Permanencia, cero: la sesión vive mientras el teléfono no se apague. Quien busque «cambiar de Android para siempre» está en la calle equivocada: eso es ROM y otra pieza de la biblioteca.
· Teléfonos cerrados, fuera: si tu fabricante no permite desbloquear el bootloader (algunos no lo permiten, sobre todo ciertos comprados por operadoras), esta pieza no es para ese aparato, y no hay truco sano que lo arregle.
· Bancos, garantía ninguna: en una GSI pueden fallar los chequeos de integridad que algunas apps bancarias y de pago exigen. La casa no promete bancos. Tu banco corre en tu Android real, que no se toca.
· Ni del hijo ni del padre: la puerta es de Google, la app es una llave. Si mañana desaparece la llave, la puerta sigue ahí (y la pieza te enseña dónde queda).

*⚖ LA VARA DEL CONSENTIMIENTO*

Antes del botón, la vara. Esta pieza tiene UNA vara más larga que las demás porque su primer
paso es el único paso que no se deshace.

La vara grande, primero y en mayúscula:
· DESBLOQUEAR EL BOOTLOADER BORRA TODO EL TELÉFONO: fotos, chats, aplicaciones, sesiones, todo. UNA SOLA VEZ. Es la llave maestra del taller y cada fabricante la abre a su manera (opción de desarrollador + comando o solicitud oficial).
· Por eso el orden sagrado de esta guía: PRIMERO respaldo completo (fotos a la nube o computadora, copia de WhatsApp según su propio respaldo, códigos de autenticación de dos pasos migrados o anotados, lista de aplicaciones), DESPUÉS desbloqueo, y solo ENTONCES el probador.
· Verifica ANTES si tu modelo permite desbloqueo y cómo: fabricantes hay con proceso libre, hay con espera de días y hay que no lo permiten. Si el tuyo no permite, esta pieza se queda en cultura general, y está bien.
· El desbloqueo puede afectar garantía según fabricante y país. La casa no da consejo legal: da el dato de que existe y la recomendación de leerlo antes, no después.

La vara del probador (después del desbloqueo, ya sin sustos):
· La sesión DSU no toca tu sistema: reiniciar la apaga y regresas. Ninguna acción dentro del probador (instalar apps de prueba, configurar, hasta botarlo) cambia tu Android real.
· Lo que SÍ gasta: espacio (una GSI pesa normalmente 2-4 gigas, cuenta además el espacio de trabajo que la app reserva) y batería mientras la sesión corre.
· La vara con los demás: prueba en TELÉFONOS TUYOS o con permiso del dueño. Y si el teléfono es el del trabajo, ni el tuyo de la familia: los aparatos con datos ajenos o corporativos no son probadores.
· La vara con las descargas: GSIs solo de las cocinas del catálogo o de fundaciones conocidas. Una imagen de sistema es un sistema operativo completo: bajarlo de un canal de Telegram anónimo es instalarle al teléfono una casa entera de nadie sabe quién.

Y la vara de la cuenta de Google, que casi nadie cuenta: al desbloquear (y su borrado), algunos
aparatos te van a pedir AL REINICIAR la cuenta de Google que tenía el teléfono (protección
antirrobo FRP). Con tu cuenta, tranquilo: la sabes.

Con un teléfono heredado o revendido, verifica las credenciales ANTES, porque sin ellas el
aparato puede quedar encerrado tras su propio borrado. Respaldo de datos y de contraseñas,
siempre.

Si tu caso no cuadra con la vara (teléfono cerrado, sin espacio, sin respaldo posible), la pieza
entera sigue valiendo como mapa: ahora sabes por qué el muchacho de la tienda «no te puede
instalar eso».

*🎒 EL CARGAMENTO*

Lo que necesitas, medido y sin humo:

· Un teléfono Android 10 o más nuevo, con particiones dinámicas (los lanzados con Android 10 de fábrica las traen; los viejos re-actualizados, a veces no). La app del hijo te lo dice en su chequeo.
· Bootloader desbloqueable en tu modelo — y el respaldo COMPLETO hecho antes del desbloqueo, como manda la vara.
· Espacio libre: 6-8 gigas cómodos para la imagen, su espacio de trabajo y aire para el sistema que corre.
· Batería alta o enchufe: ni el desbloqueo ni la primera sesión se hacen con el teléfono al 15 por ciento.
· La app: la v2.20 del repositorio del hijo (enlace en Fuentes). Se instala con el permiso normal de «aplicaciones de fuentes desconocidas» de Android, como cualquier app fuera de tienda.
· Tu GSI: del GSI Hub integrado (la vía cómoda de esta pieza) o bajada a mano de las fundaciones (phhusson, ponces, AndyYan — enlaces en Fuentes). Debe calzar con tu arquitectura (arm64 en prácticamente todos los teléfonos modernos) y tu VNDK (la app ayuda a leerlo).
· Wi-Fi de verdad para la descarga de la GSI: hablamos de gigas, no de megas; el dato móvil del plan no es el sitio para bajar sistemas.
· Tu llave de computadora SOLO para el desbloqueo si tu fabricante lo exige por comando (algunos lo hacen desde el teléfono con solicitud oficial). Después del desbloqueo, la vida del probador es 100 por ciento en el teléfono.
· Tiempo honesto: respaldo + desbloqueo + primera sesión = una tarde tranquila. Quien te lo venda en 10 minutos está vendiendo.

*💬 LA CONVERSACIÓN HONESTA*

Antes de la instalación, las verdades que el que sabe le dice al que pregunta en la barra del
colmado, sin venderle nada:

Primera: la puerta es de Google, no de un genio anónimo. Dynamic System Updates viene en tu
Android desde la versión 10, documentada por Google para desarrolladores.

Toda la magia de esta pieza es que una app seria te ahorra los comandos. Si alguien te dice
«esto es hackear», la respuesta es: es la puerta de la fábrica, mal señalada.

Segunda: el probador es real pero es un probador. La sesión corre, instalas, pruebas, juegas,
configuras... y al reiniciar, se apaga.

Quien quiera «cambiar de vida» permanente necesita ROM (otra calle, otra pieza). El valor del DSU es exactamente la reversibilidad: puedes probar HOY el Android puro, mañana un LineageOS comunitario, pasado un crDroid, sin comprometerte con ninguno.

Tercera: sin root, con matices. La vía pura (app sin root) usa los permisos normales de Android
y el permiso WRITE_SECURE_SETTINGS que se otorga por comando una vez, desde la computadora... en
el padre.

El hijo moderno lo maneja con menos baile y, donde hay root disponible, el auto-stashing
multi-slot brilla. Para la mayoría de los lectores: la vía sin root existe, tiene un paso de
permiso y la app guía.

Cuarta: las apps de banco son el muro real. Los chequeos de integridad (Play Integrity y primos)
pueden marcarte dentro de una GSI como «no certificado».

Tus pagos NO corren riesgo en tu Android real (que sigue intacto), pero DENTRO del probador no
prometas banking. La casa no promete lo que no mide.

Quinta: el catálogo es la revolución silenciosa del heredero. Antes, probar una GSI era: saber
de cocinas, leer foros, bajar el archivo correcto entre cinco variantes con nombres de
ingeniería.

Ahora el GSI Hub te muestra las cocinas vivas con su familia de sistema, sus notas y su botón.
El conocimiento experto quedó embotonado.

Eso, y no la UI bonita, es lo que baja la barrera de entrada de esta calle.

Sexta, la dominicana: todo esto es gratis. Ni «activación premium», ni «flasheo a 500 pesos» en
el kiosco (que además es la calle del flasheo, la que SÍ borra y a veces ladrilla).

Si alguien te cobra por «ponerte el DSU», está cobrando por un botón gratis.

*🔧 LA INSTALACIÓN POR LA VÍA SANA*

Paso 0, el que no se salta — respaldo y desbloqueo:

``` 0.1 Respaldo completo: fotos, chats, códigos 2FA, lista de apps. Todo, dos veces si puedes (nube + computadora).

0.2 Verifica que tu modelo PERMITE desbloqueo (opciones de desarrollador › desbloqueo OEM). 0.3 Desbloquea según tu fabricante.

EL TELÉFONO SE BORRA. Es normal y es una sola vez. 0.4 Configura tu teléfono de nuevo.

Ya está: la puerta está abierta para siempre. ```

Paso 1, la app:

``` 1. Baja la v2.20 del repositorio del hijo (app-release.apk, enlace en Fuentes). 2. Instálala con el permiso de fuentes desconocidas, como cualquier app seria fuera de tienda.

3. Abre: cuatro pestañas (Instalados, Multi-DSU, GSI Hub, Ajustes). ```

Paso 2, el permiso de la casa (vía sin root):

``` 1. En Ajustes, la app te pide el permiso WRITE_SECURE_SETTINGS: se otorga con un comando único por cable (adb), o con la vía que la propia app te muestra en pantalla según tu Android. 2. Es EL único paso de computadora de toda la vida del probador.

Hecho una vez, hecho para siempre. ```

Paso 3, tu primera sesión:

``` 1. Pestaña GSI Hub: elige una cocina viva (empieza por una GSI de AOSP o LineageOS para tu arm64). 2. Lee las notas de la versión, descarga, instala.

La app reserva el espacio y arma la sesión. 3. Te avisará el reinicio: acepta.

El teléfono arranca EN la GSI. Pruébala. 4. Reinicia normal: estás de vuelta en tu Android, intacto.

Así de grande la puerta. ```

Chequeo de casa: si tras el reinicio del paso 4 tu teléfono está exacto como antes y el archivo de la GSI queda guardado para volver a probar, la instalación está sana. Si algo se puso rara EN el probador, reinicia y cuéntalo en el cuaderno: el probador no deja secuelas.

*📻 LOS CANALES DEL TALLER*

· Repositorio del hijo: github.com/R15Hi/Dsu-Multi-sideloader — código, releases (la v2.20 con app y módulo) y su README completo.
· Repositorio del padre, por respeto y referencia: github.com/VegaBobo/DSU-Sideloader — dormido desde 2024, pero su documentación sigue enseñando.
· Las fundaciones de GSIs: phhusson/treble_experimentations (la fundación, ★3.562 al censo del 15-oct), ponces/treble_aosp (★315), y las cocinas de AndyYan y Nazim que el Hub sirve en vivo.
· El catálogo dentro de la app (GSI Hub): tu canal diario. Las cocinas nuevas entran solas.
· XDA y los foros de Treble: la sala de conversación histórica de la calle (fechado de archivo: es donde la escena ha resuelto por una década). Lee, no firmes sin leer.
· Regla de la casa: cero canales cobrando por GSIs o por «instalación DSU». El sistema lo cocina la fundación gratis y el botón es gratis. Todo lo demás, humo con APK dentro.

*🏭 LA DESPENSA DE DATOS*

Qué entra, qué se guarda y qué sale de tu teléfono en esta pieza, contado sin letra chica:

· Lo que baja: la app (del repositorio) y tu GSI (de la cocina que elijas, con su nota de cambio a la vista). Nada más.
· Lo que se guarda: la imagen de la GSI y sus metadatos de sesión en tu almacenamiento (gigas, no megas: planifica espacio). El respaldo multi-slot del hijo guarda block maps y metadatos en carpetas locales del teléfono.
· Lo que sale al internet: la descarga de la GSI que TÚ eliges, y nada más por parte de la app. La GSI que corre hará lo que cualquier Android: hablar con sus servidores de sistema y de apps. Dentro del probador, inicia sesión solo en lo que quieras probar; para la prueba fría, no inicies nada.
· Lo que NO hay: cuentas de la app, registro, cobros. Apache-2.0, código público y auditable en ambos extremos de la sucesión.
· Higiene de cuadra: si pruebas dentro del probador con tu cuenta de Google, ese probador lleva tus datos mientras corre y hasta que borres sus archivos. Con el botón de limpieza y borrando la imagen, se va. El resto es el sentido común de siempre: no pongas en un probador lo que no pondrías en un teléfono prestado.

*📼 LA ANALOGÍA MEDIDA CON REGLA*

La casa mide sus analogías; esta calza con clavos.

El probador del colmado escalado a sistema operativo: tu Android real es tu casa. La GSI es el apartamento amueblado del edificio de al lado, con la LLAVE puesta para tú entres a vivir UNA SEMANA de prueba: duchas, cocinas, duermes, invitados.

Lo que rompas o ensucies allá, allá queda; tu casa ni se enteró. Al terminar, devuelves la llave
(reinicias) y sigues en tu casa con tu vida exacta.

¿Y el bootloader? Es la administración del edificio aceptándote como inquilino capaz de probar
apartamentos.

El trámite de registrarte (desbloquear) te obliga a mudar tus muebles un día completo (el
borrado). Se hace UNA vez; después, probar apartamentos es tan fácil como cruzar la calle.

¿Y la diferencia con flashear? Flashear es VENDER tu casa y mudarte para siempre al apartamento
(con los riesgos de mudanza de verdad: te puedes quedar sin ninguna de las dos si el camión se
boltea).

DSU es alquilar para probar. La casa enseña alquilar primero, siempre.

Y la cáscara del nombre, medida: GSI, Generic System Image, imagen de sistema GENÉRICA: hecha para calzar en cualquier aparato que respete los contratos de Treble, como un sastre que cosió para el tallaje estándar. Tu teléfono es el cuerpo: si el corte es tu talla (arquitectura y VNDK correctos), el traje queda.

Una analogía que NO usamos porque miente: «doble sistema como computadora con dual boot». Miente
en lo importante: el dual boot exige ELEGIR en cada encendido y convive con particiones; el DSU
es una sesión dinámica que muere al reiniciar.

Quien lo entiende como dual boot va a buscar el menú de arranque que no existe.

*🛠 EL TALLER PRÁCTICO*

Cuatro talleres, de la primera sesión a la casa de varios slots:

``` TALLER 1: LA PRIMERA SESION (la puerta) 1. Instala la app, otorga el permiso único. 2. GSI Hub › elige una GSI AOSP o LineageOS arm64 con buena nota de versión.

3. Descarga e instala. Acepta el reinicio.

4. VIVE el probador: android puro, sin capa del fabricante. Mide todo en el cuaderno.

5. Reinicia: de vuelta en casa. Nada cambió. ```

``` TALLER 2: VOLVER SIN PERDER LA IMAGEN 1. Tras reiniciar, tu GSI queda guardada. 2. Pestaña Instalados › la sesión queda lista para relanzar cuando quieras.

3. Probar y volver, probar y volver: ese es el baile normal de esta calle. ```

``` TALLER 3: EL MULTI-SLOT (la herencia nueva) 1. Con tu primera GSI instalada, instala una SEGUNDA (otra cocina, otro sabor). 2. La app respalda la activa (block maps y metadatos a su carpeta) y libera el espacio del slot oficial.

3. Pestaña Multi-DSU: alterna entre tus sistemas guardados. Cada uno arranca, se prueba y se apaga con reinicio. ```

``` TALLER 4: LA LIMPIEZA HONESTA 1. ¿Ya no quieres una GSI? Bórrala desde la app: liberas sus gigas completos.

2. ¿Quieres TODO como estaba (con el bootloader abierto, eso no se deshace)? Borra sesiones e imágenes.

Tu Android real nunca dejó de ser tu Android real. ```

Señal de taller sano: entras a la GSI, la recorres, reinicias y tu teléfono es el mismo; el espacio libre se comporta como la app dijo; y el cuaderno anota qué GSI, qué tamaño, cuánto tardó. Con eso eres usuario de DSU, no espectador de videos.

*🧊 MITOS DESMONTADOS*

Cuatro mitos que esta calle arrastra desde siempre, desmontados con la vara:

Mito 1: «DSU hace root al teléfono.» Desmontado: root es tocar el sistema real con permisos de
superusuario; DSU arranca OTRO sistema aparte sin tocar nada. Tu Android real queda sellado.

Por eso muchos aparatos lo permiten donde el root está vetado.

Mito 2: «Con esto tu teléfono viejo se pone como nuevo para siempre.» Desmontado: dentro de la sesión puedes tener un Android moderno y fluido, pero al reiniciar vuelves a tu sistema de siempre. Es un probador con luz larga, no una restauración.

Quien venda «teléfono nuevo gratis», humo.

Mito 3: «Desbloquear el bootloader lo puede hacer cualquiera en dos minutos sin consecuencias.» Desmontado en las dos patas: no todos los modelos lo permiten (algunos jamás, otros con espera) y la consecuencia es seria y real: borra TODO una vez. La vara de esta guía existe porque ese paso no se improvisa.

Mito 4: «Las GSIs son piratas.» Desmontado: una GSI es Android (de Google o de fundaciones de
código abierto como AOSP, LineageOS y TrebleDroid) compilado genérico. Es la misma obra libre de
siempre, cosida para tallaje universal.

Las cocinas citadas (phhusson ★3.562, ponces ★315 al 15-oct) son proyectos públicos de años.

Bonus, el semimito: «una vez abierto el bootloader, tu teléfono queda inseguro para siempre». Medio desmontado: queda con una puerta más abierta, sí (ese es el costo), y algunas apps lo notan; pero tu uso normal, tus datos y tus cuentas funcionan igual en tu Android real.

El riesgo real es menor que el miedo vendido, y mayor que cero. La casa no vende ni miedo ni
certezas: vende datos.

*❓ PREGUNTAS FRECUENTES*

¿Se puede ladrillar el teléfono con esto? El probador no: reiniciar te saca siempre.

El riesgo real está concentrado en el desbloqueo mal hecho (interrumpir, usar comandos de otro
modelo). Con la vara de esta guía, el riesgo es el mínimo de la calle.

¿Pierdo garantía? El desbloqueo puede afectarla según fabricante y país: léelo ANTES (la vara lo
manda). El probador en sí no añade marcas.

¿Cuánto espacio necesito? Cuenta 6-8 gigas libres: imagen (2-4 G), espacio de trabajo de la
sesión y aire. El multi-slot usa menos por sistema extra gracias al respaldo del activo.

¿Sirve en mi Infinix/Tecno/Samsung/Xiaomi? Android 10+, particiones dinámicas y desbloqueo posible: la mayoría de los modernos sí; Samsung tiene su propio baile de desbloqueo (y en algunos modelos lo limita); los comprados por operadoras a veces llegan cerrados.

Chequea tu modelo ANTES, no después.

¿Puedo usar WhatsApp dentro del probador? Puedes, iniciando tu cuenta ahí; recuerda que es un
apartamento prestado (y que WhatsApp tiene su propio respaldo). Para pruebas frías, mejor sin
cuentas.

¿Se pueden instalar apps normales? Todas las que quieras desde el Play Store o APK dentro del
probador; los chequeos de integridad de algunas apps (bancos) pueden frenar ahí dentro.

¿La sesión aguanta un reinicio? No: reiniciar ES el botón de volver. Es el diseño oficial:
dinámica quiere decir que vive mientras no apagues.

¿Y si la GSI no arranca? Reinicias, vuelves a tu sistema, borras esa imagen y pruebas otra
cocina. Así de barato el fracaso en esta calle; en la del flasheo no.

¿El módulo zip ese para qué? Es el compañero heredado del ecosistema del padre para casos donde
la vía pura de app no basta. Instálalo solo si tu caso lo pide y solo desde el release oficial.

¿Las GSIs reciben actualizaciones de seguridad? Sí: cada cocina publica sus versiones (con nota
de cambios en el Hub); bajan la nueva, la instalas como sesión y la vieja se borra o se
respalda, según tu manejo de slots.

Lo que NO hay es actualización «por dentro» de la sesión: se cambia de versión, no se parchea en
caliente.

¿Le sirve a un teléfono que ya va lento por llenado? El probador diagnostica, no limpia: si el
llenado es el problema, primero se libera espacio (y eso es higiene básica, no esta pieza).

Después, el probador te dirá con datos si la lentitud era software de capa o edad del hierro.

¿Gratis siempre? La app sí (Apache-2.0), las GSIs de las fundaciones sí. Todo lo cobrado en esta
calle es humo con recibo.

*🧪 CASOS DEL BARRIO*

Cuatro casos dominicanos de la vida real, con lo que la pieza sí puede y no puede:

Caso 1, el Infinix lento del muchacho de la colmado: dos años de uso, la capa del fabricante llena de cosas, y quiere sentir velocidad. Con la vara cumplida (respaldo en la tarde, desbloqueo por la noche), el GSI Hub le baja una GSI de LineageOS arm64.

Dentro del probador: Android limpio, el aparato vuela con lo mismo de hardware. Veredicto del
cuaderno: probador sí; para vivirlo siempre, esa es otra pieza (ROM) y otra decisión.

Caso 2, la contadorcilla y el banco: quiere probar «lo nuevo» pero su banco exige integridad y
su teléfono es su oficina. Veredicto de la casa: NO para ese aparato.

Su banco corre en su Android real y ahí se queda; el probador es para un teléfono secundario, si
acaso. Dato honesto que ahorra sustos: la pieza no es para todos los aparatos ni todos los usos.

Caso 3, el streamer de tecnología del barrio: su canal vive de «mira esto». Con el multi-slot
del heredero tiene tres GSIs listas (AOSP puro, LineageOS, un sabor comunitario raro) y alterna
en la tarde grabando sesiones.

Su hallazgo para el video: el público pregunta más por CÓMO volvió a su sistema (reinicio,
simple) que por lo nuevo. El truco real es la reversibilidad; el truco falso es lo que venden
otros.

Caso 4, el rescatador de aparatos: le llegó un teléfono «se dañó con una actualización» que en realidad es una capa del fabricante rota. Con DSU prueba una GSI limpia para DIAGNOSTICAR: si el aparato va bien en la GSI, el hardware está sano y el problema es software del fabricante (y la solución seria es otra calle: ROM o reseteo).

El probador como mesa de diagnóstico: el uso más subestimado de la pieza.

Caso 5, el kiosco del flasheo: al muchacho del kiosco le llegan teléfonos «para revivir» y su herramienta es la del flasheo (la que escribe encima y a veces ladrilla). Con esta pieza en la mano, su servicio cambia de calle: prueba una GSI para DIAGNOSTICAR (hardware sano o no) sin comprometer nada, y solo flashea cuando hay decisión informada del dueño del aparato.

El probador como contrato honesto entre el que repara y el que paga.

El patrón de los cuatro y del quinto: el DSU no es «mejorar tu teléfono», es CONOCERLO.
Diagnostica, prueba, decide. La mejora (si procede) viene después por la puerta seria.

*📜 HISTORIA CORTA*

La vida de la calle en fechas puestas:

· 2017 (fechado de archivo): Project Treble parte Android en dos pisos con contratos. Nace la posibilidad técnica de la GSI.
· 2018-2019 (fechado de archivo): phhusson y su treble_experimentations cocinan las GSIs modernas y la escena despega. Google añade la puerta DSU con Android 10 (2019).
· 31-ene-2022: nace VegaBobo/DSU-Sideloader. La puerta escondida gana botones.
· 29-abr-2023: la 2.03 del padre, su último lanzamiento público conservado.
· 13-mar-2024: último empuje de código del padre. La calle queda con inventario vivo (las fundaciones siguen cocinando) y sin llave amable nueva.
· 01-oct-2026: aparece R15Hi/Dsu-Multi-sideloader: multi-slot, GSI Hub, UI nueva. La sucesión, con Apache-2.0 y el crédito puesto.
· 15-oct-2026 (tarde de este censo): v2.20 publicada HOY; el dueño de esta casa encuentra la pieza y la pone en la mesa; ★1 el hijo, ★2.324 el padre (censo de la tarde). Esta guía nace ese mismo día, de la lectura en cadena de los dos repositorios.

*🎙 LAS VOCES*

En esta pieza las voces no vienen de asuntos (el hijo no tiene ninguno aún): vienen del propio
texto de la calle, leído hoy y citado con su dueño:

· El heredero se presenta: «fork modernizado del DSU Sideloader original, con gestión de múltiples slots DSU, un catálogo GSI Hub integrado y una renovación estética» — textual de su README del 15-oct. Y la casa añade el matiz verificado: continuación independiente, crédito puesto, no copia silenciosa.

· El catálogo nombra a sus cocineros: «integración directa con lanzamientos GSI de maintainers activos (AndyYan, ponces, phhusson, MisterZTR, Nazim, y más)». Cinco nombres vivos; dos censados hoy por la casa (phhusson ★3.562, ponces ★315), tres fechados para re-censo.

Esa lista es el mapa de la despensa de la calle.

· El padre, por su descripción de repositorio: «una app sencilla para ayudar a los usuarios a instalar GSIs vía la función DSU de Android». Sencilla fue la promesa y sencilla se cumplió: 2.324 estrellas de gente a la que le funcionó (censo 15-oct).

· La fundación, en su propia portada: «notas sobre experimentar con Android Project Treble» — phhusson, el ingeniero que abrió la era. Tres mil quinientas estrellas de agradecimiento no se inventan.

· Y la voz del requisito, textual del README del hijo: Android 10+, bootloader desbloqueado, particiones dinámicas, GSI con arquitectura y VNDK correctas. La pieza entera está en esa línea: cuatro condiciones y ninguna negociable.

Las guías que te oculten una de las cuatro, no te están enseñando, te están apurando.

*📖 GLOSARIO*

Las palabras de esta pieza, en español de la cuadra:

· DSU: Dynamic System Updates. La función oficial de Android 10+ que arranca una imagen de sistema aparte sin tocar tu instalación. Muere al reiniciar: esa es su gracia.
· GSI: Generic System Image. Android genérico que corre sobre la capa de cualquier fabricante que respete los contratos de Treble. El inquilino de prueba.
· Treble: el proyecto de Google (2017) que separó Android en dos pisos con contratos. Sin Treble no hay GSI ni DSU.
· Bootloader: la llave maestra del taller. Desbloquearlo borra el teléfono UNA vez y abre todas las puertas (probador, ROM, recovery). Se respalda ANTES.
· Slot: el espacio de sesión dinámica. Android oficial trae uno; el heredero multiplica la cantidad con respaldos del activo.
· VNDK: la versión de los contratos de la capa del fabricante (A/B o solo-A). El dato que decide si tu GSI calza.
· arm64: la arquitectura de casi todos los teléfonos modernos. Tu GSI debe ser de tu arquitectura.

Y cuatro de la cocina de la escena, que vas a leer en los foros:

· A/B (particiones): el esquema moderno con dos copias de sistema para actualizar sin bajar la guardia. Lo pide la vía DSU pura.
· TrebleDroid: la continuación comunitaria de la fundación de phhusson; de ahí cocina ponces, entre otros.
· Block maps: los mapas de bloques del sistema activo que el heredero respalda antes de liberar el slot. La contabilidad fina del multi-slot.
· Play Integrity: el chequeo de integridad que deciden las apps serias (bancos). Dentro de una GSI puede fallar; en tu Android real, no se toca.
· FRP: la protección antirrobo que pide la cuenta de Google tras un borrado. Con tu cuenta, un trámite; sin ella, una trampa. Se verifica antes de desbloquear.
· Sesión: la vida del probador, desde que lanzas la GSI hasta que reinicias. Un día de prueba por encendido, tantas pruebas como quieras.
· Cocina (en la jerga de esta pieza): el proyecto que compila y publica una GSI. Hub es el mostrador; las fundaciones, las cocinas.

*😄 EL MEME DE LA PIEZA*

El DSU es la casucha del probador del mercado nuevo que le pusieron al sistema operativo: puedes sentarte, probar el motor, tocar la radio y hasta llevarla a dar la vuelta al bloque — pero al entregarla, el vendedor le pasa un pañito y la misma moto queda lista para el siguiente curioso. Y lo mejor: la tuya sigue en tu garage intacta, con su tanque lleno.

*🧯 SOLUCIÓN DE PROBLEMAS: LAS CUATRO TRANCAS*

Las trancas clásicas de esta calle, con su llave o con su frontera:

TRANCA 1: «La app pide el permiso y no hay manera.»
· Es el paso de WRITE_SECURE_SETTINGS: se otorga con el comando único que la propia app muestra, por cable, una vez. Tranca de calma, no de fuerza: cable bueno, seguir la pantalla de la app letra por letra. Con root, la app lo hace sola.

TRANCA 2: «Instalé la GSI y el teléfono no arranca en ella / arranca en la mía.»
· Revisa los dos calzos: arquitectura (arm64 contra arm) y VNDK (A/B contra solo-A). Casi siempre la GSI venía para otra talla. ¿El remedio? Borra esa imagen, baja la correcta del Hub — que te filtra por familia —, y vuelve a intentar. Barato el fracaso en esta calle.

TRANCA 3: «Se quedó sin espacio instalando.»
· Una GSI son gigas y la sesión quiere su aire: libera (o el multi-slot libera por ti respaldando el activo). Cuenta con 6-8 G libres y no peles cables con 3.

TRANCA 4: «Dentro del probador todo va lento / la batería vuela.»
· Frontera honesta: una GSI genérica no está afinada a tu hierro como la capa del fabricante, y la sesión consume. Es el precio del probador, no un defecto tuyo. Anota el dato en el cuaderno (el de la capa, comparado con el de la GSI) y decide con números.

Regla de la casa: tranca con llave se abre; frontera sin llave se nombra. Las cuatro de arriba
cubren el 90 por ciento de los dolores del barrio; lo demás, foros de la escena con tu cuaderno
en la mano.

*🗓 LA SEMANA DE PRUEBA*

Siete días, una hora diaria, para decidir si la calle DSU es tuya. La primera tarde ya hizo lo
difícil:

Día 1 — La vara y el respaldo: sin instalar nada, lee la vara de esta pieza y ejecuta tu plan de
respaldo completo. Verifica si tu modelo desbloquea. Si no permite, la pieza termina aquí para
ese aparato — y el día te sirvió.

Día 2 — El desbloqueo: con respaldo verificado, desbloquea siguiendo TU fabricante. El teléfono
se borra: es lo pactado. Reconfigura lo esencial y descansala. No instales el probador hoy: hoy
se abre la puerta, y ya.

Día 3 — La app y el permiso: instala la v2.20, recorre las cuatro pestañas, otorga el permiso
único con calma. Baja UNA GSI del Hub (AOSP o LineageOS arm64) pero no la lances aún: deja que
descargue tranquila.

Día 4 — La primera sesión: lanza, reinicia, VIVE el probador una hora: recórrelo sin cuentas,
instala dos apps de prueba, mide fluidez con tu mano y tu cuaderno. Reinicia de vuelta.

Comprueba que tu teléfono está exacto. Ese «exacto» es el punto de toda la pieza.

Día 5 — El diagnóstico: prueba en la GSI las tres cosas que más usas (la red, el audio, la
cámara de tu aparato). Anota qué va, qué va raro, qué no va. Ya no estás probando Android: estás
diagnosticando tu teléfono con un sistema limpio.

Día 6 — El multi-slot: instala una segunda GSI de otra cocina. Alterna. Entiende el respaldo del
activo que hace la app. Si un sabor no te cuadra, bórralo: limpiar también se practica.

Día 7 — El veredicto: relee el cuaderno. Tres caminos posibles, todos honorables: (a) la calle se queda como laboratorio para diagnosticar y curiosear; (b) te enamora un sabor y te preparas para la decisión grande (ROM, otra pieza de la biblioteca); (c) concluyes que tu capa de fabricante, con todos sus defectos, afinaba bien tu hierro — y vuelves a ella con datos, no con quejas.

Los tres caminos ganan: nadie sale de esta semana sabiendo menos.

*🗂 CUADERNO DE CAMPO*

El cuaderno de la casa para esta pieza. Cópialo a una nota y llénalo con TUS números:

``` CUADERNO — CALLE DSU Fecha de la vara: ___/___/2026 Teléfono: modelo ___ · Android ___ ¿Particiones dinámicas? SI/NO (la app lo dice) ¿Desbloqueo posible?

SI/NO · método ___ Respaldo hecho: fecha ___ · dónde ___ Desbloqueado: fecha ___ · borrado ok SI/NO App: v___ instalada ___/___/2026 Permiso único otorgado: SI/NO · intentos ___

GSI 1: cocina ___ · versión ___ · tamaño ___ G Descarga: ___ min · instalación: ___ min Fluidez (1-5): ___ · calor: ___ · batería/h: ___ Red SI/NO · audio SI/NO · cámara SI/NO GSI 2 (multi-slot): ... Vuelta a casa tras reinicio: exacto SI/NO Espacio libre antes ___ G · después ___ G Veredicto: laboratorio / enamorado / vuelvo a mi capa ```

La regla del cuaderno es la de siempre: «va más o menos» no es un dato. Una fila por GSI y una
semana te convierten en el que sabe de la cuadra — el que enseña con números y no con gritos.

*🏘 EL VECINDARIO DE ESTA PIEZA*

La calle DSU conecta con media biblioteca y con toda la escena libre:

Hermanas de la biblioteca:
· La guía 13 (Husk, Android en el iPhone) es el espejo: allá se traduce Android para otro sistema; acá se prueba Android completo dentro de Android. Juntas enseñan la lección de la semana de la casa: los sistemas ya no son murallas, son salas con puertas.
· La guía 12 (ShizuCallRecorder vía Shizuku) y la 11 (Vela, mapas sin Google): el software libre de la camada nueva moviendo el pastel de las tiendas grandes. Esta pieza añade el nivel profundo: el SISTEMA entero como territorio libre.
· Y la guía 01 de las tiendas: la vara para juzgar cualquier instalador antes de dejarlo en el teléfono.

Vecinos de la escena (fechado de archivo y censo del 15-oct):
· phhusson/treble_experimentations: la fundación (★3.562 al 15-oct). Su autor es a las GSIs lo que el que inventó el molde del pan: panaderías hay muchas, el molde es uno.
· ponces/treble_aosp (★315 al 15-oct): cocina TrebleDroid/AOSP activa, de las que el Hub sirve.
· AndyYan y Nazim: cocineros citados por el Hub; sus lanzamientos viven en espejos del ecosistema. Re-censo fechado pendiente (dato no re-medido hoy).
· LineageOS y TrebleDroid: las familias de sistema comunitario que más GSIs alimentan.
· Magisk y la calle del root: vecino SERIO, no de esta pieza: el DSU vive SIN root y así lo recomendamos para empezar. Se nombran para que sepas que no son lo mismo.

*🧩 LO QUE ESTA GUÍA NO DICE*

El anaquel de lo no dicho, que en la casa vale tanto como lo dicho:

· No damos los comandos de desbloqueo por modelo: varían por fabricante y cambian con versiones; te enseñamos A ENCONTRARLOS (documento oficial de tu marca) porque copiarlos de memoria es la tranca clásica. Lo que borra el teléfono no se improvisa con memoria de oído.
· No recomendamos UNA GSI como «la buena»: las cocinas viven, suben versiones y cambian; te enseñamos el Hub y las fundaciones para elegir del menú vivo, no del recuerdo de la guía.
· No medimos rendimiento por modelo: ni FPS ni batería por aparato. Tu cuaderno es el laboratorio; los únicos números aquí son los del censo público con su fecha.
· No tocamos la calle del root ni la de ROM: hermanas de puerta, piezas distintas. Mezclarlas en una guía es como enseñar a nadar y a bucear con tanque en el mismo párrafo: alguien se ahoga.
· No prometemos apps de banco ni pagos dentro del probador: los chequeos de integridad no son territorio de promesas de casa. Tu banco, en tu Android real.
· No avalamos GSIs de canales anónimos: la despensa de esta pieza son las fundaciones y el Hub. Una imagen de sistema es una casa entera: de nadie sabe quién, ni una ventana.

*🧮 LO QUE APRENDÍ ESTA MAÑANA, EN FICHA CORTA*

· Verificar un linaje toma cuatro llamadas y cambia la historia entera: el «fork» que GitHub no registra, el padre de 2.324 estrellas dormido en 2024, el heredero con v2.20 publicada el mismo día del censo. La etiqueta dice una cosa; el repositorio, otra.
· La mejor calle para guía no siempre es la más estrellada: es la que tiene historia probada, cabeza dormida y heredero encendido. «Sucesión de calle» es ahora categoría oficial del censo de la casa (gracias a un hallazgo del dueño, que es como deben llegar las cosas).
· La puerta DSU lleva seis años en todos los teléfonos Android 10+ y casi nadie la conoce: el conocimiento escondido detrás de un comando es conocimiento que no existe para el barrio. Toda pieza de esta biblioteca es eso: señalar la puerta.
· La reversibilidad es una feature, no una limitación: el probador que se apaga al reiniciar es exactamente lo que lo hace enseñable, regalable y seguro.
· Y la lección de siempre: los números con fecha (★1 y v2.20 hoy; ★2.324 y silencio desde 2024) cuentan la historia mejor que cualquier adjetivo.

*📝 NOTA DE VERIFICACIÓN — 15 DE OCTUBRE DE 2026*

Esta pieza nació de un hallazgo del dueño y se verificó en cadena. La boleta de qué se comprobó:

Verificado EN VIVO hoy, por API pública de GitHub (censo del turno, tarde):
· R15Hi/Dsu-Multi-sideloader: ★1 · 0 asuntos · nacida 01-oct-2026 · push 15-oct-2026 · Apache-2.0 · Kotlin · release v2.20 PUBLICADA HOY con sus dos archivos (app-release.apk y module_DSU_Sideloader.zip).
· VegaBobo/DSU-Sideloader: ★2.324 · 211 derivaciones · nacida 31-ene-2022 · push 13-mar-2024 · releases 2.01 (12-oct-2022) y 2.03 (29-abr-2023).
· Linaje: el hijo NO está registrado como fork en GitHub (fork: False verificado); su README acredita al padre con enlace. Escrito en el censo abierto de la casa.
· phhusson/treble_experimentations ★3.562 (push 27-ene-2025) y ponces/treble_aosp ★315 (push 25-jul-2025): leídos el 15-oct-2026.
· README del heredero: leído completo (7.068 caracteres): requisitos, features, pestañas, modos, créditos.

Fechado de archivo (NO re-medido hoy):
· Project Treble (2017), llegada de DSU con Android 10 (2019), la escena phh-Treble de 2018-2019, y las cocinas de AndyYan, MisterZTR y Nazim (nombres citados por el Hub; censo individual pendiente).

No verificado (y por eso NO declarado):
· Rendimiento por modelo, consumo por sesión, y compatibilidades individuales. Tu cuaderno es el laboratorio de tu aparato.

*🪧 CARTEL DE LA CASA (léelo antes de tocar)*

``` CINCO LINEAS ANTES DEL PRIMER PASO 1. Respaldo completo ANTES de desbloquear: el desbloqueo borra TODO una sola vez. 2. Verifica que tu modelo desbloquea y cómo.

3. GSIs solo del Hub o de fundaciones. 4. El probador se apaga al reiniciar: esa es su gracia, no su defecto.

5. Tu Android real nunca se toca: bancos y vida siguen en tu sistema de siempre. ```

```
Y TRES QUE NO SE NEGOCIAN
Teléfonos ajenos solo con permiso del dueño.
Nada se cobra en esta calle: todo es gratis.
Lo que no sepas explicar, no lo instales a otro.
```

*🗒 LIBRETA DE FECHAS DE ESTA PIEZA*

· 2017 — Project Treble parte Android en dos pisos (fechado de archivo).
· 2019 — Google añade la puerta DSU con Android 10 (fechado de archivo).
· 31-ene-2022 — nace VegaBobo/DSU-Sideloader.
· 29-abr-2023 — la 2.03, último lanzamiento del padre.
· 13-mar-2024 — último empuje del padre: la calle queda dormida con inventario vivo.
· 01-oct-2026 — nace R15Hi/Dsu-Multi-sideloader, la sucesión con multi-slot y GSI Hub.
· 15-oct-2026 — v2.20 publicada (con app y módulo); el dueño de esta casa aporta el hallazgo; censo de la tarde: ★1 el hijo, ★2.324 el padre; esta guía nace el mismo día.

*✍ FIRMA Y DESPEDIDA*

Esta pieza la escribe La Bandita con dos orgullos honestos: es la primera guía de la casa
dedicada a una sucesión de calle, y nació de un hallazgo del dueño puesto sobre la mesa en la
tarde exacta en que el heredero publicaba su v2.20. Las mejores piezas no las buscan las
máquinas: las traen los que caminan la calle.

Si esta guía te sirvió, pásala con la fecha puesta. Si el heredero crece, la pieza se re-censa
con nueva fecha.

Y si algún día el heredero duerme también, la puerta seguirá siendo de Google y las fundaciones
seguirán cocinando: esta pieza enseña la calle, no el negocio de la esquina.

Para el dueño, que encontró lo que la casa no vio: la vara funciona en las dos direcciones. Esa
es la casa que estamos construyendo.

el registro fechado.

*🔎 LA PORTADA OFICIAL, TRANSCRITA Y COMENTADA*

La portada del heredero, transcrita y comentada, porque aprender a leer caras es parte de la
enseñanza:

Dice el proyecto: «un fork modernizado del DSU Sideloader original que aporta gestión de múltiples slots DSU, un catálogo GSI Hub comunitario y una renovación estética Liquid Glass, para instalar, gestionar y alternar imágenes de sistema genéricas vía la función Dynamic System Updates de Android». Comenta la casa: la promesa es de gestión, no de milagro.

Nada de «tu teléfono será otro»: instalar, gestionar, alternar. Y fíjate en el verbo «alternar»: ahí está la herejía buena respecto al Android oficial, que solo aguanta un slot.

Dice al acreditar: presenta al original con su enlace y su historia. La casa verifica: no es fork de red (GitHub lo dice), es continuación independiente con crédito puesto.

Comenta la casa: en una calle llena de reapropiaciones silenciosas, llegar con el crédito puesto es la diferencia entre heredar y saquear. Este heredó.

La vara se levanta a su favor y sigue en alto hasta que demuestre lo contrario — el push de hoy y la v2.20 del día del censo ayudan.

Y el detalle que delata la escuela: «la instalación con un toque garantiza que los archivos descargados a medias jamás entren a instalación». Comenta la casa: el que piensa en el archivo a medias es el que ha sufrido el archivo a medias.

Los detalles de higiene delatan experiencia de calle, no de marketing. Es el mismo patrón que la casa enseña a buscar en toda herramienta: ¿piensan en lo que sale mal, o solo en lo que sale bien?

*🧠 MAPA MENTAL DE LA CASA*

El árbol de la pieza en una nota, para el que piensa en ramas:

```
CALLE DSU (15-oct-2026)
├─ LA PUERTA (de Google, 2019)
│  ├─ Dynamic System Updates: Android 10+
│  └─ sesión dinámica: muere al reiniciar
├─ EL INQUILINO (GSI)
│  ├─ Android genérico (AOSP/LineageOS/
│  │  crDroid/comunitarios)
│  └─ calza por: arm64 + VNDK (A/B)
├─ LA SUCESIÓN
│  ├─ Padre: VegaBobo (2022, ★2.324,
│  │  dormido 2024)
│  └─ Hijo: R15Hi (2026, v2.20 HOY,
│     multi-slot + GSI Hub)
├─ LAS CONDICIONES
│  ├─ bootloader desbloqueado (BORRA 1 vez)
│  ├─ particiones dinámicas
│  └─ espacio 6-8 G + batería
└─ LOS LIMITES
   ├─ no root · no permanente · no dual boot
   ├─ bancos: en tu Android real
   └─ rendimiento: probador, no promesa
```

*📅 EL CRONOGRAMA COMPLETO DE ESTA PIEZA*

El camino del lector nuevo, en fases con tiempos honestos:

``` FASE 0 (15 min): leer esta guía entera, sin tocar nada. Ver la vara y la frontera.

FASE 1 (1 tarde): respaldo completo verificado y desbloqueo del bootloader (borra todo: es lo pactado). Reconfigurar lo esencial.

FASE 2 (30 min): app v2.20 + permiso único. Recorrer las cuatro pestañas sin prisa.

FASE 3 (1 h): primera sesión de GSI del Hub, vivida con cuaderno. Reinicio de vuelta.

FASE 4 (1 semana): la semana de prueba — diagnóstico, multi-slot, limpieza. FASE 5 (tu ritmo): laboratorio de la casa o puerta a la decisión grande (ROM), con datos. ```

*🎓 LOS TRES ESCENARIOS DE APRENDIZAJE DE UN NOVATO DE LA CALLE*

Escenario 1, el curioso con teléfono secundario: el caso ideal. Su aparato viejo se convierte en
laboratorio de la casa: probará cuatro GSIs en la semana sin miedo porque nada de su vida diaria
depende del aparato.

Su lección: la reversibilidad convierte la curiosidad en oficio.

Escenario 2, el dueño de un solo teléfono y una vida dentro: su vara es doble y su decisión es
seria. La casa le dice: tu desbloqueo borra tu vida una vez — hazlo solo con respaldo verificado
en dos lugares, o no lo hagas todavía.

Su lección: la técnica espera al respaldo; el respaldo no espera a la técnica.

Escenario 3, el que busca «cambiar de Android para siempre»: llegó a la puerta equivocada con la prisa correcta. El probador le sirve como PASO: conocerá su aparato con sistema limpio, medirá qué gana y qué pierde, y si quiere permanencia, la casa le enseñará la calle de las ROM en su pieza propia.

Su lección: alquilar el apartamento antes de vender la casa.

*🧾 EL PLIEGO FINAL DE LA CASA (para copiar en una nota, siendo honesto)*

``` CALLE DSU EN UNA NOTA (15-oct-2026) 1. DSU = puerta oficial de Google (Android 10+). 2. GSI = Android genérico; reiniciar = volver.

3. Heredero: R15Hi v2.20 (multi-slot + Hub). 4. Padre: VegaBobo ★2.324 (dormido 2024).

5. Requisito serio: bootloader (BORRA 1 vez). 6. Respaldo completo ANTES del desbloqueo.

7. GSIs: Hub o fundaciones. Nunca anónimos.

8. 6-8 G libres · arm64 + VNDK correctos. 9. Sin root · sin flasheo · sin permanencia.

10. Bancos: en tu Android real. Aquí, probador. ```

*🌦 LOS TRES FUTUROS DE ESTA PIEZA (lectura honesta, sin boletos ganadores)*

Futuro A, la sucesión se confirma (el más probable con los datos en la mano): el heredero mantiene el ritmo (push y v2.20 el día del censo) y crece su probador social: primeros asuntos, primeros usuarios, primeras estrellas. Señales a mirar: asuntos abiertos con respuestas del autor, nuevas cocinas en el Hub, y si la versión sin root del multi-slot se suaviza.

La pieza se re-censaría con nueva fecha y los números nuevos.

Futuro B, la ventana del heredero se cierra: con ★1 y un solo autor activo, el riesgo existe y se nombra sin drama: si el push se detiene, la calle queda como en 2024 — inventario vivo (Google sigue teniendo la puerta, las fundaciones siguen cocinando) y llave otra vez huérfana. Sería la segunda sucesión que esta pieza documenta; la vara de la casa ya sabe leer ese mapa, y los forks de la obra (Apache-2.0 lo permite) serían los candidatos a examinar.

Futuro C, Google estrecha la puerta: DSU depende de una decisión de diseño de Android; si una
versión futura la limita, la calle entera se re-escribe. Señal a mirar: la documentación oficial
de desarrolladores en cada versión de Android.

No es drama previsto: es la misma vigilancia que la casa mantiene sobre el JIT en la pieza
hermana del iPhone.

Ninguno se promete. Los tres tienen señales nombradas. La diferencia entre una guía y una cadena
de humo es exactamente esta sección.

*❔ SEGUNDA RONDA CORTA (las que llegaron con la puerta cerrada)*

¿Se puede probar sin desbloquear el bootloader? No, y que quede claro desde la vara: la puerta
exige la llave maestra.

Quien ofrezca «DSU sin desbloqueo» está vendiendo otra cosa con ese nombre. La buena noticia: se
desbloquea UNA vez en la vida del aparato.

¿El probador consume datos? La descarga de la GSI sí (gigas: con Wi-Fi). La sesión corre como
cualquier Android corre.

¿Se puede tener DOS sesiones a la vez corriendo? No: una corre; las otras quedan guardadas (eso
es el multi-slot). Alternar es respaldar y lanzar.

¿Mi SIM y mis datos móviles funcionan en la GSI? La telefonía básica sí (con las variaciones
normales de una GSI genérica); tu plan y tu SIM no se tocan.

¿Puedo instalar el probador en el teléfono de mi papá? Con permiso del dueño y su respaldo hecho
juntos — y mejor aún: enséñale la vara y que la decisión sea suya. La pieza es para acompañar
decisiones, no para tomarlas por otros.

¿Cada cuánto se re-censa esta pieza? La casa re-censa cuando hay release nueva del heredero o
movimiento en las fundaciones; el registro deja fecha de cada censo. Dato sin fecha no viaja en
esta casa.

*🪴 QUÉ HACER SI LA PIEZA DESAPARECE O CAMBIA DE DUEÑO*

El seguro de la casa, escrito para una pieza con historia de sucesiones:

Si el repositorio del heredero desaparece: la obra es Apache-2.0 y ya demostró que sabe
sobrevivir a su padre: los espejos y derivaciones quedan por derecho de licencia, y la pieza
entera (la puerta de Google + las fundaciones) no depende de ningún repo de app para seguir
siendo cierta.

Si aparece otro heredero del heredero: la vara de la casa se aplica igual que hoy: leer el linaje real (¿fork de red o continuación con crédito?), verificar la licencia, cenar la actividad (push, releases, asuntos) y comparar features. El acta de hoy es el ejemplo escrito de cómo se hace.

Si tu versión instalada deja de actualizarse: tu teléfono no se daña ni se apaga: sigues con tu
Android real y tu app funcionando. Solo dejas de recibir cocinas nuevas en el Hub y ajustes.

Borra sesiones, libera espacio, y la pieza queda donde la dejaste.

Y la regla que no cambia nunca: la puerta es de tu Android, las fundaciones cocinan en público y tu respaldo es tuyo. Ninguna pieza de esta biblioteca te ata a un repositorio: te enseña la calle para que las esquinas cambien sin que tú pierdas el rumbo.

---

#LaBandita #DSU #GSIDynamicSystemUpdates #AndroidDentroDeAndroid #SinRoot #Bootloader #LineageOS
#TrebleDroid #AOSP #VegaBobo #R15Hi #HallazgoDelDueno #WhatsAppDominicano #TecnologiaDominicana

───────────────────

💓 *PULSO 29-OCT-2026 — verificación profunda de La Bandita (pieza 14).*

dormidos · 2 archivados.

*📋 LA FICHA DE HOY*

- **phhusson/treble_experimentations** — «Notes about tinkering with Android Project Treble»
  ★3.556 · su último empuje fue el 2025-01-27 (hace 640 días) · licencia sin archivo LICENSE en su repo (verificado) · Smali · última release v416 (2022-11-09) · ARCHIVADO: historia, no opción viva · https://github.com/phhusson/treble_experimentations

- **VegaBobo/DSU-Sideloader** — «A simple app made to help users easily install GSIs via DSU's Android feature.»
  ★2.344 · su último empuje fue el 2024-03-13 (hace 960 días) · licencia Apache-2.0 · Kotlin · última release 2.03 (2023-04-29) · https://github.com/VegaBobo/DSU-Sideloader

- **ponces/treble_aosp** — «Script and patches for building TrebleDroid AOSP»
  ★311 · su último empuje fue el 2025-07-25 (hace 461 días) · licencia Apache-2.0 · Shell · última release v2025.06.25 (2025-06-25) · ARCHIVADO: historia, no opción viva · https://github.com/ponces/treble_aosp

- **R15Hi/Dsu-Multi-sideloader** — su repo no trae descripción oficial
  ★3 · su último empuje fue el 2026-10-15 (hace 14 días) · licencia Apache-2.0 · Kotlin · última release v2.20 (2026-10-15) · https://github.com/R15Hi/Dsu-Multi-sideloader

*🎯 MINI-QUIZ DE HOY*

*1.* ¿Quién es el más dormido de la pieza?

*2.* ¿Cuál es el repo con más ★ de la pieza, según la medición de hoy?

*3.* La licencia de VegaBobo/DSU-Sideloader, ¿cuál es?

*Respuestas al revés (léelas de atrás para adelante):*

REV|31-30-4202 — redaolediS-USD/oboBageV=1|REV|655.3★ — snoitatnemirepxe_elbert/nossuhhp=2|REV|0.2-ehcapA=3

💓 Hoy, jueves 29 de octubre de 2026, se midieron en vivo 4 repos y 0 enlaces de esta pieza: 4 vivos, 0 firmados con su estado en la ficha. El texto es el de la casa; la ficha, la de hoy.
