# Orthogonal validation means different failure pathways

This protocol uses orthogonal in an operational, not literal geometric, sense. It does not replace statistical cross-validation, randomization, formal proof, or domain-specific measurement standards.

Ask: how could both checks be wrong together?

## Record a dependency profile

For each check, record the claim and scope, evidence source, dataset and collection process, implementation and shared libraries, derivation or assumptions, evaluator, model or human author, exposure to other answers, result, and unresolved dependencies.

Report independent properties separately. A fresh dataset can test generalization but not independently reproduce an implementation. A second implementation on the same data can expose coding errors but not dataset bias. A different model can diversify a review but does not establish a separate evidence source.

Unknown provenance is unknown independence, not zero overlap.

## Stronger and weaker examples

| Pair of checks | Useful distinction | Remaining shared risk |
| --- | --- | --- |
| Two prompts to the same model | Different elicitation may find missed details | Shared knowledge, assumptions, context, and evaluation bias |
| Different models reading the same summary | Some author diversity | Shared summary errors and incomplete evidence |
| Separately written exhaustive enumerator versus optimized dynamic program | Different implementation strategy on bounded instances | Shared problem definition or admissibility errors |
| Formal derivation versus independently constructed numeric example | Symbolic versus computational failure modes | Finite examples cannot establish a universal claim |
| Automated audio similarity versus blinded listening | Different measurement processes | Shared audio set and ambiguity in the identity construct |
| Controlled intervention versus observational comparison | Tests a causal prediction rather than association alone | Experimental implementation, confounding, and measurement assumptions |

None of these pairs warrants an unconditional independence claim.

## Blind checks without hiding evidence

Give the reviewer the claim, original specification, raw evidence, and required assumptions. Initially withhold the advocate's persuasive narrative and preferred answer where feasible. Ask for an independently derived prediction or test. Then expose the competing report and resolve factual disagreements.

Record whether contexts were actually isolated. Asking a single conversation to pretend it has not seen a conclusion is not real blinding.

## Promotion rules

A seed can remain speculative. A promoted empirical claim needs observations, a defensible comparison, uncertainty appropriate to the measurement, and a scope no broader than the experiment supports.

A mathematical claim needs a valid argument for its stated quantifiers and domain. Computation can support or refute scoped claims, but finite agreement cannot replace a general proof.

One verified admissible counterexample refutes an applicable universal statement, regardless of reviewer votes. In empirical science, a surprising observation requires accounting for noise, measurement error, and the hypothesis's actual probabilistic content.

Mark a claim INCONCLUSIVE when experiments cannot discriminate its rivals. Mark an experiment invalid when its execution or measurement is compromised; do not automatically mark the scientific hypothesis false.

## Anti-overfitting controls

Separate exploration, development, confirmation, and sealed audit inputs where feasible. Record failed attempts and adaptive choices. Define final evaluation rules before seeing final results. Use an appropriate multiplicity or sequential-testing strategy for repeated statistical claims. Do not repeatedly inspect a held-out set and continue to call it untouched.

At review time, ask whether the new result changes the original research decision. A better internal score without transfer, causal clarity, or an externally meaningful outcome may be only a proxy improvement.
