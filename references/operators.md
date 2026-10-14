# Composable research operators

These are reasoning instructions and artifact contracts, not proven transformations of arbitrary natural-language theories. The host model supplies semantic judgments. Deterministic helpers can validate records and compare declared dependencies; they cannot certify scientific truth.

Select operators in response to the investigation's bottleneck. Do not run every operator mechanically.

## view.reframe

Input: question, current representation, constraints, and evidence.

Move: describe the same target using a different useful representation: sequence versus graph, objects versus relations, static state versus dynamics, local events versus global invariants, or optimization versus identification.

Output: the new representation; a mapping to the original objects; preserved constraints; information lost; a newly accessible question; and a probe of the mapping.

Failure condition: the reframing changes the problem or silently discards a binding constraint. Do not claim equivalence without checking it.

## assumption.invert

Input: one influential assumption and the claims that depend on it.

Move: remove, weaken, reverse, or condition the assumption. Ask what observations would follow and whether the remaining model is coherent.

Output: a scoped counter-assumption, a new mechanism or consequence, a distinguishing prediction, and the evidence needed to admit it.

Failure condition: negation alone produces nonsense or contradicts established facts. A useful inversion identifies a plausible alternative, not contrarian wording.

## scale.shift

Input: proposed mechanism, relevant units, and scope.

Move: inspect the mechanism at a different spatial, temporal, organizational, or computational scale. Separate local efficiency from global interactions and transient behavior from long-run behavior.

Output: a scale mapping, a proposed interaction or emergent effect, and a test distinguishing the two scales.

Failure condition: importing conclusions across scales without a connecting mechanism.

## analogy.map

Input: target mechanism and a structurally related source domain.

Move: map objects, relationships, constraints, and interventions from the source domain onto the target. Transfer a useful mechanism rather than vocabulary.

Output: correspondence table, preserved structure, broken correspondence, missing bridge, predicted target behavior, and a minimal test of transfer.

Failure condition: the analogy has only superficial resemblance or ignores a target constraint. Treat the transferred claim as a hypothesis until checked.

## constraint.relax

Input: objective and a binding constraint or suspected bottleneck.

Move: temporarily supply an oracle or remove one constraint to estimate where attainable improvement could come from. Then reintroduce the constraint.

Output: the relaxed problem, remaining bottleneck, scoped ceiling or bound if established, and a feasible approximation to the hypothetical oracle.

Failure condition: the oracle solution is presented as deployable, or a heuristic upper estimate is represented as a proven bound.

## prediction.contrast

Input: at least two rival hypotheses and feasible interventions or observations.

Move: seek conditions under which their predictions differ. Include a null/artifact explanation and acknowledge mechanisms outside the candidate set.

Output: an experiment-by-hypothesis prediction matrix, currently indistinguishable pairs, and a ranked set of discriminating observations with a cost rationale.

Failure condition: the experiment would improve the system under both hypotheses but is incorrectly claimed to identify the cause.

## experiment.design

Input: selected uncertainty, rival predictions, tools, budget, and evidence.

Move: construct the cheapest feasible test that can meaningfully change the research decision.

Output: experiment contract, controls, metrics, sampling logic, stop criteria, interpretation of positive/negative/inconclusive results, and required authorization.

Failure condition: multiple changes confound the target effect; a surrogate metric does not measure the claim; or a plan is recorded as an executed test.

## measurement.challenge

Input: reported observation and the measurement process that produced it.

Move: ask whether the result is an artifact of data collection, preprocessing, selection, a proxy metric, leakage, or evaluation.

Output: explicit artifact hypothesis, alternative measurement route, negative or positive control, and predictions separating artifact from target phenomenon.

Failure condition: skepticism dismisses inconvenient evidence without constructing a concrete alternative account.

## evidence.audit

Input: evidence records, provenance, claim dependencies, and check reports.

Move: compare their dependency paths and claimed scopes.

Output: overlaps in source, dataset, implementation, assumptions, model exposure, and evaluator; unknown dependencies; scope mismatches; and a suggested additional check.

Deterministic portion: exact overlap of declared IDs, hashes, and dependencies.

Model-assisted portion: inferred semantic overlap and whether a check addresses a different failure mode. Label these as judgments, not certifications of independence.

## portfolio.select

Input: candidate hypotheses, mechanism groups, predictions, budget, and task objective.

Move: select a small active set that balances plausible value, information potential, cost, and distinct mechanism coverage.

Output: active and parked candidates, explicit selection rationale, uncovered axes, and reasons to reopen parked candidates.

A later implementation may use greedy coverage or quality-diversity search over declared descriptors. Any distances and weights are heuristics to validate empirically, not measurements of universal creativity.

## failure.transform

Input: a failed or inconclusive attempt with provenance and scope.

Move: distinguish a broken implementation, false mechanism, wrong regime, poor measurement, and genuinely informative negative result. Ask which changed assumption creates a new testable candidate.

Output: scoped failure explanation, surviving subclaims, a modified or newly framed hypothesis, and a test that would distinguish repair from repetition.

Failure condition: relabeling the same failed idea without identifying what has materially changed.

## result.record

Input: experiment artifacts, check reports, and a scoped decision.

Move: preserve a replayable research receipt and update dependencies without deleting prior outcomes.

Output: versioned record connecting question, operator, hypothesis, experiment, evidence, review, and next decision.

Deterministic portion: schema checks, reference integrity, versioning, and persistence. An append-only local log is an audit aid, not by itself a tamper-proof or scientifically valid record.
