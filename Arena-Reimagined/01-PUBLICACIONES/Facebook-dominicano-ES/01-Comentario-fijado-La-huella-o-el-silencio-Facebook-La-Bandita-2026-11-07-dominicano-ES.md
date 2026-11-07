*Comentario fijado · Pieza 01 de Facebook · La Bandita · 7 de noviembre de 2026*

Resumen rápido para enlaces y contexto:

**De qué trata esta publicación:** quince programas para Android nacidos en octubre de 2026, medidos uno por uno contra la API de GitHub a las 11:45 de hoy. Seis publican una huella (SHA-256) para que compruebes que el archivo que bajas es el que subió el autor. Nueve no: te piden fe.

**Los quince fichas, con datos reales de hoy:**

1. droynis ★20 · GPL-3.0 · v0.16.0 · 1 huella de 2 archivos · nota 74 · mejor puntuado

2. ADB-Root-Toolbox ★129 · GPL-3.0 · v7.22.1 · 1 huella de 4 archivos · nota 72 · más descargas (21.929)

3. OmniShizuku ★19 · Apache-2.0 · latest (hoy) · 0 huellas de 1 archivo · nota 67

4. o3root ★91 · MIT · v3.3 · 1 huella de 2 archivos · nota 65 · subió de 33 a 91 estrellas

5. SandFly ★28 · Apache-2.0 · v0.3.1 (hoy) · 0 huellas de 2 archivos · nota 61

6. RedirectGuard ★19 · Apache-2.0 · v1.7 · 0 huellas de 2 archivos · nota 59 · cero incidencias abiertas

7. Latch ★18 · MIT · v0.6.3 · 0 huellas de 1 archivo · nota 58

8. 8bercue ★18 · AGPL-3.0 · sin release · 0 huellas de 0 archivos · nota 56

9. Hush ★151 · GPL-3.0 · v2.0.5 · 0 huellas de 1 archivo · nota 55 · más estrellas de los quince

10. earshot ★38 · MIT · v0.9.1 (hoy) · 0 huellas de 1 archivo · nota 49

11. shizuku-sam ★43 · Apache-2.0 · v13.8.40 (hoy) · 0 huellas de 1 archivo · nota 45 · más pesado (139.1 MiB)

12. APK-Toolbox ★107 · GPL-3.0 · v1.1.6 · 0 huellas de 5 archivos · nota 45 · ningún flujo de compilación

13. WPAForge ★160 · Apache-2.0 · v1.9.50 · 1 huella de 2 archivos · nota 39 · el más popular, cero flujos

14. ghost-files ★16 · MIT · v0.7.3 · 1 huella de 3 archivos · nota 44 · a un punto del corte

15. MineApp ★101 · GPL-3.0 · v3.8.5 · 0 huellas de 1 archivo · nota 35 · treinta y una entregas en diez días

**Los tres que no pasan (menos de 45 puntos):** WPAForge ★160 nota 39, ghost-files ★16 nota 44, MineApp ★101 nota 35.

**Seis órdenes para comprobar por tu cuenta:**

1. Abre la página de entregas del repositorio y busca archivos .sha256, .sha512, .asc o .sig.

2. En Termux: `pkg install coreutils && sha256sum *.apk`

3. Compara con el autor: `sha256sum -c archivo.sha256`

4. Guarda la firma: `apksigner verify --print-certs archivo.apk | grep SHA-256`

5. Pide la huella al autor en sus incidencias (plantilla incluida en la pieza).

6. Verifica atestación: `gh attestation verify archivo.apk --repo dueno/nombre`

**Dónde y cómo se usa:** cada programa se busca en su repositorio de GitHub (enlaces al final de la pieza). Ningún APK se aloja aquí. La huella se calcula en el teléfono con Termux o en la computadora con sha256sum y apksigner.

**Por qué importa:** sin huella no puedes saber si el archivo que bajaste es el que publicó el autor. Con huella, comparas sesenta y cuatro caracteres y lo sabes con certeza.

**Enlaces principales:** los quince están listados con sus URLs al final de la pieza principal.

**Hashtags:** #Droynis #ADBRootToolbox #OmniShizuku #O3Root #SandFly #RedirectGuard #Latch #8bercue #Hush #Earshot #ShizukuSam #APKToolbox #WPAForge #GhostFiles #MineApp #HuellaSHA256 #Apksigner #Fontaneria #VerificacionAndroid #GitHubAPI