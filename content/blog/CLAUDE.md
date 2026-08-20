# Blog post conventions

## Frontmatter

```yaml
---
title: "Title Case-ish, sentence style is fine"
date: YYYY-MM-DD
description: "One to two sentences."
tags: ["existing-tag"]
draft: true
slug: "slug-here"
---
```

- `description`: not a summary — a contrast/hook sentence (concrete premise → broader takeaway), roughly 150–200 characters. Look at existing posts for tone before writing one.
- `tags`: exactly one tag from the existing curated set — `documentation`, `career`, `craft`, `API docs`. Don't invent a new tag ad hoc; the set stays small and recurring on purpose (see root `CLAUDE.md`). If a post doesn't fit an existing tag, propose a new one explicitly rather than silently expanding the set.
- `slug`: kebab-case.
  - If the title is a single clause, slug the full title (e.g. "The space between how we work and how we document" → `the-space-between-how-we-work-and-how-we-document`).
  - If the title has a colon (hook + subtitle), slug only the hook half (e.g. "Vibing with pride: what rebuilding my website taught me" → `vibing-with-pride`). Keeps URLs short and shareable.
- Filename pattern: `NNN_slug.md` (underscore), `NNN` zero-padded to 3 digits, matching the numeric order of posts. (Post 008 was published with a hyphen, `008-what-rebuilding-my-website-taught-me.md` — a one-off; underscore is the standard going forward.)
- Leave `draft: true` until the post is meant to go live.

## Proofreading pass (before publishing)

Do a proofread as an American English native / professional proofreader — grammar, typos, punctuation — and apply fixes directly rather than just listing them:

- **Americanize spellings**: realised→realized, colour(s)→color(s), recognise→recognize, learnt→learned, favour→favor, organise→organize, etc.
- **Americanize constructions**: "couldn't have got" → "couldn't have gotten".
- **Em dashes**: use `—` (spaced: ` — `) for asides, not a bare hyphen `-`.
- **Quote/apostrophe style**: this repo uses curly/typographic quotes and apostrophes (`'`, `"`, and `„"` for German-style scare quotes) throughout body text, not straight ones. Normalize any stragglers to match.
- Watch for made-up/misspelled words (e.g. "pixeled" → "pixelated").
- Don't touch intentional voice choices — sentence fragments, starting sentences with "And"/"But", missing Oxford commas — these are consistent stylistic choices across posts, not errors.
