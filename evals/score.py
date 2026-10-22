#!/usr/bin/env python3
"""Score prd-reviewer outputs against the answer key.

Usage: python score.py RESULTS_DIR MAPPING_FILE [LABELS_FILE]

RESULTS_DIR holds one JSON file per review (prd-01.json ...), each shaped:
  {"verdict": "Ready|Needs work|Not ready",
   "blockers": [{"title": "...", "why": "...", "fix": "..."}],
   "improvements": ["..."], "questions": ["..."]}
MAPPING_FILE maps blinded ids to test cases, one "prd-01 n3-meeting-summaries" per line.
"""
import json, os, sys

def main():
    results_dir, mapping_file = sys.argv[1], sys.argv[2]
    labels_file = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(__file__), "labels.json")
    labels = json.load(open(labels_file))
    mapping = dict(line.split() for line in open(mapping_file) if line.strip())

    rows, correct, planted, caught, false_alarms = [], 0, 0, 0, 0
    for pid, case in sorted(mapping.items()):
        out = json.load(open(os.path.join(results_dir, pid + ".json")))
        lab = labels[case]
        verdict = out["verdict"].strip()
        ok = verdict.lower() == lab["expected"].lower()
        correct += ok
        text = " ".join(" ".join(str(b.get(k, "")) for k in ("title", "why", "fix")) for b in out.get("blockers", [])).lower()
        hits = {name: any(k in text for k in kws) for name, kws in lab["blockers"].items()}
        planted += len(hits); caught += sum(hits.values())
        if lab["expected"] == "Ready":
            false_alarms += len(out.get("blockers", []))
        rows.append((case, lab["expected"], verdict, ok, hits, len(out.get("blockers", []))))

    for case, exp, got, ok, hits, nb in rows:
        miss = [n for n, h in hits.items() if not h]
        print(f"{'OK ' if ok else 'XX '} {case:<26} expected {exp:<11} got {got:<11} blockers={nb}"
              + (f"  missed: {', '.join(miss)}" if miss else ""))
    n = len(rows)
    summary = {"verdict_accuracy": f"{correct}/{n}", "blockers_caught": f"{caught}/{planted}",
               "false_blockers_on_ready_prds": false_alarms}
    print("\n" + json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
