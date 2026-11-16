---
name: rinato-hooks
description: >-
  Write and check the hook (the first 1–3 seconds) of a short vertical video (Reels, TikTok,
  Shorts) before anything else is written: 3 scored hook options, each a spoken line, on-screen
  text, a frame-0 visual and the ending it sets up, with a checker that rejects weak hooks and a
  second checker that maps the whole script onto a tension curve (Kane Kallaway's Modern Story
  Arc: open at 70/100, first peak within ~5 s, a new peak every 10–15 s, callback ending). Covers
  six hook types, a 100-formula hook library, visual hook formats and the hard rules (no logo or
  slow fade on frame 0, promise within 1.5 s, text and voice say the same, works on mute). Use it
  whenever someone plans a reel or short, asks for a hook or an opening, says "my videos get no
  views", "nobody watches past the first seconds", "the intro is slow", or wants a script paced so
  people stay, even if they never say "hook".
---

# rinato-hooks: the first 1–3 seconds

Reels and TikTok show a new video to a small test audience first and only push it further if
those people stop and stay. A slow first second means almost no reach, however good second 20
is. We learned it on our own work: one of our reels opened on a calm café shot with a quiet
voice-over. It looked nice, promised nothing, and got no views. This skill exists so that no
video is made before its opening earns the stop.

**Core framework: the Modern Story Arc** (Kane Kallaway, see
`references/source-modern-story-arc.md`). Draw the video as a tension curve from 0 to 100.
Open at 70, already in the middle of something. Spike to a first peak at 90 within about 5 s
(a contrast, a contrarian take, a hard number). Then release and peak again every 10–15 s,
stacking mini-peaks instead of one climax in the middle. The hook is the 70 start;
`references/arc.md` maps the rest.

**The rule:** every video starts from **3 hook options**, scored, and the user picks one
*before* the rest of the script is written or anything is filmed or built.

## The loop

1. **One-line brief.** Who scrolls past this (a café owner, a student looking for a room, a
   homeowner…), their one pain point, the one payoff the video delivers, the language. If the
   payoff isn't clear, the hook can't be either: ask.
2. **Facts sheet.** Every number or claim a hook might use, with its source (the user's own
   words, the product, a link). A hook that needs an invented fact is dead. Numbers that are
   true by design are always safe ("1 QR code", "0 apps to download", "4 steps", "02:14").
3. **Draft 6–8 candidates** across at least 4 of the types in `references/hook-types.md`,
   using `references/hooks-database.md` for wording ideas. Each candidate is a *pair*: a spoken
   line and a frame-0 visual from `references/visual-hooks.md`. A great line over a slow
   picture still fails on mute.
4. **Strip AI phrasing.** Hooks are where it shows most: "Discover the secret…", "It's not X,
   it's Y", slogan endings, triads. Write it the way the user would say it out loud.
5. **Pick the best 3, all different types**, with at least one stop-scroll hook (negation,
   number, question) and, where it fits, one retention hook (a mid-story scene, emotional, or
   the user's own true confession). Write each in the format below, including the callback
   ending it sets up (`references/arc.md`).
6. **Score.** `python scripts/score_hook.py hooks.md` (on Windows add `-X utf8`). Fix every
   HARD fail; rewrite any option under 80. If an option can't pass, replace it with the next
   candidate. Don't game the checker by editing the fields: they describe what will actually be
   on screen.
7. **Show the user** the 3 options as a short table (type · voice · on-screen text · frame 0 ·
   ending · score) and say which you'd pick and why, in one line. Then stop until they pick.
   Their own words always win.
8. **Map the arc.** Once a hook is picked, write the script's beats and run
   `python scripts/tension_curve.py beats.txt` (or `--blocks script.md` for a script with one
   `## Block` heading per part). Fix every HARD: a slow open, a first peak after ~5 s, or more
   than 15 s without a peak. Show the curve with the script.

## The hard checklist (the scorer enforces most of it)

- **Frame 0 is never a logo, a title card, black, or a slow fade.** Something is already
  moving or already surprising on the first frame. A small logo in a corner is fine; it is never
  the subject of the opening.
- **The promise is clear within 1.5 s.** By then the viewer knows the topic and what they get
  or what's at stake (`promise_at`).
- **Voice and on-screen text say the hook together.** Not two different messages.
- **It works with the sound off.** Cover the voice line: does frame 0 plus the text still stop
  you?
- **On-screen hook text ≤ 8 words** (≤ 6 reads faster). Each on-screen line stays fully
  visible at least 1.5 s + 0.3 s per word (`hold`).
- **Spoken hook ≤ 12 words**, under about 3.5 s.
- **Names the gain.** Viewers stop for what they get: more customers, sales, bookings, money,
  views, reach. Promise *how to* get it, truthfully; never an invented result. The ending
  delivers the same gain.
- **Specific:** a number, a named thing, or the viewer's own situation ("your loyalty card",
  "your website"). Generic hooks ("Want more customers?") are rejected.
- **True, and the video pays it off.** The `callback` field says how.
- **Text straight and inside the safe zone** of a 9:16 frame (away from the top bar and the
  caption and buttons at the bottom).

Weak hooks the scorer flags: a greeting or intro ("Hi guys", "Today I'll talk about", "Ciao",
"Oggi vi parlo di"), a vague yes/no question, stock AI or hype words, a promise after 1.5 s,
text that differs from the voice, a frame 0 that only makes sense with sound.

**Question hooks** only work when they name the viewer's concrete situation and they could
answer from their own day: "How many stamps were on the loyalty card you lost?" works; "Want
loyal customers?" doesn't. If in doubt, turn the question into a statement of the same fact.

## Hooks file format (input for the scorer)

```markdown
# Hooks · <video name>
brief: <audience> · <pain point> · <payoff>

## Option A
type: number            # question | dont | wrong | contrarian | number | interrupt | story | emotional | confession
voice: Due timbri gratis, e quasi il doppio dei clienti arriva al premio.
screen: 2 timbri gratis. Il doppio al premio.
frame0: A loyalty card already sliding onto the counter with 2 of 10 stamps filled
promise_at: 1.2
hold: 3.5               # seconds the on-screen text stays fully visible
callback: Ending: the same card gets its 10th stamp and the customer's reward lights up
fact: Nunes & Drèze 2006, Journal of Consumer Research: 34% vs 19% completed
```

`frame0` describes what is literally on screen on the first frame, in plain words. Every
number needs its source in `fact`. A complete scored example is in `examples/`.

## Files

- `references/hook-types.md`: nine hook types, the shape of each, examples (Italian and English).
- `references/hooks-database.md`: 100 hook formulas in 10 triggers (MIT, rediumvex), with
  truth marks and Italian examples.
- `references/visual-hooks.md`: frame-0 formats borrowed from viral videos, and how to borrow a
  format without copying anyone.
- `references/arc.md`: the tension curve, beat types and their default tension, callback
  endings, a worked example.
- `references/source-modern-story-arc.md`: credit and summary of the core framework.
- `scripts/score_hook.py`: scores each option out of 100; checks the set is 3 options of 3 types.
- `scripts/tension_curve.py`: maps beats onto the curve; flags slow opens and flat stretches.
- `examples/hooks-example.md`: a scored set of 3 to copy as a template.
