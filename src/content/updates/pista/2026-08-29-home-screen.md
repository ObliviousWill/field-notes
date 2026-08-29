---
project: 'pista'
title: 'Sized for a home screen'
pubDate: 'Aug 29 2026'
---

Added to an iPhone home screen the app runs in standalone mode, and that is a different shape to the one I had been measuring. There is no Safari URL bar, so it is taller, but the app now draws underneath the status bar and the home indicator, and nothing in the layout knew about either.

The page already set `viewport-fit=cover` and a translucent status bar, which is what lets it fill the screen. What it never did was pad for the inset, so the masthead and the sticky event header sat behind the clock.

Every offset now comes from four variables set once, `--sat`, `--sab`, `--sal` and `--sar`, reading `env(safe-area-inset-*)` with a zero fallback. The shell pads for the top inset, the event header sticks below it rather than at zero, and a fixed strip fills the space behind the clock so scrolled content never slides under it. Landscape gets the left and right insets too, which matters on a notched phone turned sideways. As a side effect the whole thing is testable: override the four variables and you can measure any iPhone's standalone viewport in a desktop browser.

Then a pass on spacing so the main screens fit that viewport without scrolling: tighter page heads and dividers, denser list rows and tables, and two step-down tiers for short screens, one at 815px and one at 700px, that trim chrome rather than tap targets. Everything stays at 44px.

Measured across five phones in standalone, from a 16 Pro Max down to an SE, every screen fits on every one of them, bar the third step of the event set-up on the SE, which runs 9px over. Safari with its URL bar showing improved as well: the players list and every wizard step now fit where they used to scroll.
