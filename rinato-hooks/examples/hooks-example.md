# Hooks · example: a café's loyalty card reel
brief: café and bar owners · paper stamp cards get lost and regulars restart from zero · a loyalty card that lives in the phone
note: scene details (8 stamps, the bin) are story, not statistics

## Option A
type: interrupt
voice: Otto timbri. E la tessera è nel cestino: un cliente fedele perso.
screen: 8 timbri. Nel cestino.
frame0: A paper stamp card with 8 of 10 stamps already sliding off the counter into a bin
promise_at: 1.2
hold: 3.0
callback: Ending: the same 8 stamps reappear on a phone wallet card, the 10th lands, and the customer comes back
fact: scene, no statistic

## Option B
type: number
voice: Regala 2 timbri: quasi il doppio dei clienti arriva al premio.
screen: 2 timbri gratis. Il doppio al premio.
frame0: A 10-stamp card already sliding onto the counter with the first 2 stamps filled in red
promise_at: 1.3
hold: 3.6
callback: Ending: the same card reaches stamp 10 and the reward lights up
fact: Nunes & Drèze 2006, Journal of Consumer Research 32(4): 34% vs 19% of cards completed

## Option C
type: dont
voice: Non ristampare le tessere timbro: perdi i clienti più fedeli.
screen: Non ristampare le tessere.
frame0: A stack of freshly printed stamp cards already toppling off the counter toward the camera
promise_at: 1.0
hold: 3.0
callback: Ending: the print button greys out and a single QR card lands where the stack was
fact: none needed
