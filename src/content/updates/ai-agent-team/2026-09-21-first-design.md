---
project: 'ai-agent-team'
title: 'First design: one long production line'
pubDate: 'Sep 21 2026'
---

The first version worked like a production line, with seven stages. One helper looked at the numbers, another researched, another planned, and so on down the line.

It worked, but it was slow and hard to follow. When you wanted to know why a suggestion had been made, you had to trace it back through seven steps.

One principle from that version stayed: **the helper that does the work shouldn't be the one that checks it.** It's the same reason we ask a colleague to proofread rather than proofreading our own writing. So the current design has a separate checker, which can't edit anything. It can only pass work, or send it back with reasons.
