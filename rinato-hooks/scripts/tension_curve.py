#!/usr/bin/env python3
"""Map a script's beats onto the Modern Story Arc tension curve (0-100) and check its shape.

  python -X utf8 tension_curve.py beats.txt [--end 35]
  python -X utf8 tension_curve.py --blocks script.md [--wps 2.8]

Beats file: one beat per line, `<time> <beat>[:<tension>] <what happens>`; time in seconds or m:ss.
  0.0  hook        Frame 0: cards already sliding into a bin. "Non ristampare le tessere timbro."
  3.0  peak        "Era al timbro 8. Riparte da zero."
  6.0  release:60  The lost card under a car seat.
  end  35
A bare number works as the beat too (`3.0 92 ...`). Lines starting with # are ignored.

Blocks mode reads a block-structured script (## Hook, ## Lock-in, ## Body 1, ## Rehook 1, ...), times
each block from its spoken words, and maps Hook->hook, Lock-in->peak, Body->release, Rehook->twist,
Closing->callback, CTA->cta. Override any block with a note line `> beat: payoff` or `> tension: 90`.

Checks (from Kallaway's Modern Story Arc, see references/source-modern-story-arc.md):
  HARD  slow open: the first beat isn't at 0 s or starts below 70
  HARD  first peak (>= 85) later than 6 s   (soft if between 5 and 6 s)
  HARD  a flat stretch: more than 15 s between peaks, or from the last peak to the end
  soft  only one peak (a single climax), or no release below 70 at all (peak-release rhythm)
"""
import argparse, re, sys

DEFAULT = {'hook': 70, 'peak': 90, 'twist': 90, 'turn': 90, 'stat': 90, 'contrast': 90,
           'setup': 60, 'release': 55, 'body': 55, 'payoff': 95, 'callback': 85,
           'cta': 60, 'logo': 60, 'rehook': 90, 'lock-in': 90, 'lockin': 90, 'closing': 85}
PEAK = 85
BLOCK_BEAT = [(r'^hook', 'hook'), (r'^lock', 'peak'), (r'^body', 'release'),
              (r'^re-?hook', 'twist'), (r'^clos', 'callback'), (r'^cta', 'cta')]


def secs(s):
    if ':' in s:
        m, x = s.split(':', 1)
        return int(m) * 60 + float(x)
    return float(s)


def tension_of(tok):
    if re.fullmatch(r'\d+(\.\d+)?', tok):
        return 'beat', float(tok)
    name, _, val = tok.partition(':')
    name = name.lower()
    if val:
        return name, float(val)
    if name not in DEFAULT:
        sys.exit(f'unknown beat "{tok}" (use {", ".join(sorted(DEFAULT))} or a number)')
    return name, DEFAULT[name]


def read_beats(path):
    beats, end = [], None
    for raw in open(path, encoding='utf-8'):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(None, 2)
        if parts[0].lower() == 'end':
            end = secs(parts[1])
            continue
        if len(parts) < 2:
            continue
        name, t = tension_of(parts[1])
        beats.append((secs(parts[0]), name, t, parts[2] if len(parts) > 2 else ''))
    return sorted(beats), end


def read_blocks(path, wps):
    blocks, cur = [], None
    for raw in open(path, encoding='utf-8'):
        m = re.match(r'^##\s+(.+?)\s*$', raw)
        if m:
            cur = {'name': re.sub(r'\(.*?\)', '', m.group(1)).strip(), 'text': '', 'over': None}
            blocks.append(cur)
            continue
        if cur is None:
            continue
        n = re.match(r'^\s*>\s*(beat|tension)\s*:\s*(\S+)', raw, re.I)
        if n:
            cur['over'] = n.group(2)
        elif not raw.lstrip().startswith('>'):
            cur['text'] += raw
    beats, t = [], 0.0
    for b in blocks:
        name = next((beat for rx, beat in BLOCK_BEAT if re.match(rx, b['name'], re.I)), 'release')
        label, tension = tension_of(b['over'] or name)
        first = b['text'].strip().splitlines()[0] if b['text'].strip() else ''
        beats.append((round(t, 1), f"{label} ({b['name']})", tension, first[:70]))
        t += len(re.findall(r"[\w'’]+", b['text'])) / wps
    return beats, round(t, 1)


def check(beats, end):
    hard, soft = [], []
    if not beats:
        return ['no beats found'], soft
    end = end if end is not None else beats[-1][0] + 3
    t0, _, v0, _ = beats[0]
    if t0 > 0.5 or v0 < 70:
        hard.append(f'slow open: first beat at {t0}s with tension {v0:g} (start at 0 s and >= 70, mid-story)')
    peaks = [b[0] for b in beats if b[2] >= PEAK]
    if not peaks:
        hard.append('no peak at all (nothing reaches 85)')
        return hard, soft
    if peaks[0] > 6:
        hard.append(f'first peak at {peaks[0]}s (aim ~5 s, never later than 6 s)')
    elif peaks[0] > 5:
        soft.append(f'first peak at {peaks[0]}s (aim for 5 s or sooner)')
    marks = peaks + [end]
    for a, b in zip(marks, marks[1:]):
        if b - a > 15:
            where = 'to the end' if b == end else f'to the next peak at {b}s'
            hard.append(f'flat stretch: {b - a:.1f}s from the peak at {a}s {where} (max 15 s)')
    if len(peaks) == 1:
        soft.append('only one peak: stack mini-peaks every 10-15 s instead of one climax')
    if not any(b[2] < 70 for b in beats[1:]):
        soft.append('no release below 70 anywhere: peak, release, peak, release')
    return hard, soft


def draw(beats, end):
    print('time   tension  curve (| = 70, ! = peak)')
    for t, name, v, what in beats:
        bar = '#' * int(v / 4)
        bar = (bar[:17] + '|' + bar[18:]) if len(bar) > 17 else bar
        mark = ' !' if v >= PEAK else '  '
        print(f'{t:5.1f}s  {v:5.0f}  {bar:<26}{mark} {name}: {what}')
    print(f'{end:5.1f}s  end')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('beats', nargs='?')
    ap.add_argument('--blocks')
    ap.add_argument('--wps', type=float, default=2.8)
    ap.add_argument('--end', type=float)
    a = ap.parse_args()
    if a.blocks:
        beats, end = read_blocks(a.blocks, a.wps)
    elif a.beats:
        beats, end = read_beats(a.beats)
    else:
        ap.error('give a beats file or --blocks script.md')
    end = a.end if a.end is not None else end
    end = end if end is not None else (beats[-1][0] + 3 if beats else 0)
    draw(beats, end)
    hard, soft = check(beats, end)
    for h in hard:
        print('HARD ', h)
    for s in soft:
        print('soft ', s)
    print('CURVE PASS' if not hard else 'CURVE REWRITE')
    sys.exit(0 if not hard else 1)


if __name__ == '__main__':
    main()
