"""Pure budget-window evaluation helpers."""

from __future__ import annotations

from typing import Any


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def evaluate_budget_window(state: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    estimated_cost = _as_float(state.get("estimated_cost"))
    remaining_budget = _as_float(state.get("remaining_budget"))
    max_estimated_cost = _as_float(policy.get("max_estimated_cost"))
    review_threshold = _as_float(policy.get("review_threshold"))

    if remaining_budget <= 0:
        return {
            "decision": "block",
            "reason": "Remaining budget is exhausted.",
            "estimated_cost": estimated_cost,
            "remaining_budget": remaining_budget,
            "policy_refs": ["remaining_budget"],
        }

    if estimated_cost > max_estimated_cost:
        return {
            "decision": "block",
            "reason": "Estimated cost exceeds the configured max estimated cost.",
            "estimated_cost": estimated_cost,
            "remaining_budget": remaining_budget,
            "policy_refs": ["max_estimated_cost"],
        }

    if remaining_budget <= review_threshold:
        return {
            "decision": "review",
            "reason": "Remaining budget is inside the review threshold.",
            "estimated_cost": estimated_cost,
            "remaining_budget": remaining_budget,
            "policy_refs": ["review_threshold"],
        }

    return {
        "decision": "allow",
        "reason": "Budget window allows model execution.",
        "estimated_cost": estimated_cost,
        "remaining_budget": remaining_budget,
        "policy_refs": ["max_estimated_cost", "review_threshold"],
    }
