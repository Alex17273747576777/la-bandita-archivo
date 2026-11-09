*La lección del hash SHA-256: cómo comprobar un archivo sin root, en sesenta segundos*

*La Bandita · domingo 8 de noviembre de 2026, 12:40 en Santo Domingo · edición dominicano-español · pieza 40 de Facebook*

⏱️ *Lectura total: 9 minutos · la pieza más corta de la serie, a propósito · un método, tres órdenes y una costumbre · cero paquetes alojados aquí · cero enlaces a espejos*

*🗺️ Mapa de esta pieza*

```
├── 🧱 La semilla · usted no baja archivos, baja confianza
├── ⚡ En una página · el método en sesenta segundos
├── 🔐 Qué es un hash y qué no es
├── 🧾 Los cuatro disfraces de la huella
├── 🛠️ Las tres órdenes, con lo que devuelven de verdad
├── ⚖️ HTTPS no es una huella, y la firma del APK no es la del autor
├── 📋 Lo que midió el archivo esta semana · las cuatro cifras que importan
├── 🗂️ La costumbre · su cuaderno de huellas
├── 🚪 Lo que esta pieza no tiene
├── 📅 La semana de prueba
├── ❓ Las preguntas del grupo
└── 🗒️ Notas al pie
```

───────────────────

*🧱 La semilla · usted no baja archivos, baja confianza*

Cuando usted toca «descargar» en un repositorio de GitHub, no está bajando un programa: está bajando **una promesa**. La promesa de que el archivo que llega a su teléfono es el mismo que el autor compiló, y no uno que alguien cambió en el camino —en su red, en el wifi del colmado, en un espejo que dice ser el bueno—.

Casi todo el mundo acepta esa promesa sin mirarla. Y casi todo el mundo tiene razón casi todo el tiempo. El problema es que «casi siempre» no es un método: es una racha. Las rachas se rompen sin avisar, y cuando se rompen no hay manera de saber cuándo empezó.

Un **hash SHA-256** convierte esa promesa en una cuenta que usted puede hacer en su propio teléfono, sin root, sin cuenta, sin pagar nada y sin creerle a nadie. Esta pieza enseña a hacerla. Es la más corta de la serie porque el método cabe en una pantalla y esta casa no va a rellenar cuarenta páginas para que parezca importante.

───────────────────

*⚡ En una página · el método en sesenta segundos*

1. **Baje el archivo.** APK, ZIP, EXE, lo que sea.
2. **Baje la huella del mismo autor**, de la misma página de la entrega, de preferencia en un archivo aparte (`.sha256`, `.sha512`, `sums.txt`).
3. **Calcule el hash del archivo que tiene en la mano.** En Termux: `sha256sum miarchivo.apk`. En Windows: `Get-FileHash .\miarchivo.apk -Algorithm SHA256`.
4. **Compare los sesenta y cuatro caracteres**, uno por uno. No «se parecen»: iguales o no iguales.
5. **Apunte el resultado** con la fecha, en una nota del teléfono.

Si los sesenta y cuatro coinciden, usted tiene el archivo que el autor publicó. Si no coinciden, **no lo tiene**, diga lo que diga el nombre del archivo, el tamaño o el icono. No hay tercera opción, y ahí está la gracia: no hay nada que interpretar.

───────────────────

*🔐 Qué es un hash y qué no es*

Un hash es una función que toma un archivo de cualquier tamaño —un APK de 60 megas, una imagen de 4 gigas— y devuelve una huella de tamaño fijo. En SHA-256 esa huella son **256 bits**, que se escriben como **sesenta y cuatro caracteres hexadecimales**: `a8d86ebb66aa…`.

Tres propiedades que importan y que la gente confunde:

**No se puede deshacer.** De la huella no se recupera el archivo. No sirve para espiar, sirve para comparar.

**Cambia entera con un solo bit.** No hay manera de «casi» mantenerla. Si alguien cambia una línea del programa, agrega un permiso o mete una llamada a un servidor, la huella sale completamente distinta. No existe el cambio invisible.

**No dice si el programa es bueno.** Esto es lo que más se malentiende. Un hash no opina: un programa espantoso con su hash correcto sigue siendo el programa que el autor publicó. La huella no dice «confíe»; dice **«esto es exactamente lo que esa persona publicó»**. La confianza en la persona es otro problema, y no se resuelve con una orden.

───────────────────

*🧾 Los cuatro disfraces de la huella*

Si el autor publica huella, casi siempre es uno de estos cuatro, y los cuatro se comprueban igual:

**El archivo aparte.** Algo llamado `algo.apk.sha256`, `algo.apk.sha512`, `checksums.txt`, `SHA256SUMS`. Es el mejor caso: se baja por separado y se compara.

**La nota de la entrega.** El texto de la release trae una línea tipo `sha256: 3f9a…`. Sirve, pero se copia a mano y ahí se cuela el error de dedo más común de todos.

**La firma GPG.** Un archivo `.asc` o `.sig` al lado del paquete. No es un hash: es una firma criptográfica. Se comprueba con `gpg --verify algo.apk.asc algo.apk`, y le dice además **quién** lo firmó, cosa que un hash no puede decir.

**La atestación.** El caso nuevo, y el más fuerte: una declaración firmada por el sistema de integración continua de que ese archivo salió de ese repositorio en esa compilación. Se comprueba con `gh attestation verify`.

Lo que **no** es una huella, aunque lo parezca: el tamaño en bytes, la fecha del archivo, el nombre con la versión adentro, el número de estrellas del repositorio y el candadito del navegador.

───────────────────

*🛠️ Las tres órdenes, con lo que devuelven de verdad*

**Uno · el hash a mano.** En Termux, sin instalar nada raro:

```
pkg install coreutils -y
sha256sum miarchivo.apk
```

Devuelve una línea: la huella, dos espacios y el nombre del archivo. Esa huella es la que se compara.

**Dos · comparar contra el archivo del autor.** Si el autor publica un `SHA256SUMS`, esto lo hace por usted y en un segundo:

```
sha256sum -c SHA256SUMS --ignore-missing
```

Devuelve `miarchivo.apk: OK` cuando coincide y `FAILED` cuando no. Si dice `FAILED`, no hay nada más que discutir: borre el archivo y vuelva a bajarlo de la página oficial del autor.

**Tres · mirar la firma del paquete.** Esto es otra cosa distinta y conviene no mezclarla:

```
apksigner verify --print-certs miarchivo.apk
```

Devuelve el certificado con que el paquete fue firmado. Sirve para una pregunta que el hash no responde: **¿este APK me va a poder actualizar el que ya tengo instalado?** Si el certificado cambió respecto a la versión anterior, Android se negará a actualizar, y eso es una señal.

───────────────────

*⚖️ HTTPS no es una huella, y la firma del APK no es la del autor*

Dos confusiones que se repiten en los comentarios del grupo, y las dos importan:

**«Uso HTTPS, ya estoy protegido».** HTTPS protege el camino entre el servidor y usted. No dice nada del archivo: si el repositorio del autor fue comprometido y el atacante reemplazó el paquete, HTTPS le entrega el paquete malo con el candadito puesto y funcionando perfecto. La huella publicada **aparte** es lo que rompe ese ataque, porque el atacante tendría que cambiar también la huella, y esa huella ya está copiada en su cuaderno.

**«El APK está firmado, entonces está verificado».** Todo APK de Android está firmado: sin firma no se instala. La pregunta no es si tiene firma, es **quién** firmó, y si ese quién es el mismo que firmó la versión que usted ya tiene. `apksigner` responde eso. La huella del autor responde otra cosa distinta, y las dos preguntas se hacen por separado.

───────────────────

*📋 Lo que midió el archivo esta semana · las cuatro cifras que importan*

Esta casa lleva cuarenta piezas contando lo mismo, y no cambia: **la mayoría del software libre no publica huella**. Cuatro cifras de esta semana, todas del archivo, todas con su fecha:

De las **cincuenta y seis tiendas de extensiones** de la pieza 10, **una sola firma lo que publica**: Zenbu, diez sumas de veinte archivos. Keiyoushi, la más usada del ecosistema con ★15.432, publica **2.928 archivos y ninguna suma**.

De los **cincuenta y nueve recursos** del kit de la pieza 12, **501 archivos de 3.022** llevan suma: el **17,0 %**. El mejor puntuado de la serie, **Readest**, saca 80 sobre 80 y no es el más famoso del kit.

De los **cinco gigantes de la pantalla grande** —Home Assistant, Jellyfin, Kodi, ESPHome y SmartTube—, medidos otra vez el **8 de noviembre de 2026** para esta pieza: tres no publican ningún adjunto en su última entrega, SmartTube publica cuatro y **ninguno de los cinco adjunta una suma**.

Y de los **diecisiete programas de archivos y copias** de la pieza 09, cuatro dan huella, y el que más da no es el más instalado: **AF-File-Manager**, ochenta y dos días de vida y ★18, con cuarenta sumas de ochenta y cincuenta entregas.

La conclusión no es un sermón: es un criterio de compra. **Cuando dos programas le sirven igual, el que publica la huella le está dando algo que el otro no.**

───────────────────

*🗂️ La costumbre · su cuaderno de huellas*

Una huella suelta no vale casi nada: lo que vale es la huella de **ayer**. Si usted tiene apuntado el hash de la versión que instaló, el día que salga una nueva puede preguntar dos cosas de una vez: si el archivo nuevo es el que el autor publicó, y si el autor sigue siendo el mismo.

El cuaderno puede ser una nota de texto en el teléfono, una hoja de cálculo o una carpeta con archivos `.sha256`. Lo que sea, con tres columnas: **programa · versión · huella**. Copiar y pegar. Se hace en el momento de instalar, que es el único momento en que cuesta cero.

Y si el autor **no publica** huella, la casa tiene una plantilla para pedirla en las incidencias del repositorio, sin pleito y sin exigencias: pide el archivo, no la promesa. Está al final de cada pieza de la serie. Algunas veces funciona.

───────────────────

*🚪 Lo que esta pieza no tiene*

No tiene un programa nuevo que instalar. No tiene una lista de «las diez apps más seguras», porque seguridad no es una lista, es una comprobación. No tiene capturas de pantalla de un teléfono que esta casa no tiene en la mano. No tiene premios ni concursos: el único premio que esta casa reparte es el criterio, y no se entrega, se practica.

Y no tiene la promesa de que comprobar el hash lo protege de todo. Lo protege de una cosa concreta y frecuente: **que el archivo que instala no sea el que el autor publicó**. De las demás —permisos, telemetría, código que hace lo que dice pero no lo que usted quiere— se ocupan las otras treinta y nueve piezas.

───────────────────

*📅 La semana de prueba*

Un solo ejercicio, siete días, y no cuesta nada:

**Día 1.** Elija el programa que más usa de los que instaló este año. Busque si su autor publica huella.
**Día 2.** Si publica, compruébela con las tres órdenes de arriba y apunte el resultado en el cuaderno.
**Día 3.** Si no publica, pídala en las incidencias con la plantilla. Una frase cortés y el enlace a lo que se pide.
**Día 4.** Repita con el segundo programa.
**Día 5.** Repita con el tercero.
**Día 6.** Mire el cuaderno: ¿cuántos de los tres le dieron con qué comprobar? Ese número es su mapa real de confianza, no el de las estrellas.
**Día 7.** Vuelva a esta pieza y verifique la huella del archivo que se bajó hoy. Si coincide, ya sabe hacer lo único que esta pieza enseña.

───────────────────

*❓ Las preguntas del grupo*

**¿Y si el autor no publica la huella en ningún lado?** Entonces no hay nada que comprobar, y eso también es información: anótelo en el cuaderno como «sin huella» y decida con eso a la vista.

**¿Sirve comparar el tamaño del archivo?** Como señal rápida, sí; como comprobación, no. El tamaño se puede conservar mientras el contenido cambia.

**¿Y el hash MD5 que a veces aparece?** Existe, se usa y está roto para efectos de seguridad. Si el autor solo publica MD5, pídale SHA-256. No es un capricho: es el estándar desde hace años.

**¿Tengo que hacerlo con cada actualización?** Con las que le importen. Yo lo hago con las que instalo a mano; con las que actualiza un gestor de confianza, lo hago de vez en cuando para no criar pereza.

**¿Esto necesita root?** No. Ninguna de las tres órdenes de esta pieza necesita root, ni permisos especiales, ni cuenta en ningún sitio.

**¿Y en la computadora?** Igual: `sha256sum` en Linux y macOS, `Get-FileHash` en Windows, `certutil -hashfile archivo SHA256` si prefiere lo que ya viene.

───────────────────

*🌅 Cierre*

Cuarenta piezas midiendo lo mismo, y la cifra no ha dejado de sorprenderme: la huella es barata de publicar —un archivo de texto de dos líneas— y sigue siendo rara. No es mala fe: es que nadie la pide. Por eso esta pieza no pide un cambio en el ecosistema, pide una costumbre en usted. Sesenta y cuatro caracteres, una vez por instalación, y el archivo deja de ser una promesa.

*La Bandita informa a partir de fuentes fechadas. · domingo 8 de noviembre de 2026 · las cifras de la serie se midieron con la API pública de GitHub en las fechas que declara cada pieza; la comprobación de los cinco gigantes se repitió el 8 de noviembre de 2026 para esta pieza. Ningún paquete se aloja aquí; solo enlaces al repositorio del autor en GitHub.*
