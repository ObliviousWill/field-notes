#!/usr/bin/env python3
"""Automatic content check for a skill built from a book.

Usage: python3 check_skill.py <skill-folder>

ERRORs must be fixed before packaging. WARNINGs must be read and either
fixed or explained in the check report. Exit code 1 if any ERROR.
"""

import re
import sys
from pathlib import Path

import yaml

REQUIRED_FILES = ["SKILL.md", "glossary.md", "patterns.md", "cheatsheet.md"]
CHAPTER_HEADINGS = ["Core Idea", "Key Takeaways"]
# Thin chapters (a thank-you, a request for reviews) may leave these out.
CHAPTER_HEADINGS_USUAL = ["Frameworks Introduced", "Worked Example"]
SOURCE_EXTS = {".pdf", ".epub", ".mobi", ".azw", ".azw3", ".docx", ".doc", ".txt"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
PLACEHOLDER_RE = re.compile(r"<!-- required -->|<[A-Z][^<>\n]{0,50}>|<[a-z]+(?:-[a-z]+)+>|<YYYY-MM-DD>|<N>")
QUOTE_RE = re.compile(r"[\"“]([^\"”\n]{3,})[\"”]")
CHAPTER_FILE_RE = re.compile(r"^ch(\d{2,3})-[a-z0-9-]+\.md$")

# Phrases that are fine when describing the book, but need a human look
# because Claude may repeat them as advice or as claims.
RISKY = [
    (r"\bguaranteed (results|income|returns|to)\b", "absolute result claim"),
    (r"\brisk[- ]free\b", "'risk-free' claim (CAP Code)"),
    (r"\bonly \d+ (left|spots?|places?)\b", "scarcity claim: must be real (DMCC Act 2024)"),
    (r"\b(fake|invented|made[- ]up) (scarcity|urgency|deadline|reviews?|testimonials?)\b", "fake scarcity/urgency/reviews"),
    (r"\b(buy|pay for|incentivi[sz]e[ds]?) (reviews|testimonials)\b", "incentivised reviews (DMCC Act 2024)"),
    (r"\bcountdown timers?\b", "countdown timer: must be real"),
    (r"\byou will (make|earn|lose)\b", "outcome promised to reader"),
    (r"\b(cure|cures|treats?) (anxiety|depression|cancer|diabetes|disease)\b", "medical claim"),
    (r"\b(scrape|scraping|buy(ing)? (a )?lists?)\b", "data protection (UK GDPR / PECR)"),
    (r"\b(children|pupils|minors|under-18s?)\b", "children mentioned: check safeguarding"),
]
OUTDATED = [
    (r"\bthe CPRs?\b|\bCPRs\b|Consumer Protection from Unfair Trading", "CPRs were replaced by the DMCC Act 2024 from 6 April 2025"),
]
US_SPELLINGS = [
    "optimize", "optimization", "organize", "organization", "prioritize", "monetize",
    "maximize", "minimize", "analyze", "behavior", "color", "favorite", "center",
    "program ", "catalog ", "license ", "practice ", "fulfill ",
]
MARKETING_WORDS = re.compile(r"\b(scarcity|urgency|guarantee|testimonial|discount|advert|lead magnet|offer)\b", re.I)
REGULATED_WORDS = re.compile(r"\b(diet|weight loss|medical|invest|tax|legal|lawsuit|mortgage|pension|therapy)\b", re.I)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


NEGATED_RE = re.compile(r"\b(never|don't|do not|avoid|not|no|fake)\b", re.I)


def strip_frontmatter(text):
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def check_structure(root, r):
    for f in REQUIRED_FILES:
        if not (root / f).exists():
            r.error(f, "missing")
    if not (root / "README.md").exists():
        r.warn("README.md", "missing: add one with the study-notes and keep-private note")
    skill_mds = [p for p in root.rglob("SKILL.md") if "__pycache__" not in p.parts]
    if len(skill_mds) > 1:
        r.error("SKILL.md", f"{len(skill_mds)} SKILL.md files found; a skill must have exactly one")
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in SOURCE_EXTS:
            r.error(str(p.relative_to(root)), "looks like a source file; the book must not ship inside the skill")

    skill = root / "SKILL.md"
    if not skill.exists():
        return
    text = skill.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        r.error("SKILL.md", "missing or invalid YAML frontmatter")
        return
    name, desc = fm.get("name"), fm.get("description")
    if not name or not NAME_RE.match(str(name)) or len(str(name)) > 64:
        r.error("SKILL.md", f"name '{name}' must be lowercase-hyphenated, 64 chars max")
    elif name != root.name:
        r.error("SKILL.md", f"name '{name}' does not match folder '{root.name}'")
    if not desc:
        r.error("SKILL.md", "description missing")
    else:
        if len(desc) > 1024:
            r.error("SKILL.md", f"description is {len(desc)} chars; max 1024")
        if "<" in desc or ">" in desc:
            r.error("SKILL.md", "description contains angle brackets")
    if "## Scope & Limits" not in text:
        r.error("SKILL.md", "no '## Scope & Limits' section")
    if len(text.splitlines()) > 500:
        r.warn("SKILL.md", f"{len(text.splitlines())} lines; aim for under 500")


def check_chapters(root, r):
    chdir = root / "chapters"
    if not chdir.is_dir():
        r.error("chapters/", "missing")
        return []
    files = sorted(p for p in chdir.glob("*.md"))
    nums = []
    for p in files:
        m = CHAPTER_FILE_RE.match(p.name)
        if not m:
            r.warn(f"chapters/{p.name}", "name should be chNN-short-slug.md")
            continue
        nums.append(int(m.group(1)))
        text = p.read_text(encoding="utf-8")
        for h in CHAPTER_HEADINGS:
            if not re.search(rf"^## {re.escape(h)}\b", text, re.M):
                r.error(f"chapters/{p.name}", f"missing '## {h}'")
        for h in CHAPTER_HEADINGS_USUAL:
            if not re.search(rf"^## {re.escape(h)}\b", text, re.M):
                r.warn(f"chapters/{p.name}", f"no '## {h}' (fine only for a thin chapter)")
        if not text.lstrip().startswith("# "):
            r.warn(f"chapters/{p.name}", "should start with '# Chapter N: Title'")
    if nums:
        missing = sorted(set(range(min(nums), max(nums) + 1)) - set(nums))
        if missing:
            r.warn("chapters/", f"numbering gaps: {missing}")
    skill = root / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        for p in files:
            if f"chapters/{p.name}" not in text:
                r.error("SKILL.md", f"chapter index does not link chapters/{p.name}")
    return files


def check_links(root, md_files, r):
    for p in md_files:
        text = strip_code(p.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            if re.match(r"^[a-z]+:", target):
                continue
            if not (p.parent / target).resolve().exists():
                r.error(str(p.relative_to(root)), f"broken link '{target}'")


def check_content(root, md_files, chapter_files, r):
    all_text = ""
    for p in md_files:
        rel = str(p.relative_to(root))
        raw = p.read_text(encoding="utf-8")
        text = strip_code(strip_frontmatter(raw))
        all_text += text + "\n"

        for m in PLACEHOLDER_RE.finditer(text):
            r.error(rel, f"template placeholder left in: {m.group(0)}")

        long_quotes = 0
        for q in QUOTE_RE.findall(text):
            words = len(q.split())
            if words > 25:
                r.warn(rel, f"quote of {words} words (max 25): \"{q[:60]}…\"")
            if words >= 8:
                long_quotes += 1
        if p in chapter_files and long_quotes > 3:
            r.warn(rel, f"{long_quotes} quotes of 8+ words (max 3 per chapter)")

        for n, line in enumerate(text.splitlines(), 1):
            for pat, why in RISKY:
                # A line warning against the tactic is what we want, not a problem.
                if re.search(pat, line, re.I) and not NEGATED_RE.search(line):
                    r.warn(f"{rel}:{n}", f"{why} — \"{line.strip()[:90]}\"")
            for pat, why in OUTDATED:
                if re.search(pat, line, re.I):
                    r.warn(f"{rel}:{n}", f"{why} — \"{line.strip()[:90]}\"")
            low = line.lower()
            for w in US_SPELLINGS:
                if w in low:
                    r.warn(f"{rel}:{n}", f"US spelling '{w.strip()}'")

    skill = root / "SKILL.md"
    if not skill.exists():
        return
    scope = skill.read_text(encoding="utf-8").split("## Scope & Limits", 1)
    scope = scope[1] if len(scope) > 1 else ""
    if not re.search(r"author'?s? own|author reports|illustrative", scope, re.I):
        r.warn("SKILL.md", "Scope & Limits should say figures are the author's own, not promises")
    if MARKETING_WORDS.search(all_text) and not (
        re.search(r"CAP Code", scope) and re.search(r"Digital Markets|DMCC", scope)
    ):
        r.warn("SKILL.md", "book covers marketing: Scope & Limits needs the CAP Code and DMCC Act 2024 line")
    if REGULATED_WORDS.search(all_text) and not re.search(r"not .{0,40}advice", scope, re.I):
        r.warn("SKILL.md", "book touches health/money/law: Scope & Limits needs the regulated-advice line")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"Not a folder: {root}")
        sys.exit(2)
    r = Report()
    check_structure(root, r)
    chapter_files = check_chapters(root, r)
    md_files = sorted(root.rglob("*.md"))
    check_links(root, md_files, r)
    check_content(root, md_files, chapter_files, r)

    print(f"Content check: {root.name}")
    print(f"  {len(md_files)} files, {len(chapter_files)} chapters")
    print(f"\nERRORS ({len(r.errors)})")
    for e in r.errors:
        print(f"  - {e}")
    print(f"\nWARNINGS ({len(r.warnings)})")
    for w in r.warnings:
        print(f"  - {w}")
    print("\nAutomatic checks only. Now do the read-through in references/content-check.md.")
    sys.exit(1 if r.errors else 0)


if __name__ == "__main__":
    main()
