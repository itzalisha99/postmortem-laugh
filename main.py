"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (two sentences, under 400 characters) of the
silliest time an AI coding agent misunderstood what it was asked to do.
"""

import os

ENTRY = (
    "I asked it to log every payment attempt. "
    "It put the log line after the payment call, "
    "so the only payments with no log are the ones that failed."
)


def validate(text):
    """Mirror the bounty gate and the brief: UTF-8 text, 1-400 chars,
    not only whitespace, and one or two sentences."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 400:
        raise ValueError("entry must be at most 400 characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    sentences = [s for s in text.split(".") if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise ValueError("entry must be one or two sentences")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
