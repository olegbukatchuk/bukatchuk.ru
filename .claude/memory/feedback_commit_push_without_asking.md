---
name: feedback-commit-push-without-asking
description: In bukatchuk.ru, after finishing a requested change, commit and push under the owner's name without asking
metadata:
  type: feedback
---

In the bukatchuk.ru repo, once a change the user asked for is done and verified (Jekyll build passes), commit and push it right away without waiting for "коммит, пуш". Said by the user on 2026-10-05: "если я сказал что-то сделать, то коммит, пуш от моего имени можно делать без спроса".

**Why:** The user was tired of typing "коммит, пуш" after every change; pushing to `main` is how the site is published.

**How to apply:** Commit as Oleg Bukatchuk <oleg@bukatchuk.com>, no Co-Authored-By and no Claude mentions (see [[feedback-commits-no-claude-attribution]]); plain `git push`, never `--force` unless explicitly asked. Still stop and ask first when the request is ambiguous and I had to make a judgement call the user may not want live, and for destructive or history-rewriting actions. After pushing, wait for the deploy and check the live page.
