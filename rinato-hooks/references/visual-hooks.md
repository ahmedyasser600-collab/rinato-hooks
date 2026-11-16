# Visual hooks: what is on frame 0

On mute (most people scroll on mute), the first frame and the first second of motion are the
whole hook. These formats come from what keeps working in viral short-form video. They are
**formats**: a way of opening. Borrow the format, build it from scratch in your brand, and
never copy anyone's footage, framing, graphics, colour grade or edit beat-for-beat.

Rules for every format:
- Something is already moving, or already mid-action, on frame 0. A fade from black wastes
  the 0.3–0.5 s that decide the scroll.
- One thing to look at, centred in the 4:5 box. No collage.
- Hook text straight (never tilted), inside the safe zone (roughly y 288–1536 on a 1080×1920
  frame), in your brand fonts and colours, big enough to read at phone size (aim ≥ 72 px cap height).
- No footage? Type, objects, UI screens and simple 3D objects are enough for every format below.
- Sound design helps (a hit on the text slam, a cut on the interrupt), but the hook must
  not need it.

## The formats

| Format | Frame 0 | Good for | How to build it (any editor, or code) |
| --- | --- | --- | --- |
| **Text slam** | The hook text is already on screen at full size on frame 0, landing with a scale/skew-free punch (no tilt) and a hit. Background moves underneath. | `number`, `contrarian`, `dont` | Scale 1.15 → 1 over 4–6 frames with a hard ease-out, starting at frame 0, readable by frame 2. |
| **Mid-motion object** | A surprising object already in motion: a stamp card tearing, a key spinning toward camera, a tile falling. | `interrupt`, `dont` | A cut-out object (PNG or 3D) on a motion path, a little motion blur. |
| **Before / after split** | Screen split or wipe already halfway: the bad version vs the fixed one (paper card vs phone wallet card, old site vs new site, raw bathroom vs finished). | `wrong`, `number` | A clip-path wipe already at 40–60% on frame 0, finishing by 0.8 s. Never start at 0%. |
| **Payoff first** | Open on the finished result (the full stamp card, the booked calendar, the finished room), then rewind. | story films, `number` | Freeze on the result 0.6 s, then a rewind sweep (time-reverse of the build) into the setup. |
| **Counter / clock** | A big number already counting or ticking (02:14, 9 calls, 0 → 10 stamps). | `number`, `interrupt` | A count-up with tabular (fixed-width) digits so the number doesn't jitter. |
| **Wrong thing on screen** | A UI or object behaving wrong: a loading bar going backwards, a 404, a "CHIUSO" sign flipping at noon, a shredder. | `interrupt` | UI mock in HTML/CSS (no real company UI copied), state change at 0.2–0.5 s. |
| **Zoom punch** | Frame 0 is a tight crop on a detail (a price, a stamp, a crack), punching out to reveal the context by 1 s. | `question`, `contrarian` | Punch-out: start scale 2.2, end 1.0, by 0.9 s. |
| **POV / point-of-use** | The viewer's view of the moment of pain: a phone screen with a listing, a counter with a paper card. The screen or object fills the frame. | `question`, `wrong` | Phone frame component, content scrolling on frame 0. |

## Borrowing a format from a viral video

1. Find 2+ videos from different creators that open the same way (search the platform for your topic). One video is an accident; two creators is a format.
2. Write the format as a blank template in plain words: "frame 0: [everyday object] already
   breaking; 0.4 s: text names the loss; 1.2 s: cut to the fix."
3. Fill the template with your pain point, your objects, your brand. If you could put the two
   videos side by side and someone would say "that's a copy", change it.
4. Note the source format in the hooks file (`fact:` line or a comment) so you can see
   where it came from.

## What fails on frame 0 (rejected by the checklist)

- Your logo as the subject; an end-card-style title; a brand intro.
- Black, a slow fade-in, a slow push-in on a still, an establishing shot of a calm place
  (a quiet café shot). Calm can come *after* the hook, as contrast.
- A frame that only makes sense once you hear the voice.
- Small text, text that needs more than one read, text that changes before it can be read.
