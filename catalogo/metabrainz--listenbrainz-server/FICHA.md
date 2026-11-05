# listenbrainz-server · metabrainz

*Server for the ListenBrainz project, including the front-end (javascript/react) code that it serves and all of the data processing components that LB uses.*

**Racimo:** audio · **Repositorio:** `metabrainz/listenbrainz-server` · **Estado:** vivo · **Medido:** 2026-11-05 11:43 UTC

## Qué es, según quien lo hace

> ListenBrainz keeps track of music you listen to and provides you with insights into your listening habits. We're completely open-source and publish our data as open data.

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 4 de noviembre de 2026 (hace 1 días)
- **Estrellas:** 1.052 · 388 bifurcaciones · 82 incidencias abiertas
- **Licencia:** GPL-2.0
- **Lenguaje:** Python · creado el 5 de septiembre de 2015
- **Última entrega:** `v-2026-10-28.0` del 28 de octubre de 2026 · 0 adjuntos
- **Plataformas que menciona su README:** Web
- **Medido:** 2026-11-05 11:43 UTC

## Cómo se consigue

- Installation in a production environment may be different.
- In order to work with Spark, you'll have to setup the Spark development environment.
- pip install -r requirements.txt

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/metabrainz/listenbrainz-server
- su web: https://listenbrainz.org/
- la última entrega: https://github.com/metabrainz/listenbrainz-server/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Servidor del proyecto ListenBrainz: guarda el historial de lo que escuchas y lo convierte en estadísticas e
recomendaciones, con los datos publicados en abierto. Aquí está el código del servidor, no una aplicación
para el usuario.

### Cómo se usa

1. Para usarlo, lo normal es **no instalarlo**: el proyecto ofrece su instancia pública y basta con conectar
   un programa que envíe lo escuchado.
2. Para montarlo, se despliega con contenedores y una base de datos; la entrega medida es la
   `v-2026-10-28.0`, del 28 de octubre de 2026.
3. Una vez arriba, los clientes se conectan con un testigo de usuario y le envían cada escucha.

### Lo que conviene saber antes

1.052 estrellas y GPL-2.0. Es infraestructura, no aplicación: pesa, necesita base de datos y su instalación
es un trabajo de administración. Su valor es el contrario del de los servicios comerciales: los datos son
tuyos y además se publican para que cualquiera los analice.

### Cuándo no vale la pena

Montarlo por gusto, casi nunca: para llevar tus propias estadísticas basta la instancia pública. Se justifica
si quieres los datos en casa o si investigas con ellos.

<!-- GUIA:FIN -->
