---
project: 'field-notes'
title: 'Fixing pages that ran off phone screens'
pubDate: 'Aug 29 2026'
---

Someone told me pages were running off the side of their phone screen, the projects pages worst of all.

The cause was one setting left over from the template I started with. It told the main column of every page to be a fixed width. Something else usually squeezed it down to fit a phone, but three pages had their own settings that undid that. On those pages, a third of every line was cut off.

It was easy to miss for two reasons:

- On a computer the screen is wide enough, so nothing looked wrong.
- An earlier fix stopped pages scrolling sideways. So on a phone the extra text was just cut off, quietly, instead of being obviously broken.

The fix was to stop fixing the width. The column now fills whatever space there is, up to a sensible maximum on big screens. Nothing changed on a computer, and phones now fit.

I then checked every page at four phone sizes, down to the smallest common one, with that earlier fix switched off so nothing could hide.

**The lesson:** "it looks fine on my laptop" isn't testing. Most people will read this on a phone.
