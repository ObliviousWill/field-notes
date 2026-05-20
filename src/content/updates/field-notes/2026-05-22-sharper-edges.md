---
project: 'field-notes'
title: 'Sharper edges'
pubDate: 'May 22 2026'
---

A pass over all the small things that make a personal site feel finished. None of them are big features on their own; together they're the difference between a starter template and a site.

## What landed

- **Bylines and reading time on every post.** `Will · 20 May 2026 · 5 min read`. Reading time computed at build from word count, surfaced on the post page, blog index and home recents.
- **British date format.** `20 May 2026`, not `May 20, 2026`. Set on the `FormattedDate` component once, applies everywhere.
- **Hover highlight that slides up from the underline.** Body links default to an amber underline; on hover the underline grows up the height of the text and turns into a marker-style highlight. Works cleanly on multi-line wrapped links thanks to `box-decoration-break: clone`.
- **Sticky right-rail table of contents** on long posts. Renders only when there are 2+ h2s, hides below 1080px. IntersectionObserver lights up the active section as you scroll. (Since dropped in the redesign pass — see the next update.)
- **Prev/next post navigation** at the bottom of every post.
- **Projects taxonomy.** Two new content collections (`projects` and `updates`) with a `reference()` relation, three-state status (`building` / `shipped` / `paused`), and a separate `/projects/rss.xml` feed so subscribers can pick what they follow.
- **OG share images generated per post at build time** via Satori + resvg. Pasting a post URL into LinkedIn or Slack now renders a cream-and-slate card with the title and dek, not a plain text fallback.

![Blog post with byline, reading time, and TOC](/field-notes/updates/post-detail.png)

## Plumbing tidy-up

- Removed every em-dash across the site after deciding they were a tell I wanted to dial down. Comma, colon, full stop, or parentheses depending on context. Mid-thread rewrite of two posts, the About page, and a couple of update bodies.
- Replaced the placeholder `[subscribe / follow / etc — TBD]` on About with real links to LinkedIn and RSS.
- Centred the nav menu permanently using a 3-column grid; added a burger menu below 720px.

## What I'm noticing

The site is functionally complete but visually unremarkable. The typography is fine, the layout is fine, but nothing about it announces itself. That's the next chunk: a full visual rewrite.
