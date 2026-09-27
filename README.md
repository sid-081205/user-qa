# user-qa: persona-grounded agentic UX and output evaluation

`userqa` sends an LLM-driven simulated user into a real website. The simulated user is a specific kind of person: a family-history-minded grandparent, a tech-savvy parent, a busy parent on a phone, a low-vision senior, or any user type you describe in plain words. It:

1. works out what the site is and who it is for,
2. reviews every page or screen it reaches: what is happening, a first impression, a cognitive walkthrough, and heuristic issues with quoted evidence, a severity and a concrete fix,
3. carries out the site's main task the way that person would, thinking aloud as it goes,
4. judges everything the site **generates** for it (a story, a book preview, a downloaded PDF, pictures), part by part and in the persona's frame. Each part gets a reaction, rubric problems, the change it would make and, where the text should change, a rewrite,
5. fills in a post-session SUS / UEQ-S questionnaire and interview, and a separate call audits how faithfully the persona was played.

Each run writes a self-contained HTML/Markdown report plus machine-readable JSON.

The repository also contains **StoryHearth**, a synthetic storybook website with 31 seeded UX and output defects (`demo_sites/storyhearth`). The agent is never told about it. The repository also has the experiment scripts and the paper that evaluates the agent on StoryHearth and on the real site [ourlegacy.family](https://ourlegacy.family).

## Quick start

```bash
pip install -r requirements.txt        # or: pip install -e ".[experiments,test]"
python -m playwright install chromium  # skip if Google Chrome is at /usr/local/bin/google-chrome
echo 'OPENROUTER_API_KEY=sk-or-v1-...' > .env   # .env is gitignored; never commit the key
```

Optional system packages: `ffmpeg` (to assess video outputs) and a word list in `/usr/share/dict` (for the typo check).

The browser runs headed by default, because CAPTCHAs are more likely in headless mode. On a machine without a screen, use `xvfb-run python -m userqa ...` or pass `--headless`.

**Try it on the synthetic site.** No account or credits are needed.

```bash
python demo_sites/storyhearth/serve.py --port 8765 &
python -m userqa run --site storyhearth --persona grandparent_storykeeper
```

**Try it on any website** with a user type described in words. A persona is synthesised from the description:

```bash
python -m userqa run --url https://example.com --persona-type "a techy dad who builds his own PCs"
```

**Run it on ourlegacy.family.** This signs up with a disposable mail.tm inbox, reads the one-time code from it, creates a storybook with the account's free starter credits, and reviews every page and picture:

```bash
python -m userqa run --site ourlegacy --persona grandparent_storykeeper
# a returning visit: open the same book, export the PDF, try the site's own editing tools
python -m userqa run --site ourlegacy_revisit --persona grandparent_storykeeper \
    --previous-run runs/<first-run-dir>
```

Each command prints the run directory. Open `report.html` in it.

## What a run produces

| File | Contents |
| --- | --- |
| `report.html`, `report.md` | The human-readable report: site model, page-by-page reviews, top issues (clustered), the part-by-part output review with suggested changes and rewrites, questionnaires, fidelity audit |
| `session.json` | Pages and their reviews, inputs the persona typed, captured outputs, abandonment, waits, HTTP/console errors, CAPTCHA log |
| `trace.jsonl` | One record per step: observation, think-aloud, emotion/valence/ease, actions and their results |
| `output_assessment.json` | Deterministic text measurements and the per-part LLM review, including rubric scores, input fidelity, top changes and whether the persona would pay |
| `debrief.json`, `fidelity.json` | SUS, UEQ-S, NPS, interview and recommendations; persona-fidelity audit (facet consistency, caricature, knowledge leakage) |
| `summary.json` | Headline numbers for the run |
| `llm_calls.jsonl` | Every LLM request and response, with images replaced by a digest |
| `screenshots/`, `artifacts/` | Step screenshots; captured outputs (`text.txt` plus picture crops, PDF pages, video frames) |

`python -m userqa explore` builds a website from every run under `runs/` into `explorer/`, without re-running anything. Open `explorer/index.html` to see, for each session, the persona and its task, every step with the exact prompt sent to the model and its answer, everything the persona typed, everything the site produced, the part-by-part critique, the questionnaire and, on StoryHearth, the ground-truth scores. `explorer/compare.html` puts the personas side by side. Screenshots and pictures appear only where the run folder still has them; `--copy-media` copies downscaled versions into the site so it can be shared.

`python -m userqa report <run-dir>` re-renders a report. `python -m userqa reassess <run-dir>` re-runs only the output assessment without browsing again, for example after changing the assessor. `--variant NAME` writes `output_assessment.NAME.json` and leaves the run otherwise untouched, and `--no-vision` gives the assessor alt text instead of pictures. `python -m userqa reaudit <run-dir>` re-runs only the persona-fidelity audit from the trace and keeps the previous one as `fidelity.prev.json`.

## Personas

`python -m userqa personas list` shows the library in `userqa/personas/library/`. `personas show <id>` prints one, and `personas generate "<description>" -o my.yaml` synthesises a new one. A persona is more than a demographic label. Its fields drive behaviour:

- goals, experience goals and frustrations (goal-directed personas);
- GenderMag cognitive facets: motivation, information processing, self-efficacy, risk attitude, learning style;
- Big Five descriptors, technology and privacy attitudes, language level and accessibility needs;
- a first-person backstory;
- the concrete family facts the persona uses when the site asks.

The **device** (`desktop`, `mobile`, `zoom200`) and **attention** (`full`, `skim`, `low_vision`) settings are enforced by the browser environment. A skimming persona sees long paragraphs cut to their first words. A low-vision persona gets blurred screenshots and cannot read text that fails contrast checks. `patience_steps` sets how many consecutive frustrating steps it tolerates before it would give up. `generic_user` is the no-persona baseline: task facts only.

## Site configs

`experiments/sites/<name>.yaml` tells the agent where to go and what to try:

```yaml
name: storyhearth
url: http://127.0.0.1:8765/
goal: |            # the task, in the words a participant would be given
  ...
credentials: {email: ..., password: ...}   # or inbox: mailtm for sites that e-mail a code
allowed_domains: [127.0.0.1, localhost]    # the agent cannot leave these (plus sign-in providers)
allow_click_patterns: ["regenerate"]       # lift the price soft-block for these buttons
spend_rule: "Do not spend money: ..."
max_steps: 32
max_llm_calls: 45
```

**Safety.** Buttons such as pay, buy, purchase, place order, subscribe, upgrade, buy credits, add card and delete account are hard-blocked, and a site config cannot lift that. Payment-card and banking fields are blocked too. Any other button that shows a price is soft-blocked unless the site config's `allow_click_patterns` allows it; the ourlegacy configs allow the generate buttons, which are paid from free starter credits. The agent is also told never to pay.

## Models and quotas

The default model is OpenRouter's free `stealth/space-bunny-alpha`, which has vision and JSON mode. The client falls back to `google/gemma-4-31b-it:free`, `qwen/qwen3.8-27b:free` and `openrouter/free` on errors. Choose others with `--model` and `--fallbacks`.

Every call is budgeted: `max_llm_calls` in the site config, or `--max-calls`. Calls are retried with back-off and logged with their purpose. `python -m userqa quota` shows the key's limits. OpenRouter allows 50 `:free` requests per day, or 1,000 once the account has bought $10 of credit.

## Experiments (the paper)

```bash
# 1. sessions: every persona x repetition, 3 in parallel, from a frozen copy of the code
python experiments/run_suite.py --site storyhearth --name main --reps 2 \
  --personas grandparent_storykeeper,tech_savvy_parent,busy_parent_mobile,esl_parent,low_vision_senior,privacy_conscious_parent,generic_user

# 2. paired re-assessments of the same captured outputs (vision ablation and test-retest)
python -m userqa reassess runs/suite/main/2026* --variant vision
python -m userqa reassess runs/suite/main/2026* --variant novision --no-vision
python -m userqa reassess runs/suite/main/2026* --variant vision2

# 3. score findings against the seeded defects (LLM judge + keyword baseline; judgments are cached)
python experiments/score_ground_truth.py runs/suite/main
python experiments/score_ground_truth.py runs/suite/main --variant vision   # etc.

# 4. tables, figures and \newcommand numbers for the paper
python experiments/analyze.py --main runs/suite/main --out paper/generated

# 5. build the paper
cd paper && tectonic main.tex
```

The seeded defects are in `demo_sites/storyhearth/ground_truth.json`, outside the web root. `experiments/audit/valid_unseeded_audit.json` is an audit of a random sample of findings that the judge accepted as valid but unseeded. It was labelled by the AI coding assistant that built StoryHearth, not by a person, and should be repeated by a human annotator. `runs/` contains the sessions reported in the paper. Screenshots and captured pictures are not committed, but all JSON, traces and captured output text are, so steps 3 and 4 reproduce every number without new LLM calls.

## Tests

```bash
python -m pytest -q tests
```

The tests cover the text metrics, SUS/UEQ-S scoring, JSON salvage of truncated completions, evidence verification, issue clustering, the safety policy, and the output assessor's superseding, batching and change notes. They include a scripted end-to-end session: a scripted LLM drives a real browser through a tiny local site. It is skipped when no browser can start.

## Layout

```
userqa/
  cli.py, runner.py      command line; one session end to end (browse -> assess output -> debrief -> audit -> report)
  llm.py                 OpenRouter client: budget, retries, fallbacks, lenient JSON
  browser/               Playwright environment: numbered-element observation (observe.js), persona perception
                         filters, safety policy, CAPTCHA reflex, output capture (pages, PDFs, images, video), tab triage
  agent/                 the persona agent loop, prompts, episodic memory
  personas/              persona schema, library, generator
  evaluation/            output assessor, deterministic metrics, questionnaires, fidelity audit, issue clustering
  report/                HTML/Markdown report
  tools/inbox.py         disposable mail.tm inbox for e-mail codes
demo_sites/storyhearth/  the synthetic benchmark site, its server and ground truth
experiments/             suite runner, ground-truth scorer, analysis, site configs, audit
paper/                   LaTeX source and generated tables/figures
tests/
```

## Responsible use

Run the agent only on sites you own or are allowed to test. Keep step and call budgets low on production sites. The agent ticks "verify you are human" checkboxes the way a person would, but it does not solve image or puzzle CAPTCHAs, and it should not be used to get around bot protection. Simulated users are a complement to studies with real people, not a replacement; see the paper's limitations section.
