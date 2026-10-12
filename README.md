# prd-reviewer

An [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that reviews product requirement documents for completeness, clarity and engineering readiness.

You give it a PRD, and you get back a verdict (**Ready / Needs work / Not ready**), the top three blockers with suggested fixes, smaller improvements, and questions only the author can answer.

## What's inside

```
prd-reviewer/
├── SKILL.md                    # When to use + review workflow and rules
├── scripts/
│   └── check_sections.py       # Flags missing or thin sections (no dependencies)
├── references/
│   └── prd-standards.md        # The bar for "ready for eng", section by section
├── assets/
│   └── prd-template.md         # House PRD format used for suggested rewrites
└── examples/
    └── sample-prd.md           # A realistic PRD to try it on
```

The work is split deliberately. The script catches structural gaps with no guesswork. The standards doc carries the judgment calls. The model reads for nuance and writes the feedback.

## Install

**Claude apps (claude.ai, desktop):** Zip the `prd-reviewer` folder and upload it as a custom skill in your Claude settings.

**Claude Code:** Copy the folder into your skills directory:

```bash
# Personal (all projects)
cp -r prd-reviewer ~/.claude/skills/

# Or project-only
cp -r prd-reviewer .claude/skills/
```

**Claude API:** Upload it through the Skills API. See the [Agent Skills docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

## Use

Share a PRD and ask something like:

> Review this PRD. Is it ready for eng?

The skill triggers from its description, so you don't need to name it.

## Run the checker on its own

The script uses only the Python standard library (3.8+).

```bash
python scripts/check_sections.py examples/sample-prd.md
python scripts/check_sections.py my-prd.md --json
cat my-prd.md | python scripts/check_sections.py -
```

Sample output:

```
PRD section check (243 words)

[OK  ] Problem                required    66 words <- Problem
[OK  ] Success metrics        required    30 words <- Success metrics
[OK  ] Scope & non-goals      required    20 words <- Scope
[OK  ] Requirements           required    87 words <- Requirements
[OK  ] Risks & dependencies   required    31 words <- Risks
[MISS] Rollout                required     0 words
[MISS] Users                  optional     0 words
[MISS] Timeline               optional     0 words

Issues:
  - Missing required section: Rollout
```

It exits with `0` when all required sections pass and `1` otherwise, so you can also use it in CI on a `docs/prds/` folder.

## Customize it for your team

- **Your bar:** Edit `references/prd-standards.md`. This is where most of the value lives.
- **Your format:** Replace `assets/prd-template.md` with your team's template.
- **Your section names:** Edit the `SECTIONS` list at the top of `scripts/check_sections.py` to add heading aliases or change minimum word counts.
- **Your verdict rules:** Adjust the "Verdict rules" in `SKILL.md`.

## License

MIT
