from __future__ import annotations

import json
from pathlib import Path

from token_governor_langchain_middleware.budget import evaluate_budget_window


ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads(
    (ROOT / "examples" / "policies" / "budget-window.policy.json").read_text()
)


def test_budget_ok_state_returns_allow() -> None:
    state = json.loads((ROOT / "examples" / "states" / "budget-ok.state.json").read_text())

    decision = evaluate_budget_window(state, POLICY)

    assert decision["decision"] == "allow"
    assert decision["remaining_budget"] == 0.08


def test_budget_blocked_state_returns_block() -> None:
    state = json.loads(
        (ROOT / "examples" / "states" / "budget-blocked.state.json").read_text()
    )

    decision = evaluate_budget_window(state, POLICY)

    assert decision["decision"] == "block"
    assert "max estimated cost" in str(decision["reason"]).lower()
