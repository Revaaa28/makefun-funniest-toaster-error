"""The Funniest Toaster Error Message.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner when it quits.

The line: a deadpan resignation. Error code up front so it reads like a
real appliance message; the joke lands in one read.
"""

import os

ENTRY = "E05: This is my two weeks' notice. The crumbs were in the contract."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
