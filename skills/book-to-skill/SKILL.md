---
name: book-to-skill
description: "Turn a non-fiction book the user owns into a private Claude reference skill: a core-frameworks SKILL.md, one summary page per chapter, a chapter and topic index, a glossary, a patterns file and a decision cheatsheet, then run a content check for accuracy, copyright and appropriateness before packaging it as a .skill file. Use whenever the user says 'book to skill', 'turn this book into a skill', 'make a skill from this book', 'Claude should know this book', uploads a book PDF, EPUB or text and wants Claude to work from it, or asks to re-check or audit a skill already built from a book."
---

<!-- argument-hint: [path to the book file, or the name of an existing book skill to re-check] -->

# Book to Skill

Builds a private study-notes skill from a book so Claude works *from that book* instead of from general advice. The output is summaries and frameworks in the user's own words, never the book's text.

Read [references/templates.md](references/templates.md) before writing any output file, and [references/content-check.md](references/content-check.md) before Stage 6.

## Ground rules (apply to every stage)

1. **Source only.** Every claim, framework, number and example must come from the book the user supplied. Do not fill gaps from memory of the book, other books, the author's videos or reviews. If the source is missing a chapter or is unreadable, say so and leave the gap marked, do not reconstruct it.
2. **The user must own the copy.** Work only from a file the user provides. Never search for, download or accept a pirated copy. If the user has no file, offer to build from their own reading notes instead.
3. **Summaries, not the text.** Paraphrase. Quotes only where the exact wording *is* the idea (a slogan, a formula, a named rule), at most 25 words each and no more than three per chapter, always in quotation marks.
4. **Private by default.** The finished skill stays private to the user (their own skills folder or a private repo). Never publish it, attach it to a public repo or share it as a substitute for the book.
5. **The author's results are the author's.** Figures and case studies are reported as the author's own claims ("Hormozi reports…"), never as promises or typical results.
6. **UK English**, plain words, short sentences.

## Workflow

### Stage 1: Intake
Confirm, in one message, only what you cannot work out from the file:
- the book file (PDF, EPUB, DOCX, TXT or Markdown) and that the user owns the copy
- skill name: lowercase-hyphenated, author-plus-topic (for example `hormozi-offers`)
- what the user will use it for (this shapes the cheatsheet and the "use when" triggers)
- related book skills already installed, so the two can point at each other

### Stage 2: Extract and map
1. Convert the file to plain text in a scratch folder outside the skill (for example `pdftotext -layout` for PDF, `pandoc` for EPUB and DOCX). Check the text is clean: no missing pages, no scrambled columns, no OCR junk. If it is poor, tell the user before continuing.
2. Find the real chapter boundaries from the table of contents and headings. Record title, start and end, and word count per chapter in a scratch `chapter-map.md`.
3. Note the book's metadata from the text itself: full title, author, edition or year, total word count.

### Stage 3: Chapter pages
For each chapter, read the whole chapter text, then write `chapters/chNN-short-slug.md` using the chapter template. One chapter at a time; do not write a page from a skim.
- Name every framework exactly as the author names it.
- Keep each number with its context (who, what, over what period).
- "Connects To" links only to chapters that genuinely build on each other.
- Chapters with little substance (a thank-you, a request for reviews) get a short page that says so, marked "(thin)" in the index.

For a long book, chapters can be drafted by parallel subagents, but each subagent gets the ground rules above, the chapter template and only its own chapter text, and you read every page it returns.

### Stage 4: Cross-book files
From the finished chapter pages (not from memory), write:
- `glossary.md`: every named term, one line each, with chapter references, alphabetical
- `patterns.md`: each technique as When to use / How / Trade-offs, with chapter references
- `cheatsheet.md`: decision rules (When… / Do… / Because…), pickers and thresholds, aimed at the use the user gave in Stage 1

### Stage 5: SKILL.md and README
Write the generated skill's `SKILL.md` (core frameworks, chapter index, topic index, supporting files, scope and limits) and `README.md` from the templates.
- The description says which book and author, then lists the frameworks and the jobs it helps with, so it triggers on those topics.
- Core frameworks: the 5 to 8 ideas that answer most questions, each with chapter references.
- Scope and limits always includes: content only from this book; figures are the author's own; the UK advertising and consumer law line from the template whenever the book covers marketing, pricing, guarantees, scarcity, urgency, reviews or claims; and the regulated-advice line from the template whenever the book covers health, money, law or children.

### Stage 6: Content check (mandatory)
Run both parts before anything is packaged. Do not skip this even if the user is in a hurry.
1. **Automatic:** `python3 scripts/check_skill.py <skill-folder>`. Fix every ERROR. Read every WARNING and either fix it or note why it stands.
2. **Read-through:** work through [references/content-check.md](references/content-check.md) section by section against the source text. Spot-check at least one number, one quote and one framework per chapter against the book.

Then give the user a short check report:
- what was checked
- what you changed
- anything still open that needs their judgement (one line each)

Only package once the user has seen that report.

### Stage 7: Package
`python3 scripts/package_skill.py <skill-folder> <output-dir>` produces `<name>.skill` (a zip with the folder at the root). It re-runs the check and refuses to package if any ERROR remains. Tell the user to install it by uploading the `.skill` file in Claude's Skills settings, or by copying the folder into `~/.claude/skills/`.

## Re-checking an existing book skill
When asked to audit a skill already built from a book, skip to Stage 6 and run it against that folder. If the book file is available, do the spot-checks against it. If it is not, say the accuracy check was limited to internal consistency and plausibility, and list the claims you could not verify.

## Output structure
```
<skill-name>/
├── SKILL.md
├── README.md
├── glossary.md
├── patterns.md
├── cheatsheet.md
└── chapters/
    ├── ch01-<slug>.md
    └── …
```
