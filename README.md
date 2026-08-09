# Use Case: SaaS Workflow Automation

**YouTube walkthrough:** [Saas Workflow Automation — System Design #Shorts](https://youtu.be/GI3LPaCVsTE)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [07 — Agent Runtime with Hard Containment](../07-agent-runtime-containment.md)

## Users & problem

Agents create tickets, send email, update CRM. Side effects are real—so high-impact actions need confirmation and scoped OAuth tokens the model never fully possesses.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Auth | User-held OAuth; short-lived injection |
| Confirm | Human approval for send/delete/pay |
| Audit | Full tool trace |
| Least privilege | Per-connector scopes |

## Design (from parent)

```
Model tool_call → policy risk score
  → ASK_USER if high impact
  → broker injects scoped token → SaaS API
  → result observation → continue
```

Reuse policy engine + connector token pattern from **07**.

## Specializations

| Concern | SaaS automation choice |
|---------|------------------------|
| UX | Approval cards in product UI |
| Idempotency | Dedupe sends with idempotency keys |
| Rate | Per-connector quotas |
| Revocation | User can revoke connector anytime |

## Failure modes

- Model hallucinates “user approved” → only UI/approval service grants.
- Over-scoped token → request minimal scopes at connect time.
- Duplicate emails on retry → idempotent broker.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Saas Workflow Automation — System Design #Shorts](https://youtu.be/GI3LPaCVsTE)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd saas-workflow-automation
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/tools/email.send -H 'Content-Type: application/json' -d '{"to":"a@b.com","body":"hi","approved":false}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

