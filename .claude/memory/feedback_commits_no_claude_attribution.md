---
name: feedback-commits-no-claude-attribution
description: "User wants git commits/PRs authored as themselves, no Claude Code mentions or Co-Authored-By lines"
metadata:
  node_type: memory
  type: feedback
---

User (oleg@bukatchuk.com) asked explicitly: commits should not mention Claude Code, and all commits should be made under their own name/identity.

**Why:** Personal preference for authorship attribution on their own repos (e.g. [[bukatchuk-ru-blog]]).

**How to apply:** When committing on this user's behalf, do not add the `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` trailer, and ensure commit author matches the user's own git identity (check `git config user.name`/`user.email` in the repo, or use oleg@bukatchuk.com) rather than any Claude/Anthropic identity. This overrides the default attribution reminder for this user going forward.
