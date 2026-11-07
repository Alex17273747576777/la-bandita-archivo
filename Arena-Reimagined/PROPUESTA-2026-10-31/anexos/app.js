/* La Bandita · propuesta — comportamiento de la página
   Todo local: sin red, sin dependencias. Cada cosa que falla falla en silencio
   y no se lleva por delante la lectura. */
(function () {
  "use strict";

  var doc = document.documentElement;

  /* ---------- almacenamiento defensivo (la lección del módulo de referencia) ---------- */
  function leer(clave, porDefecto) {
    try { var v = localStorage.getItem(clave); return v === null ? porDefecto : v; }
    catch (e) { return porDefecto; }
  }
  function guardar(clave, valor) {
    try { localStorage.setItem(clave, valor); } catch (e) { /* modo privado o cuota llena */ }
  }

  /* ---------- sonido sintetizado, apagado por defecto ---------- */
  var audioCtx = null, sonidoOn = leer("lbSonido", "0") === "1";
  function tono(f1, f2) {
    if (!sonidoOn) return;
    try {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return;
      if (!audioCtx) audioCtx = new AC();
      if (audioCtx.state === "suspended") { audioCtx.resume().catch(function () {}); }
      var t = audioCtx.currentTime;
      var osc = audioCtx.createOscillator(), gan = audioCtx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(f1, t);
      osc.frequency.exponentialRampToValueAtTime(f2, t + 0.09);
      gan.gain.setValueAtTime(0.0001, t);
      gan.gain.exponentialRampToValueAtTime(0.06, t + 0.012);
      gan.gain.exponentialRampToValueAtTime(0.0001, t + 0.13);
      osc.connect(gan); gan.connect(audioCtx.destination);
      osc.start(t); osc.stop(t + 0.15);
    } catch (e) { /* sin audio, no pasa nada */ }
  }
  var botonSonido = document.getElementById("sonidoBtn");
  function pintarSonido() {
    if (!botonSonido) return;
    botonSonido.setAttribute("aria-pressed", sonidoOn ? "true" : "false");
    botonSonido.title = sonidoOn ? "Sonido activo" : "Sonido apagado";
  }
  if (botonSonido) {
    botonSonido.addEventListener("click", function () {
      sonidoOn = !sonidoOn; guardar("lbSonido", sonidoOn ? "1" : "0"); pintarSonido(); tono(520, 760);
    });
  }
  pintarSonido();

  /* ---------- paletas ---------- */
  var menu = document.getElementById("paletaMenu");
  var botonPaleta = document.getElementById("paletaBtn");
  var PALETAS = ["cana", "malecon", "azucar", "fogata", "tinta", "amoled"];
  var paleta = leer("lbPaleta", "cana");
  if (PALETAS.indexOf(paleta) === -1) paleta = "cana";
  doc.setAttribute("data-paleta", paleta);

  function cerrarMenu() {
    if (!menu || !botonPaleta) return;
    menu.classList.remove("abierto");
    botonPaleta.setAttribute("aria-expanded", "false");
  }
  if (botonPaleta && menu) {
    botonPaleta.addEventListener("click", function (ev) {
      ev.stopPropagation();
      var abierto = menu.classList.toggle("abierto");
      botonPaleta.setAttribute("aria-expanded", abierto ? "true" : "false");
      tono(640, 900);
    });
    menu.addEventListener("click", function (ev) {
      var b = ev.target.closest ? ev.target.closest("button[data-paleta]") : null;
      if (!b) return;
      paleta = b.getAttribute("data-paleta");
      doc.setAttribute("data-paleta", paleta);
      guardar("lbPaleta", paleta);
      cerrarMenu(); tono(660, 990);
    });
    document.addEventListener("click", function (ev) {
      if (menu.classList.contains("abierto") && !menu.contains(ev.target) && ev.target !== botonPaleta) cerrarMenu();
    });
    document.addEventListener("keydown", function (ev) { if (ev.key === "Escape") cerrarMenu(); });
  }

  /* ---------- barra de progreso ---------- */
  var barra = document.getElementById("progreso");
  function progreso() {
    if (!barra) return;
    var alto = document.documentElement.scrollHeight - window.innerHeight;
    var pct = alto > 0 ? (window.scrollY / alto) * 100 : 0;
    barra.style.width = Math.min(100, Math.max(0, pct)) + "%";
  }

  /* ---------- navegación activa ---------- */
  var enlaces = Array.prototype.slice.call(document.querySelectorAll("[data-target]"));
  var secciones = enlaces.map(function (a) { return document.getElementById(a.getAttribute("data-target")); });
  function marcarActivo(id) {
    enlaces.forEach(function (a) {
      a.classList.toggle("activo", a.getAttribute("data-target") === id);
    });
  }
  if ("IntersectionObserver" in window) {
    var observador = new IntersectionObserver(function (entradas) {
      var visibles = entradas.filter(function (e) { return e.isIntersecting; });
      if (!visibles.length) return;
      visibles.sort(function (a, b) { return b.intersectionRatio - a.intersectionRatio; });
      marcarActivo(visibles[0].target.id);
    }, { rootMargin: "-88px 0px -62% 0px", threshold: [0.01, 0.25, 0.6] });
    secciones.forEach(function (s) { if (s) observador.observe(s); });
  }
  enlaces.forEach(function (a) { a.addEventListener("click", function () { tono(520, 700); }); });

  /* ---------- búsqueda con resaltado ---------- */
  var buscador = document.getElementById("buscador");
  var input = document.getElementById("buscarInput");
  var cuenta = document.getElementById("buscarCuenta");
  var marcas = [];

  function limpiarMarcas() {
    marcas.forEach(function (m) {
      var padre = m.parentNode;
      if (!padre) return;
      padre.replaceChild(document.createTextNode(m.textContent), m);
      padre.normalize();
    });
    marcas = [];
  }

  function buscar(texto) {
    limpiarMarcas();
    if (!texto || texto.length < 2) { if (cuenta) cuenta.textContent = "0"; return; }
    var raiz = document.getElementById("contenido");
    if (!raiz) return;
    var patron = new RegExp(texto.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi");
    var caminante = document.createTreeWalker(raiz, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        if (!p || /^(SCRIPT|STYLE|MARK)$/.test(p.nodeName)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodos = [], n;
    while ((n = caminante.nextNode())) nodos.push(n);
    nodos.forEach(function (nodo) {
      var val = nodo.nodeValue;
      if (!patron.test(val)) return;
      patron.lastIndex = 0;
      var frag = document.createDocumentFragment(), ultimo = 0, m;
      while ((m = patron.exec(val))) {
        if (m.index > ultimo) frag.appendChild(document.createTextNode(val.slice(ultimo, m.index)));
        var el = document.createElement("mark");
        el.textContent = m[0];
        frag.appendChild(el); marcas.push(el);
        ultimo = m.index + m[0].length;
        if (m[0].length === 0) patron.lastIndex++;
        if (marcas.length > 600) break;
      }
      if (ultimo < val.length) frag.appendChild(document.createTextNode(val.slice(ultimo)));
      nodo.parentNode.replaceChild(frag, nodo);
    });
    if (cuenta) cuenta.textContent = String(marcas.length);
    if (marcas.length) {
      marcas[0].classList.add("actual");
      var caja = marcas[0].closest(".tarjeta, .hero");
      if (caja) caja.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  var botonBuscar = document.getElementById("buscarBtn");
  var cerrarBuscar = document.getElementById("buscarCerrar");
  if (botonBuscar && buscador && input) {
    botonBuscar.addEventListener("click", function () {
      var oculto = buscador.hasAttribute("hidden");
      if (oculto) { buscador.removeAttribute("hidden"); input.focus(); }
      else { buscador.setAttribute("hidden", ""); limpiarMarcas(); }
      tono(600, 840);
    });
    var temporizador = null;
    input.addEventListener("input", function () {
      clearTimeout(temporizador);
      var v = input.value.trim();
      temporizador = setTimeout(function () { buscar(v); }, 180);
    });
  }
  if (cerrarBuscar) {
    cerrarBuscar.addEventListener("click", function () {
      if (buscador) buscador.setAttribute("hidden", "");
      limpiarMarcas(); if (cuenta) cuenta.textContent = "0";
    });
  }
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" && buscador && !buscador.hasAttribute("hidden")) {
      buscador.setAttribute("hidden", ""); limpiarMarcas(); if (cuenta) cuenta.textContent = "0";
    }
    if ((ev.ctrlKey || ev.metaKey) && ev.key.toLowerCase() === "k") {
      ev.preventDefault();
      if (buscador && input) { buscador.removeAttribute("hidden"); input.focus(); }
    }
  });

  /* ---------- desplazamiento ---------- */
  var pendiente = false;
  window.addEventListener("scroll", function () {
    if (pendiente) return;
    pendiente = true;
    window.requestAnimationFrame(function () { progreso(); pendiente = false; });
  }, { passive: true });
  window.addEventListener("resize", progreso, { passive: true });
  progreso();
  marcarActivo("inicio");
})();
