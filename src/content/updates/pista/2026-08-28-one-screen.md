---
project: 'pista'
title: 'One screen at a time'
pubDate: 'Aug 28 2026'
---

Measured the app in a browser at phone sizes rather than guessing, and the live event screen came out at 1.6 screens tall on a big phone, 2.1 in Safari once the URL bar takes its cut, and 2.4 with twelve players. Everything you do during a round was a scroll away from everything else.

## What changed

- **Round and Table are now two tabs**, not one long page. The standings were 471px of the 1370px total, sitting under the court you were trying to score. Both halves fit a screen on their own, and in landscape the tabs disappear because the two column layout already shows both.
- **The primary action sticks to the bottom.** Round 3 →, Start match, Set the rules: all of them used to sit at the very end of a scrolling page, off screen exactly when you wanted them.
- **Rare actions moved into a ⋯ menu** in the header: redraw, who is playing, run it back, copy the table, delete. That is 135px back, and Delete event is no longer a thumb's width from the round you are scoring.
- **The header is one sticky line** now (`← Thursday night · Americano · Round 1 of 4`) instead of a back button above a title block, which keeps the round number visible while you scroll.
- **Sitting out is a row of avatars** rather than named chips wrapping onto two lines.
- Toasts moved to the bottom of the screen, above the tab bar, so Undo is where your thumb already is.
- The fonts load through a `<link>` instead of an `@import` inside the stylesheet, which was blocking the first render on an extra round trip.
- Fixed the round chips: as `<button>` elements they were picking up the browser's default grey background, so unplayed rounds looked filled in.

## Result

| Screen | Before | After |
| --- | --- | --- |
| Live event, phone | 1.62 screens | 1.00 |
| Live event, Safari | 2.06 | 1.00 |
| Live event, small Android | 2.28 | 1.00 |
| Standings tab | (same page) | 1.00 to 1.09 |
| Desktop | 1.66 | 1.00 |

The players list and the set-up wizard still scroll a little on a short viewport, which is fine: a list of people is meant to scroll, and the wizard's button now follows you down the page.
