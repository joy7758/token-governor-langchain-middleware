# Adapter Inventory

## Repo role

Minimal middleware adapter for applying Token Governor decisions inside LangChain or LangGraph flows.

## Current retained surfaces

- package code under `src/token_governor_langchain_middleware/`
- examples under `examples/`
- tests under `tests/`
- docs under `docs/`

## Canonical overlap

- canonical governance runtime lives in `token-governor/governor/`
- canonical LangChain adapter surface exists in `token-governor/adapters/langchain_middleware.py`

## Boundary decision

Keep this repo as a thin adapter example, with canonical runtime logic anchored in `token-governor`.
