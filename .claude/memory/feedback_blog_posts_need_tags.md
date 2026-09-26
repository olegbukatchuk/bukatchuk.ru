---
name: feedback-blog-posts-need-tags
description: Every bukatchuk.ru blog post must have front-matter tags (3-5, short lowercase English, reuse existing ones)
metadata:
  type: feedback
---

Every article for the user's blog (bukatchuk.ru, see [[feedback-blog-no-meta-notes]]) must have a `tags` field in front matter. The Nyx article was first published without tags and the user asked to fix it and make it a permanent rule.

**Why:** Tags feed the post header (first tag shown in the eyebrow), the tags at the bottom of the post and the site-wide `/tags/` page; a post without tags is missing from topic navigation.

**How to apply:** Add `tags: [a, b, c]` with 3-5 short lowercase English words, matching the existing vocabulary (`bash`, `law`, `sales`, `b2b`, ...). Check existing tags first (`grep -h "^tags:" blog/_posts/*.md`), add a new tag only if nothing fits. The first tag is the main topic. Verify after a Jekyll build that tags render on the post and on `/tags/`. Never commit a post without tags.
