---
name: feedback-blog-no-meta-notes
description: "Blog posts for bukatchuk.ru must not contain meta notes about how Claude did the work (what was/wasn't run, environment limits, verification caveats)"
metadata:
  node_type: memory
  type: feedback
---

Do not put process/meta disclaimers into blog posts written for the user's blog (bukatchuk.ru, see [[feedback-commits-no-claude-attribution]]): no "how this was checked" boxes, "I did not run the scripts", "Docker/PowerShell unavailable in my environment", "this part was checked less thoroughly" and similar notes about Claude's own workflow or tooling limits. User said such notes are inappropriate for the blog (asked to remove one from the Nyx article and to make it a permanent rule).

**Why:** The blog is the user's own voice and publication; notes about the AI's working conditions don't belong in it.

**How to apply:** Never use first person ("я", "мой", "я нашёл", "я проверил") and never present Claude as the author; phrase findings impersonally ("в коде есть...", "тестами не подтверждено", "анализ проведён только по коду"). Write posts as the user's own authored content: state findings and conclusions directly. Keep caveats about limits of the *subject* itself, but not about how Claude worked. Mention any real verification limits to the user in chat instead of in the post.
