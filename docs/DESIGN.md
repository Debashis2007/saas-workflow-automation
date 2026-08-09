# Design: SaaS Workflow Automation

**Project:** `saas-workflow-automation`  
**Parent system design:** `07-agent-runtime-containment.md`

## 1. What this POC demonstrates

High-impact tools require explicit user approval; tokens injected by broker, not model.

## 2. Architecture (POC)

```text
POST /tools/email.send → ASK_USER unless approved → sent
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Human confirmation for side effects | Email/money/delete are high blast radius. | `ASK_USER`. |
| Broker-injected credentials | Model must not see refresh tokens. | `token` placeholder message. |
| Idempotency key | Retries must not double-send. | `idempotency_key`. |

## 4. Key endpoints

`GET /health`, `POST /tools/email.send`

## 5. Tradeoffs / POC limits

No real OAuth — approval is a boolean field.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

> **Watch on YouTube:** [Saas Workflow Automation — System Design #Shorts](https://youtu.be/GI3LPaCVsTE)
>
> Direct link: **https://youtu.be/GI3LPaCVsTE**

Also available in-repo:
- GIF preview: [`video/design-overview.gif`](./video/design-overview.gif)
- MP4 download: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Narration script: [`video/narration.txt`](./video/narration.txt)

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

