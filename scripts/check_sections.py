#!/usr/bin/env python3
"""Check a PRD (Markdown or plain text) for required sections.

Usage:
    python check_sections.py path/to/prd.md
    python check_sections.py path/to/prd.md --json
    cat prd.md | python check_sections.py -

Exit code: 0 if all required sections are present and substantive,
1 if anything is missing or thin, 2 on usage errors.
"""
import argparse
import json
import re
import sys

# Each section: canonical name, heading aliases (lowercase), required?, minimum words.
SECTIONS = [
    ("Problem", ["problem", "problem statement", "background", "context", "why", "motivation",
                 "pain", "pain point", "opportunity", "the pain"], True, 40),
    ("Success metrics", ["success metrics", "metrics", "success criteria", "goals", "kpis", "measuring success",
                         "how we'll know", "how we will know", "measures of success", "outcomes"], True, 15),
    ("Scope & non-goals", ["scope", "non-goals", "non goals", "out of scope", "in scope",
                           "what we're building", "not building", "boundaries"], True, 15),
    ("Requirements", ["requirements", "functional requirements", "user stories", "solution", "proposal", "features",
                      "behavior", "behaviour", "specification", "spec", "acceptance criteria"], True, 60),
    ("Risks & dependencies", ["risks", "dependencies", "open questions", "risks and dependencies", "assumptions",
                              "watch-outs", "watch outs", "watchouts", "concerns", "unknowns"], True, 15),
    ("Rollout", ["rollout", "launch", "launch plan", "release plan", "go-to-market", "gtm", "rollout plan",
                 "shipping", "release", "ship it"], True, 20),
    ("Users", ["users", "target users", "personas", "audience", "who", "who it's for", "customers"], False, 15),
    ("Timeline", ["timeline", "milestones", "schedule", "phases"], False, 10),
]

HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
METRIC_HINT_RE = re.compile(r"\d|%|baseline|target|increase|decrease|reduce", re.I)


def normalize(title: str) -> str:
    title = re.sub(r"^[\d.\)\s]+", "", title)          # strip "1." / "2)" numbering
    title = re.sub(r"[*_`:]", "", title)               # strip markdown emphasis / colons
    return re.sub(r"\s+", " ", title).strip().lower()


def split_sections(text: str):
    """Return a list of (heading, body, level) tuples from Markdown headings."""
    sections, heading, level, body = [], None, 0, []
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            if heading is not None:
                sections.append((heading, "\n".join(body), level))
            heading, level, body = m.group(2), len(m.group(1)), []
        else:
            body.append(line)
    if heading is not None:
        sections.append((heading, "\n".join(body), level))
    return sections


def match_section(heading: str):
    h = normalize(heading)
    for name, aliases, _, _ in SECTIONS:
        if any(h == a or h.startswith(a + " ") or a in h.split(" & ") or a in h.split(" and ") for a in aliases):
            return name
    for name, aliases, _, _ in SECTIONS:            # looser fallback: alias contained in heading
        if any(a in h for a in aliases):
            return name
    return None


def word_count(s: str) -> int:
    return len(re.findall(r"\b\w+\b", s))


def check(text: str):
    found, unrecognized = {}, []
    for heading, body, level in split_sections(text):
        name = match_section(heading)
        if not name and level > 1:  # level-1 heading is the document title
            unrecognized.append(heading.strip())
        if name:
            entry = found.setdefault(name, {"headings": [], "words": 0, "body": ""})
            entry["headings"].append(heading.strip())
            entry["words"] += word_count(body)
            entry["body"] += "\n" + body

    results, issues = [], []
    for name, _, required, min_words in SECTIONS:
        if name not in found:
            status = "missing"
            if required:
                issues.append(f"Missing required section: {name}")
        elif found[name]["words"] < min_words:
            status = "thin"
            if required:
                issues.append(f"{name} is thin ({found[name]['words']} words; expected at least {min_words})")
        else:
            status = "ok"
        if name == "Success metrics" and name in found and not METRIC_HINT_RE.search(found[name]["body"]):
            issues.append("Success metrics contain no numbers, baselines or targets")
            if status == "ok":
                status = "unmeasurable"
        results.append({
            "section": name,
            "required": required,
            "status": status,
            "words": found.get(name, {}).get("words", 0),
            "headings": found.get(name, {}).get("headings", []),
        })

    if not split_sections(text):
        issues.insert(0, "No Markdown headings found; the document may be an early idea rather than a PRD")

    return {
        "total_words": word_count(text),
        "sections": results,
        "issues": issues,
        "unrecognized_headings": unrecognized,
        "passed": not issues,
    }


def print_report(report):
    icons = {"ok": "OK  ", "thin": "THIN", "missing": "MISS", "unmeasurable": "WEAK"}
    print(f"PRD section check ({report['total_words']} words)\n")
    for r in report["sections"]:
        tag = "required" if r["required"] else "optional"
        found = f" <- {', '.join(r['headings'])}" if r["headings"] else ""
        print(f"[{icons[r['status']]}] {r['section']:<22} {tag:<9} {r['words']:>4} words{found}")
    if report["unrecognized_headings"]:
        print("\nUnrecognized headings (check these before calling a section missing):")
        for h in report["unrecognized_headings"]:
            print(f"  - {h}")
    print()
    if report["issues"]:
        print("Issues:")
        for i in report["issues"]:
            print(f"  - {i}")
    else:
        print("All required sections present and substantive.")


def main():
    p = argparse.ArgumentParser(description="Check a PRD for required sections.")
    p.add_argument("path", help="PRD file (Markdown or text), or - for stdin")
    p.add_argument("--json", action="store_true", help="print JSON only")
    args = p.parse_args()

    try:
        text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)

    report = check(text)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
