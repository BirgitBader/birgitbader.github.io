# birgitbader.github.io

Personal site + blog, built with Hugo. Content lives under `content/`, one Markdown file (or subtree) per page/post.

## Writing conventions

- One sentence per line in Markdown body text (semantic line breaks), regardless of page or content area.
- Curly/typographic quotes and apostrophes (`'`, `"`, `„"`) are house style, not straight ones — matches actual usage across all posts. Don't "normalize" curly quotes to straight.
- `content/imprint.md` and `content/privacy-policy.md` use raw inline HTML (`<div style="display:grid...">`) for two-column layout. Preserve this structure rather than converting it to Markdown.

## Area-specific conventions

- `content/blog/` — post frontmatter (title, slug, description, tags), filename pattern, proofreading checklist. See [content/blog/CLAUDE.md](content/blog/CLAUDE.md). Tags render as "Categories" on `/blog/` and on each post — there's no standalone `/tags/` overview page; it's deliberately disabled (`disableKinds = ["taxonomy"]` in `hugo.toml`) since the category list already lives on `/blog/`. Individual `/tags/<slug>/` pages still build, via `layouts/tag/term.html` (not `layouts/_default/term.html` — that path is silently ignored by this Hugo version once a custom `[taxonomies]` table is set).

As conventions for other content areas (about page, imprint, etc.) come up, add a `CLAUDE.md` next to that content and link it here.
