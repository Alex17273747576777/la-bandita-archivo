#!/usr/bin/env node
/*
 * bateria-viva.js — ETAPA 3 · nano-lotes 3.2+3.3: batería en vivo + capturas (solo lectura).
 * Por pieza: consola limpia (0 errores/0 pageerror/0 requestfailed) · deep-link a ancla
 * reparada (navegación real) · búsqueda funcional · tema alternante · sin overflow móvil.
 * Capturas: escritorio-claro + móvil-oscuro por pieza → 02-ARCHIVO/_capturas-etapa3/.
 */
const { chromium } = require("/tmp/node_modules/playwright");
const path = require("path");
const fs = require("fs");

const BASE = "/home/user/Arena-Reimagined/00-CANON/_envases-xhtml";
const OUT = "/home/user/Arena-Reimagined/02-ARCHIVO/_capturas-etapa3";
const PIEZAS = [
  { k: "TRATADO", f: "TRATADO-envase-XHTML-2026-10-10.xhtml", deep: "art-d-007-contradicciones-resueltas-y-registro-d", sufijo: "decision-de-integracion-3" },
  { k: "MANUAL", f: "MANUAL-COMPLETO-envase-XHTML-2026-10-10.xhtml", deep: "ficha-a01-alucinacion-factual-pura-severidad-cri", sufijo: null },
  { k: "LECCIONES", f: "LECCIONES-ALEXIS-envase-XHTML-2026-10-10.xhtml", deep: "2026-09-15-vii-mejor-que-lo-que-precedio-nunca-p", sufijo: null },
  { k: "CIMIENTO", f: "CANON-CIMIENTO-envase-XHTML-2026-10-10.xhtml", deep: "pillars", sufijo: "puerta" },
  { k: "COMPENDIO", f: "COMPENDIO-INTEGRAL-envase-XHTML-2026-10-10.xhtml", deep: null, sufijo: null },
];
const term = "bandita";

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ args: ["--no-sandbox"] });
  const resumen = [];
  for (const p of PIEZAS) {
    const url = "file://" + path.join(BASE, p.f);
    const R = { pieza: p.k, errores: [], checks: {} };
    // ── escritorio
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 950 }, deviceScaleFactor: 2 });
    const pg = await ctx.newPage();
    pg.on("console", m => { if (m.type() === "error") R.errores.push("console: " + m.text().slice(0, 100)); });
    pg.on("pageerror", e => R.errores.push("pageerror: " + String(e).slice(0, 100)));
    pg.on("requestfailed", r => R.errores.push("reqfail: " + r.url().slice(0, 80)));
    await pg.goto(url, { waitUntil: "load" });
    await pg.waitForTimeout(500);
    R.checks.secciones = await pg.locator("section.sec").count();
    R.checks.tocLinks = await pg.locator("#toclist a").count();
    // deep-link directo a la ancla reparada (espera ACTIVA: el smooth-scroll de 500k px tarda)
    if (p.deep) {
      await pg.goto(url + "#" + p.deep);
      const ok = await pg.waitForFunction(id => {
        const e = document.getElementById(id);
        if (!e) return false;
        const r = e.getBoundingClientRect();
        return r.top > -60 && r.top < window.innerHeight;
      }, p.deep, { timeout: 8000 }).then(() => true).catch(() => false);
      R.checks.deeplink = ok ? "OK ✓" : "FALLO";
      if (!ok) R.errores.push("deeplink no visible: " + p.deep);
    }
    if (p.sufijo) {
      await pg.goto(url + "#" + p.sufijo);
      await pg.waitForFunction(id => {
        const e = document.getElementById(id);
        if (!e) return false;
        const r = e.getBoundingClientRect();
        return r.top > -60 && r.top < window.innerHeight;
      }, p.sufijo, { timeout: 8000 }).catch(() => {});
      R.checks.sufijado = (await pg.evaluate(id => !!document.getElementById(id), p.sufijo)) ? "OK ✓" : "FALLO";
    }
    // búsqueda
    await pg.click("#bsearch");
    await pg.fill("#sinput", term);
    await pg.waitForTimeout(500);
    R.checks.busqueda = await pg.evaluate(() => document.getElementById("sres").children.length);
    if (R.checks.busqueda < 1) R.errores.push("búsqueda sin resultados");
    // captura escritorio (con resultados de búsqueda visibles en TRATADO, normal en el resto)
    await pg.keyboard.press("Escape");
    await pg.waitForTimeout(300);
    await pg.screenshot({ path: path.join(OUT, p.k.toLowerCase() + "-escritorio-claro.png") });
    // tema: ciclar hasta DARK (el botón va auto→light→dark; desde claro, 1 clic no cambia visual)
    const antes = await pg.evaluate(() => getComputedStyle(document.body).backgroundColor);
    for (let i = 0; i < 3; i++) {
      const t = await pg.evaluate(() => document.documentElement.getAttribute("data-theme"));
      if (t === "dark") break;
      await pg.click("#btheme");
      await pg.waitForTimeout(250);
    }
    const despues = await pg.evaluate(() => getComputedStyle(document.body).backgroundColor);
    const esDark = await pg.evaluate(() => document.documentElement.getAttribute("data-theme"));
    R.checks.tema = (esDark === "dark" && antes !== despues) ? "OK ✓" : "FALLO";
    if (R.checks.tema !== "OK ✓") R.errores.push("tema no llegó a dark (bg inicial %s vs %s)" + antes + "→" + despues);
    await ctx.close();
    // ── móvil (oscuro)
    const mctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, colorScheme: "dark" });
    const mp = await mctx.newPage();
    mp.on("pageerror", e => R.errores.push("m-pageerror: " + String(e).slice(0, 100)));
    await mp.goto(url, { waitUntil: "load" });
    await mp.waitForTimeout(500);
    R.checks.overflowMv = await mp.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    if (R.checks.overflowMv > 1) R.errores.push("overflow horizontal móvil: " + R.checks.overflowMv + "px");
    await mp.screenshot({ path: path.join(OUT, p.k.toLowerCase() + "-movil-oscuro.png") });
    await mctx.close();
    R.veredicto = R.errores.length === 0 ? "LIMPIA ✓" : "CON ERRORES";
    resumen.push(R);
    console.log(JSON.stringify(R));
  }
  await browser.close();
  const limpias = resumen.filter(r => r.veredicto === "LIMPIA ✓").length;
  console.log("VEREDICTO 3.2+3.3: %d/5 piezas LIMPIAS en navegador real", limpias);
})().catch(e => { console.error("DRIVER ABORTA:", e); process.exit(1); });
