#!/usr/bin/env python3
"""
Enrich frontmatter with feature and/or topic from content + repo corpus defaults.
Skips overview.md and toc.md (any case). Run with --dry-run to preview counts only.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def parse_fm_block(block: str) -> dict[str, str]:
    d: dict[str, str] = {}
    cur_key: str | None = None
    for line in block.splitlines():
        if not line.strip():
            cur_key = None
            continue
        if cur_key and (line.startswith(" ") or line.startswith("\t")):
            d[cur_key] = d[cur_key] + " " + line.strip()
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
            v = v[1:-1]
        d[k] = v
        cur_key = k
    return d


def split_csv(s: str) -> list[str]:
    if not s:
        return []
    return [p.strip() for p in re.split(r",(?![^()]*\))", s) if p.strip()]


def empty(v: str | None) -> bool:
    return v is None or not str(v).strip()


def mine_corpus() -> tuple[dict[str, dict[str, int]], dict[str, dict[str, int]]]:
    sol_feat: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    sol_top: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for p in ROOT.rglob("*.md"):
        if p.name.lower() in ("overview.md", "toc.md"):
            continue
        if p.resolve() == ROOT / "metadata.md":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        block, _ = split_frontmatter(text)
        if not block:
            continue
        fm = parse_fm_block(block)
        sols = split_csv(fm.get("solution", ""))
        feats = split_csv(fm.get("feature", ""))
        tops = split_csv(fm.get("topic", ""))
        for sol in sols:
            for f in feats:
                sol_feat[sol][f] += 1
            for t in tops:
                sol_top[sol][t] += 1
    return sol_feat, sol_top


def top_n(counter: dict[str, int], n: int) -> list[str]:
    return [k for k, _ in sorted(counter.items(), key=lambda x: -x[1])[:n]]


TOPIC_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bgenai\b|\bgen ai\b|generative ai|\bgpt\b|\bllm\b|ai agent|agentic", re.I), "Artificial Intelligence"),
    (re.compile(r"\bheadless\b|graphql|spa\b|react |next\.js|nextjs", re.I), "Headless"),
    (re.compile(r"personaliz|1:1 |audience segment", re.I), "Personalization"),
    (re.compile(r"\bintegrat|api\b|connector|sync with|bi-directional", re.I), "Integrations"),
    (re.compile(r"security|ssl|tls|waf|breach|privacy|consent|cookie", re.I), "Security"),
    (re.compile(r"performance|latency|cache|cdn|fastly|optimize speed|scale\b", re.I), "Performance"),
    (re.compile(r"migrat|upgrade path|cutover", re.I), "Migration"),
    (re.compile(r"govern|compliance|hipaa|shield", re.I), "Administration"),
    (re.compile(r"content supply chain|workfront planning", re.I), "Content Supply Chain"),
    (re.compile(r"certif", re.I), "Certification"),
    (re.compile(r"e-?commerce|b2b commerce|storefront|checkout|cart\b", re.I), "Commerce"),
    (re.compile(r"develop|devops|github|pipeline|code ", re.I), "Development"),
]

FEATURE_RULES: dict[str, list[tuple[re.Pattern[str], str]]] = {
    "Analytics": [
        (re.compile(r"workspace|analysis workspace|freeform", re.I), "Analysis Workspace"),
        (re.compile(r"segment|cohort", re.I), "Segmentation"),
        (re.compile(r"visualization|chart|graph|canvas", re.I), "Visualizations"),
        (re.compile(r"metric|calculated metric", re.I), "Metrics"),
        (re.compile(r"govern|data quality|labelling|labeling", re.I), "Data Governance"),
        (re.compile(r"data source|data collection|debugger|tagging", re.I), "Data Configuration and Collection"),
    ],
    "Customer Journey Analytics": [
        (re.compile(r"derived field|dimension|metric definition", re.I), "Basics"),
        (re.compile(r"use case|funnel|attribution", re.I), "Use Cases"),
        (re.compile(r"integration|connector|bigquery|snowflake", re.I), "Integrations"),
        (re.compile(r"identity|stitching|person id", re.I), "Identity"),
    ],
    "Real-Time Customer Data Platform": [
        (re.compile(r"identity|id graph|namespace", re.I), "Identities"),
        (re.compile(r"profile|unified profile|real-time profile", re.I), "Profiles"),
        (re.compile(r"audience|segment\b", re.I), "Audiences"),
        (re.compile(r"govern|policy|labels|duplicates", re.I), "Data Governance"),
    ],
    "Experience Platform": [
        (re.compile(r"ai assistant|sensei genai", re.I), "AI Assistant"),
        (re.compile(r"agentic|orchestration", re.I), "Agentic AI"),
        (re.compile(r"data collection|event forwarding|tags\b", re.I), "Data Collection"),
        (re.compile(r"audience", re.I), "Audiences"),
        (re.compile(r"personalization", re.I), "Personalization"),
    ],
    "Experience Manager": [
        (re.compile(r"edge delivery|document-based|franklin", re.I), "Edge Delivery Services"),
        (re.compile(r"release|what's new|innovations", re.I), "Release Information"),
        (re.compile(r"app builder|extensibility|sdk", re.I), "Developer Tools"),
        (re.compile(r"author|editor|universal editor", re.I), "Authoring"),
    ],
    "Experience Manager Sites": [
        (re.compile(r"edge delivery|document-based", re.I), "Edge Delivery Services"),
        (re.compile(r"content fragment|graphql", re.I), "Content Fragments"),
        (re.compile(r"author", re.I), "Authoring"),
    ],
    "Experience Manager Assets": [
        (re.compile(r"dynamic media|imaging|video profile", re.I), "Dynamic Media"),
        (re.compile(r"metadata|taxonomy", re.I), "Metadata"),
        (re.compile(r"dam\b|asset\b", re.I), "Asset Management"),
    ],
    "Journey Optimizer": [
        (re.compile(r"journey canvas|orchestrat|journey\b", re.I), "Journeys"),
        (re.compile(r"email|message preset|fragment", re.I), "Email Design"),
        (re.compile(r"audience", re.I), "Audiences"),
        (re.compile(r"code-based|web sdk|in-app", re.I), "Code-based Experiences"),
    ],
    "Marketo Engage": [
        (re.compile(r"program template|program library|program status", re.I), "Programs"),
        (re.compile(r"smart list|smart campaign", re.I), "Smart Lists"),
        (re.compile(r"design studio|email editor", re.I), "Design Studio"),
        (re.compile(r"report|performance insights", re.I), "Reporting"),
    ],
    "Commerce": [
        (re.compile(r"integration|connector|oms|erp", re.I), "Integration"),
        (re.compile(r"headless|graphql|api mesh", re.I), "Headless"),
        (re.compile(r"b2b|quote|company account", re.I), "B2B"),
        (re.compile(r"payment|checkout", re.I), "Payments"),
        (re.compile(r"edge delivery", re.I), "Edge Delivery Services"),
    ],
    "Workfront": [
        (re.compile(r"fusion|scenario", re.I), "Workfront Fusion"),
        (re.compile(r"resource management|workload|capacity", re.I), "Resource Management"),
        (re.compile(r"report|dashboard|text mode", re.I), "Reports and Dashboards"),
        (re.compile(r"admin|setup|configuration|instance", re.I), "System Setup and Administration"),
        (re.compile(r"board|agile|kanban", re.I), "Work Management"),
        (re.compile(r"content supply|planning", re.I), "Strategic Planning"),
    ],
    "Target": [
        (re.compile(r"a/b|ab test|experiment|activity\b", re.I), "A/B Tests"),
        (re.compile(r"ai assistant", re.I), "AI Assistant"),
        (re.compile(r"segment|audience", re.I), "Segments"),
        (re.compile(r"profile|rtcdp", re.I), "Profiles"),
    ],
    "Acrobat Sign": [
        (re.compile(r"sign|agreement|workflow", re.I), "Sign"),
    ],
    "Data Collection": [
        (re.compile(r"tag|launch|data layer", re.I), "Tags"),
        (re.compile(r"event forward", re.I), "Event Forwarding"),
    ],
}


def sample_body(body: str, limit: int = 2500) -> str:
    body = re.sub(r"^#+.*$", " ", body, flags=re.M)
    body = re.sub(r"\[!VIDEO\].*", " ", body, flags=re.I)
    return body[:limit]


def infer_topics(blob: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for pat, top in TOPIC_RULES:
        if pat.search(blob) and top not in seen:
            out.append(top)
            seen.add(top)
        if len(out) >= 3:
            break
    return out


def infer_features_for_solution(sol: str, blob: str, sol_feat: dict[str, dict[str, int]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for pat, feat in FEATURE_RULES.get(sol, []):
        if pat.search(blob) and feat not in seen:
            out.append(feat)
            seen.add(feat)
        if len(out) >= 3:
            break
    if not out:
        for f in top_n(sol_feat.get(sol, {}), 2):
            if f not in seen:
                out.append(f)
                seen.add(f)
            if len(out) >= 2:
                break
    return out


def merge_features_for_solutions(
    sols: list[str], blob: str, sol_feat: dict[str, dict[str, int]]
) -> list[str]:
    acc: list[str] = []
    seen: set[str] = set()
    for sol in sols:
        for f in infer_features_for_solution(sol, blob, sol_feat):
            if f not in seen:
                acc.append(f)
                seen.add(f)
        if len(acc) >= 4:
            break
    return acc[:4]


def merge_topics_for_solutions(
    sols: list[str], blob: str, sol_top: dict[str, dict[str, int]]
) -> list[str]:
    base = infer_topics(blob)
    seen = set(base)
    if not base and sols:
        primary = sols[0]
        if primary != "General":
            for t in top_n(sol_top.get(primary, {}), 2):
                if t not in seen:
                    base.append(t)
                    seen.add(t)
    if not base and sols:
        for sol in sols:
            for t in top_n(sol_top.get(sol, {}), 1):
                if t not in seen:
                    base.append(t)
                    seen.add(t)
                    break
            if base:
                break
    if not base:
        base = ["Development"]
    return base[:4]


def infer_solution_from_path_and_content(path: Path, fm: dict[str, str], blob: str) -> list[str]:
    """When solution: is missing, infer primary solution for tagging."""
    s = str(path).lower()
    blob_l = blob.lower()
    title_l = (fm.get("title") or "").lower()

    if "workfront" in s or "wake-up-with-workfront" in s:
        return ["Workfront"]
    if "marketo" in s or "mochas" in s or "foundations-of-marketo" in s:
        return ["Marketo Engage"]
    if "commerce" in s and "customer" not in s:
        return ["Commerce"]
    if "acrobat-sign" in s:
        return ["Acrobat Sign"]
    if "data-drip" in s or ("skill-exchange" in s and "analytics" in s):
        return ["Analytics"]
    if "cja" in s or "customer-journey-analytics" in s:
        return ["Customer Journey Analytics"]
    if "journey-optimizer" in s or "/ajo" in s:
        return ["Journey Optimizer"]
    if "target" in s and "skill-exchange" in s:
        return ["Target"]
    if "experience-manager" in s or "aem" in s or "espressos-and-experience" in s:
        return ["Experience Manager"]
    if "adobe-developers-live" in s or "experience-manager-gems" in s:
        return ["Experience Manager"]
    if "tech-sessions" in s:
        if "marketo" in title_l or "marketo" in blob_l:
            return ["Marketo Engage"]
        if "aem" in title_l or "experience manager" in blob_l or "forms" in title_l:
            return ["Experience Manager"]
        if "commerce" in title_l:
            return ["Commerce"]
    if "customer-success" in s or "learn-from-your-peers" in s:
        if "aem" in title_l or "experience manager" in blob_l or "edge delivery" in blob_l:
            return ["Experience Manager"]
        if "workfront" in title_l or "content supply chain" in blob_l:
            return ["Workfront"]
        if "commerce" in title_l or "b2b" in title_l:
            return ["Commerce"]
        if "cja" in title_l or "customer journey" in blob_l:
            return ["Customer Journey Analytics"]
        if "rtcdp" in title_l or "real-time" in title_l or "cdp" in title_l:
            return ["Real-Time Customer Data Platform"]
        if "marketo" in title_l:
            return ["Marketo Engage"]
        topic_hint = (fm.get("topic") or "").lower()
        if "content supply chain" in topic_hint:
            return ["Workfront"]
    if "skill-exchange" in s:
        if "/aem/" in s or "/aem" in s:
            return ["Experience Manager"]
        if "/workfront/" in s:
            return ["Workfront"]
        if "/marketo/" in s:
            return ["Marketo Engage"]
        if "/cja/" in s:
            return ["Customer Journey Analytics"]
        if "/aep" in s or "aep-apps" in s:
            return ["Experience Platform", "Journey Optimizer"]
    if "deep-dives" in s and "marketo" in blob_l:
        return ["Marketo Engage"]
    if "perfect-blend" in s:
        return ["Real-Time Customer Data Platform", "Target"]
    # Adobe Commerce webinars accelerator
    if "adobe-commerce-webinars" in s:
        return ["Commerce"]
    return []


def insert_after_key(block: str, anchor: str, new_lines: list[str]) -> str:
    lines = block.splitlines()
    idx = None
    for i, ln in enumerate(lines):
        if ln.startswith(f"{anchor}:"):
            idx = i
            break
    if idx is None:
        raise KeyError(anchor)
    j = idx + 1
    while j < len(lines) and (lines[j].startswith(" ") or lines[j].startswith("\t")):
        j += 1
    for k, nl in enumerate(new_lines):
        lines.insert(j + k, nl)
    out = "\n".join(lines)
    if block.endswith("\n"):
        out += "\n"
    return out


def pick_anchor(fm: dict[str, str], need_f: bool, need_t: bool) -> str:
    has_fs = not empty(fm.get("feature-set"))
    has_feat = not empty(fm.get("feature"))
    has_sol = not empty(fm.get("solution"))

    if need_f:
        if has_fs:
            return "feature-set"
        if has_sol:
            return "solution"
        return "description"

    if need_t:
        if has_feat:
            return "feature"
        if has_fs:
            return "feature-set"
        if has_sol:
            return "solution"
        return "description"

    return "description"


def process_file(
    path: Path,
    sol_feat: dict[str, dict[str, int]],
    sol_top: dict[str, dict[str, int]],
    dry_run: bool,
) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    block, body = split_frontmatter(text)
    if not block:
        return None
    fm = parse_fm_block(block)
    need_f = empty(fm.get("feature"))
    need_t = empty(fm.get("topic"))
    if not need_f and not need_t:
        return None

    sols = split_csv(fm.get("solution", ""))
    blob = " ".join(
        filter(
            None,
            [
                fm.get("title", ""),
                fm.get("description", ""),
                sample_body(body),
            ],
        )
    )
    if not sols:
        sols = infer_solution_from_path_and_content(path, fm, blob)

    new_feat: list[str] = []
    new_top: list[str] = []

    if sols and sols[0] != "General":
        if need_f:
            new_feat = merge_features_for_solutions(sols, blob.lower(), sol_feat)
        if need_t:
            new_top = merge_topics_for_solutions(sols, blob.lower(), sol_top)
    else:
        if need_t:
            new_top = infer_topics(blob.lower()) or ["Development"]
        if need_f and sols and sols[0] != "General":
            new_feat = merge_features_for_solutions(sols, blob.lower(), sol_feat)
        elif need_f and sols:
            pass
        elif need_f and not sols:
            # Infer solution again strictly from path for feature
            sols2 = infer_solution_from_path_and_content(path, fm, blob)
            if sols2:
                new_feat = merge_features_for_solutions(sols2, blob.lower(), sol_feat)
            elif re.search(r"web sdk|analytics|adobe experience platform", blob, re.I):
                new_feat = merge_features_for_solutions(["Analytics"], blob.lower(), sol_feat)
            elif re.search(r"workfront|data connect", blob, re.I):
                new_feat = merge_features_for_solutions(["Workfront"], blob.lower(), sol_feat)

    to_insert: list[str] = []
    if need_f and new_feat:
        to_insert.append("feature: " + ", ".join(new_feat))
    if need_t and new_top:
        to_insert.append("topic: " + ", ".join(new_top))
    if not to_insert:
        return None

    anchor = pick_anchor(
        fm,
        need_f and bool(new_feat),
        need_t and bool(new_top),
    )
    # If only inserting topic but no anchor line (no solution/feature/description?) — rare
    try:
        new_block = insert_after_key(block, anchor, to_insert)
    except KeyError:
        anchor = "title"
        new_block = insert_after_key(block, anchor, to_insert)

    # Ensure blank line before closing --- (splitlines drops final newline)
    fm_core = new_block.rstrip("\n")
    new_text = "---\n" + fm_core + "\n---\n" + body
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return path.as_posix()


def main() -> None:
    dry = "--dry-run" in sys.argv
    sol_feat, sol_top = mine_corpus()
    changed: list[str] = []
    errors: list[tuple[str, str]] = []
    for p in sorted(ROOT.rglob("*.md")):
        if p.name.lower() in ("overview.md", "toc.md"):
            continue
        # Repo-level metadata; not an event page
        if p.resolve() == ROOT / "metadata.md":
            continue
        try:
            r = process_file(p, sol_feat, sol_top, dry)
            if r:
                changed.append(r)
        except Exception as e:
            errors.append((p.as_posix(), str(e)))
    print(f"{'Would change' if dry else 'Changed'}: {len(changed)} files")
    if errors:
        print(f"Errors: {len(errors)}")
        for path, msg in errors[:25]:
            print(path, msg)


if __name__ == "__main__":
    main()
