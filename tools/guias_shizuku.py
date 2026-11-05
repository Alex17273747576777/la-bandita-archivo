#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""guias_shizuku.py · escribe a mano la guía de las fichas del racimo de Shizuku.

Las fichas se generan solas; la guía no. Este archivo es el sitio donde se escribe:
cada entrada reemplaza el bloque GUIA:INICIO…GUIA:FIN de su ficha y **no** toca lo
medido. Se puede volver a ejecutar las veces que haga falta.

Solo escribe en las fichas que ya existen y cuyo racimo es `shizuku-y-herederos`.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CATALOGO = RAIZ / "catalogo"
MEDIDO = CATALOGO / "medido.json"
INICIO, FIN = "<!-- GUIA:INICIO -->", "<!-- GUIA:FIN -->"

GUIA = {}

GUIA["RikkaApps/Shizuku"] = """
### Para qué sirve

Es el programa que le da a otras aplicaciones los permisos del sistema sin que el teléfono esté
rooteado. No hace nada visible por sí solo: enciende un servicio y las apps que lo piden (Hail, Canta,
ShizukuTools, Inure…) pueden desinstalar, congelar o cambiar ajustes que normalmente exigirían root.

### Cómo se enciende

Con **root**, el servicio arranca solo al reiniciar. Sin root, hay que encenderlo cada vez que el
teléfono se apaga, y el camino es el de la depuración inalámbrica:

1. Ajustes → Información del teléfono → toca siete veces «Número de compilación» para activar las
   opciones de desarrollador.
2. Ajustes → Sistema → Opciones de desarrollador → activa **Depuración inalámbrica** (Android 11 o
   superior) y conecta el teléfono a la misma red que el equipo desde el que vas a emparejar.
3. Abre Shizuku, pulsa «Empezar», elige «Depuración inalámbrica» y sigue el emparejamiento con el
   código de seis dígitos que muestra el sistema.
4. En Android 10 o anterior hace falta un cable y `adb` en un ordenador: no hay depuración
   inalámbrica que empareje sola.

### Lo que conviene saber antes

El último empujón del repositorio es del 18 de junio de 2025 —**505 días** antes de esta ficha— y la
última entrega, la v13.6.0, del 25 de mayo de 2025: el proyecto no está archivado, y precisamente por
eso el catálogo lo marca «parado» y no «vivo». No está roto; está quieto, que en un catálogo es un dato
distinto. Los forks que salieron de aquí —Stellar, ShizukuPlus,
Shizuku-Next— publican versiones más recientes y son la razón de que el ecosistema siga vivo aunque
el original esté quieto.

### Cuándo no vale la pena

Si el teléfono es de trabajo, si tiene una cuenta de empresa o si no puedes activar la depuración,
Shizuku no arranca y su función estrella —desinstalar sin root— se queda en nada. En ese caso la
alternativa es el camino de ADB desde un ordenador, que hace lo mismo de una vez y no hay que
mantenerlo encendido.
"""

GUIA["RikkaApps/Sui"] = """
### Para qué sirve

Es la otra forma de darle permisos de sistema a las apps de Shizuku, y la más cómoda **si ya tienes
root**: en vez de un servicio que hay que encender, se instala como módulo de Magisk y el sistema lo
levanta al arrancar. Para quien ya rooteó el teléfono, es un módulo y un reinicio.

### Cómo se instala

1. Descarga el zip desde la última entrega o instálalo desde el propio gestor de módulos de Magisk.
2. Instálalo con el gestor, o desde el ordenador con `adb shell su -c magisk --install-module`.
3. Reinicia el teléfono. A partir de ahí, las apps compatibles con la API de Shizuku lo detectan
   solas, sin emparejamientos ni códigos de seis dígitos.

### Lo que conviene saber antes

La última entrega es del 19 de septiembre de 2023 y el repositorio no se mueve desde agosto de 2024.
Funciona en los teléfonos donde ya funcionaba, y en un Android nuevo puede encontrarse con cambios de
permisos que nadie ha actualizado. No está archivado, y eso no significa que esté mantenido.

### Cuándo no vale la pena

Si no tienes root, Sui no es una opción: su camino es Magisk. Y si lo tienes, Shizuku con root hace
casi lo mismo sin convertir el asunto en un módulo del sistema que hay que quitar antes de una
actualización grande.
"""

GUIA["RikkaApps/Shizuku-API"] = """
### Para qué sirve

No es una aplicación: es la documentación y la librería para quien escribe apps que quieren usar los
permisos que da Shizuku o Sui. Si lo que quieres es usar el teléfono, esto no te sirve; si lo que
quieres es programar contra él, es el punto de partida y el único sitio donde están las reglas.

### Qué hay dentro

La guía para desarrolladores —cómo se pide el permiso, cómo se llama al código con identidad de shell
o de root, qué se puede y qué no— y las dependencias que se añaden al proyecto. La licencia es MIT, la
más permisiva de la familia, y eso importa si vas a publicar algo cerrado encima.

### Lo que conviene saber antes

Las entregas etiquetadas del repositorio son viejas —la última, de 2022— porque la librería se
publica por el repositorio de artefactos y no por entregas de GitHub: la fecha de la entrega engaña y
la del empujón, mayo de 2025, es la que vale. Es el caso típico de ficha que una lista de enlaces no
puede contar.

### Cuándo no vale la pena

Si solo quieres instalar una app que use Shizuku, esto te sobra por completo: instala Shizuku y la app.
"""

GUIA["RikkaApps/Riru"] = """
### Para qué sirve

Fue el sistema para inyectar módulos de Magisk dentro de las aplicaciones y del servidor del sistema
cuando Zygisk todavía no existía. Hoy es historia: el repositorio está **archivado** y su última
entrega es de febrero de 2022.

### Qué hacer en su lugar

Los módulos que dependían de Riru se pasaron a **Zygisk**, que viene dentro de Magisk. Si una guía
vieja te manda instalar Riru, la guía es de 2021: instala Magisk con Zygisk y busca la versión del
módulo que lo soporte.

### Por qué está en el catálogo

Porque el catálogo no es una lista de recomendaciones: es un archivo con fecha. Un recurso archivado
con su fecha al lado evita que alguien lo instale creyendo que está vivo, y explica por qué se rompió
la receta de un tutorial que circula.
"""

GUIA["roro2239/Stellar"] = """
### Para qué sirve

Es una implementación alternativa de Shizuku, escrita de nuevo y publicada bajo MPL-2.0 —una licencia
distinta de la del original—. Se instala en lugar de Shizuku y las apps que esperan la API de Shizuku
la reconocen.

### Por qué importa en este racimo

Shizuku lleva desde junio de 2025 sin un empujón y su última entrega es de mayo de 2025. Stellar
publicó la suya en agosto de 2026 y el repositorio se movió en octubre. Cuando el original se queda
quieto, los herederos son lo que mantiene viva la API: eso es exactamente lo que este catálogo quiere
medir, y por eso Stellar tiene ficha propia y no una nota al pie.

### Lo que conviene saber antes

Una reimplementación no es una actualización: si la app que usas depende de un detalle de Shizuku que
Stellar no copió, fallará en silencio. Se instala uno de los dos, no los dos, y se prueba la app que
te importa antes de dar el cambio por bueno.
"""

GUIA["rushiranpise/Shizuku-Next"] = """
### Para qué sirve

Es un fork de Shizuku con el arranque reescrito: la promesa de su autor es que empareja mejor y falla
menos. Su última entrega, `v14.0.33-next`, es del **mismo 5 de noviembre de 2026** en que se escribió
esta ficha: es el recurso más reciente de todo el racimo.

### Cómo se prueba sin estropear nada

1. Instala Shizuku-Next en el mismo teléfono donde tengas Shizuku, con otro nombre de paquete: las dos
   pueden convivir.
2. Enciende el servicio de Next siguiendo su propio asistente.
3. Abre tu app de siempre —Hail, Canta, ShizuTools— y mira cuál de los dos servicios detecta.
4. Si todo va, desinstala el original; si no, ya sabes a quién culpar.

### Lo que conviene saber antes

Lleva la etiqueta `-next` en la versión, y eso se lee como lo que es: una línea de desarrollo. Un fork
que publica hoy puede dejar de publicar el mes que viene, y entonces tu servicio deja de actualizarse
sin que te enteres. Anota la fecha en la que lo instalaste.
"""

GUIA["thejaustin/ShizukuPlus"] = """
### Para qué sirve

Es un fork de Shizuku que unifica los tres caminos —root, ADB y Dhizuku— en un solo programa, con su
propia suite de funciones y ajustes para capas de fabricante como One UI. Para quien tiene un Samsung
con capa propia y había que elegir entre tres herramientas, es la opción que las junta.

### Lo que conviene saber antes

Su última entrega —`v13.6.0.r2551`, de septiembre de 2026— **lleva dentro el número de versión del
original**, y eso confunde: no es la 13.6.0 de Rikka, es la suya con el número heredado. Al comparar
versiones entre forks, se mira la fecha de la entrega y no el número, que es el error más común de
este racimo.

### Cuándo no vale la pena

Si tu teléfono no tiene una capa que estorbe y el Shizuku original te enciende sin problema, este fork
añade piezas que no vas a usar. Los forks se justifican por un problema concreto; si no lo tienes, no
hace falta.
"""

GUIA["iamr0s/Dhizuku"] = """
### Para qué sirve

Comparte los permisos de **propietario del dispositivo** (DeviceOwner) con otras aplicaciones. Es un
camino distinto al de Shizuku: no da identidad de shell, da la del dueño del teléfono, y con eso se
pueden hacer cosas que ni el shell puede —políticas, restricciones, gestión—.

### Cómo se prepara

El teléfono tiene que estar **sin cuentas** y sin configurar del todo, o hay que ejecutar el comando de
ADB que lo convierte en propietario:

```
adb shell dpm set-device-owner com.iamr0s.dhizuku/.DhizukuDeviceAdminReceiver
```

Ese comando falla si el teléfono ya tiene una cuenta de Google configurada. Es el paso que hace que
medio mundo abandone: no es difícil, es que hay que hacerlo antes de configurar el teléfono.

### Lo que conviene saber antes

El repositorio está vivo —entrega `v2.13.0` del 30 de octubre de 2026— y su licencia es GPL-3.0. Su
README no trae un párrafo de presentación; la explicación está en su web, y por eso la ficha no cita
prosa que no existe.

### Cuándo no vale la pena

En un teléfono personal ya configurado, sin ganas de borrarlo todo. Dhizuku es para un aparato que se
prepara desde cero o para quien acepta reiniciar el camino.
"""

GUIA["aistra0528/Hail"] = """
### Para qué sirve

Congela, esconde, suspende y desinstala aplicaciones **sin root**, usando Shizuku o Dhizuku como
fuente de permisos. Es la app que más gente instala justo después de Shizuku, y con razón: hace algo
visible en treinta segundos.

### Cómo se usa

1. Instala Hail y abre Shizuku (o Dhizuku) y enciéndelo.
2. En Hail, concede el permiso cuando lo pida y elige el modo de trabajo: helar (congelar), ocultar o
   desinstalar para el usuario actual.
3. Las apps heladas dejan de aparecer en el lanzador y no consumen batería; se descongelan desde la
   propia lista de Hail.
4. Antes de desinstalar algo del sistema, mira de qué depende: Hail avisa, pero no adivina.

### Lo que conviene saber antes

Entrega `v1.11.0` del 26 de agosto de 2026, GPL-3.0, repositorio con empujón de finales de octubre:
es de los vivos. Su README es corto y sin promesas raras, que en este ecosistema ya es un dato.

### Cuándo no vale la pena

Para desinstalar dos apps que no usas, el panel de aplicaciones del sistema basta. Hail se justifica
cuando congelas de forma habitual, o cuando el fabricante no te deja desactivar lo que quieres quitar.
"""

GUIA["samolego/Canta"] = """
### Para qué sirve

Desinstala aplicaciones del sistema sin root, apoyándose en Shizuku, y está pensado para el trabajo de
limpieza: elegir, confirmar y no arrepentirse. Su nombre viene de «cantar» las apps que sobran.

### Cómo se usa

1. Enciende Shizuku y abre Canta.
2. Concede el permiso y elige si quieres desinstalar para el usuario actual o para todos.
3. Ve marcando las apps que quieres fuera; Canta las agrupa y muestra para qué sirve cada una.
4. Haz una captura de la lista antes de confirmar: en este trabajo, el arrepentimiento llega tarde.

### Lo que conviene saber antes

Entrega `v4.1.0` del 29 de octubre de 2026 y licencia LGPL-3.0: es de los más actualizados del racimo.
Funciona también con root si lo tienes, pero su gracia es no necesitarlo.

### Cuándo no vale la pena

Si el teléfono es nuevo y no tiene relleno del fabricante, Canta no tiene trabajo. Si es un Xiaomi,
un Samsung o un operador con veinte apps pregrabadas, es la primera que se instala.
"""

GUIA["MuntashirAkon/AppManager"] = """
### Para qué sirve

Es el navaja suiza de las aplicaciones de Android: ver permisos, revocarlos, ver qué hace una app por
dentro, congelarla, hacer copias de seguridad, leer sus registros y ejecutar operaciones que el sistema
esconde. Funciona con root, con Shizuku o con ADB, y esa variedad es su mejor argumento y su mayor
complicación.

### Cómo se usa sin root

1. Enciende Shizuku (o conecta por ADB desde un ordenador).
2. Abre AppManager y elige el modo de funcionamiento; pedirá el permiso correspondiente.
3. Desde la lista de apps, cada una abre una ficha con pestañas: permisos, actividades, servicios,
   receptores, registros y operaciones.
4. Todo lo que cambia algo pide confirmación y avisa si es irreversible.

### Lo que conviene saber antes

Entrega `v4.1.1` y repositorio con empujón del 3 de noviembre de 2026: vivo. Su licencia aparece en
GitHub como NOASSERTION porque es la GPL-3.0 con una excepción propia; quien vaya a reutilizar código,
lee el archivo de licencia y no se fía de la etiqueta.

### Cuándo no vale la pena

Es mucha herramienta para quien solo quiere congelar una app: para eso, Hail o Canta son tres pantallas
menos. AppManager se justifica cuando de verdad quieres mirar dentro.
"""

GUIA["zacharee/InstallWithOptions"] = """
### Para qué sirve

Instala APK en el teléfono con las opciones que el instalador del sistema no te deja elegir: instalar
para otro usuario, permitir degradar versión, conceder permisos de instalación, declarar el instalador.
Usa Shizuku para tener los permisos, y su público es quien prueba versiones beta o instala APK de
fuentes distintas.

### Cómo se usa

1. Enciende Shizuku.
2. Abre el APK con InstallWithOptions en lugar de con el instalador del sistema (desde el explorador de
   archivos, «abrir con»).
3. Marca las opciones y confirma. El registro de la operación dice qué se hizo y qué falló.

### Lo que conviene saber antes

Entrega `0.9.2` del 14 de marzo de 2026, MIT, empujón de finales de octubre: se mantiene, aunque las
entregas salen más despacio que los cambios.

### Cuándo no vale la pena

Para instalar la APK normal de una app normal, el instalador del sistema hace lo mismo y no pide nada.
"""

GUIA["legendsayantan/ShizuTools"] = """
### Para qué sirve

Reúne en una sola app un montón de operaciones que normalmente exigen terminal: congelar, desinstalar,
cambiar el estado de un paquete, leer propiedades del sistema. Todo por Shizuku, sin root.

### Lo que conviene saber antes

Su última entrega etiquetada es `v1.4.6`, de octubre de 2024, y el repositorio se movió en septiembre
de 2026: hay trabajo sin etiquetar, y eso en una ficha se escribe. Para quien quiera lo último, la
opción es compilar o mirar las compilaciones de desarrollo; para quien quiera estabilidad, la entrega
vieja funciona hasta que el sistema cambie una regla.

### Cuándo no vale la pena

Si de todo lo que trae solo vas a usar «congelar», Hail hace eso con menos superficie. Las herramientas
multiuso se justifican cuando de verdad se usan cinco de sus diez botones.
"""

GUIA["kitsumed/ShizuCallRecorder"] = """
### Para qué sirve

Graba llamadas usando los permisos que da Shizuku, sin root y sin depender de la grabadora del
fabricante, que en muchos teléfonos está capada o avisa con un tono.

### Lo que conviene saber antes

Entrega `v2.0.0` del 24 de octubre de 2026 y empujón de noviembre: vivo. Y una advertencia que no es
técnica: **grabar una llamada sin avisar a la otra persona es ilegal en muchos países**, y en la
República Dominicana la Ley 53-07 sobre delitos de alta tecnología castiga el acceso y la interceptación
no autorizada de comunicaciones. Que el programa funcione no cambia la ley; esta ficha no es asesoría
legal y no la va a dar.

### Cuándo no vale la pena

Si el teléfono ya trae grabadora integrada y funciona, esto añade una app más y un servicio que
mantener encendido.
"""

GUIA["Hamza417/Inure"] = """
### Para qué sirve

Un gestor de aplicaciones con interfaz cuidada: congelar, desinstalar, ver permisos, limpiar, todo en
un solo sitio, con root o con Shizuku.

### Lo que conviene saber antes

Entrega `build107.3.1` del 2 de noviembre de 2026 y empujón de noviembre: es de los más activos del
racimo. Su licencia es GPL-3.0. El nombre de la entrega dice `build`, no una versión con puntos, y eso
hace difícil comparar: en este racimo, la fecha manda sobre el número.

### Cuándo no vale la pena

Frente a AppManager, que lleva quince años de funciones, Inure gana en diseño y pierde en profundidad.
Si vas a mirar dentro del sistema, AppManager; si vas a ordenar el cajón de apps, Inure.
"""

GUIA["xjunz/AutoTask"] = """
### Para qué sirve

Automatiza toques y flujos en pantalla apoyándose en accesibilidad o en Shizuku: rellenar formularios,
repetir una secuencia, saltarse pasos que se hacen igual todos los días.

### Lo que conviene saber antes

Su último empujón es del 26 de abril de 2024 y no publica entregas etiquetadas: para los criterios de
este catálogo está **parado**, aunque no esté archivado. Las automatizaciones que dependen de la
estructura de una pantalla concreta envejecen rápido, y dos años son muchos.

### Cuándo no vale la pena

La automatización por accesibilidad lee lo que hay en la pantalla, incluidas contraseñas y mensajes. Si
lo que quieres automatizar es delicado, la alternativa es un ADB puntual desde un ordenador, que no
deja un servicio escuchando todo el día.
"""

GUIA["iamr0s/InstallerX"] = """
### Para qué sirve

Fue el instalador de APK con opciones avanzadas de su generación: diálogo, notificación, instalar en
todos los usuarios, permitir pruebas y degradaciones. Está **archivado** desde agosto de 2023 y su
última entrega es `v1.7` de junio de 2023.

### Qué hacer en su lugar

Su heredero es `wxxsfxyzm/InstallerX-Revived`, con ficha propia en este mismo racimo, que sigue
publicando: la última, del 30 de septiembre de 2026. Cuando un proyecto se archiva, el catálogo no lo
borra: lo deja con fecha y una flecha al que sigue.

### Por qué su README se cita en chino

Porque está en chino: su autor lo escribió así y no hay versión en español. Traducirlo aquí sería
inventar una fuente; se deja constancia y se resume lo que el propio texto dice del programa.
"""

GUIA["wxxsfxyzm/InstallerX-Revived"] = """
### Para qué sirve

Continúa InstallerX: instala APK con las opciones que el instalador del sistema esconde —elegir usuario,
permitir degradar, declarar instalador— y añade una interfaz propia para hacerlo. Usa Shizuku o root
para tener los permisos.

### Cómo se usa

1. Enciende Shizuku o ten root.
2. Instala el paquete de InstallerX-Revived y actívalo como manejador de instalaciones en los ajustes
   del sistema, o ábrelo directamente con el APK.
3. Al instalar, el diálogo deja elegir usuario, banderas y confirmación; el resultado queda en el
   registro.

### Lo que conviene saber antes

Entrega `26.09` del 30 de septiembre de 2026, GPL-3.0, empujón de noviembre: vivo y con más estrellas
—★7.327— que el original archivado, lo que en este caso dice bastante: el heredero hizo mejor trabajo
que el padre en menos tiempo.

### Cuándo no vale la pena

Si nunca has necesitado instalar para otro usuario ni degradar una versión, el instalador del sistema
va sobrado.
"""

GUIA["pass-with-high-score/universal-installer"] = """
### Para qué sirve

Instalador de paquetes con soporte de APK divididas (split APKs), que es el formato con el que llegan
casi todas las apps actuales desde fuera de una tienda. Trabaja con Shizuku y evita el clásico «la app
no se ha instalado» al abrir un paquete que trae tres archivos.

### Cómo se usa

1. Descarga el paquete completo —los `.apk` y el `.apks` o el `.xapk`— sin descomprimirlo.
2. Enciende Shizuku y abre el paquete con universal-installer.
3. Revisa qué partes va a instalar y confirma; el progreso se ve por partes.

### Lo que conviene saber antes

Entrega `v1.21.0` del 1 de noviembre de 2026, GPL-3.0, empujón de noviembre: de los más vivos del
racimo.

### Cuándo no vale la pena

Si solo instalas desde una tienda, esto no tiene trabajo. Su terreno son los paquetes partidos y las
apps que no están en ninguna tienda.
"""

GUIA["0x192/universal-android-debloater"] = """
### Para qué sirve

Fue el programa de escritorio que se conectaba por ADB y desinstalaba el relleno del fabricante desde
un ordenador, con una lista comentada de qué hace cada paquete. Es el proyecto que enseñó a media
internet a limpiar un Android sin root.

### Lo que conviene saber antes

Su último empujón es del **2 de agosto de 2024** y no tiene entregas etiquetadas: para este catálogo
está parado. Y no está archivado, lo que es peor: parece vivo.

### Qué hacer en su lugar

`Universal-Debloater-Alliance/universal-android-debloater-next-generation`, con ficha en este racimo:
entrega `v1.3.1` del 2 de noviembre de 2026 y empujón del 5 de noviembre. El heredero es más joven y
más activo que el original, que es el patrón de medio racimo.
"""

GUIA["Universal-Debloater-Alliance/universal-android-debloater-next-generation"] = """
### Para qué sirve

La continuación de UAD: conecta por ADB desde un ordenador y desinstala o desactiva paquetes del
sistema con una descripción de qué hace cada uno y una recomendación por defecto. Se puede usar con
interfaz o por línea de órdenes.

### Cómo se usa

1. En el teléfono: opciones de desarrollador y depuración USB.
2. En el ordenador: `adb devices` para comprobar que el teléfono aparece, y si no aparece, autorizar la
   huella del equipo en la pantalla del teléfono.
3. Abre el programa, elige el teléfono y filtra por recomendación: «recomendado», «avanzado»,
   «expertos». Empieza por lo recomendado y en lotes pequeños.
4. Antes de aplicar, exporta la lista de paquetes: es la única forma de volver atrás con orden.

### Lo que conviene saber antes

Entrega `v1.3.1` del 2 de noviembre de 2026, GPL-3.0, ★9.751 y empujón de hoy: el recurso más activo
del racimo junto con Shizuku-Next. Funciona sin root y sin Shizuku: solo necesita ADB.

### Cuándo no vale la pena

Si no tienes un ordenador a mano, o si el teléfono no deja activar la depuración. Y si el teléfono es
de otra persona, o está en garantía: desinstalar paquetes del sistema se nota cuando llega una
actualización.
"""

GUIA["sunilpaulmathew/De-Bloater"] = """
### Para qué sirve

Desinstala aplicaciones del sistema desde el teléfono, con la potencia de **Magisk**: es de la familia
del root, no de la de Shizuku. Para quien ya tiene Magisk, es la vía cómoda.

### Lo que conviene saber antes

Entrega `v0.32` del 25 de mayo de 2026, GPL-3.0, ★803 y empujón de mayo: se mantiene despacio. Su
README está hecho de escudos e imágenes y no tiene un párrafo que se pueda citar; el primer enlace que
aparece es la descarga directa de su APK, que es toda la documentación que da.

### Cuándo no vale la pena

Sin root no funciona, y con root hay al menos tres maneras mejores de hacer lo mismo desde un
ordenador. Se justifica si quieres limpiar sin cable y ya vives en Magisk.
"""

GUIA["timschneeb/awesome-shizuku"] = """
### Para qué sirve

Es **la lista**: un catálogo curado de aplicaciones que usan Shizuku, con ★10.708 y actualización de
noviembre de 2026. Es el tipo de recurso que este catálogo quiere mejorar, y por eso tiene ficha
propia en vez de una nota.

### Qué hace bien y qué no

Hace bien lo difícil: selecciona, agrupa y mantiene. Lo que no hace —y no es su oficio— es decir en
qué estado está cada entrada: una app listada puede llevar dos años sin actualizarse, y la lista no
lleva la fecha al lado. Eso es exactamente lo que añade esta ficha por recurso: estado, licencia,
última entrega y qué no se ha verificado.

### Cómo se usa con este catálogo

La lista sirve para descubrir; estas fichas, para decidir. Si una app aparece en la lista y aquí no
tiene ficha, es que aún no se ha medido: se pide y se mide, que es más trabajo que copiarla.

### Su licencia

GitHub la marca como NOASSERTION: no declara una licencia estándar. Para copiar su selección hay que
leer su archivo de licencia o pedir permiso; para leerla y seguir sus enlaces, no hace falta nada.
"""


def main() -> int:
    medido = json.loads(MEDIDO.read_text(encoding="utf-8"))
    escritas = 0
    for repo, texto in GUIA.items():
        f = medido.get(repo)
        if not f or f.get("racimo") != "shizuku-y-herederos":
            print("  ! sin medir en el racimo:", repo)
            continue
        p = CATALOGO / repo.replace("/", "--").lower() / "FICHA.md"
        if not p.exists():
            print("  ! sin ficha:", repo)
            continue
        t = p.read_text(encoding="utf-8")
        if INICIO not in t or FIN not in t:
            print("  ! sin marcadores:", repo)
            continue
        nuevo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIN),
                       INICIO + "\n" + texto.strip() + "\n" + FIN, t, flags=re.S)
        if nuevo != t:
            p.write_text(nuevo, encoding="utf-8")
            escritas += 1
    print(f"guías escritas: {escritas} de {len(GUIA)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
