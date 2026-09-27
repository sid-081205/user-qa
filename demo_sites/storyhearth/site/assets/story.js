// StoryHearth "AI" story generator (deterministic templates + SVG illustrations).
const StoryHearth = (() => {
  const cap = s => (s || "").charAt(0).toUpperCase() + (s || "").slice(1);
  const esc = s => String(s || "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  function pron(p) {
    if (p === "she") return { s: "she", o: "her", pp: "her" };
    if (p === "he") return { s: "he", o: "him", pp: "his" };
    return { s: "they", o: "them", pp: "their" };
  }
  const otherPron = p => (p === "she" ? "he" : "she");
  const variant = name => (name.length > 3 ? name.slice(0, -1) : name + "n");
  const COLOURS = [["blond", "#f2d16b"], ["strawberry", "#e8a86b"], ["ginger", "#c8642b"], ["red", "#b5452b"], ["black", "#1f1b18"],
    ["dark", "#2d2420"], ["brown", "#6b4226"], ["grey", "#9ca3af"], ["silver", "#cbd5e1"], ["white", "#f3f4f6"]];
  function hair(looks) {
    const m = (looks || "").toLowerCase();
    for (const [k, c] of COLOURS) if (m.includes(k)) return c;
    return "#6b4226";
  }
  const contrastHair = c => (["#f2d16b", "#e8a86b", "#f3f4f6", "#cbd5e1"].includes(c) ? "#1f1b18" : "#f2d16b");
  function objColour(o) {
    const m = (o || "").toLowerCase();
    for (const [k, c] of [["blue", "#2563eb"], ["red", "#dc2626"], ["purple", "#7c3aed"], ["green", "#16a34a"], ["yellow", "#facc15"], ["grey", "#9ca3af"], ["gray", "#9ca3af"], ["pink", "#ec4899"], ["orange", "#f97316"], ["brown", "#92400e"]])
      if (m.includes(k)) return c;
    return "#f59e0b";
  }

  // ---------- SVG building blocks
  function sky(kind) {
    const g = { day: ["#bfe3ff", "#eaf6ff"], evening: ["#6d28d9", "#fb923c"], dusk: ["#475569", "#fcd34d"], night: ["#0f172a", "#1e293b"], sunset: ["#f97316", "#fde68a"] }[kind];
    return `<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${g[0]}"/><stop offset="1" stop-color="${g[1]}"/></linearGradient></defs><rect width="640" height="420" fill="url(#sky)"/>`;
  }
  const sun = () => `<circle cx="540" cy="80" r="44" fill="#fbbf24"/><g stroke="#fbbf24" stroke-width="6">${[0, 45, 90, 135, 180, 225, 270, 315].map(a => { const r = a * Math.PI / 180; return `<line x1="${540 + 56 * Math.cos(r)}" y1="${80 + 56 * Math.sin(r)}" x2="${540 + 72 * Math.cos(r)}" y2="${80 + 72 * Math.sin(r)}"/>`; }).join("")}</g>`;
  const moon = () => `<circle cx="540" cy="80" r="36" fill="#f1f5f9"/><circle cx="556" cy="70" r="32" fill="#0f172a"/>`;
  const stars = () => [60, 140, 230, 330, 420, 480, 600, 90, 380].map((x, i) => `<circle cx="${x}" cy="${30 + (i * 37) % 120}" r="2.5" fill="#fff"/>`).join("");
  function ground(place, dark) {
    const p = (place || "").toLowerCase();
    let s = "";
    const green = dark ? "#14532d" : "#86b386";
    if (/hill|mountain|field|fields/.test(p)) s += `<path d="M0 300 Q220 190 420 290 T640 270 V420 H0Z" fill="${green}"/>`;
    else s += `<rect y="300" width="640" height="120" fill="${green}"/>`;
    if (/lake|river|sea|beach|water|pond/.test(p)) s += `<path d="M0 340 Q160 325 320 342 T640 336 V420 H0Z" fill="${dark ? "#1e3a8a" : "#60a5fa"}"/>`;
    if (/farm|house|home|school|shed|workshop|room|cottage/.test(p)) s += `<g><rect x="60" y="215" width="120" height="95" fill="${dark ? "#44403c" : "#fef3c7"}" stroke="#78350f" stroke-width="3"/><path d="M50 220 L120 165 L190 220Z" fill="#b45309"/><rect x="105" y="255" width="30" height="55" fill="#78350f"/></g>`;
    if (/park|garden|wood|forest|tree|field/.test(p) || dark) s += [470, 520, 590].map((x, i) => `<rect x="${x - 6}" y="${230 - i * 6}" width="12" height="80" fill="#78350f"/><circle cx="${x}" cy="${215 - i * 6}" r="${34 + i * 4}" fill="${dark ? "#052e16" : "#4d7c0f"}"/>`).join("");
    if (/rocket|moon|space/.test(p)) s += `<g><rect x="80" y="170" width="46" height="130" rx="20" fill="#d6d3d1" stroke="#57534e" stroke-width="3"/><path d="M80 190 L103 140 L126 190Z" fill="#dc2626"/><circle cx="103" cy="215" r="10" fill="#93c5fd"/></g>`;
    if (/lantern|festival/.test(p)) s += [120, 220, 330, 430].map((x, i) => `<g><line x1="${x}" y1="0" x2="${x}" y2="${60 + i * 12}" stroke="#78350f"/><ellipse cx="${x}" cy="${78 + i * 12}" rx="16" ry="20" fill="#ef4444"/></g>`).join("");
    return s;
  }
  function child(x, y, hairC, shirt, label, scale = 1) {
    const s = scale;
    return `<g transform="translate(${x},${y}) scale(${s})"><rect x="-16" y="30" width="32" height="46" rx="12" fill="${shirt}"/><rect x="-12" y="74" width="9" height="28" fill="#374151"/><rect x="3" y="74" width="9" height="28" fill="#374151"/><circle cx="0" cy="12" r="20" fill="#f1c7a3"/><path d="M-21 8 Q0 -22 21 8 Q12 -4 0 -2 Q-12 -4 -21 8Z" fill="${hairC}"/><circle cx="-7" cy="12" r="2.4" fill="#111"/><circle cx="7" cy="12" r="2.4" fill="#111"/><path d="M-6 21 Q0 26 6 21" stroke="#111" stroke-width="2" fill="none"/></g>` +
      (label ? `<text x="${x}" y="${y + 122 * s}" font-family="Georgia" font-size="${16 * s}" text-anchor="middle" fill="#1f2937">${esc(label)}</text>` : "");
  }
  function adult(x, y, label, beard) {
    return `<g transform="translate(${x},${y})"><rect x="-20" y="34" width="40" height="70" rx="14" fill="#1d4ed8"/><rect x="-15" y="100" width="12" height="40" fill="#1f2937"/><rect x="3" y="100" width="12" height="40" fill="#1f2937"/><circle cx="0" cy="12" r="23" fill="#e8b48f"/><path d="M-23 6 Q0 -22 23 6Z" fill="#57534e"/>${beard ? '<path d="M-14 22 Q0 40 14 22 Q0 30 -14 22Z" fill="#57534e"/>' : ""}<circle cx="-8" cy="11" r="2.6" fill="#111"/><circle cx="8" cy="11" r="2.6" fill="#111"/><rect x="26" y="40" width="14" height="20" rx="3" fill="#fde047" stroke="#a16207"/></g><text x="${x}" y="${y + 162}" font-family="Georgia" font-size="16" text-anchor="middle" fill="#1f2937">${esc(label)}</text>`;
  }
  function objectIcon(x, y, name, colourOverride) {
    const n = (name || "").toLowerCase();
    const c = colourOverride || objColour(n);
    let shape;
    if (/kite/.test(n)) shape = `<path d="M0 -34 L24 0 L0 34 L-24 0Z" fill="${c}" stroke="#1f2937" stroke-width="2"/><path d="M0 34 q10 18 -4 30 q-12 12 4 26" stroke="#1f2937" fill="none" stroke-width="2"/>`;
    else if (/balloon/.test(n)) shape = `<ellipse cx="0" cy="-10" rx="22" ry="28" fill="${c}"/><path d="M0 18 q8 16 -4 30 q-10 12 2 24" stroke="#1f2937" fill="none" stroke-width="2"/>`;
    else if (/stone|pebble|rock/.test(n)) shape = `<ellipse cx="0" cy="0" rx="22" ry="15" fill="${c === "#f59e0b" ? "#9ca3af" : c}" stroke="#4b5563" stroke-width="2"/>`;
    else if (/lantern/.test(n)) shape = `<ellipse cx="0" cy="0" rx="18" ry="24" fill="${c}"/><rect x="-6" y="-30" width="12" height="7" fill="#78350f"/>`;
    else if (/sock/.test(n)) shape = `<path d="M-8 -30 h18 v34 q0 14 -14 14 h-16 q-8 0 -8 -8 q0 -8 10 -10 h10z" fill="${c}"/>`;
    else if (/horse|dinosaur|dino/.test(n)) shape = `<rect x="-26" y="-12" width="44" height="22" rx="10" fill="${/horse/.test(n) ? "#92400e" : c}"/><circle cx="22" cy="-18" r="10" fill="${/horse/.test(n) ? "#92400e" : c}"/><rect x="-22" y="8" width="6" height="18" fill="#57534e"/><rect x="8" y="8" width="6" height="18" fill="#57534e"/>`;
    else shape = `<path d="M0 -26 L7 -8 L26 -8 L11 4 L17 24 L0 12 L-17 24 L-11 4 L-26 -8 L-7 -8Z" fill="${c}"/>`;
    return `<g transform="translate(${x},${y})">${shape}</g>`;
  }
  const rain = () => `<g fill="#64748b"><ellipse cx="160" cy="70" rx="80" ry="32"/><ellipse cx="240" cy="60" rx="70" ry="30"/><ellipse cx="420" cy="80" rx="90" ry="34"/></g><g stroke="#60a5fa" stroke-width="3">${Array.from({ length: 36 }, (_, i) => `<line x1="${30 + i * 17}" y1="${110 + (i % 5) * 18}" x2="${24 + i * 17}" y2="${128 + (i % 5) * 18}"/>`).join("")}</g>`;
  const svg = (inner, label) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 420" role="img" aria-label="${esc(label)}">${inner}</svg>`;

  // ---------- story generation
  function generate(inp) {
    const H = cap(inp.hero);
    const P = pron(inp.pronoun);
    const place = inp.place;
    const obj = inp.object;
    const hc = hair(inp.looks);
    const shirt = "#0f766e";
    const title = `The Magical Adventrue of ${H}`;
    const pages = [];
    pages.push({ kind: "cover", title, subtitle: "A StoryHearth original", info: "Illustration style: Pop-art comic",
      svg: svg(sky("day") + sun() + ground(place) + child(320, 190, hc, shirt, H, 1.3) + objectIcon(430, 250, obj) +
        `<text x="320" y="70" font-family="Georgia" font-size="30" text-anchor="middle" fill="#7c2d12">${esc(title)}</text>`, "Cover") });
    pages.push({ kind: "dedication", text: "For {{recipient_name}}, with love from {{sender_name}}" });
    pages.push({ kind: "page", text: `Once upon a time, in ${place}, there lived a curious child named ${H}. ${H} was ${inp.age} years old and loved nothing more than ${obj}.`,
      svg: svg(sky("day") + sun() + ground(place) + child(300, 190, hc, shirt, H) + objectIcon(380, 250, obj), `${H} at ${place}`) });
    pages.push({ kind: "page", text: `One evening ${H} gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.`,
      svg: svg(sky("evening") + stars() + ground(place) + child(320, 190, hc, shirt, H), `${H} looking at the evening sky`) });
    pages.push({ kind: "page", text: `Then the rain began to pour. Big grey drops splashed into the puddles as ${variant(H)} pulled up ${P.pp} hood and ran for shelter, holding ${obj} tight.`,
      svg: svg(sky("day") + sun() + ground(place) + child(300, 190, hc, shirt, H) + objectIcon(370, 250, obj), `${H} outside`) });
    pages.push({ kind: "page", text: `Suddenly, Uncle Bartholomew appeared with a lantern. "${H}, follow me!" he called, and ${otherPron(inp.pronoun)} followed him along the winding path.`,
      svg: svg(sky("dusk") + ground(place) + adult(230, 150, "Uncle Bartholomew", true) + child(360, 190, contrastHair(hc), shirt, H), `${H} and Uncle Bartholomew`) });
    pages.push({ kind: "page", text: `Deep in the woods, the shadows grew teeth and whispered that no one would ever find ${H} again. ${H} clutched a shiny red balloon and trembled in the dark.`,
      svg: svg(sky("night") + moon() + stars() + ground("forest", true) + child(300, 190, hc, shirt, H) + objectIcon(370, 175, "balloon", "#dc2626"), `${H} in the dark woods`) });
    pages.push({ kind: "page", text: `Once upon a time, in ${place}, there lived a curious child named ${H}. At last the sun came out, and ${H} skipped all the way home, happier than ever.`,
      svg: svg(sky("day") + sun() + ground(place) + child(320, 190, hc, shirt, H), `${H} going home`) });
    pages.push({ kind: "end", text: `And from that day on, whenever ${H} looked up at the sky, ${P.s} would always remember`,
      svg: svg(sky("sunset") + ground(place) + child(320, 190, hc, shirt, H) + `<text x="320" y="80" font-family="Georgia" font-size="40" text-anchor="middle" fill="#7c2d12">The End</text>`, "The End") });
    return { title, pages, created: new Date().toISOString(), level: inp.level, style: inp.style };
  }
  return { generate };
})();
