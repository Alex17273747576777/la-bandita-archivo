# RHash · rhash

*Great utility for computing hash sums*

**Racimo:** torrentes · **Repositorio:** `rhash/RHash` · **Estado:** vivo · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> RHash (Recursive Hasher) is a console utility for calculation and verification of magnet links and various message digests, including CRC32, CRC32C, MD4, MD5, SHA1, SHA256, SHA512, SHA3, AICH, ED2K, DC++ TTH, BitTorrent BTIH, Tiger, GOST R 34.11-94, GOST R 34.11-2012, RIPEMD-160, HAS-160, EDON-R, and Whirlpool.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 28 de octubre de 2026 (hace 8 días)
- **Estrellas:** 735 · 133 bifurcaciones · 55 incidencias abiertas
- **Licencia:** 0BSD
- **Lenguaje:** C · creado el 12 de junio de 2011
- **Última entrega:** `v1.4.6` del 13 de mayo de 2025 · 2 adjuntos
- **Plataformas que menciona su README:** Windows, macOS, Linux
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Installation
- ./configure && make install
- For more complicated cases of installation see the [INSTALL.md] file.
- [INSTALL.md]: INSTALL.md

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/rhash/RHash
- su web: http://rhash.sf.net
- la última entrega: https://github.com/rhash/RHash/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Utilidad de consola que calcula y verifica huellas de archivos: CRC32, MD5, SHA-1, SHA-256, SHA-512, SHA3,
BLAKE, ED2K, TTH de DC++ y **BTIH, la huella que identifica un torrent**. Con ella se comprueba que lo que se
descargó es exactamente lo que se quería descargar.

Es el corrector de errores de la cadena entera: sirve igual para un archivo bajado de una web, para un disco
que empieza a fallar o para una copia de seguridad que quieres verificar diez años después.

### Cómo se usa

1. Se instala desde los paquetes de la distribución o se compila con `./configure && make install`.
2. Para calcular todas las huellas de un archivo: `rhash -a SHA256 archivo.iso`.
3. Para verificar contra una lista: `rhash -c lista.sha256`.
4. Para recorrer una carpeta entera: `rhash --recursive --sha256 carpeta/ > lista.sha256`.

### Lo que conviene saber antes

735 estrellas, 0BSD —una licencia permisiva sin condiciones, la más libre que se puede escribir—, C, y creado
en 2011: quince años de historia. 133 bifurcaciones y 55 incidencias abiertas. Su última entrega etiquetada es
la `v1.4.6`, del 13 de mayo de 2025, aunque los empujones son recientes.

Se distribuye como programa de consola para Windows, macOS y Linux, y hay interfaces gráficas hechas por otros.
El detalle que conviene entender: una huella sirve para comprobar **integridad**, no para saber de quién es un
archivo; si alguien cambia el archivo y la lista, las dos coinciden.

### Cuándo no vale la pena

Si nunca compruebas nada de lo que descargas, ninguna herramienta de este tipo te va a cambiar la vida. Y para
un solo archivo, casi todos los sistemas ya traen un comando que calcula SHA-256.

<!-- GUIA:FIN -->
