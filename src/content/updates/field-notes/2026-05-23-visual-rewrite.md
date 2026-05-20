---
project: 'field-notes'
title: 'Visual rewrite'
pubDate: 'May 23 2026'
---

Worked through a full visual rewrite, designed off-site as a handoff document and then implemented in Astro. The bones stayed the same; the typography, atomic vocabulary, and density all changed.

## What changed

- **Bowlby One for display type**, paired with Atkinson Hyperlegible for body. The chunky slab on h1s and post titles gives the site a wordmark-level personality every page rather than only at the brand mark. Bundled locally so the build works without external font calls.
- **Wordmark header.** "FIELD NOTES" in display amber, top-left. Nav centred, LinkedIn icon top-right. Active page indicated with a 2px amber underbar.
- **Category colours.** Each tag has its own hue at matched chroma: amber for `ai`, sage for `building`, lilac for `marketing`. Small pill chips on post rows and at the top of each post.
- **`PostRow` atom.** Replaces the old list item. Meta line of chips and date, chunky display title with a marker-wipe hover, optional excerpt, optional mentions. Used on the home recents, blog index, post-detail "Next note", and project related-posts.
- **Read-state dots.** Each post row has an amber unread dot that toggles on click and persists to `localStorage`. The blog index shows a count and a "mark all unread" link.
- **Reading progress bar** on post pages. 3px amber fill at the top, updates on scroll. A `~N min left` caption in the breadcrumb strip tracks alongside it.
- **Updates timeline.** Project detail page now renders updates as a vertical timeline with a left date gutter, an amber rail dot for the most recent entry, and outlined dots for older ones.
- **Newsletter block.** Single canonical visual at the bottom of Home, Blog, Post and Project detail. Real email input + Subscribe button; RSS link alongside. Form action is a placeholder until a provider's wired up.

![Blog index in the new layout](/field-notes/updates/blog-index.png)

## What I held off on

- **Mono "code-input" blockquote** for the verbatim search-box prompts in the AI post. Current rendering uses the display-font blockquote; it works but isn't the design's intended visual for that specific case.
- **Per-tag archive pages.** The "Browse →" links on the About category blocks land at the full blog index. Tag pages earn their keep once there are more posts to filter.
- **Newsletter provider.** The form posts to `#` until I pick one. Buttondown's the likely choice when it's worth wiring.

## What's next

- Drop in real screenshots in the updates above (these three images are placeholders until I commit the proper exports).
- Soft-launch to a handful of colleagues for feedback.
- Three or four more posts before any wider promotion, so the archive doesn't read just-launched.
