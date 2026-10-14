#!/usr/bin/env python3
"""Dependency-free packaging checks, not scientific efficacy evaluation."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "SKILL.md", "assets/hypothesis-card.yaml", "assets/run-review.md",
    "examples/audio-continuity.md", "references/operators.md", "references/validation.md",
    "references/evaluation.md", "references/repo-blueprint.md", "references/research-notes.md",
    ".github/repository-metadata.json", "scripts/configure_repository.py",
)
OPERATORS = {
    "view.reframe", "assumption.invert", "scale.shift", "analogy.map", "constraint.relax",
    "prediction.contrast", "experiment.design", "measurement.challenge", "evidence.audit",
    "portfolio.select", "failure.transform", "result.record",
}


def main() -> int:
    errors = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty required file: {relative}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    if not match:
        errors.append("SKILL.md is missing frontmatter delimiters.")
    else:
        if not re.search(r"^name: orthogonal-research$", match.group(1), re.M):
            errors.append("Unexpected skill name.")
        if not re.search(r"^description: .+", match.group(1), re.M):
            errors.append("Missing skill description.")
    for ref in re.findall(r"`((?:references|assets|examples)/[^`]+)`", skill):
        if not (ROOT / ref).is_file():
            errors.append(f"Missing skill reference: {ref}")

    # Check local inline Markdown file targets; do not fetch remote links or validate anchors.
    checked_links = 0
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                errors.append(f"Link escapes package in {path.relative_to(ROOT)}: {target}")
            elif not resolved.exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")
            checked_links += 1
    headings = re.findall(r"^## ([a-z]+\.[a-z]+)$", (ROOT / "references/operators.md").read_text(encoding="utf-8"), re.M)
    if set(headings) != OPERATORS or len(headings) != len(OPERATORS):
        errors.append("Operator catalog must contain each of the twelve expected operators exactly once.")
    try:
        metadata = json.loads((ROOT / ".github/repository-metadata.json").read_text(encoding="utf-8"))
        if metadata.get("repository") != "Amal-David/orthogonal":
            errors.append("Unexpected metadata repository.")
        description = metadata.get("description")
        if not isinstance(description, str) or not description.strip() or len(description) > 350:
            errors.append("Invalid About description.")
        topics = metadata.get("topics")
        if not isinstance(topics, list) or not 1 <= len(topics) <= 20:
            errors.append("Expected 1-20 topics.")
        elif any(not isinstance(t, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,49}", t) for t in topics):
            errors.append("Invalid topic format.")
        elif len(topics) != len(set(topics)):
            errors.append("Duplicate topics.")
    except (OSError, ValueError, TypeError) as error:
        errors.append(f"Metadata validation failed: {error}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: required files, skill metadata/references, {checked_links} local Markdown links, 12 operators, and repository metadata.")
    print("Not checked: remote URLs, full YAML/JSON schemas, scientific validity, or research-performance improvement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
