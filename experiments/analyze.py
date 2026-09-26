"""Aggregate scored suites into the tables, figures and numbers used in the paper.

    python experiments/analyze.py --main runs/suite/main [--xmodel runs/suite/xmodel] [--out paper/generated]

Reads every run's summary.json and gt_scores.json (run experiments/score_ground_truth.py first), plus the
paired re-assessments gt_scores.{vision,vision2,novision}.json when present, and writes results.json,
numbers.tex, LaTeX tables (tables/*.tex) and figures (figures/*.pdf + .png).
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import re
import statistics as st
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
GT = json.loads((ROOT / "demo_sites/storyhearth/ground_truth.json").read_text())
DEFECTS = GT["defects"]
UX = [d["id"] for d in DEFECTS if d["kind"] == "ux"]
OUT = [d["id"] for d in DEFECTS if d["kind"] == "output"]
PERSONA_ORDER = ["grandparent_storykeeper", "tech_savvy_parent", "busy_parent_mobile", "esl_parent", "low_vision_senior",
                 "privacy_conscious_parent", "generic_user"]
SHORT = {"grandparent_storykeeper": "Grandparent", "tech_savvy_parent": "Tech-savvy", "busy_parent_mobile": "Busy/mobile",
         "esl_parent": "ESL", "low_vision_senior": "Low vision", "privacy_conscious_parent": "Privacy", "generic_user": "Generic (ablation)"}


def load_suite(path: Path, variant: str = "") -> list[dict]:
    runs = []
    for d in sorted(Path(path).glob(f"*/gt_scores{'.' + variant if variant else ''}.json")):
        rd = d.parent
        g = json.loads(d.read_text())
        s = json.loads((rd / "summary.json").read_text()) if (rd / "summary.json").exists() else {}
        trace = [json.loads(ln) for ln in (rd / "trace.jsonl").read_text().splitlines()] if (rd / "trace.jsonl").exists() else []
        runs.append({"dir": rd, "g": g, "s": s, "trace": trace, "persona": g.get("persona") or s.get("persona")})
    return runs


def mean_sd(xs: list) -> tuple[float | None, float | None]:
    xs = [x for x in xs if isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))]
    if not xs:
        return None, None
    return st.mean(xs), (st.stdev(xs) if len(xs) > 1 else None)


def num(x: float, digits: int = 2) -> str:
    s = f"{x:.{digits}f}"
    return "$-$" + s[1:] if s.startswith("-") else s


def fmt(m, sd=None, digits=2) -> str:
    if m is None:
        return "--"
    return num(m, digits) + (f" $\\pm$ {sd:.{digits}f}" if sd is not None else "")


def detected(run: dict, method: str = "judge") -> set[str]:
    g = run["g"][method]
    return set(g["ux"]["detected"]) | set(g["output"]["detected"])


def mcnemar_exact(b: int, c: int) -> float:
    """Two-sided exact McNemar test on the discordant pair counts (also the exact sign test for b wins vs c losses)."""
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)


def permutation_test_means(x: list[float], y: list[float]) -> float:
    """Exact two-sided permutation test for a difference in means, over every split of the pooled sample."""
    pooled, n = x + y, len(x)
    obs, total = abs(st.mean(x) - st.mean(y)), sum(pooled)
    hits = count = 0
    for idx in itertools.combinations(range(len(pooled)), n):
        sx = sum(pooled[i] for i in idx)
        count += 1
        hits += abs(sx / n - (total - sx) / (len(pooled) - n)) >= obs - 1e-12
    return hits / count


def label_permutation_test(sets: list[set], labels: list[str], perms: int = 20000, seed: int = 0) -> dict:
    """Do runs of the same persona find more similar defect sets than runs of different personas?

    Statistic: mean Jaccard similarity of same-persona pairs minus that of different-persona pairs; the null
    distribution shuffles persona labels across runs (one-sided Monte-Carlo p with the +1 correction)."""
    n = len(sets)
    jac = [[jaccard(sets[i], sets[j]) for j in range(n)] for i in range(n)]
    pairs = list(itertools.combinations(range(n), 2))

    def stat(lbl: list[str]) -> float:
        same = [jac[i][j] for i, j in pairs if lbl[i] == lbl[j]]
        cross = [jac[i][j] for i, j in pairs if lbl[i] != lbl[j]]
        return st.mean(same) - st.mean(cross)

    obs = stat(labels)
    rng = random.Random(seed)
    lbl, ge = labels[:], 0
    for _ in range(perms):
        rng.shuffle(lbl)
        ge += stat(lbl) >= obs - 1e-12
    return {"observed": obs, "p": (ge + 1) / (perms + 1), "perms": perms, "n_runs": n}


def cohen_kappa(a: list[int], b: list[int]) -> float | None:
    n = len(a)
    if not n:
        return None
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return None if pe == 1 else (po - pe) / (1 - pe)


def discovery_curve(sets: list[set[str]], universe: list[str], perms: int = 500, seed: int = 0) -> list[float]:
    rng = random.Random(seed)
    n = len(sets)
    acc = [0.0] * n
    for _ in range(perms):
        order = sets[:]
        rng.shuffle(order)
        seen: set[str] = set()
        for i, s in enumerate(order):
            seen |= s & set(universe)
            acc[i] += len(seen)
    return [a / perms for a in acc]


def titles_short(defect_id: str, n: int = 52) -> str:
    t = next(d["title"] for d in DEFECTS if d["id"] == defect_id)
    if len(t) > n:
        t = t[: t.rfind(" ", 0, n - 1)]
        if t.count("(") > t.count(")"):
            t = t[: t.rfind("(")].rstrip()
        t += "\\ldots"
    t = re.sub(r"(^|\s)'", r"\1`", t)
    return t.replace("&", "\\&").replace("_", "\\_")


def nat(ids) -> list[str]:
    return sorted(ids, key=lambda x: (x[0], int(x[1:]) if x[1:].isdigit() else 0))


def fit_lambda(curve: list[float], total: int | None = None) -> dict | None:
    """Least-squares fit of Nielsen & Landauer (1993): found(n) = N * (1 - (1 - lam)^n).

    With `total` the ceiling N is fixed (e.g. to the seeded count); otherwise N is fitted too, which estimates how many
    defects this kind of session can find at all."""
    if len(curve) < 2 and total is None:
        return None
    best = (None, None, float("inf"))
    ns = [total] if total is not None else [x / 10 for x in range(int(max(curve) * 10), int(max(curve) * 30) + 1)]
    for N in ns:
        for i in range(1, 1000):
            lam = i / 1000
            err = sum((N * (1 - (1 - lam) ** (k + 1)) - y) ** 2 for k, y in enumerate(curve))
            if err < best[2]:
                best = (lam, N, err)
    return {"lambda": best[0], "N": best[1], "rmse": math.sqrt(best[2] / len(curve))}


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    centre, half = (p + z * z / (2 * n)) / (1 + z * z / n), z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (centre - half, centre + half)


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 1.0


def expected_union(groups: list[list[set[str]]], k: int, universe: set[str], draws: int = 2000, seed: int = 0) -> float | None:
    """Mean number of distinct defects found by k sessions, each drawn from a different group (persona)."""
    rng = random.Random(seed)
    groups = [g for g in groups if g]
    if k > len(groups):
        return None
    tot = 0
    for _ in range(draws):
        picked = [rng.choice(g) for g in rng.sample(groups, k)]
        tot += len(set().union(*picked) & universe)
    return tot / draws


def valence_series(run: dict) -> list[float]:
    out = []
    for t in run["trace"]:
        try:
            out.append(float((t.get("output") or {}).get("valence")))
        except (TypeError, ValueError):
            continue
    return out


def latex_table(path: Path, header: list[str], rows: list[list[str]], caption: str, label: str, colspec: str | None = None,
                rule_before: tuple[int, ...] = (), wide: bool = False) -> None:
    colspec = colspec or ("l" + "c" * (len(header) - 1))
    env = "table*" if wide else "table"
    lines = [f"\\begin{{{env}}}[t]", "\\centering", "\\small", f"\\caption{{{caption}}}", f"\\label{{{label}}}",
             f"\\begin{{tabular}}{{{colspec}}}", "\\toprule", " & ".join(header) + " \\\\", "\\midrule"]
    for i, r in enumerate(rows):
        if i in rule_before:
            lines.append("\\midrule")
        lines.append(" & ".join(r) + " \\\\")
    lines += ["\\bottomrule", "\\end{tabular}", f"\\end{{{env}}}"]
    path.write_text("\n".join(lines) + "\n")


def save_fig(fig, out: Path, name: str) -> None:
    (out / "figures").mkdir(parents=True, exist_ok=True)
    fig.savefig(out / "figures" / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out / "figures" / f"{name}.png", bbox_inches="tight", dpi=160)
    plt.close(fig)


def write_numbers(res: dict, runs: list[dict], out: Path) -> None:
    """LaTeX macros for every number quoted in the paper text, so prose and tables cannot drift apart."""
    m: dict[str, str] = {}

    def pm(name: str, v, digits: int = 2, pct: bool = False) -> None:
        mean, sd = v if isinstance(v, (list, tuple)) else (v, None)
        if mean is None:
            m[name] = "--"
            return
        f = (lambda x: f"{100 * x:.0f}\\%") if pct else (lambda x: f"{x:.{digits}f}")
        m[name] = f(mean) + (f" $\\pm$ {f(sd)}" if sd is not None else "")
        m[name + "Mean"] = f(mean)

    def p_str(p: float) -> str:
        """Relation and value, for use in math mode as ``$p \\Macro$``."""
        return f"= {p:.3f}" if p >= 0.001 else "< 0.001"

    m["NRuns"] = str(res["n_runs"])
    m["NPersonaRuns"] = str(sum(1 for r in runs if r["persona"] != "generic_user"))
    m["NGenericRuns"] = str(sum(1 for r in runs if r["persona"] == "generic_user"))
    for suffix, o in (("", res["overall_personas"]), ("Generic", res.get("overall_generic")), ("All", res["overall"])):
        if not o:
            continue
        for k, name in (("ux_raw", "UXRecall"), ("ux_exp", "UXRecallExp"), ("out_raw", "OutRecall"), ("p_strict", "PStrict"), ("p_lenient", "PLenient"),
                        ("evidence_verified", "EvidenceVerified")):
            pm(name + suffix, o[k], pct=True)
        pm("Findings" + suffix, o["findings"], digits=0)
        pm("Steps" + suffix, o["steps"], digits=1)
        pm("Calls" + suffix, o["calls"], digits=0)
        pm("Minutes" + suffix, o["minutes"], digits=1)
    for k, name in (("ux_raw", "UX"), ("ux_exp", "UXExp"), ("out_raw", "Out"), ("p_strict", "PStrict")):
        t = (res.get("persona_vs_generic") or {}).get(k)
        if t:
            m[f"PvG{name}P"] = p_str(t["p"])
            m[f"PvG{name}Diff"] = f"${100 * t['difference']:+.0f}$"
    lt = res.get("persona_label_test")
    if lt:
        m["LabelStat"] = f"{lt['observed']:.2f}"
        m["LabelP"] = p_str(lt["p"])
        m["LabelPerms"] = f"{lt['perms']:,}".replace(",", "{,}")
    m["UnionUX"] = str(len(res["union_all_personas"]["ux"]))
    m["UnionOut"] = str(len(res["union_all_personas"]["output"]))
    m["NeverFound"] = ", ".join(res["never_found"]) or "none"
    m["PersonaOnly"] = ", ".join(res["found_by_personas_not_generic"]) or "none"
    m["GenericOnly"] = ", ".join(res["found_by_generic_not_personas"]) or "none"
    f = (res.get("discovery", {}).get("personas") or {}).get("fit_free_N") or {}
    m["LambdaFree"] = f"{f['lambda']:.2f}" if f else "--"
    m["NHat"] = f"{f['N']:.1f}" if f else "--"
    fs = (res.get("discovery", {}).get("personas") or {}).get("fit_seeded_N") or {}
    m["LambdaSeeded"] = f"{fs['lambda']:.2f}" if fs else "--"
    m["RmseFree"] = f"{f['rmse']:.2f}" if f else "--"
    m["RmseSeeded"] = f"{fs['rmse']:.2f}" if fs else "--"
    g = (res.get("discovery", {}).get("generic") or {}).get("fit_free_N") or {}
    m["LambdaFreeGeneric"] = f"{g['lambda']:.2f}" if g else "--"
    m["NHatGeneric"] = f"{g['N']:.1f}" if g else "--"
    for label, name in (("personas", "Persona"), ("generic", "Generic")):
        c = (res.get("discovery", {}).get(label) or {}).get("curve")
        if c:
            m[f"Curve{name}Last"] = f"{c[-1]:.1f}"
            m[f"Curve{name}Six"] = f"{c[5]:.1f}" if len(c) >= 6 else "--"
    for k, name in (("same_persona", "JacSame"), ("different_personas", "JacCross"), ("generic_vs_generic", "JacGeneric")):
        pm(name, res["ux_jaccard"][k][:2])
    mb = {x["k"]: x for x in res["matched_budget_union_ux"]}
    for k in (1, 2, 3, 6):
        if k in mb:
            m[f"MatchedPersona{'ABCDEF'[k - 1]}"] = f"{mb[k]['distinct_personas']:.1f}" if mb[k]["distinct_personas"] is not None else "--"
            m[f"MatchedGeneric{'ABCDEF'[k - 1]}"] = f"{mb[k]['generic_reps']:.1f}" if mb[k]["generic_reps"] is not None else "--"
    pc = res["pooled_classes"]
    m["PooledFindings"] = f"{pc['total']:,}".replace(",", "{,}")
    m["PooledMatched"], m["PooledDuplicate"], m["PooledUnseeded"], m["PooledIncorrect"] = (str(pc[k]) for k in ("matched", "duplicate", "valid_unseeded", "incorrect"))
    m["PooledPStrict"] = f"{100 * pc['p_strict']:.0f}\\%"
    m["PooledPLenient"] = f"{100 * pc['p_lenient']:.0f}\\%"
    m["UnseededShare"] = f"{100 * pc['valid_unseeded'] / pc['total']:.0f}\\%"
    au = res.get("audit")
    if au:
        m["AuditN"], m["AuditValid"], m["AuditOverlap"], m["AuditDebatable"], m["AuditWrong"] = (str(au[k]) for k in ("n", "valid", "overlaps_seeded", "debatable", "wrong"))
        m["AuditValidPct"] = f"{100 * au['valid_share']:.0f}\\%"
        m["AuditValidCI"] = f"{100 * au['valid_ci'][0]:.0f}--{100 * au['valid_ci'][1]:.0f}\\%"
        m["AdjPLenient"] = f"{100 * au['adjusted_p_lenient']:.0f}\\%"
        m["AdjPLenientCI"] = f"{100 * au['adjusted_p_lenient_ci'][0]:.0f}--{100 * au['adjusted_p_lenient_ci'][1]:.0f}\\%"
    m["KappaJK"] = f"{res['judge_keyword_kappa']:.2f}"
    m["AgreeJK"] = f"{100 * res['judge_keyword_agreement']:.0f}\\%"
    det = [len(r["g"]["deterministic_output_baseline"]["detected"]) for r in runs]
    m["DetBaseline"] = f"{st.mean(det):.1f}"
    va = res.get("vision_ablation")
    if va:
        m["AblRuns"] = str(va["n_runs"])
        for grp, name in (("visual", "Visual"), ("textual", "Textual"), ("all_output", "AllOut")):
            g = va["mcnemar"][grp]
            pm(f"Vis{name}", g["recall_vision"], pct=True)
            pm(f"NoVis{name}", g["recall_no_vision"], pct=True)
            m[f"McP{name}"] = p_str(g["p"])
            m[f"McB{name}"], m[f"McC{name}"] = str(g["vision_only"]), str(g["no_vision_only"])
            m[f"SignW{name}"], m[f"SignL{name}"], m[f"SignP{name}"] = str(g["runs_better_with_vision"]), str(g["runs_better_without"]), p_str(g["sign_test_p"])
    for key, name in (("output_test_retest", "Retest"), ("output_original_vs_rerun", "OrigRerun")):
        rt = res.get(key)
        if rt:
            m[f"{name}Runs"] = str(rt["n_runs"])
            m[f"{name}Kappa"] = f"{rt['kappa']:.2f}" if rt["kappa"] is not None else "--"
            m[f"{name}Agree"] = f"{100 * rt['agreement']:.0f}\\%"
            pm(f"{name}RecallA", rt["recall_a"], pct=True)
            pm(f"{name}RecallB", rt["recall_b"], pct=True)
    q = res["questionnaires"]
    for p, v in q.items():
        key = "".join(w.capitalize() for w in p.split("_"))
        if v["sus"][0] is not None:
            m[f"Sus{key}"] = f"{v['sus'][0]:.1f}"
    lines = ["% generated by experiments/analyze.py - do not edit"]
    for k, v in sorted(m.items()):
        lines.append(f"\\newcommand{{\\{k}}}{{{v}}}")
    (out / "numbers.tex").write_text("\n".join(lines) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", required=True)
    ap.add_argument("--xmodel", nargs="*", default=[])
    ap.add_argument("--out", default=str(ROOT / "paper/generated"))
    a = ap.parse_args()
    out = Path(a.out)
    (out / "tables").mkdir(parents=True, exist_ok=True)
    runs = load_suite(Path(a.main))
    if not runs:
        print("no scored runs found; run experiments/score_ground_truth.py first")
        return 1
    personas = [p for p in PERSONA_ORDER if any(r["persona"] == p for r in runs)] + sorted({r["persona"] for r in runs} - set(PERSONA_ORDER))
    res: dict = {"n_runs": len(runs), "personas": personas, "by_persona": {}}

    # ---- Table: per-persona detection, precision and cost
    def pooled(rs: list[dict]) -> dict:
        return {k: mean_sd(v) for k, v in dict(
            ux_raw=[len(r["g"]["judge"]["ux"]["detected"]) / len(UX) for r in rs],
            ux_exp=[r["g"]["judge"]["ux"]["exposure_adjusted"] for r in rs],
            out_raw=[len(r["g"]["judge"]["output"]["detected"]) / len(OUT) for r in rs],
            p_strict=[r["g"]["judge"]["precision_strict"] for r in rs], p_lenient=[r["g"]["judge"]["precision_lenient"] for r in rs],
            findings=[r["g"]["n_findings"] for r in rs], steps=[r["s"].get("steps") for r in rs],
            calls=[(r["s"].get("llm_usage") or {}).get("calls") for r in rs], minutes=[r["s"].get("wall_seconds", 0) / 60 for r in rs],
            evidence_verified=[r["s"].get("evidence_quotes_verified") for r in rs]).items()}

    def row(name: str, rs: list[dict], rec: dict) -> list[str]:
        return [name, str(len(rs)), fmt(*rec["ux_raw"]), fmt(*rec["ux_exp"]), fmt(*rec["out_raw"]), fmt(*rec["p_strict"]), fmt(*rec["p_lenient"]),
                fmt(*rec["findings"], digits=0), fmt(*rec["calls"], digits=0), fmt(*rec["minutes"], digits=1)]

    persona_runs = [r for r in runs if r["persona"] != "generic_user"]
    generic_runs = [r for r in runs if r["persona"] == "generic_user"]
    rows = []
    for p in personas:
        rs = [r for r in runs if r["persona"] == p]
        rec = pooled(rs)
        res["by_persona"][p] = rec | {"n": len(rs)}
        rows.append(row(SHORT.get(p, p), rs, rec))
    res["overall"] = pooled(runs)
    res["overall_personas"] = pooled(persona_runs)
    res["overall_generic"] = pooled(generic_runs) if generic_runs else None
    rows.append(row("\\textit{All persona sessions}", persona_runs, res["overall_personas"]))
    latex_table(out / "tables" / "detection.tex",
                ["Persona", "$n$", "UX recall", "UX recall (exp.)", "Output recall", "Prec. (strict)", "Prec. (lenient)", "Findings", "LLM calls", "Minutes"],
                rows, "Seeded-defect detection on StoryHearth per persona (mean $\\pm$ SD over repetitions; LLM-judge matching). "
                "UX recall over 17 seeded UX defects (raw, and over the defects the session was exposed to); output recall over 14 "
                "seeded output defects. Strict precision: share of findings matching a seeded defect; lenient additionally counts "
                "findings judged valid but unseeded. The generic agent is the no-persona ablation.", "tab:detection",
                rule_before=(len(personas),), wide=True)
    if generic_runs:
        tests = {}
        for key, fn in (("ux_raw", lambda r: len(r["g"]["judge"]["ux"]["detected"]) / len(UX)),
                        ("ux_exp", lambda r: r["g"]["judge"]["ux"]["exposure_adjusted"]),
                        ("out_raw", lambda r: len(r["g"]["judge"]["output"]["detected"]) / len(OUT)),
                        ("p_strict", lambda r: r["g"]["judge"]["precision_strict"])):
            x, y = [v for v in map(fn, persona_runs) if v is not None], [v for v in map(fn, generic_runs) if v is not None]
            tests[key] = {"persona_mean": st.mean(x), "generic_mean": st.mean(y), "difference": st.mean(x) - st.mean(y), "p": permutation_test_means(x, y)}
        res["persona_vs_generic"] = tests

    # ---- Union / diversity analysis
    union_personas = set().union(*(detected(r) for r in runs if r["persona"] != "generic_user")) if runs else set()
    generic = [detected(r) for r in runs if r["persona"] == "generic_user"]
    res["union_all_personas"] = {"ux": nat(union_personas & set(UX)), "output": nat(union_personas & set(OUT))}
    res["generic_union"] = nat(set().union(*generic)) if generic else []
    res["found_by_personas_not_generic"] = nat((union_personas - set().union(*generic)) if generic else union_personas)
    res["found_by_generic_not_personas"] = nat(set().union(*generic) - union_personas) if generic else []
    res["never_found"] = nat(set(UX + OUT) - union_personas - set(res["generic_union"]))

    # Diversity: do different personas find different things, beyond what re-sampling one prompt gives?
    by_p = {p: [detected(r) & set(UX) for r in runs if r["persona"] == p] for p in personas}
    same, cross, gen = [], [], []
    for p, q in itertools.combinations_with_replacement(personas, 2):
        for i, a_set in enumerate(by_p[p]):
            for j, b_set in enumerate(by_p[q]):
                if p == q and j <= i:
                    continue
                if p == q == "generic_user":
                    gen.append(jaccard(a_set, b_set))
                elif p == q:
                    same.append(jaccard(a_set, b_set))
                elif "generic_user" not in (p, q):
                    cross.append(jaccard(a_set, b_set))
    res["ux_jaccard"] = {"same_persona": mean_sd(same) + (len(same),), "different_personas": mean_sd(cross) + (len(cross),),
                         "generic_vs_generic": mean_sd(gen) + (len(gen),)}
    res["persona_label_test"] = label_permutation_test([detected(r) & set(UX) for r in persona_runs], [r["persona"] for r in persona_runs])
    res["ux_rate_personas_vs_generic"] = {
        d: {"personas": st.mean([float(d in detected(r)) for r in persona_runs]),
            "generic": st.mean([float(d in detected(r)) for r in generic_runs]) if generic_runs else None} for d in UX + OUT}
    persona_groups = [by_p[p] for p in personas if p != "generic_user"]
    gen_sets = by_p.get("generic_user", [])
    matched = []
    for k in range(1, len(persona_groups) + 1):
        pe = expected_union(persona_groups, k, set(UX))
        ge = expected_union([[s] for s in gen_sets], k, set(UX)) if len(gen_sets) >= k else None
        matched.append({"k": k, "distinct_personas": pe, "generic_reps": ge})
    res["matched_budget_union_ux"] = matched

    # ---- Heatmap: defect x persona detection rate
    rate = {p: {d: 0.0 for d in UX + OUT} for p in personas}
    for p in personas:
        rs = [r for r in runs if r["persona"] == p]
        for d in UX + OUT:
            rate[p][d] = sum(1 for r in rs if d in detected(r)) / max(1, len(rs))
    res["detection_rate"] = rate
    fig, ax = plt.subplots(figsize=(12.5, 0.55 * len(personas) + 1.6))
    mat = [[rate[p][d] for d in UX + OUT] for p in personas]
    im = ax.imshow(mat, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(len(UX + OUT)), UX + OUT, rotation=90, fontsize=8)
    ax.set_yticks(range(len(personas)), [SHORT.get(p, p) for p in personas], fontsize=9)
    ax.axvline(len(UX) - 0.5, color="black", lw=1)
    for i, row in enumerate(mat):
        for j, v in enumerate(row):
            if v:
                ax.text(j, i, f"{v:.1f}".rstrip("0").rstrip(".") if v < 1 else "1", ha="center", va="center", fontsize=6.5, color="white" if v > 0.6 else "black")
    ax.set_title("Detection rate of each seeded defect by persona (UX defects left, output defects right)", fontsize=10)
    fig.colorbar(im, ax=ax, fraction=0.02, pad=0.01)
    save_fig(fig, out, "heatmap")

    # ---- Discovery curve + Nielsen-Landauer fit (UX defects; persona sessions only, then all)
    curves = {}
    for label, subset in (("personas", [r for r in runs if r["persona"] != "generic_user"]), ("generic", [r for r in runs if r["persona"] == "generic_user"])):
        if not subset:
            continue
        c = discovery_curve([detected(r) for r in subset], UX)
        curves[label] = {"curve": c, "fit_seeded_N": fit_lambda(c, len(UX)), "fit_free_N": fit_lambda(c)}
    res["discovery"] = curves
    if curves:
        fig, ax = plt.subplots(figsize=(5.2, 3.4))
        for label, c in curves.items():
            xs = list(range(1, len(c["curve"]) + 1))
            f = c["fit_free_N"]
            name = "persona sessions" if label == "personas" else "generic sessions"
            ax.plot(xs, c["curve"], marker="o", ms=3, label=name + (f" ($\\hat N$={f['N']:.1f}, $\\lambda$={f['lambda']:.2f})" if f else ""))
            if f:
                ax.plot(xs, [f["N"] * (1 - (1 - f["lambda"]) ** n) for n in xs], ls="--", lw=0.8, color=ax.lines[-1].get_color())
        ax.axhline(len(UX), color="grey", lw=0.6, ls=":")
        ax.set_xlabel("number of simulated sessions")
        ax.set_ylabel("distinct seeded UX defects found")
        ax.legend(fontsize=8, loc="lower right")
        ax.set_ylim(0, len(UX) + 0.5)
        save_fig(fig, out, "discovery")

    # ---- Questionnaires by persona
    qrows = []
    res["questionnaires"] = {}
    for p in personas:
        rs = [r for r in runs if r["persona"] == p]
        sus = mean_sd([r["s"].get("sus") for r in rs])
        prag = mean_sd([(r["s"].get("ueq_s") or {}).get("pragmatic") for r in rs])
        hed = mean_sd([(r["s"].get("ueq_s") or {}).get("hedonic") for r in rs])
        nps = mean_sd([r["s"].get("nps") for r in rs])
        keep = mean_sd([r["s"].get("keepsake_worthiness") for r in rs])
        val = mean_sd([r["s"].get("mean_valence") for r in rs])
        flags = sum(1 for r in rs if r["s"].get("sus_consistency_flag"))
        real = mean_sd([(r["s"].get("fidelity") or {}).get("realism_overall") for r in rs])
        car = mean_sd([(r["s"].get("fidelity") or {}).get("caricature") for r in rs])
        leak = mean_sd([(r["s"].get("fidelity") or {}).get("knowledge_leakage") for r in rs])
        res["questionnaires"][p] = dict(sus=sus, ueq_pragmatic=prag, ueq_hedonic=hed, nps=nps, keepsake=keep, mean_valence=val,
                                        sus_flags=flags, realism=real, caricature=car, leakage=leak)
        qrows.append([SHORT.get(p, p), fmt(*sus, digits=1), fmt(*prag), fmt(*hed), fmt(*nps, digits=1), fmt(*keep, digits=1), fmt(*val),
                      f"{flags}/{len(rs)}", fmt(*real, digits=1), fmt(*car, digits=1), fmt(*leak, digits=1)])
    latex_table(out / "tables" / "questionnaires.tex",
                ["Persona", "SUS", "UEQ-S prag.", "UEQ-S hed.", "Recommend", "Keepsake", "Valence", "SUS flag", "Realism", "Caricature", "Leakage"],
                qrows, "Post-session self-report by persona (mean $\\pm$ SD): SUS (0--100), UEQ-S pragmatic/hedonic ($-3$..$3$), "
                "likelihood to recommend (0--10), keepsake-worthiness of the generated book (1--5), mean in-session valence ($-2$..$2$), "
                "SUS acquiescence-consistency flags, and the persona-fidelity audit (1--5; lower caricature/leakage is better).", "tab:questionnaires",
                wide=True)

    # ---- Valence trajectories
    fig, ax = plt.subplots(figsize=(5.6, 3.3))
    res["valence"] = {}
    for p in personas:
        series = [valence_series(r) for r in runs if r["persona"] == p]
        if not series:
            continue
        n = max(len(s) for s in series)
        mean = [st.mean([s[i] for s in series if len(s) > i]) for i in range(n)]
        res["valence"][p] = mean
        ax.plot(range(1, n + 1), mean, lw=1.2, label=SHORT.get(p, p), ls="--" if p == "generic_user" else "-")
    ax.axhline(0, color="grey", lw=0.5)
    ax.set_xlabel("step")
    ax.set_ylabel("self-reported valence")
    ax.legend(fontsize=7, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.2), frameon=False)
    save_fig(fig, out, "valence")

    # ---- Output: LLM assessment vs deterministic metrics baseline
    det_rate = {d: st.mean([1.0 if d in r["g"]["deterministic_output_baseline"]["detected"] else 0.0 for r in runs]) for d in OUT}
    llm_rate = {d: st.mean([1.0 if d in r["g"]["judge"]["output"]["detected"] else 0.0 for r in runs]) for d in OUT}
    res["output_llm_vs_deterministic"] = {"llm": llm_rate, "deterministic": det_rate}
    orows = [[d, titles_short(d), f"{llm_rate[d]:.2f}", f"{det_rate[d]:.2f}"] for d in OUT]
    latex_table(out / "tables" / "output_defects.tex", ["ID", "Seeded output defect", "Persona judge", "Metrics only"], orows,
                "Share of sessions in which each seeded output defect was reported by the persona-grounded output assessment versus "
                "flagged by the deterministic text metrics alone.", "tab:output", colspec="llcc")

    # ---- Judge vs keyword agreement
    a_, b_ = [], []
    for r in runs:
        dj, dk = detected(r, "judge"), detected(r, "keyword")
        for d in UX + OUT:
            a_.append(int(d in dj))
            b_.append(int(d in dk))
    res["judge_keyword_kappa"] = cohen_kappa(a_, b_)
    res["judge_keyword_agreement"] = sum(1 for x, y in zip(a_, b_) if x == y) / len(a_)

    # ---- Hand audit of the judge's "valid but unseeded" class -> audit-adjusted lenient precision (pooled over findings)
    classes = {k: sum(r["g"]["judge"]["classes"][k] for r in runs) for k in ("matched", "duplicate", "valid_unseeded", "incorrect")}
    total = sum(classes.values())
    res["pooled_classes"] = classes | {"total": total, "p_strict": (classes["matched"] + classes["duplicate"]) / total,
                                       "p_lenient": (total - classes["incorrect"]) / total}
    audit_path = ROOT / "experiments/audit/valid_unseeded_audit.json"
    if audit_path.exists():
        labels = [x["label"] for x in json.loads(audit_path.read_text())["items"]]
        n = len(labels)
        valid = sum(1 for x in labels if x in ("valid", "valid_overlaps_seeded"))
        lo, hi = wilson(valid, n)
        adj = lambda share: (classes["matched"] + classes["duplicate"] + share * classes["valid_unseeded"]) / total  # noqa: E731
        res["audit"] = {"n": n, "valid": valid, "overlaps_seeded": labels.count("valid_overlaps_seeded"), "debatable": labels.count("debatable"),
                        "wrong": labels.count("wrong") + labels.count("partly_wrong"), "valid_share": valid / n, "valid_ci": (lo, hi),
                        "adjusted_p_lenient": adj(valid / n), "adjusted_p_lenient_ci": (adj(lo), adj(hi))}

    # ---- Paired vision ablation: the same captured outputs re-assessed with and without pictures
    va = {r["dir"]: r for r in load_suite(Path(a.main), "vision")}
    vb = {r["dir"]: r for r in load_suite(Path(a.main), "novision")}
    paired = [d for d in va if d in vb]
    if paired:
        out_det = lambda r: set(r["g"]["judge"]["output"]["detected"])  # noqa: E731
        abl = {"n_runs": len(paired), "per_defect": {}, "mcnemar": {}}
        for d in OUT:
            abl["per_defect"][d] = {"vision": st.mean([float(d in out_det(va[x])) for x in paired]),
                                    "no_vision": st.mean([float(d in out_det(vb[x])) for x in paired])}
        visual = [d["id"] for d in DEFECTS if d["kind"] == "output" and d.get("modality") == "image"]
        for name, ids in (("all_output", OUT), ("visual", visual), ("textual", [d for d in OUT if d not in visual])):
            b = sum(1 for x in paired for d in ids if d in out_det(va[x]) and d not in out_det(vb[x]))
            c = sum(1 for x in paired for d in ids if d not in out_det(va[x]) and d in out_det(vb[x]))
            diffs = [len(out_det(va[x]) & set(ids)) - len(out_det(vb[x]) & set(ids)) for x in paired]
            wins, losses = sum(1 for v in diffs if v > 0), sum(1 for v in diffs if v < 0)
            abl["mcnemar"][name] = {"defects": ids, "vision_only": b, "no_vision_only": c, "p": mcnemar_exact(b, c),
                                    "runs_better_with_vision": wins, "runs_better_without": losses, "sign_test_p": mcnemar_exact(wins, losses),
                                    "recall_vision": mean_sd([len(out_det(va[x]) & set(ids)) / max(1, len(ids)) for x in paired]),
                                    "recall_no_vision": mean_sd([len(out_det(vb[x]) & set(ids)) / max(1, len(ids)) for x in paired])}
        res["vision_ablation"] = abl
        orows = [[d, titles_short(d), f"{abl['per_defect'][d]['vision']:.2f}", f"{abl['per_defect'][d]['no_vision']:.2f}"] for d in OUT]
        latex_table(out / "tables" / "vision_ablation.tex", ["ID", "Seeded output defect", "With pictures", "Text + alt only"], orows,
                    f"Paired vision ablation: share of the {len(paired)} sessions in which the re-run output assessment reported each seeded "
                    "output defect when it could see the pictures versus text and alt text only (same captured outputs).", "tab:vision", colspec="llcc")

    # ---- Reliability of the output assessment: two independent re-runs with the same code and inputs (test-retest),
    # and the original in-session assessment (earlier assessor version) against the first re-run.
    def agreement(xa: dict, xb: dict) -> dict | None:
        common = [d for d in xa if d in xb]
        if not common:
            return None
        x_, y_ = [], []
        for dname in common:
            o1, o2 = set(xa[dname]["g"]["judge"]["output"]["detected"]), set(xb[dname]["g"]["judge"]["output"]["detected"])
            x_ += [int(d in o1) for d in OUT]
            y_ += [int(d in o2) for d in OUT]
        return {"n_runs": len(common), "agreement": sum(1 for p, q in zip(x_, y_) if p == q) / len(x_), "kappa": cohen_kappa(x_, y_),
                "recall_a": mean_sd([len(xa[dn]["g"]["judge"]["output"]["detected"]) / len(OUT) for dn in common]),
                "recall_b": mean_sd([len(xb[dn]["g"]["judge"]["output"]["detected"]) / len(OUT) for dn in common])}

    v2 = {r["dir"]: r for r in load_suite(Path(a.main), "vision2")}
    res["output_test_retest"] = agreement(va, v2)
    res["output_original_vs_rerun"] = agreement({r["dir"]: r for r in runs}, va)
    # ---- Cross-model replication
    if a.xmodel:
        xm = [r for p in a.xmodel for r in load_suite(Path(p))]
        if xm:
            res["cross_model"] = {
                "runs": [{"persona": r["persona"], "model": r["g"].get("model"), "status": r["g"].get("status"), "steps": r["g"].get("steps"),
                          "ux": len(r["g"]["judge"]["ux"]["detected"]), "output": len(r["g"]["judge"]["output"]["detected"]),
                          "p_strict": r["g"]["judge"]["precision_strict"], "calls": (r["s"].get("llm_usage") or {}).get("calls")} for r in xm],
            }
    (out / "results.json").write_text(json.dumps(res, indent=1, default=str))
    write_numbers(res, runs, out)
    keys = ("n_runs", "overall", "union_all_personas", "found_by_personas_not_generic", "found_by_generic_not_personas", "never_found",
            "ux_jaccard", "matched_budget_union_ux", "judge_keyword_kappa")
    print(json.dumps({k: res[k] for k in keys}, default=str))
    for label, c in res.get("discovery", {}).items():
        print(label, "fixed N:", c["fit_seeded_N"], "free N:", c["fit_free_N"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
