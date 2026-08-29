---
project: 'field-notes'
title: 'The 720px main'
pubDate: 'Aug 29 2026'
---

Reported from a phone: pages were running off the side of the screen, the projects pages worst of all.

The cause was one line inherited from the starter template. `main` was laid out as a **fixed** 720px box:

```css
main {
	width: 720px;
	max-width: calc(100% - 2em);
}
```

The `max-width` was the only thing keeping that box on a small screen, and it is fragile: any page that sets its own `max-width` on `main` overrides it and leaves the fixed 720px width behind. Three pages did exactly that (the projects index, project pages, update pages), each setting `max-width: 760px`. On a 390px phone their `main` laid out 760px wide, so a third of every line sat off the right edge.

Two things hid it. `html` and `body` carry `overflow-x: clip` from an earlier overflow fix, so the page did not scroll sideways and `document.scrollWidth` reported no problem at all: the content was simply cut off instead. And on a desktop browser the fixed 720px is narrower than the space available, so nothing looked wrong.

The fix is to stop pinning the width at all:

```css
main {
	width: auto;
	max-width: 720px;
}
```

An auto width fills whatever room there is, minus its own padding, and the `max-width` caps it on big screens. The three page-level overrides came out, since with a fixed width of 720px they never widened anything on desktop anyway. Desktop is unchanged at 800px total and 720px of content; phones now fit.

Checked every page at 430, 390, 360 and 320px wide, with the `overflow-x: clip` guard switched off so real overflow could not hide, and no element crosses the viewport edge on any of them.
