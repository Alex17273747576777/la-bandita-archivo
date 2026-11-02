---
name: sellar-y-publicar
version: 1.0.1
dominio: publicación
cuando: con las piezas verdes y los envíos generados
entradas: [árbol limpio, lote cerrado]
salidas: [acta de conformidad, sello SHA-256 encadenado, commit, CI en verde]
herramientas: [tools/acta_conformidad.py, tools/atestar.py, tools/vara.py, git, GitHub Actions]
verificacion: [vara fallos NINGUNO, sello nuevo declarado, CI success]
---

# Skill · sellar y publicar

## Propósito
Dejar el lote en un estado que un tercero pueda verificar: acta escrita, sello calculado, historial
en el remoto y CI en verde.

## Pasos (en este orden, sin saltos)
1. `python3 tools/acta_conformidad.py` → escribe `docs/CONFORMIDAD-MANUAL-AAAA-MM-DD.md`.
2. `python3 tools/atestar.py` → sello SHA-256 encadenado en `attestations/`; anota el **anterior** y
   el **nuevo** para el reporte.
3. `python3 tools/vara.py` → debe terminar en `fallos: NINGUNO`. Si G5 canta, es que falta el paso 2.
4. `git add -A && git commit -m "<canal> · <qué> · <cifras>"` y `git push origin main` con `GHP_A`.
5. Esperar el run de CI y **confirmar `success`** antes de decir «publicado».
6. Copiar la entrega a la carpeta de piezas del día (fuera del repo) si el dueño la quiere a mano.

## Reglas duras
- **Nada se declara publicado sin corrida.** Ni «debería pasar», ni «seguro que va».
- Un push doble cancela el CI: un push, una espera.
- El sello se re-genera **después** del acta, nunca antes.
- El token no se imprime ni se versiona; si aparece en un `git status`, se rota.

## Verificación
`vara.py` sin fallos · CI `success` en el SHA empujado · sello nuevo citado con su huella corta.
