# Evaluation plan: does the protocol help?

Status: proposed experimental design. No model-performance evaluation has been run for this draft.

## Main research hypothesis

At matched research budgets, explicit representation-changing operators plus failure-pathway-aware validation produce more useful, distinct hypotheses and better next experiments than strong generic prompting, independent sampling, or an unstructured critic loop.

The claim is not that the protocol raises a model's universal creativity or solves every open problem.

## Comparisons

Compare the same base model and task inputs with: a strong direct research prompt; budget-matched independent sampling and selection; a self-critique or role-diverse review loop; this skill alone; and, once implemented, this skill plus deterministic evidence and portfolio tooling.

Record generation tokens, reviewer tokens, model-call overhead, retrieval access, experiment calls, wall-clock time, and monetary cost separately. Match meaningful resource limits rather than allowing the proposed method hidden extra work. Keep data access and final evaluators comparable across arms.

Use repeated runs and paired tasks. Specify the analysis plan and practical acceptance threshold before looking at final comparisons. Base the number of tasks and repetitions on pilot variability and a power or precision analysis; a small pilot is not a publishable universal claim.

## Task families

**Controlled diagnosis:** software or simulator failures with concealed causes and executable intervention tests. Include multiple simultaneous causes, misleading metrics, and insufficient-evidence cases.

**Mathematical and algorithmic exploration:** freshly generated hidden-rule tasks, symbolic relations, small-instance conjectures, and optimization problems with independent validators. Keep the target answers unavailable to generators and judges that should be blind.

**Open research cases:** genuine audio, ML, engineering, and puzzle investigations with pre-registered milestones. Treat these as case studies unless there is enough replication and a valid comparative design. An unresolved grand challenge alone is not a sensitive benchmark for incremental research quality.

Avoid contamination from previously disclosed solutions, fixed public benchmark memorization, and tuning the operator library on the final evaluation cases.

## Outcomes

Primary outcome: verified useful progress within a fixed budget. Define useful progress per task: correct cause identification, recovery of a concealed rule, a valid counterexample or lemma, externally validated performance gain, or experimentally supported mechanism.

Secondary outcomes: mechanism-distinct viable hypotheses; distinguishing-test quality; time or cost to an informative observation; redundant attempts; false promotion of unsupported claims; premature pruning of a true or useful candidate; and recovery after misleading feedback.

Blind domain reviewers may score novelty, feasibility, and clarity for open-ended ideas. Keep those scores separate from downstream experimental success. Do not use the generating model as the sole final judge.

For diversity, compare mechanisms, interventions, and predictions over a shared development probe set. Text embeddings can assist screening but do not establish causal or functional diversity. Concealed final evaluations must not become the probe set used to select hypotheses.

## Ablations and disconfirmation

Remove representation-changing operators, then independence audits, then failure memory, then diversity-aware selection. Test each component's contribution. Compare the full framework against spending the same resources on more ordinary samples or better evidence retrieval.

The framework has not earned an efficacy claim if it only increases novelty ratings, paperwork, or output length. It should not ship a strong claim if it fails to beat the strongest cost-matched baseline, or if modest gains depend on unacceptable false conclusions or latency.

Keep a regression suite for the skill itself: simple tasks should not trigger expensive research ceremonies; tool-unavailable tasks should not fabricate execution; and counterexamples should not be voted away.

## Learning the policy later

Only after static operators and outcome logging work should the project learn which operator to use next. Treat operator selection as a budgeted decision problem with delayed, noisy credit. Evaluate learned policies on held-out task families. Avoid optimizing against the same model judge used to generate the candidates.
