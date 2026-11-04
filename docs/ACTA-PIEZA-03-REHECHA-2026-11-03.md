# Acta de la pieza 03 rehecha · Facebook · 3 de noviembre de 2026

**Pieza:** `03-La-caja-fuerte-del-bolsillo-un-gestor-archivado-con-mil-seiscientos-tres-dias-de-silencio-y-tres-llaves-que-no-dejan-salir-Facebook-La-Bandita-2026-11-03-dominicano-ES.md`
**Caracteres:** 41.714 (banda Facebook 40.000–45.000)
**Reemplaza a:** `03-La-caja-fuerte-del-bolsillo-un-autenticador-muerto-mil-seiscientos-dos-dias-de-silencio-y-la-copia-que-salva-Facebook-La-Bandita-2026-11-02-dominicano-ES.md`, movida con `git mv` a `_ARCHIVO-HISTORICO/_reemplazadas-2026-11-03/`.
**Regla aplicada:** lo más nuevo, recién publicado y desconocido primero (orden del dueño, 4-nov-2026), sin dejar de medir el catálogo vivo.

## 1 · El hallazgo que cambió la pieza

La pieza vieja contaba un autenticador muerto. Al medir el dominio completo (doce programas, uno por uno, con
su archivo de licencia abierto) aparece algo más incómodo y más útil: **el programa más completo del tema se
reserva todos los derechos**. El `LICENSE` de `AChep/keyguard-app` dice, en su primera línea y en toda su
extensión, `All Rights Reserved`, y junto a él hay un `SAPCLA.md` que cede al autor los derechos de cualquier
contribución. No es software libre aunque su código esté a la vista.

Eso convirtió la pieza en un texto sobre **puertas de salida**, no sobre funciones: qué formato escribe cada
programa, qué licencia lo protege y qué pasa el día que su autor se cansa.

## 2 · Qué se midió y con qué

| Cosa | Cómo | Resultado |
|---|---|---|
| Los doce programas | `GET /repos` + `/releases/latest` + `/license` + lectura del `LICENSE` y del `SAPCLA.md` donde había duda | estrella, nacimiento, empujón, licencia, última entrega y días al corte |
| Keyguard | `raw.githubusercontent.com/.../LICENSE` y `/SAPCLA.md` | **`All Rights Reserved`** + cesión de derechos al autor |
| Monica | `/repos` + `/releases?per_page=100` | nace 5-oct-2025 · 93 entregas · 16.678 descargas · GPL-3.0 |
| andOTP | `/repos` (archivado) | push 14-jun-2022 (**1.603 d**) · entrega jun-2021 (**1.967 d**) · MIT |
| AuthPass | `/repos` + `/releases/latest` | push hace 49 d pero **entrega de 4-feb-2024 (1.003 d)** |
| Censo del dominio | `registry/` con filtro apretado | **32 fichas** · MIT 13 · GPL-3.0 9 · sin declarar 5 · Apache 2 · MPL 1 · GPL-2.0 1 |

Nueve programas más se midieron en vivo y no están en el registro; se citan desde la medición y no se siembran
fichas nuevas en esta pasada, para no mezclar medición con alta de catálogo.

## 3 · Compuertas

| Compuerta | Resultado |
|---|---|
| `manual_gate --pieza` | **VERDE** (M11 41.714 en banda) |
| `novedad_gate --corte 2026-11-03` | **VERDE** (M24 fichas de ★ baja · M25 «madurez» en cada ficha y en la cabecera de las tablas · M28 #task 001–003) |

## 4 · Fallos propios cazados en esta pieza, y qué se hizo

1. **M05 en rojo:** «En una página» salió con seis párrafos y la vara pide tres a cinco. Se fusionaron los dos
   párrafos de Monica y Keyguard con el de la licencia, sin perder un dato. Queda en cuatro.
2. **Error de conteo propio, cazado a mano y no por compuerta:** el borrador decía que «nueve» de los doce
   escriben o leen el formato abierto KeePass. Son **cinco** (KeePassDX, keepass2android, Keyguard, AuthPass y
   Monica, que lo importa). Se corrigió el párrafo y la cifra del cierre, y se repartieron los otros siete en
   dos familias (cuatro generadores de códigos, tres casos aparte).
3. **Estrella desfasada:** Bitwarden pasó de ★9.582 a ★9.583 entre la medición de la madrugada y la del cierre.
   Se tomó la última y así queda anotado.

## 5 · Qué se corrigió de la pieza vieja

- Se sustituye el eje «un autenticador muerto» por el eje **archivo + licencia + fecha**, que es el que decide
  si mañana sigues siendo dueño de tus contraseñas.
- Se añade la sección de la mudanza en cinco pasos con la salida esperada de cada uno, que la vieja no tenía.
- Se separa explícitamente **empujar código** de **publicar entrega**: es lo que deja fuera a AuthPass pese a su
  actividad reciente, y lo que explica que FreeOTP empuje hoy con una entrega de hace 259 días.
- Se cuenta y se fecha el silencio de los cuatro parados, con el día exacto y no con un «hace tiempo».

## 6 · Lo que esta pieza no afirma

- No audita la implementación criptográfica de ningún programa; afirma formatos y licencias, que son verificables.
- No dice qué variante de KDBX usa cada uno.
- No siembra fichas nuevas en el registro: eso es otra pasada y otro asunto.
