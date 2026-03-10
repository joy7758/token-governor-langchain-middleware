# Demo

## Scenario

This demo shows a small budget check before model execution for a LangChain agent runtime. The goal is to make budget-window decisions visible before the model call happens.

## Policy

The example policy defines a maximum estimated cost and a review threshold.

- [budget-window.policy.json](../examples/policies/budget-window.policy.json)

## Allowed Budget Window

The allowed example keeps enough remaining budget and stays under the maximum estimated cost.

- [budget-ok.state.json](../examples/states/budget-ok.state.json)
- [budget-ok.decision.json](../examples/results/budget-ok.decision.json)

## Blocked Budget Window

The blocked example exceeds the allowed budget window before model execution.

- [budget-blocked.state.json](../examples/states/budget-blocked.state.json)
- [budget-blocked.decision.json](../examples/results/budget-blocked.decision.json)

## Why this matters

This is not a universal token reduction claim. It is a thin example of budget-aware control before model execution, and it is designed to be composable with audit and trust-gate tooling.
