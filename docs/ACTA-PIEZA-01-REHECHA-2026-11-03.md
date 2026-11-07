# Acta de la pieza 01 rehecha · Facebook · 3 de noviembre de 2026

**Pieza:** `01-El-turno-de-los-que-nacieron-este-trimestre-doce-apps-de-octubre-que-casi-nadie-conoce-y-dos-que-no-aguantan-Facebook-La-Bandita-2026-11-03-dominicano-ES.md`
**Caracteres:** 43.593 (banda Facebook 40.000–45.000)
**Reemplaza a:** `01-El-turno-de-los-que-nacieron-este-trimestre-doce-proyectos-medidos-hoy-y-uno-que-no-aguanta-el-escrutinio-Facebook-La-Bandita-2026-11-03-dominicano-ES.md`, movida a `_ARCHIVO-HISTORICO/_reemplazadas-2026-11-03/` con `git mv` (no se borra: se conserva con su fecha).
**Motivo:** el dueño ordenó el 3-nov-2026 reescribir de raíz las piezas 01–06 de Facebook con medición nueva, y fijó una regla editorial que manda sobre las demás: **enfocarse en lo más nuevo, actualizado, recién lanzado y desconocido**.

## 1 · Lo que cambió, en una tabla

| Antes | Ahora |
|---|---|
| doce proyectos elegidos a mano entre los famosos del trimestre | doce elegidos por el selector de novedad: todos nacidos en octubre de 2026, ninguno pasa de ★132 |
| sin herramienta de descubrimiento | `tools/novedad.py`, que clasifica las 6.838 fichas y ordena por juventud × actividad |
| sin cifras del trimestre entero | 852 fichas nacidas en 90 días, 87 % por debajo de 100★, 29 % sin licencia declarada |
| un rechazo | dos rechazos razonados: WPAForge (rompe contraseñas de wifi sin poder verificar propiedad) y O3 Root (explota CVE-2026-98260 abierta) |
| sin método de adopción | la prueba de una semana, cinco días con su criterio |

## 2 · Qué se midió y con qué

| Cosa | Cómo | Resultado |
|---|---|---|
| Los doce candidatos | `GET /repos`, `/releases?per_page=3`, `/languages`, `/readme` | estrellas, nacimiento, empujón, entrega, licencia, tamaño y presentación leída |
| Los dos rechazados | las mismas cuatro puertas | WPAForge ★150 · 10-oct · Apache-2.0 · v1.9.40 · O3 Root ★31 · 25-oct · MIT · v3.3.3-o1-test |
| El trimestre entero | las 6.838 fichas + su evidencia sellada (`created_at`) | 852 nacidas ≤90 d · 743 con ≤100★ · 250 sin licencia · 411 con entrega ≤30 d |
| El selector | `tools/novedad.py --nacidos 90 --min-calidad 0.85` | 90 candidatos con señal alta, de ahí salieron los doce |

## 3 · Compuertas

| Compuerta | Resultado |
|---|---|
| `manual_gate --pieza` | **VERDE** (M01–M23; M11 43.593 en banda) |
| `novedad_gate --corte 2026-11-03` | **VERDE** (M24 doce fichas por debajo de ★500 · M25 «madurez» declarada en cada ficha y en la tabla · M27 sin meta-comentarios · M28 #task 001–003) |
| `firma_literal` | en regla, con bloque `Medición del corte:` y hora |

## 4 · Corrección propia, declarada

Al preparar la lista supuse que `btsearch/bunnylock` era un troyano por la sigla «RAT» de su descripción. Al abrir su presentación resultó ser un control de módem —bandas, *radio access technology* y bloqueo de celda—. No entró en la lista por falta de señales suficientes, no por lo que su nombre sugería. La corrección queda escrita en la pieza y en su nota al pie, porque el método de esta casa incluye equivocarse en voz alta.

## 5 · Lo que se declara como hueco

- **No hay columna de descargas**: el contador de GitHub mezcla proyectos desconocidos con proyectos que se instalan por otra vía. Se declara el hueco en el texto.
- **Ninguno de los doce tiene prueba de terceros**: todos son de octubre. La pieza lo dice y convierte la advertencia en método (la prueba de una semana).
- **Las presentaciones en chino no se tradujeron**: se declara en qué idioma está cada una, porque es lo que decide si sirve a este público.
