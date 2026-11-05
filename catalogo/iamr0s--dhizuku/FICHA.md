# Dhizuku · iamr0s

*A tool that can share DeviceOwner permissions to other application.*

**Racimo:** shizuku-y-herederos · **Repositorio:** `iamr0s/Dhizuku` · **Estado:** vivo · **Medido:** 2026-11-05 11:40 UTC

## Qué es, según quien lo hace

Su README no tiene un párrafo en prosa que se pueda citar: o es una lista de escudos, o son capturas, o no hay README. Se deja dicho en vez de rellenarlo.

## Lo que se midió

- **Estado:** vivo · último empujón el 3 de noviembre de 2026 (hace 2 días)
- **Estrellas:** 4.088 · 132 bifurcaciones · 3 incidencias abiertas
- **Licencia:** GPL-3.0
- **Lenguaje:** Kotlin · creado el 10 de abril de 2023
- **Última entrega:** `v2.13.0` del 30 de octubre de 2026 · 3 adjuntos
- **Medido:** 2026-11-05 11:40 UTC

## Cómo se consigue

Su README no dice cómo se instala en las primeras líneas. Se mira en la entrega.

## Qué no está verificado

Que funcione. Se mide el repositorio; no se ha instalado ni usado.

## Enlaces

- repositorio: https://github.com/iamr0s/Dhizuku
- la última entrega: https://github.com/iamr0s/Dhizuku/releases/latest

---

## Guía

<!-- GUIA:INICIO -->
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
<!-- GUIA:FIN -->
