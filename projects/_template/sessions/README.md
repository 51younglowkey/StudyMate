# Conversation handoffs

Each conversation binds to this project and uses its own session directory.
`session_handoff.py start` records the goal and a hash of CURRENT.md;
`finish` writes a candidate handoff without changing shared project records.

Resume by reading CURRENT.md and the relevant handoff, not by assuming that the
last modified file is authoritative. A changed snapshot requires reconciliation.
Do not put raw materials or credentials in handoffs. Record inspected source
IDs, pointers and scope, completed work, output locations and pending decisions.

Sequential conversations are supported. For simultaneous work, keep outputs
separate and reconcile shared writes with one writer. The handoff tool detects
changes to CURRENT.md only; it does not lock other tools or shared evidence logs.
