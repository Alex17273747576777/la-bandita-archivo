# Acta del escrutinio · 3 de noviembre de 2026

**Herramienta:** `tools/escrutinio.py` · **acta en crudo:** `docs/ESCRUTINIO-2026-11-03.json`
**Medidos:** 316 repositorios acumulados · **acta que se acumula**, no se sobreescribe.

## Pesos, tal como se publican

| Señal | Peso |
|---|---|
| licencia legible en la plataforma | 15 |
| flujos de integración continua | 10 |
| adjunto con huella (SHA256SUMS, .sig, .asc) | 10 |
| entrega publicada en los últimos 30 días | 10 |
| cambios en los últimos 30 días | 10 |
| personas que han empujado código | 10 |
| proporción de incidencias cerradas | 10 |
| SECURITY.md presente | 5 |
| mérito de terceros (Scorecard de deps.dev) | 20 |
| **penalizaciones** | archivado −30 · ninguna entrega con adjuntos −10 · atención anómala −15 · una sola persona con más de 50 entregas −5 |

## El error que se encontró y se publicó el mismo día

La primera corrida pedía las entregas dentro de una consulta agrupada de veinte repositorios por llamada. Cuando el lote era grande, la interfaz devolvía **vacío** el bloque de entregas; la herramienta anotaba «ninguna entrega con adjuntos» y **restaba diez puntos a quien más publicaba**.

- **Síntoma que lo delató:** un proyecto con entrega del mismo día aparecía con cero adjuntos y sin entrega reciente.
- **Corrección:** las entregas se miden ahora por REST, un repositorio por llamada (`/repos/{o}/{r}/releases?per_page=10`), sin depender del tamaño del lote.
- **Alcance:** recalculo de las **316 fichas**. Cambiaron **132 notas**.
- **Efecto en lo publicado:** porter 65→75, Shizuku-Next 60→70, ShizukuPlus 59→69; en la pieza 01, LastWave 56→76, flectar/mail 68→78, gander 56→66, msime 65→74. Las dos piezas se corrigieron con fecha de hoy y las notas de sus tablas se reescribieron.

## Notas del corte, por pieza

**Pieza 01 · El turno (Facebook).** Doce fichas: flectar/mail 78 · LastWave 76 · msime 74 · android-ad-cleaner 71 · NOIR 71 · gander 66 · dumbtv 64 · cleanyourtv-app 63 · TwinDesk 61 · tellyscope 53 · cleanyourtv 43 · Fonte 38. Fuera, con la nota publicada: PassPonyAndroid 61 (★18), Husk 50 (corre en iOS, no dentro de Android), kiosk-satellite 40.

**Pieza 04 · El permiso prestado (Facebook).** Doce fichas: porter 75 · Shizuku-Next 70 · ShizukuPlus 69 · Inure 67 · magicdesk 65 · ShizuCallRecorder 62 · CallVault 62 · wifi-password-manager 61 · AppOpsNext 60 · aShellYou 58 · Shizako 57 · Nightzuku 55. El original, `RikkaApps/Shizuku`, 40 y sin recomendación: 503 días sin empujar. Fuera: VInstall 47, BatStats 41, Shizuku-API 15.

## Lo que la nota no mide, y se declara

- **Mérito de terceros:** ninguno de los 24 proyectos publicados está indexado en deps.dev, así que 20 de los 100 puntos quedan sin repartir en todos por igual.
- **Personas empujando:** tope de medición en 100. En los derivados incluye nombres heredados del tronco.
- **Lo que decide el editor:** el cupo y el tema. La nota ordena y castiga; no elige sola. Cada exclusión va con su razón escrita, no con un número escondido.

#task 004 · volver a correr el escrutinio el 3 de diciembre sobre los 350 del tema de la pieza 04 y publicar cuántas notas se mueven sin el error de lotes.
