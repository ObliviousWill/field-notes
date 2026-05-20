---
title: 'What I learned building a website with AI'
description: 'One hour, a blank repo, and Claude Code as the only collaborator. What looking under the bonnet revealed about AI, marketing, and the work.'
pubDate: 'May 20 2026'
tags: ['building', 'ai']
mentions:
  - field-notes
---

Three pages, one hour one morning this week, no builder, no agency, no developer. Just me and Claude (chat for the thinking, Claude Code for the building) and a GitHub integration that took ten minutes to set up. This site is the result. All in, it'll cost about £10 a year for a domain; hosting is free on GitHub Pages.

I've been on all sides of the fence with websites. I've commissioned them, designed them in Figma and Sketch, briefed them to UX designers, been the page builder doing the content pop, then the admin keeping the lights on. I've used WordPress for years and Joomla before that (sorry). I've built pages in Elementor and WP Bakery and the rest. What I'd never done, until this week, is sit down with a blank repo and make a website exist.

I should be honest about what I'd have done otherwise. For a personal site like this, I wasn't going to commission anyone. I'd have reached for Wix or Squarespace, picked a template, and called it done. That's the alternative I'm comparing this to. And the comparison is interesting, because while Squarespace would have been a bit faster to have something live, I'd have learned almost nothing in the process, and I'd be locked into a platform's idea of what a website is.

The point of this post isn't you should do this too. The point is what one hour of looking under the bonnet revealed about the art of the possible with AI, and what it might mean for the marketing teams I run.

## What the builder was hiding

For my whole career, the layer I've operated in has been everywhere from oversight to page builder. Drag a block. Set padding. Pick a heading style. The layer underneath (what an actual web page is, how it gets from a folder of files to a URL someone can visit) has been opaque to me, deliberately, because that's what the builder is for.

Building this site forced me into that arena. I now know what a static site generator does. I know why you'd use one (fast, cheap, secure, version-controlled) and why you wouldn't (no live editing for non-technical users, every change is a code change). I know what a build step is and what it's for. I know what GitHub is doing when it runs workflows and serves the site.

None of this makes me a developer. I couldn't debug the slightest issue without the AI. But the shape of how a website works is no longer a mystery to me, and that turns out to matter. Because for the first time, in a conversation with devs, I might just have heard some of the words before.

## A workflow worth paying attention to

The site itself is unremarkable (for now). Three pages, customised styling, content I wrote. What was remarkable was the process.

In WordPress, making a change means logging in, clicking through to a page, dragging a block, hoping the preview is accurate, publishing. The cycle is fine but the system is heavy: plugins, themes, a database, regular updates, the occasional security panic.

This site has none of that. To change something, I edit a file, commit, and ninety seconds later it's live (or even easier, I simply describe what I want to happen and boom!). Every change is logged, reversible, and visible to anyone I want to share it with. To create a new page, I write a new file. To restructure the site, I move files around.

I won't pretend that's a workflow that suits everyone on a marketing team. It absolutely doesn't. But what it suggests is something worth paying attention to: the gap between what marketers can do directly and what they need to ask for is moving. Some things that were a ticket two years ago are a chat message now. Not because the marketer learned to code, but because the AI did, on their behalf, with enough scaffolding that the marketer can drive.

That's the workflow I'm interested in. This site is a tiny version of it.

## Three things I'd tell my own team

On the basis of one morning, with appropriate humility.

**The expertise matters and we have to respect that more than ever.** I built three pages. I didn't deal with accessibility properly, or performance, or analytics, or SEO at any depth, or any of the dozen things a good agency builds in by default. The people I've worked with over the years are exceptional; powered by this sort of technology, they'll have superpowers. What's changing is the base rate of what a non-developer can do before they need to call those people.

**The hard part isn't the building, it's the deciding.** Most of my morning wasn't spent making things. It was spent answering questions: what do you want, who is this for, what should be on it, what shouldn't, what's the URL, what's the tone. The AI was very fast at the building. The decisions were still mine. That's the right division of labour, and I suspect it's the right one for most marketing work in these early parts of the AI era.

**Start with something real.** I learned more from one hour on a real project than I would have from a week of YouTube tutorials (but I do love them too). The thing I was building was small enough to finish and serious enough to teach me. If you're trying to figure out where AI fits in your work, my honest advice is: find a project you've been putting off, and try it.

## Where this site goes next

The version you're reading is the foundation. The front end is the Astro blog starter with the lights barely on. I haven't touched the design yet. The next phase is using AI to push the look and feel into something that's actually mine, and I'm going to map that progress as I go. There'll be a dedicated project page for this site soon, tracking what I'm trying, what's working, and what isn't: the same "show the work" principle this whole site is built on.

If you want to see how far a non-developer can take a website with AI as the only collaborator, watch that page.
