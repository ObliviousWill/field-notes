---
project: 'pista'
title: 'First serve'
pubDate: 'Aug 28 2026'
---

PISTA now lives at [/pista/](/field-notes/pista/) as its own part of the site: full screen, dark, no site header or footer in the way, with one link back to Field Notes in the corner.

## What it does

- **Four formats.** Americano and Mexicano (rotating partners, you score for yourself), fixed pairs round robin, and a single match with proper sets and a golden point.
- **The draw is automatic.** Each round it picks partners and opponents by cost: heavy penalty for repeating a partner, lighter one for repeating an opponent, and it evens out who sits when the numbers do not divide by four. There is a redraw if the round it picks looks wrong.
- **Standings as you go.** Points for, wins, difference, and a running all time table across every event on the home screen.
- **Squad changes mid event.** People arrive late and leave early, so who is playing can change between rounds without restarting the event.

## Storage

The version this started from was built to save into a hosted account. On a static site there is no server to save to, so that layer came out and the app now writes straight to the browser's own storage on the device you score on.

That is a real trade: your results come back when you reopen the page on that phone, but they do not follow you to another one, and clearing site data wipes them. So History has Copy backup, Download file and Restore, and if a browser refuses to store anything (private windows, blocked site data) a banner says so up front rather than quietly losing the night's scores.

## Under the hood

One page, no framework, no build step of its own. The whole app is inline CSS and inline JavaScript inside an Astro page, which means it loads as a single document and keeps working on a phone with one bar of signal at the side of a court. Added to the home screen it opens standalone, with the icon and its own manifest.
