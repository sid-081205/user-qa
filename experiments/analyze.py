"""Aggregate scored suites into the tables, figures and numbers used in the paper.

    python experiments/analyze.py --main runs/suite/main [--novision runs/suite/novision] \
        [--xmodel runs/suite/xmodel] [--out paper/generated]

Reads every run's summary.json and gt_scores.json (run experiments/score_ground_truth.py first) and
writes results.json, LaTeX tables (tables/*.tex) and figures (figures/*.pdf + .png).
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
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


def load_suite(path: Path) -> list[dict]:
    runs = []
    for d in sorted(Path(path).glob("*/gt_scores.json")):
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
    return st.mean(xs), (st.stdev(xs) if len(xs) > 1 else 0.0)


def fmt(m, sd=None, digits=2) -> str:
    if m is None:
        return "--"
    return f"{m:.{digits}f}" + (f" $\\pm$ {sd:.{digits}f}" if sd else "")


def detected(run: dict, method: str = "judge") -> set[str]:
    g = run["g"][method]
    return set(g["ux"]["detected"]) | set(g["output"]["detected"])


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


def latex_table(path: Path, header: list[str], rows: list[list[str]], caption: str, label: str, colspec: str | None = None) -> None:
    colspec = colspec or ("l" + "c" * (len(header) - 1))
    lines = ["\\begin{table}[t]", "\\centering", "\\small", f"\\caption{{{caption}}}", f"\\label{{{label}}}",
             f"\\begin{{tabular}}{{{colspec}}}", "\\toprule", " & ".join(header) + " \\\\", "\\midrule"]
    lines += [" & ".join(r) + " \\\\" for r in rows]
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    path.write_text("\n".join(lines) + "\n")


def save_fig(fig, out: Path, name: str) -> None:
    (out / "figures").mkdir(parents=True, exist_ok=True)
    fig.savefig(out / "figures" / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out / "figures" / f"{name}.png", bbox_inches="tight", dpi=160)
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", required=True)
    ap.add_argument("--novision")
    ap.add_argument("--xmodel", nargs="*", default=[])
    ap.add_argument("--extra", nargs="*", default=[], help="extra run dirs/suites (e.g. the pilot) to include in pooled stats")
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
    rows = []
    for p in personas:
        rs = [r for r in runs if r["persona"] == p]
        ux_raw = [len(r["g"]["judge"]["ux"]["detected"]) / len(UX) for r in rs]
        ux_exp = [r["g"]["judge"]["ux"]["exposure_adjusted"] for r in rs]
        out_raw = [len(r["g"]["judge"]["output"]["detected"]) / len(OUT) for r in rs]
        ps = [r["g"]["judge"]["precision_strict"] for r in rs]
        pl = [r["g"]["judge"]["precision_lenient"] for r in rs]
        nf = [r["g"]["n_findings"] for r in rs]
        steps = [r["s"].get("steps") for r in rs]
        calls = [(r["s"].get("llm_usage") or {}).get("calls") for r in rs]
        mins = [r["s"].get("wall_seconds", 0) / 60 for r in rs]
        ev = [r["s"].get("evidence_quotes_verified") for r in rs]
        rec = {k: mean_sd(v) for k, v in dict(ux_raw=ux_raw, ux_exp=ux_exp, out_raw=out_raw, p_strict=ps, p_lenient=pl, findings=nf,
                                                  steps=steps, calls=calls, minutes=mins, evidence_verified=ev).items()}
        rec["n"] = len(rs)
        res["by_persona"][p] = {k: v for k, v in rec.items()}
        rows.append([SHORT.get(p, p), str(len(rs)), fmt(*rec["ux_raw"]), fmt(*rec["ux_exp"]), fmt(*rec["out_raw"]), fmt(*rec["p_strict"]),
                     fmt(*rec["p_lenient"]), fmt(*rec["findings"], digits=0), fmt(*rec["calls"], digits=0), fmt(*rec["minutes"], digits=1)])
    allr = runs
    tot = {k: mean_sd(v) for k, v in dict(
        ux_raw=[len(r["g"]["judge"]["ux"]["detected"]) / len(UX) for r in allr],
        ux_exp=[r["g"]["judge"]["ux"]["exposure_adjusted"] for r in allr],
        out_raw=[len(r["g"]["judge"]["output"]["detected"]) / len(OUT) for r in allr],
        p_strict=[r["g"]["judge"]["precision_strict"] for r in allr], p_lenient=[r["g"]["judge"]["precision_lenient"] for r in allr],
        findings=[r["g"]["n_findings"] for r in allr], calls=[(r["s"].get("llm_usage") or {}).get("calls") for r in allr],
        minutes=[r["s"].get("wall_seconds", 0) / 60 for r in allr]).items()}
    res["overall"] = tot
    rows.append(["\\textit{All sessions}", str(len(allr)), fmt(*tot["ux_raw"]), fmt(*tot["ux_exp"]), fmt(*tot["out_raw"]), fmt(*tot["p_strict"]),
                 fmt(*tot["p_lenient"]), fmt(*tot["findings"], digits=0), fmt(*tot["calls"], digits=0), fmt(*tot["minutes"], digits=1)])
    latex_table(out / "tables" / "detection.tex",
                ["Persona", "$n$", "UX recall", "UX recall (exp.)", "Output recall", "Prec. (strict)", "Prec. (lenient)", "Findings", "LLM calls", "Minutes"],
                rows, "Seeded-defect detection on StoryHearth per persona (mean $\\pm$ SD over repetitions; LLM-judge matching). "
                "UX recall over 17 seeded UX defects (raw, and over the defects the session was exposed to); output recall over 14 "
                "seeded output defects. Strict precision: share of findings matching a seeded defect; lenient additionally counts "
                "findings judged valid but unseeded.", "tab:detection")

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
                ["Persona", "SUS", "UEQ-S prag.", "UEQ-S hed.", "NPS", "Keepsake", "Valence", "SUS flag", "Realism", "Caricature", "Leakage"],
                qrows, "Post-session self-report by persona (mean $\\pm$ SD): SUS (0--100), UEQ-S pragmatic/hedonic ($-3$..$3$), "
                "likelihood to recommend (0--10), keepsake-worthiness of the generated book (1--5), mean in-session valence ($-2$..$2$), "
                "SUS acquiescence-consistency flags, and the persona-fidelity audit (1--5; lower caricature/leakage is better).", "tab:questionnaires")

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
    ax.legend(fontsize=7, ncol=2)
    save_fig(fig, out, "valence")

    # ---- Output: LLM assessment vs deterministic metrics baseline
    det_rate = {d: st.mean([1.0 if d in r["g"]["deterministic_output_baseline"]["detected"] else 0.0 for r in runs]) for d in OUT}
    llm_rate = {d: st.mean([1.0 if d in r["g"]["judge"]["output"]["detected"] else 0.0 for r in runs]) for d in OUT}
    res["output_llm_vs_deterministic"] = {"llm": llm_rate, "deterministic": det_rate}
    titles = {d["id"]: d["title"] for d in DEFECTS}
    orows = [[d, titles[d][:48].replace("&", "\\&").replace("_", "\\_"), f"{llm_rate[d]:.2f}", f"{det_rate[d]:.2f}"] for d in OUT]
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

    # ---- Vision ablation
    if a.novision:
        nv = load_suite(Path(a.novision))
        if nv:
            vis = [r for r in runs if r["persona"] in {x["persona"] for x in nv}]
            res["vision_ablation"] = {
                "n_vision": len(vis), "n_novision": len(nv),
                "vision": {d: st.mean([1.0 if d in detected(r) else 0.0 for r in vis]) for d in OUT},
                "novision": {d: st.mean([1.0 if d in detected(r) else 0.0 for r in nv]) for d in OUT},
                "ux_recall": {"vision": mean_sd([len(r["g"]["judge"]["ux"]["detected"]) / len(UX) for r in vis]),
                              "novision": mean_sd([len(r["g"]["judge"]["ux"]["detected"]) / len(UX) for r in nv])},
                "output_recall": {"vision": mean_sd([len(r["g"]["judge"]["output"]["detected"]) / len(OUT) for r in vis]),
                                  "novision": mean_sd([len(r["g"]["judge"]["output"]["detected"]) / len(OUT) for r in nv])},
            }
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
    keys = ("n_runs", "overall", "union_all_personas", "found_by_personas_not_generic", "found_by_generic_not_personas", "never_found",
            "ux_jaccard", "matched_budget_union_ux", "judge_keyword_kappa")
    print(json.dumps({k: res[k] for k in keys}, default=str))
    for label, c in res.get("discovery", {}).items():
        print(label, "fixed N:", c["fit_seeded_N"], "free N:", c["fit_free_N"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
