<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# 代币调控器 langchain 中间件

[代币调速器](https://github.com/joy7758/token-governor) 的薄适配器和集成表面。

## 角色

该仓库展示了一个最小的 LangChain 或 LangGraph 中间件模式，该模式使用来自 Token Governor 生态系统的规范治理逻辑。它的存在是为了打包集成胶水和可运行的示例，而不是重新定义治理层。

## 规范主页

规范的治理实现位于 `token-governor`，特别是：

- `token-governor/adapters/langchain_middleware.py`
- `token-governor/governor/`
- `token-governor/docs/boundary.md`

## 不是这个仓库

- 不是规范的治理运行时实现
- 不是架构总仓
- 不是基准套件
- 不是审计或执行完整性层

## 最少使用量

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

对于规范运行时、策略语义和 CLI 界面，请从 `token-governor` 开始。

## 地位

- 薄型适配器
- 规范主页是 `token-governor`
- 保留为最小的 LangChain 集成示例

## 笔记

- 该仓库有意仅保留适配器胶水、示例和测试。
- 核心治理逻辑应首先在 `token-governor` 中演化。
