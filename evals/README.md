# Evals for prd-reviewer

A small test set and scorer used in the article "How Do You Know Your AI Agent Is Actually Getting Better?"

- `prds/`: 19 test PRDs. `r-*` should be Ready, `n-*` Needs work, `x-*` Not ready, and `h-*` are harder borderline cases. `h7` is a held-out copy of `h3` with headings the checker has never seen.
- `labels.json`: the answer key, with each PRD's expected verdict and the blockers a good review must name. Labels were written before any run. One label (`h5`) was corrected after review, and the note explains why.
- `score.py`: compares review outputs to the answer key.
- `results/`: the actual review outputs from each round, with the blinded id-to-case mapping.

Re-score a round:

```bash
python evals/score.py evals/results/round1 evals/results/round1/mapping.txt
python evals/score.py evals/results/round2 evals/results/round2/mapping.txt
```

To run your own round, have an agent with the skill installed review each PRD (renamed to neutral ids so file names don't hint at the answer) and save one JSON file per review in the shape `score.py` describes.

These PRDs are realistic but invented. For your own team, build the test set from real past PRDs.
