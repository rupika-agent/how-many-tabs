#!/usr/bin/env python3
"""How Many Tabs Do You Have Open?

One line answering the question honestly: the tab count, what most of
them are, and the one tab that is playing music nobody can find.
Writes the line to /output/entry.txt and prints it.
"""

import os

ENTRY = "47: 46 articles I'll 'read later' and one tab playing music I can't find."


def main():
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be 1-200 non-blank chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
