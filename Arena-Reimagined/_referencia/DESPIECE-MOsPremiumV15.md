# DESPIECE TOTAL — MOs Premium v15 (el módulo real, no el escaparate)

Fecha: 15-oct-2026 noche · Hecho por la forja de La Bandita por orden del dueño
 («copiaste el diseño de la página, no del módulo» — corregido: aquí está el desarme del módulo).

## 1. Ficha del artefacto

| campo | valor medido |
|---|---|
| archivo | `MOsPremiumV15.zip` (bajado de magiskmodule.com, upload `pending_1789941125938`) |
| bytes | **4.694.366** · SHA-256 (16h) **`e658c88ad6429cd4`** |
| fecha interna zip | 20-sep-2026 17:40–21:31 |
| nota | la página ofrecía «v7»; el zip real de descarga es **v15** (el sitio sirve el último) |
| repo del dueño | `alexaindruews170206-dev/MOs-Premium-module-axmanager-Next` → **404 público** (API y codeload; solo Arena-Reimagined es público en su cuenta). Si el repo «Next» trae código distinto al zip, se disecta cuando haya token de nuevo o esté público |

## 2. Inventario (11 archivos, 10.715.394 b descomprimidos)

```
96.745   action.sh            ← motor shell (1.935 líneas)
   606   module.prop          ← manifiesto
34.619   banner.png
 1.077   ANDROID_RTL_FIX_GUIDE.md
1.582.523 webroot/app.js      ← UI + lógica (10.323 líneas)
8.158.563 webroot/paradise_resort.mp3  ← música incluida
 123.488 webroot/style.css    ← tokens + temas (3.782 líneas)
  23.573 webroot/snake_icon.jpg
461.910  webroot/index.html   ← esqueleto + iconos SVG a mano (2.557 líneas)
232.290  webroot/1164.png
```

## 3. module.prop (verbatim, manifiesto de hechos puros — anti-marketing)

```
id=MOsPremiumADB
name=MOs Premium v15 — Full-Stack FPS Engine
version=v15.0  versionCode=1500  author=jogominecraft1234
description=MOs v15.0 Full-Stack FPS — rootless ADB engine (Ax Manager only):
 adaptive-max refresh unlock, BBR2 67MB buffers, iowait_boost, USAP refill=2,
 swappiness=0, heap 2g Phantom, GPU freq scaling (Adreno/Mali/PowerVR/Xclipse),
 SF frame pacing 100-200us, APEX perf governor, dynamic CPU-core dex2oat,
 heavy-games auto-boost (…). Android 12-15. By Murilo.
minApi=21 maxApi=99 axeronPlugin=14000 banner=banner.png
```

## 4. action.sh — el motor (22 funciones, 9 perfiles)

- **Disciplina `safe_*`**: TODA mutación pasa por `safe_prop` / `safe_setting` / `safe_write` / `safe_write_glob` — cada una: intenta con guard (`2>/dev/null`, `-w` check), y **loguea a `engine.log`** con hora. Nada se aplica sin rastro.
- **Detección antes de aplicar**: `detect_cpu_cores`, `detect_device_tier`, `detect_soc`, `detect_android_ver`, `detect_oem`, `detect_max_refresh_rate`, `is_flagship`.
- **Perfiles** (entry point): `S25_ZALITH_ULTRA · COMPETITIVE_EXTREME · ULTRA_120 · THERMAL_BALANCED · TOUCH_BOOST · BATTERY_GAMING · LOW_END_FPS · EMULATOR_OPTIMIZED · ENHANCER` → `action.sh` (todo) o `action.sh <PERFIL>`.
- Aplicadores: `apply_fps_core`, `apply_competitive_extreme`, `apply_thermal_balanced`, `apply_touch_boost`, `apply_battery_gaming`, `apply_low_end_fps`, `apply_emulator_optimized`, `apply_heavy_games_boost`, `apply_mos_enhancer`.
- Estado persistente en `/data/local/tmp/mos/current_profile`; bucle de núcleos usa el **conteo real detectado** («NEVER force core 0 offline»).
- Comandos reales que aplica (muestra): `game_mode_config_game_default_frame_rate=$MAX_HZ`, `sf_early_phase_offset_ns 250000`, `fling_deceleration_rate 0.09`, `view_post_ime_input_delay 0`, cpu online loop.

## 5. app.js — la interface (39 funciones top-level)

- **Audio sintetizado sin assets**: `initAudio` (WebAudio con resume + catch), `playTick`, `setClickSound` — el sonido de clicks se GENERA, no se empaqueta (además trae mp3 aparte para música, volumen persistido `mosMusic_vol`).
- **Puente shell con cola**: `executeShellRaw`, `execQueue`, `_mosRunExecQ`, `runCustomCmd` — los comandos se encolan, no se lanzan en paralelo.
- **CAPA DE SEGURIDAD — `mosIsDangerousCmd` + `MOS_DANGEROUS_PATTERNS` (23 regex)**: se niega a ejecutar comandos destructivos ANTES de lanzarlos. Bloquea, entre otros: `adb_enabled 0`, `wm size/density`, `font_scale`, `reboot|shutdown`, `am kill-all`, `force-stop com.google.android.gms`, `setprop ro.*`, `pm uninstall com.android.systemui`, `persist.sys.zram`, claves de provisionamiento. **La vara que rechaza antes de aplicar.**
- **Sistema de temas — 23 paletas** con recolor runtime por CSS variables: `setTheme` escribe `--bg-dark, --surface-1, --border, --acc, --acc2, --acc-rgb, glow…` en `document.documentElement`. Paletas (nombre → acc): darkfantasy #e01e2b · og #00d2ff · cyan #00f2fe · purple #d946ef · red #ff2d55 · green #00ff99 · gold #ffd700 · midnight #6366f1 · rose #f43f5e · sakura #ec4899 · aurora #22d3ee · ocean #0ea5e9 · amoled #e2e8f0 · slate #b8c4d4 · nebula #b400ff · solar #ff8c00 · arctic #c8f0ff · lava #ff3c00 · toxic #00ff32 · galaxy #7850ff · copper #b87333 · void #cc0000 · mint #00d2a0 · crimson #dc143c.
- **i18n real: 6 idiomas** (en, es, pt, fr, id, ar — con `getLang/mosT/mosF/applyLanguage/setLanguage`; el guía RTL documenta soporte árabe LTR-forzado).
- **Snapshots append-only con tope**: `mos_snapshots` en localStorage, `slice(-MAX_SNAPSHOTS)`, JSON.parse con `|| '[]'` y try/catch SIEMPRE (localStorage defensivo en las 8 llaves: mosClickSound, mosMusic_vol, mosTheme, mosUIStyle, mos_lang, mos_snapshots, snakeBest, preset).
- **Presets**: `saveSelectedPreset/getSavedPreset/restoreSavedPreset` + `buildHeavyGamesCmds/applyPreset/applySpoof/applyUI/applyFun/resetAllProps`.
- **Base de datos paginada**: `renderPremiumDatabase(page, query)` sobre `generatedDatabase` (= `runtimeModuleRegistry`, IIFE construida al boot): filtro por `currentModuleCategory`, búsqueda en name+desc+**cmd**, `ITEMS_PER_PAGE`, clamp de página, conteo total.
- **Transparencia de motor**: `renderLogs/clearLogs/exportLogs` — el log del engine es VISIBLE y EXPORTABLE desde la UI. `updateMetrics` recalcula en vivo.
- Juguetes del shell: juego snake (`snakeBest`), música, `initParticles/init3DPhysics`, `vipSub/applyVipTweak`.

## 6. index.html + style.css — el esqueleto

- **App shell móvil**: header fijo (--header-height: 108px) + **bottom-nav** (--bottom-nav-height: 90px) con **14 pestañas** (13 `nav-item` + 1 activa).
- **Iconos SVG hechos a mano** («HANDMADE ICON SET — custom line-art, replaces all emoji glyphs») inline en el HTML.
- Tokens: escala de radios 8/12/18/24/32 · transiciones 120/200/350ms + spring `cubic-bezier(0.34,1.56,0.64,1)` · `env(safe-area-inset-*)` · capas «dark fantasy» (df-forge/ember/vignette) · glass `rgba` con backdrop blur.
- **DEFECTO del módulo anotado**: su webroot NO es autocontenida — fonts de `fonts.googleapis.com` (Syne/Inter/Space Grotesk/JetBrains Mono) e iconos de `unpkg.com/ionicons@7.1.0` por CDN. Sin red, se degrada.

## 7. Transplante a LA BANDITA — decisión por órgano (mi interpretación, no copia)

| órgano del módulo | decisión | por qué |
|---|---|---|
| Tokens + `setTheme` runtime | **ADOPTADO** con 6 paletas propias (Caña esmeralda default, Malecón, Azúcar, Fogata, Tinta, Amoled) y persistencia | mecanismo excelente; 23 paletas es de juguete gaming, una biblioteca curada |
| `MOS_DANGEROUS_PATTERNS` | **ADOPTADO como «LA VARA»**: auto-chequeo al arranque (cps=len, salud=sello, sellos 16hex, quices descifrables, FB=15 con 💓); no se declara sana sin pruebas | la seguridad por negación se vuelve honestidad por verificación |
| `safe_*` + engine.log | **ADOPTADO como envoltorios con try/catch y «bitácora viva»** exportable | toda acción del catálogo deja rastro visible (anti-humo) |
| Snapshots append-only + localStorage defensivo | **ADOPTADO**: punto de lectura + bitácora capped 300, parse siempre protegido | misma ley de cajas de la casa |
| Web Audio synth sin assets | **ADOPTADO** con tonos propios (nav 520→760, copiar 660→990, error 210), default OFF | sensación premium sin cargar un byte de audio |
| Bottom-nav + safe-area | **ADOPTADO** (3 pestañas: Inicio · Muro FB · Acta viva) | el shell móvil es la gran firma estructural |
| Manifiesto `module.prop` | **ADOPTADO**: pie de página con id/versión/build/motor/red=0 en voz de hechos | el tono anti-marketing ya era de la casa |
| Base de datos paginada con búsqueda | **PARCIAL**: búsqueda con conteo de ocurrencias se queda; paginación NO (23 piezas se renderizan enteras para Ctrl-F honesto) | escala distinta |
| i18n 6 idiomas | **RECHAZADO** | la especie es dominicano-es por definición; el contenido no se traduce, se adapta |
| Snake, música mp3, partículas, 3D, VIP | **RECHAZADO** | juguetes del shell gaming; una biblioteca no los necesita |
| Fonts/iconos por CDN | **RECHAZADO y SUPERADO**: iconos SVG line-art propios inline + system-ui | el módulo necesita red; el catálogo no pide nada — 100% offline |

**Ley de la familia**: el catálogo es de la familia «webroot autocontenida» del módulo, pero es especie propia: lo que el módulo hace con ADB y perfiles de FPS, el catálogo lo hace con piezas y sellos — detectar, verificar, aplicar con guardas, y dejar log de todo.
