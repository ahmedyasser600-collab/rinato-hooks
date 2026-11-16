# From hook to ending: the Modern Story Arc

Core framework: Kane Kallaway's Modern Story Arc (credit and limits in
`source-modern-story-arc.md`). The classic arc starts at zero and climbs slowly to one climax in
the middle. Short-form viewers leave before the climb. So draw the video as a **tension curve
from 0 to 100** and shape it like this:

```
100 |      P1          P2           P3        P4(payoff)
 90 |     /\          /\           /\         /\  callback
 70 |____/  \        /  \         /  \       /  \__/\
 50 |        \______/    \_______/    \_____/        \ CTA
    0s   ~5s        10–15 s later  …         end
    ^ open at 70: already mid-story
```

- **Open at 70.** Frame 0 drops the viewer into something already happening (the hook).
- **First peak (90) within ~5 s.** A contrast, a contrarian take or a hard number. Often this is
  the hook's second line or the lock-in.
- **Release, then peak again every 10–15 s.** A release is a calmer beat that explains or shows
  (50–65). A peak is a new jolt: a twist, a number, a reveal, a before/after, a turn.
- **No single climax in the middle.** Stack mini-peaks. The payoff is the last and biggest one,
  and the callback ending lands right on it.

The ending still matters: the hook makes a promise, and the last peak pays it back in a way the
viewer recognises. A hook the ending forgets feels like clickbait. A hook the ending answers gets
rewatched, because the last frame sends you back to the first.

## Beat types and their tension

These are the defaults `scripts/tension_curve.py` uses when a beat has no number.

| Beat | Tension | What it is | Usual place |
| --- | --- | --- | --- |
| `hook` | 70 | Already mid-story on frame 0 | Hook |
| `peak` | 90 | Contrast, contrarian take, shocking (true) number | Lock-in, Rehook |
| `twist` | 90 | "But…", the thing nobody checks, a reversal | Rehook |
| `turn` | 90 | The fix arrives; mark it with a visual change | Body start |
| `setup` | 60 | Shows the hook's situation as a moment | Lock-in |
| `release` / `body` | 55 | Explains or shows; the viewer breathes | Body |
| `payoff` | 95 | The result, shown, with proof | Body 3 / Closing |
| `callback` | 85 | The hook's image, word or number, now changed | Closing |
| `cta` / `logo` | 60 | One ask, lockup grows out of the callback | CTA |

## The map for a 25–45 s video

| Time | Beat | Job | Tie to the hook |
| --- | --- | --- | --- |
| 0–2 s | hook (70) | Stop the scroll, make the promise | — |
| 2–5 s | peak 1 (90) | Contrast or number that proves the stakes | Raises the hook's stake right away |
| 5–12 s | release | Setup as a moment: what it costs, who it hits | Proves the hook is real |
| ≤ 17 s | peak 2 (90) | Twist or turn: the fix appears | Starts answering the hook |
| release | body | How it works, shown | — |
| ≤ 30 s | peak 3 (90–95) | Payoff with proof | Answers the hook fully |
| last 2–4 s | callback (85) → CTA | Hook image returns, changed; logo grows out of it | Closes the loop |

Shorter films (15–20 s) can be hook → peak → release → payoff/callback. Longer ones add a peak
every 10–15 s. Never let 15 s pass between peaks.

## Callback patterns

- **Same object, new state.** Frame 0: a paper card tears. Ending: the same card shape, now a
  wallet card, gets its 10th stamp and becomes your logo.
- **Same number, new meaning.** Frame 0: "02:14, negozio chiuso". Ending: "02:14, prenotazione
  confermata."
- **The question, answered on screen.** Frame 0: "Quanti tecnici hai chiamato?" Ending: "Uno."
- **The warning, obeyed.** Frame 0: "Non ristampare le tessere." Ending: the print button greyed
  out, the QR on the counter instead.
- **Before/after closes.** A split that opened at 50% closes fully on the "after".

The callback also keeps endings fresh: each one grows out of that video's own hook, instead of
the same black logo end card every time.

## Worked example (a café loyalty card, `dont` hook)

```
0.0  hook     Frame 0: paper stamp cards already sliding off a counter into a bin. "Non ristampare le tessere timbro."
3.0  peak     "La tua cliente migliore era al timbro 8. Riparte da zero."
6.0  release  The lost card: under a car seat, in a washing machine.
14.0 turn     The QR on the counter. One scan, the card is in the phone.
18.0 release  Stamp shows live, reward unlocks.
27.0 payoff   Dashboard: who came back this week.
32.0 callback The bin from frame 0, empty. The QR card lands where the paper stack was.
35.0 cta      the logo grows from the QR's corner.
```

Run it: `python -X utf8 scripts/tension_curve.py beats.txt`. Peaks at 3, 14, 27 and 32 s keep
every gap under 15 s.

## Check before handing off

- Does frame 0 start at 70 (already in motion, mid-story)?
- Is there a 90 peak by ~5 s?
- Is the longest gap between peaks ≤ 15 s? (the checker measures it)
- Can you say in one sentence how the last 3 seconds answer the first 2?
