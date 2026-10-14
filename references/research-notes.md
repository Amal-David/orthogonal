# Research grounding

Prepared 14 October 2026. This protocol is an original synthesis and implementation proposal, not a claim that the underlying research ideas are new. No efficacy experiment has been performed for this package.

## Jacobian

The repository exposes discoverable, typed mathematical operations through math.find and math.run, with a CLI and Python API. Its architecture separates stable mathematical postconditions from the caller's strategy. Borrow the composable-contract boundary, not a promise that open-ended hypotheses can receive exact mathematical guarantees.

Primary sources:
- https://github.com/morluto/jacobian
- https://github.com/morluto/jacobian/blob/main/docs/explanation/executable-mathematical-vocabulary.md

## Cognitive tools

Ebouky, Bartezzaghi, and Rigotti, Eliciting Reasoning in Language Models with Cognitive Tools, arXiv:2506.12115v2, 20 November 2025. The study implements modular reasoning operations using model calls and evaluates mathematical reasoning. It is a close precedent for packaging reasoning moves as tools, but does not establish that this proposed research-ideation protocol works.

Primary source: https://arxiv.org/html/2506.12115v2

## SciMON

Wang et al., SciMON: Scientific Inspiration Machines Optimized for Novelty, ACL 2024. The work retrieves scientific inspirations and iteratively compares proposals with prior work. This motivates explicit structural analogy and a nearest-prior-work record. A literature search still cannot certify universal novelty.

Primary source: https://aclanthology.org/2024.acl-long.18/

## HypoGeniC and HypoRefine

The authors' repository and project describe data-driven hypothesis generation and iterative refinement, including combining literature with empirical examples. Borrow outcome-grounded refinement rather than equating a persuasive explanation with success.

Primary sources:
- https://github.com/ChicagoHAI/hypothesis-generation
- https://chicagohai.github.io/hypogenic-demo/

## Co-Scientist

Google DeepMind's 19 May 2026 account describes generation, proximity, reflection, ranking, evolution, and meta-review agents coordinated by a supervisor. This is a relevant full-system precedent; the proposed project is a smaller composable layer, not an equivalent implementation.

Primary source: https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/

## EvoDiverse

Wang et al., Towards Diverse Scientific Hypothesis Search with Large Language Models, arXiv:2606.10587v1, 9 June 2026. The work uses multiple search-temperature pools and exchange to balance quality and diversity under validation budgets. It reports computational discovery experiments; this does not establish universal real-world research performance. Its discussion notes budget tradeoffs and approximate sampling semantics.

Primary sources:
- https://arxiv.org/html/2606.10587v1
- https://github.com/zoom-wang112358/EvoDiverse

## Idea evaluation

Si, Yang, and Hashimoto, Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers, arXiv:2409.04109. Expert reviewers judged generated ideas favorably on novelty, while feasibility and generation diversity remained concerns. Judgments of a proposal are not the same outcome as completing useful research.

Primary source: https://arxiv.org/abs/2409.04109

## Self-correction is method-dependent

Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet, arXiv:2310.01798, reports difficulties without external feedback. Wu et al., Large Language Models Can Self-Correct with Key Condition Verification, EMNLP 2024, reports gains under a targeted verification method. These results motivate measuring a specific protocol instead of assuming either that critique always works or that it never can.

Primary sources:
- https://arxiv.org/abs/2310.01798
- https://aclanthology.org/2024.emnlp-main.714/

## Related interface and packaging

The Sequential Thinking reference MCP server supports step revision and branching. It is an interface precedent, not independent evidence that this proposed method improves hypothesis generation.

The Agent Skills specification defines a directory with SKILL.md, required name and description metadata, and optional references and assets. This draft follows that basic layout. Host-specific installation and triggering behavior have not been tested.

Primary sources:
- https://github.com/modelcontextprotocol/servers/blob/main/src/sequentialthinking/README.md
- https://agentskills.io/specification
