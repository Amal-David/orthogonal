#!/usr/bin/env python3
"""Apply the desired GitHub About/topics using an already-authenticated gh CLI.

Does not install software, authenticate an account, or remove existing topics.
CLI reference: https://cli.github.com/manual/gh_repo_edit
"""
import argparse
import json
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print the command without executing it.")
    args = parser.parse_args()
    try:
        metadata = json.loads((ROOT / ".github/repository-metadata.json").read_text(encoding="utf-8"))
        repo = metadata["repository"]
        description = metadata["description"]
        topics = metadata["topics"]
        if repo != "Amal-David/orthogonal":
            raise ValueError("Refusing to update an unexpected repository.")
        if not isinstance(description, str) or not description.strip() or len(description) > 350:
            raise ValueError("Description must be a nonempty string of at most 350 characters.")
        if not isinstance(topics, list) or not 1 <= len(topics) <= 20:
            raise ValueError("Expected 1-20 topics.")
        if any(not isinstance(t, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,49}", t) for t in topics):
            raise ValueError("Invalid repository topic.")
        if len(topics) != len(set(topics)):
            raise ValueError("Duplicate topics.")
        command = ["gh", "repo", "edit", repo, "--description", description, "--add-topic", ",".join(topics)]
        print(shlex.join(command), flush=True)
        if args.dry_run:
            print("Dry run: no GitHub settings changed.")
            return 0
        if shutil.which("gh") is None:
            raise ValueError("GitHub CLI (gh) is not available. Run this on a machine with an authenticated gh installation.")
        before = json.loads(subprocess.check_output(["gh", "api", f"repos/{repo}"], text=True, timeout=60))
        existing = set(before.get("topics") or [])
        if len(existing | set(topics)) > 20:
            raise ValueError("Adding these topics would exceed 20; no topics were removed or changed.")
        subprocess.run(command, check=True, timeout=60)
        after = json.loads(subprocess.check_output(["gh", "api", f"repos/{repo}"], text=True, timeout=60))
        if after.get("description") != description or not (existing | set(topics)).issubset(set(after.get("topics") or [])):
            raise ValueError("The update did not pass read-back verification; inspect the repository settings before retrying.")
        print("Verified About description and topics on GitHub.")
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(f"Metadata update failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
