---
title: 'I gave my team AI colleagues. The rules mattered more than the AI.'
description: 'Six AI helpers, each looking after one number, and a seventh that checks their work. What I learned setting them up, and why the hardest part was protecting my own attention.'
pubDate: 'Oct 13 2026'
tags: ['ai', 'marketing']
mentions:
  - ai-agent-team
---

Most AI at work is one person and one chat window. You ask, it answers, you copy the useful bit somewhere else. It helps you, and it stops with you. Nothing builds up, and nobody else benefits.

I wanted something different: AI helpers the whole team could rely on, that turn up every morning whether or not anyone remembers to ask. So for the last few weeks I've been building a small team of them for marketing. This post is about what I learned. The [project page](/field-notes/projects/ai-agent-team/) has the details.

## A quick explanation first

An "agent" is just an AI that does a job on its own, on a schedule, instead of waiting for you to type something. Mine wake up early every weekday, look at our systems, and decide whether there's anything worth raising.

There are six, plus one that checks their work:

- **Scout** watches how full our clubs and classes are.
- **Ranger** watches enquiries from schools.
- **The search helper** watches how people find us on Google.
- **The website helper** keeps our web pages accurate.
- **The writer** suggests and drafts articles.
- **Judge** checks everyone else's work before it reaches me.

## Lesson 1: the problem isn't what AI can do. It's what you can decide.

My first design produced too much. Reports, ideas, analysis, every day. All of it was decent, and I couldn't get through it. A pile you can't get through is worse than no pile, because now you feel behind as well.

So the most important rule is now: **at most one suggestion per helper per day.** It has to be the one that would make the biggest difference. If nothing is worth raising, the helper raises nothing, and that counts as a good day.

There's a second rule that goes with it: **one thing waiting at a time.** If I haven't dealt with a helper's last suggestion, it doesn't add another.

## Lesson 2: give it a job, not a to-do list

Giving a helper a list of tasks didn't work. What worked was giving each one **a single number to look after**, the way you'd describe a job to a new starter. "Keep the clubs full." "Make sure no school enquiry goes cold."

Then it needs what any new starter needs:

1. a clear job
2. access to the right systems, and nothing more
3. set working hours
4. a manager
5. someone to check its work
6. a memory of what it's been told before

Leave any one of those out and the written instructions on their own do nothing.

## Lesson 3: nothing can mark its own homework

In the first version, each helper checked its own work. Two of the worst mistakes got straight through. The helper that made a mistake was the worst one at spotting it.

So now there's Judge. Judge can't change anything. It can only pass or fail, with reasons. It re-checks at least two numbers in every suggestion against the original source, rather than trusting the summary. Its instructions say "be hard to please", and also "don't fail things just to look tough".

Every Friday, Judge checks itself too. If it has passed almost everything for two weeks running, it has to say so. Either the helpers are very good or it's gone soft.

## Lesson 4: suggest, never decide

None of the helpers can approve anything. Not because they'd do it badly, but because a person should own the decision, especially when it touches customers, money or staff.

For the first few weeks, they can't change anything at all: they can look and suggest, nothing more. The ones that could eventually edit the website have an on/off switch written into their instructions, set to off. Only I can turn it on.

I'll be honest about the weak spot. Right now they work through my login. The rule says "never approve", but nothing technical stops them. The fix is for each helper to have its own account with its own limits, and that's next on the list.

## Lesson 5: put it where people already look

I don't open a chat to manage any of this. Suggestions appear on the same task board the rest of the team uses. I approve or reject them there, with a one-line reason. Each morning Judge sends me one short email: at most three things that need me, most important first.

And when I turn something down, the helpers read my reason. They only bring the idea back if the evidence has changed.

## What I'd tell anyone trying this

- **Design around your attention, not the AI's ability.** The AI can produce far more than you can read.
- **Fewer, shorter suggestions beat more output.** Mine are about 150 words, starting with the question I need to answer.
- **Separate the doer from the checker.**
- **Talk about jobs early.** Some tasks will shrink. Plan that openly, role by role, rather than letting it happen by accident.

It's early. They went live together for the first time this week. But the shape feels right: AI does the groundwork, and people make the decisions.
