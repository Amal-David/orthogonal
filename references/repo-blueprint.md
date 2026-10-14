# Orthogonal: library and MCP blueprint

Repository: https://github.com/Amal-David/orthogonal. This repository publishes the draft skill and design documents. The research library, CLI, and MCP server described below are proposed; no installable software package has been published.

Positioning: composable hypothesis generation and independent-evidence review for research agents.

## Boundaries

The host agent owns research strategy and tool choice. The skill supplies an adaptive protocol. A small library supplies typed artifacts, operator discovery, provenance checks, portfolio bookkeeping, and reproducible research receipts. Existing tools perform computation, retrieval, and experiments.

Jacobian remains a mathematical execution backend. Orthogonal must not pretend that a generated scientific proposal has Jacobian's exact mathematical postconditions.

Do not build a general agent operating system, universal automated scientist, new graph database, large persona council, or replacement for every existing research harness as the initial product.

## Three layers

### Skill

A self-contained SKILL.md with progressively loaded operator instructions, examples, and artifact templates. It can run in the host model without hidden recursive model calls. This package implements the draft protocol layer only.

### Library and CLI — proposed, not implemented

Typed records: Problem, Assumption, Hypothesis, Prediction, Experiment, Evidence, Check, Decision, and OperatorApplication. Represent multi-premise dependencies as explicit relations, not merely text links.

Deterministic helpers: schema validation, ID and artifact-reference checks, explicit provenance overlap, budget accounting, append-only records, queryable archives, and coverage over declared descriptors.

Model-assisted helpers: alternate framing, causal mechanism inference, analogy transfer, semantic duplicate judgments, experiment proposals, and qualitative prioritization. Outputs remain proposals or model assessments until independently checked.

Start with portable JSON or JSONL records and a SQLite index. This can preserve claim/evidence hypergraph semantics without requiring a graph service. Add specialized graph infrastructure only when measured query needs justify it.

### MCP adapter — proposed, not implemented

Possible interface:

```text
research.find(query or operation_id)
research.run(operation_id, typed_payload)
```

Discovery returns prerequisites, output schema, cost or scope limits, examples, and which judgments are heuristic. Execution can either return a scaffold for the host to fill, perform deterministic bookkeeping, or invoke an explicitly configured model backend. These modes must not be conflated.

Do not quietly wrap every tiny thinking operator in another model call. The host should normally generate semantic artifacts; the library validates and stores them. Optional isolated subagents may be valuable for blinded review, with explicit cost and context controls.

## Initial admission policy

Begin with a compact subset of useful operations, not a quota of hundreds. Admit a new operator only when repeated research tasks reveal a distinct missing transformation, or when an established transformation offers clear reusable value.

The reference catalog contains twelve candidate operators. An initial implementation could prioritize view.reframe, assumption.invert, prediction.contrast, experiment.design, evidence.audit, portfolio.select, failure.transform, and result.record.

Every public operator needs a stable contract, failure cases, at least two unrelated examples, and an evaluation plan. A task-specific clever prompt is not automatically a reusable operation.

## Evidence memory

Preserve the concise transformation that led to a candidate, not private internal reasoning. Link problem state, operator, hypothesis, experiment, evidence, validation paths, decision, and next question. Keep failed branches and the conditions that could reopen them.

Checks should distinguish DECLARED, INFERRED, and VERIFIED provenance fields. A shared-dependency detector can expose known overlap but cannot certify statistical independence or identify every common cause of error.

## Shipping order

1. Test the skill on representative tasks against a strong prompt baseline.
2. Implement the deterministic helpers that eliminate repeated manual mistakes.
3. Add the CLI and thin MCP adapter over the same contracts.
4. Publish controlled comparisons, task-family limitations, and failure examples.
5. Explore learned operator selection only after an outcome-grounded evaluation exists.

The published draft skill is a starting point for step 1, not completion of steps 2–5.
