---
project: 'kpi-reports'
title: 'One page, one link, updated every day'
pubDate: 'Sep 10 2026'
---

A report that only one person reads isn't doing its job. So I changed where it goes.

The report is now a single web page in a shared folder. Every morning at 8am Claude updates that same page. People bookmark it once and it is always current. Nobody has to send anything round.

It takes about twelve minutes and nobody watches it. That made me strict about checks:

- **Look before you touch.** If the page has been changed since yesterday, stop. Don't force the update over someone's work.
- **Add it up two ways.** The daily figures must match a separately fetched total. This has already caught a wrong number.
- **Zero isn't the same as missing.** In school holidays some numbers really are zero. If a question fails, the report keeps yesterday's figure and says so, rather than showing a zero that looks real.
- **Read it back.** After saving, it opens the page again and checks what actually landed.
- **Tell a human.** It sends one short message, leading with anything that needs a person.

My favourite lesson from building it: a scheduled job that finds a problem and tells nobody has failed.

I wrote the method up as a short guide so colleagues can build their own reports the same way.
