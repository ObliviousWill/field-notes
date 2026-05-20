---
project: 'field-notes'
title: 'Foundation in place'
pubDate: 'May 20 2026'
---

Most of the scaffolding is done. The site is live on GitHub Pages, three pages render, and the first post is out.

## What's here

- **Astro blog starter**, scaffolded directly from `npm create astro@latest` and configured for the `/field-notes` base path on GitHub Pages.
- **A theme of my own**: cream `#EEE9DF`, slate `#2C3B4D`, amber `#FFB162`. Pulled from a palette I'd saved on Pinterest, then adapted using [Coolors](https://coolors.co/generator) to tune the contrast. Body text passes WCAG AAA against the cream; the amber is reserved for fills and borders, with a deeper amber for link text so the brand colour doesn't fail contrast.
- **Logo and favicon** designed in Canva and dropped into the repo as SVG. Header centred on a 3-column grid so the nav stays dead-centre regardless of what flanks it; a burger menu kicks in below 720px.
- **Post layout** has a byline (`Will · 20 May 2026 · 5 min read`), an italic dek pulled from frontmatter, a sticky right-rail table of contents with scroll-spy highlighting on wide viewports, and a tight tag taxonomy (`building`, `marketing`, `ai`) enforced by the content schema.
- **Homepage** is a curated landing: tagline + recent posts. About page is written. First blog post (*What I learned building a website with AI*) shipped.

## What's next

- This project page and its update feed — the bit you're reading.
- **Write more.** A handful more posts before promoting widely, so the site reads lived-in rather than just-launched.
- **Add more projects.** Other artefacts in flight (the AI chatbot, the meal-planning app) get their own project pages with the same update-log pattern.
- **Get feedback from colleagues.** Soft-launch to a small circle, see what lands, what's confusing, what they wish was here.
- A real typography pass: line length, code-block styling, blockquote treatment.
- Open Graph image generation so links share well.
- **Maybe** a custom domain at some point — purely to move off the `obliviouswill.github.io/field-notes` URL. It's a nice-to-have, not a blocker.
