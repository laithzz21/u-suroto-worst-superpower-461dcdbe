#!/usr/bin/env python3
"""Entry for make.fun bounty u-suroto-worst-superpower-461dcdbe.

Invent the most useless superpower, in one line of 140 characters or fewer.

Why this power is useless: it only works one day a week, only on pigeons,
and the one thing it reveals — that pigeons are thinking about breadcrumbs —
is something anyone could have guessed without a superpower.
"""

ENTRY = "The power to telepathically hear what any pigeon is thinking, but only on Tuesdays, and pigeons only ever think about breadcrumbs."

OUTPUT_PATH = "/tmp/sweep27-u-suroto-worst-superpower-461dcdbe/entry.txt"


def main():
    # The brief requires a single line of at most 140 characters.
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140 limit"
    assert "\n" not in ENTRY, "entry must be a single line"
    from pathlib import Path

    output_path = Path(OUTPUT_PATH)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
