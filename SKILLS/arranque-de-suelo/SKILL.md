---
name: arranque-de-suelo
version: 2.0.0
dominio: cimiento
nivel: puerta
cuando: al empezar cualquier sesión, antes de afirmar nada sobre el estado del repositorio
entradas: [repositorio, manifiesto de hashes si existe]
salidas: [inventario del árbol, hashes verificados, lista de desviaciones, decisión de restaurar]
herramientas: [tools/arranque.py, tools/chequeo-niveles.py, git status, git rev-list]
verificacion: [0 archivos sin dueño, 0 commits sin subir, .git/config intacto]
depende_de: []
---

# Habilidad · arranque de suelo

## Propósito
Saber en qué estado está el repositorio **antes** de tocar nada, y decirlo con números en vez de
suponerlo. Una sesión que empieza sin inventario termina afirmando cosas sobre un suelo que no miró.

## Cuándo se usa
- Al abrir la sesión.
- Antes de un `commit` que se va a declarar completo.
- Cuando algo «no cuadra» y no se sabe si el fallo es del código o del suelo.

**No se usa** para arreglar: mide y decide. Restaurar es otro paso y se hace con el manifiesto.

## Pasos
1. `git status --porcelain` y contar. Archivos sin dueño ≠ archivos modificados a propósito.
2. `git rev-list --count origin/main..HEAD` — commits hechos y no subidos.
3. `find . -name __pycache__ -prune -exec rm -rf {} +` y cualquier caché: no se versiona basura.
4. Comparar contra el manifiesto si existe (`tools/arranque.py`). Donde no haya manifiesto, dejar
   constancia de que no se puede verificar por hash y decirlo.
5. Escribir las tres cifras: **sin dueño · sin subir · desviaciones**. Con eso ya se puede trabajar.

## Reglas duras
- **Nunca decir «está todo bien» sin haber corrido los tres comandos.** El estado se mide.
- **Lo que está sin subir no se declara terminado**, aunque el archivo esté escrito.
- **Un archivo sin dueño es una pregunta**, no un estorbo: o se versiona o se borra, pero se decide.
- **No se borra evidencia para dejar el árbol limpio.** Lo que se borra son cachés, no historia.

## Verificación
- Las tres cifras se pueden repetir y dan lo mismo.
- Si hay desviaciones, están listadas una por una con su ruta.

## Errores conocidos
- Dar por limpio un árbol porque `git status` no muestra nada: los archivos ignorados por
  `.gitignore` también cuentan cuando el entregable los necesita (p. ej. un APK).
- Empezar a trabajar con 20 commits sin subir y descubrirlo al final.
