"""Thin LangChain middleware adapter for budget-window checks."""

from __future__ import annotations

from typing import Any

from .budget import evaluate_budget_window

try:
    from langchain.agents.middleware import AgentMiddleware, hook_config
except Exception:  # pragma: no cover - fallback for import compatibility
    class AgentMiddleware:  # type: ignore[no-redef]
        """Fallback base when LangChain middleware types are unavailable."""

    def hook_config(*, can_jump_to: list[str] | None = None):  # type: ignore[no-redef]
        del can_jump_to

        def decorator(func):
            return func

        return decorator


class BudgetWindowMiddleware(AgentMiddleware):
    """Budget-aware check before model execution.

    This adapter intentionally stays small. It evaluates local state against a
    local budget policy and returns either:
    - ``None`` to continue model execution,
    - a state update for ``review``,
    - or a state update plus ``jump_to: "end"`` for ``block``.
    """

    def __init__(self, policy: dict[str, Any]):
        self.policy = policy

    @hook_config(can_jump_to=["end"])
    def before_model(
        self, state: dict[str, Any], runtime: Any = None
    ) -> dict[str, Any] | None:
        del runtime
        decision = evaluate_budget_window(state, self.policy)

        if decision["decision"] == "allow":
            return None

        if decision["decision"] == "block":
            return {
                "jump_to": "end",
                "budget_window_decision": decision,
            }

        return {
            "budget_window_decision": decision,
        }
