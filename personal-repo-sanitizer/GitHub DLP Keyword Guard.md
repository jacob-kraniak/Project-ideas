# GitHub DLP Keyword Guard

Automated protection against accidental exposure of internal company identifiers, secrets, or sensitive strings in your personal and work-related repositories.

## Problem / Motivation
When moving internal tools, scripts, or notes to personal GitHub repos it is easy to miss a hardcoded company name, internal domain, IP range, or employee reference. Dark-web monitoring services then flag these as leaks. Manual scrubbing is error-prone and time-consuming.

## Proposed Solution
A reusable GitHub Action workflow that runs on every push and PR. It uses regex-based scanning (with optional Gitleaks or Nightfall integration) against a customizable list of forbidden patterns. Fail the build or post a comment if matches are found.

## Tech Stack Suggestions
- GitHub Actions (workflow YAML)
- `gitleaks/gitleaks-action` or `nightfallai/nightfall-action`
- Custom regex list stored in `.github/dlp-patterns.txt` or repo secrets
- Python or Go script for advanced pattern matching (optional)
- Slack/Email/Teams notification on failure

## Feasibility / Challenges
- Challenge 1: Balancing sensitivity (false positives) vs. strictness
- Challenge 2: Keeping the keyword list up-to-date without exposing it publicly
- Challenge 3: Handling encrypted or base64-encoded strings that still contain sensitive data

## Next Steps / Milestones
1. Create the repository folder and initial workflow YAML
2. Define a starter set of regex patterns (company name, domains, etc.)
3. Test the action on a private test repo with planted keywords
4. Add optional allow-list and PR comment reporting
5. Document how to reuse the workflow across multiple repositories via `uses:`

**Additional files to suggest** (list with brief description of purpose/content, or "none"):
- `.github/workflows/dlp-scan.yml` → Main reusable workflow file with triggers and steps
- `.github/dlp-patterns.txt` → Example regex patterns (one per line, commented)
- `scan.py` → Optional Python helper that loads patterns and scans files with context reporting
- `example-leak.md` → Test file containing fake sensitive strings for validation
- `architecture.puml` → PlantUML diagram showing workflow trigger → scan → alert flow
