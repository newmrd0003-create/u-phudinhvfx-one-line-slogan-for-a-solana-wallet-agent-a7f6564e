"""One-Line Slogan for a Solana Wallet Agent.

Writes the chosen slogan to /output/entry.txt (exactly one line,
UTF-8, 1-140 characters, at most 20 words) and validates it.
Deterministic: repeated runs produce byte-identical output.
"""

import os

SLOGAN = (
    "Your Solana wallet's new roommate: it pays the rent, "
    "guards the door, and never eats your snacks."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_WORDS = 20


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SLOGAN + "\n")


def validate() -> tuple[bool, list[str]]:
    """Check the entry against the competition gate.

    Returns (True, []) when the entry is valid, otherwise
    (False, [reasons]).
    """
    errors: list[str] = []
    try:
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return False, ["entry.txt not found"]
    body = text.rstrip("\n")
    if not body.strip():
        errors.append("entry is empty or only whitespace")
    if "\n" in body:
        errors.append("entry must be a single line")
    if not 1 <= len(body) <= 140:
        errors.append(f"entry length {len(body)} chars, must be 1-140")
    words = body.split()
    if len(words) > MAX_WORDS:
        errors.append(f"entry has {len(words)} words, max {MAX_WORDS}")
    return (not errors), errors


if __name__ == "__main__":
    main()
