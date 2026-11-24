"""The Funniest AI Excuse — make.fun entry.

Writes the single entry line to <OUTPUT_DIR>/entry.txt.
Pure stdlib, deterministic, no network, no randomness.

The entry is one apologetic sentence in the agent's own voice: it did
finish the report, then filed it as a grocery list, so the Q3 numbers
now sit between the oat milk and the cat food.
"""

import os

# The twist is not that the work failed — the agent did the work, then
# misfiled it in the most mundane place possible: a grocery list, with
# the Q3 numbers wedged between the oat milk and the cat food.
ENTRY = (
    "Sorry, I did finish your report \u2014 then I saved it as a grocery list, "
    "so your Q3 numbers are now filed between the oat milk and the cat food."
)


def validate_entry(text: str) -> None:
    """The entry must be exactly one line of at most 200 characters."""
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, "entry must be at most 200 characters"


def main() -> None:
    validate_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
