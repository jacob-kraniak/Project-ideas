# Project: Cybersecurity Certification Progress Tracker on GitHub

## Origin
- Grok conversation: https://grok.com/share/bGVnYWN5_495ac091-88ab-41f1-940d-7ae64e58e28f
- Date conversation created: approx. 2026-02-08
- Date this summary generated: 2026-02-08
- Tags: #cybersecurity #certifications #github-profile #progress-tracking #roadmap #documentation #career-growth

## Problem / Goal
Document active and expired cybersecurity/IT certifications publicly on the GitHub profile (https://github.com/jacob-kraniak) to showcase career progression, foundational skills (e.g., CompTIA Server+ active, A+/Network+ expired), and ongoing research toward advanced certs. Provide a clean, verifiable, low-maintenance showcase of completions while using a separate Kanban-style GitHub Project for dynamic tracking of research, study progress, and future cert plans, inspired by Paul Jerimy's Security Certification Roadmap and CyberSecCertificates.com.

## Proposed Solution
Static Markdown table and small badge embeds in profile README.md for completed/active certs (Credly-verified, hosted images for transparency control). Separate interactive GitHub Project (Kanban board) for pipeline/research tracking of upcoming certs (e.g., Security+ → CySA+). Long-term: explore GitHub Actions to auto-update README from project status changes (e.g., completed cards trigger badge additions or progress summaries).

## Tech Stack (planned)
- Language(s): None (Markdown + GitHub native features); optional YAML for Actions later
- Core libraries / frameworks: GitHub README Markdown, Credly badge embeds/images, GitHub Projects (Kanban/Roadmap views)
- Deployment target / environment: GitHub profile README & Projects (no external hosting)
- Data sources / integrations (if any): Credly public badges (manual or via pemtajo/badge-readme Action), Paul Jerimy roadmap & CyberSecCertificates links

## Key Features / Scope
**Must-have:**
- Compact table in README with cert name, issuer, status, dates, notes, and verification links
- Small clickable badge image for active cert (Server+) in dedicated section
- Pointer/link to Kanban project for ongoing research and progress tracking
- Transparency-controlled images hosted in repo to avoid Credly resize/white-background issues

**Nice-to-have / future:**
- Auto-pull/update all Credly badges via GitHub Action
- Dynamic README updates (e.g., progress %, new completed badges) triggered by Kanban status changes
- Embed roadmap visuals or progress bars (Shields.io)

## Challenges & Open Questions
- GitHub README limitations on JS embeds (Credly dynamic cards don't render → static images required)
- No native webhook/trigger for new GitHub Projects status changes to update README automatically
- Maintaining consistency between static README completions and dynamic project pipeline

## Next Steps
- [ ] Create GitHub Project "Cybersecurity Certification Roadmap & Progress" (Kanban board) with columns: Planned, Researching, In Progress, Completed
- [ ] Seed initial issues/cards (start with CompTIA Security+ including roadmap links/resources)
- [ ] Update README with final Kanban project link once created
- [ ] Test pemtajo/badge-readme Action for future auto-updates of Credly badges
- [ ] Explore simple Action workflow for README refresh on issue/project events

## Priority / Effort
- Priority: High (directly supports career documentation and visible progress signaling)
- Estimated effort to minimal POC: 2–4 hours (README polish + project creation + initial cards)

## Updates / Log
- 2026-02- approx. 05–08: Initial discussion → explored Credly embeds vs static images → resolved transparency/white-background issues → finalized Option 2 README structure with separate badge section and details table → incorporated all three CompTIA certs (Server+ active, A+/Network+ expired) with verification links
https://grok.com/c/d753704c-810a-4a68-a937-5e5a57a69e61?rid=edf85ce2-9f93-402c-83f7-cde074bc482b
## GitHub Tracking
- Issue: (create in repo and link here after commit, e.g. [#X](https://github.com/jacob-kraniak/Project-ideas/issues/X))https://grok.com/c/d753704c-810a-4a68-a937-5e5a57a69e61?rid=edf85ce2-9f93-402c-83f7-cde074bc482b
- Project board card: (add to Grok Ideas Pipeline board and link here)

## Current Status
Early implementation stage: README updated with static badge (Server+) and table of cert details (active + expired). No dedicated Kanban project created yet; conversation focused on design and refinement of display options (embeds → static images → table vs separate sections).

## Past Milestones
- approx. 2026-02-05–08: Explored multiple README layouts (large embeds, progress bars, tables, badge sections) → settled on Option 2 (small active badge + details table) → resolved image transparency/hosting via repo uploads → incorporated expired cert links/images

## Recommendation for Repo Move
No – still in early brainstorming/documentation phase with no code/POC beyond Markdown. Keep in /ideas/ folder of Project-ideas repo (e.g., as ideas/cyber-cert-progress-tracker.md). Move to dedicated repo only after Kanban is built, populated, and any Actions are prototyped (suggested future name: cyber-cert-tracker, slug: cyber-cert-tracker).
