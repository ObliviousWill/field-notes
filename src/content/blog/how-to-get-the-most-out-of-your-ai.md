---
title: 'How to get the most out of your AI — lessons from my time with Claude'
description: 'Three modes — setup, direction, building — that decide whether you get brilliant work or mediocre work out of any AI tool.'
pubDate: 'May 20 2026'
tags: ['ai', 'marketing']
---

I use AI every day, across just about everything. Claude is the one I reach for most — writing, thinking, design, code. I used ChatGPT every day for 3 years. I've put serious hours into Gemini. I've used Perplexity. And I've used the AI now baked into more or less every piece of software I touch. I'm not listing that to show off. I'm listing it because it's why I trust what I'm about to tell you. When you've used enough of these tools, you stop noticing the differences between them and start noticing the one thing that decides whether you get brilliant work or mediocre work out of any of them.

And it's not the tool. It's how you use it.

Most people open an AI assistant, type a question the way they'd type it into Google, read the answer, and close the tab. It works well enough that they never question it, and because it works well enough they never find out they're getting a fraction of what's on offer. The model isn't the limit. You are. That's fixable, and the fixes carry across: get them right and they make you better with every one of these tools, not just one.

I'm going to teach them through Claude, for two reasons. First, it's where I do this best and where I've learned the most. Second, of all the tools I've used, it implements these principles the most cleanly — so it's the clearest place to see them working. The lessons are universal. The worked examples are Claude. I'll tell you exactly why it's the one I reach for as we go.

The spine is this: a search box answers the question you typed. AI does its best work when you treat it as something you set up, direct, and build with. Three modes, in that order. Most people only ever do the middle one, and they do it badly. Get all three right and the gap between your output and the average user's stops being a difference of degree and becomes a difference of kind.

## 1. Setup: stop introducing yourself every single time

Picture hiring a brilliant assistant and then, every morning, pretending you've never met. You re-explain your job, your company, how you like things written, what you're working on — every day, from scratch. That's what using Claude with no setup is. The model is capable; it just has no idea who you are, so it gives you the answer it would give anyone. Average in, average out.

There are two things worth setting up once, and they pay back every conversation after.

The first is your profile — the standing brief on who you are and how you want Claude to respond. Not your life story. The few facts that change the answer: what you do, who you're usually writing for, and your preferences about output. Mine, roughly, says I lead marketing for an education company, that I want pushback rather than flattery, and that I want the best single recommendation rather than a menu of options. That last line alone changes hundreds of responses. Without it, ask Claude how to structure a campaign and you get "here are five approaches, each with pros and cons." With it, you get "do this, and here's why" — which is what you actually wanted.

The second is memory. Claude can carry useful context from past conversations forward, so the thing you explained on Tuesday is still there on Friday. This is powerful and worth one piece of discipline: the quality of what it remembers depends on the quality of what you tell it. If you say "remember that our brand voice avoids exclamation marks and never uses the word 'solutions'," it holds onto that and applies it. Treat it like onboarding a colleague — feed it the things you'd be annoyed to repeat — and it compounds. And when you're doing something you don't want shaping future answers, there's an incognito mode that doesn't touch memory at all.

Setup isn't a settings-screen chore you do once and forget. The mindset is that context is the product. Almost every disappointing answer is a context failure: you knew something the model didn't, and you didn't say it. Once that clicks, your whole way of prompting changes, which is the next mode.

## 2. Direction: the difference between a question and a brief

This is where the real craft lives, and it's almost absent from every guide I've read. Let me be concrete, because abstract advice about prompting is worthless.

Watch the difference. Here's the search-box version:

> Write a follow-up email to a prospect who went quiet.

You'll get a perfectly serviceable, perfectly generic email. The kind you'd delete from your own inbox. Now here's the same request as a brief:

> I'm following up with a prospect who was keen two weeks ago — we had a great demo, she said she'd take it to her team, then silence. I don't want to sound needy or like I'm chasing. I want to give her an easy, face-saving reason to re-engage, ideally by offering something genuinely useful rather than just "checking in." Keep it under 80 words, warm but not matey, no exclamation marks. Give me the single best version.

Same task. Completely different output, because the second one carries the context that was in your head the whole time. The model can't read your mind; it can only read your message. The skill isn't clever wording. It's the discipline of emptying your head onto the page before you ask.

A few moves that consistently raise the quality of the brief:

**Say who it's for and what you want them to feel or do.** "An email" is a format. "An email that makes a busy headteacher feel this is worth ten minutes" is a brief. The audience and the desired effect do most of the work.

**Give it a constraint to push against.** Length, tone, what to avoid, what's already been tried. Constraints don't limit the output, they focus it. "Under 80 words, no jargon" produces a sharper result than no guidance at all, every time.

**Hand over the raw material.** If you have the half-formed notes, the previous email, the messy transcript, the document — give it to Claude rather than summarising it yourself. You summarising first throws away exactly the detail it could have used. Paste the lot and let it do the sorting.

**Ask for the best one, not a list — if that's what you want.** This is a preference, but it's mine and I'll defend it: a menu of five options is the model declining to make a decision. If you'd rather it commit and reason, tell it to. If you want to compare approaches, ask for that instead. Either way, decide which you want rather than accepting the hedge by default.

**Treat it as a conversation, not a vending machine.** The first answer is a draft, not a verdict. "Good, but too formal and the second paragraph buries the ask — fix both" gets you somewhere a fresh prompt won't. The people who get the most out of Claude are the ones who argue with it.

One more thing on direction, because it's a real lever and most people never touch it: you can tell Claude how to think before it answers. For anything properly hard — a thorny decision, a complex analysis, a plan with a lot of moving parts — asking it to reason through the problem step by step, or to think it through carefully before responding, measurably improves the result. For a quick factual answer it's overkill. For a knotty one it's the difference between a glib reply and a considered one.

## 3. Building: where it stops being a chat and starts being infrastructure

Modes one and two get you dramatically better individual answers. The third mode is what separates people who use Claude as a smarter chatbot from people who've quietly built themselves a set of tools. This is the part the average user never reaches, and it's where the compounding really happens.

There are three things worth understanding here, in rising order of leverage.

**Projects are dedicated workspaces.** Each one has its own instructions and its own knowledge — documents you upload once that Claude then has at hand in every conversation inside that project. The point isn't tidiness. It's that you stop re-establishing context for recurring work. If you run the same kind of task repeatedly — drafting in a particular brand voice, analysing against a fixed framework, writing within a strategy you've already set — a project means you set the stage once and every chat inside it starts halfway up the hill. A separate project keeps unrelated work from bleeding together, so the context stays sharp instead of turning to soup.

**Skills are the step most people don't know exists, and they're the closest thing to a superpower in the whole product.** A skill teaches Claude to do something your way, permanently. Not "remember this fact" — "follow this procedure every time." I have one that produces documents in our exact brand format, colours and typography included, so I never have to re-specify it. You can build one for your analysis process, your reporting template, the way you like project plans laid out — anything you do repeatedly in a consistent way. And you don't have to write it by hand: you tell Claude you want a skill, describe the procedure, and it builds the thing for you. The mental shift is from asking Claude to do tasks toward teaching it how you work, so the asking gets shorter and the output gets more like you every time.

**Artifacts are when Claude builds you something that runs** — a document, a webpage, an interactive tool, a small working app — and shows it right there in the chat rather than just describing it. The wild version is an artifact with Claude built inside it: a little app that uses AI to do its job in real time. A topic-based quiz generator, a tutor, a tool that drafts something on demand. You describe what you want in plain English and get a working thing back, no code. Most people never realise this is possible, which is a shame, because it's the moment the tool stops answering questions and starts making things.

The three build on each other. Setup teaches it who you are. Direction teaches it what you want right now. Building teaches it how you work, so the first two get easier every time. That's the compounding, and it's why a deliberate user pulls so far ahead of a casual one. Not because they type cleverer prompts, but because they've stopped starting from zero.

## A note on the moving parts

A practical aside, because guides that hardcode this stuff are wrong within a month. Claude comes in a few models — at the time of writing, a fast lightweight one, a versatile everyday one, and a heavyweight one for hard thinking — and a few plans, from free up through individual paid tiers to team and enterprise, each with usage limits that scale with price. The exact names, prices, and limits shift often enough that the only sensible move is to check Anthropic's own pricing and documentation rather than trust a number you read in an article, this one included. The principle that won't change: use the light model for quick things, the everyday one for most things, and the heavy one when you're stuck on something hard. Expect a usage ceiling you can raise by paying more. Don't overthink it beyond that.

## The takeaway

If you remember one thing: the gap between a frustrating AI experience and an indispensable one is almost never the model. It's whether you've given it what it needs to help you. Set it up so it knows you. Direct it like you'd brief a sharp colleague, not interrogate a search engine. And when you find yourself doing the same thing twice, build the tool that means you never have to explain it a third time.

The search box is still there if you want it.
