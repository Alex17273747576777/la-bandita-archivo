# curl-impersonate · lwthiker

*curl-impersonate: A special build of curl that can impersonate Chrome & Firefox*

**Racimo:** descargas · **Repositorio:** `lwthiker/curl-impersonate` · **Estado:** parado · **Medido:** 2026-11-05 11:44 UTC

## Qué es, según quien lo hace

> A special build of curl that can impersonate the four major browsers: Chrome, Edge, Safari & Firefox. curl-impersonate is able to perform TLS and HTTP handshakes that are identical to that of a real browser.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** parado · último empujón el 18 de julio de 2024 (hace 840 días)
- **Estrellas:** 7.172 · 608 bifurcaciones · 82 incidencias abiertas
- **Licencia:** MIT
- **Lenguaje:** Python · creado el 17 de febrero de 2022
- **Última entrega:** `v0.6.1` del 2 de marzo de 2024 · 8 adjuntos
- **Plataformas que menciona su README:** Android, Windows, macOS, Linux, Web
- **Medido:** 2026-11-05 11:44 UTC

## Cómo se consigue

- Installation
- Before you use them you need to install nss (Firefox's TLS library) and CA certificates:
- Ubuntu - `sudo apt install libnss3 nss-plugin-pem ca-certificates`
- Red Hat/Fedora/CentOS - `yum install nss nss-pem ca-certificates`

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/lwthiker/curl-impersonate
- la última entrega: https://github.com/lwthiker/curl-impersonate/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Una compilación de `curl` que se presenta ante el servidor **igual que un navegador de verdad**: mismo
saludo de cifrado, mismas cabeceras, mismo orden. Sirve para los sitios que responden distinto según quién
llama, no según lo que pide.

### Cómo se usa

1. Hay paquetes para varias distribuciones y una imagen de contenedor; también se puede compilar.
2. Se usa como `curl`, con un guion añadido al nombre del ejecutable para elegir a quién imita: el de Chrome,
   el de Edge, el de Safari o el de Firefox.
3. Las mismas opciones de siempre —`-o`, `-H`, `-L`— valen igual.

### Lo que conviene saber antes

Su último cambio es de **julio de 2024** y su última entrega, `v0.6.1`, de marzo de 2024: los navegadores
han cambiado de versión muchas veces desde entonces, y la huella que imita se queda atrás. Licencia MIT.
No es un descargador: es una herramienta para que otro programa pueda pasar por navegador. Y sirve para
entender por qué tu descargador falla en una web concreta.

### Cuándo no vale la pena

Si el sitio no te bloquea, esto no cambia nada. Y si lo que quieres es bajar vídeo, no empieces por aquí:
esto es fontanería, no una aplicación.

<!-- GUIA:FIN -->
