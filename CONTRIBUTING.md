# CÓMO SE CONTRIBUYE

*Reglas de entrada, de revisión y de salida. Si algo de aquí no se cumple, no entra — y decirlo a tiempo es la forma más rápida de ayudar.*

**TL;DR —** un cambio entra si **mide**, **se puede repetir** y **no borra historia**. Se escribe en español, se confirma con [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), se anota en [CHANGELOG](CHANGELOG.md) y pasa `make verificar` con `fallos: NINGUNO`. No hace falta pedir permiso para corregir un error: hace falta decir cuál era.

---

## 1 · Antes de tocar nada

```bash
git clone https://github.com/Alex17273747576777/la-bandita-archivo.git
cd la-bandita-archivo
make doctor        # dice si tu máquina puede trabajar y en qué estado está el árbol
make verificar     # tarda unos minutos; si no sale en NINGUNO, no empieces
```

Si `make doctor` dice **DETENIDO**, no sigas: falta una pieza esencial, el árbol no es de git o la versión de Python es vieja. Arreglar eso es el primer trabajo.

---

## 2 · Las cuatro reglas de la casa

1. **Lo que es dato se genera; lo que es enseñanza se escribe.** No se teclea a mano una tabla de setenta filas ni se genera un párrafo que pretende enseñar.
2. **Nada se publica sin fecha y sin método.** Una afirmación sin un comando que la pueda repetir es una opinión, y las opiniones no entran en las piezas.
3. **No se borra historia.** Lo que se sustituye queda en `_reemplazadas/` con su fecha; lo que se archiva va a `_ARCHIVO-HISTORICO/<mes>/` y no se retoca.
4. **El que corrige, dice qué corrigió.** Un cambio sin su línea en `CHANGELOG.md` es un cambio que el próximo tendrá que redescubrir.

---

## 3 · Qué se puede mandar y qué no

| Sí | No |
|---|---|
| Una corrección de dato con su medición fechada al lado | Un cambio de cifra «porque parece más actual» |
| Una pieza nueva que pasa las dos compuertas | Una pieza que solo pasa la de forma |
| Una herramienta nueva con su docstring, su uso y su límite | Un script sin cabecera que explique qué no hace |
| Un enlace vivo al repositorio del autor | Un enlace a un espejo, a un APK alojado o a un agregador |
| Una errata con la línea y la corrección | Una reescritura de estilo sobre texto publicado |

**Nunca** entra una llave, un token o una ruta personal. Las llaves viven en `~/.boveda/tokens.env`, fuera del repositorio, y ninguna herramienta las escribe en el árbol. La compuerta M15 busca secretos y enlaces a paquetes de mods; si aparece uno, la línea se detiene.

---

## 4 · Cómo se escribe una confirmación

Forma: `tipo(alcance): descripción`, con cuerpo cuando haga falta y pies para lo que se pueda procesar.

```
fix(chapuza): corrige el conteo de piezas archivadas

El LEEME declaraba 135 archivos en Facebook y eran 135 piezas más dos
índices. La cifra se toma ahora del árbol y no de la memoria.

Refs: docs/ACTA-ORDEN-Y-VERIFICACION-2026-11-03.md
```

Tipos que se usan aquí: `feat` (algo nuevo), `fix` (algo roto), `docs` (documentación), `data` (mediciones y registro), `tools` (herramientas), `chore` (mantenimiento), `ci` (integración continua). El `!` o el pie `BREAKING CHANGE:` se reservan para cuando se rompe una ruta o un contrato, y en ese caso **el mapa se actualiza en el mismo cambio**.

---

## 5 · La revisión

Un cambio se revisa contra cuatro preguntas, en este orden:

1. **¿Se puede repetir?** ¿Trae el comando, la fecha y la fuente?
2. **¿Su límite está escrito?** Toda herramienta y toda ficha dicen qué no hacen.
3. **¿Rompe algo que ya se publicó?** Si toca una pieza publicada, se rechaza: se corrige en la siguiente.
4. **¿Pasa la vara?** `make verificar` en verde, con la frase `fallos: NINGUNO` en el informe.

La revisión no busca gusto: busca que otro pueda comprobar lo mismo sin preguntar.

---

## 6 · El día de una publicación

```bash
make publicar     # sella, regenera tableros, verifica
git add -A && git commit -m "feat(canal): pieza 06 de Facebook"
make push         # usa el token de la bóveda; nunca lo imprime
```

Después se comprueba que la integración continua termine en verde y que el resumen del trabajo diga el número de archivos sellados. Un empujón sin esa comprobación no está terminado: está empezado dos veces.

---

## 7 · Si encontrás un fallo

No hace falta ceremonia: abrí una incidencia con las seis líneas del parte de avería —qué programa y versión, qué aparato y sistema, qué hiciste, qué esperabas, qué pasó y el registro recortado—. Ese parte está explicado en el capítulo 11 de la guía maestra y es el mismo que la casa usa para sus propias herramientas.

Para un fallo de seguridad, el camino es otro y está en [SECURITY.md](SECURITY.md): no se publica en la lista de incidencias.

*La Bandita informa a partir de fuentes fechadas.*
