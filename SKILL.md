---
name: orthogonal-research
description: Generate mechanism-diverse research hypotheses, challenge assumptions across representations, design discriminating experiments, and review results through different failure pathways. Use for research ideation, stalled investigations, scientific or engineering hypothesis generation, and experiment-by-experiment adversarial review. Not for routine factual questions or as a substitute for domain verification.
metadata:
  version: "0.1.0-draft"
  status: "Unbenchmarked protocol; not an implemented MCP server"
---

# Orthogonal Research

Help the investigator discover a materially different explanation or intervention, then identify the cheapest credible observation that separates it from its rivals.

Do not equate longer answers, more agents, more ideas, confidence, or more tool calls with better research. Optimize for useful hypotheses and informative tests under an explicit budget.

## Scope and truth boundaries

This skill structures observable research artifacts; it does not require private chain-of-thought transcripts, change model weights, or certify creativity. Produce concise rationales, assumptions, predictions, evidence references, and decisions.

A proposed mechanism is not an observation. A valid schema is not a valid hypothesis. A planned check is not an executed check. A finite search is not a general proof. Distinct models, implementations, or papers do not by themselves establish independent evidence.

Use the host's existing retrieval, computation, experiment, and verification tools. When tools or data are unavailable, return explicit test plans and unresolved dependencies rather than fabricated results. Do not publish, install software, spend money, or trigger external experiments without the necessary user authorization. Preserve the host's safety and permissions boundaries.

## Select a mode

**Explore:** The investigator needs new directions. Emphasize alternative representations, mechanisms, analogies, and predictions. Keep promising but incomplete seeds.

**Discriminate:** Several explanations fit current evidence. Emphasize experiments on which their predictions differ.

**Review:** An experiment or proof attempt has finished. Audit validity and scope, update competing explanations, and select the next question.

**Stuck:** Recent rounds repeat mechanisms or produce no informative observations. Diagnose whether the bottleneck is framing, evidence, tools, validation, resources, or the search policy. Change that bottleneck rather than simply generating more text.

Modes can be combined. Do not force every operation on every problem.

## 1. Establish the research state

State the question and what would count as useful progress. Separate observed facts, user-provided premises, working assumptions, unknowns, and constraints.

Recover relevant earlier hypotheses and negative results when available. Preserve their scope and provenance. Do not silently promote a previous assistant suggestion into an established fact.

Identify the current representation, leading explanation, important alternative, and strongest unexplained observation. Record available tools, validation access, experiment budget, and stopping conditions. When the user has not specified a budget, bound the current ideation pass; do not interpret missing limits as authorization for unbounded execution.

## 2. Generate seeds by changing the problem, not its wording

Choose a few relevant operators from `references/operators.md`. Start with a small active set, usually 6–10 seeds spanning several genuinely different mechanisms. These counts are adjustable workflow defaults, not scientifically optimized constants. A larger archive may remain inactive.

Explore both nearby improvements and at least one plausible change of representation, causal model, scale, or constraint. Ask what would have to be true for an unconventional candidate to work. Make its missing bridge explicit.

At this stage a seed needs only: its central idea, what differs from current candidates, a tentative mechanism or acknowledged gap, and an observable implication. Do not demand a complete proof or implementation before retaining an exploratory seed.

Apply hard constraints immediately. Distinguish an actual contradiction from an untested premise. Missing evidence should create a test or a parked candidate, not an invented certainty.

## 3. Contrast mechanisms and predictions

Group candidates by their assumptions, intervention, causal mechanism, and predicted observations. Use wording or embedding similarity only as a preliminary duplicate warning.

Ask: under what feasible condition would candidate A and candidate B predict different outcomes? If no difference is known, record that they are currently observationally indistinguishable. Do not automatically declare them identical; the available probes may be insufficient.

Keep a small portfolio across useful mechanisms instead of selecting many paraphrases of the most persuasive proposal. Maintain an exploratory slot when the task and budget justify one. Do not manufacture diversity by retaining candidates that violate known constraints.

## 4. Turn selected seeds into hypothesis contracts

For the few candidates selected for testing, use `assets/hypothesis-card.yaml` as a template. Record:

- The claim, scope, mechanism, assumptions, nearest rival, and known prior work.
- A distinguishing prediction and what outcome would weaken the claim.
- The cheapest feasible discriminating experiment, controls, metrics, and interpretation limits.
- The validation paths, shared dependencies, and any unresolved independence concerns.

Separate novelty to this project from novelty relative to the searched literature. Record retrieval scope, dates, and unknown coverage. Do not claim global novelty from a limited search.

## 5. Choose an informative next experiment

Prefer a test that separates important rival explanations, resolves a gating assumption, or checks whether the proposed mechanism exists at all. A cheap negative result can be more valuable than a costly ambiguous improvement.

Record predictions and interpretation rules before seeing results. Include inconclusive outcomes and an alternative explanation outside the current candidate set. Specify scope, controls, units of analysis, repetitions or sampling logic, and acceptance or falsification criteria appropriate to the domain.

Do not invent numeric probabilities, effect sizes, or information-gain values. Use calibrated estimates where available and transparent qualitative comparisons otherwise.

Keep tuning data distinct from confirmation data. When repeatedly testing candidates, log every attempt and protect held-out evaluation from adaptive reuse. Change one factor for a causal isolation test, or use a justified factorial design when interactions are the actual question.

## 6. Execute and perform orthogonal review

Use authorized tools to execute only the selected test. Preserve configuration, version, inputs, outputs, artifact references, and failures. Failed execution is a result about the experiment, not necessarily a refutation of the hypothesis.

Use `references/validation.md` to construct checks with different likely failure pathways. State exactly what each path can and cannot verify. A second reviewer using the same source and derivation is not independent reproduction.

Where possible, let a checker reconstruct a result from the specification and raw evidence before reading the advocate's rationale. Give it all information necessary to assess validity; blinding must not hide relevant evidence.

A concrete, verified counterexample overrides a vote for the claim within the counterexample's applicable scope. A rhetorical objection does not. Treat noisy empirical results statistically rather than as deductive counterexamples.

## 7. Learn without erasing history

Append the outcome and a scoped decision: RETAIN_SEED, TEST_NEXT, REPAIR, REFRAME, SUPPORTED_IN_SCOPE, REFUTED_IN_SCOPE, INCONCLUSIVE, or PARKED.

Link the decision to evidence, assumptions, operator used, and rival hypotheses. Retain failures and negative evidence. Reopen an archived family only when new evidence, a changed assumption, a new representation, or a newly available tool materially changes its prospects.

Record the reusable transformation that helped or failed, including applicability and failure conditions. Do not convert one successful example into a universal thinking rule.

## 8. End every run with a research receipt

Use `assets/run-review.md`. Always provide these five items in concise prose:

1. Result: what was actually observed or established, and in what scope.
2. Strongest attempted falsification: what was tested, not merely suggested.
3. Orthogonal check: its different failure pathway, outcome, and shared dependencies.
4. Consequence: which hypotheses or assumptions changed, and what remains unresolved.
5. Next question: the most discriminating feasible experiment and why it outranks the nearest alternative.

When no experiment ran, say so and distinguish a proposed falsifier from an attempted one. Do not end with a generic request to continue. Select the next useful question while respecting the current execution budget.

## Evidence and uncertainty rules

Use explicit statuses such as PROPOSED, DERIVED, COMPUTED, OBSERVED, REPRODUCED, and FORMALLY_VERIFIED only when justified. Confidence should reflect evidence quality and dependence, not the number of agreeing agents.

Check ceilings and bounds in their actual scope. A limitation of one algorithm, representation, or backend is not proof that the entire research question is exhausted.

Never claim a universal theorem from numerical agreement, a causal effect from an uncontrolled comparison, or independence from a provenance report with unknown dependencies.

## Additional references

`references/operators.md`: composable question operators and output contracts.

`references/validation.md`: failure-pathway audit and independence examples.

`references/evaluation.md`: how to test whether this skill improves research outcomes.

`references/repo-blueprint.md`: proposed library and MCP architecture; not implemented.

`references/research-notes.md`: primary-source precedents and limitations.

`examples/audio-continuity.md`: an illustrative hypothesis portfolio, not an experimental finding.
