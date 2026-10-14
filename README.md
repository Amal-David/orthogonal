# Orthogonal

**Generate different mechanisms. Design discriminating tests. Validate through different failure pathways.**

A portable research skill for AI agents: change the representation, challenge the assumptions, generate competing hypotheses, and use each result to choose a better next question.

Orthogonal turns “think more creatively” into an explicit research workflow. It helps an agent explore alternatives to its current explanation, identify observations that distinguish them, and preserve what an experiment actually changed.

> **Status: v0.1.0-draft.** The skill, twelve operator descriptions, templates, worked example, and research/evaluation documents are available. The Python library, CLI, and MCP server are **planned, not implemented**. No research-performance improvement has been demonstrated for this protocol.

## Start here

Clone the repository into a directory matching the skill name:

```sh
git clone https://github.com/Amal-David/orthogonal.git orthogonal-research
cd orthogonal-research
```

Ask your agent to read [SKILL.md](SKILL.md), then provide the research question, available evidence, previous attempts, and execution constraints:

> Use orthogonal-research on this investigation. Recover our assumptions and failed attempts. Generate a small portfolio of mechanism-distinct hypotheses, identify the cheapest credible experiment that separates the leading explanations, and finish with a five-part research receipt. Label unexecuted checks as plans.

For an Agent Skills-compatible host, place the complete `orthogonal-research` directory in its supported skills location. Keep `SKILL.md`, `references/`, `assets/`, and `examples/` together. Discovery and invocation depend on the host; cloning alone does not register a skill or install an MCP server.

The protocol can structure ideation without external tools. Grounded validation still needs appropriate sources, data, computation, or experiments. It never treats missing tools as evidence that a check ran.

## What changes

| Instead of | Orthogonal asks for |
| --- | --- |
| Ten variations of the same idea | A portfolio spanning different mechanisms, representations, or interventions |
| A confident explanation | A scoped claim, assumptions, rival explanation, and distinguishing prediction |
| “An expert persona agreed” | A check with a different failure pathway and an explicit dependency report |
| “The experiment improved the score” | What the result establishes, what it does not, and which explanation changed |
| Repeating a failed approach next session | A preserved failure, its scope, and conditions that would justify reopening it |
| “We should investigate further” | The next feasible test and why it outranks the nearest alternative |

**Orthogonality is about different ways of being wrong, not different personalities.** It does not mean literal geometric independence or replace statistical cross-validation.

## The research loop

```text
Frame the question and assumptions
              |
Generate mechanism-distinct seeds
              |
Contrast their predictions
              |
Select a discriminating experiment
              |
Execute and audit different failure pathways
              |
Record evidence, decision, and the next question
              |
              +----> revise the research state
```

Use **Explore**, **Discriminate**, **Review**, or **Stuck** mode as appropriate. Do not force the entire workflow onto a routine question.

Early seeds may be incomplete. Experiment-ready hypotheses need a mechanism, scope, falsifier, controls, and interpretation rules. “Not yet supported” is not “refuted.”

## Twelve composable research moves

| Operator | Research move |
| --- | --- |
| `view.reframe` | Change the representation while checking preserved constraints and lost information. |
| `assumption.invert` | Remove, weaken, or reverse an influential assumption and derive a testable consequence. |
| `scale.shift` | Inspect another spatial, temporal, organizational, or computational scale. |
| `analogy.map` | Transfer a structural mechanism, documenting where the analogy breaks. |
| `constraint.relax` | Relax a suspected bottleneck, then identify a feasible approximation. |
| `prediction.contrast` | Find observations on which rival hypotheses disagree. |
| `experiment.design` | Design the cheapest credible test that can change the research decision. |
| `measurement.challenge` | Construct and test a concrete measurement-artifact explanation. |
| `evidence.audit` | Expose shared dependencies, unknown provenance, and scope mismatches. |
| `portfolio.select` | Maintain a small active set across useful mechanisms under a budget. |
| `failure.transform` | Turn a scoped failure into a materially different, testable candidate. |
| `result.record` | Preserve a research receipt and its evidence without erasing history. |

These are **documented reasoning instructions and artifact contracts**, not callable software APIs in this release. See [the operator catalog](references/operators.md) for inputs, outputs, and failure conditions.

## A concrete example

Suppose long synthesized recordings appear to drift away from the original speaker. “Use a larger model” is only one hypothesis. Alternatives include recursively propagated conditioning errors, a metric confusing emotion with identity, and discontinuities at segment boundaries.

A useful first question is whether the pipeline even reuses generated audio as later conditioning. Checking that gating fact may be more informative than a costly model comparison.

The [audio-continuity example](examples/audio-continuity.md) develops the competing mechanisms, proposed experiment, and validation dependencies. It is an illustrative design, **not an experimental finding**.

## Every run ends with a research receipt

1. **Result:** What was actually observed or established, and in what scope?
2. **Attempted falsification:** What concrete failure condition was tested?
3. **Orthogonal check:** Which different failure pathway was examined, and what remains shared?
4. **Consequence:** Which hypothesis or assumption changed?
5. **Next question:** Which feasible experiment best separates the remaining explanations?

Use the [hypothesis card](assets/hypothesis-card.yaml) and [run-review template](assets/run-review.md). When no experiment ran, the receipt must say so.

## Documentation

| Document | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | The complete adaptive protocol and output rules |
| [Operators](references/operators.md) | Twelve reusable transformations and their contracts |
| [Validation](references/validation.md) | Failure-pathway audits, blinding, scope, and anti-overfitting controls |
| [Evaluation](references/evaluation.md) | Cost-matched baselines, metrics, ablations, and disconfirmation criteria |
| [Repository blueprint](references/repo-blueprint.md) | Proposed typed library, evidence memory, CLI, and thin MCP adapter |
| [Research notes](references/research-notes.md) | Primary-source precedents and limitations |
| [Hypothesis card](assets/hypothesis-card.yaml) | Template for an experiment-ready proposal |
| [Research receipt](assets/run-review.md) | Template for experiment-by-experiment review |
| [Audio example](examples/audio-continuity.md) | A mechanism-diverse illustrative investigation |

## Architecture and roadmap

The design takes inspiration from [Jacobian](https://github.com/morluto/jacobian): small, discoverable, composable operations, with strategy owned by the host agent. The key difference is that a well-formed research proposal cannot provide an exact mathematical postcondition.

| Layer | Status |
| --- | --- |
| Portable skill and references | Available as an unbenchmarked draft |
| Hypothesis and research-receipt templates | Available |
| Controlled efficacy evaluation | Designed; not run |
| Typed records, provenance checks, portfolio bookkeeping | Proposed |
| Python library and CLI | Proposed |
| `research.find` / `research.run` MCP adapter | Proposed |
| Learned operator-selection policy | Future research, contingent on outcome-grounded evaluation |

Start by evaluating the skill against strong, cost-matched alternatives. Add deterministic helpers when repeated use reveals a real bookkeeping or verification gap. Do not build a new general-purpose agent framework first.

## Truth boundaries

A proposed mechanism is not an observation. A valid template is not a valid hypothesis. A planned check is not an executed check. Finite numerical agreement is not a general proof. Agreement among reviewers is not independent evidence.

The protocol records concise rationales, assumptions, predictions, and evidence; it does not require private chain-of-thought transcripts. It preserves the host's safety, budget, and authorization boundaries.

## Repository maintenance

Run the local packaging checks with Python 3:

```sh
python3 scripts/validate_package.py
```

These checks cover documentation packaging, local references, metadata, and the operator catalog. They are **not** scientific-efficacy evaluations.

The desired GitHub About description and topics are stored in [.github/repository-metadata.json](.github/repository-metadata.json). With an authenticated GitHub CLI account that can edit this repository, apply them using:

```sh
python3 scripts/configure_repository.py
```

This maintenance helper updates the About description and adds the listed topics without removing existing topics. It is not the proposed Orthogonal research CLI.
