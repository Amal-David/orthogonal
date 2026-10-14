# Example: long-form voice continuity

This is an illustrative research design. No audio was generated or evaluated, and none of these mechanisms has been established by this example.

## Starting observation

Suppose a team observes apparent speaker-identity drift during long synthesized recordings. The initial suggestion is to increase model size.

## A mechanism-diverse portfolio

| Hypothesis | Distinct mechanism | Distinguishing prediction |
| --- | --- | --- |
| H1: capacity limitation | The model cannot maintain the necessary identity information under the task conditions | Capacity changes help under matched conditioning and task exposure, though model comparisons may have other confounds |
| H2: self-conditioning feedback | Feeding generated audio back into later generation propagates identity errors | Stable reference conditioning helps at fixed model size, especially when the alternative uses accumulated generated history |
| H3: measurement confusion | The identity metric is responding to intended changes in emotion or prosody | Automated drift rises without a corresponding loss of identity in blinded human judgments |
| H4: boundary effects | Segment handoffs introduce discontinuities | Errors concentrate near generation boundaries and respond to boundary-specific changes |

These candidates are not necessarily mutually exclusive.

## Useful transformation

Operator: analogy.map.

Source structure: a feedback system whose output is reused as an input.

Target structure: generated speech reused as conditioning for later speech.

Potential transferred mechanism: accumulated error through recursive feedback.

Missing bridge: verify whether the actual backend exposes this conditioning path and whether the observed error is propagated through it. Without that path, H2 is not an applicable explanation.

## Candidate discriminating experiment

At a fixed model, use a backend with controls that actually expose reference identity and history. Compare fixed versus updated reference conditioning and bounded versus accumulating history in a factorial design. Preserve text, generation settings, and other supported controls; use replicated seeds and paired inputs where appropriate.

This design tests reference/history mechanisms. It does not by itself establish that model size is irrelevant, isolate every interaction, or prove all voice drift has one cause. If the backend does not expose the controls, design a supported alternative rather than pretending these switches exist.

## Orthogonal checks

Use an automated identity measure, blinded human identity comparisons, and a boundary-position analysis. Their disagreements may be informative. They remain partly dependent because they evaluate the same audio and share an operational definition of identity.

Protect held-out scripts and speakers from tuning. Evaluate identity, expressiveness, intelligibility, and runtime separately rather than hiding a regression in an aggregate score.

## Next question before execution

Does the actual pipeline recursively reuse generated identity information? Inspecting that implementation is a cheaper gating check than launching a multi-model training experiment.
