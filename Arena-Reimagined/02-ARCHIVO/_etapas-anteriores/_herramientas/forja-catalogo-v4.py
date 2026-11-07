#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FORJA v4 — NAVEGACIÓN AL NIVEL DEL MÓDULO (veredicto del dueño: v3 «apenas navegable»)
# Arquitectura: el motor VERIFICADO de plantilla-v3.html se porta POR SLICING (byte-exacto):
#   NÚCLEO slice (memoria/temas/sonido) + MOTOR slice (cps/blocks/health/vara/quiz/render/card)
#   + slice de ACCIONES (jump/toggleX/dl/cp/cpf/copy). Lo NUEVO (vistas+router v4) va en esta forja.
# Rutas hash: #/inicio #/guias #/guia/<idx> #/muro #/acta #/ajustes  → botón ATRÁS del navegador funciona.
import os, re, json, hashlib, datetime

BASE = "/home/user/Arena-Reimagined"
WA = os.path.join(BASE, "01-PUBLICACIONES/WhatsApp-dominicano-ES")
FBP = os.path.join(BASE, "01-PUBLICACIONES/Facebook-dominicano-ES")
TPL3 = open(os.path.join(BASE, "_herramientas/plantilla-v3.html"), encoding="utf-8").read()

# ── slicing del motor verificado (v3) ──
i_nuc = TPL3.index("/* ═══ NÚCLEO")
i_mot = TPL3.index("/* ═══ MOTOR DE CONTENIDO")
i_cps = TPL3.index("function cps(s)")   # el MOTOR arranca en cps: el `let view="home"` de v3 NO se porta (v4 declara el suyo)
i_vis = TPL3.index("/* ═══ VISTAS ═══ */")
i_jump = TPL3.index("function jump(id)")
i_eve = TPL3.index("/* ═══ EVENTOS")
NUCLEO_V3 = TPL3[i_nuc:i_mot]
MOTOR_V3 = TPL3[i_cps:i_vis]
ACCIONES_V3 = TPL3[i_jump:i_eve]
for s in (NUCLEO_V3, MOTOR_V3, ACCIONES_V3):
    assert "function cps(s)" in MOTOR_V3 and "function quizRevelado" in MOTOR_V3 and "function laVara" in MOTOR_V3
assert "function jump" in ACCIONES_V3 and "function fallbackCopy" in ACCIONES_V3 and "function toggleX" in ACCIONES_V3

# ── CAT/anexo igual que v3 ──
CAT = {
 "00": ("🧭", "Índice"), "01": ("🏪", "Tiendas"), "02": ("📖", "Manga"), "03": ("🔍", "Verificación"),
 "04": ("📚", "Manga"), "05": ("📖", "Manga"), "06": ("🌿", "Manga"), "07": ("🌳", "Manga"),
 "08": ("🎧", "Música"), "09": ("🧰", "Herramientas"), "10": ("🎮", "Gaming"), "11": ("🗺", "Privacidad"),
 "12": ("🛡", "Privacidad"), "13": ("🧬", "Sistemas"), "14": ("🧬", "Sistemas"), "15": ("📖", "Manga"),
 "16": ("🎬", "Video"), "17": ("🧪", "Patching"), "18": ("🖥", "Sistemas"), "19": ("🤖", "IA"),
 "20": ("🎚", "Audio · Root"),
}

def health(text):
    lines = text.split("\n"); blocks = []; cur = []; inf = False
    for l in lines:
        if l.strip().startswith("```"):
            if cur: blocks.append("\n".join(cur)); cur = []
            inf = not inf; continue
        if inf: continue
        if l.strip() == "":
            if cur: blocks.append("\n".join(cur)); cur = []
            continue
        cur.append(l)
    if cur: blocks.append("\n".join(cur))
    real = [b for b in blocks if not (b.startswith("REV|") or b.startswith("(Las respuestas"))]
    over = [len(b) for b in real if len(b) > 380]
    return {"over": len(over), "max": max((len(b) for b in real), default=0)}

def titulo_y_tag(d, nombre):
    """Título real de la pieza, leído de su propio texto (nunca del nombre de archivo):
    primer bloque; si abre con negrita, el título es el primer tramo en negrita
    (aunque envuelva varias líneas); si no, el bloque entero. El tag es el segundo
    tramo en negrita o el siguiente bloque de prosa, sin la línea de fecha de la casa."""
    bloques = [b.strip() for b in re.split(r"\n\s*\n", d) if b.strip()]
    def limpia(s):
        return re.sub(r"\s+", " ", s.replace("*", "")).strip(" ·—")
    titulo = ""; tag = ""; idx0 = 0
    def es_sep(s): return bool(s) and set(s) <= set("─━═- ")
    if bloques:
        b0 = bloques[0]
        if es_sep(b0) and len(bloques) > 1:  # separador inicial: el título vive en el bloque siguiente
            idx0 = 1; b0 = bloques[1]
        m = re.match(r"^#\s*(?:Publicación\s+\d+\s+—\s*)?(.+)$", b0, re.S)
        if m:
            titulo = limpia(m.group(1))
        else:
            negritas = re.findall(r"\*([^*]+)\*", b0, re.S)
            if negritas:
                titulo = limpia(negritas[0])
                if len(negritas) > 1: tag = limpia(negritas[1])
            else:
                titulo = limpia(b0)
    if not tag or tag == titulo:
        tag = ""
        for b in bloques[idx0+1:idx0+5]:
            c = limpia(b)
            if not c or c == titulo or c.startswith("La Bandita ·") or "Lectura total" in c or es_sep(c):
                continue
            tag = c; break
    if not titulo:
        titulo = re.sub(r"^\d+-", "", nombre).replace("-", " ")[:70]
    return titulo[:120], tag[:170]

def clave_num(f):
    m = re.match(r"(\d+)", f)
    return (int(m.group(1)) if m else 9999, f)

pieces = []
for f in sorted(os.listdir(WA), key=clave_num):
    if not f.endswith(".md") or f.startswith("LEEME") or "-2026-10-02" in f:
        continue
    d = open(os.path.join(WA, f), encoding="utf-8").read()
    pid = re.match(r"(\d+)", f).group(1)  # 19-oct: f[:2] rompía las piezas de 3 dígitos (100 -> "10")
    title, tag = titulo_y_tag(d, f)
    stars = []
    for s in re.findall(r"★\s*(\d[\d.,]*)", d):
        s2 = s.rstrip(".,")
        if s2:
            try: stars.append(float(s2.replace(".", "").replace(",", ".")))
            except ValueError: pass
    cat = CAT.get(pid, ("📄", "General"))
    pieces.append({"idx": len(pieces), "id": pid, "file": f, "title": title, "tag": tag[:170],
                   "cat": cat[1], "ico": cat[0], "len": len(d),
                   "sha": hashlib.sha256(d.encode()).hexdigest()[:16],
                   "stars": int(max(stars)) if stars else 0, "health": health(d), "text": d})

fb = []
for f in sorted(os.listdir(FBP), key=clave_num):
    if not f.endswith(".md") or f.startswith("LEEME"):
        continue
    d = open(os.path.join(FBP, f), encoding="utf-8").read()
    if "💓" not in d: continue
    ftitle, _ftag = titulo_y_tag(d, f)
    fb.append({"file": f, "title": ftitle, "len": len(d), "text": d})

data = {"wa": pieces, "fb": fb}
js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
BUILD = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# ══════════ SHELL v4 (CSS + HTML) ══════════
HEAD = r"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#060a08">
<title>LA BANDITA · Mega Catálogo</title>
<style>
:root{
  --bg:#060a08;--surf:rgba(16,26,22,0.55);--line:rgba(16,185,129,0.16);--line2:rgba(16,185,129,0.34);
  --acc:#10b981;--acc2:#34d399;--glow:rgba(16,185,129,0.26);--txt:#e7f0ea;--mut:#93a89d;
  --bad:#f87171;--warn:#f59e0b;--amber:#f59e0b;--blue:#38bdf8;
  --r1:8px;--r2:12px;--r3:18px;--r4:24px;
  --t1:120ms cubic-bezier(.4,0,.2,1);--t2:200ms cubic-bezier(.4,0,.2,1);--t3:350ms cubic-bezier(.4,0,.2,1);
}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--txt);font:15px/1.65 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;-webkit-font-smoothing:antialiased;transition:background-color var(--t3),color var(--t3)}
#glow{position:fixed;top:0;left:0;right:0;height:400px;background:linear-gradient(180deg,var(--glow),transparent 70%);pointer-events:none;z-index:0;opacity:.55}
#pbar{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,var(--acc),var(--acc2));width:0;z-index:70}
header{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.hwrap{max-width:1100px;margin:0 auto;padding:10px 14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.logo{display:flex;gap:10px;align-items:center;cursor:pointer;user-select:none}
.logo .tile{width:38px;height:38px;border-radius:var(--r2);background:linear-gradient(135deg,var(--acc2),var(--acc));display:grid;place-items:center;color:#03231a;box-shadow:0 4px 18px var(--glow)}
.logo b{font-size:14px;letter-spacing:.08em}.logo small{display:block;color:var(--mut);font-size:9.5px;letter-spacing:.24em;text-transform:uppercase}
#q{flex:1;min-width:160px;max-width:430px;background:var(--surf);border:1px solid var(--line);border-radius:999px;padding:8px 16px;color:var(--txt);font-size:13.5px;outline:none;transition:border-color var(--t2)}
#q:focus{border-color:var(--acc2)}
.hbtn{width:38px;height:38px;border-radius:var(--r2);border:1px solid var(--line);background:var(--surf);color:var(--mut);cursor:pointer;display:grid;place-items:center;transition:color var(--t2),border-color var(--t2)}
.hbtn:hover{color:var(--acc2);border-color:var(--line2)}
svg.ic{fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
main{position:relative;z-index:1;padding-bottom:130px}
.wrap{max-width:1100px;margin:0 auto;padding:22px 14px 26px}
#view{animation:viewin var(--t2)}
@keyframes viewin{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.read{max-width:800px;margin:0 auto}
.kicker{color:var(--acc);font-size:11px;letter-spacing:.28em;text-transform:uppercase;font-weight:700}
.crumbs{display:flex;gap:7px;align-items:center;color:var(--mut);font-size:12.5px;margin-bottom:18px;flex-wrap:wrap}
.crumbs a{color:var(--mut);cursor:pointer}.crumbs a:hover{color:var(--acc2)}
.crumbs .ch{opacity:.4}
.hero{display:flex;gap:18px;align-items:center;margin:4px 0 16px}
.hero .tile{width:64px;height:64px;border-radius:var(--r3);background:var(--surf);border:1px solid var(--line);display:grid;place-items:center;font-size:30px;flex:none}
.hero h1{font-size:28px;letter-spacing:-.02em;margin:0}
.sub{color:var(--mut);font-size:13.5px;margin-top:3px}
.vline{color:var(--acc2);font-size:11.5px;margin-top:6px;letter-spacing:.04em}
.chips{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:14px 0}
.chip{background:var(--surf);border:1px solid var(--line);border-radius:var(--r2);padding:10px 14px;backdrop-filter:blur(10px)}
.chip .l{color:var(--mut);font-size:10px;letter-spacing:.18em;text-transform:uppercase}
.chip .v{font-size:16px;font-weight:800;margin-top:2px;word-break:break-all}
.chip .v.ok{color:var(--acc2)}.chip .v.warn{color:var(--warn)}
.fchips{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 14px}
.fchip{background:var(--surf);border:1px solid var(--line);color:var(--mut);border-radius:999px;padding:6px 14px;cursor:pointer;font-size:12px;transition:all var(--t2)}
.fchip:hover{color:var(--txt)}.fchip.on{background:var(--acc);border-color:var(--acc);color:#03231a;font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.card{background:var(--surf);border:1px solid var(--line);border-radius:var(--r3);padding:18px 20px;backdrop-filter:blur(12px)}
.card h4{margin:0 0 10px;font-size:14.5px;letter-spacing:.02em}
.pcard{background:var(--surf);border:1px solid var(--line);border-radius:var(--r3);padding:16px 18px;cursor:pointer;transition:border-color var(--t2),transform var(--t2);backdrop-filter:blur(12px)}
.pcard:hover{border-color:var(--line2);transform:translateY(-2px)}
.pcard .top{display:flex;gap:12px;align-items:center}
.pcard .tile{width:44px;height:44px;border-radius:var(--r2);background:var(--line);display:grid;place-items:center;font-size:22px;flex:none}
.pcard .t{font-weight:700;font-size:14.5px}
.pcard .d{color:var(--mut);font-size:12.5px;margin-top:8px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.pcard .m{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.badge{font-size:10.5px;letter-spacing:.06em;border:1px solid var(--line);border-radius:999px;padding:2.5px 10px;color:var(--mut)}
.badge.ok{color:var(--acc2);border-color:var(--line2)}
.badge.wa{color:var(--warn);border-color:var(--warn)}
.badge.st{color:var(--amber);border-color:var(--amber)}
.btn{display:inline-flex;gap:7px;align-items:center;background:var(--surf);border:1px solid var(--line2);color:var(--txt);border-radius:999px;padding:9px 20px;cursor:pointer;font-size:13px;transition:all var(--t2)}
.btn:hover{border-color:var(--acc2);color:var(--acc2)}
.btn.pri{background:var(--acc);border-color:var(--acc);color:#03231a;font-weight:700}
.btn.pri:hover{background:var(--acc2)}
.btn.gho.on{border-color:var(--acc2);color:var(--acc2)}
.acts{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0}
.toc{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:4px 14px}
.toc a{color:var(--mut);cursor:pointer;font-size:13px;padding:3px 0}
.toc a:hover{color:var(--acc2)}
article{margin-top:18px}
.blk{background:var(--surf);border:1px solid var(--line);border-radius:var(--r2);padding:14px 16px;margin:12px 0;position:relative;overflow-wrap:break-word}
.blk h3,.blk h3+h3{font-size:19px;letter-spacing:-.01em;margin:4px 0 8px;color:var(--acc2)}
.blk.big{border-color:var(--bad)}
.blk.big::after{content:attr(data-n)"c > 380";position:absolute;top:-10px;right:8px;background:var(--bad);color:#111;font-size:10px;font-weight:800;padding:1px 8px;border-radius:999px}
.fence{background:rgba(0,0,0,0.35);border:1px solid var(--line);border-radius:var(--r2);padding:12px 14px;margin:12px 0;overflow:auto;font:12.5px/1.55 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.star{color:var(--amber);font-weight:700}
.rel{background:rgba(245,158,11,0.18);border-radius:4px;padding:0 3px;color:var(--amber)}
.quiz{background:var(--surf);border:1px solid var(--line2);border-radius:var(--r3);padding:16px 18px;margin:14px 0}
.ql{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);font-weight:700}
.rev{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;color:var(--mut);filter:blur(4px);user-select:none;margin:10px 0;transition:filter var(--t3)}
.sol{display:none;font-size:13.5px;border-top:1px dashed var(--line2);padding-top:10px;margin-top:6px}
.quiz.open .rev{filter:blur(0);user-select:auto}
.quiz.open .sol{display:block}
.nav2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}
.nav2 .dir{color:var(--mut);font-size:11px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:4px}
.nav2 .t{font-weight:700;font-size:13.5px}
/* ── v4: base de datos de guías (filas agrupadas) ── */
.rgroup{margin-bottom:8px}
.rhead{position:sticky;top:60px;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(8px);color:var(--acc);font-size:11px;letter-spacing:.22em;text-transform:uppercase;font-weight:800;padding:10px 4px 6px;border-bottom:1px solid var(--line)}
.row{display:flex;gap:12px;align-items:center;background:var(--surf);border:1px solid var(--line);border-radius:var(--r2);padding:11px 14px;margin:8px 0;cursor:pointer;transition:border-color var(--t2),transform var(--t2)}
.row:hover{border-color:var(--line2);transform:translateX(4px)}
.rtile{width:42px;height:42px;border-radius:var(--r2);background:var(--line);display:grid;place-items:center;font-size:21px;flex:none}
.rmain{flex:1;min-width:0}
.rt{font-weight:700;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rd{color:var(--mut);font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:1px}
.rmeta{display:flex;gap:6px;align-items:center;flex:none}
.chev{color:var(--mut);font-size:20px;line-height:1;padding:0 2px}
/* ── v4: tiles de categorías (Inicio) ── */
.tilegrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}
.ctile{background:var(--surf);border:1px solid var(--line);border-radius:var(--r3);padding:16px;cursor:pointer;transition:border-color var(--t2),transform var(--t2)}
.ctile:hover{border-color:var(--line2);transform:translateY(-3px)}
.ctile .ce{font-size:26px}
.ctile .cn{font-weight:800;font-size:13.5px;margin-top:8px}
.ctile .cc{color:var(--mut);font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin-top:2px}
.minirow{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px}
.minicard{background:var(--surf);border:1px solid var(--line);border-radius:var(--r2);padding:12px 14px;cursor:pointer;transition:border-color var(--t2)}
.minicard:hover{border-color:var(--acc2)}
.minicard .t{font-weight:700;font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.minicard .m{color:var(--mut);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:4px}
/* ── v4: FABs de navegación por pieza ── */
.fabs{position:fixed;right:calc(14px + env(safe-area-inset-right,0px));bottom:calc(96px + env(safe-area-inset-bottom,0px));display:flex;flex-direction:column;gap:10px;z-index:55}
.fab{width:48px;height:48px;border-radius:50%;background:var(--acc);color:#03231a;border:none;font-size:24px;font-weight:800;cursor:pointer;box-shadow:0 8px 26px var(--glow);transition:transform var(--t2),background var(--t2)}
.fab:active{transform:scale(0.92)}
.fab:hover{background:var(--acc2)}
/* ── v4: ajustes ── */
.swgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.sw{display:flex;gap:10px;align-items:center;background:var(--surf);border:1px solid var(--line);border-radius:var(--r2);padding:11px 13px;cursor:pointer;font-size:13px;color:var(--txt);transition:border-color var(--t2)}
.sw:hover{border-color:var(--line2)}
.sw.on{border-color:var(--acc2)}
.sw .dot{width:22px;height:22px;border-radius:50%;background:var(--sw);flex:none;box-shadow:0 0 12px var(--sw)}
textarea{width:100%;min-height:260px;background:rgba(0,0,0,0.35);border:1px solid var(--line);border-radius:var(--r2);color:var(--txt);font:12.5px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace;padding:12px;resize:vertical;margin-top:10px}
.empty{text-align:center;color:var(--mut);padding:40px 0;grid-column:1/-1}
footer#pie{position:relative;z-index:1;max-width:1100px;margin:0 auto;padding:18px 16px 20px;font:11px/1.8 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mut);border-top:1px solid var(--line)}
.bnav{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(12px + env(safe-area-inset-bottom,0px));display:flex;gap:2px;background:var(--surf);backdrop-filter:blur(16px);border:1px solid var(--line);border-radius:999px;padding:6px;z-index:60;box-shadow:0 10px 34px rgba(0,0,0,0.55)}
.btab{display:flex;flex-direction:column;align-items:center;gap:2px;padding:7px 14px;border-radius:999px;color:var(--mut);cursor:pointer;border:none;background:none;font-size:9px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;transition:all var(--t2)}
.btab svg{width:20px;height:20px}
.btab.on{color:var(--acc2);background:var(--glow)}
.brow{display:flex;gap:8px;padding:7px 0;border-bottom:1px solid var(--line);font-size:13px;flex-wrap:wrap;align-items:baseline}
.brow .bt{font-family:ui-monospace,Menlo,monospace;color:var(--mut);font-size:11.5px;flex:none}
.brow .bd{color:var(--mut)}
.blog{max-height:420px;overflow:auto;padding-right:4px}
.tst{position:fixed;left:50%;transform:translateX(-50%) translateY(20px);bottom:100px;background:var(--acc);color:#03231a;font-weight:700;font-size:13px;border-radius:999px;padding:9px 22px;opacity:0;pointer-events:none;z-index:80;transition:all var(--t2);box-shadow:0 8px 30px var(--glow)}
.tst.on{opacity:1;transform:translateX(-50%) translateY(0)}
@media(max-width:640px){.hero h1{font-size:22px}.wrap{padding:14px 12px 20px}.nav2{grid-template-columns:1fr}.rtile{width:36px;height:36px;font-size:18px}.btab{padding:7px 11px}.rhead{top:56px}}
</style>
</head><body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-ini" viewBox="0 0 24 24"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h5v-6h4v6h5V10"/></symbol>
<symbol id="i-lib" viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15.5H6.5A2.5 2.5 0 0 0 4 21V5.5z"/><path d="M4 18.5A2.5 2.5 0 0 1 6.5 16H20"/><path d="M9 7.5h6"/></symbol>
<symbol id="i-muro" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.8c2.9.2 5.5 2 5.5 5.2"/></symbol>
<symbol id="i-acta" viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="2.5"/><path d="M9 8h6M9 12h6M9 16h3.5"/></symbol>
<symbol id="i-ajus" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2"/><path d="M19 12a7 7 0 0 0-.14-1.4l2-1.55-2-3.46-2.36.95a7 7 0 0 0-2.42-1.4L13.7 2.6h-3.4l-.38 2.54a7 7 0 0 0-2.42 1.4l-2.36-.95-2 3.46 2 1.55A7 7 0 0 0 5 12c0 .47.05.94.14 1.4l-2 1.55 2 3.46 2.36-.95a7 7 0 0 0 2.42 1.4l.38 2.54h3.4l.38-2.54a7 7 0 0 0 2.42-1.4l2.36.95 2-3.46-2-1.55c.09-.46.14-.93.14-1.4z"/></symbol>
<symbol id="i-paleta" viewBox="0 0 24 24"><path d="M12 3a9 9 0 1 0 9 9c0-1.2-.9-2-2-2h-2.6a2 2 0 0 1-1.4-3.4c.6-.6.4-1.6-.3-2.2A9 9 0 0 0 12 3z"/><circle cx="7.5" cy="11.5" r="0.4"/><circle cx="10.5" cy="7.8" r="0.4"/><circle cx="15" cy="7.5" r="0.4"/></symbol>
<symbol id="i-son" viewBox="0 0 24 24"><path d="M4 10v4h3.5L13 18.5v-13L7.5 10H4z"/><path d="M16 9.5a4 4 0 0 1 0 5.5M18.5 7a8 8 0 0 1 0 10"/></symbol>
<symbol id="i-mudo" viewBox="0 0 24 24"><path d="M4 10v4h3.5L13 18.5v-13L7.5 10H4z"/><path d="M16.5 9.5l5 5M21.5 9.5l-5 5"/></symbol>
<symbol id="i-cop" viewBox="0 0 24 24"><rect x="9" y="9" width="11" height="11" rx="2.5"/><path d="M5 15h-.5A1.5 1.5 0 0 1 3 13.5v-9A1.5 1.5 0 0 1 4.5 3h9A1.5 1.5 0 0 1 15 4.5V5"/></symbol>
<symbol id="i-baj" viewBox="0 0 24 24"><path d="M12 4v11m0 0l-4.5-4.5M12 15l4.5-4.5"/><path d="M4.5 20h15"/></symbol>
<symbol id="i-xra" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M5.5 5.5l13 13"/></symbol>
</defs></svg>
<div id="pbar"></div>
<div id="glow"></div>
<header><div class="hwrap">
<div class="logo" onclick='nav("#/inicio")'><div class="tile"><svg class="ic" width="20" height="20"><use href="#i-ini"/></svg></div><div><b>LA BANDITA</b><small>mega catálogo</small></div></div>
<input id="q" placeholder="Buscar… (tecla /)">
<button class="hbtn" id="btnTema" title="Cambiar tema"><svg class="ic" width="18" height="18"><use href="#i-paleta"/></svg></button>
<button class="hbtn" id="btnSon" title="Sonido"><svg class="ic" width="18" height="18"><use id="uson" href="#i-mudo"/></svg></button>
</div></header>
<main><div class="wrap"><div id="view"></div></div></main>
<footer id="pie">id=catalogo-la-bandita · version=v4.0 · build=__BUILD__ · motor=forja-v4 · piezas=__NWA__ wa + __NFB__ fb · red=0 peticiones · rutas=6 (#/inicio #/guias #/guia #/muro #/acta #/ajustes) · temas=6 · vara=auto-chequeo al arranque<br>ADN: despiece real del modulo MOsPremiumV15 (AxManager · 4.694.366 b · sha16 e658c88ad6429cd4) — app shell con nav inferior y vistas enruteadas, base de datos de guias con filas agrupadas por familia, ajustes con temas en cuadricula, FABs de navegacion y gestos. Reconstruido, no copiado · La Bandita · corte 15-oct-2026.</footer>
<nav class="bnav">
<button class="btab" data-v="inicio" onclick='nav("#/inicio")'><svg class="ic"><use href="#i-ini"/></svg>Inicio</button>
<button class="btab" data-v="guias" onclick='nav("#/guias")'><svg class="ic"><use href="#i-lib"/></svg>Guías</button>
<button class="btab" data-v="muro" onclick='nav("#/muro")'><svg class="ic"><use href="#i-muro"/></svg>Muro FB</button>
<button class="btab" data-v="acta" onclick='nav("#/acta")'><svg class="ic"><use href="#i-acta"/></svg>Acta</button>
<button class="btab" data-v="ajustes" onclick='nav("#/ajustes")'><svg class="ic"><use href="#i-ajus"/></svg>Ajustes</button>
</nav>
<div class="tst" id="tst"></div>
<script>
const D = __DATA__;
"""

# ══════════ VISTAS + ROUTER v4 (lo nuevo) ══════════
VISTAS_V4 = r"""/* ═══ VISTAS v4 — app shell enrutado (patrón switchTab del módulo + history real) ═══ */
let view="inicio", cur=null, xray=false, cat="Todas", q="";
function pinta(html){const v=$("#view");v.innerHTML=html;v.style.animation="none";void v.offsetWidth;v.style.animation="";window.scrollTo(0,0);}
function nav(h){if(location.hash===h){route();}else{location.hash=h;}}
function route(){
  const seg=location.hash.replace(/^#\/?/,"").split("/");
  if(seg[0]==="guia"&&D.wa[+seg[1]])goPiece(+seg[1]);
  else if(seg[0]==="guias")goGuias();
  else if(seg[0]==="muro")goFB();
  else if(seg[0]==="acta")goActa();
  else if(seg[0]==="ajustes")goAjustes();
  else goHome();
}
function marcaNav(v){document.querySelectorAll(".btab").forEach(t=>t.classList.toggle("on",t.dataset.v===v));}
function titulo(t){document.title=t+" · LA BANDITA";}
function irCat(c){cat=c;nav("#/guias");}
function fila(p){
  const h=health(p.text);
  return "<div class=\"row\" onclick='nav(\"#/guia/"+p.idx+"\")'><div class=\"rtile\">"+p.ico+"</div>"+
    "<div class=\"rmain\"><div class=\"rt\">"+esc(p.title)+"</div><div class=\"rd\">"+esc(p.tag||p.title)+"</div></div>"+
    "<div class=\"rmeta\"><span class=\"badge "+(h.over===0?"ok":"wa")+"\">"+(h.over===0?"✓":h.over+" >380")+"</span>"+
    "<span class=\"badge\">"+p.len.toLocaleString()+" c</span><span class=\"chev\">›</span></div></div>";
}
function goHome(){
  view="inicio";cur=null;marcaNav("inicio");titulo("Inicio");
  const cats=[...new Set(D.wa.map(p=>p.cat))];
  const nPor=c=>D.wa.filter(p=>p.cat===c).length;
  const cont=(NUCLEO.punto>=0&&D.wa[NUCLEO.punto])?"<div class=\"card\" style=\"margin-top:16px;border-color:var(--line2)\"><h4>📌 Continuar donde te quedaste</h4>"+card(D.wa[NUCLEO.punto])+"</div>":"";
  const rec=D.wa.slice(-6);
  pinta("<div style=\"text-align:center;padding:18px 0 4px\">"+
    "<div class=\"kicker\">Biblioteca libre dominicana · corte 15-oct-2026</div>"+
    "<h1 style=\"font-size:34px;letter-spacing:-.03em;margin:10px 0 4px\">Mega Catálogo <span style=\"color:var(--acc)\">La Bandita</span></h1>"+
    "<div style=\"color:var(--mut);font-size:14px\">Una app de lectura, no una página: "+D.wa.length+" guías con sello, salud de respiro y vara de arranque — todo recalculado en tu navegador.</div></div>"+
    "<div class=\"chips\">"+chip("Piezas",D.wa.length)+chip("Muro FB (copia)",D.fb.length)+chip("Vara de arranque",(VARA.ok?"APROBADA ✓":"FALLO ✗"),(VARA.ok?"ok":"warn"))+chip("Quices",VARA.nquiz+" descifrables","ok")+"</div>"+cont+
    "<div class=\"card\" style=\"margin-top:16px\"><h4>🗂 Por familia</h4><div class=\"tilegrid\" style=\"margin-top:8px\">"+
    cats.map(c=>"<div class=\"ctile\" onclick='irCat(\""+c+"\")'><div class=\"ce\">"+(D.wa.find(p=>p.cat===c)||{}).ico+"️</div><div class=\"cn\">"+c+"</div><div class=\"cc\">"+nPor(c)+(nPor(c)===1?" guía":" guías")+"</div></div>").join("")+"</div></div>"+
    "<div class=\"card\" style=\"margin-top:16px\"><h4>🆕 El cierre del canon (las últimas seis, 103–108)</h4><div class=\"minirow\" style=\"margin-top:8px\">"+
    rec.map(p=>"<div class=\"minicard\" onclick='nav(\"#/guia/"+p.idx+"\")'><div class=\"t\">"+p.ico+" "+esc(p.title)+"</div><div class=\"m\">#"+p.id+" · "+p.len.toLocaleString()+" c · "+(health(p.text).over===0?"respirable ✓":">380")+"</div></div>").join("")+"</div></div>");
}
function goGuias(){
  view="guias";cur=null;marcaNav("guias");titulo("Guías");
  const cats=[...new Set(D.wa.map(p=>p.cat))];
  let list=D.wa.filter(p=>cat==="Todas"||p.cat===cat);
  const query=q.trim().toLowerCase();
  let note="";
  if(query.length>2){
    const hits={};
    D.wa.forEach(p=>{ hits[p.idx]=(p.text.toLowerCase().split(query).length-1); });
    list=list.filter(p=>p.title.toLowerCase().includes(query)||p.tag.toLowerCase().includes(query)||hits[p.idx]>0);
    const parts=Object.entries(hits).filter(([k,v])=>v>0).map(([k,v])=>"#"+D.wa[k].id+" ("+v+")");
    note="<div class=\"card\" style=\"margin-top:12px\"><h4>🔎 "+esc(q)+"</h4><div style=\"color:var(--mut)\">"+list.length+" piezas coinciden · ocurrencias en contenido: "+(parts.join(" · ")||"—")+"</div></div>";
  }
  const grupos=cats.map(c=>({c:c,ps:list.filter(p=>p.cat===c)})).filter(g=>g.ps.length);
  const filas=grupos.map(g=>"<div class=\"rgroup\"><div class=\"rhead\">"+g.c+" · "+g.ps.length+"</div>"+g.ps.map(fila).join("")+"</div>").join("");
  pinta("<div style=\"text-align:center;padding:12px 0 2px\"><div class=\"kicker\">Base de datos de guías</div>"+
    "<h1 style=\"font-size:28px;letter-spacing:-.02em;margin:8px 0 2px\">Las "+D.wa.length+" piezas</h1></div>"+
    "<div class=\"fchips\">"+["Todas"].concat(cats).map(c=>"<button class=\"fchip"+(c===cat?" on":"")+"\" onclick='irCat(\""+c+"\")'>"+c+"</button>").join("")+"</div>"+note+
    (list.length?filas:"<div class=\"empty\">Nada por aquí con ese filtro.</div>"));
}
function goPiece(k){
  const p=D.wa[k]; if(p==null) return;
  view="p";cur=p;marcaNav("guias");titulo("#"+p.id+" "+p.title.slice(0,30));
  NUCLEO.punto=k;memSet("bandita.punto",k);
  bitacora("Lectura","#"+p.id+" "+p.title.slice(0,42));
  tono(520,0,0.05);
  const prev=D.wa[k-1], next=D.wa[k+1];
  const h=health(p.text);
  const sim=D.wa.filter(x=>x.cat===p.cat&&x.idx!==p.idx).slice(0,5);
  const tocs=p.text.split("\n").map((l,i)=>({l,i:i+1})).filter(x=>/^\*[^*\n]{3,48}\*$/.test(x.l));
  pinta("<div class=\"read\">"+
    "<div class=\"crumbs\"><a onclick='nav(\"#/inicio\")'>Inicio</a><span class=\"ch\">›</span><a onclick='nav(\"#/guias\")'>Guías</a><span class=\"ch\">›</span><span>"+p.cat+"</span><span class=\"ch\">›</span><span>"+p.id+"</span></div>"+
    "<div class=\"hero\"><div class=\"tile\">"+p.ico+"</div><div><h1>"+esc(p.title)+"</h1>"+
    "<div class=\"sub\">"+esc(p.tag||"")+"</div>"+
    "<div class=\"vline\">✓ Verificada · batería 24/24 · 30/30 · fuzz 60/60 · lupa-v6 aire</div></div></div>"+
    "<div class=\"chips\">"+chip("Tamaño (len)",p.len.toLocaleString()+" c")+chip("Sello SHA-256",p.sha)+
    chip("Respiro",(h.over===0?"0 >380c ✓":h.over+" bloques >380c"),(h.over===0?"ok":"warn"))+
    chip("Fama censada",p.stars?("★"+p.stars.toLocaleString()+" pico"):"—")+"</div>"+
    "<div class=\"acts\"><button class=\"btn pri\" onclick='dl("+p.idx+")'><svg class=\"ic\" width=\"15\" height=\"15\"><use href=\"#i-baj\"/></svg> Descargar .md</button>"+
    "<button class=\"btn\" onclick='cp("+p.idx+")'><svg class=\"ic\" width=\"15\" height=\"15\"><use href=\"#i-cop\"/></svg> Copiar fuente</button>"+
    "<button class=\"btn"+(xray?" on":"")+"\" onclick='toggleX()'><svg class=\"ic\" width=\"15\" height=\"15\"><use href=\"#i-xra\"/></svg> Rayos-X</button></div>"+
    "<div class=\"card\"><h4>En esta guía · "+tocs.length+" secciones</h4><div class=\"toc\">"+
    tocs.map(x=>"<a onclick='jump(\"h"+x.i+"\")'>"+esc(x.l.replace(/^\*/,"").replace(/\*$/,""))+"</a>").join("")+"</div></div>"+
    "<article>"+renderContent(p.text)+"</article>"+
    "<div class=\"nav2\">"+(prev?"<div class=\"card\" onclick='nav(\"#/guia/"+(k-1)+"\")'><div class=\"dir\">← Anterior</div><div class=\"t\">"+esc(prev.title)+"</div></div>":"<div></div>")+
    (next?"<div class=\"card\" style=\"text-align:right\" onclick='nav(\"#/guia/"+(k+1)+"\")'><div class=\"dir\">Siguiente →</div><div class=\"t\">"+esc(next.title)+"</div></div>":"<div></div>")+"</div>"+
    (sim.length?"<div class=\"card\" style=\"margin-top:24px\"><h4>Piezas hermanas · "+p.cat+"</h4>"+sim.map(x=>"<div class=\"pcard\" style=\"margin:8px 0\" onclick='nav(\"#/guia/"+x.idx+"\")'><div class=\"top\"><div class=\"tile\">"+x.ico+"</div><div><div class=\"t\">"+esc(x.title)+"</div><div class=\"d\">"+esc(x.tag||"")+"</div></div></div></div>").join("")+"</div>":"")+
    "</div>"+
    "<div class=\"fabs\">"+(prev?"<button class=\"fab\" title=\"Anterior\" onclick='nav(\"#/guia/"+(k-1)+"\")'>‹</button>":"")+
    (next?"<button class=\"fab\" title=\"Siguiente\" onclick='nav(\"#/guia/"+(k+1)+"\")'>›</button>":"")+"</div>");
}
function goFB(){
  view="fb";cur=null;marcaNav("muro");titulo("Muro FB");
  bitacora("Vista","Muro FB · texto puro");tono(520,0,0.05);
  pinta("<div style=\"text-align:center;padding:14px 0 4px\"><div class=\"kicker\">Para copiar y subir a la plataforma</div>"+
    "<h1 style=\"font-size:30px;letter-spacing:-.02em;margin:8px 0 4px\">Muro Facebook · texto puro</h1>"+
    "<div style=\"color:var(--mut)\">Estas NO van en HTML: se copian tal cual al muro. Las de era-vieja ya publicadas no van aquí.</div></div>"+
    "<div style=\"display:flex;flex-direction:column;gap:14px;margin-top:18px\">"+D.fb.map((p,i)=>
    "<div class=\"card\"><div style=\"display:flex;gap:10px;align-items:center;flex-wrap:wrap\"><b>💓 "+esc(p.title)+"</b>"+
    "<span class=\"badge\">"+p.len.toLocaleString()+" c</span><span class=\"badge ok\">caja de pulso viva</span>"+
    "<button class=\"btn pri\" style=\"margin-left:auto;padding:8px 18px;font-size:12px\" onclick='cpf("+i+")'><svg class=\"ic\" width=\"14\" height=\"14\"><use href=\"#i-cop\"/></svg> Copiar pieza entera</button></div>"+
    "<details><summary style=\"cursor:pointer;color:var(--acc2);font-size:13px;margin-top:10px\">ver texto</summary>"+
    "<textarea id=\"fb"+i+"\" readonly>"+esc(p.text)+"</textarea></details></div>").join("")+"</div>");
}
function goActa(){
  view="acta";cur=null;marcaNav("acta");titulo("Acta viva");
  const filas=NUCLEO.bitacora.slice().reverse().map(e=>"<div class=\"brow\"><span class=\"bt\">"+esc(e.t)+"</span><b>"+esc(e.h)+"</b>"+(e.d?"<span class=\"bd\">— "+esc(e.d)+"</span>":"")+"</div>").join("")||"<div class=\"empty\">Bitácora vacía.</div>";
  pinta("<div class=\"read\">"+
    "<div class=\"kicker\" style=\"text-align:center\">Transparencia del motor — todo deja rastro</div>"+
    "<h1 style=\"font-size:30px;letter-spacing:-.02em;text-align:center;margin:8px 0 4px\">Acta viva</h1>"+
    "<div class=\"chips\">"+chip("Vara de arranque",(VARA.ok?"APROBADA ✓":"CON FALLOS ✗"),(VARA.ok?"ok":"warn"))+chip("Quices descifrables",VARA.nquiz)+chip("Entradas",NUCLEO.bitacora.length)+chip("Tema",TEMAS[NUCLEO.tema].nom)+"</div>"+
    (!VARA.ok?"<div class=\"card\" style=\"border-color:var(--bad)\"><h4>✗ Fallos detectados al arranque</h4><div style=\"color:var(--bad);font-size:13.5px\">"+esc(VARA.lineas.join(" · "))+"</div></div>":"")+
    "<div class=\"card\"><h4>Bitácora de esta copia (últimas "+NUCLEO.bitacora.length+")</h4><div class=\"blog\">"+filas+"</div>"+
    "<div style=\"margin-top:12px\"><button class=\"btn pri\" onclick='expBit()'><svg class=\"ic\" width=\"15\" height=\"15\"><use href=\"#i-baj\"/></svg> Exportar bitácora .txt</button></div></div>"+
    "<div class=\"card\" style=\"margin-top:16px\"><h4>Cómo se construyó este catálogo</h4><div style=\"color:var(--mut);font-size:13.5px;line-height:1.75\">Despiece real del módulo <b>MOsPremiumV15</b> (AxManager · 4.694.366 b · sha16 e658c88ad6429cd4): app shell enrutado, base de datos con filas por familia, vara que auto-verifica antes de declararse sana, bitácora exportable, temas con recolor runtime, sonidos sintetizados sin assets, memoria persistente protegida. Sin CDN: funciona sin red. Reconstrucción propia — ni una línea copiada.</div></div>"+
    "</div>");
}
function goAjustes(){
  view="ajustes";cur=null;marcaNav("ajustes");titulo("Ajustes");
  const sws=ORDEN.map(n=>"<button class=\"sw"+(NUCLEO.tema===n?" on":"")+"\" style=\"--sw:"+TEMAS[n].acc+"\" onclick='setTema(\""+n+"\",true)'><span class=\"dot\"></span>"+TEMAS[n].nom+"</button>").join("");
  pinta("<div class=\"read\">"+
    "<div class=\"kicker\" style=\"text-align:center\">La sala de máquinas</div>"+
    "<h1 style=\"font-size:30px;letter-spacing:-.02em;text-align:center;margin:8px 0 14px\">Ajustes</h1>"+
    "<div class=\"card\"><h4>🎨 Tema (recolor al instante, se recuerda)</h4><div class=\"swgrid\" style=\"margin-top:8px\">"+sws+"</div></div>"+
    "<div class=\"card\" style=\"margin-top:14px\"><h4>🔊 Sonido de síntesis (Web Audio, sin archivos)</h4>"+
    "<div style=\"display:flex;gap:10px;margin-top:8px\"><button class=\"btn"+(NUCLEO.sonido?" pri":"")+"\" onclick='setSon(true)'>Encendido</button>"+
    "<button class=\"btn"+(!NUCLEO.sonido?" pri":"")+"\" onclick='setSon(false)'>Apagado</button>"+
    "<span style=\"color:var(--mut);font-size:12.5px;align-self:center\">"+(NUCLEO.sonido?"tonos activos":"silencio")+"</span></div></div>"+
    "<div class=\"card\" style=\"margin-top:14px\"><h4>🩺 La vara de arranque</h4><div style=\"color:var(--mut);font-size:13px;line-height:1.7\">El catálogo se examina solo cada vez que abre: cps=len en las 23 piezas, salud=sello, sellos de 16 hex, quices descifrables ("+VARA.nquiz+"), muro FB con 💓. Resultado de esta sesión: <b style=\"color:var("+(VARA.ok?"--acc2":"--bad")+")\">"+(VARA.ok?"APROBADA":"CON FALLOS")+"</b>"+(VARA.ok?"":" — "+esc(VARA.lineas.join(" · ")))+"</div></div>"+
    "<div class=\"card\" style=\"margin-top:14px\"><h4>🧠 Memoria de esta copia</h4><div style=\"color:var(--mut);font-size:13px\">Punto de lectura: "+(NUCLEO.punto>=0&&D.wa[NUCLEO.punto]?"#"+D.wa[NUCLEO.punto].id+" "+esc(D.wa[NUCLEO.punto].title.slice(0,40)):"—")+" · Entradas en bitácora: "+NUCLEO.bitacora.length+"</div>"+
    "<div style=\"margin-top:10px\"><button class=\"btn\" onclick='borraMemoria()'>Borrar memoria local</button></div></div>"+
    "</div>");
}
function borraMemoria(){
  bitacora("Memoria","borrada por el lector");
  const ultima=NUCLEO.bitacora.slice(-1);
  ["bandita.tema","bandita.sonido","bandita.punto","bandita.bitacora"].forEach(k=>{try{localStorage.removeItem(k)}catch(e){}});
  NUCLEO.punto=-1;NUCLEO.bitacora=ultima;NUCLEO.tema="cana";setTema("cana",false);
  toast("Memoria borrada");goAjustes();
}
function expBit(){
  try{const t=NUCLEO.bitacora.map(e=>"["+e.t+"] "+e.h+(e.d?" — "+e.d:"")).join("\n")+"\n";const b=new Blob([t],{type:"text/plain"});const a=document.createElement("a");a.href=URL.createObjectURL(b);a.download="bandita-bitacora.txt";a.click();bitacora("Bitácora","exportada");toast("⬇ Bitácora exportada")}catch(e){toast("Exportación bloqueada aquí — captura de pantalla")}
}
function setCat(c){cat=c;goGuias()}
/* ═══ GESTOS: deslizar ← / → entre piezas (mobile) ═══ */
let tX=0,tY=0;
document.addEventListener("touchstart",e=>{if(view!=="p")return;tX=e.touches[0].clientX;tY=e.touches[0].clientY;},{passive:true});
document.addEventListener("touchend",e=>{
  if(view!=="p"||!cur)return;
  const dx=e.changedTouches[0].clientX-tX, dy=e.changedTouches[0].clientY-tY;
  if(Math.abs(dx)>70&&Math.abs(dy)<50){const nk=cur.idx+(dx<0?1:-1);if(D.wa[nk])nav("#/guia/"+nk);}
},{passive:true});
"""

EVENTOS_V4 = r"""/* ═══ EVENTOS ═══ */
$("#q").addEventListener("input",e=>{q=e.target.value;if(view!=="guias"){cat="Todas";nav("#/guias");}else goGuias();});
document.addEventListener("keydown",e=>{
  if(e.target.tagName==="INPUT"||e.target.tagName==="TEXTAREA"){if(e.key==="Escape")e.target.blur();return;}
  if(e.key==="/"&&view!=="fb"){e.preventDefault();$("#q").focus();}
  if(view==="p"&&cur){if(e.key==="ArrowRight"&&D.wa[cur.idx+1])nav("#/guia/"+(cur.idx+1));if(e.key==="ArrowLeft"&&D.wa[cur.idx-1])nav("#/guia/"+(cur.idx-1));}
});
document.addEventListener("pointerdown",initAudio);
window.addEventListener("scroll",()=>{const h=document.documentElement;$("#pbar").style.width=((h.scrollTop/(h.scrollHeight-h.clientHeight)*100)||0)+"%";});
window.addEventListener("hashchange",route);
$("#btnTema").addEventListener("click",cicloTema);
$("#btnSon").addEventListener("click",()=>setSon(!NUCLEO.sonido));
/* ═══ ARRANQUE: tema → sonido → vara → bitácora → ruta inicial ═══ */
setTema(TEMAS[NUCLEO.tema]?NUCLEO.tema:"cana",false);
if($("#uson"))$("#uson").setAttribute("href",NUCLEO.sonido?"#i-son":"#i-mudo");
$("#q").placeholder="Buscar en "+D.wa.length+" piezas… (tecla /)";
VARA=laVara();
bitacora("Arranque","vara "+(VARA.ok?"completa":"CON FALLOS")+" · "+D.wa.length+" piezas · "+D.fb.length+" FB · "+VARA.nquiz+" quices descifrables");
if(!VARA.ok)bitacora("FALLO",VARA.lineas.join(" · "));
route();
</script></body></html>
"""

# HEAD ya abre <script> y deja `const D = __DATA__;` al final — NO repetir la etiqueta
html = (HEAD.replace("__DATA__", js)
            .replace("__BUILD__", BUILD)
            + NUCLEO_V3 + MOTOR_V3 + VISTAS_V4 + ACCIONES_V3 + EVENTOS_V4)
html = html.replace("__NWA__", str(len(data["wa"]))).replace("__NFB__", str(len(data["fb"])))
assert "__NWA__" not in html and "__NFB__" not in html and "__BUILD__" not in html, "token sin reemplazar"
# sanity del ensamblado
for token in ("function cps(s)", "function quizRevelado", "function laVara", "function route", "function goAjustes", "function fallbackCopy", "route();"):
    assert token in html, "falta " + token
assert html.count("const D = ") == 1
out = os.path.join(BASE, "02-ARCHIVO/catalogo-la-bandita.html")
open(out, "w", encoding="utf-8").write(html)
print("CATÁLOGO v4:", len(html), "chars ·", os.path.getsize(out), "bytes · WA:", len(pieces), "· FB:", len(fb), "· build:", BUILD)
