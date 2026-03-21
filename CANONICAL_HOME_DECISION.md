# Canonical Home Decision

## Decision

Canonical home: `token-governor`

## Why

- governance semantics and runtime behavior belong in the governance layer repo
- `token-governor` already exposes a LangChain adapter surface
- this standalone repo remains useful only as a minimal integration package and example wrapper

## Posture

- thin adapter, not deprecated yet
- parent repo remains the source of truth for policy and runtime behavior
