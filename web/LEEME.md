# La página pública del archivo

**Está publicada:** https://alex17273747576777.github.io/la-bandita-archivo/

Salida del despliegue: `completed success` en 5 pasos. Respuesta medida desde fuera:
`HTTP 200 · 613.314 bytes`, idéntica byte a byte al `index.html` construido.

## Qué es

3.116 repositorios medidos contra la API pública de GitHub, dentro de un solo archivo: sin CDN, sin
fuentes externas, sin rastreadores y sin una sola llamada a un servidor al abrirlo. 613 KB.

## Lo que hay que decir sin adornos

- **Los datos van dentro del HTML** (607.200 caracteres de JSON en línea), pero se pintan con
  JavaScript. Se abre sin red y funciona; con JavaScript desactivado se ve el encabezado y una tabla
  vacía. Es una página que depende de su propio script, no de nada de fuera.
- **Los buscadores ven poco:** el contenido no está en el HTML, así que el índice de Google no lo
  lee. Si eso importa, hay que añadir una versión estática de la tabla.
- **El dominio propio no está:** `la-bandita-archivo.eu.org` no tiene DNS todavía. El archivo se
  guarda en `CNAME.eu-org-en-espera.txt`; en cuanto haya registros, se repone y Pages lo sirve.

## Cómo se publica

`.github/workflows/pagina.yml` empaqueta `web/` y lo publica con `actions/deploy-pages`. Se dispara
solo cuando cambia algo de `web/`, y a mano desde la pestaña Actions.

El despliegue clásico de Pages **no sirvió**: se quedó más de media hora en «building», con
`duration 0`, y al final cayó con `failure`. No era la página: era el despliegue.

## Los otros alojamientos

`COMO-PUBLICAR.md` sigue teniendo los pasos de GitVerse (Rusia) y Brasil. Ya no son la única vía:
GitHub Pages está funcionando.
