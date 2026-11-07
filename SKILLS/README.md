# SKILLS · habilidades operativas

Cada carpeta es **una habilidad completa y autónoma**: se puede leer sola, sin haber leído el resto del
repositorio. Todas siguen el mismo contrato de `SKILL.md`:

```
---
name: <slug igual al nombre de la carpeta>
version: <semver>
dominio: <medición | redacción | control de calidad | publicación>
cuando: <el disparador, en una línea>
entradas / salidas / herramientas / verificacion
---
```

Después del frontmatter, cinco epígrafes fijos: **Propósito · Cuándo se usa · Pasos · Reglas duras ·
Verificación** (más *Errores conocidos* cuando los hay).

## Las siete habilidades del ciclo

| # | Habilidad | Entra | Sale |
|---|---|---|---|
| 1 | [`medir-recurso`](medir-recurso/SKILL.md) | lista de repos | dato medido tres veces, fechado |
| 2 | [`censo-de-pieza`](censo-de-pieza/SKILL.md) | medición guardada | cifras madre de la pieza |
| 3 | [`escribir-pieza`](escribir-pieza/SKILL.md) | censo + banda | pieza dentro de banda |
| 4 | [`compuerta-manual`](compuerta-manual/SKILL.md) | pieza | VERDE/ROJO por criterio |
| 5 | [`envio-canal`](envio-canal/SKILL.md) | piezas verdes | envíos por canal |
| 6 | [`sellar-y-publicar`](sellar-y-publicar/SKILL.md) | lote cerrado | acta + sello + commit + CI verde |
| 7 | [`informe-al-dueño`](informe-al-dueño/SKILL.md) | lote cerrado | informe con cifras, hora y pendiente |

## Cómo se encadenan

```
medir-recurso → censo-de-pieza → escribir-pieza → compuerta-manual → envio-canal → sellar-y-publicar
        ↑                                                                              │
        └──────────────────── error detectado (CIMIENTOS/06-PROTOCOLO-DE-ERRORES) ─────┘
```

Una habilidad nunca hace el trabajo de la siguiente: `escribir-pieza` no genera envíos, `envio-canal`
no sella y `sellar-y-publicar` no escribe texto. Si una habilidad necesita algo que no tiene, **para y
avisa**: no improvisa.

## Cómo se añade una habilidad nueva

1. Copiar la estructura de una existente; el frontmatter es obligatorio.
2. Escribirla de forma que se entienda sin contexto previo.
3. Añadirla a la tabla de arriba y al flujo si interviene en el ciclo.
4. Probarla en un lote real y anotar en *Errores conocidos* lo que salió mal la primera vez.

## Regla de oro

Una habilidad que no dice **cómo se verifica** no es una habilidad: es un consejo.
