# REGISTRO DE PROMPTS · declaración de uso de IA

Adjunto obligatorio para la propuesta de NLnet (su política de IA exige entregar los prompts cuando
se usa asistencia generativa). Aquí está el registro de forma honesta y resumida: **las instrucciones
del dueño, palabra por palabra**, y **qué hizo el asistente con cada una**.

Herramienta: asistente de Arena.ai (Agent Mode, que enruta entre varios modelos: Claude, GPT, Gemini
y otros). Uso: escribir código, ejecutar mediciones, redactar borradores y revisar. Lo que **no** hizo:
decidir qué se recomienda, firmar, ni publicar nada sin orden explícita.

---

## 1. Instrucciones del dueño (verbatim, en español)

**a) Orden de trabajo inicial y estándar de entrega**
> «Buenas noches, bendiciones. Por favor, continúe con la investigación y exploración a profundidad
> hasta lograr formular una propuesta a nivel experto empresarial.»

Con cuatro requisitos: analizar todos los archivos del repositorio, leer la estructura técnica,
evaluar servicios MCP oficiales y explorar fuentes abiertas legítimas «con innovación real, no con
repetición genérica», sin falsos positivos y con total transparencia.

**b) Presentación**
> «me gustaría empaquetar la propuesta con un diseño web moderno en HTML, tomando como referencia
> estética la página de presentación de MOS Premium V7/V15 de Magisk Module.»

**c) Continuidad**
> «procede hasta terminar cada pendiente»
> «Procede hasta terminar cada pendiente y corregir cada error hasta ahora ademas no olvides revisar
> la fecha a dia de hoy y descubrimiento de nuevos recursos como https://github.com/krishna3163/OmniShizuku
> y https://github.com/krishna3163/best_shizuku_apps_for_android_no_root»

**d) Decisiones finales (31-oct-2026)**
> «La primera la decides tu … es un proyecto personal … si lo publicamos principalmente en whatsapp
> elige la mejor [in]teligencia disponible para este caso y no acepto dinero si publica el MCP y la 7
> lo presentó yo … autorizó la 8 y te concedo los permisos … no revocare al pat hasta finalizar todo»

**e) Reglas permanentes que el dueño dictó para el proyecto**
- «Sin moderte a ti misma ni rasguñarte»: admitir errores con hechos, sin teatro.
- «Bit a bit y continuidad»: seguir hasta que no quede un bit dañado ni un pendiente vivo.
- «Cero falsos positivos»: ningún «arreglado» sin prueba ejecutada.
- «Nada de declarar sano lo no medido.»

## 2. Qué produjo el asistente, tarea por tarea

| Tarea | Qué hizo el asistente | Verificación humana o automática |
|---|---|---|
| Lectura del repositorio | clonó, contó archivos y palabras, leyó el canon y las herramientas | cifras reproducibles con `find`, `du`, `wc` |
| Medición del ecosistema | escribió `tools/pulso.py` y midió 6.826 repositorios | cada ficha guarda el payload de la API y su SHA-256 |
| Registro y esquema | escribió `schemas/ficha.schema.json` y `tools/registro_construir.py` | validador JSON Schema en CI, 6.826 fichas |
| Compuertas | escribió `tools/vara.py` y `tools/autoprueba.py` | 8/8 violaciones sintéticas detectadas |
| Servidor MCP | escribió `mcp-labandita-registro/servidor.py` | probado con el cliente oficial del SDK |
| Propuesta y documentos | redactó borradores en español e inglés | el dueño decide qué se publica y con qué voz |
| Errata | redactó las correcciones con el error original a la vista | las cifras se re-midieron antes de publicarlas |

## 3. Los errores del asistente que quedaron publicados

Se listan porque la propuesta afirma que el proyecto enseña sus fallos; ocultarlos sería incoherente.

1. **Censo mal contado:** el asistente reportó 573 repositorios cuando había 5.684, por un error de
   lectura del CSV (dos comillas sueltas). Publicado y corregido en `docs/ERRATA-2026-10-31.md`.
2. **Afirmación sin medir:** dijo que una pieza en portugués tenía texto corrupto (mojibake); la
   medición posterior mostró 0 casos en 2.284 archivos. Retirado con errata.
3. **Fecha en UTC:** fechó documentos el 1 de noviembre cuando en Santo Domingo era 31 de octubre.
   Corregido con una única fuente de fecha (`tools/fecha_casa.py`).
4. **Plazo mal leído:** afirmó que la convocatoria de NLnet había cerrado cuando cerraba tres días
   después. Corregido en la matriz de pendientes.

## 4. Límites declarados

- El asistente **no** puede verificar por sí mismo que una app sea segura: solo mide lo que una API
  pública declara, y lo fecha.
- El asistente **no** firma la licencia, ni la propuesta, ni las recomendaciones. La firma es del
  dueño y así consta en `NOTICE`.
- Las decisiones editoriales —qué se publica, qué se retira, qué se recomienda— son humanas. El
  asistente propone y mide; el dueño decide.

---

*Registro generado el 31 de octubre de 2026, hora de Santo Domingo, a partir de la conversación real
de trabajo. No se incluyen datos personales ni credenciales.*
