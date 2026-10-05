---
name: feedback-no-font-size-changes
description: "Never change font sizes on bukatchuk.ru without the owner's explicit instruction"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4c743645-b3c1-4181-8c98-2ea5b76bf5cc
  modified: 2026-10-04T21:29:27.307Z
---

Do not change font sizes on bukatchuk.ru unless the user explicitly asks for it. On 2026-10-05 I shrank the home page hero heading (99px → ~62px) so that a longer headline would fit on two lines; the user said it became "очень маленький", asked to restore the size and added "в будущем не меняй размер шрифта без моего указания".

**Why:** The typography of the Axis Industrial template is the owner's deliberate design; a text edit is not permission to touch the layout.

**How to apply:** When new text doesn't fit (wraps to an extra line, overflows), keep the size as is and tell the user about the wrap, offering options (shorter text, different line break, smaller size) for them to choose. My interpretation: the same applies to other visual parameters of the template (spacing, weights, colors) — change only what was asked.
