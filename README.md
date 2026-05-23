> **Maintenance notice**
>
> This repository is no longer the primary maintenance entry for the Agent Evidence / Operation Accountability Profile（智能体执行证据与操作问责配置文件）mainline. It is retained for migration review or historical reference. This change does not delete or archive the repository. See `MIGRATED_TO.md` for the current migration target and review status.

<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# token-governor-langchain-middleware

Thin adapter and integration surface for [token-governor](https://github.com/joy7758/token-governor).

## Role

This repo shows a minimal LangChain or LangGraph middleware pattern that consumes canonical governance logic from the Token Governor ecosystem. It exists to package integration glue and runnable examples, not to redefine the governance layer.

## Canonical home

The canonical governance implementation lives in `token-governor`, especially:

- `token-governor/adapters/langchain_middleware.py`
- `token-governor/governor/`
- `token-governor/docs/boundary.md`

## Not this repo

- not the canonical governance runtime implementation
- not the architecture hub
- not the benchmark suite
- not the audit or execution-integrity layer

## Minimal usage

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
pytest
```

```python
import json
from pathlib import Path

from token_governor_langchain_middleware.budget import evaluate_budget_window

policy = json.loads(Path("examples/policies/budget-window.policy.json").read_text())
state = json.loads(Path("examples/states/budget-ok.state.json").read_text())
print(evaluate_budget_window(state, policy))
```

For the canonical runtime, policy semantics, and CLI surface, start from `token-governor`.

## Status

- thin adapter
- canonical home is `token-governor`
- kept as a minimal LangChain integration example

## Notes

- This repo intentionally keeps only adapter glue, examples, and tests.
- Core governance logic should evolve in `token-governor` first.
