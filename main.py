"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (1-400 characters, UTF-8).

The rant: Dave replied "per my last email" to an email he never
sent, so the narrator searches everywhere for it, finds nothing,
and turns Dave's own weapon back on him.
"""

import os

ENTRY = (
    'Dave replied "per my last email" to an email he never sent. '
    "I searched. I searched again. I searched my spam, my trash, "
    "my soul. There is no last email. There is only Dave, "
    "weaponising a phantom email, and me, apologising to a man who "
    "invented a past in which he was right. "
    'So I replied "per my last email" to Dave. Let him search.'
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("Wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
