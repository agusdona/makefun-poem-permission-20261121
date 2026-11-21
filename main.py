"""make.fun — "The poem about permission".

Writes one short original poem about agency to /output/entry.txt.

Pure standard library, no network access, fully deterministic: running
this program any number of times produces byte-identical output.
"""

import os

# The poem, as Unicode text. Length is measured in code points (Python 3
# str length), which is what the bounty counts — not bytes.
POEM = (
    "I asked the doorman for the key.\n"
    "He gave it, warm from his chest.\n"
    "The bolt stayed shut.\n"
    "\n"
    "“A key is a shape,” he said.\n"
    "“Permission is a door held open\n"
    "by someone who could have kept it shut.”\n"
    "\n"
    "I turned it his way. It opened.\n"
    "I held it open with my foot.\n"
    "That was the asking."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    length = len(POEM)
    if not 1 <= length <= 280:
        raise ValueError(f"poem must be 1-280 Unicode code points, got {length}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()