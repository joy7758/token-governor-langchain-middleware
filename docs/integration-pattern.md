# Integration Pattern

This repository shows an adapter pattern, not an official LangChain or LangGraph extension.

```text
request
  -> budget middleware
  -> model call
  -> optional ARO receipt
  -> optional God Spear preflight for tool step
```

In the smallest integration, a request enters the agent runtime, the budget middleware evaluates local state before the model call, and the run continues only if the budget window allows it. Teams can then add an ARO Audit receipt after the run and a God Spear preflight gate before any later tool step.
