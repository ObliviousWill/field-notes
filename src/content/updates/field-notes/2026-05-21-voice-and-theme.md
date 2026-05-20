---
project: 'field-notes'
title: 'Voice, theme, and the first post out'
pubDate: 'May 21 2026'
---

The bare Astro starter is gone. The site now has a colour scheme of its own, a logo, an About page that sounds like me, and the first real post is live.

## What landed

- **Cream / slate / amber palette.** Pulled from a Pinterest palette I'd saved, adapted in [Coolors](https://coolors.co/generator) for contrast. Body text passes WCAG AAA against the cream; the amber stays out of text contexts because it fails at 1.5:1 against the background. A deeper amber sits behind the link text for the same reason.
- **Logo and favicon.** Designed in Canva (a chunky orange "F"), exported as SVG, dropped into the repo. The header centres the nav using a 3-column CSS grid so the menu is dead-centre regardless of what flanks it.
- **About page rewritten.** Three pillars (Things I'm building / Marketing thinking / AI, practically) and a short note on what the site isn't. The voice is mine, not the starter's.
- **First post: *What I learned building a website with AI*.** Tagged `building` and `ai`. The whole point of the post is the thing the post is hosted on, which felt like the right way to start.
- **Tag schema locked.** Only three tags exist in the content collection: `building`, `marketing`, `ai`. The schema enforces it, so I can't accidentally invent a fourth.

![About page with the new theme](/field-notes/updates/about.png)

## What I'm noticing

The post body needs more typographic care than I gave it on day one. Headings, blockquotes, code blocks all want a deliberate pass rather than the starter's defaults. That's the next chunk of work.
