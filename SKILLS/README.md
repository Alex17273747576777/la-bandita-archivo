# SKILLS · las diecinueve habilidades de La Bandita

*Sistema unificado. Sustituye a `SKILLS/` (7 habilidades) y a `Arena-Reimagined/HABILIDADES/` (7 más), que tenían capacidades distintas y ninguna completa. Última revisión: 9 de noviembre de 2026.*

---

## Cómo se lee esto

Cada carpeta es **una habilidad autónoma**: se puede leer sola, sin haber leído el resto del
repositorio. Todas siguen el mismo contrato:

```
---
name: <slug igual al nombre de la carpeta>
version: <semver>
dominio: <cimiento | medición | redacción | control de calidad | publicación | app>
nivel: <puerta | medidor>
cuando: <el disparador, en una línea>
entradas / salidas / herramientas / verificacion / depende_de
---
```

Y después, cinco epígrafes fijos: **Propósito · Cuándo se usa · Pasos · Reglas duras · Verificación**
(más *Errores conocidos* cuando los hay).

**Puerta contra medidor.** Una puerta que falla detiene la línea. Un medidor que sube se informa y se
sigue: publica su cifra, no bloquea. Confundir los dos es lo que hace que un proyecto se pase tres
días discutiendo un cero que era correcto.

---

## Las diecinueve

### Cimiento — cómo se empieza y cómo se aprende
| # | Habilidad | Qué hace | Nivel |
|---|---|---|---|
| 1 | [`arranque-de-suelo`](arranque-de-suelo/SKILL.md) | sabe en qué estado está el repositorio antes de tocar nada | puerta |
| 2 | [`fusionar-subsistemas`](fusionar-subsistemas/SKILL.md) | une dos sistemas sin perder la capacidad que solo tenía uno | puerta |
| 3 | [`corregir-a-la-vista`](corregir-a-la-vista/SKILL.md) | convierte cada fallo en una regla y arregla la herramienta | puerta |

### Medición — de un nombre a un dato publicable
| # | Habilidad | Qué hace | Nivel |
|---|---|---|---|
| 4 | [`medir-recurso`](medir-recurso/SKILL.md) | repositorio → estrellas, licencia, actividad, sumas, **fechado** | medidor |
| 5 | [`medir-hecho`](medir-hecho/SKILL.md) | fechas, dominios, obras, cronologías y hashes, cada tema por su vía | medidor |
| 6 | [`censo-de-pieza`](censo-de-pieza/SKILL.md) | recorta el universo al tema y deja las cifras madre en un JSON | medidor |
| 7 | [`descubrir-recursos`](descubrir-recursos/SKILL.md) | busca lo que no está medido, sin confundir «no lo tengo» con «no existe» | medidor |

### Redacción — la voz es de una persona, las cifras son del JSON
| # | Habilidad | Qué hace | Nivel |
|---|---|---|---|
| 8 | [`escribir-pieza`](escribir-pieza/SKILL.md) | alma + marcas + motor: la pieza nace dentro de banda | medidor |

### Control de calidad — lo que decide si algo sale
| # | Habilidad | Qué hace | Nivel |
|---|---|---|---|
| 9 | [`cotejar-cifras`](cotejar-cifras/SKILL.md) | cada número existe en el archivo del que dice salir | puerta |
| 10 | [`compuerta-manual`](compuerta-manual/SKILL.md) | el manual de estilo como criterios con cita, no como gusto | puerta |
| 11 | [`verificar-17-veces`](verificar-17-veces/SKILL.md) | diecisiete vías distintas, no el mismo comando diecisiete veces | puerta |
| 12 | [`informe-al-dueno`](informe-al-dueno/SKILL.md) | cifras del medidor, fallos propios y el pendiente exacto | medidor |

### Publicación — que salga y que se pueda comprobar
| # | Habilidad | Qué hace | Nivel |
|---|---|---|---|
| 13 | [`envio-canal`](envio-canal/SKILL.md) | cuerpo + fijado + bandas + LEEME, todo cuadrando | medidor |
| 14 | [`sellar-y-publicar`](sellar-y-publicar/SKILL.md) | commit y push al cerrar cada bloque, con testigo | puerta |
| 15 | [`publicar-fuera`](publicar-fuera/SKILL.md) | lleva el hallazgo al proyecto ajeno con la medición delante | medidor |

### App — el otro oficio
| # | Habilidad | Qué hace | Nivel |
|---|---|---|---|
| 16 | [`compatibilidad-multiplataforma`](compatibilidad-multiplataforma/SKILL.md) | compila y arranca en cada plataforma que declara | puerta |
| 17 | [`construir-y-entregar-apk`](construir-y-entregar-apk/SKILL.md) | el archivo que baja el usuario es el que se compiló | puerta |
| 18 | [`traducir-multilingue`](traducir-multilingue/SKILL.md) | un idioma nuevo no deja huecos silenciosos | medidor |
| 19 | [`medir-en-dispositivo`](medir-en-dispositivo/SKILL.md) | distingue compila / arranca / funciona de verdad | medidor |

---

## Cómo se encadenan

```
arranque-de-suelo
      │
      ├── medir-recurso ──┐
      ├── medir-hecho ────┴── censo-de-pieza ── escribir-pieza ── cotejar-cifras
      └── descubrir-recursos                                          │
                                                                 compuerta-manual
                                                                      │
                                                              verificar-17-veces
                                                                      │
                                                         envio-canal ── sellar-y-publicar
                                                                      │
                                                              informe-al-dueno
                                                                      │
                                                          corregir-a-la-vista
                                                            └── (vuelve a empezar)
```

El camino de la app es paralelo y se une en `sellar-y-publicar`:

```
compatibilidad-multiplataforma → construir-y-entregar-apk → medir-en-dispositivo
                            └── traducir-multilingue
```

**Una habilidad nunca hace el trabajo de la siguiente.** `escribir-pieza` no genera envíos,
`envio-canal` no sella y `sellar-y-publicar` no escribe texto. Si una habilidad necesita algo que no
tiene, **para y lo dice**.

---

## Lo que se fusionó y de dónde vino

| Habilidad nueva | Venía de |
|---|---|
| `arranque-de-suelo` | HABILIDADES/ *Arranque de suelo firme* + *Verificación multinivel* + SKILLS/README |
| `medir-recurso` | SKILLS/ `medir-recurso` + HABILIDADES/ *Pulso de repos* + *Licencias sin inventar* |
| `medir-hecho` | **nueva** — la lección de las piezas 35–40 |
| `censo-de-pieza` | SKILLS/ `censo-de-pieza` |
| `escribir-pieza` | SKILLS/ `escribir-pieza` + HABILIDADES/ *Pieza editorial* + *Formato respirable* |
| `cotejar-cifras` | **nueva** — la lección de las siete rondas de detector equivocado |
| `compuerta-manual` | SKILLS/ `compuerta-manual` |
| `verificar-17-veces` | **nueva** — la regla del dueño del 9-nov |
| `descubrir-recursos` | HABILIDADES/ *Pulso* + la lección de FMHY/Miyomi |
| `envio-canal` | SKILLS/ `envio-canal` |
| `sellar-y-publicar` | SKILLS/ `sellar-y-publicar` + HABILIDADES/ *Guardado en GitHub* |
| `informe-al-dueno` | SKILLS/ `informe-al-dueño` |
| `publicar-fuera` | **nueva** — los issues de FMHY |
| `fusionar-subsistemas` | **nueva** — esta misma fusión |
| `corregir-a-la-vista` | HABILIDADES/ bitácora de lecciones + `aprender.py` |
| Las cuatro de app | **nuevas** — salieron del trabajo del APK y de la lección 519→0 |

---

## Cómo se ejecuta esto

El catálogo **se lee del disco**, no de una lista clavada en el código:

```
python3 tools/skill_framework.py listar          # las 19, con su nivel y su dependencia
python3 tools/skill_framework.py documentar <slug>
python3 tools/skill_framework.py ejecutar <slug> [--piezas 01 02]
```

- Si la habilidad declara una herramienta (`tools/*.py` en su frontmatter), el framework **la llama**.
- Si no, se ejecuta como **procedimiento**: devuelve sus pasos y sus reglas. No se inventa un
  comportamiento que nadie escribió.

---

## Las reglas que mandan sobre todas

1. **Un verde solo vale si se midió contra algo real.**
2. **Nada de relleno**: si un dato no se midió, se escribe «aquí no hay».
3. **Se arregla el detector, nunca se baja el listón.**
4. **Corregir hacia adelante, no reescribir en silencio.**
5. **Commit y push al cerrar cada bloque.** No se espera a que lo pidan.
6. **No se declara verificado en dispositivo** lo que se midió en otro sitio.
7. **Prohibido almacenar recursos en el almacenamiento interno; única excepción: los tokens.**
8. **Español dominicano solo en las publicaciones.** Las apps son multilingües.
9. **Nada sale del dispositivo sin consentimiento o llave del usuario**, y eso se dice en la app.
10. **Los fallos propios se cuentan con el mismo detalle que los hallazgos.**

---

*Ver [`LECCIONES.md`](LECCIONES.md) para los fallos que produjeron estas reglas, uno por uno, con su
fecha y su número. Y [`DEPRECADOS.md`](DEPRECADOS.md) para saber a dónde fue cada archivo del sistema
anterior.*
