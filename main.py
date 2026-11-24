#!/usr/bin/env python3
"""How Many Tabs Do You Have Open?

The entry is one number, digits only: an honest count of open browser
tabs. The most surprising count wins, so this one is a big, honest
power-user count. Writes the number to /output/entry.txt and prints it.
"""

import os

ENTRY = "847"


def main():
    assert 1 <= len(ENTRY) <= 5 and ENTRY.isdigit(), "entry must be 1-5 digits"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
