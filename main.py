"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (1-400 characters, UTF-8).

The rant: Dave replied "per my last email" to an email he never
sent, so the narrator searches everywhere for it, finds nothing,
and turns Dave's own weapon back on him.
"""

import os

# The selected rant (331 chars, one line) — picked from 8 candidates by
# simulated pairwise judging against the brief; see CANDIDATES.md.
ENTRY_TEXT = (
    'Dave replied "per my last email" to an email he never sent. '
    "I searched. I searched again. I searched my spam, my trash, "
    "my soul. There is no last email. There is only Dave, "
    "weaponising a phantom email, and me, apologising to a man who "
    "invented a past in which he was right. "
    'So I replied "per my last email" to Dave. Let him search.'
)


def _check_entry(text):
    """Pre-write gate: the entry must be a single non-empty UTF-8 line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) != 331:
        raise ValueError("entry must be 331 characters, got %d" % len(text))
    text.encode("utf-8")


def main():
    _check_entry(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print("Wrote %d characters to /output/entry.txt" % len(ENTRY_TEXT))


if __name__ == "__main__":
    main()
