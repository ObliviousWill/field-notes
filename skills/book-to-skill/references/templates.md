# Templates

Copy these shapes exactly. `check_skill.py` looks for the headings marked `<!-- required -->`; leave those markers out of the files you write.

## Generated SKILL.md

```markdown
---
name: <skill-name>
description: "Knowledge base from \"<Full Title>\" by <Author>. Use when applying <Author>'s frameworks for <framework 1>, <framework 2>, <job 1>, <job 2>…, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# <Full Title>
**Author**: <Author> (<edition/year>) | **Words**: ~<N>K | **Chapters**: <N> | **Generated**: <YYYY-MM-DD>

## How to Use This Skill
- **Without arguments**: use the core frameworks below.
- **With a topic**: find the topic in the Topic Index and read that chapter before answering.
- **With a chapter**: load that chapter file.
- **Applying it**: apply the frameworks to the user's situation and show the steps; don't just repeat the book back.

Read the relevant chapter file before answering any "how do I actually do this?" question.

---

## Core Frameworks & Mental Models
### 1. <Framework>
<3–6 sentences in plain words, the author's named terms in bold.> (Ch N)
…

---

## Chapter Index
| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-<slug>.md) | <Title> | <frameworks> |

## Topic Index
- **<Topic>** → ch03, ch07

## Supporting Files
- [glossary.md](glossary.md): key terms
- [patterns.md](patterns.md): techniques and patterns
- [cheatsheet.md](cheatsheet.md): decision rules, pickers and thresholds

---

## Scope & Limits   <!-- required -->
This skill covers this book's content only. <Related skills and what they cover.> Figures and case studies are the author's own reported results, not promises or typical outcomes.
<Marketing line, if relevant> Before using any claim, guarantee, price comparison, scarcity, urgency, testimonial or review tactic in the UK, check it against the CAP Code (non-broadcast advertising) and the Digital Markets, Competition and Consumers Act 2024 (unfair commercial practices, fake reviews and drip pricing). False scarcity or urgency is banned outright.
<Regulated-advice line, if relevant> This is not <medical / financial / legal / safeguarding> advice; check anything that affects people's health, money, legal position or children with a qualified person or the relevant policy.
```

## Chapter page

```markdown
# Chapter N: <Title>

## Core Idea            <!-- required -->
<2–4 sentences: what the chapter argues and why it matters.>

## Frameworks Introduced   <!-- required -->
- **<Name>**: <what it is and how it works.>

## Key Concepts
- **<Concept>**: <one or two sentences.>

## Mental Models
- **<Rule of thumb>**

## Anti-patterns
- **<Mistake>**: <why it fails.>

## Worked Example      <!-- required -->
<The author's example, paraphrased, with numbers kept in context and attributed. Or one clearly labelled "Illustration (not from the book)" if the chapter has none.>

## Key Takeaways        <!-- required -->
1. <Action-shaped takeaway.>

## Connects To
- **Ch N**: <how.>
```

## glossary.md
```markdown
# Glossary — <Short Title>

**<Term>** — <definition in one line.> (Ch N)
```

## patterns.md
```markdown
# Patterns & Techniques — <Short Title>

## <Pattern>
**When to use**: …
**How**: … (Ch N)
**Trade-offs**: …
```

## cheatsheet.md
```markdown
# Cheatsheet — <Short Title>

## Diagnose first
- <Symptom> → <where to look>.

## Decision rules
| When… | Do… | Because… |
|---|---|---|

## <Picker or quick score>
```

## README.md
```markdown
# <skill-name>

A private Claude skill built from *<Full Title>* by <Author>. <One sentence on what it gives Claude.>

**These are synthesised study notes, not the book's text.** Keep this skill private: the source is a copyrighted book. If you find it useful, buy the book.

## Install
Upload `<skill-name>.skill` in Claude, or copy this folder into `~/.claude/skills/<skill-name>/`.

## Files
- `SKILL.md`: core frameworks, chapter index and topic index
- `chapters/`: <N> chapter summaries
- `glossary.md`, `patterns.md`, `cheatsheet.md`

## Content check
Checked on <YYYY-MM-DD>: <one line on what was checked and anything left open>.
```
