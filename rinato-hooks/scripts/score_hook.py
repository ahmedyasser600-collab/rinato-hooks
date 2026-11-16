#!/usr/bin/env python3
"""Score hook options (rinato-hooks):  python -X utf8 score_hook.py hooks.md

The file holds "## Option X" sections with `key: value` lines:
  type, voice, screen, frame0, promise_at, hold, callback, fact
(format in SKILL.md). Each option starts at 100; a HARD fail costs 20, a soft flag 5.
An option passes at 80+ with zero HARD fails. The set passes when there are exactly
3 options, of 3 different types, and all of them pass.

The checker catches the mechanical failures. Taste is still yours.
"""
import re, sys

TYPES = {'question', 'dont', 'wrong', 'contrarian', 'number', 'interrupt', 'story', 'emotional', 'confession'}
STOP = {'question', 'dont', 'number', 'contrarian', 'wrong'}
RETAIN = {'story', 'emotional', 'confession'}
FIELDS = ['type', 'voice', 'screen', 'frame0', 'promise_at', 'hold', 'callback']

# Frame 0 must not be a logo card, black, a title card or a slow open.
BAD_FRAME0 = [
    (r'(?i)\b(logo|emblem|lockup|marchio)\b(?!.*\b(corner|angolo|small|piccol))', 'logo as the subject of frame 0'),
    (r'(?i)\b(fade[sd]?[- ]?in|fades? from|dissolve|dissolvenza|from black|da nero|black screen|schermo nero)\b', 'fade / black open'),
    (r'(?i)\b(title card|intro card|cartello|end card)\b', 'title card open'),
    (r'(?i)\bslow (push|zoom|pan|reveal)|lento\b', 'slow open'),
    (r'(?i)\b(establishing|calm|calmo|tranquill|static|statico|still life)\b', 'calm or static open (no motion on frame 0)'),
]
MOTION = r'(?i)\b(already|gi[aà]|mid|slam|slams|lands|landing|falling|cade|tearing|strapp|spinning|sliding|scivol|counting|ticking|crack|shredd|wipe|punch|flip|breaking|moving|crawl|climb|drop|flying|vola|freezes|cuts?)\w*'

WEAK_OPENERS = r'(?i)^(ciao|hey|ehi|salve|oggi|in questo video|benvenut|allora|sapevi che|hi\b|today|in this video|welcome|so,)'
GENERIC_Q = r'(?i)^(vuoi|volete|ti piacerebbe|sei pronto|do you want|want to|are you ready)\b'
AI_WORDS = r'(?i)\b(scopri|svela|il segreto|segreti|rivoluzion\w*|svolta|next level|game[- ]?changer|viaggio|unlock|discover|secret|journey|elevate|seamless|incredibile|pazzesco)\b'
NOT_X_Y = r"(?i)\b(non [eè] solo\b.*\bma\b|non [eè] \w+[^.]*?, [eè]\b|not just\b.*\bbut\b|it'?s not \w+[^.]*?, it'?s)"
NUM = r'\d|\b(zero|uno|una|due|tre|quattro|cinque|sei|sette|otto|nove|dieci|cento|mille|one|two|three|four|five|ten|hundred)\b'
YOU = r"(?i)\b(tu|tuo|tua|tuoi|tue|ti|te|hai|sei|you|your|you're)\b"
BLANK = r'\[[^\]]*\]'
GAIN = r'(?i)\b(soldi|guadagn\w*|incass\w*|fattur\w*|vend\w*|client\w*|prenotazion\w*|ordin\w*|fila|follower|visualizzazion\w*|view\w*|reach|raggiung\w*|famos\w*|notat\w*|ricord\w*|scelg\w*|sceglie|money|earn\w*|sales?|customers?|clients?|bookings?|followers?|famous|revenue|profit\w*|grow\w*|cresc\w*)\b'


def stems(text):
    words = re.findall(r"[\wàèéìòù%']+", text.lower())
    return {w[:5] for w in words if len(w) > 2 or w.isdigit()}


def parse(src):
    opts, cur = [], None
    for line in src.splitlines():
        m = re.match(r'^##\s+(.*)', line)
        if m:
            cur = {'name': m.group(1).strip()}
            opts.append(cur)
            continue
        m = re.match(r'^\s*(\w+)\s*:\s*(.*?)\s*(#.*)?$', line)
        if cur is not None and m:
            cur[m.group(1).lower()] = m.group(2).strip()
    return opts


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def score(o):
    hard, soft = [], []
    for f in FIELDS:
        if not o.get(f):
            hard.append(f'missing field: {f}')
    t = o.get('type', '').lower()
    if t and t not in TYPES:
        hard.append(f'unknown type "{t}" (use {", ".join(sorted(TYPES))})')
    voice, screen, f0 = o.get('voice', ''), o.get('screen', ''), o.get('frame0', '')
    vw, sw = len(voice.split()), len(screen.split())

    # Frame 0
    for rx, why in BAD_FRAME0:
        if re.search(rx, f0):
            hard.append(why)
    if f0 and not re.search(MOTION, f0):
        soft.append('frame0 names no motion or mid-action (is something already moving on frame 0?)')

    # Promise within 1.5 s
    p = num(o.get('promise_at'))
    if p is None and o.get('promise_at'):
        hard.append('promise_at is not a number of seconds')
    elif p is not None and p > 1.5:
        hard.append(f'promise lands at {p}s (must be ≤ 1.5 s)')

    # Lengths
    if sw > 8:
        hard.append(f'on-screen hook is {sw} words (max 8)')
    elif sw > 6:
        soft.append(f'on-screen hook is {sw} words (≤ 6 reads faster)')
    if vw > 12:
        hard.append(f'spoken hook is {vw} words (max 12, ~3.5 s)')

    # Reading time: 1.5 s + 0.3 s per word
    need = round(1.5 + 0.3 * sw, 1)
    h = num(o.get('hold'))
    if sw and h is not None and h < need:
        hard.append(f'screen text held {h}s, needs ≥ {need}s for {sw} words')

    # Voice and screen say the same thing (sound-off test)
    if voice and screen:
        sv, ss = stems(voice), stems(screen)
        overlap = len(sv & ss) / max(1, len(ss))
        if overlap < 0.5:
            hard.append(f'screen text and voice say different things ({round(overlap * 100)}% shared words)')

    # Wording
    for line, who in ((voice, 'voice'), (screen, 'screen')):
        if re.search(WEAK_OPENERS, line):
            hard.append(f'{who} opens with a greeting/intro/cliché')
        if re.search(AI_WORDS, line):
            soft.append(f'{who} uses stock AI/hype wording')
        if re.search(NOT_X_Y, line):
            hard.append(f'{who} uses "not X, but Y"')
        if '—' in line or ';' in line:
            soft.append(f'{who} has an em dash or semicolon')
        if re.search(BLANK, line):
            hard.append(f'{who} still has an unfilled blank {re.search(BLANK, line).group(0)}')
    if voice.strip().endswith('?') and re.search(GENERIC_Q, voice.strip()):
        hard.append('generic yes/no question (name the viewer\'s concrete situation instead)')
    if not re.search(NUM, voice + ' ' + screen, re.I) and not re.search(YOU, voice + ' ' + screen) \
            and not re.search(r'\b[A-Z][a-zà-ù]+\w*\b', (voice + ' ' + screen)[1:]):
        soft.append('no number, named thing or "you/tu": is it specific to the viewer?')
    if not re.search(GAIN, voice + ' ' + screen):
        soft.append('names no gain for the viewer (money, customers, sales, reach, views, fame)')
    if re.search(NUM, voice + screen) and not o.get('fact'):
        soft.append('has a number but no fact: line with its source')

    # Callback
    cb = o.get('callback', '')
    if cb and len(cb.split()) < 5:
        soft.append('callback is too thin: say how the ending answers frame 0')

    total = max(0, 100 - 20 * len(hard) - 5 * len(soft))
    return total, hard, soft, need


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: python -X utf8 score_hook.py hooks.md')
    opts = parse(open(sys.argv[1], encoding='utf-8').read())
    opts = [o for o in opts if re.match(r'(?i)option|opzione', o['name'])]
    ok_all = True
    for o in opts:
        total, hard, soft, need = score(o)
        ok = not hard and total >= 80
        ok_all &= ok
        print(f"{o['name']}  [{o.get('type', '?')}]  SCORE {total}/100  {'PASS' if ok else 'REWRITE'}")
        print(f"   voice : {o.get('voice', '')}")
        print(f"   screen: {o.get('screen', '')}  (needs ≥ {need}s on screen)")
        for x in hard:
            print('   HARD ', x)
        for x in soft:
            print('   soft ', x)
    types = [o.get('type', '').lower() for o in opts]
    if len(opts) != 3:
        ok_all = False
        print(f'SET: {len(opts)} options (need exactly 3)')
    if len(set(types)) != len(types):
        ok_all = False
        print(f'SET: repeated hook types {types} (the 3 options must be 3 different types)')
    if not set(types) & STOP:
        print('SET note: no stop-scroll hook (negation/number/question); consider swapping one in')
    if not set(types) & RETAIN:
        print('SET note: no retention hook (story/emotional/confession, see hooks-database.md); consider one')
    print('SET PASS: pick one' if ok_all else 'SET REWRITE')
    sys.exit(0 if ok_all else 1)


if __name__ == '__main__':
    main()
