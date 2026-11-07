# Acta de etiquetas estratégicas · 4 de noviembre de 2026

**Lo que pasó:** las piezas 01, 02, 03 y 04 de Facebook se publicaron **sin una sola etiqueta**. El dueño lo
detectó y lo dijo así: «los #pings son esenciales en redes como Facebook y deben ser 100 % específicos, no
genéricos». Tenía razón y el fallo es de esta casa: se midió todo y no se puso la puerta de entrada.

## 1 · Qué se hizo

| Paso | Qué | Dónde |
|---|---|---|
| 1 | Política escrita, con lista negra y ocho reglas | `docs/POLITICA-ETIQUETAS.md` |
| 2 | Compuerta nueva **M29** (bloque, 8–12, sin genéricas, sin tildes, ganadas en el texto) | `tools/manual_gate.py` |
| 3 | Etiquetas en las seis piezas de Facebook, sacadas de su propio contenido | `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/` |
| 4 | Las etiquetas viajan en el **último mensaje** del envío, no enterradas | `tools/envio.py` |

## 2 · Las etiquetas, pieza por pieza

- **01 · El turno de los que nacieron este trimestre** (12): #Hush #MineApp #ShizukuSam #Earshot #SandFly #Latch
  #8bercue #OmniShizuku #Droynis #RedirectGuard #WPAForge #O3Root
- **02 · La música que no se cae** (12): #SaltPlayer #Namida #ArchiveTune #SimpMusic #Metrolist #AntennaPod
  #SplitAudio #DualAudio #BudsFirst #AudioScope #RootlessJamesDSP #Shizuku
- **03 · La caja fuerte del bolsillo** (12): #Monica #Keyguard #AegisAuthenticator #Stratum #KeePassDX
  #KeePass2Android #Bitwarden #FreeOTP #andOTP #Authorizer #OpenKeychain #AuthPass
- **04 · La lista del permiso** (12): #Shizuku #ShizukuNext #Porter #Droynis #OmniShizuku #GhostMode #Aura #Canta
  #Dhizuku #Shevery #Nightzuku #ShizukuPlus
- **05 · La guía maestra** (12): #Kodi #NetGuard #AuroraStore #PermissionManagerX #TrackerControl #Scrcpy
  #Obtainium #LocalSend #Immich #AntennaPod #Hail #Canta
- **06 · El taller** (10): #UniversalPatchManager #PatchBundleRegistry #MorpheManager #MorphePatches
  #UniversalInstaller #ReVanced #ReVancedManager #Shizuku #Morphe #Bundle

Regla 7 aplicada: 01 y 04 comparten dos (#OmniShizuku, #Droynis), que es el máximo permitido y está justificado
porque la 04 vuelve a medirlos. 02 y 05 comparten dos (#AntennaPod, #Shizuku). Ninguna pareja pasa de ahí.

## 3 · Fallos propios de esta pasada

1. **M11 en rojo en la 04** al añadir el bloque (45.101): se recortaron dos párrafos de método sin perder datos
   hasta 44.957.
2. **El primer arreglo de `envio.py` se comió la última nota al pie y los tres #task de cada pieza**, porque el
   bloque de etiquetas compartía párrafo final con ellos. Lo cazó el propio verificador de envíos («10 líneas del
   cuerpo no llegaron al envío») y se corrigió recortando solo el bloque, no la parte entera.
3. **Casi dejo CI en rojo por alcance**: M29 se aplica por ahora **solo a Facebook**. La banda de WhatsApp
   (63.000–63.099) está tan justa que añadir 250 caracteres obliga a recortar otros tantos: eso es una pasada
   aparte, declarada en `docs/PENDIENTES.md`, no un descuido escondido.

## 4 · Lo que sigue

La pasada de WhatsApp: cinco piezas, banda de 63.000 a 63.099, hay que recortar para hacer sitio a las etiquetas
sin romper la banda. Va después de la 06 de Facebook.
