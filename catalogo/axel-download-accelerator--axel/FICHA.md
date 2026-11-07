# axel · axel-download-accelerator

*Lightweight CLI download accelerator*

**Racimo:** descargas · **Repositorio:** `axel-download-accelerator/axel` · **Estado:** lento · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> Axel tries to accelerate the download process by using multiple connections per file, and can also balance the load between different servers.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** lento · último empujón el 30 de septiembre de 2026 (hace 36 días)
- **Estrellas:** 3.423 · 309 bifurcaciones · 87 incidencias abiertas
- **Licencia:** GPL-2.0
- **Lenguaje:** C · creado el 13 de agosto de 2015
- **Última entrega:** `v2.17.14` del 7 de abril de 2024 · 3 adjuntos
- **Plataformas que menciona su README:** Linux, Web
- **Lo que dice su propio texto:** abandono declarado
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- AXEL - Lightweight CLI download accelerator
- Axel tries to accelerate the download process by using multiple
- open tickets.
- Installing from binaries

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/axel-download-accelerator/axel
- la última entrega: https://github.com/axel-download-accelerator/axel/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Acelerador de descargas de terminal, minúsculo: abre varias conexiones contra el mismo archivo para que la
descarga no dependa de la lentitud de una sola. También reparte la carga entre varios servidores espejo del
mismo archivo, que es donde de verdad se nota.

### Cómo se usa

1. Se instala desde el gestor de paquetes de la distribución; si no está, se compila, que son dos órdenes.
2. Descarga normal: `axel` y la dirección. Con `-n` se fija el número de conexiones, con `-o` el nombre de
   salida.
3. Para reanudar algo cortado se vuelve a lanzar la misma orden con el archivo a medias en la carpeta: lo
   detecta y sigue.

### Lo que conviene saber antes

Tiene 3.423 estrellas, licencia GPL-2.0 y una entrega `v2.17.14` de **abril de 2024**, aunque el
repositorio recibe cambios en septiembre de 2026. Es una herramienta vieja y estable; no espera interfaz,
ni cola, ni historial decorado.

### Cuándo no vale la pena

Contra servidores que limitan por conexión —los que te cortan si abres varias—, `axel` empeora las cosas.
Para una descarga suelta, `wget2` o `curl` hacen el trabajo sin multiplicar conexiones.

<!-- GUIA:FIN -->
