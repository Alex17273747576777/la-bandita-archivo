# Cómo publicar esta página (Rusia · Brasil · dominio gratis)

> **Ya está publicada en GitHub Pages:** https://alex17273747576777.github.io/la-bandita-archivo/
> Este documento queda como plan B (Rusia · Brasil · dominio propio), no como el único camino.

La página ya está armada y **funciona sin red**: `web/index.html` lleva los 3.116 repositorios medidos
dentro del propio archivo, sin CDN, sin fuentes externas, sin rastreadores y sin una sola llamada a un
servidor. 599 KB. Se abre con doble clic y se ve igual.

Lo que no puedo hacer yo: **abrir una cuenta a tu nombre**. Los registros de dominio y las cuentas de
GitVerse, GitFlic y nic.eu.org piden correo, captcha y un código que llega a tu bandeja. Eso es tuyo.
Lo que sí queda hecho: los archivos, los datos y los pasos exactos, en orden, con lo que cuesta cada uno.

---

## Rusia · GitVerse (recomendado)

GitVerse es el alojamiento de código ruso (Sber). Tiene **páginas estáticas** y es gratis.

1. Crea la cuenta en `https://gitverse.ru` (pide correo; acepta registro desde fuera de Rusia).
2. Crea un repositorio público, por ejemplo `archivo-abierto`. **Sin README automático.**
3. Desde esta carpeta:

   ```bash
   cd web
   git init -b main
   git add index.html datos.json CNAME .nojekyll robots.txt
   git -c user.name="La Bandita" -c user.email="tu@correo" commit -m "archivo abierto: 3.116 repositorios medidos"
   git remote add gitverse https://gitverse.ru/TU-USUARIO/archivo-abierto.git
   git push gitverse main
   ```

4. En el repositorio: **Settings → Pages** (o «Страницы»). Elige la rama `main` y la carpeta raíz.
5. La dirección que te da GitVerse es del tipo `https://TU-USUARIO.gitverse.site/archivo-abierto/`.
   Esa ya es pública y es gratis, sin dominio propio.

**Aviso medido:** `gitverse.ru` respondió **429** (demasiadas peticiones) a la comprobación automática
desde este entorno. No es que esté caído: está limitando. Desde un navegador abre normal.

## Rusia · GitFlic (alternativa)

`https://gitflic.ru` respondió **200**. También es ruso y también tiene páginas. El proceso es el mismo:
cuenta, repositorio, `git push` y activar páginas en los ajustes. Su registro pide más datos que GitVerse
y su interfaz está solo en ruso.

**Sobre un dominio `.ru`:** no hay `.ru` gratis. El registro ruso (nic.ru, reg.ru, timeweb) cobra entre
200 y 300 rublos al año, y **exige pasaporte ruso o INN para personas de fuera**. Por eso el paquete va
con la dirección que te da el propio GitVerse, que no cuesta nada y no pide documentos.

---

## Brasil · Codeberg (recomendado, sin costo y sin documentos)

Codeberg es una cooperativa sin ánimo de lucro, con servidores en Alemania, **gratis, sin anuncios y sin
venta de datos**. Respondió **200**. Su servicio de páginas estáticas funciona así:

1. Cuenta en `https://codeberg.org` (solo correo).
2. Repositorio público `archivo-abierto`.
3. `git remote add codeberg https://codeberg.org/TU-USUARIO/archivo-abierto.git` y `git push codeberg main`.
4. En **Settings → Pages** activa «Static pages» para la rama `main`.
5. Te queda en `https://TU-USUARIO.codeberg.page/archivo-abierto/`.

**¿Y algo alojado en Brasil?** No encontré un servicio de páginas estáticas gratuito con sede en Brasil
que se pueda abrir sin empresa ni tarjeta. Lo que sí hay en Brasil es **registro de dominio con
CPF/CNPJ** en `registro.br` —que respondió **200**— y hospedaje barato (Hostinger Brasil, HostGator
Brasil). Ninguno es gratuito para alguien sin documentos brasileños, y aquí no se va a escribir que sí
lo es. Si tienes CPF o CNPJ, la vía es `registro.br` para el `.com.br` y Codeberg o GitHub para servir
los archivos.

---

## Dominio gratis de verdad (y lo que hay que saber)

### Opción 1 — `eu.org` (la mejor relación esfuerzo/beneficio)

`https://nic.eu.org` respondió **200**. Da subdominios **gratis desde 1996**, a personas y a
organizaciones sin ánimo de lucro, sin pedir documentos y sin cobrar nunca.

- Se pide en `https://nic.eu.org/arf/en/`: eliges un nombre bajo `eu.org` y **dos servidores de nombres**.
- La aprobación es **manual y tarda días o semanas**. No es instantánea.
- Para que funcione con GitVerse o Codeberg, en la solicitud se ponen los servidores de nombres del
  proveedor (Codeberg Pages usa `ns1.codeberg.org`, pero se puede apuntar por CNAME al `*.codeberg.page`).
  Lo más simple: pedir el `eu.org`, y en tu proveedor de DNS gratuito (Cloudflare, `1984.is`) poner un
  CNAME al sitio que ya funciona.

### Opción 2 — DigitalPlat FreeDomain

`https://dash.domain.digitalplat.org/` — regala dominios en `.dpdns.org`, `.us.kg`, `.qzz.io`, `.xx.kg`
y `.qd.je`. Respondió **200** y su proyecto de código abierto tiene ★207.640. Registro automático por
correo, se conecta con servidores de nombres propios. Es la vía más rápida de las dos.

### Opción 3 — sin dominio propio

GitVerse, GitFlic y Codeberg ya te dan una dirección pública gratis el primer día. Un dominio propio no
cambia lo que la página hace: cambia cómo se ve el enlace. No es el paso urgente.

---

## El atajo: `publicar.sh`

En vez de hacer los pasos a mano, el paquete trae el script. Comprueba la página, crea el repositorio
con la API del proveedor y empuja:

```bash
cd web
TOKEN=tu-token ./publicar.sh gitverse  tu-usuario  archivo-abierto
TOKEN=tu-token ./publicar.sh codeberg  tu-usuario  archivo-abierto
TOKEN=tu-token ./publicar.sh gitflic   tu-usuario  archivo-abierto
```

Antes de tocar nada verifica dos cosas: que estén los cuatro archivos y que la página **no descargue
nada de fuera** (cuenta `src`, `<link>`, `@import` y `url()` externos, y se detiene si hay alguno).
Después del `push` queda un paso que solo puedes dar tú: activar Pages en los ajustes del repositorio,
porque ninguno de los tres deja activarlo por token.

**Los tres puntos de la API se comprobaron hoy con un token falso**, para no escribir un nombre
inventado: `api.gitverse.ru/v1/user/repos` contesta **400 VALIDATION_ERROR** (y enlaza su
documentación), `api.gitflic.ru/project` contesta **403 AccessDenied**, y
`codeberg.org/api/v1/user/repos` contesta **401 «token is malformed»** —el comportamiento correcto de
Gitea—. Los tres existen; los tres piden tu token bueno.

## Lo que ya está hecho, para que no se repita

| Archivo | Qué es |
|---|---|
| `web/index.html` | la página entera, con los datos dentro (599 KB, 3.116 fichas) |
| `web/datos.json` | los mismos datos en JSON, para reusar (776 KB) |
| `web/CNAME` | `la-bandita-archivo.eu.org`, para cuando el dominio esté aprobado |
| `web/.nojekyll` | para que GitHub Pages no procese nada |
| `web/robots.txt` | permitir la indexación: son datos públicos |
| `web/LEEME.md` | qué es la página y qué licencia tiene |

## La licencia

Los **datos** (lo que se midió) van como **CC0**: dominio público, sin pedir permiso. El **código** de la
página también. Los programas enlazados tienen la licencia que declara cada autor, y se consulta en su
repositorio: aquí no se afirma la licencia de nadie más allá de lo que la API devolvió.
