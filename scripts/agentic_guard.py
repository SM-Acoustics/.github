#!/usr/bin/env python3
"""Review newly added code for high-confidence unfinished work and disabled tests.

This is a bounded static PR gate; it does not prove functional correctness.
Python 3 stdlib only. Run: python3 scripts/agentic_guard.py --base <commit>.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys

CODE_SUFFIXES = {".rs", ".c", ".cc", ".cpp", ".h", ".hpp", ".py", ".ts", ".tsx", ".js", ".jsx"}
EXCLUDED_PARTS = {"third_party", "vendor", "node_modules", "target", "baseline", "fixtures", "generated"}
HIGH_CONFIDENCE = (
    ("unfinished runtime marker", re.compile(r"\b(?:todo|unimplemented)!\s*\(")),
    ("disabled Rust test", re.compile(r"#\s*\[\s*ignore\b")),
    ("disabled Python test", re.compile(r"(?:pytest\.mark\.(?:skip|xfail)|unittest\.skip\s*\(|\.skipTest\s*\()")),
    ("disabled JS test", re.compile(r"\b(?:describe|it|test)\.skip\s*\(")),
    ("vacuous assertion", re.compile(r"\bassert!?\s*\(\s*(?:true|True)\s*\)")),
)
REVIEW_FLAGS = (
    ("possible success stub; inspect side effects", re.compile(r"\b(?:return\s+)?Ok\s*\(\s*\(\s*\)\s*\)")),
    ("possible placeholder; review completion status", re.compile(r"\b(?:TODO|FIXME|XXX)\b")),
    ("potentially unreachable path", re.compile(r"\bif\s+(?:false|False)\s*[:{]")),
)
WORKFLOW_HAZARD = re.compile(r"\bcontinue-on-error\s*:\s*true\b", flags=re.I)

def classify(path: str, line: str) -> tuple[str, str] | None:
    p = pathlib.PurePosixPath(path)
    if any(part in EXCLUDED_PARTS for part in p.parts):
        return None
    if path.startswith(".github/workflows/"):
        if WORKFLOW_HAZARD.search(line):
            return "ERROR", "new workflow suppresses failures (continue-on-error)"
        return None
    if p.suffix.lower() not in CODE_SUFFIXES:
        return None
    # Static gate is deliberately narrow: review must still establish behavior.
    if path == "scripts/agentic_guard.py":
        return None
    for message, expression in HIGH_CONFIDENCE:
        if expression.search(line):
            return "ERROR", message
    for message, expression in REVIEW_FLAGS:
        if expression.search(line):
            return "REVIEW", message
    return None

def diff_lines(base: str):
    command = ["git", "diff", "--no-ext-diff", "--unified=0", "--no-color",
               "--diff-filter=ACMR", f"{base}...HEAD", "--"]
    proc = subprocess.run(command, capture_output=True, text=True, check=False)
    if proc.returncode:
        raise RuntimeError(f"git diff failed ({proc.returncode}): {proc.stderr.strip()}")
    path = None
    line_number = 0
    for line in proc.stdout.splitlines():
        if line.startswith("+++ b/"):
            path = line[6:]
        elif line.startswith("@@"):
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            if m:
                line_number = int(m.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            if path:
                yield path, line_number, line[1:]
            line_number += 1
        elif line.startswith(" "):
            line_number += 1

def self_test():
    examples = (
        ("src/main.rs", "todo!();", "ERROR"),
        ("tests/test_example.py", "@pytest.mark.skip", "ERROR"),
        ("src/audio.rs", "Ok(())", "REVIEW"),
        ("src/audio.rs", "let x = 10;", None),
        (".github/workflows/ci.yml", "continue-on-error: true", "ERROR"),
        ("third_party/vendor.rs", "todo!()", None),
    )
    for path, source, expectation in examples:
        got = classify(path, source)
        assert (got[0] if got else None) == expectation, (path, got, expectation)
    print("agentic_guard self-test: 6 PASS")

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="base commit/ref for pull request, e.g. event.pull_request.base.sha")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.base:
        parser.error("--base is required outside --self-test")
    errors, reviews, inspected = 0, 0, 0
    try:
        for path, lineno, line in diff_lines(args.base):
            inspected += 1
            hit = classify(path, line)
            if not hit:
                continue
            severity, explanation = hit
            print(f"{severity}: {path}:{lineno}: {explanation}")
            if severity == "ERROR":
                errors += 1
            else:
                reviews += 1
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"agentic_guard: added_lines={inspected} blocked={errors} review_flags={reviews}")
    print("Scope: new-line patterns only; human review, independent tests and hardware gates remain required.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
