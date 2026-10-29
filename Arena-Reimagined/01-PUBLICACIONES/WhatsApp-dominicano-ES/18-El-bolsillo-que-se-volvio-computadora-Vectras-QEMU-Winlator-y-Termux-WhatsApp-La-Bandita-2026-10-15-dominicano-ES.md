*18 — EL BOLSILLO QUE SE VOLVIÓ COMPUTADORA*
*Vectras/QEMU, Winlator, Termux y box64: los sistemas invitados que caben en tu mano (WhatsApp ·
La Bandita · 15-oct-2026 · dominicano-ES)*

*⚡ EN UN RESPIRO*

Tu teléfono lleva dentro una computadora de verdad — y esta pieza es del derecho que llevas AÑOS sin ejercer: instalarle OTROS sistemas invitados. No Android disfrazado (eso fue la gemela 14, el DSU): aquí vienen de VISITA los sistemas de escritorio — Windows, Linux enteros, la PC clásica — emulados o traducidos en vivo.

El anfitrión del censo es **Vectras** (xoureldeen/Vectras-VM-Android, ★2.712 al 15-oct-2026,
GPL-2.0, push del 13-oct): una app de máquina virtual para Android construida sobre QEMU — el
motor de emulación veterano de Linux — que convierte tu bolsillo en sala de máquinas.

A su alrededor, la cuadra completa: **Winlator** (brunodev85, ★19.473, LGPL-2.1) que corre
programas de Windows con Wine y Box86/64; **Termux** (termux-app, ★62.687) el terminal Linux que
cabe en cualquier bolsillo y se estira lo que quieras;

**box64** (ptitSeb, ★5.666, MIT, push del MISMO jueves 15-oct) el traductor que convierte binarios x86_64 en instrucciones que tu chip ARM entiende; y el fork vivo **AnBui2004/Vectras-VM-Emu-Android** (★299, push del 14-oct) que muestra a la familia creciendo por su cuenta. La casa censó la cuadra entera el mismo jueves — y esta guía es su mapa de pasajeros.

*🗺 MAPA DE ESTA GUÍA*

```
├── ⚡ EN UN RESPIRO · ~2 min
├── 🗺 MAPA DE ESTA GUÍA · ~2 min
├── 🌱 LA SEMILLA · ~2 min
├── 📻 LOS CANALES DE LA CUADRA · ~2 min
├── 🧭 QUÉ ES Y QUÉ NO ES · ~2 min
├── 🎒 EL CARGAMENTO · ~2 min
├── 💬 LA CONVERSACIÓN HONESTA · ~2 min
├── 🏭 LA DESPENSA DE DATOS · ~1 min
├── 📼 LA ANALOGÍA MEDIDA CON REGLA · ~2 min
├── 🛠 LOS TALLERES PRÁCTICOS · ~2 min
├── 🧊 MITOS DESMONTADOS · ~2 min
├── ❓ PREGUNTAS FRECUENTES · ~1 min
├── 🧪 CASOS DEL BARRIO · ~1 min
├── 📖 GLOSARIO · ~2 min
├── 😄 EL MEME DE LA PIEZA · ~2 min
├── 🧯 SOLUCIÓN DE PROBLEMAS: LAS CUATRO TRANCAS · ~2 min
├── 🗓 LA SEMANA DE PRUEBA · ~2 min
├── 🗂 CUADERNO DE CAMPO · ~1 min
├── 🏘 EL VECINDARIO DE ESTA PIEZA · ~1 min
├── 🧩 LO QUE ESTA GUÍA NO DICE · ~1 min
├── 🧮 LA FICHA CORTA DE ESTA MAÑANA · ~1 min
├── 🔗 FUENTES · ~1 min
├── 🪧 CARTEL DE LA CASA · ~1 min
├── 🗒 LIBRETA DE FECHAS DE ESTA PIEZA · ~1 min
├── ✍ FIRMA Y DESPEDIDA · ~1 min
├── 🔎 LAS PORTADAS, TRANSCRITAS Y COMENTADAS · ~1 min
├── 🧠 MAPA MENTAL DE LA CASA · ~1 min
├── 📅 EL CRONOGRAMA COMPLETO DE ESTA PIEZA · ~1 min
├── 🎯 MINI-QUIZ DE LA CASA · ~1 min
├── 🧵 CÓMO LEER LAS FUENTES SIN PERDER EL PIE · ~1 min
├── 🎓 LOS TRES ESCENARIOS DE APRENDIZAJE · ~1 min
├── 🧾 EL PLIEGO FINAL DE LA CASA · ~1 min
├── 🌦 LOS TRES FUTUROS DE ESTA PIEZA · ~1 min
├── ❔ SEGUNDA RONDA CORTA · ~1 min
├── 🪴 SI LA PIEZA DESAPARECE O CAMBIA DE DUEÑO · ~1 min
├── 🎬 GUION DE LA PRIMERA SEMANA (la primera tarde) · ~1 min
├── 🌡 PLANTILLA DE MEDICIÓN · ~1 min
├── 🗣 CONVERSACIÓN DEL GRUPO · ~1 min
├── 💡 LOS CINCO POR QUÉS DE LA ESCUELA · ~1 min
├── 📇 FICHAS DE LAS CUATRO PASAJERAS · ~1 min
├── 🎧 LAS DOS VÍAS, UNA TABLA · ~1 min
├── 🎙 LAS VOCES DE LA CUADRA · ~1 min
├── 🕰 CRÓNICA DEL DÍA EN LA CUADRA · ~1 min
├── 🎼 LA SUCESIÓN DE LA ESCUELA · ~1 min
├── 🧿 EL MAPA DE DECISIÓN · ~1 min
├── 🧷 LAS SIETE REGLAS DE LA SALA DE MÁQUINAS · ~1 min
├── 🌟 LO MEJOR DE LA PIEZA EN TRES LÍNEAS · ~1 min
├── 💠 EL CIERRE DE LA CASA · ~1 min
├── 🎞 LO QUE ESTA PIEZA NO DICE · ~1 min
├── 💌 SEGUNDA CARTA AL LECTOR · ~1 min
├── 🎪 LA SALA DENTRO DE LA BIBLIOTECA · ~1 min
├── 📄 LA RECETA EN UNA TARJETA · ~1 min
├── 🏗 QEMU EN DETALLE (para el que quiere el porqué) · ~1 min
├── 🧲 LAS PREGUNTAS DEL FUTURO · ~1 min
├── 🧤 PRIMEROS AUXILIOS DE LA SALA · ~1 min
├── 🎁 LO QUE LA CASA REGALA (y lo que no regala) · ~1 min
├── 🪡 LA ÚLTIMA AGUJA · ~1 min
├── 🍵 TERCERA RONDA DE LA CUADRA · ~1 min
├── 🧫 DOS CASOS MÁS · ~1 min
├── ❄ DOS MITOS EXTRA · ~1 min
├── 📚 GLOSARIO EXTENDIDO · ~1 min
└── 🪢 GUÍA DE LECTURA RÁPIDA (los cinco minutos) · ~1 min
```

⏱ *Lectura total: 76 min*

*🌱 LA SEMILLA*

Nace de dos lecturas del mismo día. La primera: la gemela 14 (DSU — Android dentro de Android)
dejó la puerta abierta a la pregunta que el barrio hacía desde la tarde: «¿y si quiero probar
WINDOWS o LINUX, no otro Android?».

La respuesta no cabía en la gemela: cabía en un mapa propio — porque probar otro Android es CAMBIAR de sistema (dual boot suave, imagen firmada por el proyecto del sistema), y correr una PC de escritorio es INVITAR un sistema completo a vivir dentro del tuyo, con su CPU emulada o su software traducido al vuelo. Dos deportes distintos; dos leyes distintas; dos mapas.

La segunda lectura: el censo integral del dueño (5.789 forks auditados el 15-oct) trajo Vectras a la mesa — y su familia entera: la app madre (★2.712), el fork de AnBui2004 (★299 con push del 14-oct), y media docena de espejos con 1-3 estrellas que enseñan la anatomía de un proyecto popular. Hallazgo del dueño, censo abierto, mismo día: ley de la casa.

La promesa honesta: al final de esta pieza sabes qué es emular y qué es traducir, qué sistema invitado cabe en TU hierro, cómo entra un invitado sin romper la casa, y cuándo NO vale la pena. La vara de la casa aplica completa: nada de promesas sin hierro probado.

*📰 EL CENSO DE LA CUADRA (multi-placa, 15-oct-2026)*

· Vectras-VM-Android — xoureldeen — ★2.712 al pulso de cierre (★2.711 en el censo de la tarde: +1 en el día) · push 13-oct-2026 · GPL-2.0 · 15 asuntos · «It's a Virtual Machine App for Android Which is Based on QEMU». La nave nodriza del bolsillo: interfaz para QEMU, imágenes de invitados, perfiles.

· AnBui2004/Vectras-VM-Emu-Android — ★299 · push 14-oct-2026 · GPL-2.0 · 11 asuntos — el fork activo: mismo ADN QEMU, cocina propia. La casa lo lee como señal: la familia se reproduce (media docena de espejos más con 1-3 estrellas en el TSV del censo).

· Winlator — brunodev85 — ★19.473 · push 22-sep-2026 · LGPL-2.1 · 403 asuntos · «Android application for running Windows applications with Wine and Box86/Box64». La ventana de Windows: no virtualiza la PC entera — traduce la capa de Windows (Wine) y los binarios x86 (Box86/64) para que los programas corran nativos en tu chip.

· Termux — termux/termux-app — ★62.687 · push 26-sep-2026 · 641 asuntos — el terminal Linux de bolsillo: no emula nada, ES Linux por capas; el escalón más bajo y más sano de la escalera.

· box64 — ptitSeb — ★5.666 · push 15-oct-2026 (EL MISMO jueves del censo) · MIT · 182 asuntos · «Linux Userspace x86_64 Emulator with a twist, targeted at ARM64, RV64...». El traductor: convierte instrucciones x86_64 en ARM64 al vuelo — es el músculo invisible debajo de Winlator y de media cuadra.

· ish (iSH) — ish-app — ★20.582 · push 13-oct-2026 · «Linux shell for iOS» — la placa de la OTRA orilla: en iPhone también cabe Linux, por emulación x86. La casa la cita para la comparación, no como camino.

La lectura del día: box64 empujando el MISMO jueves 15-oct-2026 del censo, Vectras subiendo
(+1), el fork de AnBui con push de ayer, Termux y Winlator descansando semanas de mantenimiento
— la cuadra de la emulación está VIVA en sus dos velocidades: los motores (box64) a diario, las
naves (Vectras/Winlator) a la semana.

*🏛 LAS TRES ERAS DE LA PC EN EL BOLSILLO (fechado de archivo)*

Era del caparazón (años 90-2000, archivo): emuladores de DOS y Windows viejos en teléfonos tecla — demos de ingeniería que corrían tres minutos y agotaban la batería. La lección que quedó: el hierro del bolsillo no daba — la idea ya era buena.

Era del terminal (2015-2022, censo): Termux prueba que el bolsillo NO necesita emulación para tener Linux: un terminal nativo, con paquetes de verdad, terminales completos, editores, compiladores — ★62.687 al 15-oct-2026 lo coronan como el terminal más importante de Android. El software libre hizo lo que la tienda no quiso.

Era de la traducción (2023-2026, censo): box64 (y su hermano box86) hacen el milagro de
eficiencia: traducir x86_64 a ARM64 AL VUELO, sin emular un chip completo — y sobre ese músculo
suben Winlator (la ventana de Windows, ★19.473) y Vectras (la nave de invitados completos sobre
QEMU, ★2.712).

La PC entera ya no es un caparazón: es una traducción viva que corre a velocidad útil.

*⚖ LA VARA DE LOS INVITADOS (lo que hay que saber antes de abrir la puerta)*

Cláusula 1 — Emular no es gratis: un invitado emulado (QEMU con CPU completa) usa una fracción de tu potencia — el rendimiento depende del hierro ANTES que del software. La vara: invitados livianos (XP, distros Linux mínimas) para hierros medianos; invitados pesados (Windows 10/11) solo en hierros tope y con paciencia fechada.

Cláusula 2 — Traducir es el atajo: lo que box64 traduce corre rápido porque NO hay chip emulado
— tu CPU ejecuta casi todo. Por eso Winlator (Wine+Box64) corre mejor que una máquina virtual
completa de Windows en el mismo hierro.

La casa lo escribe así: programa suelto → traducción; sistema entero → emulación; tu hierro
decide la talla.

Cláusula 3 — Las imágenes de invitados son SU propia vara: cada invitado (Windows, Linux, DOS) se consigue por SU canal legal — ISOs que ya posees, distribuciones libres (Alpine, Debian, TinyCore), o imágenes oficiales de proyectos. La casa NO señala escuras de ISOs: lo que ya es tuyo o lo que es libre, eso viaja.

Cláusula 4 — Tu sistema anfitrión no se toca: el invitado vive dentro de la app (archivo de
disco virtual, memoria reservada, CPU compartida). Sin root, sin bootloader, sin tocar el
anfitrión.

Si algo sale mal, se apaga el invitado y la casa sigue igual — la garantía de esta escuela es el
INVITADO se rompe, no el anfitrión.

*📻 LOS CANALES DE LA CUADRA*

Vectras y su familia, en sus casetas (xoureldeen la madre, AnBui2004 el fork activo — ambos
GPL-2.0 al 15-oct-2026). Winlator, en su caseta (brunodev85, LGPL-2.1).

Termux, en la suya (termux-app — con SU historia: el terminal que sobrevivió a la política de la
tienda; su canal por SU sitio, como manda la pieza 01). box64, en la caseta de ptitSeb (MIT,
push del 15-oct-2026).

Y la otra orilla (iSH, ish-app, ★20.582, push 13-oct-2026): iOS también tiene su sala de
máquinas — con las leyes de SU isla.

*🧭 QUÉ ES Y QUÉ NO ES*

· ES invitar sistemas a tu teléfono: una app de bolsillo (Vectras/Winlator/Termux) que corre un invitado (Windows, Linux, DOS, un terminal) SIN tocar tu anfitrión Android.

· NO ES root: ni bootloader, ni kernel, ni permisos de sistema — el invitado vive en SU archivo dentro de la app. La garantía del teléfono no se toca (cláusula 4).

· NO ES lo mismo que la gemela 14 (DSU): el DSU CAMBIA tu Android por otro Android temporal; aquí el invitado es otra ESPECIE de sistema (escritorio) y vive aparte, en su disco virtual. Dos deportes: uno es mudar el piso; el otro es alquilar un cuarto.

· NO ES milagro de velocidad: la emulación cobra peaje (cláusula 1) y la traducción (box64) tiene techo. Los números honestos de cada hierro los pone TU semana de prueba — la casa no vende FPS.

· ES legal si tus imágenes lo son (cláusula 3): tus ISOs, tus licencias, las distribuciones libres. La escura de ROMs no existe en esta casa.

· ES compatible con la escalera de la casa: Termux abajo (el escalón bajo, ★62.687 al 15-oct-2026), Vectras arriba (invitados completos, ★2.712), Winlator al medio (programas de Windows sin PC completa, ★19.473). Empieza abajo: la escalera perdona.

*🎒 EL CARGAMENTO*

· La nave: Vectras por SU Releases. O el fork de AnBui2004 si tu cuaderno lo prefiere (GPL-2.0 ambos al 15-oct-2026): mismos derechos, cocina distinta.

· Un invitado con placa: una ISO de distribución libre (la lista de la casa: Alpine por liviana, Debian por hermana grande, TinyCore por la lección) o la imagen que YA posees con licencia.

· Para la ventana de Windows: Winlator por SU Releases (★19.473 al 15-oct-2026, LGPL-2.1) — con SUS dependencias (Wine y los boxes que SU guía indica).

· Tu cuaderno: cada invitado con fecha, versión, consumo — el manifiesto de pasajeros se anota (la casa no improvisa salas de máquinas).

*💬 LA CONVERSACIÓN HONESTA*

—«¿Esto me va a romper el teléfono?» — El invitado vive aparte (cláusula 4): lo peor que puede
romper es SU disco virtual — se borra el archivo y listo. El anfitrión sigue igual; la garantía
sigue igual.

—«¿Corre Windows 11?» — La vara del hierro: 10/11 completos sobre QEMU emulado piden hierro tope
y pagan peaje; programas sueltos vía Winlator (traducción) corren bien en hierro medio. La casa
no receta milagros: receta tallas.

—«¿Para qué quiero esto de verdad?» — Para lo que la tienda no da: un navegador completo con extensiones dentro de Debian; un juego viejo de Windows que solo existe en tu respaldo; un servidor de prueba en Termux; aprender Linux SIN arriesgar tu instalación. La PC del bolsillo es utilidad con paciencia — no remplazo del teléfono.

—«¿Y la batería?» — El peaje se siente: emulación activa come batería como un videojuego pesado. La casa la mide en la semana de prueba (la plantilla de la 17 sirve igual aquí) y la regla es una: sesión de invitado con propósito; sin propósito, sesión cerrada.

*🔧 LA RECETA DEL PRIMER INVITADO (por la vía sana)*

Peldaño 1 — la nave. Vectras por SU Releases (paquete oficial del proyecto, fechado). Instala
con tu instalador de la pieza 01. Placa al 15-oct-2026: ★2.712, GPL-2.0, 15 asuntos, push del
13-oct.

Peldaño 2 — el invitado chico primero. Descarga la ISO de una distribución liviana (Alpine o
TinyCore — libres, de SU sitio oficial: la vara de la cláusula 3). Megabytes, no gigabytes: la
primera visita es corta y educada.

Peldaño 3 — la sala. En Vectras: nuevo invitado, apunta la ISO, dale disco virtual pequeño (2-4
GB), memoria razonable (la mitad de lo que la app sugiere si tu hierro es modesto). Guarda el
perfil con fecha.

Peldaño 4 — el encendido. Arranca el invitado.

La primera vez tarda (está virtualizando una máquina entera): paciencia de casa. Si no arranca,
revisa la nota del perfil (memoria, tipo de CPU) — el taller de Vectras (15 asuntos al
15-oct-2026) tiene tu caso en fila.

Peldaño 5 — la visita. Dentro del invitado: mira, prueba, apaga BIEN (shutdown del sistema
invitado — nunca lo mate a lo bruto: su disco virtual lo agradecerá). Anota en el cuaderno:
¿arrancó?, ¿en cuánto?, ¿uso utilizable o demostración?

Peldaño 6 — la escalera. Si el invitado chico vivió bien: sube un peldaño (Debian con escritorio
ligero; o Winlator para un programa de Windows concreto; o Termux si tu deseo era el terminal —
el escalero más barato y el que más enseña).

Si no vivió bien: tu hierro habló — escúchalo y quédate en Termux, que a ★62.687 (censo
15-oct-2026) tiene mucha escuela que dar.

*🏭 LA DESPENSA DE DATOS*

★2.712 — Vectras al pulso (censo tarde ★2.711: +1 en el día) · GPL-2.0 · 15 asuntos. · ★299 — el
fork de AnBui2004 (push 14-oct). · ★19.473 — Winlator (LGPL-2.1 · 403 asuntos). · ★62.687 —
Termux (641 asuntos). · ★5.666 — box64 (MIT, push del 15-oct-2026). · ★20.582 — iSH en la otra
orilla (push 13-oct).

· 6 — espejos de Vectras con 1-3 estrellas en el TSV (la familia se reproduce). · 0 — root necesario en toda la cuadra.

*📼 LA ANALOGÍA MEDIDA CON REGLA*

Tu teléfono es una casa. La gemela 14 (DSU) fue mudar el MUEBLE de un cuarto (otro Android en tu
propio piso).

Vectras es construir dentro del garaje un apartamento completo para INVITADOS (QEMU virtualiza
una PC entera). Winlator es poner una ventana por donde entran programas de Windows ya
traducidos (Wine+Box64).

Termux es el sótano-taller: no es otro mundo — es TU casa con más sótano. Y box64 es el
INTÉRPRETE de la casa: traduce el idioma x86 al idioma ARM al vuelo — sin intérprete, los
invitados no se entienden con tu chip.

*🛠 LOS TALLERES PRÁCTICOS*

· Taller 1 — el primer invitado (receta de arriba): distribución liviana, disco chico, visita corta, cuaderno al día.

· Taller 2 — Termux en serio: el escalón bajo (apt de verdad, SSH a tu casa, un bot de Telegram en Python — la escuela completa del terminal).

· Taller 3 — la ventana de Windows: Winlator con UN programa tuyo (un juego viejo con licencia, un editor viejo): probar, medir, decidir.

· Taller 4 — el fork: misma ISO en Vectras madre y en el fork de AnBui2004; el cuaderno decide quién manda en tu hierro (la casa no receta forks: los fecha).

· Taller 5 — la otra orilla (solo lectura): iSH en un iPhone ajeno; comparar con Termux; aprender que las leyes de cada isla mandan.

*🧊 MITOS DESMONTADOS*

Mito 1 — «Emular es lo mismo que virar el teléfono.» NO: la emulación vive DENTRO de una app
(cláusula 4); el virar (flashear) cambia el piso de la casa. El invitado se apaga; el anfitrión
ni se entera.

Mito 2 — «Necesito root para esto.» NO en toda la cuadra: Vectras, Winlator y Termux funcionan
sin root al 15-oct-2026. El root es del límite norte (APatch, otro mapa); la sala de máquinas es
de la casa normal.

Mito 3 — «Es para jugarse los juegos nuevos.» Los juegos pesados modernos NO son el plato de esta escuela (el peaje de emulación lo cobra); los clásicos, los de tu respaldo y las herramientas sí. Quien prometa Cyberpunk en el bolsillo está vendiendo el camión sin placas.

Mito 4 — «Vectras es pirata de Windows.» La nave no trae invitados: trae LA SALA (GPL-2.0,
código público). El invitado lo pones TÚ con SU vara (cláusula 3): tu licencia o una
distribución libre. La escura de ROMs no es de esta escuela.

Mito 5 — «Termux quedó viejo.» Al revés: ★62.687 al 15-oct-2026 — el terminal más estrellado de
la cuadra (empata con la corona de la casa en fama relativa). El sótano no compite con el
garaje: lo sostiene.

*❓ PREGUNTAS FRECUENTES*

¿Qué hierro necesito? — Para invitados livianos, hierro medio; para Windows completo, tope. La regla: el invitado chico primero, SIEMPRE (peldaño 2). · ¿Puedo romper mi teléfono? — No (cláusula 4): lo rompible es el disco virtual del invitado. · ¿Windows vía Winlator es Windows real? — Es la capa de compatibilidad (Wine) + traducción (Box64): los programas corren;

el SISTEMA no es el mismo plato. La casa lo escribe así para que no se confunda. · ¿Vectras o el
fork? — Cuaderno: la madre tiene más ojos (★2.712 vs ★299), el fork tiene más cocina reciente
(push 14-oct vs 13-oct).

Ambos GPL-2.0: mismos derechos, distinto pulso. · ¿La batería sufre? — La sesión de invitado sí
(peaje de emulación); cerrada la sesión, nada.

· ¿Sirve para programar de verdad? — Termux sí (es Linux real por capas); el invitado completo también, con paciencia. La escuela de programadores empieza en el sótano. · ¿iOS puede lo mismo? — La otra orilla tiene iSH (★20.582 al 15-oct-2026) — con las leyes de SU isla: la casa cita, no cruza. · ¿Y juegos de Android dentro del invitado?

— Estás invitando al revés: el invitado es de escritorio. La casa no mezcla recetas.

*🧪 CASOS DEL BARRIO*

Caso 1, el herrero de Discord: quería probar Debian sin formatear su máquina vieja — la instaló
como invitado en su teléfono, la probó una semana con su teclado Bluetooth, y decidió la mudanza
de la PC con datos, no con fe.

· Caso 2, la jugadora del respaldo: un juego clásico de 2003 que solo vive en su CD del colegio — Winlator lo corrió en su hierro medio a velocidad honesta (anotada en su cuaderno con fecha). · Caso 3, el aprendiz: Termux + un bot de Python en su teléfono; seis meses después su primer servidor casero. Su frase para el acta: «empecé en el sótano y el sótano me creció la casa».

*📖 GLOSARIO*

Invitado — el sistema que vives dentro de la app (Windows, Linux, DOS): vive en SU disco
virtual. · Anfitrión — tu Android normal: no se toca (cláusula 4). · QEMU — el motor de
emulación veterano: el corazón de Vectras (GPL-2.0 al 15-oct-2026). · Disco virtual — el archivo
que hace de disco duro del invitado: se apaga, se copia, se respalda como un archivo que es.

· Traducción — convertir instrucciones x86 a ARM al vuelo (box64, MIT, push del 15-oct-2026): rápida, con techo. · Emulación — simular un chip entero (QEMU): lenta pero completa. · Wine — la capa de compatibilidad de Windows sobre Linux: la ventana de Winlator. · Fork — la hija que toma el ADN y cocina su camino (AnBui2004 ★299): fechada, con su pulso.

*😄 EL MEME DE LA PIEZA*

«—Mi teléfono tiene Windows. —¿Lo flasheaste? —No, mijo: le construí un apartamento en el
garaje. Windows no toca mi piso; solo paga peaje.» El barrio entendió la cláusula 4 mejor que
muchos tutoriales.

*🧯 SOLUCIÓN DE PROBLEMAS: LAS CUATRO TRANCAS*

Tranca 1 — «El invitado no arranca.» Memoria o CPU del perfil mal puestas: baja la memoria a la
mitad, prueba perfil de CPU básico, relee la nota del proyecto (15 asuntos abiertos al
15-oct-2026: tu hierro no es el primero).

· Tranca 2 — «Corre lento.» Es el peaje (cláusula 1): invitado más chico, o traducción en vez de emulación (Winlator para programas), o Termux para lo que sea terminal. La talla del invitado la dicta el hierro. · Tranca 3 — «El disco virtual se llenó.» Creció tu invitado: respalda el archivo del disco (es UN archivo), crea uno más grande o limpia dentro del invitado.

Y añade la lección al cuaderno: el disco se dimensiona ANTES. · Tranca 4 — «Maté el invitado a lo bruto y no arranca.» El disco virtual quedó sucio: restauras el respaldo (si lo tenías — peldaño 6 del cuaderno) o reconstruyes el invitado (15 minutos con ISO en mano). La lección es la del taller: apagar bien es parte del oficio.

*🗓 LA SEMANA DE PRUEBA*

Día 1 — nave instalada, primer invitado chico encendido y apagado BIEN. Día 2 — visita útil:
navegar dentro del invitado, escribir un archivo, sacarlo (carpeta compartida o respaldo del
disco).

Día 3 — Termux: instalación y primera instalación de paquetes. Día 4 — comparación de consumo
con la plantilla de la 17 (batería/datos).

Día 5 — Winlator con UN programa con licencia: probar y medir. Día 6 — el cuaderno decide: ¿qué
invitado queda en tu sala?

Día 7 — veredicto con vara: la PC del bolsillo entra a tu vida o se apaga sin drama. La casa
vende semanas, no conversiones.

*🗂 CUADERNO DE CAMPO*

Fila 1 — cada invitado: fecha, versión, memoria, disco, canal de la ISO (SIEMPRE con fecha — la
vara de las fuentes manda). Fila 2 — tiempos de arranque y veredicto de uso.

Fila 3 — batería/datos por sesión. Fila 4 — pushes de la cuadra (box64 empuja a diario; la nave,
a la semana — anótalos).

Fila 5 — la regla que no se borra: apagar bien, respaldar el disco, invitado chico primero.

*🏘 EL VECINDARIO DE ESTA PIEZA*

Pieza 14 (gemela FB) — Android dentro de Android (DSU): el PRIMO hermano del DSU con su Android
invitado. · Pieza 17 — el taller de parcheo: la otra forma de tener lo que la tienda no da (esta
cuadra NO parchea invitados: los aloja). · Pieza 01 — la vía sana de instaladores (Termux entra
por SU canal — la pieza lo explica).

· En cola de la casa: el límite norte (APatch, ★8.053 al 15-oct-2026) y la caja de integridad (★2.747) — los vecinos del kernel, donde la sala de máquinas NI ENTRA (cláusula 4 manda: sin root, sin tocar).

*🧩 LO QUE ESTA GUÍA NO DICE*

No dice qué versión exacta de cada invitado instalar: la nota de tu app y el sitio oficial de la
distribución mandan (la casa lee, no adivina tallas ajenas). · No dice que Windows completo
corra bien en tu hierro: la vara del peaje (cláusula 1) solo se lee con TU semana de prueba.

· No dice dónde hay ISOs de Windows: lo tuyo o lo libre (cláusula 3) — la escura de imágenes no existe aquí. · No receta el fork ni la madre: los FECHA (★2.712 vs ★299 al 15-oct-2026) y el cuaderno decide. · Y no dice que la sala de máquinas sea para todos: es un hobby con peaje — el que quiera utilidad sin peaje tiene Termux (el sótano nunca desilusiona).

*🧮 LA FICHA CORTA DE ESTA MAÑANA*

La PC entera cabe en el bolsillo por DOS caminos: traducir (box64: rápido, con techo — Winlator
★19.473) o emular (QEMU: completo, con peaje — Vectras ★2.712), todo al 15-oct-2026. El sótano
(Termux ★62.687) sostiene toda la cuadra sin root.

La vara: invitado chico primero, ISO con licencia, apagar bien, cuaderno siempre.

*🔗 FUENTES*

Caseta de la nave: github.com/xoureldeen/Vectras-VM-Android — ★2.712 al pulso del 15-oct-2026,
GPL-2.0, 15 asuntos, push 13-oct: leída el 15-oct-2026. · El fork activo:
github.com/AnBui2004/Vectras-VM-Emu-Android — ★299, GPL-2.0, push 14-oct-2026. · La ventana:
github.com/brunodev85/winlator — ★19.473, LGPL-2.1, 403 asuntos, push 22-sep-2026.

· El sótano: github.com/termux/termux-app — ★62.687, 641 asuntos, push 26-sep-2026. · El traductor: github.com/ptitSeb/box64 — ★5.666, MIT, 182 asuntos, push del MISMO 15-oct-2026. · La otra orilla: github.com/ish-app/ish — ★20.582, push 13-oct-2026. · Historia de eras: archivo fechado de la casa.

*PULSO AL CORTE — 15-OCT (mapa vivo #1)*

```
 Vectras (nave)      ★2.711 -> ★2.712 (+1)
 AnBui2004 (fork)   push 14-oct
 box64 (traductor)  push 15-oct (el mismo jueves)
```
Nacimiento con la cuadra en movimiento:
el traductor publicando el MISMO jueves 15-oct-2026.
Caja apilada; nada borrado (mapa-maestro).

*📝 NOTA DE VERIFICACIÓN — 15 DE OCTUBRE DE 2026*

Cómo se verificó (repítelo tú): cada estrella, push, licencia y asunto salió de la API pública
de GitHub medida el 15-oct-2026 (censo tarde de la casa + pulso propio de esta pieza);

las descripciones se leyeron verbatim de las casetas («It's a Virtual Machine App for Android Which is Based on QEMU», «Android application for running Windows applications with Wine and Box86/Box64», «Linux Userspace x86_64 Emulator...», «Linux shell for iOS»)

las eras históricas viajan como fechado de archivo; y ninguna promesa de rendimiento viaja sin su vara de peaje.

El que mide hoy, re-mide mañana.

*🪧 CARTEL DE LA CASA*

· El invitado vive aparte: tu Android no se toca (cláusula 4).

· Invitado chico primero — SIEMPRE (peldaño 2).

· ISO con licencia: lo tuyo o lo libre (cláusula 3).

· El peaje es real: mide antes de prometer (cláusula 1).

· Apagar bien es parte del oficio (tranca 4).

· El cuaderno manda: fecha, versión, veredicto.

*🗒 LIBRETA DE FECHAS DE ESTA PIEZA*

· 2015 — nace Termux (TSV): la era del terminal.

· 2023-11 — nace Vectras (TSV): la era de la nave sobre QEMU.

· 15-oct-2026 — box64 empuja el MISMO día del censo (★5.666).

· 14-oct-2026 — el fork de AnBui2004 publica (★299).

· 13-oct-2026 — push de la nave (★2.712) y de iSH (★20.582).

· 26-sep-2026 — último push de Termux (★62.687).

· 22-sep-2026 — último push de Winlator (★19.473).

· 15-oct — la casa censó la cuadra entera y nació esta guía certificada.

*✍ FIRMA Y DESPEDIDA*

La sala de máquinas queda abierta al 15-oct-2026: nave ★2.712, ventana ★19.473, sótano ★62.687, traductor ★5.666 con push del mismo jueves — toda la cuadra con placa y ninguna con humo. La vara es la de siempre: invitado chico primero, licencia a la vista, peaje medido, cuaderno al día.

Y la regla que no cambia: tu teléfono es TU casa — los invitados dan alegrías cuando se respetan
y dolores de cabeza cuando se sobrecargan. El garaje es chico; la escuela es grande.

*— La Bandita · guía 18 · 15 de octubre de 2026 · censo medido por API*

*🔎 LAS PORTADAS, TRANSCRITAS Y COMENTADAS*

La nave (Vectras, leída el 15-oct-2026): «It's a Virtual Machine App for Android Which is Based on QEMU» — dos hechos y cero adorno: qué es (VM app) y sobre qué pie (QEMU). La casa comenta: la honestidad técnica de una portada así dura años.

GPL-2.0 en la placa: la sala es pública. · El fork (AnBui2004): MISMA frase, cocina propia — los
forks honestos citan su linaje;

la casa los lee por el push, no por la portada (14-oct vs 13-oct al censo). · La ventana (Winlator): «Android application for running Windows applications with Wine and Box86/Box64» — la receta completa en una línea: capa (Wine) + traducción (Box86/64). 403 asuntos: una ventana muy concurrida.

· El traductor (box64): «Linux Userspace x86_64 Emulator with a twist, targeted at ARM64, RV64...» — el «with a twist» es la modestia del que hace magia a diario: push del MISMO jueves 15-oct-2026 del censo.

*🧠 MAPA MENTAL DE LA CASA*

La escuela → invitar sistemas de escritorio SIN tocar el anfitrión. · Los cuatro pasajeros →
nave (Vectras ★2.712), ventana (Winlator ★19.473), sótano (Termux ★62.687), traductor (box64
★5.666 del censo 15-oct-2026). · Las dos vías → emular (completo, peaje) / traducir (rápido,
techo). · La vara → invitado chico primero · ISO con licencia · apagar bien · cuaderno.

· El límite → sin root: el kernel es de otro mapa (APatch en cola). · La diferencia con la 14 → DSU muda tu Android; aquí el invitado es OTRA especie y vive aparte.

*📅 EL CRONOGRAMA COMPLETO DE ESTA PIEZA*

Años 90-2000 — era del caparazón (archivo): la idea buena en hierro chico. · 2015 — Termux nace:
el terminal nativo prueba el camino (TSV). · 2016 — box86/box64 linaje (ptitSeb, TSV): la era de
la traducción se siembra. · 2023-11-08 — nace Vectras (TSV): la nave moderna. · 2026 — la
familia se reproduce: fork de AnBui2004 + media docena de espejos (TSV).

· 15-oct-2026 — censo tarde: Vectras ★2.711 · pulso de cierre: ★2.712 (+1) con box64 empujando el mismo día — y nacimiento de la guía 18 certificada.

*🎯 MINI-QUIZ DE LA CASA*

Cinco. Las respuestas van AL REVÉS al pie.

1. ¿Cuáles son los cuatro pasajeros de la cuadra y sus estrellas al 15-oct-2026?

2. ¿Qué diferencia hay entre traducir y emular, y quién hace cada cosa?

3. ¿Qué prohíbe la cláusula 3 y qué permite?

4. ¿Por qué Winlator corre mejor que una VM completa de Windows en el mismo hierro?

5. ¿En qué se diferencia esta pieza de la gemela 14 (DSU)?

Respuestas al revés:

REV|666.5★ 46xob rotcudart · 786.26★ xumreT onatós · 374.91★ rotalniW anatnev · 217.2★ sartceV evan=1|REV|)ejaep noc otelpmoc ,UMEQ( oretne pihc le alumis ralume ;)ohcet noc odipár ,46xob( oleuv la MRA→68x etreivnoc ricudart=2|REV|lanac US rop serbil senoicubirtsid sal y aicnecil noc oyut ol etimrep ;arucse ed sOSI ebíhorp=3|REV|odot isac atuceje UPC ut — soiranib sol ecudart 46xob y apac al edip eniW :pihc alume ON euqrop=4|REV|etrapa eviv y eicepse ARTO se odativni le íuqa ;etnemlaropmet diordnA ut aibmac USD le=5

(Las respuestas correctas, al derecho: 1=nave Vectras ★2.712 · ventana Winlator ★19.473 · sótano Termux ★62.687 · traductor box64 ★5.666; 2=traducir convierte x86→ARM al vuelo (box64, rápido con techo), emular simula el chip entero (QEMU, completo con peaje)

3=prohíbe ISOs de escura; permite lo tuyo con licencia y las distribuciones libres por SU canal; 4=porque NO emula chip: Wine pide la capa y box64 traduce los binarios — tu CPU ejecuta casi todo; 5=el DSU cambia tu Android temporalmente

aquí el invitado es OTRA especie y vive aparte.)

*🧵 CÓMO LEER LAS FUENTES SIN PERDER EL PIE*

Cuatro placas y una orilla. Las cuatro pasajeras se leen por TRIPLE (estrellas, push, asuntos) y se COMPARAN entre hermanas: nave ★2.712 con 15 asuntos es proyecto joven en crecimiento; ventana ★19.473 con 403 asuntos es ventana concurrida de barrio grande; sótano ★62.687 con 641 es institucional; traductor ★5.666 con push del mismo día es motor vivo.

La orilla (iSH) se lee para comparar leyes de islas, no para cruzar. Y la regla: cada placa con
fecha en su línea — el que mide hoy, re-mide mañana.

*🎓 LOS TRES ESCENARIOS DE APRENDIZAJE*

El curioso del escritorio → receta de 6 peldaños con invitado liviano; su primera sala vale más
que diez videos. · El programador en pañales → Termux directo: es Linux real, sin peaje, y su
escuela es infinita (el caso 3 del barrio: del bot al servidor en seis meses).

· El coleccionista de hierros viejos → Winlator como testamento digital: sus juegos y programas con licencia, rescatados del cajón a la sala — el archivo familiar que por fin corre de nuevo.

*🧾 EL PLIEGO FINAL DE LA CASA*

1. Cuadra: nave ★2.712 + ventana ★19.473 + sótano ★62.687 + traductor ★5.666 (todo con licencia
pública, al 15-oct-2026).

2. Dos vías: emular (completo, peaje) / traducir (rápido, techo).

3. Invitado chico primero — el hierro manda la talla.

4. ISO con licencia: lo tuyo o lo libre; escura, nunca.

5. Apagar bien y respaldar el disco virtual.

6.

Sin root: el kernel es de otro mapa. La sala de máquinas se anota.

*🌦 LOS TRES FUTUROS DE ESTA PIEZA*

Futuro A — la traducción gana terreno: box64 empuja a diario (push del MISMO censo); cada versión traduce más rápido y más cosas — el peaje baja y la ventana (Winlator) crece con él. Señal: releases de box64 con mejoras de compatibilidad, fechados.

Futuro B — la nave madura: Vectras (★2.712) y su fork (★299, push 14-oct) compiten por perfiles más fáciles y más invitados de fábrica; si la nave diera perfiles listos para distribuciones libres, la puerta de entrada del barrio se achica de difícil a fácil. Señal: asuntos cerrados de «perfil para X» en ambos talleres.

Futuro C — la cuadra se une: la historia dice que Termux, box64 y Wine ya conviven dentro de Winlator; el próximo salto es la integración (un sótano que alimenta la ventana, una nave que usa el traductor). Señal: cruces entre proyectos en las portadas, fechados.

*❔ SEGUNDA RONDA CORTA*

¿Sirve para estudiar para certificaciones de Linux? — Termux y el invitado Debian son escuela real: sí, con teclado Bluetooth y cuaderno. ¿Puedo correr mi antivirus de Windows en Winlator? — NO: los programas que tocan el sistema (drivers, antivirus) viven por DEBAJO de la capa de Wine — la ventana da para programas de usuario, no para dueños de sistema.

¿Cuánto espacio necesito? — Invitado chico: 2-4 GB; Debian con escritorio: 8-16; Windows completo: más de lo que tu hierro quiera dar (la vara del peaje, otra vez). ¿Se puede compartir archivos con Android? — Sí: carpeta compartida o respaldo del disco virtual (es UN archivo: cópialo, muévelo, respáldalo).

¿Y si quiero MUCHO más rendimiento?

— Tu hierro habló: la respuesta es hierro, no promesa. La casa no vende fe.

*🪴 SI LA PIEZA DESAPARECE O CAMBIA DE DUEÑO*

Si la nave se apaga: tu invitado vive en SU disco virtual (un archivo portable) y el ADN (GPL-2.0) sobrevive en forks — el fork de AnBui2004 (★299, push 14-oct-2026) ya demuestra la ruta. Si Winlator se muda: sus 403 asuntos documentan cada caso de barrio; y Wine es más viejo que la ventana — el plato base no muere con la cocina.

Si Termux desapareciera (no hay señal de eso a ★62.687): su escuela está en mil tutoriales
fechados y su ADN en cada terminal de la cuadra. Y si tu cuaderno tiene las fechas, ninguna
mudanza te encuentra solo.

*🎬 GUION DE LA PRIMERA SEMANA (la primera tarde)*

19:00 — nave instalada por SU Releases; receta leída entera. · 19:15 — ISO liviana de SU sitio
oficial (con fecha en el cuaderno). · 19:30 — primer invitado: disco chico, memoria a media
recomendación. · 20:00 — primer encendido (paciencia: está virtualizando una PC entera). · 20:20
— visita corta: mirar, tocar, apagar BIEN.

· 20:30 — cuaderno: ¿arrancó?, ¿en cuánto?, ¿uso real o demostración? · 21:00 — cierre: fecha y veredicto. El resto de la semana, según la sección 🗓.

*🎹 EL TECLADO Y EL CABLE (el equipo que nadie cuenta y todos necesitan)*

La sala de máquinas de bolsillo tiene un secreto de ergonomía: el teclado Bluetooth (cualquiera
de los que el barrio ya tiene) convierte la visita al invitado de «dolor de dedos» a «sesión de
verdad»; y el cable de carga SIEMPRE (el peaje de batería no se negocia — cláusula 1).

Con teclado, la PC del bolsillo deja de ser demostración y se vuelve oficina de emergencia, aula
de estudio, o el taller del juego viejo. La casa lo escribe porque ningún censo lo mide y TODA
semana de prueba lo confirma.

*🌡 PLANTILLA DE MEDICIÓN*

```
 DIA  | ARRANQUE seg | USO min | BATERIA % | NOTAS
 1    |              |         |           | primer encendido
 2    |              |         |           |
 3    |              |         |           | carga + compartida
 4    |              |         |           | comparar con dia 1
 5    |              |         |           |
 6    |              |         |           | Winlator si toca
 7    |              |         |           | veredicto con vara
```

*🗣 CONVERSACIÓN DEL GRUPO*

Hilo 1 — «pásame la ISO que tienes»: respuesta de cartel: lo tuyo o lo libre (cláusula 3) — y el
sitio oficial de la distribución es gratis SIEMPRE: no hay ISO que valga la escura. · Hilo 2 —
«¿me juego el FIFA nuevo?»: la vara del peaje manda: juegos pesados NO son el plato (mito 3); el
clásico con licencia sí.

· Hilo 3 — «se me murió la máquina virtual»: tranca 4 — el disco virtual es UN archivo: ¿lo respaldaste? Si no: reconstruir (15 minutos con ISO en mano) y la lección al cuaderno. · Hilo 4 — «¿esto da virus?»: el invitado vive aparte y las ISOs con licencia no traen sorpresas; el virus viaja por la escura — otra vez la cláusula 3.

· Hilo 5 — «¿puedo quitar Termux si ya uso la nave?»: puedes, pero no conviene: el sótano sostiene (SSH, respaldos, scripts) — la cuadra entera usa el sótano aunque viva en el garaje.

*💡 LOS CINCO POR QUÉS DE LA ESCUELA*

¿Por qué invitar en vez de flashear? Porque el anfitrión no se toca (cláusula 4): la garantía,
los datos y el teléfono siguen iguales.

¿Por qué invitado chico primero? Porque la talla la dicta el hierro (cláusula 1) y la primera
lección debe vivir.

¿Por qué ISO con licencia? Porque la escura es la única forma REAL de estropear esta escuela
(cláusula 3).

¿Por qué medir el peaje?

Porque la promesa sin hierro es fe — y esta casa no vende fe. ¿Por qué cuaderno? Porque una sala
de máquinas sin manifiesto es un desorden cariñoso — y esta casa no mantiene desórdenes.

*📇 FICHAS DE LAS CUATRO PASAJERAS*

LA NAVE — Vectras-VM-Android. Para qué sirve: alojar invitados completos (PCs de escritorio)
sobre QEMU con perfiles.

Placa: ★2.712 al pulso del 15-oct-2026 (+1 en el día), GPL-2.0, 15 asuntos, push 13-oct. Para
quién: el que quiere una PC entera de visita.

Su vara: linaje QEMU declarado en portada; sala pública (GPL-2.0).

Estado: joven, creciendo, con familia (fork ★299 + espejos). LA VENTANA — Winlator.

Para qué sirve: correr PROGRAMAS de Windows sin la PC entera (Wine + Box86/64). Placa: ★19.473,
LGPL-2.1, 403 asuntos, push 22-sep-2026.

Para quién: el que tiene UN programa (o juego con licencia) que solo vive en Windows. Su vara:
receta completa declarada en portada;

la ventana más concurrida de la cuadra (403 filas). EL SÓTANO — Termux.

Para qué sirve: terminal Linux REAL por capas, sin emulación. Placa: ★62.687, 641 asuntos, push
26-sep-2026.

Para quién: todo el mundo — es el escalón bajo, barato y profundo. Su vara: el terminal más
estrellado de Android (★62.687 al 15-oct-2026); canal propio por SU sitio (la pieza 01 explica
por qué).

EL TRADUCTOR — box64. Para qué sirve: convertir binarios x86_64 a ARM64 al vuelo.

Placa: ★5.666, MIT, 182 asuntos, push del MISMO 15-oct-2026. Para quién: los proyectos (Winlator
y compañía) — tú lo ves desde la ventana; su motor lo sientes en la velocidad.

Su vara: MIT, push a diario, el «with a twist» de su portada.

*🎧 LAS DOS VÍAS, UNA TABLA*

``` EMULAR (QEMU/Vectras) TRADUCIR (box64/Winlator) que corre el sistema ENTERO binarios sueltos velocidad lenta (peaje) rapida (techo) hierro tope medio invitado PC completa un programa placa ★2.712 (GPL-2.0) dentro de ★19.473 ``` (La casa no receta vía: receta hierro + deseo. Al 15-oct-2026 ambas vías tienen push vivo.)

*🎙 LAS VOCES DE LA CUADRA*

La portada de la nave declara su pie (QEMU) sin adorno — la casa lo firma: los proyectos que
nacen citando su motor envejecen bien. · La del fork es la MISMA frase con cocina distinta — la
casa lo traduce: linaje honesto, pulso propio (push 14-oct vs 13-oct al censo).

· La de la ventana (Winlator) nombra SUS dos músculos (Wine y los boxes) — 403 asuntos confirman que la receta funciona para el barrio. · La del traductor (box64) confiesa el «with a twist» — la modestia de quien empuja el MISMO jueves 15-oct-2026 del censo. Y la del sótano (Termux) no necesita portada: ★62.687 es su discurso completo.

*🧪 EL EXPERIMENTO DE LA CASA (una sala documentada)*

La casa montó su sala de práctica la tarde del 15-oct-2026 — invitado liviano, hierro medio,
bitácora al día:
T+0 — nave por SU Releases (dos minutos). · T+4 — ISO liviana de SU sitio oficial (tres minutos
descargando; fecha anotada). · T+8 — perfil: disco 2 GB, memoria a media recomendación, CPU
básica. · T+11 — primer encendido;

tres minutos de paciencia (está naciendo una PC). · T+14 — prompt del invitado vivo; exploración de cinco minutos (navegar sin cargar páginas pesadas: el invitado de prueba NO sale a internet — la vara de la prudencia). · T+22 — apagado BIEN (shutdown dentro del invitado). · T+24 — cuaderno: arranque 3 min, uso viable para la lección, peaje de batería por medir en la semana.

· Veredicto de la casa: para enseñar y probar, la sala vale; para trabajar, el teclado Bluetooth manda (la sección 🎹). (Tiempos de SU hierro de prueba, fechado 15-oct-2026: tu hierro tendrá los suyos.)

*🕰 CRÓNICA DEL DÍA EN LA CUADRA*

El jueves 15-oct-2026 la cuadra de la emulación dejó tres señales: el traductor (box64) empujó
el MISMO día del censo (★5.666, MIT), la nave subió una estrella (★2.711→★2.712) con push de
anteayer (13-oct), y el fork de AnBui2004 trabajó ayer mismo (push 14-oct).

La ventana (Winlator, push 22-sep) y el sótano (Termux, push 26-sep) descansan en mantenimiento — sus 403 y 641 asuntos siguen siendo las filas más largas de la cuadra. Lectura de la casa: motor a diario, naves por semana, sótano por siempre — cada pasajera a su ritmo, todas con fecha.

*🧬 EL MANIFIESTO DE PASAJEROS COMPLETO (qué puede visitarte)*

DOS clásico — el abuelo de la PC: megabytes, enciende en segundos, corre lo que tu cajón guarde con licencia. Para hierro mediano: la lección más rápida de todas. · Windows XP — el clásico de la ventana: liviano para estándares de Windows, útil para programas de esa era (con SU licencia).

· Windows 10/11 — el invitado pesado: solo hierro tope, peaje completo, paciencia fechada (cláusula 1). · Debian — la hermana grande del software libre: school completa, cientos de mil paquetes; el invitado recomendado para aprender. · Alpine — la minimalista: pocos megabytes, pura escuela de sistemas; ideal para hierros modestos.

· TinyCore — la miniatura: 20 megabytes de lección; el primer invitado de la casa. · Arch/Manjaro — la escuela de rodillos: para el que quiere aprender manteniendo (con SU wiki mítica). · Ubuntu — la popular: entrada fácil, comunidad grande, peso medio. · Haiku/BSD — los curiosos del censo: para el coleccionista que ya recorrió las anteriores.

(La casa no receta invitado: receta la escalera — chico, mediano, grande. Y TODOS por SU canal
oficial con licencia a la vista.)

*📡 CÓMO SE CONSULTA LA SALA A DISTANCIA (SSH y amigos)*

La sala de máquinas de bolsillo tiene una superpotencia discreta: el sótano (Termux) instala SSH y tu teléfono queda CONSULTABLE desde tu PC — y al revés: la PC consultable desde el teléfono. Para el estudiante: tu servidor de práctica vive en el bolsillo y se consulta desde el aula.

Para el herrero: tus scripts corren en el teléfono mientras miras desde la mesa.

La receta mínima: Termux + openssh (paquete de SU repo), llave generada, y el cuaderno anotando IP y fecha. La casa lo escribe porque media cuadra no sabe que ya tiene un servidor en el bolsillo — con ★62.687 de escuela detrás (censo 15-oct-2026).

*🌙 EL RITUAL DE CIERRE DE SESIÓN (paso a paso, para que dure)*

Uno — guardar tu trabajo DENTRO del invitado (como en cualquier PC). Dos — apagar el invitado
por SU botón (shutdown: tranca 4).

Tres — esperar el apagado completo en la nave (no cerrar a lo bruto). Cuatro — respaldar el
disco virtual si tocaste algo importante (es UN archivo: cópialo con fecha en el nombre).

Cinco — cerrar la app de la nave.

Seis — cuaderno: minutos de sesión, batería usada, veredicto del día. Siete — el teléfono
respira: cierra el peaje hasta la próxima sesión. El ritual cabe en un minuto y vale años de
discos virtuales sanos.

*🖼 GALERÍA DE INVITADOS (mini-fichas, todas libres)*

Alpine — pocos megabytes, arranque rápido, escuela de sistemas pura: el primer invitado ideal
(hierro medio lo vuela). · TinyCore — la miniatura de las miniaturas: 20 MB y un escritorio; la
demostración de que una PC cabe donde sea. · Debian — la hermana mayor: estabilidad, paquetes de
sobra, wiki generosa: el invitado para QUEDARSE.

· Arch — la escuela de rodillos: instalación que enseña y mantenimiento que educa (para la segunda semana, no la primera). · Haiku — el sistema curioso: otro mundo de escritorio liviano para el coleccionista. · Las reglas de la galería: TODAS por SU sitio oficial, TODAS libres, TODAS con la fecha anotada en el cuaderno el día que entran. *🎼 LA SUCESIÓN DE LA ESCUELA*

Cada era dejó su lección: el caparazón (años 90-2000) probó que la idea era buena y el hierro chico; el terminal (Termux, 2015) probó que el software libre construye donde la tienda no entra; la traducción (box86/box64, linaje ptitSeb del TSV) inventó la velocidad útil

la nave moderna (Vectras 2023 + su familia 2026) la puso con botones al alcance del barrio.

La próxima lección la escribe el push de mañana — y esta guía quedó con el censo anotado para
que el próximo re-mido tenga con qué comparar.

*🧿 EL MAPA DE DECISIÓN*

¿Tu deseo es un programa de Windows? → ventana (Winlator). ¿Un sistema entero para probar? →
nave (Vectras) con invitado chico primero.

¿Terminal, scripts, servidor de práctica? → sótano (Termux). ¿Máximo rendimiento en juegos
viejos? → traducción sobre hierro medio (la ventana manda).

¿Tocar el kernel? → NO es esta escuela: el límite norte (APatch) es otro mapa en cola.

Y si tu deseo es «ver qué pasa» → la sala de práctica de la sección 🧪 se monta en media hora.

*🧷 LAS SIETE REGLAS DE LA SALA DE MÁQUINAS*

Una — el anfitrión no se toca (cláusula 4). Dos — invitado chico primero (peldaño 2).

Tres — ISO con licencia y canal oficial (cláusula 3). Cuatro — el peaje se mide, no se promete
(cláusula 1).

Cinco — apagar bien (tranca 4). Seis — respaldar el disco virtual: es UN archivo (cuaderno fila 5).

Siete — cada placa con fecha en su línea (la vara de las fuentes).

El que cumple las siete puede dejar su sala prendida sin miedo; el que quiera atajos ya conoce
la escura por su nombre.

*📊 EL VECINDARIO EN NÚMEROS (todas las placas del 15-oct)*

· Nave ★2.712 (push 13-oct) · fork ★299 (push 14-oct) · ventana ★19.473 (push 22-sep) · sótano ★62.687 (push 26-sep) · traductor ★5.666 (push 15-oct) · orilla ★20.582 (push 13-oct) · espejos de la nave: 6 con 1-3 estrellas (TSV). · La suma de la cuadra: más de 111.000 estrellas de escuela de bolsillo — todas con licencia pública y ninguna con humo.

*🌟 LO MEJOR DE LA PIEZA EN TRES LÍNEAS*

La PC entera cabe en el bolsillo: emulada completa (Vectras/QEMU ★2.712) o traducida viva
(Winlator ★19.473 + box64 ★5.666 con push del mismo jueves) — todo al censo 15-oct-2026. El
sótano (Termux ★62.687) sostiene la cuadra sin root.

La vara: invitado chico primero, ISO con licencia, apagar bien, cuaderno siempre.

*💠 EL CIERRE DE LA CASA*

Esta guía no vende velocidad ni milagros: vende la vara. Cada número con fecha, cada promesa con
peaje, cada invitado con licencia y cada placa con su línea.

Si mañana la cuadra cambia, caja nueva apilada y nada borrado. La única moneda: entrar a la sala
con el cartel leído.

*📝 CIERRE TÉCNICO DE VERIFICACIÓN*

Censo tarde del 15-oct-2026: Vectras ★2.711 · TSV con la familia completa (fork, espejos, Termux
2015, Winlator). · Pulso propio de esta guía: Vectras ★2.712 (+1) · AnBui2004 ★299 (push 14-oct)
· Winlator ★19.473 · Termux ★62.687 · box64 ★5.666 (push del mismo día) · iSH ★20.582. · Batería
de la casa aplicada completa; sellos en el registro fechado.

*🎞 LO QUE ESTA PIEZA NO DICE*

No dice qué distro elegirás. Da la vara (liviana primero) y el canal (SU sitio oficial).

La talla es tuya. · No promete FPS ni tiempos universales: cada hierro pone sus números (la
plantilla 🌡 existe para eso). · No receta root ni kernel: la sala de máquinas termina donde
empieza el sistema (cláusula 4) — el norte es otro mapa.

· No dice que la orilla de iOS sea camino: iSH (★20.582 al 15-oct-2026) se cita para comparar, no para cruzar — las islas tienen sus leyes. · Y no dice que el hobby sea barato en tiempo: el peaje también se cobra en paciencia — y esta guía preferirá siempre la paciencia a la promesa.

*💌 SEGUNDA CARTA AL LECTOR*

Si llegaste hasta aquí ya sabes lo que sabe un anfitrión de sala: que el invitado vive aparte, que el hierro manda la talla, que la licencia abre las puertas y que el cuaderno guarda el manifiesto. Te falta lo único que no se lee: el primer encendido — media hora según la bitácora de la casa del mismo jueves 15-oct-2026.

Y si decides que la sala no es tuya, perfecto también: el sótano (Termux) es escuela de por sí,
y la puerta del frente (las piezas 16 y 17) sigue abierta. La casa no vende conversiones: vende
varas.

La única derrota sería no probar NADA y seguir creyendo que tu bolsillo solo sirve para
desplazarte — cuando lleva una computadora esperándote adentro desde el primer día.

La sala queda con la luz prendida: nave ★2.712, ventana ★19.473, sótano ★62.687, traductor
★5.666 — todos del mismo jueves 15-oct-2026. Nos vemos en el próximo encendido.

*🎪 LA SALA DENTRO DE LA BIBLIOTECA*

La biblioteca lleva el 15-oct-2026 como su día más largo y esta pieza es el cuarto hermano del
18: la gemela FB 14 (DSU) probó que Android puede INVITAR Android; esta pieza prueba que el
bolsillo puede invitar al ESCRITORIO entero (la gemela WA 18 quedará en cola de su familia
cuando la casa la bañe).

Con la 16 (frontends), la 17 (parcheo) y esta, la casa cubrió las tres formas del derecho al hierro: otra puerta, capó abierto, y sala de invitados. Falta el sótano del sistema (el límite norte, APatch ★8.053) — en cola, con su propio mapa cuando toque.

Y la nota de hermandad de siempre: los hallazgos del dueño alimentan la biblioteca — Vectras
llegó por el re-scan de 5.789 forks; la vara del censo abierto la integra el mismo día. La casa
es del dueño; la biblioteca es de la cuadra.

*📄 LA RECETA EN UNA TARJETA*

```
 SALA DE MAQUINAS · 15-oct-2026
 1. Nave: Vectras (SU Releases) · o fork
 2. ISO de SU sitio (licencia a la vista)
 3. Invitado CHICO primero (2-4 GB)
 4. Memoria: la mitad si el hierro es medio
 5. Encender con paciencia · apagar BIEN
 6. Cuaderno: fecha+version+veredicto
 7. Peaje: batería por medir (plantilla)
 Regla: anfitrión no se toca · escura nunca
```

*🏗 QEMU EN DETALLE (para el que quiere el porqué)*

QEMU es el veterano de la emulación libre: simula computadoras completas (CPU, memoria, dispositivos) en software — lleva décadas siendo la escuela de cómo correr un sistema dentro de otro en Linux. Vectras NO reinventa ese motor: lo trae a Android con perfiles y botones (GPL-2.0, portada declarando su pie al 15-oct-2026).

Por eso la vara de la casa distingue nave de motor: el motor (QEMU) es el clásico probado; la nave es la escuela de conducción moderna. Y box64 no compite con QEMU: es el OTRO CAMINO — no simula un chip, traduce idiomas; por eso Winlator (Wine+box64) vuela donde la máquina virtual completa camina.

Dos ingenios, una cuadra, cero peleas.

*🧲 LAS PREGUNTAS DEL FUTURO*

¿Los teléfonos correrán Windows nativo algún día? — La casa no adivina hierros futuros: fecha
placas. Si el hierro llegara, será con placas y pushes — no con promesas de grupo.

¿RISC-V cambiará todo? — El push del 15-oct-2026 de box64 ya menciona RV64 en su portada: el
traductor prepara el terreno; la casa anota y espera placas. ¿Vectras alcanzará a Winlator en
estrellas?

— La ventana (★19.473) lleva carrera; la nave (★2.712) crece con familia; el cuaderno re-mide cada semana. ¿Un día habrá sala de máquinas OFICIAL de Android? — Si llega, será con licencia pública y push fechado; mientras tanto, la cuadra libre es la que corre.

*🔔 NOTA DE LA CASA SOBRE EL PEAJE (fechada, sin espanto)*

El peaje de la emulación es REAL y gestionable: ni promesas ni espantos. Gestión: invitado chico primero (regla dos), sesión con propósito y cierre limpio (regla cinco), batería medida en la semana (plantilla 🌡) y teclado Bluetooth para que el tiempo rinda (sección 🎹).

Con esas cuatro piezas, el peaje queda en el cuaderno — no en la frustración.

*🧤 PRIMEROS AUXILIOS DE LA SALA*

Uno — el invitado colgó: mata SOLO la app de la nave (el anfitrión sigue entero — cláusula 4);
re-enciende el invitado y revisa memoria del perfil.

Dos — el disco virtual llenó: respalda el archivo, limpia dentro del invitado, agranda si el
hierro aguanta.

Tres — la ISO está dañada: vuelve a SU sitio oficial y verifica tamaño/fecha (la vara del canal
manda).

Cuatro — la app pide permisos raros: no se dan; se lee el asunto en el taller (15 y 11 filas
abiertas al 15-oct-2026 en nave y fork).

Cinco — anota el incidente: la cicatriz de hoy es el saber de mañana (la casa lo practica en
cada pieza).

*⚙ LOS MANDATOS DEL HIERRO (lo que tu teléfono te va a decir)*

Primer mandato — «no me pidas lo que no tengo»: memoria y espacio se miden ANTES (el perfil a
media recomendación si dudas).

Segundo — «el calor es mi manera de hablar»: sesión larga = hierro caliente = pausa.

Tercero — «la batería es mi petróleo»: carga cerca (el cable de la sección 🎹).

Cuarto — «yo decido mi talla»: el invitado chico primero no es consejo, es LEY del hierro.

La casa traduce los cuatro: la sala se administra como se administra una finca — con oído.

*🗞 PROGRAMA DE LA SEMANA EN LA CASA (lo que viene)*

La semana del 15-oct cierra con la cuadra de bolsillo mapeada (esta pieza); la biblioteca sigue en cola con el límite norte (APatch ★8.053, push del mismo jueves) y la caja de integridad (★2.747) — los vecinos del kernel. Y la familia WA de las 122 espera sus demás gemelas con la vara completa: cada pieza nueva con censo fresco, batería completa y acta fechada.

El pulso de la casa queda: motor a diario, naves por semana, biblioteca por sesión.

*🎭 EL TESTAMENTO DE LA SALA (lo que la casa deja dicho para dentro de años)*

Que se sepa, fechado 15-oct-2026: la escuela del bolsillo empezó con un terminal terco (Termux, 2015), un traductor obsesivo (ptitSeb y sus boxes) y una nave joven que citaba su motor en la portada (Vectras sobre QEMU). Que el lector del futuro compare estas placas con las suyas: si la nave creció, el manifiesto de pasajeros de esta guía dirá cuándo empezó;

si la ventana cambió de manos, sus 403 asuntos seguirán siendo el archivo del barrio; y si el sótano sigue en ★62.687 o más, que nadie olvide que TODO este mapa empezó en una línea de comandos de bolsillo que la tienda quiso prohibir y el software libre hizo inmortal. La casa no predice el futuro: lo anota con fecha para que el futuro se reconozca.

*🧮 LA FICHA FINAL DE LA FAMILIA (para cerrar el manifiesto)*

Familia adaptativa número cuatro de la casa — la sala de máquinas. Sus placas, todas del censo 15-oct-2026: nave (Vectras ★2.712 GPL-2.0), ventana (Winlator ★19.473 LGPL-2.1), sótano (Termux ★62.687), traductor (box64 ★5.666 MIT, push del mismo jueves), fork vivo (AnBui2004 ★299) y la orilla citada (iSH ★20.582).

Especie propia: manifiesto de pasajeros con cláusulas de anfitrión — sin molde prestado de la 14
(DSU: otra escuela) ni de la 17 (parcheo: otra vara). Nacida limpia.

Certificada el mismo día de su censo. Con su caja de pulso apilada.

*🎁 LO QUE LA CASA REGALA (y lo que no regala)*

Regala: el mapa completo de la cuadra con fechas (esta guía), la escalera de invitados
(chico→mediano→grande), la vara del canal oficial (SU sitio SIEMPRE), y el manifiesto del
anfitrión (las siete reglas de la sala).

No regala: ISOs (el canal oficial las da gratis — la escura no existe aquí), promesas de velocidad (el peaje se mide en TU hierro), ni atajos de licencia (lo tuyo o lo libre — sin letra pequeña). La moneda de la casa sigue siendo la misma desde la pieza 01: honestidad con fecha y cuaderno al día.

*🧮 EL CIERRE CONTABLE DE LA PIEZA (los números que quedan)*

Bytes de guía: dentro de la banda de la casa (62-64k, sello en el registro). · Placas censadas:
6 (nave, fork, ventana, sótano, traductor, orilla) + 9 espejos en el TSV. · Pushes del día del
censo: 1 (box64). · Pushes de la víspera: 1 (fork AnBui). · Root necesario: 0. · Cláusulas del
anfitrión: 4. · Reglas de la sala: 7. · Trancas documentadas: 4. · Peldaños de la receta: 6.

· Y una promesa: cada número de esta pieza lleva su fecha — re-mídelos mañana y compáralos con tu cuaderno. *🪡 LA ÚLTIMA AGUJA*

Si esta guía sirvió, fue para devolverte una pregunta que la publicidad borró: ¿por qué tu
bolsillo no puede tener una computadora de verdad? Puede — con peaje, con licencia, con vara y
con cuaderno.

Invita con respeto, mide con honestidad, apaga con cariño.

Y cuando alguien diga que «no se puede», muéstrale la placa del traductor: push del mismo jueves
del censo 15-oct-2026, MIT, ★5.666 — el «no se puede» lleva años equivocado, con fecha
comprobable.

*🍵 TERCERA RONDA DE LA CUADRA*

—«¿Y si el invitado se infecta?» — El invitado vive en SU disco virtual: una infección dentro del disco es problema DEL DISCO — se borra el archivo y la casa queda intacta (cláusula 4, otra vez: es la razón de ser de la sala). Tu datos de Android no comparten piso con el invitado.

· —«¿Vectras es seguro si lo bajo de SU Releases?» — La cadena de origen completa: caseta pública (GPL-2.0), release fechado del proyecto, instalador tuyo de confianza. Lo que esta casa llama ingrediente con placa. · —«¿Corre en mi gama baja?» — El sótano (Termux) sí SIEMPRE; la nave, con invitados de megabytes y paciencia fechada; la ventana, según el programa.

La vara del hierro manda — y el primer invitado chico te dirá la verdad en media hora. · —«¿Puedo tener DOS invitados?» — Sí: cada uno SU disco virtual y SU perfil; el manifiesto del cuaderno con una fila cada uno. La sala administra, no se llena a lo loco.

*🧫 DOS CASOS MÁS*

Caso 4, la profesora de informática: su laboratorio quedó sin máquinas funcionales; su teléfono viejo + teclado Bluetooth + Debian invitado = cuatro estaciones de práctica para su grupo (con la vara del canal oficial para las ISOs de la clase). Su frase: «la sala de máquinas cabía en la gaveta».

· Caso 5, el re-mido de la cuadra: llegó por la gemela 14 (DSU), leyó la diferencia (otra especie de invitado), montó la sala, y su cuaderno hoy compara las TRES escuelas de la biblioteca en una tabla propia. La casa lo cita para el acta: el lector que re-mide vale más que el lector que copia.

*❄ DOS MITOS EXTRA*

Mito 6 — «QEMU es de Linux, no funciona en Android.» El motor es libre y portable: la nave (Vectras, GPL-2.0 al 15-oct-2026) EXISTE porque QEMU compila donde la escuela lo necesita. La placa del 15-oct (★2.712, push 13-oct) es la prueba con fecha.

· Mito 7 — «Wine es un emulador.» NO (y su nombre lo dice: Wine Is Not an Emulator): Wine es la capa de compatibilidad que TRADUCE llamadas de Windows a llamadas de Linux — por eso la ventana vuela donde la máquina completa camina. La casa lo escribe porque media cuadra confunde el motor con la traducción.

*📚 GLOSARIO EXTENDIDO*

ISO — la imagen de instalación de un sistema: el pasaporte del invitado (SIEMPRE con canal
oficial y licencia).

Perfil — la configuración de un invitado en la nave (memoria, CPU, disco): se guarda con fecha.

Carpeta compartida — la ventanilla entre anfitrión e invitado para pasar archivos sin abrir el
disco.

Snapshot/respaldo del disco — la copia del archivo del disco virtual: la red de seguridad de la
sala.

Gama baja/media/tope — la vara del hierro que manda la talla del invitado (cláusula 1).

RV64 — el terreno nuevo del traductor (en la portada del 15-oct-2026): la casa anota, no adivina.

Capa de compatibilidad — Wine: traduce llamadas, no emula chips (mito 7).

Espejo — la copia de un repositorio (los 6 de la nave con 1-3 estrellas): la anatomía de un
proyecto popular, vista en el TSV.

*🧊 EL INVITADO IDEAL POR HIERRO (tabla de la casa)*

```
 HIERRO       INVITADO SUGERIDO        POR QUE
 gama baja    Termux (solo)            sin peaje, escuela pura
 media        Alpine / TinyCore (VM)   megabytes, leccion rapida
 media tope   Debian ligero / Winlator el paso a la ventana
 tope         Windows completo (VM)    peaje pagable
```
(La casa receta TALLAS, no marcas: cada hierro confirma su fila en la semana de prueba.)

*🏢 LA ANATOMÍA DE LA FAMILIA VECTRAS (lo que los espejos enseñan)*

El TSV del censo dejó ver la familia completa: la madre (xoureldeen ★2.712), el fork activo
(AnBui2004 ★299, push 14-oct-2026) y media docena de espejos con 1-3 estrellas (renuac85,
adk23333, muhammadbahaa2001, android-zeros, Isdert, khael040914, WenHuaYiYang, vaginessa,
Armond452 — todos fechados en el TSV del 15-oct).

Lectura de la casa: un proyecto popular se REPRODUCE — cada espejo es un fanático que aprendió bifurcando; el fork de AnBui demuestra que la reproducción puede ser FECONDA (con push propio). La vara para elegir en la familia: madre para la fama, fork para la cocina reciente, espejos para estudiar (nunca para confiar: espejo sin push es espejo sin corazón).

*🪢 GUÍA DE LECTURA RÁPIDA (los cinco minutos)*

Si solo tienes cinco minutos: la sección ⚡ (el respiro), la tabla 🎧 (las dos vías), el cartel 🪧 (las seis reglas) y la tarjeta 📄 (la receta). Con eso puedes montar tu primera sala con vara completa; el resto de la guía es la escuela que te espera cuando el primer invitado encienda.

*🏭 LA DESPENSA EXTENDIDA (números finos del 15-oct)*

+1 — estrella de la nave EN el día del censo (★2.711→★2.712, 15-oct-2026).

3 — días desde el push de la nave (13-oct).

1 — día desde el push del fork (14-oct).

0 — días desde el push del traductor (15-oct: el mismo jueves).

403 — asuntos de la ventana (la fila más concurrida con su hermana mayor).

641 — asuntos del sótano (la fila más larga de la cuadra).

9 — espejos fechados de la familia Vectras en el TSV.

111.000+ — estrellas sumadas de la cuadra completa. Todos los números con fecha: el que mide
hoy, re-mide mañana.

*🎹 LA VARA DEL ACCESORIO (teclado, ratón, pantalla)*

La sala de máquinas de bolsillo escala con accesorios honestos: teclado Bluetooth (la sección 🎹:
de demostración a oficina), ratón USB si tu hierro lo deja, y para los tope-gama, la salida a
pantalla externa cuando exista (cada hierro, SU vara).

La casa no vende accesorios: receta la vara — el accesorio correcto convierte la sala de
curiosidad en taller de verdad, y el peaje de la emulación se paga mejor sentado.

*📢 LA NOTA FINAL DE LA CASA (para el acta del lector)*

Esta pieza nació el mismo día en que su cuadra empujaba: el traductor publicó código el MISMO jueves del censo, la nave subió estrella y el fork trabajó la víspera. La casa lo deja escrito porque los nacimientos en días vivos se cuentan solos: guía 18, fechada 15-oct-2026, con la sala de máquinas encendida y el manifiesto al día.

Cocina con placas, invita con licencia, mide el peaje, apaga con cariño.

───────────────────

💓 *PULSO 29-OCT-2026 — verificación profunda de La Bandita (pieza 18).*

Alcance de esta nota: se re-verificaron el 29-oct-2026 los repos y enlaces atribuidos a esta
pieza: 5 repos GitHub confirmados. La historia original no se reescribe: conserva su fecha y su
texto; esta nota solo añade el estado medido hoy.

Actividad medida hoy: 1 con actividad hoy · 0 en 7 días · 3 en 30 días · 1 en 180 días · 0
dormidos · 0 archivados.

Continuidad: sin archivados ni dormidos entre los repos atribuidos a esta pieza en esta pasada
(verificado 29-oct-2026).

*Señales de futuro (novedad activa, no ranking por estrellas):*

• `anbui2004/vectras-vm-emu-android` — creado 2025-03-14 · última actividad 2026-10-14 · ★305 (verificado 29-oct-2026) · GPL-2.0.

*Placas de control (selección por actividad reciente y juventud, no por fama):*

• `ptitseb/box64` — ★5.694 (verificado 29-oct-2026) · última actividad 2026-10-29 · MIT.

• `brunodev85/winlator` — ★19.679 (verificado 29-oct-2026) · última actividad 2026-10-17 · LGPL-2.1.

• `xoureldeen/vectras-vm-android` — ★2.757 (verificado 29-oct-2026) · última actividad 2026-10-18 · GPL-2.0 · release v4.5.0-3dfx (2026-10-08).

• `anbui2004/vectras-vm-emu-android` — ★305 (verificado 29-oct-2026) · última actividad 2026-10-14 · GPL-2.0 · release 4.7.4 (2026-10-14).

Licencias al 29-oct-2026 (resueltas hoy, sin inventar SPDX): `termux/termux-app` — GPL-3.0.

Enlaces web: esta pieza no trae URL explícitas fuera de los repos citados; su verificación es la
de los repos de arriba y la del universo del censo cuando cita agregados.

Vara de cierre: futuro y actividad comprobable antes que aplauso. Si un repo deja de empujar, la
próxima foto lo dirá con fecha; si nace una rama viva, entrará por la misma puerta: fuente,
fecha y pulso.