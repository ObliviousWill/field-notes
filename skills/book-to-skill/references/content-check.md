# Content check

Work through every section. For each problem found: fix it, or record it in the check report with a reason. "Looks fine" is not a result; name what you checked.

## 1. Accuracy (against the source text)
- [ ] Every chapter page matches its chapter: right title, right number, nothing from a neighbouring chapter.
- [ ] Every named framework is spelled and named exactly as in the book.
- [ ] Spot-check per chapter: at least one number, one framework and one example traced back to the page they came from.
- [ ] Numbers keep their context (who, what, when). No rounding that changes the meaning; no sums the book doesn't make. Recompute any arithmetic shown.
- [ ] Nothing was added from memory, other books or the internet. Anything you cannot find in the source is removed.
- [ ] Quotes are word-for-word, in quotation marks, attributed, 25 words or fewer, at most three per chapter.
- [ ] Core frameworks in SKILL.md agree with the chapter pages they cite.
- [ ] Chapter and topic indexes point to the chapters that actually cover each topic.
- [ ] Glossary, patterns and cheatsheet agree with the chapter pages (same names, same numbers, same chapter references).

## 2. Copyright
- [ ] No passage is a close paraphrase that tracks the book sentence by sentence. Rewrite it in your own structure.
- [ ] No reproduced tables, diagrams, worksheets or exercises in full; summarise what they do.
- [ ] README says the files are study notes, not the book's text, and that the skill stays private.
- [ ] The source file itself is not inside the skill folder.

## 3. Appropriateness
Flag anything that, if Claude followed the skill literally, could mislead or harm someone.
- [ ] **Author's results as promises**: income, growth, weight-loss or conversion figures framed as what the reader will get. Reframe as "the author reports".
- [ ] **Advertising and consumer law (UK)**: tactics the book recommends that would breach the CAP Code or the Digital Markets, Competition and Consumers Act 2024, including:
  - false or invented scarcity or urgency ("only 3 left", countdowns that reset)
  - fake, bought or undisclosed incentivised reviews and testimonials
  - guarantees with hidden conditions, or "risk-free" claims that aren't
  - fake reference prices or "was/now" discounts, and drip pricing
  - pressure selling or exploiting vulnerable people
  Keep the idea where an honest version exists (real capacity limits, real deadlines) and say so in the chapter page; otherwise mark the tactic as not for UK use.
- [ ] **Regulated advice**: health, diet, medical, financial, investment, tax, legal or employment guidance stated as fact. Add the regulated-advice line to Scope & Limits and soften absolute claims.
- [ ] **Children and safeguarding**: anything about working with, marketing to or contacting children or parents is checked against safeguarding norms and the user's organisation's policy. Remove anything that wouldn't pass.
- [ ] **Data protection**: outreach, scraping, list-buying or cold contact tactics noted with a UK GDPR and PECR caution (marketing emails and texts to individuals need consent or a genuine soft opt-in).
- [ ] **Offensive or exclusionary content**: slurs, stereotypes, discriminatory hiring or targeting advice, crude language. Paraphrase neutrally or leave out; don't repeat it in quotes.
- [ ] **Real people**: named individuals in case studies are described only as the book describes them; no added claims about them.
- [ ] **Dated content**: platform rules, ad policies, laws or prices the book states that may have changed. Mark them "as of the book's publication".

## 4. Structure and quality
- [ ] `check_skill.py` passes with no ERRORs.
- [ ] Description names the book, author and main frameworks, and reads as a trigger, not a blurb.
- [ ] SKILL.md stays under about 500 lines.
- [ ] UK spelling throughout; plain words; no filler.
- [ ] Each "Worked Example" is either from the book (attributed) or clearly labelled "Illustration (not from the book)".

## Check report (give this to the user)
```
Content check — <skill-name> — <date>
Checked: <sections 1–4, N chapters, N spot-checks>
Changed: <one line per change>
Open, needs your call: <one line each, or "nothing">
```
