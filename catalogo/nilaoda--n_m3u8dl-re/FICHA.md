# N_m3u8DL-RE · nilaoda

*Cross-Platform, modern and powerful stream downloader for MPD/M3U8/ISM. English/简体中文/繁體中文.*

**Racimo:** descargas · **Repositorio:** `nilaoda/N_m3u8DL-RE` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> 遇到 BUG 请首先确认软件是否为最新版本（如果是 Release 版本，建议到 Actions 页面下载最新自动构建版本后查看问题是否已经被修复），如果确认版本最新且问题依旧存在，可以到 Issues 中查找是否有人遇到过相关问题，没有的话再进行询问。

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 9.038 · 892 bifurcaciones · 369 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** C# · creado el 25 de mayo de 2022
- **Última entrega:** `v0.6.0-beta` del 28 de junio de 2026 · 9 adjuntos
- **Plataformas que menciona su README:** iOS, Windows, macOS, Linux, Web
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- save-dir "Downloads/My Videos"
- download-retry-count <number> 每个分片下载异常时的重试次数；直播失败分片独立补片，超过补片窗口后标记缺片 [default: 7]
- skip-download 跳过下载 [default: False]
- mt, --concurrent-download 并发下载已选择的音频、视频和字幕 [default: False]

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/nilaoda/N_m3u8DL-RE
- la última entrega: https://github.com/nilaoda/N_m3u8DL-RE/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Descargador de **emisiones por trozos**: toma la lista de fragmentos de una emisión (HLS, DASH o ISM) y los
une en un solo archivo, con las pistas de audio y subtítulos que elijas. Es lo que se usa cuando el vídeo no
es un archivo sino una retransmisión partida en mil pedazos.

### Cómo se usa

1. Se descarga el binario de la entrega `v0.6.0-beta`, del 28 de junio de 2026, para Windows, Linux o macOS.
2. Se le pasa la dirección de la lista de fragmentos y, opcionalmente, la del audio por separado.
3. Se eligen pistas con `--select-video`, `--select-audio` y `--select-subtitle`, y el programa descarga en
   paralelo y une con `FFmpeg`.

### Lo que conviene saber antes

La etiqueta dice **beta** y así hay que tomarlo, aunque lleve 9.038 estrellas y dos años de entregas. Su
documentación está en chino, inglés y chino tradicional; la ayuda de la propia orden, en inglés. Aquí **no
se enlaza ninguna lista de fragmentos ni ninguna emisión concreta**: la herramienta vale para lo que sea
que tengas derecho a descargar, y eso no lo decide el programa.

### Cuándo no vale la pena

Si el vídeo ya es un archivo, esto es un rodeo: usa `aria2` o el navegador. Y sin `FFmpeg` instalado no une
nada, así que la instalación son dos piezas, no una.

<!-- GUIA:FIN -->
