import os

# One sentence that IS the meeting's outcome: the verdict (launch Friday,
# budget approved) plus a rule that kills future pointless meetings,
# with the sting landing on this very meeting.
ENTRY = "Approved: launch Friday, budget $40k, and from today every meeting must fit in one sentence or it doesn't happen, starting with this one."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# No trailing newline: the gate counts characters, and the entry is one line.
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
