---
name: feedback-vinyl-about-search-web
description: For the vinyl section, when Wikipedia has no article about an album, search the web before leaving «Об альбоме» empty
metadata:
  type: feedback
---

When writing the «Об альбоме» text for a release in the bukatchuk.ru vinyl section and Wikipedia has no article (or only a line) about it, search the web for other sources instead of leaving the field empty. Said by the user on 2026-10-05 after I left four Schiller releases without the text and only offered to look further.

**Why:** The user wants every release page to have the album story; "no Wikipedia article" is not a reason to stop.

**How to apply:** Order: English Wikipedia, then German or the artist's language, then web search — label press release, artist's official site or shop, interview, review. Take only facts (dates, chart positions, names), not promotional wording; skip a fact when sources disagree and tell the user. Put the source URL in `about_source` and its name in Latin script in `about_source_name` (`Wikipedia`, `Sony Music`, `Discogs`). Leave the field empty only when the search found nothing reliable, and say where I looked. The same rule is written in the repo's `.claude/CLAUDE.md`, section «Раздел „Винил“».
