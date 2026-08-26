# birgitbader.github.io

Personal site + blog, built with Hugo. Content lives under `content/`, one Markdown file (or subtree) per page/post.

## Writing conventions

- One sentence per line in Markdown body text (semantic line breaks), regardless of page or content area.
- Curly/typographic quotes and apostrophes (`'`, `"`, `„"`) are house style, not straight ones — matches actual usage across all posts. Don't "normalize" curly quotes to straight.
- `content/imprint.md` and `content/privacy-policy.md` use raw inline HTML (`<div style="display:grid...">`) for two-column layout. Preserve this structure rather than converting it to Markdown.

## Area-specific conventions

- `content/blog/` — post frontmatter (title, slug, description, tags), filename pattern, proofreading checklist. See [content/blog/CLAUDE.md](content/blog/CLAUDE.md). Tags render as "Categories" on `/blog/` and on each post — there's no standalone `/tags/` overview page; it's deliberately disabled (`disableKinds = ["taxonomy"]` in `hugo.toml`) since the category list already lives on `/blog/`. Individual `/tags/<slug>/` pages still build, via `layouts/tag/term.html` (not `layouts/_default/term.html` — that path is silently ignored by this Hugo version once a custom `[taxonomies]` table is set).

As conventions for other content areas (about page, imprint, etc.) come up, add a `CLAUDE.md` next to that content and link it here.

## Redirects

This site has no automatic redirect mechanism — renaming a post `slug` or a tag value breaks the old URL permanently unless a redirect is added, and old links (search engine index, social shares, bookmarks) keep pointing at it indefinitely. This already caused real 404s in production once (a pre-launch URL cleanup and an August 2026 tag rename, both without redirects).

- **Renaming a post's `slug`**: add the old path to that post's `aliases:` front matter field, e.g. `aliases: ["/blog/old-slug/"]`. Hugo generates a redirect stub there automatically.
- **Renaming a tag value**: taxonomy term pages can't take `aliases:` (no content file backs them). Instead, add a static redirect stub at `static/tags/<old-tag-slug>/index.html` — a minimal HTML file with `<meta http-equiv="refresh" content="0; url=...">` pointing at the new tag URL. See `static/tags/technical-writing-craft/index.html` for the pattern.
