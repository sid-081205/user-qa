(args) => {
  // Serialises the visible page into an accessibility-tree-like text with numbered
  // interactive elements ("[12] button \"Continue\""), in reading order, marking the fold.
  // Also runs cheap deterministic accessibility/perception checks (WCAG 2.2).
  const MAX_TEXT = args.maxText || 9000;
  const ATTENTION = args.attention || "full"; // full | skim | low_vision
  const vw = window.innerWidth, vh = window.innerHeight;
  if (!window.__uqaNext) window.__uqaNext = 1;

  const SKIP = new Set(["SCRIPT", "STYLE", "NOSCRIPT", "TEMPLATE", "HEAD", "META", "LINK", "PATH", "DEFS"]);
  const BLOCK = new Set(["P", "DIV", "SECTION", "ARTICLE", "HEADER", "FOOTER", "MAIN", "NAV", "ASIDE", "LI", "UL", "OL",
    "TR", "TABLE", "FORM", "FIELDSET", "LEGEND", "BLOCKQUOTE", "FIGURE", "FIGCAPTION", "DL", "DT", "DD", "BR", "HR",
    "H1", "H2", "H3", "H4", "H5", "H6", "PRE", "DIALOG", "LABEL", "TD", "TH"]);
  const ROLES = new Set(["button", "link", "checkbox", "radio", "tab", "menuitem", "menuitemcheckbox", "menuitemradio",
    "option", "switch", "combobox", "textbox", "slider", "spinbutton", "searchbox", "treeitem"]);

  const lines = [];
  let cur = "";
  const flush = () => { const t = cur.replace(/\s+/g, " ").trim(); if (t) lines.push(t); cur = ""; };
  const elements = [];
  const images = [];
  const a11y = { images_missing_alt: [], unlabeled_fields: [], placeholder_only_fields: [], unnamed_controls: [],
    small_targets: [], low_contrast: [], tiny_text: [], checked_text_nodes: 0 };
  let foldMarked = false;
  const scrolled = window.scrollY > 10;

  function cssVisible(el) {
    return !el.checkVisibility || el.checkVisibility({ checkOpacity: false, checkVisibilityCSS: true });
  }
  function hasSize(el) {
    const r = el.getBoundingClientRect();
    return r.width >= 1 && r.height >= 1;
  }
  function visible(el) {
    return cssVisible(el) && hasSize(el);
  }
  function srOnly(el) {
    const r = el.getBoundingClientRect();
    if (r.width > 2 || r.height > 2) return false;
    const s = getComputedStyle(el);
    return s.overflow === "hidden" || s.clip !== "auto" || s.position === "absolute";
  }
  function transparentish(el) {
    const s = getComputedStyle(el);
    return parseFloat(s.opacity) < 0.05;
  }
  function textOf(el) {
    return (el.innerText || el.textContent || "").replace(/\s+/g, " ").trim();
  }
  function labelFor(el) {
    const al = el.getAttribute("aria-label");
    if (al && al.trim()) return al.trim();
    const lb = el.getAttribute("aria-labelledby");
    if (lb) {
      const t = lb.split(/\s+/).map(id => { const n = document.getElementById(id); return n ? textOf(n) : ""; }).join(" ").trim();
      if (t) return t;
    }
    if (el.labels && el.labels.length) {
      const t = Array.from(el.labels).map(textOf).join(" ").trim();
      if (t) return t;
    }
    return "";
  }
  function accName(el) {
    const tag = el.tagName;
    let n = labelFor(el);
    if (!n && (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT")) {
      n = el.getAttribute("title") || "";
    }
    if (!n && tag !== "INPUT" && tag !== "TEXTAREA" && tag !== "SELECT") n = textOf(el);
    if (!n) {
      const img = el.querySelector && el.querySelector("img[alt]");
      if (img) n = img.getAttribute("alt");
    }
    if (!n) n = el.getAttribute("title") || "";
    if (!n && tag === "INPUT" && ["submit", "button", "reset"].includes(el.type)) n = el.value || "";
    return (n || "").replace(/\s+/g, " ").trim();
  }
  function roleOf(el) {
    const r = (el.getAttribute("role") || "").toLowerCase();
    if (ROLES.has(r)) return r;
    const tag = el.tagName;
    if (tag === "A") return "link";
    if (tag === "BUTTON" || tag === "SUMMARY") return "button";
    if (tag === "SELECT") return "combobox";
    if (tag === "TEXTAREA") return "textbox";
    if (tag === "IFRAME") return "iframe";
    if (tag === "INPUT") {
      const t = (el.type || "text").toLowerCase();
      if (["submit", "button", "reset", "image"].includes(t)) return "button";
      if (t === "checkbox") return "checkbox";
      if (t === "radio") return "radio";
      if (t === "range") return "slider";
      if (t === "file") return "file-upload";
      if (t === "hidden") return null;
      return "textbox";
    }
    if (el.isContentEditable && el.getAttribute("contenteditable") !== null) return "textbox";
    return null;
  }
  function isInteractive(el) {
    if (roleOf(el)) return true;
    if (el.hasAttribute("onclick")) return true;
    const ti = el.getAttribute("tabindex");
    if (ti !== null && parseInt(ti) >= 0 && textOf(el).length > 0 && textOf(el).length < 120) return true;
    return false;
  }
  function pointerClickable(el) {
    // React-style <div onClick> detection: cursor:pointer on a leaf-ish element with short text.
    const s = getComputedStyle(el);
    if (s.cursor !== "pointer") return false;
    const p = el.parentElement;
    if (p && getComputedStyle(p).cursor === "pointer") return false;
    const t = textOf(el);
    return t.length > 0 && t.length < 100;
  }
  function parseColor(c) {
    const m = c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  }
  function lum(c) {
    const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  }
  function bgOf(el) {
    let n = el;
    while (n && n.nodeType === 1) {
      const s = getComputedStyle(n);
      if (s.backgroundImage && s.backgroundImage !== "none") return null; // unknown (image/gradient)
      const c = parseColor(s.backgroundColor);
      if (c && c.a > 0.5) return c;
      n = n.parentElement || (n.getRootNode && n.getRootNode().host);
    }
    return { r: 255, g: 255, b: 255, a: 1 };
  }
  function contrastOf(el) {
    const s = getComputedStyle(el);
    const fg = parseColor(s.color);
    const bg = bgOf(el);
    if (!fg || !bg) return null;
    const a = fg.a === undefined ? 1 : fg.a;
    const blended = { r: fg.r * a + bg.r * (1 - a), g: fg.g * a + bg.g * (1 - a), b: fg.b * a + bg.b * (1 - a) };
    const L1 = lum(blended), L2 = lum(bg);
    return (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
  }
  const perceptCache = new Map();
  function perception(el) {
    // Returns {ratio, size, large, faint}
    if (perceptCache.has(el)) return perceptCache.get(el);
    const s = getComputedStyle(el);
    const size = parseFloat(s.fontSize) || 16;
    const weight = parseInt(s.fontWeight) || 400;
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const ratio = contrastOf(el);
    const res = { ratio, size, large };
    perceptCache.set(el, res);
    return res;
  }
  function isFaint(pr) {
    return (pr.ratio !== null && pr.ratio < 3.0) || pr.size < 11;
  }
  function checkTextPerception(el, text, id) {
    const pr = perception(el);
    a11y.checked_text_nodes++;
    if (pr.ratio !== null && pr.ratio < (pr.large ? 3 : 4.5) && a11y.low_contrast.length < 40) {
      const entry = { text: text.trim().slice(0, 60), ratio: Math.round(pr.ratio * 100) / 100, font_px: pr.size };
      if (id) entry.id = id;
      a11y.low_contrast.push(entry);
    }
    if (pr.size < 12 && a11y.tiny_text.length < 30) a11y.tiny_text.push({ text: text.trim().slice(0, 60), font_px: pr.size });
    return pr;
  }
  function ancestorsDisplayed(el) {
    for (let n = el.parentElement; n; n = n.parentElement) {
      const s = getComputedStyle(n);
      if (s.display === "none" || s.visibility === "hidden") return false;
    }
    return true;
  }
  function targetBox(el) {
    // A label wrapping or pointing at a checkbox/radio is part of its click target (WCAG 2.5.8).
    let r = el.getBoundingClientRect();
    let w = r.width, h = r.height;
    if (el.labels) for (const l of el.labels) {
      const lr = l.getBoundingClientRect();
      if (lr.width * lr.height > w * h) { w = lr.width; h = lr.height; }
    }
    return { w, h };
  }
  function markFold(el) {
    if (foldMarked) return;
    const r = el.getBoundingClientRect();
    if (r.top >= vh) {
      flush();
      lines.push("----- fold: everything below needs scrolling -----");
      foldMarked = true;
    }
  }
  function skimText(t) {
    const words = t.split(" ");
    if (words.length <= 14) return t;
    return words.slice(0, 10).join(" ") + " …";
  }
  function assignId(el) {
    let id = el.getAttribute("data-uqa-id");
    if (!id) { id = String(window.__uqaNext++); el.setAttribute("data-uqa-id", id); }
    return parseInt(id);
  }
  function describe(el, role) {
    const tag = el.tagName;
    const id = assignId(el);
    const r = el.getBoundingClientRect();
    let name = accName(el).slice(0, 140);
    const states = [];
    const info = { id, role, tag: tag.toLowerCase(), name, bbox: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)] };
    if (tag === "INPUT" || tag === "TEXTAREA") {
      const t = (el.type || "text").toLowerCase();
      info.type = t;
      if (el.placeholder) info.placeholder = el.placeholder.slice(0, 80);
      if (t === "password") states.push(el.value ? `filled (${el.value.length} chars)` : "empty");
      else if (["checkbox", "radio"].includes(t)) {
        states.push(el.checked ? "checked" : "unchecked");
        if (el.value && el.value !== "on") info.value = el.value;
      } else if (t === "range") {
        states.push(`value ${el.value} (min ${el.min || 0}, max ${el.max || 100}, step ${el.step || 1})`);
      } else if (t === "file") {
        states.push(el.files && el.files.length ? `${el.files.length} file(s) chosen` : "no file chosen");
        if (el.accept) info.accept = el.accept;
      } else if (!["submit", "button", "reset", "image"].includes(t)) {
        const v = el.value || "";
        states.push(v ? `value "${v.slice(0, 120)}${v.length > 120 ? "…" : ""}" (${v.length} chars)` : "empty");
        if (el.maxLength > 0) info.maxlength = el.maxLength;
      }
      if (el.required) states.push("required");
      if (el.getAttribute("aria-invalid") === "true") states.push("invalid");
      if (el.placeholder && el.value) info.placeholderHidden = true;
    } else if (tag === "SELECT") {
      const opts = Array.from(el.options).slice(0, 25).map(o => (o.selected ? "*" : "") + o.text.trim().slice(0, 50));
      info.options = opts;
      states.push("selected: " + (el.selectedOptions[0] ? el.selectedOptions[0].text.trim() : "none"));
      if (el.required) states.push("required");
    } else if (tag === "A") {
      const href = el.getAttribute("href") || "";
      try {
        const u = new URL(href, location.href);
        info.href = u.origin === location.origin ? (u.pathname + u.search + u.hash) : u.href.slice(0, 80);
      } catch (e) { info.href = href.slice(0, 80); }
    } else if (tag === "IFRAME") {
      let src = el.getAttribute("src") || "";
      try { src = new URL(src, location.href).host; } catch (e) {}
      info.src = src;
      if (!name) info.name = name = (el.getAttribute("title") || "embedded frame");
    }
    for (const a of ["aria-expanded", "aria-pressed", "aria-selected", "aria-checked"]) {
      const v = el.getAttribute(a);
      if (v !== null) states.push(`${a.replace("aria-", "")}=${v}`);
    }
    if (el.disabled || el.getAttribute("aria-disabled") === "true") states.push("disabled");
    if (r.bottom < 0 || r.top > vh) states.push("offscreen");
    // Is it covered by something else (e.g. a modal/cookie banner)?
    const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
    if (cx >= 0 && cy >= 0 && cx < vw && cy < vh && r.width >= 4 && r.height >= 4) {
      const topEl = document.elementFromPoint(cx, cy);
      if (topEl && topEl !== el && !el.contains(topEl) && !(topEl.contains && topEl.contains(el)) && !(el.labels && Array.from(el.labels).some(l => l.contains(topEl)))) {
        states.push("covered");
      }
    }
    info.states = states;
    // accessibility checks
    if (!name && !["iframe"].includes(role)) {
      if (["textbox", "combobox", "slider", "checkbox", "radio", "file-upload"].includes(role)) {
        if (info.placeholder) a11y.placeholder_only_fields.push({ id, placeholder: info.placeholder });
        else a11y.unlabeled_fields.push({ id, role });
      } else {
        a11y.unnamed_controls.push({ id, role, tag: tag.toLowerCase() });
      }
    }
    if (["button", "link", "checkbox", "radio"].includes(role) && r.width > 0 && tag !== "A") {
      const tb = targetBox(el);
      if (tb.w < 24 || tb.h < 24) a11y.small_targets.push({ id, name: name.slice(0, 40), size: `${Math.round(tb.w)}x${Math.round(tb.h)}` });
    }
    let faint = false;
    if (["button", "link", "clickable", "tab", "menuitem"].includes(role) && textOf(el) && r.width > 0) {
      // Measure the element that actually paints the text (a link may wrap a styled button).
      const tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: n => n.textContent.trim() ? 1 : 3 });
      const tn = tw.nextNode();
      faint = isFaint(checkTextPerception(tn && tn.parentElement ? tn.parentElement : el, textOf(el), id));
    }
    elements.push(info);
    const bits = [`[${id}] ${role}`];
    if (ATTENTION === "low_vision" && faint) bits.push("[faint/small text you cannot make out]");
    else bits.push(name ? `"${name}"` : "(no label)");
    if (info.placeholder) bits.push(info.placeholderHidden ? `(its placeholder "${info.placeholder}" is no longer shown because the box has text)` : `placeholder "${info.placeholder}"`);
    if (info.href) bits.push(`-> ${info.href}`);
    if (info.src) bits.push(`src ${info.src}`);
    if (info.options) bits.push(`options [${info.options.join(" | ")}]`);
    if (info.accept) bits.push(`accepts ${info.accept}`);
    if (states.length) bits.push(`(${states.join(", ")})`);
    return bits.join(" ");
  }

  function walk(node, depth) {
    if (!node) return;
    if (node.nodeType === 3) {
      const p = node.parentElement;
      const t = node.textContent.replace(/\s+/g, " ");
      if (!t.trim() || !p) return;
      const pr = checkTextPerception(p, t);
      if (ATTENTION === "low_vision" && isFaint(pr)) {
        cur += " [faint/small text you cannot make out] ";
        return;
      }
      cur += t;
      return;
    }
    if (node.nodeType !== 1) return;
    const el = node;
    const tag = el.tagName;
    if (SKIP.has(tag)) return;
    if (el.getAttribute("aria-hidden") === "true" && !el.querySelector("input,button,a,select,textarea")) return;
    const role = roleOf(el);
    const shown = cssVisible(el);
    const sized = hasSize(el);
    // Visually hidden radios/checkboxes/file inputs are still operable through their labels.
    const hiddenOperable = tag === "INPUT" && ["radio", "checkbox", "file"].includes((el.type || "").toLowerCase()) && (!shown || !sized || srOnly(el));
    if (!shown && !hiddenOperable) return;
    if (!hiddenOperable && sized && srOnly(el)) return; // screen-reader-only text is invisible to sighted users
    if (!sized && !hiddenOperable && getComputedStyle(el).display !== "contents") {
      // zero-size wrapper: its (absolutely positioned / overflowing) children may still be visible
      for (const c of el.childNodes) if (c.nodeType === 1) walk(c, depth + 1);
      return;
    }
    if (tag === "svg" || tag === "SVG") {
      const t = el.getAttribute("aria-label") || (el.querySelector("title") ? el.querySelector("title").textContent : "");
      const r = el.getBoundingClientRect();
      if (r.width >= 120 && r.height >= 90) { flush(); lines.push(`[picture${t ? ": " + t.trim().slice(0, 100) : ""} ${Math.round(r.width)}x${Math.round(r.height)}]`); }
      return;
    }
    markFold(el);
    if (tag === "IMG" || tag === "CANVAS" || tag === "VIDEO") {
      const r = el.getBoundingClientRect();
      if (r.width >= 40 && r.height >= 40) {
        const alt = el.getAttribute("alt");
        const decorative = alt === "" || el.getAttribute("role") === "presentation";
        const src = (el.currentSrc || el.src || "").slice(0, 200);
        images.push({ tag: tag.toLowerCase(), alt, src, w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y + window.scrollY) });
        if (alt === null && tag === "IMG" && a11y.images_missing_alt.length < 30) a11y.images_missing_alt.push({ src: src.slice(-60), size: `${Math.round(r.width)}x${Math.round(r.height)}` });
        flush();
        lines.push(`[${tag === "IMG" ? "image" : tag.toLowerCase()}${alt ? ': "' + alt.slice(0, 100) + '"' : decorative ? " (decorative)" : " (no description)"} ${Math.round(r.width)}x${Math.round(r.height)}]`);
      }
      return;
    }
    const isHeading = /^H[1-6]$/.test(tag);
    if (tag === "LABEL" && el.control && el.contains(el.control) && ["radio", "checkbox"].includes((el.control.type || "").toLowerCase())) {
      flush();
      lines.push(describe(el.control, roleOf(el.control)));
      return;
    }
    const interactive = role || isInteractive(el) || (!isHeading && pointerClickable(el));
    if (interactive) {
      flush();
      let line = describe(el, role || "clickable");
      if (ATTENTION === "skim") line = line.replace(/"([^"]{90,})"/, (m, g) => `"${skimText(g)}"`);
      lines.push(line);
      if (tag === "IFRAME") return;
      // descend only into containers that hold other controls (e.g. a card link wrapping buttons is rare)
      if (el.querySelector && el.querySelector("input,select,textarea,button")) {
        for (const c of el.childNodes) if (c.nodeType === 1) walkControlsOnly(c);
      }
      return;
    }
    if (isHeading) {
      flush();
      const t = textOf(el);
      if (t) {
        const pr = perception(el);
        if (ATTENTION === "low_vision" && pr.ratio !== null && pr.ratio < 3.0) lines.push("#".repeat(parseInt(tag[1])) + " [faint heading you cannot make out]");
        else lines.push("#".repeat(parseInt(tag[1])) + " " + t.slice(0, 200));
      }
      for (const c of el.querySelectorAll("a,button")) if (visible(c)) lines.push(describe(c, roleOf(c) || "clickable"));
      return;
    }
    const block = BLOCK.has(tag);
    if (block) flush();
    if (tag === "LI") cur += "- ";
    const sr = el.shadowRoot;
    for (const c of (sr ? sr.childNodes : el.childNodes)) walk(c, depth + 1);
    if (sr) for (const c of el.childNodes) walk(c, depth + 1);
    if (block) {
      if (ATTENTION === "skim") cur = skimText(cur.replace(/\s+/g, " ").trim());
      flush();
    }
  }
  function walkControlsOnly(node) {
    if (node.nodeType !== 1) return;
    const role = roleOf(node);
    if (role && (visible(node) || (node.tagName === "INPUT" && ["radio", "checkbox", "file"].includes(node.type)))) {
      lines.push("  " + describe(node, role));
      return;
    }
    for (const c of node.childNodes) walkControlsOnly(c);
  }

  if (scrolled) lines.push(`(page scrolled to ${Math.round(window.scrollY)}px; content above is out of view)`);
  walk(document.body, 0);
  flush();

  // Hidden file inputs are commonly triggered by a styled button; expose them explicitly.
  document.querySelectorAll("input[type=file]").forEach(el => {
    if (!ancestorsDisplayed(el)) return;
    if (!el.getAttribute("data-uqa-id") || !elements.find(e => e.id === parseInt(el.getAttribute("data-uqa-id")))) {
      lines.push(describe(el, "file-upload") + " (hidden file input; use upload action)");
    }
  });

  // WCAG 2.5.8 spacing exception: an undersized target passes if a 24px circle on its centre touches no other target.
  const byId = new Map(elements.map(e => [e.id, e]));
  const small = new Set(a11y.small_targets.map(t => t.id));
  for (const t of a11y.small_targets) {
    const e = byId.get(t.id);
    const [x, y, w, h] = e.bbox, cx = x + w / 2, cy = y + h / 2;
    t.spacing_ok = !elements.some(o => {
      if (o.id === t.id || !o.bbox || o.bbox[2] <= 0) return false;
      const [ox, oy, ow, oh] = o.bbox;
      if (small.has(o.id)) return Math.hypot(ox + ow / 2 - cx, oy + oh / 2 - cy) < 24;
      const dx = Math.max(ox - cx, 0, cx - (ox + ow)), dy = Math.max(oy - cy, 0, cy - (oy + oh));
      return Math.hypot(dx, dy) < 12;
    });
  }

  // Dedupe consecutive identical lines and cap length.
  const out = [];
  for (const l of lines) if (out[out.length - 1] !== l) out.push(l);
  let text = out.join("\n");
  const truncated = text.length > MAX_TEXT;
  if (truncated) text = text.slice(0, MAX_TEXT) + "\n… (page text truncated)";

  const headings = Array.from(document.querySelectorAll("h1,h2,[role=heading]")).filter(visible).slice(0, 6).map(h => textOf(h).slice(0, 80));
  const dialogs = Array.from(document.querySelectorAll("dialog[open],[role=dialog],[role=alertdialog],[aria-modal=true]")).filter(visible).map(d => (d.getAttribute("aria-label") || textOf(d)).slice(0, 80));
  const fullText = (document.body.innerText || "").replace(/\n{3,}/g, "\n\n");
  return {
    url: location.href,
    title: document.title,
    lang: document.documentElement.getAttribute("lang") || "",
    viewport: { w: vw, h: vh, scrollY: Math.round(window.scrollY), scrollHeight: document.documentElement.scrollHeight },
    text, truncated, elements, images, headings, dialogs, a11y,
    fullTextLength: fullText.length,
    fullText: args.includeFullText ? fullText.slice(0, 60000) : undefined,
  };
}
