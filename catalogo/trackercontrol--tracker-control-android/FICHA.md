# tracker-control-android · TrackerControl

*TrackerControl Android: monitor and control trackers and ads.*

**Racimo:** reemplazo-del-stack · **Repositorio:** `TrackerControl/tracker-control-android` · **Estado:** vivo · **Medido:** 2026-11-05 11:42 UTC

## Qué es, según quien lo hace

> TrackerControl is an Android app that monitors and controls the widespread, hidden data collection in mobile apps about user behaviour ('tracking'). It uses Android's VPN functionality to analyse network traffic locally on the device — no root, no external VPN server by default, and no personal data leaves the device. TrackerControl also protects against DNS cloaking, a popular technique used to h

*Es lo que declara su README. No es una verificación: está aquí porque es lo que el autor dice de su propio programa, y eso también se mide con la fecha delante.*

## Lo que se midió

- **Estado:** vivo · último empujón el 2 de noviembre de 2026 (hace 3 días)
- **Estrellas:** 2.723 · 141 bifurcaciones · 6 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Java · creado el 10 de noviembre de 2019
- **Última entrega:** `2026110101` del 1 de noviembre de 2026 · 3 adjuntos
- **Plataformas que menciona su README:** Android, iOS, Web
- **Lo que dice su propio texto:** pide root
- **Medido:** 2026-11-05 11:42 UTC

## Cómo se consigue

- Download / Installation
- height="80">](https://github.com/TrackerControl/tracker-control-android/releases/latest/download/TrackerControl-githubRelease-latest.apk)
- | **Default for new installs** | Yes | No | No |
- ./scripts/setup_rust_android.sh

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/TrackerControl/tracker-control-android
- su web: https://trackercontrol.org/
- la última entrega: https://github.com/TrackerControl/tracker-control-android/releases/latest

---

## Guía

<!-- GUIA:INICIO -->

### Para qué sirve

Mide y corta los rastreadores que llevan dentro las aplicaciones de Android. Usa la red privada local
—una VPN que corre en el propio teléfono— para ver a qué servidores llama cada app, y deja bloquear por
aplicación o por rastreador.

### Cómo se usa

1. Se instala la APK de su última entrega (`2026110101`, del 1 de noviembre de 2026).
2. Se concede el permiso de VPN local cuando lo pida; no hay que contratar nada.
3. En la lista de aplicaciones se ve cuántos rastreadores tiene cada una, quién los firma y qué dominios
   toca; se bloquea con un interruptor.
4. Con root se puede además bloquear a nivel de sistema, pero **no es necesario**.

### Lo que conviene saber antes

Solo puede vigilar una VPN a la vez: si usas otra, la sustituye. Y no es un antivirus: ve conexiones, no
intenciones.

<!-- GUIA:FIN -->
