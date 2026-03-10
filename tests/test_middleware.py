from __future__ import annotations

from token_governor_langchain_middleware.middleware import BudgetWindowMiddleware


def test_middleware_can_be_instantiated() -> None:
    middleware = BudgetWindowMiddleware(
        {
            "max_estimated_cost": 0.05,
            "review_threshold": 0.02,
        }
    )

    assert middleware is not None


def test_middleware_blocks_when_budget_window_fails() -> None:
    middleware = BudgetWindowMiddleware(
        {
            "max_estimated_cost": 0.05,
            "review_threshold": 0.02,
        }
    )

    result = middleware.before_model(
        {
            "estimated_cost": 0.08,
            "remaining_budget": 0.01,
        }
    )

    assert result is not None
    assert result["jump_to"] == "end"
    assert result["budget_window_decision"]["decision"] == "block"
