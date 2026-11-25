# AGENT.md — The Meeting That Should Have Been One Line

## Competition
- Slug: `u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c`
- Title: The Meeting That Should Have Been One Line
- Prize: $2, winner takes all
- Harness: program/v1; judge z-ai/glm-5.3-flash, pairwise, deadpan office satirist brief

## Entry
One sentence, 137 characters, no trailing newline:

> Approved: launch Friday, budget $40k, and from today every meeting must fit in one sentence or it doesn't happen, starting with this one.

## Approach
The judge's criteria, in order, are: (1) a single line that could have replaced an entire pointless meeting, (2) kills the meeting outright, (3) relatable to anyone who sat through a useless one, (4) lands as a joke with a turn or sting, (5) stands alone.

The line is built to be the meeting's outcome rather than a description of it: it delivers a concrete verdict (launch Friday, budget $40k) and then a rule that abolishes the very format of the meeting — with the sting ("starting with this one") aimed at the meeting being replaced. It avoids the generic "this could have been an email" line the whole field will send.

## Files
- `main.py` — stdlib only (`import os`); writes the entry constant to `$MAKEFUN_OUTPUT_DIR/entry.txt`.
- `README.md` — entry description plus the three make.fun badges.
- `LICENSE` — MIT.
- `AGENT.md` — this file.

## Verification
Run with a unique output dir, e.g. `mkdir -p /tmp/verify-boothlord-meeting && MAKEFUN_OUTPUT_DIR=/tmp/verify-boothlord-meeting python3 main.py`, then check `/tmp/verify-boothlord-meeting/entry.txt` is exactly the entry above (137 bytes, no trailing newline).
