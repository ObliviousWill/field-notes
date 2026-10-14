---
title: 'I cloned my voice to read my blog'
description: "Every post and guide on this site now has an audio version, read by an AI version of my voice. How I did it, what it cost, what I had to fix, and where I drew the line."
pubDate: 'Oct 14 2026'
audio: '/blog/audio/i-cloned-my-voice.mp3'
tags: ['building', 'ai']
mentions:
  - field-notes
---

Press play at the top of this post and you'll hear me reading it. Except it isn't me. It's an AI copy of my voice.

I wanted audio versions because plenty of people would rather listen than read: on a walk, in the car, or because reading a screen is hard work for them. Recording every post myself, and re-recording every time I changed a word, wasn't going to happen. So I got AI to do it.

## Version one: a free AI voice

I started with a free, open-source voice model called Kokoro. It runs on an ordinary computer, costs nothing, and comes with a handful of British voices. I picked one called George.

It worked, and it was a useful first step. But listening back, two things bothered me. It wasn't my voice, on a site that's very much me. And it read things it shouldn't, because I'd simply fed it the page.

## Version two: my own voice

For the second version I used ElevenLabs, a voice service that can clone a voice from a recording. The process was simpler than I expected:

1. **Record a sample.** A few minutes of you reading naturally, in a quiet room, at your normal pace.
2. **Make the clone.** Upload the recording to ElevenLabs, and it creates a voice that sounds like you.
3. **Turn each post into speech.** Claude wrote a small script that takes each post, prepares the text, sends it to ElevenLabs in my voice, and saves the audio file next to the post.

That last step is where most of the work went.

## The fiddly bit: text isn't speech

A web page is written to be looked at, not listened to. Read it out word for word and it sounds odd. So the script prepares each post first:

- **Headings get a pause** after them, so you can hear a new section start.
- **Tables are read as sentences.** A table makes sense to the eye. Read cell by cell, it's gibberish. So "Delegation | Is this the right job for AI?" becomes "Delegation: is this the right job for AI?"
- **Symbols are spelled out.** £100 becomes "100 pounds". Number ranges like "4–5" become "4 to 5".
- **On-screen tools are skipped.** Several guides have interactive exercises. You can't use those when you're listening, so the script leaves them out, along with the line that introduces them.
- **Long posts are sent in chunks**, each one carrying a little of the text either side, so the voice keeps its rhythm across the joins.

<aside class="margin-note">Always build in a retry.</aside>

The first run in my voice cut out partway through the longest post when the connection dropped. So the script now retries automatically.

## What it cost

Voice services charge by the number of characters they read. Every post and guide on the site came to roughly 68,000 characters. That fits within a paid monthly plan, but it isn't free, so it's worth checking your allowance before you voice a whole site at once. The free Kokoro version cost nothing at all.

## Where I drew the line

<aside class="margin-note">The most important part of this post.</aside>

A cloned voice is powerful, and it's easy to use it badly. My rules:

- **Always say it's AI.** Every player on this site says "read by an AI version of my voice". People who know me would notice if it isn't quite me, and they deserve to know why.
- **Only ever my own voice.** Cloning someone else's voice without their clear permission is a line I won't cross.
- **Keep the key safe.** A voice service gives you a private key, like a password, that lets anyone use your account, and your voice. Keep it out of shared documents, chats and code you publish. If one ever slips out, delete it and make a new one.
- **Check the result.** I listened back to a sample before voicing everything. The AI version of me is good, but it's not perfect, and you only find that out by listening.

## Version three: a professional clone

The quick clone works from a few minutes of audio. ElevenLabs also offers a professional clone, which is trained on a much longer recording and takes longer to make. Once mine was ready, I swapped it in and re-voiced every post and guide with the same script. Changing voice was one setting.

## Would I recommend it?

If you write regularly and your audience might rather listen, yes. Start with a free voice to see whether anyone presses play. Clone your own voice if your writing is personal enough that it should sound like you.

And be honest about it. The point of an audio version is to make your writing easier to take in, not to trick anyone into thinking you sat in a studio reading it.
