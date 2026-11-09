---
name: sellar-y-publicar
version: 2.0.0
dominio: publicación
nivel: puerta
cuando: al cerrar un bloque de trabajo, siempre, sin que nadie lo pida
entradas: [cambio terminado y verificado]
salidas: [commit con mensaje que dice qué se midió, push, testigo de que subió]
herramientas: [git, tools/atestar.py, tools/swhid.py, gh api]
verificacion: [0 commits sin subir, 0 archivos sin dueño, atestación con huella]
depende_de: [envio-canal]
---

# Habilidad · sellar y publicar

## Propósito
Cerrar el bloque con **commit y push**, con un mensaje que diga lo que se midió y lo que se corrigió,
y con un testigo de que el remoto lo tiene. La regla de la casa es permanente: no se espera a que lo
pidan.

## Cuándo se usa
- Al terminar cada bloque de tareas, aunque sea pequeño.
- Nunca «al final de todo»: los bloques se suben uno por uno.

## Pasos
1. `python3 tools/atestar.py` — huella del árbol.
2. Mensaje en un archivo y `git commit -F <archivo>`. **Nunca heredoc con `$`**: el shell lo expande.
3. `git push origin main`.
4. `git rev-list --count origin/main..HEAD` debe dar **0**.
5. Si el bloque tocó el issue de otro proyecto, comentarlo allí y guardar el enlace.

## Reglas duras
- **Sin push no hay bloque terminado.**
- **El mensaje dice qué se corrigió y por qué**, no «varios cambios».
- **No hacer tandas locales largas.** Bloque terminado, bloque subido.
- **Si un push falla, no se reintenta a ciegas**: se lee el error y se arregla la causa.

## Verificación
- Cero commits sin subir.
- `git log --oneline -1` con el mensaje del bloque.
- La atestación tiene huella distinta de la anterior.

## Errores conocidos
- `git commit -m` con heredoc y `$` dentro: el mensaje se corrompe en silencio.
- Declarar «subido» sin comprobar `rev-list`.
