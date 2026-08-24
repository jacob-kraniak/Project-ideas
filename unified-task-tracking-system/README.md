# Unified Family + Personal Task & Project Tracking System

**Status**: Planning / Architecture locked  
**Date**: 2026-08-23  
**Origin**: Grok conversation (project workspace)  
**Tags**: `#organization` `#projects` `#renovations` `#privacy` `#self-hosted` `#adhd` `#family` `#mcp`

## Problem / Goal

A long-standing goal is a **unified project/task tracking solution** that serves both family and personal needs without SaaS costs or cloud lock-in.

### Family goals
- Overall tracking of projects (renovations, contractors, repairs)
- Vendor / contractor directory and history
- Recurring family tasks and responsibilities
- Easy sharing and visibility for family members

### Personal goals
- Lightweight capture surface for ideas, goals, and projects (ADHD-friendly)
- Many ideas surface over time and are hard to track
- Some currently live in this `Project-ideas` repo and Obsidian

### Constraints & preferences
- Strong preference against SaaS / recurring cloud costs (prior Monday.com trial was not a fit)
- Data sovereignty and privacy are high priority
- Existing Proxmox container/host is available and already running Phase 2 self-hosted services
- Preference for MCP-driven updates from Grok (and potential future private voice interface as a Google Assistant alternative)
- Aligns with existing Actual Budget tags (`#project:Bathroom2026`, etc.), Obsidian vault, and home-network-security self-hosted roadmap

## Recommended Architecture

### Shared / Family core → **Plane.so (self-hosted Community Edition)**
- Modern open-source alternative to Monday / Jira / Linear / ClickUp
- Multi-user workspaces with roles & permissions
- Excellent fit for renovations (Projects + Modules), vendors (Pages/Wiki + custom properties), and recurring work (Cycles)
- Official MCP server available (`makeplane/plane-mcp-server`) that works against self-hosted instances via `PLANE_BASE_URL`
- Deploy via Docker Compose on existing Proxmox host (LXC or small VM)
- Minimum practical resources: 2 vCPU / 4 GB RAM (prefer 4 vCPU / 8 GB)

### Personal / daily driver → **SuperProductivity**
- Local-first, lightweight, timeboxing + focus tools, fast capture
- Strong GitHub integration (can pull from this `Project-ideas` repo)
- Mature community MCP servers/plugins (e.g. b0x42/Super-Productivity-MCP and variants)
- Ideal for personal goals, quick idea dumps, and deep-work sessions
- Promote mature items into Plane when they need family visibility or longer-term tracking

### Ideation / capture layer (already in place)
- This `Project-ideas` repository + Obsidian vault for brainstorming
- Mature ideas get promoted into Plane projects or SuperProductivity tasks

### Integration & MCP path
- **Plane**: Official first-class MCP server. Run locally or on Proxmox pointed at the self-hosted instance. Supports stdio, HTTP, OAuth/API-key auth. ~28–30 resource tools covering projects, work items, cycles, modules, pages, etc.
- **SuperProductivity**: Community MCP bridges (plugin inside SP + local MCP server process). Full task/project/tag CRUD + time-tracking summaries.
- Both enable the preferred Grok MCP workflow for clean, natural-language or structured updates.
- Future private voice interface becomes realistic once the MCP surfaces are live.

Fallback without full MCP: Plane has a solid REST API + webhooks; SuperProductivity can be driven via its plugin API or JSON export/import. Direct SQL against SP storage is possible but brittle.

## Proposed Plane Workspace Structure (initial)

**Workspace**: `Kraniak Family`

Suggested top-level organization:
- **Projects** for active renovations / large efforts (e.g. Bathroom2026, other home projects)
- **Modules** inside projects for contractors, phases, or work packages
- Dedicated project or module for **Vendors & Contractors** (contact info, history, notes, links to invoices/receipts)
- **Recurring Household** project or cycle-based tracking for ongoing responsibilities
- Personal projects area (visible primarily to Jacob) for longer-horizon goals that may later become family-visible
- Custom properties / labels aligned with existing Actual Budget tags where useful
- Pages / Wiki for living documentation, decision logs, and SOPs

Roles: Jacob as admin; family members invited with appropriate project-level visibility.

## Phased Rollout

### Phase 0 – Documentation & Decision (this document)
- [x] Capture requirements and architecture from Grok discussion
- [ ] Confirm Proxmox host headroom and preferred deployment method (LXC vs VM)

### Phase 1 – Plane foundation
- [ ] Deploy Plane Community Edition (Docker Compose) on Proxmox
- [ ] Configure reverse proxy / HTTPS / VPN access as needed (align with existing WireGuard/Tailscale plans)
- [ ] Create workspace, seed with 1–2 real projects (e.g. current renovation + Vendors)
- [ ] Invite family members and validate visibility/roles
- [ ] Document API token + MCP server configuration for self-hosted instance

### Phase 2 – Personal layer + MCP
- [ ] Install / configure SuperProductivity on daily machines
- [ ] Point GitHub integration at this repo (and any other relevant sources)
- [ ] Stand up Plane official MCP server against the self-hosted instance
- [ ] Evaluate / install a SuperProductivity community MCP bridge
- [ ] Test Grok MCP → create/update flows for both systems

### Phase 3 – Operationalization
- [ ] Migrate key existing items (from notes, this repo, Actual Budget tags, etc.)
- [ ] Establish recurring family processes and review cadence
- [ ] Optional: thin local JSON bridge or voice front-end experiments
- [ ] Update `home-network-security` self-hosted-services-roadmap.md to include Plane as a Phase 2 service

### Later
- Bi-directional or selective sync between SuperProductivity and Plane if desired
- Deeper Obsidian / Actual Budget linking
- Private voice assistant surface as Google Assistant replacement

## Related Repositories & Systems
- [Project-ideas](https://github.com/jacob-kraniak/Project-ideas) (this repo) – ideation source
- [home-network-security](https://github.com/jacob-kraniak/home-network-security) – Proxmox + self-hosted services roadmap (cross-reference recommended)
- Actual Budget (local) – existing `#project:*` tags and goal tracking
- Obsidian vault – long-form notes and knowledge base

## Open Questions / Decisions Still Needed
- Exact Proxmox deployment target and resource allocation
- Initial family invite list and permission model
- Whether to run Plane MCP server on the same host or on a daily driver machine
- Priority order for first projects to seed (Bathroom vs others)
- How aggressively to push existing Project-ideas items into Plane vs keeping them in GitHub longer

## Updates / Log
- **2026-08-23**: Initial project plan documented from Grok conversation. Architecture preference locked around self-hosted Plane (family) + SuperProductivity (personal) + official/community MCP. No prior dedicated documentation found in jacob-kraniak repos.

---

*This document follows the Project-ideas workspace conventions. Promote to a dedicated implementation repo only if/when the system moves beyond planning into sustained development.*
