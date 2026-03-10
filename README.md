# Token Governor LangChain Middleware

Budget-window middleware for LangChain agents running on LangGraph.

Part of the Agent Runtime Safety Kit.  
This repo shows a thin middleware pattern for budget-aware control before model execution.

## What this is

- A docs-first and minimal runnable adapter repo.
- A small budget-window decision core that works on local JSON-like state.
- A thin `before_model` middleware example for LangChain agents.
- A composable control layer that can sit before model execution.

## What this is not

- Not a full agent framework.
- Not a promise of universal token reduction.
- Not an official LangChain or LangGraph extension.
- Not a production-ready control plane by itself.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[test]"

python - <<'PY'
import json
from pathlib import Path
from token_governor_langchain_middleware.budget import evaluate_budget_window

policy = json.loads(Path("examples/policies/budget-window.policy.json").read_text())
state = json.loads(Path("examples/states/budget-ok.state.json").read_text())
print(evaluate_budget_window(state, policy))
PY

pytest
```

## Demo Assets

- [Demo](docs/demo.md)
- [Integration Pattern](docs/integration-pattern.md)
- [Budget Window Policy](examples/policies/budget-window.policy.json)
- [Budget OK State](examples/states/budget-ok.state.json)
- [Budget Blocked State](examples/states/budget-blocked.state.json)
- [Budget OK Decision](examples/results/budget-ok.decision.json)
- [Budget Blocked Decision](examples/results/budget-blocked.decision.json)

## Middleware Shape

- `evaluate_budget_window(state, policy)` returns a small decision object with `allow`, `review`, or `block`.
- `BudgetWindowMiddleware.before_model(...)` uses that decision before model execution.
- `allow` returns `None` so the model call can continue.
- `review` returns a small state update.
- `block` returns a small state update plus `jump_to: "end"` to stop before the model call.

This is a thin adapter example, not an official middleware extension.

## Related Projects

- [Token Governor](https://github.com/joy7758/token-governor)
- [ARO Audit](https://github.com/joy7758/aro-audit)
- [God Spear](https://github.com/joy7758/god-spear)
- [God Spear MCP Gate](https://github.com/joy7758/god-spear-mcp-gate)
