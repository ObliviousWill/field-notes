---
title: 'Rota and holiday planner'
summary: 'Two simple web pages for my teams. One shows who is covering customer service each day and warns when a day is going to be too busy. The other shows who has booked holiday, and spots clashes before they happen.'
status: 'shipped'
area: 'work'
startDate: 'Sep 18 2026'
facts:
  - label: 'What it is'
    value: 'A shared cover rota and a holiday planner'
  - label: 'Who uses it'
    value: 'Me and the people who manage the teams'
  - label: 'What it replaced'
    value: 'A fixed rota on paper and a holiday system nobody could plan from'
  - label: 'Personal data'
    value: 'First names only. No reasons for leave are stored'
---

Small teams are fragile. If two people out of five are off on a busy Monday, customers wait. I wanted to see that coming instead of finding out on the day.

So I built two pages, using Claude. You just open them in a browser like any other website. Nobody needs to install anything.

**The cover rota** shows the next fortnight as a row of days. Each day shows who's on. Days turn amber when the workload looks heavy and red when there aren't enough people. It knows that school holidays, half terms and bank holidays change how busy we are. It learns from what actually happened in past weeks, so its forecast gets better over time. If someone books holiday, they drop off the rota automatically.

**The holiday planner** answers the questions a manager actually has:

- Is anyone on track to lose days at the end of the year?
- Are too many people off at once?
- Are two people who cover for each other both off?
- What should I raise in this week's one-to-ones?

The HR system is still the official record. These pages are for planning.

## Privacy

Rotas and holidays are about people, so I kept the data to a minimum:

- Only first names are stored.
- A reason for leave is only ever "holiday", "training" or "unavailable", so no health information can end up in there.
- Only I can edit. Anyone I share it with can look but not change anything.
