## Problem

- `docs/operations/merge-gate.md` documents a four-layer merge-protection stack and the incident that motivated it: "A single rapid burst of auto-merges flipped `main` red" (`merge-gate.md:18`).

- Those four layers (autosync, main-red guard, merge queue, nightly drift sweep) prevent that specific failure mode at the workflow level, but none of them emit a record. After a merge lands, there is no way to prove which bars it satisfied, at what chain head, under whose authority.

- The re