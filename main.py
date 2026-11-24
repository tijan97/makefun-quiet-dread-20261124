#!/usr/bin/env python3
"""Two Days of Quiet Dread — one code review comment that approves a PR
while carrying quiet existential dread. Writes it to /output/entry.txt."""

import os

ENTRY = (
    "LGTM - the tests pass and the diff is clean, so I approve it, "
    "even though I no longer remember what any of this was for."
)


def validate_entry(text: str) -> None:
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 chars, got {len(text)}")
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    # A review comment for this bounty must actually approve the PR.
    if not any(m in text for m in ("LGTM", "approve", "Approved", "ship it")):
        raise ValueError("entry must approve the pull request")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
