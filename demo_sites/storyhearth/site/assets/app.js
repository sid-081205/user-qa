// Shared StoryHearth front-end logic: accounts, session, navigation.
const SH = (() => {
  const SEED_ACCOUNTS = [
    { name: "Demo Family", email: "demo.family@storyhearth.test", password: "Bedtime-2026" },
  ];
  function accounts() {
    const extra = JSON.parse(localStorage.getItem("sh_accounts") || "[]");
    return SEED_ACCOUNTS.concat(extra);
  }
  function currentUser() {
    try { return JSON.parse(localStorage.getItem("sh_user") || "null"); } catch (e) { return null; }
  }
  function login(email, password) {
    const acc = accounts().find(a => a.email.toLowerCase() === String(email).trim().toLowerCase() && a.password === password);
    if (acc) { localStorage.setItem("sh_user", JSON.stringify({ name: acc.name, email: acc.email })); return true; }
    return false;
  }
  function signup(name, email, password) {
    const list = JSON.parse(localStorage.getItem("sh_accounts") || "[]");
    list.push({ name, email, password });
    localStorage.setItem("sh_accounts", JSON.stringify(list));
    localStorage.setItem("sh_user", JSON.stringify({ name, email }));
  }
  function logout() { localStorage.removeItem("sh_user"); location.href = "index.html"; }
  function requireLogin() {
    if (!currentUser()) {
      const next = location.pathname.split("/").pop() + location.search;
      location.replace("login.html?next=" + encodeURIComponent(next));
      return false;
    }
    return true;
  }
  function renderNav() {
    const el = document.getElementById("navlinks");
    if (!el) return;
    const u = currentUser();
    el.innerHTML = u
      ? '<a href="index.html#how">How it works</a><a href="pricing.html">Pricing</a><a href="dashboard.html">My books</a><a href="#" id="logout">Log out</a>'
      : '<a href="index.html#how">How it works</a><a href="pricing.html">Pricing</a><a class="pill" href="login.html">Log in</a>';
    const lo = document.getElementById("logout");
    if (lo) lo.addEventListener("click", e => { e.preventDefault(); logout(); });
  }
  function footer() {
    const f = document.getElementById("footer");
    if (f) f.innerHTML = '<div class="legal"><a href="privacy.html">Privacy</a><a href="privacy.html#terms">Terms</a><a href="mailto:hello@storyhearth.test">Contact</a> &copy; 2026 StoryHearth Ltd.</div>';
  }
  document.addEventListener("DOMContentLoaded", () => { renderNav(); footer(); });
  return { accounts, currentUser, login, signup, logout, requireLogin };
})();
