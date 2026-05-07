# Personal Repo Sanitizer

Lightweight suite of hooks and actions to keep personal GitHub activity clean of organizational data.

## Problem / Motivation
Occasional oversights when copying internal code or notes lead to security alerts. A proactive multi-layer defense reduces risk and saves time.

## Proposed Solution
Combine local pre-commit hooks with a centralized GitHub Action. The tool scans for user-defined keywords, offers automatic redaction suggestions, and enforces policy on push/PR.

## Tech Stack Suggestions
- pre-commit framework + custom hook
- GitHub Actions matrix for multiple repos
- Python with `re` module or `detect-secrets` library
- Optional: GitHub App or Dependabot-style reusable workflow

## Feasibility / Challenges
- Challenge 1: Performance on large repositories
- Challenge 2: Educating the user on false-positive tuning
- Challenge 3: Handling binary files and large documents

## Next Steps / Milestones
1. Set up pre-commit config with initial hooks
2. Build the GitHub Action composite action
3. Create a template repository that new repos can copy
4. Add reporting dashboard (simple Markdown summary)
5. Explore integration with VS Code extension for real-time warnings

**Additional files to suggest** (list with brief description of purpose/content, or "none"):
- `.pre-commit-config.yaml` → Configuration for local hooks
- `sanitizer_action.yml` → Composite action for easy reuse
- `patterns.yaml` → Structured keyword list with severity levels
- `redact_example.py` → Script demonstrating automatic masking of matched strings
