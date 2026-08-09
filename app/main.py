# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""SaaS Workflow Automation — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "SaaS Workflow Automation"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


class EmailIn(BaseModel):
    to: str
    body: str
    approved: bool = False

@app.post("/tools/email.send")
def email_send(body: EmailIn):
    if not body.approved:
        return {"status": "ASK_USER", "tool": "email.send", "reason": "high_impact_side_effect"}
    return {"status": "sent", "to": body.to, "idempotency_key": "email-1", "token": "injected-scoped-not-in-prompt"}
